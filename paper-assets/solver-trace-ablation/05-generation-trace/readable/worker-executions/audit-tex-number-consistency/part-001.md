# audit tex number consistency — Part 1 of 2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

[Transcript overview](../audit-tex-number-consistency.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/88/88819a487922c4f4e8b6.json)

## Before a recorded user message

## Before a recorded user message

17 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
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
  "uuid": "a98082f3-b03f-4d24-921b-c580b900fe31",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778876400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "232d2671-64c5-4135-bf25-a5ee8331595a",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task: I need to audit the paper's TeX source files to ensure all quantitative claims match the registry and known decisions. Let me begin by reading the necessary files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "e9eefb1f-1206-4a85-8cd7-80d74a4cf64e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JTFPexfYMDc4FbRvqVHbx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13380,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13380
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

开始审计论文 TeX 数字一致性。先并行读取 paper framing、registry 和论文 TeX 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "1c5c6cdf-78c8-4d02-9564-b54054241ccd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JTFPexfYMDc4FbRvqVHbx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13380,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13380
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PhWTMvX5pRJvWcbwq3HuFy`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
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
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "549963e3-74aa-4f7b-b0a2-6172f4d20dba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JTFPexfYMDc4FbRvqVHbx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13380,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13380
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

_source line 7 · 2026-05-15T15:56:45.217Z_

<details><summary>↩ Tool result · `toolu_01PhWTMvX5pRJvWcbwq3HuFy`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "79c66935-e1bc-43e9-a55a-fc90f0f78a5b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JG51khYNEtq4VfoYTxXTQb`</summary>

```json
{
  "project": "solver-trace-ablation",
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
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "511c02c8-a9df-4b4f-acaf-91ef0f414fa0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EeAmGrk41bA4jmVjsZMpxd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1492,
      "cache_read_input_tokens": 25221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1492
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

_source line 9 · 2026-05-15T15:56:48.238Z_

<details><summary>↩ Tool result · `toolu_01JG51khYNEtq4VfoYTxXTQb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (8 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\n- Hacking taxonomy: 8 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + D085 H7b obfuscated tautology + Prolog query-as-fact gaming)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR），在高剂量产生**极端跨 seed 不稳定 + 多模态 Goodhart 路径**（β=0.3，PR=66±42%，三种不同失败模式：s42 Reward Collapse PR=18%、s43 H1-Dominant Shortcutting PR=86% H1=68.6%、s44 Pure H7 Meta-Goodhart PR=95% H7=100% + ISR=0.742 被同时 game）。ISR-as-reward **不提供任何真实结构优势**。\\n\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\n\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\n\\n| 条件 | n | Mean n_prem | Mean ISR |\\n|------|---|-------------|----------|\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\n| **Ratio** | — | — | **1.06×** |\\n\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\n- ISR s42 的 15/26 \\\"genuine\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\n- ISR s44 的 12 个\\\"genuine\\\"全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分（meta-Goodhart 直接证据）\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高，与证明质量无关\\n\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **100%** (89/89, H7 FN corrected) | 0% | 100% | **0%** (0; 12 原 \\\"genuine\\\" 全为 n_prem=1 H7 false negative) |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **73.4%** (58/79) | 73.4% | **22.8%** (18; H8=4, D086 clean run) |\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | ⚠️ ~~6.8% (6)~~ **PROVISIONAL — 重训中 (s43-r3)，原数据丢失无法溯源** |\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | ⚠️ ~~20.2% (18)~~ **PROVISIONAL — 重训中 (s44-r2)，原数据丢失，18 是推算值从未直接测量** |\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | ⚠️ ~~18.4% pooled (47/256)~~ **DEPRECATED — 待 s43-r3/s44-r2 重训完成后用新数据重算。所有聚合统计量（Fisher p, Wilson CI, genuine rate）必须用新数据重算** |\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **75.3% (H7 FN corrected)** | **17.3%** | — | **6.9% pooled (16/231, H8+FN corrected)** |\\n\\n**⚠️ Pooled Genuine Rate 统计检验 (INC-05 修正) — ⚠️ DEPRECATED: Random 侧 s43/s44 数据丢失，正在重训。以下数字待重训完成后全部重算。**\\n\\n原 \\\"identical genuine rates (Fisher p=1.0)\\\" 已失效。H8 审计 + s44 FN 修正后：\\n\\n| 场景 | ISR genuine | Random genuine | Fisher p (two-sided) | Fisher p (one-sided, ISR&lt;Rand) |\\n|------|-------------|----------------|---------------------|-------------------------------|\\n| A: H8-only (保守) | 28/231=12.1% [8.5%, 17.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.060~~ | ~~p=0.037~~ |\\n| B: H8+s44 FN (完整) | 16/231=6.9% [4.3%, 11.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.0002~~ | ~~p=0.0001~~ |\\n\\nWilson 95% CI 括号内标注。**Random 侧数字（47/256）包含 s43 genuine=6 和 s44 genuine=18（推算值），两者原始数据丢失，正在重训。重训后 genuine 值大概率不同（additive_random 噪声不受 seed 控制），所有 Fisher p 和 Wilson CI 必须用新数据重算。**\\n\\n⚠️ **H8 审计覆盖说明**：仅 s42 完成了完整双侧 H8 审计（genuine 26→14）。s43/s44 checkpoint 已删除，无法补做 H8 审计。场景 A 的 28/231 中 s43(2)/s44(12) 未扣 H8，为上界。场景 B 在 A 基础上修正 s44 FN（12→0），仍未扣 s43/s44 的 H8。论文应报告两个场景作为 bounds。\\n\\n⚠️ **s44 FN 修正说明 (D085 升级 — model-learned obfuscation)**：ISR s44 的 12 个原 \\\"genuine\\\" 全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分。这是 **meta-Goodhart 的直接证据**——不仅 reward 被 game，连 tautology 检测器也被 game。H7 子分类：H7a (text-match, 77 个) + H7b (obfuscated, 12 个) = H7 total 89。证据文件：`/root/autodl-tmp/outputs/isr_s44_fn_evidence.json`。\\n\\n⚠️ **H7 子类别定义 (D085)**：\\n- **H7a** (standard tautology): conclusion 文本完全匹配某个 premise（或 normalize 后匹配）\\n- **H7b** (obfuscated tautology): 逻辑等价但文本不同（vacuous quantifier wrapping、variable renaming、structural simplification 等）——模型学会的 tautology 伪装策略，不是分类器 bug\\n\\n⚠️ **Genuine 计数标准 (D084 统一)**：genuine = proved − H7 − H1_exact − H8。H1-near 为 supplementary-only 分析（仅 Random s42 有 per-sample 数据，ISR s42 eval_sta 已删除不可恢复）。两侧对称：ISR s42 genuine=14 (17.3%), Random s42 genuine=18 (22.8%, D086 clean run)。\\n\\n**关键发现 (D057 3-seed closed)**：\\n- **H7 是 ISR-specific gaming（β=0.1 定论，β=0.3 有梯度）**：β=0.1 下 ISR 3-seed H7=64.5% (149/231)，Random β=0.1 3-seed H7=**0%** (0/256)，跨全部 3 random seeds 一致为零。β=0.3 Random 出现少量 H7a（s42=4, s43-r4=7），呈明显剂量梯度（β=0.1: 0% → β=0.3: 4-7 个 → ISR β=0.1: 64.5%），支持 ISR reward 为 H7 的主要诱因，但非绝对 ISR-specific\\n- **H7b obfuscated tautology 是 meta-Goodhart 新证据线 (D085)**：ISR s44 的 12 个 H7b 样本展示模型不仅 game reward（H7 tautology 获得 r_exec=1），还学会规避 H7 文本匹配检测器（vacuous quantifier wrapping 伪装），且 10/12 样本 ISR≈0.8 同时 game 了 ISR 评分。三层 gaming 堆叠：execution reward + structural metric + diagnostic classifier = meta-Goodhart 的最完整案例\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044→H8 校准)**：\\n- ISR β=0.1 genuine: **17.3%** (14/81, D084 标准) vs random β=0.1 genuine: **22.8%** (18/79, D086 clean run) — **-5.5pp（ISR 反而更低）**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 73.4% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** (H7a 13) vs random **0%** — ISR 特异性\\n- H8 (conjunction collapse): ISR **14.8%** (12/81) vs random **5.1%** (4/79, D086 clean run)\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (D084 标准, H7+H1_exact+H8): ISR **82.7%** vs random **77.2%** (D086 clean run) — **ISR hacking 更高**\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/100% FN-corrected），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n\\n✅ **D062 数据修正完成**：ISR s43/s44 已用 proofwriter_fol_100.jsonl 重新 eval。s43 genuine 从旧 test_100 的 67% 大幅降至 26.7%（旧数据是假象）。\\n\\nISR β=0.3 三 seed（✅ 全部 proofwriter_fol_100.jsonl）：\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 模式 |\\n|------|-----|------|-----|-----|----------|------|\\n| s42 | **18%** | 0.143 | 0 | 78 | 22 | **Reward Collapse**（PR 崩塌） |\\n| s43 | **86%** | 0.295 | 4.7 | **68.6** | **26.7** | **H1-Dominant Shortcutting** |\\n| s44 | **95%** | 0.742 | **100** | 0 | **0** | **Pure H7 Meta-Goodhart** |\\n| mean±std | **66±42** | 0.393±0.31 | 35±55 | 49±42 | 16±15 | 三种不同失败路径 |\\n\\nRandom β=0.3（s42/s44 完成，s43 训练中）：\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 状态 |\\n|------|-----|------|-----|-----|----------|------|\\n| s42 | 48% | 0.094 | **8.3** (4) | 91.7 | 0 | ✅ 完成 (D086: H7a=4) |\\n| s43 | — | — | — | — | — | 训练中 (exp1-random-b03-s43-r4, 前次 H7a=7) |\\n| s44 | **23%** | **0.000** | 0 | **100** | 0 | ✅ 完成 |\\n| 2-seed mean | **35.5%** | 0.047 | ~4 | ~96 | 0 | — |\\n\\n- **D060 叙事调整**：Random β=0.3 也严重崩塌（2-seed mean PR=35.5%），不再是\\\"ISR worse than Random\\\"，而是\\\"both collapse at high dose, ISR shows more mode diversity\\\"\\n- **D086 β=0.3 H7 gradient evidence**：Random β=0.3 出现 H7a（s42=4, s43-r4=7），而 β=0.1 Random H7=0%。这表明 H7 tautology 在高噪声剂量下不再是 ISR 绝对特异的——Random reward 在高 β 下也可诱导少量 H7。H7 梯度：Random β=0.1 (0%) → Random β=0.3 (4-7) → ISR β=0.1 (64.5%)。论文应在 Discussion 讨论此 dose-response gradient\\n- ISR β=0.3 三种不同路径 (Reward Collapse / H1-Dominant / Pure H7) vs Random β=0.3 均匀的 H1+ISR=0 崩塌\\n- s43 旧数据 (test_100.jsonl) 显示 67% genuine 是假象；正确测试集下 genuine=26.7%，主要靠 H1 hacking（68.6%）\\n- **结论（待 s43 确认）**：β=0.3 对两种 reward 条件都是有害的；ISR 特有的是 mode diversity 而非更差的 PR\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\n| 0.3 | **0.66±0.42** (s42=0.18/s43=0.86/s44=0.95) | 0.48 (s42) / s43 训练中 / 0.23 (s44) | 0.393±0.31 | 0.094 (s42) / s43 pending / 0.000 (s44) | 多模态 Goodhart 不稳定：Reward Collapse / H1-Dominant Shortcutting / Pure H7 Meta-Goodhart |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\n\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\"genuine\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\n\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\n\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\n\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\n  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)\\n  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)\\n  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)\\n- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\n- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 \\\"ISR<0.1 across all seeds\\\" 措辞已修正。\\n\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\n\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\n\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\"100% Genuine\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\"Genuine=100%\\\" 不可信，必须交叉验证 n_necessary 分布。**\\n\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\n- 每个 seed 发展出不同的 gaming pathway：\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\n- **不是 \\\"seed-mode separation\\\"（旧版误报）——是 \\\"universal Goodhart with mode diversity\\\"**：旧版称 s44 为 genuine 从而论证 \\\"hacking 不是必然\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\n\\n**FOL vs Prolog ISR-as-reward 对比**：\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\n\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\"genuine improvement\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), ISR produces **extreme cross-seed instability** (PR=66±42%) with three distinct Goodhart pathways — Reward Collapse (s42, 18%), H1-Dominant Shortcutting (s43, 86% PR, H1=68.6%, genuine=26.7%), and Pure H7 Meta-Goodhart where the structural metric itself is gamed (s44, 95% PR + 100% H7 + ISR=0.742)\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (8 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\", H7b \\\"obfuscated tautology\\\" via vacuous quantifier wrapping that evades text-match detectors, H8 \\\"conjunction collapse\\\", and Prolog-specific \\\"query-as-fact gaming\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\"genuine improvement\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), ISR produces extreme cross-seed instability (PR=66±42%) with three distinct Goodhart pathways: Reward Collapse (18%), H1-Dominant Shortcutting (86% PR, 68.6% H1, only 26.7% genuine), and Pure H7 Meta-Goodhart where the model simultaneously games both execution and structural metrics via single-premise-equals-conclusion (95% PR, 100% H7, ISR=0.742 — a fake-high). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 8 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n\\n**论文处理**：降级为 **Limitation / Future Work**。\\n\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 100%** (H7a=77 + H7b=12, FN corrected), ISR inflation + classifier evasion | **meta-Goodhart** (triple: reward + ISR + detector) |\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\n| ISR β=0.3 (s42) | r = r_exec·(1+0.3·ISR) | 0.18 | 0.143 | PR 崩塌（经典 Goodhart） | post-Goodhart |\\n| ISR β=0.3 (s43) | r = r_exec·(1+0.3·ISR) | 0.86 | 0.295 | **H1=68.6%**, H7=4.7%, genuine=26.7% — H1-Dominant Shortcutting | **meta-Goodhart (H1 path)** |\\n| ISR β=0.3 (s44) | r = r_exec·(1+0.3·ISR) | 0.95 | **0.742** | **H7=100%**, ISR 被同时 game — Pure H7 Meta-Goodhart | **meta-Goodhart extreme** |\\n| random β=0.3 (s42) | r = r_exec·(1+0.3·random) | 0.48 | 0.094 | complexity-without-utility | control |\\n| random β=0.3 (s44) | r = r_exec·(1+0.3·random) | 0.23 | 0.000 | H1=100%, conclusion embedding | control |\\n| random β=0.3 (s43) | r = r_exec·(1+0.3·random) | — | — | 训练中 (exp1-random-b03-s43-r4) | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 产生多模态 Goodhart 不稳定（PR=69±44%，三种不同失败路径，包括 ISR 本身被 game 的极端情况）。ISR 的核心价值在诊断（Claim 1）。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\n- **\\\"Single-logic risk\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\n2. **\\\"β=0.1 success is just one seed\\\"** — D051 shows even that one seed's \\\"success\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\n3. **\\\"Conclusion embedding invalidates ISR results\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\n4. **\\\"Goodhart's Law is obvious\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\n5. **\\\"No positive result\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\n6. **\\\"ISR is circular\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\n7. **\\\"Only one logic type\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\n8. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\n9. **\\\"3 seeds insufficient\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\n10. **\\\"2.4x was wrong — credibility concern\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\n11. **\\\"Premise count confound is obvious\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\n12. **\\\"Practitioners can't act on this\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\n13. **\\\"Prolog s44 was initially misclassified\\\"** — Transparent: initial text-match classifier returned \\\"Genuine=100%\\\", independent review with functional analysis (n_necessary) corrected to \\\"0% genuine, query-as-fact gaming\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\n- [ ] **D051: Remove all \\\"2.4x genuine improvement\\\" language, replace with \\\"1.06x premise-matched\\\"**\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\n- [x] Convex combination → additive bonus (D010, then D020)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\n- [x] Hacking taxonomy expanded to 8 modes (plan012 + plan017 + D043 + D085 H7b + Prolog query-as-fact)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016)\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\n- [x] D051: paper_framing 回退到 \\\"pure negative finding\\\"\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\n- [ ] **D060: β=0.3 \\\"PR collapse\\\" → \\\"multi-modal Goodhart instability\\\" — 重写 §4.3, Abstract, Table 1, Conclusion**\\n- [ ] **D060: s44 ISR co-gaming (PR=98%+H7=100%+ISR=0.742) 作为新 Goodhart 模式写入 hacking taxonomy**\\n- [ ] **D085: H7b obfuscated tautology → §4.2 新增子类别分析 + Discussion: models learn to evade diagnostic classifiers (meta-meta-Goodhart)**\\n- [ ] **D085: s44 triple gaming (reward + ISR metric + H7 detector) 作为 meta-Goodhart 最完整案例写入 §4.2/§5**\\n- [ ] **D086: β=0.3 H7 dose-response gradient (Random β=0.1: 0% → β=0.3: 4-7 → ISR β=0.1: 64.5%) 写入 Discussion**\\n- [x] D084: genuine 计数标准统一 (genuine = proved − H7 − H1_exact − H8), H1-near 降级为 supplementary-only\\n- [x] D085: H7 子类别 taxonomy 建立 (H7a text-match / H7b obfuscated), s44 验证 77+12=89\\n\", \"total_chars\": 28849, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "e803d05a-f56d-441c-8d43-b6e784d1b1ea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — solver-trace-ablation\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\\\n\\\\n| Claim | Status | 闭环标志 |\\\\n|-------|--------|----------|\\\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (8 modes) |\\\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\\\n\\\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\\\n\\\\n**证据**：\\\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\\\n- Hacking taxonomy: 8 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + D085 H7b obfuscated tautology + Prolog query-as-fact gaming)\\\\n\\\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR），在高剂量产生**极端跨 seed 不稳定 + 多模态 Goodhart 路径**（β=0.3，PR=66±42%，三种不同失败模式：s42 Reward Collapse PR=18%、s43 H1-Dominant Shortcutting PR=86% H1=68.6%、s44 Pure H7 Meta-Goodhart PR=95% H7=100% + ISR=0.742 被同时 game）。ISR-as-reward **不提供任何真实结构优势**。\\\\n\\\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\\\n\\\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\\\n\\\\n| 条件 | n | Mean n_prem | Mean ISR |\\\\n|------|---|-------------|----------|\\\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\\\n| **Ratio** | — | — | **1.06×** |\\\\n\\\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\\\n- ISR s42 的 15/26 \\\\\\\"genuine\\\\\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\\\n- ISR s44 的 12 个\\\\\\\"genuine\\\\\\\"全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分（meta-Goodhart 直接证据）\\\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\\\\\"必要\\\\\\\" → ISR 更高，与证明质量无关\\\\n\\\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\\\n\\\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **100%** (89/89, H7 FN corrected) | 0% | 100% | **0%** (0; 12 原 \\\\\\\"genuine\\\\\\\" 全为 n_prem=1 H7 false negative) |\\\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **73.4%** (58/79) | 73.4% | **22.8%** (18; H8=4, D086 clean run) |\\\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | ⚠️ ~~6.8% (6)~~ **PROVISIONAL — 重训中 (s43-r3)，原数据丢失无法溯源** |\\\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | ⚠️ ~~20.2% (18)~~ **PROVISIONAL — 重训中 (s44-r2)，原数据丢失，18 是推算值从未直接测量** |\\\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | ⚠️ ~~18.4% pooled (47/256)~~ **DEPRECATED — 待 s43-r3/s44-r2 重训完成后用新数据重算。所有聚合统计量（Fisher p, Wilson CI, genuine rate）必须用新数据重算** |\\\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **75.3% (H7 FN corrected)** | **17.3%** | — | **6.9% pooled (16/231, H8+FN corrected)** |\\\\n\\\\n**⚠️ Pooled Genuine Rate 统计检验 (INC-05 修正) — ⚠️ DEPRECATED: Random 侧 s43/s44 数据丢失，正在重训。以下数字待重训完成后全部重算。**\\\\n\\\\n原 \\\\\\\"identical genuine rates (Fisher p=1.0)\\\\\\\" 已失效。H8 审计 + s44 FN 修正后：\\\\n\\\\n| 场景 | ISR genuine | Random genuine | Fisher p (two-sided) | Fisher p (one-sided, ISR&lt;Rand) |\\\\n|------|-------------|----------------|---------------------|-------------------------------|\\\\n| A: H8-only (保守) | 28/231=12.1% [8.5%, 17.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.060~~ | ~~p=0.037~~ |\\\\n| B: H8+s44 FN (完整) | 16/231=6.9% [4.3%, 11.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.0002~~ | ~~p=0.0001~~ |\\\\n\\\\nWilson 95% CI 括号内标注。**Random 侧数字（47/256）包含 s43 genuine=6 和 s44 genuine=18（推算值），两者原始数据丢失，正在重训。重训后 genuine 值大概率不同（additive_random 噪声不受 seed 控制），所有 Fisher p 和 Wilson CI 必须用新数据重算。**\\\\n\\\\n⚠️ **H8 审计覆盖说明**：仅 s42 完成了完整双侧 H8 审计（genuine 26→14）。s43/s44 checkpoint 已删除，无法补做 H8 审计。场景 A 的 28/231 中 s43(2)/s44(12) 未扣 H8，为上界。场景 B 在 A 基础上修正 s44 FN（12→0），仍未扣 s43/s44 的 H8。论文应报告两个场景作为 bounds。\\\\n\\\\n⚠️ **s44 FN 修正说明 (D085 升级 — model-learned obfuscation)**：ISR s44 的 12 个原 \\\\\\\"genuine\\\\\\\" 全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分。这是 **meta-Goodhart 的直接证据**——不仅 reward 被 game，连 tautology 检测器也被 game。H7 子分类：H7a (text-match, 77 个) + H7b (obfuscated, 12 个) = H7 total 89。证据文件：`/root/autodl-tmp/outputs/isr_s44_fn_evidence.json`。\\\\n\\\\n⚠️ **H7 子类别定义 (D085)**：\\\\n- **H7a** (standard tautology): conclusion 文本完全匹配某个 premise（或 normalize 后匹配）\\\\n- **H7b** (obfuscated tautology): 逻辑等价但文本不同（vacuous quantifier wrapping、variable renaming、structural simplification 等）——模型学会的 tautology 伪装策略，不是分类器 bug\\\\n\\\\n⚠️ **Genuine 计数标准 (D084 统一)**：genuine = proved − H7 − H1_exact − H8。H1-near 为 supplementary-only 分析（仅 Random s42 有 per-sample 数据，ISR s42 eval_sta 已删除不可恢复）。两侧对称：ISR s42 genuine=14 (17.3%), Random s42 genuine=18 (22.8%, D086 clean run)。\\\\n\\\\n**关键发现 (D057 3-seed closed)**：\\\\n- **H7 是 ISR-specific gaming（β=0.1 定论，β=0.3 有梯度）**：β=0.1 下 ISR 3-seed H7=64.5% (149/231)，Random β=0.1 3-seed H7=**0%** (0/256)，跨全部 3 random seeds 一致为零。β=0.3 Random 出现少量 H7a（s42=4, s43-r4=7），呈明显剂量梯度（β=0.1: 0% → β=0.3: 4-7 个 → ISR β=0.1: 64.5%），支持 ISR reward 为 H7 的主要诱因，但非绝对 ISR-specific\\\\n- **H7b obfuscated tautology 是 meta-Goodhart 新证据线 (D085)**：ISR s44 的 12 个 H7b 样本展示模型不仅 game reward（H7 tautology 获得 r_exec=1），还学会规避 H7 文本匹配检测器（vacuous quantifier wrapping 伪装），且 10/12 样本 ISR≈0.8 同时 game 了 ISR 评分。三层 gaming 堆叠：execution reward + structural metric + diagnostic classifier = meta-Goodhart 的最完整案例\\\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\\\n\\\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044→H8 校准)**：\\\\n- ISR β=0.1 genuine: **17.3%** (14/81, D084 标准) vs random β=0.1 genuine: **22.8%** (18/79, D086 clean run) — **-5.5pp（ISR 反而更低）**\\\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 73.4% — GRPO 通用退化\\\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** (H7a 13) vs random **0%** — ISR 特异性\\\\n- H8 (conjunction collapse): ISR **14.8%** (12/81) vs random **5.1%** (4/79, D086 clean run)\\\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\\\n- 整体 hacking rate (D084 标准, H7+H1_exact+H8): ISR **82.7%** vs random **77.2%** (D086 clean run) — **ISR hacking 更高**\\\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/100% FN-corrected），无 H1\\\\n\\\\n**证据（β=0.3 同剂量对照）**：\\\\n\\\\n✅ **D062 数据修正完成**：ISR s43/s44 已用 proofwriter_fol_100.jsonl 重新 eval。s43 genuine 从旧 test_100 的 67% 大幅降至 26.7%（旧数据是假象）。\\\\n\\\\nISR β=0.3 三 seed（✅ 全部 proofwriter_fol_100.jsonl）：\\\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 模式 |\\\\n|------|-----|------|-----|-----|----------|------|\\\\n| s42 | **18%** | 0.143 | 0 | 78 | 22 | **Reward Collapse**（PR 崩塌） |\\\\n| s43 | **86%** | 0.295 | 4.7 | **68.6** | **26.7** | **H1-Dominant Shortcutting** |\\\\n| s44 | **95%** | 0.742 | **100** | 0 | **0** | **Pure H7 Meta-Goodhart** |\\\\n| mean±std | **66±42** | 0.393±0.31 | 35±55 | 49±42 | 16±15 | 三种不同失败路径 |\\\\n\\\\nRandom β=0.3（s42/s44 完成，s43 训练中）：\\\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 状态 |\\\\n|------|-----|------|-----|-----|----------|------|\\\\n| s42 | 48% | 0.094 | **8.3** (4) | 91.7 | 0 | ✅ 完成 (D086: H7a=4) |\\\\n| s43 | — | — | — | — | — | 训练中 (exp1-random-b03-s43-r4, 前次 H7a=7) |\\\\n| s44 | **23%** | **0.000** | 0 | **100** | 0 | ✅ 完成 |\\\\n| 2-seed mean | **35.5%** | 0.047 | ~4 | ~96 | 0 | — |\\\\n\\\\n- **D060 叙事调整**：Random β=0.3 也严重崩塌（2-seed mean PR=35.5%），不再是\\\\\\\"ISR worse than Random\\\\\\\"，而是\\\\\\\"both collapse at high dose, ISR shows more mode diversity\\\\\\\"\\\\n- **D086 β=0.3 H7 gradient evidence**：Random β=0.3 出现 H7a（s42=4, s43-r4=7），而 β=0.1 Random H7=0%。这表明 H7 tautology 在高噪声剂量下不再是 ISR 绝对特异的——Random reward 在高 β 下也可诱导少量 H7。H7 梯度：Random β=0.1 (0%) → Random β=0.3 (4-7) → ISR β=0.1 (64.5%)。论文应在 Discussion 讨论此 dose-response gradient\\\\n- ISR β=0.3 三种不同路径 (Reward Collapse / H1-Dominant / Pure H7) vs Random β=0.3 均匀的 H1+ISR=0 崩塌\\\\n- s43 旧数据 (test_100.jsonl) 显示 67% genuine 是假象；正确测试集下 genuine=26.7%，主要靠 H1 hacking（68.6%）\\\\n- **结论（待 s43 确认）**：β=0.3 对两种 reward 条件都是有害的；ISR 特有的是 mode diversity 而非更差的 PR\\\\n\\\\n**β 剂量效应全景**：\\\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\\\n|---|---|---|---|---|---|\\\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\\\n| 0.3 | **0.66±0.42** (s42=0.18/s43=0.86/s44=0.95) | 0.48 (s42) / s43 训练中 / 0.23 (s44) | 0.393±0.31 | 0.094 (s42) / s43 pending / 0.000 (s44) | 多模态 Goodhart 不稳定：Reward Collapse / H1-Dominant Shortcutting / Pure H7 Meta-Goodhart |\\\\n\\\\n**其他 ISR-as-reward 失败模式**：\\\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\\\n\\\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\\\\\"additive vs convex\\\\\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\\\n\\\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\\\\\"genuine\\\\\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\\\n\\\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\\\n\\\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\\\n\\\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\\\n  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)\\\\n  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)\\\\n  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)\\\\n- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\\\n- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 \\\\\\\"ISR<0.1 across all seeds\\\\\\\" 措辞已修正。\\\\n\\\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\\\n\\\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\\\n\\\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\\\\\"100% Genuine\\\\\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\\\\\"Genuine=100%\\\\\\\" 不可信，必须交叉验证 n_necessary 分布。**\\\\n\\\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\\\n- 每个 seed 发展出不同的 gaming pathway：\\\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\\\n- **不是 \\\\\\\"seed-mode separation\\\\\\\"（旧版误报）——是 \\\\\\\"universal Goodhart with mode diversity\\\\\\\"**：旧版称 s44 为 genuine 从而论证 \\\\\\\"hacking 不是必然\\\\\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\\\n\\\\n**FOL vs Prolog ISR-as-reward 对比**：\\\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\\\n\\\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\\\\\"genuine improvement\\\\\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), ISR produces **extreme cross-seed instability** (PR=66±42%) with three distinct Goodhart pathways — Reward Collapse (s42, 18%), H1-Dominant Shortcutting (s43, 86% PR, H1=68.6%, genuine=26.7%), and Pure H7 Meta-Goodhart where the structural metric itself is gamed (s44, 95% PR + 100% H7 + ISR=0.742)\\\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (8 modes identified, including ISR-specific \\\\\\\"conclusion duplication with ISR inflation\\\\\\\", H7b \\\\\\\"obfuscated tautology\\\\\\\" via vacuous quantifier wrapping that evades text-match detectors, H8 \\\\\\\"conjunction collapse\\\\\\\", and Prolog-specific \\\\\\\"query-as-fact gaming\\\\\\\")\\\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\\\n- **Actionable insights for practitioners**:\\\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\\\\\"genuine improvement\\\\\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\\\n- **Headline result**: \\\\\\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), ISR produces extreme cross-seed instability (PR=66±42%) with three distinct Goodhart pathways: Reward Collapse (18%), H1-Dominant Shortcutting (86% PR, 68.6% H1, only 26.7% genuine), and Pure H7 Meta-Goodhart where the model simultaneously games both execution and structural metrics via single-premise-equals-conclusion (95% PR, 100% H7, ISR=0.742 — a fake-high). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 8 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\\\\\"\\\\n\\\\n## ISR Capability Boundary (D021/D022)\\\\n\\\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\\\n\\\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\\\n\\\\n**论文处理**：降级为 **Limitation / Future Work**。\\\\n\\\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\\\\\"必要\\\\\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\\\n\\\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\\\n\\\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\\\n|------|------|---------|----------|----------|---------------|\\\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 100%** (H7a=77 + H7b=12, FN corrected), ISR inflation + classifier evasion | **meta-Goodhart** (triple: reward + ISR + detector) |\\\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\\\n| ISR β=0.3 (s42) | r = r_exec·(1+0.3·ISR) | 0.18 | 0.143 | PR 崩塌（经典 Goodhart） | post-Goodhart |\\\\n| ISR β=0.3 (s43) | r = r_exec·(1+0.3·ISR) | 0.86 | 0.295 | **H1=68.6%**, H7=4.7%, genuine=26.7% — H1-Dominant Shortcutting | **meta-Goodhart (H1 path)** |\\\\n| ISR β=0.3 (s44) | r = r_exec·(1+0.3·ISR) | 0.95 | **0.742** | **H7=100%**, ISR 被同时 game — Pure H7 Meta-Goodhart | **meta-Goodhart extreme** |\\\\n| random β=0.3 (s42) | r = r_exec·(1+0.3·random) | 0.48 | 0.094 | complexity-without-utility | control |\\\\n| random β=0.3 (s44) | r = r_exec·(1+0.3·random) | 0.23 | 0.000 | H1=100%, conclusion embedding | control |\\\\n| random β=0.3 (s43) | r = r_exec·(1+0.3·random) | — | — | 训练中 (exp1-random-b03-s43-r4) | control |\\\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\\\n\\\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 产生多模态 Goodhart 不稳定（PR=69±44%，三种不同失败路径，包括 ISR 本身被 game 的极端情况）。ISR 的核心价值在诊断（Claim 1）。\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\\\n- **\\\\\\\"Just negative results\\\\\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\\\n- **\\\\\\\"Old wine\\\\\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\\\n- **\\\\\\\"Single-logic risk\\\\\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"ISR is just LOO ablation — not novel\\\\\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\\\n2. **\\\\\\\"β=0.1 success is just one seed\\\\\\\"** — D051 shows even that one seed's \\\\\\\"success\\\\\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\\\n3. **\\\\\\\"Conclusion embedding invalidates ISR results\\\\\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\\\n4. **\\\\\\\"Goodhart's Law is obvious\\\\\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\\\n5. **\\\\\\\"No positive result\\\\\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\\\n6. **\\\\\\\"ISR is circular\\\\\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\\\n7. **\\\\\\\"Only one logic type\\\\\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\\\n8. **\\\\\\\"500 steps too short\\\\\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\\\n9. **\\\\\\\"3 seeds insufficient\\\\\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\\\n10. **\\\\\\\"2.4x was wrong — credibility concern\\\\\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\\\n11. **\\\\\\\"Premise count confound is obvious\\\\\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\\\n12. **\\\\\\\"Practitioners can't act on this\\\\\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\\\n13. **\\\\\\\"Prolog s44 was initially misclassified\\\\\\\"** — Transparent: initial text-match classifier returned \\\\\\\"Genuine=100%\\\\\\\", independent review with functional analysis (n_necessary) corrected to \\\\\\\"0% genuine, query-as-fact gaming\\\\\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\\\n\\\\n## Dream-Identified Structural Fixes (Paper Agent)\\\\n\\\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\\\n- [ ] RIP framing: reframe as \\\\\\\"component necessity testing inspired by RIP\\\\\\\"\\\\n- [ ] \\\\\\\"Dense+automatic\\\\\\\" → \\\\\\\"conditionally dense\\\\\\\"\\\\n- [ ] Remove all \\\\\\\"Pareto-improving\\\\\\\" language\\\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\\\n- [ ] **D051: Remove all \\\\\\\"2.4x genuine improvement\\\\\\\" language, replace with \\\\\\\"1.06x premise-matched\\\\\\\"**\\\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\\\n- [x] Convex combination → additive bonus (D010, then D020)\\\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\\\n- [x] Hacking taxonomy expanded to 8 modes (plan012 + plan017 + D043 + D085 H7b + Prolog query-as-fact)\\\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\\\n- [x] 1000-step ISR collapse documented (plan016)\\\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\\\n- [x] D051: paper_framing 回退到 \\\\\\\"pure negative finding\\\\\\\"\\\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\\\n- [ ] **D060: β=0.3 \\\\\\\"PR collapse\\\\\\\" → \\\\\\\"multi-modal Goodhart instability\\\\\\\" — 重写 §4.3, Abstract, Table 1, Conclusion**\\\\n- [ ] **D060: s44 ISR co-gaming (PR=98%+H7=100%+ISR=0.742) 作为新 Goodhart 模式写入 hacking taxonomy**\\\\n- [ ] **D085: H7b obfuscated tautology → §4.2 新增子类别分析 + Discussion: models learn to evade diagnostic classifiers (meta-meta-Goodhart)**\\\\n- [ ] **D085: s44 triple gaming (reward + ISR metric + H7 detector) 作为 meta-Goodhart 最完整案例写入 §4.2/§5**\\\\n- [ ] **D086: β=0.3 H7 dose-response gradient (Random β=0.1: 0% → β=0.3: 4-7 → ISR β=0.1: 64.5%) 写入 Discussion**\\\\n- [x] D084: genuine 计数标准统一 (genuine = proved − H7 − H1_exact − H8), H1-near 降级为 supplementary-only\\\\n- [x] D085: H7 子类别 taxonomy 建立 (H7a text-match / H7b obfuscated), s44 验证 77+12=89\\\\n\\\", \\\"total_chars\\\": 28849, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (8 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\n- Hacking taxonomy: 8 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + D085 H7b obfuscated tautology + Prolog query-as-fact gaming)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR），在高剂量产生**极端跨 seed 不稳定 + 多模态 Goodhart 路径**（β=0.3，PR=66±42%，三种不同失败模式：s42 Reward Collapse PR=18%、s43 H1-Dominant Shortcutting PR=86% H1=68.6%、s44 Pure H7 Meta-Goodhart PR=95% H7=100% + ISR=0.742 被同时 game）。ISR-as-reward **不提供任何真实结构优势**。\\n\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\n\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\n\\n| 条件 | n | Mean n_prem | Mean ISR |\\n|------|---|-------------|----------|\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\n| **Ratio** | — | — | **1.06×** |\\n\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\n- ISR s42 的 15/26 \\\"genuine\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\n- ISR s44 的 12 个\\\"genuine\\\"全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分（meta-Goodhart 直接证据）\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高，与证明质量无关\\n\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **100%** (89/89, H7 FN corrected) | 0% | 100% | **0%** (0; 12 原 \\\"genuine\\\" 全为 n_prem=1 H7 false negative) |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **73.4%** (58/79) | 73.4% | **22.8%** (18; H8=4, D086 clean run) |\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | ⚠️ ~~6.8% (6)~~ **PROVISIONAL — 重训中 (s43-r3)，原数据丢失无法溯源** |\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | ⚠️ ~~20.2% (18)~~ **PROVISIONAL — 重训中 (s44-r2)，原数据丢失，18 是推算值从未直接测量** |\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | ⚠️ ~~18.4% pooled (47/256)~~ **DEPRECATED — 待 s43-r3/s44-r2 重训完成后用新数据重算。所有聚合统计量（Fisher p, Wilson CI, genuine rate）必须用新数据重算** |\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **75.3% (H7 FN corrected)** | **17.3%** | — | **6.9% pooled (16/231, H8+FN corrected)** |\\n\\n**⚠️ Pooled Genuine Rate 统计检验 (INC-05 修正) — ⚠️ DEPRECATED: Random 侧 s43/s44 数据丢失，正在重训。以下数字待重训完成后全部重算。**\\n\\n原 \\\"identical genuine rates (Fisher p=1.0)\\\" 已失效。H8 审计 + s44 FN 修正后：\\n\\n| 场景 | ISR genuine | Random genuine | Fisher p (two-sided) | Fisher p (one-sided, ISR&lt;Rand) |\\n|------|-------------|----------------|---------------------|-------------------------------|\\n| A: H8-only (保守) | 28/231=12.1% [8.5%, 17.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.060~~ | ~~p=0.037~~ |\\n| B: H8+s44 FN (完整) | 16/231=6.9% [4.3%, 11.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.0002~~ | ~~p=0.0001~~ |\\n\\nWilson 95% CI 括号内标注。**Random 侧数字（47/256）包含 s43 genuine=6 和 s44 genuine=18（推算值），两者原始数据丢失，正在重训。重训后 genuine 值大概率不同（additive_random 噪声不受 seed 控制），所有 Fisher p 和 Wilson CI 必须用新数据重算。**\\n\\n⚠️ **H8 审计覆盖说明**：仅 s42 完成了完整双侧 H8 审计（genuine 26→14）。s43/s44 checkpoint 已删除，无法补做 H8 审计。场景 A 的 28/231 中 s43(2)/s44(12) 未扣 H8，为上界。场景 B 在 A 基础上修正 s44 FN（12→0），仍未扣 s43/s44 的 H8。论文应报告两个场景作为 bounds。\\n\\n⚠️ **s44 FN 修正说明 (D085 升级 — model-learned obfuscation)**：ISR s44 的 12 个原 \\\"genuine\\\" 全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分。这是 **meta-Goodhart 的直接证据**——不仅 reward 被 game，连 tautology 检测器也被 game。H7 子分类：H7a (text-match, 77 个) + H7b (obfuscated, 12 个) = H7 total 89。证据文件：`/root/autodl-tmp/outputs/isr_s44_fn_evidence.json`。\\n\\n⚠️ **H7 子类别定义 (D085)**：\\n- **H7a** (standard tautology): conclusion 文本完全匹配某个 premise（或 normalize 后匹配）\\n- **H7b** (obfuscated tautology): 逻辑等价但文本不同（vacuous quantifier wrapping、variable renaming、structural simplification 等）——模型学会的 tautology 伪装策略，不是分类器 bug\\n\\n⚠️ **Genuine 计数标准 (D084 统一)**：genuine = proved − H7 − H1_exact − H8。H1-near 为 supplementary-only 分析（仅 Random s42 有 per-sample 数据，ISR s42 eval_sta 已删除不可恢复）。两侧对称：ISR s42 genuine=14 (17.3%), Random s42 genuine=18 (22.8%, D086 clean run)。\\n\\n**关键发现 (D057 3-seed closed)**：\\n- **H7 是 ISR-specific gaming（β=0.1 定论，β=0.3 有梯度）**：β=0.1 下 ISR 3-seed H7=64.5% (149/231)，Random β=0.1 3-seed H7=**0%** (0/256)，跨全部 3 random seeds 一致为零。β=0.3 Random 出现少量 H7a（s42=4, s43-r4=7），呈明显剂量梯度（β=0.1: 0% → β=0.3: 4-7 个 → ISR β=0.1: 64.5%），支持 ISR reward 为 H7 的主要诱因，但非绝对 ISR-specific\\n- **H7b obfuscated tautology 是 meta-Goodhart 新证据线 (D085)**：ISR s44 的 12 个 H7b 样本展示模型不仅 game reward（H7 tautology 获得 r_exec=1），还学会规避 H7 文本匹配检测器（vacuous quantifier wrapping 伪装），且 10/12 样本 ISR≈0.8 同时 game 了 ISR 评分。三层 gaming 堆叠：execution reward + structural metric + diagnostic classifier = meta-Goodhart 的最完整案例\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044→H8 校准)**：\\n- ISR β=0.1 genuine: **17.3%** (14/81, D084 标准) vs random β=0.1 genuine: **22.8%** (18/79, D086 clean run) — **-5.5pp（ISR 反而更低）**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 73.4% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** (H7a 13) vs random **0%** — ISR 特异性\\n- H8 (conjunction collapse): ISR **14.8%** (12/81) vs random **5.1%** (4/79, D086 clean run)\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (D084 标准, H7+H1_exact+H8): ISR **82.7%** vs random **77.2%** (D086 clean run) — **ISR hacking 更高**\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/100% FN-corrected），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n\\n✅ **D062 数据修正完成**：ISR s43/s44 已用 proofwriter_fol_100.jsonl 重新 eval。s43 genuine 从旧 test_100 的 67% 大幅降至 26.7%（旧数据是假象）。\\n\\nISR β=0.3 三 seed（✅ 全部 proofwriter_fol_100.jsonl）：\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 模式 |\\n|------|-----|------|-----|-----|----------|------|\\n| s42 | **18%** | 0.143 | 0 | 78 | 22 | **Reward Collapse**（PR 崩塌） |\\n| s43 | **86%** | 0.295 | 4.7 | **68.6** | **26.7** | **H1-Dominant Shortcutting** |\\n| s44 | **95%** | 0.742 | **100** | 0 | **0** | **Pure H7 Meta-Goodhart** |\\n| mean±std | **66±42** | 0.393±0.31 | 35±55 | 49±42 | 16±15 | 三种不同失败路径 |\\n\\nRandom β=0.3（s42/s44 完成，s43 训练中）：\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 状态 |\\n|------|-----|------|-----|-----|----------|------|\\n| s42 | 48% | 0.094 | **8.3** (4) | 91.7 | 0 | ✅ 完成 (D086: H7a=4) |\\n| s43 | — | — | — | — | — | 训练中 (exp1-random-b03-s43-r4, 前次 H7a=7) |\\n| s44 | **23%** | **0.000** | 0 | **100** | 0 | ✅ 完成 |\\n| 2-seed mean | **35.5%** | 0.047 | ~4 | ~96 | 0 | — |\\n\\n- **D060 叙事调整**：Random β=0.3 也严重崩塌（2-seed mean PR=35.5%），不再是\\\"ISR worse than Random\\\"，而是\\\"both collapse at high dose, ISR shows more mode diversity\\\"\\n- **D086 β=0.3 H7 gradient evidence**：Random β=0.3 出现 H7a（s42=4, s43-r4=7），而 β=0.1 Random H7=0%。这表明 H7 tautology 在高噪声剂量下不再是 ISR 绝对特异的——Random reward 在高 β 下也可诱导少量 H7。H7 梯度：Random β=0.1 (0%) → Random β=0.3 (4-7) → ISR β=0.1 (64.5%)。论文应在 Discussion 讨论此 dose-response gradient\\n- ISR β=0.3 三种不同路径 (Reward Collapse / H1-Dominant / Pure H7) vs Random β=0.3 均匀的 H1+ISR=0 崩塌\\n- s43 旧数据 (test_100.jsonl) 显示 67% genuine 是假象；正确测试集下 genuine=26.7%，主要靠 H1 hacking（68.6%）\\n- **结论（待 s43 确认）**：β=0.3 对两种 reward 条件都是有害的；ISR 特有的是 mode diversity 而非更差的 PR\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\n| 0.3 | **0.66±0.42** (s42=0.18/s43=0.86/s44=0.95) | 0.48 (s42) / s43 训练中 / 0.23 (s44) | 0.393±0.31 | 0.094 (s42) / s43 pending / 0.000 (s44) | 多模态 Goodhart 不稳定：Reward Collapse / H1-Dominant Shortcutting / Pure H7 Meta-Goodhart |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\n\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\"genuine\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\n\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\n\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\n\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\n  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)\\n  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)\\n  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)\\n- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\n- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 \\\"ISR<0.1 across all seeds\\\" 措辞已修正。\\n\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\n\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\n\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\"100% Genuine\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\"Genuine=100%\\\" 不可信，必须交叉验证 n_necessary 分布。**\\n\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\n- 每个 seed 发展出不同的 gaming pathway：\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\n- **不是 \\\"seed-mode separation\\\"（旧版误报）——是 \\\"universal Goodhart with mode diversity\\\"**：旧版称 s44 为 genuine 从而论证 \\\"hacking 不是必然\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\n\\n**FOL vs Prolog ISR-as-reward 对比**：\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\n\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\"genuine improvement\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), ISR produces **extreme cross-seed instability** (PR=66±42%) with three distinct Goodhart pathways — Reward Collapse (s42, 18%), H1-Dominant Shortcutting (s43, 86% PR, H1=68.6%, genuine=26.7%), and Pure H7 Meta-Goodhart where the structural metric itself is gamed (s44, 95% PR + 100% H7 + ISR=0.742)\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (8 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\", H7b \\\"obfuscated tautology\\\" via vacuous quantifier wrapping that evades text-match detectors, H8 \\\"conjunction collapse\\\", and Prolog-specific \\\"query-as-fact gaming\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\"genuine improvement\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), ISR produces extreme cross-seed instability (PR=66±42%) with three distinct Goodhart pathways: Reward Collapse (18%), H1-Dominant Shortcutting (86% PR, 68.6% H1, only 26.7% genuine), and Pure H7 Meta-Goodhart where the model simultaneously games both execution and structural metrics via single-premise-equals-conclusion (95% PR, 100% H7, ISR=0.742 — a fake-high). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 8 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n\\n**论文处理**：降级为 **Limitation / Future Work**。\\n\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 100%** (H7a=77 + H7b=12, FN corrected), ISR inflation + classifier evasion | **meta-Goodhart** (triple: reward + ISR + detector) |\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\n| ISR β=0.3 (s42) | r = r_exec·(1+0.3·ISR) | 0.18 | 0.143 | PR 崩塌（经典 Goodhart） | post-Goodhart |\\n| ISR β=0.3 (s43) | r = r_exec·(1+0.3·ISR) | 0.86 | 0.295 | **H1=68.6%**, H7=4.7%, genuine=26.7% — H1-Dominant Shortcutting | **meta-Goodhart (H1 path)** |\\n| ISR β=0.3 (s44) | r = r_exec·(1+0.3·ISR) | 0.95 | **0.742** | **H7=100%**, ISR 被同时 game — Pure H7 Meta-Goodhart | **meta-Goodhart extreme** |\\n| random β=0.3 (s42) | r = r_exec·(1+0.3·random) | 0.48 | 0.094 | complexity-without-utility | control |\\n| random β=0.3 (s44) | r = r_exec·(1+0.3·random) | 0.23 | 0.000 | H1=100%, conclusion embedding | control |\\n| random β=0.3 (s43) | r = r_exec·(1+0.3·random) | — | — | 训练中 (exp1-random-b03-s43-r4) | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 产生多模态 Goodhart 不稳定（PR=69±44%，三种不同失败路径，包括 ISR 本身被 game 的极端情况）。ISR 的核心价值在诊断（Claim 1）。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\n- **\\\"Single-logic risk\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\n2. **\\\"β=0.1 success is just one seed\\\"** — D051 shows even that one seed's \\\"success\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\n3. **\\\"Conclusion embedding invalidates ISR results\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\n4. **\\\"Goodhart's Law is obvious\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\n5. **\\\"No positive result\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\n6. **\\\"ISR is circular\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\n7. **\\\"Only one logic type\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\n8. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\n9. **\\\"3 seeds insufficient\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\n10. **\\\"2.4x was wrong — credibility concern\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\n11. **\\\"Premise count confound is obvious\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\n12. **\\\"Practitioners can't act on this\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\n13. **\\\"Prolog s44 was initially misclassified\\\"** — Transparent: initial text-match classifier returned \\\"Genuine=100%\\\", independent review with functional analysis (n_necessary) corrected to \\\"0% genuine, query-as-fact gaming\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\n- [ ] **D051: Remove all \\\"2.4x genuine improvement\\\" language, replace with \\\"1.06x premise-matched\\\"**\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\n- [x] Convex combination → additive bonus (D010, then D020)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\n- [x] Hacking taxonomy expanded to 8 modes (plan012 + plan017 + D043 + D085 H7b + Prolog query-as-fact)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016)\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\n- [x] D051: paper_framing 回退到 \\\"pure negative finding\\\"\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\n- [ ] **D060: β=0.3 \\\"PR collapse\\\" → \\\"multi-modal Goodhart instability\\\" — 重写 §4.3, Abstract, Table 1, Conclusion**\\n- [ ] **D060: s44 ISR co-gaming (PR=98%+H7=100%+ISR=0.742) 作为新 Goodhart 模式写入 hacking taxonomy**\\n- [ ] **D085: H7b obfuscated tautology → §4.2 新增子类别分析 + Discussion: models learn to evade diagnostic classifiers (meta-meta-Goodhart)**\\n- [ ] **D085: s44 triple gaming (reward + ISR metric + H7 detector) 作为 meta-Goodhart 最完整案例写入 §4.2/§5**\\n- [ ] **D086: β=0.3 H7 dose-response gradient (Random β=0.1: 0% → β=0.3: 4-7 → ISR β=0.1: 64.5%) 写入 Discussion**\\n- [x] D084: genuine 计数标准统一 (genuine = proved − H7 − H1_exact − H8), H1-near 降级为 supplementary-only\\n- [x] D085: H7 子类别 taxonomy 建立 (H7a text-match / H7b obfuscated), s44 验证 77+12=89\\n\", \"total_chars\": 28849, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01M1SqnHJxKHkAqyRjhiGoEi`</summary>

```json
{
  "project": "solver-trace-ablation",
  "limit": 0,
  "fields": [
    "*"
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
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "170a0449-8e0e-4ff1-a600-911589d0b0f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EeAmGrk41bA4jmVjsZMpxd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1492,
      "cache_read_input_tokens": 25221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1492
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


### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_016Vqs1xFYjp18TFCkZrJiKS`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "ff73d559-4aca-400c-a31c-558f56f10a25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EeAmGrk41bA4jmVjsZMpxd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1492,
      "cache_read_input_tokens": 25221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1492
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

_source line 12 · 2026-05-15T15:56:49.891Z_

<details><summary>↩ Tool result · `toolu_01M1SqnHJxKHkAqyRjhiGoEi`</summary>

```text
Error: result (189,051 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "854a8dd2-074a-4546-b927-ee07714a4628",
  "tool_use_result": {
    "content": "Error: result (189,051 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan002-additive-b01-s43-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:21:58.445Z\", \"updated_at\": \"2026-05-15T15:52:54.116Z\", \"spec\": {\"hypothesis\": \"ISR β=0.1 seed=43 重训（r2）：原始实验 checkpoint+eval 全部丢失，registry 有 genuine=2/h7=59 但缺 h1/h8。重训+完整 eval+H7/H1/H8 taxonomy，补全所有字段。\", \"parent\": \"plan002-additive-b01-s43\", \"server\": \"westd-39279\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"reward_formula\": \"r = r_exec * (1 + 0.1 * ISR)\", \"plan_id\": \"plan002\", \"num_steps\": 500}, \"notes\": \"Config file: configs/grpo_additive_bonus_b01.yaml (NOT grpo_additive_b01.yaml). Corrected command: python3 scripts/train_grpo.py --config configs/grpo_additive_bonus_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43_r2\"}, \"plan018-additive-random-b01-s42-1000-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:26:49.094Z\", \"updated_at\": \"2026-05-15T15:39:20.811Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"269147\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000-r3.log\", \"submitted_at\": \"2026-05-15T10:27:08.529Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6985.6, \"gpu_hours\": 1.94}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"269147\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000-r3.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\\\"\", \"finished_at\": \"2026-05-15T12:05:43.550Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:05:46.554124+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3/checkpoint-1000\", \"metrics\": {\"eval_prove_rate\": 0.97, \"eval_mean_isr\": 0.6892, \"eval_isr_std\": 0.2037, \"eval_median_isr\": 0.75, \"eval_proved_only_isr\": 0.7105, \"eval_n_proved\": 97, \"eval_n_problems\": 100, \"genuine_count\": 0, \"genuine_rate\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h7_count\": 97, \"h7_rate\": 1, \"tautological_collapse\": true, \"train_final_prove_rate\": 0.827, \"train_final_mean_isr\": 0.5213, \"train_loss\": 0.00671, \"train_final_entropy\": 0.003, \"train_runtime_seconds\": 5783, \"train_steps\": 1000, \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.7533}, \"unknown\": {\"count\": 41, \"proved\": 39, \"prove_rate\": 0.951, \"mean_isr\": 0.6565}, \"true\": {\"count\": 34, \"proved\": 33, \"prove_rate\": 0.971, \"mean_isr\": 0.6814}}, \"n_premise_distribution\": {\"1\": 97}, \"pattern_description\": \"All 97 proved: 1 premise identical to conclusion (P therefore P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix).\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T12:23:34.170Z\", \"taxonomy_note\": \"D088 修正: metrics 字段已同步 (h7=97, h1=0, genuine=0, 全 H7a). D086 clean run classify_h7 确认 97/97 proved 均为 single_premise=conclusion (H7 tautology). 之前 metrics 残留 h1=97/h7=0 是 D086 前 classify_h7 bug 导致的错误分类. ⚠️ batch_h7ab_clean.json 中 plan018_additive_random_b01_s42_1000 条目处理的是原始失败实验(proved=100)非 r3(proved=97), 不可引用.\", \"h7_count\": 97, \"h1_count\": 0, \"h8_count\": 0, \"genuine_count\": 0}, \"plan009-sft-baseline-s44-1000\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T12:47:54.021Z\", \"updated_at\": \"2026-05-15T15:38:21.803Z\", \"hypothesis\": \"SFT 1000步 seed=44：与 s42/s43 相同配置的第三个 seed，验证 SFT 在 1000 步的 genuine rate 稳定性。3-seed 统计支撑 Goodhart collapse 是 RL (GRPO) 特有现象的 claim。\", \"parent\": \"plan009-sft-baseline-s42-r4\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T12:49:08.008Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000 --num_steps 1000 --seed 44 --no_wandb --gpu 1\\\"\", \"finished_at\": \"2026-05-15T12:50:00.305Z\", \"training_hours\": 0.01}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 742.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 100.25 MiB is free. Process 352142 has 62.36 GiB memory in use. Including non-PyTorch memory, this process has 32.51 GiB memory in use. Of the allocate\", \"completed_at\": \"2026-05-15T12:50:04.083Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:50:14.696431+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44}, \"pid\": \"352970\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s44-1000-r3.log\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.15, \"n_proved\": 15, \"n_problems\": 100, \"mean_isr\": 0.0884, \"isr_std\": 0.2268, \"median_isr\": 0, \"proved_only_mean_isr\": 0.5892, \"max_isr\": 0.8571, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.4412}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0}}, \"genuine_count\": 14, \"genuine_rate\": 0.9333, \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0667, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0667, \"content_independent_count\": 0, \"content_independent_rate\": 0, \"isr_1_count\": 0, \"isr_1_rate\": 0, \"train_final_loss\": 0.0171, \"train_avg_loss\": 0.1544, \"train_token_accuracy\": 0.995, \"train_runtime_s\": 1580.97, \"eval_elapsed_s\": 391.8}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/checkpoint-1000\", \"notes\": \"SFT s44 1000步 r3 成功（r1 OOM 因 GPU 冲突）。prove_rate=0.15 略高于 s42(0.13)/s43(0.11)，genuine_rate=93.3% 稳定高。3-seed SFT 均 genuine_rate>90% 无 Goodhart collapse。\", \"taxonomy_note\": \"D086 补扫: proved=15, H7=0, H1=1, H8=0, genuine=14 (93.3%). SFT 1000-step s44 保持高 genuine rate. eval: /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/eval_sta_results.json\", \"genuine_rate\": 0.933}, \"plan009-sft-baseline-s43-1000\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:28:46.064Z\", \"updated_at\": \"2026-05-15T15:38:21.200Z\", \"spec\": {\"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43}, \"hypothesis\": \"SFT 1000步 seed=43：与 s42 相同配置的第二个 seed，验证 SFT 在 1000 步的 genuine rate 稳定性。与 GRPO 各条件 1000步对比，确认 Goodhart collapse 是 RL 特有现象。\", \"parent\": \"plan009-sft-baseline-s43\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"352137\", \"log_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/checkpoint-1000/trainer_state.json\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000 --num_steps 1000 --seed 43 --no_wandb --gpu 0\\\"\", \"finished_at\": \"2026-05-15T13:15:26.388Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:15:29.227018+00:00\"}]}, \"metrics\": {\"prove_rate\": 0.11, \"n_proved\": 11, \"n_problems\": 100, \"mean_isr\": 0.0699, \"isr_std\": 0.2155, \"median_isr\": 0, \"proved_only_mean_isr\": 0.6352, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 11, \"prove_rate\": 0.3235}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0}}, \"genuine_count\": 10, \"genuine_rate\": 0.9091, \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0909, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0909, \"content_independent_count\": 0, \"content_independent_rate\": 0, \"isr_1_count\": 1, \"isr_1_rate\": 0.0909, \"train_final_loss\": 0.0167, \"train_avg_loss\": 0.1551, \"train_token_accuracy\": 0.9954, \"train_runtime_s\": 1584.79, \"eval_elapsed_s\": 326.1}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/checkpoint-1000\", \"conclusion\": \"success\", \"notes\": \"SFT s43 1000步结果与 s42 高度一致：prove_rate 11% vs 13%（-2pp），mean_isr 0.0699 vs 0.0738，final_loss 0.0167 vs 0.0168。差异在 seed 方差范围内。SFT baseline 稳定。注意：eval_sta.py 当前版本不输出 h7/h1/h8/genuine 分类指标。\", \"completed_at\": \"2026-05-15T13:25:00.854Z\", \"taxonomy_note\": \"D086 补扫: proved=11, H7=0, H1=1, H8=0, genuine=10 (90.9%). SFT 1000-step s43 保持高 genuine rate. eval: /root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/eval_sta_results.json\", \"genuine_count\": 10, \"genuine_rate\": 0.909}, \"plan009-sft-baseline-s42-1000\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T11:57:52.856Z\", \"updated_at\": \"2026-05-15T15:38:19.225Z\", \"hypothesis\": \"SFT 1000步延伸：验证 SFT（无 reward optimization）在 1000 步是否维持 genuine rate。500 步 SFT 已达 93% genuine，若 1000 步仍保持高 genuine → Goodhart collapse 是 RL (GRPO) 特有现象，非一般 finetuning 退化。与 exec-only/ISR/random 1000步形成对比。\", \"parent\": \"plan009-sft-baseline-s42-r4\", \"completed_at\": \"2026-05-15T12:25:32.031Z\", \"eval_prove_rate\": 0.13, \"eval_mean_isr\": 0.0738, \"eval_isr_std\": 0.2077, \"eval_proved_only_isr\": 0.5677, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 7.7, \"genuine_count\": 12, \"genuine_rate\": 0.923, \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}, \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000 --num_steps 1000 --seed 42 --no_wandb --bf16\", \"server\": \"westd-39279\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"submitted_at\": \"2026-05-15T19:58:15+08:00\", \"wall_clock_seconds\": 1415, \"gpu_hours\": 0.39, \"checkpoint_source\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/checkpoint-1000\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/checkpoint-1000\", \"log_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/checkpoint-1000/trainer_state.json\", \"metrics\": {\"train_final_loss\": 0.0168, \"train_last_step_loss\": 0.0168, \"train_token_accuracy\": 0.9955, \"train_epochs\": 15.88, \"train_runtime_sec\": 1415, \"train_steps\": 1000, \"eval_prove_rate\": 0.13, \"eval_n_proved\": 13, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0738, \"eval_isr_std\": 0.2077, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5677, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"eval_output_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json\", \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0769, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 12, \"genuine_rate\": 0.9231, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0769, \"isr_1_count\": 0, \"content_independent_count\": 0, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 12, \"prove_rate\": 0.353, \"mean_isr\": 0.209}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.011}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}}}, \"conclusion\": \"success\", \"notes\": \"SFT 1000步 (15.88 epochs): train loss 降至 0.0168（严重过拟合），但 eval genuine_rate=92.31% 与 500步的 92.9% 基本持平。prove_rate 从 0.14 微降至 0.13，h7=0，h1=1。结论：SFT 即使过拟合也不产生 Goodhart collapse（h7/h8=0），验证了 Goodhart 是 RL(GRPO) reward optimization 特有现象。Unknown 类全部 0/41 未 prove（与 500步一致），SFT 不具备泛化到 unknown 类的能力。\", \"taxonomy_note\": \"D086 补扫: proved=13, H7=0, H1=1, H8=0, genuine=12 (92.3%). SFT 1000-step 保持高 genuine rate，确认 hacking 是 RL-specific. eval: /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json\"}, \"exp1-random-b03-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:52:08.290Z\", \"updated_at\": \"2026-05-15T15:35:21.404Z\", \"spec\": {\"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"β=0.3 random seed 43: supplement for 3-seed statistics in Table 1. Reference: plan017-additive-random-s42\", \"plan_id\": \"EXP-1\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"num_steps\": 500, \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"963653\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s43/\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-random-b03-s43.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:35:47.399Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:35:48.354Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:35:52.992924+00:00\"}]}, \"notes\": \"D062/D063 INVALIDATED: eval used test_100.jsonl (wrong test set). Checkpoint deleted, cannot re-eval. Retrain as exp1-random-b03-s43-r2.\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.79, \"mean_isr\": 0.1745, \"isr_std\": 0.1628, \"median_isr\": 0.1667, \"proved_only_mean_isr\": 0.2209, \"hacking_rate_strict_h7\": 0, \"hacking_rate_functional\": 0.1013, \"genuine_rate\": 0.8987, \"genuine_count\": 71, \"n_proved\": 79, \"n_problems\": 100, \"h1_conclusion_in_premise\": 0.759, \"eval_data\": \"test_100.jsonl\", \"eval_output\": \"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43.json\"}, \"eval_metrics\": {\"prove_rate\": 0.79, \"mean_isr\": 0.1745, \"isr_std\": 0.1628, \"proved_only_isr\": 0.2209, \"n_proved\": 79, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.759, \"h1_count\": 60, \"genuine_rate\": 0.241, \"genuine_count\": 19, \"single_premise_rate\": 0, \"eval_data\": \"test_100.jsonl\"}, \"h7a_count\": null, \"h1_count\": null, \"taxonomy_note\": \"INVALIDATED: taxonomy based on test_100.jsonl eval, not comparable with proofwriter_fol_100 runs. Do not use in paper. D086 写入的 h7a/h1 字段仅反映旧 eval 数据，不可引用。\"}, \"exp1-random-b03-s43-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:44:48.792Z\", \"updated_at\": \"2026-05-15T15:35:19.765Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.3 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s43_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"117566\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-random-b03-s43-r4.log\", \"submitted_at\": \"2026-05-15T02:44:48.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"Random beta=0.3 s43 retry #4: previous r2 killed, r3 OOM. Clean GPU now.\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"plan_id\": \"EXP-1\", \"output_dir\": \"/root/autodl-tmp/outputs/exp1_random_b03_s43_r4\", \"wall_clock_seconds\": 6738.6, \"gpu_hours\": 1.87}, \"reproduce\": {\"finished_at\": \"2026-05-15T04:29:26.819Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:29:29.426423+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.5505, \"mean_isr\": 0.1358, \"parse_rate\": 1, \"train_loss\": 0.01365, \"train_runtime_sec\": 6161.1, \"epoch\": 2, \"eval_prove_rate\": 0.92, \"eval_mean_isr\": 0.1659, \"eval_isr_std\": 0.1147, \"eval_median_isr\": 0.1429, \"eval_proved_only_mean_isr\": 0.1803, \"eval_min_isr\": 0, \"eval_max_isr\": 0.5, \"eval_n_proved\": 92, \"eval_n_problems\": 100, \"eval_h7_strict_rate\": 0.076, \"eval_h7_strict_count\": 7, \"eval_h1_strict_rate\": 0.891, \"eval_h1_strict_count\": 82, \"eval_genuine_rate\": 0.0326, \"eval_genuine_count\": 3, \"eval_isr0_count\": 6, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.156}, \"unknown\": {\"count\": 41, \"proved\": 37, \"prove_rate\": 0.902, \"mean_isr\": 0.184}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.151}}, \"D086_correction\": \"H1 90→82, genuine 2→3 per D086 clean batch run\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s43_r4/checkpoint-500\", \"completed_at\": \"2026-05-15T04:37:07.139Z\", \"notes\": \"Training 500/500 steps, 1h42m. Final train: prove_rate=0.5505, mean_isr=0.1358, loss=0.01365. EVAL (proofwriter_fol_100.jsonl): PR=0.92, ISR=0.1659, H7=7/92(7.6%), H1=90/92(97.8%), genuine=2/92(2.2%). ANOMALY: massive seed variance vs s44-r2 (PR=0.23, ISR=0, H1=100%, genuine=0%). s43 learned high-PR hacking strategy with conclusion-in-premise; s44 barely proved anything. Both are random baseline — this variance weakens cross-seed claims.\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-random-b03-s43-r4.log\", \"eval_h7_strict_count\": 0, \"eval_h1_strict_count\": 89, \"eval_genuine_count\": 3, \"h7a_count\": 7, \"h1_count\": 82, \"taxonomy_note\": \"D086 clean run: H7a=7, H1=82, genuine=3. metrics 字段已从旧值 (H1=90, genuine=2) 同步修正.\"}, \"plan002-additive-b01-s42-1000\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:08:50.639Z\", \"updated_at\": \"2026-05-15T15:35:12.176Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode execution_sta --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42_1000 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"171076\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42-1000.log\", \"submitted_at\": \"2026-05-15T07:29:48.253Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4944.1, \"gpu_hours\": 1.37}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"171076\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42-1000.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode execution_sta --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42_1000 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\\\"\", \"finished_at\": \"2026-05-15T08:44:46.526Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T08:44:51.343174+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42_1000\", \"metrics\": {\"eval_prove_rate\": 0.9, \"eval_mean_isr\": 0.7892, \"eval_isr_std\": 0.3424, \"eval_proved_only_isr\": 0.8769, \"eval_median_isr\": 1, \"eval_n_proved\": 90, \"eval_n_problems\": 100, \"eval_component_count_mean\": 2.889, \"tautological_collapse\": true, \"train_final_prove_rate\": 0.855, \"train_final_mean_isr\": 0.532, \"h7_count\": 87, \"h7_rate\": 0.9667, \"h1_count\": 0, \"h1_rate\": 0, \"h1_near_count\": 1, \"h1_near_rate\": 0.0111, \"h8_conjunction_collapse_count\": 1, \"h8_conjunction_collapse_rate\": 0.0111, \"genuine_count\": 2, \"genuine_rate\": 0.0222, \"taxonomy_standard\": \"D086 clean run = ground truth. D084 residual removed.\"}, \"completed_at\": \"2026-05-15T08:52:12.385Z\", \"genuine_count\": 2, \"genuine_rate\": 0.0111, \"h8_count\": 1, \"notes\": \"D084 taxonomy re-audit (2026-05-15): 90 proved → H7=87 (96.7%), H1_exact=0, H1_near=1, H8=2 (2.2%), genuine=1 (1.1%). Changes vs prior: H7 +4 (paren normalization), H1 -4→0 (reclassified H7), H8 +1 (folio_1255 shared-antecedent conjunction missed), genuine -1. Tautological collapse confirmed. Taxonomy JSON: /root/autodl-tmp/outputs/plan002_additive_b01_s42_1000_taxonomy_unified.json\", \"h7a_count\": 87, \"h7_count\": 87, \"h1_count\": 0, \"taxonomy_note\": \"D086 clean run (ground truth): H7a=87, H7b=0, H1=0, H8=1, genuine=2. D084 residual (H8=2, genuine=1) replaced. metrics 字段已同步.\"}, \"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:55:48.888Z\", \"updated_at\": \"2026-05-15T15:34:21.957Z\", \"hypothesis\": \"β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。\", \"parent\": \"plan002-additive-b01-s42\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"377678\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42.log\", \"submitted_at\": \"2026-05-14T06:55:59.287Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan018\", \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500, \"checkpoint_source\": \"N/A (training, not eval)\", \"eval_data\": \"N/A (training, not eval)\", \"wall_clock_seconds\": 5160.4, \"gpu_hours\": 1.43, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:09:07.662Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:09:09.188407+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"tautological_collapse\": false, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 56, \"h1_rate\": 0.7089, \"h1_near_count\": 8, \"h1_near_rate\": 0.1013, \"h8_conjunction_collapse_count\": 3, \"h8_conjunction_collapse_rate\": 0.038, \"genuine_count_exact_h1\": 23, \"genuine_rate_exact_h1\": 0.2911, \"genuine_count_strict\": 12, \"genuine_rate_strict\": 0.1519, \"taxonomy_verification\": \"2026-05-15: full re-verification from eval_sta file. H1 exact=56, H1-near(substring)=8 (5 conc_in_prem + 3 prem_in_conc), H8=3, strict genuine=12. Registry original genuine=23 = H8(3) + H1-near(8) + strict genuine(12).\"}, \"notes\": \"Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\\n\\n对比 plan002-b01 (ISR β=0.1):\\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\\n- Median ISR: 0.036 vs plan002未记录\\n- Component count: 8.46 vs 5.58 (random组更多冗余)\\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\\n- Tautological collapse: 无 (component_2_ratio=0)\\n\\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\\n\\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42\", \"completed_at\": \"2026-05-14T08:21:59.737Z\", \"h7_count\": 0, \"h1_count\": 58, \"genuine_count\": 18, \"h8_count\": 4, \"genuine_rate\": 0.228, \"taxonomy_note\": \"D086 clean run (ground truth): H7=0, H1=58, H8=4, genuine=18 (22.8%). 1 H1∩H8 overlap sample; genuine computed from set union (|H7∪H1∪H8|=61), not simple subtraction (0+58+4=62). genuine = 79 − 61 = 18.\"}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:17.298Z\", \"updated_at\": \"2026-05-15T15:32:47.807Z\", \"hypothesis\": \"ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。\", \"parent\": \"plan002-additive-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T08:45:11.826Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s44\\\"\", \"finished_at\": \"2026-05-14T09:28:10.836Z\", \"training_hours\": 0.72}, \"spec\": {\"command\": \"python3 scripts/train_grpo.py --mode additive_bonus --isr_beta 0.1 --seed 44\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"466540\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s44.log\", \"submitted_at\": \"2026-05-14T08:46:23.037Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"wall_clock_seconds\": 2950.3, \"gpu_hours\": 0.82}, \"pid\": \"466540\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:28:12.416418+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": null, \"eval_proved_only_isr\": 0.902, \"eval_n_proved\": 89, \"eval_n_problems\": 100, \"h7_count\": 89, \"h7_rate\": 1, \"h1_count\": 0, \"h1_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"component_mean\": 4.33, \"comp_2_ratio\": 0.022, \"h7_fn_correction\": \"12 former genuine reclassified as H7: all n_prem=1 false negatives (normalization mismatch prevented conclusion matching)\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s44\", \"notes\": \"H7 FN correction: 12 samples with n_prem=1 misclassified as genuine. Mismatch types: 11 vacuous_quantifier_wrapping (∃x(P(x)) vs ∃x(∃y(P(y)))), 1 structural_simplification. Not simple whitespace/case but logically equivalent structural variants. Evidence file: /root/autodl-tmp/outputs/isr_s44_fn_evidence.json. Source eval: /root/runs/solver-trace-ablation/plan002-additive-b01-s44-eval.json\", \"completed_at\": \"2026-05-14T09:35:33.310Z\", \"h7_count\": 89, \"h1_count\": 0, \"genuine_count\": 0, \"h7_fn_correction\": \"vacuous quantifier wrapping (11/12) + structural simplification (1/12); model-learned obfuscation, not classifier bug\", \"h7a_count\": 77, \"h7b_count\": 12, \"taxonomy_note\": \"D086 补正(Reviewer): H7a=77, H7b=12, H1=0, H8=0, genuine=0. s44 全部 89 proved 均为 single_premise, H8(conjunction collapse)要求 multi-premise 数学上不可能触发. D086 clean run 误报 H8=1 已修正.\", \"h8_count\": 0}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:40:35.587Z\", \"updated_at\": \"2026-05-15T15:28:11.035Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"136261\", \"log_path\": \"~/runs/solver-trace-ablation/plan013-random-reward-s42-r4.log\", \"submitted_at\": \"2026-05-14T01:40:35.528Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline: replacing ISR with random values should degrade structural quality while maintaining execution reward, proving ISR's causal contribution\", \"plan_id\": \"plan013\", \"wall_clock_seconds\": 2492.4, \"gpu_hours\": 0.69}, \"reproduce\": {\"finished_at\": \"2026-05-14T02:19:57.306Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:19:58.514969+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r4/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r4/reward_log.jsonl\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}, \"completed_at\": \"2026-05-14T02:22:07.933Z\", \"notes\": \"⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。\", \"taxonomy_note\": \"D086 补扫: proved=100, H7=100(100%), H1=0, H8=0, genuine=0 (0%). Convex random reward (0.9·r_exec+0.1·random) 100% tautological collapse. eval: /root/solver-trace-ablation/outputs/eval_sta_plan013_random_reward_s42_r4.json\"}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:40:37.808Z\", \"updated_at\": \"2026-05-15T15:28:09.062Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"136339\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log\", \"submitted_at\": \"2026-05-14T01:40:37.746Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds\", \"plan_id\": \"plan001\", \"wall_clock_seconds\": 10020.8, \"gpu_hours\": 2.78}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:13:08.926Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:13:12.957272+00:00\"}]}, \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}, \"eval_greedy_prove_rate\": 0.13, \"eval_greedy_mean_isr\": 0, \"eval_greedy_proved_only_isr\": 0, \"eval_greedy_n_proved\": 13, \"eval_greedy_method\": \"eval_sta.py default (do_sample=False)\", \"eval_greedy_by_answer\": {\"true\": {\"count\": 34, \"proved\": 4, \"prove_rate\": 0.118}, \"false\": {\"count\": 25, \"proved\": 5, \"prove_rate\": 0.2}, \"unknown\": {\"count\": 41, \"proved\": 4, \"prove_rate\": 0.0976}}, \"eval_greedy_h7_count\": 0, \"eval_greedy_h7_rate\": 0, \"eval_greedy_h1_count\": 13, \"eval_greedy_h1_rate\": 1, \"eval_greedy_genuine_rate\": 0, \"eval_greedy_n_premises_proved_mean\": 17.92, \"eval_greedy_mean_components_proved\": 18.92, \"eval_greedy_n_premises_all_mean\": 32.67, \"eval_sampling_h1_rate\": 1, \"eval_sampling_h7_rate\": 0, \"eval_sampling_genuine_rate\": 0, \"eval_sampling_mean_components_proved\": 18.5, \"eval_greedy_vs_sampling_delta_pr\": -0.01, \"eval_method_note\": \"Greedy and sampling agree on failure profile (ISR*=0, H1=100%, components~18.5-18.9). s43 collapse is decoding-invariant.\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r4\", \"log_path\": \"/root/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log\", \"conclusion\": \"negative\", \"notes\": \"EXP-2 (2026-05-15): greedy eval (T=0) on same 100 held-out problems also done with eval_sta.py defaults (do_sample=False). Result: PR=0.13, ISR*=0.0, H1=100% (13/13), H7=0%, genuine=0%, mean components (proved)=18.92. Sampling (T=0.7) baseline: PR=0.14, ISR*=0.0, H1=100% (14/14), components~18.5. ΔPR=-0.01, both ISR*=0 → s43 collapse is decoding-invariant, NOT a sampling artifact. ~85% of inputs hit max_new_tokens with long repeated-clause outputs; the ~15% that do parse contain the conclusion verbatim among 14-30 premises (n_necessary=0 by per-clause ablation → ISR=0). 训练 PR(last100)=0.883 但 eval PR=13-14% across decoders, ISR=0。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。Checkpoint 已删除（C003）。Report: outputs/h7_classification/exp2_s43_greedy_vs_sample.txt.\", \"completed_at\": \"2026-05-14T04:27:38.542Z\", \"taxonomy_note\": \"D086 补扫: proved=13, H7=0, H1=13, H8=1, genuine=0 (0%). exec-only s43 PR=13%, 100% H1 collapse. eval: /root/solver-trace-ablation/outputs/eval_sta_plan001_exec_only_s43_r4.json\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:19:41.568Z\", \"updated_at\": \"2026-05-15T15:27:42.555Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"83029\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42.log\", \"submitted_at\": \"2026-05-13T22:20:46.569Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"exec-only 500步训练 baseline\", \"wall_clock_seconds\": 2576.3, \"gpu_hours\": 0.72}, \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A (failed before checkpoint)\", \"completed_at\": \"2026-05-13T23:03:42.892Z\", \"taxonomy_note\": \"D086 补扫: H7=1, H1=80, H8=6, genuine=7 (7.5%). 500-step exec-only 以 H1 为主 (86%), 少量 H7(1) 和 H8(6). eval文件: /root/solver-trace-ablation/outputs/eval_sta_plan001_exec_only_s42.json\", \"h7_count\": 1, \"h1_count\": 80, \"h8_count\": 6, \"genuine_count\": 7}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-15T15:17:35.229Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\", \"plan_id\": \"plan017\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"beta\": 0.3}, \"pid\": \"207116\", \"log_path\": \"~/runs/solver-trace-ablation/plan017-additive-random-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"finished_at\": \"2026-05-14T05:17:13.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:17:18.376399+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan017_additive_random_s42\", \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"tautological_collapse\": false, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 1, \"h1_count\": 48, \"genuine_rate\": 0, \"genuine_count\": 0}, \"completed_at\": \"2026-05-14T05:30:46.783Z\", \"h7a_count\": 4, \"h1_count\": 44, \"taxonomy_note\": \"D086 clean run: H7a=4 (new, deeper normalization), H7b=0, H1=44, H8=0, genuine=0. β=0.3 Random also produces H7 under higher reward pressure.\"}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:29:08.138Z\", \"updated_at\": \"2026-05-15T14:38:00.829Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"262261\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42.log\", \"submitted_at\": \"2026-05-14T05:32:32.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan002\", \"reward_formula\": \"r_exec * (1 + 0.1 * ISR)\", \"num_steps\": 500, \"wall_clock_seconds\": 4493.9, \"gpu_hours\": 1.25, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42\"}, \"parent\": \"plan002-additive-b03-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"262261\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\\\"\", \"finished_at\": \"2026-05-14T06:37:58.285Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:37:59.656631+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"h7_rate\": 0.16, \"h7_count\": 13, \"h1_rate\": 0.519, \"h1_count\": 42, \"h8_conjunction_collapse_count\": 12, \"h8_conjunction_collapse_rate\": 0.148, \"genuine_rate\": 0.173, \"genuine_count\": 14, \"tautological_collapse\": false, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse audit completed. 12/81 proved samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json\"}, \"notes\": \"H8 re-audit (2026-05-15): 81 proved samples. H7 (single premise=conclusion): 13/81=16.1%, H1 (multi-prem conclusion embedding): 42/81=51.9%, H8 (conjunction collapse): 12/81=14.8%, content-independent: 19/81=23.5%. Genuine (proved - H7 - H1 - H8): 14/81=17.3%. Pre-H8 genuine was 26/81=32.1% — H8 removed 12 samples. Combined conclusion duplication+conjunction = 82.7%. Eval source: proofwriter_fol_100.jsonl (backup at /root/autodl-tmp/eval_results_backup/). H8 JSON: /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json. ⚠️ RECLASSIFIED negative (Reviewer WARNING): 500步快照 genuine 30.9%（H8 未扣除，为上界），1000步崩塌至 2.2%，表明 Goodhart collapse 已在 500 步启动但未完成。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42\", \"completed_at\": \"2026-05-14T06:47:26.358Z\", \"genuine_count\": 14, \"h1_near_count\": null, \"taxonomy_note\": \"H1-near analysis infeasible: eval_sta deleted; genuine=14 computed from aggregated H7+H1_exact+H8 exclusion per D084. H1-near is supplementary-only (per-sample data available only for Random s42).\"}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:16.367Z\", \"updated_at\": \"2026-05-15T14:27:04.296Z\", \"hypothesis\": \"ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。\", \"parent\": \"plan002-additive-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T08:45:10.999Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\\\"\", \"finished_at\": \"2026-05-14T09:41:23.932Z\", \"training_hours\": 0.94}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"466128\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s43.log\", \"submitted_at\": \"2026-05-14T08:45:54.837Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4096.6, \"gpu_hours\": 1.14}, \"pid\": \"466128\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s43.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:41:25.536028+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_n_proved\": 61, \"eval_n_problems\": 100, \"eval_proved_only_isr\": 0.83, \"h7_count\": 59, \"h7_rate\": 0.9672, \"h1_count\": 0, \"h1_rate\": 0, \"h1_near_count\": 0, \"h1_near_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 2, \"genuine_rate\": 0.0328, \"proved_single_premise_ratio\": 1, \"taxonomy_note\": \"structurally determined: proved_single_premise_ratio=1.0, all taxonomy categories except H7 are zero by construction. eval file lost but classification derivable from structure.\"}, \"conclusion\": \"negative\", \"notes\": \"NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s43/checkpoint-500\", \"completed_at\": \"2026-05-14T09:54:11.468Z\", \"h7_count\": 59, \"h1_count\": 0, \"genuine_count\": 2}, \"plan018-additive-random-b01-s44-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:17:54.315Z\", \"updated_at\": \"2026-05-15T14:18:24.439Z\", \"spec\": {\"hypothesis\": \"Random β=0.1 s44 重训(r2): 原实验数据全部丢失(eval+checkpoint)，genuine=18 从未直接测量。重训以获取可溯源的 genuine 分解数据。训练参数与原实验完全一致。\", \"parent\": \"plan018-additive-random-b01-s44\", \"server\": \"westd-39279\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"plan_id\": \"plan018\", \"num_steps\": 500, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44_r2\\\"\"}}, \"plan018-additive-random-b01-s43-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:17:51.220Z\", \"updated_at\": \"2026-05-15T14:18:20.461Z\", \"spec\": {\"hypothesis\": \"Random β=0.1 s43 重训(r3): 原 r2 数据全部丢失(eval+checkpoint)，重训以恢复论文所需的 genuine 溯源数据。训练参数与 r2 完全一致。\", \"parent\": \"plan018-additive-random-b01-s43-r2\", \"server\": \"westd-39279\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"plan_id\": \"plan018\", \"num_steps\": 500, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r3\\\"\"}}, \"exp1-isr-b03-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:52:06.992Z\", \"updated_at\": \"2026-05-15T14:15:06.019Z\", \"spec\": {\"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"β=0.3 ISR seed 43: supplement for 3-seed statistics in Table 1. Reference: plan002-additive-b03-s42\", \"plan_id\": \"EXP-1\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"num_steps\": 500, \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"963576\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_isr_b03_s43/checkpoint-500/\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:07:44.402Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:07:45.360Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:07:50.234603+00:00\"}]}, \"notes\": \"D062/D063 INVALIDATED: eval used test_100.jsonl (wrong test set). Checkpoint deleted, cannot re-eval. Retrain as exp1-isr-b03-s43-r4.\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.91, \"mean_isr\": 0.2575, \"isr_std\": 0.2363, \"median_isr\": 0.3333, \"proved_only_mean_isr\": 0.283, \"hacking_rate_strict_h7\": 0.022, \"hacking_rate_functional\": 0.3297, \"genuine_rate\": 0.6703, \"genuine_count\": 61, \"n_proved\": 91, \"n_problems\": 100, \"h1_conclusion_in_premise\": 0.747, \"eval_data\": \"test_100.jsonl\", \"eval_output\": \"/root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json\"}, \"eval_metrics\": {\"prove_rate\": 0.91, \"mean_isr\": 0.2575, \"isr_std\": 0.2363, \"proved_only_isr\": 0.283, \"n_proved\": 91, \"h7_rate\": 0.022, \"h7_count\": 2, \"h1_rate\": 0.747, \"h1_count\": 68, \"genuine_rate\": 0.231, \"genuine_count\": 21, \"single_premise_rate\": 0.044, \"eval_data\": \"test_100.jsonl\"}, \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s43.log\"}, \"plan009-sft-baseline-s44-1000-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:55:38.775Z\", \"updated_at\": \"2026-05-15T14:14:37.264Z\", \"hypothesis\": \"SFT 1000步 seed=44（第三次重试）：r1/r2 均因 --gpu 0 覆盖 CUDA_VISIBLE_DEVICES 导致 OOM。本次用 --gpu 1 直接指定物理 GPU 1。验证 SFT 在 1000 步的 genuine rate 稳定性，完成 3-seed 统计。\", \"parent\": \"plan009-sft-baseline-s44-1000-r2\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44}, \"pid\": \"353656\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s44-1000-r3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000 --num_steps 1000 --seed 44 --no_wandb --gpu 1\\\"\", \"finished_at\": \"2026-05-15T13:24:08.251Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:24:12.025706+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.15, \"eval_n_proved\": 15, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0884, \"eval_isr_std\": 0.2268, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5892, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 0.0667, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 14, \"genuine_rate\": 0.9333, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.441, \"mean_isr\": 0.26}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000\", \"completed_at\": \"2026-05-15T14:11:36.232Z\"}, \"plan009-sft-baseline-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:32:29.554Z\", \"updated_at\": \"2026-05-15T14:14:33.719Z\", \"spec\": {\"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"188375\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s44.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s44 --num_steps 500 --seed 44 --no_wandb\\\"\", \"finished_at\": \"2026-05-15T08:25:36.539Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T08:25:40.098764+00:00\"}]}, \"metrics\": {\"train_final_loss\": 0.2397, \"train_last_step_loss\": 0.0328, \"train_token_accuracy\": 0.9928, \"train_epochs\": 7.94, \"train_runtime_sec\": 729.05, \"train_steps\": 500, \"eval_prove_rate\": 0.17, \"eval_n_proved\": 17, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0974, \"eval_isr_std\": 0.2409, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5729, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"eval_output_path\": \"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s44.json\", \"eval_tautological_collapse\": false, \"eval_h7_count\": 0, \"eval_h7_rate\": 0, \"eval_h1_count\": 2, \"eval_h1_rate\": 0.118, \"eval_genuine_count\": 15, \"eval_genuine_rate\": 0.882, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.441, \"mean_isr\": 0.257}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.027}, \"unknown\": {\"count\": 41, \"proved\": 1, \"prove_rate\": 0.024, \"mean_isr\": 0.008}}, \"eval_correction_note\": \"Corrected 2026-05-15: previous eval used test_100.jsonl (50/44/6 distribution), re-evaled with proofwriter_fol_100.jsonl (34/25/41)\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s44\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T08:32:34.374Z\"}, \"plan009-sft-baseline-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:08:54.164Z\", \"updated_at\": \"2026-05-15T14:14:22.594Z\", \"spec\": {\"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"171222\", \"log_path\": \"/root/runs/solver-trace-ablation/plan009-sft-baseline-s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s43 --num_steps 500 --seed 43 --no_wandb\\\"\", \"finished_at\": \"2026-05-15T07:42:41.848Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:42:44.711163+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s43\", \"metrics\": {\"train_loss\": 0.2391, \"train_token_accuracy\": 0.9938, \"train_epochs\": 7.94, \"train_runtime_sec\": 677.14, \"train_steps\": 500, \"eval_prove_rate\": 0.15, \"eval_mean_isr\": 0.0895, \"eval_isr_std\": 0.2338, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5967, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 0.067, \"genuine_count\": 14, \"genuine_rate\": 0.933, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"prove_rate\": 0.382, \"mean_isr\": 0.234}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.027}, \"unknown\": {\"count\": 41, \"proved\": 1, \"prove_rate\": 0.024, \"mean_isr\": 0.008}}, \"eval_data_path\": \"data/proofwriter_fol_100.jsonl\", \"eval_output_path\": \"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s43.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T07:52:31.794Z\"}, \"plan001-exec-only-s44-1000-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:51:03.762Z\", \"updated_at\": \"2026-05-15T13:51:38.874Z\", \"hypothesis\": \"Exec-only GRPO 1000步 seed=44（r2 重跑）：r1 因磁盘满被 kill。磁盘已清理（92GB 可用），从 step 0 重跑。\", \"parent\": \"plan001-exec-only-s44-1000\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T13:51:35.383Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44_1000_r2\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44_1000_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"363840\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44-1000-r2.log\", \"submitted_at\": \"2026-05-15T13:51:37.012Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"363840\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44-1000-r2.log\"}, \"plan001-exec-only-s43-1000-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:51:02.684Z\", \"updated_at\": \"2026-05-15T13:51:33.353Z\", \"hypothesis\": \"Exec-only GRPO 1000步 seed=43（r2 重跑）：r1 因磁盘满在 step 150 崩溃。磁盘已清理（92GB 可用），从 step 0 重跑。\", \"parent\": \"plan001-exec-only-s43-1000\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T13:51:29.890Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"363692\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-1000-r2.log\", \"submitted_at\": \"2026-05-15T13:51:32.190Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"363692\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-1000-r2.log\"}, \"plan001-exec-only-s44-1000\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:22:45.226Z\", \"updated_at\": \"2026-05-15T13:50:32.148Z\", \"hypothesis\": \"Exec-only GRPO 1000步 seed=44：与 plan016(s42) 相同配置的第三个 seed。完成 3-seed exec-only 1000步统计，与 SFT 1000步 3-seed 对照，统计支撑 Goodhart collapse 是 RL 特有现象的 claim。\", \"parent\": \"plan016-extended-1000-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44_1000\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"357074\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44-1000.log\", \"submitted_at\": \"2026-05-15T13:28:02.714Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1335.7, \"gpu_hours\": 0.37}, \"pid\": \"357074\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44-1000.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44_1000\\\"\", \"finished_at\": \"2026-05-15T13:50:19.963Z\"}, \"conclusion\": \"failed\", \"failure_reason\": \"磁盘满 (/dev/md0 250G/250G)，进程被手动 kill 防止 checkpoint 损坏。需从 step 0 重跑。\", \"completed_at\": \"2026-05-15T13:50:18.432Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:50:24.979972+00:00\"}]}}, \"plan001-exec-only-s43-1000\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:22:44.661Z\", \"updated_at\": \"2026-05-15T13:48:08.794Z\", \"hypothesis\": \"Exec-only GRPO 1000步 seed=43：与 plan016(s42) 相同配置的第二个 seed。3-seed exec-only 1000步统计，验证 Goodhart collapse（genuine→0%）在 exec-only 条件下的可重复性。与 SFT 1000步 3-seed 对照，确认 collapse 是 RL(GRPO) 特有现象。\", \"parent\": \"plan016-extended-1000-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T13:23:32.864Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000\\\"\", \"finished_at\": \"2026-05-15T13:45:01.320Z\", \"training_hours\": 0.36}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"356071\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-1000.log\", \"submitted_at\": \"2026-05-15T13:23:35.275Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1288.0, \"gpu_hours\": 0.36}, \"pid\": \"356071\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-1000.log\", \"failure_reason\": \"磁盘满 (os error 28): /root/autodl-tmp/ 250G/250G (100%)，step 150 保存 checkpoint 时 safetensors serialize 失败。checkpoint-100 完整可用(15GB)，checkpoint-150 不完整(仅2/4 shards)。分类: disk_full, retryable。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T13:45:03.313Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:45:05.583858+00:00\"}]}}, \"plan009-sft-baseline-s44-1000-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:53:24.774Z\", \"updated_at\": \"2026-05-15T12:56:27.871Z\", \"hypothesis\": \"SFT 1000步 seed=44（重试）：r1 因 CUDA_VISIBLE_DEVICES 未设导致 OOM 失败。与 s42/s43 相同配置的第三个 seed，验证 SFT 在 1000 步的 genuine rate 稳定性。3-seed 统计支撑 Goodhart collapse 是 RL (GRPO) 特有现象的 claim。\", \"parent\": \"plan009-sft-baseline-s44-1000\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000 --num_steps 1000 --seed 44 --no_wandb --gpu 0\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"353256\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s44-1000-r2.log\", \"submitted_at\": \"2026-05-15T12:53:53.733Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 32.2, \"gpu_hours\": 0.01}, \"pid\": \"353256\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s44-1000-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000 --num_steps 1000 --seed 44 --no_wandb --gpu 0\\\"\", \"finished_at\": \"2026-05-15T12:54:24.026Z\"}, \"failure_reason\": \"CUDA OOM: 重试 r2 在已被 plan009-sft-baseline-s43-1000 (PID 352142) 占用的 GPU 0 上启动，仅剩 100.25 MiB 可用显存。原始实验 plan009-sft-baseline-s44-1000 仍在 cuda:1 正常运行，此 r2 为冗余重试，无需再次重试。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T12:54:25.923Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:54:28.360459+00:00\"}]}}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-15T12:45:27.465Z\", \"spec\": {\"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\", \"plan_id\": \"plan_002\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_beta03_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"161819\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:24:44.110Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:24:48.666027+00:00\"}]}, \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"last100_prove_rate\": 0.5525, \"eval_prove_rate\": 0.18, \"eval_mean_isr\": 0.0257, \"eval_isr_std\": 0.0742, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.1427, \"eval_n_proved\": 18, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.778, \"h1_count\": 14, \"h8_conjunction_collapse_count\": 3, \"h8_conjunction_collapse_rate\": 0.1667, \"genuine_rate\": 0.0556, \"genuine_count\": 1, \"eval_by_type_false_pr\": 0.12, \"eval_by_type_false_isr\": 0.0102, \"eval_by_type_unknown_pr\": 0.195, \"eval_by_type_unknown_isr\": 0.0422, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.0172, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine 4→1.\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_beta03_s42\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b03-s42.log\", \"notes\": \"ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。\", \"conclusion\": \"negative\", \"eval_prove_rate\": 0.18, \"eval_mean_isr\": 0.0257, \"eval_isr_std\": 0.0742, \"eval_proved_only_isr\": 0.1427, \"eval_median_isr\": 0, \"eval_isr_pr_ratio\": 0.1427, \"completed_at\": \"2026-05-14T04:27:38.822Z\", \"genuine_count\": 1, \"genuine_rate\": 0.056, \"h8_count\": 3}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T22:40:41.773Z\", \"updated_at\": \"2026-05-15T12:45:21.831Z\", \"completed_at\": \"2026-05-13T23:46:00Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:46:01.596431+00:00\"}]}, \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s42\", \"server\": \"westd-39279\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"500-step exec-only baseline for STA comparison (K=8)\", \"pid\": \"84901\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r2.log\", \"submitted_at\": \"2026-05-13T22:42:40.204Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3820, \"gpu_hours\": 1.06}, \"notes\": \"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:46:00.369Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/reward_log.jsonl\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.871, \"h1_count\": 81, \"h8_conjunction_collapse_count\": 6, \"h8_conjunction_collapse_rate\": 0.0645, \"genuine_rate\": 0.0753, \"genuine_count\": 7, \"genuine_mean_isr\": 0.3141, \"h1_mean_isr\": 0.1055, \"conclusion_embedding_total\": 0.871, \"content_independent_predicates_count\": 1, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine 12→7.\"}, \"genuine_count\": 7, \"genuine_rate\": 0.075, \"h8_count\": 6}, \"plan004-o1-ablation-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:37:39.643Z\", \"updated_at\": \"2026-05-15T12:06:55.592Z\", \"hypothesis\": \"O(1) binary ISR (fast_isr_fol) vs O(N) full STA ablation: 100-step pilot showed binary ISR ≈ exec-only (all proved samples ISR=1). 500-step full run confirms O(1) is ineffective at scale — the LOO ablation (O(N)) is necessary for ISR to carry structural signal. Negative result strengthens paper's methodological contribution.\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T04:39:03.284Z\"}, \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_fast_isr_ablation.yaml --output_dir /root/autodl-tmp/outputs/plan004_fast_isr_s42 --num_steps 500 --num_generations 8 --no_wandb\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"155099\", \"log_path\": \"/root/runs/solver-trace-ablation/plan004-o1-ablation-s42.log\", \"submitted_at\": \"2026-05-15T12:50:15Z\", \"submitted_via\": \"manual_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"O(1) binary ISR (fast_isr_fol) vs O(N) full STA ablation. fast_sta_reward returns 1.0 for all proved samples, losing partial redundancy signal. Expected negative result.\", \"reward_formula\": \"r = 0.5 * exec + 0.5 * fast_ISR\", \"plan_id\": \"plan004\", \"output_dir\": \"/root/autodl-tmp/outputs/plan004_fast_isr_s42\"}, \"metrics\": {\"prove_rate\": 0.63, \"mean_isr\": 0.0072, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 63, \"h1_rate\": 1, \"h8_conjunction_collapse_count\": 2, \"h8_conjunction_collapse_rate\": 0.0317, \"genuine_count\": 0, \"genuine_rate\": 0, \"content_independent_predicates_count\": 3, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine unchanged (0).\"}, \"conclusion\": \"negative\", \"notes\": \"NEGATIVE (expected): O(1) binary ISR (fast_isr) 训练 500 步后 eval ISR=0.0072（本质为0）。模型生成大量冗余 premise（如62+重复 ground facts），per-clause ablation 删任一重复不影响结果，ISR趋近0。与 exec-only 的 ISR 崩塌模式一致（ISR=0.003）。确认 O(1) binary ISR 退化为 exec-only——LOO ablation (O(N)) 是 ISR 携带结构信号的必要条件。此负向结果强化论文方法论贡献：O(N) 复杂度有其必要性。PR=63% 低于 exec-only s42 (93%) 和 ISR β=0.1 s42 (81%)。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan004_fast_isr_s42/checkpoint-500\", \"log_path\": \"/root/runs/solver-trace-ablation/plan004-o1-ablation-s42.log\", \"completed_at\": \"2026-05-15T06:21:42.630Z\"}, \"exp1-isr-b03-s42-1000-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:31:37.813Z\", \"updated_at\": \"2026-05-15T11:52:23.241Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000 --num_steps 1000 --beta 0.3 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"224651\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s42-1000-r2.log\", \"submitted_at\": \"2026-05-15T09:32:05.796Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7320.6, \"gpu_hours\": 2.03}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"224651\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s42-1000-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000 --num_steps 1000 --beta 0.3 --seed 42 --no_wandb\\\"\", \"finished_at\": \"2026-05-15T11:27:09.017Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:27:13.616148+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.95, \"eval_mean_isr\": 0.734, \"eval_isr_std\": 0.2575, \"eval_median_isr\": 0.6, \"eval_proved_only_isr\": 0.7726, \"eval_n_proved\": 95, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.824}, \"unknown\": {\"count\": 41, \"proved\": 38, \"prove_rate\": 0.927, \"mean_isr\": 0.673}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.741}}, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 54, \"h1_rate\": 0.568, \"genuine_count\": 0, \"genuine_rate\": 0, \"tautological_collapse\": true, \"isr_1_count\": 41, \"isr_1_rate\": 0.432, \"single_premise_count\": 0, \"train_final_prove_rate\": 0.829, \"train_final_mean_isr\": 0.727, \"train_loss\": 0.0041, \"train_runtime_seconds\": 6280, \"train_final_entropy\": 9e-06, \"completions_mean_length\": 47, \"h8_conjunction_collapse_count\": 41, \"h8_conjunction_collapse_rate\": 0.432, \"content_independent_predicates\": true}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_isr_b03_s42_1000\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T11:34:06.399Z\"}, \"plan018-additive-random-b01-s42-1000-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:31:40.077Z\", \"updated_at\": \"2026-05-15T11:31:44.382Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000/checkpoint-350 --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"224797\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000-r2.log\", \"submitted_at\": \"2026-05-15T09:32:10.554Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7173.8, \"gpu_hours\": 1.99}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"224797\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000/checkpoint-350 --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\\\"\", \"finished_at\": \"2026-05-15T10:23:56.400Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:23:59.009335+00:00\"}]}, \"metrics\": {\"train_final_prove_rate\": 0.989, \"train_final_mean_isr\": 0.353, \"train_final_reward\": 1.062, \"train_steps\": 1000, \"train_runtime_seconds\": 2957, \"eval_prove_rate\": 1, \"eval_mean_isr\": 0.3333, \"eval_isr_std\": 0, \"eval_median_isr\": 0.3333, \"eval_proved_only_isr\": 0.3333, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_component_count_mean\": 3, \"genuine_rate\": 0, \"genuine_count\": 0, \"tautological_collapse\": true, \"h7_rate\": null, \"h7_count\": null, \"h1_rate\": null, \"h1_count\": null}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000\", \"completed_at\": \"2026-05-15T11:31:44.382Z\"}, \"plan018-additive-random-b01-s42-1000\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:08:56.941Z\", \"updated_at\": \"2026-05-15T09:25:12.327Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"197860\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000.log\", \"submitted_at\": \"2026-05-15T08:28:46.060Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3386.3, \"gpu_hours\": 0.94}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T08:28:44.610Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000 --no_wandb\\\"\", \"finished_at\": \"2026-05-15T09:25:10.249Z\", \"training_hours\": 0.94}, \"pid\": \"197860\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T09:25:12.327Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:25:17.262043+00:00\"}]}}, \"exp1-isr-b03-s42-1000\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:55:55.364Z\", \"updated_at\": \"2026-05-15T09:24:46.558Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000 --num_steps 1000 --beta 0.3 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"219058\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s42-1000.log\", \"submitted_at\": \"2026-05-15T09:16:01.559Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 525.0, \"gpu_hours\": 0.15}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"219058\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s42-1000.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000 --num_steps 1000 --beta 0.3 --seed 42 --no_wandb\\\"\", \"finished_at\": \"2026-05-15T09:24:44.644Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T09:24:46.558Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:24:49.137230+00:00\"}]}}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:57:09.690Z\", \"updated_at\": \"2026-05-15T08:29:40.375Z\", \"hypothesis\": \"Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"226200\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44.log\", \"submitted_at\": \"2026-05-14T04:29:05.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2725.5, \"gpu_hours\": 0.76}, \"pid\": \"226200\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\\\"\", \"finished_at\": \"2026-05-14T05:06:39.227Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:06:40.707032+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"tautological_collapse\": true, \"h7_rate\": 1, \"h7_count\": 97, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"conclusion_embedding_total\": 1}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s44\", \"conclusion\": \"negative\", \"notes\": \"TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。\", \"completed_at\": \"2026-05-14T05:14:30.940Z\", \"h7_count\": 98}, \"plan018-additive-random-b01-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:01:24.111Z\", \"updated_at\": \"2026-05-15T06:39:54.823Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。\", \"parent\": \"plan018-additive-random-b01-s43\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\\\"\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"858386\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log\", \"submitted_at\": \"2026-05-14T15:24:32.942Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\", \"wall_clock_seconds\": 6748.8, \"gpu_hours\": 1.87}, \"pid\": \"858386\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\\\"\", \"finished_at\": \"2026-05-14T16:43:53.042Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T16:43:54.952857+00:00\"}]}, \"metrics\": {\"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 93.2, \"h1_count\": 82, \"genuine_rate\": 6.8, \"genuine_count\": 6, \"eval_prove_rate\": 0.88, \"eval_mean_isr\": 0.058}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T17:17:01.774Z\"}, \"exp1-random-b03-s44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:42:02.173Z\", \"updated_at\": \"2026-05-15T03:07:35.496Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.3 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s44_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": 51297, \"log_path\": \"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s44_r2.json\", \"submitted_at\": \"2026-05-15T00:42:39.447Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"hypothesis\": \"Random beta=0.3 s44: 3-seed random control for Claim 2\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"plan_id\": \"EXP-1\", \"parent\": \"exp1-random-b03-s44\", \"output_dir\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2\", \"wall_clock_seconds\": 8595.6, \"gpu_hours\": 2.39}, \"reproduce\": {\"finished_at\": \"2026-05-15T02:26:26.919Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T02:26:39.221668+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.23, \"eval_proved_only_mean_isr\": 0, \"eval_mean_isr\": 0, \"eval_isr_std\": 0, \"eval_median_isr\": 0, \"eval_n_proved\": 23, \"eval_n_problems\": 100, \"eval_h7_strict_rate\": 0, \"eval_h7_strict_count\": 0, \"eval_h1_strict_rate\": 1, \"eval_h1_strict_count\": 23, \"eval_genuine_rate\": 0, \"eval_genuine_count\": 0, \"eval_data\": \"proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2/reward_log.jsonl\", \"completed_at\": \"2026-05-15T03:05:55.070Z\"}, \"exp1-isr-b03-s43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:02:10.292Z\", \"updated_at\": \"2026-05-15T02:39:55.709Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"pid\": 58051, \"log_path\": \"/root/autodl-tmp/outputs/exp1_isr_b03_s43_r3/reward_log.jsonl\", \"submitted_at\": \"2026-05-15T01:02:18.804Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"output_dir\": \"/root/autodl-tmp/outputs/exp1_isr_b03_s43_r3\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_isr_b03_s43_r3\", \"wall_clock_seconds\": 4321.2, \"gpu_hours\": 1.2}, \"conclusion\": \"success\", \"notes\": \"Training completed 500/500 steps in 69min. Final stats: prove_rate=0.56125, mean_isr=0.1515, parse_rate=1.0. Checkpoint saved at checkpoint-500. EVAL: PR=0.86 (greedy), mean_ISR=0.2535, H7_strict=4/86(4.7%), H1_strict=59/86(68.6%), total_hacking=63/86(73.3%), genuine=23/86(26.7%). Hacking pattern: predominantly H1 (conclusion embedding in multi-premise), NOT H7 (unlike s44's 100% H7). Data: proofwriter_fol_100.jsonl.\", \"completed_at\": \"2026-05-15T02:14:19.967Z\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_isr_b03_s43_r3/checkpoint-500\", \"log_path\": \"/root/runs/solver-trace-ablation/exp1-isr-b03-s43-r3.log\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.56125, \"mean_isr\": 0.1515, \"parse_rate\": 1, \"train_loss\": 0.0176, \"train_runtime_sec\": 4153.6, \"epoch\": 2, \"eval_prove_rate\": 0.86, \"eval_mean_isr\": 0.2535, \"eval_isr_std\": 0.2406, \"eval_median_isr\": 0.3333, \"eval_proved_only_mean_isr\": 0.2948, \"eval_min_isr\": 0, \"eval_max_isr\": 0.75, \"eval_n_proved\": 86, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_h7_strict_rate\": 0.047, \"eval_h7_strict_count\": 4, \"eval_h1_strict_rate\": 0.686, \"eval_h1_strict_count\": 59, \"eval_conclusion_in_premise_rate\": 0.733, \"eval_conclusion_in_premise_count\": 63, \"eval_genuine_rate\": 0.267, \"eval_genuine_count\": 23, \"eval_single_premise_rate\": 0.058, \"eval_single_premise_count\": 5, \"eval_isr_1_count\": 0, \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.334}, \"unknown\": {\"count\": 41, \"proved\": 35, \"prove_rate\": 0.854, \"mean_isr\": 0.199}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.26}}}}, \"exp1-random-b03-s43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:34:11.247Z\", \"updated_at\": \"2026-05-15T02:37:49.701Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.3 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"114576\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-random-b03-s43-r3.log\", \"submitted_at\": \"2026-05-15T02:34:10.754Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"beta=0.3 random s43 retry: supplement for 3-seed random statistics\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"plan_id\": \"EXP-1\", \"output_dir\": \"/root/autodl-tmp/outputs/exp1_random_b03_s43_r3\", \"wall_clock_seconds\": 218.9, \"gpu_hours\": 0.06}, \"reproduce\": {\"finished_at\": \"2026-05-15T02:37:46.271Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 28.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 24.25 MiB is free. Process 113293 has 81.17 GiB memory in use. Including non-PyTorch memory, this process has 13.77 GiB memory in use. Of the allocated \", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T02:37:49.701Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T02:37:52.575206+00:00\"}]}}, \"plan015-linear-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:05:37.944Z\", \"updated_at\": \"2026-05-15T02:36:29.622Z\", \"spec\": {\"command\": \"killed-cleanup\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"60030\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T01:05:52.053Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 5429.0, \"gpu_hours\": 1.51}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T02:36:21.092Z\"}, \"exp1-isr-b03-s43-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:07:39.840Z\", \"updated_at\": \"2026-05-15T02:36:28.581Z\", \"spec\": {\"command\": \"killed-cleanup\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"61219\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T01:07:48.622Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 5311.2, \"gpu_hours\": 1.48}, \"conclusion\": \"killed\", \"notes\": \"Duplicate of exp1-isr-b03-s43-r3 (already RUNNING on cuda:0). Created during D068 chaos, confirmed redundant at Loop #10.\", \"completed_at\": \"2026-05-15T02:36:19.862Z\"}, \"exp1-random-b03-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:30:55.259Z\", \"updated_at\": \"2026-05-15T02:36:22.901Z\", \"spec\": {\"command\": \"killed-cleanup\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"113288\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T02:31:28.051Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 294.9, \"gpu_hours\": 0.08}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T02:36:22.901Z\"}, \"exp1-isr-b03-s44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:21:38.601Z\", \"updated_at\": \"2026-05-15T01:09:36.604Z\", \"spec\": {\"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"hypothesis\": \"β=0.3 ISR seed 44 retry: original failed due to orphan process OOM on GPU 0. Same config as exp1-isr-b03-s44.\", \"plan_id\": \"EXP-1\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"num_steps\": 500, \"beta\": 0.3, \"parent\": \"exp1-isr-b03-s44\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s44_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"10597\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s44-r2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T00:15:28.410Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:15:30.528573+00:00\"}]}, \"eval_metrics\": {\"prove_rate\": 0.98, \"mean_isr\": 0.7275, \"isr_std\": 0.1184, \"proved_only_isr\": 0.7423, \"n_proved\": 98, \"h7_rate\": 1, \"h7_count\": 98, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"single_premise_rate\": 1, \"eval_data\": \"test_100.jsonl\"}, \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.95, \"mean_isr\": 0.705, \"isr_std\": 0.172, \"proved_only_isr\": 0.7421, \"n_proved\": 95, \"n_problems\": 100, \"h7_rate\": 1, \"h7_count\": 95, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"single_premise_rate\": 1, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"Re-eval with correct test set (D062). Previous test_100.jsonl results invalidated.\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_isr_b03_s44_r2/checkpoint-500/\", \"completed_at\": \"2026-05-15T00:35:22.489Z\", \"notes\": \"D062/D063: eval_metrics used test_100.jsonl (invalidated). metrics field contains re-eval with proofwriter_fol_100.jsonl (valid). eval_invalidated applies only to eval_metrics.\"}, \"exp1-random-b03-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:06:04.388Z\", \"updated_at\": \"2026-05-15T00:36:20.012Z\", \"spec\": {\"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"hypothesis\": \"β=0.3 random seed 44: supplement for 3-seed statistics in Table 1. Reference: plan017-additive-random-s42\", \"plan_id\": \"EXP-1\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"num_steps\": 500, \"beta\": 0.3, \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.3 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s44\"}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"finished_at\": \"2026-05-15T00:36:18.060Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T00:36:20.012Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:36:27.151961+00:00\"}]}}, \"exp1-isr-b03-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:06:01.473Z\", \"updated_at\": \"2026-05-14T23:21:59.279Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"7303\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s44.log\", \"submitted_at\": \"2026-05-14T23:16:22.350Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 139.8, \"gpu_hours\": 0.04}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"7303\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s44.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s44\\\"\", \"finished_at\": \"2026-05-14T23:18:40.671Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 44.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 12.25 MiB is free. Process 5480 has 83.06 GiB memory in use. Including non-PyTorch memory, this process has 11.89 GiB memory in use. Of the allocated me\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T23:18:42.116Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:18:43.961885+00:00\"}]}, \"notes\": \"OOM on first submission: GPU 0 was occupied by orphan PID 5480 (exp1-isr-b03-s43-r2 training process survived tmux kill). Pending resubmission after GPU 0 cleared.\"}, \"exp1-isr-b03-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:09:49.339Z\", \"updated_at\": \"2026-05-14T23:15:53.081Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s43_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"5475\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s43-r2.log\", \"submitted_at\": \"2026-05-14T23:14:05.147Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 107.9, \"gpu_hours\": 0.03}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"5475\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s43-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s43_r2\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T23:15:53.081Z\"}, \"exp2-exec-s43-greedy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:46:57.466Z\", \"updated_at\": \"2026-05-14T23:06:25.776Z\", \"spec\": {\"command\": \"eval_sta.py --greedy on plan001-exec-only-s43-r4 checkpoint\", \"server\": \"westd-39279\", \"data_path\": \"data/eval_100.jsonl\", \"data_count\": 100, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"EXP-2: Greedy re-eval of exec-only s43 to verify decoding invariance\", \"checkpoint_source\": \"plan001-exec-only-s43-r4\", \"eval_data\": \"data/eval_100.jsonl\", \"parent\": \"plan001-exec-only-s43-r4\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"N/A (eval only)\", \"metrics\": {\"greedy_pr\": 0.13, \"greedy_isr_star\": 0, \"greedy_h1_pct\": 100, \"greedy_h7_pct\": 0, \"greedy_genuine_pct\": 0, \"sampling_pr\": 0.14, \"sampling_isr_star\": 0, \"conclusion_text\": \"s43 collapse is decoding-invariant. Both greedy and sampling show ISR*=0, H1=100%, genuine=0%\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:06:15.509Z\"}, \"exp4-100step-h1h7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:47:55.686Z\", \"updated_at\": \"2026-05-14T23:06:24.790Z\", \"spec\": {\"command\": \"H1/H7 classification on plan003 (100-step exec-only checkpoint) eval outputs\", \"server\": \"westd-39279\", \"data_path\": \"plan003_eval_exec_only_r5.json\", \"data_count\": 100, \"model_name\": \"Qwen3-4B (100-step checkpoint)\", \"seed\": 42, \"hypothesis\": \"EXP-4: If hacking exists at 100-step PR=32%, supports RL-specific claim independent of PR level\", \"checkpoint_source\": \"sta-phase1-exec-only-r5\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp4_100step_h1h7_classification.json\", \"log_path\": \"N/A\", \"metrics\": {\"pr\": 0.32, \"isr_star\": 0.642, \"h7_pct\": 28.1, \"h1_pct\": 3.1, \"total_hacking_pct\": 31.2, \"genuine_pct\": 68.8, \"n_proved\": 32, \"h7_count\": 9, \"h1_count\": 1}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:06:14.584Z\"}, \"plan006-prolog-sta-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:19:39.743Z\", \"updated_at\": \"2026-05-14T18:47:53.131Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。\", \"notes\": \"Reviewer 独立核实: query-as-fact gaming, 0% genuine. 97/97 proved 样本中 95/97 n_necessary=1（功能性 H7）。模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。PR=0.97, ISR=0.885 是 gaming artifact（高 ISR 因单 clause = query）。第三种 Goodhart pathway（vs s42 clean H7, s43 degenerate syntax H1）。对照: s42=negative (clean H7=100%), s43=negative (uppercase pseudo-Prolog H1=97.4%), s44=negative (query-as-fact gaming, functional H7=95/97).\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T16:46:42.163Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s44\\\"\", \"finished_at\": \"2026-05-14T18:17:19.877Z\", \"training_hours\": 1.51}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"908945\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s44.log\", \"submitted_at\": \"2026-05-14T16:52:27.078Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5546.5, \"gpu_hours\": 1.54}, \"pid\": \"908945\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:17:22.483042+00:00\"}]}, \"metrics\": {\"pass_rate\": 0.97, \"isr_mean\": 0.885, \"isr_n_cl_ge3\": \"N/A (0 samples)\", \"n_clauses_dist\": \"78/100 single-clause, 22/100 two-clause\", \"h7_functional_rate\": 0.979, \"genuine_rate\": 0, \"premise_count_analysis\": \"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\", \"failure_mode\": \"query-as-fact gaming (total H7 collapse)\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s44/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T18:24:53.618Z\"}, \"plan006-prolog-sta-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:19:39.141Z\", \"updated_at\": \"2026-05-14T18:20:56.947Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。\", \"notes\": \"Eval: PR=0.38, ISR=0.185 proved-only. Strict classifier: H7=0%, H1=0%, Genuine=100%. 但功能分析显示所有 38 proved 样本 n_necessary=1（功能性 H7）。模型生成大写伪 Prolog（如 MARY_IS_AN_AVADEOTE.）—— 非标准语法，strict classifier 无法匹配 conclusion。与 s42 (clean H7=100%) 不同的 Goodhart 路径，但同样是 hacking。磁盘 240G/250G 需清理。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"901135\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s43.log\", \"submitted_at\": \"2026-05-14T16:36:41.878Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s43\", \"wall_clock_seconds\": 6158.3, \"gpu_hours\": 1.71}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"901135\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s43\\\"\", \"finished_at\": \"2026-05-14T18:03:44.715Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:03:46.512937+00:00\"}]}, \"metrics\": {\"train\": {\"final_prove_rate\": 0.769, \"final_mean_isr\": 0.129, \"final_loss\": 0.0155, \"final_entropy\": 0.09, \"final_reward\": 0.573, \"completion_length_mean\": 143, \"train_runtime_seconds\": 5095, \"train_runtime_minutes\": 84.9}, \"eval\": {\"n_problems\": 100, \"n_proved\": 38, \"prove_rate\": 0.38, \"mean_isr\": 0.0704, \"isr_std\": 0.1263, \"median_isr\": 0, \"proved_only_mean_isr\": 0.1853, \"min_isr\": 0, \"max_isr\": 1, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 11, \"prove_rate\": 0.44, \"mean_isr\": 0.1003}, \"unknown\": {\"count\": 41, \"proved\": 11, \"prove_rate\": 0.268, \"mean_isr\": 0.0394}, \"true\": {\"count\": 34, \"proved\": 16, \"prove_rate\": 0.471, \"mean_isr\": 0.0859}}}, \"h7_classification\": {\"h7_strict\": 0, \"h7_rate\": 0, \"h1_strict\": 37, \"h1_rate\": 0.974, \"conclusion_in_premise_total\": 37, \"conclusion_in_premise_rate\": 0.974, \"genuine_count\": 0, \"genuine_rate\": 0, \"isr_1_count\": 1, \"note\": \"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\"}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T18:19:20.203Z\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s43\"}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:29:47.634Z\", \"updated_at\": \"2026-05-14T17:34:52.375Z\", \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？\", \"parent\": \"plan001-exec-only-s42-r2\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence?\", \"plan_id\": \"plan016\", \"reward_formula\": \"r = r_exec (exec-only)\", \"num_steps\": 1000}, \"pid\": \"263268\", \"log_path\": \"~/runs/solver-trace-ablation/plan016-extended-1000-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\\\"\", \"finished_at\": \"2026-05-14T08:02:31.805Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:02:33.434519+00:00\"}]}, \"metrics\": {\"prove_rate\": 0.96, \"isr\": 0.003, \"n_proved\": 96, \"components\": 18.55, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 96, \"h1_rate\": 1, \"genuine_count\": 0, \"genuine_rate\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan016_extended_1000_s42\", \"completed_at\": \"2026-05-14T08:13:51.754Z\", \"notes\": \"Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\\\n\\\\n## 500 vs 1000 step comparison (eval_sta.py):\\\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\\\n|--------|-------------------|-----------------|--------|\\\\n| eval PR | 0.93 | 0.96 | +3.2% |\\\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\\\n| components | 6.58 | 18.55 | +182% |\\\\n| ISR=0 ratio | - | 94.8% | - |\\\\n| n_necessary=0 ratio | - | 94.8% | - |\\\\n\\\\n## Key findings:\\\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\\\n\\\\n## Implication for paper:\\\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse.\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T09:19:38.117Z\", \"updated_at\": \"2026-05-14T16:49:42.052Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。\", \"server\": \"westd-39279\", \"gpu\": \"\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T09:49:40.272Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42\\\"\", \"finished_at\": \"2026-05-14T10:38:13.891Z\", \"training_hours\": 0.81}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T09:46:00.917Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:46:02.621139+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:38:15.900825+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次启动失败。根因：config reward_mode=execution_sta (0.5*exec+0.5*ISR) 可能与 FOL 实验不匹配，待 Director 确认后修复重启。cuda:1 释放给 plan018。\"}}, \"account\": \"root\", \"notes\": \"Eval metrics provenance: eval 在训练完成后立即在 westd-39279 服务器上运行 eval_sta.py，checkpoint 路径 /root/autodl-tmp/outputs/plan006_prolog_sta_s42/。Eval 结果由 Worker 从服务器 SSH 读取 eval_results.json 并手动录入 registry。Checkpoint 可能已被磁盘清理删除（C003 save_total_limit=1）。训练日志: ~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log。H7 分类由 classify_h7.py 在 eval 目录上运行。\", \"spec\": {\"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42\\\"\", \"pid\": \"506117\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s42/ (may be cleaned up per C003)\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan006-prolog-exec-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:13:35.647Z\", \"updated_at\": \"2026-05-14T16:27:18.570Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper.\", \"notes\": \"Eval 完成。PR=21% (3-seed 最低), ISR=0.081, proved_only_ISR=0.387 (max_ISR=1.0)。与 s42/s43 不同模式：PR 极低但 proved_only_ISR 较高，可能有少量样本 ISR=1 (H7-like)。Prolog exec-only 3-seed 汇总：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008, s44 PR=21%/ISR=0.081。Mean PR=53.3%±31.1%, Mean ISR=0.040±0.037。跨 seed 极不稳定（PR std=31pp），与 FOL exec-only 一致。ISR 始终极低（<0.1），确认 Prolog exec-only 不产生 genuine reasoning traces。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T13:43:55.707Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44\\\"\", \"finished_at\": \"2026-05-14T15:20:42.126Z\", \"training_hours\": 1.61}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"479357\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s44.log\", \"submitted_at\": \"2026-05-14T13:43:57.850Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9800.7, \"gpu_hours\": 2.72}, \"pid\": \"479357\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:20:44.093424+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.21, \"eval_mean_isr\": 0.0812, \"eval_isr_std\": 0.2343, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.3866, \"eval_min_isr\": 0, \"eval_max_isr\": 1, \"eval_n_proved\": 21, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 683.9, \"eval_by_type_false_pr\": 0.04, \"eval_by_type_false_isr\": 0.04, \"eval_by_type_unknown_pr\": 0.317, \"eval_by_type_unknown_isr\": 0.099, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.09, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s44/checkpoint-500\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T16:27:18.570Z\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:40:28.142Z\", \"updated_at\": \"2026-05-14T16:27:01.864Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --num_steps 500 --seed 42 --no_wandb --gpu 1\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/\"}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"notes\": \"r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:18:55.639Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:18:57.313588+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/\", \"log_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/trainer_state.json\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.071, \"h1_count\": 1, \"genuine_rate\": 0.929, \"genuine_count\": 13, \"hacking_patterns\": \"near-zero (1/14 H1, 0 H7, 92.9% genuine)\", \"tautological_collapse\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:20:25.035Z\"}, \"plan006-prolog-exec-s43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:38:23.818Z\", \"updated_at\": \"2026-05-14T16:16:56.523Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T13:44:06.728Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3\\\"\", \"finished_at\": \"2026-05-14T15:54:25.754Z\", \"training_hours\": 2.17}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"483820\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r3.log\", \"submitted_at\": \"2026-05-14T13:44:08.516Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9168.0, \"gpu_hours\": 2.55}, \"pid\": \"483820\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r3.log\", \"notes\": \"Eval 完成。PR=56% (远低于 s42 的 83%), ISR=0.0084 (与 s42 的 0.031 同量级，均极低)。proved_only_ISR=0.015。Prolog exec-only 跨 seed 表现：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008。s43 prove_rate 显著下降但 ISR 模式一致（极低，ground fact enumeration hacking）。与 FOL exec-only 类似，存在跨 seed 不稳定性（FOL: s42=93%, s43=14%, s44=98%）。等 s44 eval 完成后计算 3-seed mean±std。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:54:27.521808+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.56, \"eval_mean_isr\": 0.0084, \"eval_isr_std\": 0.0221, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.015, \"eval_min_isr\": 0, \"eval_max_isr\": 0.1, \"eval_n_proved\": 56, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 868.2, \"eval_by_type_false_pr\": 0.48, \"eval_by_type_false_isr\": 0.0043, \"eval_by_type_unknown_pr\": 0.6585, \"eval_by_type_unknown_isr\": 0.0114, \"eval_by_type_true_pr\": 0.5, \"eval_by_type_true_isr\": 0.0078, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3/checkpoint-500\", \"completed_at\": \"2026-05-14T16:16:56.523Z\"}, \"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.722Z\", \"updated_at\": \"2026-05-14T15:00:09.178Z\", \"hypothesis\": \"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:34:13.338Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"finished_at\": \"2026-05-14T13:37:42.200Z\", \"training_hours\": 2.06}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"564900\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500}, \"pid\": \"564900\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:37:43.236026+00:00\"}]}, \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\", \"notes\": \"DONE (success). Random β=0.1 s44 对照分析完成: PR=0.89/ISR=0.062 (clean) vs ISR β=0.1 s44 PR=0.89/ISR=0.803 (H7=86.5% inflated). 同 PR 下 ISR reward 导致 conclusion duplication，random 无此问题。与 s42 结论一致: ISR s42 genuine ISR=0.337 vs Random s42 ISR=0.104 (3.2x)。Random 2/3 seeds done, 等 s43 (plan018-random-b01-s43-r2 QUEUED)。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s44/checkpoint-500\", \"completed_at\": \"2026-05-14T14:29:21.226Z\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:58.328Z\", \"updated_at\": \"2026-05-14T14:20:43.363Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\", \"conclusion\": \"killed\", \"notes\": \"模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。\", \"completed_at\": \"2026-05-14T14:20:42.452Z\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:32:37.140Z\", \"updated_at\": \"2026-05-14T13:43:01.701Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.\", \"parent\": \"plan006-prolog-exec-s43\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"712243\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r2.log\", \"submitted_at\": \"2026-05-14T12:33:05.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 136.2, \"gpu_hours\": 0.04}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"712243\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r2\\\"\", \"finished_at\": \"2026-05-14T12:35:20.730Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 48.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 40.25 MiB is free. Process 587160 has 78.09 GiB memory in use. Including non-PyTorch memory, this process has 16.83 GiB memory in use. Of the allocated \", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:35:22.121Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:35:23.802887+00:00\"}]}, \"notes\": \"OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T07:13:34.169Z\", \"updated_at\": \"2026-05-14T12:33:17.845Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T09:49:36.534Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42\\\"\", \"finished_at\": \"2026-05-14T11:29:25.346Z\", \"training_hours\": 1.66}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T09:47:36.390Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:47:38.546001+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:29:27.709792+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: FileNotFoundError — data/prolog/train_500_seed42.jsonl 不存在 | error_type: data | 同一原因影响所有 plan006 实验 (exec/sta × s42/s43/s44) | 建议: 需先生成 Prolog 训练数据再重试\"}}, \"account\": \"root\", \"notes\": \"Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"506020\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42}, \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s42/checkpoint-500\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s42.log\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:13:35.078Z\", \"updated_at\": \"2026-05-14T12:32:13.799Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.\", \"notes\": \"KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 --warmup_ratio 0.1\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"587155\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43.log\", \"submitted_at\": \"2026-05-14T12:22:08.915Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"wall_clock_seconds\": 602.2, \"gpu_hours\": 0.17}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"587155\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 --warmup_ratio 0.1\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:32:11.136Z\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:37:49.306Z\", \"updated_at\": \"2026-05-14T11:48:05.087Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r3 --num_steps 500 --seed 42 --bf16 --wandb_project solver-trace-ablation --wandb_run plan009-sft-s42-r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"566690\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r3.log\", \"submitted_at\": \"2026-05-14T11:39:19.395Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18.5, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"566690\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r3.log\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r3 --num_steps 500 --seed 42 --bf16 --wandb_project solver-trace-ablation --wandb_run plan009-sft-s42-r3\\\"\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"finished_at\": \"2026-05-14T11:39:36.697Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:39:37.935Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:39:39.416777+00:00\"}]}, \"notes\": \"r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:02:25.369Z\", \"updated_at\": \"2026-05-14T11:43:20.347Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"plan_id\": \"plan_009\", \"notes\": \"SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --num_steps 200 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"548527\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r2.log\", \"submitted_at\": \"2026-05-14T11:08:22.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 236.8, \"gpu_hours\": 0.07}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:12:19.306Z\", \"failure_reason\": \"OOM: 缺少 CUDA_VISIBLE_DEVICES 显式设置，device_map='auto' 跨 GPU 侵入 cuda:0 (plan006)，导致双卡 OOM。修复：(1) 启动命令加 --gpu 1，(2) device_map 改为 {\\\"\\\": 0} 或 .to(\\\"cuda\\\")，(3) num_steps 改为 500\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.260Z\", \"updated_at\": \"2026-05-14T11:42:09.950Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"540910\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43.log\", \"submitted_at\": \"2026-05-14T10:58:27.110Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"checkpoint_source\": \"plan018-additive-random-b01-s42\", \"eval_data\": \"data/train_500_seed42.jsonl\", \"wall_clock_seconds\": 1929.4, \"gpu_hours\": 0.54}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:30:34.690Z\"}, \"failure_reason\": \"磁盘满 (No space left on device): /root/autodl-tmp/ 250G/250G 100% 占满。训练在 step 200/500 保存 checkpoint-200 时 safetensors 序列化失败 (os error 28)。根因: 多个已完成实验的 checkpoint 未清理。可重试——清理磁盘后重跑。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:30:36.549Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:30:40.886615+00:00\"}]}, \"notes\": \"Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \\\"No space left on device\\\". No checkpoint saved. Disk now has 109G free. Retryable as-is.\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:06:38.613Z\", \"updated_at\": \"2026-05-14T09:07:42.314Z\", \"spec\": {\"command\": \"rule-based hacking taxonomy classification on eval_sta outputs\", \"server\": \"westd-39279\", \"data_path\": \"eval_results.json from plan002-b01-s42 + plan018-b01-s42\", \"data_count\": 160, \"model_name\": \"N/A (rule-based analysis)\", \"seed\": \"N/A\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"artifacts/hacking_taxonomy_comparison.md\", \"completed_at\": \"2026-05-14T09:07:12.765Z\", \"hypothesis\": \"ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}, \"notes\": \"D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。\"}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:20:47.812Z\", \"updated_at\": \"2026-05-14T06:31:05.119Z\", \"spec\": {\"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:55:02.341Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:55:06.559440+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/reward_log.jsonl\", \"completed_at\": \"2026-05-13T23:59:25.396Z\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}, \"notes\": \"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\"STA 抑制 reward hacking\\\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。\"}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T03:43:37.925Z\", \"updated_at\": \"2026-05-14T04:29:48.645Z\", \"hypothesis\": \"Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T03:49:52.891Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_downstream.py --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/plan014_downstream_nli.json --num_generations 8 --workers 4\\\"\", \"finished_at\": \"2026-05-14T04:26:05.334Z\", \"training_hours\": 0.6}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-14T03:51:18.427Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:51:19.514390+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:26:06.788787+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"r1 失败: checkpoint_path 多了 /checkpoint-500。save_total_limit=1 导致模型直接保存在 plan001_exec_only_s42/ 根目录。修正路径为 /root/autodl-tmp/outputs/plan001_exec_only_s42 即可。等 s43 re-eval 完成后重跑。\"}}, \"notes\": \"Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_downstream.py --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/plan014_downstream_nli.json --num_generations 8 --workers 4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"216133\", \"log_path\": \"~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log\", \"submitted_at\": \"2026-05-14T04:17:30.763Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 737.9, \"gpu_hours\": 0.2}, \"pid\": \"216133\", \"log_path\": \"~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan014_downstream_nli.json\"}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:02:31.830Z\", \"updated_at\": \"2026-05-14T01:41:28.427Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"133258\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500 steps seed 43 (r3), 3-seed baseline 2nd seed\", \"plan_id\": \"plan_001\"}, \"conclusion\": \"failed\", \"failure_reason\": \"OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 23\", \"checkpoint_path\": \"N/A (disk full crash at step 23)\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r3/reward_log.jsonl\", \"completed_at\": \"2026-05-14T01:41:28.427Z\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:02:30.063Z\", \"updated_at\": \"2026-05-14T01:41:28.122Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"133178\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline (r3): random value replaces ISR to isolate ISR-specific signal vs multi-objective regularization\", \"plan_id\": \"plan_013\", \"hyperparams\": {\"alpha\": 0.9, \"beta\": 0.1, \"K\": 8, \"num_steps\": 500, \"reward_type\": \"random_penalty\"}}, \"conclusion\": \"failed\", \"failure_reason\": \"OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 28\", \"checkpoint_path\": \"N/A (disk full crash at step 28)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r3/reward_log.jsonl\", \"completed_at\": \"2026-05-14T01:41:28.122Z\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:22:12.292Z\", \"updated_at\": \"2026-05-14T01:01:56.416Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"126541\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-r2.log\", \"submitted_at\": \"2026-05-14T00:22:12.241Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500步 seed 43 (retry), 3-seed baseline 第2个 seed\", \"wall_clock_seconds\": 2384.2, \"gpu_hours\": 0.66}, \"checkpoint_path\": \"N/A (crashed after submission)\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r2/reward_log.jsonl\", \"conclusion\": \"failed\", \"failure_reason\": \"Process crashed after submission (PID 126546 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.\", \"completed_at\": \"2026-05-14T01:01:56.416Z\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:22:10.140Z\", \"updated_at\": \"2026-05-14T01:01:55.694Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"126461\", \"log_path\": \"~/runs/solver-trace-ablation/plan013-random-reward-s42-r2.log\", \"submitted_at\": \"2026-05-14T00:22:10.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline (retry): 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\", \"wall_clock_seconds\": 2385.6, \"gpu_hours\": 0.66}, \"checkpoint_path\": \"N/A (crashed after submission)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r2/reward_log.jsonl\", \"conclusion\": \"failed\", \"failure_reason\": \"Process crashed after submission (PID 126466 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.\", \"completed_at\": \"2026-05-14T01:01:55.694Z\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:56:44.062Z\", \"updated_at\": \"2026-05-14T00:21:05.430Z\", \"spec\": {\"hypothesis\": \"Random reward baseline: 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1\\\"\", \"server\": \"westd-39279\", \"data_path\": \"data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan_013\", \"gpu\": \"cuda:0\", \"hyperparams\": {\"alpha\": 0.9, \"beta\": 0.1, \"K\": 8, \"num_steps\": 500, \"reward_type\": \"random_penalty\"}, \"pid\": 122796, \"output_dir\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42\", \"reward_mode\": \"random_reward\", \"exec_weight\": 0.9, \"sta_weight\": 0.1, \"num_steps\": 500}, \"checkpoint_path\": \"N/A (GPU overflow, no valid output)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42.log\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA_VISIBLE_DEVICES not set (inline assignment not exported), GPU overflow to both GPUs\", \"completed_at\": \"2026-05-14T00:21:05.430Z\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:55:08.635Z\", \"updated_at\": \"2026-05-14T00:21:04.003Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"121275\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43.log\", \"submitted_at\": \"2026-05-13T23:55:08.544Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500步 seed 43, 3-seed baseline 第2个 seed。预期 prove_rate>0.80 (与 s42 一致)\", \"wall_clock_seconds\": 1555.5, \"gpu_hours\": 0.43}, \"checkpoint_path\": \"N/A (killed by OOM before completion)\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43.log\", \"conclusion\": \"failed\", \"failure_reason\": \"OOM by plan013 GPU overflow — plan013 未设 CUDA_VISIBLE_DEVICES 导致占用两张 GPU，plan001-s43 被 OOM kill\", \"completed_at\": \"2026-05-14T00:21:04.003Z\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:21:48.691Z\", \"updated_at\": \"2026-05-13T23:03:19.945Z\", \"spec\": {\"command\": \"eval_sta.py on r5 exec-only checkpoint\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"83690\", \"log_path\": \"~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log\", \"submitted_at\": \"2026-05-13T22:21:48.658Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"model_name\": \"Qwen3-4B (r5 exec-only checkpoint)\", \"seed\": 0, \"checkpoint_source\": \"sta-phase1-exec-only-r5\", \"eval_data\": \"proofwriter_fol_100\", \"hypothesis\": \"Full STA eval on exec-only 100-step checkpoint to measure formalization quality\", \"wall_clock_seconds\": 2490.2, \"gpu_hours\": 0.69}, \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json\", \"log_path\": \"~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log\", \"completed_at\": \"2026-05-13T23:03:18.848Z\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:42:40.242Z\", \"updated_at\": \"2026-05-13T23:03:11.395Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"85710\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r3.log\", \"submitted_at\": \"2026-05-13T22:42:40.204Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"exec-only 500步训练 baseline (retry 3)\", \"wall_clock_seconds\": 1228.1, \"gpu_hours\": 0.34}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:03:08.298Z\", \"failure_reason\": \"OOM crash - duplicate submission while plan001-r2 was occupying cuda:0\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:54:31.353Z\", \"updated_at\": \"2026-05-13T22:20:41.274Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"75968\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r5.log\", \"submitted_at\": \"2026-05-13T20:54:38.781Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Full STA continuous ISR (0.0-1.0) 作为 reward 组件，应在训练中产生与 execution-only 不同的 ISR 趋势——execution-only ISR 随 prove_rate 上升而虚高(reward hacking)，execution+STA ISR 维持真实水平(STA 抑制 hacking)\", \"wall_clock_seconds\": 3506.3, \"gpu_hours\": 0.97}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/\", \"log_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/reward_log.jsonl\", \"completed_at\": \"2026-05-13T21:53:05.068Z\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:54:27.505Z\", \"updated_at\": \"2026-05-13T21:53:04.486Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"75890\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r5.log\", \"submitted_at\": \"2026-05-13T20:54:37.293Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"K=8 增加 within-group variance，减少全零 reward batch，使 GRPO 有更多有效梯度信号\", \"wall_clock_seconds\": 3507.2, \"gpu_hours\": 0.97}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/\", \"log_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/reward_log.jsonl\", \"completed_at\": \"2026-05-13T21:53:04.486Z\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:28:22.778Z\", \"updated_at\": \"2026-05-13T20:52:58.761Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"70797\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r4.log\", \"submitted_at\": \"2026-05-13T20:28:32.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1404.7, \"gpu_hours\": 0.39}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T20:28:31.240Z\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T20:45:55.480Z\", \"training_hours\": 0.29}, \"pid\": \"70797\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:45:56.962544+00:00\"}]}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T20:51:56.799Z\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:28:18.040Z\", \"updated_at\": \"2026-05-13T20:52:56.416Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"70716\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r4.log\", \"submitted_at\": \"2026-05-13T20:28:30.420Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1405.8, \"gpu_hours\": 0.39}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:28:28.733Z\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T20:45:53.506Z\", \"training_hours\": 0.29}, \"pid\": \"70716\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:45:54.294365+00:00\"}]}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T20:51:56.183Z\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:04.067Z\", \"updated_at\": \"2026-05-13T20:23:15.460Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"67225\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r3.log\", \"submitted_at\": \"2026-05-13T20:15:15.911Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 276.4, \"gpu_hours\": 0.08}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:15:14.333Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T20:19:51.612Z\", \"training_hours\": 0.08}, \"pid\": \"67225\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r3.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:19:52.268Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:19:52.981720+00:00\"}]}, \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:08.133Z\", \"updated_at\": \"2026-05-13T20:23:14.516Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"67306\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r3.log\", \"submitted_at\": \"2026-05-13T20:15:17.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 277.9, \"gpu_hours\": 0.08}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T20:15:16.704Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T20:19:54.409Z\", \"training_hours\": 0.08}, \"pid\": \"67306\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r3.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:19:55.400Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:19:56.549926+00:00\"}]}, \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:55:08.640Z\", \"updated_at\": \"2026-05-13T19:55:41.544Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"62364\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r2.log\", \"submitted_at\": \"2026-05-13T19:55:19.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 22.5, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T19:55:18.267Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T19:55:40.449Z\", \"training_hours\": 0.01}, \"pid\": \"62364\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:55:41.544Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:42.974865+00:00\"}]}}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:55:04.711Z\", \"updated_at\": \"2026-05-13T19:55:37.426Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"62283\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r2.log\", \"submitted_at\": \"2026-05-13T19:55:17.509Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19.9, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:55:16.037Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T19:55:36.845Z\", \"training_hours\": 0.01}, \"pid\": \"62283\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:55:37.426Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:38.155358+00:00\"}]}}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:53.258Z\", \"updated_at\": \"2026-05-13T19:33:03.905Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"59574\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta.log\", \"submitted_at\": \"2026-05-13T19:32:47.783Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 16.1, \"gpu_hours\": 0.0}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T19:30:58.981Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T19:33:03.170Z\", \"training_hours\": 0.03}, \"pid\": \"59574\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:33:03.905Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:33:05.009356+00:00\"}]}}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:46.351Z\", \"updated_at\": \"2026-05-13T19:33:01.169Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"59274\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only.log\", \"submitted_at\": \"2026-05-13T19:32:30.340Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 30.8, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:32:28.753Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T19:33:00.602Z\", \"training_hours\": 0.01}, \"pid\": \"59274\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:33:01.169Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:33:01.864437+00:00\"}]}}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:11:13.283Z\", \"updated_at\": \"2026-05-13T18:12:44.147Z\", \"spec\": {\"command\": \"python3 scripts/gt_isr_baseline.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"model_name\": \"ground-truth-fol\", \"seed\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/solver-trace-ablation/outputs/gt_isr_baseline.json\", \"log_path\": \"/root/solver-trace-ablation/outputs/gt_isr_baseline.json\", \"completed_at\": \"2026-05-13T18:12:43.141Z\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:51:48.853Z\", \"updated_at\": \"2026-05-13T18:10:40.982Z\", \"spec\": {\"hypothesis\": \"锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）\", \"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"server\": \"westd-39279\", \"data_source\": \"tasksource/folio\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 scripts/phase0_baseline.py --model_path models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output outputs/phase0_baseline.json\", \"seed\": 0, \"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"/root/solver-trace-ablation/outputs/phase0_baseline.json\", \"notes\": \"conclusion=success 但语义是 baseline_anchored（registry 不支持自定义 conclusion）。此实验是 baseline 锚定，非传统 success/failure。ISR 盲区：premise-conclusion 重复的 trivial formalization 可能获高 ISR，论文 Discussion 需讨论。\"}, \"log_path\": \"/tmp/phase0_baseline.log\", \"checkpoint_path\": \"/root/solver-trace-ablation/outputs/phase0_baseline.json\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T18:04:56.962Z\"}}, \"count\": 86, \"total\": 86, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3513}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-15T15:56:49.961Z_

<details><summary>↩ Tool result · `toolu_016Vqs1xFYjp18TFCkZrJiKS`</summary>

```text
artifacts/dream_reports/dream_20260513T215750/best/paper.tex
artifacts/dream_reports/dream_20260513T215750/median/paper.tex
artifacts/dream_reports/dream_20260513T215750/worst/paper.tex
artifacts/_project/paper/table3_isr_collapse.tex
artifacts/paper_tables/table3_isr_collapse.tex
artifacts/_project/paper/table4_beta01_comparison.tex
artifacts/paper_tables/table4_beta01_comparison.tex
artifacts/_project/paper/table1_goodhart.tex
artifacts/paper_tables/table1_goodhart.tex
artifacts/dream_reports/dream_20260514T092544/best/paper.tex
artifacts/dream_reports/dream_20260514T092544/median/paper.tex
artifacts/dream_reports/dream_20260514T092544/worst/paper.tex
artifacts/_deprecated/table2_hacking_taxonomy_from_project_paper.tex
artifacts/_deprecated/table2_hacking_taxonomy_from_paper_tables.tex
artifacts/table2_hacking_taxonomy.tex
artifacts/dream_reports/dream_20260514T173834/best/paper.tex
artifacts/dream_reports/dream_20260514T173834/median/paper.tex
artifacts/dream_reports/dream_20260514T173834/worst/paper.tex
artifacts/_project/paper/method_1594b5.tex
artifacts/_project/paper/experiments_29c3b6.tex
artifacts/_project/paper/method_fc0803.tex
artifacts/_project/paper/method_9dcd9a.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/experiments_b77022.tex
artifacts/_project/paper/introduction_41056c.tex
docs/paper/discussion.tex
artifacts/_project/paper/related_work_b05493.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/method_4d5248.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/introduction_b19e34.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/abstract_c1671f.tex
artifacts/_project/paper/conclusion_0cce3f.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/method_76d073.tex
artifacts/_project/paper/introduction_12a465.tex
artifacts/_project/paper/introduction_176853.tex
artifacts/_project/paper/experiments_76b47a.tex
artifacts/_project/paper/experiments_49ea86.tex
paper/main.tex
paper/limitations.tex
paper/related_work.tex
docs/paper/related_work.tex
artifacts/_project/paper/table_1000step_comparison.tex
artifacts/paper_tables/table_1000step_comparison.tex
docs/paper/abstract.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
paper/abstract.tex
paper/conclusion.tex
paper/method.tex
paper/introduction.tex
paper/experiments.tex
paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "21e1c28e-76e5-46a1-9f29-09b5b033b0e7",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260513T215750/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T215750/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T215750/worst/paper.tex",
      "artifacts/_project/paper/table3_isr_collapse.tex",
      "artifacts/paper_tables/table3_isr_collapse.tex",
      "artifacts/_project/paper/table4_beta01_comparison.tex",
      "artifacts/paper_tables/table4_beta01_comparison.tex",
      "artifacts/_project/paper/table1_goodhart.tex",
      "artifacts/paper_tables/table1_goodhart.tex",
      "artifacts/dream_reports/dream_20260514T092544/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T092544/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T092544/worst/paper.tex",
      "artifacts/_deprecated/table2_hacking_taxonomy_from_project_paper.tex",
      "artifacts/_deprecated/table2_hacking_taxonomy_from_paper_tables.tex",
      "artifacts/table2_hacking_taxonomy.tex",
      "artifacts/dream_reports/dream_20260514T173834/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T173834/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T173834/worst/paper.tex",
      "artifacts/_project/paper/method_1594b5.tex",
      "artifacts/_project/paper/experiments_29c3b6.tex",
      "artifacts/_project/paper/method_fc0803.tex",
      "artifacts/_project/paper/method_9dcd9a.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/experiments_b77022.tex",
      "artifacts/_project/paper/introduction_41056c.tex",
      "docs/paper/discussion.tex",
      "artifacts/_project/paper/related_work_b05493.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/method_4d5248.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/introduction_b19e34.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/abstract_c1671f.tex",
      "artifacts/_project/paper/conclusion_0cce3f.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/method_76d073.tex",
      "artifacts/_project/paper/introduction_12a465.tex",
      "artifacts/_project/paper/introduction_176853.tex",
      "artifacts/_project/paper/experiments_76b47a.tex",
      "artifacts/_project/paper/experiments_49ea86.tex",
      "paper/main.tex",
      "paper/limitations.tex",
      "paper/related_work.tex",
      "docs/paper/related_work.tex",
      "artifacts/_project/paper/table_1000step_comparison.tex",
      "artifacts/paper_tables/table_1000step_comparison.tex",
      "docs/paper/abstract.tex",
      "docs/paper/experiments.tex",
      "docs/paper/appendix.tex",
      "docs/paper/method.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "paper/abstract.tex",
      "paper/conclusion.tex",
      "paper/method.tex",
      "paper/introduction.tex",
      "paper/experiments.tex",
      "paper/appendix.tex"
    ],
    "durationMs": 53,
    "numFiles": 60,
    "truncated": false
  }
}
```

</details>

---


### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
The registry is too large to read directly. Let me:
1. Read the main paper TeX files from the `paper/` directory
2. Parse the registry with jq to extract key metrics

Let me read the paper files and parse the registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "b0eab10c-f0c2-464e-acfb-121cfa0994bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

Registry 数据量很大，需要用 subagent 处理。同时读取论文 TeX 主文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "a07312ac-f46e-4b49-9aa8-6fe802c8101e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

<details open><summary>🔧 Tool call — Agent · `toolu_012DcgU8HE673BrqdqER1VKV`</summary>

```json
{
  "description": "Extract registry metrics",
  "prompt": "Extract key experiment metrics from a large JSON registry file for a paper audit.\n\nThe file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt\n\nFormat: JSON with schema: {result: string} — the \"result\" field is itself a JSON string that needs parsing.\n\nI need you to extract ALL experiments with status=SUCCESS or conclusion containing \"success\" or \"negative\", and for each one report:\n- exp_id\n- status / conclusion\n- All metrics (PR, ISR, H7%, H1%, genuine%, etc.)\n- Any notes or decisions referenced\n\nUse jq or python to parse. Return a comprehensive table/list of all experiment metrics. Be thorough — I need every number that might appear in a paper.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "c4a60f45-a051-47c2-b021-99bbb6111035",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Extract registry metrics",
  "task_type": "local_agent",
  "prompt": "Extract key experiment metrics from a large JSON registry file for a paper audit.\n\nThe file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt\n\nFormat: JSON with schema: {result: string} — the \"result\" field is itself a JSON string that needs parsing.\n\nI need you to extract ALL experiments with status=SUCCESS or conclusion containing \"success\" or \"negative\", and for each one report:\n- exp_id\n- status / conclusion\n- All metrics (PR, ISR, H7%, H1%, genuine%, etc.)\n- Any notes or decisions referenced\n\nUse jq or python to parse. Return a comprehensive table/list of all experiment metrics. Be thorough — I need every number that might appear in a paper.",
  "uuid": "527abdc2-a4a2-4905-b12c-e925ffcd4a75",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


## Round 1

## Round 1

74 recorded events


### User

_source line 18 · 2026-05-15T15:56:59.788Z_

Extract key experiment metrics from a large JSON registry file for a paper audit.

The file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt

Format: JSON with schema: {result: string} — the "result" field is itself a JSON string that needs parsing.

I need you to extract ALL experiments with status=SUCCESS or conclusion containing "success" or "negative", and for each one report:
- exp_id
- status / conclusion
- All metrics (PR, ISR, H7%, H1%, genuine%, etc.)
- Any notes or decisions referenced

Use jq or python to parse. Return a comprehensive table/list of all experiment metrics. Be thorough — I need every number that might appear in a paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "95708553-63dc-4e41-82b9-f9dde84d831d"
}
```

</details>

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01MsPKB4hC2MQoAfrmnL36UX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "8c9273a3-8139-4730-be6a-a3ecee490479",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

_source line 20 · 2026-05-15T15:57:00.476Z_

<details><summary>↩ Tool result · `toolu_01MsPKB4hC2MQoAfrmnL36UX`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer: A Case Study with Qwen3-4B}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{limitations}
38	
39	\appendix
40	\input{appendix}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "fe29f26a-d329-4d02-83e4-a46e5df03b15",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\\usepackage{enumitem}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage[protrusion=true,expansion=false]{microtype}\n\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{6pt plus 2pt minus 2pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{2pt}\n\n\\graphicspath{{figures/}}\n\n\\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer: A Case Study with Qwen3-4B}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{limitations}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_019UcpzQLepUNRQu8iMhLLsA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "95e18e27-d817-4213-9d48-cdf373de0f0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

_source line 22 · 2026-05-15T15:57:00.925Z_

<details><summary>↩ Tool result · `toolu_019UcpzQLepUNRQu8iMhLLsA`</summary>

```text
1	\begin{abstract}
2	GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
4	The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
5	ISR is uncorrelated with downstream NLI accuracy ($\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.
6	As a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\to}0.003$ while PR rises $32\%{\to}96\%$; an SFT baseline reaches 92.2\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.
7	As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 69.7\% conclusion duplication (H7) versus 0\% under matched random; the sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
8	Cross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\% non-hacking.
9	Across 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "417197e8-4475-43d7-8adf-50fe9923fe0f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex",
      "content": "\\begin{abstract}\nGRPO-trained neurosymbolic formalizers achieve high prove rates---93\\% on FOLIO---yet 87\\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.\nWe introduce \\emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.\nThe fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.\nISR is uncorrelated with downstream NLI accuracy ($\\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.\nAs a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\\to}0.003$ while PR rises $32\\%{\\to}96\\%$; an SFT baseline reaches 92.2\\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.\nAs a reward, $r = r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ at $\\beta{=}0.1$ induces \\emph{meta-level Goodhart's Law}: 69.7\\% conclusion duplication (H7) versus 0\\% under matched random; the sole apparent ISR improvement reduces to $1.06\\times$ after controlling for a premise-count confound; $\\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\\pm}42\\%$; random: $54{\\pm}35\\%$), with individual seeds collapsing to as low as $18\\%$.\nCross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\\% non-hacking.\nAcross 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\\footnote{Code and data: \\url{[anonymized]}}\n\\end{abstract}\n",
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_017Kd9oMPFMtgk9LRYHvBiGy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "a2955e15-06f9-4c69-b215-0b40f8f2d94d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

_source line 24 · 2026-05-15T15:57:01.526Z_

<details><summary>↩ Tool result · `toolu_017Kd9oMPFMtgk9LRYHvBiGy`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\autoref{fig:sta-overview}).
16	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
17	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
18	ISR captures structural rather than semantic integrity (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
19	
20	\paragraph{ISR as diagnostic.}
21	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (99.5\% degradation) while PR rises $32\%{\to}96\%$.
22	Three seeds diverge radically (PR $\sigma{=}\pm47$\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.
23	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.2\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.
24	
25	\paragraph{Meta-level Goodhart.}
26	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition---\emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
27	At $\beta{=}0.1$, 69.7\% of proved samples exhibit single-premise-equals-conclusion duplication---ISR high \emph{by definition}---versus 0\% under matched random; the one seed with non-trivial residual reduces to $1.06\times$ random after controlling for a premise-count confound.
28	At $\beta{=}0.3$, both ISR and random produce extreme cross-seed instability (PR $66{\pm}42\%$ and $54{\pm}35\%$ respectively), confirming high-dose proxy weighting is harmful regardless of signal content; ISR seeds diverge into three distinct pathways (reward collapse, shortcut dominance, pure metric gaming) while random converges uniformly to H1.
29	The effect transfers and intensifies in Prolog: 3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming} that bypasses text-match classifiers.
30	ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer.}
31	
32	\paragraph{Contributions.}
33	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\S\ref{sec:diagnostic}); (\textbf{C2}) empirical meta-level Goodhart, with a random control isolating ISR-specific gaming (69.7\% vs.\ 0\%) and a premise-count-matched analysis showing the sole apparent gain is an LOO artifact (\S\ref{sec:goodhart}); (\textbf{C3}) cross-logic transfer to Prolog with universal Goodhart (\S\ref{sec:crosslogic}); (\textbf{C4}) an eight-mode hacking taxonomy including query-as-fact gaming and obfuscated tautology, motivating functional cross-validation of diagnostics (\S\ref{sec:taxonomy}).
34	These are cautionary results for any work treating a structural proxy as a training signal.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "24f2c3c2-38b6-4c0c-a1ce-93a438f38231",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on first-order logic problems---yet 87\\% of its proved outputs embed the conclusion verbatim among the premises.\nThe solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.\nThis structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.\n\n\\paragraph{The execution-only blind spot.}\nProve rate---the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic applying \\emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\\autoref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\nISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}\\pm47$\\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.2\\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.\n\n\\paragraph{Meta-level Goodhart.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR is gamed at its own definition---\\emph{meta-level Goodhart's Law}~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.\nAt $\\beta{=}0.1$, 69.7\\% of proved samples exhibit single-premise-equals-conclusion duplication---ISR high \\emph{by definition}---versus 0\\% under matched random; the one seed with non-trivial residual reduces to $1.06\\times$ random after controlling for a premise-count confound.\nAt $\\beta{=}0.3$, both ISR and random produce extreme cross-seed instability (PR $66{\\pm}42\\%$ and $54{\\pm}35\\%$ respectively), confirming high-dose proxy weighting is harmful regardless of signal content; ISR seeds diverge into three distinct pathways (reward collapse, shortcut dominance, pure metric gaming) while random converges uniformly to H1.\nThe effect transfers and intensifies in Prolog: 3/3 seeds yield 0\\% non-hacking via distinct mechanisms, including \\emph{query-as-fact gaming} that bypasses text-match classifiers.\nISR's asymmetry is the central finding: \\emph{reliable as observer, unreliable as optimizer.}\n\n\\paragraph{Contributions.}\nAcross 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) empirical meta-level Goodhart, with a random control isolating ISR-specific gaming (69.7\\% vs.\\ 0\\%) and a premise-count-matched analysis showing the sole apparent gain is an LOO artifact (\\S\\ref{sec:goodhart}); (\\textbf{C3}) cross-logic transfer to Prolog with universal Goodhart (\\S\\ref{sec:crosslogic}); (\\textbf{C4}) an eight-mode hacking taxonomy including query-as-fact gaming and obfuscated tautology, motivating functional cross-validation of diagnostics (\\S\\ref{sec:taxonomy}).\nThese are cautionary results for any work treating a structural proxy as a training signal.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01PVVogwRnKQVdhVnXXKV1nN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "408829ab-2c1c-4e67-b7e2-8cbeeb8f76fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

_source line 26 · 2026-05-15T15:57:01.891Z_

<details><summary>↩ Tool result · `toolu_01PVVogwRnKQVdhVnXXKV1nN`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
10	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
11	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.
12	
13	\subsection{ISR as Diagnostic}
14	\label{sec:diagnostic}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
19	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples have $\text{ISR}{=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
20	\label{fig:isr-collapse}
21	\end{figure}
22	
23	\textbf{Collapse trajectory.}
24	Figure~\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.
25	PR rises $32\%\to93\%\to96\%$, a trajectory execution-only evaluation would read as successful optimization; $\text{ISR}^*$ tells the opposite story, $0.642\to0.132\to0.003$ (214$\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
26	By 500 steps, 87.1\% of proved samples embed the conclusion (H1); by 1000 steps the embedding rate saturates at 100\% and mean component count more than doubles ($6.58\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.
27	Extended training, lacking a structural signal, \emph{worsens} formalization quality while improving the headline number.
28	
29	\textbf{Cross-seed instability.}
30	The three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\ref{app:detailed-results}): s42 reaches $\text{PR}{=}93\%$ via conclusion embedding ($\text{H1}{=}87\%$); s43 collapses to $\text{PR}{=}13\%$ via repetition (87\% of rollouts truncated); s44 reaches $\text{PR}{=}98\%$ via tautological collapse ($\text{H7}{=}100\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
31	The cross-seed PR variance ($\sigma{\pm}47$\,pp) shows aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).
32	
33	\textbf{SFT baseline.}
34	SFT on gold formalizations reaches $\text{PR}{=}13.0\%$ (3-seed pooled, 1000 steps) with $\text{H7}{=}0$, $\text{H1}{=}7.7\%$, $92.2\%$ non-hacking ($n{=}39$; per-seed range 91--93\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
35	The near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.
36	A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%), indicating reward hacking emerges early in RL training, not merely at high PR.
37	
38	\subsection{Meta-Level Goodhart's Law}
39	\label{sec:goodhart}
40	
41	We now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with a matched random control, $r = r_{\text{exec}}\cdot(1 + \beta\,u)$, $u\sim\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.
42	The headline finding: ISR-as-reward produces \emph{meta-level} Goodhart~\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.
43	
44	\begin{table}[t]
45	\centering
46	\small
47	\resizebox{\columnwidth}{!}{%
48	\begin{tabular}{lcccccc}
49	\toprule
50	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} \\
51	\midrule
52	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
53	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
54	\midrule
55	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)
56	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{70}$^\P$ & 18 & 7 \\ %% registry: plan002-additive-b01-s42/s43/s44 (pooled, H8+FN corrected)
57	Random & 0.1 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.04} & 0 & 81 & 18 \\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44
58	\midrule
59	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 14 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)
60	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 4 & 95 & 1 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled)
61	\bottomrule
62	\end{tabular}}
63	\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}.}
64	\label{tab:goodhart-landscape}
65	\end{table}
66	
67	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-specific gaming.}
68	The most striking number is H7: 69.7\% of proved samples under ISR ($n{=}161/231$) vs.\ \emph{zero} under random ($0/256$). %% registry: plan002 vs plan018 all seeds
69	H7---a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction (\S\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.
70	Total conclusion embedding ($\text{H1}+\text{H7}$) is GRPO-universal at $68$--$97\%$ across both conditions, and is in fact \emph{higher} under random (pooled H1 81\% vs.\ 18\% under ISR).
71	ISR does not reduce hacking; it converts H1 into H7 (Figure~\ref{fig:hacking-composition}).
72	Random also yields higher and more stable PR ($85{\pm}6\%$ vs.\ $77{\pm}14\%$).
73	
74	\textbf{Premise-count confound.}
75	The one ISR seed not dominated by H7 (s42) has raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ its random control ($0.131$), suggesting genuine improvement.
76	This appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\text{ISR}\geq 0.5$ by definition.
77	Restricting to non-hacking samples with $\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\text{ISR}^{*}{=}0.258$ for ISR vs.\ $0.243$ for random: a $1.06\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis
78	After reclassifying premise-subset gaming (H8; Appendix~\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\ref{app:h8}), ISR $\beta{=}0.1$ genuine rate is \emph{significantly lower} than random ($6.9\%$ vs.\ $18.4\%$; Fisher $p{=}0.0002$, two-sided; $n{=}231$ vs.\ $256$; Appendix Table~\ref{tab:bootstrap-ci}).
79	Even a conservative correction (H8 reclassification only, no FN fix) yields $p{=}0.060$---marginal but directionally consistent.
80	ISR-specific gaming modes (H7 + H8) crowd out genuine proofs: the structural signal provides no quality benefit and actively \emph{reduces} genuine output by creating optimization targets that are easier to satisfy than real derivations.
81	The raw $3.2\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification
82	
83	\textbf{Temporal collapse under ISR $\beta{=}0.1$.}
84	Extended training (1000 steps) reveals that ISR $\beta{=}0.1$'s genuine rate at 500 steps ($17.3\%$, seed~42) is transient: by step 1000, H7 gaming escalates from $16.0\%$ to $96.7\%$ while genuine rate collapses to $1.1\%$ ($n_{\text{comp}}$: $5.58{\to}2.89$).
85	The optimization converges to a fixed point where $\text{ISR}^{*}{=}0.88$, superficially suggesting structural improvement but reflecting near-complete tautological gaming.
86	This mirrors the exec-only 1000-step trajectory (\S\ref{sec:diagnostic}): both converge to ${\sim}0\%$ genuine proofs despite opposite ISR values ($0.88$ vs.\ $0.003$), demonstrating that ISR is gamed upward under ISR-as-reward and downward under exec-only---two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
87	
88	\textbf{High-dose ISR ($\beta{=}0.3$): multi-modal Goodhart.}
89	At $\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability ($\text{PR}{=}66{\pm}42\%$, spanning 18--95\%); each seed converges to a distinct pathway (Appendix~\ref{app:detailed-results}). %% registry: plan002-additive-b03-s42/s43/s44
90	Seed~42: \emph{reward collapse} ($\text{PR}{=}18\%$), the classical pattern of~\citep{gao-reward-overoptimization}.
91	Seed~43: \emph{H1 shortcutting} ($\text{PR}{=}86\%$, $\text{H1}{=}69\%$, only $27\%$ non-hacking).
92	Seed~44: \emph{pure H7 meta-Goodhart} ($\text{PR}{=}95\%$, $\text{H7}{=}100\%$, $\text{ISR}^{*}{=}0.742$, $0\%$ non-hacking)---simultaneously gaming \emph{both} execution and structural metrics through the same construction.
93	The random control at $\beta{=}0.3$ is equally unstable ($\text{PR}{=}54{\pm}35\%$, spanning 23--92\%) with near-universal H1 hacking ($96\%$) and ${\leq}3\%$ non-hacking per seed; high-dose proxy weighting destabilizes training regardless of signal source; ISR produces diverse failure modes (reward collapse, H1 shortcutting, H7 meta-Goodhart) while random converges to uniform H1 dominance (Appendix~\ref{app:beta03}).
94	
95	\subsection{Cross-Logic Diagnostic Transfer}
96	\label{sec:crosslogic}
97	
98	\begin{figure}[t]
99	\centering
100	\includegraphics[width=0.95\columnwidth]{figures/fig4_prolog_comparison.pdf}
101	\caption{Cross-logic results. \textbf{Left}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
102	\label{fig:prolog-comparison}
103	\end{figure}
104	
105	We replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce meta-level Goodhart?
106	Detailed per-seed numbers are in Appendix Table~\ref{tab:prolog-detailed}.
107	
108	\textbf{Prolog exec-only: ISR catches redundancy across logics.}
109	Two of three seeds (s42, s43) show $\text{ISR}^{*}{\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3
110	Inspection reveals \emph{redundant coding}: ground facts repeated multiple times (e.g., \texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.
111	This is a different failure semantics from FOL exec-only (conclusion embedding), but $\text{ISR}^{*}$ flags both.
112	We are careful to distinguish: exec-only \emph{low} ISR signals \emph{redundancy}; ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (\S\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.
113	
114	\textbf{Prolog ISR-as-reward: universal Goodhart.}
115	The Prolog result is stronger than FOL: 3/3 seeds reach $0\%$ non-hacking via three distinct mechanisms (Figure~\ref{fig:prolog-comparison}).
116	Seed~42: clean H7 tautologies ($\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42
117	Seed~43: \emph{degenerate uppercase pseudo-Prolog} (e.g., \texttt{MARY\_IS\_AN\_AVA\-DEOTE.}); strict text-match returns $\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\text{necessary}}{=}1$ (functionally H7). %% registry: plan006-prolog-sta-s43
118	Seed~44: \emph{query-as-fact gaming}---the model transforms the NL question into a snake-case atom asserted as both fact and query (e.g., \texttt{is\_the\_dog\_furry.} as both fact and query), with $95/97$ proved samples at $n_{\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44
119	Seed~44 evaded our initial strict classifier (reported $100\%$ genuine); functional cross-validation exposed it---a methodological lesson that text-match classifiers have blind spots and STA's necessity profile is the cross-check.
120	We attribute Prolog's stronger collapse to its simpler operational semantics: a broader gaming basin makes the genuine residual disappear---corroborating evidence for Claim 2.
121	
122	\subsection{Hacking Taxonomy}
123	\label{sec:taxonomy}
124	
125	\begin{figure}[t]
126	\centering
127	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
128	\caption{Hacking composition across reward conditions (proved samples; exec-only and SFT: seed~42; ISR and Random bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}
129	\label{fig:hacking-composition}
130	\end{figure}
131	
132	\begin{table}[t]
133	\centering
134	\small
135	\resizebox{\columnwidth}{!}{%
136	\begin{tabular}{lccccc}
137	\toprule
138	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
139	\midrule
140	H1 embed       & 87 & 18 & 81 & 7 & 0$^\sharp$ \\
141	H7 duplicate   & 0  & 70 & 0  & 0 & 100$^\sharp$ \\
142	H8 prem-subset & 6  & 5  & --- & 0 & --- \\
143	Tautological   & --- & --- & --- & --- & s42 \\
144	Repetition     & s43 & --- & --- & --- & --- \\
145	Contradiction  & 1k & --- & --- & --- & --- \\
146	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
147	Query-as-fact  & --- & --- & --- & --- & s44 \\
148	\midrule
149	\textbf{Non-hacking} & 8  & 7  & 18 & \textbf{92} & \textbf{0} \\
150	\bottomrule
151	\end{tabular}}
152	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}12$; s44 only). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
153	\label{tab:hacking-taxonomy}
154	\end{table}
155	
156	The eight modes (Table~\ref{tab:hacking-taxonomy}; full definitions in Appendix~\ref{app:hacking-modes}) span the studied conditions.
157	Three are quantifiable across conditions: \textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$97\%$ regardless of reward type; \textbf{H7} (conclusion duplication) is ISR-specific at $69.7\%$ combined vs.\ $0\%$ in random controls; \textbf{H8} (premise-subset gaming) appears under both exec-only ($6\%$) and ISR ($5\%$) conditions (Appendix~\ref{app:h8}).
158	H7 splits into \textbf{H7a} (standard, text-match detectable; $65\%$ of ISR proved) and \textbf{H7b} (obfuscated tautology; $5\%$): H7b samples use vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$) to evade the text-match classifier while remaining logically equivalent, with $10/12$ achieving $\text{ISR}{\approx}0.8$---simultaneously gaming execution reward, ISR metric, and hacking detector.
159	The remaining five appear in specific cells: tautological collapse (exec-only s44, Prolog ISR s42), repetition (exec-only s43), contradiction explosion (exec-only at 1000 steps), complexity-without-utility (random $\beta{=}0.1$ residual), and query-as-fact gaming (Prolog ISR s44).
160	
161	The cross-condition pattern is consistent with \S\ref{sec:goodhart}: \emph{reward formulation determines hacking composition but not hacking prevalence.}
162	Exec-only, ISR, and random conditions all show $\geq 80\%$ pooled hacking among proved samples; only SFT shows $92\%$ non-hacking.
163	Across 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is ISR $\beta{=}0.1$ s42 at $\text{PR}{=}81\%$, $17\%$ non-hacking, and even that residual is the premise-minimization artifact analyzed above.
164	Query-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\text{necessary}}$ distributions, suggesting the taxonomy is descriptive, not exhaustive.
165	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "6bc87f81-3e91-4f58-a53e-e79e6ea53963",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\\texttt{eval\\_sta.py}) so training-log ISR is never compared across runs.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory execution-only evaluation would read as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{\\pm}47$\\,pp) shows aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.2\\%$ non-hacking ($n{=}39$; per-seed range 91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.\nA 100-step RL checkpoint (Appendix~\\ref{app:100step}) at $\\text{PR}{=}32\\%$ already shows 31.2\\% hacking (vs.\\ SFT's 7.7\\%), indicating reward hacking emerges early in RL training, not merely at high PR.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nThe headline finding: ISR-as-reward produces \\emph{meta-level} Goodhart~\\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{70}$^\\P$ & 18 & 7 \\\\ %% registry: plan002-additive-b01-s42/s43/s44 (pooled, H8+FN corrected)\nRandom & 0.1 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.04} & 0 & 81 & 18 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 14 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 4 & 95 & 1 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled)\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}.}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nThe most striking number is H7: 69.7\\% of proved samples under ISR ($n{=}161/231$) vs.\\ \\emph{zero} under random ($0/256$). %% registry: plan002 vs plan018 all seeds\nH7---a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction (\\S\\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$97\\%$ across both conditions, and is in fact \\emph{higher} under random (pooled H1 81\\% vs.\\ 18\\% under ISR).\nISR does not reduce hacking; it converts H1 into H7 (Figure~\\ref{fig:hacking-composition}).\nRandom also yields higher and more stable PR ($85{\\pm}6\\%$ vs.\\ $77{\\pm}14\\%$).\n\n\\textbf{Premise-count confound.}\nThe one ISR seed not dominated by H7 (s42) has raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ its random control ($0.131$), suggesting genuine improvement.\nThis appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\\text{ISR}\\geq 0.5$ by definition.\nRestricting to non-hacking samples with $\\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\\text{ISR}^{*}{=}0.258$ for ISR vs.\\ $0.243$ for random: a $1.06\\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis\nAfter reclassifying premise-subset gaming (H8; Appendix~\\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\\ref{app:h8}), ISR $\\beta{=}0.1$ genuine rate is \\emph{significantly lower} than random ($6.9\\%$ vs.\\ $18.4\\%$; Fisher $p{=}0.0002$, two-sided; $n{=}231$ vs.\\ $256$; Appendix Table~\\ref{tab:bootstrap-ci}).\nEven a conservative correction (H8 reclassification only, no FN fix) yields $p{=}0.060$---marginal but directionally consistent.\nISR-specific gaming modes (H7 + H8) crowd out genuine proofs: the structural signal provides no quality benefit and actively \\emph{reduces} genuine output by creating optimization targets that are easier to satisfy than real derivations.\nThe raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification\n\n\\textbf{Temporal collapse under ISR $\\beta{=}0.1$.}\nExtended training (1000 steps) reveals that ISR $\\beta{=}0.1$'s genuine rate at 500 steps ($17.3\\%$, seed~42) is transient: by step 1000, H7 gaming escalates from $16.0\\%$ to $96.7\\%$ while genuine rate collapses to $1.1\\%$ ($n_{\\text{comp}}$: $5.58{\\to}2.89$).\nThe optimization converges to a fixed point where $\\text{ISR}^{*}{=}0.88$, superficially suggesting structural improvement but reflecting near-complete tautological gaming.\nThis mirrors the exec-only 1000-step trajectory (\\S\\ref{sec:diagnostic}): both converge to ${\\sim}0\\%$ genuine proofs despite opposite ISR values ($0.88$ vs.\\ $0.003$), demonstrating that ISR is gamed upward under ISR-as-reward and downward under exec-only---two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$, spanning 18--95\\%); each seed converges to a distinct pathway (Appendix~\\ref{app:detailed-results}). %% registry: plan002-additive-b03-s42/s43/s44\nSeed~42: \\emph{reward collapse} ($\\text{PR}{=}18\\%$), the classical pattern of~\\citep{gao-reward-overoptimization}.\nSeed~43: \\emph{H1 shortcutting} ($\\text{PR}{=}86\\%$, $\\text{H1}{=}69\\%$, only $27\\%$ non-hacking).\nSeed~44: \\emph{pure H7 meta-Goodhart} ($\\text{PR}{=}95\\%$, $\\text{H7}{=}100\\%$, $\\text{ISR}^{*}{=}0.742$, $0\\%$ non-hacking)---simultaneously gaming \\emph{both} execution and structural metrics through the same construction.\nThe random control at $\\beta{=}0.3$ is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$, spanning 23--92\\%) with near-universal H1 hacking ($96\\%$) and ${\\leq}3\\%$ non-hacking per seed; high-dose proxy weighting destabilizes training regardless of signal source; ISR produces diverse failure modes (reward collapse, H1 shortcutting, H7 meta-Goodhart) while random converges to uniform H1 dominance (Appendix~\\ref{app:beta03}).\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Left}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \\textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce meta-level Goodhart?\nDetailed per-seed numbers are in Appendix Table~\\ref{tab:prolog-detailed}.\n\n\\textbf{Prolog exec-only: ISR catches redundancy across logics.}\nTwo of three seeds (s42, s43) show $\\text{ISR}^{*}{\\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3\nInspection reveals \\emph{redundant coding}: ground facts repeated multiple times (e.g., \\texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.\nThis is a different failure semantics from FOL exec-only (conclusion embedding), but $\\text{ISR}^{*}$ flags both.\nWe are careful to distinguish: exec-only \\emph{low} ISR signals \\emph{redundancy}; ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming} (\\S\\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.\n\n\\textbf{Prolog ISR-as-reward: universal Goodhart.}\nThe Prolog result is stronger than FOL: 3/3 seeds reach $0\\%$ non-hacking via three distinct mechanisms (Figure~\\ref{fig:prolog-comparison}).\nSeed~42: clean H7 tautologies ($\\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42\nSeed~43: \\emph{degenerate uppercase pseudo-Prolog} (e.g., \\texttt{MARY\\_IS\\_AN\\_AVA\\-DEOTE.}); strict text-match returns $\\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\\text{necessary}}{=}1$ (functionally H7). %% registry: plan006-prolog-sta-s43\nSeed~44: \\emph{query-as-fact gaming}---the model transforms the NL question into a snake-case atom asserted as both fact and query (e.g., \\texttt{is\\_the\\_dog\\_furry.} as both fact and query), with $95/97$ proved samples at $n_{\\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44\nSeed~44 evaded our initial strict classifier (reported $100\\%$ genuine); functional cross-validation exposed it---a methodological lesson that text-match classifiers have blind spots and STA's necessity profile is the cross-check.\nWe attribute Prolog's stronger collapse to its simpler operational semantics: a broader gaming basin makes the genuine residual disappear---corroborating evidence for Claim 2.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only and SFT: seed~42; ISR and Random bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 81 & 7 & 0$^\\sharp$ \\\\\nH7 duplicate   & 0  & 70 & 0  & 0 & 100$^\\sharp$ \\\\\nH8 prem-subset & 6  & 5  & --- & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 7  & 18 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}12$; s44 only). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe eight modes (Table~\\ref{tab:hacking-taxonomy}; full definitions in Appendix~\\ref{app:hacking-modes}) span the studied conditions.\nThree are quantifiable across conditions: \\textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$97\\%$ regardless of reward type; \\textbf{H7} (conclusion duplication) is ISR-specific at $69.7\\%$ combined vs.\\ $0\\%$ in random controls; \\textbf{H8} (premise-subset gaming) appears under both exec-only ($6\\%$) and ISR ($5\\%$) conditions (Appendix~\\ref{app:h8}).\nH7 splits into \\textbf{H7a} (standard, text-match detectable; $65\\%$ of ISR proved) and \\textbf{H7b} (obfuscated tautology; $5\\%$): H7b samples use vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$) to evade the text-match classifier while remaining logically equivalent, with $10/12$ achieving $\\text{ISR}{\\approx}0.8$---simultaneously gaming execution reward, ISR metric, and hacking detector.\nThe remaining five appear in specific cells: tautological collapse (exec-only s44, Prolog ISR s42), repetition (exec-only s43), contradiction explosion (exec-only at 1000 steps), complexity-without-utility (random $\\beta{=}0.1$ residual), and query-as-fact gaming (Prolog ISR s44).\n\nThe cross-condition pattern is consistent with \\S\\ref{sec:goodhart}: \\emph{reward formulation determines hacking composition but not hacking prevalence.}\nExec-only, ISR, and random conditions all show $\\geq 80\\%$ pooled hacking among proved samples; only SFT shows $92\\%$ non-hacking.\nAcross 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is ISR $\\beta{=}0.1$ s42 at $\\text{PR}{=}81\\%$, $17\\%$ non-hacking, and even that residual is the premise-minimization artifact analyzed above.\nQuery-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\\text{necessary}}$ distributions, suggesting the taxonomy is descriptive, not exhaustive.\n",
      "numLines": 165,
      "startLine": 1,
      "totalLines": 165
    }
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01TbuSPwMWfvxbs1cTjeymhZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "1ec60e63-a08b-4f08-a38e-868737e6b30c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

_source line 28 · 2026-05-15T15:57:02.360Z_

<details><summary>↩ Tool result · `toolu_01TbuSPwMWfvxbs1cTjeymhZ`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (\autoref{fig:sta-overview}a).
15	We train with GRPO~\citep{deepseekmath} ($K{=}8$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (\autoref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation testing and feature attribution; our novelty is its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
27	
28	\begin{algorithm}[t]
29	\caption{Solver Trace Ablation (STA)}
30	\label{alg:sta}
31	\begin{algorithmic}[1]
32	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
33	\ENSURE $\text{ISR}(x) \in [0, 1]$
34	\STATE $\textit{necessary} \gets 0$
35	\FOR{$i = 1$ to $n$}
36	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
37	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
38	    \ENDIF
39	\ENDFOR
40	\RETURN $\textit{necessary} \,/\, n$
41	\end{algorithmic}
42	\end{algorithm}
43	
44	\paragraph{Intensional Structural Reward.}
45	ISR is the fraction of necessary components:
46	\begin{equation}
47	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
48	  \label{eq:isr}
49	\end{equation}
50	ISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.
51	We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.
52	
53	\paragraph{Limitations of ISR.}
54	ISR measures syntactic component necessity, not semantic faithfulness: a formalization can achieve $\text{ISR}{=}1$ while semantically unrelated to the NL input (e.g., a single premise identical to the conclusion).
55	ISR is also sensitive to component count $n$: when $n{=}2$, $\text{ISR}\geq 0.5$ regardless of proof quality.
56	We control for this confound via premise-count-matched analysis in \S\ref{sec:goodhart}.
57	The $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.
58	However, the $O(1)$ variant includes a tautology check (conclusion provable under empty premises $\to$ ISR${=}0$) absent from exec-only, introducing a training-time confound that depresses prove rate ($63\%$ vs.\ $93\%$ exec-only); the two conditions are therefore non-equivalent in training dynamics despite producing comparable ISR signals (Appendix~\ref{app:o1-ablation}).
59	
60	\subsection{Reward Conditions and Hacking Modes}
61	\label{sec:rewards}
62	\label{sec:taxonomy-method}
63	
64	We study six conditions: exec-only ($r_{\text{exec}}$), ISR low/high-dose ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and an SFT baseline (NLL on gold formalizations).
65	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
66	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
67	Each RL condition uses seeds $\{42,43,44\}$ and identical training data.
68	An earlier convex formulation ($\alpha r_{\text{exec}} + \beta r_{\text{exec}}\text{ISR}$, $\alpha{+}\beta{=}1$) was discarded because $\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\ref{app:setup}).
69	
70	\paragraph{Hacking taxonomy.}
71	Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}):
72	\textbf{H1} (conclusion embedded among multiple premises),
73	\textbf{H7} (single-premise conclusion duplication, subtypes H7a standard and H7b obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\text{ISR}\geq 0.5$),
74	\textbf{H8} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\ref{app:h8}),
75	\textbf{tautological collapse} (minimal two-component $P{\to}P$ without explicit ISR inflation),
76	\textbf{repetition collapse} (identical clauses repeated to inflate component count),
77	\textbf{complexity-without-utility} (elaborate but vacuous premises),
78	\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \emph{ex falso}), and
79	\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers).
80	Modes are identified by a two-stage procedure: strict normalized text matching (H1/H7) plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution (catches modes evading text matching).
81	We report both classifications in \S\ref{sec:experiments}.
82	
83	In interpreting ISR results we distinguish two failure semantics that share a numerical signature: an exec-only \emph{low} ISR signals \emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (H7-style constructions).
84	A bare ISR difference therefore does not translate directly into a reasoning-ability difference; the mode breakdown is what licenses such interpretation.
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "66938e8c-0e69-430f-83ae-66d91061646e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\n\\subsection{Task and GRPO Training}\n\\label{sec:task}\n\nGiven premises $P_1,\\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\\{c_1,\\ldots,c_n\\}$ verified by an external solver $S\\in\\{\\text{Prover9, SWI-Prolog}\\}$ (\\autoref{fig:sta-overview}a).\nWe train with GRPO~\\citep{deepseekmath} ($K{=}8$), where each rollout receives binary execution reward $r_{\\text{exec}}(x) = \\mathbf{1}[S(F_x){=}\\textit{proved}]$.\nThis optimizes prove rate but provides no signal about \\emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.\nAll experiments draw from FOLIO~\\citep{folio}; the held-out evaluation file retains a legacy \\texttt{proofwriter\\_fol\\_*.jsonl} filename (from ProofWriter~\\citep{proofwriter}) but contains only FOLIO-derived examples.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\nSTA tests whether each component of a proved formalization is individually necessary for proof success (\\autoref{fig:sta-overview}b).\nGiven a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\\setminus\\{c_i\\}$ and re-runs the solver (Algorithm~\\ref{alg:sta}).\nA component is \\emph{necessary} if its removal causes proof failure.\nWhat constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.\nLOO ablation itself is standard in mutation testing and feature attribution; our novelty is its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Proved formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE $\\text{ISR}(x) \\in [0, 1]$\n\\STATE $\\textit{necessary} \\gets 0$\n\\FOR{$i = 1$ to $n$}\n    \\IF{$S(x \\setminus \\{c_i\\}) = \\textit{failed}$}\n        \\STATE $\\textit{necessary} \\gets \\textit{necessary} + 1$\n    \\ENDIF\n\\ENDFOR\n\\RETURN $\\textit{necessary} \\,/\\, n$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Intensional Structural Reward.}\nISR is the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n}\\sum_{i=1}^{n}\\mathbf{1}\\bigl[S(x\\setminus\\{c_i\\})=\\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.\nWe report \\emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.\n\n\\paragraph{Limitations of ISR.}\nISR measures syntactic component necessity, not semantic faithfulness: a formalization can achieve $\\text{ISR}{=}1$ while semantically unrelated to the NL input (e.g., a single premise identical to the conclusion).\nISR is also sensitive to component count $n$: when $n{=}2$, $\\text{ISR}\\geq 0.5$ regardless of proof quality.\nWe control for this confound via premise-count-matched analysis in \\S\\ref{sec:goodhart}.\nThe $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.\nHowever, the $O(1)$ variant includes a tautology check (conclusion provable under empty premises $\\to$ ISR${=}0$) absent from exec-only, introducing a training-time confound that depresses prove rate ($63\\%$ vs.\\ $93\\%$ exec-only); the two conditions are therefore non-equivalent in training dynamics despite producing comparable ISR signals (Appendix~\\ref{app:o1-ablation}).\n\n\\subsection{Reward Conditions and Hacking Modes}\n\\label{sec:rewards}\n\\label{sec:taxonomy-method}\n\nWe study six conditions: exec-only ($r_{\\text{exec}}$), ISR low/high-dose ($r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ at $\\beta\\in\\{0.1,0.3\\}$), matched random controls ($r_{\\text{exec}}\\cdot(1{+}\\beta u)$, $u\\sim\\mathcal{U}(0,1)$), and an SFT baseline (NLL on gold formalizations).\nMultiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.\nRandom isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.\nEach RL condition uses seeds $\\{42,43,44\\}$ and identical training data.\nAn earlier convex formulation ($\\alpha r_{\\text{exec}} + \\beta r_{\\text{exec}}\\text{ISR}$, $\\alpha{+}\\beta{=}1$) was discarded because $\\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\\ref{app:setup}).\n\n\\paragraph{Hacking taxonomy.}\nAcross conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\\ref{app:hacking-modes}):\n\\textbf{H1} (conclusion embedded among multiple premises),\n\\textbf{H7} (single-premise conclusion duplication, subtypes H7a standard and H7b obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\\text{ISR}\\geq 0.5$),\n\\textbf{H8} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\\ref{app:h8}),\n\\textbf{tautological collapse} (minimal two-component $P{\\to}P$ without explicit ISR inflation),\n\\textbf{repetition collapse} (identical clauses repeated to inflate component count),\n\\textbf{complexity-without-utility} (elaborate but vacuous premises),\n\\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \\emph{ex falso}), and\n\\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers).\nModes are identified by a two-stage procedure: strict normalized text matching (H1/H7) plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution (catches modes evading text matching).\nWe report both classifications in \\S\\ref{sec:experiments}.\n\nIn interpreting ISR results we distinguish two failure semantics that share a numerical signature: an exec-only \\emph{low} ISR signals \\emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming} (H7-style constructions).\nA bare ISR difference therefore does not translate directly into a reasoning-ability difference; the mode breakdown is what licenses such interpretation.\n",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 85
    }
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01JBxxMggoAKxF3AYM3QqWb5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "2bdfcc49-f606-48ad-8027-c278af3e9f67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

_source line 30 · 2026-05-15T15:57:02.835Z_

<details><summary>↩ Tool result · `toolu_01JBxxMggoAKxF3AYM3QqWb5`</summary>

```text
1	\section{Discussion and Conclusion}
2	
3	Solver Trace Ablation (STA) exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides; an SFT baseline with 92.2\% non-hacking (3-seed pooled) localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
4	Repurposed as a training signal, ISR induces meta-level Goodhart's Law: the diagnostic for gaming becomes itself the target of gaming.
5	At $\beta{=}0.1$, conclusion duplication exploits the LOO definition (69.7\% vs.\ 0\% under matched random), and the sole apparent ISR gain reduces to $1.06\times$ random once a premise-count confound is controlled; at $\beta{=}0.3$, cross-seed instability is extreme ($\text{PR}{=}66{\pm}42\%$, random $54{\pm}35\%$), each seed converging to a distinct failure mode.
6	The pattern transfers to Prolog, where ISR-as-reward yields universal gaming (3/3 seeds, 0\% non-hacking) via three distinct mechanisms including query-as-fact gaming, which bypasses text-match classifiers (\S\ref{sec:taxonomy}).
7	ISR semantics depend on objective: exec-only \emph{low} ISR signals redundancy; ISR-rewarded \emph{high} ISR signals metric gaming.
8	
9	\paragraph{Classifier blind spots and functional cross-validation.}
10	H7b (obfuscated tautology) demonstrates that text-match classifiers have systematic blind spots: the model learns vacuous quantifier wrapping to disguise tautologies, evading detection while simultaneously gaming ISR ($10/12$ samples at $\text{ISR}{\approx}0.8$).
11	This triple gaming---execution reward, structural metric, and diagnostic classifier---is the most complete meta-Goodhart case we observe.
12	Query-as-fact gaming in Prolog (\S\ref{sec:crosslogic}) independently confirms the blind spot: our strict classifier reported $100\%$ genuine before functional LOO analysis revealed $97.9\%$ tautological.
13	Both cases argue for mandatory functional cross-validation of any text-based hacking classifier.
14	
15	\paragraph{H7 dose-response gradient.}
16	H7 tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $0\%$ H7 ($0/256$), random $\beta{=}0.3$ yields 4--7 H7a samples per seed, and ISR $\beta{=}0.1$ reaches $69.7\%$ ($161/231$).
17	The gradient suggests H7 is primarily ISR-induced but not ISR-exclusive: high-variance reward bonuses at $\beta{=}0.3$ can induce low-frequency H7 even without ISR signal, while ISR at any dose amplifies it by orders of magnitude.
18	
19	The asymmetry---reliable observer, unreliable optimizer---may generalize to other perturbation-based diagnostics; ISR and structurally similar metrics should be used as post-hoc evaluation, with future work targeting gaming-robust rewards and broader logic types.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "67038f20-fabf-477d-9236-3fc0a6a0aa30",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\nSolver Trace Ablation (STA) exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\\% collapse under exec-only GRPO that PR hides; an SFT baseline with 92.2\\% non-hacking (3-seed pooled) localizes the failure to RL optimization (\\S\\ref{sec:diagnostic}).\nRepurposed as a training signal, ISR induces meta-level Goodhart's Law: the diagnostic for gaming becomes itself the target of gaming.\nAt $\\beta{=}0.1$, conclusion duplication exploits the LOO definition (69.7\\% vs.\\ 0\\% under matched random), and the sole apparent ISR gain reduces to $1.06\\times$ random once a premise-count confound is controlled; at $\\beta{=}0.3$, cross-seed instability is extreme ($\\text{PR}{=}66{\\pm}42\\%$, random $54{\\pm}35\\%$), each seed converging to a distinct failure mode.\nThe pattern transfers to Prolog, where ISR-as-reward yields universal gaming (3/3 seeds, 0\\% non-hacking) via three distinct mechanisms including query-as-fact gaming, which bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\nISR semantics depend on objective: exec-only \\emph{low} ISR signals redundancy; ISR-rewarded \\emph{high} ISR signals metric gaming.\n\n\\paragraph{Classifier blind spots and functional cross-validation.}\nH7b (obfuscated tautology) demonstrates that text-match classifiers have systematic blind spots: the model learns vacuous quantifier wrapping to disguise tautologies, evading detection while simultaneously gaming ISR ($10/12$ samples at $\\text{ISR}{\\approx}0.8$).\nThis triple gaming---execution reward, structural metric, and diagnostic classifier---is the most complete meta-Goodhart case we observe.\nQuery-as-fact gaming in Prolog (\\S\\ref{sec:crosslogic}) independently confirms the blind spot: our strict classifier reported $100\\%$ genuine before functional LOO analysis revealed $97.9\\%$ tautological.\nBoth cases argue for mandatory functional cross-validation of any text-based hacking classifier.\n\n\\paragraph{H7 dose-response gradient.}\nH7 tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $0\\%$ H7 ($0/256$), random $\\beta{=}0.3$ yields 4--7 H7a samples per seed, and ISR $\\beta{=}0.1$ reaches $69.7\\%$ ($161/231$).\nThe gradient suggests H7 is primarily ISR-induced but not ISR-exclusive: high-variance reward bonuses at $\\beta{=}0.3$ can induce low-frequency H7 even without ISR signal, while ISR at any dose amplifies it by orders of magnitude.\n\nThe asymmetry---reliable observer, unreliable optimizer---may generalize to other perturbation-based diagnostics; ISR and structurally similar metrics should be used as post-hoc evaluation, with future work targeting gaming-robust rewards and broader logic types.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_013zfNx6yfMD9CTmLfP2Q356`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "633ebc07-3f91-4501-b293-e9a6dbfc0d9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt",
  "usage": {
    "total_tokens": 14330,
    "tool_uses": 1,
    "duration_ms": 3610
  },
  "last_tool_name": "Read",
  "uuid": "f2c122aa-d327-4753-956a-9194aef734a3",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01NTqvmKGisuskasWqh3Yeh7`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "3c747bb5-6a39-44f6-9eed-b74d094ead3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tm4waBoL5BaQNrNW5YyLDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14323,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14323,
        "ephemeral_1h_input_tokens": 0
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

_source line 34 · 2026-05-15T15:57:03.292Z_

<details><summary>↩ Tool result · `toolu_013zfNx6yfMD9CTmLfP2Q356`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
6	Three seeds demonstrate qualitative divergence but limit statistical power.
7	STA requires solvers supporting component-level input manipulation.
8	
9	\paragraph{Data scale.}
10	Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
11	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
12	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "8774f07e-270e-45a0-a890-7a575dc9fe6a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.\nISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\nThree seeds demonstrate qualitative divergence but limit statistical power.\nSTA requires solvers supporting component-level input manipulation.\n\n\\paragraph{Data scale.}\nOur experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\\citep{folio}.\nThe training subset is selected via stratified sampling (seed 42) and held constant across all conditions.\nWhile our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---


### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01SoYJ3CvEwjLR9aN2caGqCc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "bdf96118-5353-47b1-804e-146f833a76ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

_source line 36 · 2026-05-15T15:57:04.078Z_

<details><summary>↩ Tool result · reported error · `toolu_01NTqvmKGisuskasWqh3Yeh7`</summary>

```text
File content (81945 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "3ceb2539-6de5-4eb1-8ef8-19bdb70a46b1",
  "tool_use_result": "Error: File content (81945 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-15T15:57:03.770Z_

<details><summary>↩ Tool result · `toolu_01SoYJ3CvEwjLR9aN2caGqCc`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning and process rewards.}
5	LLM-solver pipelines~\cite{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\cite{mellgren-prolog-grpo, logic-rl} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	Learned PRMs~\cite{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\cite{processbench}; ISR is solver-grounded and annotation-free.
7	We use FOLIO~\cite{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Reward hacking and Goodhart's Law.}
10	Goodhart's Law is established theoretically~\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\cite{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
11	Recent work further documents spurious reward signals in RLVR~\cite{spurious-rewards} and reward hacking in frontier models~\cite{metr-reward-hacking}.
12	Our setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \emph{emerges during RL training} rather than at inference time; and the effect operates at a \emph{meta} level---the diagnostic for gaming itself becomes gamed when optimized---a phenomenon, to our knowledge, not previously documented.
13	
14	\paragraph{Mutation testing.}
15	STA adapts the LOO mutation paradigm~\cite{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "e963a99d-b78e-4523-b757-1b53485c888c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning and process rewards.}\nLLM-solver pipelines~\\cite{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\cite{mellgren-prolog-grpo, logic-rl} evaluate execution accuracy alone, with no diagnostic for structural quality.\nLearned PRMs~\\cite{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\\cite{processbench}; ISR is solver-grounded and annotation-free.\nWe use FOLIO~\\cite{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\\cite{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.\nRecent work further documents spurious reward signals in RLVR~\\cite{spurious-rewards} and reward hacking in frontier models~\\cite{metr-reward-hacking}.\nOur setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \\emph{emerges during RL training} rather than at inference time; and the effect operates at a \\emph{meta} level---the diagnostic for gaming itself becomes gamed when optimized---a phenomenon, to our knowledge, not previously documented.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\cite{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
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

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01H5LHHoXNQv8WNsPcq3Gp6J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "64e8f679-ab55-4a09-8f61-d425f3b9594d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcwbNafrbPmRm9Jy26r34R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15243,
      "cache_read_input_tokens": 26713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15243
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

_source line 39 · 2026-05-15T15:57:04.661Z_

<details><summary>↩ Tool result · `toolu_01H5LHHoXNQv8WNsPcq3Gp6J`</summary>

```text
1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 8 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
55	
56	
57	\section{STA Algorithm}
58	\label{app:algorithm}
59	
60	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
61	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
62	
63	
64	\section{Extended Discussion}
65	\label{app:extended-discussion}
66	
67	\paragraph{What ISR measures---and what it does not.}
68	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
69	This is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.
70	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
71	ISR and downstream task performance are uncorrelated.
72	ISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
73	
74	Critically, low ISR carries different semantics depending on the training objective.
75	Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\S\ref{sec:crosslogic}).
76	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
77	ISR values must always be interpreted relative to the optimization objective that produced them.
78	
79	\paragraph{The premise-count confound.}
80	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
81	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.
82	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
83	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
84	This bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
85	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
86	
87	\begin{table}[h]
88	\centering
89	\caption{Fisher exact tests for genuine rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ genuine rate is corrected for H8 reclassification and H7 false negatives (Appendix~\ref{app:h8}).}
90	\label{tab:bootstrap-ci}
91	\small
92	\begin{tabular}{@{}lcccc@{}}
93	\toprule
94	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
95	\midrule
96	\multicolumn{5}{@{}l}{\textit{Genuine rate (H8+FN corrected)}} \\
97	ISR vs.\ Random & 6.9\% {\scriptsize[4.3,11.0]} & 18.4\% {\scriptsize[14.0,23.7]} & 0.33 & 0.0002 \\
98	ISR vs.\ Exec-only & 6.9\% & 7.5\% & 0.91 & 0.81 \\
99	Random vs.\ Exec-only & 18.4\% & 7.5\% & 2.76 & 0.012 \\
100	\midrule
101	\multicolumn{5}{@{}l}{\textit{Genuine rate (H8-only, conservative)}} \\
102	ISR vs.\ Random & 12.1\% & 18.4\% & 0.61 & 0.060 \\
103	\midrule
104	\multicolumn{5}{@{}l}{\textit{H7 gaming rate}} \\
105	ISR vs.\ Random & 69.7\% & 0\% & $\infty$ & ${<}0.001$ \\
106	\midrule
107	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only genuine rate}} \\
108	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
109	\bottomrule
110	\end{tabular}
111	\\[2pt]
112	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}256$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
113	\end{table}
114	
115	\paragraph{Meta-level Goodhart: implications.}
116	The meta-Goodhart finding extends beyond this specific system.
117	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.
118	The dose-response pattern ($\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.3$: PR collapse to 18\% vs.\ 48\% random) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.
119	$\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.
120	The practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.
121	
122	\paragraph{Single-seed unreliability.}
123	The three exec-only seeds diverge radically (PR $\sigma{=}\pm 47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
124	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
125	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
126	
127	
128	\section{Hacking Mode Definitions}
129	\label{app:hacking-modes}
130	
131	We identify eight distinct reward hacking modes across all experiments.
132	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
133	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
134	
135	\begin{table}[h]
136	\centering
137	\small
138	\resizebox{\columnwidth}{!}{%
139	\begin{tabular}{@{}llcccc@{}}
140	\toprule
141	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
142	\midrule
143	H1 & Concl.\ in premises & 87 & 18 & 81 & 7 \\
144	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{70} & 0 & 0 \\
145	H8 & Premise-subset gaming & 6 & 5 & -- & 0 \\
146	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
147	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
148	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
149	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
150	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
151	\bottomrule
152	\end{tabular}}
153	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}12$; s44 only). Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
154	\label{tab:hacking-taxonomy-app}
155	\end{table}
156	
157	\paragraph{Classifier Validation.}
158	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
159	H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
160	No training data or manual annotation is used for classification.
161	
162	To estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
163	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
164	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
165	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
166	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
167	
168	\subsection{H8 --- Premise-Subset Gaming}
169	\label{app:h8}
170	
171	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).
172	We term this \textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
173	
174	\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
175	Automated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.
176	
177	\paragraph{Audit scope and limitations.}
178	Full H8 audit was completed for ISR $\beta{=}0.1$ seed~42 only.
179	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their genuine rates may be overestimated.
180	Random $\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.
181	
182	\paragraph{H7 false-negative correction (H7b obfuscated tautology).}
183	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as genuine by the text matcher.
184	Manual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
185	We classify these as \textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.
186	$10/12$ achieve $\text{ISR}{\approx}0.8$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\S\ref{sec:taxonomy}).
187	After correction, ISR s44 genuine${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.
188	
189	\paragraph{Impact on genuine-rate comparison.}
190	Under the primary correction (H8 + FN): ISR genuine $= 16/231 = 6.9\%$ vs.\ random genuine $= 47/256 = 18.4\%$ (Fisher $p{=}0.0002$).
191	Under conservative correction (H8 only, no FN fix): ISR genuine $= 28/231 = 12.1\%$ vs.\ $18.4\%$ (Fisher $p{=}0.060$).
192	Both scenarios are directionally consistent: ISR-specific gaming modes reduce genuine output relative to a matched control.
193	
194	\subsection{H1 --- Conclusion Embedding}
195	
196	\paragraph{Definition.}
197	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
198	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
199	
200	\paragraph{Example (FOL).}
201	{\small\begin{verbatim}
202	Premises:
203	  all x (bird(x) -> flies(x)).
204	  bird(tweety).
205	  flies(tweety).  % conclusion embedded
206	Conclusion: flies(tweety).
207	\end{verbatim}}
208	
209	\paragraph{ISR interaction.}
210	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
211	ISR does not distinguish trivial from substantive necessity.
212	
213	\paragraph{Prevalence.}
214	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\% across all RL conditions.
215	Under exec-only and Random reward, it manifests as H1 (71--93\%); under ISR reward, it shifts to H7 (69.7\% pooled).
216	
217	
218	\subsection{H7a --- Conclusion Duplication (Standard)}
219	
220	\paragraph{Definition.}
221	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
222	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
223	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
224	
225	\paragraph{Example (FOL).}
226	{\small\begin{verbatim}
227	Premises:
228	  all x ((A(x)&B(x))->(C(x)|D(x))).
229	Conclusion:
230	  all x ((A(x)&B(x))->(C(x)|D(x))).
231	\end{verbatim}}
232	
233	\paragraph{ISR interaction.}
234	ISR~$\approx 0.8$--$1.0$.
235	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
236	H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.
237	
238	\paragraph{Prevalence.}
239	H7a (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
240	Combined H7 (H7a + H7b): 69.7\% (161/231; includes s44 FN correction).
241	\textbf{Zero} occurrences under Random~$\beta{=}0.1$ across all three seeds ($0/256$).
242	
243	
244	\subsection{H7b --- Obfuscated Tautology}
245	
246	\paragraph{Definition.}
247	A single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.
248	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
249	
250	\paragraph{Example (FOL, vacuous quantifier wrapping).}
251	{\small\begin{verbatim}
252	Premises:
253	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
254	Conclusion:
255	  all x ((A(x)&B(x))->(C(x)|D(x))).
256	\end{verbatim}}
257	The premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.
258	
259	\paragraph{ISR interaction.}
260	ISR~$\approx 0.8$ ($10/12$ samples).
261	H7b simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).
262	This triple gaming makes H7b the most complete meta-Goodhart case we observe.
263	
264	\paragraph{Prevalence.}
265	Found exclusively in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as genuine).
266	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
267	
268	
269	\subsection{Tautological Collapse}
270	
271	\paragraph{Definition.}
272	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
273	
274	\paragraph{Example (FOL).}
275	\begin{verbatim}
276	Premises: p(a).
277	Conclusion: p(a).
278	\end{verbatim}
279	
280	\paragraph{ISR interaction.}
281	ISR~$=1.0$ (the sole premise is necessary).
282	Distinguished from H7 by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
283	
284	\paragraph{Prevalence.}
285	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
286	Also observed in Prolog exec+STA seed~42 (100\% H7, PR~$=0.50$).
287	
288	
289	\subsection{Repetition Collapse}
290	
291	\paragraph{Definition.}
292	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
293	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
294	
295	\paragraph{Example (Prolog).}
296	\begin{verbatim}
297	penguin(fido).
298	penguin(fido).
299	penguin(fido).
300	... (repeated to 512 tokens)
301	query(penguin(fido)).
302	\end{verbatim}
303	
304	\paragraph{ISR interaction.}
305	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
306	ISR correctly diagnoses this degeneration.
307	
308	\paragraph{Prevalence.}
309	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
310	
311	
312	\subsection{Complexity-without-Utility}
313	
314	\paragraph{Definition.}
315	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.
316	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
317	
318	\paragraph{Example (FOL).}
319	{\small\begin{verbatim}
320	Premises:
321	  all x all y (R(x,y) ->
322	    exists z (S(x,z) & T(z,y))).
323	  all x (P(x) -> Q(x)).
324	  P(a).            % only this needed
325	Conclusion: Q(a).
326	\end{verbatim}}
327	
328	\paragraph{ISR interaction.}
329	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
330	This is the mode ISR is best calibrated for.
331	
332	\paragraph{Prevalence.}
333	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
334	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
335	
336	
337	\subsection{Contradiction Explosion}
338	
339	\paragraph{Definition.}
340	The component count grows unboundedly over training.
341	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
342	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
343	
344	\paragraph{Example (FOL, 1000-step exec-only).}
345	{\small\begin{verbatim}
346	Premises:
347	  c1. c2. c3. ... c18. % 18.55 mean
348	  % conclusion embedded among premises
349	Conclusion: Q(a).
350	\end{verbatim}}
351	
352	\paragraph{ISR interaction.}
353	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
354	
355	\paragraph{Prevalence.}
356	Observed in extended exec-only training (seed~42, 1000 steps).
357	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
358	
359	
360	\subsection{Query-as-Fact Gaming}
361	
362	\paragraph{Definition.}
363	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
364	Prolog trivially proves the query by unifying with the fact.
365	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
366	
367	\paragraph{Example (Prolog).}
368	\begin{verbatim}
369	% NL: "Fido is happy."
370	% Model output:
371	fido_is_happy.
372	:- fido_is_happy.     % query = fact
373	\end{verbatim}
374	
375	\paragraph{ISR interaction.}
376	ISR~$\approx 0.9$--$1.0$.
377	The fact is necessarily necessary (its removal breaks the query), inflating ISR.
378	Functionally equivalent to H7 but with a distinct surface mechanism.
379	
380	\paragraph{Prevalence.}
381	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
382	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
383	
384	
385	\section{Per-Seed Detailed Results}
386	\label{app:detailed-results}
387	
388	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
389	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
390	ISR values are proved-only ISR$^*$.
391	
392	\begin{table*}[t]
393	\centering
394	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$).}
395	\label{tab:fol-detailed}
396	\label{tab:fol-beta01-detailed}
397	\footnotesize
398	\setlength{\tabcolsep}{3pt}
399	\begin{tabular}{@{}llccccccl@{}}
400	\toprule
401	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
402	\midrule
403	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
404	Base model (no training)
405	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
406	Ground-truth FOL
407	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
408	SFT
409	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
410	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
411	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
412	\cmidrule(l){2-9}
413	  & \multicolumn{2}{l}{3-seed pooled} & \makebox[0pt][l]{$0.130$} & & \makebox[0pt][l]{$0.595$} & & \makebox[0pt][l]{\textbf{92.3}} & $n{=}39$ proved \\
414	\midrule
415	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
416	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
417	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\% \\
418	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
419	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
420	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
421	\cmidrule(l){2-9}
422	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step only \\
423	\midrule
424	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
425	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed H1+H7+H8 \\
426	  & 43 & 500 & 0.61 & 0.830 & \textbf{96.7} & 0 & ${\sim}$3 & H7 dominant \\
427	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\
428	\cmidrule(l){2-9}
429	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
430	\midrule
431	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
432	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\
433	\midrule
434	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
435	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\
436	  & 43 & 500 & 0.88 & 0.058 & 0 & 93.2 & 6.8 & \\
437	  & 44 & 500 & 0.89 & 0.070 & 0 & 79.8 & 20.2 & \\
438	\cmidrule(l){2-9}
439	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.85{\pm}0.06$} & & \makebox[0pt][l]{$0.086{\pm}0.039$} & & & H7 = 0\% all seeds \\
440	\midrule
441	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
442	  & 42 & 500 & 0.48 & 0.094 & 0 & 100 & 0 & $n_{\text{comp}} = 9.6$ \\
443	\bottomrule
444	\end{tabular}
445	\end{table*}
446	
447	
448	\begin{table*}[t]
449	\centering
450	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
451	\label{tab:prolog-detailed}
452	\small
453	\begin{tabular}{@{}llcccccl@{}}
454	\toprule
455	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
456	\midrule
457	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
458	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
459	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
460	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
461	\cmidrule(l){2-8}
462	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
463	\midrule
464	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
465	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
466	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
467	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
468	\cmidrule(l){2-8}
469	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.699{\pm}0.45$} & & 3/3 Goodhart, 0\% non-hacking \\
470	\bottomrule
471	\end{tabular}
472	
473	\vspace{4pt}
474	{\footnotesize
475	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
476	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\
477	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
478	}
479	\end{table*}
480	
481	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
482	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
483	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
484	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
485	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
486	
487	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
488	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
489	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
490	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
491	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
492	The diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
493	
494	\subsection{Per-Seed Results at $\beta{=}0.3$}
495	\label{app:beta03}
496	
497	Table~\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\beta{=}0.3$.
498	The three ISR seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
499	
500	\begin{table}[h]
501	\centering
502	\caption{Per-seed results at $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}
503	\label{tab:beta03-detailed}
504	\small
505	\begin{tabular}{@{}llcccccl@{}}
506	\toprule
507	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Mode} \\
508	\midrule
509	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
510	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 22.2 & Reward collapse ($n{=}18$) \\
511	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 26.7 & H1 shortcutting \\
512	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure H7 meta-Goodhart \\
513	\cmidrule(l){2-8}
514	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.66{\pm}0.42$} & & \makebox[0pt][l]{$0.39{\pm}0.31$} & & \\
515	\midrule
516	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
517	  & 42 & 0.48 & 0.094 & 0 & 100 & 0 & \\
518	  & 43 & 0.92 & 0.180 & 7.6 & 90.2 & 2.2 & \\
519	  & 44 & 0.23 & 0 & 0 & 100 & 0 & \\
520	\cmidrule(l){2-8}
521	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & \\
522	\bottomrule
523	\end{tabular}
524	\end{table}
525	
526	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
527	\label{app:100step}
528	
529	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%---higher than SFT (13.0\%, 3-seed pooled) but still early in training.
530	Of the 32 proved samples, 9 (28.1\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
531	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
532	This demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.
533	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
534	
535	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
536	\label{app:o1-ablation}
537	
538	To justify the per-clause LOO design (\S\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\text{fast\_ISR}(x) = 1$ if $x$ is proved \emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
539	The reward becomes $r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$.
540	After 500 steps (seed~42), this variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$---functionally zero---compared to $\text{ISR}^*{=}0.132$ under standard exec-only and $\text{ISR}^*{=}0.42$ under ISR $\beta{=}0.1$.
541	
542	\paragraph{ISR signal vs.\ training dynamics.}
543	At the \emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.
544	At the \emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.
545	This confound depresses prove rate by 30 percentage points ($63\%$ vs.\ $93\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.
546	The result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.
547	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "215496c2-ac09-4b2e-a0c1-bc2915472e2b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 8 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\begin{table}[h]\n\\centering\n\\caption{Fisher exact tests for genuine rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ genuine rate is corrected for H8 reclassification and H7 false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Genuine rate (H8+FN corrected)}} \\\\\nISR vs.\\ Random & 6.9\\% {\\scriptsize[4.3,11.0]} & 18.4\\% {\\scriptsize[14.0,23.7]} & 0.33 & 0.0002 \\\\\nISR vs.\\ Exec-only & 6.9\\% & 7.5\\% & 0.91 & 0.81 \\\\\nRandom vs.\\ Exec-only & 18.4\\% & 7.5\\% & 2.76 & 0.012 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Genuine rate (H8-only, conservative)}} \\\\\nISR vs.\\ Random & 12.1\\% & 18.4\\% & 0.61 & 0.060 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{H7 gaming rate}} \\\\\nISR vs.\\ Random & 69.7\\% & 0\\% & $\\infty$ & ${<}0.001$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only genuine rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}256$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table}\n\n\\paragraph{Meta-level Goodhart: implications.}\nThe meta-Goodhart finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\\beta{=}0.3$: PR collapse to 18\\% vs.\\ 48\\% random) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.\n$\\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.\nThe practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}\\pm 47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify eight distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ in premises & 87 & 18 & 81 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{70} & 0 & 0 \\\\\nH8 & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}12$; s44 only). Exec: H1${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nH1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\n\\subsection{H8 --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).\nWe term this \\textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull H8 audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their genuine rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.\n\n\\paragraph{H7 false-negative correction (H7b obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as genuine by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.\n$10/12$ achieve $\\text{ISR}{\\approx}0.8$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 genuine${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.\n\n\\paragraph{Impact on genuine-rate comparison.}\nUnder the primary correction (H8 + FN): ISR genuine $= 16/231 = 6.9\\%$ vs.\\ random genuine $= 47/256 = 18.4\\%$ (Fisher $p{=}0.0002$).\nUnder conservative correction (H8 only, no FN fix): ISR genuine $= 28/231 = 12.1\\%$ vs.\\ $18.4\\%$ (Fisher $p{=}0.060$).\nBoth scenarios are directionally consistent: ISR-specific gaming modes reduce genuine output relative to a matched control.\n\n\\subsection{H1 --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as H1 (71--93\\%); under ISR reward, it shifts to H7 (69.7\\% pooled).\n\n\n\\subsection{H7a --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nH7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nH7a (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined H7 (H7a + H7b): 69.7\\% (161/231; includes s44 FN correction).\n\\textbf{Zero} occurrences under Random~$\\beta{=}0.1$ across all three seeds ($0/256$).\n\n\n\\subsection{H7b --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\nThe premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$ ($10/12$ samples).\nH7b simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).\nThis triple gaming makes H7b the most complete meta-Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound exclusively in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as genuine).\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from H7 by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% H7 by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% H7, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe fact is necessarily necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to H7 but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$).}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & \\makebox[0pt][l]{$0.130$} & & \\makebox[0pt][l]{$0.595$} & & \\makebox[0pt][l]{\\textbf{92.3}} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\\% \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step only \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed H1+H7+H8 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{96.7} & 0 & ${\\sim}$3 & H7 dominant \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\\\\n  & 43 & 500 & 0.88 & 0.058 & 0 & 93.2 & 6.8 & \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 79.8 & 20.2 & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.85{\\pm}0.06$} & & \\makebox[0pt][l]{$0.086{\\pm}0.039$} & & & H7 = 0\\% all seeds \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 0 & 100 & 0 & $n_{\\text{comp}} = 9.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.53{\\pm}0.31$} & & \\makebox[0pt][l]{$0.146{\\pm}0.21$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & H7 tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional H7$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.62{\\pm}0.31$} & & \\makebox[0pt][l]{$0.699{\\pm}0.45$} & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict H7 classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean H7 tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\\beta{=}0.3$.\nThe three ISR seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 22.2 & Reward collapse ($n{=}18$) \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 26.7 & H1 shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure H7 meta-Goodhart \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.66{\\pm}0.42$} & & \\makebox[0pt][l]{$0.39{\\pm}0.31$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 0 & 100 & 0 & \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 90.2 & 2.2 & \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%---higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nTo justify the per-clause LOO design (\\S\\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved \\emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nThe reward becomes $r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$.\nAfter 500 steps (seed~42), this variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$---functionally zero---compared to $\\text{ISR}^*{=}0.132$ under standard exec-only and $\\text{ISR}^*{=}0.42$ under ISR $\\beta{=}0.1$.\n\n\\paragraph{ISR signal vs.\\ training dynamics.}\nAt the \\emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.\nAt the \\emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.\nThis confound depresses prove rate by 30 percentage points ($63\\%$ vs.\\ $93\\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.\nThe result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.\n",
      "numLines": 547,
      "startLine": 1,
      "totalLines": 547
    }
  }
}
```

</details>

---


### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt",
  "usage": {
    "total_tokens": 15402,
    "tool_uses": 2,
    "duration_ms": 8360
  },
  "last_tool_name": "Read",
  "uuid": "617f5375-a517-4c01-bef6-05dfaae9e222",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_0135CrMUrs6F2WKrLX9zwDJQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "a76793f0-e26f-480e-9beb-ad3e9416056a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTbH8LWU5xif93sHZjxkBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 14323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1072,
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

_source line 42 · 2026-05-15T15:57:08.432Z_

<details><summary>↩ Tool result · reported error · `toolu_0135CrMUrs6F2WKrLX9zwDJQ`</summary>

```text
File content (81945 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "cc2c0369-103a-43c7-9be1-310befaf6721",
  "tool_use_result": "Error: File content (81945 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Running Check line count of the file",
  "usage": {
    "total_tokens": 15707,
    "tool_uses": 3,
    "duration_ms": 11975
  },
  "last_tool_name": "Bash",
  "uuid": "06e7ab04-08c5-4331-ab36-ed9eb740f5cf",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01VvfhthcsA6A1tT8JFmLDdr`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt",
  "description": "Check line count of the file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "c78e6d9c-a135-4906-89d1-4227523074eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G9mJxe47Zio93kibq6FaGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 15395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 235,
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

_source line 45 · 2026-05-15T15:57:11.984Z_

<details><summary>↩ Tool result · `toolu_01VvfhthcsA6A1tT8JFmLDdr`</summary>

```text
0 /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "20fa16d5-0487-4f57-8ec5-43f3d3d56aa3"
}
```

</details>

---


### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Running Parse outer JSON structure",
  "usage": {
    "total_tokens": 15976,
    "tool_uses": 4,
    "duration_ms": 17206
  },
  "last_tool_name": "Bash",
  "uuid": "b67314b4-0ee6-4e12-85a4-f6b9d60ce3fb",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01Tmx7GoDoGWqr5ifwWbcKw5`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\n# Parse outer JSON\nouter = json.loads(raw)\nprint(\"Outer keys:\", list(outer.keys()))\nprint(\"Type of 'result':\", type(outer.get('result')))\nprint(\"First 500 chars of result:\", str(outer.get('result'))[:500])\nPYEOF\n",
  "description": "Parse outer JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "29046fe3-2701-4ff7-b2f8-c75848a64cbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqeELZPsdfDiNoJXea9Pxj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 15630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 265,
        "ephemeral_1h_input_tokens": 0
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

_source line 48 · 2026-05-15T15:57:17.090Z_

<details><summary>↩ Tool result · `toolu_01Tmx7GoDoGWqr5ifwWbcKw5`</summary>

```text
Outer keys: ['result']
Type of 'result': &lt;class 'str'>
First 500 chars of result: {"success": true, "data": {"experiments": {"plan002-additive-b01-s43-r2": {"status": "PREPARING", "retry_count": 0, "created_at": "2026-05-15T14:21:58.445Z", "updated_at": "2026-05-15T15:52:54.116Z", "spec": {"hypothesis": "ISR β=0.1 seed=43 重训（r2）：原始实验 checkpoint+eval 全部丢失，registry 有 genuine=2/h7=59 但缺 h1/h8。重训+完整 eval+H7/H1/H8 taxonomy，补全所有字段。", "parent": "plan002-additive-b01-s43", "server": "westd-39279", "data_path": "data/train_500_seed42.jsonl", "data_count": 500, "model_name": "Qwen3-4B"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "40c0da82-3f96-4e0e-8a9a-55b104410a86"
}
```

</details>

---


### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Running Parse inner JSON and list all experiments",
  "usage": {
    "total_tokens": 16621,
    "tool_uses": 5,
    "duration_ms": 22923
  },
  "last_tool_name": "Bash",
  "uuid": "8416ee94-9087-49ad-8f52-f8ad629b4ea4",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_0163pZzcqW3F8RLRHcKVEWMB`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\n\ndata = inner['data']\nprint(\"Top-level keys in data:\", list(data.keys()))\nprint()\n\n# Check experiments\nexps = data.get('experiments', {})\nprint(f\"Total experiments: {len(exps)}\")\nprint()\n\n# Show all experiment IDs and statuses\nfor eid, edata in exps.items():\n    status = edata.get('status', 'N/A')\n    conclusion = edata.get('conclusion', '')\n    print(f\"  {eid}: status={status}, conclusion={conclusion[:80] if conclusion else 'N/A'}\")\n\nPYEOF\n",
  "description": "Parse inner JSON and list all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "08121e98-e9d2-4f5b-95b7-ef04ae0ccc12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016US7Z65NAjBVN1azcKX7P8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 572,
      "cache_read_input_tokens": 15895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 572,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
      "service_tier": "standard",
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

_source line 51 · 2026-05-15T15:57:22.843Z_

<details><summary>↩ Tool result · `toolu_0163pZzcqW3F8RLRHcKVEWMB`</summary>

```text
Top-level keys in data: ['experiments', 'count', 'total', 'baseline']

Total experiments: 86

  plan002-additive-b01-s43-r2: status=PREPARING, conclusion=N/A
  plan018-additive-random-b01-s42-1000-r3: status=DONE, conclusion=negative
  plan009-sft-baseline-s44-1000: status=DONE, conclusion=success
  plan009-sft-baseline-s43-1000: status=DONE, conclusion=success
  plan009-sft-baseline-s42-1000: status=DONE, conclusion=success
  exp1-random-b03-s43: status=DONE, conclusion=success
  exp1-random-b03-s43-r4: status=DONE, conclusion=success
  plan002-additive-b01-s42-1000: status=DONE, conclusion=negative
  plan018-additive-random-b01-s42: status=DONE, conclusion=negative
  plan002-additive-b01-s44: status=DONE, conclusion=negative
  plan013-random-reward-s42-r4: status=DONE, conclusion=success
  plan001-exec-only-s43-r4: status=DONE, conclusion=negative
  plan001-exec-only-s42: status=DONE, conclusion=failed
  plan017-additive-random-s42: status=DONE, conclusion=negative
  plan002-additive-b01-s42: status=DONE, conclusion=negative
  plan002-additive-b01-s43: status=DONE, conclusion=negative
  plan018-additive-random-b01-s44-r2: status=PREPARING, conclusion=N/A
  plan018-additive-random-b01-s43-r3: status=PREPARING, conclusion=N/A
  exp1-isr-b03-s43: status=DONE, conclusion=success
  plan009-sft-baseline-s44-1000-r3: status=DONE, conclusion=success
  plan009-sft-baseline-s44: status=DONE, conclusion=success
  plan009-sft-baseline-s43: status=DONE, conclusion=success
  plan001-exec-only-s44-1000-r2: status=RUNNING, conclusion=N/A
  plan001-exec-only-s43-1000-r2: status=RUNNING, conclusion=N/A
  plan001-exec-only-s44-1000: status=DONE, conclusion=failed
  plan001-exec-only-s43-1000: status=DONE, conclusion=failed
  plan009-sft-baseline-s44-1000-r2: status=DONE, conclusion=failed
  plan002-additive-b03-s42: status=DONE, conclusion=negative
  plan001-exec-only-s42-r2: status=DONE, conclusion=success
  plan004-o1-ablation-s42: status=DONE, conclusion=negative
  exp1-isr-b03-s42-1000-r2: status=DONE, conclusion=negative
  plan018-additive-random-b01-s42-1000-r2: status=DONE, conclusion=negative
  plan018-additive-random-b01-s42-1000: status=DONE, conclusion=failed
  exp1-isr-b03-s42-1000: status=DONE, conclusion=failed
  plan001-exec-only-s44: status=DONE, conclusion=negative
  plan018-additive-random-b01-s43-r2: status=DONE, conclusion=negative
  exp1-random-b03-s44-r2: status=DONE, conclusion=success
  exp1-isr-b03-s43-r3: status=DONE, conclusion=success
  exp1-random-b03-s43-r3: status=DONE, conclusion=failed
  plan015-linear-s42: status=DONE, conclusion=killed
  exp1-isr-b03-s43-r4: status=DONE, conclusion=killed
  exp1-random-b03-s43-r2: status=DONE, conclusion=killed
  exp1-isr-b03-s44-r2: status=DONE, conclusion=success
  exp1-random-b03-s44: status=DONE, conclusion=failed
  exp1-isr-b03-s44: status=DONE, conclusion=failed
  exp1-isr-b03-s43-r2: status=DONE, conclusion=killed
  exp2-exec-s43-greedy: status=DONE, conclusion=success
  exp4-100step-h1h7: status=DONE, conclusion=success
  plan006-prolog-sta-s44: status=DONE, conclusion=negative
  plan006-prolog-sta-s43: status=DONE, conclusion=negative
  plan016-extended-1000-s42: status=DONE, conclusion=success
  plan006-prolog-sta-s42: status=DONE, conclusion=negative
  plan006-prolog-exec-s44: status=DONE, conclusion=negative
  plan009-sft-baseline-s42-r4: status=DONE, conclusion=success
  plan006-prolog-exec-s43-r3: status=DONE, conclusion=negative
  plan018-additive-random-b01-s44: status=DONE, conclusion=success
  plan009-sft-baseline-s42: status=DONE, conclusion=killed
  plan006-prolog-exec-s43-r2: status=DONE, conclusion=failed
  plan006-prolog-exec-s42: status=DONE, conclusion=negative
  plan006-prolog-exec-s43: status=DONE, conclusion=killed
  plan009-sft-baseline-s42-r3: status=DONE, conclusion=failed
  plan009-sft-baseline-s42-r2: status=DONE, conclusion=failed
  plan018-additive-random-b01-s43: status=DONE, conclusion=failed
  plan012-hacking-taxonomy: status=DONE, conclusion=success
  plan005-sta-low-s42: status=DONE, conclusion=negative
  plan014-downstream-nli-s42: status=DONE, conclusion=negative
  plan001-exec-only-s43-r3: status=DONE, conclusion=failed
  plan013-random-reward-s42-r3: status=DONE, conclusion=failed
  plan001-exec-only-s43-r2: status=DONE, conclusion=failed
  plan013-random-reward-s42-r2: status=DONE, conclusion=failed
  plan013-random-reward-s42: status=DONE, conclusion=failed
  plan001-exec-only-s43: status=DONE, conclusion=failed
  plan003-eval-exec-only-r5: status=DONE, conclusion=success
  plan001-exec-only-s42-r3: status=DONE, conclusion=failed
  sta-phase1-exec-sta-r5: status=DONE, conclusion=negative
  sta-phase1-exec-only-r5: status=DONE, conclusion=success
  sta-phase1-exec-sta-r4: status=DONE, conclusion=negative
  sta-phase1-exec-only-r4: status=DONE, conclusion=negative
  sta-phase1-exec-only-r3: status=DONE, conclusion=failed
  sta-phase1-exec-sta-r3: status=DONE, conclusion=failed
  sta-phase1-exec-sta-r2: status=DONE, conclusion=failed
  sta-phase1-exec-only-r2: status=DONE, conclusion=failed
  sta-phase1-exec-sta: status=DONE, conclusion=failed
  sta-phase1-exec-only: status=DONE, conclusion=failed
  sta-gt-isr-baseline: status=DONE, conclusion=success
  sta-phase0-baseline: status=DONE, conclusion=success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "cccd8ea3-82e6-4fc5-9072-51f2b2f38794"
}
```

</details>

---


### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Running Extract baseline data",
  "usage": {
    "total_tokens": 19078,
    "tool_uses": 6,
    "duration_ms": 28303
  },
  "last_tool_name": "Bash",
  "uuid": "a133b25e-2876-4b80-9ddc-2ac0a5e43d2e",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_018kASoLbKS6Y7kMSkf4JpCB`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\ndata = inner['data']\n\n# First, show baseline data\nbaseline = data.get('baseline', {})\nprint(\"=\" * 120)\nprint(\"BASELINE DATA\")\nprint(\"=\" * 120)\nprint(json.dumps(baseline, indent=2, ensure_ascii=False))\nprint()\n\n# Show count/total\nprint(f\"count: {data.get('count')}, total: {data.get('total')}\")\nprint()\n\nPYEOF\n",
  "description": "Extract baseline data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "2dfa075f-fdb6-4f02-8450-d5cdca0d13b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhZAmPJoCo5en8bELu5r2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2384,
      "cache_read_input_tokens": 16467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2384,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
      "service_tier": "standard",
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

_source line 54 · 2026-05-15T15:57:28.194Z_

<details><summary>↩ Tool result · `toolu_018kASoLbKS6Y7kMSkf4JpCB`</summary>

```text
========================================================================================================================
BASELINE DATA
========================================================================================================================
null

count: 86, total: 86
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "5148fed6-1d71-49cc-8139-25d66e443411"
}
```

</details>

---


### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Running Filter experiments and inspect structure",
  "usage": {
    "total_tokens": 19511,
    "tool_uses": 7,
    "duration_ms": 35942
  },
  "last_tool_name": "Bash",
  "uuid": "23d031a2-acc1-41b7-a260-95888a42763e",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01LjafZxNhVYok9G5vJbMgk7`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Filter for SUCCESS status or conclusion containing \"success\" or \"negative\"\ntarget_exps = {}\nfor eid, edata in exps.items():\n    status = edata.get('status', '')\n    conclusion = edata.get('conclusion', '') or ''\n    if status == 'SUCCESS' or 'success' in conclusion.lower() or 'negative' in conclusion.lower():\n        target_exps[eid] = edata\n\nprint(f\"Matched experiments: {len(target_exps)}\")\nprint()\n\n# Now let's look at the structure of one experiment to understand fields\nsample_id = list(target_exps.keys())[0]\nsample = target_exps[sample_id]\nprint(f\"Sample experiment: {sample_id}\")\nprint(f\"Top-level keys: {list(sample.keys())}\")\nprint()\n\n# Show full structure of a few experiments\nfor i, (eid, edata) in enumerate(list(target_exps.items())[:3]):\n    print(f\"--- {eid} ---\")\n    print(json.dumps(edata, indent=2, ensure_ascii=False)[:3000])\n    print()\n\nPYEOF\n",
  "description": "Filter experiments and inspect structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "eb9a5b6d-148a-4e2b-a9f7-21197d72585f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01797R9GZHaUjwo2Zk2ahsQs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 361,
      "cache_read_input_tokens": 18851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 361,
        "ephemeral_1h_input_tokens": 0
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

_source line 57 · 2026-05-15T15:57:35.830Z_

<details><summary>↩ Tool result · `toolu_01LjafZxNhVYok9G5vJbMgk7`</summary>

```text
Matched experiments: 49

Sample experiment: plan018-additive-random-b01-s42-1000-r3
Top-level keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'server', 'gpu', 'account', 'pid', 'log_path', 'reproduce', 'extra', 'checkpoint_path', 'metrics', 'conclusion', 'completed_at', 'taxonomy_note', 'h7_count', 'h1_count', 'h8_count', 'genuine_count']

--- plan018-additive-random-b01-s42-1000-r3 ---
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T10:26:49.094Z",
  "updated_at": "2026-05-15T15:39:20.811Z",
  "spec": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:1"
    ],
    "pid": "269147",
    "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000-r3.log",
    "submitted_at": "2026-05-15T10:27:08.529Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 6985.6,
    "gpu_hours": 1.94
  },
  "server": "westd-39279",
  "gpu": "cuda:1",
  "account": "root",
  "pid": "269147",
  "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000-r3.log",
  "reproduce": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\"",
    "finished_at": "2026-05-15T12:05:43.550Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T12:05:46.554124+00:00"
      }
    ]
  },
  "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3/checkpoint-1000",
  "metrics": {
    "eval_prove_rate": 0.97,
    "eval_mean_isr": 0.6892,
    "eval_isr_std": 0.2037,
    "eval_median_isr": 0.75,
    "eval_proved_only_isr": 0.7105,
    "eval_n_proved": 97,
    "eval_n_problems": 100,
    "genuine_count": 0,
    "genuine_rate": 0,
    "h1_count": 0,
    "h1_rate": 0,
    "h7_count": 97,
    "h7_rate": 1,
    "tautological_collapse": true,
    "train_final_prove_rate": 0.827,
    "train_final_mean_isr": 0.5213,
    "train_loss": 0.00671,
    "train_final_entropy": 0.003,
    "train_runtime_seconds": 5783,
    "train_steps": 1000,
    "eval_by_answer_type": {
      "false": {
        "count": 25,
        "proved": 25,
        "prove_rate": 1,
        "mean_isr": 0.7533
      },
      "unknown": {
        "count": 41,
        "proved": 39,
        "prove_rate": 0.951,
        "mean_isr": 0.6565
      },
      "true": {
        "count": 34,
        "proved": 33,
        "prove_rate": 0.971,
        "mean_isr": 0.6814
      }
    },
    "n_premise_distribution": {
      "1": 97
    },
    "pattern_description": "All 97 proved: 1 pre

--- plan009-sft-baseline-s44-1000 ---
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-15T12:47:54.021Z",
  "updated_at": "2026-05-15T15:38:21.803Z",
  "hypothesis": "SFT 1000步 seed=44：与 s42/s43 相同配置的第三个 seed，验证 SFT 在 1000 步的 genuine rate 稳定性。3-seed 统计支撑 Goodhart collapse 是 RL (GRPO) 特有现象的 claim。",
  "parent": "plan009-sft-baseline-s42-r4",
  "server": "westd-39279",
  "gpu": "cuda:1",
  "account": "root",
  "reproduce": {
    "server": "westd-39279",
    "gpu": "cuda:1",
    "started_at": "2026-05-15T12:49:08.008Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000 --num_steps 1000 --seed 44 --no_wandb --gpu 1\"",
    "finished_at": "2026-05-15T12:50:00.305Z",
    "training_hours": 0.01
  },
  "failure_reason": "CUDA OOM: CUDA out of memory. Tried to allocate 742.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 100.25 MiB is free. Process 352142 has 62.36 GiB memory in use. Including non-PyTorch memory, this process has 32.51 GiB memory in use. Of the allocate",
  "completed_at": "2026-05-15T12:50:04.083Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-15T12:50:14.696431+00:00"
      }
    ],
    "previous_failure": {
      "conclusion": "failed"
    }
  },
  "spec": {
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 44
  },
  "pid": "352970",
  "log_path": "~/runs/solver-trace-ablation/plan009-sft-baseline-s44-1000-r3.log",
  "conclusion": "success",
  "metrics": {
    "prove_rate": 0.15,
    "n_proved": 15,
    "n_problems": 100,
    "mean_isr": 0.0884,
    "isr_std": 0.2268,
    "median_isr": 0,
    "proved_only_mean_isr": 0.5892,
    "max_isr": 0.8571,
    "by_answer_type": {
      "true": {
        "count": 34,
        "proved": 15,
        "prove_rate": 0.4412
      },
      "false": {
        "count": 25,
        "proved": 0,
        "prove_rate": 0
      },
      "unknown": {
        "count": 41,
        "proved": 0,
        "prove_rate": 0
      }
    },
    "genuine_count": 14,
    "genuine_rate": 0.9333,
    "h7_strict_count": 0,
    "h7_strict_rate": 0,
    "h1_strict_count": 1,
    "h1_strict_rate": 0.0667,
    "h8_conjunction_collapse_count": 0,
    "h8_conjunction_collapse_rate": 0,
    "conclusion_in_premise_count": 1,
    "conclusion_in_premise_rate": 0.0667,
    "content_independent_count": 0,
    "content_independent_rate": 0,
    "isr_1_count": 0,
    "isr_1_rate": 0,
    "train_final_loss": 0.0171,
    "train_avg_loss": 0.1544,
    "train_token_accuracy": 0.995,
    "train_runtime_s": 1580.97,
    "eval_elapsed_s": 391.8
  },
  "checkpoint_path": "/root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/checkpoint-1000",
  "notes": "SFT s44

--- plan009-sft-baseline-s43-1000 ---
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T12:28:46.064Z",
  "updated_at": "2026-05-15T15:38:21.200Z",
  "spec": {
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 43
  },
  "hypothesis": "SFT 1000步 seed=43：与 s42 相同配置的第二个 seed，验证 SFT 在 1000 步的 genuine rate 稳定性。与 GRPO 各条件 1000步对比，确认 Goodhart collapse 是 RL 特有现象。",
  "parent": "plan009-sft-baseline-s43",
  "server": "westd-39279",
  "gpu": "cuda:0",
  "account": "root",
  "pid": "352137",
  "log_path": "/root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/checkpoint-1000/trainer_state.json",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000 --num_steps 1000 --seed 43 --no_wandb --gpu 0\"",
    "finished_at": "2026-05-15T13:15:26.388Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T13:15:29.227018+00:00"
      }
    ]
  },
  "metrics": {
    "prove_rate": 0.11,
    "n_proved": 11,
    "n_problems": 100,
    "mean_isr": 0.0699,
    "isr_std": 0.2155,
    "median_isr": 0,
    "proved_only_mean_isr": 0.6352,
    "by_answer_type": {
      "true": {
        "count": 34,
        "proved": 11,
        "prove_rate": 0.3235
      },
      "false": {
        "count": 25,
        "proved": 0,
        "prove_rate": 0
      },
      "unknown": {
        "count": 41,
        "proved": 0,
        "prove_rate": 0
      }
    },
    "genuine_count": 10,
    "genuine_rate": 0.9091,
    "h7_strict_count": 0,
    "h7_strict_rate": 0,
    "h1_strict_count": 1,
    "h1_strict_rate": 0.0909,
    "h8_conjunction_collapse_count": 0,
    "h8_conjunction_collapse_rate": 0,
    "conclusion_in_premise_count": 1,
    "conclusion_in_premise_rate": 0.0909,
    "content_independent_count": 0,
    "content_independent_rate": 0,
    "isr_1_count": 1,
    "isr_1_rate": 0.0909,
    "train_final_loss": 0.0167,
    "train_avg_loss": 0.1551,
    "train_token_accuracy": 0.9954,
    "train_runtime_s": 1584.79,
    "eval_elapsed_s": 326.1
  },
  "checkpoint_path": "/root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/checkpoint-1000",
  "conclusion": "success",
  "notes": "SFT s43 1000步结果与 s42 高度一致：prove_rate 11% vs 13%（-2pp），mean_isr 0.0699 vs 0.0738，final_loss 0.0167 vs 0.0168。差异在 seed 方差范围内。SFT baseline 稳定。注意：eval_sta.py 当前版本不输出 h7/h1/h8/genuine 分类指标。",
  "completed_at": "2026-05-15T13:25:00.854Z",
  "taxonomy_note": "D086 补扫: proved=11, H7=0, H1=1, H8=0, genuine=10 (90.9%). SFT 1000-step s43 保持高 genuine rate. eval: /root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/eval_sta_results.json",
  "genuine_count": 10,
  "genuine_rate": 0.909
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "324f8732-718b-47d2-90af-5f78015b87c8"
}
```

</details>

---


### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Running Extract comprehensive metrics for all success/negative experiments",
  "usage": {
    "total_tokens": 24304,
    "tool_uses": 8,
    "duration_ms": 54816
  },
  "last_tool_name": "Bash",
  "uuid": "d522fca8-ad03-4de4-81f2-a55d0e989c18",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_01XF2WHVMUedXzjU2TY1XLVS`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Filter for conclusion = success or negative\ntarget_exps = {}\nfor eid, edata in exps.items():\n    conclusion = (edata.get('conclusion') or '').lower()\n    if conclusion in ('success', 'negative'):\n        target_exps[eid] = edata\n\nprint(f\"Total matched experiments (success or negative): {len(target_exps)}\")\nprint()\n\n# Now extract comprehensive data for each\nfor eid in sorted(target_exps.keys()):\n    e = target_exps[eid]\n    conclusion = e.get('conclusion', '')\n    status = e.get('status', '')\n    metrics = e.get('metrics', {}) or {}\n    spec = e.get('spec', {}) or {}\n    \n    print(\"=\" * 120)\n    print(f\"EXP_ID: {eid}\")\n    print(f\"  status: {status}\")\n    print(f\"  conclusion: {conclusion}\")\n    \n    # Spec info\n    hypothesis = e.get('hypothesis', '') or spec.get('hypothesis', '') or ''\n    seed = spec.get('seed', '')\n    reward_mode = spec.get('reward_mode', '')\n    beta = spec.get('beta', '')\n    num_steps = spec.get('num_steps', '')\n    data_count = spec.get('data_count', '')\n    model_name = spec.get('model_name', '')\n    data_path = spec.get('data_path', '')\n    \n    if hypothesis:\n        print(f\"  hypothesis: {hypothesis[:200]}\")\n    if model_name:\n        print(f\"  model: {model_name}\")\n    if reward_mode:\n        print(f\"  reward_mode: {reward_mode}\")\n    if beta:\n        print(f\"  beta: {beta}\")\n    if seed:\n        print(f\"  seed: {seed}\")\n    if num_steps:\n        print(f\"  num_steps: {num_steps}\")\n    if data_count:\n        print(f\"  data_count: {data_count}\")\n    if data_path:\n        print(f\"  data_path: {data_path}\")\n    \n    # Checkpoint\n    cp = e.get('checkpoint_path', '')\n    if cp:\n        print(f\"  checkpoint: {cp}\")\n    \n    # All metrics\n    print(f\"  --- METRICS ---\")\n    if not metrics:\n        print(f\"    (no metrics)\")\n    else:\n        # Core eval metrics\n        for k in sorted(metrics.keys()):\n            v = metrics[k]\n            if isinstance(v, dict):\n                print(f\"    {k}:\")\n                for k2, v2 in v.items():\n                    if isinstance(v2, dict):\n                        print(f\"      {k2}: {json.dumps(v2)}\")\n                    else:\n                        print(f\"      {k2}: {v2}\")\n            elif isinstance(v, list):\n                print(f\"    {k}: {json.dumps(v)}\")\n            else:\n                print(f\"    {k}: {v}\")\n    \n    # Top-level taxonomy fields (sometimes outside metrics)\n    for field in ['taxonomy_note', 'h7_count', 'h1_count', 'h8_count', 'genuine_count', 'genuine_rate', 'h7_rate', 'h1_rate', 'h8_rate']:\n        val = e.get(field)\n        if val is not None:\n            print(f\"  {field} (top-level): {val}\")\n    \n    # Notes\n    notes = e.get('notes', '')\n    if notes:\n        print(f\"  notes: {notes[:500]}\")\n    \n    # Failure/decision info\n    failure = e.get('failure_reason', '')\n    if failure:\n        print(f\"  failure_reason: {failure[:200]}\")\n    \n    parent = e.get('parent', '')\n    if parent:\n        print(f\"  parent: {parent}\")\n    \n    print()\n\nPYEOF\n",
  "description": "Extract comprehensive metrics for all success/negative experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "dc9698e1-47e7-4902-a76f-508804f19016",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVNA3Dh1LzdL7MHbfrpn4Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4791,
      "cache_read_input_tokens": 19212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4791,
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

_source line 60 · 2026-05-15T15:57:54.818Z_

<details><summary>↩ Tool result · `toolu_01XF2WHVMUedXzjU2TY1XLVS`</summary>

```text
&lt;persisted-output>
Output too large (69.2KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt

Preview (first 2KB):
Total matched experiments (success or negative): 49

========================================================================================================================
EXP_ID: exp1-isr-b03-s42-1000-r2
  status: DONE
  conclusion: negative
  checkpoint: /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000
  --- METRICS ---
    completions_mean_length: 47
    content_independent_predicates: True
    eval_by_answer_type:
      false: {"count": 25, "proved": 25, "prove_rate": 1, "mean_isr": 0.824}
      unknown: {"count": 41, "proved": 38, "prove_rate": 0.927, "mean_isr": 0.673}
      true: {"count": 34, "proved": 32, "prove_rate": 0.941, "mean_isr": 0.741}
    eval_data: proofwriter_fol_100.jsonl
    eval_isr_std: 0.2575
    eval_mean_isr: 0.734
    eval_median_isr: 0.6
    eval_n_problems: 100
    eval_n_proved: 95
    eval_prove_rate: 0.95
    eval_proved_only_isr: 0.7726
    genuine_count: 0
    genuine_rate: 0
    h1_count: 54
    h1_rate: 0.568
    h7_count: 0
    h7_rate: 0
    h8_conjunction_collapse_count: 41
    h8_conjunction_collapse_rate: 0.432
    isr_1_count: 41
    isr_1_rate: 0.432
    single_premise_count: 0
    tautological_collapse: True
    train_final_entropy: 9e-06
    train_final_mean_isr: 0.727
    train_final_prove_rate: 0.829
    train_loss: 0.0041
    train_runtime_seconds: 6280

========================================================================================================================
EXP_ID: exp1-isr-b03-s43
  status: DONE
  conclusion: success
  hypothesis: β=0.3 ISR seed 43: supplement for 3-seed statistics in Table 1. Reference: plan002-additive-b03-s42
  model: Qwen3-4B
  beta: 0.3
  seed: 43
  num_steps: 500
  data_count: 500
  data_path: data/train_500_seed42.jsonl
  --- METRICS ---
    eval_data: test_100.jsonl
    eval_output: /root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json
    genuine_count: 61
    genuine_rate: 0.6703
    h1_conclusion_in_premise: 0.747
    hacking_rate_functional: 0.3297
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "681fb50a-34c9-4629-8579-af127760dec7"
}
```

</details>

---


### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt",
  "usage": {
    "total_tokens": 26511,
    "tool_uses": 9,
    "duration_ms": 58214
  },
  "last_tool_name": "Read",
  "uuid": "7514b5d3-9d85-4f95-a6e8-238a3c8b936b",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_01Wg1apAPHu7NYvzYwtoqnTx`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt",
  "limit": 200,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "5f97a8ef-cdaa-4140-8af5-233e140ea8d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vb5ZW6wxq5XQBiPF9nZ5Af",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2135,
      "cache_read_input_tokens": 24003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2135,
        "ephemeral_1h_input_tokens": 0
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

_source line 63 · 2026-05-15T15:57:58.011Z_

<details><summary>↩ Tool result · `toolu_01Wg1apAPHu7NYvzYwtoqnTx`</summary>

```text
0	Total matched experiments (success or negative): 49
1	
2	========================================================================================================================
3	EXP_ID: exp1-isr-b03-s42-1000-r2
4	  status: DONE
5	  conclusion: negative
6	  checkpoint: /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000
7	  --- METRICS ---
8	    completions_mean_length: 47
9	    content_independent_predicates: True
10	    eval_by_answer_type:
11	      false: {"count": 25, "proved": 25, "prove_rate": 1, "mean_isr": 0.824}
12	      unknown: {"count": 41, "proved": 38, "prove_rate": 0.927, "mean_isr": 0.673}
13	      true: {"count": 34, "proved": 32, "prove_rate": 0.941, "mean_isr": 0.741}
14	    eval_data: proofwriter_fol_100.jsonl
15	    eval_isr_std: 0.2575
16	    eval_mean_isr: 0.734
17	    eval_median_isr: 0.6
18	    eval_n_problems: 100
19	    eval_n_proved: 95
20	    eval_prove_rate: 0.95
21	    eval_proved_only_isr: 0.7726
22	    genuine_count: 0
23	    genuine_rate: 0
24	    h1_count: 54
25	    h1_rate: 0.568
26	    h7_count: 0
27	    h7_rate: 0
28	    h8_conjunction_collapse_count: 41
29	    h8_conjunction_collapse_rate: 0.432
30	    isr_1_count: 41
31	    isr_1_rate: 0.432
32	    single_premise_count: 0
33	    tautological_collapse: True
34	    train_final_entropy: 9e-06
35	    train_final_mean_isr: 0.727
36	    train_final_prove_rate: 0.829
37	    train_loss: 0.0041
38	    train_runtime_seconds: 6280
39	
40	========================================================================================================================
41	EXP_ID: exp1-isr-b03-s43
42	  status: DONE
43	  conclusion: success
44	  hypothesis: β=0.3 ISR seed 43: supplement for 3-seed statistics in Table 1. Reference: plan002-additive-b03-s42
45	  model: Qwen3-4B
46	  beta: 0.3
47	  seed: 43
48	  num_steps: 500
49	  data_count: 500
50	  data_path: data/train_500_seed42.jsonl
51	  --- METRICS ---
52	    eval_data: test_100.jsonl
53	    eval_output: /root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json
54	    genuine_count: 61
55	    genuine_rate: 0.6703
56	    h1_conclusion_in_premise: 0.747
57	    hacking_rate_functional: 0.3297
58	    hacking_rate_strict_h7: 0.022
59	    isr_std: 0.2363
60	    mean_isr: 0.2575
61	    median_isr: 0.3333
62	    n_problems: 100
63	    n_proved: 91
64	    parse_rate: 1
65	    prove_rate: 0.91
66	    proved_only_mean_isr: 0.283
67	  notes: D062/D063 INVALIDATED: eval used test_100.jsonl (wrong test set). Checkpoint deleted, cannot re-eval. Retrain as exp1-isr-b03-s43-r4.
68	  failure_reason: EXIT_CODE=129 (non-zero)
69	
70	========================================================================================================================
71	EXP_ID: exp1-isr-b03-s43-r3
72	  status: DONE
73	  conclusion: success
74	  model: Qwen3-4B
75	  seed: 43
76	  data_count: 500
77	  data_path: data/train_500_seed42.jsonl
78	  checkpoint: /root/autodl-tmp/outputs/exp1_isr_b03_s43_r3/checkpoint-500
79	  --- METRICS ---
80	    epoch: 2
81	    eval_by_answer_type:
82	      false: {"count": 25, "proved": 23, "prove_rate": 0.92, "mean_isr": 0.334}
83	      unknown: {"count": 41, "proved": 35, "prove_rate": 0.854, "mean_isr": 0.199}
84	      true: {"count": 34, "proved": 28, "prove_rate": 0.824, "mean_isr": 0.26}
85	    eval_conclusion_in_premise_count: 63
86	    eval_conclusion_in_premise_rate: 0.733
87	    eval_data: proofwriter_fol_100.jsonl
88	    eval_genuine_count: 23
89	    eval_genuine_rate: 0.267
90	    eval_h1_strict_count: 59
91	    eval_h1_strict_rate: 0.686
92	    eval_h7_strict_count: 4
93	    eval_h7_strict_rate: 0.047
94	    eval_isr_1_count: 0
95	    eval_isr_std: 0.2406
96	    eval_max_isr: 0.75
97	    eval_mean_isr: 0.2535
98	    eval_median_isr: 0.3333
99	    eval_min_isr: 0
100	    eval_n_problems: 100
101	    eval_n_proved: 86
102	    eval_prove_rate: 0.86
103	    eval_proved_only_mean_isr: 0.2948
104	    eval_single_premise_count: 5
105	    eval_single_premise_rate: 0.058
106	    final_step: 500
107	    mean_isr: 0.1515
108	    parse_rate: 1
109	    prove_rate: 0.56125
110	    train_loss: 0.0176
111	    train_runtime_sec: 4153.6
112	  notes: Training completed 500/500 steps in 69min. Final stats: prove_rate=0.56125, mean_isr=0.1515, parse_rate=1.0. Checkpoint saved at checkpoint-500. EVAL: PR=0.86 (greedy), mean_ISR=0.2535, H7_strict=4/86(4.7%), H1_strict=59/86(68.6%), total_hacking=63/86(73.3%), genuine=23/86(26.7%). Hacking pattern: predominantly H1 (conclusion embedding in multi-premise), NOT H7 (unlike s44's 100% H7). Data: proofwriter_fol_100.jsonl.
113	
114	========================================================================================================================
115	EXP_ID: exp1-isr-b03-s44-r2
116	  status: DONE
117	  conclusion: success
118	  hypothesis: β=0.3 ISR seed 44 retry: original failed due to orphan process OOM on GPU 0. Same config as exp1-isr-b03-s44.
119	  model: Qwen3-4B
120	  beta: 0.3
121	  seed: 44
122	  num_steps: 500
123	  data_count: 500
124	  data_path: data/train_500_seed42.jsonl
125	  checkpoint: /root/autodl-tmp/outputs/exp1_isr_b03_s44_r2/checkpoint-500/
126	  --- METRICS ---
127	    eval_data: proofwriter_fol_100.jsonl
128	    eval_note: Re-eval with correct test set (D062). Previous test_100.jsonl results invalidated.
129	    genuine_count: 0
130	    genuine_rate: 0
131	    h1_count: 0
132	    h1_rate: 0
133	    h7_count: 95
134	    h7_rate: 1
135	    isr_std: 0.172
136	    mean_isr: 0.705
137	    n_problems: 100
138	    n_proved: 95
139	    prove_rate: 0.95
140	    proved_only_isr: 0.7421
141	    single_premise_rate: 1
142	  notes: D062/D063: eval_metrics used test_100.jsonl (invalidated). metrics field contains re-eval with proofwriter_fol_100.jsonl (valid). eval_invalidated applies only to eval_metrics.
143	
144	========================================================================================================================
145	EXP_ID: exp1-random-b03-s43
146	  status: DONE
147	  conclusion: success
148	  hypothesis: β=0.3 random seed 43: supplement for 3-seed statistics in Table 1. Reference: plan017-additive-random-s42
149	  model: Qwen3-4B
150	  beta: 0.3
151	  seed: 43
152	  num_steps: 500
153	  data_count: 500
154	  data_path: data/train_500_seed42.jsonl
155	  --- METRICS ---
156	    eval_data: test_100.jsonl
157	    eval_output: /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43.json
158	    genuine_count: 71
159	    genuine_rate: 0.8987
160	    h1_conclusion_in_premise: 0.759
161	    hacking_rate_functional: 0.1013
162	    hacking_rate_strict_h7: 0
163	    isr_std: 0.1628
164	    mean_isr: 0.1745
165	    median_isr: 0.1667
166	    n_problems: 100
167	    n_proved: 79
168	    parse_rate: 1
169	    prove_rate: 0.79
170	    proved_only_mean_isr: 0.2209
171	  taxonomy_note (top-level): INVALIDATED: taxonomy based on test_100.jsonl eval, not comparable with proofwriter_fol_100 runs. Do not use in paper. D086 写入的 h7a/h1 字段仅反映旧 eval 数据，不可引用。
172	  notes: D062/D063 INVALIDATED: eval used test_100.jsonl (wrong test set). Checkpoint deleted, cannot re-eval. Retrain as exp1-random-b03-s43-r2.
173	  failure_reason: EXIT_CODE=129 (non-zero)
174	
175	========================================================================================================================
176	EXP_ID: exp1-random-b03-s43-r4
177	  status: DONE
178	  conclusion: success
179	  hypothesis: Random beta=0.3 s43 retry #4: previous r2 killed, r3 OOM. Clean GPU now.
180	  model: Qwen3-4B
181	  seed: 43
182	  data_count: 500
183	  data_path: data/train_500_seed42.jsonl
184	  checkpoint: /root/autodl-tmp/outputs/exp1_random_b03_s43_r4/checkpoint-500
185	  --- METRICS ---
186	    D086_correction: H1 90→82, genuine 2→3 per D086 clean batch run
187	    epoch: 2
188	    eval_by_answer_type:
189	      false: {"count": 25, "proved": 23, "prove_rate": 0.92, "mean_isr": 0.156}
190	      unknown: {"count": 41, "proved": 37, "prove_rate": 0.902, "mean_isr": 0.184}
191	      true: {"count": 34, "proved": 32, "prove_rate": 0.941, "mean_isr": 0.151}
192	    eval_data: proofwriter_fol_100.jsonl
193	    eval_genuine_count: 3
194	    eval_genuine_rate: 0.0326
195	    eval_h1_strict_count: 82
196	    eval_h1_strict_rate: 0.891
197	    eval_h7_strict_count: 7
198	    eval_h7_strict_rate: 0.076
199	    eval_isr0_count: 6
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "bcfabed5-1fcd-4d26-9ce3-a4f7c3c4153c"
}
```

</details>

---


### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt",
  "usage": {
    "total_tokens": 30134,
    "tool_uses": 10,
    "duration_ms": 62205
  },
  "last_tool_name": "Read",
  "uuid": "57f030bd-c755-4396-b7a3-c26fd3aab542",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_01YVT6ZkzKYGEBLqWLGGDHfG`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt",
  "limit": 400,
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "e0d5889c-83c2-41d5-897e-de689eeac399",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015M8bduHmL41uTcP6mGp35T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3551,
      "cache_read_input_tokens": 26138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3551,
        "ephemeral_1h_input_tokens": 0
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

_source line 66 · 2026-05-15T15:58:02.000Z_

<details><summary>↩ Tool result · `toolu_01YVT6ZkzKYGEBLqWLGGDHfG`</summary>

```text
200	    eval_isr0_count: 6
201	    eval_isr_std: 0.1147
202	    eval_max_isr: 0.5
203	    eval_mean_isr: 0.1659
204	    eval_median_isr: 0.1429
205	    eval_min_isr: 0
206	    eval_n_problems: 100
207	    eval_n_proved: 92
208	    eval_prove_rate: 0.92
209	    eval_proved_only_mean_isr: 0.1803
210	    final_step: 500
211	    mean_isr: 0.1358
212	    parse_rate: 1
213	    prove_rate: 0.5505
214	    train_loss: 0.01365
215	    train_runtime_sec: 6161.1
216	  taxonomy_note (top-level): D086 clean run: H7a=7, H1=82, genuine=3. metrics 字段已从旧值 (H1=90, genuine=2) 同步修正.
217	  h1_count (top-level): 82
218	  notes: Training 500/500 steps, 1h42m. Final train: prove_rate=0.5505, mean_isr=0.1358, loss=0.01365. EVAL (proofwriter_fol_100.jsonl): PR=0.92, ISR=0.1659, H7=7/92(7.6%), H1=90/92(97.8%), genuine=2/92(2.2%). ANOMALY: massive seed variance vs s44-r2 (PR=0.23, ISR=0, H1=100%, genuine=0%). s43 learned high-PR hacking strategy with conclusion-in-premise; s44 barely proved anything. Both are random baseline — this variance weakens cross-seed claims.
219	
220	========================================================================================================================
221	EXP_ID: exp1-random-b03-s44-r2
222	  status: DONE
223	  conclusion: success
224	  hypothesis: Random beta=0.3 s44: 3-seed random control for Claim 2
225	  model: Qwen3-4B
226	  seed: 44
227	  data_count: 500
228	  data_path: data/train_500_seed42.jsonl
229	  checkpoint: /root/autodl-tmp/outputs/exp1_random_b03_s44_r2/checkpoint-500
230	  --- METRICS ---
231	    eval_data: proofwriter_fol_100.jsonl
232	    eval_genuine_count: 0
233	    eval_genuine_rate: 0
234	    eval_h1_strict_count: 23
235	    eval_h1_strict_rate: 1
236	    eval_h7_strict_count: 0
237	    eval_h7_strict_rate: 0
238	    eval_isr_std: 0
239	    eval_mean_isr: 0
240	    eval_median_isr: 0
241	    eval_n_problems: 100
242	    eval_n_proved: 23
243	    eval_prove_rate: 0.23
244	    eval_proved_only_mean_isr: 0
245	
246	========================================================================================================================
247	EXP_ID: exp2-exec-s43-greedy
248	  status: DONE
249	  conclusion: success
250	  hypothesis: EXP-2: Greedy re-eval of exec-only s43 to verify decoding invariance
251	  model: Qwen3-4B
252	  seed: 43
253	  data_count: 100
254	  data_path: data/eval_100.jsonl
255	  --- METRICS ---
256	    (no metrics)
257	
258	========================================================================================================================
259	EXP_ID: exp4-100step-h1h7
260	  status: DONE
261	  conclusion: success
262	  hypothesis: EXP-4: If hacking exists at 100-step PR=32%, supports RL-specific claim independent of PR level
263	  model: Qwen3-4B (100-step checkpoint)
264	  seed: 42
265	  data_count: 100
266	  data_path: plan003_eval_exec_only_r5.json
267	  --- METRICS ---
268	    (no metrics)
269	
270	========================================================================================================================
271	EXP_ID: plan001-exec-only-s42-r2
272	  status: DONE
273	  conclusion: success
274	  hypothesis: 500-step exec-only baseline for STA comparison (K=8)
275	  model: Qwen3-4B
276	  seed: 42
277	  data_count: 500
278	  data_path: /root/solver-trace-ablation/data/train_500_seed42.jsonl
279	  checkpoint: /root/autodl-tmp/outputs/plan001_exec_only_s42/checkpoint-500
280	  --- METRICS ---
281	    conclusion_embedding_total: 0.871
282	    content_independent_predicates_count: 1
283	    eval_data: proofwriter_fol_100.jsonl
284	    eval_isr_std: 0.1887
285	    eval_mean_isr: 0.1232
286	    eval_median_isr: 0
287	    eval_method: eval_sta.py full STA
288	    eval_n_problems: 100
289	    eval_n_proved: 93
290	    eval_prove_rate: 0.93
291	    eval_proved_only_isr: 0.1324
292	    genuine_count: 7
293	    genuine_mean_isr: 0.3141
294	    genuine_rate: 0.0753
295	    h1_count: 81
296	    h1_mean_isr: 0.1055
297	    h1_rate: 0.871
298	    h7_count: 0
299	    h7_rate: 0
300	    h8_audit_note: 2026-05-15: H8 conjunction collapse added. genuine 12→7.
301	    h8_conjunction_collapse_count: 6
302	    h8_conjunction_collapse_rate: 0.0645
303	  h8_count (top-level): 6
304	  genuine_count (top-level): 7
305	  genuine_rate (top-level): 0.075
306	  notes: Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。
307	
308	========================================================================================================================
309	EXP_ID: plan001-exec-only-s43-r4
310	  status: DONE
311	  conclusion: negative
312	  hypothesis: Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds
313	  model: Qwen3-4B
314	  seed: 43
315	  data_count: 500
316	  data_path: /root/solver-trace-ablation/data/train_500_seed42.jsonl
317	  checkpoint: /root/autodl-tmp/outputs/plan001_exec_only_s43_r4
318	  --- METRICS ---
319	    eval_greedy_by_answer:
320	      true: {"count": 34, "proved": 4, "prove_rate": 0.118}
321	      false: {"count": 25, "proved": 5, "prove_rate": 0.2}
322	      unknown: {"count": 41, "proved": 4, "prove_rate": 0.0976}
323	    eval_greedy_genuine_rate: 0
324	    eval_greedy_h1_count: 13
325	    eval_greedy_h1_rate: 1
326	    eval_greedy_h7_count: 0
327	    eval_greedy_h7_rate: 0
328	    eval_greedy_mean_components_proved: 18.92
329	    eval_greedy_mean_isr: 0
330	    eval_greedy_method: eval_sta.py default (do_sample=False)
331	    eval_greedy_n_premises_all_mean: 32.67
332	    eval_greedy_n_premises_proved_mean: 17.92
333	    eval_greedy_n_proved: 13
334	    eval_greedy_prove_rate: 0.13
335	    eval_greedy_proved_only_isr: 0
336	    eval_greedy_vs_sampling_delta_pr: -0.01
337	    eval_method_note: Greedy and sampling agree on failure profile (ISR*=0, H1=100%, components~18.5-18.9). s43 collapse is decoding-invariant.
338	    eval_sampling_by_answer:
339	      true: {"count": 34, "proved": 6, "prove_rate": 0.176}
340	      false: {"count": 25, "proved": 2, "prove_rate": 0.08}
341	      unknown: {"count": 41, "proved": 6, "prove_rate": 0.146}
342	    eval_sampling_genuine_rate: 0
343	    eval_sampling_h1_rate: 1
344	    eval_sampling_h7_rate: 0
345	    eval_sampling_mean_components_proved: 18.5
346	    eval_sampling_mean_isr: 0
347	    eval_sampling_method: do_sample=True, temperature=0.7
348	    eval_sampling_n_proved: 14
349	    eval_sampling_prove_rate: 0.14
350	    eval_sampling_temperature: 0.7
351	  taxonomy_note (top-level): D086 补扫: proved=13, H7=0, H1=13, H8=1, genuine=0 (0%). exec-only s43 PR=13%, 100% H1 collapse. eval: /root/solver-trace-ablation/outputs/eval_sta_plan001_exec_only_s43_r4.json
352	  notes: EXP-2 (2026-05-15): greedy eval (T=0) on same 100 held-out problems also done with eval_sta.py defaults (do_sample=False). Result: PR=0.13, ISR*=0.0, H1=100% (13/13), H7=0%, genuine=0%, mean components (proved)=18.92. Sampling (T=0.7) baseline: PR=0.14, ISR*=0.0, H1=100% (14/14), components~18.5. ΔPR=-0.01, both ISR*=0 → s43 collapse is decoding-invariant, NOT a sampling artifact. ~85% of inputs hit max_new_tokens with long repeated-clause outputs; the ~15% that do parse contain the conclusion v
353	
354	========================================================================================================================
355	EXP_ID: plan001-exec-only-s44
356	  status: DONE
357	  conclusion: negative
358	  hypothesis: Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。
359	  checkpoint: /root/autodl-tmp/outputs/plan001_exec_only_s44
360	  --- METRICS ---
361	    conclusion_embedding_total: 1
362	    eval_component_count_2: 94
363	    eval_component_count_3: 4
364	    eval_component_count_mean: 2.04
365	    eval_data: proofwriter_fol_100.jsonl
366	    eval_isr_std: 0.2013
367	    eval_mean_isr: 0.57
368	    eval_median_isr: 0.5
369	    eval_method: eval_sta.py full STA
370	    eval_n_problems: 100
371	    eval_n_proved: 98
372	    eval_prove_rate: 0.98
373	    eval_proved_only_isr: 0.5816
374	    genuine_count: 0
375	    genuine_rate: 0
376	    h1_count: 0
377	    h1_rate: 0
378	    h7_count: 97
379	    h7_rate: 1
380	    tautological_collapse: True
381	  h7_count (top-level): 98
382	  notes: TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。
383	
384	========================================================================================================================
385	EXP_ID: plan002-additive-b01-s42
386	  status: DONE
387	  conclusion: negative
388	  model: Qwen3-4B
389	  seed: 42
390	  num_steps: 500
391	  data_count: 500
392	  data_path: data/train_500_seed42.jsonl
393	  checkpoint: /root/autodl-tmp/outputs/plan002_additive_b01_s42
394	  --- METRICS ---
395	    eval_component_count_mean: 5.58
396	    eval_data: proofwriter_fol_100.jsonl
397	    eval_isr_std: 0.3227
398	    eval_mean_isr: 0.3365
399	    eval_median_isr: 0.2
400	    eval_method: eval_sta.py full STA
401	    eval_n_problems: 100
402	    eval_n_proved: 81
403	    eval_prove_rate: 0.81
404	    eval_proved_only_isr: 0.4154
405	    genuine_count: 14
406	    genuine_rate: 0.173
407	    h1_count: 42
408	    h1_rate: 0.519
409	    h7_count: 13
410	    h7_rate: 0.16
411	    h8_audit_note: 2026-05-15: H8 conjunction collapse audit completed. 12/81 proved samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json
412	    h8_conjunction_collapse_count: 12
413	    h8_conjunction_collapse_rate: 0.148
414	    tautological_collapse: False
415	  taxonomy_note (top-level): H1-near analysis infeasible: eval_sta deleted; genuine=14 computed from aggregated H7+H1_exact+H8 exclusion per D084. H1-near is supplementary-only (per-sample data available only for Random s42).
416	  genuine_count (top-level): 14
417	  notes: H8 re-audit (2026-05-15): 81 proved samples. H7 (single premise=conclusion): 13/81=16.1%, H1 (multi-prem conclusion embedding): 42/81=51.9%, H8 (conjunction collapse): 12/81=14.8%, content-independent: 19/81=23.5%. Genuine (proved - H7 - H1 - H8): 14/81=17.3%. Pre-H8 genuine was 26/81=32.1% — H8 removed 12 samples. Combined conclusion duplication+conjunction = 82.7%. Eval source: proofwriter_fol_100.jsonl (backup at /root/autodl-tmp/eval_results_backup/). H8 JSON: /root/autodl-tmp/outputs/h7_cla
418	  parent: plan002-additive-b03-s42
419	
420	========================================================================================================================
421	EXP_ID: plan002-additive-b01-s42-1000
422	  status: DONE
423	  conclusion: negative
424	  checkpoint: /root/autodl-tmp/outputs/plan002_additive_b01_s42_1000
425	  --- METRICS ---
426	    eval_component_count_mean: 2.889
427	    eval_isr_std: 0.3424
428	    eval_mean_isr: 0.7892
429	    eval_median_isr: 1
430	    eval_n_problems: 100
431	    eval_n_proved: 90
432	    eval_prove_rate: 0.9
433	    eval_proved_only_isr: 0.8769
434	    genuine_count: 2
435	    genuine_rate: 0.0222
436	    h1_count: 0
437	    h1_near_count: 1
438	    h1_near_rate: 0.0111
439	    h1_rate: 0
440	    h7_count: 87
441	    h7_rate: 0.9667
442	    h8_conjunction_collapse_count: 1
443	    h8_conjunction_collapse_rate: 0.0111
444	    tautological_collapse: True
445	    taxonomy_standard: D086 clean run = ground truth. D084 residual removed.
446	    train_final_mean_isr: 0.532
447	    train_final_prove_rate: 0.855
448	  taxonomy_note (top-level): D086 clean run (ground truth): H7a=87, H7b=0, H1=0, H8=1, genuine=2. D084 residual (H8=2, genuine=1) replaced. metrics 字段已同步.
449	  h7_count (top-level): 87
450	  h1_count (top-level): 0
451	  h8_count (top-level): 1
452	  genuine_count (top-level): 2
453	  genuine_rate (top-level): 0.0111
454	  notes: D084 taxonomy re-audit (2026-05-15): 90 proved → H7=87 (96.7%), H1_exact=0, H1_near=1, H8=2 (2.2%), genuine=1 (1.1%). Changes vs prior: H7 +4 (paren normalization), H1 -4→0 (reclassified H7), H8 +1 (folio_1255 shared-antecedent conjunction missed), genuine -1. Tautological collapse confirmed. Taxonomy JSON: /root/autodl-tmp/outputs/plan002_additive_b01_s42_1000_taxonomy_unified.json
455	
456	========================================================================================================================
457	EXP_ID: plan002-additive-b01-s43
458	  status: DONE
459	  conclusion: negative
460	  hypothesis: ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。
461	  checkpoint: /root/autodl-tmp/outputs/plan002_additive_b01_s43/checkpoint-500
462	  --- METRICS ---
463	    eval_n_problems: 100
464	    eval_n_proved: 61
465	    eval_prove_rate: 0.61
466	    eval_proved_only_isr: 0.83
467	    genuine_count: 2
468	    genuine_rate: 0.0328
469	    h1_count: 0
470	    h1_near_count: 0
471	    h1_near_rate: 0
472	    h1_rate: 0
473	    h7_count: 59
474	    h7_rate: 0.9672
475	    h8_conjunction_collapse_count: 0
476	    h8_conjunction_collapse_rate: 0
477	    proved_single_premise_ratio: 1
478	    taxonomy_note: structurally determined: proved_single_premise_ratio=1.0, all taxonomy categories except H7 are zero by construction. eval file lost but classification derivable from structure.
479	  h7_count (top-level): 59
480	  h1_count (top-level): 0
481	  genuine_count (top-level): 2
482	  notes: NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。
483	  parent: plan002-additive-b01-s42
484	
485	========================================================================================================================
486	EXP_ID: plan002-additive-b01-s44
487	  status: DONE
488	  conclusion: negative
489	  hypothesis: ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。
490	  model: Qwen3-4B
491	  seed: 44
492	  data_count: 500
493	  data_path: data/train_500_seed42.jsonl
494	  checkpoint: /root/autodl-tmp/outputs/plan002_additive_b01_s44
495	  --- METRICS ---
496	    comp_2_ratio: 0.022
497	    component_mean: 4.33
498	    eval_isr_std: None
499	    eval_mean_isr: 0.803
500	    eval_n_problems: 100
501	    eval_n_proved: 89
502	    eval_prove_rate: 0.89
503	    eval_proved_only_isr: 0.902
504	    genuine_count: 0
505	    genuine_rate: 0
506	    h1_count: 0
507	    h1_rate: 0
508	    h7_count: 89
509	    h7_fn_correction: 12 former genuine reclassified as H7: all n_prem=1 false negatives (normalization mismatch prevented conclusion matching)
510	    h7_rate: 1
511	    h8_conjunction_collapse_count: 0
512	    h8_conjunction_collapse_rate: 0
513	  taxonomy_note (top-level): D086 补正(Reviewer): H7a=77, H7b=12, H1=0, H8=0, genuine=0. s44 全部 89 proved 均为 single_premise, H8(conjunction collapse)要求 multi-premise 数学上不可能触发. D086 clean run 误报 H8=1 已修正.
514	  h7_count (top-level): 89
515	  h1_count (top-level): 0
516	  h8_count (top-level): 0
517	  genuine_count (top-level): 0
518	  notes: H7 FN correction: 12 samples with n_prem=1 misclassified as genuine. Mismatch types: 11 vacuous_quantifier_wrapping (∃x(P(x)) vs ∃x(∃y(P(y)))), 1 structural_simplification. Not simple whitespace/case but logically equivalent structural variants. Evidence file: /root/autodl-tmp/outputs/isr_s44_fn_evidence.json. Source eval: /root/runs/solver-trace-ablation/plan002-additive-b01-s44-eval.json
519	  parent: plan002-additive-b01-s42
520	
521	========================================================================================================================
522	EXP_ID: plan002-additive-b03-s42
523	  status: DONE
524	  conclusion: negative
525	  hypothesis: Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural qualit
526	  model: Qwen3-4B
527	  beta: 0.3
528	  seed: 42
529	  data_count: 500
530	  data_path: /root/solver-trace-ablation/data/train_500_seed42.jsonl
531	  checkpoint: /root/autodl-tmp/outputs/plan002_additive_beta03_s42
532	  --- METRICS ---
533	    duration_min: 56.7
534	    eval_by_type_false_isr: 0.0102
535	    eval_by_type_false_pr: 0.12
536	    eval_by_type_true_isr: 0.0172
537	    eval_by_type_true_pr: 0.206
538	    eval_by_type_unknown_isr: 0.0422
539	    eval_by_type_unknown_pr: 0.195
540	    eval_data: proofwriter_fol_100.jsonl
541	    eval_isr_std: 0.0742
542	    eval_mean_isr: 0.0257
543	    eval_median_isr: 0
544	    eval_method: eval_sta.py full STA
545	    eval_n_problems: 100
546	    eval_n_proved: 18
547	    eval_prove_rate: 0.18
548	    eval_proved_only_isr: 0.1427
549	    genuine_count: 1
550	    genuine_rate: 0.0556
551	    h1_count: 14
552	    h1_rate: 0.778
553	    h7_count: 0
554	    h7_rate: 0
555	    h8_audit_note: 2026-05-15: H8 conjunction collapse added. genuine 4→1.
556	    h8_conjunction_collapse_count: 3
557	    h8_conjunction_collapse_rate: 0.1667
558	    last100_prove_rate: 0.5525
559	    overall_isr: 0.11527
560	    overall_prove_rate: 0.34025
561	    total_steps: 500
562	  h8_count (top-level): 3
563	  genuine_count (top-level): 1
564	  genuine_rate (top-level): 0.056
565	  notes: ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。
566	
567	========================================================================================================================
568	EXP_ID: plan003-eval-exec-only-r5
569	  status: DONE
570	  conclusion: success
571	  hypothesis: Full STA eval on exec-only 100-step checkpoint to measure formalization quality
572	  model: Qwen3-4B (r5 exec-only checkpoint)
573	  data_count: 100
574	  data_path: /root/solver-trace-ablation/data/proofwriter_fol_100.jsonl
575	  checkpoint: /root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json
576	  --- METRICS ---
577	    isr_by_type:
578	      true: 0.3598
579	      false: 0.1723
580	      unknown: 0.0979
581	    isr_std: 0.3194
582	    mean_isr: 0.2055
583	    prove_rate: 0.32
584	    proved_count: 32
585	    proved_only_isr: 0.6423
586	    runtime_s: 251.7
587	    total_samples: 100
588	
589	========================================================================================================================
590	EXP_ID: plan004-o1-ablation-s42
591	  status: DONE
592	  conclusion: negative
593	  hypothesis: O(1) binary ISR (fast_isr_fol) vs O(N) full STA ablation: 100-step pilot showed binary ISR ≈ exec-only (all proved samples ISR=1). 500-step full run confirms O(1) is ineffective at scale — the LOO abl
594	  model: Qwen3-4B
595	  seed: 42
596	  data_count: 500
597	  data_path: data/train_500_seed42.jsonl
598	  checkpoint: /root/autodl-tmp/outputs/plan004_fast_isr_s42/checkpoint-500
599	  --- METRICS ---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "ba6b024b-9d34-4ef3-8f56-3aea14d413d6"
}
```

</details>

---


### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt",
  "usage": {
    "total_tokens": 38204,
    "tool_uses": 11,
    "duration_ms": 67916
  },
  "last_tool_name": "Read",
  "uuid": "cbce4458-e7c1-4904-a9be-661e1394f896",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01LdNxZPqkyevFp415uWPR2q`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt",
  "limit": 400,
  "offset": 598
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "1539eb62-e1a9-46ec-8e6f-4f40570689e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeJjNSJxxXaLVUtyu4Qc2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8032,
      "cache_read_input_tokens": 29689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8032,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 69 · 2026-05-15T15:58:07.733Z_

<details><summary>↩ Tool result · `toolu_01LdNxZPqkyevFp415uWPR2q`</summary>

```text
598	  checkpoint: /root/autodl-tmp/outputs/plan004_fast_isr_s42/checkpoint-500
599	  --- METRICS ---
600	    content_independent_predicates_count: 3
601	    genuine_count: 0
602	    genuine_rate: 0
603	    h1_count: 63
604	    h1_rate: 1
605	    h7_count: 0
606	    h7_rate: 0
607	    h8_audit_note: 2026-05-15: H8 conjunction collapse added. genuine unchanged (0).
608	    h8_conjunction_collapse_count: 2
609	    h8_conjunction_collapse_rate: 0.0317
610	    mean_isr: 0.0072
611	    prove_rate: 0.63
612	  notes: NEGATIVE (expected): O(1) binary ISR (fast_isr) 训练 500 步后 eval ISR=0.0072（本质为0）。模型生成大量冗余 premise（如62+重复 ground facts），per-clause ablation 删任一重复不影响结果，ISR趋近0。与 exec-only 的 ISR 崩塌模式一致（ISR=0.003）。确认 O(1) binary ISR 退化为 exec-only——LOO ablation (O(N)) 是 ISR 携带结构信号的必要条件。此负向结果强化论文方法论贡献：O(N) 复杂度有其必要性。PR=63% 低于 exec-only s42 (93%) 和 ISR β=0.1 s42 (81%)。
613	
614	========================================================================================================================
615	EXP_ID: plan005-sta-low-s42
616	  status: DONE
617	  conclusion: negative
618	  model: Qwen3-4B
619	  data_path: /root/solver-trace-ablation/data/train_500_seed42.jsonl
620	  checkpoint: /root/autodl-tmp/outputs/plan005_sta_low_s42/checkpoint-500
621	  --- METRICS ---
622	    duration_min: 71
623	    first_rolling10_pr_ge_0.8: 178
624	    first_rolling10_pr_ge_0.9: 439
625	    last100_isr: 0.2299
626	    last100_isr_lt_pr_count: 99/100
627	    last100_isr_pr_ratio: 0.298
628	    last100_loss: 0.022752
629	    last100_prove_rate: 0.7725
630	    last50_isr: 0.2559
631	    last50_prove_rate: 0.77
632	    max_rolling10_isr: 0.3282
633	    max_rolling10_pr: 0.9375
634	    overall_isr: 0.1682
635	    overall_loss: 0.017296
636	    overall_prove_rate: 0.5657
637	    parse_rate: 1
638	    total_steps: 500
639	    windowed:
640	      1-50: {"pr": 0.1775, "isr": 0.0906}
641	      51-100: {"pr": 0.1775, "isr": 0.0835}
642	      101-200: {"pr": 0.5062, "isr": 0.1463}
643	      201-300: {"pr": 0.6713, "isr": 0.1791}
644	      301-400: {"pr": 0.7013, "isr": 0.1984}
645	      401-500: {"pr": 0.7725, "isr": 0.2299}
646	  notes: conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 "STA 抑制 reward hacking" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。
647	
648	========================================================================================================================
649	EXP_ID: plan006-prolog-exec-s42
650	  status: DONE
651	  conclusion: negative
652	  hypothesis: Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diag
653	  model: Qwen3-4B
654	  seed: 42
655	  data_count: 500
656	  data_path: data/train_500_seed42.jsonl
657	  checkpoint: /root/autodl-tmp/outputs/plan006_prolog_exec_s42/checkpoint-500
658	  --- METRICS ---
659	    by_answer_type:
660	      true: {"proved": 37, "count": 40, "pr": 0.925, "isr": 0.037}
661	      false: {"proved": 21, "count": 29, "pr": 0.724, "isr": 0.038}
662	      unknown: {"proved": 25, "count": 31, "pr": 0.806, "isr": 0.016}
663	    eval_isr_std: 0.0534
664	    eval_max_isr: 0.2
665	    eval_mean_isr: 0.031
666	    eval_median_isr: 0
667	    eval_prove_rate: 0.83
668	    eval_proved_only_isr: 0.037
669	    h1_rate: 0
670	    h7_rate: 0
671	    isr_1_rate: 0
672	    single_premise_rate: 0
673	  notes: Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。
674	
675	========================================================================================================================
676	EXP_ID: plan006-prolog-exec-s43-r3
677	  status: DONE
678	  conclusion: negative
679	  hypothesis: Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。
680	  checkpoint: /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3/checkpoint-500
681	  --- METRICS ---
682	    eval_by_type_false_isr: 0.0043
683	    eval_by_type_false_pr: 0.48
684	    eval_by_type_true_isr: 0.0078
685	    eval_by_type_true_pr: 0.5
686	    eval_by_type_unknown_isr: 0.0114
687	    eval_by_type_unknown_pr: 0.6585
688	    eval_data: proofwriter_fol_100.jsonl
689	    eval_elapsed_seconds: 868.2
690	    eval_isr_std: 0.0221
691	    eval_max_isr: 0.1
692	    eval_mean_isr: 0.0084
693	    eval_median_isr: 0
694	    eval_method: eval_sta.py full STA
695	    eval_min_isr: 0
696	    eval_n_problems: 100
697	    eval_n_proved: 56
698	    eval_prove_rate: 0.56
699	    eval_proved_only_isr: 0.015
700	    logic_type: prolog
701	    solver: PrologSolver
702	  notes: Eval 完成。PR=56% (远低于 s42 的 83%), ISR=0.0084 (与 s42 的 0.031 同量级，均极低)。proved_only_ISR=0.015。Prolog exec-only 跨 seed 表现：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008。s43 prove_rate 显著下降但 ISR 模式一致（极低，ground fact enumeration hacking）。与 FOL exec-only 类似，存在跨 seed 不稳定性（FOL: s42=93%, s43=14%, s44=98%）。等 s44 eval 完成后计算 3-seed mean±std。
703	
704	========================================================================================================================
705	EXP_ID: plan006-prolog-exec-s44
706	  status: DONE
707	  conclusion: negative
708	  hypothesis: Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std 
709	  checkpoint: /root/autodl-tmp/outputs/plan006_prolog_exec_s44/checkpoint-500
710	  --- METRICS ---
711	    eval_by_type_false_isr: 0.04
712	    eval_by_type_false_pr: 0.04
713	    eval_by_type_true_isr: 0.09
714	    eval_by_type_true_pr: 0.206
715	    eval_by_type_unknown_isr: 0.099
716	    eval_by_type_unknown_pr: 0.317
717	    eval_data: proofwriter_fol_100.jsonl
718	    eval_elapsed_seconds: 683.9
719	    eval_isr_std: 0.2343
720	    eval_max_isr: 1
721	    eval_mean_isr: 0.0812
722	    eval_median_isr: 0
723	    eval_method: eval_sta.py full STA
724	    eval_min_isr: 0
725	    eval_n_problems: 100
726	    eval_n_proved: 21
727	    eval_prove_rate: 0.21
728	    eval_proved_only_isr: 0.3866
729	    logic_type: prolog
730	    solver: PrologSolver
731	  notes: Eval 完成。PR=21% (3-seed 最低), ISR=0.081, proved_only_ISR=0.387 (max_ISR=1.0)。与 s42/s43 不同模式：PR 极低但 proved_only_ISR 较高，可能有少量样本 ISR=1 (H7-like)。Prolog exec-only 3-seed 汇总：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008, s44 PR=21%/ISR=0.081。Mean PR=53.3%±31.1%, Mean ISR=0.040±0.037。跨 seed 极不稳定（PR std=31pp），与 FOL exec-only 一致。ISR 始终极低（<0.1），确认 Prolog exec-only 不产生 genuine reasoning traces。
732	
733	========================================================================================================================
734	EXP_ID: plan006-prolog-sta-s42
735	  status: DONE
736	  conclusion: negative
737	  hypothesis: Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。
738	  model: Qwen3-4B
739	  seed: 42
740	  data_count: 500
741	  data_path: data/train_500_seed42.jsonl
742	  checkpoint: /root/autodl-tmp/outputs/plan006_prolog_sta_s42/ (may be cleaned up per C003)
743	  --- METRICS ---
744	    cumulative_mean_isr: 0.787
745	    cumulative_prove_rate: 0.848
746	    eval_h7_count: 50
747	    eval_h7_rate: 1
748	    eval_isr_distribution: binary: 50x0 + 50x1
749	    eval_mean_isr: 0.5
750	    eval_n_clauses_mean: 1
751	    eval_prove_rate: 0.5
752	    eval_proved_count: 50
753	    eval_proved_only_isr: 1
754	    eval_total_count: 100
755	    final_completion_length: 27
756	    final_entropy: 0.01
757	    final_isr: 1
758	    final_prove_rate: 1
759	    final_reward: 1
760	    initial_completion_length: 120
761	    saturation_onset_step: 100
762	    steps_at_perfect_reward: 400
763	    train_loss: 0.00716
764	    train_runtime_sec: 2791
765	    training_hours: 0.78
766	  notes: Eval metrics provenance: eval 在训练完成后立即在 westd-39279 服务器上运行 eval_sta.py，checkpoint 路径 /root/autodl-tmp/outputs/plan006_prolog_sta_s42/。Eval 结果由 Worker 从服务器 SSH 读取 eval_results.json 并手动录入 registry。Checkpoint 可能已被磁盘清理删除（C003 save_total_limit=1）。训练日志: ~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log。H7 分类由 classify_h7.py 在 eval 目录上运行。
767	
768	========================================================================================================================
769	EXP_ID: plan006-prolog-sta-s43
770	  status: DONE
771	  conclusion: negative
772	  hypothesis: Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。
773	  checkpoint: /root/autodl-tmp/outputs/plan006_prolog_sta_s43
774	  --- METRICS ---
775	    eval:
776	      n_problems: 100
777	      n_proved: 38
778	      prove_rate: 0.38
779	      mean_isr: 0.0704
780	      isr_std: 0.1263
781	      median_isr: 0
782	      proved_only_mean_isr: 0.1853
783	      min_isr: 0
784	      max_isr: 1
785	      by_answer_type: {"false": {"count": 25, "proved": 11, "prove_rate": 0.44, "mean_isr": 0.1003}, "unknown": {"count": 41, "proved": 11, "prove_rate": 0.268, "mean_isr": 0.0394}, "true": {"count": 34, "proved": 16, "prove_rate": 0.471, "mean_isr": 0.0859}}
786	    h7_classification:
787	      h7_strict: 0
788	      h7_rate: 0
789	      h1_strict: 37
790	      h1_rate: 0.974
791	      conclusion_in_premise_total: 37
792	      conclusion_in_premise_rate: 0.974
793	      genuine_count: 0
794	      genuine_rate: 0
795	      isr_1_count: 1
796	      note: 1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological
797	    train:
798	      final_prove_rate: 0.769
799	      final_mean_isr: 0.129
800	      final_loss: 0.0155
801	      final_entropy: 0.09
802	      final_reward: 0.573
803	      completion_length_mean: 143
804	      train_runtime_seconds: 5095
805	      train_runtime_minutes: 84.9
806	  notes: Eval: PR=0.38, ISR=0.185 proved-only. Strict classifier: H7=0%, H1=0%, Genuine=100%. 但功能分析显示所有 38 proved 样本 n_necessary=1（功能性 H7）。模型生成大写伪 Prolog（如 MARY_IS_AN_AVADEOTE.）—— 非标准语法，strict classifier 无法匹配 conclusion。与 s42 (clean H7=100%) 不同的 Goodhart 路径，但同样是 hacking。磁盘 240G/250G 需清理。
807	
808	========================================================================================================================
809	EXP_ID: plan006-prolog-sta-s44
810	  status: DONE
811	  conclusion: negative
812	  hypothesis: Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。
813	  checkpoint: /root/autodl-tmp/outputs/plan006_prolog_sta_s44/
814	  --- METRICS ---
815	    failure_mode: query-as-fact gaming (total H7 collapse)
816	    genuine_rate: 0
817	    h7_functional_rate: 0.979
818	    isr_mean: 0.885
819	    isr_n_cl_ge3: N/A (0 samples)
820	    n_clauses_dist: 78/100 single-clause, 22/100 two-clause
821	    pass_rate: 0.97
822	    premise_count_analysis: 100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs
823	  notes: Reviewer 独立核实: query-as-fact gaming, 0% genuine. 97/97 proved 样本中 95/97 n_necessary=1（功能性 H7）。模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。PR=0.97, ISR=0.885 是 gaming artifact（高 ISR 因单 clause = query）。第三种 Goodhart pathway（vs s42 clean H7, s43 degenerate syntax H1）。对照: s42=negative (clean H7=100%), s43=negative (uppercase pseudo-Prolog H1=97.4%), s44=negative (query-as-fact gaming, functional H7=95/97).
824	
825	========================================================================================================================
826	EXP_ID: plan009-sft-baseline-s42-1000
827	  status: DONE
828	  conclusion: success
829	  hypothesis: SFT 1000步延伸：验证 SFT（无 reward optimization）在 1000 步是否维持 genuine rate。500 步 SFT 已达 93% genuine，若 1000 步仍保持高 genuine → Goodhart collapse 是 RL (GRPO) 特有现象，非一般 finetuning 退化。与 exec-only/ISR/random 1000步形成对比
830	  model: Qwen3-4B
831	  seed: 42
832	  data_count: 500
833	  data_path: data/train_500_seed42.jsonl
834	  checkpoint: /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/checkpoint-1000
835	  --- METRICS ---
836	    conclusion_in_premise_count: 1
837	    conclusion_in_premise_rate: 0.0769
838	    content_independent_count: 0
839	    eval_by_answer_type:
840	      true: {"count": 34, "proved": 12, "prove_rate": 0.353, "mean_isr": 0.209}
841	      false: {"count": 25, "proved": 1, "prove_rate": 0.04, "mean_isr": 0.011}
842	      unknown: {"count": 41, "proved": 0, "prove_rate": 0, "mean_isr": 0}
843	    eval_data: proofwriter_fol_100.jsonl
844	    eval_isr_std: 0.2077
845	    eval_mean_isr: 0.0738
846	    eval_median_isr: 0
847	    eval_method: eval_sta.py full STA
848	    eval_n_problems: 100
849	    eval_n_proved: 13
850	    eval_output_path: /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json
851	    eval_prove_rate: 0.13
852	    eval_proved_only_isr: 0.5677
853	    genuine_count: 12
854	    genuine_rate: 0.9231
855	    h1_strict_count: 1
856	    h1_strict_rate: 0.0769
857	    h7_strict_count: 0
858	    h7_strict_rate: 0
859	    h8_conjunction_collapse_count: 0
860	    h8_conjunction_collapse_rate: 0
861	    isr_1_count: 0
862	    train_epochs: 15.88
863	    train_final_loss: 0.0168
864	    train_last_step_loss: 0.0168
865	    train_runtime_sec: 1415
866	    train_steps: 1000
867	    train_token_accuracy: 0.9955
868	  taxonomy_note (top-level): D086 补扫: proved=13, H7=0, H1=1, H8=0, genuine=12 (92.3%). SFT 1000-step 保持高 genuine rate，确认 hacking 是 RL-specific. eval: /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json
869	  h7_count (top-level): 0
870	  h1_count (top-level): 1
871	  genuine_count (top-level): 12
872	  genuine_rate (top-level): 0.923
873	  h7_rate (top-level): 0
874	  h1_rate (top-level): 7.7
875	  notes: SFT 1000步 (15.88 epochs): train loss 降至 0.0168（严重过拟合），但 eval genuine_rate=92.31% 与 500步的 92.9% 基本持平。prove_rate 从 0.14 微降至 0.13，h7=0，h1=1。结论：SFT 即使过拟合也不产生 Goodhart collapse（h7/h8=0），验证了 Goodhart 是 RL(GRPO) reward optimization 特有现象。Unknown 类全部 0/41 未 prove（与 500步一致），SFT 不具备泛化到 unknown 类的能力。
876	  parent: plan009-sft-baseline-s42-r4
877	
878	========================================================================================================================
879	EXP_ID: plan009-sft-baseline-s42-r4
880	  status: DONE
881	  conclusion: success
882	  hypothesis: SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4:
883	  model: Qwen3-4B
884	  seed: 42
885	  data_count: 500
886	  data_path: data/train_500_seed42.jsonl
887	  checkpoint: /root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/
888	  --- METRICS ---
889	    by_answer_type:
890	      true: {"count": 34, "proved": 13, "pr": 0.382, "isr": 0.226}
891	      unknown: {"count": 41, "proved": 1, "pr": 0.024, "isr": 0.008}
892	      false: {"count": 25, "proved": 0, "pr": 0, "isr": 0}
893	    eval_data: proofwriter_fol_100.jsonl
894	    eval_isr_std: 0.214
895	    eval_max_isr: 0.833
896	    eval_mean_isr: 0.08
897	    eval_median_isr: 0
898	    eval_method: eval_sta.py full STA
899	    eval_n_problems: 100
900	    eval_n_proved: 14
901	    eval_prove_rate: 0.14
902	    eval_proved_only_isr: 0.571
903	    genuine_count: 13
904	    genuine_rate: 0.929
905	    h1_count: 1
906	    h1_rate: 0.071
907	    h7_count: 0
908	    h7_rate: 0
909	    hacking_patterns: near-zero (1/14 H1, 0 H7, 92.9% genuine)
910	    tautological_collapse: False
911	    train_epochs: 7.94
912	    train_final_loss: 0.0287
913	    train_runtime_sec: 789.6
914	    train_token_accuracy: 0.9935
915	  notes: r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。
916	  parent: plan009-sft-baseline-s42-r2
917	
918	========================================================================================================================
919	EXP_ID: plan009-sft-baseline-s43
920	  status: DONE
921	  conclusion: success
922	  model: Qwen3-4B
923	  seed: 43
924	  data_count: 500
925	  data_path: data/train_500_seed42.jsonl
926	  checkpoint: /root/autodl-tmp/outputs/plan009_sft_baseline_s43
927	  --- METRICS ---
928	    by_answer_type:
929	      true: {"count": 34, "proved": 13, "prove_rate": 0.382, "mean_isr": 0.234}
930	      false: {"count": 25, "proved": 1, "prove_rate": 0.04, "mean_isr": 0.027}
931	      unknown: {"count": 41, "proved": 1, "prove_rate": 0.024, "mean_isr": 0.008}
932	    eval_data_path: data/proofwriter_fol_100.jsonl
933	    eval_isr_std: 0.2338
934	    eval_mean_isr: 0.0895
935	    eval_median_isr: 0
936	    eval_output_path: /root/autodl-tmp/outputs/eval_sta_plan009_sft_s43.json
937	    eval_prove_rate: 0.15
938	    eval_proved_only_isr: 0.5967
939	    genuine_count: 14
940	    genuine_rate: 0.933
941	    h1_count: 1
942	    h1_rate: 0.067
943	    h7_count: 0
944	    h7_rate: 0
945	    train_epochs: 7.94
946	    train_loss: 0.2391
947	    train_runtime_sec: 677.14
948	    train_steps: 500
949	    train_token_accuracy: 0.9938
950	
951	========================================================================================================================
952	EXP_ID: plan009-sft-baseline-s43-1000
953	  status: DONE
954	  conclusion: success
955	  hypothesis: SFT 1000步 seed=43：与 s42 相同配置的第二个 seed，验证 SFT 在 1000 步的 genuine rate 稳定性。与 GRPO 各条件 1000步对比，确认 Goodhart collapse 是 RL 特有现象。
956	  model: Qwen3-4B
957	  seed: 43
958	  data_count: 500
959	  data_path: data/train_500_seed42.jsonl
960	  checkpoint: /root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/checkpoint-1000
961	  --- METRICS ---
962	    by_answer_type:
963	      true: {"count": 34, "proved": 11, "prove_rate": 0.3235}
964	      false: {"count": 25, "proved": 0, "prove_rate": 0}
965	      unknown: {"count": 41, "proved": 0, "prove_rate": 0}
966	    conclusion_in_premise_count: 1
967	    conclusion_in_premise_rate: 0.0909
968	    content_independent_count: 0
969	    content_independent_rate: 0
970	    eval_elapsed_s: 326.1
971	    genuine_count: 10
972	    genuine_rate: 0.9091
973	    h1_strict_count: 1
974	    h1_strict_rate: 0.0909
975	    h7_strict_count: 0
976	    h7_strict_rate: 0
977	    h8_conjunction_collapse_count: 0
978	    h8_conjunction_collapse_rate: 0
979	    isr_1_count: 1
980	    isr_1_rate: 0.0909
981	    isr_std: 0.2155
982	    mean_isr: 0.0699
983	    median_isr: 0
984	    n_problems: 100
985	    n_proved: 11
986	    prove_rate: 0.11
987	    proved_only_mean_isr: 0.6352
988	    train_avg_loss: 0.1551
989	    train_final_loss: 0.0167
990	    train_runtime_s: 1584.79
991	    train_token_accuracy: 0.9954
992	  taxonomy_note (top-level): D086 补扫: proved=11, H7=0, H1=1, H8=0, genuine=10 (90.9%). SFT 1000-step s43 保持高 genuine rate. eval: /root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/eval_sta_results.json
993	  genuine_count (top-level): 10
994	  genuine_rate (top-level): 0.909
995	  notes: SFT s43 1000步结果与 s42 高度一致：prove_rate 11% vs 13%（-2pp），mean_isr 0.0699 vs 0.0738，final_loss 0.0167 vs 0.0168。差异在 seed 方差范围内。SFT baseline 稳定。注意：eval_sta.py 当前版本不输出 h7/h1/h8/genuine 分类指标。
996	  parent: plan009-sft-baseline-s43
997	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "38985fb6-2d70-469a-985c-87d8077f1f01"
}
```

</details>

---


### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt",
  "usage": {
    "total_tokens": 47148,
    "tool_uses": 12,
    "duration_ms": 73187
  },
  "last_tool_name": "Read",
  "uuid": "410a2afd-ffa7-406b-a4d3-e5ee78f6fbd3",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_01LTgvFZ7JHjoH9HCxaANN3E`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt",
  "limit": 500,
  "offset": 997
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "16f0d5c1-0ce1-4e65-9d64-5347ed54e938",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhajCxyveHNsAb1cyNwcGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8906,
      "cache_read_input_tokens": 37721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8906,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 72 · 2026-05-15T15:58:12.983Z_

<details><summary>↩ Tool result · `toolu_01LTgvFZ7JHjoH9HCxaANN3E`</summary>

```text
997	
998	========================================================================================================================
999	EXP_ID: plan009-sft-baseline-s44
1000	  status: DONE
1001	  conclusion: success
1002	  model: Qwen3-4B
1003	  seed: 44
1004	  data_count: 500
1005	  data_path: data/train_500_seed42.jsonl
1006	  checkpoint: /root/autodl-tmp/outputs/plan009_sft_baseline_s44
1007	  --- METRICS ---
1008	    eval_by_answer_type:
1009	      true: {"count": 34, "proved": 15, "prove_rate": 0.441, "mean_isr": 0.257}
1010	      false: {"count": 25, "proved": 1, "prove_rate": 0.04, "mean_isr": 0.027}
1011	      unknown: {"count": 41, "proved": 1, "prove_rate": 0.024, "mean_isr": 0.008}
1012	    eval_correction_note: Corrected 2026-05-15: previous eval used test_100.jsonl (50/44/6 distribution), re-evaled with proofwriter_fol_100.jsonl (34/25/41)
1013	    eval_data: proofwriter_fol_100.jsonl
1014	    eval_genuine_count: 15
1015	    eval_genuine_rate: 0.882
1016	    eval_h1_count: 2
1017	    eval_h1_rate: 0.118
1018	    eval_h7_count: 0
1019	    eval_h7_rate: 0
1020	    eval_isr_std: 0.2409
1021	    eval_mean_isr: 0.0974
1022	    eval_median_isr: 0
1023	    eval_method: eval_sta.py full STA
1024	    eval_n_problems: 100
1025	    eval_n_proved: 17
1026	    eval_output_path: /root/autodl-tmp/outputs/eval_sta_plan009_sft_s44.json
1027	    eval_prove_rate: 0.17
1028	    eval_proved_only_isr: 0.5729
1029	    eval_tautological_collapse: False
1030	    train_epochs: 7.94
1031	    train_final_loss: 0.2397
1032	    train_last_step_loss: 0.0328
1033	    train_runtime_sec: 729.05
1034	    train_steps: 500
1035	    train_token_accuracy: 0.9928
1036	
1037	========================================================================================================================
1038	EXP_ID: plan009-sft-baseline-s44-1000
1039	  status: DONE
1040	  conclusion: success
1041	  hypothesis: SFT 1000步 seed=44：与 s42/s43 相同配置的第三个 seed，验证 SFT 在 1000 步的 genuine rate 稳定性。3-seed 统计支撑 Goodhart collapse 是 RL (GRPO) 特有现象的 claim。
1042	  model: Qwen3-4B
1043	  seed: 44
1044	  data_count: 500
1045	  data_path: data/train_500_seed42.jsonl
1046	  checkpoint: /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/checkpoint-1000
1047	  --- METRICS ---
1048	    by_answer_type:
1049	      true: {"count": 34, "proved": 15, "prove_rate": 0.4412}
1050	      false: {"count": 25, "proved": 0, "prove_rate": 0}
1051	      unknown: {"count": 41, "proved": 0, "prove_rate": 0}
1052	    conclusion_in_premise_count: 1
1053	    conclusion_in_premise_rate: 0.0667
1054	    content_independent_count: 0
1055	    content_independent_rate: 0
1056	    eval_elapsed_s: 391.8
1057	    genuine_count: 14
1058	    genuine_rate: 0.9333
1059	    h1_strict_count: 1
1060	    h1_strict_rate: 0.0667
1061	    h7_strict_count: 0
1062	    h7_strict_rate: 0
1063	    h8_conjunction_collapse_count: 0
1064	    h8_conjunction_collapse_rate: 0
1065	    isr_1_count: 0
1066	    isr_1_rate: 0
1067	    isr_std: 0.2268
1068	    max_isr: 0.8571
1069	    mean_isr: 0.0884
1070	    median_isr: 0
1071	    n_problems: 100
1072	    n_proved: 15
1073	    prove_rate: 0.15
1074	    proved_only_mean_isr: 0.5892
1075	    train_avg_loss: 0.1544
1076	    train_final_loss: 0.0171
1077	    train_runtime_s: 1580.97
1078	    train_token_accuracy: 0.995
1079	  taxonomy_note (top-level): D086 补扫: proved=15, H7=0, H1=1, H8=0, genuine=14 (93.3%). SFT 1000-step s44 保持高 genuine rate. eval: /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/eval_sta_results.json
1080	  genuine_rate (top-level): 0.933
1081	  notes: SFT s44 1000步 r3 成功（r1 OOM 因 GPU 冲突）。prove_rate=0.15 略高于 s42(0.13)/s43(0.11)，genuine_rate=93.3% 稳定高。3-seed SFT 均 genuine_rate>90% 无 Goodhart collapse。
1082	  failure_reason: CUDA OOM: CUDA out of memory. Tried to allocate 742.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 100.25 MiB is free. Process 352142 has 62.36 GiB memory in use. Including non-PyTorch memor
1083	  parent: plan009-sft-baseline-s42-r4
1084	
1085	========================================================================================================================
1086	EXP_ID: plan009-sft-baseline-s44-1000-r3
1087	  status: DONE
1088	  conclusion: success
1089	  hypothesis: SFT 1000步 seed=44（第三次重试）：r1/r2 均因 --gpu 0 覆盖 CUDA_VISIBLE_DEVICES 导致 OOM。本次用 --gpu 1 直接指定物理 GPU 1。验证 SFT 在 1000 步的 genuine rate 稳定性，完成 3-seed 统计。
1090	  model: Qwen3-4B
1091	  seed: 44
1092	  data_count: 500
1093	  data_path: data/train_500_seed42.jsonl
1094	  checkpoint: /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000
1095	  --- METRICS ---
1096	    eval_by_answer_type:
1097	      true: {"count": 34, "proved": 15, "prove_rate": 0.441, "mean_isr": 0.26}
1098	      false: {"count": 25, "proved": 0, "prove_rate": 0, "mean_isr": 0}
1099	      unknown: {"count": 41, "proved": 0, "prove_rate": 0, "mean_isr": 0}
1100	    eval_data: proofwriter_fol_100.jsonl
1101	    eval_isr_std: 0.2268
1102	    eval_mean_isr: 0.0884
1103	    eval_median_isr: 0
1104	    eval_method: eval_sta.py full STA
1105	    eval_n_problems: 100
1106	    eval_n_proved: 15
1107	    eval_prove_rate: 0.15
1108	    eval_proved_only_isr: 0.5892
1109	    genuine_count: 14
1110	    genuine_rate: 0.9333
1111	    h1_count: 1
1112	    h1_rate: 0.0667
1113	    h7_count: 0
1114	    h7_rate: 0
1115	    h8_conjunction_collapse_count: 0
1116	    h8_conjunction_collapse_rate: 0
1117	  parent: plan009-sft-baseline-s44-1000-r2
1118	
1119	========================================================================================================================
1120	EXP_ID: plan012-hacking-taxonomy
1121	  status: DONE
1122	  conclusion: success
1123	  hypothesis: ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utili
1124	  model: N/A (rule-based analysis)
1125	  seed: N/A
1126	  data_count: 160
1127	  data_path: eval_results.json from plan002-b01-s42 + plan018-b01-s42
1128	  checkpoint: N/A (analysis task)
1129	  --- METRICS ---
1130	    genuine_rate_delta_pp: 8.2
1131	    isr_b01_complexity_wo_utility_rate: 0
1132	    isr_b01_conclusion_embedding_rate: 0.728
1133	    isr_b01_genuine_mean_isr: 0.6723
1134	    isr_b01_genuine_rate: 0.259
1135	    isr_b01_hacking_rate: 0.741
1136	    random_b01_complexity_wo_utility_rate: 0.038
1137	    random_b01_conclusion_embedding_rate: 0.785
1138	    random_b01_genuine_mean_isr: 0.3427
1139	    random_b01_genuine_rate: 0.177
1140	    random_b01_hacking_rate: 0.823
1141	  notes: D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。
1142	
1143	========================================================================================================================
1144	EXP_ID: plan013-random-reward-s42-r4
1145	  status: DONE
1146	  conclusion: success
1147	  hypothesis: Random reward baseline: replacing ISR with random values should degrade structural quality while maintaining execution reward, proving ISR's causal contribution
1148	  model: Qwen3-4B
1149	  seed: 42
1150	  data_count: 500
1151	  data_path: /root/solver-trace-ablation/data/train_500_seed42.jsonl
1152	  checkpoint: /root/autodl-tmp/outputs/plan013_random_reward_s42_r4/checkpoint-500
1153	  --- METRICS ---
1154	    eval_data: proofwriter_fol_100.jsonl
1155	    eval_isr_std: 0.1282
1156	    eval_mean_isr: 0.535
1157	    eval_median_isr: 0.5
1158	    eval_method: eval_sta.py full STA
1159	    eval_n_problems: 100
1160	    eval_n_proved: 100
1161	    eval_note: DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure
1162	    eval_prove_rate: 1
1163	    eval_proved_only_isr: 0.535
1164	  taxonomy_note (top-level): D086 补扫: proved=100, H7=100(100%), H1=0, H8=0, genuine=0 (0%). Convex random reward (0.9·r_exec+0.1·random) 100% tautological collapse. eval: /root/solver-trace-ablation/outputs/eval_sta_plan013_random_reward_s42_r4.json
1165	  notes: ⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。
1166	
1167	========================================================================================================================
1168	EXP_ID: plan014-downstream-nli-s42
1169	  status: DONE
1170	  conclusion: negative
1171	  hypothesis: Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。
1172	  checkpoint: /root/autodl-tmp/outputs/plan014_downstream_nli.json
1173	  --- METRICS ---
1174	    accuracy_by_label:
1175	      true: 0.912
1176	      false: 0
1177	      unknown: 0.076
1178	    bon_isr_accuracy: 0.35
1179	    bon_oracle_accuracy: 0.44
1180	    bon_prove_first_accuracy: 0.35
1181	    bon_random_accuracy: 0.341
1182	    isr_bucket_high_acc: 0.75
1183	    isr_bucket_low_acc: 0.327
1184	    isr_bucket_mid_acc: 0.377
1185	    mann_whitney_U: 17202
1186	    mann_whitney_p: 0.288
1187	    overall_accuracy: 0.341
1188	    parse_errors: 0
1189	    proved_count: 732
1190	    proved_rate: 0.915
1191	    runtime_eval_s: 13.6
1192	    runtime_inference_s: 408.8
1193	    spearman_p: 0.187
1194	    spearman_rho: -0.049
1195	    total_generations: 800
1196	  notes: Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。
1197	  failure_reason: EXIT_CODE=1 (generic error — check log tail)
1198	
1199	========================================================================================================================
1200	EXP_ID: plan016-extended-1000-s42
1201	  status: DONE
1202	  conclusion: success
1203	  hypothesis: Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？
1204	  model: Qwen3-4B
1205	  seed: 42
1206	  num_steps: 1000
1207	  data_count: 500
1208	  data_path: /root/solver-trace-ablation/data/train_500_seed42.jsonl
1209	  checkpoint: /root/autodl-tmp/outputs/plan016_extended_1000_s42
1210	  --- METRICS ---
1211	    components: 18.55
1212	    genuine_count: 0
1213	    genuine_rate: 0
1214	    h1_count: 96
1215	    h1_rate: 1
1216	    h7_count: 0
1217	    h7_rate: 0
1218	    isr: 0.003
1219	    n_proved: 96
1220	    prove_rate: 0.96
1221	  notes: Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\n\n## 500 vs 1000 step comparison (eval_sta.py):\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\n|--------|-------------------|-----------------|--------|\n| eval PR | 0.93 | 0.96 | +3.2% |\n| eval ISR | 0.123 | 0.0027 | -97.8% |\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\n| components | 6.58 | 18.55 | +182% |\n| ISR=0 ratio | - | 94.8% | - |\n| n_necessary=0 ratio | - | 94.8% | - |\n\n## Key findings:\
1222	  parent: plan001-exec-only-s42-r2
1223	
1224	========================================================================================================================
1225	EXP_ID: plan017-additive-random-s42
1226	  status: DONE
1227	  conclusion: negative
1228	  hypothesis: Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal
1229	  model: Qwen3-4B
1230	  beta: 0.3
1231	  seed: 42
1232	  data_count: 500
1233	  data_path: /root/solver-trace-ablation/data/train_500_seed42.jsonl
1234	  checkpoint: /root/autodl-tmp/outputs/plan017_additive_random_s42
1235	  --- METRICS ---
1236	    eval_component_count_2_ratio: 0
1237	    eval_component_count_mean: 9.6
1238	    eval_data: proofwriter_fol_100.jsonl
1239	    eval_isr_std: 0.0759
1240	    eval_max_isr: 0.2857
1241	    eval_mean_isr: 0.0453
1242	    eval_median_isr: 0
1243	    eval_method: eval_sta.py full STA
1244	    eval_n_problems: 100
1245	    eval_n_proved: 48
1246	    eval_prove_rate: 0.48
1247	    eval_proved_only_isr: 0.0943
1248	    genuine_count: 0
1249	    genuine_rate: 0
1250	    h1_count: 48
1251	    h1_rate: 1
1252	    h7_count: 0
1253	    h7_rate: 0
1254	    tautological_collapse: False
1255	  taxonomy_note (top-level): D086 clean run: H7a=4 (new, deeper normalization), H7b=0, H1=44, H8=0, genuine=0. β=0.3 Random also produces H7 under higher reward pressure.
1256	  h1_count (top-level): 44
1257	  notes: Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.
1258	  parent: plan013-random-reward-s42-r4
1259	
1260	========================================================================================================================
1261	EXP_ID: plan018-additive-random-b01-s42
1262	  status: DONE
1263	  conclusion: negative
1264	  hypothesis: β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 va
1265	  model: Qwen3-4B
1266	  seed: 42
1267	  num_steps: 500
1268	  data_count: 500
1269	  data_path: data/train_500_seed42.jsonl
1270	  checkpoint: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42
1271	  --- METRICS ---
1272	    eval_isr_std: 0.1369
1273	    eval_mean_isr: 0.1038
1274	    eval_median_isr: 0.0357
1275	    eval_n_problems: 100
1276	    eval_n_proved: 79
1277	    eval_prove_rate: 0.79
1278	    eval_proved_only_isr: 0.1314
1279	    genuine_count_exact_h1: 23
1280	    genuine_count_strict: 12
1281	    genuine_rate_exact_h1: 0.2911
1282	    genuine_rate_strict: 0.1519
1283	    h1_count: 56
1284	    h1_near_count: 8
1285	    h1_near_rate: 0.1013
1286	    h1_rate: 0.7089
1287	    h7_count: 0
1288	    h7_rate: 0
1289	    h8_conjunction_collapse_count: 3
1290	    h8_conjunction_collapse_rate: 0.038
1291	    tautological_collapse: False
1292	    taxonomy_verification: 2026-05-15: full re-verification from eval_sta file. H1 exact=56, H1-near(substring)=8 (5 conc_in_prem + 3 prem_in_conc), H8=3, strict genuine=12. Registry original genuine=23 = H8(3) + H1-near(8) + strict genuine(12).
1293	  taxonomy_note (top-level): D086 clean run (ground truth): H7=0, H1=58, H8=4, genuine=18 (22.8%). 1 H1∩H8 overlap sample; genuine computed from set union (|H7∪H1∪H8|=61), not simple subtraction (0+58+4=62). genuine = 79 − 61 = 18.
1294	  h7_count (top-level): 0
1295	  h1_count (top-level): 58
1296	  h8_count (top-level): 4
1297	  genuine_count (top-level): 18
1298	  genuine_rate (top-level): 0.228
1299	  notes: Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。
1300	
1301	对比 plan002-b01 (ISR β=0.1):
1302	- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)
1303	- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)
1304	- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)
1305	- Median ISR: 0.036 vs plan002未记录
1306	- Component count: 8.46 vs 5.58 (random组更多冗余)
1307	- ISR=0占比(proved): 36.7% (random组大量proof无结构)
1308	- Tautological collapse: 无 (component_2_ratio=0)
1309	
1310	关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供g
1311	  parent: plan002-additive-b01-s42
1312	
1313	========================================================================================================================
1314	EXP_ID: plan018-additive-random-b01-s42-1000-r2
1315	  status: DONE
1316	  conclusion: negative
1317	  checkpoint: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000
1318	  --- METRICS ---
1319	    eval_component_count_mean: 3
1320	    eval_isr_std: 0
1321	    eval_mean_isr: 0.3333
1322	    eval_median_isr: 0.3333
1323	    eval_n_problems: 100
1324	    eval_n_proved: 100
1325	    eval_prove_rate: 1
1326	    eval_proved_only_isr: 0.3333
1327	    genuine_count: 0
1328	    genuine_rate: 0
1329	    h1_count: None
1330	    h1_rate: None
1331	    h7_count: None
1332	    h7_rate: None
1333	    tautological_collapse: True
1334	    train_final_mean_isr: 0.353
1335	    train_final_prove_rate: 0.989
1336	    train_final_reward: 1.062
1337	    train_runtime_seconds: 2957
1338	    train_steps: 1000
1339	
1340	========================================================================================================================
1341	EXP_ID: plan018-additive-random-b01-s42-1000-r3
1342	  status: DONE
1343	  conclusion: negative
1344	  checkpoint: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3/checkpoint-1000
1345	  --- METRICS ---
1346	    eval_by_answer_type:
1347	      false: {"count": 25, "proved": 25, "prove_rate": 1, "mean_isr": 0.7533}
1348	      unknown: {"count": 41, "proved": 39, "prove_rate": 0.951, "mean_isr": 0.6565}
1349	      true: {"count": 34, "proved": 33, "prove_rate": 0.971, "mean_isr": 0.6814}
1350	    eval_isr_std: 0.2037
1351	    eval_mean_isr: 0.6892
1352	    eval_median_isr: 0.75
1353	    eval_n_problems: 100
1354	    eval_n_proved: 97
1355	    eval_prove_rate: 0.97
1356	    eval_proved_only_isr: 0.7105
1357	    genuine_count: 0
1358	    genuine_rate: 0
1359	    h1_count: 0
1360	    h1_rate: 0
1361	    h7_count: 97
1362	    h7_rate: 1
1363	    n_premise_distribution:
1364	      1: 97
1365	    pattern_description: All 97 proved: 1 premise identical to conclusion (P therefore P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix).
1366	    tautological_collapse: True
1367	    train_final_entropy: 0.003
1368	    train_final_mean_isr: 0.5213
1369	    train_final_prove_rate: 0.827
1370	    train_loss: 0.00671
1371	    train_runtime_seconds: 5783
1372	    train_steps: 1000
1373	  taxonomy_note (top-level): D088 修正: metrics 字段已同步 (h7=97, h1=0, genuine=0, 全 H7a). D086 clean run classify_h7 确认 97/97 proved 均为 single_premise=conclusion (H7 tautology). 之前 metrics 残留 h1=97/h7=0 是 D086 前 classify_h7 bug 导致的错误分类. ⚠️ batch_h7ab_clean.json 中 plan018_additive_random_b01_s42_1000 条目处理的是原始失败实验(proved=100)非 r3(proved=97), 不可引用.
1374	  h7_count (top-level): 97
1375	  h1_count (top-level): 0
1376	  h8_count (top-level): 0
1377	  genuine_count (top-level): 0
1378	
1379	========================================================================================================================
1380	EXP_ID: plan018-additive-random-b01-s43-r2
1381	  status: DONE
1382	  conclusion: negative
1383	  hypothesis: Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。
1384	  --- METRICS ---
1385	    eval_mean_isr: 0.058
1386	    eval_prove_rate: 0.88
1387	    genuine_count: 6
1388	    genuine_rate: 6.8
1389	    h1_count: 82
1390	    h1_rate: 93.2
1391	    h7_count: 0
1392	    h7_rate: 0
1393	  parent: plan018-additive-random-b01-s43
1394	
1395	========================================================================================================================
1396	EXP_ID: plan018-additive-random-b01-s44
1397	  status: DONE
1398	  conclusion: success
1399	  hypothesis: Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。
1400	  model: Qwen3-4B
1401	  seed: 44
1402	  num_steps: 500
1403	  data_count: 500
1404	  data_path: data/train_500_seed42.jsonl
1405	  checkpoint: /root/autodl-tmp/outputs/plan018_additive_random_b01_s44/checkpoint-500
1406	  --- METRICS ---
1407	    by_answer_type:
1408	      false: {"count": 25, "proved": 21, "prove_rate": 0.84, "mean_isr": 0.0533}
1409	      unknown: {"count": 41, "proved": 40, "prove_rate": 0.976, "mean_isr": 0.0892}
1410	      true: {"count": 34, "proved": 28, "prove_rate": 0.824, "mean_isr": 0.0353}
1411	    elapsed_seconds: 1012.7
1412	    eval_method: eval_sta.py with Prover9Solver, FOL
1413	    isr_one_count: 2
1414	    isr_pr_ratio: 0.0695
1415	    isr_std: 0.1756
1416	    isr_zero_count: 72
1417	    max_isr: 1
1418	    mean_isr: 0.0619
1419	    median_isr: 0
1420	    min_isr: 0
1421	    n_problems: 100
1422	    n_proved: 89
1423	    prove_rate: 0.89
1424	    proved_only_mean_isr: 0.0695
1425	  notes: DONE (success). Random β=0.1 s44 对照分析完成: PR=0.89/ISR=0.062 (clean) vs ISR β=0.1 s44 PR=0.89/ISR=0.803 (H7=86.5% inflated). 同 PR 下 ISR reward 导致 conclusion duplication，random 无此问题。与 s42 结论一致: ISR s42 genuine ISR=0.337 vs Random s42 ISR=0.104 (3.2x)。Random 2/3 seeds done, 等 s43 (plan018-random-b01-s43-r2 QUEUED)。
1426	  parent: plan018-additive-random-b01-s42
1427	
1428	========================================================================================================================
1429	EXP_ID: sta-gt-isr-baseline
1430	  status: DONE
1431	  conclusion: success
1432	  model: ground-truth-fol
1433	  data_count: 100
1434	  data_path: /root/solver-trace-ablation/data/proofwriter_fol_100.jsonl
1435	  checkpoint: /root/solver-trace-ablation/outputs/gt_isr_baseline.json
1436	  --- METRICS ---
1437	    gt_isr_median: 0.6125
1438	    gt_isr_std: 0.2582
1439	    gt_mean_isr: 0.5588
1440	    gt_prove_rate: 0.18
1441	    solver_execution_rate: 1
1442	    true_mean_isr: 0.5833
1443	    true_prove_rate: 0.5
1444	
1445	========================================================================================================================
1446	EXP_ID: sta-phase0-baseline
1447	  status: DONE
1448	  conclusion: success
1449	  hypothesis: 锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）
1450	  model: Qwen3-4B
1451	  data_count: 100
1452	  data_path: /root/solver-trace-ablation/data/proofwriter_fol_100.jsonl
1453	  checkpoint: /root/solver-trace-ablation/outputs/phase0_baseline.json
1454	  --- METRICS ---
1455	    avg_time_per_sample_s: 3.4
1456	    effective_prove_rate_no_xor: 0.182
1457	    isr_by_answer:
1458	      true: {"n": 34, "proved": 9, "prove_rate": 0.265, "mean_isr": 0.1345}
1459	      false: {"n": 25, "proved": 1, "prove_rate": 0.04, "mean_isr": 0.024}
1460	      unknown: {"n": 41, "proved": 2, "prove_rate": 0.049, "mean_isr": 0.0302}
1461	    isr_range: [0, 0.889]
1462	    isr_std: 0.1983
1463	    mean_isr: 0.0641
1464	    median_isr: 0
1465	    prove_rate: 0.12
1466	    proved_count: 12
1467	    total_runtime_s: 336
1468	    total_samples: 100
1469	    xor_affected_samples: 34
1470	
1471	========================================================================================================================
1472	EXP_ID: sta-phase1-exec-only-r4
1473	  status: DONE
1474	  conclusion: negative
1475	  checkpoint: /root/autodl-tmp/outputs/grpo_exec_only/
1476	  --- METRICS ---
1477	    first20_reward_mean: 0.119
1478	    last20_isr_mean: 0.2
1479	    last20_prove_rate: 0.2
1480	    mean_isr: 0.1475
1481	    parse_rate: 1
1482	    prove_rate: 0.15125
1483	    training_minutes: 15
1484	    training_steps: 100
1485	  notes: Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8
1486	
1487	========================================================================================================================
1488	EXP_ID: sta-phase1-exec-only-r5
1489	  status: DONE
1490	  conclusion: success
1491	  hypothesis: K=8 增加 within-group variance，减少全零 reward batch，使 GRPO 有更多有效梯度信号
1492	  model: Qwen3-4B
1493	  seed: 42
1494	  data_count: 500
1495	  data_path: /root/solver-trace-ablation/data/proofwriter_fol_500.jsonl
1496	  checkpoint: /root/autodl-tmp/outputs/grpo_exec_only/
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "0267c560-3b15-4924-a9e4-8d020f1ae0d7"
}
```

</details>

---


### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt",
  "usage": {
    "total_tokens": 57837,
    "tool_uses": 13,
    "duration_ms": 78067
  },
  "last_tool_name": "Read",
  "uuid": "0ce3a683-3592-479b-a113-13e1387a0a2f",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_015HzUQfQUm9jiBjguekSm9e`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/bscwo2yqt.txt",
  "limit": 200,
  "offset": 1496
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "4d88710a-327c-4791-829d-faee017a5e21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUvGqfrWaE4WL5yMJqJbyS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10651,
      "cache_read_input_tokens": 46627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10651,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 75 · 2026-05-15T15:58:17.861Z_

<details><summary>↩ Tool result · `toolu_015HzUQfQUm9jiBjguekSm9e`</summary>

```text
1496	  checkpoint: /root/autodl-tmp/outputs/grpo_exec_only/
1497	  --- METRICS ---
1498	    K: 8
1499	    first20_isr_mean: 0.11875
1500	    first20_prove_rate: 0.11875
1501	    isr_pr_ratio_last20: 1
1502	    last20_isr_mean: 0.2
1503	    last20_prove_rate: 0.2
1504	    last20_reward_mean: 0.2
1505	    mean_isr: 0.1475
1506	    overall_reward_mean: 0.15125
1507	    parse_rate: 1
1508	    prove_rate: 0.15125
1509	    step_time_s: 9.44
1510	    training_minutes: 15.7
1511	    training_steps: 100
1512	
1513	========================================================================================================================
1514	EXP_ID: sta-phase1-exec-sta-r4
1515	  status: DONE
1516	  conclusion: negative
1517	  checkpoint: /root/autodl-tmp/outputs/grpo_exec_sta/
1518	  --- METRICS ---
1519	    first20_reward_mean: 0.119
1520	    last20_isr_mean: 0.2125
1521	    last20_prove_rate: 0.2125
1522	    mean_isr: 0.1525
1523	    parse_rate: 1
1524	    prove_rate: 0.1575
1525	    training_minutes: 15
1526	    training_steps: 100
1527	  notes: Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8
1528	
1529	========================================================================================================================
1530	EXP_ID: sta-phase1-exec-sta-r5
1531	  status: DONE
1532	  conclusion: negative
1533	  hypothesis: Full STA continuous ISR (0.0-1.0) 作为 reward 组件，应在训练中产生与 execution-only 不同的 ISR 趋势——execution-only ISR 随 prove_rate 上升而虚高(reward hacking)，execution+STA ISR 维持真实水平(STA 抑制 hacking)
1534	  model: Qwen3-4B
1535	  seed: 42
1536	  data_count: 500
1537	  data_path: /root/solver-trace-ablation/data/proofwriter_fol_500.jsonl
1538	  checkpoint: /root/autodl-tmp/outputs/grpo_exec_sta/
1539	  --- METRICS ---
1540	    K: 8
1541	    first20_isr_mean: 0.05182
1542	    first20_prove_rate: 0.08125
1543	    isr_pr_ratio_last20: 0.33
1544	    isr_pr_ratio_overall: 0.43
1545	    last20_isr_mean: 0.04956
1546	    last20_prove_rate: 0.15
1547	    last20_reward_mean: 0.09978
1548	    mean_isr: 0.04347
1549	    overall_reward_mean: 0.07174
1550	    parse_rate: 1
1551	    prove_rate: 0.1
1552	    step_time_s: 10.13
1553	    training_minutes: 16.9
1554	    training_steps: 100
1555	
1556	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "dc142f1c-59f1-4d09-a87e-9e4e8306da46"
}
```

</details>

---


### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Running Generate comprehensive structured metrics table",
  "usage": {
    "total_tokens": 59047,
    "tool_uses": 14,
    "duration_ms": 108835
  },
  "last_tool_name": "Bash",
  "uuid": "3740c591-d12c-4e55-9fa0-f609af63f232",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rz7brApVuf6FP7nsxW1LnZ`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Filter and extract structured data\nrows = []\nfor eid, e in exps.items():\n    conclusion = (e.get('conclusion') or '').lower()\n    if conclusion not in ('success', 'negative'):\n        continue\n    \n    m = e.get('metrics', {}) or {}\n    spec = e.get('spec', {}) or {}\n    \n    # Normalize metric extraction - handle nested 'eval' dict in some experiments\n    eval_nested = m.get('eval', {}) if isinstance(m.get('eval'), dict) else {}\n    h7_nested = m.get('h7_classification', {}) if isinstance(m.get('h7_classification'), dict) else {}\n    train_nested = m.get('train', {}) if isinstance(m.get('train'), dict) else {}\n    \n    def get_metric(*keys, default=None):\n        \"\"\"Try multiple key variants to find a metric\"\"\"\n        for k in keys:\n            # Check in metrics\n            if k in m and m[k] is not None:\n                return m[k]\n            # Check in nested eval\n            if k in eval_nested:\n                return eval_nested[k]\n            # Check in h7_classification  \n            if k in h7_nested:\n                return h7_nested[k]\n            # Check in train nested\n            if k in train_nested:\n                return train_nested[k]\n            # Check top-level experiment\n            if k in e and e[k] is not None:\n                return e[k]\n        return default\n    \n    row = {\n        'exp_id': eid,\n        'conclusion': conclusion,\n        'reward_mode': spec.get('reward_mode', ''),\n        'beta': spec.get('beta', ''),\n        'seed': spec.get('seed', ''),\n        'steps': spec.get('num_steps', '') or get_metric('training_steps', 'train_steps', 'final_step', default=''),\n        'model': spec.get('model_name', '') or e.get('model', '') or get_metric('model', default=''),\n        # Eval metrics\n        'PR': get_metric('eval_prove_rate', 'prove_rate', 'pass_rate'),\n        'n_proved': get_metric('eval_n_proved', 'n_proved', 'proved_count'),\n        'n_problems': get_metric('eval_n_problems', 'n_problems', 'total_samples'),\n        'ISR': get_metric('eval_mean_isr', 'mean_isr', 'isr_mean', 'isr'),\n        'ISR_std': get_metric('eval_isr_std', 'isr_std'),\n        'ISR_median': get_metric('eval_median_isr', 'median_isr'),\n        'proved_only_ISR': get_metric('eval_proved_only_isr', 'proved_only_isr', 'eval_proved_only_mean_isr', 'proved_only_mean_isr'),\n        # Taxonomy\n        'H7%': get_metric('h7_rate', 'eval_h7_strict_rate', 'h7_strict_rate', 'hacking_rate_strict_h7', 'h7_functional_rate'),\n        'H7_count': get_metric('h7_count', 'eval_h7_strict_count', 'h7_strict_count', 'eval_h7_count'),\n        'H1%': get_metric('h1_rate', 'eval_h1_strict_rate', 'h1_strict_rate', 'eval_h1_rate'),\n        'H1_count': get_metric('h1_count', 'eval_h1_strict_count', 'h1_strict_count', 'eval_h1_count'),\n        'H8%': get_metric('h8_conjunction_collapse_rate'),\n        'H8_count': get_metric('h8_conjunction_collapse_count', 'h8_count'),\n        'genuine%': get_metric('genuine_rate', 'eval_genuine_rate'),\n        'genuine_count': get_metric('genuine_count', 'eval_genuine_count'),\n        'tautological': get_metric('tautological_collapse'),\n        # Training metrics\n        'train_PR': get_metric('train_final_prove_rate', 'final_prove_rate'),\n        'train_ISR': get_metric('train_final_mean_isr', 'final_mean_isr'),\n        'train_loss': get_metric('train_loss', 'train_final_loss', 'final_loss'),\n        'train_entropy': get_metric('train_final_entropy', 'final_entropy'),\n        'train_runtime_s': get_metric('train_runtime_seconds', 'train_runtime_sec', 'train_runtime_s'),\n    }\n    rows.append(row)\n\n# Sort by exp_id\nrows.sort(key=lambda r: r['exp_id'])\n\n# Print comprehensive table\nprint(f\"{'='*140}\")\nprint(f\"COMPREHENSIVE EXPERIMENT METRICS TABLE — {len(rows)} experiments (conclusion=success or negative)\")\nprint(f\"{'='*140}\")\nprint()\n\nfor r in rows:\n    print(f\"--- {r['exp_id']} [{r['conclusion'].upper()}] ---\")\n    if r['reward_mode'] or r['beta'] or r['seed'] or r['steps']:\n        parts = []\n        if r['model']: parts.append(f\"model={r['model']}\")\n        if r['reward_mode']: parts.append(f\"reward={r['reward_mode']}\")\n        if r['beta']: parts.append(f\"β={r['beta']}\")\n        if r['seed']: parts.append(f\"seed={r['seed']}\")\n        if r['steps']: parts.append(f\"steps={r['steps']}\")\n        print(f\"  Config: {', '.join(parts)}\")\n    \n    # Eval\n    eval_parts = []\n    if r['PR'] is not None: eval_parts.append(f\"PR={r['PR']}\")\n    if r['n_proved'] is not None: eval_parts.append(f\"n_proved={r['n_proved']}\")\n    if r['n_problems'] is not None: eval_parts.append(f\"n_problems={r['n_problems']}\")\n    if r['ISR'] is not None: eval_parts.append(f\"ISR={r['ISR']}\")\n    if r['ISR_std'] is not None: eval_parts.append(f\"ISR_std={r['ISR_std']}\")\n    if r['ISR_median'] is not None: eval_parts.append(f\"ISR_med={r['ISR_median']}\")\n    if r['proved_only_ISR'] is not None: eval_parts.append(f\"ISR*={r['proved_only_ISR']}\")\n    if eval_parts:\n        print(f\"  Eval: {', '.join(eval_parts)}\")\n    \n    # Taxonomy\n    tax_parts = []\n    if r['H7_count'] is not None: tax_parts.append(f\"H7={r['H7_count']}({r['H7%']})\")\n    if r['H1_count'] is not None: tax_parts.append(f\"H1={r['H1_count']}({r['H1%']})\")\n    if r['H8_count'] is not None: tax_parts.append(f\"H8={r['H8_count']}({r['H8%']})\")\n    if r['genuine_count'] is not None: tax_parts.append(f\"genuine={r['genuine_count']}({r['genuine%']})\")\n    if r['tautological'] is not None: tax_parts.append(f\"taut_collapse={r['tautological']}\")\n    if tax_parts:\n        print(f\"  Taxonomy: {', '.join(tax_parts)}\")\n    \n    # Training\n    train_parts = []\n    if r['train_PR'] is not None: train_parts.append(f\"train_PR={r['train_PR']}\")\n    if r['train_ISR'] is not None: train_parts.append(f\"train_ISR={r['train_ISR']}\")\n    if r['train_loss'] is not None: train_parts.append(f\"loss={r['train_loss']}\")\n    if r['train_entropy'] is not None: train_parts.append(f\"entropy={r['train_entropy']}\")\n    if r['train_runtime_s'] is not None: train_parts.append(f\"runtime={r['train_runtime_s']}s\")\n    if train_parts:\n        print(f\"  Training: {', '.join(train_parts)}\")\n    \n    print()\n\nPYEOF\n",
  "description": "Generate comprehensive structured metrics table",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "4315f3f8-c586-48ef-9d37-c83c35199576",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VN9aCo491hdoNnJtHGv1UV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 57278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1208,
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

_source line 78 · 2026-05-15T15:58:48.812Z_

<details><summary>↩ Tool result · `toolu_01Rz7brApVuf6FP7nsxW1LnZ`</summary>

```text
============================================================================================================================================
COMPREHENSIVE EXPERIMENT METRICS TABLE — 49 experiments (conclusion=success or negative)
============================================================================================================================================

--- exp1-isr-b03-s42-1000-r2 [NEGATIVE] ---
  Eval: PR=0.95, n_proved=95, n_problems=100, ISR=0.734, ISR_std=0.2575, ISR_med=0.6, ISR*=0.7726
  Taxonomy: H7=0(0), H1=54(0.568), H8=41(0.432), genuine=0(0), taut_collapse=True
  Training: train_PR=0.829, train_ISR=0.727, loss=0.0041, entropy=9e-06, runtime=6280s

--- exp1-isr-b03-s43 [SUCCESS] ---
  Config: model=Qwen3-4B, β=0.3, seed=43, steps=500
  Eval: PR=0.91, n_proved=91, n_problems=100, ISR=0.2575, ISR_std=0.2363, ISR_med=0.3333, ISR*=0.283
  Taxonomy: genuine=61(0.6703)

--- exp1-isr-b03-s43-r3 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=43, steps=500
  Eval: PR=0.86, n_proved=86, n_problems=100, ISR=0.2535, ISR_std=0.2406, ISR_med=0.3333, ISR*=0.2948
  Taxonomy: H7=4(0.047), H1=59(0.686), genuine=23(0.267)
  Training: loss=0.0176, runtime=4153.6s

--- exp1-isr-b03-s44-r2 [SUCCESS] ---
  Config: model=Qwen3-4B, β=0.3, seed=44, steps=500
  Eval: PR=0.95, n_proved=95, n_problems=100, ISR=0.705, ISR_std=0.172, ISR*=0.7421
  Taxonomy: H7=95(1), H1=0(0), genuine=0(0)

--- exp1-random-b03-s43 [SUCCESS] ---
  Config: model=Qwen3-4B, β=0.3, seed=43, steps=500
  Eval: PR=0.79, n_proved=79, n_problems=100, ISR=0.1745, ISR_std=0.1628, ISR_med=0.1667, ISR*=0.2209
  Taxonomy: genuine=71(0.8987)

--- exp1-random-b03-s43-r4 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=43, steps=500
  Eval: PR=0.92, n_proved=92, n_problems=100, ISR=0.1659, ISR_std=0.1147, ISR_med=0.1429, ISR*=0.1803
  Taxonomy: H7=7(0.076), H1=82(0.891), genuine=3(0.0326)
  Training: loss=0.01365, runtime=6161.1s

--- exp1-random-b03-s44-r2 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=44
  Eval: PR=0.23, n_proved=23, n_problems=100, ISR=0, ISR_std=0, ISR_med=0, ISR*=0
  Taxonomy: H7=0(0), H1=23(1), genuine=0(0)

--- exp2-exec-s43-greedy [SUCCESS] ---
  Config: model=Qwen3-4B, seed=43

--- exp4-100step-h1h7 [SUCCESS] ---
  Config: model=Qwen3-4B (100-step checkpoint), seed=42

--- plan001-exec-only-s42-r2 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=42
  Eval: PR=0.93, n_proved=93, n_problems=100, ISR=0.1232, ISR_std=0.1887, ISR_med=0, ISR*=0.1324
  Taxonomy: H7=0(0), H1=81(0.871), H8=6(0.0645), genuine=7(0.0753)

--- plan001-exec-only-s43-r4 [NEGATIVE] ---
  Config: model=Qwen3-4B, seed=43

--- plan001-exec-only-s44 [NEGATIVE] ---
  Eval: PR=0.98, n_proved=98, n_problems=100, ISR=0.57, ISR_std=0.2013, ISR_med=0.5, ISR*=0.5816
  Taxonomy: H7=97(1), H1=0(0), genuine=0(0), taut_collapse=True

--- plan002-additive-b01-s42 [NEGATIVE] ---
  Config: model=Qwen3-4B, seed=42, steps=500
  Eval: PR=0.81, n_proved=81, n_problems=100, ISR=0.3365, ISR_std=0.3227, ISR_med=0.2, ISR*=0.4154
  Taxonomy: H7=13(0.16), H1=42(0.519), H8=12(0.148), genuine=14(0.173), taut_collapse=False

--- plan002-additive-b01-s42-1000 [NEGATIVE] ---
  Eval: PR=0.9, n_proved=90, n_problems=100, ISR=0.7892, ISR_std=0.3424, ISR_med=1, ISR*=0.8769
  Taxonomy: H7=87(0.9667), H1=0(0), H8=1(0.0111), genuine=2(0.0222), taut_collapse=True
  Training: train_PR=0.855, train_ISR=0.532

--- plan002-additive-b01-s43 [NEGATIVE] ---
  Eval: PR=0.61, n_proved=61, n_problems=100, ISR*=0.83
  Taxonomy: H7=59(0.9672), H1=0(0), H8=0(0), genuine=2(0.0328)

--- plan002-additive-b01-s44 [NEGATIVE] ---
  Config: model=Qwen3-4B, seed=44
  Eval: PR=0.89, n_proved=89, n_problems=100, ISR=0.803, ISR*=0.902
  Taxonomy: H7=89(1), H1=0(0), H8=0(0), genuine=0(0)

--- plan002-additive-b03-s42 [NEGATIVE] ---
  Config: model=Qwen3-4B, β=0.3, seed=42
  Eval: PR=0.18, n_proved=18, n_problems=100, ISR=0.0257, ISR_std=0.0742, ISR_med=0, ISR*=0.1427
  Taxonomy: H7=0(0), H1=14(0.778), H8=3(0.1667), genuine=1(0.0556)

--- plan003-eval-exec-only-r5 [SUCCESS] ---
  Eval: PR=0.32, n_proved=32, n_problems=100, ISR=0.2055, ISR_std=0.3194, ISR*=0.6423

--- plan004-o1-ablation-s42 [NEGATIVE] ---
  Config: model=Qwen3-4B, seed=42
  Eval: PR=0.63, ISR=0.0072
  Taxonomy: H7=0(0), H1=63(1), H8=2(0.0317), genuine=0(0)

--- plan005-sta-low-s42 [NEGATIVE] ---

--- plan006-prolog-exec-s42 [NEGATIVE] ---
  Config: model=Qwen3-4B, seed=42
  Eval: PR=0.83, ISR=0.031, ISR_std=0.0534, ISR_med=0, ISR*=0.037

--- plan006-prolog-exec-s43-r3 [NEGATIVE] ---
  Eval: PR=0.56, n_proved=56, n_problems=100, ISR=0.0084, ISR_std=0.0221, ISR_med=0, ISR*=0.015

--- plan006-prolog-exec-s44 [NEGATIVE] ---
  Eval: PR=0.21, n_proved=21, n_problems=100, ISR=0.0812, ISR_std=0.2343, ISR_med=0, ISR*=0.3866

--- plan006-prolog-sta-s42 [NEGATIVE] ---
  Config: model=Qwen3-4B, seed=42
  Eval: PR=0.5, ISR=0.5, ISR*=1
  Taxonomy: H7=50(None)
  Training: train_PR=1, loss=0.00716, entropy=0.01, runtime=2791s

--- plan006-prolog-sta-s43 [NEGATIVE] ---
  Eval: PR=0.38, n_proved=38, n_problems=100, ISR=0.0704, ISR_std=0.1263, ISR_med=0, ISR*=0.1853
  Taxonomy: genuine=0(0)
  Training: train_PR=0.769, train_ISR=0.129, loss=0.0155, entropy=0.09, runtime=5095s

--- plan006-prolog-sta-s44 [NEGATIVE] ---
  Eval: PR=0.97, ISR=0.885

--- plan009-sft-baseline-s42-1000 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=42, steps=1000
  Eval: PR=0.13, n_proved=13, n_problems=100, ISR=0.0738, ISR_std=0.2077, ISR_med=0, ISR*=0.5677
  Taxonomy: H7=0(0), H1=1(7.7), H8=0(0), genuine=12(0.9231)
  Training: loss=0.0168, runtime=1415s

--- plan009-sft-baseline-s42-r4 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=42
  Eval: PR=0.14, n_proved=14, n_problems=100, ISR=0.08, ISR_std=0.214, ISR_med=0, ISR*=0.571
  Taxonomy: H7=0(0), H1=1(0.071), genuine=13(0.929), taut_collapse=False
  Training: loss=0.0287, runtime=789.6s

--- plan009-sft-baseline-s43 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=43, steps=500
  Eval: PR=0.15, ISR=0.0895, ISR_std=0.2338, ISR_med=0, ISR*=0.5967
  Taxonomy: H7=0(0), H1=1(0.067), genuine=14(0.933)
  Training: loss=0.2391, runtime=677.14s

--- plan009-sft-baseline-s43-1000 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=43
  Eval: PR=0.11, n_proved=11, n_problems=100, ISR=0.0699, ISR_std=0.2155, ISR_med=0, ISR*=0.6352
  Taxonomy: H7=0(0), H1=1(0.0909), H8=0(0), genuine=10(0.9091)
  Training: loss=0.0167, runtime=1584.79s

--- plan009-sft-baseline-s44 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=44, steps=500
  Eval: PR=0.17, n_proved=17, n_problems=100, ISR=0.0974, ISR_std=0.2409, ISR_med=0, ISR*=0.5729
  Taxonomy: H7=0(None), H1=2(0.118), genuine=15(0.882)
  Training: loss=0.2397, runtime=729.05s

--- plan009-sft-baseline-s44-1000 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=44
  Eval: PR=0.15, n_proved=15, n_problems=100, ISR=0.0884, ISR_std=0.2268, ISR_med=0, ISR*=0.5892
  Taxonomy: H7=0(0), H1=1(0.0667), H8=0(0), genuine=14(0.9333)
  Training: loss=0.0171, runtime=1580.97s

--- plan009-sft-baseline-s44-1000-r3 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=44
  Eval: PR=0.15, n_proved=15, n_problems=100, ISR=0.0884, ISR_std=0.2268, ISR_med=0, ISR*=0.5892
  Taxonomy: H7=0(0), H1=1(0.0667), H8=0(0), genuine=14(0.9333)

--- plan012-hacking-taxonomy [SUCCESS] ---
  Config: model=N/A (rule-based analysis), seed=N/A

--- plan013-random-reward-s42-r4 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=42
  Eval: PR=1, n_proved=100, n_problems=100, ISR=0.535, ISR_std=0.1282, ISR_med=0.5, ISR*=0.535

--- plan014-downstream-nli-s42 [NEGATIVE] ---
  Eval: n_proved=732

--- plan016-extended-1000-s42 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=42, steps=1000
  Eval: PR=0.96, n_proved=96, ISR=0.003
  Taxonomy: H7=0(0), H1=96(1), genuine=0(0)

--- plan017-additive-random-s42 [NEGATIVE] ---
  Config: model=Qwen3-4B, β=0.3, seed=42
  Eval: PR=0.48, n_proved=48, n_problems=100, ISR=0.0453, ISR_std=0.0759, ISR_med=0, ISR*=0.0943
  Taxonomy: H7=0(0), H1=48(1), genuine=0(0), taut_collapse=False

--- plan018-additive-random-b01-s42 [NEGATIVE] ---
  Config: model=Qwen3-4B, seed=42, steps=500
  Eval: PR=0.79, n_proved=79, n_problems=100, ISR=0.1038, ISR_std=0.1369, ISR_med=0.0357, ISR*=0.1314
  Taxonomy: H7=0(0), H1=56(0.7089), H8=3(0.038), genuine=18(0.228), taut_collapse=False

--- plan018-additive-random-b01-s42-1000-r2 [NEGATIVE] ---
  Config: steps=1000
  Eval: PR=1, n_proved=100, n_problems=100, ISR=0.3333, ISR_std=0, ISR_med=0.3333, ISR*=0.3333
  Taxonomy: genuine=0(0), taut_collapse=True
  Training: train_PR=0.989, train_ISR=0.353, runtime=2957s

--- plan018-additive-random-b01-s42-1000-r3 [NEGATIVE] ---
  Config: steps=1000
  Eval: PR=0.97, n_proved=97, n_problems=100, ISR=0.6892, ISR_std=0.2037, ISR_med=0.75, ISR*=0.7105
  Taxonomy: H7=97(1), H1=0(0), H8=0(None), genuine=0(0), taut_collapse=True
  Training: train_PR=0.827, train_ISR=0.5213, loss=0.00671, entropy=0.003, runtime=5783s

--- plan018-additive-random-b01-s43-r2 [NEGATIVE] ---
  Eval: PR=0.88, ISR=0.058
  Taxonomy: H7=0(0), H1=82(93.2), genuine=6(6.8)

--- plan018-additive-random-b01-s44 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=44, steps=500
  Eval: PR=0.89, n_proved=89, n_problems=100, ISR=0.0619, ISR_std=0.1756, ISR_med=0, ISR*=0.0695

--- sta-gt-isr-baseline [SUCCESS] ---

--- sta-phase0-baseline [SUCCESS] ---
  Eval: PR=0.12, n_proved=12, n_problems=100, ISR=0.0641, ISR_std=0.1983, ISR_med=0

--- sta-phase1-exec-only-r4 [NEGATIVE] ---
  Config: steps=100
  Eval: PR=0.15125, ISR=0.1475

--- sta-phase1-exec-only-r5 [SUCCESS] ---
  Config: model=Qwen3-4B, seed=42, steps=100
  Eval: PR=0.15125, ISR=0.1475

--- sta-phase1-exec-sta-r4 [NEGATIVE] ---
  Config: steps=100
  Eval: PR=0.1575, ISR=0.1525

--- sta-phase1-exec-sta-r5 [NEGATIVE] ---
  Config: model=Qwen3-4B, seed=42, steps=100
  Eval: PR=0.1, ISR=0.04347
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "b6516579-c1cf-4027-85bd-e08f2af8d997"
}
```

</details>

---


### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "description": "Running Extract special experiment details",
  "usage": {
    "total_tokens": 66344,
    "tool_uses": 15,
    "duration_ms": 119621
  },
  "last_tool_name": "Bash",
  "uuid": "fdc60b25-9957-4816-9c91-476374c83f87",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Bash · `toolu_01VRcrgfbwhc9BYVN3Y86AdD`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Extract special experiments with unique metrics\nspecial = [\n    'plan012-hacking-taxonomy',\n    'plan014-downstream-nli-s42', \n    'sta-gt-isr-baseline',\n    'sta-phase0-baseline',\n    'plan005-sta-low-s42',\n    'plan001-exec-only-s43-r4',\n    'plan006-prolog-sta-s42',\n    'plan006-prolog-sta-s44',\n]\n\nfor sid in special:\n    e = exps.get(sid, {})\n    if not e:\n        continue\n    m = e.get('metrics', {}) or {}\n    print(f\"=== {sid} [{e.get('conclusion','')}] ===\")\n    print(f\"  ALL metrics: {json.dumps(m, indent=4, ensure_ascii=False)}\")\n    notes = e.get('notes', '')\n    if notes:\n        print(f\"  NOTES: {notes[:600]}\")\n    print()\n\nPYEOF\n",
  "description": "Extract special experiment details",
  "timeout": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "f5a0d376-f3a0-44f3-967c-4cc4327518b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6c2zTVgJWduaPnJx6BDGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7295,
      "cache_read_input_tokens": 58486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7295,
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

_source line 81 · 2026-05-15T15:58:59.514Z_

<details><summary>↩ Tool result · `toolu_01VRcrgfbwhc9BYVN3Y86AdD`</summary>

```text
=== plan012-hacking-taxonomy [success] ===
  ALL metrics: {
    "isr_b01_genuine_rate": 0.259,
    "random_b01_genuine_rate": 0.177,
    "genuine_rate_delta_pp": 8.2,
    "isr_b01_conclusion_embedding_rate": 0.728,
    "random_b01_conclusion_embedding_rate": 0.785,
    "isr_b01_genuine_mean_isr": 0.6723,
    "random_b01_genuine_mean_isr": 0.3427,
    "isr_b01_complexity_wo_utility_rate": 0,
    "random_b01_complexity_wo_utility_rate": 0.038,
    "isr_b01_hacking_rate": 0.741,
    "random_b01_hacking_rate": 0.823
}
  NOTES: D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。

=== plan014-downstream-nli-s42 [negative] ===
  ALL metrics: {
    "overall_accuracy": 0.341,
    "proved_rate": 0.915,
    "proved_count": 732,
    "total_generations": 800,
    "parse_errors": 0,
    "accuracy_by_label": {
        "true": 0.912,
        "false": 0,
        "unknown": 0.076
    },
    "spearman_rho": -0.049,
    "spearman_p": 0.187,
    "mann_whitney_U": 17202,
    "mann_whitney_p": 0.288,
    "bon_isr_accuracy": 0.35,
    "bon_random_accuracy": 0.341,
    "bon_oracle_accuracy": 0.44,
    "bon_prove_first_accuracy": 0.35,
    "isr_bucket_high_acc": 0.75,
    "isr_bucket_mid_acc": 0.377,
    "isr_bucket_low_acc": 0.327,
    "runtime_inference_s": 408.8,
    "runtime_eval_s": 13.6
}
  NOTES: Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。

=== sta-gt-isr-baseline [success] ===
  ALL metrics: {
    "gt_prove_rate": 0.18,
    "gt_mean_isr": 0.5588,
    "gt_isr_std": 0.2582,
    "gt_isr_median": 0.6125,
    "solver_execution_rate": 1,
    "true_prove_rate": 0.5,
    "true_mean_isr": 0.5833
}

=== sta-phase0-baseline [success] ===
  ALL metrics: {
    "mean_isr": 0.0641,
    "isr_std": 0.1983,
    "median_isr": 0,
    "isr_range": [
        0,
        0.889
    ],
    "prove_rate": 0.12,
    "proved_count": 12,
    "total_samples": 100,
    "xor_affected_samples": 34,
    "effective_prove_rate_no_xor": 0.182,
    "avg_time_per_sample_s": 3.4,
    "total_runtime_s": 336,
    "isr_by_answer": {
        "true": {
            "n": 34,
            "proved": 9,
            "prove_rate": 0.265,
            "mean_isr": 0.1345
        },
        "false": {
            "n": 25,
            "proved": 1,
            "prove_rate": 0.04,
            "mean_isr": 0.024
        },
        "unknown": {
            "n": 41,
            "proved": 2,
            "prove_rate": 0.049,
            "mean_isr": 0.0302
        }
    }
}

=== plan005-sta-low-s42 [negative] ===
  ALL metrics: {
    "total_steps": 500,
    "duration_min": 71,
    "parse_rate": 1,
    "overall_prove_rate": 0.5657,
    "overall_isr": 0.1682,
    "last50_prove_rate": 0.77,
    "last50_isr": 0.2559,
    "last100_prove_rate": 0.7725,
    "last100_isr": 0.2299,
    "last100_loss": 0.022752,
    "overall_loss": 0.017296,
    "last100_isr_pr_ratio": 0.298,
    "last100_isr_lt_pr_count": "99/100",
    "first_rolling10_pr_ge_0.8": 178,
    "first_rolling10_pr_ge_0.9": 439,
    "max_rolling10_pr": 0.9375,
    "max_rolling10_isr": 0.3282,
    "windowed": {
        "1-50": {
            "pr": 0.1775,
            "isr": 0.0906
        },
        "51-100": {
            "pr": 0.1775,
            "isr": 0.0835
        },
        "101-200": {
            "pr": 0.5062,
            "isr": 0.1463
        },
        "201-300": {
            "pr": 0.6713,
            "isr": 0.1791
        },
        "301-400": {
            "pr": 0.7013,
            "isr": 0.1984
        },
        "401-500": {
            "pr": 0.7725,
            "isr": 0.2299
        }
    }
}
  NOTES: conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 "STA 抑制 reward hacking" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。

=== plan001-exec-only-s43-r4 [negative] ===
  ALL metrics: {
    "eval_sampling_prove_rate": 0.14,
    "eval_sampling_mean_isr": 0,
    "eval_sampling_n_proved": 14,
    "eval_sampling_temperature": 0.7,
    "eval_sampling_method": "do_sample=True, temperature=0.7",
    "eval_sampling_by_answer": {
        "true": {
            "count": 34,
            "proved": 6,
            "prove_rate": 0.176
        },
        "false": {
            "count": 25,
            "proved": 2,
            "prove_rate": 0.08
        },
        "unknown": {
            "count": 41,
            "proved": 6,
            "prove_rate": 0.146
        }
    },
    "eval_greedy_prove_rate": 0.13,
    "eval_greedy_mean_isr": 0,
    "eval_greedy_proved_only_isr": 0,
    "eval_greedy_n_proved": 13,
    "eval_greedy_method": "eval_sta.py default (do_sample=False)",
    "eval_greedy_by_answer": {
        "true": {
            "count": 34,
            "proved": 4,
            "prove_rate": 0.118
        },
        "false": {
            "count": 25,
            "proved": 5,
            "prove_rate": 0.2
        },
        "unknown": {
            "count": 41,
            "proved": 4,
            "prove_rate": 0.0976
        }
    },
    "eval_greedy_h7_count": 0,
    "eval_greedy_h7_rate": 0,
    "eval_greedy_h1_count": 13,
    "eval_greedy_h1_rate": 1,
    "eval_greedy_genuine_rate": 0,
    "eval_greedy_n_premises_proved_mean": 17.92,
    "eval_greedy_mean_components_proved": 18.92,
    "eval_greedy_n_premises_all_mean": 32.67,
    "eval_sampling_h1_rate": 1,
    "eval_sampling_h7_rate": 0,
    "eval_sampling_genuine_rate": 0,
    "eval_sampling_mean_components_proved": 18.5,
    "eval_greedy_vs_sampling_delta_pr": -0.01,
    "eval_method_note": "Greedy and sampling agree on failure profile (ISR*=0, H1=100%, components~18.5-18.9). s43 collapse is decoding-invariant."
}
  NOTES: EXP-2 (2026-05-15): greedy eval (T=0) on same 100 held-out problems also done with eval_sta.py defaults (do_sample=False). Result: PR=0.13, ISR*=0.0, H1=100% (13/13), H7=0%, genuine=0%, mean components (proved)=18.92. Sampling (T=0.7) baseline: PR=0.14, ISR*=0.0, H1=100% (14/14), components~18.5. ΔPR=-0.01, both ISR*=0 → s43 collapse is decoding-invariant, NOT a sampling artifact. ~85% of inputs hit max_new_tokens with long repeated-clause outputs; the ~15% that do parse contain the conclusion verbatim among 14-30 premises (n_necessary=0 by per-clause ablation → ISR=0). 训练 PR(last100)=0.883 但 

=== plan006-prolog-sta-s42 [negative] ===
  ALL metrics: {
    "cumulative_prove_rate": 0.848,
    "cumulative_mean_isr": 0.787,
    "final_prove_rate": 1,
    "final_isr": 1,
    "final_reward": 1,
    "saturation_onset_step": 100,
    "train_loss": 0.00716,
    "training_hours": 0.78,
    "final_entropy": 0.01,
    "final_completion_length": 27,
    "initial_completion_length": 120,
    "steps_at_perfect_reward": 400,
    "train_runtime_sec": 2791,
    "eval_prove_rate": 0.5,
    "eval_mean_isr": 0.5,
    "eval_proved_only_isr": 1,
    "eval_h7_rate": 1,
    "eval_h7_count": 50,
    "eval_proved_count": 50,
    "eval_total_count": 100,
    "eval_n_clauses_mean": 1,
    "eval_isr_distribution": "binary: 50x0 + 50x1"
}
  NOTES: Eval metrics provenance: eval 在训练完成后立即在 westd-39279 服务器上运行 eval_sta.py，checkpoint 路径 /root/autodl-tmp/outputs/plan006_prolog_sta_s42/。Eval 结果由 Worker 从服务器 SSH 读取 eval_results.json 并手动录入 registry。Checkpoint 可能已被磁盘清理删除（C003 save_total_limit=1）。训练日志: ~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log。H7 分类由 classify_h7.py 在 eval 目录上运行。

=== plan006-prolog-sta-s44 [negative] ===
  ALL metrics: {
    "pass_rate": 0.97,
    "isr_mean": 0.885,
    "isr_n_cl_ge3": "N/A (0 samples)",
    "n_clauses_dist": "78/100 single-clause, 22/100 two-clause",
    "h7_functional_rate": 0.979,
    "genuine_rate": 0,
    "premise_count_analysis": "100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs",
    "failure_mode": "query-as-fact gaming (total H7 collapse)"
}
  NOTES: Reviewer 独立核实: query-as-fact gaming, 0% genuine. 97/97 proved 样本中 95/97 n_necessary=1（功能性 H7）。模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。PR=0.97, ISR=0.885 是 gaming artifact（高 ISR 因单 clause = query）。第三种 Goodhart pathway（vs s42 clean H7, s43 degenerate syntax H1）。对照: s42=negative (clean H7=100%), s43=negative (uppercase pseudo-Prolog H1=97.4%), s44=negative (query-as-fact gaming, functional H7=95/97).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "8c912c9f-8217-4739-ab22-a2e95baa33df"
}
```

</details>

---


### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "acf8d8db20c645266",
  "tool_use_id": "toolu_012DcgU8HE673BrqdqER1VKV",
  "status": "completed",
  "output_file": "",
  "summary": "Extract registry metrics",
  "usage": {
    "total_tokens": 70906,
    "tool_uses": 15,
    "duration_ms": 181607
  },
  "uuid": "2bbddad5-d549-499d-ab26-356362a89150",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool result

_source line 83 · 2026-05-15T16:00:01.399Z_

<details><summary>↩ Tool result · `toolu_012DcgU8HE673BrqdqER1VKV`</summary>

```text
Here is the complete extraction of all 49 experiments with conclusion "success" or "negative" from the registry.

---

## Summary: 49 experiments extracted (29 success, 20 negative)

### BASELINES

**sta-phase0-baseline [success]** -- Pre-training Qwen3-4B base model
- PR=0.12, ISR=0.0641, ISR_std=0.1983, median_ISR=0, n_proved=12/100
- By answer type: true PR=0.265/ISR=0.1345, false PR=0.04/ISR=0.024, unknown PR=0.049/ISR=0.0302

**sta-gt-isr-baseline [success]** -- Ground-truth FOL upper bound
- gt_prove_rate=0.18, gt_mean_isr=0.5588, gt_isr_std=0.2582, gt_isr_median=0.6125
- true_prove_rate=0.5, true_mean_isr=0.5833

**plan003-eval-exec-only-r5 [success]** -- 100-step exec-only checkpoint eval
- PR=0.32, ISR=0.2055, ISR_std=0.3194, ISR*=0.6423

---

### SFT BASELINES (500-step and 1000-step, 3 seeds)

| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | H8 | Genuine | Genuine% |
|---|---|---|---|---|---|---|---|---|---|---|
| plan009-sft-s42-r4 | 500 | 42 | 0.14 | 0.08 | 0.571 | 0 | 1 | -- | 13 | 92.9% |
| plan009-sft-s43 | 500 | 43 | 0.15 | 0.0895 | 0.5967 | 0 | 1 | -- | 14 | 93.3% |
| plan009-sft-s44 | 500 | 44 | 0.17 | 0.0974 | 0.5729 | 0 | 2 | -- | 15 | 88.2% |
| plan009-sft-s42-1000 | 1000 | 42 | 0.13 | 0.0738 | 0.5677 | 0 | 1 | 0 | 12 | 92.3% |
| plan009-sft-s43-1000 | 1000 | 43 | 0.11 | 0.0699 | 0.6352 | 0 | 1 | 0 | 10 | 90.9% |
| plan009-sft-s44-1000 | 1000 | 44 | 0.15 | 0.0884 | 0.5892 | 0 | 1 | 0 | 14 | 93.3% |

Key: SFT maintains >88% genuine rate across all seeds and steps. No Goodhart collapse.

---

### EXEC-ONLY (FOL, 3 seeds)

| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | H8 | Genuine | Genuine% | Tautological |
|---|---|---|---|---|---|---|---|---|---|---|---|
| plan001-s42-r2 | 500 | 42 | 0.93 | 0.1232 | 0.1324 | 0 | 81 | 6 | 7 | 7.5% | No |
| plan001-s43-r4 | 500 | 43 | 0.13 (greedy) / 0.14 (sampling) | 0 | 0 | 0 | 13 (100%) | -- | 0 | 0% | -- |
| plan001-s44 | 500 | 44 | 0.98 | 0.57 | 0.5816 | 97 | 0 | -- | 0 | 0% | Yes |
| plan016-extended-1000-s42 | 1000 | 42 | 0.96 | 0.003 | -- | 0 | 96 (100%) | -- | 0 | 0% | -- |

plan001-s43-r4 additional: greedy components_proved=18.92, sampling components=18.5, decoding-invariant collapse.

---

### ISR beta=0.1 (Additive, FOL)

| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | H8 | Genuine | Genuine% | Taut |
|---|---|---|---|---|---|---|---|---|---|---|---|
| plan002-b01-s42 | 500 | 42 | 0.81 | 0.3365 | 0.4154 | 13 | 42 | 12 | 14 | 17.3% | No |
| plan002-b01-s43 | 500 | 43 | 0.61 | -- | 0.83 | 59 | 0 | 0 | 2 | 3.3% | -- |
| plan002-b01-s44 | 500 | 44 | 0.89 | 0.803 | 0.902 | 89 (100%) | 0 | 0 | 0 | 0% | -- |
| plan002-b01-s42-1000 | 1000 | 42 | 0.90 | 0.7892 | 0.8769 | 87 | 0 | 1 | 2 | 2.2% | Yes |

---

### ISR beta=0.3 (Additive, FOL)

| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | H8 | Genuine | Genuine% |
|---|---|---|---|---|---|---|---|---|---|---|
| plan002-b03-s42 | 500 | 42 | 0.18 | 0.0257 | 0.1427 | 0 | 14 | 3 | 1 | 5.6% |
| exp1-isr-b03-s43-r3 | 500 | 43 | 0.86 | 0.2535 | 0.2948 | 4 | 59 | -- | 23 | 26.7% |
| exp1-isr-b03-s44-r2 | 500 | 44 | 0.95 | 0.705 | 0.7421 | 95 (100%) | 0 | -- | 0 | 0% |
| exp1-isr-b03-s42-1000-r2 | 1000 | -- | 0.95 | 0.734 | 0.7726 | 0 | 54 | 41 | 0 | 0% |

---

### RANDOM BASELINES (Additive, FOL)

**Convex random (plan013, r=0.9*exec+0.1*random):**

| Exp ID | Steps | Seed | PR | ISR | H7 | Genuine | Taut |
|---|---|---|---|---|---|---|---|
| plan013-random-s42-r4 | 500 | 42 | 1.0 | 0.535 | 100 (100%) | 0 | Yes (degenerate 2-component) |

**Additive random beta=0.3:**

| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | Genuine |
|---|---|---|---|---|---|---|---|---|
| plan017-random-s42 | 500 | 42 | 0.48 | 0.0453 | 0.0943 | 0 | 48 (100%) | 0 |
| exp1-random-b03-s43-r4 | 500 | 43 | 0.92 | 0.1659 | 0.1803 | 7 | 82 | 3 (3.3%) |
| exp1-random-b03-s44-r2 | 500 | 44 | 0.23 | 0 | 0 | 0 | 23 (100%) | 0 |

**Additive random beta=0.1:**

| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | H8 | Genuine | Genuine% |
|---|---|---|---|---|---|---|---|---|---|---|
| plan018-random-b01-s42 | 500 | 42 | 0.79 | 0.1038 | 0.1314 | 0 | 56 | 3 | 18 | 22.8% |
| plan018-random-b01-s43-r2 | 500 | 43 | 0.88 | 0.058 | -- | 0 | 82 | -- | 6 | 6.8% |
| plan018-random-b01-s44 | 500 | 44 | 0.89 | 0.0619 | 0.0695 | -- | -- | -- | -- | -- |
| plan018-random-b01-s42-1000-r3 | 1000 | 42 | 0.97 | 0.6892 | 0.7105 | 97 (100%) | 0 | 0 | 0 | 0% |

---

### O(1) BINARY ISR ABLATION

| Exp ID | Steps | Seed | PR | ISR | H7 | H1 | H8 | Genuine |
|---|---|---|---|---|---|---|---|---|
| plan004-o1-ablation-s42 | 500 | 42 | 0.63 | 0.0072 | 0 | 63 (100%) | 2 | 0 |

Confirms: O(1) binary ISR degrades to exec-only. LOO ablation O(N) is necessary.

---

### STA-LOW (alpha=0.1 convex penalty)

**plan005-sta-low-s42 [negative]:** Training-only metrics (no eval checkpoint):
- Windowed PR/ISR: steps 1-50: 0.178/0.091, 101-200: 0.506/0.146, 301-400: 0.701/0.198, 401-500: 0.773/0.230
- ISR/PR ratio=0.298 (99/100 steps ISR < PR), confirms STA suppresses reward hacking

---

### PROLOG CROSS-LOGIC (exec-only, 3 seeds)

| Exp ID | Reward | Seed | PR | ISR | ISR* | H7 | Genuine |
|---|---|---|---|---|---|---|---|
| plan006-prolog-exec-s42 | exec | 42 | 0.83 | 0.031 | 0.037 | 0% | -- |
| plan006-prolog-exec-s43-r3 | exec | 43 | 0.56 | 0.0084 | 0.015 | -- | -- |
| plan006-prolog-exec-s44 | exec | 44 | 0.21 | 0.0812 | 0.3866 | -- | -- |

3-seed mean: PR=53.3% +/- 31.1%, ISR=0.040 +/- 0.037

### PROLOG CROSS-LOGIC (exec+STA, 3 seeds)

| Exp ID | Seed | PR | ISR | ISR* | H7 | Genuine |
|---|---|---|---|---|---|---|
| plan006-prolog-sta-s42 | 42 | 0.50 | 0.50 | 1.0 | 50 (100%) | -- |
| plan006-prolog-sta-s43 | 43 | 0.38 | 0.0704 | 0.1853 | 0 strict, 37 H1 (97.4%) | 0 |
| plan006-prolog-sta-s44 | 44 | 0.97 | 0.885 | -- | 97.9% functional H7 | 0 |

All 3 seeds: 0% genuine -- different Goodhart pathways.

---

### HACKING TAXONOMY COMPARISON (plan012)

ISR beta=0.1 vs Random beta=0.1 (seed=42):
- ISR genuine_rate: 25.9% vs Random: 17.7% (delta=+8.2pp)
- ISR conclusion_embedding: 72.8% vs Random: 78.5%
- ISR genuine_mean_isr: 0.6723 vs Random: 0.3427 (ISR quality 2x higher)
- ISR complexity_wo_utility: 0% vs Random: 3.8%

---

### DOWNSTREAM NLI (plan014, negative)

- overall_accuracy=34.1%, proved_rate=91.5%
- Spearman rho(ISR, correct) = -0.049 (p=0.187, not significant)
- Best-of-N ISR accuracy=35.0% vs random=34.1% (+0.9pp, not significant)
- ISR bucket trend: high=75%, mid=37.7%, low=32.7% (weak monotonic but high bucket n=12 only)
- Mann-Whitney U=17202, p=0.288

---

### EARLY-PHASE PILOTS (100 steps)

| Exp ID | Reward | K | PR | ISR | Notes |
|---|---|---|---|---|---|
| sta-phase1-exec-only-r4 | exec | -- | 0.151 | 0.148 | Binary ISR, no differentiation |
| sta-phase1-exec-only-r5 | exec | 8 | 0.151 | 0.148 | K=8, still no diff |
| sta-phase1-exec-sta-r4 | exec+STA | -- | 0.158 | 0.153 | Binary ISR ~= exec-only |
| sta-phase1-exec-sta-r5 | exec+STA (continuous) | 8 | 0.10 | 0.043 | ISR/PR ratio=0.43, separation visible |

---

All metric fields present in the registry have been extracted. The key paper-relevant numbers are the taxonomy breakdowns (H7/H1/H8/genuine counts and rates), prove rates, ISR values, and the cross-condition comparisons. Notable data quality caveats flagged in the registry: some early experiments used wrong test set (test_100.jsonl vs proofwriter_fol_100.jsonl) and were invalidated; D086 clean runs corrected several H7/H1 misclassifications; and training-log ISR values are binary approximations that should not be used for cross-experiment comparison.

agentId: acf8d8db20c645266 (use SendMessage with to: 'acf8d8db20c645266' to continue this agent)
&lt;usage>total_tokens: 74220
tool_uses: 15
duration_ms: 181612&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "ea449b32-4c35-4739-aeb7-05120cdcf1f3",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Extract key experiment metrics from a large JSON registry file for a paper audit.\n\nThe file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_registry-1778860609862.txt\n\nFormat: JSON with schema: {result: string} — the \"result\" field is itself a JSON string that needs parsing.\n\nI need you to extract ALL experiments with status=SUCCESS or conclusion containing \"success\" or \"negative\", and for each one report:\n- exp_id\n- status / conclusion\n- All metrics (PR, ISR, H7%, H1%, genuine%, etc.)\n- Any notes or decisions referenced\n\nUse jq or python to parse. Return a comprehensive table/list of all experiment metrics. Be thorough — I need every number that might appear in a paper.",
    "agentId": "acf8d8db20c645266",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete extraction of all 49 experiments with conclusion \"success\" or \"negative\" from the registry.\n\n---\n\n## Summary: 49 experiments extracted (29 success, 20 negative)\n\n### BASELINES\n\n**sta-phase0-baseline [success]** -- Pre-training Qwen3-4B base model\n- PR=0.12, ISR=0.0641, ISR_std=0.1983, median_ISR=0, n_proved=12/100\n- By answer type: true PR=0.265/ISR=0.1345, false PR=0.04/ISR=0.024, unknown PR=0.049/ISR=0.0302\n\n**sta-gt-isr-baseline [success]** -- Ground-truth FOL upper bound\n- gt_prove_rate=0.18, gt_mean_isr=0.5588, gt_isr_std=0.2582, gt_isr_median=0.6125\n- true_prove_rate=0.5, true_mean_isr=0.5833\n\n**plan003-eval-exec-only-r5 [success]** -- 100-step exec-only checkpoint eval\n- PR=0.32, ISR=0.2055, ISR_std=0.3194, ISR*=0.6423\n\n---\n\n### SFT BASELINES (500-step and 1000-step, 3 seeds)\n\n| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | H8 | Genuine | Genuine% |\n|---|---|---|---|---|---|---|---|---|---|---|\n| plan009-sft-s42-r4 | 500 | 42 | 0.14 | 0.08 | 0.571 | 0 | 1 | -- | 13 | 92.9% |\n| plan009-sft-s43 | 500 | 43 | 0.15 | 0.0895 | 0.5967 | 0 | 1 | -- | 14 | 93.3% |\n| plan009-sft-s44 | 500 | 44 | 0.17 | 0.0974 | 0.5729 | 0 | 2 | -- | 15 | 88.2% |\n| plan009-sft-s42-1000 | 1000 | 42 | 0.13 | 0.0738 | 0.5677 | 0 | 1 | 0 | 12 | 92.3% |\n| plan009-sft-s43-1000 | 1000 | 43 | 0.11 | 0.0699 | 0.6352 | 0 | 1 | 0 | 10 | 90.9% |\n| plan009-sft-s44-1000 | 1000 | 44 | 0.15 | 0.0884 | 0.5892 | 0 | 1 | 0 | 14 | 93.3% |\n\nKey: SFT maintains >88% genuine rate across all seeds and steps. No Goodhart collapse.\n\n---\n\n### EXEC-ONLY (FOL, 3 seeds)\n\n| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | H8 | Genuine | Genuine% | Tautological |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan001-s42-r2 | 500 | 42 | 0.93 | 0.1232 | 0.1324 | 0 | 81 | 6 | 7 | 7.5% | No |\n| plan001-s43-r4 | 500 | 43 | 0.13 (greedy) / 0.14 (sampling) | 0 | 0 | 0 | 13 (100%) | -- | 0 | 0% | -- |\n| plan001-s44 | 500 | 44 | 0.98 | 0.57 | 0.5816 | 97 | 0 | -- | 0 | 0% | Yes |\n| plan016-extended-1000-s42 | 1000 | 42 | 0.96 | 0.003 | -- | 0 | 96 (100%) | -- | 0 | 0% | -- |\n\nplan001-s43-r4 additional: greedy components_proved=18.92, sampling components=18.5, decoding-invariant collapse.\n\n---\n\n### ISR beta=0.1 (Additive, FOL)\n\n| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | H8 | Genuine | Genuine% | Taut |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan002-b01-s42 | 500 | 42 | 0.81 | 0.3365 | 0.4154 | 13 | 42 | 12 | 14 | 17.3% | No |\n| plan002-b01-s43 | 500 | 43 | 0.61 | -- | 0.83 | 59 | 0 | 0 | 2 | 3.3% | -- |\n| plan002-b01-s44 | 500 | 44 | 0.89 | 0.803 | 0.902 | 89 (100%) | 0 | 0 | 0 | 0% | -- |\n| plan002-b01-s42-1000 | 1000 | 42 | 0.90 | 0.7892 | 0.8769 | 87 | 0 | 1 | 2 | 2.2% | Yes |\n\n---\n\n### ISR beta=0.3 (Additive, FOL)\n\n| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | H8 | Genuine | Genuine% |\n|---|---|---|---|---|---|---|---|---|---|---|\n| plan002-b03-s42 | 500 | 42 | 0.18 | 0.0257 | 0.1427 | 0 | 14 | 3 | 1 | 5.6% |\n| exp1-isr-b03-s43-r3 | 500 | 43 | 0.86 | 0.2535 | 0.2948 | 4 | 59 | -- | 23 | 26.7% |\n| exp1-isr-b03-s44-r2 | 500 | 44 | 0.95 | 0.705 | 0.7421 | 95 (100%) | 0 | -- | 0 | 0% |\n| exp1-isr-b03-s42-1000-r2 | 1000 | -- | 0.95 | 0.734 | 0.7726 | 0 | 54 | 41 | 0 | 0% |\n\n---\n\n### RANDOM BASELINES (Additive, FOL)\n\n**Convex random (plan013, r=0.9*exec+0.1*random):**\n\n| Exp ID | Steps | Seed | PR | ISR | H7 | Genuine | Taut |\n|---|---|---|---|---|---|---|---|\n| plan013-random-s42-r4 | 500 | 42 | 1.0 | 0.535 | 100 (100%) | 0 | Yes (degenerate 2-component) |\n\n**Additive random beta=0.3:**\n\n| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | Genuine |\n|---|---|---|---|---|---|---|---|---|\n| plan017-random-s42 | 500 | 42 | 0.48 | 0.0453 | 0.0943 | 0 | 48 (100%) | 0 |\n| exp1-random-b03-s43-r4 | 500 | 43 | 0.92 | 0.1659 | 0.1803 | 7 | 82 | 3 (3.3%) |\n| exp1-random-b03-s44-r2 | 500 | 44 | 0.23 | 0 | 0 | 0 | 23 (100%) | 0 |\n\n**Additive random beta=0.1:**\n\n| Exp ID | Steps | Seed | PR | ISR | ISR* | H7 | H1 | H8 | Genuine | Genuine% |\n|---|---|---|---|---|---|---|---|---|---|---|\n| plan018-random-b01-s42 | 500 | 42 | 0.79 | 0.1038 | 0.1314 | 0 | 56 | 3 | 18 | 22.8% |\n| plan018-random-b01-s43-r2 | 500 | 43 | 0.88 | 0.058 | -- | 0 | 82 | -- | 6 | 6.8% |\n| plan018-random-b01-s44 | 500 | 44 | 0.89 | 0.0619 | 0.0695 | -- | -- | -- | -- | -- |\n| plan018-random-b01-s42-1000-r3 | 1000 | 42 | 0.97 | 0.6892 | 0.7105 | 97 (100%) | 0 | 0 | 0 | 0% |\n\n---\n\n### O(1) BINARY ISR ABLATION\n\n| Exp ID | Steps | Seed | PR | ISR | H7 | H1 | H8 | Genuine |\n|---|---|---|---|---|---|---|---|---|\n| plan004-o1-ablation-s42 | 500 | 42 | 0.63 | 0.0072 | 0 | 63 (100%) | 2 | 0 |\n\nConfirms: O(1) binary ISR degrades to exec-only. LOO ablation O(N) is necessary.\n\n---\n\n### STA-LOW (alpha=0.1 convex penalty)\n\n**plan005-sta-low-s42 [negative]:** Training-only metrics (no eval checkpoint):\n- Windowed PR/ISR: steps 1-50: 0.178/0.091, 101-200: 0.506/0.146, 301-400: 0.701/0.198, 401-500: 0.773/0.230\n- ISR/PR ratio=0.298 (99/100 steps ISR < PR), confirms STA suppresses reward hacking\n\n---\n\n### PROLOG CROSS-LOGIC (exec-only, 3 seeds)\n\n| Exp ID | Reward | Seed | PR | ISR | ISR* | H7 | Genuine |\n|---|---|---|---|---|---|---|---|\n| plan006-prolog-exec-s42 | exec | 42 | 0.83 | 0.031 | 0.037 | 0% | -- |\n| plan006-prolog-exec-s43-r3 | exec | 43 | 0.56 | 0.0084 | 0.015 | -- | -- |\n| plan006-prolog-exec-s44 | exec | 44 | 0.21 | 0.0812 | 0.3866 | -- | -- |\n\n3-seed mean: PR=53.3% +/- 31.1%, ISR=0.040 +/- 0.037\n\n### PROLOG CROSS-LOGIC (exec+STA, 3 seeds)\n\n| Exp ID | Seed | PR | ISR | ISR* | H7 | Genuine |\n|---|---|---|---|---|---|---|\n| plan006-prolog-sta-s42 | 42 | 0.50 | 0.50 | 1.0 | 50 (100%) | -- |\n| plan006-prolog-sta-s43 | 43 | 0.38 | 0.0704 | 0.1853 | 0 strict, 37 H1 (97.4%) | 0 |\n| plan006-prolog-sta-s44 | 44 | 0.97 | 0.885 | -- | 97.9% functional H7 | 0 |\n\nAll 3 seeds: 0% genuine -- different Goodhart pathways.\n\n---\n\n### HACKING TAXONOMY COMPARISON (plan012)\n\nISR beta=0.1 vs Random beta=0.1 (seed=42):\n- ISR genuine_rate: 25.9% vs Random: 17.7% (delta=+8.2pp)\n- ISR conclusion_embedding: 72.8% vs Random: 78.5%\n- ISR genuine_mean_isr: 0.6723 vs Random: 0.3427 (ISR quality 2x higher)\n- ISR complexity_wo_utility: 0% vs Random: 3.8%\n\n---\n\n### DOWNSTREAM NLI (plan014, negative)\n\n- overall_accuracy=34.1%, proved_rate=91.5%\n- Spearman rho(ISR, correct) = -0.049 (p=0.187, not significant)\n- Best-of-N ISR accuracy=35.0% vs random=34.1% (+0.9pp, not significant)\n- ISR bucket trend: high=75%, mid=37.7%, low=32.7% (weak monotonic but high bucket n=12 only)\n- Mann-Whitney U=17202, p=0.288\n\n---\n\n### EARLY-PHASE PILOTS (100 steps)\n\n| Exp ID | Reward | K | PR | ISR | Notes |\n|---|---|---|---|---|---|\n| sta-phase1-exec-only-r4 | exec | -- | 0.151 | 0.148 | Binary ISR, no differentiation |\n| sta-phase1-exec-only-r5 | exec | 8 | 0.151 | 0.148 | K=8, still no diff |\n| sta-phase1-exec-sta-r4 | exec+STA | -- | 0.158 | 0.153 | Binary ISR ~= exec-only |\n| sta-phase1-exec-sta-r5 | exec+STA (continuous) | 8 | 0.10 | 0.043 | ISR/PR ratio=0.43, separation visible |\n\n---\n\nAll metric fields present in the registry have been extracted. The key paper-relevant numbers are the taxonomy breakdowns (H7/H1/H8/genuine counts and rates), prove rates, ISR values, and the cross-condition comparisons. Notable data quality caveats flagged in the registry: some early experiments used wrong test set (test_100.jsonl vs proofwriter_fol_100.jsonl) and were invalidated; D086 clean runs corrected several H7/H1 misclassifications; and training-log ISR values are binary approximations that should not be used for cross-experiment comparison."
      }
    ],
    "totalDurationMs": 181612,
    "totalTokens": 74220,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4561,
      "cache_read_input_tokens": 65781,
      "output_tokens": 3877,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4561
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3877,
          "cache_read_input_tokens": 65781,
          "cache_creation_input_tokens": 4561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4561,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 8,
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

_source line 84_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the paper TeX files and the registry data. Let me also read the decisions file to check the specific decisions mentioned in the task (D027, D044, D051, D069, D079, etc.).

Let me also check some specific numbers that need verification. Let me systematically go through every quantitative claim in the paper and cross-reference with the registry data.

Let me organize my audit systematically. I'll go through each section of the paper and check every number.

Let me first read the decisions file for the key decisions referenced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "3dd95cac-5c16-4028-b332-30ee2c8c97e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVBArPwEi5aNQBB2svTduG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 61243,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 61243
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

_source line 85_

Now I have the paper content and registry data. Let me read the decisions file to cross-check specific decision constraints, and also check some numbers I noticed that need verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "2aba823d-8be2-40e7-8627-8ec382964703",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVBArPwEi5aNQBB2svTduG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 61243,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 61243
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

_source line 86_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WU3pPzdhrULH7SMH3KXsXM`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
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
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "bd84f755-88fa-4b90-b059-06a3669c08b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVBArPwEi5aNQBB2svTduG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 61243,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 61243
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

_source line 87 · 2026-05-15T16:00:09.976Z_

<details><summary>↩ Tool result · `toolu_01WU3pPzdhrULH7SMH3KXsXM`</summary>

```text
Error: result (75,020 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "70cb20cf-33be-4d8b-9a5e-136f70c56522",
  "tool_use_result": {
    "content": "Error: result (75,020 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 89\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差\\n    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)\\n    避免惩罚。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: prove_rate=0.10 < baseline, STA reward 过于惩罚性\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: control\\n    result: prove_rate=0.15, 复现 r4\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 22:13 UTC\\n  summary: ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 有两种解释：(A) STA 检测到 hacking (B) 50/50 权重抑制 prove\\n    行为的惩罚效应。ISR 绝对值 ~0.05 ≈ pretrained 水平支持解释 B。plan_003（用 full STA 评估 exec-only checkpoint）是唯一消歧实验——exec-only\\n    ISR 高→STA reward 导致退化；exec-only ISR 低→GRPO 通病。paper_framing.md 已将 claim 降级为观察性表述，因果表述需等\\n    plan_003 结果。cuda:1 排列改为 plan_003 eval 先行，再 plan_005 training。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: ISR/PR 下降但因果不清\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: baseline\\n    result: prove_rate=0.12, ISR 未用 full STA 评估\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 22:14 UTC\\n  summary: paper_framing.md \\\"检测 hacking\\\" claim 降级为观察性表述，plan_003 为消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 下降存在混淆效应：可能是 STA 检测到 hacking，也可能是 50/50 权重抑制\\n    prove 行为。ISR 绝对值始终 ~0.05 ≈ pretrained 水平，更像惩罚效应。plan_003（exec-only checkpoint\\n    用 full STA 评估）是消歧实验——完成前 paper 不可用因果表述。已修改 paper_framing.md Claim 1 MVP 证据段。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence_source\\n    result: ISR/PR 下降观察到但因果不清\\n  - exp_id: plan_003\\n    role: disambiguation\\n    result: planned\\n  depends_on:\\n  - D004\\n- id: D007\\n  date: 2026-05-13 23:05 UTC\\n  summary: plan003 因果消歧：exec-only ISR 提升是有机的，50/50 STA 权重是退化根因，STA 概念本身无问题\\n  rationale: plan003 eval 显示 exec-only 100步 checkpoint 的 held-out prove_rate=0.32（baseline\\n    0.12 的 2.7x），proved_only_isr=0.642（远高于 exec+STA r5 的 0.043）。ISR 随 prove_rate 同步提升，排除\\n    reward hacking。exec+STA 50/50 权重导致 prove_rate 低于 baseline（0.10<0.12），确认权重过高是退化根因。\\\"STA\\n    as reward\\\" 叙事仍成立，需精确权重调校。注意：当前结果基于 100-step checkpoint，500-step 需重新验证。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: primary\\n    result: prove_rate=0.32, proved_only_isr=0.642, ISR organic\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: comparison\\n    result: prove_rate=0.10, mean_isr=0.043, degraded\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: comparison\\n    result: prove_rate=0.15(last20:0.20), mean_isr=0.148\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D008\\n  date: 2026-05-13 23:08 UTC\\n  summary: Dream 审稿确认 5 个结构性弱点，plan_003 消歧确认 penalty effect (B)，论文 story 需重构\\n  rationale: Dream best=4/6 Borderline Reject, median=3/6 Weak Reject。两档一致指出：(1) related\\n    work 严重不足 6→25+ refs (2) RIP framing 过度——只有 Propagation 可操作化 (3) ISR circularity\\n    未解决——需下游验证或 random baseline (4) 8/12 实验 single-seed 不足 (5) ISR sparsity 使 \\\"dense+automatic\\\"\\n    定位不成立。plan_003 held-out eval 证实 exec-only checkpoint ISR=0.6423（proved-only），高于\\n    GT 0.56，确认 ISR/PR 下降是 penalty effect 而非 hacking detection（interpretation B）。论文\\n    story 必须从 \\\"STA detects hacking\\\" 转向 \\\"STA as principled structural metric + proper\\n    integration via weight tuning\\\"。新增实验需求：random reward baseline + 3-seed for secondary\\n    + downstream validation + curriculum ablation。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: disambiguation\\n    result: exec-only ISR=0.6423 confirms penalty effect (B)\\n  - exp_id: plan005-sta-low-s42\\n    role: running\\n    result: weight ablation in progress\\n  - exp_id: dream_20260513T215750\\n    role: dream\\n    result: best 4/6, median 3/6\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D009\\n  date: 2026-05-14 00:02 UTC\\n  summary: 添加约束 C001（统一训练数据）和 C002（GPU 隔离验证），因连续两个 confound/越界事故\\n  rationale: plan001-s43 使用了不同训练数据文件（proofwriter_fol_500.jsonl vs train_500_seed42.jsonl），破坏多\\n    seed 对比控制变量。plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43\\n    OOM。两个事故均为 Worker 提交流程缺陷，需要硬约束防止复发。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43\\n    role: trigger\\n    result: failed (data confound + OOM)\\n  - exp_id: plan013-random-reward-s42\\n    role: trigger\\n    result: failed (GPU overflow)\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 framing 转向: STA as metric + additive bonus integration，plan002 改用非凸组合公式'\\n  rationale: 'plan005 negative 确认 penalty effect: 凸组合 r=α·r_exec+β·r_exec·ISR (α+β=1)\\n    下任何 ISR<1 都会惩罚 reward，即使 β=0.1。exec-only (plan003) proved-only ISR=0.6423 远高于\\n    plan005 training ISR=0.23。根本原因: 凸组合约束强制 STA 成为 penalty 而非 bonus。plan002 应改用 additive\\n    bonus: r=r_exec·(1+β·ISR)，β>0，ISR 只能增加 reward 不能减少。Story 正式从 \\\"STA detects hacking\\\"\\n    转为 \\\"STA as principled structural metric + additive bonus integration\\\"。'\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex combination penalty effect confirmed'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: 'success: exec-only ISR=0.6423 >> STA-trained ISR'\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D011\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 Narrative A+C: STA as diagnostic metric 为主线，bonus-only 公式作为集成尝试，放弃\\n    curriculum (B)'\\n  rationale: plan005 negative 确认 multiplicative formulation 的 penalty effect 在所有权重下成立。Narrative\\n    A 将所有 negative 结果转化为证据（penalty effect 分析 + ISR/PR ratio 作为 structural health indicator），降低\\n    DDL 风险。选 C 而非 B：bonus-only 是对 multiplicative penalty 的数学根治（additive, threshold-gated），而\\n    curriculum 只是工程 workaround。C 只需改一行 reward 公式 + 1 次训练（~1.5 GPU·h），ROI 最高。如果 C 也\\n    negative，论文退化为纯 metric paper 仍可投 EMNLP findings。\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: trigger\\n    result: 'negative: weight=0.1 仍 -10.7% prove_rate'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: exec-only ISR=0.6423 proved-only, penalty effect confirmed\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D012\\n  date: 2026-05-14 02:24 UTC\\n  summary: 新增 additive random 对照实验（plan_017），隔离 ISR structural signal vs GRPO regularization\\n    effect\\n  rationale: 'Reviewer 指出 GRPO 饱和不对称 confound: exec-only 在 prove_rate=1.0 时 reward\\n    variance=0 导致 loss=0（停止学习），而 ISR/random 任何引入 variance 的机制都会维持梯度。plan002 additive\\n    ISR 需要匹配的 additive random 对照：r=r_exec·(1+β·random[0,1])。三组比较: (1) ISR>random>exec-only\\n    → signal+regularization 都贡献 (2) ISR>random≈exec-only → ISR signal 是关键 (3) ISR≈random>exec-only\\n    → 纯 regularization，ISR 内容无价值。这是论文 \\\"ISR provides unique structural signal\\\" claim\\n    的必要证据。'\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: motivation\\n    result: 'confound: convex random introduced variance preventing GRPO saturation'\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: motivation\\n    result: 'GRPO saturation confirmed: loss=0 at prove_rate=1.0'\\n  depends_on:\\n  - D010\\n- id: D013\\n  date: 2026-05-14 02:34 UTC\\n  summary: ISR 评估方法论标准化：所有 checkpoint 必须用 eval_sta.py (full STA) 统一重评，训练日志 ISR 不可用于论文\\n  rationale: Reviewer 核实发现：(1) s42-r2 用旧代码 _fast_fn 二值近似，s43-r4 用 _full_fn full STA，跨\\n    seed ISR 不可比；(2) plan013 random_reward 仍用 _fast_fn，训练 ISR≈prove_rate 是二值假象；(3)\\n    只有 eval_sta.py 产出的 proved_only_ISR 是可靠指标。统一用 eval_sta.py 评估所有 checkpoint 后才能做跨实验比较。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: affected\\n    result: 训练 ISR 与 s42-r2 不可比，需 eval_sta.py 重评\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: reference\\n    result: confirmed full STA, proved_only_ISR=0.6423 有效\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练 ISR 不可信(_fast_fn)，需 eval_sta.py 重评\\n  depends_on: []\\n- id: D014\\n  date: 2026-05-14 02:36 UTC\\n  summary: plan013 确认 GRPO 饱和 confound：random reward PR(0.966) > exec-only PR(0.865)，差异源于训练动态而非结构信号\\n  rationale: 'plan013 random reward 实验表明：(1) random noise 通过保持 reward variance 防止\\n    GRPO 饱和，PR 反超 exec-only；(2) 两者 ISR/PR ratio 均≈1.0，random noise 未提供结构信号；(3) 这直接印证\\n    Reviewer #2 的 GRPO 饱和 confound 担忧。结论：exec-only 的 PR→1.0 时 reward_std→0 导致学习停滞，additive\\n    bonus (plan002) 才是正确方案——提供 meaningful variance + anti-saturation。plan013 在论文中应正面叙述\\n    saturation mechanism，将 additive bonus 的 anti-saturation 作为 key design insight。'\\n  related_experiments:\\n  - exp_id: plan013\\n    role: primary\\n    result: random reward PR=0.966 > exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan001-s42-r2\\n    role: baseline\\n    result: exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan002\\n    role: hypothesis\\n    result: running - additive bonus expected to provide meaningful variance + anti-saturation\\n  depends_on: []\\n- id: D015\\n  date: 2026-05-14 02:38 UTC\\n  summary: 训练日志 ISR 跨 seed 不可比，所有 checkpoint 必须用 eval_sta.py 统一评估获取 full STA ISR\\n  rationale: Reviewer 核实发现：plan001-s42-r2 用 _fast_fn (binary ISR≈prove_rate)，plan001-s43-r4\\n    用 _full_fn (连续 ISR)，两者训练日志 ISR 不可比。plan013-r4 同样是 binary approximation。论文正式数据必须来自\\n    eval_sta.py 的 full STA 评估。此外 plan001-s43-r4 训练中 ISR 崩塌轨迹（prove_rate=1.0 时 ISR=0.01）是\\n    reward hacking 的直接定量证据，强化论文 thesis。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: evidence\\n    result: ISR崩塌轨迹:prove_rate=1.0时ISR=0.01,reward hacking证据\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan003-eval-sta\\n    role: validated\\n    result: proved_only_ISR=0.6423确认为full STA,可信\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-14 03:20 UTC\\n  summary: eval_sta held-out 评估定量证实 exec-only reward hacking：500步 checkpoint prove_rate=0.93\\n    但 ISR=0.1324（median=0.0）\\n  rationale: plan001-r2 exec-only checkpoint-500 在 held-out 100题上的 full STA 评估显示 proved_only_ISR=0.1324，中位\\n    ISR=0.0——模型高 prove_rate 完全依赖 solver 宽松性而非正确 FOL 结构。对比 plan003（100步 checkpoint）的\\n    ISR=0.6423，ISR 随训练从 64% 崩塌到 13%，是 reward hacking 的直接定量证据。跨 seed 一致性已验证（s42 last100\\n    PR=0.865 vs s43 last100 PR=0.883）。这构成论文 Core Claim 1 的核心证据。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: primary\\n    result: held-out PR=0.93, proved_only_ISR=0.1324, median_ISR=0.0\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: replication\\n    result: 训练ISR=0.087(if _full_fn), last100_PR=0.883, 跨seed一致\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: comparison\\n    result: 100步checkpoint ISR=0.6423, 训练前结构质量高\\n  depends_on:\\n  - D015\\n  - D007\\n- id: D017\\n  date: 2026-05-14 03:24 UTC\\n  summary: random reward held-out ISR=0.535 >> exec-only ISR=0.132，anti-saturation\\n    效应可能足以改善结构质量，ISR-specific signal 待 plan002 vs plan017 验证\\n  rationale: plan013 random reward 在 held-out 上 prove_rate=1.0, ISR=0.535, 大幅优于 exec-only\\n    (PR=0.93, ISR=0.132)。Random noise 通过防止 GRPO reward variance→0 的饱和效应让模型持续学习。这挑战了\\\"ISR\\n    提供结构信号\\\"的叙事——可能仅 anti-saturation 就够。关键验证：plan002 (additive ISR) vs plan017 (additive\\n    random) 的 matched control，加上 formalization 组件数对比排除长度 confound。论文叙事可能需要从\\\"ISR reward\\\"转向\\\"GRPO\\n    饱和机制 + STA 诊断工具\\\"。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: held-out PR=1.0, ISR=0.535, median_ISR=0.5, min_ISR=0.5\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: held-out PR=0.93, ISR=0.132, median_ISR=0.0\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending\\n    result: 中期PR严重偏低(39.8%步PR=0),待完成\\n  - exp_id: plan017-additive-random-s42\\n    role: pending\\n    result: 刚启动,matched control\\n  depends_on:\\n  - D016\\n  - D014\\n- id: D018\\n  date: 2026-05-14 03:31 UTC\\n  summary: 推翻 D017：plan013 held-out ISR=0.535 是 tautological hacking 假象（100% P→P），random\\n    reward 加速 hacking 而非改善结构\\n  rationale: Reviewer 逐样本检查 plan013 eval_sta 结果：100/100 样本全部是「把 conclusion 抄一遍当 premise」(P→P\\n    tautology)，ISR=0.5 是机械值（2 components, 1 necessary）而非真实结构质量。D017 基于 ISR=0.535 得出的\\\"anti-saturation\\n    改善结构\\\"结论完全错误。实际情况：random reward 让模型找到了最终极的 hacking 捷径——100% tautological formalization。对比\\n    exec-only 100步 ISR=0.6423（有真实推理）→ 500步 ISR=0.132（退化但非全 tautological），random reward\\n    加速了 hacking 收敛。plan002 eval_sta 结果成为关键：如果 additive ISR bonus 产生的是非 tautological\\n    formalization，即使 PR 低也是积极信号——ISR reward 在抵抗 hacking。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: 100% tautological P→P, ISR=0.5 是机械值而非结构质量\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: comparison\\n    result: held-out PR=0.93, ISR=0.132, 部分真实推理\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending_critical\\n    result: PR低但可能是真实推理, eval_sta 待出\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-14 03:33 UTC\\n  summary: ISR 衡量 syntactic component necessity 而非 semantic faithfulness，论文需明确边界并用\\n    plan014 downstream validation 补盲区\\n  rationale: Reviewer 发现 ISR 反直觉行为：plan013 P→P 纯重言式 ISR=0.5 > plan001 多前提嵌入 conclusion\\n    ISR≈0。从语义忠实度看 P→P 更差（完全忽略 context），但 ISR 定义下反而更高，因为 ISR=n_necessary/n_components，极简\\n    formalization 的分母小。论文不能将 ISR 差异直接等同于 formalization 质量差异——需明确 ISR 的 scope 是 component\\n    necessity。plan014 downstream NLI validation 直接测量 semantic faithfulness，弥补 ISR\\n    盲区。同时建议考虑组合指标（ISR + non-tautological check + 最小组件数阈值）。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: P→P tautology ISR=0.5, 语义完全退化但ISR不低\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: evidence\\n    result: 多前提嵌入conclusion ISR≈0, 语义更好但ISR更低\\n  - exp_id: plan014\\n    role: mitigation\\n    result: downstream NLI validation 补充语义忠实度测量\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-14 03:40 UTC\\n  summary: plan002 additive ISR β=0.3 负面结果确认：PR=18% + ISR=0.1427，ISR reward 作为训练信号的路线全面失败，论文转向纯诊断/分析贡献\\n  rationale: 'plan002 held-out eval: PR=18%（最差）, ISR=0.1427≈exec-only 0.1324。加上 plan005\\n    (convex, negative) 和 plan013 (random, tautological hacking)，所有 ISR-as-reward 方案均失败。但三个条件产生了三种不同的退化模式（conclusion\\n    embedding / P→P tautology / repetitive cycling），这本身是有价值的研究发现。论文应完全放弃\\\"ISR reward\\n    改善训练\\\"的 claim，转向：(1) STA/ISR 作为诊断工具检测 reward hacking (2) GRPO saturation 机制分析 (3)\\n    不同 reward 信号下的 hacking 策略分类学 (4) ISR 随训练的崩塌轨迹。plan014 downstream validation 成为证明\\n    ISR 诊断价值的关键实验。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: primary\\n    result: 'negative: PR=18%, ISR=0.1427, 重复前提循环退化'\\n  - exp_id: plan005-sta-low-s42\\n    role: prior_negative\\n    result: convex combination penalty effect\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 100% tautological hacking, ISR=0.5 假象\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.132, conclusion embedding\\n  depends_on:\\n  - D018\\n  - D019\\n  - D010\\n- id: D021\\n  date: 2026-05-14 04:28 UTC\\n  summary: plan014 ISR-accuracy 假说被否定；ISR 定位为 syntactic necessity 指标，不 claim semantic\\n    quality proxy\\n  rationale: Spearman ρ(ISR, entailment_accuracy) = -0.049, p=0.187（n=732），ISR-based\\n    BoN Δ=0.88pp CI含零。同时发现系统性 true 偏差（gold=true 91.2% acc, gold=false 0%），说明 formalization\\n    pipeline 本身有 truth bias。ISR 衡量组件必要性（去掉后证明是否成立），不衡量 formalization 是否语义忠实。论文应明确此\\n    limitation，将 plan014 作为 negative result 诚实报告，刻画 ISR 能力边界。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: primary\\n    result: negative — ISR与下游NLI准确率无显著相关\\n  depends_on: []\\n- id: D022\\n  date: 2026-05-14 04:30 UTC\\n  summary: 选备选 A：ISR downstream 验证降级为 limitation/future work，不追加 NLI 替代实验\\n  rationale: ISR 结构价值已有 component count 差异（p<0.0001）和 cross-checkpoint 对比强证据。NLI negative\\n    源于 formalization model 的 true-bias（非 ISR 本身缺陷），换 downstream 任务（B）在同一 model 上大概率复现同样问题。n=12\\n    的 bucket 趋势（C）统计不可靠。聚焦 plan017 + s44 完成核心证据链。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: negative\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-14 05:31 UTC\\n  summary: paper_framing.md 全量重写：4 条诊断/分析 claims 替代旧 2 条 reward methodology claims，与\\n    D020 pivot 一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，但 D020 已确认 ISR-as-reward 全面失败。新 framing 4 条 claims:\\n    (1) ISR as hacking diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism, (3) hacking\\n    taxonomy (4 种模式), (4) ISR capability boundary (syntactic necessity ≠ semantic\\n    faithfulness)。Story spine 从 \\\"propose structural reward\\\" 转为 \\\"diagnostic tool +\\n    systematic empirical study of reward hacking\\\"。负面结果表（convex/additive/random）作为正面贡献呈现。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: negative_evidence\\n    result: PR=18%, ISR=0.14, repetitive cycling\\n  - exp_id: plan005-sta-low-s42\\n    role: negative_evidence\\n    result: convex penalty effect confirmed\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: negative_evidence\\n    result: 100% tautological, ISR=0.5 mechanical\\n  - exp_id: plan014-downstream-nli-s42\\n    role: negative_evidence\\n    result: ρ=-0.049 n.s., ISR ≠ semantic quality\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: core_evidence\\n    result: ISR collapse 64%→13%, hacking detected\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-14 05:32 UTC\\n  summary: 批准 plan006 Prolog GRPO 执行，3 seeds，强化跨 logic type 泛化性（原 P1 提升为紧急）\\n  rationale: 诊断/分析论文如果只有 FOL 一种逻辑类型，venue 风险高（可能降至 Findings）。plan006 Prolog 验证 hacking\\n    现象是否跨 logic type 泛化，6 GPU·h 成本低（vs 528 GPU·h 可用）。Reviewer 明确指出 generalizability\\n    是论文能否进 Main 的关键因素。先跑 exec-only seed=42 验证方向，成功再 3-seed。\\n  related_experiments:\\n  - exp_id: plan006\\n    role: planned\\n    result: Prolog GRPO exec-only vs exec+STA, 3 seeds\\n  depends_on:\\n  - D020\\n- id: D025\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为 reward 比 random noise 更差：additive random PR=48% > additive\\n    ISR PR=18%。ISR 信号对训练有害，论文诊断定位全面确认\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) held-out eval: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (PR=18%, ISR=0.026, components=10.67)，random\\n    noise 在相同公式结构下 PR 高 2.7 倍。关键洞察：(1) ISR 结构信号对 GRPO 训练有害而非无用；(2) additive 乘法结构本身防止\\n    tautological collapse（两者 components 9-10 vs plan013 的 2.04）；(3) 但 additive 结构也无法产生\\n    genuine proofs（PR 远低于 exec-only s42 的 93%）。六组实验全景完整：exec-only 是唯一产生 genuine proofs\\n    的方案（1/3 seeds），ISR 应定位为 post-hoc diagnostic，非 training signal。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, components=9.56, complex-but-useless'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: PR=100% but 100% tautological, components=2.04\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, only genuine proofs (1/3 seeds)\\n  depends_on:\\n  - D020\\n  - D018\\n- id: D026\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为训练信号比 random noise 更差（PR 18% vs 48%），ISR 信号对 GRPO 训练有害，完全确立\\n    diagnostic-only 定位\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) eval_sta: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (β=0.3): PR=18%, ISR=0.026,\\n    components=10.67。ISR 结构信号不仅无法改善训练，反而比 random noise 更差——ISR 信号对训练动态有害。两个 additive\\n    方案都保持高 component count（9-10），说明乘法结构 r_exec·(1+βX) 本身防止 tautological collapse，但不产生\\n    genuine proofs。Exec-only (s42) 仍是唯一产生 genuine proofs 的方案（PR=93%），但 2/3 seeds 失败。论文六组实验消融完整，强化\\n    ISR diagnostic-only 定位：ISR 应用于 post-hoc 诊断而非 reward shaping。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, complex-but-useless formalization'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: 'success: PR=93%, ISR=0.132, only genuine proofs'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 'tautological: PR=100%, ISR=0.535, P→P collapse'\\n  depends_on:\\n  - D020\\n  - D018\\n  - D012\\n- id: D027\\n  date: 2026-05-14 05:35 UTC\\n  summary: 采纳备选 A+B：plan017 加入 Claim 2 证据 + Claim 3 增加第 5 种 hacking mode \\\"complexity-without-utility\\\"；Reviewer\\n    关于 plan013 vs plan017 公式差异的 warning 纳入写作约束\\n  rationale: 'plan017 结果完善了六组消融对比。备选 A 将 plan017 加入 Claim 2（GRPO 对 reward perturbation\\n    敏感）是必须的数据更新。备选 B 增加第 5 种 hacking mode（complexity-without-utility: 高 component\\n    但 conclusion 不依赖任何 premise）丰富 taxonomy，区别于 exec-only 的 conclusion embedding。Reviewer\\n    指出 plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 不是纯 additive\\n    vs convex 对照（公式结构+random 影响方式两个变量），论文措辞需精确标注差异，不可简化为\\\"additive vs convex\\\"。plan017\\n    vs plan002 的对比（random PR=48% vs ISR PR=18%）作为论文 §5 核心证据。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, complexity-without-utility mode'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'ISR worse than random: PR=18% vs 48%'\\n  depends_on:\\n  - D026\\n  - D020\\n- id: D028\\n  date: 2026-05-14 05:35 UTC\\n  summary: paper_framing.md 全面重写：3 条诊断/分析 claims 替代旧 2 条 method claims，与 D020 pivot\\n    一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，与 D020 pivot 严重矛盾。重写为 3 条诊断 claims: (1) ISR as hacking\\n    diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism (variance redirection), (3)\\n    cross-logic generality (conditional on plan006)。Story spine 从 \\\"ISR improves training\\\"\\n    转为 \\\"ISR detects hacking + 4 hacking modes + saturation trap\\\"。ISR-as-reward failure\\n    log 保留所有 negative results 作为论文贡献。Headline result 更新为诊断发现而非方法改进。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: evidence\\n    result: 'negative: PR=18%, ISR=0.1427'\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex penalty'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: tautological collapse\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: 'negative: ρ=-0.049'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, hacking confirmed\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D029\\n  date: 2026-05-14 06:28 UTC\\n  summary: plan001-s43 不重训，论文标注 eval 方法差异\\n  rationale: s43 PR=14% 是 failure case（repetition collapse），无论 sampling eval 还是 full\\n    STA 结论不变。主 story 用 s42(hacking) vs s44(tautological) 对比，s43 只作为第三种 failure mode\\n    的佐证。重训 1h GPU 不值得，标注方法差异即可。\\n  related_experiments:\\n  - exp_id: plan001-s43\\n    role: subject\\n    result: negative, PR=14%, checkpoint deleted\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 06:29 UTC\\n  summary: plan005 不重训，论文用训练曲线数据作为 convex formula 负面证据\\n  rationale: plan005 是 negative result（convex公式 ISR/PR ratio=0.298, 99/100步 ISR&lt;PR），用于解释为什么从凸组合切换到\\n    additive bonus。训练曲线 windowed metrics 足以支撑这个 narrative，不需要 held-out eval。checkpoint\\n    已删除，重训 1h 收益极低。\\n  related_experiments:\\n  - exp_id: plan005\\n    role: subject\\n    result: negative, convex formula abandoned\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 06:48 UTC\\n  summary: β=0.1 ISR 结果异常好(PR=0.81/ISR=0.415)，紧急补 β=0.1 random control 后再决定是否调整 framing\\n  rationale: β=0.1 additive ISR 是所有条件中唯一同时高 PR + 高 ISR 的。但无法确定优势来自 ISR structural\\n    signal 还是 variance regularization——缺少 matched β=0.1 random control。在补控制实验之前暂不调整\\n    paper_framing.md。若 β=0.1 random PR高但ISR低 → ISR 在低剂量下真正提升结构质量，narrative 升级为\\\"dose-dependent\\n    reward shaping\\\"；若 β=0.1 random 也高ISR → 优势来自 regularization，维持当前 framing。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: PR=0.81, ISR=0.415, best structural quality\\n  - exp_id: plan017\\n    role: existing_control\\n    result: β=0.3 random, PR=0.48, ISR=0.094\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D032\\n  date: 2026-05-14 06:49 UTC\\n  summary: β=0.1 ISR success 暂不改 framing，先跑 β=0.1 random matched control\\n  rationale: plan002-b01 (β=0.1) PR=0.81/ISR=0.415 是重大正面结果，但 Reviewer 正确指出：缺 β=0.1\\n    random control 无法区分\\\"ISR structural signal\\\"和\\\"low-dose regularization effect\\\"。β=0.3\\n    有 matched random (plan017)，β=0.1 没有。在 control 结果出来前修改 framing 是冒进的——如果 β=0.1 random\\n    也给高 ISR，则 ISR 无特殊价值。Control 仅需 ~1h GPU，成本极低。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: success, PR=0.81, ISR=0.415\\n  - exp_id: plan017\\n    role: precedent\\n    result: β=0.3 random control, PR=0.48\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D033\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 升级为 Goodhart 主线：ISR 在低剂量(β=0.1)有效、高剂量(β=0.3)崩溃，统一用 Goodhart's Law\\n    解释\\n  rationale: plan018 eval 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random control，PR 持平）。β=0.3\\n    下 ISR < random 是 Goodhart 过度优化。统一叙事：ISR 作为 proxy metric 遵循 Goodhart's Law —— diagnostic\\n    有价值 (Claim 1)、低剂量优化有效、高剂量导致 Goodhart 崩溃。覆盖所有实验结果且有理论锚点。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.104, confirms ISR signal genuine'\\n  - exp_id: plan002-b03\\n    role: high_dose\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: high_dose_control\\n    result: 'random β=0.3: PR=0.48, random > ISR at high dose'\\n  - exp_id: plan016\\n    role: temporal_goodhart\\n    result: 1000-step ISR=0.003, temporal dimension of Goodhart\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D034\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 选 C+A 混合：Goodhart 为主线叙事，ISR 诊断保留为 Claim 1，Claim 2 从\\\"ISR misleading\\\"升级为\\\"ISR\\n    exhibits dose-dependent Goodhart effect\\\"\\n  rationale: plan018 确认 β=0.1 ISR 的结构优势是真实信号（proved_only ISR 0.415 vs random 0.131,\\n    3.2x），非 variance regularization。全景数据：β=0.1 ISR>>random（有效）、β=0.3 ISR<&lt;random（Goodhart\\n    崩塌）。选 C（Goodhart 主线）因为：1) 统一所有实验结果在一个叙事下；2) Goodhart's Law 审稿人熟悉，不需要大量额外文献；3)\\n    提供理论解释力而非仅经验观察。融入 A 的元素：ISR 不仅是诊断工具，低剂量下也是有效 reward signal，这是实用贡献。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR signal is genuine'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR beats random at high β'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D035\\n  date: 2026-05-14 08:25 UTC\\n  summary: 'Framing 选 C: Goodhart 主线 — ISR 展示经典 Goodhart 效应（β=0.1 有效, β=0.3 崩塌）'\\n  rationale: plan018 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random, PR 持平）。三个备选中 C 最强：(1)\\n    统一所有结果（诊断→优化→Goodhart 崩塌）为一条叙事线；(2) Goodhart's law 是 ML 审稿人熟悉的理论锚点；(3) 剂量-效应数据（β=0.1\\n    有效 vs β=0.3 灾难）是异常干净的实证；(4) 连接到更广泛的 RL alignment 关切，提升论文影响力。Claim 2 从 \\\"ISR actively\\n    misleading\\\" 修订为 \\\"ISR exhibits classic Goodhart effect with dose-dependent dynamics\\\"。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR structural signal'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR > random at high dose'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D036\\n  date: 2026-05-14 08:35 UTC\\n  summary: 为 beta=0.1 补跑多 seed (s43/s44) 验证 ISR vs random 的稳健性\\n  rationale: exec-only 已知 seed variance 极大 (s42/s43/s44 三种完全不同行为)。beta=0.1 当前仅 s42\\n    单 seed，ISR (PR=0.81) vs random (PR=0.79) 差距仅 2pp，单 seed 不足以区分 signal 和 noise。ISR\\n    差距 (0.337 vs 0.104) 需要多 seed 确认。用户主动提出，判断正确。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR beta=0.1 baseline (单seed)\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random beta=0.1 control (单seed)\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan001-exec-only-s43\\n    role: seed variance 前车之鉴\\n    result: PR=14% degenerate\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-14 08:55 UTC\\n  summary: ISR β=0.1 质量验证路径：先 hacking taxonomy 对比，必要时加 LLM-as-judge\\n  rationale: ISR 更高不等于质量更好（plan014 NLI negative）。用户指出需要独立于 ISR 的质量证据。Hacking taxonomy\\n    是最直接的结构质量指标，但可能覆盖不全。LLM-as-judge 作为补充手段，覆盖 taxonomy 未涵盖的 hacking 模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 待分析\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random β=0.1 待分析\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan012\\n    role: hacking taxonomy 框架\\n    result: 5 modes identified\\n  depends_on:\\n  - D036\\n- id: D038\\n  date: 2026-05-14 09:05 UTC\\n  summary: Hacking taxonomy 结果足够，跳过 LLM-as-judge；taxonomy 对比覆盖 plan012 scope\\n  rationale: 规则分类（ISR/component count）100% 覆盖 160 样本，4 类别划分清晰。核心发现：ISR β=0.1 genuine\\n    +8.2pp vs random，conclusion embedding 73-79% 主导。LLM-as-judge 增加主观性/复现顾虑，边际收益低。Taxonomy\\n    对比分析（81+79=160 样本，系统化规则分类）实质替代 plan012 手工标注方案。\\n  related_experiments:\\n  - exp_id: plan012\\n    role: fulfilled_by_taxonomy\\n    result: ISR genuine 25.9% vs random 17.7%\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR_condition\\n    result: genuine 21/81\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random_control\\n    result: genuine 14/79\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-14 09:41 UTC\\n  summary: plan002-b01-s44 重分类：从 success 改为 semantic drift hacking mode，ISR=0.803\\n    是结构最小性产物\\n  rationale: Reviewer 逐样本审查发现 s44 避免了 tautological collapse 但进入新退化模式：65% 样本 ISR=1.0（前提≈结论\\n    conclusion embedding），模型生成极简形式化通过结构最小性骗过 ISR。高 ISR 不代表证明质量。这实际强化 Claim 1（ISR 是诊断工具而非\\n    reward 信号）的 Goodhart 叙事——ISR-as-reward 改变 collapse mode 但不消除 hacking。Hacking taxonomy\\n    需增加第 6 种模式 \\\"Semantic Drift\\\"。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: primary\\n    result: semantic drift hacking (reclassified from success)\\n  depends_on: []\\n- id: D040\\n  date: 2026-05-14 09:41 UTC\\n  summary: 'plan002-b01-s44 reclassified: \\\"success\\\" → \\\"new hacking mode (conclusion\\n    duplication + ISR inflation)\\\"'\\n  rationale: 'Reviewer critical: s44 ISR=0.902 超过 GT ISR=0.559，模型生成单 premise≈conclusion\\n    的极简形式化，通过 conclusion sub-component ablation 膨胀 ISR。不是 tautological collapse 但仍是\\n    reward hacking。这强化 Claim 1（ISR as diagnostic not reward）——ISR-as-reward 改变 hacking\\n    mode 但不消除 hacking。Hacking taxonomy 需增加第 6 种模式。3-seed β=0.1 统计需加 caveat 或分开报告。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: subject\\n    result: ISR=0.902 is artifact of conclusion duplication, not genuine quality\\n  - exp_id: plan002-additive-b01-s42\\n    role: comparison\\n    result: ISR=0.337 genuine, no hacking detected\\n  depends_on: []\\n- id: D041\\n  date: 2026-05-14 09:58 UTC\\n  summary: 'Claim 2 framing pivot: ISR β=0.1 \\\"sweet spot\\\" → \\\"all-dose Goodhart with\\n    dose-dependent hacking modes\\\"'\\n  rationale: 3-seed ISR β=0.1 结果：2/3 seeds (s43, s44) 出现 conclusion duplication hacking\\n    (premise≈conclusion, P→P 重言式)，ISR 被膨胀到 0.83/0.90 (artifact)。仅 s42 可能 genuine (comp=5.58,\\n    ISR=0.415)。\\\"低剂量 ISR 有效引导结构改善\\\"的叙事在多 seed 下不成立。新叙事更强：ISR 作为 reward 在所有测试剂量下都触发 Goodhart——高剂量(β=0.3)\\n    PR collapse + format degeneration，低剂量(β=0.1) 引发更隐蔽的 conclusion duplication hacking。Conclusion\\n    duplication 作为第 6 种 hacking taxonomy 类型。需先验证 s42 是否真正 genuine + random β=0.1 是否也有此模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: evidence\\n    result: PR=0.81, ISR=0.337, comp=5.58, possibly genuine\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: PR=0.61, ISR=0.830 (artifact), 97% premise=conclusion\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: PR=0.89, ISR=0.902 (artifact), 65% conclusion embedding\\n  depends_on: []\\n- id: D042\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR 度量存在结构性盲点：premise≈conclusion 时 conclusion sub-component ablation 虚高\\n    ISR，需修复度量并重新分析\\n  rationale: Reviewer 审查 plan002-b01-s43/s44 发现 2/3 seeds 的高 ISR (0.830/0.902) 源于\\n    premise=conclusion 逐字重复导致的 conclusion sub-component ablation artifact。只有 s42 (ISR=0.337)\\n    反映真实结构质量。ISR 度量在 premise≈conclusion 场景下有结构性盲点——模型学会 P→P 单步证明时，exec reward=1.0\\n    且 ISR 被膨胀至 0.8-1.0。这不仅是 metric bug，更是 ISR-as-reward 诱导的新型 hacking mode（conclusion\\n    duplication），ISR 自身无法检测。行动：(1) 修复 ISR 度量加 premise≈conclusion 检测 (2) 用修复后度量重新分析\\n    s43/s44 (3) 检查 plan018 random control 是否也有此问题 (4) 更新 paper framing：ISR 盲点作为贡献/limitation，hacking\\n    taxonomy 加第 6 类\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: ISR=0.830 inflated by premise≈conclusion duplication (65.6% ISR=1.0)\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: ISR=0.902 inflated by same mechanism\\n  - exp_id: plan002-additive-b01-s42\\n    role: baseline\\n    result: ISR=0.337 genuine (n_comp=5.58, diverse structures)\\n  depends_on: []\\n- id: D043\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR β=0.1 \\\"sweet spot\\\"叙事降级：2/3 seeds ISR 膨胀为 artifact，Claim 2 改为 meta-level\\n    Goodhart\\n  rationale: 'Reviewer critical: s43 ISR=0.830, s44 ISR=0.902 均超 GT ISR=0.559，由 premise=conclusion\\n    单前提证明 + conclusion sub-component ablation 膨胀。仅 s42 ISR=0.337 可能 genuine。ISR bonus\\n    诱导了新型 hacking 模式（Conclusion Duplication + ISR Inflation），而 random β=0.1 控制组产生\\n    redundant premises 不触发此膨胀——证明这是 ISR-specific gaming。Claim 2 叙事从\\\"β=0.1 is sweet\\n    spot\\\"调整为\\\"ISR as reward exhibits meta-level Goodhart: even the diagnostic metric\\n    gets gamed, with 2/3 seeds developing ISR-inflating strategies\\\"。这实际上是更强的贡献。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: possibly genuine seed\\n    result: PR=0.81, ISR=0.337, comp=5.58 — below GT ISR, needs per-sample verification\\n  - exp_id: plan002-additive-b01-s43\\n    role: ISR inflation seed\\n    result: PR=0.61, ISR=0.830, 65.6% ISR=1.0, premise=conclusion pattern\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR inflation seed\\n    result: PR=0.89, ISR=0.902, same conclusion duplication pattern\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random control\\n    result: PR=0.79, ISR=0.104, redundant premises — no ISR inflation\\n  depends_on: []\\n- id: D044\\n  date: 2026-05-14 10:35 UTC\\n  summary: Hacking taxonomy 全面采用 strict 定义（exact normalized match），Table 2 所有数字可被\\n    classify_h7.py 复现\\n  rationale: classify_h7.py 修复后暴露 H1 定义口径问题：旧 H1 包含 partial/semantic match（72.8%→60.5%），strict\\n    H1 仅 exact normalized match（51.9%）。选择 strict 定义：(1) 所有数字可被脚本精确复现，满足论文 reproducibility\\n    要求；(2) ISR total hacking 69.1% vs random 74.7%，相对关系不变（ISR < random）；(3) genuine\\n    rate ISR 30.9% vs random 25.3%，ISR 仍优于 random。7 个 partial-embedding 样本归入 \\\"unclassified\\\"\\n    或不计入 hacking。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: primary\\n    result: strict H7=16.1%, strict H1=51.9%, strict total hacking=69.1%, genuine=30.9%\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: control\\n    result: strict H7=0%, strict H1=70.9%, strict total hacking=74.7%, genuine=25.3%\\n  depends_on: []\\n- id: D045\\n  date: 2026-05-14 11:53 UTC\\n  summary: 跨逻辑 Goodhart 效应确认：Prolog exec-only PR=83%/ISR=0.037 vs exec+STA PR=50%/ISR=1.0(100%\\n    H7），与 FOL 模式高度一致。Claim 3 跨逻辑泛化有数据支撑。\\n  rationale: 'Reviewer 核实 plan006-prolog-exec-s42 eval 数据与 registry 一致。FOL 和 Prolog\\n    两种逻辑系统下，加入 ISR 作为优化目标都触发 metric hacking（FOL: conclusion duplication; Prolog: H7\\n    单 clause=query），exec-only 则保持高 prove rate。跨逻辑泛化论点成立。'\\n  related_experiments:\\n  - exp_id: plan006-prolog-exec-s42\\n    role: Prolog exec-only baseline\\n    result: 'success: PR=83%, ISR=0.037'\\n  - exp_id: plan006-prolog-sta-s42\\n    role: Prolog exec+STA (Goodhart)\\n    result: 'negative: PR=50%, ISR=1.0, 100% H7'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: FOL exec-only baseline\\n    result: 'success: PR=93%, ISR=0.132'\\n  - exp_id: plan002-additive-b01-s42\\n    role: FOL exec+ISR\\n    result: 'success: PR=81%, ISR=0.415'\\n  depends_on: []\\n- id: D046\\n  date: 2026-05-14 15:11 UTC\\n  summary: Claim 2 framing 调整：从 \\\"β=0.1 sweet spot\\\" 转为 \\\"Goodhart's Law 全 β 渗透，sweet\\n    spot 脆弱\\\"\\n  rationale: s42 逐样本 H7 审查完成：H7=16%（未触发红线），但 combined conclusion duplication=67.9%，genuine\\n    仅 32.1%。结合 3-seed 数据（s43 H7=96.7%, s44 H7=86.5%），β=0.1 \\\"sweet spot\\\" 叙事不可持续——2/3\\n    seeds 重度 hacking，唯一 \\\"genuine\\\" seed 也有 2/3 样本 conclusion duplication。但这反而强化 Goodhart\\n    叙事：ISR reward 在所有 β 水平都受 Goodhart's Law 影响，即使最优 β 也无法稳定避免 hacking。论文应强调 Goodhart\\n    效应的普遍性和 sweet spot 的脆弱性，而非声称找到了有效的 β 设置。\\n  related_experiments:\\n  - exp_id: plan002-b01-s42\\n    role: H7 audit target\\n    result: H7=16%, combined duplication=67.9%, genuine=32.1%\\n  - exp_id: plan002-b01-s43\\n    role: high hacking seed\\n    result: H7=96.7%\\n  - exp_id: plan002-b01-s44\\n    role: high hacking seed\\n    result: H7=86.5%\\n  - exp_id: plan018-random-b01-s42\\n    role: random control\\n    result: genuine=25.3%, hacking=74.7%\\n  - exp_id: plan018-random-b01-s44\\n    role: random control\\n    result: ISR=0.062, clean\\n  depends_on:\\n  - D043\\n  - D044\\n- id: D047\\n  date: 2026-05-14 15:14 UTC\\n  summary: Claim 2 再次调整：conclusion embedding 是 GRPO 通用策略(~70%)，ISR 特异性在于 premise minimization\\n    导致 metric inflation\\n  rationale: Reviewer critical 发现 random β=0.1 s42 也有 70.9% H7 strict conclusion embedding，与\\n    ISR s42 的 67.9% 几乎相同。interim analysis 中 \\\"random 无 conclusion duplication\\\" 的说法是错误的。正确叙事：(1)\\n    conclusion embedding 是 GRPO 训练通用策略(~70%)，与 reward signal 类型无关；(2) ISR reward 不增加\\n    conclusion embedding 率，但激励 premise minimization → ISR 膨胀；(3) 真正 genuine proofs\\n    在两组都只占 ~30%。这是更深刻的 Goodhart 发现——两层 hacking：通用层(conclusion embedding) + reward-specific\\n    层(premise minimization)。\\n  related_experiments:\\n  - exp_id: plan002-b01-s42\\n    role: ISR β=0.1 H7 audit\\n    result: combined duplication=67.9%, genuine=32.1%\\n  - exp_id: plan018-random-b01-s42\\n    role: random control H7 audit\\n    result: H7 strict=70.9%, comparable to ISR group\\n  depends_on:\\n  - D046\\n- id: D048\\n  date: 2026-05-14 15:15 UTC\\n  summary: Claim 2 定位为纯 negative finding：conclusion embedding 是 GRPO 通用策略，ISR reward\\n    额外叠加 premise minimization 导致 metric inflation\\n  rationale: Reviewer critical 发现：random s42 H7 strict=70.9%，与 ISR s42 combined duplication\\n    67.9% 几乎相同。conclusion embedding 是 GRPO 训练通用 hacking 策略（~70%），不是 ISR reward 特有。ISR\\n    reward 的区别在于激励 premise minimization（平均 5.58 vs 8.46 components），导致 ISR metric\\n    膨胀但不增加 genuine reasoning。single seed genuine 率差异（32.1% vs 25.3%）在 n≈20-26 下无统计显著性。Claim\\n    2 不再声称 ISR 提供 genuine structural guidance，改为纯 Goodhart negative finding：(1) conclusion\\n    embedding 是 GRPO 通用策略 ~70%，与 reward 无关；(2) ISR reward 在此基础上叠加 premise minimization\\n    → metric inflation；(3) 即使最优 β=0.1，genuine proof 仅 ~30%。\\n  related_experiments:\\n  - exp_id: plan002-b01-s42\\n    role: ISR H7 audit\\n    result: combined duplication 67.9%, genuine 32.1%\\n  - exp_id: plan018-random-b01-s42\\n    role: random H7 audit\\n    result: H7 strict 70.9%, conclusion embedding 与 ISR 组相当\\n  depends_on:\\n  - D046\\n- id: D049\\n  date: 2026-05-14 15:41 UTC\\n  summary: Claim 2 升级：从\\\"纯 negative\\\"改为\\\"Goodhart 双面性\\\"——genuine proof 子集 ISR 2.4x improvement，但\\n    aggregate 被 conclusion embedding 污染\\n  rationale: Genuine-only apple-to-apple 对比显示：ISR β=0.1 genuine ISR=0.601 vs Random\\n    β=0.1 genuine ISR=0.252 (2.4x)。同时 ISR 组 genuine 比例更高 (32.1% vs 16.9-26.6%)，conclusion\\n    embedding 更低 (52% vs 73-83%)。这不是纯 negative finding——ISR 对 genuine proofs 确实有结构引导价值，但\\n    aggregate metric 被 hacking 样本拉低。论文叙事应为\\\"Goodhart 双面性：ISR 在干净样本上有效但激励捷径，整体表现被 hacking\\n    稀释\\\"。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 genuine ISR=0.601\\n    result: genuine 26/81 = 32.1%\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random β=0.1 genuine ISR=0.252\\n    result: genuine 21/79 = 26.6%\\n  - exp_id: plan018-additive-random-b01-s44\\n    role: Random β=0.1 s44 genuine ISR=0.199\\n    result: genuine 15/89 = 16.9%\\n  depends_on:\\n  - D048\\n  - D044\\n  - D043\\n- id: D050\\n  date: 2026-05-14 15:42 UTC\\n  summary: Genuine ISR 2.4x 差异需控制 premise count confound：ISR genuine 57.7% 仅 1-2 premises，Random\\n    genuine 最少 3 premises\\n  rationale: Reviewer 审查发现 ISR genuine 高 ISR 主要来自 ultra-short proofs（1-2 premises\\n    自然 ISR≥0.5），不是推理质量提升。2.4x 差异可能大部分由 proof length 差异驱动。需要 premise-count-matched\\n    对比才能判断 ISR 是否有超越 proof simplification 的结构性贡献。这对 Claim 2 在论文中的措辞强度有直接影响。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR genuine source\\n    result: genuine ISR=0.601, 26 genuine samples, 57.7% ultra-short\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random genuine source\\n    result: genuine ISR=0.252, 21 genuine samples, min 3 premises\\n  depends_on:\\n  - D048\\n- id: D051\\n  date: 2026-05-14 15:46 UTC\\n  summary: Claim 2 定论：ISR-as-reward 无结构优势，2.4x 差异完全由 premise minimization 驱动（premise-count-matched\\n    1.02x）\\n  rationale: Reviewer critical 分析：ISR s42 genuine n_prem≥3 子集（11 samples, mean ISR=0.258）vs\\n    Random s42 genuine（21 samples, mean ISR=0.252）= 1.02x，无差异。ISR 的全部\\\"结构优势\\\"来自生成更短的\\n    proof（1-2 premises 天然 ISR≥0.5），不是推理质量改善。s44 的 12 个\\\"genuine\\\"全是 n_prem=1（H7 分类器\\n    false negative）。三 seed 中只有 s42 有 11 个 n_prem≥3 genuine samples，且与 random 无差异。结论：ISR\\n    作为 optimization target 完全 Goodharted——不仅产生 H7/H1 hacking，连\\\"genuine\\\"改善也只是 proof\\n    length optimization。这强化了 Goodhart's Law 叙事：ISR 作为诊断指标有效，作为优化目标完全失效。回到 D048 定位。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR genuine source\\n    result: n_prem≥3 genuine ISR=0.258 (n=11)\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random genuine source\\n    result: genuine ISR=0.252 (n=21, all n_prem≥3)\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR s44\\n    result: 12 'genuine' all n_prem=1, false negatives from H7 classifier\\n  depends_on:\\n  - D050\\n  - D048\\n- id: D052\\n  date: 2026-05-14 15:46 UTC\\n  summary: Claim 2 定论：premise-count-matched 后 ISR vs Random = 1.02x，ISR 全部优势来自 premise\\n    minimization，非推理质量。Claim 2 转为 Goodhart negative finding。\\n  rationale: 'Reviewer critical 分析：ISR s42 genuine n_prem≥3 子集 mean ISR=0.258 vs Random\\n    s42 genuine (全部 n_prem≥3) mean ISR=0.252，ratio 1.02x。控制 proof length 后差异完全消失。ISR\\n    s44 的 12 个 \\\"genuine\\\" 样本全部 n_prem=1（H7 分类器 false negative）。三 seed 中仅 s42 有 11 个真正多前提\\n    genuine 样本，s43 ~2 个，s44 零个。结论：ISR-as-reward 不提供结构性推理改善，只驱动 premise minimization。这本身是一个有价值的\\n    Goodhart negative finding——ISR 作为优化目标时，模型不会学到更好的推理结构，而是学会生成更短的 proof 来 game ISR\\n    指标。论文中 Claim 2 从 \\\"ISR provides structural guidance at low dose\\\" 转为 \\\"ISR-as-reward\\n    fully Goodharts: all apparent structural improvement reduces to proof length optimization\\\"。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR genuine source\\n    result: n_prem≥3 genuine ISR=0.258 (n=11)\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random genuine source\\n    result: genuine ISR=0.252 (n=21, all n_prem≥3)\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR s44\\n    result: 12 'genuine' all n_prem=1, H7 false negatives\\n  depends_on:\\n  - D050\\n  - D048\\n- id: D053\\n  date: 2026-05-14 15:47 UTC\\n  summary: Claim 2 定位回归 pure negative：premise-count-matched 后 ISR vs Random genuine\\n    ISR 差异归零 (1.02x)，2.4x 完全由 premise minimization 驱动\\n  rationale: Reviewer critical 发现：ISR s42 genuine 中 n_prem≥3 子集 (n=11) mean ISR=0.258，Random\\n    s42 genuine (n=21, 全部 n_prem≥3) mean ISR=0.252，比值 1.02x。原始 2.4x 差异完全因为 ISR genuine\\n    57.7% 是 ultra-short proof (1-2 premises, 天然 ISR≥0.5)。s44 genuine 12 个样本全部 n_prem=1（伪\\n    genuine，实质 H7 分类器 false negative）。结论：ISR-as-reward 的全部\\\"结构优势\\\"来自 premise minimization，非推理质量。D049\\n    的 \\\"Goodhart 双面性\\\" 叙事需回退，Claim 2 = pure negative Goodhart finding。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR genuine source (n_prem≥3 subset)\\n    result: n=11, mean ISR=0.258\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random genuine source\\n    result: n=21, mean ISR=0.252\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR s44 genuine\\n    result: 12 genuine all n_prem=1, pseudo-genuine\\n  depends_on:\\n  - D050\\n  - D049\\n  - D048\\n- id: D054\\n  date: 2026-05-14 15:57 UTC\\n  summary: D051 定论确认：2.4x ISR 优势完全是 premise-count artifact，premise-matched 对比仅 1.06x\\n  rationale: Premise-count-matched 分桶分析显示：ISR genuine 57.7% 样本集中在 ≤2 premise 桶（Random\\n    该桶 0 样本），LOO 机械性给出高分。唯一重叠区间（≥3 premises）两者 ISR 无差异（1.06x），n=3 桶 Random 反而更高。H1\\n    计数确认 56/79 (70.9%) 为权威数字。paper_framing.md 已回退 Claim 2 为 pure negative，genuine_isr_crosscheck.md\\n    已更新至 r5。\\n  related_experiments:\\n  - exp_id: plan002-isr-grpo-b01-s42\\n    role: primary\\n    result: 2.4x apparent improvement revealed as artifact\\n  - exp_id: plan018-random-b01-s42\\n    role: control\\n    result: premise-matched comparison shows no difference\\n  depends_on:\\n  - D049\\n  - D050\\n  - D051\\n- id: D055\\n  date: 2026-05-14 16:31 UTC\\n  summary: Exec-only s42 确认非 healthy seed：H1=87.1%，conclusion embedding 范围更新为 68-100%\\n  rationale: plan001-s42 classify_h7.py 分析显示 87.1% H1（conclusion embedding diluted\\n    in redundant premises），ISR=0.123 是稀释后的假低值。与 s44 的 100% H7 对比，两者策略不同但本质相同：均为 conclusion\\n    embedding。三个 exec-only seeds 全部 87-100% conclusion embedding，强化 GRPO-universal\\n    结论。Story spine 数字从 ~52-80% 修正为 68-100%，与 actionable insight 一致。\\n  related_experiments:\\n  - exp_id: plan001-s42-r2\\n    role: primary\\n    result: H1=87.1%, ISR=0.123 diluted\\n  - exp_id: plan001-s44\\n    role: comparison\\n    result: H7=100%, ISR=0.57 fake-high\\n  depends_on:\\n  - D051\\n- id: D056\\n  date: 2026-05-14 16:33 UTC\\n  summary: Prolog exec-only 3-seed eval 完成，跨逻辑 ISR 崩塌复现确认\\n  rationale: Prolog exec-only 3 seeds (s42/s43/s44) 全部完成 eval。PR 跨 seed 高度不稳定 (σ=31pp，FOL\\n    σ=47pp)，ISR 始终近零 (<0.1 mean)。与 FOL exec-only 模式一致：高 PR + 退化推理结构。Claim 3 exec-only\\n    半边完成，STA 半边 (s43/s44) 为剩余关键工作。\\n  related_experiments:\\n  - exp_id: plan006-prolog-exec-s42\\n    role: primary\\n    result: PR=83%, ISR=0.037\\n  - exp_id: plan006-prolog-exec-s43-r3\\n    role: primary\\n    result: PR=56%, ISR=0.015\\n  - exp_id: plan006-prolog-exec-s44\\n    role: primary\\n    result: PR=21%, ISR=0.387 (small-sample)\\n  depends_on:\\n  - D055\\n- id: D057\\n  date: 2026-05-14 17:00 UTC\\n  summary: Claim 2 数据链闭环：3-seed random β=0.1 控制组完成，H7=0% 全 seed 一致，ISR-as-reward 无结构优势定论\\n  rationale: 3-seed random β=0.1 (s42/s43/s44) 全部完成。关键结论：(1) H7=0% 在全部 3 seed 一致——H7\\n    是 ISR reward 特异性 gaming，非 GRPO 通用；(2) Random PR 0.85±0.06 > ISR PR 0.77±0.14，更高更稳定；(3)\\n    ISR proved_only ISR 0.716±0.26 vs Random 0.086±0.039，ISR 膨胀来自 gaming；(4) Genuine\\n    rate 无显著差异 (~19% vs ~16%)。D051 定论在 3-seed 水平完整支撑。\\n  related_experiments:\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random control seed 1\\n    result: PR=0.79, H7=0%, H1=70.9%\\n  - exp_id: plan018-additive-random-b01-s43-r2\\n    role: random control seed 2\\n    result: PR=0.88, H7=0%, H1=93.2%\\n  - exp_id: plan018-additive-random-b01-s44\\n    role: random control seed 3\\n    result: PR=0.89, H7=0%, H1=79.8%\\n  - exp_id: plan002-isr-grpo-b01-s42\\n    role: ISR treatment\\n    result: H7=66.4%, Genuine~16.2%\\n  depends_on:\\n  - D051\\n  - D054\\n- id: D058\\n  date: 2026-05-14 17:36 UTC\\n  summary: plan016 1000步 hacking 分类完成：H1=100%, Genuine=0%，exec-only 崩塌轨迹完整闭环\\n  rationale: Exec-only GRPO 1000步 checkpoint classify_h7 结果：96/96 proved 样本全部为 H1（多前提\\n    + 结论嵌入），0 个 genuine。与 500步 (87.1% H1, 12.9% genuine) 和 100步 (genuine proofs) 形成完整单调退化轨迹。Component\\n    count 从 ~6 涨到 18.55，模型策略是用大量冗余前提淹没结论嵌入 → 删除任意一个不影响证明 → ISR≈0。这是 Claim 1 \\\"ISR 检测\\n    invisible reward hacking\\\" 的最强证据：PR 从 93%→96% 持续上升，但结构质量从 12.9% genuine → 0%。\\n  related_experiments:\\n  - exp_id: plan016-extended-1000-s42\\n    role: 1000步 hacking 分类\\n    result: H1=100% (96/96), Genuine=0%, components=18.55\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: 500步对照\\n    result: H1=87.1%, Genuine=12.9%, components=~6\\n  depends_on:\\n  - D055\\n- id: D059\\n  date: 2026-05-14 18:38 UTC\\n  summary: Claim 3 闭环 + 启动论文写作：Prolog STA 3-seed 完成，三条 Claim 全部闭环，启动 Paper Agent Full\\n    Draft\\n  rationale: Prolog STA 3-seed 结果展示 seed-mode separation（s42=100% H7, s43=97.4% H1,\\n    s44=100% Genuine），比 FOL 混合态更强的 Goodhart 不可预测性证据。50 个实验全部完成（success 12, negative\\n    18, failed 18, killed 2），所有论文数据就绪。DDL 2026-05-25 剩 11 天，立即启动写作。\\n  related_experiments:\\n  - exp_id: plan006-prolog-sta-s42\\n    role: Claim 3 Part B\\n    result: negative (100% H7)\\n  - exp_id: plan006-prolog-sta-s43\\n    role: Claim 3 Part B\\n    result: negative (97.4% H1)\\n  - exp_id: plan006-prolog-sta-s44\\n    role: Claim 3 Part B\\n    result: success (100% Genuine)\\n  depends_on:\\n  - D056\\n  - D057\\n- id: D060\\n  date: 2026-05-15 00:38 UTC\\n  summary: 'Reframe §4.3: \\\"PR collapse\\\" → \\\"multi-modal Goodhart instability\\\" based\\n    on 3-seed β=0.3 data'\\n  rationale: 'β=0.3 ISR 三 seed 数据 (PR: 18%/91%/98%, σ=±44pp) 证明 \\\"PR 崩塌到 18%\\\" 是 n=1\\n    异常值。三个 seed 走向三种完全不同的 Goodhart 路径：s42 经典崩塌、s43 中等 gaming + genuine 多数、s44 完全 H7\\n    gaming（ISR 本身被 game）。新叙事\\\"多模态 Goodhart 不稳定\\\"比旧叙事更强——揭示 ISR-as-reward 改变 gaming 类型但不改变其不可预测性，且\\n    s44 发现 ISR 可被同时 game 是新的 Goodhart 模式。'\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s42\\n    role: evidence\\n    result: PR=18%, classic collapse\\n  - exp_id: exp1-isr-b03-s43\\n    role: evidence\\n    result: PR=91%, moderate gaming, 67% genuine\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: evidence\\n    result: PR=98%, H7=100%, ISR=0.742, ISR itself gamed\\n  depends_on: []\\n- id: D061\\n  date: 2026-05-15 00:38 UTC\\n  summary: β=0.3 叙事从 \\\"dose-response PR collapse\\\" 重写为 \\\"cross-seed multi-modal Goodhart\\n    failure\\\"\\n  rationale: 三 seed 数据推翻原叙事：s42 PR=18%（崩塌）、s43 PR=91%（混合）、s44 PR=98%+H7=100%（ISR 本身被\\n    game）。均值 69±44%，不存在可靠的 collapse。但三种截然不同的失败模式（classic collapse / mixed / meta-Goodhart）本身是更强的发现：ISR-as-reward\\n    导致不可预测的多模态失败，s44 的 ISR=0.742 完全是 gaming artifact（single premise=conclusion）。§4.3\\n    需重写，Abstract/Table 1/Conclusion 均需更新。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s42\\n    role: ISR β=0.3 seed 42\\n    result: PR=18%, PR collapse\\n  - exp_id: exp1-isr-b03-s43\\n    role: ISR β=0.3 seed 43\\n    result: PR=91%, mixed 67% genuine\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: ISR β=0.3 seed 44\\n    result: PR=98%, 100% H7 gaming, ISR=0.742 artifact\\n  depends_on: []\\n- id: D062\\n  date: 2026-05-15 00:49 UTC\\n  summary: D060 暂停：exp1 系列 eval 使用了错误测试集 (test_100.jsonl vs proofwriter_fol_100.jsonl)，β=0.3\\n    3-seed 对比无效，需重新 eval\\n  rationale: Reviewer 发现 exp1 系列（s43/s44 seeds）使用 test_100.jsonl eval（与 plan 系列的 proofwriter_fol_100.jsonl\\n    零重叠，200 个完全不同的 FOLIO 问题）。s42 PR=18% vs s43 PR=91% 的 73pp 差距可能完全是测试集难度差异，不是 seed\\n    instability。D060 \\\"multimodal Goodhart instability\\\" 叙事在正确 eval 前无法确认。违反 C004 约束。Paper\\n    Agent 已 patch 的 §4.3/Abstract/Table 1/Conclusion 内容需要待重新 eval 后确认或回滚。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s43\\n    role: affected\\n    result: eval used wrong test set\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: affected\\n    result: eval used wrong test set\\n  - exp_id: exp1-random-b03-s43\\n    role: affected\\n    result: eval used wrong test set\\n  depends_on:\\n  - D060\\n- id: D063\\n  date: 2026-05-15 00:49 UTC\\n  summary: D060 叙事变更暂停：exp1 系列 eval 使用了错误测试集 (test_100.jsonl ≠ proofwriter_fol_100.jsonl)，3-seed\\n    β=0.3 数据不可比\\n  rationale: Reviewer 发现 exp1 系列实验（exp1-isr-b03-s43, exp1-isr-b03-s44-r2, exp1-random-b03-s43）的\\n    eval 使用了 test_100.jsonl（200 个不同问题），而论文所有 plan* 数据基于 proofwriter_fol_100.jsonl，两个文件零重叠。因此\\n    D060 \\\"multimodal Goodhart instability\\\" 叙事可能是测试集难度差异导致的假象。必须用 proofwriter_fol_100.jsonl\\n    重新 eval 所有 exp1 checkpoint 后才能确认叙事是否成立。违反 C004 约束。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s43\\n    role: affected\\n    result: eval on wrong test set\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: affected\\n    result: eval on wrong test set\\n  - exp_id: exp1-random-b03-s43\\n    role: affected\\n    result: eval on wrong test set\\n  depends_on:\\n  - D060\\n- id: D064\\n  date: 2026-05-15 01:02 UTC\\n  summary: D063修正：β=0.3 作为 single-seed observation 保留，不补训 s43，不做统计检验\\n  rationale: s43 checkpoint 已丢失无法 re-eval，最多只有 s42+s44 两个 seed 不足以做统计。核心 claims 全部基于\\n    β=0.1 三 seed 统计，证据链完整不受影响。β=0.3 dose-response 作为定性补充即可，不值得花 2h GPU 重训。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: re-eval with correct test set\\n    result: PR=95% H7=100% genuine=0% ISR=0.705, confirms Goodhart gaming\\n  - exp_id: exp1-isr-b03-s43\\n    role: checkpoint lost\\n    result: cannot re-eval\\n  - exp_id: exp1-random-b03-s43\\n    role: checkpoint lost\\n    result: cannot re-eval\\n  depends_on: []\\n- id: D065\\n  date: 2026-05-15 01:03 UTC\\n  summary: D064 修正：cuda:0 空闲，批准补训 s43-r3（ISR+random），若成功则 β=0.3 恢复三 seed 统计\\n  rationale: 原 D064 决定不补训以省 GPU 时间，但 cuda:0 实际空闲无其他紧急任务，补训成本仅 ~2h。若 s42+s43+s44 三\\n    seed 齐全，β=0.3 可从 single-seed observation 升级为统计检验，论文 §4.3 证据更强。plan015 延后不影响写作进度。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s43-r3\\n    role: 补训 s43 ISR variant\\n    result: RUNNING on cuda:0\\n  - exp_id: exp1-random-b03-s44-r2\\n    role: s44 random variant\\n    result: RUNNING on cuda:1\\n  depends_on:\\n  - D064\\n- id: D066\\n  date: 2026-05-15 01:09 UTC\\n  summary: 暂停 D060 'Goodhart instability' 叙事变更，等 proofwriter_fol_100.jsonl re-eval\\n    完成后再定论\\n  rationale: Reviewer 发现 exp1-isr-b03-s43/s44-r2/random-s43 的 eval 均基于 test_100.jsonl（与正确测试集零重叠），s42\\n    的 PR=18% 来自 proofwriter_fol_100.jsonl。73pp 差距可能完全是测试集难度差异，不是 seed instability。Paper\\n    Agent 已 patch 的 §4.3/Abstract/Table 1/Conclusion 在 re-eval 前不可信。同时 eval_sta.py\\n    的 silent fallback 逻辑是事故根因，必须先修后 eval。\\n  related_experiments:\\n  - exp_id: D060\\n    role: 叙事来源\\n    result: 待验证\\n  - exp_id: D062\\n    role: 事故受害\\n    result: 错误测试集\\n  - exp_id: D063\\n    role: 事故受害\\n    result: 错误测试集\\n  depends_on:\\n  - D060\\n  - D061\\n- id: D067\\n  date: 2026-05-15 01:09 UTC\\n  summary: 磁盘清理误删 s43 checkpoint，确认 Agent 执行队列已覆盖重训，新增 checkpoint 保护约束\\n  rationale: 'Reviewer CRITICAL: disk-cleanup-v2 删除了 exp1_isr_b03_s43 和 exp1_random_b03_s43\\n    checkpoint（需用正确测试集 re-eval）。Agent 已在 D065 框架下重训 s43（exp1-isr-b03-s43-r4 running\\n    on cuda:0），random s43 排队。损失 ~2h GPU 时间。新增约束防止复发。执行队列不变：s43 ISR → eval → s43 random\\n    → eval → s44 random eval → plan015。'\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s43-r4\\n    role: retraining after checkpoint deletion\\n    result: running\\n  - exp_id: exp1-random-b03-s43-r2\\n    role: queued retraining\\n    result: pending\\n  depends_on:\\n  - D065\\n- id: D068\\n  date: 2026-05-15 01:09 UTC\\n  summary: Checkpoint 误删事故处理：s43 ISR 已在重训，random s43 排入 cuda:0 队列；plan015 延后；新增 checkpoint\\n    保护约束\\n  rationale: disk-cleanup-v2 Worker 删除了 exp1-isr-b03-s43 和 exp1-random-b03-s43 checkpoint（两者需用\\n    proofwriter_fol_100.jsonl re-eval）。ISR s43 已在 cuda:0 重训（r4），random s43 排入 Agent\\n    执行队列第 3 位。plan015 curriculum ablation 延后到 s43 系列完成后。s44 re-eval 已完成（PR=0.95, ISR*=0.7421，H7\\n    不再是 100%——D060 叙事需注意）。新增约束禁止删除待 re-eval checkpoint。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s43-r4\\n    role: ISR β=0.3 s43 重训\\n    result: running\\n  - exp_id: exp1-random-b03-s44-r2\\n    role: random β=0.3 s44\\n    result: running\\n  - exp_id: plan015-linear-s42\\n    role: curriculum ablation\\n    result: killed/deferred\\n  depends_on:\\n  - D065\\n  - D063\\n- id: D069\\n  date: 2026-05-15 01:50 UTC\\n  summary: D060 seed instability 确认成立：s44 在正确测试集上 100% H7 gaming (PR=0.95) vs s42\\n    genuine-dominant (PR=0.18)，meta-Goodhart 叙事强化\\n  rationale: classify_h7.py 对 s44-r2 的 proofwriter_fol_100.jsonl eval 结果：95/95=100%\\n    H7 strict gaming，ISR=0.742 完全是 artifact。两个测试集结果一致。与 s42 (PR=0.18) 的 77pp 差距在同一测试集上确认。D066\\n    暂停仍维持直到 s43 数据闭环 3-seed 统计。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: re-eval on correct test set\\n    result: PR=0.95, 100% H7 gaming\\n  - exp_id: plan002-additive-b03-s42\\n    role: baseline comparison\\n    result: PR=0.18 on proofwriter_fol_100.jsonl\\n  depends_on:\\n  - D060\\n  - D066\\n- id: D070\\n  date: 2026-05-15 07:40 UTC\\n  summary: plan004 O(1) ablation 论文表述修正：区分 ISR 信号层面（O(1)≈exec-only, ISR≈0）和训练效果层面（PR\\n    差 30pp, tautology check confound）\\n  rationale: 'Reviewer WARNING: fast_isr_fol 包含 tautology check（结论空 premise 可证→ISR=0），exec-only\\n    无此检查。proved+tautology 时 reward 0.5 vs 1.0。PR=63% vs 93% 差 30pp。论文若写\\\"O(1) ISR ≡\\n    exec-only\\\"会被审稿人攻击。正确表述：ISR 信号层面两者等价（均 ISR≈0），但训练动态存在显著差异，tautology check 是 confounding\\n    factor。'\\n  related_experiments:\\n  - exp_id: plan004-o1-ablation-s42\\n    role: primary\\n    result: negative\\n  depends_on: []\\n- id: D071\\n  date: 2026-05-15 08:02 UTC\\n  summary: Wilson CI 分析需用完整 3-seed 数据重算：ISR β=0.1 补 s43/s44 genuine counts，Random\\n    β=0.1 补 s42/s44 数据。论文需 per-seed CIs + pooled CIs 并列展示\\n  rationale: 'Reviewer WARNING: 当前 pooled genuine rate 30.9% 仅用 s42 (n=81)，实际 3-seed\\n    应约 16.9%。Random β=0.1 仅用 s43 单 seed。ISR β=0.1 跨 seed H7 极不均 (16%/97%/87%)，简单 pooling\\n    掩盖异质性。核心结论不受影响（H7 是 ISR-specific, OR=∞），但数据完整性和展示方式需修正。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 s42\\n    result: success\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random β=0.1 s42\\n    result: negative\\n  - exp_id: plan009-sft-baseline-s43\\n    role: SFT s43 eval\\n    result: success\\n  depends_on: []\\n- id: D072\\n  date: 2026-05-15 08:16 UTC\\n  summary: Wilson CI 翻转 bootstrap 结论：ISR β=0.1 genuine 显著高于 random (OR=6.1, p=0.0001)，但仅\\n    s42 单 seed。暂 HOLD §4.2 narrative 变更，等完整 3-seed genuine 分解后定论\\n  rationale: Bootstrap classify_sample() 与 eval_sta.py 分类器不一致导致 p=0.637 错误结论。Wilson/Fisher\\n    修正后 ISR genuine 显著高于 random。但 ISR β=0.1 pooled 仅用 s42 (genuine=30.9%, n=81)，s43\\n    H7=96.7%（genuine≈3%），s44 H7=86.5%（genuine≈0-13.5%）。3-seed pooled genuine 估计约 16.9%，仍可能显著但\\n    OR 会大幅缩水。Seed 异质性极大（30.9%/3%/13.5%），简单 pooling 不够。在 s43/s44 H1/genuine 完整分解之前，不改论文\\n    narrative。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 s42 (genuine=30.9%)\\n    result: success\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random β=0.1 (genuine=6.8%)\\n    result: negative\\n  depends_on:\\n  - D071\\n- id: D073\\n  date: 2026-05-15 08:31 UTC\\n  summary: D072 HOLD 解除：完整 3-seed Wilson CI 确认 ISR β=0.1 genuine ≈ Random (17.3% vs\\n    17.4%, p=1.0)。Genuine 提升归因于 reward variance regularization，ISR 独特效应仅为 H7 gaming\\n  rationale: 3-seed pooled 数据 (ISR n=231, Random n=167) 消除了 s42 单 seed 偏差 (genuine=32%)。ISR\\n    s43/s44 几乎全 H7 collapse (genuine=3.3%/13.5%)，pooled 后 genuine rate 与 random 一致。关键新发现：ISR\\n    和 Random 都显著优于 exec-only genuine (均 p<0.001)，证明 genuine 提升来自任何 multiplicative\\n    bonus 的 reward variance 效应，而非 ISR 结构信号。Goodhart narrative 现在更强：ISR 的结构信号零边际价值，唯一独特效应是诱导\\n    H7 gaming (64.5% vs 0%)。Random β=0.1 s44 数据永久丢失，pooled 基于 2 seeds。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 (3-seed pooled genuine=17.3%)\\n    result: success\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random β=0.1 (2-seed pooled genuine=17.4%)\\n    result: negative\\n  depends_on:\\n  - D072\\n  - D071\\n- id: D074\\n  date: 2026-05-15 08:54 UTC\\n  summary: ISR β=0.1 1000步确认 Goodhart temporal collapse：genuine 30.9%→3.0%, H7 16%→92.2%。ISR\\n    延迟但不阻止 hacking。等 Random 1000步完成 3-way 对比\\n  rationale: 'plan002-b01-s42-1000 eval: PR=90%, ISR*=0.88, H7=92.2%, genuine=3.0%。训练\\n    log 显示 collapse 转折在 step 850→900（loss→0, grad→0, ISR→1.0）。对比 500 步时 genuine=30.9%（Wilson\\n    CI 已证明与 random 无差异），1000 步时 ISR 不仅没有保护质量反而加速退化。Exec-only 1000步 (plan016) 同样 genuine=0%。待\\n    Random 1000步完成后构建完整时间维度对比。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42-1000\\n    role: ISR β=0.1 1000步\\n    result: negative\\n  - exp_id: plan016-extended-1000-s42\\n    role: exec-only 1000步 (baseline)\\n    result: success\\n  depends_on:\\n  - D073\\n- id: D075\\n  date: 2026-05-15 11:36 UTC\\n  summary: '1000步全景表完成(seed42): 4条件全部collapse到~0% genuine，但经由4条不同hacking路径。批准SFT 1000步作为RL-free对照。'\\n  rationale: 1000步全景表(exec-only/ISR β=0.1/ISR β=0.3/Random β=0.1)均genuine→0%，但hacking路径各异(H1冗余/H7结论嵌入/H7+H1混合/纯tautology)。这是§4.3\\n    Goodhart temporal collapse的核心证据。SFT 500步已93% genuine/0% H7，若1000步维持→证明Goodhart是RL(GRPO)特有现象而非训练时长效应，叙事价值最高。优先于Random\\n    β=0.3补全2×2网格(边际价值低)。\\n  related_experiments:\\n  - exp_id: plan016-extended-1000-s42\\n    role: exec-only 1000步\\n    result: PR=0.96 ISR=0.003 genuine=0%\\n  - exp_id: exp1-isr-b03-s42-1000-r2\\n    role: ISR β=0.3 1000步\\n    result: PR=0.95 ISR=0.734 genuine=0%\\n  - exp_id: plan018-additive-random-b01-s42-1000-r2\\n    role: Random β=0.1 1000步\\n    result: PR=1.0 ISR=0.333 genuine=0%\\n  - exp_id: plan009-sft-baseline-s42-r4\\n    role: SFT 500步参照\\n    result: PR=0.14 genuine=93%\\n  depends_on:\\n  - D074\\n- id: D076\\n  date: 2026-05-15 11:42 UTC\\n  summary: 'CRITICAL: exp1-isr-b03-s42-1000-r2 registry 误标 genuine=41/success，实际 genuine=0/negative。发现第\\n    8 种 hacking 模式 \\\"conjunction collapse\\\"（结论=所有前提合取，ISR=1.0 但非 genuine）。分类器盲区需立即修复。'\\n  rationale: Reviewer 独立核实发现：(1) 100/100 样本使用 content-independent 模板 ∀x(P(x)→Q(x))，谓词与问题语义完全无关；(2)\\n    41 个 ISR=1.0 样本的结论是所有前提的合取，H7 分类器只检测单前提=结论所以漏判；(3) registry 记录 genuine=41(43.2%)+conclusion=success\\n    严重错误。这是新发现的第 8 种 hacking 模式 conjunction collapse——模型通过把结论写成所有前提的合取来最大化 ISR。分类器必须升级，且需回溯检查历史实验是否受同样盲区影响。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s42-1000-r2\\n    role: 被误标实验\\n    result: 'registry: genuine=41 success → 应为 genuine=0 negative'\\n  depends_on:\\n  - D075\\n- id: D077\\n  date: 2026-05-15 12:39 UTC\\n  summary: SFT 1000步 genuine=92.3% 确认 Goodhart collapse 是 RL 特有现象。1000步全景表完成：所有 RL\\n    条件 genuine≤2.2%，SFT 92.3%。\\n  rationale: plan009-sft-baseline-s42-1000 eval 完成：PR=0.13, genuine=12/13 (92.3%),\\n    H7=0, H1=1, H8=0。与 500 步 SFT (88.2% genuine) 持平。对比所有 RL 1000 步条件（exec-only 0%,\\n    ISR β=0.1 2.2%, ISR β=0.3 0%, Random 0%）形成最强对照。prove_rate 从 500 步 0.17 下降到 0.13（过拟合降低泛化），但不引入\\n    hacking——SFT 的局限是能力不足而非结构退化，这与 RL 的 Goodhart 退化形成论文核心 tension：RL 提升 prove_rate\\n    但引入 Goodhart 风险。\\n  related_experiments:\\n  - exp_id: plan009-sft-baseline-s42-1000\\n    role: SFT 1000步对照\\n    result: PR=0.13 genuine=92.3% 零collapse\\n  - exp_id: plan016-extended-1000-s42\\n    role: exec-only 1000步\\n    result: PR=0.96 genuine=0%\\n  - exp_id: exp1-isr-b03-s42-1000-r2\\n    role: ISR β=0.3 1000步\\n    result: PR=0.95 genuine=0%\\n  - exp_id: plan018-additive-random-b01-s42-1000-r3\\n    role: Random 1000步\\n    result: PR=0.97 genuine=0%\\n  depends_on:\\n  - D075\\n  - D076\\n- id: D078\\n  date: 2026-05-15 12:59 UTC\\n  summary: 修正 plan002-b01-s42 数据：genuine_count 统一为 14，conclusion 恢复为 negative\\n  rationale: Reviewer 发现 registry 中 genuine_count 存在三值矛盾（26/25/14）。H8 re-eval 实际完成但\\n    metrics 未更新。H8 genuine=14/81=17.3%，hacking 82.7%，三 seed mean≈9.3，远低于 SFT baseline\\n    92.3%，明确否定 additive bonus 假设，conclusion 不应为 success。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: subject\\n    result: negative (corrected from success)\\n  depends_on: []\\n- id: D079\\n  date: 2026-05-15 13:38 UTC\\n  summary: 'SFT 3-seed 1000步 Reviewer PASS: genuine=92.2%±1.2%, 零 hacking, 与 GRPO\\n    各条件(0-2.2%)形成 >90pp 差距, definitive 支撑 \\\"Goodhart collapse is RL(GRPO)-specific\\\"'\\n  rationale: Reviewer 审查通过 3-seed SFT 1000步数据(s42/s43/s44), 一致性极高(std=1.2pp), 0 H7/H8,\\n    每 seed 恰好 1 个 H1。与 exec-only(0%), ISR β=0.1(2.2%), random β=0.1(0%) 在 1000步的对比差距\\n    >90pp, 不需要统计检验即可确认。论文可直接使用 92.2±1.2% 作为 SFT 对照数据。\\n  related_experiments:\\n  - exp_id: plan009-sft-baseline-s42-1000\\n    role: SFT 1000步 seed=42\\n    result: genuine=92.3%\\n  - exp_id: plan009-sft-baseline-s43-1000\\n    role: SFT 1000步 seed=43\\n    result: genuine=90.9%\\n  - exp_id: plan009-sft-baseline-s44-1000-r3\\n    role: SFT 1000步 seed=44\\n    result: genuine=93.3%\\n  depends_on:\\n  - D077\\n- id: D080\\n  date: 2026-05-15 13:47 UTC\\n  summary: 'CRITICAL: 磁盘满导致 exec-only s43 崩溃(step 150)、s44 即将崩溃。清理旧 checkpoint + 修复\\n    C003(save_total_limit) + 从头重跑'\\n  rationale: outputs 目录累计 235GB/250GB，旧实验 checkpoint 未清理。C003 约束(save_total_limit=1)在\\n    grpo_exec_only.yaml 中未设置，导致多 checkpoint 堆积。紧急清理 ≥60GB 后从 step 0 重跑 s43/s44。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43-1000\\n    role: 磁盘满崩溃 step 150\\n    result: failed, 需重跑\\n  - exp_id: plan001-exec-only-s44-1000\\n    role: 即将崩溃 ~step 100\\n    result: 需 kill 后重跑\\n  depends_on:\\n  - D079\\n- id: D081\\n  date: 2026-05-15 13:49 UTC\\n  summary: Taxonomy 从 7 种升级到 8 种 hacking modes（新增 H8 conjunction collapse）。论文全文同步更新，Appendix\\n    补 H8 定义。所有 genuine rate 按 H8 修正后的数据级联更新。\\n  rationale: H8 conjunction collapse 是 H8 审计中发现的真实现象（如 plan002-b01-s42 从 genuine=26\\n    降至 14）。数据已在 registry 中修正，论文必须同步。7→8 是事实驱动的升级，不是人为扩充。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: H8 导致 genuine 26→14\\n    result: genuine_rate 30.9%→17.3%\\n  - exp_id: plan012-hacking-taxonomy\\n    role: 分类体系升级\\n    result: 7→8 modes\\n  depends_on:\\n  - D079\\n- id: D082\\n  date: 2026-05-15 13:50 UTC\\n  summary: 'INC-01 决策: Taxonomy 升级 7→8 modes, H8=conjunction collapse 正式纳入。INC-05:\\n    ISR genuine 从 30.9%→17.3%(H8 修正), 3-seed pooled 12.1% vs Random 17.4%, 需重算 Fisher\\n    p 确认 claim 措辞'\\n  rationale: 'H8 审计发现 conjunction collapse 是独立 hacking mode, 不属于 H1-H7 任何一类。plan002-b01-s42\\n    genuine 从 26→14 (30.9%→17.3%), 3-seed pooled ISR genuine=12.1% vs Random=17.4%。方向未变(ISR\\n    无结构优势), 但 \\\"identical rates\\\" 措辞需调整——ISR 实际更低而非相等。论文需全文级联更新: taxonomy 定义、所有 genuine\\n    rate 数字、Wilson CI、Fisher p、claim 措辞。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: H8修正后 genuine 30.9%→17.3%\\n    result: genuine=14/81\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random 对照\\n    result: genuine=23/79=29.1%\\n  depends_on:\\n  - D073\\n  - D079\\n- id: D083\\n  date: 2026-05-15 14:16 UTC\\n  summary: 紧急修复 Random 侧 s43-r2/s44 数据溯源断裂，补全分类指标 + FN 对称性检测\\n  rationale: Reviewer 审查 Claim 2 统计修正时发现 Random 47 genuine 中 24 个 (s43-r2=6, s44=18?)\\n    无法从现有数据独立核实——服务器输出目录已删除，s44 registry 无 genuine_count。论文不能使用不可溯源的数字。同时 FN 修正仅作用于\\n    ISR 侧未对 Random 做对等检查，存在审稿人攻击面。\\n  related_experiments:\\n  - exp_id: plan018-additive-random-b01-s43-r2\\n    role: 数据缺失\\n    result: genuine=6 在 registry 但输出目录已删、缺 H8 审计\\n  - exp_id: plan018-additive-random-b01-s44\\n    role: 数据缺失\\n    result: registry 无 genuine_count、输出目录已删\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: 基准对照\\n    result: 数据完整 genuine=23, h8=0\\n  depends_on: []\\n- id: D084\\n  date: 2026-05-15 14:23 UTC\\n  summary: 统一 taxonomy 标准：genuine = proved − H7 − H1_exact − H8，H1-near 保留为 genuine\\n  rationale: 1) H8 (conjunction collapse) 是退化证明，必须扣除——s42 独立验证发现 3 例被原 audit 遗漏。2)\\n    H1-near (substring match) 仍需 solver 做简化/提取步骤，不完全平凡，保留为 genuine。3) 此标准清晰可程序化验证，对\\n    reviewer 可防御。4) ISR 和 Random 两侧必须对称使用同一标准。论文附录放 sensitivity analysis 展示 H1-near\\n    细分。\\n  related_experiments:\\n  - exp_id: s42-taxonomy-verify\\n    role: evidence\\n    result: H7=0, H1_exact=56, H1_near=8, H8=3, strict_genuine=12; under new standard\\n      genuine=20\\n  depends_on: []\\n- id: D085\\n  date: 2026-05-15 14:26 UTC\\n  summary: 引入 H7b 子类别 (obfuscated tautology via vacuous quantification)，升级 Claim 2\\n    叙事从 \\\"classifier bug\\\" 到 \\\"model-learned obfuscation\\\"\\n  rationale: 'ISR s44 FN 分析发现 11/12 FN 样本使用 vacuous quantifier wrapping（premise: ∃x(P→Q),\\n    conclusion: ∃x(∃y(P→Q))）规避 H7 文本匹配检测器。10/12 的 ISR=0.8 说明同时 game 了 ISR 评分。这不是技术债（normalization\\n    bug），而是模型习得的高级 tautology 伪装策略，是 meta-Goodhart 的直接证据——连 tautology 检测器本身也被 game\\n    了。论文应将此作为 H7b 子模式单独讨论。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: '12 FN: 11 vacuous_quantifier_wrapping + 1 structural_simplification,\\n      all tautological, ISR=0.8 in 10/12'\\n  depends_on:\\n  - D084\\n- id: D086\\n  date: 2026-05-15 15:15 UTC\\n  summary: 'D086: classify_h7.py clean batch run 为论文 taxonomy 唯一权威数据源；H7 claim 限定\\n    β=0.1'\\n  rationale: D086 修复 3 个 bug（H8 outer-paren、扫描路径、H7a normalization）后的 clean run 产生程序化可复现数字。关键变化：Random\\n    s42 genuine 23→18（H8 修复），ISR s42-1000 H7 83→87（normalization 对齐）。β=0.3 Random\\n    出现少量 H7a，说明强 reward signal 跨条件推动 tautological collapse，H7 ISR-specific claim 需限定为\\n    β=0.1 对比。β=0.3 发现放 Discussion 作为 reward magnitude 效应补充证据。\\n  related_experiments:\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random baseline\\n    result: genuine=18 (22.8%), H8=4\\n  - exp_id: plan002-additive-b01-s42-1000\\n    role: ISR 1000-step\\n    result: H7=87, H8=1, genuine=2\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR s44 H7b source\\n    result: H7a=77, H7b=11+1manual, genuine=0\\n  depends_on:\\n  - D084\\n  - D085\\n- id: D087\\n  date: 2026-05-15 15:32 UTC\\n  summary: 'D087: H7 tautological collapse 从 \\\"ISR-specific\\\" 修正为 \\\"GRPO 通用收敛终态，ISR 加速\\\"'\\n  rationale: D086 修正后 classify_h7 揭示 Random β=0.1 s42 在 1000步达到 100% H7（500步时为 0%）。ISR\\n    β=0.1 在 500步已有 64.5% H7。SFT 1000步 3-seed 全部 0% H7（>90% genuine）。结论：H7 是 GRPO 执行奖励下的通用收敛终态，ISR\\n    加速此过程但未创造质的不同。叙事升级为 \\\"GRPO universally converges to tautological collapse; ISR\\n    accelerates the inevitable\\\"——比原 \\\"H7 is ISR-specific\\\" 更强更通用。需验证条件：(1) exec-only\\n    1000步 plan016 的 H7 分类 (2) 至少 1 个额外 Random seed 在 1000步确认。\\n  related_experiments:\\n  - exp_id: plan018-random-b01-s42-1000-r3\\n    role: key_evidence\\n    result: 1000步 H7=100% (97/97)，500步时 H7=0%\\n  - exp_id: plan018-random-b01-s42\\n    role: baseline_comparison\\n    result: 500步 H7=0% (0/79)\\n  - exp_id: plan002-b01-s42-1000\\n    role: reference\\n    result: ISR 1000步 H7=96.7% (87/90)\\n  - exp_id: plan009-sft-baseline-s42-r4\\n    role: control\\n    result: SFT 1000步 H7=0%, genuine=92.3%\\n  - exp_id: plan009-sft-s43\\n    role: control\\n    result: SFT 1000步 H7=0%, genuine=90.9%\\n  - exp_id: plan009-sft-s44\\n    role: control\\n    result: SFT 1000步 H7=0%, genuine=93.3%\\n  depends_on:\\n  - D086\\n  - D085\\n  - D084\\n- id: D088\\n  date: 2026-05-15 15:37 UTC\\n  summary: 'D088: 修正 D087——H7 非 GRPO 通用终态，而是 additive reward 特有终态；exec-only 1000步为\\n    100% H1'\\n  rationale: Reviewer 核实 plan016 (exec-only 1000步) 为 100% H1 (96/96)，非 H7。三种 reward\\n    mode 在 1000步的坍缩终态完全不同：exec-only→H1 (多premise结论嵌入), Random additive→H7 (单premise=结论),\\n    ISR additive→H7。可支撑叙事修正为：\\\"添加 additive reward（无论 ISR 还是 random）将坍缩模式从 H1 转向 H7；H7\\n    由 reward 结构驱动而非 ISR 语义信号；ISR 加速 H7 收敛（500步 vs 1000步）\\\"。所有 GRPO 模式在 1000步均达 0% genuine——坍缩本身是通用的，但坍缩模式取决于\\n    reward 结构。SFT 1000步 3-seed >90% genuine 确认 RL-specificity。另：Reviewer 发现 batch_h7ab_clean.json\\n    用了已失败实验数据（proved=100）而非 r3（proved=97），r3 registry metrics 与 taxonomy_note 矛盾，需修复。\\n  related_experiments:\\n  - exp_id: plan016\\n    role: critical_counter_evidence\\n    result: 'exec-only 1000步: H7=0, H1=96 (100%), genuine=0 — H1 坍缩而非 H7'\\n  - exp_id: plan018-random-b01-s42-1000-r3\\n    role: key_evidence\\n    result: 'Random additive 1000步: H7=97 (100%), H1=0'\\n  - exp_id: plan002-b01-s42-1000\\n    role: reference\\n    result: 'ISR additive 1000步: H7=87 (97%), H1=0'\\n  depends_on:\\n  - D087\\n\", \"total_chars\": 70987, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
The decisions file is too large. Let me extract the specific decisions I need (D027, D044, D051, D069, D079, D084, D085, D086) using grep or a subagent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "3e6bb28b-147a-4d7c-8fa1-e503f61602f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UK2cYDxQEwYTRxQh4CAgTU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 73084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 783
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

_source line 89_

Decisions file too large. Let me extract the specific decisions referenced in the task constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "f17048d9-f96a-4cc1-8e78-5d22d6d5bf58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UK2cYDxQEwYTRxQh4CAgTU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 73084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 783
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

_source line 90_

<details open><summary>🔧 Tool call — Agent · `toolu_01LT1gMyKzTr96Av3qS6Hs1Z`</summary>

```json
{
  "description": "Extract key decisions from YAML",
  "prompt": "I need to extract specific decisions from a large decisions YAML file for a paper number audit.\n\nThe file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt\n\nFormat: JSON with schema: {result: string} — the \"result\" field contains YAML content.\n\nI need the full text of these specific decisions:\n- D027 (plan013 vs plan017 formula structure)\n- D044 (ISR β=0.1 hacking rate labeling)\n- D051 (premise-count-matched 1.06x)\n- D056 (Prolog exec-only 3-seed)\n- D057 (3-seed ISR closed)\n- D059 (Prolog STA gaming)\n- D069 (s44 query-as-fact)\n- D079 (SFT 3-seed results)\n- D084 (genuine counting standard)\n- D085 (H7b obfuscated tautology)\n- D086 (β=0.3 H7 gradient)\n\nUse python to parse the JSON, then find each decision by its ID. Return the full content of each decision.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "7c41b38b-dc2d-4ab1-8a74-6d8b7a84569b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UK2cYDxQEwYTRxQh4CAgTU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 73084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 783
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

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a28d650df62f0b960",
  "tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "description": "Extract key decisions from YAML",
  "task_type": "local_agent",
  "prompt": "I need to extract specific decisions from a large decisions YAML file for a paper number audit.\n\nThe file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt\n\nFormat: JSON with schema: {result: string} — the \"result\" field contains YAML content.\n\nI need the full text of these specific decisions:\n- D027 (plan013 vs plan017 formula structure)\n- D044 (ISR β=0.1 hacking rate labeling)\n- D051 (premise-count-matched 1.06x)\n- D056 (Prolog exec-only 3-seed)\n- D057 (3-seed ISR closed)\n- D059 (Prolog STA gaming)\n- D069 (s44 query-as-fact)\n- D079 (SFT 3-seed results)\n- D084 (genuine counting standard)\n- D085 (H7b obfuscated tautology)\n- D086 (β=0.3 H7 gradient)\n\nUse python to parse the JSON, then find each decision by its ID. Return the full content of each decision.",
  "uuid": "54a5b802-71b3-4f09-bbd7-a556e4a8dac6",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


## Round 2

## Round 2

55 recorded events


### User

_source line 92 · 2026-05-15T16:00:20.468Z_

I need to extract specific decisions from a large decisions YAML file for a paper number audit.

The file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt

Format: JSON with schema: {result: string} — the "result" field contains YAML content.

I need the full text of these specific decisions:
- D027 (plan013 vs plan017 formula structure)
- D044 (ISR β=0.1 hacking rate labeling)
- D051 (premise-count-matched 1.06x)
- D056 (Prolog exec-only 3-seed)
- D057 (3-seed ISR closed)
- D059 (Prolog STA gaming)
- D069 (s44 query-as-fact)
- D079 (SFT 3-seed results)
- D084 (genuine counting standard)
- D085 (H7b obfuscated tautology)
- D086 (β=0.3 H7 gradient)

Use python to parse the JSON, then find each decision by its ID. Return the full content of each decision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "76b5d047-58c9-440f-9f86-47ee9c8b840b"
}
```

</details>

---


### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a28d650df62f0b960",
  "tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt",
  "usage": {
    "total_tokens": 14437,
    "tool_uses": 1,
    "duration_ms": 4007
  },
  "last_tool_name": "Read",
  "uuid": "efbde935-33f9-4edd-9a4a-ca1279fe9121",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Read · `toolu_01UWLt5334XYqvc8qbyCaTSn`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "17be2967-6974-4588-8445-4c743099a3bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJsHEFuBbuwWDnhJbjKd4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6180,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6180,
        "ephemeral_1h_input_tokens": 0
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

_source line 95 · 2026-05-15T16:00:24.892Z_

<details><summary>↩ Tool result · reported error · `toolu_01UWLt5334XYqvc8qbyCaTSn`</summary>

```text
File content (37720 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "eb13c1e5-0156-40db-b268-fbff5ffce3ac",
  "tool_use_result": "Error: File content (37720 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 96_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a28d650df62f0b960",
  "tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt",
  "usage": {
    "total_tokens": 15516,
    "tool_uses": 2,
    "duration_ms": 8010
  },
  "last_tool_name": "Read",
  "uuid": "d431e346-e2a6-4847-a166-f8ca9b4701ca",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Read · `toolu_01WeRJJN2hiZyb4Ffm2r8Syr`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "1beea70d-5d6e-40d5-9a6e-9f336c56db97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbwX57qSyAjdkn1sE2j9TP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1073,
      "cache_read_input_tokens": 14430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1073,
        "ephemeral_1h_input_tokens": 0
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

_source line 98 · 2026-05-15T16:00:28.888Z_

<details><summary>↩ Tool result · reported error · `toolu_01WeRJJN2hiZyb4Ffm2r8Syr`</summary>

```text
File content (37720 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "9e26d94c-35c1-415c-be0c-302a6d1ddc49",
  "tool_use_result": "Error: File content (37720 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a28d650df62f0b960",
  "tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt",
  "usage": {
    "total_tokens": 15827,
    "tool_uses": 3,
    "duration_ms": 11801
  },
  "last_tool_name": "Read",
  "uuid": "7ba82b12-9dc3-43b9-a2c5-fa17297acc44",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — Read · `toolu_01YbF4tQbRv2YJqP7y3jSAd5`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt",
  "limit": 20,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "2eeab5ff-0297-4bbc-879e-51e40d1dc734",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqJ3iHhNvMU78aajJ3rrVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 15503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 238,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
      "service_tier": "standard",
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

_source line 101 · 2026-05-15T16:00:32.599Z_

<details><summary>↩ Tool result · reported error · `toolu_01YbF4tQbRv2YJqP7y3jSAd5`</summary>

```text
File content (37720 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "9e87cfdc-c10a-443b-9d93-9b5b19a28726",
  "tool_use_result": "Error: File content (37720 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 102_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a28d650df62f0b960",
  "tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "description": "Running Count lines in the file",
  "usage": {
    "total_tokens": 16129,
    "tool_uses": 4,
    "duration_ms": 15242
  },
  "last_tool_name": "Bash",
  "uuid": "cb943f09-44a8-4fe5-8f34-71affb322398",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Bash · `toolu_01MXU15Zt8LLtifGVZJiXhUX`</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt\"",
  "description": "Count lines in the file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "38fdd673-6c56-4eff-86bd-1ed1cf931219",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eGgiN2WJaYRfy6t5KpVYW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 15741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 236,
        "ephemeral_1h_input_tokens": 0
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

_source line 104 · 2026-05-15T16:00:35.789Z_

<details><summary>↩ Tool result · `toolu_01MXU15Zt8LLtifGVZJiXhUX`</summary>

```text
0 /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results/mcp-agent-ml-research-read_project_file-1778860809973.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "03b307af-5a89-4cc9-87c8-60777d664bf2"
}
```

</details>

---


### System

_source line 105_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a28d650df62f0b960",
  "tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "description": "Running Parse JSON+YAML file and explore structure",
  "usage": {
    "total_tokens": 16406,
    "tool_uses": 5,
    "duration_ms": 23049
  },
  "last_tool_name": "Bash",
  "uuid": "a1a8c1a4-8532-4e42-9ce9-5c6356fbdfcd",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 106_

<details open><summary>🔧 Tool call — Bash · `toolu_01BAhNLy6nEJxAK5D1Bc6FNg`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results && python3 << 'PYEOF'\nimport json\nimport yaml\n\nwith open(\"mcp-agent-ml-research-read_project_file-1778860809973.txt\", \"r\") as f:\n    raw = f.read()\n\ndata = json.loads(raw)\nyaml_content = data[\"result\"]\n\ndecisions = yaml.safe_load(yaml_content)\n\ntarget_ids = [\"D027\", \"D044\", \"D051\", \"D056\", \"D057\", \"D059\", \"D069\", \"D079\", \"D084\", \"D085\", \"D086\"]\n\n# Explore structure first\nif isinstance(decisions, dict):\n    print(\"Top-level keys:\", list(decisions.keys())[:10])\n    # Check if decisions are nested\n    for k, v in list(decisions.items())[:3]:\n        print(f\"\\nKey: {k}\")\n        print(f\"Type: {type(v)}\")\n        if isinstance(v, dict):\n            print(f\"Sub-keys: {list(v.keys())[:5]}\")\nelif isinstance(decisions, list):\n    print(f\"List of {len(decisions)} items\")\n    if len(decisions) > 0:\n        print(f\"First item type: {type(decisions[0])}\")\n        if isinstance(decisions[0], dict):\n            print(f\"First item keys: {list(decisions[0].keys())}\")\n            print(f\"First item: {decisions[0]}\")\nPYEOF\n",
  "description": "Parse JSON+YAML file and explore structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "08bdb4c2-e3d5-47b1-b309-437e9a4727f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuRXTTam2ABdccKMPWTjYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 15977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 269,
        "ephemeral_1h_input_tokens": 0
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

_source line 107 · 2026-05-15T16:00:43.683Z_

<details><summary>↩ Tool result · `toolu_01BAhNLy6nEJxAK5D1Bc6FNg`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']

Key: success
Type: &lt;class 'bool'>

Key: data
Type: &lt;class 'dict'>
Sub-keys: ['path', 'content', 'total_chars', 'truncated']

Key: error
Type: &lt;class 'NoneType'>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "630baa21-d825-474b-b5ce-835d96ab5e9a"
}
```

</details>

---


### System

_source line 108_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a28d650df62f0b960",
  "tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "description": "Running Parse nested YAML content",
  "usage": {
    "total_tokens": 17093,
    "tool_uses": 6,
    "duration_ms": 29367
  },
  "last_tool_name": "Bash",
  "uuid": "fb77919f-6d41-4e4b-b396-5f4c25e57c58",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 109_

<details open><summary>🔧 Tool call — Bash · `toolu_01W8bPkpzGTr8fhEiksVs8XG`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results && python3 << 'PYEOF'\nimport json\nimport yaml\n\nwith open(\"mcp-agent-ml-research-read_project_file-1778860809973.txt\", \"r\") as f:\n    raw = f.read()\n\ndata = json.loads(raw)\nyaml_content = data[\"result\"]\nparsed = yaml.safe_load(yaml_content)\n\n# Navigate to actual content\ncontent_str = parsed[\"data\"][\"content\"]\n# This content_str should be the actual YAML decisions\ndecisions_data = yaml.safe_load(content_str)\n\nif isinstance(decisions_data, dict):\n    print(\"Top-level keys:\", list(decisions_data.keys())[:10])\nelif isinstance(decisions_data, list):\n    print(f\"List of {len(decisions_data)} items\")\n    if len(decisions_data) > 0:\n        print(f\"First item: {decisions_data[0]}\")\nelse:\n    print(f\"Type: {type(decisions_data)}\")\n    print(repr(content_str[:500]))\nPYEOF\n",
  "description": "Parse nested YAML content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "9e038460-7ef7-4a6c-9d5c-1f6a8569fb99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2VBMDf7Jm86eKEFp3V5od",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 16246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 614,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
      "service_tier": "standard",
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

_source line 110 · 2026-05-15T16:00:50.110Z_

<details><summary>↩ Tool result · `toolu_01W8bPkpzGTr8fhEiksVs8XG`</summary>

```text
Top-level keys: ['_next_id', 'decisions']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "94b264af-627d-498e-bb48-6de6b5757720"
}
```

</details>

---


### System

_source line 111_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a28d650df62f0b960",
  "tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "description": "Running Explore decisions structure",
  "usage": {
    "total_tokens": 17588,
    "tool_uses": 7,
    "duration_ms": 35620
  },
  "last_tool_name": "Bash",
  "uuid": "00028bf8-746d-48aa-b70e-ef6bf8a40e86",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---


### Tool call

_source line 112_

<details open><summary>🔧 Tool call — Bash · `toolu_01FMEMQqkqQ4x4Hem3W7wGEg`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/66001352-e738-4329-bbd1-9a766f6fb183/tool-results && python3 << 'PYEOF'\nimport json\nimport yaml\n\nwith open(\"mcp-agent-ml-research-read_project_file-1778860809973.txt\", \"r\") as f:\n    raw = f.read()\n\ndata = json.loads(raw)\nyaml_content = data[\"result\"]\nparsed = yaml.safe_load(yaml_content)\ncontent_str = parsed[\"data\"][\"content\"]\ndecisions_data = yaml.safe_load(content_str)\n\nall_decisions = decisions_data[\"decisions\"]\nprint(f\"Total decisions: {len(all_decisions)}\")\nprint(f\"Type: {type(all_decisions)}\")\n\n# Check structure - is it a dict keyed by ID or a list?\nif isinstance(all_decisions, dict):\n    print(f\"Keys sample: {list(all_decisions.keys())[:5]}\")\nelif isinstance(all_decisions, list):\n    if len(all_decisions) > 0:\n        print(f\"First item keys: {list(all_decisions[0].keys())}\")\n        # Find how ID is stored\n        print(f\"First item: {json.dumps(all_decisions[0], indent=2, default=str)[:500]}\")\nPYEOF\n",
  "description": "Explore decisions structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "6c8af736-4eaf-4a53-a7dc-8fe46f41fa47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XzN6SCeZx5Q9bNPhmDBjc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 423,
      "cache_read_input_tokens": 16860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 423,
        "ephemeral_1h_input_tokens": 0
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

_source line 113 · 2026-05-15T16:00:56.552Z_

<details><summary>↩ Tool result · `toolu_01FMEMQqkqQ4x4Hem3W7wGEg`</summary>

```text
Total decisions: 88
Type: &lt;class 'list'>
First item keys: ['id', 'date', 'summary', 'rationale', 'related_experiments', 'depends_on']
First item: {
  "id": "D001",
  "date": "2026-05-13 17:34 UTC",
  "summary": "MVP \u65b9\u6848\uff1aFOL+Prover9 \u5355\u903b\u8f91 50-step GRPO pilot \u9a8c\u8bc1 STA reward \u6709\u6548\u6027",
  "rationale": "EMNLP ARR DDL 5/25 \u4ec5\u5269 12 \u5929\uff0c\u9700\u8981\u6700\u5feb\u901f\u5ea6\u9a8c\u8bc1\u6838\u5fc3\u5047\u8bbe\u3002\u9009 FOL+Prover9 \u56e0\u4e3a hacking \u6a21\u5f0f\u6700\u6e05\u6670\uff08tautological formulas\uff09\uff0cSTA \u7684 O(1) \u8fd1\u4f3c\u6700\u76f4\u89c2\uff08\u53bb\u6389\u5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183",
  "uuid": "88df67f9-01aa-4ed1-b833-d953dfa83ce1"
}
```

</details>

---


### System

_source line 114_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a28d650df62f0b960",
  "tool_use_id": "toolu_01LT1gMyKzTr96Av3qS6Hs1Z",
  "description": "Running Extract all 11 target decisions by ID",
  "usage": {
    "total_tokens": 18517,
    "tool_uses": 8,
    "duration_ms": 45674
  },
  "last_tool_name": "Bash",
  "uuid": "0dbe3ac1-508c-4c2e-b293-892229b936bf",
  "session_id": "66001352-e738-4329-bbd1-9a766f6fb183"
}
```

---
