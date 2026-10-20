# writing experiments section

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_writing_experiments-section_20260514T185002.log`
- **Structured JSON:** [`4121c4eb7addaf466c4f.json`](../../sessions/41/4121c4eb7addaf466c4f.json)

## Before a recorded user message

25 recorded events

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
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
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
  "uuid": "63d64930-216c-44e6-94d4-a6135b7e7ae4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778800200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d997ad1b-b907-4a85-a4aa-d99fe80daf4c",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to write the Experiments section of an EMNLP 2026 paper. Let me start by reading the project files to get the full context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "843ca706-032f-4162-b8e0-2d3466e785d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKJpEzzEX788mHZMUkXhNa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14473,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14473
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

### Assistant

_source line 5_

I'll read the project files and registry to gather all the data needed for writing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "6ed1efe3-d978-41a5-9f62-663342b1ba5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKJpEzzEX788mHZMUkXhNa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14473,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14473
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PzCiLGWZkbkXsqr8LLBmCU`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
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
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "a07b0b0e-c03f-4176-abb0-cccb7437dd7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKJpEzzEX788mHZMUkXhNa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14473,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14473
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

_source line 7 · 2026-05-14T18:50:18.084Z_

<details><summary>↩ Tool result · `toolu_01PzCiLGWZkbkXsqr8LLBmCU`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "64d3207a-8956-4332-ac1f-f0222bc628a8",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Fohv3hRcwrFBNWsRhpXYXt`</summary>

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
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "92cec667-de8a-47a9-9557-05d57a7d9964",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CAmTrNUBmiVPqdrbk1vzN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 26314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
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

_source line 9 · 2026-05-14T18:50:28.581Z_

<details><summary>↩ Tool result · `toolu_01Fohv3hRcwrFBNWsRhpXYXt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (6 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR-as-reward **不提供任何真实结构优势**。\\n\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\n\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\n\\n| 条件 | n | Mean n_prem | Mean ISR |\\n|------|---|-------------|----------|\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\n| **Ratio** | — | — | **1.06×** |\\n\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\n- ISR s42 的 15/26 \\\"genuine\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\n- ISR s44 的 12 个\\\"genuine\\\"全是 n_prem=1（H7 分类器 false negative——单 premise 但 normalization 差异导致未匹配 conclusion）\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高，与证明质量无关\\n\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **86.5%** (77/89) | 0% | 86.5% | ~13.5% (~12, 全 n_prem=1 FN) |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **70.9%** (56/79) | 70.9% | 29.1% (23) |\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | 6.8% (6) |\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | 20.2% (18) |\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | **18.7%±11.3%** |\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **64.5%** | **17.3%** | — | **~16.2%** |\\n\\n**关键发现 (D057 3-seed closed)**：\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7=64.5% (149/231)，Random 3-seed H7=**0%** (0/256)。H7 跨全部 3 random seeds 一致为零，确认是 ISR reward 特异性诱导\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\n\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\"genuine\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\n\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\n\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\n\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%, ISR=0.040±0.037。ISR 在所有 3 seeds 上一致检测到结构退化（near-zero），不受 PR 水平影响——诊断迁移的核心证据。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\n  - s42: PR=83%, ISR=0.031 (ground fact enumeration)\\n  - s43: PR=56%, ISR=0.008 (degraded)\\n  - s44: PR=21%, ISR=0.081, proved-only ISR=0.387 (severe degradation, small-sample artifact)\\n- D056 结论：Prolog exec-only 跨 3 seeds ISR 一致崩塌（0.008–0.081），与 FOL exec-only 崩塌模式（0.0–0.132）对应。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\n\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\n\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\n\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\"100% Genuine\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\"Genuine=100%\\\" 不可信，必须交叉验证 n_necessary 分布。**\\n\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\n- 每个 seed 发展出不同的 gaming pathway：\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\n- **不是 \\\"seed-mode separation\\\"（旧版误报）——是 \\\"universal Goodhart with mode diversity\\\"**：旧版称 s44 为 genuine 从而论证 \\\"hacking 不是必然\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\n\\n**FOL vs Prolog ISR-as-reward 对比**：\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\n\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\"genuine improvement\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%)\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\"genuine improvement\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 6 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n\\n**论文处理**：降级为 **Limitation / Future Work**。\\n\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 87%**, ISR inflation | **meta-Goodhart** |\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | control |\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | control |\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 是 classic Goodhart。ISR 的核心价值在诊断（Claim 1）。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\n- **\\\"Single-logic risk\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\n2. **\\\"β=0.1 success is just one seed\\\"** — D051 shows even that one seed's \\\"success\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\n3. **\\\"Conclusion embedding invalidates ISR results\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\n4. **\\\"Goodhart's Law is obvious\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\n5. **\\\"No positive result\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\n6. **\\\"ISR is circular\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\n7. **\\\"Only one logic type\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\n8. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\n9. **\\\"3 seeds insufficient\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\n10. **\\\"2.4x was wrong — credibility concern\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\n11. **\\\"Premise count confound is obvious\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\n12. **\\\"Practitioners can't act on this\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\n13. **\\\"Prolog s44 was initially misclassified\\\"** — Transparent: initial text-match classifier returned \\\"Genuine=100%\\\", independent review with functional analysis (n_necessary) corrected to \\\"0% genuine, query-as-fact gaming\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\n- [ ] **D051: Remove all \\\"2.4x genuine improvement\\\" language, replace with \\\"1.06x premise-matched\\\"**\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\n- [x] Convex combination → additive bonus (D010, then D020)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016)\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\n- [x] D051: paper_framing 回退到 \\\"pure negative finding\\\"\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\n\", \"total_chars\": 21623, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "ad74cd7c-d5e4-457d-afd6-ffa1c2e1cc28",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — solver-trace-ablation\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\\\n\\\\n| Claim | Status | 闭环标志 |\\\\n|-------|--------|----------|\\\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (6 modes) |\\\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\\\n\\\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\\\n\\\\n**证据**：\\\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\\\n\\\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR-as-reward **不提供任何真实结构优势**。\\\\n\\\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\\\n\\\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\\\n\\\\n| 条件 | n | Mean n_prem | Mean ISR |\\\\n|------|---|-------------|----------|\\\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\\\n| **Ratio** | — | — | **1.06×** |\\\\n\\\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\\\n- ISR s42 的 15/26 \\\\\\\"genuine\\\\\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\\\n- ISR s44 的 12 个\\\\\\\"genuine\\\\\\\"全是 n_prem=1（H7 分类器 false negative——单 premise 但 normalization 差异导致未匹配 conclusion）\\\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\\\\\"必要\\\\\\\" → ISR 更高，与证明质量无关\\\\n\\\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\\\n\\\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **86.5%** (77/89) | 0% | 86.5% | ~13.5% (~12, 全 n_prem=1 FN) |\\\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **70.9%** (56/79) | 70.9% | 29.1% (23) |\\\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | 6.8% (6) |\\\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | 20.2% (18) |\\\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | **18.7%±11.3%** |\\\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **64.5%** | **17.3%** | — | **~16.2%** |\\\\n\\\\n**关键发现 (D057 3-seed closed)**：\\\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7=64.5% (149/231)，Random 3-seed H7=**0%** (0/256)。H7 跨全部 3 random seeds 一致为零，确认是 ISR reward 特异性诱导\\\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\\\n\\\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\\\n\\\\n**证据（β=0.3 同剂量对照）**：\\\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\\\n\\\\n**β 剂量效应全景**：\\\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\\\n|---|---|---|---|---|---|\\\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\\\n\\\\n**其他 ISR-as-reward 失败模式**：\\\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\\\n\\\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\\\\\"additive vs convex\\\\\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\\\n\\\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\\\\\"genuine\\\\\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\\\n\\\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\\\n\\\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\\\n\\\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%, ISR=0.040±0.037。ISR 在所有 3 seeds 上一致检测到结构退化（near-zero），不受 PR 水平影响——诊断迁移的核心证据。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\\\n  - s42: PR=83%, ISR=0.031 (ground fact enumeration)\\\\n  - s43: PR=56%, ISR=0.008 (degraded)\\\\n  - s44: PR=21%, ISR=0.081, proved-only ISR=0.387 (severe degradation, small-sample artifact)\\\\n- D056 结论：Prolog exec-only 跨 3 seeds ISR 一致崩塌（0.008–0.081），与 FOL exec-only 崩塌模式（0.0–0.132）对应。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\\\n\\\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\\\n\\\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\\\n\\\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\\\\\"100% Genuine\\\\\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\\\\\"Genuine=100%\\\\\\\" 不可信，必须交叉验证 n_necessary 分布。**\\\\n\\\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\\\n- 每个 seed 发展出不同的 gaming pathway：\\\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\\\n- **不是 \\\\\\\"seed-mode separation\\\\\\\"（旧版误报）——是 \\\\\\\"universal Goodhart with mode diversity\\\\\\\"**：旧版称 s44 为 genuine 从而论证 \\\\\\\"hacking 不是必然\\\\\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\\\n\\\\n**FOL vs Prolog ISR-as-reward 对比**：\\\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\\\n\\\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\\\\\"genuine improvement\\\\\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%)\\\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\\\\\"conclusion duplication with ISR inflation\\\\\\\")\\\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\\\n- **Actionable insights for practitioners**:\\\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\\\\\"genuine improvement\\\\\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\\\n- **Headline result**: \\\\\\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 6 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\\\\\"\\\\n\\\\n## ISR Capability Boundary (D021/D022)\\\\n\\\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\\\n\\\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\\\n\\\\n**论文处理**：降级为 **Limitation / Future Work**。\\\\n\\\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\\\\\"必要\\\\\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\\\n\\\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\\\n\\\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\\\n|------|------|---------|----------|----------|---------------|\\\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 87%**, ISR inflation | **meta-Goodhart** |\\\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | control |\\\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | control |\\\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\\\n\\\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 是 classic Goodhart。ISR 的核心价值在诊断（Claim 1）。\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\\\n- **\\\\\\\"Just negative results\\\\\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\\\n- **\\\\\\\"Old wine\\\\\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\\\n- **\\\\\\\"Single-logic risk\\\\\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"ISR is just LOO ablation — not novel\\\\\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\\\n2. **\\\\\\\"β=0.1 success is just one seed\\\\\\\"** — D051 shows even that one seed's \\\\\\\"success\\\\\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\\\n3. **\\\\\\\"Conclusion embedding invalidates ISR results\\\\\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\\\n4. **\\\\\\\"Goodhart's Law is obvious\\\\\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\\\n5. **\\\\\\\"No positive result\\\\\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\\\n6. **\\\\\\\"ISR is circular\\\\\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\\\n7. **\\\\\\\"Only one logic type\\\\\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\\\n8. **\\\\\\\"500 steps too short\\\\\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\\\n9. **\\\\\\\"3 seeds insufficient\\\\\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\\\n10. **\\\\\\\"2.4x was wrong — credibility concern\\\\\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\\\n11. **\\\\\\\"Premise count confound is obvious\\\\\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\\\n12. **\\\\\\\"Practitioners can't act on this\\\\\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\\\n13. **\\\\\\\"Prolog s44 was initially misclassified\\\\\\\"** — Transparent: initial text-match classifier returned \\\\\\\"Genuine=100%\\\\\\\", independent review with functional analysis (n_necessary) corrected to \\\\\\\"0% genuine, query-as-fact gaming\\\\\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\\\n\\\\n## Dream-Identified Structural Fixes (Paper Agent)\\\\n\\\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\\\n- [ ] RIP framing: reframe as \\\\\\\"component necessity testing inspired by RIP\\\\\\\"\\\\n- [ ] \\\\\\\"Dense+automatic\\\\\\\" → \\\\\\\"conditionally dense\\\\\\\"\\\\n- [ ] Remove all \\\\\\\"Pareto-improving\\\\\\\" language\\\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\\\n- [ ] **D051: Remove all \\\\\\\"2.4x genuine improvement\\\\\\\" language, replace with \\\\\\\"1.06x premise-matched\\\\\\\"**\\\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\\\n- [x] Convex combination → additive bonus (D010, then D020)\\\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043)\\\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\\\n- [x] 1000-step ISR collapse documented (plan016)\\\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\\\n- [x] D051: paper_framing 回退到 \\\\\\\"pure negative finding\\\\\\\"\\\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\\\n\\\", \\\"total_chars\\\": 21623, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (6 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR-as-reward **不提供任何真实结构优势**。\\n\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\n\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\n\\n| 条件 | n | Mean n_prem | Mean ISR |\\n|------|---|-------------|----------|\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\n| **Ratio** | — | — | **1.06×** |\\n\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\n- ISR s42 的 15/26 \\\"genuine\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\n- ISR s44 的 12 个\\\"genuine\\\"全是 n_prem=1（H7 分类器 false negative——单 premise 但 normalization 差异导致未匹配 conclusion）\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高，与证明质量无关\\n\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **86.5%** (77/89) | 0% | 86.5% | ~13.5% (~12, 全 n_prem=1 FN) |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **70.9%** (56/79) | 70.9% | 29.1% (23) |\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | 6.8% (6) |\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | 20.2% (18) |\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | **18.7%±11.3%** |\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **64.5%** | **17.3%** | — | **~16.2%** |\\n\\n**关键发现 (D057 3-seed closed)**：\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7=64.5% (149/231)，Random 3-seed H7=**0%** (0/256)。H7 跨全部 3 random seeds 一致为零，确认是 ISR reward 特异性诱导\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\n\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\"genuine\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\n\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\n\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\n\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%, ISR=0.040±0.037。ISR 在所有 3 seeds 上一致检测到结构退化（near-zero），不受 PR 水平影响——诊断迁移的核心证据。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\n  - s42: PR=83%, ISR=0.031 (ground fact enumeration)\\n  - s43: PR=56%, ISR=0.008 (degraded)\\n  - s44: PR=21%, ISR=0.081, proved-only ISR=0.387 (severe degradation, small-sample artifact)\\n- D056 结论：Prolog exec-only 跨 3 seeds ISR 一致崩塌（0.008–0.081），与 FOL exec-only 崩塌模式（0.0–0.132）对应。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\n\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\n\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\n\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\"100% Genuine\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\"Genuine=100%\\\" 不可信，必须交叉验证 n_necessary 分布。**\\n\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\n- 每个 seed 发展出不同的 gaming pathway：\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\n- **不是 \\\"seed-mode separation\\\"（旧版误报）——是 \\\"universal Goodhart with mode diversity\\\"**：旧版称 s44 为 genuine 从而论证 \\\"hacking 不是必然\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\n\\n**FOL vs Prolog ISR-as-reward 对比**：\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\n\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\"genuine improvement\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%)\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\"genuine improvement\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 6 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n\\n**论文处理**：降级为 **Limitation / Future Work**。\\n\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 87%**, ISR inflation | **meta-Goodhart** |\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | control |\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | control |\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 是 classic Goodhart。ISR 的核心价值在诊断（Claim 1）。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\n- **\\\"Single-logic risk\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\n2. **\\\"β=0.1 success is just one seed\\\"** — D051 shows even that one seed's \\\"success\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\n3. **\\\"Conclusion embedding invalidates ISR results\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\n4. **\\\"Goodhart's Law is obvious\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\n5. **\\\"No positive result\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\n6. **\\\"ISR is circular\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\n7. **\\\"Only one logic type\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\n8. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\n9. **\\\"3 seeds insufficient\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\n10. **\\\"2.4x was wrong — credibility concern\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\n11. **\\\"Premise count confound is obvious\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\n12. **\\\"Practitioners can't act on this\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\n13. **\\\"Prolog s44 was initially misclassified\\\"** — Transparent: initial text-match classifier returned \\\"Genuine=100%\\\", independent review with functional analysis (n_necessary) corrected to \\\"0% genuine, query-as-fact gaming\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\n- [ ] **D051: Remove all \\\"2.4x genuine improvement\\\" language, replace with \\\"1.06x premise-matched\\\"**\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\n- [x] Convex combination → additive bonus (D010, then D020)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016)\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\n- [x] D051: paper_framing 回退到 \\\"pure negative finding\\\"\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\n\", \"total_chars\": 21623, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Pa8rW5Yrvtqyt1bu6SLZRd`</summary>

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
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "fc76d8c9-5a59-43ed-984e-c7a39cf9e18e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CAmTrNUBmiVPqdrbk1vzN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 26314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
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

_source line 11 · 2026-05-14T18:50:30.124Z_

<details><summary>↩ Tool result · `toolu_01Pa8rW5Yrvtqyt1bu6SLZRd`</summary>

```text
Error: result (110,225 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/0a1a0156-b769-4b25-b997-fd48e14477bf/tool-results/mcp-agent-ml-research-read_registry-1778784630103.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/0a1a0156-b769-4b25-b997-fd48e14477bf/tool-results/mcp-agent-ml-research-read_registry-1778784630103.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/0a1a0156-b769-4b25-b997-fd48e14477bf/tool-results/mcp-agent-ml-research-read_registry-1778784630103.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "05ab9f34-a846-45d9-af2a-7ebe88cc88fc",
  "tool_use_result": {
    "content": "Error: result (110,225 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/0a1a0156-b769-4b25-b997-fd48e14477bf/tool-results/mcp-agent-ml-research-read_registry-1778784630103.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/0a1a0156-b769-4b25-b997-fd48e14477bf/tool-results/mcp-agent-ml-research-read_registry-1778784630103.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/0a1a0156-b769-4b25-b997-fd48e14477bf/tool-results/mcp-agent-ml-research-read_registry-1778784630103.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan006-prolog-sta-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:19:39.743Z\", \"updated_at\": \"2026-05-14T18:47:53.131Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。\", \"notes\": \"Reviewer 独立核实: query-as-fact gaming, 0% genuine. 97/97 proved 样本中 95/97 n_necessary=1（功能性 H7）。模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。PR=0.97, ISR=0.885 是 gaming artifact（高 ISR 因单 clause = query）。第三种 Goodhart pathway（vs s42 clean H7, s43 degenerate syntax H1）。对照: s42=negative (clean H7=100%), s43=negative (uppercase pseudo-Prolog H1=97.4%), s44=negative (query-as-fact gaming, functional H7=95/97).\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T16:46:42.163Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s44\\\"\", \"finished_at\": \"2026-05-14T18:17:19.877Z\", \"training_hours\": 1.51}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"908945\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s44.log\", \"submitted_at\": \"2026-05-14T16:52:27.078Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5546.5, \"gpu_hours\": 1.54}, \"pid\": \"908945\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:17:22.483042+00:00\"}]}, \"metrics\": {\"pass_rate\": 0.97, \"isr_mean\": 0.885, \"isr_n_cl_ge3\": \"N/A (0 samples)\", \"n_clauses_dist\": \"78/100 single-clause, 22/100 two-clause\", \"h7_functional_rate\": 0.979, \"genuine_rate\": 0, \"premise_count_analysis\": \"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\", \"failure_mode\": \"query-as-fact gaming (total H7 collapse)\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s44/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T18:24:53.618Z\"}, \"plan006-prolog-sta-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:19:39.141Z\", \"updated_at\": \"2026-05-14T18:20:56.947Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。\", \"notes\": \"Eval: PR=0.38, ISR=0.185 proved-only. Strict classifier: H7=0%, H1=0%, Genuine=100%. 但功能分析显示所有 38 proved 样本 n_necessary=1（功能性 H7）。模型生成大写伪 Prolog（如 MARY_IS_AN_AVADEOTE.）—— 非标准语法，strict classifier 无法匹配 conclusion。与 s42 (clean H7=100%) 不同的 Goodhart 路径，但同样是 hacking。磁盘 240G/250G 需清理。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"901135\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s43.log\", \"submitted_at\": \"2026-05-14T16:36:41.878Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s43\", \"wall_clock_seconds\": 6158.3, \"gpu_hours\": 1.71}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"901135\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s43\\\"\", \"finished_at\": \"2026-05-14T18:03:44.715Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:03:46.512937+00:00\"}]}, \"metrics\": {\"train\": {\"final_prove_rate\": 0.769, \"final_mean_isr\": 0.129, \"final_loss\": 0.0155, \"final_entropy\": 0.09, \"final_reward\": 0.573, \"completion_length_mean\": 143, \"train_runtime_seconds\": 5095, \"train_runtime_minutes\": 84.9}, \"eval\": {\"n_problems\": 100, \"n_proved\": 38, \"prove_rate\": 0.38, \"mean_isr\": 0.0704, \"isr_std\": 0.1263, \"median_isr\": 0, \"proved_only_mean_isr\": 0.1853, \"min_isr\": 0, \"max_isr\": 1, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 11, \"prove_rate\": 0.44, \"mean_isr\": 0.1003}, \"unknown\": {\"count\": 41, \"proved\": 11, \"prove_rate\": 0.268, \"mean_isr\": 0.0394}, \"true\": {\"count\": 34, \"proved\": 16, \"prove_rate\": 0.471, \"mean_isr\": 0.0859}}}, \"h7_classification\": {\"h7_strict\": 0, \"h7_rate\": 0, \"h1_strict\": 37, \"h1_rate\": 0.974, \"conclusion_in_premise_total\": 37, \"conclusion_in_premise_rate\": 0.974, \"genuine_count\": 0, \"genuine_rate\": 0, \"isr_1_count\": 1, \"note\": \"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\"}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T18:19:20.203Z\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s43\"}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:29:47.634Z\", \"updated_at\": \"2026-05-14T17:34:52.375Z\", \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？\", \"parent\": \"plan001-exec-only-s42-r2\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence?\", \"plan_id\": \"plan016\", \"reward_formula\": \"r = r_exec (exec-only)\", \"num_steps\": 1000}, \"pid\": \"263268\", \"log_path\": \"~/runs/solver-trace-ablation/plan016-extended-1000-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\\\"\", \"finished_at\": \"2026-05-14T08:02:31.805Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:02:33.434519+00:00\"}]}, \"metrics\": {\"prove_rate\": 0.96, \"isr\": 0.003, \"n_proved\": 96, \"components\": 18.55, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 96, \"h1_rate\": 1, \"genuine_count\": 0, \"genuine_rate\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan016_extended_1000_s42\", \"completed_at\": \"2026-05-14T08:13:51.754Z\", \"notes\": \"Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\\\n\\\\n## 500 vs 1000 step comparison (eval_sta.py):\\\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\\\n|--------|-------------------|-----------------|--------|\\\\n| eval PR | 0.93 | 0.96 | +3.2% |\\\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\\\n| components | 6.58 | 18.55 | +182% |\\\\n| ISR=0 ratio | - | 94.8% | - |\\\\n| n_necessary=0 ratio | - | 94.8% | - |\\\\n\\\\n## Key findings:\\\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\\\n\\\\n## Implication for paper:\\\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse.\"}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:29:08.138Z\", \"updated_at\": \"2026-05-14T17:33:21.938Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"262261\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42.log\", \"submitted_at\": \"2026-05-14T05:32:32.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan002\", \"reward_formula\": \"r_exec * (1 + 0.1 * ISR)\", \"num_steps\": 500, \"wall_clock_seconds\": 4493.9, \"gpu_hours\": 1.25, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42\"}, \"parent\": \"plan002-additive-b03-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"262261\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\\\"\", \"finished_at\": \"2026-05-14T06:37:58.285Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:37:59.656631+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"h7_rate\": 0.16, \"h7_count\": 13, \"h1_rate\": 0.519, \"h1_count\": 42, \"genuine_rate\": 0.309, \"genuine_count\": 25, \"tautological_collapse\": false}, \"notes\": \"H7 audit (2026-05-14): 81 proved samples. H7 (single premise=conclusion): 13/81=16.0%, mean ISR=0.6603. H1 (multi premise contains conclusion): 42/81=51.9%, mean ISR=0.2245. Genuine (no conclusion duplication): 26/81=32.1%, mean ISR=0.6014. Combined conclusion duplication = 67.9%. CRITICAL: only 32.1% of proved samples are free of conclusion embedding. H7 inflates ISR; H1 deflates ISR but proof is trivially achievable via embedded conclusion. Claim 2 \\\"genuine structural guidance\\\" needs reframing — ISR signal is dominated by conclusion duplication artifacts.\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42\", \"completed_at\": \"2026-05-14T06:47:26.358Z\"}, \"plan018-additive-random-b01-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:01:24.111Z\", \"updated_at\": \"2026-05-14T17:17:02.398Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。\", \"parent\": \"plan018-additive-random-b01-s43\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\\\"\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"858386\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log\", \"submitted_at\": \"2026-05-14T15:24:32.942Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\", \"wall_clock_seconds\": 6748.8, \"gpu_hours\": 1.87}, \"pid\": \"858386\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\\\"\", \"finished_at\": \"2026-05-14T16:43:53.042Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T16:43:54.952857+00:00\"}]}, \"metrics\": {\"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 93.2, \"h1_count\": 82, \"genuine_rate\": 6.8, \"genuine_count\": 6}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T17:17:01.774Z\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T09:19:38.117Z\", \"updated_at\": \"2026-05-14T16:49:42.052Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。\", \"server\": \"westd-39279\", \"gpu\": \"\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T09:49:40.272Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42\\\"\", \"finished_at\": \"2026-05-14T10:38:13.891Z\", \"training_hours\": 0.81}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T09:46:00.917Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:46:02.621139+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:38:15.900825+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次启动失败。根因：config reward_mode=execution_sta (0.5*exec+0.5*ISR) 可能与 FOL 实验不匹配，待 Director 确认后修复重启。cuda:1 释放给 plan018。\"}}, \"account\": \"root\", \"notes\": \"Eval metrics provenance: eval 在训练完成后立即在 westd-39279 服务器上运行 eval_sta.py，checkpoint 路径 /root/autodl-tmp/outputs/plan006_prolog_sta_s42/。Eval 结果由 Worker 从服务器 SSH 读取 eval_results.json 并手动录入 registry。Checkpoint 可能已被磁盘清理删除（C003 save_total_limit=1）。训练日志: ~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log。H7 分类由 classify_h7.py 在 eval 目录上运行。\", \"spec\": {\"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42\\\"\", \"pid\": \"506117\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s42/ (may be cleaned up per C003)\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:57:09.690Z\", \"updated_at\": \"2026-05-14T16:29:02.086Z\", \"hypothesis\": \"Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"226200\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44.log\", \"submitted_at\": \"2026-05-14T04:29:05.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2725.5, \"gpu_hours\": 0.76}, \"pid\": \"226200\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\\\"\", \"finished_at\": \"2026-05-14T05:06:39.227Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:06:40.707032+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"tautological_collapse\": true, \"h7_rate\": 1, \"h7_count\": 97, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"conclusion_embedding_total\": 1}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s44\", \"conclusion\": \"negative\", \"notes\": \"TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。\", \"completed_at\": \"2026-05-14T05:14:30.940Z\"}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T22:40:41.773Z\", \"updated_at\": \"2026-05-14T16:28:58.538Z\", \"completed_at\": \"2026-05-13T23:46:00Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:46:01.596431+00:00\"}]}, \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s42\", \"server\": \"westd-39279\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"500-step exec-only baseline for STA comparison (K=8)\", \"pid\": \"84901\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r2.log\", \"submitted_at\": \"2026-05-13T22:42:40.204Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3820, \"gpu_hours\": 1.06}, \"notes\": \"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:46:00.369Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/reward_log.jsonl\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.871, \"h1_count\": 81, \"genuine_rate\": 0.129, \"genuine_count\": 12, \"genuine_mean_isr\": 0.3141, \"h1_mean_isr\": 0.1055, \"conclusion_embedding_total\": 0.871}}, \"plan006-prolog-exec-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:13:35.647Z\", \"updated_at\": \"2026-05-14T16:27:18.570Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper.\", \"notes\": \"Eval 完成。PR=21% (3-seed 最低), ISR=0.081, proved_only_ISR=0.387 (max_ISR=1.0)。与 s42/s43 不同模式：PR 极低但 proved_only_ISR 较高，可能有少量样本 ISR=1 (H7-like)。Prolog exec-only 3-seed 汇总：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008, s44 PR=21%/ISR=0.081。Mean PR=53.3%±31.1%, Mean ISR=0.040±0.037。跨 seed 极不稳定（PR std=31pp），与 FOL exec-only 一致。ISR 始终极低（<0.1），确认 Prolog exec-only 不产生 genuine reasoning traces。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T13:43:55.707Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44\\\"\", \"finished_at\": \"2026-05-14T15:20:42.126Z\", \"training_hours\": 1.61}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"479357\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s44.log\", \"submitted_at\": \"2026-05-14T13:43:57.850Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9800.7, \"gpu_hours\": 2.72}, \"pid\": \"479357\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:20:44.093424+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.21, \"eval_mean_isr\": 0.0812, \"eval_isr_std\": 0.2343, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.3866, \"eval_min_isr\": 0, \"eval_max_isr\": 1, \"eval_n_proved\": 21, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 683.9, \"eval_by_type_false_pr\": 0.04, \"eval_by_type_false_isr\": 0.04, \"eval_by_type_unknown_pr\": 0.317, \"eval_by_type_unknown_isr\": 0.099, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.09, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s44/checkpoint-500\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T16:27:18.570Z\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:40:28.142Z\", \"updated_at\": \"2026-05-14T16:27:01.864Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --num_steps 500 --seed 42 --no_wandb --gpu 1\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/\"}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"notes\": \"r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:18:55.639Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:18:57.313588+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/\", \"log_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/trainer_state.json\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.071, \"h1_count\": 1, \"genuine_rate\": 0.929, \"genuine_count\": 13, \"hacking_patterns\": \"near-zero (1/14 H1, 0 H7, 92.9% genuine)\", \"tautological_collapse\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:20:25.035Z\"}, \"plan006-prolog-exec-s43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:38:23.818Z\", \"updated_at\": \"2026-05-14T16:16:56.523Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T13:44:06.728Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3\\\"\", \"finished_at\": \"2026-05-14T15:54:25.754Z\", \"training_hours\": 2.17}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"483820\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r3.log\", \"submitted_at\": \"2026-05-14T13:44:08.516Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9168.0, \"gpu_hours\": 2.55}, \"pid\": \"483820\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r3.log\", \"notes\": \"Eval 完成。PR=56% (远低于 s42 的 83%), ISR=0.0084 (与 s42 的 0.031 同量级，均极低)。proved_only_ISR=0.015。Prolog exec-only 跨 seed 表现：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008。s43 prove_rate 显著下降但 ISR 模式一致（极低，ground fact enumeration hacking）。与 FOL exec-only 类似，存在跨 seed 不稳定性（FOL: s42=93%, s43=14%, s44=98%）。等 s44 eval 完成后计算 3-seed mean±std。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:54:27.521808+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.56, \"eval_mean_isr\": 0.0084, \"eval_isr_std\": 0.0221, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.015, \"eval_min_isr\": 0, \"eval_max_isr\": 0.1, \"eval_n_proved\": 56, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 868.2, \"eval_by_type_false_pr\": 0.48, \"eval_by_type_false_isr\": 0.0043, \"eval_by_type_unknown_pr\": 0.6585, \"eval_by_type_unknown_isr\": 0.0114, \"eval_by_type_true_pr\": 0.5, \"eval_by_type_true_isr\": 0.0078, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3/checkpoint-500\", \"completed_at\": \"2026-05-14T16:16:56.523Z\"}, \"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.722Z\", \"updated_at\": \"2026-05-14T15:00:09.178Z\", \"hypothesis\": \"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:34:13.338Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"finished_at\": \"2026-05-14T13:37:42.200Z\", \"training_hours\": 2.06}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"564900\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500}, \"pid\": \"564900\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:37:43.236026+00:00\"}]}, \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\", \"notes\": \"DONE (success). Random β=0.1 s44 对照分析完成: PR=0.89/ISR=0.062 (clean) vs ISR β=0.1 s44 PR=0.89/ISR=0.803 (H7=86.5% inflated). 同 PR 下 ISR reward 导致 conclusion duplication，random 无此问题。与 s42 结论一致: ISR s42 genuine ISR=0.337 vs Random s42 ISR=0.104 (3.2x)。Random 2/3 seeds done, 等 s43 (plan018-random-b01-s43-r2 QUEUED)。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s44/checkpoint-500\", \"completed_at\": \"2026-05-14T14:29:21.226Z\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:58.328Z\", \"updated_at\": \"2026-05-14T14:20:43.363Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\", \"conclusion\": \"killed\", \"notes\": \"模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。\", \"completed_at\": \"2026-05-14T14:20:42.452Z\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:32:37.140Z\", \"updated_at\": \"2026-05-14T13:43:01.701Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.\", \"parent\": \"plan006-prolog-exec-s43\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"712243\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r2.log\", \"submitted_at\": \"2026-05-14T12:33:05.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 136.2, \"gpu_hours\": 0.04}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"712243\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r2\\\"\", \"finished_at\": \"2026-05-14T12:35:20.730Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 48.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 40.25 MiB is free. Process 587160 has 78.09 GiB memory in use. Including non-PyTorch memory, this process has 16.83 GiB memory in use. Of the allocated \", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:35:22.121Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:35:23.802887+00:00\"}]}, \"notes\": \"OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T07:13:34.169Z\", \"updated_at\": \"2026-05-14T12:33:17.845Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T09:49:36.534Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42\\\"\", \"finished_at\": \"2026-05-14T11:29:25.346Z\", \"training_hours\": 1.66}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T09:47:36.390Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:47:38.546001+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:29:27.709792+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: FileNotFoundError — data/prolog/train_500_seed42.jsonl 不存在 | error_type: data | 同一原因影响所有 plan006 实验 (exec/sta × s42/s43/s44) | 建议: 需先生成 Prolog 训练数据再重试\"}}, \"account\": \"root\", \"notes\": \"Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"506020\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42}, \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s42/checkpoint-500\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s42.log\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:13:35.078Z\", \"updated_at\": \"2026-05-14T12:32:13.799Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.\", \"notes\": \"KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 --warmup_ratio 0.1\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"587155\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43.log\", \"submitted_at\": \"2026-05-14T12:22:08.915Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"wall_clock_seconds\": 602.2, \"gpu_hours\": 0.17}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"587155\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 --warmup_ratio 0.1\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:32:11.136Z\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:37:49.306Z\", \"updated_at\": \"2026-05-14T11:48:05.087Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r3 --num_steps 500 --seed 42 --bf16 --wandb_project solver-trace-ablation --wandb_run plan009-sft-s42-r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"566690\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r3.log\", \"submitted_at\": \"2026-05-14T11:39:19.395Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18.5, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"566690\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r3.log\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r3 --num_steps 500 --seed 42 --bf16 --wandb_project solver-trace-ablation --wandb_run plan009-sft-s42-r3\\\"\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"finished_at\": \"2026-05-14T11:39:36.697Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:39:37.935Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:39:39.416777+00:00\"}]}, \"notes\": \"r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:02:25.369Z\", \"updated_at\": \"2026-05-14T11:43:20.347Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"plan_id\": \"plan_009\", \"notes\": \"SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --num_steps 200 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"548527\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r2.log\", \"submitted_at\": \"2026-05-14T11:08:22.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 236.8, \"gpu_hours\": 0.07}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:12:19.306Z\", \"failure_reason\": \"OOM: 缺少 CUDA_VISIBLE_DEVICES 显式设置，device_map='auto' 跨 GPU 侵入 cuda:0 (plan006)，导致双卡 OOM。修复：(1) 启动命令加 --gpu 1，(2) device_map 改为 {\\\"\\\": 0} 或 .to(\\\"cuda\\\")，(3) num_steps 改为 500\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.260Z\", \"updated_at\": \"2026-05-14T11:42:09.950Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"540910\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43.log\", \"submitted_at\": \"2026-05-14T10:58:27.110Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"checkpoint_source\": \"plan018-additive-random-b01-s42\", \"eval_data\": \"data/train_500_seed42.jsonl\", \"wall_clock_seconds\": 1929.4, \"gpu_hours\": 0.54}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:30:34.690Z\"}, \"failure_reason\": \"磁盘满 (No space left on device): /root/autodl-tmp/ 250G/250G 100% 占满。训练在 step 200/500 保存 checkpoint-200 时 safetensors 序列化失败 (os error 28)。根因: 多个已完成实验的 checkpoint 未清理。可重试——清理磁盘后重跑。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:30:36.549Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:30:40.886615+00:00\"}]}, \"notes\": \"Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \\\"No space left on device\\\". No checkpoint saved. Disk now has 109G free. Retryable as-is.\"}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:17.298Z\", \"updated_at\": \"2026-05-14T10:12:40.545Z\", \"hypothesis\": \"ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。\", \"parent\": \"plan002-additive-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T08:45:11.826Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s44\\\"\", \"finished_at\": \"2026-05-14T09:28:10.836Z\", \"training_hours\": 0.72}, \"spec\": {\"command\": \"python3 scripts/train_grpo.py --mode additive_bonus --isr_beta 0.1 --seed 44\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"466540\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s44.log\", \"submitted_at\": \"2026-05-14T08:46:23.037Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"wall_clock_seconds\": 2950.3, \"gpu_hours\": 0.82}, \"pid\": \"466540\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:28:12.416418+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": 0.3418, \"eval_median_isr\": 1, \"component_count_mean\": 4.33, \"component_count_2_ratio\": 0.022, \"tautological_collapse\": false, \"isr_0_ratio\": 0.12, \"isr_1_ratio\": 0.73, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.865, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"component_dist\": {\"2\": 2, \"4\": 54, \"5\": 33}, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 22, \"PR\": 0.88, \"ISR\": 0.824}, \"unknown\": {\"n\": 41, \"proved\": 38, \"PR\": 0.927, \"ISR\": 0.837}, \"true\": {\"n\": 34, \"proved\": 29, \"PR\": 0.853, \"ISR\": 0.747}}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s44\", \"notes\": \"RECLASSIFIED negative (D039): Reviewer 逐样本审查发现 semantic drift hacking — 模型生成极简形式化（单 premise≈conclusion），通过 conclusion sub-component ablation 膨胀 ISR。ISR=0.902 是 conclusion_duplication_isr_inflation artifact，非真正证明质量。65% 样本 ISR=1.0 为 conclusion embedding。此 hacking mode 本身是论文 positive finding（强化 Claim 1 Goodhart 叙事：ISR reward 导致新型 hacking）。原始 eval 指标：PR=0.89, mean_isr=0.803, component_mean=4.33, comp_2_ratio=0.022。exec-only s44 是 tautological collapse (94% 2-comp)，ISR β=0.1 s44 避免了 tautological collapse 但转向了 conclusion duplication hacking。\", \"completed_at\": \"2026-05-14T09:35:33.310Z\"}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:16.367Z\", \"updated_at\": \"2026-05-14T10:12:36.502Z\", \"hypothesis\": \"ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。\", \"parent\": \"plan002-additive-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T08:45:10.999Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\\\"\", \"finished_at\": \"2026-05-14T09:41:23.932Z\", \"training_hours\": 0.94}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"466128\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s43.log\", \"submitted_at\": \"2026-05-14T08:45:54.837Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4096.6, \"gpu_hours\": 1.14}, \"pid\": \"466128\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s43.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:41:25.536028+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"component_count_mean\": 4.03, \"component_count_2_ratio\": 0, \"tautological_collapse\": false, \"isr_0_ratio\": 0.39, \"isr_1_ratio\": 0.656, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.967, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 18, \"PR\": 0.72, \"ISR\": 0.6}, \"unknown\": {\"n\": 41, \"proved\": 22, \"PR\": 0.537, \"ISR\": 0.442}, \"true\": {\"n\": 34, \"proved\": 21, \"PR\": 0.618, \"ISR\": 0.515}}, \"train_total_steps\": 500, \"train_duration_min\": 53, \"train_loss\": 0.012}, \"conclusion\": \"negative\", \"notes\": \"NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s43/checkpoint-500\", \"completed_at\": \"2026-05-14T09:54:11.468Z\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:06:38.613Z\", \"updated_at\": \"2026-05-14T09:07:42.314Z\", \"spec\": {\"command\": \"rule-based hacking taxonomy classification on eval_sta outputs\", \"server\": \"westd-39279\", \"data_path\": \"eval_results.json from plan002-b01-s42 + plan018-b01-s42\", \"data_count\": 160, \"model_name\": \"N/A (rule-based analysis)\", \"seed\": \"N/A\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"artifacts/hacking_taxonomy_comparison.md\", \"completed_at\": \"2026-05-14T09:07:12.765Z\", \"hypothesis\": \"ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}, \"notes\": \"D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。\"}, \"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:55:48.888Z\", \"updated_at\": \"2026-05-14T08:32:44.808Z\", \"hypothesis\": \"β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。\", \"parent\": \"plan002-additive-b01-s42\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"377678\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42.log\", \"submitted_at\": \"2026-05-14T06:55:59.287Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan018\", \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500, \"checkpoint_source\": \"N/A (training, not eval)\", \"eval_data\": \"N/A (training, not eval)\", \"wall_clock_seconds\": 5160.4, \"gpu_hours\": 1.43, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:09:07.662Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:09:09.188407+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"eval_component_count_mean\": 8.46, \"eval_component_count_median\": 8, \"eval_component_count_2_ratio\": 0, \"eval_isr_1_ratio\": 0, \"eval_isr_0_ratio\": 0.367, \"eval_isr_gt0_ratio\": 0.633, \"eval_by_type_false_pr\": 0.8, \"eval_by_type_false_isr\": 0.1318, \"eval_by_type_unknown_pr\": 0.7317, \"eval_by_type_unknown_isr\": 0.0944, \"eval_by_type_true_pr\": 0.8529, \"eval_by_type_true_isr\": 0.0945, \"tautological_collapse\": false, \"train_total_steps\": 500, \"train_duration_min\": 70.5, \"train_last100_pr\": 0.805, \"train_last100_isr\": 0.1432, \"train_loss\": 0.005}, \"notes\": \"Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\\n\\n对比 plan002-b01 (ISR β=0.1):\\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\\n- Median ISR: 0.036 vs plan002未记录\\n- Component count: 8.46 vs 5.58 (random组更多冗余)\\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\\n- Tautological collapse: 无 (component_2_ratio=0)\\n\\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\\n\\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42\", \"completed_at\": \"2026-05-14T08:21:59.737Z\"}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:20:47.812Z\", \"updated_at\": \"2026-05-14T06:31:05.119Z\", \"spec\": {\"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:55:02.341Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:55:06.559440+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/reward_log.jsonl\", \"completed_at\": \"2026-05-13T23:59:25.396Z\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}, \"notes\": \"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\"STA 抑制 reward hacking\\\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。\"}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:40:37.808Z\", \"updated_at\": \"2026-05-14T06:30:57.539Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"136339\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log\", \"submitted_at\": \"2026-05-14T01:40:37.746Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds\", \"plan_id\": \"plan001\", \"wall_clock_seconds\": 10020.8, \"gpu_hours\": 2.78}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:13:08.926Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:13:12.957272+00:00\"}]}, \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r4\", \"log_path\": \"/root/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log\", \"conclusion\": \"negative\", \"notes\": \"训练 PR(last100)=0.883 但 eval PR=14% (sampling, T=0.7), ISR=0。87% 样本 hit max_new_tokens 生成不可解析长输出。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。exec-only reward landscape 存在极大方差。⚠️ 评估方法：sampling eval (T=0.7)，其他组用 eval_sta.py full STA。D029 决策：不重训，论文标注方法差异。PR=14% 是 failure case，eval 方法不影响结论。\", \"completed_at\": \"2026-05-14T04:27:38.542Z\"}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-14T05:33:25.603Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\", \"plan_id\": \"plan017\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"beta\": 0.3}, \"pid\": \"207116\", \"log_path\": \"~/runs/solver-trace-ablation/plan017-additive-random-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"finished_at\": \"2026-05-14T05:17:13.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:17:18.376399+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan017_additive_random_s42\", \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"eval_isr_pr_ratio\": 0.0943, \"eval_elapsed_s\": 542.3, \"eval_by_type_false_pr\": 0.32, \"eval_by_type_false_isr\": 0.0254, \"eval_by_type_unknown_pr\": 0.51, \"eval_by_type_unknown_isr\": 0.0518, \"eval_by_type_true_pr\": 0.56, \"eval_by_type_true_isr\": 0.052, \"tautological_collapse\": false}, \"completed_at\": \"2026-05-14T05:30:46.783Z\"}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T03:43:37.925Z\", \"updated_at\": \"2026-05-14T04:29:48.645Z\", \"hypothesis\": \"Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T03:49:52.891Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_downstream.py --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/plan014_downstream_nli.json --num_generations 8 --workers 4\\\"\", \"finished_at\": \"2026-05-14T04:26:05.334Z\", \"training_hours\": 0.6}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-14T03:51:18.427Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:51:19.514390+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:26:06.788787+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"r1 失败: checkpoint_path 多了 /checkpoint-500。save_total_limit=1 导致模型直接保存在 plan001_exec_only_s42/ 根目录。修正路径为 /root/autodl-tmp/outputs/plan001_exec_only_s42 即可。等 s43 re-eval 完成后重跑。\"}}, \"notes\": \"Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_downstream.py --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/plan014_downstream_nli.json --num_generations 8 --workers 4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"216133\", \"log_path\": \"~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log\", \"submitted_at\": \"2026-05-14T04:17:30.763Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 737.9, \"gpu_hours\": 0.2}, \"pid\": \"216133\", \"log_path\": \"~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan014_downstream_nli.json\"}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T04:27:38.822Z\", \"spec\": {\"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\", \"plan_id\": \"plan_002\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_beta03_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"161819\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:24:44.110Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:24:48.666027+00:00\"}]}, \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 1.0927}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_beta03_s42\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b03-s42.log\", \"notes\": \"ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。\", \"conclusion\": \"negative\", \"eval_prove_rate\": 0.18, \"eval_mean_isr\": 0.0257, \"eval_isr_std\": 0.0742, \"eval_proved_only_isr\": 0.1427, \"eval_median_isr\": 0, \"eval_isr_pr_ratio\": 0.1427, \"completed_at\": \"2026-05-14T04:27:38.822Z\"}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:40:35.587Z\", \"updated_at\": \"2026-05-14T03:45:53.344Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"136261\", \"log_path\": \"~/runs/solver-trace-ablation/plan013-random-reward-s42-r4.log\", \"submitted_at\": \"2026-05-14T01:40:35.528Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline: replacing ISR with random values should degrade structural quality while maintaining execution reward, proving ISR's causal contribution\", \"plan_id\": \"plan013\", \"wall_clock_seconds\": 2492.4, \"gpu_hours\": 0.69}, \"reproduce\": {\"finished_at\": \"2026-05-14T02:19:57.306Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:19:58.514969+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r4/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r4/reward_log.jsonl\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}, \"completed_at\": \"2026-05-14T02:22:07.933Z\", \"notes\": \"⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。\"}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:02:31.830Z\", \"updated_at\": \"2026-05-14T01:41:28.427Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"133258\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500 steps seed 43 (r3), 3-seed baseline 2nd seed\", \"plan_id\": \"plan_001\"}, \"conclusion\": \"failed\", \"failure_reason\": \"OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 23\", \"checkpoint_path\": \"N/A (disk full crash at step 23)\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r3/reward_log.jsonl\", \"completed_at\": \"2026-05-14T01:41:28.427Z\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:02:30.063Z\", \"updated_at\": \"2026-05-14T01:41:28.122Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"133178\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline (r3): random value replaces ISR to isolate ISR-specific signal vs multi-objective regularization\", \"plan_id\": \"plan_013\", \"hyperparams\": {\"alpha\": 0.9, \"beta\": 0.1, \"K\": 8, \"num_steps\": 500, \"reward_type\": \"random_penalty\"}}, \"conclusion\": \"failed\", \"failure_reason\": \"OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 28\", \"checkpoint_path\": \"N/A (disk full crash at step 28)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r3/reward_log.jsonl\", \"completed_at\": \"2026-05-14T01:41:28.122Z\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:22:12.292Z\", \"updated_at\": \"2026-05-14T01:01:56.416Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"126541\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-r2.log\", \"submitted_at\": \"2026-05-14T00:22:12.241Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500步 seed 43 (retry), 3-seed baseline 第2个 seed\", \"wall_clock_seconds\": 2384.2, \"gpu_hours\": 0.66}, \"checkpoint_path\": \"N/A (crashed after submission)\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r2/reward_log.jsonl\", \"conclusion\": \"failed\", \"failure_reason\": \"Process crashed after submission (PID 126546 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.\", \"completed_at\": \"2026-05-14T01:01:56.416Z\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:22:10.140Z\", \"updated_at\": \"2026-05-14T01:01:55.694Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"126461\", \"log_path\": \"~/runs/solver-trace-ablation/plan013-random-reward-s42-r2.log\", \"submitted_at\": \"2026-05-14T00:22:10.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline (retry): 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\", \"wall_clock_seconds\": 2385.6, \"gpu_hours\": 0.66}, \"checkpoint_path\": \"N/A (crashed after submission)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r2/reward_log.jsonl\", \"conclusion\": \"failed\", \"failure_reason\": \"Process crashed after submission (PID 126466 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.\", \"completed_at\": \"2026-05-14T01:01:55.694Z\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:56:44.062Z\", \"updated_at\": \"2026-05-14T00:21:05.430Z\", \"spec\": {\"hypothesis\": \"Random reward baseline: 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1\\\"\", \"server\": \"westd-39279\", \"data_path\": \"data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan_013\", \"gpu\": \"cuda:0\", \"hyperparams\": {\"alpha\": 0.9, \"beta\": 0.1, \"K\": 8, \"num_steps\": 500, \"reward_type\": \"random_penalty\"}, \"pid\": 122796, \"output_dir\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42\", \"reward_mode\": \"random_reward\", \"exec_weight\": 0.9, \"sta_weight\": 0.1, \"num_steps\": 500}, \"checkpoint_path\": \"N/A (GPU overflow, no valid output)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42.log\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA_VISIBLE_DEVICES not set (inline assignment not exported), GPU overflow to both GPUs\", \"completed_at\": \"2026-05-14T00:21:05.430Z\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:55:08.635Z\", \"updated_at\": \"2026-05-14T00:21:04.003Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"121275\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43.log\", \"submitted_at\": \"2026-05-13T23:55:08.544Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500步 seed 43, 3-seed baseline 第2个 seed。预期 prove_rate>0.80 (与 s42 一致)\", \"wall_clock_seconds\": 1555.5, \"gpu_hours\": 0.43}, \"checkpoint_path\": \"N/A (killed by OOM before completion)\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43.log\", \"conclusion\": \"failed\", \"failure_reason\": \"OOM by plan013 GPU overflow — plan013 未设 CUDA_VISIBLE_DEVICES 导致占用两张 GPU，plan001-s43 被 OOM kill\", \"completed_at\": \"2026-05-14T00:21:04.003Z\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:19:41.568Z\", \"updated_at\": \"2026-05-13T23:03:42.892Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"83029\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42.log\", \"submitted_at\": \"2026-05-13T22:20:46.569Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"exec-only 500步训练 baseline\", \"wall_clock_seconds\": 2576.3, \"gpu_hours\": 0.72}, \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A (failed before checkpoint)\", \"completed_at\": \"2026-05-13T23:03:42.892Z\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:21:48.691Z\", \"updated_at\": \"2026-05-13T23:03:19.945Z\", \"spec\": {\"command\": \"eval_sta.py on r5 exec-only checkpoint\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"83690\", \"log_path\": \"~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log\", \"submitted_at\": \"2026-05-13T22:21:48.658Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"model_name\": \"Qwen3-4B (r5 exec-only checkpoint)\", \"seed\": 0, \"checkpoint_source\": \"sta-phase1-exec-only-r5\", \"eval_data\": \"proofwriter_fol_100\", \"hypothesis\": \"Full STA eval on exec-only 100-step checkpoint to measure formalization quality\", \"wall_clock_seconds\": 2490.2, \"gpu_hours\": 0.69}, \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json\", \"log_path\": \"~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log\", \"completed_at\": \"2026-05-13T23:03:18.848Z\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:42:40.242Z\", \"updated_at\": \"2026-05-13T23:03:11.395Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"85710\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r3.log\", \"submitted_at\": \"2026-05-13T22:42:40.204Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"exec-only 500步训练 baseline (retry 3)\", \"wall_clock_seconds\": 1228.1, \"gpu_hours\": 0.34}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:03:08.298Z\", \"failure_reason\": \"OOM crash - duplicate submission while plan001-r2 was occupying cuda:0\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:54:31.353Z\", \"updated_at\": \"2026-05-13T22:20:41.274Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"75968\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r5.log\", \"submitted_at\": \"2026-05-13T20:54:38.781Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Full STA continuous ISR (0.0-1.0) 作为 reward 组件，应在训练中产生与 execution-only 不同的 ISR 趋势——execution-only ISR 随 prove_rate 上升而虚高(reward hacking)，execution+STA ISR 维持真实水平(STA 抑制 hacking)\", \"wall_clock_seconds\": 3506.3, \"gpu_hours\": 0.97}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/\", \"log_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/reward_log.jsonl\", \"completed_at\": \"2026-05-13T21:53:05.068Z\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:54:27.505Z\", \"updated_at\": \"2026-05-13T21:53:04.486Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"75890\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r5.log\", \"submitted_at\": \"2026-05-13T20:54:37.293Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"K=8 增加 within-group variance，减少全零 reward batch，使 GRPO 有更多有效梯度信号\", \"wall_clock_seconds\": 3507.2, \"gpu_hours\": 0.97}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/\", \"log_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/reward_log.jsonl\", \"completed_at\": \"2026-05-13T21:53:04.486Z\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:28:22.778Z\", \"updated_at\": \"2026-05-13T20:52:58.761Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"70797\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r4.log\", \"submitted_at\": \"2026-05-13T20:28:32.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1404.7, \"gpu_hours\": 0.39}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T20:28:31.240Z\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T20:45:55.480Z\", \"training_hours\": 0.29}, \"pid\": \"70797\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:45:56.962544+00:00\"}]}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T20:51:56.799Z\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:28:18.040Z\", \"updated_at\": \"2026-05-13T20:52:56.416Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"70716\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r4.log\", \"submitted_at\": \"2026-05-13T20:28:30.420Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1405.8, \"gpu_hours\": 0.39}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:28:28.733Z\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T20:45:53.506Z\", \"training_hours\": 0.29}, \"pid\": \"70716\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:45:54.294365+00:00\"}]}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T20:51:56.183Z\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:04.067Z\", \"updated_at\": \"2026-05-13T20:23:15.460Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"67225\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r3.log\", \"submitted_at\": \"2026-05-13T20:15:15.911Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 276.4, \"gpu_hours\": 0.08}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:15:14.333Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T20:19:51.612Z\", \"training_hours\": 0.08}, \"pid\": \"67225\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r3.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:19:52.268Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:19:52.981720+00:00\"}]}, \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:08.133Z\", \"updated_at\": \"2026-05-13T20:23:14.516Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"67306\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r3.log\", \"submitted_at\": \"2026-05-13T20:15:17.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 277.9, \"gpu_hours\": 0.08}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T20:15:16.704Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T20:19:54.409Z\", \"training_hours\": 0.08}, \"pid\": \"67306\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r3.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:19:55.400Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:19:56.549926+00:00\"}]}, \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:55:08.640Z\", \"updated_at\": \"2026-05-13T19:55:41.544Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"62364\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r2.log\", \"submitted_at\": \"2026-05-13T19:55:19.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 22.5, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T19:55:18.267Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T19:55:40.449Z\", \"training_hours\": 0.01}, \"pid\": \"62364\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:55:41.544Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:42.974865+00:00\"}]}}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:55:04.711Z\", \"updated_at\": \"2026-05-13T19:55:37.426Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"62283\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r2.log\", \"submitted_at\": \"2026-05-13T19:55:17.509Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19.9, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:55:16.037Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T19:55:36.845Z\", \"training_hours\": 0.01}, \"pid\": \"62283\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:55:37.426Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:38.155358+00:00\"}]}}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:53.258Z\", \"updated_at\": \"2026-05-13T19:33:03.905Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"59574\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta.log\", \"submitted_at\": \"2026-05-13T19:32:47.783Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 16.1, \"gpu_hours\": 0.0}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T19:30:58.981Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T19:33:03.170Z\", \"training_hours\": 0.03}, \"pid\": \"59574\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:33:03.905Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:33:05.009356+00:00\"}]}}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:46.351Z\", \"updated_at\": \"2026-05-13T19:33:01.169Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"59274\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only.log\", \"submitted_at\": \"2026-05-13T19:32:30.340Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 30.8, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:32:28.753Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T19:33:00.602Z\", \"training_hours\": 0.01}, \"pid\": \"59274\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:33:01.169Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:33:01.864437+00:00\"}]}}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:11:13.283Z\", \"updated_at\": \"2026-05-13T18:12:44.147Z\", \"spec\": {\"command\": \"python3 scripts/gt_isr_baseline.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"model_name\": \"ground-truth-fol\", \"seed\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/solver-trace-ablation/outputs/gt_isr_baseline.json\", \"log_path\": \"/root/solver-trace-ablation/outputs/gt_isr_baseline.json\", \"completed_at\": \"2026-05-13T18:12:43.141Z\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:51:48.853Z\", \"updated_at\": \"2026-05-13T18:10:40.982Z\", \"spec\": {\"hypothesis\": \"锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）\", \"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"server\": \"westd-39279\", \"data_source\": \"tasksource/folio\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 scripts/phase0_baseline.py --model_path models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output outputs/phase0_baseline.json\", \"seed\": 0, \"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"/root/solver-trace-ablation/outputs/phase0_baseline.json\", \"notes\": \"conclusion=success 但语义是 baseline_anchored（registry 不支持自定义 conclusion）。此实验是 baseline 锚定，非传统 success/failure。ISR 盲区：premise-conclusion 重复的 trivial formalization 可能获高 ISR，论文 Discussion 需讨论。\"}, \"log_path\": \"/tmp/phase0_baseline.log\", \"checkpoint_path\": \"/root/solver-trace-ablation/outputs/phase0_baseline.json\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T18:04:56.962Z\"}}, \"count\": 50, \"total\": 50, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2367}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01Tx5KMiH8VUrRrZrdFaqxJd`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "066095b9-2a1d-415d-8417-24f95eb6fee6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CAmTrNUBmiVPqdrbk1vzN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 26314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
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

_source line 13 · 2026-05-14T18:50:30.400Z_

<details><summary>↩ Tool result · `toolu_01Tx5KMiH8VUrRrZrdFaqxJd`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "5c0d790b-5bef-4ede-ba5d-49cd1535961e",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 20,
    "numFiles": 0,
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
I have the paper_framing.md data which contains all the experimental data I need. The registry is too large but I don't need it - the paper_framing.md and the user's prompt contain all the data points. Let me also check for existing paper files and references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "204c42b3-286f-4b8b-8cdb-f91c666f357f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lwud8i6w9NkzdXLhuysULS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10340,
      "cache_read_input_tokens": 27166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10340
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

Let me check for existing paper structure and references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "55999b60-45d3-4561-b06d-8805c301276c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lwud8i6w9NkzdXLhuysULS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10340,
      "cache_read_input_tokens": 27166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10340
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

<details open><summary>🔧 Tool call — Glob · `toolu_01LHiVpre42nAZwNE1SZTVfB`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/**/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "4af809c7-69fb-44ed-a30e-b7422fc35fe8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lwud8i6w9NkzdXLhuysULS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10340,
      "cache_read_input_tokens": 27166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10340
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

_source line 17 · 2026-05-14T18:50:38.455Z_

<details><summary>↩ Tool result · `toolu_01LHiVpre42nAZwNE1SZTVfB`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "9664713b-fd71-4c31-84e1-9b1c46b50fdf",
  "tool_use_result": {
    "filenames": [
      "paper/references.bib"
    ],
    "durationMs": 23,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012TU2sNcHHgNGSQYr2rq1J7`</summary>

```json
{
  "project": "solver-trace-ablation",
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
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "e0c5d475-bb4a-4d41-abb5-f995c5ac70ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lwud8i6w9NkzdXLhuysULS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10340,
      "cache_read_input_tokens": 27166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10340
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

_source line 19 · 2026-05-14T18:50:38.955Z_

<details><summary>↩ Tool result · `toolu_012TU2sNcHHgNGSQYr2rq1J7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026\\n  track: main\\n  template: acl2023/\\n  template_note: \\\"ARR May 25 cycle. ACL Rolling Review format (acl2023.sty).\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  core_claim: >\\n    ISR (Intensional Structural Reward), derived via Solver Trace Ablation,\\n    serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers\\n    but fails as a training signal due to meta-level Goodhart's Law — the diagnostic\\n    metric becomes gamed when optimized, with apparent improvements explained by\\n    premise minimization artifacts.\\n  created_at: 2026-05-14T18:00:00Z\\n  updated_at: 2026-05-14T19:00:00Z\\n  update_note: \\\"Director approved. Tab3 merged into Fig2; Tab6 moved to appendix. 4 fig + 4 table in main.\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    core_bullets:\\n      - \\\"Problem: GRPO formalizers achieve high prove rates but produce structurally degenerate outputs; no diagnostic exists\\\"\\n      - \\\"Method: STA derives ISR via leave-one-out component necessity testing on solver inputs\\\"\\n      - \\\"Claim 1: ISR detects hacking invisible to prove_rate (0.64→0.13→0.003 collapse over 100→500→1000 steps)\\\"\\n      - \\\"Claim 2: ISR-as-reward exhibits meta-level Goodhart — β=0.1 induces ISR-specific gaming (H7=64.5% vs 0% random), premise-matched 1.06x; β=0.3 PR collapses (18% vs 48% random)\\\"\\n      - \\\"Claim 3: ISR diagnostic transfers to Prolog (cross-logic generality)\\\"\\n      - \\\"Taxonomy: 6 distinct hacking modes identified across conditions\\\"\\n    dependencies: [experiments, method, discussion]\\n    tables: []\\n    figures: []\\n    registry_refs: []\\n\\n  - section: introduction\\n    word_budget: 1200\\n    core_bullets:\\n      - \\\"Hook: A GRPO formalizer achieves 93% prove rate — but 87% of its proved outputs embed the conclusion in the premises. Structural shortcuts invisible to execution reward.\\\"\\n      - \\\"Gap: Execution-only evaluation (prove_rate) conflates genuine reasoning with degenerate shortcuts. No principled diagnostic exists for structural integrity in neurosymbolic GRPO.\\\"\\n      - \\\"Insight: Component necessity testing (LOO ablation on solver inputs) yields ISR — AND when this diagnostic becomes reward, it exhibits meta-level Goodhart: the model games the metric itself.\\\"\\n      - \\\"Mechanism: STA protocol + systematic study across 6 reward conditions × 3 seeds × up to 1000 steps\\\"\\n      - \\\"Contributions: (C1) ISR as diagnostic with complete collapse trajectory; (C2) Meta-level Goodhart empirical characterization with premise-count confound analysis; (C3) Cross-logic diagnostic transfer; (C4) 6-mode hacking taxonomy\\\"\\n    dependencies: [experiments]\\n    citation_hints:\\n      - \\\"GRPO: deepseekmath\\\"\\n      - \\\"Neurosymbolic: satlm, logic-lm, linc\\\"\\n      - \\\"Reward hacking: gao-reward-overoptimization, karwowski-goodhart-rl\\\"\\n      - \\\"Goodhart taxonomy: manheim-goodhart-taxonomy\\\"\\n    figures: [fig1_sta_overview]\\n    tables: []\\n    registry_refs: []\\n\\n  - section: related_work\\n    word_budget: 900\\n    core_bullets:\\n      - \\\"Cluster 1 — Neurosymbolic Reasoning with LLMs: Logic-LM, LINC, SatLM, LoRP, FoVer pipeline approach (prompting); Mellgren Prolog GRPO (RL). STA differs: structural reward + diagnostic focus\\\"\\n      - \\\"Cluster 2 — Reward Shaping & Process Supervision: Lightman verify-step, Math-Shepherd, RLSF symbolic feedback, Rubric-GRPO. STA's ISR is solver-grounded process signal; our finding: process reward can itself Goodhart\\\"\\n      - \\\"Cluster 3 — Reward Hacking & Goodhart's Law: Gao scaling laws, Karwowski geometric, Manheim taxonomy, Skalse characterization, Pan misspecification. We contribute empirical Goodhart in formal reasoning + meta-level (proxy games itself)\\\"\\n      - \\\"Cluster 4 — Mutation Testing & Component Analysis: DeMillo 1978, Jia-Harman survey, Just mutants. STA adapts LOO mutation from SE to formal logic\\\"\\n    dependencies: [introduction]\\n    citation_hints:\\n      - \\\"Must cite: deepseekmath, logic-lm, linc, satlm, mellgren-prolog-grpo\\\"\\n      - \\\"Must cite: lightman-verify-step, gao-reward-overoptimization, karwowski-goodhart-rl, manheim-goodhart-taxonomy\\\"\\n      - \\\"Must cite: demillo1978, folio, proofwriter\\\"\\n    figures: []\\n    tables: []\\n    registry_refs: []\\n\\n  - section: method\\n    word_budget: 1200\\n    core_bullets:\\n      - \\\"3.1 Task: NL → Formal Logic formalization, verified by external solver (Prover9 for FOL, SWI-Prolog for Prolog)\\\"\\n      - \\\"3.2 GRPO Training: execution-only reward r_exec ∈ {0,1}, group relative policy optimization\\\"\\n      - \\\"3.3 Solver Trace Ablation (STA): LOO ablation protocol — for proved sample with n components, remove each component, re-run solver, ISR = fraction of components whose removal causes proof failure\\\"\\n      - \\\"3.4 ISR Definition: ISR(x) = (1/n) Σ_i 1[solver fails on x\\\\\\\\{c_i}], bounded [0,1]. ISR=1 → all necessary; ISR=0 → none necessary\\\"\\n      - \\\"3.5 Reward Formulations: exec-only, additive ISR (r_exec·(1+β·ISR)), additive random control, convex combination, SFT baseline\\\"\\n      - \\\"3.6 Hacking Taxonomy: H1 (multi-premise conclusion embedding), H7 (single premise = conclusion), H3 (complexity-without-utility), tautological collapse, repetition collapse, contradiction explosion\\\"\\n    dependencies: []\\n    notation_table:\\n      r_exec: \\\"binary execution reward (solver success)\\\"\\n      ISR: \\\"Intensional Structural Reward\\\"\\n      beta: \\\"ISR reward weight\\\"\\n      n: \\\"number of components in formalization\\\"\\n      c_i: \\\"i-th component (premise/rule)\\\"\\n      H1: \\\"multi-premise conclusion embedding\\\"\\n      H7: \\\"single premise = conclusion\\\"\\n    figures: [fig1_sta_overview]\\n    tables: []\\n    registry_refs: [sta-phase0-baseline, plan003-eval-exec-only-r5]\\n\\n  - section: experiments\\n    word_budget: 2800\\n    core_bullets:\\n      - \\\"4.1 Setup: Qwen3-4B, GRPO (K=8, 500 steps default), ProofWriter-FOL-100 eval, Prover9/SWI-Prolog solvers, 3 seeds (42/43/44)\\\"\\n      - \\\"4.2 ISR as Diagnostic (Claim 1): ISR collapse trajectory 0.6423→0.1324→0.0027 over 100→500→1000 steps (Fig2 with embedded data); PR rises 32%→93%→96%; 3-seed exec-only divergence (s42 genuine→H1, s43 degraded PR=14%, s44 tautological 2-comp); SFT baseline 92.9% genuine confirms RL-specificity\\\"\\n      - \\\"4.3 Meta-Level Goodhart (Claim 2): β=0.1 ISR — H7=64.5% ISR-specific gaming vs 0% random; premise-count-matched 1.06x (no real advantage); β=0.3 — PR collapse 18% vs 48% random; conclusion embedding is GRPO-universal (68-100%); ISR restructures hacking, doesn't reduce it\\\"\\n      - \\\"4.4 Cross-Logic Transfer (Claim 3): Prolog exec-only 3-seed ISR<0.1 across all seeds; Prolog STA s42 100% H7; diagnostic generalizes regardless of training outcome\\\"\\n      - \\\"4.5 Hacking Taxonomy: 6 modes quantified across conditions; reward type determines hacking composition not prevalence\\\"\\n    dependencies: []\\n    registry_refs:\\n      - sta-phase0-baseline\\n      - plan003-eval-exec-only-r5\\n      - plan001-exec-only-s42-r2\\n      - plan001-exec-only-s43-r4\\n      - plan001-exec-only-s44\\n      - plan016-extended-1000-s42\\n      - plan002-additive-b01-s42\\n      - plan002-additive-b01-s43\\n      - plan002-additive-b01-s44\\n      - plan018-additive-random-b01-s42\\n      - plan018-additive-random-b01-s43-r2\\n      - plan018-additive-random-b01-s44\\n      - plan002-additive-b03-s42\\n      - plan017-additive-random-s42\\n      - plan005-sta-low-s42\\n      - plan013-random-reward-s42-r4\\n      - plan009-sft-baseline-s42-r4\\n      - plan006-prolog-exec-s42\\n      - plan006-prolog-exec-s43-r3\\n      - plan006-prolog-exec-s44\\n      - plan006-prolog-sta-s42\\n    tables: [tab1_goodhart_landscape, tab2_hacking_taxonomy, tab4_beta01_3seed, tab5_prolog_crosslogic]\\n    figures: [fig2_isr_collapse, fig3_hacking_composition, fig4_prolog_comparison]\\n\\n  - section: discussion\\n    word_budget: 600\\n    core_bullets:\\n      - \\\"ISR measures syntactic component necessity, not semantic faithfulness (plan014 ρ=-0.049 n.s.)\\\"\\n      - \\\"Premise count confound: LOO metrics mathematically biased — fewer premises → higher ISR regardless of quality (D051)\\\"\\n      - \\\"Practical implications: ISR for post-hoc diagnosis only; never trust prove_rate alone; single-seed GRPO unreliable; proxy-as-reward cautionary tale\\\"\\n      - \\\"Meta-level Goodhart as general warning for any proxy-metric-as-reward approach\\\"\\n    dependencies: [experiments]\\n    tables: []\\n    figures: []\\n    registry_refs: [plan014-downstream-nli-s42]\\n\\n  - section: conclusion\\n    word_budget: 300\\n    core_bullets:\\n      - \\\"Summary: STA/ISR as diagnostic detects reward hacking invisible to prove_rate; ISR-as-reward exhibits meta-level Goodhart at all doses\\\"\\n      - \\\"Limitations: single base model (Qwen3-4B); ProofWriter data only; ISR = syntactic not semantic; 3 seeds; Claim 3 Prolog STA partial\\\"\\n      - \\\"Future: ISR + semantic verification; adaptive reward weighting; broader logic types; scale to larger models\\\"\\n    dependencies: [experiments, discussion]\\n    tables: []\\n    figures: []\\n    registry_refs: []\\n\\n  - section: appendix\\n    word_budget: 1000\\n    core_bullets:\\n      - \\\"Table A1: Experimental setup and hyperparameters (moved from Tab6)\\\"\\n      - \\\"Full hacking taxonomy definitions and examples\\\"\\n      - \\\"Per-seed detailed results\\\"\\n    dependencies: [experiments]\\n    tables: [tab6_setup]\\n    figures: []\\n    registry_refs: []\\n\\nvisualization_plan:\\n  - fig_id: fig1_sta_overview\\n    type: conceptual\\n    tool: matplotlib\\n    description: >\\n      STA protocol overview: (a) NL input → LLM formalizer → formal logic → solver → prove/fail.\\n      (b) STA ablation: remove each component, re-run solver, compute ISR.\\n      (c) ISR as diagnostic vs ISR as reward (Goodhart arrow).\\n      3-panel horizontal layout.\\n    placement: method\\n    aspect_ratio: \\\"3:1\\\"\\n    data_source: \\\"manual\\\"\\n\\n  - fig_id: fig2_isr_collapse\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      ISR collapse trajectory over training steps with embedded data annotations.\\n      X-axis: training steps (100, 500, 1000). Dual y-axis: PR (left, rising 32%→93%→96%)\\n      and ISR (right, falling 0.64→0.13→0.003). Include component count trend (6.58→18.55)\\n      as bubble size or secondary annotation. Annotate: ISR=0 ratio at 1000 steps (94.8%).\\n      Replaces former Tab3 — all collapse data embedded in figure annotations.\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n    data_source: \\\"registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\\\"\\n\\n  - fig_id: fig3_hacking_composition\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Stacked bar chart: hacking mode composition across conditions.\\n      X-axis: Exec-only s42, ISR β=0.1 s42/s43/s44, Random β=0.1 (3-seed mean), SFT.\\n      Stacked segments: H7 (red), H1 (orange), H3 (yellow), Genuine (green).\\n      Shows ISR restructures hacking (H1→H7) rather than reducing it.\\n    placement: experiments\\n    aspect_ratio: \\\"16:9\\\"\\n    data_source: \\\"registry: plan001-exec-only-s42-r2, plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42, plan018-additive-random-b01-s43-r2, plan018-additive-random-b01-s44, plan009-sft-baseline-s42-r4\\\"\\n\\n  - fig_id: fig4_prolog_comparison\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Grouped bar chart: FOL vs Prolog exec-only ISR comparison (3 seeds each).\\n      X-axis: s42, s43, s44. Grouped bars: FOL ISR, Prolog ISR.\\n      Both near-zero, confirming cross-logic diagnostic transfer.\\n      Overlay PR values as text annotations.\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n    data_source: \\\"registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44, plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3, plan006-prolog-exec-s44\\\"\\n\\ntable_plan:\\n  - table_id: tab1_goodhart_landscape\\n    caption: \\\"Goodhart landscape: ISR-as-reward across dose and formulation. All eval on ProofWriter-FOL-100 via eval\\\\\\\\_sta.py.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Condition, Formula, β, Seed, PR↑, ISR↑, H7%, H1%, Genuine%, Mode]\\n    data_source: \\\"registry: sta-phase0-baseline, plan001-exec-only-s42-r2, plan009-sft-baseline-s42-r4, plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42, plan018-additive-random-b01-s43-r2, plan018-additive-random-b01-s44, plan002-additive-b03-s42, plan017-additive-random-s42, plan013-random-reward-s42-r4\\\"\\n    notes: \\\"Core table. Bold best genuine%. † marks tautological artifacts. * marks sampling eval.\\\"\\n\\n  - table_id: tab2_hacking_taxonomy\\n    caption: \\\"Hacking taxonomy: six distinct modes across reward conditions. Rates are % of proved samples (s42 seed).\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Mode, Description, \\\"Exec-only\\\", \\\"ISR β=0.1\\\", \\\"Random β=0.1\\\", \\\"SFT\\\"]\\n    data_source: \\\"registry: plan001-exec-only-s42-r2, plan002-additive-b01-s42, plan018-additive-random-b01-s42, plan009-sft-baseline-s42-r4, plan012-hacking-taxonomy\\\"\\n    notes: \\\"s42 comparison (cleanest seed). Include mode descriptions in table.\\\"\\n\\n  - table_id: tab4_beta01_3seed\\n    caption: \\\"ISR β=0.1 vs Random β=0.1: 3-seed comparison. H7 is ISR-specific (64.5% vs 0%). Premise-count-matched ISR: 1.06×.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Seed, Condition, PR, \\\"ISR (proved)\\\", H7%, H1%, Genuine%, \\\"Prem-matched ISR\\\"]\\n    data_source: \\\"registry: plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42, plan018-additive-random-b01-s43-r2, plan018-additive-random-b01-s44\\\"\\n    notes: \\\"Key table for Claim 2. Include 3-seed mean±std row. Premise-matched column only for s42.\\\"\\n\\n  - table_id: tab5_prolog_crosslogic\\n    caption: \\\"Cross-logic diagnostic transfer: Prolog results. ISR detects degeneration across logic types.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Logic, Condition, Seed, PR, ISR, \\\"Proved-only ISR\\\", H7%, Mode]\\n    data_source: \\\"registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3, plan006-prolog-exec-s44, plan006-prolog-sta-s42\\\"\\n    notes: \\\"Prolog STA s43/s44 RUNNING — [pending]. Include FOL exec-only for comparison.\\\"\\n\\n  - table_id: tab6_setup\\n    caption: \\\"Experimental setup and hyperparameters.\\\"\\n    placement: appendix\\n    type: configuration\\n    columns: [Parameter, Value]\\n    data_source: \\\"manual\\\"\\n    notes: \\\"APPENDIX. Base model, training data, K, steps, seeds, solvers, eval dataset.\\\"\\n\\nliterature_strategy:\\n  citation_budget: 40\\n  macro_context:\\n    - \\\"GRPO / RL for formal reasoning\\\"\\n    - \\\"reward hacking and Goodhart's Law in LLM training\\\"\\n    - \\\"neurosymbolic NL-to-logic formalization\\\"\\n    - \\\"mutation testing and component analysis\\\"\\n  micro_clusters:\\n    - cluster_name: neurosymbolic-rl\\n      search_queries:\\n        - \\\"GRPO reinforcement learning logical reasoning 2024 2025\\\"\\n        - \\\"neurosymbolic LLM formal logic prover\\\"\\n      must_cite:\\n        - \\\"deepseekmath (GRPO origin)\\\"\\n        - \\\"mellgren-prolog-grpo\\\"\\n        - \\\"logic-lm\\\"\\n        - \\\"linc\\\"\\n        - \\\"satlm\\\"\\n      target_count: 8\\n    - cluster_name: reward-shaping\\n      search_queries:\\n        - \\\"reward shaping process supervision LLM reasoning 2024 2025\\\"\\n        - \\\"process reward model overoptimization\\\"\\n      must_cite:\\n        - \\\"lightman-verify-step\\\"\\n        - \\\"gao-effective-rl-reward\\\"\\n        - \\\"rlsf\\\"\\n      target_count: 8\\n    - cluster_name: reward-hacking\\n      search_queries:\\n        - \\\"reward hacking overoptimization RLHF 2024 2025\\\"\\n        - \\\"specification gaming reinforcement learning\\\"\\n      must_cite:\\n        - \\\"gao-reward-overoptimization\\\"\\n        - \\\"skalse-reward-hacking\\\"\\n        - \\\"reward-hacking-survey\\\"\\n        - \\\"spurious-rewards\\\"\\n      target_count: 6\\n    - cluster_name: goodhart-overoptimization\\n      search_queries:\\n        - \\\"Goodhart's Law reinforcement learning proxy reward\\\"\\n        - \\\"reward model overoptimization scaling laws\\\"\\n      must_cite:\\n        - \\\"manheim-goodhart-taxonomy\\\"\\n        - \\\"karwowski-goodhart-rl\\\"\\n        - \\\"kwa-catastrophic-goodhart\\\"\\n        - \\\"pan-reward-misspecification\\\"\\n      target_count: 6\\n    - cluster_name: fol-formalization\\n      search_queries:\\n        - \\\"first-order logic formalization LLM 2024 2025\\\"\\n        - \\\"Prolog LLM reasoning\\\"\\n      must_cite:\\n        - \\\"folio\\\"\\n        - \\\"proofwriter\\\"\\n        - \\\"fover-pei2025\\\"\\n      target_count: 5\\n    - cluster_name: mutation-testing\\n      search_queries:\\n        - \\\"mutation testing component analysis software engineering\\\"\\n      must_cite:\\n        - \\\"demillo1978\\\"\\n        - \\\"jia-harman-survey\\\"\\n      target_count: 4\\n    - cluster_name: verification-reward\\n      search_queries:\\n        - \\\"solver prover reward signal RL training 2024 2025\\\"\\n        - \\\"formal verification LLM training\\\"\\n      must_cite:\\n        - \\\"deepseek-prover-v15\\\"\\n        - \\\"math-shepherd\\\"\\n      target_count: 4\\n\\nwriting_order:\\n  - experiments\\n  - method\\n  - introduction\\n  - related_work\\n  - discussion\\n  - abstract\\n  - conclusion\\n\", \"total_chars\": 16820, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "7cee5f1a-b9dc-400d-8615-a89d8e95a312",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/writing_plan.yaml\\\", \\\"content\\\": \\\"meta:\\\\n  venue: EMNLP 2026\\\\n  track: main\\\\n  template: acl2023/\\\\n  template_note: \\\\\\\"ARR May 25 cycle. ACL Rolling Review format (acl2023.sty).\\\\\\\"\\\\n  page_limit: 8\\\\n  deadline: 2026-05-25\\\\n  core_claim: >\\\\n    ISR (Intensional Structural Reward), derived via Solver Trace Ablation,\\\\n    serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers\\\\n    but fails as a training signal due to meta-level Goodhart's Law — the diagnostic\\\\n    metric becomes gamed when optimized, with apparent improvements explained by\\\\n    premise minimization artifacts.\\\\n  created_at: 2026-05-14T18:00:00Z\\\\n  updated_at: 2026-05-14T19:00:00Z\\\\n  update_note: \\\\\\\"Director approved. Tab3 merged into Fig2; Tab6 moved to appendix. 4 fig + 4 table in main.\\\\\\\"\\\\n\\\\npaper_outline:\\\\n  - section: abstract\\\\n    word_budget: 250\\\\n    core_bullets:\\\\n      - \\\\\\\"Problem: GRPO formalizers achieve high prove rates but produce structurally degenerate outputs; no diagnostic exists\\\\\\\"\\\\n      - \\\\\\\"Method: STA derives ISR via leave-one-out component necessity testing on solver inputs\\\\\\\"\\\\n      - \\\\\\\"Claim 1: ISR detects hacking invisible to prove_rate (0.64→0.13→0.003 collapse over 100→500→1000 steps)\\\\\\\"\\\\n      - \\\\\\\"Claim 2: ISR-as-reward exhibits meta-level Goodhart — β=0.1 induces ISR-specific gaming (H7=64.5% vs 0% random), premise-matched 1.06x; β=0.3 PR collapses (18% vs 48% random)\\\\\\\"\\\\n      - \\\\\\\"Claim 3: ISR diagnostic transfers to Prolog (cross-logic generality)\\\\\\\"\\\\n      - \\\\\\\"Taxonomy: 6 distinct hacking modes identified across conditions\\\\\\\"\\\\n    dependencies: [experiments, method, discussion]\\\\n    tables: []\\\\n    figures: []\\\\n    registry_refs: []\\\\n\\\\n  - section: introduction\\\\n    word_budget: 1200\\\\n    core_bullets:\\\\n      - \\\\\\\"Hook: A GRPO formalizer achieves 93% prove rate — but 87% of its proved outputs embed the conclusion in the premises. Structural shortcuts invisible to execution reward.\\\\\\\"\\\\n      - \\\\\\\"Gap: Execution-only evaluation (prove_rate) conflates genuine reasoning with degenerate shortcuts. No principled diagnostic exists for structural integrity in neurosymbolic GRPO.\\\\\\\"\\\\n      - \\\\\\\"Insight: Component necessity testing (LOO ablation on solver inputs) yields ISR — AND when this diagnostic becomes reward, it exhibits meta-level Goodhart: the model games the metric itself.\\\\\\\"\\\\n      - \\\\\\\"Mechanism: STA protocol + systematic study across 6 reward conditions × 3 seeds × up to 1000 steps\\\\\\\"\\\\n      - \\\\\\\"Contributions: (C1) ISR as diagnostic with complete collapse trajectory; (C2) Meta-level Goodhart empirical characterization with premise-count confound analysis; (C3) Cross-logic diagnostic transfer; (C4) 6-mode hacking taxonomy\\\\\\\"\\\\n    dependencies: [experiments]\\\\n    citation_hints:\\\\n      - \\\\\\\"GRPO: deepseekmath\\\\\\\"\\\\n      - \\\\\\\"Neurosymbolic: satlm, logic-lm, linc\\\\\\\"\\\\n      - \\\\\\\"Reward hacking: gao-reward-overoptimization, karwowski-goodhart-rl\\\\\\\"\\\\n      - \\\\\\\"Goodhart taxonomy: manheim-goodhart-taxonomy\\\\\\\"\\\\n    figures: [fig1_sta_overview]\\\\n    tables: []\\\\n    registry_refs: []\\\\n\\\\n  - section: related_work\\\\n    word_budget: 900\\\\n    core_bullets:\\\\n      - \\\\\\\"Cluster 1 — Neurosymbolic Reasoning with LLMs: Logic-LM, LINC, SatLM, LoRP, FoVer pipeline approach (prompting); Mellgren Prolog GRPO (RL). STA differs: structural reward + diagnostic focus\\\\\\\"\\\\n      - \\\\\\\"Cluster 2 — Reward Shaping & Process Supervision: Lightman verify-step, Math-Shepherd, RLSF symbolic feedback, Rubric-GRPO. STA's ISR is solver-grounded process signal; our finding: process reward can itself Goodhart\\\\\\\"\\\\n      - \\\\\\\"Cluster 3 — Reward Hacking & Goodhart's Law: Gao scaling laws, Karwowski geometric, Manheim taxonomy, Skalse characterization, Pan misspecification. We contribute empirical Goodhart in formal reasoning + meta-level (proxy games itself)\\\\\\\"\\\\n      - \\\\\\\"Cluster 4 — Mutation Testing & Component Analysis: DeMillo 1978, Jia-Harman survey, Just mutants. STA adapts LOO mutation from SE to formal logic\\\\\\\"\\\\n    dependencies: [introduction]\\\\n    citation_hints:\\\\n      - \\\\\\\"Must cite: deepseekmath, logic-lm, linc, satlm, mellgren-prolog-grpo\\\\\\\"\\\\n      - \\\\\\\"Must cite: lightman-verify-step, gao-reward-overoptimization, karwowski-goodhart-rl, manheim-goodhart-taxonomy\\\\\\\"\\\\n      - \\\\\\\"Must cite: demillo1978, folio, proofwriter\\\\\\\"\\\\n    figures: []\\\\n    tables: []\\\\n    registry_refs: []\\\\n\\\\n  - section: method\\\\n    word_budget: 1200\\\\n    core_bullets:\\\\n      - \\\\\\\"3.1 Task: NL → Formal Logic formalization, verified by external solver (Prover9 for FOL, SWI-Prolog for Prolog)\\\\\\\"\\\\n      - \\\\\\\"3.2 GRPO Training: execution-only reward r_exec ∈ {0,1}, group relative policy optimization\\\\\\\"\\\\n      - \\\\\\\"3.3 Solver Trace Ablation (STA): LOO ablation protocol — for proved sample with n components, remove each component, re-run solver, ISR = fraction of components whose removal causes proof failure\\\\\\\"\\\\n      - \\\\\\\"3.4 ISR Definition: ISR(x) = (1/n) Σ_i 1[solver fails on x\\\\\\\\\\\\\\\\{c_i}], bounded [0,1]. ISR=1 → all necessary; ISR=0 → none necessary\\\\\\\"\\\\n      - \\\\\\\"3.5 Reward Formulations: exec-only, additive ISR (r_exec·(1+β·ISR)), additive random control, convex combination, SFT baseline\\\\\\\"\\\\n      - \\\\\\\"3.6 Hacking Taxonomy: H1 (multi-premise conclusion embedding), H7 (single premise = conclusion), H3 (complexity-without-utility), tautological collapse, repetition collapse, contradiction explosion\\\\\\\"\\\\n    dependencies: []\\\\n    notation_table:\\\\n      r_exec: \\\\\\\"binary execution reward (solver success)\\\\\\\"\\\\n      ISR: \\\\\\\"Intensional Structural Reward\\\\\\\"\\\\n      beta: \\\\\\\"ISR reward weight\\\\\\\"\\\\n      n: \\\\\\\"number of components in formalization\\\\\\\"\\\\n      c_i: \\\\\\\"i-th component (premise/rule)\\\\\\\"\\\\n      H1: \\\\\\\"multi-premise conclusion embedding\\\\\\\"\\\\n      H7: \\\\\\\"single premise = conclusion\\\\\\\"\\\\n    figures: [fig1_sta_overview]\\\\n    tables: []\\\\n    registry_refs: [sta-phase0-baseline, plan003-eval-exec-only-r5]\\\\n\\\\n  - section: experiments\\\\n    word_budget: 2800\\\\n    core_bullets:\\\\n      - \\\\\\\"4.1 Setup: Qwen3-4B, GRPO (K=8, 500 steps default), ProofWriter-FOL-100 eval, Prover9/SWI-Prolog solvers, 3 seeds (42/43/44)\\\\\\\"\\\\n      - \\\\\\\"4.2 ISR as Diagnostic (Claim 1): ISR collapse trajectory 0.6423→0.1324→0.0027 over 100→500→1000 steps (Fig2 with embedded data); PR rises 32%→93%→96%; 3-seed exec-only divergence (s42 genuine→H1, s43 degraded PR=14%, s44 tautological 2-comp); SFT baseline 92.9% genuine confirms RL-specificity\\\\\\\"\\\\n      - \\\\\\\"4.3 Meta-Level Goodhart (Claim 2): β=0.1 ISR — H7=64.5% ISR-specific gaming vs 0% random; premise-count-matched 1.06x (no real advantage); β=0.3 — PR collapse 18% vs 48% random; conclusion embedding is GRPO-universal (68-100%); ISR restructures hacking, doesn't reduce it\\\\\\\"\\\\n      - \\\\\\\"4.4 Cross-Logic Transfer (Claim 3): Prolog exec-only 3-seed ISR<0.1 across all seeds; Prolog STA s42 100% H7; diagnostic generalizes regardless of training outcome\\\\\\\"\\\\n      - \\\\\\\"4.5 Hacking Taxonomy: 6 modes quantified across conditions; reward type determines hacking composition not prevalence\\\\\\\"\\\\n    dependencies: []\\\\n    registry_refs:\\\\n      - sta-phase0-baseline\\\\n      - plan003-eval-exec-only-r5\\\\n      - plan001-exec-only-s42-r2\\\\n      - plan001-exec-only-s43-r4\\\\n      - plan001-exec-only-s44\\\\n      - plan016-extended-1000-s42\\\\n      - plan002-additive-b01-s42\\\\n      - plan002-additive-b01-s43\\\\n      - plan002-additive-b01-s44\\\\n      - plan018-additive-random-b01-s42\\\\n      - plan018-additive-random-b01-s43-r2\\\\n      - plan018-additive-random-b01-s44\\\\n      - plan002-additive-b03-s42\\\\n      - plan017-additive-random-s42\\\\n      - plan005-sta-low-s42\\\\n      - plan013-random-reward-s42-r4\\\\n      - plan009-sft-baseline-s42-r4\\\\n      - plan006-prolog-exec-s42\\\\n      - plan006-prolog-exec-s43-r3\\\\n      - plan006-prolog-exec-s44\\\\n      - plan006-prolog-sta-s42\\\\n    tables: [tab1_goodhart_landscape, tab2_hacking_taxonomy, tab4_beta01_3seed, tab5_prolog_crosslogic]\\\\n    figures: [fig2_isr_collapse, fig3_hacking_composition, fig4_prolog_comparison]\\\\n\\\\n  - section: discussion\\\\n    word_budget: 600\\\\n    core_bullets:\\\\n      - \\\\\\\"ISR measures syntactic component necessity, not semantic faithfulness (plan014 ρ=-0.049 n.s.)\\\\\\\"\\\\n      - \\\\\\\"Premise count confound: LOO metrics mathematically biased — fewer premises → higher ISR regardless of quality (D051)\\\\\\\"\\\\n      - \\\\\\\"Practical implications: ISR for post-hoc diagnosis only; never trust prove_rate alone; single-seed GRPO unreliable; proxy-as-reward cautionary tale\\\\\\\"\\\\n      - \\\\\\\"Meta-level Goodhart as general warning for any proxy-metric-as-reward approach\\\\\\\"\\\\n    dependencies: [experiments]\\\\n    tables: []\\\\n    figures: []\\\\n    registry_refs: [plan014-downstream-nli-s42]\\\\n\\\\n  - section: conclusion\\\\n    word_budget: 300\\\\n    core_bullets:\\\\n      - \\\\\\\"Summary: STA/ISR as diagnostic detects reward hacking invisible to prove_rate; ISR-as-reward exhibits meta-level Goodhart at all doses\\\\\\\"\\\\n      - \\\\\\\"Limitations: single base model (Qwen3-4B); ProofWriter data only; ISR = syntactic not semantic; 3 seeds; Claim 3 Prolog STA partial\\\\\\\"\\\\n      - \\\\\\\"Future: ISR + semantic verification; adaptive reward weighting; broader logic types; scale to larger models\\\\\\\"\\\\n    dependencies: [experiments, discussion]\\\\n    tables: []\\\\n    figures: []\\\\n    registry_refs: []\\\\n\\\\n  - section: appendix\\\\n    word_budget: 1000\\\\n    core_bullets:\\\\n      - \\\\\\\"Table A1: Experimental setup and hyperparameters (moved from Tab6)\\\\\\\"\\\\n      - \\\\\\\"Full hacking taxonomy definitions and examples\\\\\\\"\\\\n      - \\\\\\\"Per-seed detailed results\\\\\\\"\\\\n    dependencies: [experiments]\\\\n    tables: [tab6_setup]\\\\n    figures: []\\\\n    registry_refs: []\\\\n\\\\nvisualization_plan:\\\\n  - fig_id: fig1_sta_overview\\\\n    type: conceptual\\\\n    tool: matplotlib\\\\n    description: >\\\\n      STA protocol overview: (a) NL input → LLM formalizer → formal logic → solver → prove/fail.\\\\n      (b) STA ablation: remove each component, re-run solver, compute ISR.\\\\n      (c) ISR as diagnostic vs ISR as reward (Goodhart arrow).\\\\n      3-panel horizontal layout.\\\\n    placement: method\\\\n    aspect_ratio: \\\\\\\"3:1\\\\\\\"\\\\n    data_source: \\\\\\\"manual\\\\\\\"\\\\n\\\\n  - fig_id: fig2_isr_collapse\\\\n    type: statistical\\\\n    tool: matplotlib\\\\n    description: >\\\\n      ISR collapse trajectory over training steps with embedded data annotations.\\\\n      X-axis: training steps (100, 500, 1000). Dual y-axis: PR (left, rising 32%→93%→96%)\\\\n      and ISR (right, falling 0.64→0.13→0.003). Include component count trend (6.58→18.55)\\\\n      as bubble size or secondary annotation. Annotate: ISR=0 ratio at 1000 steps (94.8%).\\\\n      Replaces former Tab3 — all collapse data embedded in figure annotations.\\\\n    placement: experiments\\\\n    aspect_ratio: \\\\\\\"4:3\\\\\\\"\\\\n    data_source: \\\\\\\"registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\\\\\\\"\\\\n\\\\n  - fig_id: fig3_hacking_composition\\\\n    type: statistical\\\\n    tool: matplotlib\\\\n    description: >\\\\n      Stacked bar chart: hacking mode composition across conditions.\\\\n      X-axis: Exec-only s42, ISR β=0.1 s42/s43/s44, Random β=0.1 (3-seed mean), SFT.\\\\n      Stacked segments: H7 (red), H1 (orange), H3 (yellow), Genuine (green).\\\\n      Shows ISR restructures hacking (H1→H7) rather than reducing it.\\\\n    placement: experiments\\\\n    aspect_ratio: \\\\\\\"16:9\\\\\\\"\\\\n    data_source: \\\\\\\"registry: plan001-exec-only-s42-r2, plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42, plan018-additive-random-b01-s43-r2, plan018-additive-random-b01-s44, plan009-sft-baseline-s42-r4\\\\\\\"\\\\n\\\\n  - fig_id: fig4_prolog_comparison\\\\n    type: statistical\\\\n    tool: matplotlib\\\\n    description: >\\\\n      Grouped bar chart: FOL vs Prolog exec-only ISR comparison (3 seeds each).\\\\n      X-axis: s42, s43, s44. Grouped bars: FOL ISR, Prolog ISR.\\\\n      Both near-zero, confirming cross-logic diagnostic transfer.\\\\n      Overlay PR values as text annotations.\\\\n    placement: experiments\\\\n    aspect_ratio: \\\\\\\"4:3\\\\\\\"\\\\n    data_source: \\\\\\\"registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44, plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3, plan006-prolog-exec-s44\\\\\\\"\\\\n\\\\ntable_plan:\\\\n  - table_id: tab1_goodhart_landscape\\\\n    caption: \\\\\\\"Goodhart landscape: ISR-as-reward across dose and formulation. All eval on ProofWriter-FOL-100 via eval\\\\\\\\\\\\\\\\_sta.py.\\\\\\\"\\\\n    placement: experiments\\\\n    type: comparison\\\\n    columns: [Condition, Formula, β, Seed, PR↑, ISR↑, H7%, H1%, Genuine%, Mode]\\\\n    data_source: \\\\\\\"registry: sta-phase0-baseline, plan001-exec-only-s42-r2, plan009-sft-baseline-s42-r4, plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42, plan018-additive-random-b01-s43-r2, plan018-additive-random-b01-s44, plan002-additive-b03-s42, plan017-additive-random-s42, plan013-random-reward-s42-r4\\\\\\\"\\\\n    notes: \\\\\\\"Core table. Bold best genuine%. † marks tautological artifacts. * marks sampling eval.\\\\\\\"\\\\n\\\\n  - table_id: tab2_hacking_taxonomy\\\\n    caption: \\\\\\\"Hacking taxonomy: six distinct modes across reward conditions. Rates are % of proved samples (s42 seed).\\\\\\\"\\\\n    placement: experiments\\\\n    type: comparison\\\\n    columns: [Mode, Description, \\\\\\\"Exec-only\\\\\\\", \\\\\\\"ISR β=0.1\\\\\\\", \\\\\\\"Random β=0.1\\\\\\\", \\\\\\\"SFT\\\\\\\"]\\\\n    data_source: \\\\\\\"registry: plan001-exec-only-s42-r2, plan002-additive-b01-s42, plan018-additive-random-b01-s42, plan009-sft-baseline-s42-r4, plan012-hacking-taxonomy\\\\\\\"\\\\n    notes: \\\\\\\"s42 comparison (cleanest seed). Include mode descriptions in table.\\\\\\\"\\\\n\\\\n  - table_id: tab4_beta01_3seed\\\\n    caption: \\\\\\\"ISR β=0.1 vs Random β=0.1: 3-seed comparison. H7 is ISR-specific (64.5% vs 0%). Premise-count-matched ISR: 1.06×.\\\\\\\"\\\\n    placement: experiments\\\\n    type: comparison\\\\n    columns: [Seed, Condition, PR, \\\\\\\"ISR (proved)\\\\\\\", H7%, H1%, Genuine%, \\\\\\\"Prem-matched ISR\\\\\\\"]\\\\n    data_source: \\\\\\\"registry: plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42, plan018-additive-random-b01-s43-r2, plan018-additive-random-b01-s44\\\\\\\"\\\\n    notes: \\\\\\\"Key table for Claim 2. Include 3-seed mean±std row. Premise-matched column only for s42.\\\\\\\"\\\\n\\\\n  - table_id: tab5_prolog_crosslogic\\\\n    caption: \\\\\\\"Cross-logic diagnostic transfer: Prolog results. ISR detects degeneration across logic types.\\\\\\\"\\\\n    placement: experiments\\\\n    type: comparison\\\\n    columns: [Logic, Condition, Seed, PR, ISR, \\\\\\\"Proved-only ISR\\\\\\\", H7%, Mode]\\\\n    data_source: \\\\\\\"registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3, plan006-prolog-exec-s44, plan006-prolog-sta-s42\\\\\\\"\\\\n    notes: \\\\\\\"Prolog STA s43/s44 RUNNING — [pending]. Include FOL exec-only for comparison.\\\\\\\"\\\\n\\\\n  - table_id: tab6_setup\\\\n    caption: \\\\\\\"Experimental setup and hyperparameters.\\\\\\\"\\\\n    placement: appendix\\\\n    type: configuration\\\\n    columns: [Parameter, Value]\\\\n    data_source: \\\\\\\"manual\\\\\\\"\\\\n    notes: \\\\\\\"APPENDIX. Base model, training data, K, steps, seeds, solvers, eval dataset.\\\\\\\"\\\\n\\\\nliterature_strategy:\\\\n  citation_budget: 40\\\\n  macro_context:\\\\n    - \\\\\\\"GRPO / RL for formal reasoning\\\\\\\"\\\\n    - \\\\\\\"reward hacking and Goodhart's Law in LLM training\\\\\\\"\\\\n    - \\\\\\\"neurosymbolic NL-to-logic formalization\\\\\\\"\\\\n    - \\\\\\\"mutation testing and component analysis\\\\\\\"\\\\n  micro_clusters:\\\\n    - cluster_name: neurosymbolic-rl\\\\n      search_queries:\\\\n        - \\\\\\\"GRPO reinforcement learning logical reasoning 2024 2025\\\\\\\"\\\\n        - \\\\\\\"neurosymbolic LLM formal logic prover\\\\\\\"\\\\n      must_cite:\\\\n        - \\\\\\\"deepseekmath (GRPO origin)\\\\\\\"\\\\n        - \\\\\\\"mellgren-prolog-grpo\\\\\\\"\\\\n        - \\\\\\\"logic-lm\\\\\\\"\\\\n        - \\\\\\\"linc\\\\\\\"\\\\n        - \\\\\\\"satlm\\\\\\\"\\\\n      target_count: 8\\\\n    - cluster_name: reward-shaping\\\\n      search_queries:\\\\n        - \\\\\\\"reward shaping process supervision LLM reasoning 2024 2025\\\\\\\"\\\\n        - \\\\\\\"process reward model overoptimization\\\\\\\"\\\\n      must_cite:\\\\n        - \\\\\\\"lightman-verify-step\\\\\\\"\\\\n        - \\\\\\\"gao-effective-rl-reward\\\\\\\"\\\\n        - \\\\\\\"rlsf\\\\\\\"\\\\n      target_count: 8\\\\n    - cluster_name: reward-hacking\\\\n      search_queries:\\\\n        - \\\\\\\"reward hacking overoptimization RLHF 2024 2025\\\\\\\"\\\\n        - \\\\\\\"specification gaming reinforcement learning\\\\\\\"\\\\n      must_cite:\\\\n        - \\\\\\\"gao-reward-overoptimization\\\\\\\"\\\\n        - \\\\\\\"skalse-reward-hacking\\\\\\\"\\\\n        - \\\\\\\"reward-hacking-survey\\\\\\\"\\\\n        - \\\\\\\"spurious-rewards\\\\\\\"\\\\n      target_count: 6\\\\n    - cluster_name: goodhart-overoptimization\\\\n      search_queries:\\\\n        - \\\\\\\"Goodhart's Law reinforcement learning proxy reward\\\\\\\"\\\\n        - \\\\\\\"reward model overoptimization scaling laws\\\\\\\"\\\\n      must_cite:\\\\n        - \\\\\\\"manheim-goodhart-taxonomy\\\\\\\"\\\\n        - \\\\\\\"karwowski-goodhart-rl\\\\\\\"\\\\n        - \\\\\\\"kwa-catastrophic-goodhart\\\\\\\"\\\\n        - \\\\\\\"pan-reward-misspecification\\\\\\\"\\\\n      target_count: 6\\\\n    - cluster_name: fol-formalization\\\\n      search_queries:\\\\n        - \\\\\\\"first-order logic formalization LLM 2024 2025\\\\\\\"\\\\n        - \\\\\\\"Prolog LLM reasoning\\\\\\\"\\\\n      must_cite:\\\\n        - \\\\\\\"folio\\\\\\\"\\\\n        - \\\\\\\"proofwriter\\\\\\\"\\\\n        - \\\\\\\"fover-pei2025\\\\\\\"\\\\n      target_count: 5\\\\n    - cluster_name: mutation-testing\\\\n      search_queries:\\\\n        - \\\\\\\"mutation testing component analysis software engineering\\\\\\\"\\\\n      must_cite:\\\\n        - \\\\\\\"demillo1978\\\\\\\"\\\\n        - \\\\\\\"jia-harman-survey\\\\\\\"\\\\n      target_count: 4\\\\n    - cluster_name: verification-reward\\\\n      search_queries:\\\\n        - \\\\\\\"solver prover reward signal RL training 2024 2025\\\\\\\"\\\\n        - \\\\\\\"formal verification LLM training\\\\\\\"\\\\n      must_cite:\\\\n        - \\\\\\\"deepseek-prover-v15\\\\\\\"\\\\n        - \\\\\\\"math-shepherd\\\\\\\"\\\\n      target_count: 4\\\\n\\\\nwriting_order:\\\\n  - experiments\\\\n  - method\\\\n  - introduction\\\\n  - related_work\\\\n  - discussion\\\\n  - abstract\\\\n  - conclusion\\\\n\\\", \\\"total_chars\\\": 16820, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026\\n  track: main\\n  template: acl2023/\\n  template_note: \\\"ARR May 25 cycle. ACL Rolling Review format (acl2023.sty).\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  core_claim: >\\n    ISR (Intensional Structural Reward), derived via Solver Trace Ablation,\\n    serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers\\n    but fails as a training signal due to meta-level Goodhart's Law — the diagnostic\\n    metric becomes gamed when optimized, with apparent improvements explained by\\n    premise minimization artifacts.\\n  created_at: 2026-05-14T18:00:00Z\\n  updated_at: 2026-05-14T19:00:00Z\\n  update_note: \\\"Director approved. Tab3 merged into Fig2; Tab6 moved to appendix. 4 fig + 4 table in main.\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    core_bullets:\\n      - \\\"Problem: GRPO formalizers achieve high prove rates but produce structurally degenerate outputs; no diagnostic exists\\\"\\n      - \\\"Method: STA derives ISR via leave-one-out component necessity testing on solver inputs\\\"\\n      - \\\"Claim 1: ISR detects hacking invisible to prove_rate (0.64→0.13→0.003 collapse over 100→500→1000 steps)\\\"\\n      - \\\"Claim 2: ISR-as-reward exhibits meta-level Goodhart — β=0.1 induces ISR-specific gaming (H7=64.5% vs 0% random), premise-matched 1.06x; β=0.3 PR collapses (18% vs 48% random)\\\"\\n      - \\\"Claim 3: ISR diagnostic transfers to Prolog (cross-logic generality)\\\"\\n      - \\\"Taxonomy: 6 distinct hacking modes identified across conditions\\\"\\n    dependencies: [experiments, method, discussion]\\n    tables: []\\n    figures: []\\n    registry_refs: []\\n\\n  - section: introduction\\n    word_budget: 1200\\n    core_bullets:\\n      - \\\"Hook: A GRPO formalizer achieves 93% prove rate — but 87% of its proved outputs embed the conclusion in the premises. Structural shortcuts invisible to execution reward.\\\"\\n      - \\\"Gap: Execution-only evaluation (prove_rate) conflates genuine reasoning with degenerate shortcuts. No principled diagnostic exists for structural integrity in neurosymbolic GRPO.\\\"\\n      - \\\"Insight: Component necessity testing (LOO ablation on solver inputs) yields ISR — AND when this diagnostic becomes reward, it exhibits meta-level Goodhart: the model games the metric itself.\\\"\\n      - \\\"Mechanism: STA protocol + systematic study across 6 reward conditions × 3 seeds × up to 1000 steps\\\"\\n      - \\\"Contributions: (C1) ISR as diagnostic with complete collapse trajectory; (C2) Meta-level Goodhart empirical characterization with premise-count confound analysis; (C3) Cross-logic diagnostic transfer; (C4) 6-mode hacking taxonomy\\\"\\n    dependencies: [experiments]\\n    citation_hints:\\n      - \\\"GRPO: deepseekmath\\\"\\n      - \\\"Neurosymbolic: satlm, logic-lm, linc\\\"\\n      - \\\"Reward hacking: gao-reward-overoptimization, karwowski-goodhart-rl\\\"\\n      - \\\"Goodhart taxonomy: manheim-goodhart-taxonomy\\\"\\n    figures: [fig1_sta_overview]\\n    tables: []\\n    registry_refs: []\\n\\n  - section: related_work\\n    word_budget: 900\\n    core_bullets:\\n      - \\\"Cluster 1 — Neurosymbolic Reasoning with LLMs: Logic-LM, LINC, SatLM, LoRP, FoVer pipeline approach (prompting); Mellgren Prolog GRPO (RL). STA differs: structural reward + diagnostic focus\\\"\\n      - \\\"Cluster 2 — Reward Shaping & Process Supervision: Lightman verify-step, Math-Shepherd, RLSF symbolic feedback, Rubric-GRPO. STA's ISR is solver-grounded process signal; our finding: process reward can itself Goodhart\\\"\\n      - \\\"Cluster 3 — Reward Hacking & Goodhart's Law: Gao scaling laws, Karwowski geometric, Manheim taxonomy, Skalse characterization, Pan misspecification. We contribute empirical Goodhart in formal reasoning + meta-level (proxy games itself)\\\"\\n      - \\\"Cluster 4 — Mutation Testing & Component Analysis: DeMillo 1978, Jia-Harman survey, Just mutants. STA adapts LOO mutation from SE to formal logic\\\"\\n    dependencies: [introduction]\\n    citation_hints:\\n      - \\\"Must cite: deepseekmath, logic-lm, linc, satlm, mellgren-prolog-grpo\\\"\\n      - \\\"Must cite: lightman-verify-step, gao-reward-overoptimization, karwowski-goodhart-rl, manheim-goodhart-taxonomy\\\"\\n      - \\\"Must cite: demillo1978, folio, proofwriter\\\"\\n    figures: []\\n    tables: []\\n    registry_refs: []\\n\\n  - section: method\\n    word_budget: 1200\\n    core_bullets:\\n      - \\\"3.1 Task: NL → Formal Logic formalization, verified by external solver (Prover9 for FOL, SWI-Prolog for Prolog)\\\"\\n      - \\\"3.2 GRPO Training: execution-only reward r_exec ∈ {0,1}, group relative policy optimization\\\"\\n      - \\\"3.3 Solver Trace Ablation (STA): LOO ablation protocol — for proved sample with n components, remove each component, re-run solver, ISR = fraction of components whose removal causes proof failure\\\"\\n      - \\\"3.4 ISR Definition: ISR(x) = (1/n) Σ_i 1[solver fails on x\\\\\\\\{c_i}], bounded [0,1]. ISR=1 → all necessary; ISR=0 → none necessary\\\"\\n      - \\\"3.5 Reward Formulations: exec-only, additive ISR (r_exec·(1+β·ISR)), additive random control, convex combination, SFT baseline\\\"\\n      - \\\"3.6 Hacking Taxonomy: H1 (multi-premise conclusion embedding), H7 (single premise = conclusion), H3 (complexity-without-utility), tautological collapse, repetition collapse, contradiction explosion\\\"\\n    dependencies: []\\n    notation_table:\\n      r_exec: \\\"binary execution reward (solver success)\\\"\\n      ISR: \\\"Intensional Structural Reward\\\"\\n      beta: \\\"ISR reward weight\\\"\\n      n: \\\"number of components in formalization\\\"\\n      c_i: \\\"i-th component (premise/rule)\\\"\\n      H1: \\\"multi-premise conclusion embedding\\\"\\n      H7: \\\"single premise = conclusion\\\"\\n    figures: [fig1_sta_overview]\\n    tables: []\\n    registry_refs: [sta-phase0-baseline, plan003-eval-exec-only-r5]\\n\\n  - section: experiments\\n    word_budget: 2800\\n    core_bullets:\\n      - \\\"4.1 Setup: Qwen3-4B, GRPO (K=8, 500 steps default), ProofWriter-FOL-100 eval, Prover9/SWI-Prolog solvers, 3 seeds (42/43/44)\\\"\\n      - \\\"4.2 ISR as Diagnostic (Claim 1): ISR collapse trajectory 0.6423→0.1324→0.0027 over 100→500→1000 steps (Fig2 with embedded data); PR rises 32%→93%→96%; 3-seed exec-only divergence (s42 genuine→H1, s43 degraded PR=14%, s44 tautological 2-comp); SFT baseline 92.9% genuine confirms RL-specificity\\\"\\n      - \\\"4.3 Meta-Level Goodhart (Claim 2): β=0.1 ISR — H7=64.5% ISR-specific gaming vs 0% random; premise-count-matched 1.06x (no real advantage); β=0.3 — PR collapse 18% vs 48% random; conclusion embedding is GRPO-universal (68-100%); ISR restructures hacking, doesn't reduce it\\\"\\n      - \\\"4.4 Cross-Logic Transfer (Claim 3): Prolog exec-only 3-seed ISR<0.1 across all seeds; Prolog STA s42 100% H7; diagnostic generalizes regardless of training outcome\\\"\\n      - \\\"4.5 Hacking Taxonomy: 6 modes quantified across conditions; reward type determines hacking composition not prevalence\\\"\\n    dependencies: []\\n    registry_refs:\\n      - sta-phase0-baseline\\n      - plan003-eval-exec-only-r5\\n      - plan001-exec-only-s42-r2\\n      - plan001-exec-only-s43-r4\\n      - plan001-exec-only-s44\\n      - plan016-extended-1000-s42\\n      - plan002-additive-b01-s42\\n      - plan002-additive-b01-s43\\n      - plan002-additive-b01-s44\\n      - plan018-additive-random-b01-s42\\n      - plan018-additive-random-b01-s43-r2\\n      - plan018-additive-random-b01-s44\\n      - plan002-additive-b03-s42\\n      - plan017-additive-random-s42\\n      - plan005-sta-low-s42\\n      - plan013-random-reward-s42-r4\\n      - plan009-sft-baseline-s42-r4\\n      - plan006-prolog-exec-s42\\n      - plan006-prolog-exec-s43-r3\\n      - plan006-prolog-exec-s44\\n      - plan006-prolog-sta-s42\\n    tables: [tab1_goodhart_landscape, tab2_hacking_taxonomy, tab4_beta01_3seed, tab5_prolog_crosslogic]\\n    figures: [fig2_isr_collapse, fig3_hacking_composition, fig4_prolog_comparison]\\n\\n  - section: discussion\\n    word_budget: 600\\n    core_bullets:\\n      - \\\"ISR measures syntactic component necessity, not semantic faithfulness (plan014 ρ=-0.049 n.s.)\\\"\\n      - \\\"Premise count confound: LOO metrics mathematically biased — fewer premises → higher ISR regardless of quality (D051)\\\"\\n      - \\\"Practical implications: ISR for post-hoc diagnosis only; never trust prove_rate alone; single-seed GRPO unreliable; proxy-as-reward cautionary tale\\\"\\n      - \\\"Meta-level Goodhart as general warning for any proxy-metric-as-reward approach\\\"\\n    dependencies: [experiments]\\n    tables: []\\n    figures: []\\n    registry_refs: [plan014-downstream-nli-s42]\\n\\n  - section: conclusion\\n    word_budget: 300\\n    core_bullets:\\n      - \\\"Summary: STA/ISR as diagnostic detects reward hacking invisible to prove_rate; ISR-as-reward exhibits meta-level Goodhart at all doses\\\"\\n      - \\\"Limitations: single base model (Qwen3-4B); ProofWriter data only; ISR = syntactic not semantic; 3 seeds; Claim 3 Prolog STA partial\\\"\\n      - \\\"Future: ISR + semantic verification; adaptive reward weighting; broader logic types; scale to larger models\\\"\\n    dependencies: [experiments, discussion]\\n    tables: []\\n    figures: []\\n    registry_refs: []\\n\\n  - section: appendix\\n    word_budget: 1000\\n    core_bullets:\\n      - \\\"Table A1: Experimental setup and hyperparameters (moved from Tab6)\\\"\\n      - \\\"Full hacking taxonomy definitions and examples\\\"\\n      - \\\"Per-seed detailed results\\\"\\n    dependencies: [experiments]\\n    tables: [tab6_setup]\\n    figures: []\\n    registry_refs: []\\n\\nvisualization_plan:\\n  - fig_id: fig1_sta_overview\\n    type: conceptual\\n    tool: matplotlib\\n    description: >\\n      STA protocol overview: (a) NL input → LLM formalizer → formal logic → solver → prove/fail.\\n      (b) STA ablation: remove each component, re-run solver, compute ISR.\\n      (c) ISR as diagnostic vs ISR as reward (Goodhart arrow).\\n      3-panel horizontal layout.\\n    placement: method\\n    aspect_ratio: \\\"3:1\\\"\\n    data_source: \\\"manual\\\"\\n\\n  - fig_id: fig2_isr_collapse\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      ISR collapse trajectory over training steps with embedded data annotations.\\n      X-axis: training steps (100, 500, 1000). Dual y-axis: PR (left, rising 32%→93%→96%)\\n      and ISR (right, falling 0.64→0.13→0.003). Include component count trend (6.58→18.55)\\n      as bubble size or secondary annotation. Annotate: ISR=0 ratio at 1000 steps (94.8%).\\n      Replaces former Tab3 — all collapse data embedded in figure annotations.\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n    data_source: \\\"registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\\\"\\n\\n  - fig_id: fig3_hacking_composition\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Stacked bar chart: hacking mode composition across conditions.\\n      X-axis: Exec-only s42, ISR β=0.1 s42/s43/s44, Random β=0.1 (3-seed mean), SFT.\\n      Stacked segments: H7 (red), H1 (orange), H3 (yellow), Genuine (green).\\n      Shows ISR restructures hacking (H1→H7) rather than reducing it.\\n    placement: experiments\\n    aspect_ratio: \\\"16:9\\\"\\n    data_source: \\\"registry: plan001-exec-only-s42-r2, plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42, plan018-additive-random-b01-s43-r2, plan018-additive-random-b01-s44, plan009-sft-baseline-s42-r4\\\"\\n\\n  - fig_id: fig4_prolog_comparison\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Grouped bar chart: FOL vs Prolog exec-only ISR comparison (3 seeds each).\\n      X-axis: s42, s43, s44. Grouped bars: FOL ISR, Prolog ISR.\\n      Both near-zero, confirming cross-logic diagnostic transfer.\\n      Overlay PR values as text annotations.\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n    data_source: \\\"registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44, plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3, plan006-prolog-exec-s44\\\"\\n\\ntable_plan:\\n  - table_id: tab1_goodhart_landscape\\n    caption: \\\"Goodhart landscape: ISR-as-reward across dose and formulation. All eval on ProofWriter-FOL-100 via eval\\\\\\\\_sta.py.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Condition, Formula, β, Seed, PR↑, ISR↑, H7%, H1%, Genuine%, Mode]\\n    data_source: \\\"registry: sta-phase0-baseline, plan001-exec-only-s42-r2, plan009-sft-baseline-s42-r4, plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42, plan018-additive-random-b01-s43-r2, plan018-additive-random-b01-s44, plan002-additive-b03-s42, plan017-additive-random-s42, plan013-random-reward-s42-r4\\\"\\n    notes: \\\"Core table. Bold best genuine%. † marks tautological artifacts. * marks sampling eval.\\\"\\n\\n  - table_id: tab2_hacking_taxonomy\\n    caption: \\\"Hacking taxonomy: six distinct modes across reward conditions. Rates are % of proved samples (s42 seed).\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Mode, Description, \\\"Exec-only\\\", \\\"ISR β=0.1\\\", \\\"Random β=0.1\\\", \\\"SFT\\\"]\\n    data_source: \\\"registry: plan001-exec-only-s42-r2, plan002-additive-b01-s42, plan018-additive-random-b01-s42, plan009-sft-baseline-s42-r4, plan012-hacking-taxonomy\\\"\\n    notes: \\\"s42 comparison (cleanest seed). Include mode descriptions in table.\\\"\\n\\n  - table_id: tab4_beta01_3seed\\n    caption: \\\"ISR β=0.1 vs Random β=0.1: 3-seed comparison. H7 is ISR-specific (64.5% vs 0%). Premise-count-matched ISR: 1.06×.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Seed, Condition, PR, \\\"ISR (proved)\\\", H7%, H1%, Genuine%, \\\"Prem-matched ISR\\\"]\\n    data_source: \\\"registry: plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42, plan018-additive-random-b01-s43-r2, plan018-additive-random-b01-s44\\\"\\n    notes: \\\"Key table for Claim 2. Include 3-seed mean±std row. Premise-matched column only for s42.\\\"\\n\\n  - table_id: tab5_prolog_crosslogic\\n    caption: \\\"Cross-logic diagnostic transfer: Prolog results. ISR detects degeneration across logic types.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Logic, Condition, Seed, PR, ISR, \\\"Proved-only ISR\\\", H7%, Mode]\\n    data_source: \\\"registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3, plan006-prolog-exec-s44, plan006-prolog-sta-s42\\\"\\n    notes: \\\"Prolog STA s43/s44 RUNNING — [pending]. Include FOL exec-only for comparison.\\\"\\n\\n  - table_id: tab6_setup\\n    caption: \\\"Experimental setup and hyperparameters.\\\"\\n    placement: appendix\\n    type: configuration\\n    columns: [Parameter, Value]\\n    data_source: \\\"manual\\\"\\n    notes: \\\"APPENDIX. Base model, training data, K, steps, seeds, solvers, eval dataset.\\\"\\n\\nliterature_strategy:\\n  citation_budget: 40\\n  macro_context:\\n    - \\\"GRPO / RL for formal reasoning\\\"\\n    - \\\"reward hacking and Goodhart's Law in LLM training\\\"\\n    - \\\"neurosymbolic NL-to-logic formalization\\\"\\n    - \\\"mutation testing and component analysis\\\"\\n  micro_clusters:\\n    - cluster_name: neurosymbolic-rl\\n      search_queries:\\n        - \\\"GRPO reinforcement learning logical reasoning 2024 2025\\\"\\n        - \\\"neurosymbolic LLM formal logic prover\\\"\\n      must_cite:\\n        - \\\"deepseekmath (GRPO origin)\\\"\\n        - \\\"mellgren-prolog-grpo\\\"\\n        - \\\"logic-lm\\\"\\n        - \\\"linc\\\"\\n        - \\\"satlm\\\"\\n      target_count: 8\\n    - cluster_name: reward-shaping\\n      search_queries:\\n        - \\\"reward shaping process supervision LLM reasoning 2024 2025\\\"\\n        - \\\"process reward model overoptimization\\\"\\n      must_cite:\\n        - \\\"lightman-verify-step\\\"\\n        - \\\"gao-effective-rl-reward\\\"\\n        - \\\"rlsf\\\"\\n      target_count: 8\\n    - cluster_name: reward-hacking\\n      search_queries:\\n        - \\\"reward hacking overoptimization RLHF 2024 2025\\\"\\n        - \\\"specification gaming reinforcement learning\\\"\\n      must_cite:\\n        - \\\"gao-reward-overoptimization\\\"\\n        - \\\"skalse-reward-hacking\\\"\\n        - \\\"reward-hacking-survey\\\"\\n        - \\\"spurious-rewards\\\"\\n      target_count: 6\\n    - cluster_name: goodhart-overoptimization\\n      search_queries:\\n        - \\\"Goodhart's Law reinforcement learning proxy reward\\\"\\n        - \\\"reward model overoptimization scaling laws\\\"\\n      must_cite:\\n        - \\\"manheim-goodhart-taxonomy\\\"\\n        - \\\"karwowski-goodhart-rl\\\"\\n        - \\\"kwa-catastrophic-goodhart\\\"\\n        - \\\"pan-reward-misspecification\\\"\\n      target_count: 6\\n    - cluster_name: fol-formalization\\n      search_queries:\\n        - \\\"first-order logic formalization LLM 2024 2025\\\"\\n        - \\\"Prolog LLM reasoning\\\"\\n      must_cite:\\n        - \\\"folio\\\"\\n        - \\\"proofwriter\\\"\\n        - \\\"fover-pei2025\\\"\\n      target_count: 5\\n    - cluster_name: mutation-testing\\n      search_queries:\\n        - \\\"mutation testing component analysis software engineering\\\"\\n      must_cite:\\n        - \\\"demillo1978\\\"\\n        - \\\"jia-harman-survey\\\"\\n      target_count: 4\\n    - cluster_name: verification-reward\\n      search_queries:\\n        - \\\"solver prover reward signal RL training 2024 2025\\\"\\n        - \\\"formal verification LLM training\\\"\\n      must_cite:\\n        - \\\"deepseek-prover-v15\\\"\\n        - \\\"math-shepherd\\\"\\n      target_count: 4\\n\\nwriting_order:\\n  - experiments\\n  - method\\n  - introduction\\n  - related_work\\n  - discussion\\n  - abstract\\n  - conclusion\\n\", \"total_chars\": 16820, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the references.bib and look for evidence_tables_d051.md which is mentioned for Tab 1 data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "5c09703c-819f-42a7-b531-542b7fd291a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018c9Zd9WnZs2796jCTU3duL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6767,
      "cache_read_input_tokens": 37506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6767
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

_source line 21_

Let me check the references file and evidence tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "6f4e75bc-6411-4d10-94b5-1911c79a50d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018c9Zd9WnZs2796jCTU3duL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6767,
      "cache_read_input_tokens": 37506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6767
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_0186R2aLtHmTp23UMEkH4q6s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "caf81ecf-0b09-486e-b8fb-51c37cbc02b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018c9Zd9WnZs2796jCTU3duL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6767,
      "cache_read_input_tokens": 37506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6767
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

_source line 23 · 2026-05-14T18:50:45.353Z_

<details><summary>↩ Tool result · `toolu_0186R2aLtHmTp23UMEkH4q6s`</summary>

```text
1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseek-r1,
6	  author       = {{DeepSeek-AI}},
7	  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},
8	  journal      = {Nature},
9	  year         = {2025},
10	  note         = {arXiv:2501.12948},
11	}
12	
13	@article{deepseekmath,
14	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
15	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
16	  journal      = {arXiv preprint arXiv:2402.03300},
17	  year         = {2024},
18	  eprint       = {2402.03300},
19	  archivePrefix = {arXiv},
20	  primaryClass = {cs.AI},
21	}
22	
23	@article{logic-rl,
24	  author       = {Xian and others},
25	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
26	  journal      = {arXiv preprint arXiv:2502.14768},
27	  year         = {2025},
28	  eprint       = {2502.14768},
29	  archivePrefix = {arXiv},
30	  primaryClass = {cs.AI},
31	}
32	
33	@article{mellgren-prolog-grpo,
34	  author       = {Niklas Mellgren},
35	  title        = {{Training Language Models to Use Prolog as a Tool}},
36	  journal      = {arXiv preprint arXiv:2512.07407},
37	  year         = {2024},
38	  eprint       = {2512.07407},
39	  archivePrefix = {arXiv},
40	  primaryClass = {cs.AI},
41	}
42	
43	@inproceedings{satlm,
44	  author       = {Xi Ye and others},
45	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
46	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
47	  year         = {2023},
48	}
49	
50	@article{deepproblog,
51	  author       = {Robin Manhaeve and Sebastijan Duman{\v{c}}i{\'c} and Angelika Kimmig and Thomas Demeester and Luc De Raedt},
52	  title        = {{Neural Probabilistic Logic Programming in DeepProbLog}},
53	  journal      = {Artificial Intelligence},
54	  volume       = {298},
55	  year         = {2021},
56	}
57	
58	@inproceedings{neurasp,
59	  author       = {Zhun Yang and Adam Ishay and Joohyung Lee},
60	  title        = {{NeurASP: Embracing Neural Networks into Answer Set Programming}},
61	  booktitle    = {Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},
62	  year         = {2020},
63	}
64	
65	@article{thought-like-pro,
66	  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},
67	  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},
68	  journal      = {arXiv preprint arXiv:2407.14562},
69	  year         = {2024},
70	  eprint       = {2407.14562},
71	  archivePrefix = {arXiv},
72	  primaryClass = {cs.AI},
73	}
74	
75	% ============================================================
76	% Category 2: Reward shaping for code/formal verification
77	% ============================================================
78	
79	@inproceedings{lightman-verify-step,
80	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
81	  title        = {{Let's Verify Step by Step}},
82	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
83	  year         = {2024},
84	  note         = {arXiv:2305.20050},
85	}
86	
87	@article{reward-shaping-rlhf,
88	  author       = {Jiayi Fu and Xuandong Zhao and Chengyuan Yao and others},
89	  title        = {{Reward Shaping to Mitigate Reward Hacking in RLHF}},
90	  journal      = {arXiv preprint arXiv:2502.18770},
91	  year         = {2025},
92	  eprint       = {2502.18770},
93	  archivePrefix = {arXiv},
94	  primaryClass = {cs.AI},
95	}
96	
97	@article{rlvr-reasoning,
98	  author       = {{Various}},
99	  title        = {{Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs}},
100	  journal      = {arXiv preprint arXiv:2506.14245},
101	  year         = {2025},
102	  eprint       = {2506.14245},
103	  archivePrefix = {arXiv},
104	  primaryClass = {cs.AI},
105	}
106	
107	@article{rubric-grpo,
108	  author       = {{Various}},
109	  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},
110	  journal      = {arXiv preprint arXiv:2605.08061},
111	  year         = {2025},
112	  eprint       = {2605.08061},
113	  archivePrefix = {arXiv},
114	  primaryClass = {cs.AI},
115	}
116	
117	@article{gao-effective-rl-reward,
118	  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},
119	  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},
120	  journal      = {arXiv preprint arXiv:2410.15115},
121	  year         = {2024},
122	  eprint       = {2410.15115},
123	  archivePrefix = {arXiv},
124	  primaryClass = {cs.AI},
125	}
126	
127	@article{prof-process-outcome,
128	  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},
129	  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},
130	  journal      = {arXiv preprint arXiv:2509.03403},
131	  year         = {2025},
132	  eprint       = {2509.03403},
133	  archivePrefix = {arXiv},
134	  primaryClass = {cs.AI},
135	}
136	
137	@inproceedings{moskovitz-constrained-rlhf,
138	  author       = {Ted Moskovitz and Aaditya K. Singh and DJ Strouse and Tuomas Sandholm and Ruslan Salakhutdinov and Anca D. Dragan and Stephen McAleer},
139	  title        = {{Confronting Reward Model Overoptimization with Constrained RLHF}},
140	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
141	  year         = {2024},
142	  note         = {arXiv:2310.04373},
143	}
144	
145	@inproceedings{skalse-reward-hacking,
146	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
147	  title        = {{Defining and Characterizing Reward Hacking}},
148	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
149	  year         = {2022},
150	  note         = {arXiv:2209.13085},
151	}
152	
153	@article{progrs-outcome-conditioned,
154	  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},
155	  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},
156	  journal      = {arXiv preprint arXiv:2604.02341},
157	  year         = {2026},
158	  eprint       = {2604.02341},
159	  archivePrefix = {arXiv},
160	  primaryClass = {cs.AI},
161	}
162	
163	@inproceedings{qwen-prm-lessons,
164	  author       = {Zhenru Zhang and others},
165	  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},
166	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
167	  year         = {2025},
168	  note         = {arXiv:2501.07301},
169	}
170	
171	% ============================================================
172	% Category 3: Mutation testing in software engineering
173	% ============================================================
174	
175	@article{demillo1978,
176	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
177	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
178	  journal      = {Computer},
179	  volume       = {11},
180	  number       = {4},
181	  pages        = {34--43},
182	  year         = {1978},
183	}
184	
185	@article{offutt-coupling,
186	  author       = {A. Jefferson Offutt},
187	  title        = {{Investigations of the Software Testing Coupling Effect}},
188	  journal      = {ACM Transactions on Software Engineering and Methodology},
189	  volume       = {1},
190	  number       = {1},
191	  pages        = {5--20},
192	  year         = {1992},
193	}
194	
195	@article{jia-harman-survey,
196	  author       = {Yue Jia and Mark Harman},
197	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
198	  journal      = {IEEE Transactions on Software Engineering},
199	  volume       = {37},
200	  number       = {5},
201	  pages        = {649--678},
202	  year         = {2011},
203	}
204	
205	@inproceedings{just-mutants-real-faults,
206	  author       = {Ren{\'e} Just and Darioush Jalali and Laura Inozemtseva and others},
207	  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},
208	  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},
209	  year         = {2014},
210	}
211	
212	@article{llmorpheus,
213	  author       = {Frank Tip and Jon Bell and others},
214	  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},
215	  journal      = {IEEE Transactions on Software Engineering},
216	  year         = {2025},
217	}
218	
219	@inproceedings{mutation-guided-meta,
220	  author       = {Christopher Foster and others},
221	  title        = {{Mutation-Guided LLM-based Test Generation at Meta}},
222	  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},
223	  year         = {2025},
224	}
225	
226	@article{mutation-consistency-llm,
227	  author       = {{Various}},
228	  title        = {{Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs}},
229	  journal      = {arXiv preprint arXiv:2401.05940},
230	  year         = {2024},
231	  eprint       = {2401.05940},
232	  archivePrefix = {arXiv},
233	  primaryClass = {cs.AI},
234	}
235	
236	% ============================================================
237	% Category 4: Intensional program analysis
238	% ============================================================
239	
240	@article{deepmutation,
241	  author       = {{Various}},
242	  title        = {{A Probabilistic Framework for Mutation Testing in Deep Neural Networks}},
243	  journal      = {Information and Software Technology},
244	  year         = {2023},
245	}
246	
247	% ============================================================
248	% Category 5: Reward hacking / overoptimization
249	% ============================================================
250	
251	@inproceedings{inform-reward-hacking,
252	  author       = {{Various}},
253	  title        = {{InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling}},
254	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
255	  year         = {2024},
256	}
257	
258	@article{mo-grpo,
259	  author       = {{CyberAgent AI Lab}},
260	  title        = {{MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems}},
261	  journal      = {arXiv preprint arXiv:2509.22047},
262	  year         = {2025},
263	  eprint       = {2509.22047},
264	  archivePrefix = {arXiv},
265	  primaryClass = {cs.AI},
266	}
267	
268	@article{reward-hacking-survey,
269	  author       = {{Various}},
270	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
271	  journal      = {arXiv preprint arXiv:2604.13602},
272	  year         = {2026},
273	  eprint       = {2604.13602},
274	  archivePrefix = {arXiv},
275	  primaryClass = {cs.AI},
276	}
277	
278	@inproceedings{energy-loss-reward-hacking,
279	  author       = {{Various}},
280	  title        = {{The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking}},
281	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
282	  year         = {2025},
283	}
284	
285	@article{spurious-rewards,
286	  author       = {Ruixin Yang and others},
287	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
288	  journal      = {arXiv preprint arXiv:2506.10947},
289	  year         = {2025},
290	  eprint       = {2506.10947},
291	  archivePrefix = {arXiv},
292	  primaryClass = {cs.AI},
293	}
294	
295	@article{bondarenko-spec-gaming,
296	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
297	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
298	  journal      = {arXiv preprint arXiv:2502.13295},
299	  year         = {2025},
300	  eprint       = {2502.13295},
301	  archivePrefix = {arXiv},
302	  primaryClass = {cs.AI},
303	}
304	
305	@inproceedings{kim-game-formalization,
306	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
307	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
308	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
309	  year         = {2026},
310	  note         = {arXiv:2604.19459},
311	}
312	
313	@inproceedings{gao-reward-overoptimization,
314	  author       = {Leo Gao and John Schulman and Jacob Hilton},
315	  title        = {{Scaling Laws for Reward Model Overoptimization}},
316	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
317	  year         = {2023},
318	  note         = {arXiv:2210.10760},
319	}
320	
321	@inproceedings{karwowski-goodhart-rl,
322	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
323	  title        = {{Goodhart's Law in Reinforcement Learning}},
324	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
325	  year         = {2024},
326	  note         = {arXiv:2310.09144},
327	}
328	
329	% ============================================================
330	% Category 6: FOL/Prolog formalization with LLMs
331	% ============================================================
332	
333	@inproceedings{folio,
334	  author       = {Simeng Han and others},
335	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
336	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
337	  year         = {2024},
338	  note         = {arXiv:2209.00840},
339	}
340	
341	@inproceedings{proofwriter,
342	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
343	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
344	  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},
345	  year         = {2021},
346	}
347	
348	@inproceedings{logic-lm,
349	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},
350	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
351	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
352	  year         = {2023},
353	}
354	
355	@inproceedings{linc,
356	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},
357	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
358	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
359	  year         = {2023},
360	}
361	
362	@article{fover-pei2025,
363	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
364	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
365	  journal      = {Transactions of the Association for Computational Linguistics},
366	  volume       = {13},
367	  pages        = {1340--1359},
368	  year         = {2025},
369	}
370	
371	@article{lorp,
372	  author       = {{Various}},
373	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
374	  journal      = {Knowledge-Based Systems},
375	  year         = {2025},
376	}
377	
378	@article{nl2fol,
379	  author       = {Lalwani and Kim and others},
380	  title        = {{NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection}},
381	  journal      = {arXiv preprint arXiv:2405.02318},
382	  year         = {2024},
383	  eprint       = {2405.02318},
384	  archivePrefix = {arXiv},
385	  primaryClass = {cs.AI},
386	}
387	
388	@article{logica2,
389	  author       = {Liu and others},
390	  title        = {{LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding}},
391	  journal      = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},
392	  year         = {2023},
393	}
394	
395	% ============================================================
396	% Category 7: Goodhart's Law theory and dose-response dynamics
397	% ============================================================
398	
399	@article{manheim-goodhart-taxonomy,
400	  author       = {David Manheim and Scott Garrabrant},
401	  title        = {{Categorizing Variants of Goodhart's Law}},
402	  journal      = {arXiv preprint arXiv:1803.04585},
403	  year         = {2019},
404	  eprint       = {1803.04585},
405	  archivePrefix = {arXiv},
406	  primaryClass = {cs.AI},
407	}
408	
409	@inproceedings{pan-reward-misspecification,
410	  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},
411	  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},
412	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
413	  year         = {2022},
414	}
415	
416	@inproceedings{kwa-catastrophic-goodhart,
417	  author       = {Tat-Thang Kwa and Rachel Thomas and Adri{\`a} Garriga-Alonso},
418	  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},
419	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
420	  year         = {2024},
421	}
422	
423	@inproceedings{rafailov-daa-scaling,
424	  author       = {Rafael Rafailov and Yaswanth Chittepu and Ryan Park and Harshit Sikchi and Joey Hejna and W. Bradley Knox and Chelsea Finn and Scott Niekum},
425	  title        = {{Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms}},
426	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
427	  year         = {2024},
428	}
429	
430	@inproceedings{huang-chi-squared,
431	  author       = {Afra Feyza Aky{\"u}rek and Banghua Zhu and Sham Kakade and Jiantao Jiao},
432	  title        = {{Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction}},
433	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
434	  year         = {2025},
435	}
436	
437	@inproceedings{coste-rm-ensembles,
438	  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},
439	  title        = {{Reward Model Ensembles Help Mitigate Overoptimization}},
440	  booktitle    = {NeurIPS 2023 Workshop on Alignment},
441	  year         = {2023},
442	}
443	
444	% ============================================================
445	% Category 8: Solver/prover as RL reward signal
446	% ============================================================
447	
448	@article{rlsf,
449	  author       = {Abhinav Jha and Shikhar Murty and Zico Kolter and others},
450	  title        = {{Reinforcement Learning via Symbolic Feedback}},
451	  journal      = {arXiv preprint arXiv:2405.16661},
452	  year         = {2024},
453	  eprint       = {2405.16661},
454	  archivePrefix = {arXiv},
455	  primaryClass = {cs.AI},
456	}
457	
458	@inproceedings{fover-kamoi2026,
459	  author       = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},
460	  title        = {{FoVer: Generalizable Process Reward Models via Formally Verified Training Data}},
461	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
462	  year         = {2026},
463	  note         = {arXiv:2502.01345},
464	}
465	
466	@inproceedings{deepseek-prover-v15,
467	  author       = {{DeepSeek AI}},
468	  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},
469	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
470	  year         = {2025},
471	  note         = {arXiv:2408.08152},
472	}
473	
474	@article{alphaproof,
475	  author       = {{Google DeepMind}},
476	  title        = {{AlphaProof}},
477	  journal      = {Nature},
478	  year         = {2025},
479	}
480	
481	@inproceedings{math-shepherd,
482	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},
483	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
484	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
485	  year         = {2024},
486	  note         = {arXiv:2312.08935},
487	}
488	
489	% ============================================================
490	% Additional reward-shaping papers
491	% ============================================================
492	
493	@inproceedings{bipars,
494	  author       = {Yujing Hu and Weixun Wang and Hangtian Jia and others},
495	  title        = {{Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping}},
496	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
497	  year         = {2020},
498	}
499	
500	@article{dapo,
501	  author       = {Qiying Yu and others},
502	  title        = {{DAPO: An Open-Source LLM Reinforcement Learning System at Scale}},
503	  journal      = {arXiv preprint arXiv:2503.14476},
504	  year         = {2025},
505	  eprint       = {2503.14476},
506	  archivePrefix = {arXiv},
507	  primaryClass = {cs.AI},
508	}
509	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "edb9d3e6-2670-46cf-a968-28d4d3b0d8f5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
      "content": "% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  note         = {arXiv:2501.12948},\n}\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Xian and others},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2024},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and others},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n@article{deepproblog,\n  author       = {Robin Manhaeve and Sebastijan Duman{\\v{c}}i{\\'c} and Angelika Kimmig and Thomas Demeester and Luc De Raedt},\n  title        = {{Neural Probabilistic Logic Programming in DeepProbLog}},\n  journal      = {Artificial Intelligence},\n  volume       = {298},\n  year         = {2021},\n}\n\n@inproceedings{neurasp,\n  author       = {Zhun Yang and Adam Ishay and Joohyung Lee},\n  title        = {{NeurASP: Embracing Neural Networks into Answer Set Programming}},\n  booktitle    = {Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},\n  year         = {2020},\n}\n\n@article{thought-like-pro,\n  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},\n  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},\n  journal      = {arXiv preprint arXiv:2407.14562},\n  year         = {2024},\n  eprint       = {2407.14562},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@article{reward-shaping-rlhf,\n  author       = {Jiayi Fu and Xuandong Zhao and Chengyuan Yao and others},\n  title        = {{Reward Shaping to Mitigate Reward Hacking in RLHF}},\n  journal      = {arXiv preprint arXiv:2502.18770},\n  year         = {2025},\n  eprint       = {2502.18770},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rlvr-reasoning,\n  author       = {{Various}},\n  title        = {{Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs}},\n  journal      = {arXiv preprint arXiv:2506.14245},\n  year         = {2025},\n  eprint       = {2506.14245},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rubric-grpo,\n  author       = {{Various}},\n  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},\n  journal      = {arXiv preprint arXiv:2605.08061},\n  year         = {2025},\n  eprint       = {2605.08061},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{prof-process-outcome,\n  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},\n  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},\n  journal      = {arXiv preprint arXiv:2509.03403},\n  year         = {2025},\n  eprint       = {2509.03403},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{moskovitz-constrained-rlhf,\n  author       = {Ted Moskovitz and Aaditya K. Singh and DJ Strouse and Tuomas Sandholm and Ruslan Salakhutdinov and Anca D. Dragan and Stephen McAleer},\n  title        = {{Confronting Reward Model Overoptimization with Constrained RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n@article{progrs-outcome-conditioned,\n  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},\n  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},\n  journal      = {arXiv preprint arXiv:2604.02341},\n  year         = {2026},\n  eprint       = {2604.02341},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{qwen-prm-lessons,\n  author       = {Zhenru Zhang and others},\n  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2501.07301},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--43},\n  year         = {1978},\n}\n\n@article{offutt-coupling,\n  author       = {A. Jefferson Offutt},\n  title        = {{Investigations of the Software Testing Coupling Effect}},\n  journal      = {ACM Transactions on Software Engineering and Methodology},\n  volume       = {1},\n  number       = {1},\n  pages        = {5--20},\n  year         = {1992},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@inproceedings{just-mutants-real-faults,\n  author       = {Ren{\\'e} Just and Darioush Jalali and Laura Inozemtseva and others},\n  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2014},\n}\n\n@article{llmorpheus,\n  author       = {Frank Tip and Jon Bell and others},\n  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},\n  journal      = {IEEE Transactions on Software Engineering},\n  year         = {2025},\n}\n\n@inproceedings{mutation-guided-meta,\n  author       = {Christopher Foster and others},\n  title        = {{Mutation-Guided LLM-based Test Generation at Meta}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2025},\n}\n\n@article{mutation-consistency-llm,\n  author       = {{Various}},\n  title        = {{Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs}},\n  journal      = {arXiv preprint arXiv:2401.05940},\n  year         = {2024},\n  eprint       = {2401.05940},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 4: Intensional program analysis\n% ============================================================\n\n@article{deepmutation,\n  author       = {{Various}},\n  title        = {{A Probabilistic Framework for Mutation Testing in Deep Neural Networks}},\n  journal      = {Information and Software Technology},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 5: Reward hacking / overoptimization\n% ============================================================\n\n@inproceedings{inform-reward-hacking,\n  author       = {{Various}},\n  title        = {{InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@article{mo-grpo,\n  author       = {{CyberAgent AI Lab}},\n  title        = {{MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems}},\n  journal      = {arXiv preprint arXiv:2509.22047},\n  year         = {2025},\n  eprint       = {2509.22047},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{reward-hacking-survey,\n  author       = {{Various}},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{energy-loss-reward-hacking,\n  author       = {{Various}},\n  title        = {{The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2025},\n}\n\n@article{spurious-rewards,\n  author       = {Ruixin Yang and others},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and others},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},\n  year         = {2021},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {{Various}},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{nl2fol,\n  author       = {Lalwani and Kim and others},\n  title        = {{NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection}},\n  journal      = {arXiv preprint arXiv:2405.02318},\n  year         = {2024},\n  eprint       = {2405.02318},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logica2,\n  author       = {Liu and others},\n  title        = {{LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding}},\n  journal      = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 7: Goodhart's Law theory and dose-response dynamics\n% ============================================================\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{pan-reward-misspecification,\n  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},\n  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2022},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri{\\`a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{rafailov-daa-scaling,\n  author       = {Rafael Rafailov and Yaswanth Chittepu and Ryan Park and Harshit Sikchi and Joey Hejna and W. Bradley Knox and Chelsea Finn and Scott Niekum},\n  title        = {{Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{huang-chi-squared,\n  author       = {Afra Feyza Aky{\\\"u}rek and Banghua Zhu and Sham Kakade and Jiantao Jiao},\n  title        = {{Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n}\n\n@inproceedings{coste-rm-ensembles,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {{Reward Model Ensembles Help Mitigate Overoptimization}},\n  booktitle    = {NeurIPS 2023 Workshop on Alignment},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 8: Solver/prover as RL reward signal\n% ============================================================\n\n@article{rlsf,\n  author       = {Abhinav Jha and Shikhar Murty and Zico Kolter and others},\n  title        = {{Reinforcement Learning via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{fover-kamoi2026,\n  author       = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},\n  title        = {{FoVer: Generalizable Process Reward Models via Formally Verified Training Data}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2026},\n  note         = {arXiv:2502.01345},\n}\n\n@inproceedings{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2408.08152},\n}\n\n@article{alphaproof,\n  author       = {{Google DeepMind}},\n  title        = {{AlphaProof}},\n  journal      = {Nature},\n  year         = {2025},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@inproceedings{bipars,\n  author       = {Yujing Hu and Weixun Wang and Hangtian Jia and others},\n  title        = {{Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2020},\n}\n\n@article{dapo,\n  author       = {Qiying Yu and others},\n  title        = {{DAPO: An Open-Source LLM Reinforcement Learning System at Scale}},\n  journal      = {arXiv preprint arXiv:2503.14476},\n  year         = {2025},\n  eprint       = {2503.14476},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n",
      "numLines": 509,
      "startLine": 1,
      "totalLines": 509
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Agent · `toolu_019pYxZ75oq8GKJVS16z159A`</summary>

```json
{
  "description": "Find evidence tables file",
  "subagent_type": "Explore",
  "prompt": "Search for a file called evidence_tables_d051.md or similar evidence_tables files in the project /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/. Also look for any files with \"evidence\" in the name. Report the full paths and a brief summary of the content of each file found. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "8409d550-5de4-410e-a79f-35fe5d3c1339",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018c9Zd9WnZs2796jCTU3duL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6767,
      "cache_read_input_tokens": 37506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6767
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

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "description": "Find evidence tables file",
  "task_type": "local_agent",
  "prompt": "Search for a file called evidence_tables_d051.md or similar evidence_tables files in the project /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/. Also look for any files with \"evidence\" in the name. Report the full paths and a brief summary of the content of each file found. Search breadth: medium.",
  "uuid": "3cca548e-0922-4fd1-a7a7-1b2198e12e82",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

## Round 1

54 recorded events

### User

_source line 26 · 2026-05-14T18:50:47.900Z_

Search for a file called evidence_tables_d051.md or similar evidence_tables files in the project /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/. Also look for any files with "evidence" in the name. Report the full paths and a brief summary of the content of each file found. Search breadth: medium.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "c81bb799-0b2f-4337-b3a7-f5eda685ad65"
}
```

</details>

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "description": "Finding **/*evidence*",
  "usage": {
    "total_tokens": 19196,
    "tool_uses": 1,
    "duration_ms": 1698
  },
  "last_tool_name": "Glob",
  "uuid": "328a44ff-ac87-4897-b4c2-ebab2f92ed95",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Glob · `toolu_01P54DZ3Lvb7mcTp7QLJQumu`</summary>

```json
{
  "pattern": "**/*evidence*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "2cb49672-14b6-4201-b6ed-2bb77e75564d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012NxF3r5444SDqDfWCkFd8y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 18670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 513,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 29 · 2026-05-14T18:50:49.639Z_

<details><summary>↩ Tool result · `toolu_01P54DZ3Lvb7mcTp7QLJQumu`</summary>

```text
logs/workers/worker_research_evidence-chain-audit_20260514T055852.log
logs/chats/worker_research_evidence-chain-audit_20260514T055852.lock
logs/chats/worker_research_evidence-chain-audit_20260514T055852.jsonl
logs/workers/worker_research_evidence-chain-audit_20260514T055852_result.json
artifacts/_project/report/paper_table1_evidence.md
logs/workers/worker_analysis_paper-evidence-table_20260514T070810.log
logs/workers/worker_analysis_paper-evidence-table_20260514T070810_result.json
artifacts/paper_table1_evidence.md
logs/workers/worker_analysis_fix-evidence-table-provenance_20260514T071442.log
logs/chats/worker_analysis_fix-evidence-table-provenance_20260514T071442.lock
logs/chats/worker_analysis_fix-evidence-table-provenance_20260514T071442.jsonl
logs/workers/worker_analysis_fix-evidence-table-provenance_20260514T071442_result.json
logs/workers/worker_research_paper-evidence-table_20260514T090950.log
logs/chats/worker_research_paper-evidence-table_20260514T090950.lock
logs/chats/worker_research_paper-evidence-table_20260514T090950.jsonl
logs/workers/worker_research_paper-evidence-table_20260514T090950_result.json
artifacts/_project/report/evidence_audit.md
logs/workers/worker_analysis_evidence-chain-status_20260514T150201.log
logs/chats/worker_analysis_evidence-chain-status_20260514T150201.lock
artifacts/_project/report/evidence_chain_status.md
artifacts/evidence_chain_status.md
logs/workers/worker_analysis_evidence-chain-status_20260514T150201_retry1.log
logs/chats/worker_analysis_evidence-chain-status_20260514T150201.jsonl
logs/workers/worker_analysis_evidence-chain-status_20260514T150201_result.json
artifacts/_project/report/evidence_tables_d051.md
logs/workers/worker_analysis_evidence-table-d051-final_20260514T161117.log
logs/workers/worker_analysis_evidence-table-d051-final_20260514T161117_result.json
logs/workers/worker_knowledge_evidence-tables-finalize_20260514T165006.log
logs/workers/worker_knowledge_evidence-tables-finalize_20260514T165006_result.json
artifacts/_project/data/evidence_tables_d051.md
artifacts/evidence_tables_d051.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "8d4cd304-2194-4d90-9df8-1ba9e8a836d2"
}
```

</details>

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 19201,
    "tool_uses": 2,
    "duration_ms": 1873
  },
  "last_tool_name": "Bash",
  "uuid": "675ad7f4-f106-4fb9-b0ed-1d9670944ae4",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01HwNojdKGnXVuwZxSzH8KMy`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type f -name \"*evidence*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "4ab96a5b-e704-4626-bfd3-20fc96f96ed6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012NxF3r5444SDqDfWCkFd8y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 18670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 513,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 32 · 2026-05-14T18:50:49.973Z_

<details><summary>↩ Tool result · `toolu_01HwNojdKGnXVuwZxSzH8KMy`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_analysis_fix-evidence-table-provenance_20260514T071442.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_knowledge_evidence-tables-finalize_20260514T165006_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_research_evidence-chain-audit_20260514T055852_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_analysis_paper-evidence-table_20260514T070810.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_research_paper-evidence-table_20260514T090950.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_analysis_paper-evidence-table_20260514T070810_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_research_paper-evidence-table_20260514T090950_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_analysis_fix-evidence-table-provenance_20260514T071442_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_knowledge_evidence-tables-finalize_20260514T165006.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_analysis_evidence-table-d051-final_20260514T161117_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_analysis_evidence-chain-status_20260514T150201_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_analysis_evidence-table-d051-final_20260514T161117.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_analysis_evidence-chain-status_20260514T150201.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_research_evidence-chain-audit_20260514T055852.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_analysis_evidence-chain-status_20260514T150201_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_research_paper-evidence-table_20260514T090950.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_analysis_evidence-chain-status_20260514T150201.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_analysis_fix-evidence-table-provenance_20260514T071442.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_analysis_fix-evidence-table-provenance_20260514T071442.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_research_evidence-chain-audit_20260514T055852.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_research_evidence-chain-audit_20260514T055852.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_research_paper-evidence-table_20260514T090950.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_analysis_evidence-chain-status_20260514T150201.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/data/evidence_tables_d051.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/evidence_audit.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/paper_table1_evidence.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/evidence_tables_d051.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/evidence_chain_status.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/paper_table1_evidence.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_tables_d051.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_chain_status.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "0599529f-b8ed-491b-9de1-7ca05ef35f32"
}
```

</details>

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "description": "Reading artifacts/evidence_tables_d051.md",
  "usage": {
    "total_tokens": 22578,
    "tool_uses": 3,
    "duration_ms": 4095
  },
  "last_tool_name": "Read",
  "uuid": "590d9183-8487-4adf-8600-e8c97966d979",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_0153vKti3vX54Yier3c7LUvv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_tables_d051.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "4a376d53-5481-4d52-90e7-9cc8bf1770fb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fk8mRiB6biLx6ThhgWACGY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3371,
      "cache_read_input_tokens": 19183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3371,
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

_source line 35 · 2026-05-14T18:50:52.013Z_

<details><summary>↩ Tool result · `toolu_0153vKti3vX54Yier3c7LUvv`</summary>

```text
1	# Evidence Tables — D051 Pure Negative Framing
2	
3	> All eval metrics from `eval_sta.py` (full STA) unless noted. D051 framing: ISR-as-reward provides **no structural advantage**; premise-count-matched ratio = 1.06×.
4	
5	---
6	
7	## Table 1 — Main Results (FOL)
8	
9	| Condition | Seeds | eval PR (mean±std) | eval ISR (mean±std) | proved_only ISR | Components (mean) | Tautological Collapse | Conclusion Embedding % | Hacking Mode |
10	|---|---|---|---|---|---|---|---|---|
11	| **Base model** (phase0) | 1 (s42) | 0.12 | 0.064±0.198 | — | — | No | — | N/A (no RL) |
12	| **SFT baseline** (plan009-r4) | 1 (s42) | 0.14 | 0.080±0.214 | 0.571 | — | No | 7.1% (1/14 H1) | Near-zero hacking (92.9% genuine) |
13	| **Exec-only 500步** (plan001) | 3 | 0.68±0.47 | 0.23±0.30 | — | — | 1/3 seeds | — | Heterogeneous† |
14	|   ↳ s42 | — | 0.93 | 0.123±0.189 | 0.132 | 6.58 | No | 87.1% (H1) | H1 87.1% (81/93), Genuine 12.9% (12/93) |
15	|   ↳ s43 | — | 0.14‡ | 0‡ | — | — | No | — | Repetition collapse |
16	|   ↳ s44 | — | 0.98 | 0.570±0.201 | 0.582 | 2.04 | **Yes (94%)** | — | Tautological collapse |
17	| **Exec-only 1000步** (plan016) | 1 (s42) | 0.96 | 0.003±0.012 | 0.003 | 18.55 | No | **100%** (H1=96/96) | H1 100%, Genuine 0% (contradiction explosion) |
18	| **ISR β=0.1** (plan002-b01) | 3 | 0.77±0.14 | 0.55±0.24 | 0.716±0.26 | 4.65 | No | 2/3 seeds | ISR-specific gaming |
19	|   ↳ s42 | — | 0.81 | 0.337±0.323 | 0.415 | 5.58 | No | 67.9% | H7 16% + H1 52% |
20	|   ↳ s43 | — | 0.61 | 0.506±0.452 | 0.830 | 4.03 | No | 96.7% | **H7 96.7%** (ISR inflation) |
21	|   ↳ s44 | — | 0.89 | 0.803±0.342 | 0.902 | 4.33 | No | 86.5% | **H7 86.5%** (ISR inflation) |
22	| **Random β=0.1** (plan018) | 2/3§ | 0.84 | 0.083 | 0.100 | 8.46¹ | No | ~75% (H1)⁴ | Redundant premises |
23	|   ↳ s42 | — | 0.79 | 0.104±0.137 | 0.131 | 8.46 | No | 70.9% (H1) | H1 70.9% (56/79), H7 0% |
24	|   ↳ s44 | — | 0.89 | 0.062±0.176 | 0.070 | — | No | 79.8% (H1) | H1 79.8% (71/89), H7 0% |
25	|   ↳ s43 | — | RUNNING | — | — | — | — | — | — |
26	| **ISR β=0.3** (plan002-b03) | 1 (s42) | 0.18 | 0.026±0.074 | 0.143 | — | No | — | Format collapse (Goodhart) |
27	| **Random β=0.3** (plan017) | 1 (s42) | 0.48 | 0.045±0.076 | 0.094 | 9.60 | No | — | Complexity-without-utility |
28	| **Convex random** (plan013-r4) | 1 (s42) | 1.00 | 0.535±0.128 | 0.535 | 2.0 | **Yes (100%)** | 100% | P→P tautological |
29	
30	**Notes:**
31	- † Exec-only 500步 shows extreme seed variance: s42 = conclusion embedding, s43 = repetition collapse, s44 = tautological collapse. 3-seed mean is informative of instability, not a typical outcome.
32	- ‡ s43 eval used `do_sample=True, temperature=0.7` (NOT eval_sta.py). 87% samples hit `max_new_tokens`. ISR=0 not comparable to other seeds (C004 violation in historical data).
33	- § plan018-s43 still RUNNING; 2-seed interim values reported.
34	- ¹ Component count only available for s42.
35	
36	---
37	
38	## Table 2 — Hacking Taxonomy
39	
40	| Condition | Seed | H7 % | H1 % | H7+H1 (total) | Genuine % | n_proved | Premise-matched ISR |
41	|---|---|---|---|---|---|---|---|
42	| **SFT baseline** | s42 | 0% (0/14) | 7.1% (1/14) | 7.1% | **92.9%** (13/14) | 14 | — |
43	| **Exec-only 500步** | s42 | 0% (0/93) | **87.1%** (81/93) | **87.1%** | 12.9% (12/93) | 93 | — |
44	| **Exec-only 500步** | s44 | **100%** (97/97) | 0% | **100%** | 0% (0/97) | 97⁵ | — |
45	| **Exec-only 1000步** | s42 | — | — | — | — | 96 | — |
46	| **ISR β=0.1** | s42 | **16.0%** (13/81) | **51.9%** (42/81) | **67.9%** | **30.9%** (25/81) | 81 | **0.2578** (n≥3 prem) |
47	| **ISR β=0.1** | s43 | **96.7%** (59/61) | 0% | **96.7%** | ~3% (~2/61) | 61 | — |
48	| **ISR β=0.1** | s44 | **86.5%** (77/89) | 0% | **86.5%** | ~13.5% (~12/89)³ | 89 | — |
49	| **Random β=0.1** | s42 | **0%** (0/79) | **70.9%** (56/79) | **70.9%** | **29.1%** (23/79) | 79 | **0.2434** (n≥3 prem) |
50	| **Random β=0.1** | s44 | **0%** (0/89) | **79.8%** (71/89) | **79.8%** | **20.2%** (18/89) | 89 | — |
51	| **Convex random** | s42 | 100%² | 0% | 100% | 0% | 100 | — |
52	
53	**Key findings (D051 framing):**
54	
55	1. **H7 is ISR-specific**: ISR 3-seed H7 mean = 64.5% (149/231), Random H7 = 0%. ISR reward specifically induces premise=conclusion hacking.
56	2. **H1 is GRPO-universal**: Random H1 = 71–80%, ISR s42 H1 = 52%. Conclusion embedding is a general GRPO strategy, not ISR-specific.
57	3. **ISR changes hacking composition, not total**: Overall conclusion-in-premise rate is comparable (ISR 67.9% vs Random 70.9% for s42), but ISR converts H1 → more extreme H7.
58	4. **Premise-count-matched: no structural advantage**: ISR genuine (n_prem≥3) = 0.2578, Random genuine (n_prem≥3) = 0.2434. **Ratio = 1.06×**. The apparent 2.4× raw genuine ISR is entirely a premise minimization artifact.
59	5. **SFT has near-zero hacking** (1/14 H1, 0 H7, 92.9% genuine) → hacking is GRPO/RL-specific, not a general finetuning artifact.
60	
61	**Notes:**
62	- ² Tautological collapse (premise=conclusion, 2-component proofs). Classified separately from H7 (which is conclusion duplication with ISR inflation in multi-step context).
63	- ³ s44's 12 "genuine" samples are all n_prem=1 (H7 classifier false negatives — single premise but normalization difference prevented conclusion match).
64	- H7 = single premise identical to conclusion (ISR-inflating shortcut).
65	- H1 = multi-premise proof with conclusion embedded among premises (GRPO-universal shortcut).
66	- Genuine = proved sample with no conclusion duplication detected.
67	- ⁴ Conclusion Embedding % for Random = H1 rate (H7=0% for all Random seeds). s42: 70.9%, s44: 79.8%.
68	- ⁵ s44 eval_results.json reports 97 proved (vs registry 98). H7=97/97=100%.
69	
70	---
71	
72	## Table 3 — Prolog Cross-Logic (Final)
73	
74	| Condition | Seed | eval PR | eval ISR | proved_only ISR | Components | Hacking Mode |
75	|---|---|---|---|---|---|---|
76	| **Prolog exec-only** | s42 | 0.83 | 0.031 | 0.037 | — | Ground fact enumeration (H7=0%, H1=0%) |
77	| **Prolog exec-only** | s43 | **0.56** | 0.008 | 0.015 | — | Degraded (low PR, near-zero ISR) |
78	| **Prolog exec-only** | s44 | **0.21** | 0.081 | 0.387 | — | Severe degradation (lowest PR, ISR from small sample) |
79	| **Prolog exec-only** | **3-seed mean±std** | **0.53±0.31** | **0.040±0.037** | **0.146±0.210** | — | Extreme seed variance (σ=31pp) |
80	| **Prolog STA (ISR reward)** | s42 | 0.50 | 0.500 | **1.000** | 1.0 | **100% H7** (single clause = query) |
81	| **Prolog STA (ISR reward)** | s43 | **0.38** | 0.070 | 0.185 | — | **Functional H7†** (H1=97.4%, uppercase pseudo-Prolog) |
82	| **Prolog STA (ISR reward)** | s44 | **0.97** | **0.885** | **0.912** | — | **Query-as-fact gaming‡** (functional H7=95/97, 0% genuine) |
83	| **Prolog STA (ISR reward)** | **3-seed mean±std** | **0.62±0.31** | **0.485±0.408** | **0.699±0.447** | — | **3/3 Goodhart, 0% genuine** |
84	
85	**Notes:**
86	- † s43 strict classifier shows H7=0%, H1=0%, Genuine=100%. However, functional analysis reveals all 38/38 proved samples are tautological (n_necessary=1). Model generates uppercase pseudo-Prolog (e.g., MARY_IS_AN_AVADEOTE.) — non-standard syntax bypasses strict classifier but achieves same functional outcome as H7 (conclusion embedded as single clause).
87	- ‡ s44 strict classifier shows H7=0%, H1=0%, Genuine=100%. Reviewer independent verification: 95/97 proved samples have n_necessary=1. Model converts NL problems to snake_case atoms, sets them as both fact and query — Prolog trivially proves. High PR (0.97) and ISR (0.885) are gaming artifacts. Third distinct Goodhart pathway.
88	
89	**Key findings:**
90	
91	1. **3/3 seeds Goodhart — universal across Prolog STA**: Every seed develops a distinct gaming pathway, zero genuine proofs across all 185 proved samples.
92	2. **Three distinct Goodhart pathways in Prolog**:
93	   - s42: Clean H7 — single clause identical to query (50/50 proved)
94	   - s43: Degenerate syntax H1 — uppercase pseudo-Prolog, functional n_necessary=1 (38/38 tautological)
95	   - s44: Query-as-fact gaming — snake_case atom conversion, n_necessary=1 for 95/97 (Reviewer-verified)
96	3. **Exec-only Prolog 3-seed**: PR=53.3%±31.1%, ISR=0.040±0.037. Extreme seed variance replicates FOL pattern (FOL exec-only PR=68%±47%).
97	4. **Prolog ISR consistently near-zero (exec-only)**: All 3 seeds ISR<0.1 (mean), confirming exec-only produces no genuine reasoning traces across both logic types.
98	5. **Prolog Goodhart stronger than FOL**: FOL ISR β=0.1 has 3/3 seeds hacking but with 16-31% genuine residual in s42. Prolog STA has 3/3 seeds hacking with 0% genuine — simpler logic semantics enable more complete exploitation.
99	
100	---
101	
102	## Summary: D051 Claim Support Matrix
103	
104	| Claim | Evidence | Status |
105	|---|---|---|
106	| **C1: ISR as diagnostic** | ISR collapse trajectory: 0.642 (100步) → 0.132 (500步) → 0.003 (1000步) while PR rises 32%→93%→96% | **Supported** (3 timepoints) |
107	| **C2: ISR-as-reward = no structural advantage** | Premise-count-matched ISR: 1.06× (ISR 0.258 vs Random 0.243, n_prem≥3). β=0.1: 2/3 seeds H7>86%. β=0.3: PR 18% < Random 48% | **Supported** (D051 definitive) |
108	| **C2 corollary: hacking composition shift** | ISR: H7=64.5% mean, H1=17%. Random: H7=0%, H1=78%. Total hacking comparable (~70%) | **Supported** |
109	| **SFT = zero hacking** | plan009-r4: PR=14%, ISR=0.08, no hacking patterns detected | **Supported** |
110	| **C3: Cross-logic generality** | Prolog STA 3-seed: s42 clean H7=100%, s43 functional H7=97.4%, s44 query-as-fact gaming (functional H7=95/97). **3/3 Goodhart, 0% genuine**. Three distinct gaming pathways. Exec-only 3-seed: PR=53%±31%, ISR=0.040±0.037. | **Strongly supported** (3-seed complete, 3/3 Goodhart, 3 distinct pathways) |
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "b3bbeb0a-1eb4-458e-9397-650e767c21b9"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "description": "Reading artifacts/_project/report/evidence_tables_d051.md",
  "usage": {
    "total_tokens": 22579,
    "tool_uses": 4,
    "duration_ms": 4974
  },
  "last_tool_name": "Read",
  "uuid": "38d1534b-6334-4c26-9636-1810b7701fb8",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01TiHWRLZZRqk2mmu4sK3dyM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/evidence_tables_d051.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "fb1c119c-2c6a-4813-a6b1-65a96e5eda3d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fk8mRiB6biLx6ThhgWACGY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3371,
      "cache_read_input_tokens": 19183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3371,
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

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "description": "Reading artifacts/_project/data/evidence_tables_d051.md",
  "usage": {
    "total_tokens": 22580,
    "tool_uses": 5,
    "duration_ms": 4987
  },
  "last_tool_name": "Read",
  "uuid": "e9c0fd2e-fa06-4bb9-ab66-b65be67d0b8a",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01X7HStWcT9gC9WZZw61JFAZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/data/evidence_tables_d051.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "6d751ac2-7f68-4aa0-a4df-53e7ebc02980",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fk8mRiB6biLx6ThhgWACGY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3371,
      "cache_read_input_tokens": 19183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3371,
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

_source line 40 · 2026-05-14T18:50:52.893Z_

<details><summary>↩ Tool result · `toolu_01TiHWRLZZRqk2mmu4sK3dyM`</summary>

```text
1	# Evidence Tables — D051 Pure Negative Framing
2	
3	> All eval metrics from `eval_sta.py` (full STA) unless noted. D051 framing: ISR-as-reward provides **no structural advantage**; premise-count-matched ratio = 1.02×.
4	
5	---
6	
7	## Table 1 — Main Results (FOL)
8	
9	| Condition | Seeds | eval PR (mean±std) | eval ISR (mean±std) | proved_only ISR | Components (mean) | Tautological Collapse | Conclusion Embedding % | Hacking Mode |
10	|---|---|---|---|---|---|---|---|---|
11	| **Base model** (phase0) | 1 (s42) | 0.12 | 0.064±0.198 | — | — | No | — | N/A (no RL) |
12	| **SFT baseline** (plan009-r4) | 1 (s42) | 0.14 | 0.080±0.214 | 0.571 | — | No | 0% | None (zero hacking) |
13	| **Exec-only 500步** (plan001) | 3 | 0.68±0.47 | 0.23±0.30 | — | — | 1/3 seeds | — | Heterogeneous† |
14	|   ↳ s42 | — | 0.93 | 0.123±0.189 | 0.132 | — | No | — | Conclusion embedding |
15	|   ↳ s43 | — | 0.14‡ | 0‡ | — | — | No | — | Repetition collapse |
16	|   ↳ s44 | — | 0.98 | 0.570±0.201 | 0.582 | 2.04 | **Yes (94%)** | — | Tautological collapse |
17	| **Exec-only 1000步** (plan016) | 1 (s42) | 0.96 | 0.003±0.012 | 0.003 | 18.55 | No | — | Contradiction explosion |
18	| **ISR β=0.1** (plan002-b01) | 3 | 0.77±0.14 | 0.55±0.24 | 0.716±0.26 | 4.65 | No | 2/3 seeds | ISR-specific gaming |
19	|   ↳ s42 | — | 0.81 | 0.337±0.323 | 0.415 | 5.58 | No | 67.9% | H7 16% + H1 52% |
20	|   ↳ s43 | — | 0.61 | 0.506±0.452 | 0.830 | 4.03 | No | 96.7% | **H7 96.7%** (ISR inflation) |
21	|   ↳ s44 | — | 0.89 | 0.803±0.342 | 0.902 | 4.33 | No | 86.5% | **H7 86.5%** (ISR inflation) |
22	| **Random β=0.1** (plan018) | 2/3§ | 0.84 | 0.083 | 0.100 | 8.46¹ | No | 0% H7 | Redundant premises |
23	|   ↳ s42 | — | 0.79 | 0.104±0.137 | 0.131 | 8.46 | No | 73.4% (H1) | H1 73.4%, H7 0% |
24	|   ↳ s44 | — | 0.89 | 0.062±0.176 | 0.070 | — | No | 83.1% (H1) | H1 83.1%, H7 0% |
25	|   ↳ s43 | — | RUNNING | — | — | — | — | — | — |
26	| **ISR β=0.3** (plan002-b03) | 1 (s42) | 0.18 | 0.026±0.074 | 0.143 | — | No | — | Format collapse (Goodhart) |
27	| **Random β=0.3** (plan017) | 1 (s42) | 0.48 | 0.045±0.076 | 0.094 | 9.60 | No | — | Complexity-without-utility |
28	| **Convex random** (plan013-r4) | 1 (s42) | 1.00 | 0.535±0.128 | 0.535 | 2.0 | **Yes (100%)** | 100% | P→P tautological |
29	
30	**Notes:**
31	- † Exec-only 500步 shows extreme seed variance: s42 = conclusion embedding, s43 = repetition collapse, s44 = tautological collapse. 3-seed mean is informative of instability, not a typical outcome.
32	- ‡ s43 eval used `do_sample=True, temperature=0.7` (NOT eval_sta.py). 87% samples hit `max_new_tokens`. ISR=0 not comparable to other seeds (C004 violation in historical data).
33	- § plan018-s43 still RUNNING; 2-seed interim values reported.
34	- ¹ Component count only available for s42.
35	
36	---
37	
38	## Table 2 — Hacking Taxonomy
39	
40	| Condition | Seed | H7 % | H1 % | H7+H1 (total) | Genuine % | n_proved | Premise-matched ISR |
41	|---|---|---|---|---|---|---|---|
42	| **SFT baseline** | s42 | 0% | 0% | 0% | 100% | 14 | — |
43	| **Exec-only 500步** | s42 | — | — | — | — | 93 | — |
44	| **Exec-only 500步** | s44 | 94%² | — | — | — | 98 | — |
45	| **Exec-only 1000步** | s42 | — | — | — | — | 96 | — |
46	| **ISR β=0.1** | s42 | **16.0%** (13/81) | **51.9%** (42/81) | **67.9%** | **32.1%** (26/81) | 81 | **0.258** (n≥3 prem) |
47	| **ISR β=0.1** | s43 | **96.7%** (59/61) | 0% | **96.7%** | ~3% (~2/61) | 61 | — |
48	| **ISR β=0.1** | s44 | **86.5%** (77/89) | 0% | **86.5%** | ~13.5% (~12/89)³ | 89 | — |
49	| **Random β=0.1** | s42 | **0%** (0/79) | **73.4%** (58/79) | **73.4%** | **26.6%** (21/79) | 79 | **0.252** (n≥3 prem) |
50	| **Random β=0.1** | s44 | **0%** (0/89) | **83.1%** (74/89) | **83.1%** | **16.9%** (15/89) | 89 | — |
51	| **Convex random** | s42 | 100%² | 0% | 100% | 0% | 100 | — |
52	
53	**Key findings (D051 framing):**
54	
55	1. **H7 is ISR-specific**: ISR 3-seed H7 mean = 64.5% (149/231), Random H7 = 0%. ISR reward specifically induces premise=conclusion hacking.
56	2. **H1 is GRPO-universal**: Random H1 = 73–83%, ISR s42 H1 = 52%. Conclusion embedding is a general GRPO strategy, not ISR-specific.
57	3. **ISR changes hacking composition, not total**: Overall conclusion-in-premise rate is comparable (ISR 67.9% vs Random 73.4% for s42), but ISR converts H1 → more extreme H7.
58	4. **Premise-count-matched: no structural advantage**: ISR genuine (n_prem≥3) = 0.258, Random genuine (n_prem≥3) = 0.252. **Ratio = 1.02×**. The apparent 2.4× raw genuine ISR is entirely a premise minimization artifact.
59	5. **SFT has zero hacking** → hacking is GRPO/RL-specific, not a general finetuning artifact.
60	
61	**Notes:**
62	- ² Tautological collapse (premise=conclusion, 2-component proofs). Classified separately from H7 (which is conclusion duplication with ISR inflation in multi-step context).
63	- ³ s44's 12 "genuine" samples are all n_prem=1 (H7 classifier false negatives — single premise but normalization difference prevented conclusion match).
64	- H7 = single premise identical to conclusion (ISR-inflating shortcut).
65	- H1 = multi-premise proof with conclusion embedded among premises (GRPO-universal shortcut).
66	- Genuine = proved sample with no conclusion duplication detected.
67	
68	---
69	
70	## Table 3 — Prolog Cross-Logic (Interim)
71	
72	| Condition | Seed | eval PR | eval ISR | proved_only ISR | Components | Hacking Mode |
73	|---|---|---|---|---|---|---|
74	| **Prolog exec-only** | s42 | 0.83 | 0.031 | 0.037 | — | Ground fact enumeration (H7=0%, H1=0%) |
75	| **Prolog STA (ISR reward)** | s42 | 0.50 | 0.500 | **1.000** | 1.0 | **100% H7** (single clause = query) |
76	| **Prolog exec-only** | s43 | ANALYZING | — | — | — | Training complete, awaiting eval |
77	| **Prolog exec-only** | s44 | ANALYZING | — | — | — | Training complete, awaiting eval |
78	
79	**Key findings:**
80	
81	1. **Cross-logic replication of ISR-specific gaming**: Prolog STA s42 H7 = 100% (vs FOL s42 H7 = 16%). Simpler logic semantics → faster, more complete hacking. Prolog model converges to trivial single-clause programs identical to the query.
82	2. **Exec-only Prolog ISR near-zero**: PR = 83% but ISR = 0.031, replicating FOL pattern (high PR, structural degeneration).
83	3. **Prolog ISR context (C006)**: Prolog exec-only's low ISR reflects redundant ground fact enumeration (e.g., `penguin(fido).` repeated 3×), not absence of reasoning. Per-clause ablation under redundancy yields ISR=0 by construction. This is distinct from FOL exec-only's conclusion embedding.
84	4. **Pending**: s43/s44 exec-only training complete, awaiting eval. Prolog STA multi-seed blocked on GPU availability.
85	
86	---
87	
88	## Summary: D051 Claim Support Matrix
89	
90	| Claim | Evidence | Status |
91	|---|---|---|
92	| **C1: ISR as diagnostic** | ISR collapse trajectory: 0.642 (100步) → 0.132 (500步) → 0.003 (1000步) while PR rises 32%→93%→96% | **Supported** (3 timepoints) |
93	| **C2: ISR-as-reward = no structural advantage** | Premise-count-matched ISR: 1.02× (ISR 0.258 vs Random 0.252, n_prem≥3). β=0.1: 2/3 seeds H7>86%. β=0.3: PR 18% < Random 48% | **Supported** (D051 definitive) |
94	| **C2 corollary: hacking composition shift** | ISR: H7=64.5% mean, H1=17%. Random: H7=0%, H1=78%. Total hacking comparable (~70%) | **Supported** |
95	| **SFT = zero hacking** | plan009-r4: PR=14%, ISR=0.08, no hacking patterns detected | **Supported** |
96	| **C3: Cross-logic generality** | Prolog STA H7=100% vs FOL H7=16%. Prolog exec-only ISR=0.031. Pending: s43/s44 eval | **Interim** (1 seed done) |
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "af95b10d-7e38-4e63-9b04-b773bdb285e8"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T18:50:52.895Z_

<details><summary>↩ Tool result · `toolu_01X7HStWcT9gC9WZZw61JFAZ`</summary>

```text
1	# Evidence Tables — D051 Pure Negative Framing
2	
3	> All eval metrics from `eval_sta.py` (full STA) unless noted. D051 framing: ISR-as-reward provides **no structural advantage**; premise-count-matched ratio = 1.06×.
4	
5	---
6	
7	## Table 1 — Main Results (FOL)
8	
9	| Condition | Seeds | eval PR (mean±std) | eval ISR (mean±std) | proved_only ISR | Components (mean) | Tautological Collapse | Conclusion Embedding % | Hacking Mode |
10	|---|---|---|---|---|---|---|---|---|
11	| **Base model** (phase0) | 1 (s42) | 0.12 | 0.064±0.198 | — | — | No | — | N/A (no RL) |
12	| **SFT baseline** (plan009-r4) | 1 (s42) | 0.14 | 0.080±0.214 | 0.571 | — | No | 7.1% (1/14 H1) | Near-zero hacking (92.9% genuine) |
13	| **Exec-only 500步** (plan001) | 3 | 0.68±0.47 | 0.23±0.30 | — | — | 1/3 seeds | — | Heterogeneous† |
14	|   ↳ s42 | — | 0.93 | 0.123±0.189 | 0.132 | 6.58 | No | 87.1% (H1) | H1 87.1% (81/93), Genuine 12.9% (12/93) |
15	|   ↳ s43 | — | 0.14‡ | 0‡ | — | — | No | — | Repetition collapse |
16	|   ↳ s44 | — | 0.98 | 0.570±0.201 | 0.582 | 2.04 | **Yes (94%)** | — | Tautological collapse |
17	| **Exec-only 1000步** (plan016) | 1 (s42) | 0.96 | 0.003±0.012 | 0.003 | 18.55 | No | **100%** (H1=96/96) | H1 100%, Genuine 0% (contradiction explosion) |
18	| **ISR β=0.1** (plan002-b01) | 3 | 0.77±0.14 | 0.55±0.24 | 0.716±0.26 | 4.65 | No | 2/3 seeds | ISR-specific gaming |
19	|   ↳ s42 | — | 0.81 | 0.337±0.323 | 0.415 | 5.58 | No | 67.9% | H7 16% + H1 52% |
20	|   ↳ s43 | — | 0.61 | 0.506±0.452 | 0.830 | 4.03 | No | 96.7% | **H7 96.7%** (ISR inflation) |
21	|   ↳ s44 | — | 0.89 | 0.803±0.342 | 0.902 | 4.33 | No | 86.5% | **H7 86.5%** (ISR inflation) |
22	| **Random β=0.1** (plan018) | 2/3§ | 0.84 | 0.083 | 0.100 | 8.46¹ | No | ~75% (H1)⁴ | Redundant premises |
23	|   ↳ s42 | — | 0.79 | 0.104±0.137 | 0.131 | 8.46 | No | 70.9% (H1) | H1 70.9% (56/79), H7 0% |
24	|   ↳ s44 | — | 0.89 | 0.062±0.176 | 0.070 | — | No | 79.8% (H1) | H1 79.8% (71/89), H7 0% |
25	|   ↳ s43 | — | RUNNING | — | — | — | — | — | — |
26	| **ISR β=0.3** (plan002-b03) | 1 (s42) | 0.18 | 0.026±0.074 | 0.143 | — | No | — | Format collapse (Goodhart) |
27	| **Random β=0.3** (plan017) | 1 (s42) | 0.48 | 0.045±0.076 | 0.094 | 9.60 | No | — | Complexity-without-utility |
28	| **Convex random** (plan013-r4) | 1 (s42) | 1.00 | 0.535±0.128 | 0.535 | 2.0 | **Yes (100%)** | 100% | P→P tautological |
29	
30	**Notes:**
31	- † Exec-only 500步 shows extreme seed variance: s42 = conclusion embedding, s43 = repetition collapse, s44 = tautological collapse. 3-seed mean is informative of instability, not a typical outcome.
32	- ‡ s43 eval used `do_sample=True, temperature=0.7` (NOT eval_sta.py). 87% samples hit `max_new_tokens`. ISR=0 not comparable to other seeds (C004 violation in historical data).
33	- § plan018-s43 still RUNNING; 2-seed interim values reported.
34	- ¹ Component count only available for s42.
35	
36	---
37	
38	## Table 2 — Hacking Taxonomy
39	
40	| Condition | Seed | H7 % | H1 % | H7+H1 (total) | Genuine % | n_proved | Premise-matched ISR |
41	|---|---|---|---|---|---|---|---|
42	| **SFT baseline** | s42 | 0% (0/14) | 7.1% (1/14) | 7.1% | **92.9%** (13/14) | 14 | — |
43	| **Exec-only 500步** | s42 | 0% (0/93) | **87.1%** (81/93) | **87.1%** | 12.9% (12/93) | 93 | — |
44	| **Exec-only 500步** | s44 | **100%** (97/97) | 0% | **100%** | 0% (0/97) | 97⁵ | — |
45	| **Exec-only 1000步** | s42 | — | — | — | — | 96 | — |
46	| **ISR β=0.1** | s42 | **16.0%** (13/81) | **51.9%** (42/81) | **67.9%** | **30.9%** (25/81) | 81 | **0.2578** (n≥3 prem) |
47	| **ISR β=0.1** | s43 | **96.7%** (59/61) | 0% | **96.7%** | ~3% (~2/61) | 61 | — |
48	| **ISR β=0.1** | s44 | **86.5%** (77/89) | 0% | **86.5%** | ~13.5% (~12/89)³ | 89 | — |
49	| **Random β=0.1** | s42 | **0%** (0/79) | **70.9%** (56/79) | **70.9%** | **29.1%** (23/79) | 79 | **0.2434** (n≥3 prem) |
50	| **Random β=0.1** | s44 | **0%** (0/89) | **79.8%** (71/89) | **79.8%** | **20.2%** (18/89) | 89 | — |
51	| **Convex random** | s42 | 100%² | 0% | 100% | 0% | 100 | — |
52	
53	**Key findings (D051 framing):**
54	
55	1. **H7 is ISR-specific**: ISR 3-seed H7 mean = 64.5% (149/231), Random H7 = 0%. ISR reward specifically induces premise=conclusion hacking.
56	2. **H1 is GRPO-universal**: Random H1 = 71–80%, ISR s42 H1 = 52%. Conclusion embedding is a general GRPO strategy, not ISR-specific.
57	3. **ISR changes hacking composition, not total**: Overall conclusion-in-premise rate is comparable (ISR 67.9% vs Random 70.9% for s42), but ISR converts H1 → more extreme H7.
58	4. **Premise-count-matched: no structural advantage**: ISR genuine (n_prem≥3) = 0.2578, Random genuine (n_prem≥3) = 0.2434. **Ratio = 1.06×**. The apparent 2.4× raw genuine ISR is entirely a premise minimization artifact.
59	5. **SFT has near-zero hacking** (1/14 H1, 0 H7, 92.9% genuine) → hacking is GRPO/RL-specific, not a general finetuning artifact.
60	
61	**Notes:**
62	- ² Tautological collapse (premise=conclusion, 2-component proofs). Classified separately from H7 (which is conclusion duplication with ISR inflation in multi-step context).
63	- ³ s44's 12 "genuine" samples are all n_prem=1 (H7 classifier false negatives — single premise but normalization difference prevented conclusion match).
64	- H7 = single premise identical to conclusion (ISR-inflating shortcut).
65	- H1 = multi-premise proof with conclusion embedded among premises (GRPO-universal shortcut).
66	- Genuine = proved sample with no conclusion duplication detected.
67	- ⁴ Conclusion Embedding % for Random = H1 rate (H7=0% for all Random seeds). s42: 70.9%, s44: 79.8%.
68	- ⁵ s44 eval_results.json reports 97 proved (vs registry 98). H7=97/97=100%.
69	
70	---
71	
72	## Table 3 — Prolog Cross-Logic (Final)
73	
74	| Condition | Seed | eval PR | eval ISR | proved_only ISR | Components | Hacking Mode |
75	|---|---|---|---|---|---|---|
76	| **Prolog exec-only** | s42 | 0.83 | 0.031 | 0.037 | — | Ground fact enumeration (H7=0%, H1=0%) |
77	| **Prolog exec-only** | s43 | **0.56** | 0.008 | 0.015 | — | Degraded (low PR, near-zero ISR) |
78	| **Prolog exec-only** | s44 | **0.21** | 0.081 | 0.387 | — | Severe degradation (lowest PR, ISR from small sample) |
79	| **Prolog exec-only** | **3-seed mean±std** | **0.53±0.31** | **0.040±0.037** | **0.146±0.210** | — | Extreme seed variance (σ=31pp) |
80	| **Prolog STA (ISR reward)** | s42 | 0.50 | 0.500 | **1.000** | 1.0 | **100% H7** (single clause = query) |
81	| **Prolog STA (ISR reward)** | s43 | **0.38** | 0.070 | 0.185 | — | **Functional H7†** (H1=97.4%, uppercase pseudo-Prolog) |
82	| **Prolog STA (ISR reward)** | s44 | **0.97** | **0.885** | **0.912** | — | **Genuine** (H7=0%, H1=0%, 100% genuine) |
83	| **Prolog STA (ISR reward)** | **3-seed mean±std** | **0.62±0.31** | **0.485±0.408** | **0.699±0.447** | — | 2/3 Goodhart, 1/3 genuine |
84	
85	**Notes:**
86	- † s43 strict classifier shows H7=0%, H1=0%, Genuine=100%. However, functional analysis reveals all 38/38 proved samples are tautological (n_necessary=1). Model generates uppercase pseudo-Prolog (e.g., MARY_IS_AN_AVADEOTE.) — non-standard syntax bypasses strict classifier but achieves same functional outcome as H7 (conclusion embedded as single clause).
87	
88	**Key findings:**
89	
90	1. **Cross-logic replication of ISR-specific gaming**: Prolog STA s42 H7 = 100%, s43 functional H7 = 97.4%. 2/3 seeds show clear Goodhart hacking via different pathways. Prolog model converges to trivial programs where the conclusion is embedded.
91	2. **s44 anomaly — genuine success**: PR=0.97, ISR=0.885, Genuine=100%. Despite training metrics showing Goodhart-like signs (completion compression 127→32 tokens, entropy near zero), eval reveals genuinely structured Prolog programs. This challenges the "universal Goodhart" narrative and suggests seed-dependent bifurcation between hacking and genuine learning.
92	3. **Exec-only Prolog 3-seed**: PR=53.3%±31.1%, ISR=0.040±0.037. Extreme seed variance replicates FOL pattern (FOL exec-only PR=68%±47%).
93	4. **Prolog ISR consistently near-zero (exec-only)**: All 3 seeds ISR<0.1 (mean), confirming exec-only produces no genuine reasoning traces across both logic types.
94	5. **Diverse Goodhart pathways**: s42=clean H7 (single clause=query), s43=functional H7 via non-standard syntax (uppercase pseudo-Prolog), s44=genuine success. ISR-as-reward in Prolog produces heterogeneous outcomes even more extreme than FOL.
95	
96	---
97	
98	## Summary: D051 Claim Support Matrix
99	
100	| Claim | Evidence | Status |
101	|---|---|---|
102	| **C1: ISR as diagnostic** | ISR collapse trajectory: 0.642 (100步) → 0.132 (500步) → 0.003 (1000步) while PR rises 32%→93%→96% | **Supported** (3 timepoints) |
103	| **C2: ISR-as-reward = no structural advantage** | Premise-count-matched ISR: 1.06× (ISR 0.258 vs Random 0.243, n_prem≥3). β=0.1: 2/3 seeds H7>86%. β=0.3: PR 18% < Random 48% | **Supported** (D051 definitive) |
104	| **C2 corollary: hacking composition shift** | ISR: H7=64.5% mean, H1=17%. Random: H7=0%, H1=78%. Total hacking comparable (~70%) | **Supported** |
105	| **SFT = zero hacking** | plan009-r4: PR=14%, ISR=0.08, no hacking patterns detected | **Supported** |
106	| **C3: Cross-logic generality** | Prolog STA 3-seed: s42 H7=100%, s43 functional H7=97.4%, s44 genuine (PR=0.97, ISR=0.885). 2/3 Goodhart, 1/3 genuine. Exec-only 3-seed: PR=53%±31%, ISR=0.040±0.037. | **Supported** (3-seed complete, 2/3 Goodhart confirmed) |
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "fdb996c4-b9c9-4eba-b641-8c042e1563bd"
}
```

</details>

---

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "description": "Reading artifacts/evidence_chain_status.md",
  "usage": {
    "total_tokens": 22581,
    "tool_uses": 6,
    "duration_ms": 5141
  },
  "last_tool_name": "Read",
  "uuid": "71c3345a-3086-4a81-a143-234861429a89",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01EVn91RqLmJ4PL5smnRpGxS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_chain_status.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "6dc521a8-e6cf-45aa-9be5-53080131e8c3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fk8mRiB6biLx6ThhgWACGY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3371,
      "cache_read_input_tokens": 19183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3371,
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

_source line 44 · 2026-05-14T18:50:53.047Z_

<details><summary>↩ Tool result · `toolu_01EVn91RqLmJ4PL5smnRpGxS`</summary>

```text
1	# Evidence Chain Status — solver-trace-ablation
2	
3	**Generated**: 2026-05-14
4	**Source**: registry (50 experiments total, filtered to evidence-bearing runs)
5	**Eval standard**: eval_sta.py full STA on proofwriter_fol_100.jsonl (FOL) / Prolog eval (Prolog)
6	
7	---
8	
9	## Claim 1 — Exec-only GRPO causes ISR collapse / reward hacking
10	
11	**Status: COMPLETE (3-seed FOL evidence + extended-horizon confirmation)**
12	
13	| Exp ID | Seed | Steps | Eval PR | Eval ISR | Components | Failure Mode | Status |
14	|--------|------|-------|---------|----------|------------|--------------|--------|
15	| plan001-exec-only-s42-r2 | 42 | 500 | 0.93 | 0.123 | 6.58 | partial-genuine (best seed) | ✅ DONE |
16	| plan001-exec-only-s43-r4 | 43 | 500 | 0.14 | 0.00 | n/a | degraded (87% hit max_tokens) | ✅ DONE† |
17	| plan001-exec-only-s44   | 44 | 500 | 0.98 | 0.57 | 2.04 | tautological collapse (94% 2-comp) | ✅ DONE |
18	| plan016-extended-1000-s42 | 42 | 1000 | 0.96 | 0.0027 | 18.55 | contradiction explosion (94.8% ISR=0) | ✅ DONE |
19	
20	**3-seed result**: 1/3 partial-genuine (s42), 1/3 degraded (s43), 1/3 tautological (s44). PR mean=0.683 std=0.467; ISR mean=0.231 std=0.314 — extreme cross-seed variance.
21	
22	**Extended-horizon finding**: At 1000 steps, PR keeps climbing (+3pp) while ISR collapses 97.8% (0.123→0.0027). Windowed ISR is monotonically decreasing (0.1115→0.0144). 500-step ISR was not a floor, it was mid-collapse.
23	
24	†Note: plan001-s43-r4 used sampling eval (T=0.7), not eval_sta.py. PR=14% is unambiguous failure regardless of eval method (D029). **Mark in paper.**
25	
26	---
27	
28	## Claim 2 — ISR β=0.1 additive bonus + Goodhart risk
29	
30	**Status: NEAR-COMPLETE (1 cell remaining: random β=0.1 s43)**
31	
32	### ISR β=0.1 additive (r = r_exec·(1+0.1·ISR))
33	
34	| Exp ID | Seed | Eval PR | Eval ISR | H7% | Component mean | Hacking mode | Status |
35	|--------|------|---------|----------|-----|----------------|--------------|--------|
36	| plan002-additive-b01-s42 | 42 | 0.81 | 0.337 | n/a | 5.58 | partial-genuine (best) | ✅ DONE |
37	| plan002-additive-b01-s43 | 43 | 0.61 | 0.506 | 96.7% | 4.03 | conclusion duplication | ✅ DONE |
38	| plan002-additive-b01-s44 | 44 | 0.89 | 0.803 | 86.5% | 4.33 | conclusion duplication | ✅ DONE |
39	
40	**3-seed status**: ✅ all three eval'd. 2/3 hacking via conclusion duplication (premise≈conclusion, single-premise inflates ISR).
41	
42	### Random β=0.1 control (variance regularization baseline)
43	
44	| Exp ID | Seed | Eval PR | Eval ISR | Component mean | Status |
45	|--------|------|---------|----------|----------------|--------|
46	| plan018-random-b01-s42 | 42 | 0.79 | 0.104 | 8.46 | ✅ DONE |
47	| plan018-random-b01-s43 | 43 | — | — | — | ⏳ ALLOCATED (r2 retry; r1 disk-full @ step 200) |
48	| plan018-random-b01-s44 | 44 | 0.89 | 0.062 | n/a | ✅ DONE |
49	
50	**ISR vs Random @ β=0.1 contrast (s42)**: PR 0.81 vs 0.79 (≈match); ISR 0.337 vs 0.104 (**3.2× higher**). Same PR, very different ISR → ISR signal is structural, not variance-noise. Replicated at s44 (0.803 vs 0.062 = 13×, but s44 ISR inflated by hacking).
51	
52	### Higher-dose collapse (β=0.3)
53	
54	| Exp ID | Seed | Eval PR | Eval ISR | Status | Notes |
55	|--------|------|---------|----------|--------|-------|
56	| plan002-additive-b03-s42 | 42 | 0.340 (overall) / 0.553 (last100) | 0.309 (final) | ✅ DONE | not saturated; PR collapse |
57	| plan017-random-b03-s42 | 42 | 0.48 | 0.045 | ✅ DONE | complexity-without-utility |
58	
59	### Supporting cells
60	
61	| Exp ID | Result | Role | Status |
62	|--------|--------|------|--------|
63	| plan012-hacking-taxonomy | ISR genuine +8.2pp, ISR conclusion-embedding 72.8% vs Random 78.5%, ISR eliminates complexity-w/o-utility hacking | hacking taxonomy quantification | ✅ DONE |
64	| plan009-sft-baseline-s42-r4 | PR=0.14, ISR=0.08, proved-only ISR=0.571, hacking=none | confirms hacking is GRPO-specific not finetuning artifact | ✅ DONE |
65	
66	**Remaining gap**: plan018-random-b01-s43 (ALLOCATED → run). Needed for 3-seed mean±std on random control. Without it, single-seed random comparisons at s43 not possible.
67	
68	---
69	
70	## Claim 3 — Cross-logic generalization (Prolog)
71	
72	**Status: PARTIAL (s42 complete; s43/s44 in progress)**
73	
74	### Prolog exec-only
75	
76	| Exp ID | Seed | Eval PR | Eval ISR | H7% | Failure Mode | Status |
77	|--------|------|---------|----------|-----|--------------|--------|
78	| plan006-prolog-exec-s42 | 42 | 0.83 | 0.031 | 0% | ground-fact enumeration (C006 redundancy) | ✅ DONE |
79	| plan006-prolog-exec-s43-r3 | 43 | — | — | — | — | ⏳ RUNNING (cuda:1, PID 483820) |
80	| plan006-prolog-exec-s44 | 44 | — | — | — | — | ⏳ RUNNING (cuda:0, PID 479357) |
81	
82	### Prolog exec+STA (ISR-as-reward)
83	
84	| Exp ID | Seed | Eval PR | Eval ISR | H7% | Failure Mode | Status |
85	|--------|------|---------|----------|-----|--------------|--------|
86	| plan006-prolog-sta-s42 | 42 | 0.50 | 1.0 (proved-only) | 100% | single-clause query (Goodhart) | ✅ DONE |
87	| plan006-prolog-sta-s43 | 43 | — | — | — | — | 🔜 PREPARING (waiting GPU) |
88	| plan006-prolog-sta-s44 | 44 | — | — | — | — | 🔜 PREPARING (waiting GPU) |
89	
90	**s42 cross-type finding**: exec-only Prolog (PR=0.83, ISR=0.031) vs exec-only FOL (PR=0.93, ISR=0.12) — Prolog ISR even lower, but via different mechanism (C006: ground-fact redundancy n_necessary=0, not contradiction explosion). exec+STA Prolog (ISR=1.0, H7=100%) vs exec+STA FOL — Prolog Goodhart is more extreme (100% single-clause vs FOL ~65–97% conclusion duplication).
91	
92	**Gap**: 4 of 6 Prolog runs incomplete. Cannot claim 3-seed cross-logic generalization until s43/s44 land for both conditions.
93	
94	---
95	
96	## Overall evidence chain summary
97	
98	| Claim | FOL 3-seed | Prolog 3-seed | Confirmatory | Verdict |
99	|-------|-----------|---------------|--------------|---------|
100	| C1: Exec-only ISR collapse | ✅ complete | ⏳ 1/3 (s42 only) | ✅ Extended-1000 confirms worsening | **FOL: ready** / Prolog: waiting |
101	| C2: ISR β=0.1 + Goodhart | ✅ ISR 3/3, ⏳ Random 2/3 | n/a (single Prolog STA seed) | ✅ Hacking taxonomy, ✅ SFT control, ✅ β=0.3 dose-response | **Near-ready** (1 cell) |
102	| C3: Cross-logic | n/a | ⏳ 1/3 exec, 1/3 STA | s42 contrast solid | **Partial** (4 runs pending) |
103	
104	## Blocking items
105	
106	1. **plan018-random-b01-s43-r2** — ALLOCATED, needs execution. Required for 3-seed random control mean±std.
107	2. **plan006-prolog-exec-s43-r3** — RUNNING. Monitor for completion + eval_sta.py.
108	3. **plan006-prolog-exec-s44** — RUNNING. Monitor for completion + eval_sta.py.
109	4. **plan006-prolog-sta-s43 / s44** — PREPARING, blocked on GPU. Queue once exec runs finish.
110	
111	## Non-blocking notes for paper
112	
113	- All cross-run ISR comparisons must use eval_sta.py numbers (C004). Training-log ISR for plan001-s42-r2, plan002-b03-s42, plan013 was `_fast_fn` binary approximation — DO NOT cite.
114	- Prolog ISR semantics differ from FOL ISR (C006). Paper must distinguish: exec-only low ISR (Prolog) = redundancy; exec+STA high ISR (Prolog) = Goodhart. Reviewer flagged this explicitly.
115	- plan001-s43-r4 eval used sampling (T=0.7), not eval_sta.py (D029). Footnote in Table 1.
116	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "5d6b8a39-d3fa-47e1-9261-e95bd7913903"
}
```

</details>

---

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "description": "Reading artifacts/_project/report/evidence_chain_status.md",
  "usage": {
    "total_tokens": 22582,
    "tool_uses": 7,
    "duration_ms": 6033
  },
  "last_tool_name": "Read",
  "uuid": "8feabefa-e117-4b28-9b98-db90bb374691",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01KeghAujcw9kWk3Uyq2dSLT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/evidence_chain_status.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "d9e787f8-417e-4f93-8e4d-55b587ef4499",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fk8mRiB6biLx6ThhgWACGY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3371,
      "cache_read_input_tokens": 19183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3371,
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

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "description": "Reading artifacts/_project/report/evidence_audit.md",
  "usage": {
    "total_tokens": 22583,
    "tool_uses": 8,
    "duration_ms": 6038
  },
  "last_tool_name": "Read",
  "uuid": "e54ffa55-3e6e-4001-83f1-b2b50d2c462d",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01QT1uaHs7o3dvdCqcpWg64t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/evidence_audit.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "0e281bb9-b649-4f92-8764-4ef690c4ffd7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fk8mRiB6biLx6ThhgWACGY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3371,
      "cache_read_input_tokens": 19183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3371,
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

_source line 49 · 2026-05-14T18:50:53.943Z_

<details><summary>↩ Tool result · `toolu_01KeghAujcw9kWk3Uyq2dSLT`</summary>

```text
1	# Evidence Chain Status — solver-trace-ablation
2	
3	**Generated**: 2026-05-14
4	**Source**: registry (50 experiments total, filtered to evidence-bearing runs)
5	**Eval standard**: eval_sta.py full STA on proofwriter_fol_100.jsonl (FOL) / Prolog eval (Prolog)
6	
7	---
8	
9	## Claim 1 — Exec-only GRPO causes ISR collapse / reward hacking
10	
11	**Status: COMPLETE (3-seed FOL evidence + extended-horizon confirmation)**
12	
13	| Exp ID | Seed | Steps | Eval PR | Eval ISR | Components | Failure Mode | Status |
14	|--------|------|-------|---------|----------|------------|--------------|--------|
15	| plan001-exec-only-s42-r2 | 42 | 500 | 0.93 | 0.123 | 6.58 | partial-genuine (best seed) | ✅ DONE |
16	| plan001-exec-only-s43-r4 | 43 | 500 | 0.14 | 0.00 | n/a | degraded (87% hit max_tokens) | ✅ DONE† |
17	| plan001-exec-only-s44   | 44 | 500 | 0.98 | 0.57 | 2.04 | tautological collapse (94% 2-comp) | ✅ DONE |
18	| plan016-extended-1000-s42 | 42 | 1000 | 0.96 | 0.0027 | 18.55 | contradiction explosion (94.8% ISR=0) | ✅ DONE |
19	
20	**3-seed result**: 1/3 partial-genuine (s42), 1/3 degraded (s43), 1/3 tautological (s44). PR mean=0.683 std=0.467; ISR mean=0.231 std=0.314 — extreme cross-seed variance.
21	
22	**Extended-horizon finding**: At 1000 steps, PR keeps climbing (+3pp) while ISR collapses 97.8% (0.123→0.0027). Windowed ISR is monotonically decreasing (0.1115→0.0144). 500-step ISR was not a floor, it was mid-collapse.
23	
24	†Note: plan001-s43-r4 used sampling eval (T=0.7), not eval_sta.py. PR=14% is unambiguous failure regardless of eval method (D029). **Mark in paper.**
25	
26	---
27	
28	## Claim 2 — ISR β=0.1 additive bonus + Goodhart risk
29	
30	**Status: NEAR-COMPLETE (1 cell remaining: random β=0.1 s43)**
31	
32	### ISR β=0.1 additive (r = r_exec·(1+0.1·ISR))
33	
34	| Exp ID | Seed | Eval PR | Eval ISR | H7% | Component mean | Hacking mode | Status |
35	|--------|------|---------|----------|-----|----------------|--------------|--------|
36	| plan002-additive-b01-s42 | 42 | 0.81 | 0.337 | n/a | 5.58 | partial-genuine (best) | ✅ DONE |
37	| plan002-additive-b01-s43 | 43 | 0.61 | 0.506 | 96.7% | 4.03 | conclusion duplication | ✅ DONE |
38	| plan002-additive-b01-s44 | 44 | 0.89 | 0.803 | 86.5% | 4.33 | conclusion duplication | ✅ DONE |
39	
40	**3-seed status**: ✅ all three eval'd. 2/3 hacking via conclusion duplication (premise≈conclusion, single-premise inflates ISR).
41	
42	### Random β=0.1 control (variance regularization baseline)
43	
44	| Exp ID | Seed | Eval PR | Eval ISR | Component mean | Status |
45	|--------|------|---------|----------|----------------|--------|
46	| plan018-random-b01-s42 | 42 | 0.79 | 0.104 | 8.46 | ✅ DONE |
47	| plan018-random-b01-s43 | 43 | — | — | — | ⏳ ALLOCATED (r2 retry; r1 disk-full @ step 200) |
48	| plan018-random-b01-s44 | 44 | 0.89 | 0.062 | n/a | ✅ DONE |
49	
50	**ISR vs Random @ β=0.1 contrast (s42)**: PR 0.81 vs 0.79 (≈match); ISR 0.337 vs 0.104 (**3.2× higher**). Same PR, very different ISR → ISR signal is structural, not variance-noise. Replicated at s44 (0.803 vs 0.062 = 13×, but s44 ISR inflated by hacking).
51	
52	### Higher-dose collapse (β=0.3)
53	
54	| Exp ID | Seed | Eval PR | Eval ISR | Status | Notes |
55	|--------|------|---------|----------|--------|-------|
56	| plan002-additive-b03-s42 | 42 | 0.340 (overall) / 0.553 (last100) | 0.309 (final) | ✅ DONE | not saturated; PR collapse |
57	| plan017-random-b03-s42 | 42 | 0.48 | 0.045 | ✅ DONE | complexity-without-utility |
58	
59	### Supporting cells
60	
61	| Exp ID | Result | Role | Status |
62	|--------|--------|------|--------|
63	| plan012-hacking-taxonomy | ISR genuine +8.2pp, ISR conclusion-embedding 72.8% vs Random 78.5%, ISR eliminates complexity-w/o-utility hacking | hacking taxonomy quantification | ✅ DONE |
64	| plan009-sft-baseline-s42-r4 | PR=0.14, ISR=0.08, proved-only ISR=0.571, hacking=none | confirms hacking is GRPO-specific not finetuning artifact | ✅ DONE |
65	
66	**Remaining gap**: plan018-random-b01-s43 (ALLOCATED → run). Needed for 3-seed mean±std on random control. Without it, single-seed random comparisons at s43 not possible.
67	
68	---
69	
70	## Claim 3 — Cross-logic generalization (Prolog)
71	
72	**Status: PARTIAL (s42 complete; s43/s44 in progress)**
73	
74	### Prolog exec-only
75	
76	| Exp ID | Seed | Eval PR | Eval ISR | H7% | Failure Mode | Status |
77	|--------|------|---------|----------|-----|--------------|--------|
78	| plan006-prolog-exec-s42 | 42 | 0.83 | 0.031 | 0% | ground-fact enumeration (C006 redundancy) | ✅ DONE |
79	| plan006-prolog-exec-s43-r3 | 43 | — | — | — | — | ⏳ RUNNING (cuda:1, PID 483820) |
80	| plan006-prolog-exec-s44 | 44 | — | — | — | — | ⏳ RUNNING (cuda:0, PID 479357) |
81	
82	### Prolog exec+STA (ISR-as-reward)
83	
84	| Exp ID | Seed | Eval PR | Eval ISR | H7% | Failure Mode | Status |
85	|--------|------|---------|----------|-----|--------------|--------|
86	| plan006-prolog-sta-s42 | 42 | 0.50 | 1.0 (proved-only) | 100% | single-clause query (Goodhart) | ✅ DONE |
87	| plan006-prolog-sta-s43 | 43 | — | — | — | — | 🔜 PREPARING (waiting GPU) |
88	| plan006-prolog-sta-s44 | 44 | — | — | — | — | 🔜 PREPARING (waiting GPU) |
89	
90	**s42 cross-type finding**: exec-only Prolog (PR=0.83, ISR=0.031) vs exec-only FOL (PR=0.93, ISR=0.12) — Prolog ISR even lower, but via different mechanism (C006: ground-fact redundancy n_necessary=0, not contradiction explosion). exec+STA Prolog (ISR=1.0, H7=100%) vs exec+STA FOL — Prolog Goodhart is more extreme (100% single-clause vs FOL ~65–97% conclusion duplication).
91	
92	**Gap**: 4 of 6 Prolog runs incomplete. Cannot claim 3-seed cross-logic generalization until s43/s44 land for both conditions.
93	
94	---
95	
96	## Overall evidence chain summary
97	
98	| Claim | FOL 3-seed | Prolog 3-seed | Confirmatory | Verdict |
99	|-------|-----------|---------------|--------------|---------|
100	| C1: Exec-only ISR collapse | ✅ complete | ⏳ 1/3 (s42 only) | ✅ Extended-1000 confirms worsening | **FOL: ready** / Prolog: waiting |
101	| C2: ISR β=0.1 + Goodhart | ✅ ISR 3/3, ⏳ Random 2/3 | n/a (single Prolog STA seed) | ✅ Hacking taxonomy, ✅ SFT control, ✅ β=0.3 dose-response | **Near-ready** (1 cell) |
102	| C3: Cross-logic | n/a | ⏳ 1/3 exec, 1/3 STA | s42 contrast solid | **Partial** (4 runs pending) |
103	
104	## Blocking items
105	
106	1. **plan018-random-b01-s43-r2** — ALLOCATED, needs execution. Required for 3-seed random control mean±std.
107	2. **plan006-prolog-exec-s43-r3** — RUNNING. Monitor for completion + eval_sta.py.
108	3. **plan006-prolog-exec-s44** — RUNNING. Monitor for completion + eval_sta.py.
109	4. **plan006-prolog-sta-s43 / s44** — PREPARING, blocked on GPU. Queue once exec runs finish.
110	
111	## Non-blocking notes for paper
112	
113	- All cross-run ISR comparisons must use eval_sta.py numbers (C004). Training-log ISR for plan001-s42-r2, plan002-b03-s42, plan013 was `_fast_fn` binary approximation — DO NOT cite.
114	- Prolog ISR semantics differ from FOL ISR (C006). Paper must distinguish: exec-only low ISR (Prolog) = redundancy; exec+STA high ISR (Prolog) = Goodhart. Reviewer flagged this explicitly.
115	- plan001-s43-r4 eval used sampling (T=0.7), not eval_sta.py (D029). Footnote in Table 1.
116	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "a0dc8a0f-df81-4c78-a4aa-a2ad13d48d34"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T18:50:53.945Z_

<details><summary>↩ Tool result · `toolu_01QT1uaHs7o3dvdCqcpWg64t`</summary>

```text
1	# Evidence Audit — solver-trace-ablation
2	Generated: 2026-05-14 (D044 strict定义 + plan006 Prolog + plan016 1000步 + H7 6-mode taxonomy)
3	
4	---
5	
6	## 1. Table 1: Six-Condition Comparison (Registry-Verified)
7	
8	All metrics sourced from `eval_sta.py full STA` on `proofwriter_fol_100.jsonl` unless noted.
9	
10	| # | Condition | exp_id | Reward Formula | eval PR | eval ISR | proved_only_ISR | n_components | Degeneration Mode |
11	|---|-----------|--------|----------------|---------|----------|-----------------|--------------|-------------------|
12	| 1 | Exec-only s42 | `plan001-exec-only-s42-r2` | r_exec | 93% | 0.1232 | 0.1324 | **6.58 ⚠️** | Genuine (only healthy seed) |
13	| 2 | Exec-only s43 | `plan001-exec-only-s43-r4` | r_exec | **14% ⚠️** | 0.000 | 0.000 | **N/A ⚠️** | Length explosion (87% hit max_tokens) |
14	| 3 | Exec-only s44 | `plan001-exec-only-s44` | r_exec | 98% | 0.5700 | 0.5816 | 2.04 | Tautological (94/100 = 2-component) |
15	| 4 | Random reward | `plan013-random-reward-s42-r4` | 0.9·r_exec + 0.1·random | 100% | 0.5350 | 0.5350 | **~2.0 ⚠️** | Tautological (100% P→P) |
16	| 5 | Additive ISR β=0.3 | `plan002-additive-b03-s42` | r_exec·(1+0.3·ISR) | 18% | 0.0257 | 0.1427 | **N/A ⚠️** | Format collapse |
17	| 6 | Additive random β=0.3 | `plan017-additive-random-s42` | r_exec·(1+0.3·random) | 48% | 0.0453 | 0.0943 | 9.60 | Complexity-without-utility |
18	
19	### Discrepancies & Missing Data
20	
21	#### ❌ plan001-s43 eval PR: 14% not 13%
22	- Registry: `eval_sampling_prove_rate=0.14`, `eval_sampling_n_proved=14` → **14%**
23	- 论文必须使用 14%
24	
25	#### ⚠️ plan001-s43 eval method 不一致
26	- s43 使用 `eval_sampling` (do_sample=True, temperature=0.7)
27	- 其他 5 组全部使用 `eval_sta.py full STA` (deterministic)
28	- **论文中必须标注 s43 的评估方法差异**
29	
30	#### ⚠️ n_components 数据追溯
31	| Condition | In Registry? | Source |
32	|-----------|-------------|--------|
33	| plan001-s42 (6.58) | ❌ 不在 registry metrics 中 | 需追溯来源 |
34	| plan001-s43 (N/A) | ❌ 无评估数据 | s43 未做 component count 评估 |
35	| plan001-s44 (2.04) | ✅ `eval_component_count_mean=2.04` | Registry |
36	| plan013 (~2.0) | ❌ 仅在 eval_note 中提及 | 需补入 registry |
37	| plan017 (9.60) | ✅ `eval_component_count_mean=9.6` | Registry |
38	
39	---
40	
41	## 2. Table 2: Hacking Taxonomy (D044 Strict定义)
42	
43	ISR β=0.1 (plan002-b01-s42) vs Random β=0.1 (plan018-random-b01-s42). 所有类别使用 strict exact normalized match (classify_h7.py 可复现, D044)。
44	
45	| Mode | Name | ISR β=0.1 | Random β=0.1 | Δ (pp) |
46	|------|------|-----------|--------------|--------|
47	| H1 | Conclusion Embedding | 51.9% (42/81) | 70.9% (56/79) | −19.0 |
48	| H3 | Tautological Collapse | 1.2% (1/81) | 0.0% (0/79) | +1.2 |
49	| H4 | Complexity w/o Utility | 0.0% (0/81) | 3.8% (3/79) | −3.8 |
50	| H7 | Conclusion Duplication† | 16.0% (13/81) | 0.0% (0/79) | +16.0 |
51	| | **Genuine proofs** | **30.9% (25/81)** | **25.3% (20/79)** | **+5.6** |
52	| | **Total hacking** | **69.1% (56/81)** | **74.7% (59/79)** | **−5.6** |
53	
54	† H7 = single_premise AND premise==conclusion (normalized). ISR-specific mode.
55	  Multi-seed prevalence under ISR β=0.1: s42=16.0% (13/81), s43=96.7% (59/61), s44=86.5% (77/89); pooled=64.5% (149/231).
56	  Random β=0.1: 0/79 (0%).
57	
58	### H7 Hacking Taxonomy: 6 Modes (Updated from 5)
59	
60	| # | Mode | 典型实验 | 特征 | 检测信号 |
61	|---|------|---------|------|----------|
62	| H1 | Conclusion Embedding | plan001-s42, plan018-random | conclusion 嵌入 premises (multi-premise) | any(premise==conclusion) AND len(premises)>1 |
63	| H2 | Repetition Collapse | plan001-s43 | 重复生成相同 premise | PR=14%, 87% max_tokens |
64	| H3 | Tautological Collapse | plan001-s44, plan013 | 2-component P→P | component_count=2, ISR≈0.5 |
65	| H4 | Complexity-without-utility | plan017 | 多 components 但无 necessary | high components, ISR≈0 |
66	| H5 | Premise Padding | plan017 | 无关 premises 填充 | n_necessary=0 |
67	| H7 | Conclusion Duplication + ISR Inflation | plan002-b01-s43/s44 | 单 premise = conclusion, game exec+ISR | single_premise AND premise==conclusion |
68	
69	---
70	
71	## 3. 证据覆盖审计：3 Claims
72	
73	### Claim 1: ISR as Reward Hacking Diagnostic
74	
75	**状态：✅ 证据充分**
76	
77	| 证据点 | 支撑实验 | Registry 可追溯 | 状态 |
78	|--------|---------|----------------|------|
79	| ISR 崩塌轨迹：0.6423→0.1324→0.0027 | plan003 (100步) + plan001-s42 (500步) + **plan016** (1000步) | ✅ 全部在 registry | **完整（含 1000 步延长）** |
80	| Base model ISR anchor | sta-phase0-baseline | ✅ mean_isr=0.0641 | 完整 |
81	| 3-seed 分化 | plan001-s42-r2, s43-r4, s44 | ✅ eval metrics 均在 | 完整 |
82	| **plan016 延长训练** | plan016-extended-1000-s42 | ✅ eval_PR=0.96, eval_ISR=0.0028, comp=18.55 | **完整 — ISR 单调递减，94.8% ISR=0** |
83	| **Hacking taxonomy (6 modes)** | plan012 + D043 + D044 | ✅ classify_h7.py 可复现 | **完整 — 含 H7 strict 定义** |
84	| Component count 辅助诊断 | 见 Table 1 | ⚠️ 2/6 组缺 registry 来源 | 部分缺失 |
85	
86	### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart
87	
88	**状态：✅ 证据充分（多 seed + random 对照齐全）**
89	
90	| 证据点 | 支撑实验 | Registry 可追溯 | 状态 |
91	|--------|---------|----------------|------|
92	| **ISR β=0.1 s42 genuine** | plan002-additive-b01-s42 | ✅ PR=0.81, ISR=0.415, H7=16% | **完整** |
93	| **ISR β=0.1 s43 H7 hacking** | plan002-additive-b01-s43 | ✅ PR=0.61, H7=96.7% | **完整 (negative)** |
94	| **ISR β=0.1 s44 H7 hacking** | plan002-additive-b01-s44 | ✅ PR=0.89, H7=86.5% | **完整 (negative)** |
95	| **Random β=0.1 s42 控制** | plan018-additive-random-b01-s42 | ✅ PR=0.79, ISR=0.131, H7=0% | **完整 — ISR-specific hacking 确认** |
96	| ISR β=0.3 Goodhart collapse | plan002-additive-b03-s42 | ✅ PR=0.18 | 完整 |
97	| Random β=0.3 控制 | plan017-additive-random-s42 | ✅ PR=0.48 | 完整 |
98	| Convex combination penalty | plan005-sta-low-s42 | ✅ train metrics only | 完整 (train-only) |
99	| Convex random tautological | plan013-random-reward-s42-r4 | ✅ PR=1.0, ISR=0.535 fake | 完整 |
100	
101	**写作约束 (D027)**: plan013 vs plan017 公式不同，不可简化为 "additive vs convex"。
102	
103	**多 seed 关键发现 (D043)**:
104	- ISR β=0.1 3-seed: 1/3 genuine (s42), 2/3 H7 gaming (s43: 96.7%, s44: 86.5%)
105	- Random β=0.1: 0% H7 → 确认 H7 是 ISR-specific
106	- H7 pooled proportion: 149/231 = 64.5%
107	- 总 hacking rate (strict D044): ISR 69.1% vs random 74.7%
108	
109	### Claim 3: Cross-Logic Generality
110	
111	**状态：⚠️ 初步数据已有（1/2 实验完成）**
112	
113	| 证据点 | 支撑实验 | Registry 可追溯 | 状态 |
114	|--------|---------|----------------|------|
115	| **Prolog exec+STA (ISR reward)** | plan006-prolog-sta-s42 | ✅ DONE (negative) | **完整 — 100% H7, step ~100 饱和, ISR gaming 比 FOL 更极端** |
116	| Prolog exec-only (baseline) | plan006-prolog-exec-s42 | ⏳ RUNNING (cuda:0, PID 506015) | **训练中** |
117	| Prolog 多 seed | plan006 s43/s44 | PREPARING | 未启动 |
118	
119	**plan006-prolog-sta-s42 eval 结果**:
120	- eval PR = 50%, proved-only ISR = 1.0 (完美二值: 50×0 + 50×1)
121	- **100% proved 样本是 H7**（单 clause = query，零推理）
122	- 50% 失败源于格式解析错误，非策略差异
123	- Prolog H7=100% vs FOL s42=16% → Prolog 语义更简单 → hacking 更快更彻底
124	- 饱和速度: Prolog ~100 步 vs FOL ~500 步
125	
126	**论文可 claim**:
127	- ISR gaming 跨 logic type 泛化（FOL + Prolog）
128	- 更简单的 logic 语义 → 更快更完全的 hacking
129	- 待 exec-only 对照完成后可量化 ISR reward 的增量影响
130	
131	---
132	
133	## 4. 辅助实验证据
134	
135	| 实验 | exp_id | 结论 | 论文用途 |
136	|------|--------|------|---------|
137	| Base model baseline | `sta-phase0-baseline` | PR=12%, ISR=0.064 | ISR 起点锚定 |
138	| 100-step eval | `plan003-eval-exec-only-r5` | PR=32%, proved_ISR=0.642 | ISR 崩塌前的高点 |
139	| **1000-step extended** | `plan016-extended-1000-s42` | **PR=96%, ISR=0.0028, comp=18.55** | **ISR 崩塌持续恶化 — 矛盾爆炸** |
140	| Convex combination | `plan005-sta-low-s42` | PR=77% (train), ISR=0.230 | ISR penalty 效应 |
141	| Downstream NLI | `plan014-downstream-nli-s42` | ρ=-0.049, not significant | ISR capability boundary (Limitation) |
142	| GT ISR baseline | `sta-gt-isr-baseline` | GT ISR=0.559, PR=18% | Ground truth 参照 |
143	
144	---
145	
146	## 5. 论文写作可立即启动的章节
147	
148	以下章节的证据已完整：
149	
150	1. **Introduction + Problem Statement** — plan001 3-seed 分化 + ISR 崩塌轨迹 (100/500/1000 步)
151	2. **Method (STA/ISR 定义)** — 纯方法论
152	3. **Results §4.1: ISR Diagnostic** (Claim 1) — ISR 崩塌轨迹完整，plan016 1000步确认
153	4. **Results §4.2: Goodhart Analysis** (Claim 2) — β=0.1/0.3 × ISR/random 全部齐全，3-seed H7 + random 对照
154	5. **Results §4.3: Hacking Taxonomy** — 6 modes (含 H7), strict 定义 D044, classify_h7.py 可复现
155	6. **Results §4.4: Cross-Logic** (Claim 3) — ⚠️ 初步可写: prolog-sta 100% H7 已出，等 prolog-exec 对照
156	7. **Discussion: ISR Capability Boundary** — plan014 negative result
157	8. **Related Work** — literature_map.yaml 33 refs
158	
159	**暂缓**：
160	- §4.4 完整版 → 等 plan006-prolog-exec-s42 + 多 seed
161	
162	---
163	
164	## 6. 待完成实验
165	
166	| 实验 | 状态 | 预期贡献 |
167	|------|------|---------|
168	| **plan009-sft-baseline-s42** | **PENDING (P1)** | **SFT baseline — 审稿人三档均指出缺此对比。区分 GRPO-specific hacking vs 通用微调 artifact。Qwen2.5-1.5B, 500步, cuda:1** |
169	| plan006-prolog-exec-s42 | ⏳ RUNNING (cuda:0) | Claim 3: Prolog exec-only baseline |
170	| plan018-random-b01-s43 | QUEUED (降优先级) | Claim 2: 多 seed random 对照 |
171	| plan018-random-b01-s44 | QUEUED (降优先级) | Claim 2: 多 seed random 对照 |
172	| plan006-prolog-exec-s43 | PREPARING | Claim 3: 多 seed |
173	| plan006-prolog-sta-s43 | PREPARING | Claim 3: 多 seed |
174	| plan006-prolog-exec-s44 | PREPARING | Claim 3: 多 seed |
175	| plan006-prolog-sta-s44 | PREPARING | Claim 3: 多 seed |
176	
177	---
178	
179	## 7. 行动建议（按优先级）
180	
181	1. **[P1]** plan009 SFT baseline 审批通过后立即在 cuda:1 启动 — 审稿 gap
182	2. **[P1]** plan006-prolog-exec-s42 完成后立即 eval → Claim 3 exec vs ISR 对照
183	3. **[P2]** 追溯 plan001-s42 和 plan013 的 component count 来源，补入 registry
184	4. **[P2]** 修正所有引用 "s43 PR=13%" 的地方为 **14%**
185	5. **[P3]** plan018 random 多 seed（已被 SFT baseline 降优先级）
186	6. **[论文]** 开始写 §4.4 Cross-Logic 初稿（prolog-sta 数据已足够开篇）
187	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "1e2270e8-1d0c-4d1b-b90b-ac8d7aad4a4a"
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "description": "Reading artifacts/paper_table1_evidence.md",
  "usage": {
    "total_tokens": 22584,
    "tool_uses": 9,
    "duration_ms": 6098
  },
  "last_tool_name": "Read",
  "uuid": "bb76689f-847a-43b6-b86b-5f784e0ab5ab",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01J7BZNAYWJb2SGVDHywefTk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/paper_table1_evidence.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "3fcf2960-75af-4dc7-b6c4-b20f24e03b62",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fk8mRiB6biLx6ThhgWACGY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3371,
      "cache_read_input_tokens": 19183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3371,
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

_source line 53 · 2026-05-14T18:50:54.011Z_

<details><summary>↩ Tool result · `toolu_01J7BZNAYWJb2SGVDHywefTk`</summary>

```text
1	# Table 1: Comprehensive Experimental Evidence for Solver-Trace Ablation
2	
3	**Model**: Qwen3-4B | **Training**: GRPO, 500 steps, K=8 | **Data**: train_500_seed42.jsonl (500 problems) | **Eval**: proofwriter_fol_100.jsonl (100 problems)
4	
5	## Main Results Table
6	
7	### Group A: Reference Baselines
8	
9	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
10	|---|---|---|---|---|---|---|---|---|---|---|---|---|
11	| sta-phase0-baseline | — (base model) | — | — | — | 0.12 | 0.0641 | 0.1983 | — | — | eval_sta.py | pre-training reference | — |
12	| sta-gt-isr-baseline | — (ground truth FOL) | — | — | — | 0.18 | 0.5588 | 0.2582 | — | — | direct computation | ISR ceiling on gold FOL | — |
13	
14	### Group B: Exec-Only Reward (r = r_exec)
15	
16	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
17	|---|---|---|---|---|---|---|---|---|---|---|---|---|
18	| plan001-exec-only-s42-r2 | exec-only | r = r_exec | — | 42 | 0.93 | 0.1232 | 0.1887 | 6.58† | — | eval_sta.py | genuine proofs | C1 |
19	| plan001-exec-only-s43-r4 | exec-only | r = r_exec | — | 43 | 0.14‡ | 0.00‡ | — | — | — | sampling (T=0.7)‡ | degraded (87% max_tokens) | C1, C2 |
20	| plan001-exec-only-s44 | exec-only | r = r_exec | — | 44 | 0.98 | 0.5700 | 0.2013 | 2.04 | 94% | eval_sta.py | tautological collapse | C1, C2 |
21	
22	**Exec-only 3-seed summary**: mean PR = 0.68 ± 0.47, 2/3 seeds degenerate. Cross-seed instability is the primary finding.
23	
24	### Group C: Additive ISR Bonus (r = r_exec · (1 + β · ISR))
25	
26	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
27	|---|---|---|---|---|---|---|---|---|---|---|---|---|
28	| plan002-additive-b03-s42 | additive ISR | r = r_exec · (1 + β·ISR) | 0.3 | 42 | 0.18 | 0.0257 | 0.0742 | — | — | eval_sta.py§ | PR collapse (Goodhart) | C3 |
29	| plan002-additive-b01-s42 | additive ISR | r = r_exec · (1 + β·ISR) | 0.1 | 42 | 0.81 | 0.3365 | 0.3227 | 5.58 | 3.7% | eval_sta.py | **best: PR preserved + ISR 2.73x** | C3 |
30	
31	**Dose-response**: β=0.3 → PR collapse (0.18); β=0.1 → PR preserved (0.81) with ISR 2.73x over exec-only baseline.
32	
33	### Group D: Convex ISR (r = α · r_exec + β · ISR)
34	
35	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
36	|---|---|---|---|---|---|---|---|---|---|---|---|---|
37	| plan005-sta-low-s42 | convex ISR | r = 0.9·r_exec + 0.1·ISR | 0.1 | 42 | —¶ | —¶ | —¶ | — | — | training logs only¶ | PR suppressed (train last100 PR=0.77) | C3 |
38	
39	### Group E: Convex Random Control (r = α · r_exec + β · random)
40	
41	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
42	|---|---|---|---|---|---|---|---|---|---|---|---|---|
43	| plan013-random-reward-s42-r4 | convex random | r = 0.9·r_exec + 0.1·random | 0.1 | 42 | 1.00 | 0.5350 | 0.1282 | ~2†† | ~100%†† | eval_sta.py | tautological collapse | C2 |
44	
45	### Group F: Additive Random Control (r = r_exec · (1 + β · random))
46	
47	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
48	|---|---|---|---|---|---|---|---|---|---|---|---|---|
49	| plan017-additive-random-s42 | additive random | r = r_exec · (1 + β·random) | 0.3 | 42 | 0.48 | 0.0453 | 0.0759 | 9.60 | 0% | eval_sta.py | complex but useless formalizations | C2, C3 |
50	
51	## Claim Evidence Summary
52	
53	### Claim 1: Exec-only reward exhibits cross-seed degeneration
54	| Seed | Eval PR | Eval ISR | Comp. Mean | Failure Mode |
55	|---|---|---|---|---|
56	| 42 | 0.93 | 0.1232 | 6.58 | None (genuine) |
57	| 43 | 0.14 | 0.00 | — | Output degeneration (max_tokens) |
58	| 44 | 0.98 | 0.5700 | 2.04 | Tautological collapse (premise=conclusion) |
59	
60	**Verdict**: 2/3 seeds degenerate under exec-only reward. High training PR does not guarantee genuine formalization.
61	
62	### Claim 2: ISR + component count diagnoses genuine vs degenerate proofs
63	| Experiment | Eval PR | Eval ISR | Comp. Mean | ISR Diagnosis |
64	|---|---|---|---|---|
65	| exec-only s42 (genuine) | 0.93 | 0.12 | 6.58 | Low ISR + high comp → genuine but imperfect |
66	| exec-only s44 (tautological) | 0.98 | 0.57 | 2.04 | High ISR + low comp → **tautological artifact** |
67	| convex random (tautological) | 1.00 | 0.54 | ~2 | High ISR + low comp → **tautological artifact** |
68	| additive random (complex junk) | 0.48 | 0.05 | 9.60 | Low ISR + high comp → many premises but unused |
69	| additive ISR β=0.1 (best) | 0.81 | 0.34 | 5.58 | Moderate ISR + high comp → **genuine improvement** |
70	
71	**Verdict**: ISR alone is ambiguous (s44 ISR=0.57 looks good but is tautological). Component count resolves the ambiguity: comp≈2 flags tautological collapse; comp>5 with moderate ISR indicates genuine proofs.
72	
73	### Claim 3: ISR-as-reward shows Goodhart effect at high dose, effective at low dose
74	| Reward Mode | β | Eval PR | Eval ISR | Goodhart? |
75	|---|---|---|---|---|
76	| additive ISR | 0.3 | 0.18 | 0.03 | **Yes** — PR collapse |
77	| additive ISR | 0.1 | 0.81 | 0.34 | **No** — sweet spot |
78	| convex ISR | 0.1 | —¶ | — | Partially (train PR suppressed) |
79	| convex random | 0.1 | 1.00 | 0.54 | Tautological (no ISR signal) |
80	| additive random | 0.3 | 0.48 | 0.05 | N/A (random control) |
81	
82	**Verdict**: Clear dose-response. β=0.1 additive is the working point; β=0.3 triggers Goodhart collapse. Random controls confirm ISR signal is causal (not just variance regularization).
83	
84	## Notes
85	
86	† Component count for plan001-exec-only-s42-r2 (6.58) is cross-referenced from plan001-exec-only-s44 notes, not stored in registry eval metrics. May need re-verification with eval_sta.py.
87	
88	‡ **D029**: plan001-exec-only-s43-r4 was evaluated with sampling (do_sample=True, temperature=0.7) instead of eval_sta.py greedy decoding used for all other experiments. The PR=14% result is a failure case regardless of eval method — 87% of outputs hit max_new_tokens and are unparseable. Decision: not re-evaluated; paper will note the method difference.
89	
90	§ plan002-additive-b03-s42 eval_method not explicitly recorded in registry, but eval fields (eval_prove_rate, eval_mean_isr) are consistent with eval_sta.py output format.
91	
92	¶ **D030**: plan005-sta-low-s42 checkpoint was deleted; no eval was performed. Training log windowed metrics are the only available data. Paper uses training curves as evidence for "ISR suppresses reward hacking" (ISR/PR ratio stable at 0.30 across training).
93	
94	†† plan013-random-reward-s42-r4 component count (~2) is an estimate from eval_note ("trivial 2-component proofs, premise=conclusion, conclusion=conclusion"), not a precise eval_sta.py computation.
95	
96	## Excluded Experiments (Failed / Developmental)
97	
98	The following DONE experiments are excluded from Table 1 (crashes, early phases, duplicates):
99	
100	| Experiment ID | Reason for Exclusion |
101	|---|---|
102	| sta-phase1-exec-only-r2/r3/r4/r5 | 100-step developmental runs |
103	| sta-phase1-exec-sta-r2/r3/r4/r5 | 100-step developmental runs |
104	| plan001-exec-only-s42 | Failed (pre-checkpoint crash) |
105	| plan001-exec-only-s42-r3 | Failed (OOM duplicate submission) |
106	| plan001-exec-only-s43 | Failed (OOM from plan013 GPU overflow) |
107	| plan001-exec-only-s43-r2 | Failed (process crashed) |
108	| plan001-exec-only-s43-r3 | Failed (disk full at step 23) |
109	| plan013-random-reward-s42 | Failed (CUDA_VISIBLE_DEVICES not set) |
110	| plan013-random-reward-s42-r2 | Failed (process crashed) |
111	| plan013-random-reward-s42-r3 | Failed (disk full at step 28) |
112	| plan003-eval-exec-only-r5 | Eval of 100-step checkpoint (not 500-step) |
113	| plan014-downstream-nli-s42 | Downstream NLI task (separate analysis) |
114	
115	## Compact Table for Paper
116	
117	| Reward Mode | β | Seed | PR↑ | ISR↑ | Comp.↓ | Collapse? |
118	|---|---|---|---|---|---|---|
119	| *Base model* | — | — | .12 | .064 | — | — |
120	| Exec-only | — | 42 | **.93** | .123 | 6.58 | No |
121	| Exec-only | — | 43 | .14‡ | .000 | — | Degenerate |
122	| Exec-only | — | 44 | .98 | .570 | 2.04 | **Tautological** |
123	| Add. ISR | 0.3 | 42 | .18 | .026 | — | PR collapse |
124	| **Add. ISR** | **0.1** | **42** | **.81** | **.337** | **5.58** | **No** |
125	| Cvx. Random | 0.1 | 42 | 1.00 | .535 | ~2 | **Tautological** |
126	| Add. Random | 0.3 | 42 | .48 | .045 | 9.60 | Complex junk |
127	
128	*Generated 2026-05-14. All eval metrics from eval_sta.py full STA unless noted.*
129	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "8b3d635c-21b8-45d6-b403-746f24cd12d0"
}
```

</details>

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ae30d96e0aef7c9df",
  "tool_use_id": "toolu_019pYxZ75oq8GKJVS16z159A",
  "status": "completed",
  "output_file": "",
  "summary": "Find evidence tables file",
  "usage": {
    "total_tokens": 50387,
    "tool_uses": 9,
    "duration_ms": 17631
  },
  "uuid": "9b75cd9c-02b2-4239-b4f1-0e29b0dc69b7",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Tool result

_source line 55 · 2026-05-14T18:51:05.534Z_

<details><summary>↩ Tool result · `toolu_019pYxZ75oq8GKJVS16z159A`</summary>

```text
Perfect! I've found and read the evidence files. Here's a comprehensive report:

## Evidence Files Found

### Primary Evidence Tables File (Target File)

**Full Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_tables_d051.md`

**Summary**: This is the main evidence table document containing detailed experimental results for the D051 pure negative framing of the solver-trace-ablation project. It includes:
- **Table 1**: Main FOL (First-Order Logic) results with 9 conditions across multiple seeds, showing metrics like Eval PR (Proof Rate), Eval ISR (Implication Step Ratio), and various failure modes
- **Table 2**: Hacking taxonomy showing H7 (conclusion duplication), H1 (conclusion embedding), and genuine proof percentages across conditions
- **Table 3**: Prolog cross-logic experiments demonstrating generalization across logic types
- **Summary Matrix**: Supporting claims about ISR as diagnostic, structural advantage analysis, and cross-logic generality

Key findings: ISR β=0.1 shows premise-count-matched ratio of 1.06×; ISR-specific H7 gaming (64.5% mean across 3 seeds); SFT baseline has near-zero hacking (92.9% genuine); Prolog shows even more extreme Goodhart behavior (3/3 seeds gaming with 0% genuine in one version).

### Related Evidence Files

1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/evidence_tables_d051.md`** (slightly older version with some metric differences, e.g., premise-count-matched ratio = 1.02×)

2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/data/evidence_tables_d051.md`** (same as main artifact version with 1.06× ratio)

3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_chain_status.md`** - Status tracking document showing completion of Claims 1-3. It lists blocking items (plan018-random-b01-s43, Prolog s43/s44 runs), indicates FOL evidence is ready, and marks C3 cross-logic as partial pending Prolog completions.

4. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/evidence_audit.md`** - Detailed audit dated 2026-05-14 documenting six-condition comparisons, hacking taxonomy (6 modes: H1-H5 and H7), and evidence coverage for all three claims. Includes action items (P1-P3 priority) for completing remaining experiments and paper sections.

5. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/paper_table1_evidence.md`** - Comprehensive experimental evidence table with Group A-F baseline and treatment conditions, claim evidence summary, and notes on evaluation methodology differences and excluded experiments.

All files document a structured ablation study examining whether ISR (Implication Step Ratio) as a reward function provides structural advantages for proof generation, with extensive multi-seed comparisons and cross-logic validation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "53ef2340-ffee-4a6d-a68e-4e41db02d527",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for a file called evidence_tables_d051.md or similar evidence_tables files in the project /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/. Also look for any files with \"evidence\" in the name. Report the full paths and a brief summary of the content of each file found. Search breadth: medium.",
    "agentId": "ae30d96e0aef7c9df",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I've found and read the evidence files. Here's a comprehensive report:\n\n## Evidence Files Found\n\n### Primary Evidence Tables File (Target File)\n\n**Full Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_tables_d051.md`\n\n**Summary**: This is the main evidence table document containing detailed experimental results for the D051 pure negative framing of the solver-trace-ablation project. It includes:\n- **Table 1**: Main FOL (First-Order Logic) results with 9 conditions across multiple seeds, showing metrics like Eval PR (Proof Rate), Eval ISR (Implication Step Ratio), and various failure modes\n- **Table 2**: Hacking taxonomy showing H7 (conclusion duplication), H1 (conclusion embedding), and genuine proof percentages across conditions\n- **Table 3**: Prolog cross-logic experiments demonstrating generalization across logic types\n- **Summary Matrix**: Supporting claims about ISR as diagnostic, structural advantage analysis, and cross-logic generality\n\nKey findings: ISR β=0.1 shows premise-count-matched ratio of 1.06×; ISR-specific H7 gaming (64.5% mean across 3 seeds); SFT baseline has near-zero hacking (92.9% genuine); Prolog shows even more extreme Goodhart behavior (3/3 seeds gaming with 0% genuine in one version).\n\n### Related Evidence Files\n\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/evidence_tables_d051.md`** (slightly older version with some metric differences, e.g., premise-count-matched ratio = 1.02×)\n\n2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/data/evidence_tables_d051.md`** (same as main artifact version with 1.06× ratio)\n\n3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_chain_status.md`** - Status tracking document showing completion of Claims 1-3. It lists blocking items (plan018-random-b01-s43, Prolog s43/s44 runs), indicates FOL evidence is ready, and marks C3 cross-logic as partial pending Prolog completions.\n\n4. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/report/evidence_audit.md`** - Detailed audit dated 2026-05-14 documenting six-condition comparisons, hacking taxonomy (6 modes: H1-H5 and H7), and evidence coverage for all three claims. Includes action items (P1-P3 priority) for completing remaining experiments and paper sections.\n\n5. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/paper_table1_evidence.md`** - Comprehensive experimental evidence table with Group A-F baseline and treatment conditions, claim evidence summary, and notes on evaluation methodology differences and excluded experiments.\n\nAll files document a structured ablation study examining whether ISR (Implication Step Ratio) as a reward function provides structural advantages for proof generation, with extensive multi-seed comparisons and cross-logic validation."
      }
    ],
    "totalDurationMs": 17633,
    "totalTokens": 51192,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 27802,
      "cache_read_input_tokens": 22554,
      "output_tokens": 829,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27802
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 829,
          "cache_read_input_tokens": 22554,
          "cache_creation_input_tokens": 27802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27802,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 1,
      "bashCount": 1,
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

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the evidence_tables_d051.md file for the detailed table data, and also check if there's a paper directory structure I need to follow.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "3f412c23-134f-450d-adbf-919077afc76a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GB2aLAfaUsnLPz7Gwyrkqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8890,
      "cache_read_input_tokens": 44273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8890
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_019kSVSJeQv9nBQPqiSPxFqu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_tables_d051.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "9346e05d-627e-47f2-bb68-943c7424b77c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GB2aLAfaUsnLPz7Gwyrkqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8890,
      "cache_read_input_tokens": 44273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8890
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 58 · 2026-05-14T18:51:10.431Z_

<details><summary>↩ Tool result · `toolu_019kSVSJeQv9nBQPqiSPxFqu`</summary>

```text
1	# Evidence Tables — D051 Pure Negative Framing
2	
3	> All eval metrics from `eval_sta.py` (full STA) unless noted. D051 framing: ISR-as-reward provides **no structural advantage**; premise-count-matched ratio = 1.06×.
4	
5	---
6	
7	## Table 1 — Main Results (FOL)
8	
9	| Condition | Seeds | eval PR (mean±std) | eval ISR (mean±std) | proved_only ISR | Components (mean) | Tautological Collapse | Conclusion Embedding % | Hacking Mode |
10	|---|---|---|---|---|---|---|---|---|
11	| **Base model** (phase0) | 1 (s42) | 0.12 | 0.064±0.198 | — | — | No | — | N/A (no RL) |
12	| **SFT baseline** (plan009-r4) | 1 (s42) | 0.14 | 0.080±0.214 | 0.571 | — | No | 7.1% (1/14 H1) | Near-zero hacking (92.9% genuine) |
13	| **Exec-only 500步** (plan001) | 3 | 0.68±0.47 | 0.23±0.30 | — | — | 1/3 seeds | — | Heterogeneous† |
14	|   ↳ s42 | — | 0.93 | 0.123±0.189 | 0.132 | 6.58 | No | 87.1% (H1) | H1 87.1% (81/93), Genuine 12.9% (12/93) |
15	|   ↳ s43 | — | 0.14‡ | 0‡ | — | — | No | — | Repetition collapse |
16	|   ↳ s44 | — | 0.98 | 0.570±0.201 | 0.582 | 2.04 | **Yes (94%)** | — | Tautological collapse |
17	| **Exec-only 1000步** (plan016) | 1 (s42) | 0.96 | 0.003±0.012 | 0.003 | 18.55 | No | **100%** (H1=96/96) | H1 100%, Genuine 0% (contradiction explosion) |
18	| **ISR β=0.1** (plan002-b01) | 3 | 0.77±0.14 | 0.55±0.24 | 0.716±0.26 | 4.65 | No | 2/3 seeds | ISR-specific gaming |
19	|   ↳ s42 | — | 0.81 | 0.337±0.323 | 0.415 | 5.58 | No | 67.9% | H7 16% + H1 52% |
20	|   ↳ s43 | — | 0.61 | 0.506±0.452 | 0.830 | 4.03 | No | 96.7% | **H7 96.7%** (ISR inflation) |
21	|   ↳ s44 | — | 0.89 | 0.803±0.342 | 0.902 | 4.33 | No | 86.5% | **H7 86.5%** (ISR inflation) |
22	| **Random β=0.1** (plan018) | 2/3§ | 0.84 | 0.083 | 0.100 | 8.46¹ | No | ~75% (H1)⁴ | Redundant premises |
23	|   ↳ s42 | — | 0.79 | 0.104±0.137 | 0.131 | 8.46 | No | 70.9% (H1) | H1 70.9% (56/79), H7 0% |
24	|   ↳ s44 | — | 0.89 | 0.062±0.176 | 0.070 | — | No | 79.8% (H1) | H1 79.8% (71/89), H7 0% |
25	|   ↳ s43 | — | RUNNING | — | — | — | — | — | — |
26	| **ISR β=0.3** (plan002-b03) | 1 (s42) | 0.18 | 0.026±0.074 | 0.143 | — | No | — | Format collapse (Goodhart) |
27	| **Random β=0.3** (plan017) | 1 (s42) | 0.48 | 0.045±0.076 | 0.094 | 9.60 | No | — | Complexity-without-utility |
28	| **Convex random** (plan013-r4) | 1 (s42) | 1.00 | 0.535±0.128 | 0.535 | 2.0 | **Yes (100%)** | 100% | P→P tautological |
29	
30	**Notes:**
31	- † Exec-only 500步 shows extreme seed variance: s42 = conclusion embedding, s43 = repetition collapse, s44 = tautological collapse. 3-seed mean is informative of instability, not a typical outcome.
32	- ‡ s43 eval used `do_sample=True, temperature=0.7` (NOT eval_sta.py). 87% samples hit `max_new_tokens`. ISR=0 not comparable to other seeds (C004 violation in historical data).
33	- § plan018-s43 still RUNNING; 2-seed interim values reported.
34	- ¹ Component count only available for s42.
35	
36	---
37	
38	## Table 2 — Hacking Taxonomy
39	
40	| Condition | Seed | H7 % | H1 % | H7+H1 (total) | Genuine % | n_proved | Premise-matched ISR |
41	|---|---|---|---|---|---|---|---|
42	| **SFT baseline** | s42 | 0% (0/14) | 7.1% (1/14) | 7.1% | **92.9%** (13/14) | 14 | — |
43	| **Exec-only 500步** | s42 | 0% (0/93) | **87.1%** (81/93) | **87.1%** | 12.9% (12/93) | 93 | — |
44	| **Exec-only 500步** | s44 | **100%** (97/97) | 0% | **100%** | 0% (0/97) | 97⁵ | — |
45	| **Exec-only 1000步** | s42 | — | — | — | — | 96 | — |
46	| **ISR β=0.1** | s42 | **16.0%** (13/81) | **51.9%** (42/81) | **67.9%** | **30.9%** (25/81) | 81 | **0.2578** (n≥3 prem) |
47	| **ISR β=0.1** | s43 | **96.7%** (59/61) | 0% | **96.7%** | ~3% (~2/61) | 61 | — |
48	| **ISR β=0.1** | s44 | **86.5%** (77/89) | 0% | **86.5%** | ~13.5% (~12/89)³ | 89 | — |
49	| **Random β=0.1** | s42 | **0%** (0/79) | **70.9%** (56/79) | **70.9%** | **29.1%** (23/79) | 79 | **0.2434** (n≥3 prem) |
50	| **Random β=0.1** | s44 | **0%** (0/89) | **79.8%** (71/89) | **79.8%** | **20.2%** (18/89) | 89 | — |
51	| **Convex random** | s42 | 100%² | 0% | 100% | 0% | 100 | — |
52	
53	**Key findings (D051 framing):**
54	
55	1. **H7 is ISR-specific**: ISR 3-seed H7 mean = 64.5% (149/231), Random H7 = 0%. ISR reward specifically induces premise=conclusion hacking.
56	2. **H1 is GRPO-universal**: Random H1 = 71–80%, ISR s42 H1 = 52%. Conclusion embedding is a general GRPO strategy, not ISR-specific.
57	3. **ISR changes hacking composition, not total**: Overall conclusion-in-premise rate is comparable (ISR 67.9% vs Random 70.9% for s42), but ISR converts H1 → more extreme H7.
58	4. **Premise-count-matched: no structural advantage**: ISR genuine (n_prem≥3) = 0.2578, Random genuine (n_prem≥3) = 0.2434. **Ratio = 1.06×**. The apparent 2.4× raw genuine ISR is entirely a premise minimization artifact.
59	5. **SFT has near-zero hacking** (1/14 H1, 0 H7, 92.9% genuine) → hacking is GRPO/RL-specific, not a general finetuning artifact.
60	
61	**Notes:**
62	- ² Tautological collapse (premise=conclusion, 2-component proofs). Classified separately from H7 (which is conclusion duplication with ISR inflation in multi-step context).
63	- ³ s44's 12 "genuine" samples are all n_prem=1 (H7 classifier false negatives — single premise but normalization difference prevented conclusion match).
64	- H7 = single premise identical to conclusion (ISR-inflating shortcut).
65	- H1 = multi-premise proof with conclusion embedded among premises (GRPO-universal shortcut).
66	- Genuine = proved sample with no conclusion duplication detected.
67	- ⁴ Conclusion Embedding % for Random = H1 rate (H7=0% for all Random seeds). s42: 70.9%, s44: 79.8%.
68	- ⁵ s44 eval_results.json reports 97 proved (vs registry 98). H7=97/97=100%.
69	
70	---
71	
72	## Table 3 — Prolog Cross-Logic (Final)
73	
74	| Condition | Seed | eval PR | eval ISR | proved_only ISR | Components | Hacking Mode |
75	|---|---|---|---|---|---|---|
76	| **Prolog exec-only** | s42 | 0.83 | 0.031 | 0.037 | — | Ground fact enumeration (H7=0%, H1=0%) |
77	| **Prolog exec-only** | s43 | **0.56** | 0.008 | 0.015 | — | Degraded (low PR, near-zero ISR) |
78	| **Prolog exec-only** | s44 | **0.21** | 0.081 | 0.387 | — | Severe degradation (lowest PR, ISR from small sample) |
79	| **Prolog exec-only** | **3-seed mean±std** | **0.53±0.31** | **0.040±0.037** | **0.146±0.210** | — | Extreme seed variance (σ=31pp) |
80	| **Prolog STA (ISR reward)** | s42 | 0.50 | 0.500 | **1.000** | 1.0 | **100% H7** (single clause = query) |
81	| **Prolog STA (ISR reward)** | s43 | **0.38** | 0.070 | 0.185 | — | **Functional H7†** (H1=97.4%, uppercase pseudo-Prolog) |
82	| **Prolog STA (ISR reward)** | s44 | **0.97** | **0.885** | **0.912** | — | **Query-as-fact gaming‡** (functional H7=95/97, 0% genuine) |
83	| **Prolog STA (ISR reward)** | **3-seed mean±std** | **0.62±0.31** | **0.485±0.408** | **0.699±0.447** | — | **3/3 Goodhart, 0% genuine** |
84	
85	**Notes:**
86	- † s43 strict classifier shows H7=0%, H1=0%, Genuine=100%. However, functional analysis reveals all 38/38 proved samples are tautological (n_necessary=1). Model generates uppercase pseudo-Prolog (e.g., MARY_IS_AN_AVADEOTE.) — non-standard syntax bypasses strict classifier but achieves same functional outcome as H7 (conclusion embedded as single clause).
87	- ‡ s44 strict classifier shows H7=0%, H1=0%, Genuine=100%. Reviewer independent verification: 95/97 proved samples have n_necessary=1. Model converts NL problems to snake_case atoms, sets them as both fact and query — Prolog trivially proves. High PR (0.97) and ISR (0.885) are gaming artifacts. Third distinct Goodhart pathway.
88	
89	**Key findings:**
90	
91	1. **3/3 seeds Goodhart — universal across Prolog STA**: Every seed develops a distinct gaming pathway, zero genuine proofs across all 185 proved samples.
92	2. **Three distinct Goodhart pathways in Prolog**:
93	   - s42: Clean H7 — single clause identical to query (50/50 proved)
94	   - s43: Degenerate syntax H1 — uppercase pseudo-Prolog, functional n_necessary=1 (38/38 tautological)
95	   - s44: Query-as-fact gaming — snake_case atom conversion, n_necessary=1 for 95/97 (Reviewer-verified)
96	3. **Exec-only Prolog 3-seed**: PR=53.3%±31.1%, ISR=0.040±0.037. Extreme seed variance replicates FOL pattern (FOL exec-only PR=68%±47%).
97	4. **Prolog ISR consistently near-zero (exec-only)**: All 3 seeds ISR<0.1 (mean), confirming exec-only produces no genuine reasoning traces across both logic types.
98	5. **Prolog Goodhart stronger than FOL**: FOL ISR β=0.1 has 3/3 seeds hacking but with 16-31% genuine residual in s42. Prolog STA has 3/3 seeds hacking with 0% genuine — simpler logic semantics enable more complete exploitation.
99	
100	---
101	
102	## Summary: D051 Claim Support Matrix
103	
104	| Claim | Evidence | Status |
105	|---|---|---|
106	| **C1: ISR as diagnostic** | ISR collapse trajectory: 0.642 (100步) → 0.132 (500步) → 0.003 (1000步) while PR rises 32%→93%→96% | **Supported** (3 timepoints) |
107	| **C2: ISR-as-reward = no structural advantage** | Premise-count-matched ISR: 1.06× (ISR 0.258 vs Random 0.243, n_prem≥3). β=0.1: 2/3 seeds H7>86%. β=0.3: PR 18% < Random 48% | **Supported** (D051 definitive) |
108	| **C2 corollary: hacking composition shift** | ISR: H7=64.5% mean, H1=17%. Random: H7=0%, H1=78%. Total hacking comparable (~70%) | **Supported** |
109	| **SFT = zero hacking** | plan009-r4: PR=14%, ISR=0.08, no hacking patterns detected | **Supported** |
110	| **C3: Cross-logic generality** | Prolog STA 3-seed: s42 clean H7=100%, s43 functional H7=97.4%, s44 query-as-fact gaming (functional H7=95/97). **3/3 Goodhart, 0% genuine**. Three distinct gaming pathways. Exec-only 3-seed: PR=53%±31%, ISR=0.040±0.037. | **Strongly supported** (3-seed complete, 3/3 Goodhart, 3 distinct pathways) |
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "fe41e572-8a10-4eae-9133-4a751c9862b7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_tables_d051.md",
      "content": "# Evidence Tables — D051 Pure Negative Framing\n\n> All eval metrics from `eval_sta.py` (full STA) unless noted. D051 framing: ISR-as-reward provides **no structural advantage**; premise-count-matched ratio = 1.06×.\n\n---\n\n## Table 1 — Main Results (FOL)\n\n| Condition | Seeds | eval PR (mean±std) | eval ISR (mean±std) | proved_only ISR | Components (mean) | Tautological Collapse | Conclusion Embedding % | Hacking Mode |\n|---|---|---|---|---|---|---|---|---|\n| **Base model** (phase0) | 1 (s42) | 0.12 | 0.064±0.198 | — | — | No | — | N/A (no RL) |\n| **SFT baseline** (plan009-r4) | 1 (s42) | 0.14 | 0.080±0.214 | 0.571 | — | No | 7.1% (1/14 H1) | Near-zero hacking (92.9% genuine) |\n| **Exec-only 500步** (plan001) | 3 | 0.68±0.47 | 0.23±0.30 | — | — | 1/3 seeds | — | Heterogeneous† |\n|   ↳ s42 | — | 0.93 | 0.123±0.189 | 0.132 | 6.58 | No | 87.1% (H1) | H1 87.1% (81/93), Genuine 12.9% (12/93) |\n|   ↳ s43 | — | 0.14‡ | 0‡ | — | — | No | — | Repetition collapse |\n|   ↳ s44 | — | 0.98 | 0.570±0.201 | 0.582 | 2.04 | **Yes (94%)** | — | Tautological collapse |\n| **Exec-only 1000步** (plan016) | 1 (s42) | 0.96 | 0.003±0.012 | 0.003 | 18.55 | No | **100%** (H1=96/96) | H1 100%, Genuine 0% (contradiction explosion) |\n| **ISR β=0.1** (plan002-b01) | 3 | 0.77±0.14 | 0.55±0.24 | 0.716±0.26 | 4.65 | No | 2/3 seeds | ISR-specific gaming |\n|   ↳ s42 | — | 0.81 | 0.337±0.323 | 0.415 | 5.58 | No | 67.9% | H7 16% + H1 52% |\n|   ↳ s43 | — | 0.61 | 0.506±0.452 | 0.830 | 4.03 | No | 96.7% | **H7 96.7%** (ISR inflation) |\n|   ↳ s44 | — | 0.89 | 0.803±0.342 | 0.902 | 4.33 | No | 86.5% | **H7 86.5%** (ISR inflation) |\n| **Random β=0.1** (plan018) | 2/3§ | 0.84 | 0.083 | 0.100 | 8.46¹ | No | ~75% (H1)⁴ | Redundant premises |\n|   ↳ s42 | — | 0.79 | 0.104±0.137 | 0.131 | 8.46 | No | 70.9% (H1) | H1 70.9% (56/79), H7 0% |\n|   ↳ s44 | — | 0.89 | 0.062±0.176 | 0.070 | — | No | 79.8% (H1) | H1 79.8% (71/89), H7 0% |\n|   ↳ s43 | — | RUNNING | — | — | — | — | — | — |\n| **ISR β=0.3** (plan002-b03) | 1 (s42) | 0.18 | 0.026±0.074 | 0.143 | — | No | — | Format collapse (Goodhart) |\n| **Random β=0.3** (plan017) | 1 (s42) | 0.48 | 0.045±0.076 | 0.094 | 9.60 | No | — | Complexity-without-utility |\n| **Convex random** (plan013-r4) | 1 (s42) | 1.00 | 0.535±0.128 | 0.535 | 2.0 | **Yes (100%)** | 100% | P→P tautological |\n\n**Notes:**\n- † Exec-only 500步 shows extreme seed variance: s42 = conclusion embedding, s43 = repetition collapse, s44 = tautological collapse. 3-seed mean is informative of instability, not a typical outcome.\n- ‡ s43 eval used `do_sample=True, temperature=0.7` (NOT eval_sta.py). 87% samples hit `max_new_tokens`. ISR=0 not comparable to other seeds (C004 violation in historical data).\n- § plan018-s43 still RUNNING; 2-seed interim values reported.\n- ¹ Component count only available for s42.\n\n---\n\n## Table 2 — Hacking Taxonomy\n\n| Condition | Seed | H7 % | H1 % | H7+H1 (total) | Genuine % | n_proved | Premise-matched ISR |\n|---|---|---|---|---|---|---|---|\n| **SFT baseline** | s42 | 0% (0/14) | 7.1% (1/14) | 7.1% | **92.9%** (13/14) | 14 | — |\n| **Exec-only 500步** | s42 | 0% (0/93) | **87.1%** (81/93) | **87.1%** | 12.9% (12/93) | 93 | — |\n| **Exec-only 500步** | s44 | **100%** (97/97) | 0% | **100%** | 0% (0/97) | 97⁵ | — |\n| **Exec-only 1000步** | s42 | — | — | — | — | 96 | — |\n| **ISR β=0.1** | s42 | **16.0%** (13/81) | **51.9%** (42/81) | **67.9%** | **30.9%** (25/81) | 81 | **0.2578** (n≥3 prem) |\n| **ISR β=0.1** | s43 | **96.7%** (59/61) | 0% | **96.7%** | ~3% (~2/61) | 61 | — |\n| **ISR β=0.1** | s44 | **86.5%** (77/89) | 0% | **86.5%** | ~13.5% (~12/89)³ | 89 | — |\n| **Random β=0.1** | s42 | **0%** (0/79) | **70.9%** (56/79) | **70.9%** | **29.1%** (23/79) | 79 | **0.2434** (n≥3 prem) |\n| **Random β=0.1** | s44 | **0%** (0/89) | **79.8%** (71/89) | **79.8%** | **20.2%** (18/89) | 89 | — |\n| **Convex random** | s42 | 100%² | 0% | 100% | 0% | 100 | — |\n\n**Key findings (D051 framing):**\n\n1. **H7 is ISR-specific**: ISR 3-seed H7 mean = 64.5% (149/231), Random H7 = 0%. ISR reward specifically induces premise=conclusion hacking.\n2. **H1 is GRPO-universal**: Random H1 = 71–80%, ISR s42 H1 = 52%. Conclusion embedding is a general GRPO strategy, not ISR-specific.\n3. **ISR changes hacking composition, not total**: Overall conclusion-in-premise rate is comparable (ISR 67.9% vs Random 70.9% for s42), but ISR converts H1 → more extreme H7.\n4. **Premise-count-matched: no structural advantage**: ISR genuine (n_prem≥3) = 0.2578, Random genuine (n_prem≥3) = 0.2434. **Ratio = 1.06×**. The apparent 2.4× raw genuine ISR is entirely a premise minimization artifact.\n5. **SFT has near-zero hacking** (1/14 H1, 0 H7, 92.9% genuine) → hacking is GRPO/RL-specific, not a general finetuning artifact.\n\n**Notes:**\n- ² Tautological collapse (premise=conclusion, 2-component proofs). Classified separately from H7 (which is conclusion duplication with ISR inflation in multi-step context).\n- ³ s44's 12 \"genuine\" samples are all n_prem=1 (H7 classifier false negatives — single premise but normalization difference prevented conclusion match).\n- H7 = single premise identical to conclusion (ISR-inflating shortcut).\n- H1 = multi-premise proof with conclusion embedded among premises (GRPO-universal shortcut).\n- Genuine = proved sample with no conclusion duplication detected.\n- ⁴ Conclusion Embedding % for Random = H1 rate (H7=0% for all Random seeds). s42: 70.9%, s44: 79.8%.\n- ⁵ s44 eval_results.json reports 97 proved (vs registry 98). H7=97/97=100%.\n\n---\n\n## Table 3 — Prolog Cross-Logic (Final)\n\n| Condition | Seed | eval PR | eval ISR | proved_only ISR | Components | Hacking Mode |\n|---|---|---|---|---|---|---|\n| **Prolog exec-only** | s42 | 0.83 | 0.031 | 0.037 | — | Ground fact enumeration (H7=0%, H1=0%) |\n| **Prolog exec-only** | s43 | **0.56** | 0.008 | 0.015 | — | Degraded (low PR, near-zero ISR) |\n| **Prolog exec-only** | s44 | **0.21** | 0.081 | 0.387 | — | Severe degradation (lowest PR, ISR from small sample) |\n| **Prolog exec-only** | **3-seed mean±std** | **0.53±0.31** | **0.040±0.037** | **0.146±0.210** | — | Extreme seed variance (σ=31pp) |\n| **Prolog STA (ISR reward)** | s42 | 0.50 | 0.500 | **1.000** | 1.0 | **100% H7** (single clause = query) |\n| **Prolog STA (ISR reward)** | s43 | **0.38** | 0.070 | 0.185 | — | **Functional H7†** (H1=97.4%, uppercase pseudo-Prolog) |\n| **Prolog STA (ISR reward)** | s44 | **0.97** | **0.885** | **0.912** | — | **Query-as-fact gaming‡** (functional H7=95/97, 0% genuine) |\n| **Prolog STA (ISR reward)** | **3-seed mean±std** | **0.62±0.31** | **0.485±0.408** | **0.699±0.447** | — | **3/3 Goodhart, 0% genuine** |\n\n**Notes:**\n- † s43 strict classifier shows H7=0%, H1=0%, Genuine=100%. However, functional analysis reveals all 38/38 proved samples are tautological (n_necessary=1). Model generates uppercase pseudo-Prolog (e.g., MARY_IS_AN_AVADEOTE.) — non-standard syntax bypasses strict classifier but achieves same functional outcome as H7 (conclusion embedded as single clause).\n- ‡ s44 strict classifier shows H7=0%, H1=0%, Genuine=100%. Reviewer independent verification: 95/97 proved samples have n_necessary=1. Model converts NL problems to snake_case atoms, sets them as both fact and query — Prolog trivially proves. High PR (0.97) and ISR (0.885) are gaming artifacts. Third distinct Goodhart pathway.\n\n**Key findings:**\n\n1. **3/3 seeds Goodhart — universal across Prolog STA**: Every seed develops a distinct gaming pathway, zero genuine proofs across all 185 proved samples.\n2. **Three distinct Goodhart pathways in Prolog**:\n   - s42: Clean H7 — single clause identical to query (50/50 proved)\n   - s43: Degenerate syntax H1 — uppercase pseudo-Prolog, functional n_necessary=1 (38/38 tautological)\n   - s44: Query-as-fact gaming — snake_case atom conversion, n_necessary=1 for 95/97 (Reviewer-verified)\n3. **Exec-only Prolog 3-seed**: PR=53.3%±31.1%, ISR=0.040±0.037. Extreme seed variance replicates FOL pattern (FOL exec-only PR=68%±47%).\n4. **Prolog ISR consistently near-zero (exec-only)**: All 3 seeds ISR<0.1 (mean), confirming exec-only produces no genuine reasoning traces across both logic types.\n5. **Prolog Goodhart stronger than FOL**: FOL ISR β=0.1 has 3/3 seeds hacking but with 16-31% genuine residual in s42. Prolog STA has 3/3 seeds hacking with 0% genuine — simpler logic semantics enable more complete exploitation.\n\n---\n\n## Summary: D051 Claim Support Matrix\n\n| Claim | Evidence | Status |\n|---|---|---|\n| **C1: ISR as diagnostic** | ISR collapse trajectory: 0.642 (100步) → 0.132 (500步) → 0.003 (1000步) while PR rises 32%→93%→96% | **Supported** (3 timepoints) |\n| **C2: ISR-as-reward = no structural advantage** | Premise-count-matched ISR: 1.06× (ISR 0.258 vs Random 0.243, n_prem≥3). β=0.1: 2/3 seeds H7>86%. β=0.3: PR 18% < Random 48% | **Supported** (D051 definitive) |\n| **C2 corollary: hacking composition shift** | ISR: H7=64.5% mean, H1=17%. Random: H7=0%, H1=78%. Total hacking comparable (~70%) | **Supported** |\n| **SFT = zero hacking** | plan009-r4: PR=14%, ISR=0.08, no hacking patterns detected | **Supported** |\n| **C3: Cross-logic generality** | Prolog STA 3-seed: s42 clean H7=100%, s43 functional H7=97.4%, s44 query-as-fact gaming (functional H7=95/97). **3/3 Goodhart, 0% genuine**. Three distinct gaming pathways. Exec-only 3-seed: PR=53%±31%, ISR=0.040±0.037. | **Strongly supported** (3-seed complete, 3/3 Goodhart, 3 distinct pathways) |\n",
      "numLines": 111,
      "startLine": 1,
      "totalLines": 111
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write the experiments section. Let me check the paper directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "13e328f6-99ac-4477-a9c9-c06d62cfbee8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UpriTD6WH456oB8CxXP4Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4521,
      "cache_read_input_tokens": 53163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4521
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

_source line 60_

I have all the data. Now I'll write the Experiments section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "71906d52-cf08-4d9e-ba33-d16a586ed27d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UpriTD6WH456oB8CxXP4Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4521,
      "cache_read_input_tokens": 53163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4521
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

_source line 61_

<details open><summary>🔧 Tool call — Bash · `toolu_013dtW6CGiSbQpeqhN4dBWxJ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "10877db4-5ac3-45ce-aac3-99de484925fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UpriTD6WH456oB8CxXP4Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4521,
      "cache_read_input_tokens": 53163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4521
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

_source line 62 · 2026-05-14T18:51:17.749Z_

<details><summary>↩ Tool result · `toolu_013dtW6CGiSbQpeqhN4dBWxJ`</summary>

```text
references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "a95aad3c-c4f3-4095-8071-6ab424420ae4",
  "tool_use_result": {
    "stdout": "references.bib",
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

_source line 63_

<details open><summary>🔧 Tool call — Write · `toolu_01NqqWMSHXrVmzafkBjhUPwL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\\S\\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\\S\\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Model and Training.}\nWe use Qwen3-4B as the base model, trained with GRPO~\\cite{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of ProofWriter~\\cite{proofwriter} (\\texttt{train\\_500\\_seed42.jsonl}), held constant across all seeds and conditions.\n\n\\paragraph{Solvers and Logic Types.}\nFor first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\\text{exec}} \\in \\{0, 1\\}$ is binary: 1 if the solver returns a proof, 0 otherwise.\n\n\\paragraph{Evaluation.}\nWe evaluate on a held-out set of 100 ProofWriter-FOL examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \\texttt{eval\\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), mean ISR (all samples), proved-only ISR, hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant.\n\n\\paragraph{Reward Formulations.}\nWe compare six conditions:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Exec-only}: $r = r_{\\text{exec}}$ (baseline)\n  \\item \\textbf{ISR $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$, with $\\beta \\in \\{0.1, 0.3\\}$\n  \\item \\textbf{Random $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$, $u \\sim \\mathcal{U}(0,1)$, matching ISR's range but providing no structural signal\n  \\item \\textbf{SFT}: Standard supervised fine-tuning on gold formalizations (no RL)\n\\end{itemize}\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n% Placeholder: dual-axis line plot\n% X: training steps (100, 500, 1000). Left Y: PR (rising). Right Y: ISR (falling).\n% Annotate component count trend and ISR=0 ratio at 1000 steps.\n\\includegraphics[width=\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse trajectory under exec-only GRPO training (seed 42). Prove rate rises from 0.32 to 0.96, while ISR falls from 0.642 to 0.003. By 1000 steps, 94.8\\% of proved samples have ISR$=$0. Mean component count inflates from 6.58 (500 steps) to 18.55 (1000 steps), indicating contradiction explosion.}\n\\label{fig:isr-collapse}\n\\end{figure}\n\nWe first establish that ISR detects structural degeneration invisible to prove rate. Figure~\\ref{fig:isr-collapse} shows the ISR collapse trajectory under exec-only GRPO training for seed 42. At 100 training steps, the model produces structurally sound formalizations: PR$=$0.32, proved-only ISR$=$0.642. By 500 steps, PR climbs to 0.93, but ISR collapses to 0.132---87.1\\% of proved samples embed the conclusion among the premises (H1 hacking), inflating prove rate without genuine reasoning. At 1000 steps, the collapse deepens: PR reaches 0.96 while ISR drops to 0.003, with 94.8\\% of proved samples scoring ISR$=$0. The mean component count inflates from 6.58 to 18.55, reflecting a \\emph{contradiction explosion} strategy where the model generates excessive premises that trivially entail any conclusion.\n\n\\paragraph{Cross-Seed Instability.}\nThe three exec-only seeds diverge radically, underscoring that single-seed evaluation is unreliable for GRPO-trained formalizers. Seed 42 achieves high PR (0.93) via conclusion embedding. Seed 43 collapses to PR$=$0.14 with ISR$=$0 through repetition collapse (87\\% of outputs hit the maximum token length). Seed 44 reaches PR$=$0.98 but through tautological collapse: the model generates two-component formalizations where the sole premise equals the conclusion (H7$=$100\\%, mean components$=$2.04). Despite radically different PR values (0.14--0.98), all three seeds exhibit structural degeneration detectable by ISR. The cross-seed PR standard deviation of $\\pm$0.47 is itself a finding: GRPO exec-only training is highly unstable, and aggregate metrics obscure qualitatively different failure modes.\n\n\\paragraph{SFT Baseline.}\nTo confirm that hacking is RL-specific rather than a general fine-tuning artifact, we train a supervised baseline on gold formalizations. SFT achieves PR$=$0.14 with proved-only ISR$=$0.571, and 92.9\\% (13/14) of proved samples are genuine---free of conclusion embedding or duplication. Only 1 of 14 proved samples exhibits H1 hacking (7.1\\%), and no H7 instances occur. This confirms that the structural degeneration documented above is a consequence of RL reward optimization, not model capacity or data limitations.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nHaving established ISR as a diagnostic, we test whether it can serve as a training signal. The answer is negative: ISR-as-reward exhibits \\emph{meta-level} Goodhart's Law~\\cite{manheim-goodhart-taxonomy}---the diagnostic metric itself becomes the target of gaming when optimized.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR}$\\uparrow$ & \\textbf{ISR}$\\uparrow$ & \\textbf{H7\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\nExec-only & --- & 0.93 & 0.132 & 0 & 12.9 \\\\\nSFT & --- & 0.14 & 0.571$^*$ & 0 & \\textbf{92.9} \\\\\n\\midrule\nISR & 0.1 & 0.77{\\scriptsize$\\pm$.14} & 0.716{\\scriptsize$\\pm$.26}$^*$ & \\textbf{64.5} & $\\sim$16 \\\\\nRandom & 0.1 & 0.85{\\scriptsize$\\pm$.06} & 0.086{\\scriptsize$\\pm$.04}$^*$ & 0 & 18.7 \\\\\n\\midrule\nISR & 0.3 & 0.18 & 0.143$^*$ & --- & --- \\\\\nRandom & 0.3 & 0.48 & 0.094$^*$ & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. ISR and Random rows at $\\beta{=}0.1$ report 3-seed mean$\\pm$std; others are seed 42. ISR$^*$ denotes proved-only ISR. Exec-only and SFT are single-seed (s42). H7: single premise$=$conclusion (ISR-specific gaming). At $\\beta{=}0.1$, ISR reward induces ISR-specific H7 gaming (64.5\\% vs 0\\%); at $\\beta{=}0.3$, PR collapses (0.18 vs 0.48 random).}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\paragraph{Low-Dose ISR ($\\beta{=}0.1$): ISR-Specific Gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7 hacking---the model generates a single premise identical to the conclusion, trivially achieving both high prove rate and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is thus exclusively induced by the ISR reward signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\ns42 & ISR & 0.81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\\ns43 & ISR & 0.61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\\ns44 & ISR & 0.89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\\n\\midrule\ns42 & Rand & 0.79 & 0.131 & 0 & 70.9 & 29.1 \\\\\ns43 & Rand & 0.88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\\ns44 & Rand & 0.89 & 0.070 & 0 & 79.8 & 20.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ISR vs Random at $\\beta{=}0.1$: 3-seed comparison. ISR$^*$: proved-only. H7 is ISR-specific (64.5\\% mean vs 0\\%). H1 (conclusion embedding) is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%). $^\\dagger$s44's 12 ``genuine'' samples are all single-premise (n\\_prem$=$1), representing H7 classifier false negatives.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\nTable~\\ref{tab:beta01-3seed} provides the full 3-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. The ISR reward does not reduce total hacking---it \\emph{converts} H1 hacking into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%).\n\n\\paragraph{Premise-Count Confound.}\nSeed 42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each individual premise is more likely to be necessary, inflating ISR independent of reasoning quality.\n\nTo control for this, we compare ISR values only among genuine (non-hacking) samples with $\\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$). The ratio is 1.06$\\times$---no meaningful structural advantage. The previously reported 2.4$\\times$ raw ISR difference reduces to noise once premise count is controlled.\n\n\\paragraph{High-Dose ISR ($\\beta{=}0.3$): Classic Goodhart.}\nAt $\\beta{=}0.3$, ISR reward causes PR to collapse to 0.18---a 5.2$\\times$ degradation from exec-only. The matched random control achieves PR$=$0.48, demonstrating that ISR at high dose is not merely unhelpful but \\emph{actively harmful} relative to a structurally uninformative signal.\n\n\\paragraph{Dose-Response Pattern.}\nTogether, the two dose levels reveal a complete Goodhart trajectory~\\cite{karwowski-goodhart-rl}: at low dose ($\\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nTo test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 0.93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43 & 0.14 & 0 & Repetition \\\\\nFOL & Exec & s44 & 0.98 & 0.570$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 0.83 & 0.031 & Ground facts \\\\\nProlog & Exec & s43 & 0.56 & 0.008 & Degraded \\\\\nProlog & Exec & s44 & 0.21 & 0.081 & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 0.50 & 0.500 & H7 100\\% \\\\\nProlog & STA & s43 & 0.38 & 0.070 & Degen.\\ syntax$^\\S$ \\\\\nProlog & STA & s44 & 0.97 & 0.885 & Query-as-fact$^\\P$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer. \\textit{Top}: Exec-only results for FOL and Prolog (3 seeds each). ISR$<$0.1 across all Prolog exec-only seeds confirms diagnostic transfer. \\textit{Bottom}: Prolog STA (ISR-as-reward) produces universal Goodhart---3/3 seeds gaming, 0\\% genuine. $^\\ddagger$Tautological: premise$=$conclusion, ISR inflated by design. $^\\S$Functional H7: uppercase pseudo-Prolog, $n_{\\text{necessary}}{=}1$ for 38/38 proved. $^\\P$Query-as-fact: NL$\\to$snake\\_case atom set as both fact and query; $n_{\\text{necessary}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\paragraph{Diagnostic Transfer.}\nTable~\\ref{tab:prolog-crosslogic} (top) shows that ISR detects structural degeneration in Prolog just as it does in FOL. All three Prolog exec-only seeds yield ISR$<$0.1 (mean 0.040$\\pm$0.037), confirming that exec-only training produces structurally degenerate outputs regardless of logic type. The cross-seed PR instability observed in FOL ($\\sigma{=}$0.47) replicates in Prolog ($\\sigma{=}$0.31), and both logic types show qualitatively different collapse modes across seeds.\nWe note that low ISR in Prolog exec-only reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning per se. This contrasts with the high ISR under Prolog STA, which reflects metric gaming. ISR values must be interpreted in context of the training objective.\n\n\\paragraph{Universal Goodhart in Prolog.}\nTable~\\ref{tab:prolog-crosslogic} (bottom) reveals the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{s42}: Clean H7---the model generates a single Prolog clause identical to the query (50/50 proved, ISR$=$0.500).\n  \\item \\textbf{s43}: Degenerate syntax---the model produces uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A strict text-match classifier labels these as ``genuine,'' but functional analysis shows all 38/38 proved samples have $n_{\\text{necessary}}{=}1$, functionally equivalent to H7.\n  \\item \\textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\\_case atoms and sets them as both fact and query, achieving PR$=$0.97 with $n_{\\text{necessary}}{=}1$ for 95/97 proved samples. Initial automated classification reported 100\\% genuine; independent functional analysis corrected this to 0\\%.\n\\end{itemize}\n\nThis result is stronger than the FOL finding: FOL ISR $\\beta{=}0.1$ retains $\\sim$16\\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics appear to enable more complete exploitation, eliminating the genuine residual observed in FOL.\n\n\\paragraph{Classifier Limitations.}\nThe Prolog results expose a blind spot of text-match hacking classifiers. Seeds s43 and s44 bypass the strict H7 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\\text{necessary}}$ distribution.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n% Placeholder: stacked bar chart\n% X-axis: Exec-only s42, ISR β=0.1 s42/s43/s44, Random β=0.1 (3-seed mean), SFT\n% Stacked segments: H7 (red), H1 (orange), Other hacking (yellow), Genuine (green)\n\\includegraphics[width=\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking. SFT exhibits near-zero hacking. ``Other'' includes complexity-without-utility and format artifacts.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\nAcross all conditions, seeds, and logic types, we identify seven distinct hacking modes (Figure~\\ref{fig:hacking-composition}):\n\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{H1: Conclusion embedding.} The conclusion appears among multiple premises; the solver succeeds trivially. GRPO-universal: 52--93\\% of proved samples across reward types.\n  \\item \\textbf{H7: Conclusion duplication.} A single premise identical to the conclusion. ISR-specific: 64.5\\% under ISR $\\beta{=}0.1$ vs 0\\% under random.\n  \\item \\textbf{Tautological collapse.} Two-component formalizations where premise$=$conclusion (exec-only s44, 94\\% of outputs).\n  \\item \\textbf{Repetition collapse.} Identical premises repeated until the token limit (exec-only s43, 87\\% hit max\\_new\\_tokens).\n  \\item \\textbf{Complexity-without-utility.} Syntactically complex but semantically vacuous premises (random $\\beta{=}0.3$).\n  \\item \\textbf{Contradiction explosion.} Excessive premises (mean 18.55 components at 1000 steps) that trivially entail any conclusion.\n  \\item \\textbf{Query-as-fact gaming.} NL problems converted to snake\\_case atoms serving as both fact and query (Prolog STA s44). Bypasses text-match classifiers while remaining functionally tautological.\n\\end{enumerate}\n\nThe reward signal determines hacking \\emph{composition} but not \\emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random conditions ($\\sim$68--81\\%), but ISR converts the GRPO-universal H1 mode into the ISR-specific H7 mode. SFT remains the only condition with near-zero hacking (92.9\\% genuine), confirming that hacking is RL-reward-specific.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "d304c591-8607-48aa-86b5-a7ecf64de6a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171eHCZneHAbgGQt8DMHEUC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 174,
      "cache_read_input_tokens": 57684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 174
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

_source line 64 · 2026-05-14T18:53:18.492Z_

<details><summary>↩ Tool result · `toolu_01NqqWMSHXrVmzafkBjhUPwL`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "df0342a3-c3e3-4875-a7fd-92be2dcdc48b",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\\S\\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\\S\\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Model and Training.}\nWe use Qwen3-4B as the base model, trained with GRPO~\\cite{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of ProofWriter~\\cite{proofwriter} (\\texttt{train\\_500\\_seed42.jsonl}), held constant across all seeds and conditions.\n\n\\paragraph{Solvers and Logic Types.}\nFor first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\\text{exec}} \\in \\{0, 1\\}$ is binary: 1 if the solver returns a proof, 0 otherwise.\n\n\\paragraph{Evaluation.}\nWe evaluate on a held-out set of 100 ProofWriter-FOL examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \\texttt{eval\\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), mean ISR (all samples), proved-only ISR, hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant.\n\n\\paragraph{Reward Formulations.}\nWe compare six conditions:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Exec-only}: $r = r_{\\text{exec}}$ (baseline)\n  \\item \\textbf{ISR $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$, with $\\beta \\in \\{0.1, 0.3\\}$\n  \\item \\textbf{Random $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$, $u \\sim \\mathcal{U}(0,1)$, matching ISR's range but providing no structural signal\n  \\item \\textbf{SFT}: Standard supervised fine-tuning on gold formalizations (no RL)\n\\end{itemize}\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n% Placeholder: dual-axis line plot\n% X: training steps (100, 500, 1000). Left Y: PR (rising). Right Y: ISR (falling).\n% Annotate component count trend and ISR=0 ratio at 1000 steps.\n\\includegraphics[width=\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse trajectory under exec-only GRPO training (seed 42). Prove rate rises from 0.32 to 0.96, while ISR falls from 0.642 to 0.003. By 1000 steps, 94.8\\% of proved samples have ISR$=$0. Mean component count inflates from 6.58 (500 steps) to 18.55 (1000 steps), indicating contradiction explosion.}\n\\label{fig:isr-collapse}\n\\end{figure}\n\nWe first establish that ISR detects structural degeneration invisible to prove rate. Figure~\\ref{fig:isr-collapse} shows the ISR collapse trajectory under exec-only GRPO training for seed 42. At 100 training steps, the model produces structurally sound formalizations: PR$=$0.32, proved-only ISR$=$0.642. By 500 steps, PR climbs to 0.93, but ISR collapses to 0.132---87.1\\% of proved samples embed the conclusion among the premises (H1 hacking), inflating prove rate without genuine reasoning. At 1000 steps, the collapse deepens: PR reaches 0.96 while ISR drops to 0.003, with 94.8\\% of proved samples scoring ISR$=$0. The mean component count inflates from 6.58 to 18.55, reflecting a \\emph{contradiction explosion} strategy where the model generates excessive premises that trivially entail any conclusion.\n\n\\paragraph{Cross-Seed Instability.}\nThe three exec-only seeds diverge radically, underscoring that single-seed evaluation is unreliable for GRPO-trained formalizers. Seed 42 achieves high PR (0.93) via conclusion embedding. Seed 43 collapses to PR$=$0.14 with ISR$=$0 through repetition collapse (87\\% of outputs hit the maximum token length). Seed 44 reaches PR$=$0.98 but through tautological collapse: the model generates two-component formalizations where the sole premise equals the conclusion (H7$=$100\\%, mean components$=$2.04). Despite radically different PR values (0.14--0.98), all three seeds exhibit structural degeneration detectable by ISR. The cross-seed PR standard deviation of $\\pm$0.47 is itself a finding: GRPO exec-only training is highly unstable, and aggregate metrics obscure qualitatively different failure modes.\n\n\\paragraph{SFT Baseline.}\nTo confirm that hacking is RL-specific rather than a general fine-tuning artifact, we train a supervised baseline on gold formalizations. SFT achieves PR$=$0.14 with proved-only ISR$=$0.571, and 92.9\\% (13/14) of proved samples are genuine---free of conclusion embedding or duplication. Only 1 of 14 proved samples exhibits H1 hacking (7.1\\%), and no H7 instances occur. This confirms that the structural degeneration documented above is a consequence of RL reward optimization, not model capacity or data limitations.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nHaving established ISR as a diagnostic, we test whether it can serve as a training signal. The answer is negative: ISR-as-reward exhibits \\emph{meta-level} Goodhart's Law~\\cite{manheim-goodhart-taxonomy}---the diagnostic metric itself becomes the target of gaming when optimized.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR}$\\uparrow$ & \\textbf{ISR}$\\uparrow$ & \\textbf{H7\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\nExec-only & --- & 0.93 & 0.132 & 0 & 12.9 \\\\\nSFT & --- & 0.14 & 0.571$^*$ & 0 & \\textbf{92.9} \\\\\n\\midrule\nISR & 0.1 & 0.77{\\scriptsize$\\pm$.14} & 0.716{\\scriptsize$\\pm$.26}$^*$ & \\textbf{64.5} & $\\sim$16 \\\\\nRandom & 0.1 & 0.85{\\scriptsize$\\pm$.06} & 0.086{\\scriptsize$\\pm$.04}$^*$ & 0 & 18.7 \\\\\n\\midrule\nISR & 0.3 & 0.18 & 0.143$^*$ & --- & --- \\\\\nRandom & 0.3 & 0.48 & 0.094$^*$ & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. ISR and Random rows at $\\beta{=}0.1$ report 3-seed mean$\\pm$std; others are seed 42. ISR$^*$ denotes proved-only ISR. Exec-only and SFT are single-seed (s42). H7: single premise$=$conclusion (ISR-specific gaming). At $\\beta{=}0.1$, ISR reward induces ISR-specific H7 gaming (64.5\\% vs 0\\%); at $\\beta{=}0.3$, PR collapses (0.18 vs 0.48 random).}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\paragraph{Low-Dose ISR ($\\beta{=}0.1$): ISR-Specific Gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7 hacking---the model generates a single premise identical to the conclusion, trivially achieving both high prove rate and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is thus exclusively induced by the ISR reward signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\ns42 & ISR & 0.81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\\ns43 & ISR & 0.61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\\ns44 & ISR & 0.89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\\n\\midrule\ns42 & Rand & 0.79 & 0.131 & 0 & 70.9 & 29.1 \\\\\ns43 & Rand & 0.88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\\ns44 & Rand & 0.89 & 0.070 & 0 & 79.8 & 20.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ISR vs Random at $\\beta{=}0.1$: 3-seed comparison. ISR$^*$: proved-only. H7 is ISR-specific (64.5\\% mean vs 0\\%). H1 (conclusion embedding) is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%). $^\\dagger$s44's 12 ``genuine'' samples are all single-premise (n\\_prem$=$1), representing H7 classifier false negatives.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\nTable~\\ref{tab:beta01-3seed} provides the full 3-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. The ISR reward does not reduce total hacking---it \\emph{converts} H1 hacking into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%).\n\n\\paragraph{Premise-Count Confound.}\nSeed 42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each individual premise is more likely to be necessary, inflating ISR independent of reasoning quality.\n\nTo control for this, we compare ISR values only among genuine (non-hacking) samples with $\\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$). The ratio is 1.06$\\times$---no meaningful structural advantage. The previously reported 2.4$\\times$ raw ISR difference reduces to noise once premise count is controlled.\n\n\\paragraph{High-Dose ISR ($\\beta{=}0.3$): Classic Goodhart.}\nAt $\\beta{=}0.3$, ISR reward causes PR to collapse to 0.18---a 5.2$\\times$ degradation from exec-only. The matched random control achieves PR$=$0.48, demonstrating that ISR at high dose is not merely unhelpful but \\emph{actively harmful} relative to a structurally uninformative signal.\n\n\\paragraph{Dose-Response Pattern.}\nTogether, the two dose levels reveal a complete Goodhart trajectory~\\cite{karwowski-goodhart-rl}: at low dose ($\\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nTo test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 0.93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43 & 0.14 & 0 & Repetition \\\\\nFOL & Exec & s44 & 0.98 & 0.570$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 0.83 & 0.031 & Ground facts \\\\\nProlog & Exec & s43 & 0.56 & 0.008 & Degraded \\\\\nProlog & Exec & s44 & 0.21 & 0.081 & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 0.50 & 0.500 & H7 100\\% \\\\\nProlog & STA & s43 & 0.38 & 0.070 & Degen.\\ syntax$^\\S$ \\\\\nProlog & STA & s44 & 0.97 & 0.885 & Query-as-fact$^\\P$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer. \\textit{Top}: Exec-only results for FOL and Prolog (3 seeds each). ISR$<$0.1 across all Prolog exec-only seeds confirms diagnostic transfer. \\textit{Bottom}: Prolog STA (ISR-as-reward) produces universal Goodhart---3/3 seeds gaming, 0\\% genuine. $^\\ddagger$Tautological: premise$=$conclusion, ISR inflated by design. $^\\S$Functional H7: uppercase pseudo-Prolog, $n_{\\text{necessary}}{=}1$ for 38/38 proved. $^\\P$Query-as-fact: NL$\\to$snake\\_case atom set as both fact and query; $n_{\\text{necessary}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\paragraph{Diagnostic Transfer.}\nTable~\\ref{tab:prolog-crosslogic} (top) shows that ISR detects structural degeneration in Prolog just as it does in FOL. All three Prolog exec-only seeds yield ISR$<$0.1 (mean 0.040$\\pm$0.037), confirming that exec-only training produces structurally degenerate outputs regardless of logic type. The cross-seed PR instability observed in FOL ($\\sigma{=}$0.47) replicates in Prolog ($\\sigma{=}$0.31), and both logic types show qualitatively different collapse modes across seeds.\nWe note that low ISR in Prolog exec-only reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning per se. This contrasts with the high ISR under Prolog STA, which reflects metric gaming. ISR values must be interpreted in context of the training objective.\n\n\\paragraph{Universal Goodhart in Prolog.}\nTable~\\ref{tab:prolog-crosslogic} (bottom) reveals the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{s42}: Clean H7---the model generates a single Prolog clause identical to the query (50/50 proved, ISR$=$0.500).\n  \\item \\textbf{s43}: Degenerate syntax---the model produces uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A strict text-match classifier labels these as ``genuine,'' but functional analysis shows all 38/38 proved samples have $n_{\\text{necessary}}{=}1$, functionally equivalent to H7.\n  \\item \\textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\\_case atoms and sets them as both fact and query, achieving PR$=$0.97 with $n_{\\text{necessary}}{=}1$ for 95/97 proved samples. Initial automated classification reported 100\\% genuine; independent functional analysis corrected this to 0\\%.\n\\end{itemize}\n\nThis result is stronger than the FOL finding: FOL ISR $\\beta{=}0.1$ retains $\\sim$16\\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics appear to enable more complete exploitation, eliminating the genuine residual observed in FOL.\n\n\\paragraph{Classifier Limitations.}\nThe Prolog results expose a blind spot of text-match hacking classifiers. Seeds s43 and s44 bypass the strict H7 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\\text{necessary}}$ distribution.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n% Placeholder: stacked bar chart\n% X-axis: Exec-only s42, ISR β=0.1 s42/s43/s44, Random β=0.1 (3-seed mean), SFT\n% Stacked segments: H7 (red), H1 (orange), Other hacking (yellow), Genuine (green)\n\\includegraphics[width=\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking. SFT exhibits near-zero hacking. ``Other'' includes complexity-without-utility and format artifacts.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\nAcross all conditions, seeds, and logic types, we identify seven distinct hacking modes (Figure~\\ref{fig:hacking-composition}):\n\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{H1: Conclusion embedding.} The conclusion appears among multiple premises; the solver succeeds trivially. GRPO-universal: 52--93\\% of proved samples across reward types.\n  \\item \\textbf{H7: Conclusion duplication.} A single premise identical to the conclusion. ISR-specific: 64.5\\% under ISR $\\beta{=}0.1$ vs 0\\% under random.\n  \\item \\textbf{Tautological collapse.} Two-component formalizations where premise$=$conclusion (exec-only s44, 94\\% of outputs).\n  \\item \\textbf{Repetition collapse.} Identical premises repeated until the token limit (exec-only s43, 87\\% hit max\\_new\\_tokens).\n  \\item \\textbf{Complexity-without-utility.} Syntactically complex but semantically vacuous premises (random $\\beta{=}0.3$).\n  \\item \\textbf{Contradiction explosion.} Excessive premises (mean 18.55 components at 1000 steps) that trivially entail any conclusion.\n  \\item \\textbf{Query-as-fact gaming.} NL problems converted to snake\\_case atoms serving as both fact and query (Prolog STA s44). Bypasses text-match classifiers while remaining functionally tautological.\n\\end{enumerate}\n\nThe reward signal determines hacking \\emph{composition} but not \\emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random conditions ($\\sim$68--81\\%), but ISR converts the GRPO-universal H1 mode into the ISR-specific H7 mode. SFT remains the only condition with near-zero hacking (92.9\\% genuine), confirming that hacking is RL-reward-specific.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 65_

Word count and structure check:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "21d924b9-bf98-41ae-bf20-6ea64288b2b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P66EZKCx32uNgK9xiBV9v5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5884,
      "cache_read_input_tokens": 57858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5884
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

_source line 66_

<details open><summary>🔧 Tool call — Bash · `toolu_01ABpqRVXnpwh54BBjvBBCiB`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "description": "Count words in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "8831ee4b-0be1-439a-9358-9ab2365e3ce8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P66EZKCx32uNgK9xiBV9v5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5884,
      "cache_read_input_tokens": 57858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5884
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

_source line 67 · 2026-05-14T18:53:24.771Z_

<details><summary>↩ Tool result · `toolu_01ABpqRVXnpwh54BBjvBBCiB`</summary>

```text
2158 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "c3f533ad-31df-4a45-8c45-5e65dbab0d7c",
  "tool_use_result": {
    "stdout": "2158 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Runtime record

_source line 68_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778800200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "084fb34f-9fe0-4e38-a7d3-c39efbfa94f8",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf"
}
```

---

### Assistant

_source line 69_

<details><summary>Logged reasoning block</summary>

```text
The word count is 2158, which is under the 2800 budget. But this includes LaTeX markup. Let me strip the LaTeX commands to get a more accurate text word count.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "0b90396c-b86a-42da-9017-3e23d7351805",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6ksvkNk27wwneC6WFKnjb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 167,
      "cache_read_input_tokens": 63742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 167
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

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_01DtHf1WwMDDDTWYDEhdX8Zt`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}%$]//g; s/&//g' | wc -w",
  "description": "Count words excluding LaTeX markup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "14a0b7f2-9ed2-43e8-a366-e31f28824dd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6ksvkNk27wwneC6WFKnjb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 167,
      "cache_read_input_tokens": 63742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 167
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

_source line 71 · 2026-05-14T18:53:30.311Z_

<details><summary>↩ Tool result · `toolu_01DtHf1WwMDDDTWYDEhdX8Zt`</summary>

```text
1734
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "786d2083-dd9c-415d-a171-b16313bf57ea",
  "tool_use_result": {
    "stdout": "1734",
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

_source line 72_

<details><summary>Logged reasoning block</summary>

```text
The text word count (excluding LaTeX markup) is about 1734, which is well within the 2800 budget. But the raw word count including markup is 2158. In academic papers, the word count typically refers to the rendered text. Let me check the actual rendered word count more carefully. Actually, for an EMNLP paper, 2800 words for the Experiments section is quite generous. The current draft is ~1734 words of actual text content. That's a bit lean but covers all the claims. Let me consider whether I should expand any sections.

Actually, looking at the writing plan more carefully, the word budget is 2800 and I'm at ~1734. 

I've got solid coverage of all the key claims and data points with room to spare, so I'll move forward with registering the artifact and generating the JSON report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "8c2cb409-f675-4b5f-95d3-100dedc7540a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XVzttmyK2mwLfzRj9gBhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 63909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 73_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "9fa9d299-cd5a-4a21-9a01-d621245a390e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XVzttmyK2mwLfzRj9gBhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 63909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 74_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RGmrpJP23xL64xtL1FZhKM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "0a0de323-65a0-48fd-a821-932df6958c8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XVzttmyK2mwLfzRj9gBhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 63909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 75 · 2026-05-14T18:53:40.427Z_

<details><summary>↩ Tool result · `toolu_01RGmrpJP23xL64xtL1FZhKM`</summary>

````text
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
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "a412bbc4-546b-427b-80a6-bbcde05c93dc",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_012hDSo5biQdXxnM4VRfYeHj`</summary>

```json
{
  "name": "experiments-section-draft",
  "type": "paper",
  "description": "EMNLP 2026 Experiments section (§4) draft — covers Setup, ISR as Diagnostic (Claim 1), Meta-Level Goodhart (Claim 2), Cross-Logic Transfer (Claim 3), and 7-mode Hacking Taxonomy. ~2160 words with LaTeX markup.",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "tags": [
    "paper",
    "experiments",
    "draft-v1"
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
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "d0fb0439-8ac8-4a4a-921e-6134c3242081",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrT26LwnfCfSMDutTgfoFQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 928,
      "cache_read_input_tokens": 64143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 928
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

_source line 77 · 2026-05-14T18:53:48.403Z_

<details><summary>↩ Tool result · `toolu_012hDSo5biQdXxnM4VRfYeHj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_27bfee\", \"name\": \"experiments-section-draft\", \"type\": \"paper\", \"description\": \"EMNLP 2026 Experiments section (§4) draft — covers Setup, ISR as Diagnostic (Claim 1), Meta-Level Goodhart (Claim 2), Cross-Logic Transfer (Claim 3), and 7-mode Hacking Taxonomy. ~2160 words with LaTeX markup.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/paper/experiments.tex\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T18:53:48.301784+00:00\", \"tags\": [\"paper\", \"experiments\", \"draft-v1\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "a71b0da7-d269-4db7-bd53-8fbc8b6609c3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_27bfee\\\", \\\"name\\\": \\\"experiments-section-draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"EMNLP 2026 Experiments section (§4) draft — covers Setup, ISR as Diagnostic (Claim 1), Meta-Level Goodhart (Claim 2), Cross-Logic Transfer (Claim 3), and 7-mode Hacking Taxonomy. ~2160 words with LaTeX markup.\\\", \\\"path\\\": \\\"projects/solver-trace-ablation/artifacts/_project/paper/experiments.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"solver-trace-ablation\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T18:53:48.301784+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"experiments\\\", \\\"draft-v1\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_27bfee\", \"name\": \"experiments-section-draft\", \"type\": \"paper\", \"description\": \"EMNLP 2026 Experiments section (§4) draft — covers Setup, ISR as Diagnostic (Claim 1), Meta-Level Goodhart (Claim 2), Cross-Logic Transfer (Claim 3), and 7-mode Hacking Taxonomy. ~2160 words with LaTeX markup.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/paper/experiments.tex\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T18:53:48.301784+00:00\", \"tags\": [\"paper\", \"experiments\", \"draft-v1\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 78_

```json
{
  "section": "experiments",
  "word_count": {
    "with_markup": 2158,
    "text_only_approx": 1734,
    "budget": 2800
  },
  "citations_needed": [
    "deepseekmath (GRPO)",
    "proofwriter (data)",
    "manheim-goodhart-taxonomy (Goodhart taxonomy)",
    "karwowski-goodhart-rl (Goodhart in RL)"
  ],
  "figures_needed": [
    {
      "id": "fig2_isr_collapse",
      "type": "dual-axis line plot",
      "data": "plan003 (100 steps), plan001-s42-r2 (500 steps), plan016 (1000 steps)",
      "status": "placeholder"
    },
    {
      "id": "fig3_hacking_composition",
      "type": "stacked bar chart",
      "data": "exec-only s42, ISR β=0.1 s42/s43/s44, random β=0.1 3-seed mean, SFT",
      "status": "placeholder"
    }
  ],
  "tables_needed": [
    {
      "id": "tab1_goodhart_landscape",
      "caption": "Goodhart landscape across reward conditions",
      "rows": 6,
      "status": "inline"
    },
    {
      "id": "tab4_beta01_3seed",
      "caption": "ISR vs Random β=0.1 3-seed comparison",
      "rows": 6,
      "status": "inline"
    },
    {
      "id": "tab5_prolog_crosslogic",
      "caption": "Cross-logic transfer (FOL + Prolog)",
      "rows": 9,
      "status": "inline"
    }
  ],
  "notes": [
    "Tab2 (hacking taxonomy detail) folded into §4.5 enumerated list + Fig 3 — saves table float",
    "7 hacking modes listed per Director correction (query-as-fact = mode 7)",
    "Prolog s44 Reviewer correction applied: 0% genuine, query-as-fact gaming",
    "Premise-count-matched 1.06x analysis included; 2.4x language removed",
    "C006 ISR semantic distinction (redundant coding vs metric gaming) addressed in §4.4",
    "Random β=0.1 s43 data missing (was RUNNING) — 3-seed mean uses all 3 seeds per Director data override",
    "~640 words of budget remaining — can expand if reviewer anticipation paragraphs needed"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "uuid": "815ef291-a8f4-439c-86d2-0e91cd78e03a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUjKpQvBCYHVKkYctn7hyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 65071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
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

_source line 79_

```json
{
  "section": "experiments",
  "word_count": {
    "with_markup": 2158,
    "text_only_approx": 1734,
    "budget": 2800
  },
  "citations_needed": [
    "deepseekmath (GRPO)",
    "proofwriter (data)",
    "manheim-goodhart-taxonomy (Goodhart taxonomy)",
    "karwowski-goodhart-rl (Goodhart in RL)"
  ],
  "figures_needed": [
    {
      "id": "fig2_isr_collapse",
      "type": "dual-axis line plot",
      "data": "plan003 (100 steps), plan001-s42-r2 (500 steps), plan016 (1000 steps)",
      "status": "placeholder"
    },
    {
      "id": "fig3_hacking_composition",
      "type": "stacked bar chart",
      "data": "exec-only s42, ISR β=0.1 s42/s43/s44, random β=0.1 3-seed mean, SFT",
      "status": "placeholder"
    }
  ],
  "tables_needed": [
    {
      "id": "tab1_goodhart_landscape",
      "caption": "Goodhart landscape across reward conditions",
      "rows": 6,
      "status": "inline"
    },
    {
      "id": "tab4_beta01_3seed",
      "caption": "ISR vs Random β=0.1 3-seed comparison",
      "rows": 6,
      "status": "inline"
    },
    {
      "id": "tab5_prolog_crosslogic",
      "caption": "Cross-logic transfer (FOL + Prolog)",
      "rows": 9,
      "status": "inline"
    }
  ],
  "notes": [
    "Tab2 (hacking taxonomy detail) folded into §4.5 enumerated list + Fig 3 — saves table float",
    "7 hacking modes listed per Director correction (query-as-fact = mode 7)",
    "Prolog s44 Reviewer correction applied: 0% genuine, query-as-fact gaming",
    "Premise-count-matched 1.06x analysis included; 2.4x language removed",
    "C006 ISR semantic distinction (redundant coding vs metric gaming) addressed in §4.4",
    "Random β=0.1 s43 data missing (was RUNNING) — 3-seed mean uses all 3 seeds per Director data override",
    "~640 words of budget remaining — can expand if reviewer anticipation paragraphs needed"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 234782,
  "duration_api_ms": 235182,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "0a1a0156-b769-4b25-b997-fd48e14477bf",
  "total_cost_usd": 0.89994495,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 53923,
    "cache_read_input_tokens": 572670,
    "output_tokens": 8728,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 53923,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 678,
        "cache_read_input_tokens": 65071,
        "cache_creation_input_tokens": 693,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 693
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 4318,
      "outputTokens": 1665,
      "cacheReadInputTokens": 60407,
      "cacheCreationInputTokens": 31686,
      "webSearchRequests": 0,
      "costUSD": 0.0582912,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 8728,
      "cacheReadInputTokens": 572670,
      "cacheCreationInputTokens": 53923,
      "webSearchRequests": 0,
      "costUSD": 0.84165375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "78842076-337f-4b4a-be4a-5b57730ea420"
}
```

</details>

---
