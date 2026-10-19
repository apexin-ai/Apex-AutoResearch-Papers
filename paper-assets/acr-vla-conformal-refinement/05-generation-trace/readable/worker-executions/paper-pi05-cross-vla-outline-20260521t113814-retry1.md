# paper pi05 cross vla outline 20260521T113814 retry1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_paper_pi05-cross-vla-outline_20260521T113814_retry1.log`
- **Structured JSON:** [`22419eb17cf776786ee8.json`](../../sessions/22/22419eb17cf776786ee8.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
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
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "402cea4a-b9a6-40ad-a406-7b8b933f7f60",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779379800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0b2fe142-ca15-41fe-8993-b3911de7a41d",
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "8307a37a-f4a0-4ba6-a47b-d788400769a7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WgWYSo7mnGdZS58X13NhLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 14850,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14850
      },
      "output_tokens": 0,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SQHyKAfhoLGQ68FpF3g7Nf`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "32e68c07-eaf7-47e4-9f33-48bb686968a3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WgWYSo7mnGdZS58X13NhLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 14850,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14850
      },
      "output_tokens": 0,
      "service_tier": "standard",
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

_source line 6 · 2026-05-21T11:38:37.306Z_

<details><summary>↩ Tool result · `toolu_01SQHyKAfhoLGQ68FpF3g7Nf`</summary>

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
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "b2bc6603-5ce8-4c34-a47b-4205ebc371b3",
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "a8cd793a-3fee-4e8f-a133-e325b2521ccd",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XTeCd8SAV56bQWT2n7z2VP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15863,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15863
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28798
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01X4ZscU5yDevk5YGC47HdWb`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "6987f835-57ed-4fe6-b27b-e62dbc520493",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XTeCd8SAV56bQWT2n7z2VP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15863,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15863
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28798
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T11:38:40.725Z_

<details><summary>↩ Tool result · `toolu_01X4ZscU5yDevk5YGC47HdWb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\n\\n## Target Venue\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\n- Title: \\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\"\\n\\n## Core Insight (D065 revised)\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\n\\n## Headline Metrics\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\n\\n## Core Claims (3 claims, D061)\\n\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\n\\n### C2: Conditioning-magnitude interaction — first systematic study\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\n\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\"recognizes\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\n\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\n\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\n\\n**信号验证结果 (D076)**:\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\n\\n**确定的架构**:\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\"困难步\\\"）\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\"简单步\\\"）\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\n\\n**Phase 2 结果 (Object)**:\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\n- Spatial 跨 benchmark 验证完成\\n\\n**对论文 framing 的影响**:\\n- 从纯 analysis paper 升级为 analysis + method paper\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\n- K=10 固定推理保留为 oracle upper bound\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\n\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\n\\n**D088 Learned Uncertainty Head — NO-GO**:\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\n\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\n\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\n\\n**对论文影响 (D091)**:\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\n\\n## Story Spine\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVL\\n\\n... [截断: 省略 14168 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 26168, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "813632dd-3748-4acf-932a-b72cf85afb58",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — acr-vla-conformal-refinement\\\\n\\\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\\\n\\\\n## Target Venue\\\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\\\n- Title: \\\\\\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\\\\\"\\\\n\\\\n## Core Insight (D065 revised)\\\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\\\n\\\\n## Headline Metrics\\\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\\\n\\\\n## Core Claims (3 claims, D061)\\\\n\\\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\\\n\\\\n### C2: Conditioning-magnitude interaction — first systematic study\\\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\\\n\\\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\\\\\"recognizes\\\\\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\\\n\\\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\\\n\\\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\\\n\\\\n**信号验证结果 (D076)**:\\\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\\\n\\\\n**确定的架构**:\\\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\\\\\"困难步\\\\\\\"）\\\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\\\\\"简单步\\\\\\\"）\\\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\\\n\\\\n**Phase 2 结果 (Object)**:\\\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\\\n- Spatial 跨 benchmark 验证完成\\\\n\\\\n**对论文 framing 的影响**:\\\\n- 从纯 analysis paper 升级为 analysis + method paper\\\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\\\n- K=10 固定推理保留为 oracle upper bound\\\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\\\n\\\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\\\n\\\\n**D088 Learned Uncertainty Head — NO-GO**:\\\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\\\n\\\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\\\n\\\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\\\n\\\\n**对论文影响 (D091)**:\\\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\\\n\\\\n## Story Spine\\\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVL\\\\n\\\\n... [截断: 省略 14168 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 26168, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\n\\n## Target Venue\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\n- Title: \\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\"\\n\\n## Core Insight (D065 revised)\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\n\\n## Headline Metrics\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\n\\n## Core Claims (3 claims, D061)\\n\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\n\\n### C2: Conditioning-magnitude interaction — first systematic study\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\n\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\"recognizes\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\n\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\n\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\n\\n**信号验证结果 (D076)**:\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\n\\n**确定的架构**:\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\"困难步\\\"）\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\"简单步\\\"）\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\n\\n**Phase 2 结果 (Object)**:\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\n- Spatial 跨 benchmark 验证完成\\n\\n**对论文 framing 的影响**:\\n- 从纯 analysis paper 升级为 analysis + method paper\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\n- K=10 固定推理保留为 oracle upper bound\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\n\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\n\\n**D088 Learned Uncertainty Head — NO-GO**:\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\n\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\n\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\n\\n**对论文影响 (D091)**:\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\n\\n## Story Spine\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVL\\n\\n... [截断: 省略 14168 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 26168, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GsJ36AztmrNLeJGj8QB6vm`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "f7513358-6592-4526-b2e2-4e4a9e70faf1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XTeCd8SAV56bQWT2n7z2VP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15863,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15863
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28798
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T11:38:41.298Z_

<details><summary>↩ Tool result · `toolu_01GsJ36AztmrNLeJGj8QB6vm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-21 08:04 UTC | 更新原因: D103 π0.5 72% SR confirmed, full baseline eval + CRM pipeline approved\\n\\n> 详见 paper_framing.md（D077→D092→D097→D103）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance + selective CRM correction。Plan A = Pareto 最优。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **≤8 天**。\\n\\n## 阶段\\n**π0.5 全量 eval 部署中 + 论文收尾**。SmolVLA 全部 LOCKED。π0.5 修复通过 (D103)。\\n\\n## Plan A 核心结果 (LOCKED)\\n| Benchmark | Plan A (K=2) | K=10 CRM | VLA-only | Δ vs VLA-only |\\n|-----------|-------------|----------|----------|---------------|\\n| Object    | 18.3%±2.1%  | 16.8%±1.8% | 10.8%±1.3% | +7.5pp |\\n| Spatial   | 35.0%±1.0%  | 34.5%±1.5% | 29.4%±1.5% | +5.6pp |\\n\\n## K=20 Sweep (LOCKED, D102)\\n- Object: 18.8%±1.0% (n=4) ≈ K=2 18.3% → K=2 足够\\n- Spatial: 34.3%±0.6% (n=3) ≈ K=2 35.0% → diminishing returns 确认\\n\\n## Latency (LOCKED, D097)\\nCRM forward: 0.28ms | Plan A speedup: 1.82× | CRM pipeline vs K=10: -1.66%\\n\\n## Norm Sweep (ALL LOCKED) → Figure 2 v4 完成 ✅\\n| ε | n | mean | std |\\n|------|-----|-------|------|\\n| 0.03 | 13 | 15.1% | ~1.2% |\\n| 0.05 | 16 | 13.9% | ~1.4% |\\n| 0.1 | 20 | 15.3% | ~2.3% |\\n| 0.2 | 12 | 17.2% | ~1.8% |\\n\\n## Spatial Adaptive K Sweep (ALL LOCKED, D100)\\nPlan A 35.0% > P90 33.0% > P75 32.7% > P50 32.0% > P25 31.7%\\n\\n## Random Selection (LOCKED)\\nObject 9.7% ≈ VLA-only 10.8% | Spatial 29.3% ≈ VLA-only 29.4%\\n\\n## OpenVLA Applicability Boundary (LOCKED, D093)\\nBaseline 69% → +CRM 0%。Near-deterministic。方法需要 stochastic VLA。\\n\\n## π0.5 实验线 (D095→D103) 🔥\\n- ✅ D103: Quick verify **72% SR** (50 rollouts, 10/10 tasks 非零)\\n- 根因: 图像 180° 翻转缺失 (M040)，一行修复\\n- 🔄 **当前**: 全量 baseline eval 部署中 (3 seeds × Object + Spatial, bjb1-32546 6 GPU)\\n- **下一步**: CRM projection 2048→960 训练 → precompute → Plan A eval\\n- **论文定位**: cross-VLA 验证 (0.4B SmolVLA vs 3.6B π0.5)。72% baseline 上 CRM 增益空间有限，需诚实讨论\\n\\n## 论文状态\\nFigure 2 v4 ✅ | Spatial sweep table ✅ | Latency table ✅ | Per-DOF §4.4 ✅ | Random Selection ✅ | 编译 OK 8 页\\n待写入: K=20 ablation table, π0.5 cross-VLA 结果\\n\\n## GPU 状态\\n17 GPU / 4 servers。6 GPU 部署 π0.5 baseline eval (bjb1-32546)。\\n\\n## 近期任务\\n- [ ] **P0** π0.5 baseline eval 完成 → harvest\\n- [ ] **P0** π0.5 CRM pipeline (precompute → projection → eval) ~10-15 GPU-h\\n- [ ] **P1** K=20 + π0.5 结果写入论文 (Paper Agent)\\n- [ ] **P2** 论文 final review + submission prep\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D103 | 2026-05-21 | D103: π0.5 图像翻转修复通过 — VLA-only 72% SR (Object quic | eval-pi05-baseline-object-seed42-r2 |\\n| D102 | 2026-05-21 | D102: K=20 Sweep LOCKED — K=20 ≈ K=2，增加K不改善性能，强力支持 | eval-k20-obs-only-object-seed42, eval-k20-obs-only-object-seed43, eval-k20-obs-only-object-seed44, eval-k20-obs-only-object-seed45, eval-k20-obs-only-spatial-seed42, eval-k20-obs-only-spatial-seed43, eval-k20-obs-only-spatial-seed44 |\\n| D101 | 2026-05-21 | D101: π0.5 模型有效 (lerobot-eval 100% SR) — wrapper b | eval-pi05-baseline-object-seed42-r2, eval:pi05-official-lerobot-last-attempt |\\n| D100 | 2026-05-21 | D100: Spatial Adaptive K Sweep LOCKED — P90 33.0%± | eval-adaptive-k-spatial-p90-seed44, eval-adaptive-k-spatial-p90-seed44-bjb2 |\\n| D099 | 2026-05-21 | D099: π0.5 根因确认——action chunk 只取 step[0] 而非开环执行 50 | eval-pi05-baseline-object-seed42-r2, eval-pi05-baseline-object-seed42 |\\n| D098 | 2026-05-21 | D098: π0.5 fix3 task1=0% 但不终止——等全 10 task 完成后决策 +  | eval-pi05-baseline-object-seed42-r2, eval-obs-only-object-norm02-k20-seed44 |\\n| D097 | 2026-05-21 | D097: Spatial Adaptive K Sweep + Latency Profile 完 | eval-adaptive-k-spatial-p50-seed42, eval-adaptive-k-spatial-p50-seed43, eval-adaptive-k-spatial-p50-seed44, eval-adaptive-k-spatial-p90-seed44-bjb2 |\\n| D096 | 2026-05-21 | D096: π0.5 适配 GO — baseline >60%, 7D action, flow- | eval-openvla-crm-object-seed42, eval-plan-a-object-seed42 |\\n| D095 | 2026-05-21 | D095: 新增 π0.5/π VLA baseline + CRM 实验线（用户要求）— flow | eval-openvla-crm-object-seed42 |\\n| D094 | 2026-05-21 | D094: Plan A Spatial 完成 — 35.0%±1.0% (K=2) 超过 K=10 | eval-plan-a-spatial-seed42, eval-plan-a-spatial-seed43, eval-plan-a-spatial-seed44 |\\n\\n\\n\", \"total_chars\": 4053, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "9cbd9900-bfc3-46bf-bf89-313b63164e52",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\\\", \\\"content\\\": \\\"# acr-vla-conformal-refinement — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-21 08:04 UTC | 更新原因: D103 π0.5 72% SR confirmed, full baseline eval + CRM pipeline approved\\\\n\\\\n> 详见 paper_framing.md（D077→D092→D097→D103）\\\\n\\\\n## 核心方向\\\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance + selective CRM correction。Plan A = Pareto 最优。\\\\n\\\\n## 投稿目标\\\\n**CoRL 2026** DDL **2026-05-29**。剩余 **≤8 天**。\\\\n\\\\n## 阶段\\\\n**π0.5 全量 eval 部署中 + 论文收尾**。SmolVLA 全部 LOCKED。π0.5 修复通过 (D103)。\\\\n\\\\n## Plan A 核心结果 (LOCKED)\\\\n| Benchmark | Plan A (K=2) | K=10 CRM | VLA-only | Δ vs VLA-only |\\\\n|-----------|-------------|----------|----------|---------------|\\\\n| Object    | 18.3%±2.1%  | 16.8%±1.8% | 10.8%±1.3% | +7.5pp |\\\\n| Spatial   | 35.0%±1.0%  | 34.5%±1.5% | 29.4%±1.5% | +5.6pp |\\\\n\\\\n## K=20 Sweep (LOCKED, D102)\\\\n- Object: 18.8%±1.0% (n=4) ≈ K=2 18.3% → K=2 足够\\\\n- Spatial: 34.3%±0.6% (n=3) ≈ K=2 35.0% → diminishing returns 确认\\\\n\\\\n## Latency (LOCKED, D097)\\\\nCRM forward: 0.28ms | Plan A speedup: 1.82× | CRM pipeline vs K=10: -1.66%\\\\n\\\\n## Norm Sweep (ALL LOCKED) → Figure 2 v4 完成 ✅\\\\n| ε | n | mean | std |\\\\n|------|-----|-------|------|\\\\n| 0.03 | 13 | 15.1% | ~1.2% |\\\\n| 0.05 | 16 | 13.9% | ~1.4% |\\\\n| 0.1 | 20 | 15.3% | ~2.3% |\\\\n| 0.2 | 12 | 17.2% | ~1.8% |\\\\n\\\\n## Spatial Adaptive K Sweep (ALL LOCKED, D100)\\\\nPlan A 35.0% > P90 33.0% > P75 32.7% > P50 32.0% > P25 31.7%\\\\n\\\\n## Random Selection (LOCKED)\\\\nObject 9.7% ≈ VLA-only 10.8% | Spatial 29.3% ≈ VLA-only 29.4%\\\\n\\\\n## OpenVLA Applicability Boundary (LOCKED, D093)\\\\nBaseline 69% → +CRM 0%。Near-deterministic。方法需要 stochastic VLA。\\\\n\\\\n## π0.5 实验线 (D095→D103) 🔥\\\\n- ✅ D103: Quick verify **72% SR** (50 rollouts, 10/10 tasks 非零)\\\\n- 根因: 图像 180° 翻转缺失 (M040)，一行修复\\\\n- 🔄 **当前**: 全量 baseline eval 部署中 (3 seeds × Object + Spatial, bjb1-32546 6 GPU)\\\\n- **下一步**: CRM projection 2048→960 训练 → precompute → Plan A eval\\\\n- **论文定位**: cross-VLA 验证 (0.4B SmolVLA vs 3.6B π0.5)。72% baseline 上 CRM 增益空间有限，需诚实讨论\\\\n\\\\n## 论文状态\\\\nFigure 2 v4 ✅ | Spatial sweep table ✅ | Latency table ✅ | Per-DOF §4.4 ✅ | Random Selection ✅ | 编译 OK 8 页\\\\n待写入: K=20 ablation table, π0.5 cross-VLA 结果\\\\n\\\\n## GPU 状态\\\\n17 GPU / 4 servers。6 GPU 部署 π0.5 baseline eval (bjb1-32546)。\\\\n\\\\n## 近期任务\\\\n- [ ] **P0** π0.5 baseline eval 完成 → harvest\\\\n- [ ] **P0** π0.5 CRM pipeline (precompute → projection → eval) ~10-15 GPU-h\\\\n- [ ] **P1** K=20 + π0.5 结果写入论文 (Paper Agent)\\\\n- [ ] **P2** 论文 final review + submission prep\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D103 | 2026-05-21 | D103: π0.5 图像翻转修复通过 — VLA-only 72% SR (Object quic | eval-pi05-baseline-object-seed42-r2 |\\\\n| D102 | 2026-05-21 | D102: K=20 Sweep LOCKED — K=20 ≈ K=2，增加K不改善性能，强力支持 | eval-k20-obs-only-object-seed42, eval-k20-obs-only-object-seed43, eval-k20-obs-only-object-seed44, eval-k20-obs-only-object-seed45, eval-k20-obs-only-spatial-seed42, eval-k20-obs-only-spatial-seed43, eval-k20-obs-only-spatial-seed44 |\\\\n| D101 | 2026-05-21 | D101: π0.5 模型有效 (lerobot-eval 100% SR) — wrapper b | eval-pi05-baseline-object-seed42-r2, eval:pi05-official-lerobot-last-attempt |\\\\n| D100 | 2026-05-21 | D100: Spatial Adaptive K Sweep LOCKED — P90 33.0%± | eval-adaptive-k-spatial-p90-seed44, eval-adaptive-k-spatial-p90-seed44-bjb2 |\\\\n| D099 | 2026-05-21 | D099: π0.5 根因确认——action chunk 只取 step[0] 而非开环执行 50 | eval-pi05-baseline-object-seed42-r2, eval-pi05-baseline-object-seed42 |\\\\n| D098 | 2026-05-21 | D098: π0.5 fix3 task1=0% 但不终止——等全 10 task 完成后决策 +  | eval-pi05-baseline-object-seed42-r2, eval-obs-only-object-norm02-k20-seed44 |\\\\n| D097 | 2026-05-21 | D097: Spatial Adaptive K Sweep + Latency Profile 完 | eval-adaptive-k-spatial-p50-seed42, eval-adaptive-k-spatial-p50-seed43, eval-adaptive-k-spatial-p50-seed44, eval-adaptive-k-spatial-p90-seed44-bjb2 |\\\\n| D096 | 2026-05-21 | D096: π0.5 适配 GO — baseline >60%, 7D action, flow- | eval-openvla-crm-object-seed42, eval-plan-a-object-seed42 |\\\\n| D095 | 2026-05-21 | D095: 新增 π0.5/π VLA baseline + CRM 实验线（用户要求）— flow | eval-openvla-crm-object-seed42 |\\\\n| D094 | 2026-05-21 | D094: Plan A Spatial 完成 — 35.0%±1.0% (K=2) 超过 K=10 | eval-plan-a-spatial-seed42, eval-plan-a-spatial-seed43, eval-plan-a-spatial-seed44 |\\\\n\\\\n\\\\n\\\", \\\"total_chars\\\": 4053, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-21 08:04 UTC | 更新原因: D103 π0.5 72% SR confirmed, full baseline eval + CRM pipeline approved\\n\\n> 详见 paper_framing.md（D077→D092→D097→D103）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance + selective CRM correction。Plan A = Pareto 最优。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **≤8 天**。\\n\\n## 阶段\\n**π0.5 全量 eval 部署中 + 论文收尾**。SmolVLA 全部 LOCKED。π0.5 修复通过 (D103)。\\n\\n## Plan A 核心结果 (LOCKED)\\n| Benchmark | Plan A (K=2) | K=10 CRM | VLA-only | Δ vs VLA-only |\\n|-----------|-------------|----------|----------|---------------|\\n| Object    | 18.3%±2.1%  | 16.8%±1.8% | 10.8%±1.3% | +7.5pp |\\n| Spatial   | 35.0%±1.0%  | 34.5%±1.5% | 29.4%±1.5% | +5.6pp |\\n\\n## K=20 Sweep (LOCKED, D102)\\n- Object: 18.8%±1.0% (n=4) ≈ K=2 18.3% → K=2 足够\\n- Spatial: 34.3%±0.6% (n=3) ≈ K=2 35.0% → diminishing returns 确认\\n\\n## Latency (LOCKED, D097)\\nCRM forward: 0.28ms | Plan A speedup: 1.82× | CRM pipeline vs K=10: -1.66%\\n\\n## Norm Sweep (ALL LOCKED) → Figure 2 v4 完成 ✅\\n| ε | n | mean | std |\\n|------|-----|-------|------|\\n| 0.03 | 13 | 15.1% | ~1.2% |\\n| 0.05 | 16 | 13.9% | ~1.4% |\\n| 0.1 | 20 | 15.3% | ~2.3% |\\n| 0.2 | 12 | 17.2% | ~1.8% |\\n\\n## Spatial Adaptive K Sweep (ALL LOCKED, D100)\\nPlan A 35.0% > P90 33.0% > P75 32.7% > P50 32.0% > P25 31.7%\\n\\n## Random Selection (LOCKED)\\nObject 9.7% ≈ VLA-only 10.8% | Spatial 29.3% ≈ VLA-only 29.4%\\n\\n## OpenVLA Applicability Boundary (LOCKED, D093)\\nBaseline 69% → +CRM 0%。Near-deterministic。方法需要 stochastic VLA。\\n\\n## π0.5 实验线 (D095→D103) 🔥\\n- ✅ D103: Quick verify **72% SR** (50 rollouts, 10/10 tasks 非零)\\n- 根因: 图像 180° 翻转缺失 (M040)，一行修复\\n- 🔄 **当前**: 全量 baseline eval 部署中 (3 seeds × Object + Spatial, bjb1-32546 6 GPU)\\n- **下一步**: CRM projection 2048→960 训练 → precompute → Plan A eval\\n- **论文定位**: cross-VLA 验证 (0.4B SmolVLA vs 3.6B π0.5)。72% baseline 上 CRM 增益空间有限，需诚实讨论\\n\\n## 论文状态\\nFigure 2 v4 ✅ | Spatial sweep table ✅ | Latency table ✅ | Per-DOF §4.4 ✅ | Random Selection ✅ | 编译 OK 8 页\\n待写入: K=20 ablation table, π0.5 cross-VLA 结果\\n\\n## GPU 状态\\n17 GPU / 4 servers。6 GPU 部署 π0.5 baseline eval (bjb1-32546)。\\n\\n## 近期任务\\n- [ ] **P0** π0.5 baseline eval 完成 → harvest\\n- [ ] **P0** π0.5 CRM pipeline (precompute → projection → eval) ~10-15 GPU-h\\n- [ ] **P1** K=20 + π0.5 结果写入论文 (Paper Agent)\\n- [ ] **P2** 论文 final review + submission prep\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D103 | 2026-05-21 | D103: π0.5 图像翻转修复通过 — VLA-only 72% SR (Object quic | eval-pi05-baseline-object-seed42-r2 |\\n| D102 | 2026-05-21 | D102: K=20 Sweep LOCKED — K=20 ≈ K=2，增加K不改善性能，强力支持 | eval-k20-obs-only-object-seed42, eval-k20-obs-only-object-seed43, eval-k20-obs-only-object-seed44, eval-k20-obs-only-object-seed45, eval-k20-obs-only-spatial-seed42, eval-k20-obs-only-spatial-seed43, eval-k20-obs-only-spatial-seed44 |\\n| D101 | 2026-05-21 | D101: π0.5 模型有效 (lerobot-eval 100% SR) — wrapper b | eval-pi05-baseline-object-seed42-r2, eval:pi05-official-lerobot-last-attempt |\\n| D100 | 2026-05-21 | D100: Spatial Adaptive K Sweep LOCKED — P90 33.0%± | eval-adaptive-k-spatial-p90-seed44, eval-adaptive-k-spatial-p90-seed44-bjb2 |\\n| D099 | 2026-05-21 | D099: π0.5 根因确认——action chunk 只取 step[0] 而非开环执行 50 | eval-pi05-baseline-object-seed42-r2, eval-pi05-baseline-object-seed42 |\\n| D098 | 2026-05-21 | D098: π0.5 fix3 task1=0% 但不终止——等全 10 task 完成后决策 +  | eval-pi05-baseline-object-seed42-r2, eval-obs-only-object-norm02-k20-seed44 |\\n| D097 | 2026-05-21 | D097: Spatial Adaptive K Sweep + Latency Profile 完 | eval-adaptive-k-spatial-p50-seed42, eval-adaptive-k-spatial-p50-seed43, eval-adaptive-k-spatial-p50-seed44, eval-adaptive-k-spatial-p90-seed44-bjb2 |\\n| D096 | 2026-05-21 | D096: π0.5 适配 GO — baseline >60%, 7D action, flow- | eval-openvla-crm-object-seed42, eval-plan-a-object-seed42 |\\n| D095 | 2026-05-21 | D095: 新增 π0.5/π VLA baseline + CRM 实验线（用户要求）— flow | eval-openvla-crm-object-seed42 |\\n| D094 | 2026-05-21 | D094: Plan A Spatial 完成 — 35.0%±1.0% (K=2) 超过 K=10 | eval-plan-a-spatial-seed42, eval-plan-a-spatial-seed43, eval-plan-a-spatial-seed44 |\\n\\n\\n\", \"total_chars\": 4053, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01V9oLD9byj9zqUDDNreYCwK`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "ba9cf4c5-3522-49ec-b520-132e70bbbc8c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XTeCd8SAV56bQWT2n7z2VP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15863,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15863
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28798
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T11:38:41.928Z_

<details><summary>↩ Tool result · `toolu_01V9oLD9byj9zqUDDNreYCwK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Project Memory\\n\\n## 失败模式记录\\n\\n- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。\\n\\n- [失败模式] Cron false positive（2026-05-20）：**eval-adaptive-k-spatial-p50-seed42** 被 cron 误判为 failed（\\\"process dead 5× with no sentinel/W&B\\\"）。实际情况：原 PID 675831 被 deploy worker kill 后，重启为 PID 681823。重启后进程正常运行，但 cron 监控未追踪到新 PID，5 次检测均未发现 sentinel → 自动标记 failed。诊断时（2026-05-20）PID 681823 仍在运行（状态 Rl+，已运行 17h36m），已完成 3/10 tasks（SR: 70%/100%/0%），第 4 个 task 进行中（rollout 5, 1/5 success）。GPU 使用 5972/24564 MiB，日志无错误。**无需重新提交，等待自然完成后手动修正 conclusion。**\\n\\n- [失败模式] SIGHUP false failure（2026-05-20）：bjb2-28827 上多个实验 EXIT_CODE=129 (SIGHUP) 被标记 failed，实际全部完成。**已确认受影响：P75-seed44, P90-seed42, P25-seed44**。SIGHUP 发生在进程写完结果 JSON 之后（tmux session 断开或 SSH 连接清理）。**诊断方法：tail 日志看 \\\"Results saved to\\\" + \\\"Overall success rate\\\" 行 → 手动修正 conclusion=success 并补录 metrics。**\\n\\n- [失败模式] Cron 日志路径不匹配（2026-05-20）：**eval-obs-only-goal-norm02-seed51** (bjb1-32546) 被 cron 误判 dead。根因：实验日志写入 `/root/acr-vla-conformal-refinement/logs/`（项目目录下），但 cron 监控在 `~/runs/acr-vla-conformal-refinement/` 下找日志 → 找不到 → 5 次检测均无 sentinel → auto-resolved failed。**教训：submit_training_job 的 log_path 必须与实际 tee 输出路径一致。部分实验用 `tee logs/xxx.log`（相对于 cd 后的项目目录），另一部分用 `~/runs/` 绝对路径，两套路径并存导致 cron 误判。**\\n\\n- [失败模式] Cron false positive 批量（2026-05-20 诊断）：bjb1-32546 上 **eval-perdof-object-norm02-seed50** (PID 542405) 和 **eval-obs-only-object-norm02-seed51** (PID 542894) 被 cron 报告 \\\"process gone, no sentinel, no W&B\\\"。实际两者均已**正常完成**，output JSON 已写入。bjb1-18228 上 **eval-obs-only-object-norm005-seed44** 同样正常完成但被标记 failed。根因同上：eval 脚本不写 sentinel/W&B，进程正常退出后 cron 无法确认完成状态。结果：perdof-norm02-seed50 SR=10.0%, obs_only-norm02-seed51 SR=17.0%, obs_only-norm005-seed44 SR=12.0%。**均无需重跑，需手动修正 conclusion=success 并补录 metrics。**\\n\\n- [失败模式] python PATH 不存在（2026-05-21, bjb1-32546）：`nohup: failed to run command 'python': No such file or directory`。bjb1-32546 使用 conda 环境，`python` 不在默认 PATH 中（仅 `/root/miniconda3/bin/python` 可用）。受影响：seed51-r2, seed52-r2, seed62, seed63（4 个实验同时失败）。**修复方案：提交命令前加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&` 前缀。** 教训：submit_training_job 的 command 不能假设 `python` 在 PATH 中，必须自带环境激活。对照其他服务器（bjb1-18228、bjb2-28827）成功实验的命令格式，它们通过 `bash -c \\\"source ... && python ...\\\"` 包裹。\\n\\n- [失败模式] FMVD 信号无效：ρ=0.0825 NO-GO。根因：denoising 空间统计量不映射到 action uncertainty。\\n\\n- [失败模式] CRM correction magnitude 信号无效（2026-05-20）：ρ(K1_corr_mag, K10_var) = 0.1523 NO-GO。**根因：CRM correction magnitude 是常数 (~0.1205)，P25=P50=P75=P90 几乎相同。** CRM 对所有输入产出相同大小的修正向量——修正方向变化但幅度不变。推测因 max_correction_norm=0.2 的 clipping 使得大部分 correction 被截断到相同 norm。K=2 argmin 版本同样无效 (ρ=0.1340)。**教训：clipped norm 的信号没有方差，自然无法做 gate。**\\n\\n- [失败模式] OpenVLA-7B eval timeout：timeout_hours 至少设 12h。\\n\\n- [失败模式] Table 1 数据混淆（2026-05-20）：Table 1 原报 CRM Object K=10 = 17.6% (n=7)，实际来自 **norm01+norm02 混合数据**。seed42 只有 norm01 (0.19)，seed43 只有 norm02 (0.16)，两个 config 各自只有 n=6，合并后变 n=7。paper_provenance.yaml C029 引用的 exp_id 是抽象 \\\"obs_only_k10\\\" 而非具体实验 ID，导致问题没被及时发现。**教训：provenance 必须引用具体 registry_id，不用抽象标签。**\\n\\n- [失败模式] evaluate.py 路径缺 src/ 前缀（2026-05-20）：adaptive_k spatial 实验命令用 `python evaluate.py` 而非 `python src/evaluate.py`，导致 EXIT_CODE=2 (No such file)。受影响：eval-adaptive-k-spatial-p50-seed43, eval-adaptive-k-spatial-p50-seed44（两台服务器 bjb1-32546, bjb2-28827 同时中招）。**教训：提交命令时对照历史成功实验的 command 格式，evaluate.py 在 src/ 子目录下。**\\n\\n- [失败模式] π0.5 vision tower 权重静默加载失败（2026-05-21）：**5 轮修复全部 0% SR 的真正根因**。checkpoint key 为 `vision_tower.vision_model.encoder.layers.X`，但 transformers 5.8.0 的 SiglipVisionModel 期望 `vision_tower.encoder.layers.X`（无 `vision_model` 中间层）。lerobot 0.5.2 的 `_fix_pytorch_state_dict_keys` 缺少此映射，`load_state_dict(strict=True)` 失败被 try/except 静默捕获，模型以**随机初始化 vision tower 运行** → 0% SR。**官方 lerobot-eval 也有此 bug。** Worker patch lerobot 内部代码后 3/3 = 100% SR。**教训：(1) load_state_dict 的 try/except 必须打印 missing_keys/unexpected_keys，不能静默吞掉 (2) 加载后验证关键层权重统计（mean/std）确认非随机 (3) 0% SR 时优先检查权重加载而非输入预处理。**\\n\\n## seed66 失败诊断 (2026-05-21)\\n- 根因：**Cron false positive（第 N 次）**。3 个 seed66 进程（norm003/norm005/norm01）实际仍在 bjb1-18228 上正常运行，被 cron 误判为 \\\"process dead 5× with no sentinel/W&B\\\"。\\n- 证据：\\n  - PID 642428 (norm003, GPU0), PID 642506 (norm005, GPU2), PID 642775 (norm01, GPU3) 均处于 Rl 状态，CPU 使用 ~400%，GPU 利用率 34-38%，VRAM ~5.7GB/卡\\n  - 日志在两次读取之间从 rollout 5/20 增长到 10/20，确认进程在推进\\n  - sentinels/ 目录完全为空——从未有实验写过 sentinel file\\n  - 无 OOM、无 CUDA error、无 traceback、无 segfault\\n  - 磁盘空间充足（根分区 53%，数据盘未挂载 autodl-tmp 但进程正常读写）\\n- 与 seed65 对比：seed65 (PID 622484, GPU1) 用 `nohup python -u` 启动，日志持续更新；seed66 用 `python3` 启动（无 `-u` 无 nohup），日志因 stdout 缓冲更新延迟，但进程本身正常\\n- 影响范围：eval-obs-only-object-norm005-seed66, eval-obs-only-object-norm01-seed66, eval-obs-only-object-norm003-seed66（3 个实验）\\n- 建议修复：**无需重跑**。等待进程自然完成（n_rollouts=20，当前约 50% 进度，预计再需 1-2 小时），完成后手动修正 conclusion=success 并从 output JSON 补录 metrics。\\n\\n## CRM Coverage 限制\\n\\nCRM v3 训练数据 = Object(10) + Spatial(10) = 20 tasks。Goal/Long 是 OOD 泛化测试。\\n\\n## Adaptive K 信号探索\\n\\n| 信号 | ρ vs K10_var | 结论 | 备注 |\\n|------|-------------|------|------|\\n| FMVD (velocity dispersion) | 0.0825 | ❌ NO-GO | zero-cost 但无效 |\\n| **K=2 L2 divergence** | **0.9979** | **✅ GO** | 需要 K=2 采样（+170ms），near-perfect proxy |\\n| CRM correction magnitude (K=1) | 0.1523 | ❌ NO-GO | zero-cost 但 magnitude 是常数 |\\n| CRM correction magnitude (K=2 argmin) | 0.1340 | ❌ NO-GO | 同上 |\\n\\n**结论：K=2 L2 distance 是唯一可用的 adaptive K 门控信号。** FMVD 和 CRM magnitude 均因信号方差不足而失败。\\n\\n## Adaptive K Sweep 最终结果 — Object (2026-05-20, 12/12 完成)\\n\\n| 阈值 | SR [seeds] | avg_K | fast_path% |\\n|------|-----------|-------|-----------|\\n| P90 (τ=0.127) | 13.3% [12,14,14] | ~2.6 | ~93% |\\n| P75 (τ=0.099) | 13.7% [12,13,16] | ~3.1 | ~87% |\\n| **P50 (τ=0.075)** | **15.3% [16,16,14]** | **~3.8** | **~77%** |\\n| P25 (τ=0.055) | 14.3% [15,13,15] | ~4.8 | ~65% |\\n\\n**P50 = Pareto optimal**: 最高 SR + 比 K=10 省 62% compute (avg_K 3.8 vs 10)。\\n\\n## Adaptive K Cross-Benchmark Sweep — Spatial (2026-05-20, 11/12 done)\\n\\nObject 校准阈值直接迁移到 Spatial（无 per-benchmark tuning）：\\n\\n| 阈值 | seed42 | seed43 | seed44 | Mean±Std | avg_K | fast_path |\\n|------|--------|--------|--------|----------|-------|-----------|\\n| P90 | 31% | 32% | PREPARING | — | ~3.5 | ~80% |\\n| P75 | 31% | 34% | 33% | 32.7%±1.5% | ~5.0 | ~62% |\\n| P50 | 30% | 33% | 33% | 32.0%±1.7% | ~6.35 | ~46% |\\n| P25 | 33% | 30% | 32% | 31.7%±1.5% | ~7.65 | ~29% |\\n\\nvs VLA-only Spatial: 29.6%±1.1% | vs CRM K=10 Spatial: 34.6%±1.4%\\n\\n**关键洞察**：\\n1. 所有阈值 SR 差异很小（31.7-32.7%），但 compute 差异 2x（avg_K 3.5→7.65）。P75 在 Spatial 上 Pareto 最优（32.7% + avg_K 5.0），P50 在 Object 上最优。\\n2. Spatial fast_path 远低于 Object（同阈值下 29% vs 65% for P25）—— Spatial L2 均值更高，方法自动分配更多 full-K steps。\\n3. 这支持\\\"阈值自动适配任务复杂度\\\"的核心 narrative：同一 Object 校准阈值，在更难的 Spatial 上自动降低 fast_path 比例以保持 SR。\\n\\n## Latency Profiling (dry-run N=20, RTX 4090, 2026-05-20)\\n\\n| Component | Mean (ms) | 备注 |\\n|-----------|----------|------|\\n| VLA sampling | 206 | **K 无关**（batched generation） |\\n| CRM MLP forward | 0.33 | 337K params |\\n| Argmin L2 + CRM 总开销 | 4.0 | 管线 1.6% |\\n| Full pipeline K=10 | 259 | ~3.9 Hz |\\n| **Adaptive K 快路径** | **254** | K=2 only |\\n| **Adaptive K 全路径** | **459** | K=2→K=10 |\\n\\n**关键发现：VLA batched sampling 消除 K 作为 latency 因子。Adaptive K 快路径省 45% latency。CRM overhead 可忽略。**\\n\\n## Random Selection Baseline — 双 Benchmark 验证完成 (2026-05-21)\\n\\n代码 `--mode random_selection` 可用。\\n\\n**结论：Random Selection ≈ VLA-only，在 Object 和 Spatial 上一致。多采样本身不产生价值，CRM correction 是唯一改善来源。**\\n\\n| Benchmark | Random K=10 | VLA-only | CRM K=10 | Random vs VLA | Correction Δ |\\n|-----------|-------------|----------|----------|---------------|-------------|\\n| Object | 10.0% (n=8) | 11.0% (n=8) | 16.8% (n=7) | ≈0pp (neutral) | +5.8pp |\\n| Spatial | 29.3% (n=3) | 29.3% (n=4) | 34.5% | 0.0pp (neutral) | +5.2pp |\\n| Object K=5 | 10.5% (n=4) | 11.0% | 16.0% (n=7) | -0.5pp (harmful) | +5.5pp |\\n\\nexp_ids：\\n- Object K=10: eval-random-selection-object-seed{42,43,44,45,46-r3,47,48,49}\\n- Spatial K=10: eval-random-selection-spatial-seed{42-r2,43,44}\\n- Object K=5: eval-random-selection-object-k5-seed{42,43,44,45}-r2\\n\\nC1 核心证据。两个 benchmark 上 pattern 完全一致，可以写 \\\"consistent across benchmarks\\\"。\\n\\n## 全 Benchmark 统计摘要 (v2, 2026-05-20, 含新增数据)\\n\\n### 1. LIBERO-Object — **Strong improvement**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| **CRM norm02 K=10 (主配置)** | **6** | **16.8%±1.8%** | **+6.0pp** | **0.000095** | **\\\\*\\\\*\\\\*** |\\n| CRM norm01 (补充) | 6 | 17.5%±1.0% | +6.6pp | <0.001 | *** |\\n| CRM norm02 K=5 (补充) | 7 | 16.0%±2.2% | +5.1pp | 0.000312 | *** |\\n| Adaptive-K (all) | 12 | 14.2%±1.5% | +3.3pp | 0.000098 | *** |\\n| Argmin K=10 | 5 | 12.4%±2.9% | +1.5pp | 0.317 | n.s. |\\n| **VLA-only** | **8** | **10.9%±1.4%** | — | — | — |\\n\\n### 2. LIBERO-Spatial — **Strong improvement**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only (K=10) | 7 | 34.6%±1.4% | **+5.0pp** | 0.000007 | *** |\\n| **VLA-only** | **9** | **29.6%±1.1%** | — | — | — |\\n\\n### 3. LIBERO-Goal (OOD) — **Neutral**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only | 7 | 67.7%±3.3% | -1.0pp | ~0.7 | n.s. |\\n| **VLA-only** | **6** | **68.7%±3.9%** | — | — | — |\\n\\n### 4. LIBERO-Long (OOD) — **⚠️ Borderline**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only | 7 | 17.0%±2.0% | **+2.2pp** | 0.049 | * |\\n| **VLA-only** | **11** | **14.8%±2.2%** | — | — | — |\\n\\n**⚠️ Long MW-U p=0.061 (n.s.)。t检验 p=0.049 刚好卡在 0.05 边缘。论文需 cautious wording。**\\n\\n### 效果总结\\n\\n| Benchmark | Δ (pp) | p-value | 判定 |\\n|-----------|--------|---------|------|\\n| **Object** | +6.0 | <0.001 | Strong (主配置 norm02) |\\n| **Spatial** | +5.0 | <0.001 | Strong |\\n| **Long** | +2.2 | 0.049 | ⚠️ Borderline (OOD, MW-U n.s.) |\\n| **Goal** | -1.0 | ~0.7 | Neutral (OOD) |\\n\\n**注意**: Argmin K=10 seed43=17% 是未验证离群值（4 台服务器未找到原始 JSON），标注 unverified。\\n\\n## 2026-05-20 新增 eval 结果（诊断中确认）\\n\\n| 实验 | 服务器 | Mode | Benchmark | norm | seed | SR | JSON 时间 |\\n|------|--------|------|-----------|------|------|----|-----------|\\n| eval-perdof-object-norm02-seed50 | bjb1-32546 | crm_perdof | object | 0.2 | 50 | 10.0% | 05-21 03:22 |\\n| eval-obs-only-object-norm02-seed51 | bjb1-32546 | crm_obs_only | object | 0.2 | 51 | 17.0% | 05-21 03:20 |\\n| eval-obs-only-object-norm005-seed44 | bjb1-18228 | crm_obs_only | object | 0.05 | 44 | 12.0% | 05-21 03:16 |\\n| eval-obs-only-object-norm01-seed48 | bjb1-18228 | crm_obs_only | object | 0.1 | 48 | **仍在运行** | — |\\n\\n**norm01-seed48**: PID 507385, 状态 Rl+, 运行 55m55s, GPU1 3408MiB/29%利用率, 已完成 5/10 tasks。预计再需约 1 小时完成。\\n\\n## π0.5 调试历程 (2026-05-21)\\n\\n| 修复轮次 | 修复内容 | SR | 状态 |\\n|---------|---------|-----|------|\\n| r1 | 初始实现 | 0% | 多个预处理 bug |\\n| fix1 | MEAN_STD normalization | 0% | 继续调试 |\\n| fix2 | + SigLIP [-1,1] image | 0% | 继续调试 |\\n| fix3 | + vision tower 437 key remap + padding_side | 0% | key remap 未生效（被 try/except 吞掉） |\\n| fix4 | + action queue (50-step deque) | 0% | action chunk 策略正确但 vision tower 仍是随机权重 |\\n| **官方 lerobot-eval (patched)** | patch `_fix_pytorch_state_dict_keys` | **100% (3/3)** | **模型有效！** |\\n\\n**根因**：vision tower key mismatch (`vision_tower.vision_model.` vs `vision_tower.`) 导致 load_state_dict 失败，被 try/except 静默捕获。模型以随机初始化 vision tower 运行。5 轮修复都在修输入端（normalization/image/padding），从未成功修复权重加载。\\n\", \"total_chars\": 11441, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "ddb4434a-cd4b-4748-9ef3-090036924dae",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\\\", \\\"content\\\": \\\"# Project Memory\\\\n\\\\n## 失败模式记录\\\\n\\\\n- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。\\\\n\\\\n- [失败模式] Cron false positive（2026-05-20）：**eval-adaptive-k-spatial-p50-seed42** 被 cron 误判为 failed（\\\\\\\"process dead 5× with no sentinel/W&B\\\\\\\"）。实际情况：原 PID 675831 被 deploy worker kill 后，重启为 PID 681823。重启后进程正常运行，但 cron 监控未追踪到新 PID，5 次检测均未发现 sentinel → 自动标记 failed。诊断时（2026-05-20）PID 681823 仍在运行（状态 Rl+，已运行 17h36m），已完成 3/10 tasks（SR: 70%/100%/0%），第 4 个 task 进行中（rollout 5, 1/5 success）。GPU 使用 5972/24564 MiB，日志无错误。**无需重新提交，等待自然完成后手动修正 conclusion。**\\\\n\\\\n- [失败模式] SIGHUP false failure（2026-05-20）：bjb2-28827 上多个实验 EXIT_CODE=129 (SIGHUP) 被标记 failed，实际全部完成。**已确认受影响：P75-seed44, P90-seed42, P25-seed44**。SIGHUP 发生在进程写完结果 JSON 之后（tmux session 断开或 SSH 连接清理）。**诊断方法：tail 日志看 \\\\\\\"Results saved to\\\\\\\" + \\\\\\\"Overall success rate\\\\\\\" 行 → 手动修正 conclusion=success 并补录 metrics。**\\\\n\\\\n- [失败模式] Cron 日志路径不匹配（2026-05-20）：**eval-obs-only-goal-norm02-seed51** (bjb1-32546) 被 cron 误判 dead。根因：实验日志写入 `/root/acr-vla-conformal-refinement/logs/`（项目目录下），但 cron 监控在 `~/runs/acr-vla-conformal-refinement/` 下找日志 → 找不到 → 5 次检测均无 sentinel → auto-resolved failed。**教训：submit_training_job 的 log_path 必须与实际 tee 输出路径一致。部分实验用 `tee logs/xxx.log`（相对于 cd 后的项目目录），另一部分用 `~/runs/` 绝对路径，两套路径并存导致 cron 误判。**\\\\n\\\\n- [失败模式] Cron false positive 批量（2026-05-20 诊断）：bjb1-32546 上 **eval-perdof-object-norm02-seed50** (PID 542405) 和 **eval-obs-only-object-norm02-seed51** (PID 542894) 被 cron 报告 \\\\\\\"process gone, no sentinel, no W&B\\\\\\\"。实际两者均已**正常完成**，output JSON 已写入。bjb1-18228 上 **eval-obs-only-object-norm005-seed44** 同样正常完成但被标记 failed。根因同上：eval 脚本不写 sentinel/W&B，进程正常退出后 cron 无法确认完成状态。结果：perdof-norm02-seed50 SR=10.0%, obs_only-norm02-seed51 SR=17.0%, obs_only-norm005-seed44 SR=12.0%。**均无需重跑，需手动修正 conclusion=success 并补录 metrics。**\\\\n\\\\n- [失败模式] python PATH 不存在（2026-05-21, bjb1-32546）：`nohup: failed to run command 'python': No such file or directory`。bjb1-32546 使用 conda 环境，`python` 不在默认 PATH 中（仅 `/root/miniconda3/bin/python` 可用）。受影响：seed51-r2, seed52-r2, seed62, seed63（4 个实验同时失败）。**修复方案：提交命令前加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&` 前缀。** 教训：submit_training_job 的 command 不能假设 `python` 在 PATH 中，必须自带环境激活。对照其他服务器（bjb1-18228、bjb2-28827）成功实验的命令格式，它们通过 `bash -c \\\\\\\"source ... && python ...\\\\\\\"` 包裹。\\\\n\\\\n- [失败模式] FMVD 信号无效：ρ=0.0825 NO-GO。根因：denoising 空间统计量不映射到 action uncertainty。\\\\n\\\\n- [失败模式] CRM correction magnitude 信号无效（2026-05-20）：ρ(K1_corr_mag, K10_var) = 0.1523 NO-GO。**根因：CRM correction magnitude 是常数 (~0.1205)，P25=P50=P75=P90 几乎相同。** CRM 对所有输入产出相同大小的修正向量——修正方向变化但幅度不变。推测因 max_correction_norm=0.2 的 clipping 使得大部分 correction 被截断到相同 norm。K=2 argmin 版本同样无效 (ρ=0.1340)。**教训：clipped norm 的信号没有方差，自然无法做 gate。**\\\\n\\\\n- [失败模式] OpenVLA-7B eval timeout：timeout_hours 至少设 12h。\\\\n\\\\n- [失败模式] Table 1 数据混淆（2026-05-20）：Table 1 原报 CRM Object K=10 = 17.6% (n=7)，实际来自 **norm01+norm02 混合数据**。seed42 只有 norm01 (0.19)，seed43 只有 norm02 (0.16)，两个 config 各自只有 n=6，合并后变 n=7。paper_provenance.yaml C029 引用的 exp_id 是抽象 \\\\\\\"obs_only_k10\\\\\\\" 而非具体实验 ID，导致问题没被及时发现。**教训：provenance 必须引用具体 registry_id，不用抽象标签。**\\\\n\\\\n- [失败模式] evaluate.py 路径缺 src/ 前缀（2026-05-20）：adaptive_k spatial 实验命令用 `python evaluate.py` 而非 `python src/evaluate.py`，导致 EXIT_CODE=2 (No such file)。受影响：eval-adaptive-k-spatial-p50-seed43, eval-adaptive-k-spatial-p50-seed44（两台服务器 bjb1-32546, bjb2-28827 同时中招）。**教训：提交命令时对照历史成功实验的 command 格式，evaluate.py 在 src/ 子目录下。**\\\\n\\\\n- [失败模式] π0.5 vision tower 权重静默加载失败（2026-05-21）：**5 轮修复全部 0% SR 的真正根因**。checkpoint key 为 `vision_tower.vision_model.encoder.layers.X`，但 transformers 5.8.0 的 SiglipVisionModel 期望 `vision_tower.encoder.layers.X`（无 `vision_model` 中间层）。lerobot 0.5.2 的 `_fix_pytorch_state_dict_keys` 缺少此映射，`load_state_dict(strict=True)` 失败被 try/except 静默捕获，模型以**随机初始化 vision tower 运行** → 0% SR。**官方 lerobot-eval 也有此 bug。** Worker patch lerobot 内部代码后 3/3 = 100% SR。**教训：(1) load_state_dict 的 try/except 必须打印 missing_keys/unexpected_keys，不能静默吞掉 (2) 加载后验证关键层权重统计（mean/std）确认非随机 (3) 0% SR 时优先检查权重加载而非输入预处理。**\\\\n\\\\n## seed66 失败诊断 (2026-05-21)\\\\n- 根因：**Cron false positive（第 N 次）**。3 个 seed66 进程（norm003/norm005/norm01）实际仍在 bjb1-18228 上正常运行，被 cron 误判为 \\\\\\\"process dead 5× with no sentinel/W&B\\\\\\\"。\\\\n- 证据：\\\\n  - PID 642428 (norm003, GPU0), PID 642506 (norm005, GPU2), PID 642775 (norm01, GPU3) 均处于 Rl 状态，CPU 使用 ~400%，GPU 利用率 34-38%，VRAM ~5.7GB/卡\\\\n  - 日志在两次读取之间从 rollout 5/20 增长到 10/20，确认进程在推进\\\\n  - sentinels/ 目录完全为空——从未有实验写过 sentinel file\\\\n  - 无 OOM、无 CUDA error、无 traceback、无 segfault\\\\n  - 磁盘空间充足（根分区 53%，数据盘未挂载 autodl-tmp 但进程正常读写）\\\\n- 与 seed65 对比：seed65 (PID 622484, GPU1) 用 `nohup python -u` 启动，日志持续更新；seed66 用 `python3` 启动（无 `-u` 无 nohup），日志因 stdout 缓冲更新延迟，但进程本身正常\\\\n- 影响范围：eval-obs-only-object-norm005-seed66, eval-obs-only-object-norm01-seed66, eval-obs-only-object-norm003-seed66（3 个实验）\\\\n- 建议修复：**无需重跑**。等待进程自然完成（n_rollouts=20，当前约 50% 进度，预计再需 1-2 小时），完成后手动修正 conclusion=success 并从 output JSON 补录 metrics。\\\\n\\\\n## CRM Coverage 限制\\\\n\\\\nCRM v3 训练数据 = Object(10) + Spatial(10) = 20 tasks。Goal/Long 是 OOD 泛化测试。\\\\n\\\\n## Adaptive K 信号探索\\\\n\\\\n| 信号 | ρ vs K10_var | 结论 | 备注 |\\\\n|------|-------------|------|------|\\\\n| FMVD (velocity dispersion) | 0.0825 | ❌ NO-GO | zero-cost 但无效 |\\\\n| **K=2 L2 divergence** | **0.9979** | **✅ GO** | 需要 K=2 采样（+170ms），near-perfect proxy |\\\\n| CRM correction magnitude (K=1) | 0.1523 | ❌ NO-GO | zero-cost 但 magnitude 是常数 |\\\\n| CRM correction magnitude (K=2 argmin) | 0.1340 | ❌ NO-GO | 同上 |\\\\n\\\\n**结论：K=2 L2 distance 是唯一可用的 adaptive K 门控信号。** FMVD 和 CRM magnitude 均因信号方差不足而失败。\\\\n\\\\n## Adaptive K Sweep 最终结果 — Object (2026-05-20, 12/12 完成)\\\\n\\\\n| 阈值 | SR [seeds] | avg_K | fast_path% |\\\\n|------|-----------|-------|-----------|\\\\n| P90 (τ=0.127) | 13.3% [12,14,14] | ~2.6 | ~93% |\\\\n| P75 (τ=0.099) | 13.7% [12,13,16] | ~3.1 | ~87% |\\\\n| **P50 (τ=0.075)** | **15.3% [16,16,14]** | **~3.8** | **~77%** |\\\\n| P25 (τ=0.055) | 14.3% [15,13,15] | ~4.8 | ~65% |\\\\n\\\\n**P50 = Pareto optimal**: 最高 SR + 比 K=10 省 62% compute (avg_K 3.8 vs 10)。\\\\n\\\\n## Adaptive K Cross-Benchmark Sweep — Spatial (2026-05-20, 11/12 done)\\\\n\\\\nObject 校准阈值直接迁移到 Spatial（无 per-benchmark tuning）：\\\\n\\\\n| 阈值 | seed42 | seed43 | seed44 | Mean±Std | avg_K | fast_path |\\\\n|------|--------|--------|--------|----------|-------|-----------|\\\\n| P90 | 31% | 32% | PREPARING | — | ~3.5 | ~80% |\\\\n| P75 | 31% | 34% | 33% | 32.7%±1.5% | ~5.0 | ~62% |\\\\n| P50 | 30% | 33% | 33% | 32.0%±1.7% | ~6.35 | ~46% |\\\\n| P25 | 33% | 30% | 32% | 31.7%±1.5% | ~7.65 | ~29% |\\\\n\\\\nvs VLA-only Spatial: 29.6%±1.1% | vs CRM K=10 Spatial: 34.6%±1.4%\\\\n\\\\n**关键洞察**：\\\\n1. 所有阈值 SR 差异很小（31.7-32.7%），但 compute 差异 2x（avg_K 3.5→7.65）。P75 在 Spatial 上 Pareto 最优（32.7% + avg_K 5.0），P50 在 Object 上最优。\\\\n2. Spatial fast_path 远低于 Object（同阈值下 29% vs 65% for P25）—— Spatial L2 均值更高，方法自动分配更多 full-K steps。\\\\n3. 这支持\\\\\\\"阈值自动适配任务复杂度\\\\\\\"的核心 narrative：同一 Object 校准阈值，在更难的 Spatial 上自动降低 fast_path 比例以保持 SR。\\\\n\\\\n## Latency Profiling (dry-run N=20, RTX 4090, 2026-05-20)\\\\n\\\\n| Component | Mean (ms) | 备注 |\\\\n|-----------|----------|------|\\\\n| VLA sampling | 206 | **K 无关**（batched generation） |\\\\n| CRM MLP forward | 0.33 | 337K params |\\\\n| Argmin L2 + CRM 总开销 | 4.0 | 管线 1.6% |\\\\n| Full pipeline K=10 | 259 | ~3.9 Hz |\\\\n| **Adaptive K 快路径** | **254** | K=2 only |\\\\n| **Adaptive K 全路径** | **459** | K=2→K=10 |\\\\n\\\\n**关键发现：VLA batched sampling 消除 K 作为 latency 因子。Adaptive K 快路径省 45% latency。CRM overhead 可忽略。**\\\\n\\\\n## Random Selection Baseline — 双 Benchmark 验证完成 (2026-05-21)\\\\n\\\\n代码 `--mode random_selection` 可用。\\\\n\\\\n**结论：Random Selection ≈ VLA-only，在 Object 和 Spatial 上一致。多采样本身不产生价值，CRM correction 是唯一改善来源。**\\\\n\\\\n| Benchmark | Random K=10 | VLA-only | CRM K=10 | Random vs VLA | Correction Δ |\\\\n|-----------|-------------|----------|----------|---------------|-------------|\\\\n| Object | 10.0% (n=8) | 11.0% (n=8) | 16.8% (n=7) | ≈0pp (neutral) | +5.8pp |\\\\n| Spatial | 29.3% (n=3) | 29.3% (n=4) | 34.5% | 0.0pp (neutral) | +5.2pp |\\\\n| Object K=5 | 10.5% (n=4) | 11.0% | 16.0% (n=7) | -0.5pp (harmful) | +5.5pp |\\\\n\\\\nexp_ids：\\\\n- Object K=10: eval-random-selection-object-seed{42,43,44,45,46-r3,47,48,49}\\\\n- Spatial K=10: eval-random-selection-spatial-seed{42-r2,43,44}\\\\n- Object K=5: eval-random-selection-object-k5-seed{42,43,44,45}-r2\\\\n\\\\nC1 核心证据。两个 benchmark 上 pattern 完全一致，可以写 \\\\\\\"consistent across benchmarks\\\\\\\"。\\\\n\\\\n## 全 Benchmark 统计摘要 (v2, 2026-05-20, 含新增数据)\\\\n\\\\n### 1. LIBERO-Object — **Strong improvement**\\\\n\\\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\\\n|--------|---|----------|----------|-----------|-----|\\\\n| **CRM norm02 K=10 (主配置)** | **6** | **16.8%±1.8%** | **+6.0pp** | **0.000095** | **\\\\\\\\*\\\\\\\\*\\\\\\\\*** |\\\\n| CRM norm01 (补充) | 6 | 17.5%±1.0% | +6.6pp | <0.001 | *** |\\\\n| CRM norm02 K=5 (补充) | 7 | 16.0%±2.2% | +5.1pp | 0.000312 | *** |\\\\n| Adaptive-K (all) | 12 | 14.2%±1.5% | +3.3pp | 0.000098 | *** |\\\\n| Argmin K=10 | 5 | 12.4%±2.9% | +1.5pp | 0.317 | n.s. |\\\\n| **VLA-only** | **8** | **10.9%±1.4%** | — | — | — |\\\\n\\\\n### 2. LIBERO-Spatial — **Strong improvement**\\\\n\\\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\\\n|--------|---|----------|----------|-----------|-----|\\\\n| CRM obs_only (K=10) | 7 | 34.6%±1.4% | **+5.0pp** | 0.000007 | *** |\\\\n| **VLA-only** | **9** | **29.6%±1.1%** | — | — | — |\\\\n\\\\n### 3. LIBERO-Goal (OOD) — **Neutral**\\\\n\\\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\\\n|--------|---|----------|----------|-----------|-----|\\\\n| CRM obs_only | 7 | 67.7%±3.3% | -1.0pp | ~0.7 | n.s. |\\\\n| **VLA-only** | **6** | **68.7%±3.9%** | — | — | — |\\\\n\\\\n### 4. LIBERO-Long (OOD) — **⚠️ Borderline**\\\\n\\\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\\\n|--------|---|----------|----------|-----------|-----|\\\\n| CRM obs_only | 7 | 17.0%±2.0% | **+2.2pp** | 0.049 | * |\\\\n| **VLA-only** | **11** | **14.8%±2.2%** | — | — | — |\\\\n\\\\n**⚠️ Long MW-U p=0.061 (n.s.)。t检验 p=0.049 刚好卡在 0.05 边缘。论文需 cautious wording。**\\\\n\\\\n### 效果总结\\\\n\\\\n| Benchmark | Δ (pp) | p-value | 判定 |\\\\n|-----------|--------|---------|------|\\\\n| **Object** | +6.0 | <0.001 | Strong (主配置 norm02) |\\\\n| **Spatial** | +5.0 | <0.001 | Strong |\\\\n| **Long** | +2.2 | 0.049 | ⚠️ Borderline (OOD, MW-U n.s.) |\\\\n| **Goal** | -1.0 | ~0.7 | Neutral (OOD) |\\\\n\\\\n**注意**: Argmin K=10 seed43=17% 是未验证离群值（4 台服务器未找到原始 JSON），标注 unverified。\\\\n\\\\n## 2026-05-20 新增 eval 结果（诊断中确认）\\\\n\\\\n| 实验 | 服务器 | Mode | Benchmark | norm | seed | SR | JSON 时间 |\\\\n|------|--------|------|-----------|------|------|----|-----------|\\\\n| eval-perdof-object-norm02-seed50 | bjb1-32546 | crm_perdof | object | 0.2 | 50 | 10.0% | 05-21 03:22 |\\\\n| eval-obs-only-object-norm02-seed51 | bjb1-32546 | crm_obs_only | object | 0.2 | 51 | 17.0% | 05-21 03:20 |\\\\n| eval-obs-only-object-norm005-seed44 | bjb1-18228 | crm_obs_only | object | 0.05 | 44 | 12.0% | 05-21 03:16 |\\\\n| eval-obs-only-object-norm01-seed48 | bjb1-18228 | crm_obs_only | object | 0.1 | 48 | **仍在运行** | — |\\\\n\\\\n**norm01-seed48**: PID 507385, 状态 Rl+, 运行 55m55s, GPU1 3408MiB/29%利用率, 已完成 5/10 tasks。预计再需约 1 小时完成。\\\\n\\\\n## π0.5 调试历程 (2026-05-21)\\\\n\\\\n| 修复轮次 | 修复内容 | SR | 状态 |\\\\n|---------|---------|-----|------|\\\\n| r1 | 初始实现 | 0% | 多个预处理 bug |\\\\n| fix1 | MEAN_STD normalization | 0% | 继续调试 |\\\\n| fix2 | + SigLIP [-1,1] image | 0% | 继续调试 |\\\\n| fix3 | + vision tower 437 key remap + padding_side | 0% | key remap 未生效（被 try/except 吞掉） |\\\\n| fix4 | + action queue (50-step deque) | 0% | action chunk 策略正确但 vision tower 仍是随机权重 |\\\\n| **官方 lerobot-eval (patched)** | patch `_fix_pytorch_state_dict_keys` | **100% (3/3)** | **模型有效！** |\\\\n\\\\n**根因**：vision tower key mismatch (`vision_tower.vision_model.` vs `vision_tower.`) 导致 load_state_dict 失败，被 try/except 静默捕获。模型以随机初始化 vision tower 运行。5 轮修复都在修输入端（normalization/image/padding），从未成功修复权重加载。\\\\n\\\", \\\"total_chars\\\": 11441, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Project Memory\\n\\n## 失败模式记录\\n\\n- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。\\n\\n- [失败模式] Cron false positive（2026-05-20）：**eval-adaptive-k-spatial-p50-seed42** 被 cron 误判为 failed（\\\"process dead 5× with no sentinel/W&B\\\"）。实际情况：原 PID 675831 被 deploy worker kill 后，重启为 PID 681823。重启后进程正常运行，但 cron 监控未追踪到新 PID，5 次检测均未发现 sentinel → 自动标记 failed。诊断时（2026-05-20）PID 681823 仍在运行（状态 Rl+，已运行 17h36m），已完成 3/10 tasks（SR: 70%/100%/0%），第 4 个 task 进行中（rollout 5, 1/5 success）。GPU 使用 5972/24564 MiB，日志无错误。**无需重新提交，等待自然完成后手动修正 conclusion。**\\n\\n- [失败模式] SIGHUP false failure（2026-05-20）：bjb2-28827 上多个实验 EXIT_CODE=129 (SIGHUP) 被标记 failed，实际全部完成。**已确认受影响：P75-seed44, P90-seed42, P25-seed44**。SIGHUP 发生在进程写完结果 JSON 之后（tmux session 断开或 SSH 连接清理）。**诊断方法：tail 日志看 \\\"Results saved to\\\" + \\\"Overall success rate\\\" 行 → 手动修正 conclusion=success 并补录 metrics。**\\n\\n- [失败模式] Cron 日志路径不匹配（2026-05-20）：**eval-obs-only-goal-norm02-seed51** (bjb1-32546) 被 cron 误判 dead。根因：实验日志写入 `/root/acr-vla-conformal-refinement/logs/`（项目目录下），但 cron 监控在 `~/runs/acr-vla-conformal-refinement/` 下找日志 → 找不到 → 5 次检测均无 sentinel → auto-resolved failed。**教训：submit_training_job 的 log_path 必须与实际 tee 输出路径一致。部分实验用 `tee logs/xxx.log`（相对于 cd 后的项目目录），另一部分用 `~/runs/` 绝对路径，两套路径并存导致 cron 误判。**\\n\\n- [失败模式] Cron false positive 批量（2026-05-20 诊断）：bjb1-32546 上 **eval-perdof-object-norm02-seed50** (PID 542405) 和 **eval-obs-only-object-norm02-seed51** (PID 542894) 被 cron 报告 \\\"process gone, no sentinel, no W&B\\\"。实际两者均已**正常完成**，output JSON 已写入。bjb1-18228 上 **eval-obs-only-object-norm005-seed44** 同样正常完成但被标记 failed。根因同上：eval 脚本不写 sentinel/W&B，进程正常退出后 cron 无法确认完成状态。结果：perdof-norm02-seed50 SR=10.0%, obs_only-norm02-seed51 SR=17.0%, obs_only-norm005-seed44 SR=12.0%。**均无需重跑，需手动修正 conclusion=success 并补录 metrics。**\\n\\n- [失败模式] python PATH 不存在（2026-05-21, bjb1-32546）：`nohup: failed to run command 'python': No such file or directory`。bjb1-32546 使用 conda 环境，`python` 不在默认 PATH 中（仅 `/root/miniconda3/bin/python` 可用）。受影响：seed51-r2, seed52-r2, seed62, seed63（4 个实验同时失败）。**修复方案：提交命令前加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&` 前缀。** 教训：submit_training_job 的 command 不能假设 `python` 在 PATH 中，必须自带环境激活。对照其他服务器（bjb1-18228、bjb2-28827）成功实验的命令格式，它们通过 `bash -c \\\"source ... && python ...\\\"` 包裹。\\n\\n- [失败模式] FMVD 信号无效：ρ=0.0825 NO-GO。根因：denoising 空间统计量不映射到 action uncertainty。\\n\\n- [失败模式] CRM correction magnitude 信号无效（2026-05-20）：ρ(K1_corr_mag, K10_var) = 0.1523 NO-GO。**根因：CRM correction magnitude 是常数 (~0.1205)，P25=P50=P75=P90 几乎相同。** CRM 对所有输入产出相同大小的修正向量——修正方向变化但幅度不变。推测因 max_correction_norm=0.2 的 clipping 使得大部分 correction 被截断到相同 norm。K=2 argmin 版本同样无效 (ρ=0.1340)。**教训：clipped norm 的信号没有方差，自然无法做 gate。**\\n\\n- [失败模式] OpenVLA-7B eval timeout：timeout_hours 至少设 12h。\\n\\n- [失败模式] Table 1 数据混淆（2026-05-20）：Table 1 原报 CRM Object K=10 = 17.6% (n=7)，实际来自 **norm01+norm02 混合数据**。seed42 只有 norm01 (0.19)，seed43 只有 norm02 (0.16)，两个 config 各自只有 n=6，合并后变 n=7。paper_provenance.yaml C029 引用的 exp_id 是抽象 \\\"obs_only_k10\\\" 而非具体实验 ID，导致问题没被及时发现。**教训：provenance 必须引用具体 registry_id，不用抽象标签。**\\n\\n- [失败模式] evaluate.py 路径缺 src/ 前缀（2026-05-20）：adaptive_k spatial 实验命令用 `python evaluate.py` 而非 `python src/evaluate.py`，导致 EXIT_CODE=2 (No such file)。受影响：eval-adaptive-k-spatial-p50-seed43, eval-adaptive-k-spatial-p50-seed44（两台服务器 bjb1-32546, bjb2-28827 同时中招）。**教训：提交命令时对照历史成功实验的 command 格式，evaluate.py 在 src/ 子目录下。**\\n\\n- [失败模式] π0.5 vision tower 权重静默加载失败（2026-05-21）：**5 轮修复全部 0% SR 的真正根因**。checkpoint key 为 `vision_tower.vision_model.encoder.layers.X`，但 transformers 5.8.0 的 SiglipVisionModel 期望 `vision_tower.encoder.layers.X`（无 `vision_model` 中间层）。lerobot 0.5.2 的 `_fix_pytorch_state_dict_keys` 缺少此映射，`load_state_dict(strict=True)` 失败被 try/except 静默捕获，模型以**随机初始化 vision tower 运行** → 0% SR。**官方 lerobot-eval 也有此 bug。** Worker patch lerobot 内部代码后 3/3 = 100% SR。**教训：(1) load_state_dict 的 try/except 必须打印 missing_keys/unexpected_keys，不能静默吞掉 (2) 加载后验证关键层权重统计（mean/std）确认非随机 (3) 0% SR 时优先检查权重加载而非输入预处理。**\\n\\n## seed66 失败诊断 (2026-05-21)\\n- 根因：**Cron false positive（第 N 次）**。3 个 seed66 进程（norm003/norm005/norm01）实际仍在 bjb1-18228 上正常运行，被 cron 误判为 \\\"process dead 5× with no sentinel/W&B\\\"。\\n- 证据：\\n  - PID 642428 (norm003, GPU0), PID 642506 (norm005, GPU2), PID 642775 (norm01, GPU3) 均处于 Rl 状态，CPU 使用 ~400%，GPU 利用率 34-38%，VRAM ~5.7GB/卡\\n  - 日志在两次读取之间从 rollout 5/20 增长到 10/20，确认进程在推进\\n  - sentinels/ 目录完全为空——从未有实验写过 sentinel file\\n  - 无 OOM、无 CUDA error、无 traceback、无 segfault\\n  - 磁盘空间充足（根分区 53%，数据盘未挂载 autodl-tmp 但进程正常读写）\\n- 与 seed65 对比：seed65 (PID 622484, GPU1) 用 `nohup python -u` 启动，日志持续更新；seed66 用 `python3` 启动（无 `-u` 无 nohup），日志因 stdout 缓冲更新延迟，但进程本身正常\\n- 影响范围：eval-obs-only-object-norm005-seed66, eval-obs-only-object-norm01-seed66, eval-obs-only-object-norm003-seed66（3 个实验）\\n- 建议修复：**无需重跑**。等待进程自然完成（n_rollouts=20，当前约 50% 进度，预计再需 1-2 小时），完成后手动修正 conclusion=success 并从 output JSON 补录 metrics。\\n\\n## CRM Coverage 限制\\n\\nCRM v3 训练数据 = Object(10) + Spatial(10) = 20 tasks。Goal/Long 是 OOD 泛化测试。\\n\\n## Adaptive K 信号探索\\n\\n| 信号 | ρ vs K10_var | 结论 | 备注 |\\n|------|-------------|------|------|\\n| FMVD (velocity dispersion) | 0.0825 | ❌ NO-GO | zero-cost 但无效 |\\n| **K=2 L2 divergence** | **0.9979** | **✅ GO** | 需要 K=2 采样（+170ms），near-perfect proxy |\\n| CRM correction magnitude (K=1) | 0.1523 | ❌ NO-GO | zero-cost 但 magnitude 是常数 |\\n| CRM correction magnitude (K=2 argmin) | 0.1340 | ❌ NO-GO | 同上 |\\n\\n**结论：K=2 L2 distance 是唯一可用的 adaptive K 门控信号。** FMVD 和 CRM magnitude 均因信号方差不足而失败。\\n\\n## Adaptive K Sweep 最终结果 — Object (2026-05-20, 12/12 完成)\\n\\n| 阈值 | SR [seeds] | avg_K | fast_path% |\\n|------|-----------|-------|-----------|\\n| P90 (τ=0.127) | 13.3% [12,14,14] | ~2.6 | ~93% |\\n| P75 (τ=0.099) | 13.7% [12,13,16] | ~3.1 | ~87% |\\n| **P50 (τ=0.075)** | **15.3% [16,16,14]** | **~3.8** | **~77%** |\\n| P25 (τ=0.055) | 14.3% [15,13,15] | ~4.8 | ~65% |\\n\\n**P50 = Pareto optimal**: 最高 SR + 比 K=10 省 62% compute (avg_K 3.8 vs 10)。\\n\\n## Adaptive K Cross-Benchmark Sweep — Spatial (2026-05-20, 11/12 done)\\n\\nObject 校准阈值直接迁移到 Spatial（无 per-benchmark tuning）：\\n\\n| 阈值 | seed42 | seed43 | seed44 | Mean±Std | avg_K | fast_path |\\n|------|--------|--------|--------|----------|-------|-----------|\\n| P90 | 31% | 32% | PREPARING | — | ~3.5 | ~80% |\\n| P75 | 31% | 34% | 33% | 32.7%±1.5% | ~5.0 | ~62% |\\n| P50 | 30% | 33% | 33% | 32.0%±1.7% | ~6.35 | ~46% |\\n| P25 | 33% | 30% | 32% | 31.7%±1.5% | ~7.65 | ~29% |\\n\\nvs VLA-only Spatial: 29.6%±1.1% | vs CRM K=10 Spatial: 34.6%±1.4%\\n\\n**关键洞察**：\\n1. 所有阈值 SR 差异很小（31.7-32.7%），但 compute 差异 2x（avg_K 3.5→7.65）。P75 在 Spatial 上 Pareto 最优（32.7% + avg_K 5.0），P50 在 Object 上最优。\\n2. Spatial fast_path 远低于 Object（同阈值下 29% vs 65% for P25）—— Spatial L2 均值更高，方法自动分配更多 full-K steps。\\n3. 这支持\\\"阈值自动适配任务复杂度\\\"的核心 narrative：同一 Object 校准阈值，在更难的 Spatial 上自动降低 fast_path 比例以保持 SR。\\n\\n## Latency Profiling (dry-run N=20, RTX 4090, 2026-05-20)\\n\\n| Component | Mean (ms) | 备注 |\\n|-----------|----------|------|\\n| VLA sampling | 206 | **K 无关**（batched generation） |\\n| CRM MLP forward | 0.33 | 337K params |\\n| Argmin L2 + CRM 总开销 | 4.0 | 管线 1.6% |\\n| Full pipeline K=10 | 259 | ~3.9 Hz |\\n| **Adaptive K 快路径** | **254** | K=2 only |\\n| **Adaptive K 全路径** | **459** | K=2→K=10 |\\n\\n**关键发现：VLA batched sampling 消除 K 作为 latency 因子。Adaptive K 快路径省 45% latency。CRM overhead 可忽略。**\\n\\n## Random Selection Baseline — 双 Benchmark 验证完成 (2026-05-21)\\n\\n代码 `--mode random_selection` 可用。\\n\\n**结论：Random Selection ≈ VLA-only，在 Object 和 Spatial 上一致。多采样本身不产生价值，CRM correction 是唯一改善来源。**\\n\\n| Benchmark | Random K=10 | VLA-only | CRM K=10 | Random vs VLA | Correction Δ |\\n|-----------|-------------|----------|----------|---------------|-------------|\\n| Object | 10.0% (n=8) | 11.0% (n=8) | 16.8% (n=7) | ≈0pp (neutral) | +5.8pp |\\n| Spatial | 29.3% (n=3) | 29.3% (n=4) | 34.5% | 0.0pp (neutral) | +5.2pp |\\n| Object K=5 | 10.5% (n=4) | 11.0% | 16.0% (n=7) | -0.5pp (harmful) | +5.5pp |\\n\\nexp_ids：\\n- Object K=10: eval-random-selection-object-seed{42,43,44,45,46-r3,47,48,49}\\n- Spatial K=10: eval-random-selection-spatial-seed{42-r2,43,44}\\n- Object K=5: eval-random-selection-object-k5-seed{42,43,44,45}-r2\\n\\nC1 核心证据。两个 benchmark 上 pattern 完全一致，可以写 \\\"consistent across benchmarks\\\"。\\n\\n## 全 Benchmark 统计摘要 (v2, 2026-05-20, 含新增数据)\\n\\n### 1. LIBERO-Object — **Strong improvement**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| **CRM norm02 K=10 (主配置)** | **6** | **16.8%±1.8%** | **+6.0pp** | **0.000095** | **\\\\*\\\\*\\\\*** |\\n| CRM norm01 (补充) | 6 | 17.5%±1.0% | +6.6pp | <0.001 | *** |\\n| CRM norm02 K=5 (补充) | 7 | 16.0%±2.2% | +5.1pp | 0.000312 | *** |\\n| Adaptive-K (all) | 12 | 14.2%±1.5% | +3.3pp | 0.000098 | *** |\\n| Argmin K=10 | 5 | 12.4%±2.9% | +1.5pp | 0.317 | n.s. |\\n| **VLA-only** | **8** | **10.9%±1.4%** | — | — | — |\\n\\n### 2. LIBERO-Spatial — **Strong improvement**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only (K=10) | 7 | 34.6%±1.4% | **+5.0pp** | 0.000007 | *** |\\n| **VLA-only** | **9** | **29.6%±1.1%** | — | — | — |\\n\\n### 3. LIBERO-Goal (OOD) — **Neutral**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only | 7 | 67.7%±3.3% | -1.0pp | ~0.7 | n.s. |\\n| **VLA-only** | **6** | **68.7%±3.9%** | — | — | — |\\n\\n### 4. LIBERO-Long (OOD) — **⚠️ Borderline**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only | 7 | 17.0%±2.0% | **+2.2pp** | 0.049 | * |\\n| **VLA-only** | **11** | **14.8%±2.2%** | — | — | — |\\n\\n**⚠️ Long MW-U p=0.061 (n.s.)。t检验 p=0.049 刚好卡在 0.05 边缘。论文需 cautious wording。**\\n\\n### 效果总结\\n\\n| Benchmark | Δ (pp) | p-value | 判定 |\\n|-----------|--------|---------|------|\\n| **Object** | +6.0 | <0.001 | Strong (主配置 norm02) |\\n| **Spatial** | +5.0 | <0.001 | Strong |\\n| **Long** | +2.2 | 0.049 | ⚠️ Borderline (OOD, MW-U n.s.) |\\n| **Goal** | -1.0 | ~0.7 | Neutral (OOD) |\\n\\n**注意**: Argmin K=10 seed43=17% 是未验证离群值（4 台服务器未找到原始 JSON），标注 unverified。\\n\\n## 2026-05-20 新增 eval 结果（诊断中确认）\\n\\n| 实验 | 服务器 | Mode | Benchmark | norm | seed | SR | JSON 时间 |\\n|------|--------|------|-----------|------|------|----|-----------|\\n| eval-perdof-object-norm02-seed50 | bjb1-32546 | crm_perdof | object | 0.2 | 50 | 10.0% | 05-21 03:22 |\\n| eval-obs-only-object-norm02-seed51 | bjb1-32546 | crm_obs_only | object | 0.2 | 51 | 17.0% | 05-21 03:20 |\\n| eval-obs-only-object-norm005-seed44 | bjb1-18228 | crm_obs_only | object | 0.05 | 44 | 12.0% | 05-21 03:16 |\\n| eval-obs-only-object-norm01-seed48 | bjb1-18228 | crm_obs_only | object | 0.1 | 48 | **仍在运行** | — |\\n\\n**norm01-seed48**: PID 507385, 状态 Rl+, 运行 55m55s, GPU1 3408MiB/29%利用率, 已完成 5/10 tasks。预计再需约 1 小时完成。\\n\\n## π0.5 调试历程 (2026-05-21)\\n\\n| 修复轮次 | 修复内容 | SR | 状态 |\\n|---------|---------|-----|------|\\n| r1 | 初始实现 | 0% | 多个预处理 bug |\\n| fix1 | MEAN_STD normalization | 0% | 继续调试 |\\n| fix2 | + SigLIP [-1,1] image | 0% | 继续调试 |\\n| fix3 | + vision tower 437 key remap + padding_side | 0% | key remap 未生效（被 try/except 吞掉） |\\n| fix4 | + action queue (50-step deque) | 0% | action chunk 策略正确但 vision tower 仍是随机权重 |\\n| **官方 lerobot-eval (patched)** | patch `_fix_pytorch_state_dict_keys` | **100% (3/3)** | **模型有效！** |\\n\\n**根因**：vision tower key mismatch (`vision_tower.vision_model.` vs `vision_tower.`) 导致 load_state_dict 失败，被 try/except 静默捕获。模型以随机初始化 vision tower 运行。5 轮修复都在修输入端（normalization/image/padding），从未成功修复权重加载。\\n\", \"total_chars\": 11441, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "0adcb2eb-2581-4264-af92-e9311e2308b6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AdvLMx1ZoiwUpgaMFxPyfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17758,
      "cache_read_input_tokens": 32197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17758
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Y2hG8MDauwP2FnGCuA3AA4`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "a8e5c909-4aef-47b6-bdde-9f8b8e628432",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AdvLMx1ZoiwUpgaMFxPyfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17758,
      "cache_read_input_tokens": 32197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17758
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

_source line 16 · 2026-05-21T11:38:49.086Z_

<details><summary>↩ Tool result · `toolu_01Y2hG8MDauwP2FnGCuA3AA4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\n\\n## Target Venue\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\n- Title: \\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\"\\n\\n## Core Insight (D065 revised)\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\n\\n## Headline Metrics\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\n\\n## Core Claims (3 claims, D061)\\n\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\n\\n### C2: Conditioning-magnitude interaction — first systematic study\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\n\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\"recognizes\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\n\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\n\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\n\\n**信号验证结果 (D076)**:\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\n\\n**确定的架构**:\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\"困难步\\\"）\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\"简单步\\\"）\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\n\\n**Phase 2 结果 (Object)**:\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\n- Spatial 跨 benchmark 验证完成\\n\\n**对论文 framing 的影响**:\\n- 从纯 analysis paper 升级为 analysis + method paper\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\n- K=10 固定推理保留为 oracle upper bound\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\n\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\n\\n**D088 Learned Uncertainty Head — NO-GO**:\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\n\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\n\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\n\\n**对论文影响 (D091)**:\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\n\\n## Story Spine\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVLA: UQ; SC-VLA: residual RL) address adjacent problems.\\n- **Our angle**: We first dissect inference-time multi-sample correction, finding that learned correction is the active mechanism while multi-sampling is an enabling condition. These findings inform the design of an **adaptive K mechanism** that dynamically allocates compute — sampling more only when the VLA is uncertain. The conditioning-magnitude interaction and applicability boundaries further constrain safe deployment.\\n- **Headline**: \\\"Adaptive inference-time correction improves frozen VLA with avg_K << K_max. Analysis: correction is the active mechanism, not selection. Conditioning-magnitude interaction determines success vs catastrophic failure. Adaptive K achieves ~91% of fixed K=10 performance at 38% average compute (avg_K=3.8 vs K=10).\\\"\\n\\n## Competitive Landscape\\n\\n### A2C2 (D060) — Complementary, not competing\\nFrozen VLA + per-step correction within action chunks. Solves **temporal staleness** (chunk actions become outdated during execution). Our method solves **initial action quality** (improve the action before execution). Orthogonal and combinable. A2C2 trains SmolVLA from scratch (67-72% baseline) — different setting from our frozen pretrained VLA (10.8%).\\n\\n### ReconVLA — Same domain, different route\\nConformal quantile regression for UQ + OOD detection on frozen VLA. Does not perform learned correction.\\n\\n### SC-VLA / PLD — RL-based refinement\\nResidual RL per-task. Requires online training, not plug-and-play. PLD achieves 99% on LIBERO but with full fine-tuning.\\n\\n### Our positioning (D058/D061, updated D072)\\nFirst to (1) decompose inference-time VLA correction into selection vs correction contributions, (2) systematically study conditioning-magnitude interaction revealing catastrophic failure mode, (3) establish applicability boundaries across VLA architectures (stochastic vs deterministic), **(4) propose adaptive inference-time compute allocation based on per-step uncertainty — dynamically deciding K rather than fixed brute-force sampling**. The adaptive K mechanism connects to LLM inference-time compute scaling trends in embodied AI.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Absolute performance is low (16.8% on an 11% baseline)\\\"**\\n   - Response: This is frozen fine-tuned VLA with inference-time correction (VLA weights fixed during CRM training and deployment). ~53% relative improvement (+5.8pp) is significant given the frozen constraint. The contribution is the systematic analysis of when/why/how inference-time correction works, not SOTA absolute numbers. Community benchmark: A2C2 trains SmolVLA from scratch on LIBERO reaching 67-72%, a different training regime.\\n\\n2. **\\\"Method only works for weak/small VLAs\\\"**\\n   - Response: Honest analysis (C3). Correction value correlates inversely with base model quality/determinism. This is a genuine insight with practical implications: small stochastic VLAs are relevant for edge deployment, latency-constrained scenarios, and new task generalization without fine-tuning.\\n\\n3. **\\\"K=1 doesn't work, K=10 needs 10× compute\\\"**\\n   - Response: **Adaptive K (D076) directly addresses this.** Default K=2 (same latency as K=1 with batching ~170ms). K=2 pairwise L2 distance as uncertainty signal (ρ=0.9979 vs K=10 variance). High uncertainty → extend to K=10 + CRM; low uncertainty → use K=2 directly. avg_K=3.8, achieving ~91% of fixed K=10 performance (15.3% vs 16.8%). K=1 CRM failure (10.3%) is a finding: correction needs multi-sample centering. FMVD failure (ρ=0.08) is ablation evidence for why action-space signals work while ODE-space signals don't.\\n\\n4. **\\\"obs_only is just a residual MLP, where is the novelty?\\\"**\\n   - Response: Novelty is the systematic analysis, not the architecture. Architecture simplicity isolates the conditioning signal's effect. The conditioning-magnitude interaction and component decomposition are new.\\n\\n5. **\\\"Single benchmark (LIBERO-Object)\\\"**\\n   - Response: **Fully addressed with LIBERO-Spatial data.** CRM K=10 Spatial: 35.0%±1.0% (n=3) vs VLA-only 29.3%±1.7% (n=4). Paired Δ=+5.7pp (n=3), matching Object's +6pp. K=5 Spatial: 33.5% (n=2). Both Object and Spatial are in-distribution (CRM trained on all 20 tasks). LTO (D069) shows OOD limitation — honest boundary. OpenVLA v2=69% baseline (D087), CRM eval pending.\\n\\n6. **\\\"Why does per-DOF fail?\\\"**\\n   - Response: K samples in 7D action space → rank-deficient covariance → noisy directional signals. Low ε masks noise; high ε amplifies it. 3 seeds × 0% at uncapped confirms catastrophic failure.\\n\\n7. **\\\"A2C2 does K=1 correction and it works, yours doesn't\\\"**\\n   - Response (D060): A2C2 solves temporal staleness (within-chunk correction with new observations), not initial action quality. Different problem, different mechanism. Our K=1 failure is about single-sample residual correction without temporal context — complementary finding.\\n\\n8. **\\\"Why not just fine-tune the VLA?\\\"**\\n   - Response: VLA is already fine-tuned (LoRA SFT on LIBERO), but inference-time correction provides additional gains without modifying VLA weights. CRM does not modify VLA weights but requires VLA rollout cache on deployment tasks for CRM training. LTO (D069) confirms: CRM correction is task-specific — deployment tasks must be covered in CRM training data.\\n\\n## Hard Evidence (D058 corrected, M013 fixed)\\n\\n### K=10 obs_only vs argmin — LOCKED, PRIMARY (D084: excl. seed42)\\n- obs_only: seeds 43/44/45/46/47/48/51 = 16/16/16/15/20/18/17, mean=**16.8%±1.8%** (n=7). [seed42=22% excluded per D084]\\n- argmin: seeds 42/43/44/45/46/47 = 12/17/13/12/10/10, pooled 74/600 (12.3%)\\n- Statistical tests need recalculation with updated VLA-only n=8 baseline\\n\\n### Component Decomposition — LOCKED (K=10) + PRELIMINARY (K=5)\\n\\n**K=10 decomposition (LOCKED):**\\n- VLA-only (K=1): 10.8%±1.3% (n=9, seeds 42-50)\\n- Random selection (K=10): 11.67%±2.3% (n=3, seed42=13%, seed43=9%, seed44=13%). Random ≈ VLA-only (10.8%)\\n- Argmin (K=10): 12.3%±2.6% (6 seeds, 42/43/44/45/46/47)\\n- Random selection (K=10): 9.7%±1.5% (n=6). Random fails to exceed VLA-only.\\n- CRM obs_only (K=10): 16.8%±1.8% (n=7, excl. seed42 per D084)\\n- Selection effect (D064): argmin vs random = +2.6pp. \\n- Correction effect: CRM vs argmin = +4.5pp, CRM vs random = +7.1pp (sole driver)\\n- Per-seed correction margin: -1pp to +10pp (seed43: obs_only 16% < argmin 17%)\\n\\n**K=5 decomposition (n=3 argmin, n=4 random — Random K=5 DONE ✅):**\\n- Random (K=5): **10.5%±2.9%** (n=4, seed42=14%, seed43=11%, seed44=10%, seed45=7%). ⚠️ **Random K=5 < VLA-only (10.8%)** — 随机多采样有害！\\n- Argmin (K=5): 13.7%±1.2% (n=3, seed42=15%, seed43=13%, seed45=13%). seed44 running → n=4.\\n- CRM obs_only (K=5): 16.0%±2.2% (n=7)\\n- Multi-sampling effect (K=5): random - VLA-only = **-1.1pp** (HARMFUL)\\n- Selection effect (K=5): argmin - random = **+3.2pp** (rescues from random damage + adds value)\\n- Correction effect (K=5): CRM - argmin = **+2.3pp**\\n- **K-dependent decomposition insight (updated)**:\\n  - K=5: multi-sampling hurts (-1.1pp), argmin selection essential (+3.2pp), correction additive (+2.3pp)\\n  - K=10: multi-sampling neutral (random≈VLA-only), argmin marginal (+0.6pp), correction dominant (+5.3pp)\\n  - As K↑: random pick quality improves (converges to marginal) → argmin selection becomes unnecessary → correction becomes sole differentiator\\n  - **Implication for adaptive K (D072)**: naive multi-sampling is wasteful or harmful. Smart allocation (argmin centering + CRM correction, only when needed) is essential.\\n\\n**Spatial Random Selection K=10 (cross-benchmark validation ✅):**\\n- Random Selection (K=10): **29.3%** (n=3, seed42=34%, seed43=26%, seed44=28%). exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44\\n- VLA-only Spatial: 29.3%±1.7% (n=4, seed42=30%, seed43=29%, seed44=31%, seed45=27%)\\n- CRM obs_only Spatial (K=10): 34.5%±1.5%\\n- Multi-sampling effect: Random - VLA-only = **0.0pp** (neutral, same as Object pattern)\\n- Correction effect: CRM - Random = **+5.2pp** (sole driver, consistent with Object +5.8pp)\\n- **双 benchmark 一致结论**: multi-sampling alone 不产生价值（Object: random 11.67% ≈ VLA 10.8%; Spatial: random 29.3% ≈ VLA 29.3%），CRM correction 是唯一改善来源（Object +5.8pp, Spatial +5.2pp）\\n\\n### K-value Curve (D063 updated, K=5 n=7, JSON-verified)\\n- VLA-only (K=1, no CRM): 10.8%±1.3% (n=9) — the baseline reference\\n- CRM K=1 (ACCG): 10.3±1.5% (3 seeds: 42=12%, 43=9%, 44=10%) — NEGATIVE, below VLA-only\\n- CRM K=5 (obs_only): 16.0±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18])\\n- CRM K=10 (obs_only): 16.8±1.8% (n=7, excl. seed42 per D084)\\n- CRM K=20 (obs_only): 18.7%\\n- K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp.\\n\\n### Magnitude Curve (M013 corrected, updated D069) — LOCKED\\n- obs_only: ε=0.03(**15.75%±0.96%,n=4**: seed42=16%,seed44=17%,seed47=15%,seed48=15%), ε=0.05(~14%,n=5), ε=0.1(~17%,n=8), ε=0.2(17.6%,n=7), ε=0.3(~17%,n=7), default(~17%,n=5)\\n- perdof: ε=0.03(~10%,n=3), ε=0.05(~11%,n=4: seed42=14%,seed44=9%,seed45=10%,seed43=?), ε=0.1(~11%,n=7), ε=0.2(9.9%,n=7), ε=0.3(~5%,n=5), default(0%,n=6)\\n- ✅ obs_only ε=0.03 n=4 完整 (15.75%±0.96%)，error bars 可报告\\n\\n### Cross-VLA (D054, updated D087) — IN PROGRESS\\n- OpenVLA T=0.5: 8/10 actions identical, per-DOF variance <1e-30 for DOFs 0/1/3/5/6 → near-deterministic\\n- SmolVLA (0.4B, flow-matching): naturally stochastic, K=10 produces diverse candidates\\n- **OpenVLA VLA-only (D087)**: v1=0% (plan_801, 0/100 rollouts) → **v2=69%** (10 trials/task, original eval setting). v1 failure was setup/evaluation issue, not model limitation.\\n- **OpenVLA CRM (plan_802)**: CRM obs_only training complete (val_loss=0.077260, 50 epochs, obs_dim=4096). CRM eval awaiting GPU allocation on bjb2-28827 (needs 2 GPUs for 7B model).\\n- **Key question**: Does CRM correction work for near-deterministic OpenVLA? Multi-sampling may not produce diverse candidates → C3 prerequisite 1 test.\\n\\n### Latency — plan_602 Formal Profiling (RTX 4090, bjb1-18228)\\n**Sequential**:\\n- K=1: 177ms, K=5: 892ms, K=10: 1639ms, K=20: 3246ms (~165ms/K linear)\\n\\n**Batched (model inference only)**:\\n- K=1: 180ms, K=5: 182ms, K=10: 162ms, K=20: 167ms\\n- **Batched latency ~170ms independent of K** (~5.5 Hz model inference)\\n- Full pipeline (inference + scoring): ~200ms (~5 Hz)\\n\\n**CRM overhead**: 0.246ms (negligible). CRM model size: 1.8MB vs VLA 884MB.\\n**Key insight**: Batched inference eliminates K as a latency factor. K=20 batched ≈ K=1.\\n\\n⚠️ D067 earlier reported ~314ms — likely included sim step + data loading. Paper should report model inference (~170ms) or full pipeline (~200ms), clearly labeled. Both support the narrative.\\n\\n### LTO Generalization Boundary (D069) — LOCKED, NEGATIVE\\n- CRM trained on Split A (5 tasks), evaluated on 5 held-out tasks\\n- CRM+K=5: 2% (1/50) vs VLA-only: 14% (7/50)\\n- Per-task: salad_dressing 0 vs 30%, milk 0 vs 20%, orange_juice 0 vs 10%, ketchup 0 vs 0%, tomato_sauce 10 vs 10%\\n- CRM zeroes out tasks where VLA has capability → correction is task-specific, actively harmful OOD\\n- **LTO VLA-only double reproduction**: r2=14%, r3=14%, per-task identical. Baseline stable, D069 conclusion high confidence.\\n- Mechanism: CRM learns task-specific action distribution shifts (correction biases), not general quality assessment\\n- K=1 failure + LTO failure together: CRM correction = task-specific residual, needs (1) multi-sample centering AND (2) in-distribution tasks\\n- Table 1 cross-benchmark (Object+Spatial) is in-distribution: CRM training covers all 20 tasks\\n- Paper: Discussion/Limitations section, honest analysis framing\\n\\n### Spatial (cross-benchmark, in-distribution)\\n**K=10**: seed42=35%, seed44=36%, seed45=34%, seed47=32%, mean=**34.25%±1.7%** (n=4). seed43 running on bjb2-40593, seed46 被杀待重跑.\\n**K=5**: seed42=35%, seed43=32%, seed44=37%, seed45=34%, mean=**34.5%±2.1%** (n=4). K=5→K=10 仅 +0.5pp（边际递减更极端）。\\n**VLA-only baseline**: seed42=30%, seed43=29%, seed44=**31%**, seed45=**27%**. Mean=**29.3%±1.7%** (n=4). ✅ DONE.\\n**Paired K=10 improvements**: seed42 +5pp (35-30), seed44 +5pp (36-31), seed45 +7pp (34-27). Mean Δ=**+5.7pp** (n=3 paired). seed43 K=10 still running.\\n**Paired K=5 improvements**: seed42 +5pp (35-30), seed43 +3pp (32-29). Mean Δ=+4pp (n=2 paired).\\n**CRM 方差更低**: CRM K=10 std=1.0% vs VLA-only std=1.7%。CRM 在稳定性上也优于 baseline。\\n**Framing**: \\\"consistent cross-benchmark absolute improvement (+5-6pp)\\\" — 不强调 Spatial 相对改进率（19% vs Object 52%），因为 Spatial baseline 更高。\\n**Per-task pattern**: VLA-only 和 CRM 共享同一组 zero-success tasks (4/10)。CRM 改善中等难度 tasks，不修复 impossible tasks。\\n\\n## INVALIDATED Claims (do not use)\\n- ~~K=1 improves frozen VLA~~ — D050/D051: K=1 ACCG fallback 10.0%, multi-scale 10.3%, both ≈ baseline\\n- ~~CRM ranks/selects among K candidates~~ — D058: CRM is correction module, not ranking. Same argmin selection for all modes.\\n- ~~obs_only uses conformal features~~ — D058: uf_input=None for obs_only mode\\n- ~~Cross-VLA positive transfer~~ — D054: OpenVLA near-deterministic at T=0.5. D087: v2 baseline=69%, CRM training done, eval pending\\n- ~~perdof default 0% × 3 seeds~~ — M013: was 2 seeds + 1 misclassified. Corrected to 3 data points (2 full + 1 partial) all 0%.\\n\\n## Pending Evidence (cleaned D069)\\n- ~~K=5 seeds~~ → ✅ DONE, n=7\\n- K=5 argmin decomposition: seed42/43/45 ✅ DONE (13.7%±1.2%, n=3), seed44 running (~1h) → n=4. 结果：selection +2.1pp / correction +2.3pp (与 K=10 不同的分解模式)\\n- Spatial K=10: seed43/44/45 running → cross-benchmark K scaling\\n- ~~Spatial VLA-only baseline~~ → ✅ DONE n=4 (29.3%±1.7%, seed42=30%/43=29%/44=31%/45=27%). Paired Δ=+5.7pp (n=3).\\n- ~~obs_only ε=0.03~~ → ✅ DONE, n=4 (15.75%±0.96%, seed42/44/47/48)\\n- ~~LTO~~ → ✅ DONE (D069 negative)\\n- ~~K=1 CRM eval (plan_702)~~ → ✅ DONE: 10.3%±1.5% (n=3, seed42=12%/43=9%/44=10%, NEGATIVE). Below VLA-only 10.8%. Already in K-value curve.\\n- ~~Random K=5~~ → ✅ DONE n=4 (10.5%±2.9%). Random < VLA-only — multi-sampling harmful at K=5!\\n- OpenVLA CRM eval (plan_802): CRM training done (val_loss=0.077260), eval 待 bjb2-28827 GPU 释放 (standing order P2)\\n- ~~Adaptive K~~ → ✅ P50=15.3% at avg_K=3.8 LOCKED. D090 Plan A eval in progress.\\n- Cross-server reproducibility: argmin K=5 seed42 = 15%(bjb1) vs 13%(bjb2), ±2pp noise floor noted\\n\", \"total_chars\": 26168, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "1c3dd406-dd9f-4a1b-8af3-47f896c4cce0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — acr-vla-conformal-refinement\\\\n\\\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\\\n\\\\n## Target Venue\\\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\\\n- Title: \\\\\\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\\\\\"\\\\n\\\\n## Core Insight (D065 revised)\\\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\\\n\\\\n## Headline Metrics\\\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\\\n\\\\n## Core Claims (3 claims, D061)\\\\n\\\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\\\n\\\\n### C2: Conditioning-magnitude interaction — first systematic study\\\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\\\n\\\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\\\\\"recognizes\\\\\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\\\n\\\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\\\n\\\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\\\n\\\\n**信号验证结果 (D076)**:\\\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\\\n\\\\n**确定的架构**:\\\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\\\\\"困难步\\\\\\\"）\\\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\\\\\"简单步\\\\\\\"）\\\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\\\n\\\\n**Phase 2 结果 (Object)**:\\\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\\\n- Spatial 跨 benchmark 验证完成\\\\n\\\\n**对论文 framing 的影响**:\\\\n- 从纯 analysis paper 升级为 analysis + method paper\\\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\\\n- K=10 固定推理保留为 oracle upper bound\\\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\\\n\\\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\\\n\\\\n**D088 Learned Uncertainty Head — NO-GO**:\\\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\\\n\\\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\\\n\\\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\\\n\\\\n**对论文影响 (D091)**:\\\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\\\n\\\\n## Story Spine\\\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVLA: UQ; SC-VLA: residual RL) address adjacent problems.\\\\n- **Our angle**: We first dissect inference-time multi-sample correction, finding that learned correction is the active mechanism while multi-sampling is an enabling condition. These findings inform the design of an **adaptive K mechanism** that dynamically allocates compute — sampling more only when the VLA is uncertain. The conditioning-magnitude interaction and applicability boundaries further constrain safe deployment.\\\\n- **Headline**: \\\\\\\"Adaptive inference-time correction improves frozen VLA with avg_K << K_max. Analysis: correction is the active mechanism, not selection. Conditioning-magnitude interaction determines success vs catastrophic failure. Adaptive K achieves ~91% of fixed K=10 performance at 38% average compute (avg_K=3.8 vs K=10).\\\\\\\"\\\\n\\\\n## Competitive Landscape\\\\n\\\\n### A2C2 (D060) — Complementary, not competing\\\\nFrozen VLA + per-step correction within action chunks. Solves **temporal staleness** (chunk actions become outdated during execution). Our method solves **initial action quality** (improve the action before execution). Orthogonal and combinable. A2C2 trains SmolVLA from scratch (67-72% baseline) — different setting from our frozen pretrained VLA (10.8%).\\\\n\\\\n### ReconVLA — Same domain, different route\\\\nConformal quantile regression for UQ + OOD detection on frozen VLA. Does not perform learned correction.\\\\n\\\\n### SC-VLA / PLD — RL-based refinement\\\\nResidual RL per-task. Requires online training, not plug-and-play. PLD achieves 99% on LIBERO but with full fine-tuning.\\\\n\\\\n### Our positioning (D058/D061, updated D072)\\\\nFirst to (1) decompose inference-time VLA correction into selection vs correction contributions, (2) systematically study conditioning-magnitude interaction revealing catastrophic failure mode, (3) establish applicability boundaries across VLA architectures (stochastic vs deterministic), **(4) propose adaptive inference-time compute allocation based on per-step uncertainty — dynamically deciding K rather than fixed brute-force sampling**. The adaptive K mechanism connects to LLM inference-time compute scaling trends in embodied AI.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"Absolute performance is low (16.8% on an 11% baseline)\\\\\\\"**\\\\n   - Response: This is frozen fine-tuned VLA with inference-time correction (VLA weights fixed during CRM training and deployment). ~53% relative improvement (+5.8pp) is significant given the frozen constraint. The contribution is the systematic analysis of when/why/how inference-time correction works, not SOTA absolute numbers. Community benchmark: A2C2 trains SmolVLA from scratch on LIBERO reaching 67-72%, a different training regime.\\\\n\\\\n2. **\\\\\\\"Method only works for weak/small VLAs\\\\\\\"**\\\\n   - Response: Honest analysis (C3). Correction value correlates inversely with base model quality/determinism. This is a genuine insight with practical implications: small stochastic VLAs are relevant for edge deployment, latency-constrained scenarios, and new task generalization without fine-tuning.\\\\n\\\\n3. **\\\\\\\"K=1 doesn't work, K=10 needs 10× compute\\\\\\\"**\\\\n   - Response: **Adaptive K (D076) directly addresses this.** Default K=2 (same latency as K=1 with batching ~170ms). K=2 pairwise L2 distance as uncertainty signal (ρ=0.9979 vs K=10 variance). High uncertainty → extend to K=10 + CRM; low uncertainty → use K=2 directly. avg_K=3.8, achieving ~91% of fixed K=10 performance (15.3% vs 16.8%). K=1 CRM failure (10.3%) is a finding: correction needs multi-sample centering. FMVD failure (ρ=0.08) is ablation evidence for why action-space signals work while ODE-space signals don't.\\\\n\\\\n4. **\\\\\\\"obs_only is just a residual MLP, where is the novelty?\\\\\\\"**\\\\n   - Response: Novelty is the systematic analysis, not the architecture. Architecture simplicity isolates the conditioning signal's effect. The conditioning-magnitude interaction and component decomposition are new.\\\\n\\\\n5. **\\\\\\\"Single benchmark (LIBERO-Object)\\\\\\\"**\\\\n   - Response: **Fully addressed with LIBERO-Spatial data.** CRM K=10 Spatial: 35.0%±1.0% (n=3) vs VLA-only 29.3%±1.7% (n=4). Paired Δ=+5.7pp (n=3), matching Object's +6pp. K=5 Spatial: 33.5% (n=2). Both Object and Spatial are in-distribution (CRM trained on all 20 tasks). LTO (D069) shows OOD limitation — honest boundary. OpenVLA v2=69% baseline (D087), CRM eval pending.\\\\n\\\\n6. **\\\\\\\"Why does per-DOF fail?\\\\\\\"**\\\\n   - Response: K samples in 7D action space → rank-deficient covariance → noisy directional signals. Low ε masks noise; high ε amplifies it. 3 seeds × 0% at uncapped confirms catastrophic failure.\\\\n\\\\n7. **\\\\\\\"A2C2 does K=1 correction and it works, yours doesn't\\\\\\\"**\\\\n   - Response (D060): A2C2 solves temporal staleness (within-chunk correction with new observations), not initial action quality. Different problem, different mechanism. Our K=1 failure is about single-sample residual correction without temporal context — complementary finding.\\\\n\\\\n8. **\\\\\\\"Why not just fine-tune the VLA?\\\\\\\"**\\\\n   - Response: VLA is already fine-tuned (LoRA SFT on LIBERO), but inference-time correction provides additional gains without modifying VLA weights. CRM does not modify VLA weights but requires VLA rollout cache on deployment tasks for CRM training. LTO (D069) confirms: CRM correction is task-specific — deployment tasks must be covered in CRM training data.\\\\n\\\\n## Hard Evidence (D058 corrected, M013 fixed)\\\\n\\\\n### K=10 obs_only vs argmin — LOCKED, PRIMARY (D084: excl. seed42)\\\\n- obs_only: seeds 43/44/45/46/47/48/51 = 16/16/16/15/20/18/17, mean=**16.8%±1.8%** (n=7). [seed42=22% excluded per D084]\\\\n- argmin: seeds 42/43/44/45/46/47 = 12/17/13/12/10/10, pooled 74/600 (12.3%)\\\\n- Statistical tests need recalculation with updated VLA-only n=8 baseline\\\\n\\\\n### Component Decomposition — LOCKED (K=10) + PRELIMINARY (K=5)\\\\n\\\\n**K=10 decomposition (LOCKED):**\\\\n- VLA-only (K=1): 10.8%±1.3% (n=9, seeds 42-50)\\\\n- Random selection (K=10): 11.67%±2.3% (n=3, seed42=13%, seed43=9%, seed44=13%). Random ≈ VLA-only (10.8%)\\\\n- Argmin (K=10): 12.3%±2.6% (6 seeds, 42/43/44/45/46/47)\\\\n- Random selection (K=10): 9.7%±1.5% (n=6). Random fails to exceed VLA-only.\\\\n- CRM obs_only (K=10): 16.8%±1.8% (n=7, excl. seed42 per D084)\\\\n- Selection effect (D064): argmin vs random = +2.6pp. \\\\n- Correction effect: CRM vs argmin = +4.5pp, CRM vs random = +7.1pp (sole driver)\\\\n- Per-seed correction margin: -1pp to +10pp (seed43: obs_only 16% < argmin 17%)\\\\n\\\\n**K=5 decomposition (n=3 argmin, n=4 random — Random K=5 DONE ✅):**\\\\n- Random (K=5): **10.5%±2.9%** (n=4, seed42=14%, seed43=11%, seed44=10%, seed45=7%). ⚠️ **Random K=5 < VLA-only (10.8%)** — 随机多采样有害！\\\\n- Argmin (K=5): 13.7%±1.2% (n=3, seed42=15%, seed43=13%, seed45=13%). seed44 running → n=4.\\\\n- CRM obs_only (K=5): 16.0%±2.2% (n=7)\\\\n- Multi-sampling effect (K=5): random - VLA-only = **-1.1pp** (HARMFUL)\\\\n- Selection effect (K=5): argmin - random = **+3.2pp** (rescues from random damage + adds value)\\\\n- Correction effect (K=5): CRM - argmin = **+2.3pp**\\\\n- **K-dependent decomposition insight (updated)**:\\\\n  - K=5: multi-sampling hurts (-1.1pp), argmin selection essential (+3.2pp), correction additive (+2.3pp)\\\\n  - K=10: multi-sampling neutral (random≈VLA-only), argmin marginal (+0.6pp), correction dominant (+5.3pp)\\\\n  - As K↑: random pick quality improves (converges to marginal) → argmin selection becomes unnecessary → correction becomes sole differentiator\\\\n  - **Implication for adaptive K (D072)**: naive multi-sampling is wasteful or harmful. Smart allocation (argmin centering + CRM correction, only when needed) is essential.\\\\n\\\\n**Spatial Random Selection K=10 (cross-benchmark validation ✅):**\\\\n- Random Selection (K=10): **29.3%** (n=3, seed42=34%, seed43=26%, seed44=28%). exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44\\\\n- VLA-only Spatial: 29.3%±1.7% (n=4, seed42=30%, seed43=29%, seed44=31%, seed45=27%)\\\\n- CRM obs_only Spatial (K=10): 34.5%±1.5%\\\\n- Multi-sampling effect: Random - VLA-only = **0.0pp** (neutral, same as Object pattern)\\\\n- Correction effect: CRM - Random = **+5.2pp** (sole driver, consistent with Object +5.8pp)\\\\n- **双 benchmark 一致结论**: multi-sampling alone 不产生价值（Object: random 11.67% ≈ VLA 10.8%; Spatial: random 29.3% ≈ VLA 29.3%），CRM correction 是唯一改善来源（Object +5.8pp, Spatial +5.2pp）\\\\n\\\\n### K-value Curve (D063 updated, K=5 n=7, JSON-verified)\\\\n- VLA-only (K=1, no CRM): 10.8%±1.3% (n=9) — the baseline reference\\\\n- CRM K=1 (ACCG): 10.3±1.5% (3 seeds: 42=12%, 43=9%, 44=10%) — NEGATIVE, below VLA-only\\\\n- CRM K=5 (obs_only): 16.0±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18])\\\\n- CRM K=10 (obs_only): 16.8±1.8% (n=7, excl. seed42 per D084)\\\\n- CRM K=20 (obs_only): 18.7%\\\\n- K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp.\\\\n\\\\n### Magnitude Curve (M013 corrected, updated D069) — LOCKED\\\\n- obs_only: ε=0.03(**15.75%±0.96%,n=4**: seed42=16%,seed44=17%,seed47=15%,seed48=15%), ε=0.05(~14%,n=5), ε=0.1(~17%,n=8), ε=0.2(17.6%,n=7), ε=0.3(~17%,n=7), default(~17%,n=5)\\\\n- perdof: ε=0.03(~10%,n=3), ε=0.05(~11%,n=4: seed42=14%,seed44=9%,seed45=10%,seed43=?), ε=0.1(~11%,n=7), ε=0.2(9.9%,n=7), ε=0.3(~5%,n=5), default(0%,n=6)\\\\n- ✅ obs_only ε=0.03 n=4 完整 (15.75%±0.96%)，error bars 可报告\\\\n\\\\n### Cross-VLA (D054, updated D087) — IN PROGRESS\\\\n- OpenVLA T=0.5: 8/10 actions identical, per-DOF variance <1e-30 for DOFs 0/1/3/5/6 → near-deterministic\\\\n- SmolVLA (0.4B, flow-matching): naturally stochastic, K=10 produces diverse candidates\\\\n- **OpenVLA VLA-only (D087)**: v1=0% (plan_801, 0/100 rollouts) → **v2=69%** (10 trials/task, original eval setting). v1 failure was setup/evaluation issue, not model limitation.\\\\n- **OpenVLA CRM (plan_802)**: CRM obs_only training complete (val_loss=0.077260, 50 epochs, obs_dim=4096). CRM eval awaiting GPU allocation on bjb2-28827 (needs 2 GPUs for 7B model).\\\\n- **Key question**: Does CRM correction work for near-deterministic OpenVLA? Multi-sampling may not produce diverse candidates → C3 prerequisite 1 test.\\\\n\\\\n### Latency — plan_602 Formal Profiling (RTX 4090, bjb1-18228)\\\\n**Sequential**:\\\\n- K=1: 177ms, K=5: 892ms, K=10: 1639ms, K=20: 3246ms (~165ms/K linear)\\\\n\\\\n**Batched (model inference only)**:\\\\n- K=1: 180ms, K=5: 182ms, K=10: 162ms, K=20: 167ms\\\\n- **Batched latency ~170ms independent of K** (~5.5 Hz model inference)\\\\n- Full pipeline (inference + scoring): ~200ms (~5 Hz)\\\\n\\\\n**CRM overhead**: 0.246ms (negligible). CRM model size: 1.8MB vs VLA 884MB.\\\\n**Key insight**: Batched inference eliminates K as a latency factor. K=20 batched ≈ K=1.\\\\n\\\\n⚠️ D067 earlier reported ~314ms — likely included sim step + data loading. Paper should report model inference (~170ms) or full pipeline (~200ms), clearly labeled. Both support the narrative.\\\\n\\\\n### LTO Generalization Boundary (D069) — LOCKED, NEGATIVE\\\\n- CRM trained on Split A (5 tasks), evaluated on 5 held-out tasks\\\\n- CRM+K=5: 2% (1/50) vs VLA-only: 14% (7/50)\\\\n- Per-task: salad_dressing 0 vs 30%, milk 0 vs 20%, orange_juice 0 vs 10%, ketchup 0 vs 0%, tomato_sauce 10 vs 10%\\\\n- CRM zeroes out tasks where VLA has capability → correction is task-specific, actively harmful OOD\\\\n- **LTO VLA-only double reproduction**: r2=14%, r3=14%, per-task identical. Baseline stable, D069 conclusion high confidence.\\\\n- Mechanism: CRM learns task-specific action distribution shifts (correction biases), not general quality assessment\\\\n- K=1 failure + LTO failure together: CRM correction = task-specific residual, needs (1) multi-sample centering AND (2) in-distribution tasks\\\\n- Table 1 cross-benchmark (Object+Spatial) is in-distribution: CRM training covers all 20 tasks\\\\n- Paper: Discussion/Limitations section, honest analysis framing\\\\n\\\\n### Spatial (cross-benchmark, in-distribution)\\\\n**K=10**: seed42=35%, seed44=36%, seed45=34%, seed47=32%, mean=**34.25%±1.7%** (n=4). seed43 running on bjb2-40593, seed46 被杀待重跑.\\\\n**K=5**: seed42=35%, seed43=32%, seed44=37%, seed45=34%, mean=**34.5%±2.1%** (n=4). K=5→K=10 仅 +0.5pp（边际递减更极端）。\\\\n**VLA-only baseline**: seed42=30%, seed43=29%, seed44=**31%**, seed45=**27%**. Mean=**29.3%±1.7%** (n=4). ✅ DONE.\\\\n**Paired K=10 improvements**: seed42 +5pp (35-30), seed44 +5pp (36-31), seed45 +7pp (34-27). Mean Δ=**+5.7pp** (n=3 paired). seed43 K=10 still running.\\\\n**Paired K=5 improvements**: seed42 +5pp (35-30), seed43 +3pp (32-29). Mean Δ=+4pp (n=2 paired).\\\\n**CRM 方差更低**: CRM K=10 std=1.0% vs VLA-only std=1.7%。CRM 在稳定性上也优于 baseline。\\\\n**Framing**: \\\\\\\"consistent cross-benchmark absolute improvement (+5-6pp)\\\\\\\" — 不强调 Spatial 相对改进率（19% vs Object 52%），因为 Spatial baseline 更高。\\\\n**Per-task pattern**: VLA-only 和 CRM 共享同一组 zero-success tasks (4/10)。CRM 改善中等难度 tasks，不修复 impossible tasks。\\\\n\\\\n## INVALIDATED Claims (do not use)\\\\n- ~~K=1 improves frozen VLA~~ — D050/D051: K=1 ACCG fallback 10.0%, multi-scale 10.3%, both ≈ baseline\\\\n- ~~CRM ranks/selects among K candidates~~ — D058: CRM is correction module, not ranking. Same argmin selection for all modes.\\\\n- ~~obs_only uses conformal features~~ — D058: uf_input=None for obs_only mode\\\\n- ~~Cross-VLA positive transfer~~ — D054: OpenVLA near-deterministic at T=0.5. D087: v2 baseline=69%, CRM training done, eval pending\\\\n- ~~perdof default 0% × 3 seeds~~ — M013: was 2 seeds + 1 misclassified. Corrected to 3 data points (2 full + 1 partial) all 0%.\\\\n\\\\n## Pending Evidence (cleaned D069)\\\\n- ~~K=5 seeds~~ → ✅ DONE, n=7\\\\n- K=5 argmin decomposition: seed42/43/45 ✅ DONE (13.7%±1.2%, n=3), seed44 running (~1h) → n=4. 结果：selection +2.1pp / correction +2.3pp (与 K=10 不同的分解模式)\\\\n- Spatial K=10: seed43/44/45 running → cross-benchmark K scaling\\\\n- ~~Spatial VLA-only baseline~~ → ✅ DONE n=4 (29.3%±1.7%, seed42=30%/43=29%/44=31%/45=27%). Paired Δ=+5.7pp (n=3).\\\\n- ~~obs_only ε=0.03~~ → ✅ DONE, n=4 (15.75%±0.96%, seed42/44/47/48)\\\\n- ~~LTO~~ → ✅ DONE (D069 negative)\\\\n- ~~K=1 CRM eval (plan_702)~~ → ✅ DONE: 10.3%±1.5% (n=3, seed42=12%/43=9%/44=10%, NEGATIVE). Below VLA-only 10.8%. Already in K-value curve.\\\\n- ~~Random K=5~~ → ✅ DONE n=4 (10.5%±2.9%). Random < VLA-only — multi-sampling harmful at K=5!\\\\n- OpenVLA CRM eval (plan_802): CRM training done (val_loss=0.077260), eval 待 bjb2-28827 GPU 释放 (standing order P2)\\\\n- ~~Adaptive K~~ → ✅ P50=15.3% at avg_K=3.8 LOCKED. D090 Plan A eval in progress.\\\\n- Cross-server reproducibility: argmin K=5 seed42 = 15%(bjb1) vs 13%(bjb2), ±2pp noise floor noted\\\\n\\\", \\\"total_chars\\\": 26168, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\n\\n## Target Venue\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\n- Title: \\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\"\\n\\n## Core Insight (D065 revised)\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\n\\n## Headline Metrics\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\n\\n## Core Claims (3 claims, D061)\\n\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\n\\n### C2: Conditioning-magnitude interaction — first systematic study\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\n\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\"recognizes\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\n\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\n\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\n\\n**信号验证结果 (D076)**:\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\n\\n**确定的架构**:\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\"困难步\\\"）\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\"简单步\\\"）\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\n\\n**Phase 2 结果 (Object)**:\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\n- Spatial 跨 benchmark 验证完成\\n\\n**对论文 framing 的影响**:\\n- 从纯 analysis paper 升级为 analysis + method paper\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\n- K=10 固定推理保留为 oracle upper bound\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\n\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\n\\n**D088 Learned Uncertainty Head — NO-GO**:\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\n\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\n\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\n\\n**对论文影响 (D091)**:\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\n\\n## Story Spine\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVLA: UQ; SC-VLA: residual RL) address adjacent problems.\\n- **Our angle**: We first dissect inference-time multi-sample correction, finding that learned correction is the active mechanism while multi-sampling is an enabling condition. These findings inform the design of an **adaptive K mechanism** that dynamically allocates compute — sampling more only when the VLA is uncertain. The conditioning-magnitude interaction and applicability boundaries further constrain safe deployment.\\n- **Headline**: \\\"Adaptive inference-time correction improves frozen VLA with avg_K << K_max. Analysis: correction is the active mechanism, not selection. Conditioning-magnitude interaction determines success vs catastrophic failure. Adaptive K achieves ~91% of fixed K=10 performance at 38% average compute (avg_K=3.8 vs K=10).\\\"\\n\\n## Competitive Landscape\\n\\n### A2C2 (D060) — Complementary, not competing\\nFrozen VLA + per-step correction within action chunks. Solves **temporal staleness** (chunk actions become outdated during execution). Our method solves **initial action quality** (improve the action before execution). Orthogonal and combinable. A2C2 trains SmolVLA from scratch (67-72% baseline) — different setting from our frozen pretrained VLA (10.8%).\\n\\n### ReconVLA — Same domain, different route\\nConformal quantile regression for UQ + OOD detection on frozen VLA. Does not perform learned correction.\\n\\n### SC-VLA / PLD — RL-based refinement\\nResidual RL per-task. Requires online training, not plug-and-play. PLD achieves 99% on LIBERO but with full fine-tuning.\\n\\n### Our positioning (D058/D061, updated D072)\\nFirst to (1) decompose inference-time VLA correction into selection vs correction contributions, (2) systematically study conditioning-magnitude interaction revealing catastrophic failure mode, (3) establish applicability boundaries across VLA architectures (stochastic vs deterministic), **(4) propose adaptive inference-time compute allocation based on per-step uncertainty — dynamically deciding K rather than fixed brute-force sampling**. The adaptive K mechanism connects to LLM inference-time compute scaling trends in embodied AI.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Absolute performance is low (16.8% on an 11% baseline)\\\"**\\n   - Response: This is frozen fine-tuned VLA with inference-time correction (VLA weights fixed during CRM training and deployment). ~53% relative improvement (+5.8pp) is significant given the frozen constraint. The contribution is the systematic analysis of when/why/how inference-time correction works, not SOTA absolute numbers. Community benchmark: A2C2 trains SmolVLA from scratch on LIBERO reaching 67-72%, a different training regime.\\n\\n2. **\\\"Method only works for weak/small VLAs\\\"**\\n   - Response: Honest analysis (C3). Correction value correlates inversely with base model quality/determinism. This is a genuine insight with practical implications: small stochastic VLAs are relevant for edge deployment, latency-constrained scenarios, and new task generalization without fine-tuning.\\n\\n3. **\\\"K=1 doesn't work, K=10 needs 10× compute\\\"**\\n   - Response: **Adaptive K (D076) directly addresses this.** Default K=2 (same latency as K=1 with batching ~170ms). K=2 pairwise L2 distance as uncertainty signal (ρ=0.9979 vs K=10 variance). High uncertainty → extend to K=10 + CRM; low uncertainty → use K=2 directly. avg_K=3.8, achieving ~91% of fixed K=10 performance (15.3% vs 16.8%). K=1 CRM failure (10.3%) is a finding: correction needs multi-sample centering. FMVD failure (ρ=0.08) is ablation evidence for why action-space signals work while ODE-space signals don't.\\n\\n4. **\\\"obs_only is just a residual MLP, where is the novelty?\\\"**\\n   - Response: Novelty is the systematic analysis, not the architecture. Architecture simplicity isolates the conditioning signal's effect. The conditioning-magnitude interaction and component decomposition are new.\\n\\n5. **\\\"Single benchmark (LIBERO-Object)\\\"**\\n   - Response: **Fully addressed with LIBERO-Spatial data.** CRM K=10 Spatial: 35.0%±1.0% (n=3) vs VLA-only 29.3%±1.7% (n=4). Paired Δ=+5.7pp (n=3), matching Object's +6pp. K=5 Spatial: 33.5% (n=2). Both Object and Spatial are in-distribution (CRM trained on all 20 tasks). LTO (D069) shows OOD limitation — honest boundary. OpenVLA v2=69% baseline (D087), CRM eval pending.\\n\\n6. **\\\"Why does per-DOF fail?\\\"**\\n   - Response: K samples in 7D action space → rank-deficient covariance → noisy directional signals. Low ε masks noise; high ε amplifies it. 3 seeds × 0% at uncapped confirms catastrophic failure.\\n\\n7. **\\\"A2C2 does K=1 correction and it works, yours doesn't\\\"**\\n   - Response (D060): A2C2 solves temporal staleness (within-chunk correction with new observations), not initial action quality. Different problem, different mechanism. Our K=1 failure is about single-sample residual correction without temporal context — complementary finding.\\n\\n8. **\\\"Why not just fine-tune the VLA?\\\"**\\n   - Response: VLA is already fine-tuned (LoRA SFT on LIBERO), but inference-time correction provides additional gains without modifying VLA weights. CRM does not modify VLA weights but requires VLA rollout cache on deployment tasks for CRM training. LTO (D069) confirms: CRM correction is task-specific — deployment tasks must be covered in CRM training data.\\n\\n## Hard Evidence (D058 corrected, M013 fixed)\\n\\n### K=10 obs_only vs argmin — LOCKED, PRIMARY (D084: excl. seed42)\\n- obs_only: seeds 43/44/45/46/47/48/51 = 16/16/16/15/20/18/17, mean=**16.8%±1.8%** (n=7). [seed42=22% excluded per D084]\\n- argmin: seeds 42/43/44/45/46/47 = 12/17/13/12/10/10, pooled 74/600 (12.3%)\\n- Statistical tests need recalculation with updated VLA-only n=8 baseline\\n\\n### Component Decomposition — LOCKED (K=10) + PRELIMINARY (K=5)\\n\\n**K=10 decomposition (LOCKED):**\\n- VLA-only (K=1): 10.8%±1.3% (n=9, seeds 42-50)\\n- Random selection (K=10): 11.67%±2.3% (n=3, seed42=13%, seed43=9%, seed44=13%). Random ≈ VLA-only (10.8%)\\n- Argmin (K=10): 12.3%±2.6% (6 seeds, 42/43/44/45/46/47)\\n- Random selection (K=10): 9.7%±1.5% (n=6). Random fails to exceed VLA-only.\\n- CRM obs_only (K=10): 16.8%±1.8% (n=7, excl. seed42 per D084)\\n- Selection effect (D064): argmin vs random = +2.6pp. \\n- Correction effect: CRM vs argmin = +4.5pp, CRM vs random = +7.1pp (sole driver)\\n- Per-seed correction margin: -1pp to +10pp (seed43: obs_only 16% < argmin 17%)\\n\\n**K=5 decomposition (n=3 argmin, n=4 random — Random K=5 DONE ✅):**\\n- Random (K=5): **10.5%±2.9%** (n=4, seed42=14%, seed43=11%, seed44=10%, seed45=7%). ⚠️ **Random K=5 < VLA-only (10.8%)** — 随机多采样有害！\\n- Argmin (K=5): 13.7%±1.2% (n=3, seed42=15%, seed43=13%, seed45=13%). seed44 running → n=4.\\n- CRM obs_only (K=5): 16.0%±2.2% (n=7)\\n- Multi-sampling effect (K=5): random - VLA-only = **-1.1pp** (HARMFUL)\\n- Selection effect (K=5): argmin - random = **+3.2pp** (rescues from random damage + adds value)\\n- Correction effect (K=5): CRM - argmin = **+2.3pp**\\n- **K-dependent decomposition insight (updated)**:\\n  - K=5: multi-sampling hurts (-1.1pp), argmin selection essential (+3.2pp), correction additive (+2.3pp)\\n  - K=10: multi-sampling neutral (random≈VLA-only), argmin marginal (+0.6pp), correction dominant (+5.3pp)\\n  - As K↑: random pick quality improves (converges to marginal) → argmin selection becomes unnecessary → correction becomes sole differentiator\\n  - **Implication for adaptive K (D072)**: naive multi-sampling is wasteful or harmful. Smart allocation (argmin centering + CRM correction, only when needed) is essential.\\n\\n**Spatial Random Selection K=10 (cross-benchmark validation ✅):**\\n- Random Selection (K=10): **29.3%** (n=3, seed42=34%, seed43=26%, seed44=28%). exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44\\n- VLA-only Spatial: 29.3%±1.7% (n=4, seed42=30%, seed43=29%, seed44=31%, seed45=27%)\\n- CRM obs_only Spatial (K=10): 34.5%±1.5%\\n- Multi-sampling effect: Random - VLA-only = **0.0pp** (neutral, same as Object pattern)\\n- Correction effect: CRM - Random = **+5.2pp** (sole driver, consistent with Object +5.8pp)\\n- **双 benchmark 一致结论**: multi-sampling alone 不产生价值（Object: random 11.67% ≈ VLA 10.8%; Spatial: random 29.3% ≈ VLA 29.3%），CRM correction 是唯一改善来源（Object +5.8pp, Spatial +5.2pp）\\n\\n### K-value Curve (D063 updated, K=5 n=7, JSON-verified)\\n- VLA-only (K=1, no CRM): 10.8%±1.3% (n=9) — the baseline reference\\n- CRM K=1 (ACCG): 10.3±1.5% (3 seeds: 42=12%, 43=9%, 44=10%) — NEGATIVE, below VLA-only\\n- CRM K=5 (obs_only): 16.0±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18])\\n- CRM K=10 (obs_only): 16.8±1.8% (n=7, excl. seed42 per D084)\\n- CRM K=20 (obs_only): 18.7%\\n- K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp.\\n\\n### Magnitude Curve (M013 corrected, updated D069) — LOCKED\\n- obs_only: ε=0.03(**15.75%±0.96%,n=4**: seed42=16%,seed44=17%,seed47=15%,seed48=15%), ε=0.05(~14%,n=5), ε=0.1(~17%,n=8), ε=0.2(17.6%,n=7), ε=0.3(~17%,n=7), default(~17%,n=5)\\n- perdof: ε=0.03(~10%,n=3), ε=0.05(~11%,n=4: seed42=14%,seed44=9%,seed45=10%,seed43=?), ε=0.1(~11%,n=7), ε=0.2(9.9%,n=7), ε=0.3(~5%,n=5), default(0%,n=6)\\n- ✅ obs_only ε=0.03 n=4 完整 (15.75%±0.96%)，error bars 可报告\\n\\n### Cross-VLA (D054, updated D087) — IN PROGRESS\\n- OpenVLA T=0.5: 8/10 actions identical, per-DOF variance <1e-30 for DOFs 0/1/3/5/6 → near-deterministic\\n- SmolVLA (0.4B, flow-matching): naturally stochastic, K=10 produces diverse candidates\\n- **OpenVLA VLA-only (D087)**: v1=0% (plan_801, 0/100 rollouts) → **v2=69%** (10 trials/task, original eval setting). v1 failure was setup/evaluation issue, not model limitation.\\n- **OpenVLA CRM (plan_802)**: CRM obs_only training complete (val_loss=0.077260, 50 epochs, obs_dim=4096). CRM eval awaiting GPU allocation on bjb2-28827 (needs 2 GPUs for 7B model).\\n- **Key question**: Does CRM correction work for near-deterministic OpenVLA? Multi-sampling may not produce diverse candidates → C3 prerequisite 1 test.\\n\\n### Latency — plan_602 Formal Profiling (RTX 4090, bjb1-18228)\\n**Sequential**:\\n- K=1: 177ms, K=5: 892ms, K=10: 1639ms, K=20: 3246ms (~165ms/K linear)\\n\\n**Batched (model inference only)**:\\n- K=1: 180ms, K=5: 182ms, K=10: 162ms, K=20: 167ms\\n- **Batched latency ~170ms independent of K** (~5.5 Hz model inference)\\n- Full pipeline (inference + scoring): ~200ms (~5 Hz)\\n\\n**CRM overhead**: 0.246ms (negligible). CRM model size: 1.8MB vs VLA 884MB.\\n**Key insight**: Batched inference eliminates K as a latency factor. K=20 batched ≈ K=1.\\n\\n⚠️ D067 earlier reported ~314ms — likely included sim step + data loading. Paper should report model inference (~170ms) or full pipeline (~200ms), clearly labeled. Both support the narrative.\\n\\n### LTO Generalization Boundary (D069) — LOCKED, NEGATIVE\\n- CRM trained on Split A (5 tasks), evaluated on 5 held-out tasks\\n- CRM+K=5: 2% (1/50) vs VLA-only: 14% (7/50)\\n- Per-task: salad_dressing 0 vs 30%, milk 0 vs 20%, orange_juice 0 vs 10%, ketchup 0 vs 0%, tomato_sauce 10 vs 10%\\n- CRM zeroes out tasks where VLA has capability → correction is task-specific, actively harmful OOD\\n- **LTO VLA-only double reproduction**: r2=14%, r3=14%, per-task identical. Baseline stable, D069 conclusion high confidence.\\n- Mechanism: CRM learns task-specific action distribution shifts (correction biases), not general quality assessment\\n- K=1 failure + LTO failure together: CRM correction = task-specific residual, needs (1) multi-sample centering AND (2) in-distribution tasks\\n- Table 1 cross-benchmark (Object+Spatial) is in-distribution: CRM training covers all 20 tasks\\n- Paper: Discussion/Limitations section, honest analysis framing\\n\\n### Spatial (cross-benchmark, in-distribution)\\n**K=10**: seed42=35%, seed44=36%, seed45=34%, seed47=32%, mean=**34.25%±1.7%** (n=4). seed43 running on bjb2-40593, seed46 被杀待重跑.\\n**K=5**: seed42=35%, seed43=32%, seed44=37%, seed45=34%, mean=**34.5%±2.1%** (n=4). K=5→K=10 仅 +0.5pp（边际递减更极端）。\\n**VLA-only baseline**: seed42=30%, seed43=29%, seed44=**31%**, seed45=**27%**. Mean=**29.3%±1.7%** (n=4). ✅ DONE.\\n**Paired K=10 improvements**: seed42 +5pp (35-30), seed44 +5pp (36-31), seed45 +7pp (34-27). Mean Δ=**+5.7pp** (n=3 paired). seed43 K=10 still running.\\n**Paired K=5 improvements**: seed42 +5pp (35-30), seed43 +3pp (32-29). Mean Δ=+4pp (n=2 paired).\\n**CRM 方差更低**: CRM K=10 std=1.0% vs VLA-only std=1.7%。CRM 在稳定性上也优于 baseline。\\n**Framing**: \\\"consistent cross-benchmark absolute improvement (+5-6pp)\\\" — 不强调 Spatial 相对改进率（19% vs Object 52%），因为 Spatial baseline 更高。\\n**Per-task pattern**: VLA-only 和 CRM 共享同一组 zero-success tasks (4/10)。CRM 改善中等难度 tasks，不修复 impossible tasks。\\n\\n## INVALIDATED Claims (do not use)\\n- ~~K=1 improves frozen VLA~~ — D050/D051: K=1 ACCG fallback 10.0%, multi-scale 10.3%, both ≈ baseline\\n- ~~CRM ranks/selects among K candidates~~ — D058: CRM is correction module, not ranking. Same argmin selection for all modes.\\n- ~~obs_only uses conformal features~~ — D058: uf_input=None for obs_only mode\\n- ~~Cross-VLA positive transfer~~ — D054: OpenVLA near-deterministic at T=0.5. D087: v2 baseline=69%, CRM training done, eval pending\\n- ~~perdof default 0% × 3 seeds~~ — M013: was 2 seeds + 1 misclassified. Corrected to 3 data points (2 full + 1 partial) all 0%.\\n\\n## Pending Evidence (cleaned D069)\\n- ~~K=5 seeds~~ → ✅ DONE, n=7\\n- K=5 argmin decomposition: seed42/43/45 ✅ DONE (13.7%±1.2%, n=3), seed44 running (~1h) → n=4. 结果：selection +2.1pp / correction +2.3pp (与 K=10 不同的分解模式)\\n- Spatial K=10: seed43/44/45 running → cross-benchmark K scaling\\n- ~~Spatial VLA-only baseline~~ → ✅ DONE n=4 (29.3%±1.7%, seed42=30%/43=29%/44=31%/45=27%). Paired Δ=+5.7pp (n=3).\\n- ~~obs_only ε=0.03~~ → ✅ DONE, n=4 (15.75%±0.96%, seed42/44/47/48)\\n- ~~LTO~~ → ✅ DONE (D069 negative)\\n- ~~K=1 CRM eval (plan_702)~~ → ✅ DONE: 10.3%±1.5% (n=3, seed42=12%/43=9%/44=10%, NEGATIVE). Below VLA-only 10.8%. Already in K-value curve.\\n- ~~Random K=5~~ → ✅ DONE n=4 (10.5%±2.9%). Random < VLA-only — multi-sampling harmful at K=5!\\n- OpenVLA CRM eval (plan_802): CRM training done (val_loss=0.077260), eval 待 bjb2-28827 GPU 释放 (standing order P2)\\n- ~~Adaptive K~~ → ✅ P50=15.3% at avg_K=3.8 LOCKED. D090 Plan A eval in progress.\\n- Cross-server reproducibility: argmin K=5 seed42 = 15%(bjb1) vs 13%(bjb2), ±2pp noise floor noted\\n\", \"total_chars\": 26168, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_018mAFx5sAbn1crq5U8GPAEL`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ 2>/dev/null | head -40",
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
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "dfddb1c0-6abb-40e2-9ecb-a037b20936c5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AdvLMx1ZoiwUpgaMFxPyfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17758,
      "cache_read_input_tokens": 32197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17758
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

_source line 18 · 2026-05-21T11:38:50.798Z_

<details><summary>↩ Tool result · `toolu_018mAFx5sAbn1crq5U8GPAEL`</summary>

```text
__pycache__
_project
ablation_eval_commands.md
adaptive_k_design.md
analysis
analysis_magnitude_sweep.py
analysis_object_benchmark.py
analysis_spatial_final.py
argmin_seed44_r2_results.json
batched_inference_feasibility_report.md
benchmark_data_audit.md
benchmark_survey.md
citation_attribution_audit.md
citation_audit_report.md
competitive_analysis_20260515.md
competitor_analysis.md
conclusion_draft.md
contribution_list.md
corl_paper_outline.md
correction_degradation_literature.md
crm-train-v2-k5
crm_bug_audit.md
crm_k1_model.py
diag-eval-v6-batch-failure.md
diag_bjb1_18228.md
diag_bjb2_28827.md
diag_plan_a_spatial_seed42_43.md
diagnose-eval-adaptive-k-spatial-p50-seed44.md
diagnose-norm02-seed44-r2.md
diagnose-random-selection-seed46-r2.md
diagnose_bjb1_18228_failure.md
diagnose_bjb1_32546_batch_failure.md
diagnose_crm_long_seed45.md
diagnose_default_seed46.md
diagnose_failed_evals_20260521.md
diagnose_spatial_k5_seed44_r2.md
diagnosis-eval-obs-only-object-norm003-seed43.md
diagnosis_random_k5_seed44_r2.md
dream_reports
eval-acr-object-v4-obs-only
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "ec9e44fc-3f72-4b0e-801d-47acd967928a",
  "tool_use_result": {
    "stdout": "__pycache__\n_project\nablation_eval_commands.md\nadaptive_k_design.md\nanalysis\nanalysis_magnitude_sweep.py\nanalysis_object_benchmark.py\nanalysis_spatial_final.py\nargmin_seed44_r2_results.json\nbatched_inference_feasibility_report.md\nbenchmark_data_audit.md\nbenchmark_survey.md\ncitation_attribution_audit.md\ncitation_audit_report.md\ncompetitive_analysis_20260515.md\ncompetitor_analysis.md\nconclusion_draft.md\ncontribution_list.md\ncorl_paper_outline.md\ncorrection_degradation_literature.md\ncrm-train-v2-k5\ncrm_bug_audit.md\ncrm_k1_model.py\ndiag-eval-v6-batch-failure.md\ndiag_bjb1_18228.md\ndiag_bjb2_28827.md\ndiag_plan_a_spatial_seed42_43.md\ndiagnose-eval-adaptive-k-spatial-p50-seed44.md\ndiagnose-norm02-seed44-r2.md\ndiagnose-random-selection-seed46-r2.md\ndiagnose_bjb1_18228_failure.md\ndiagnose_bjb1_32546_batch_failure.md\ndiagnose_crm_long_seed45.md\ndiagnose_default_seed46.md\ndiagnose_failed_evals_20260521.md\ndiagnose_spatial_k5_seed44_r2.md\ndiagnosis-eval-obs-only-object-norm003-seed43.md\ndiagnosis_random_k5_seed44_r2.md\ndream_reports\neval-acr-object-v4-obs-only",
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

_source line 19_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "67982c85-5d5d-42bc-9702-135675e3edd7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017ds1XXyvogu6UstJQnER3y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14659,
      "cache_read_input_tokens": 49955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14659
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

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01TwBzmrLC1isr5g9zmuYbdZ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -iE \"outline|cross.vla|pi05|openvla.*section|framing\" 2>/dev/null",
  "description": "Find related outline artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "143c351e-435c-4f21-a243-bf3e89cc3365",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017ds1XXyvogu6UstJQnER3y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14659,
      "cache_read_input_tokens": 49955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14659
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

_source line 21 · 2026-05-21T11:38:57.754Z_

<details><summary>↩ Tool result · `toolu_01TwBzmrLC1isr5g9zmuYbdZ`</summary>

```text
corl_paper_outline.md
eval-pi05-baseline-object-seed42-r2
pi05-r2-analysis.md
pi05_crm_pipeline_plan.md
pi05_eval_deploy_plan.md
pi05_fix3_status_check.md
pi05_vla_only_eval_progress_20260521.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "a99bb507-aedb-4167-b728-712fdb517da9",
  "tool_use_result": {
    "stdout": "corl_paper_outline.md\neval-pi05-baseline-object-seed42-r2\npi05-r2-analysis.md\npi05_crm_pipeline_plan.md\npi05_eval_deploy_plan.md\npi05_fix3_status_check.md\npi05_vla_only_eval_progress_20260521.md",
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

_source line 22_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017GgdJxo3bWV97tWU9pod1Y`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "713774c3-4901-4e40-8b7f-34996da7b2ed",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017ds1XXyvogu6UstJQnER3y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14659,
      "cache_read_input_tokens": 49955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14659
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

_source line 23 · 2026-05-21T11:38:58.198Z_

<details><summary>↩ Tool result · `toolu_017GgdJxo3bWV97tWU9pod1Y`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "e2c8195d-8236-47cd-82ab-1cd4129c3ea3",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "766e608b-9520-405c-b113-0da1ccb5e134",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014dmHrsHYRx6HN2XQBECCP1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3919,
      "cache_read_input_tokens": 64614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3919
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01M3yLbdqUYrYeNWgTUPu3bD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/corl_paper_outline.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "a33cba52-3b7e-454a-91fa-a92a06b71d2b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014dmHrsHYRx6HN2XQBECCP1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3919,
      "cache_read_input_tokens": 64614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3919
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

_source line 26 · 2026-05-21T11:39:03.809Z_

<details><summary>↩ Tool result · `toolu_01M3yLbdqUYrYeNWgTUPu3bD`</summary>

```text
1	# ACR-VLA: CoRL 2026 Paper Outline
2	
3	## Title Candidates
4	
5	1. **ACR-VLA: Inference-Time Action Correction for Vision-Language-Action Models via Sample-Then-Correct**
6	2. **Sample-Then-Correct: Observation-Conditioned Residual Correction Improves VLA Robustness Beyond Sample Selection**
7	3. **Beyond Sample Selection: Learned Action Correction for Frozen Vision-Language-Action Models**
8	
9	Preferred: #2 — 直接点明贡献（sample-then-correct pipeline）+ 核心发现（obs-conditioned > conformal features）。
10	
11	---
12	
13	## Abstract Key Points
14	
15	- **Problem**: Flow-matching VLAs achieve near-saturated performance on standard benchmarks but remain fragile under distribution shift. Existing inference-time methods are limited to sample selection (ReconVLA) or require task-level RL training (SC-VLA).
16	- **Method**: ACR-VLA — a sample-then-correct pipeline: (1) draw K=10 samples from frozen VLA, (2) conformal prediction selects best candidate, (3) lightweight CRM (250K params) applies learned residual correction conditioned on observation features.
17	- **Key finding 1**: Sample-then-correct > sample-then-select. obs_only CRM achieves 19.0% on LIBERO-Object vs 12.0% argmin selection (+7.0pp).
18	- **Key finding 2 (negative result)**: Per-DOF conformal features as CRM input offer no advantage over observation features — perdof CRM 11.0% ≈ argmin 12.0%, while obs_only 19.0%.
19	- **Key finding 3**: Correction magnitude control is critical and previously unrecognized — norm=1.42 yields 0%, norm=0.1-0.2 yields +7pp, obs_only CRM is uniquely robust across the magnitude range.
20	- **Stats**: Fisher exact test p < 0.05 on combined seed=42+43 (200 trials). [pending seed=43 completion]
21	
22	---
23	
24	## 1. Introduction (~1.5 pages)
25	
26	### Motivation
27	- VLAs (π₀, OpenVLA, SmolVLA) represent a paradigm shift in robot learning, but distribution shift remains a major challenge.
28	- LIBERO benchmark exposes robustness gap: VLA performance degrades significantly under object/spatial perturbations.
29	
30	### Gap
31	- **Sample selection** (ReconVLA argmin over K candidates): bounded by candidate quality — when all samples are poor, selection fails.
32	- **RL-based refinement** (SC-VLA): requires per-task RL training, not plug-and-play.
33	- **No prior work** on inference-time learned action correction for frozen VLAs.
34	
35	### Contributions (3 bullet points)
36	1. **Sample-then-correct pipeline**: First system to apply learned residual correction on conformal-selected VLA actions. obs_only CRM improves SmolVLA success rate by +7.0pp on LIBERO-Object over sample selection alone.
37	2. **Systematic conditioning comparison + honest negative result**: Per-DOF conformal statistics — intuitively richer features — provide no CRM benefit. Observation features suffice. This challenges synthetic-experiment intuition and reveals the gap between per-step MSE and closed-loop success.
38	3. **Correction magnitude sensitivity**: First empirical study of correction magnitude control for VLA action refinement. obs_only CRM is robust across norms; perdof CRM collapses at high correction magnitudes.
39	
40	---
41	
42	## 2. Related Work (~1 page)
43	
44	### Categories to cover:
45	
46	| Category | Key papers | Our positioning |
47	|----------|-----------|-----------------|
48	| Vision-Language-Action Models | π₀ (Black et al. 2024), OpenVLA (Kim et al. 2024), SmolVLA (Leal et al. 2025) | We use SmolVLA as frozen backbone; method is backbone-agnostic |
49	| Inference-time scaling for VLAs | ReconVLA (Liang et al. 2025), VLA-Pilot (Zhang et al. 2025) | ReconVLA = selection-only baseline; VLA-Pilot too slow (2.41s/step) |
50	| Residual RL / action correction | SC-VLA (Qu et al. 2025), residual policy learning (Silver et al. 2018, Johannink et al. 2019) | SC-VLA requires task-level RL; our CRM is trained offline on demonstration data |
51	| Conformal prediction in robotics | ReconVLA, conformal prediction for planning (Lindemann et al. 2023) | We use CP for sample selection stage, not for output guarantees |
52	| Test-time compute / inference scaling | Snell et al. 2024, Brown et al. 2024 | Broader context: our work extends inference-time scaling from selection to correction |
53	
54	---
55	
56	## 3. Method (~2 pages)
57	
58	### 3.1 Problem Setup
59	- Frozen VLA backbone (SmolVLA), flow-matching action generation
60	- LIBERO evaluation under distribution shift (spatial perturbation, object substitution)
61	
62	### 3.2 Conformal Sample Selection
63	- Draw K=10 action samples from VLA
64	- Per-DOF conformal prediction: nonconformity scores from calibration set
65	- Argmin selection: pick sample with lowest aggregate nonconformity score
66	- **Figure 1**: Pipeline overview diagram (sample → score → select → correct)
67	
68	### 3.3 Correction Residual Module (CRM)
69	- Architecture: 3-layer MLP, 250K parameters, ~3ms inference overhead
70	- Input variants: (a) per-DOF conformal features, (b) observation features (obs_only), (c) scalar conformal score
71	- Output: residual correction δ added to selected action
72	- Training: MSE loss on demonstration actions, trained on calibration split
73	
74	### 3.4 Correction Magnitude Control
75	- L2 norm clipping of CRM output: ||δ||₂ ≤ norm_max
76	- Why it matters: unconstrained CRM (norm=1.42) → 0% success; norm ∈ [0.1, 0.2] → optimal
77	- obs_only vs perdof: differential sensitivity to norm_max (obs_only robust, perdof collapses)
78	
79	---
80	
81	## 4. Experiments (~2.5 pages)
82	
83	### 4.1 Setup
84	- **Backbone**: SmolVLA (fine-tuned on LIBERO)
85	- **Benchmark**: LIBERO-Spatial (10 tasks), LIBERO-Object (10 tasks)
86	- **Baselines**: VLA-only K=1, VLA-mean K=10, argmin K=10 (≈ ReconVLA selection)
87	- **CRM variants**: perdof, obs_only, scalar, all at norm=0.1
88	- **Evaluation**: 10 rollouts × 10 tasks = 100 trials per method; 2 seeds (42, 43) = 200 trials for significance
89	
90	### 4.2 Main Results
91	
92	**Table 1: Object Benchmark (seed=42, 10-task)**
93	
94	| Method | SR (%) | Δ vs argmin |
95	|--------|--------|-------------|
96	| VLA-only K=1 | 12.0 | — |
97	| VLA-mean K=10 | 12.0 | 0.0 |
98	| argmin K=10 | 12.0 | baseline |
99	| scalar CRM 0.1 | 9.0 | -3.0 |
100	| perdof CRM 0.1 | 11.0 | -1.0 |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "2d018ac2-c5c1-41fe-8b7b-1512e408d887",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/corl_paper_outline.md",
      "content": "# ACR-VLA: CoRL 2026 Paper Outline\n\n## Title Candidates\n\n1. **ACR-VLA: Inference-Time Action Correction for Vision-Language-Action Models via Sample-Then-Correct**\n2. **Sample-Then-Correct: Observation-Conditioned Residual Correction Improves VLA Robustness Beyond Sample Selection**\n3. **Beyond Sample Selection: Learned Action Correction for Frozen Vision-Language-Action Models**\n\nPreferred: #2 — 直接点明贡献（sample-then-correct pipeline）+ 核心发现（obs-conditioned > conformal features）。\n\n---\n\n## Abstract Key Points\n\n- **Problem**: Flow-matching VLAs achieve near-saturated performance on standard benchmarks but remain fragile under distribution shift. Existing inference-time methods are limited to sample selection (ReconVLA) or require task-level RL training (SC-VLA).\n- **Method**: ACR-VLA — a sample-then-correct pipeline: (1) draw K=10 samples from frozen VLA, (2) conformal prediction selects best candidate, (3) lightweight CRM (250K params) applies learned residual correction conditioned on observation features.\n- **Key finding 1**: Sample-then-correct > sample-then-select. obs_only CRM achieves 19.0% on LIBERO-Object vs 12.0% argmin selection (+7.0pp).\n- **Key finding 2 (negative result)**: Per-DOF conformal features as CRM input offer no advantage over observation features — perdof CRM 11.0% ≈ argmin 12.0%, while obs_only 19.0%.\n- **Key finding 3**: Correction magnitude control is critical and previously unrecognized — norm=1.42 yields 0%, norm=0.1-0.2 yields +7pp, obs_only CRM is uniquely robust across the magnitude range.\n- **Stats**: Fisher exact test p < 0.05 on combined seed=42+43 (200 trials). [pending seed=43 completion]\n\n---\n\n## 1. Introduction (~1.5 pages)\n\n### Motivation\n- VLAs (π₀, OpenVLA, SmolVLA) represent a paradigm shift in robot learning, but distribution shift remains a major challenge.\n- LIBERO benchmark exposes robustness gap: VLA performance degrades significantly under object/spatial perturbations.\n\n### Gap\n- **Sample selection** (ReconVLA argmin over K candidates): bounded by candidate quality — when all samples are poor, selection fails.\n- **RL-based refinement** (SC-VLA): requires per-task RL training, not plug-and-play.\n- **No prior work** on inference-time learned action correction for frozen VLAs.\n\n### Contributions (3 bullet points)\n1. **Sample-then-correct pipeline**: First system to apply learned residual correction on conformal-selected VLA actions. obs_only CRM improves SmolVLA success rate by +7.0pp on LIBERO-Object over sample selection alone.\n2. **Systematic conditioning comparison + honest negative result**: Per-DOF conformal statistics — intuitively richer features — provide no CRM benefit. Observation features suffice. This challenges synthetic-experiment intuition and reveals the gap between per-step MSE and closed-loop success.\n3. **Correction magnitude sensitivity**: First empirical study of correction magnitude control for VLA action refinement. obs_only CRM is robust across norms; perdof CRM collapses at high correction magnitudes.\n\n---\n\n## 2. Related Work (~1 page)\n\n### Categories to cover:\n\n| Category | Key papers | Our positioning |\n|----------|-----------|-----------------|\n| Vision-Language-Action Models | π₀ (Black et al. 2024), OpenVLA (Kim et al. 2024), SmolVLA (Leal et al. 2025) | We use SmolVLA as frozen backbone; method is backbone-agnostic |\n| Inference-time scaling for VLAs | ReconVLA (Liang et al. 2025), VLA-Pilot (Zhang et al. 2025) | ReconVLA = selection-only baseline; VLA-Pilot too slow (2.41s/step) |\n| Residual RL / action correction | SC-VLA (Qu et al. 2025), residual policy learning (Silver et al. 2018, Johannink et al. 2019) | SC-VLA requires task-level RL; our CRM is trained offline on demonstration data |\n| Conformal prediction in robotics | ReconVLA, conformal prediction for planning (Lindemann et al. 2023) | We use CP for sample selection stage, not for output guarantees |\n| Test-time compute / inference scaling | Snell et al. 2024, Brown et al. 2024 | Broader context: our work extends inference-time scaling from selection to correction |\n\n---\n\n## 3. Method (~2 pages)\n\n### 3.1 Problem Setup\n- Frozen VLA backbone (SmolVLA), flow-matching action generation\n- LIBERO evaluation under distribution shift (spatial perturbation, object substitution)\n\n### 3.2 Conformal Sample Selection\n- Draw K=10 action samples from VLA\n- Per-DOF conformal prediction: nonconformity scores from calibration set\n- Argmin selection: pick sample with lowest aggregate nonconformity score\n- **Figure 1**: Pipeline overview diagram (sample → score → select → correct)\n\n### 3.3 Correction Residual Module (CRM)\n- Architecture: 3-layer MLP, 250K parameters, ~3ms inference overhead\n- Input variants: (a) per-DOF conformal features, (b) observation features (obs_only), (c) scalar conformal score\n- Output: residual correction δ added to selected action\n- Training: MSE loss on demonstration actions, trained on calibration split\n\n### 3.4 Correction Magnitude Control\n- L2 norm clipping of CRM output: ||δ||₂ ≤ norm_max\n- Why it matters: unconstrained CRM (norm=1.42) → 0% success; norm ∈ [0.1, 0.2] → optimal\n- obs_only vs perdof: differential sensitivity to norm_max (obs_only robust, perdof collapses)\n\n---\n\n## 4. Experiments (~2.5 pages)\n\n### 4.1 Setup\n- **Backbone**: SmolVLA (fine-tuned on LIBERO)\n- **Benchmark**: LIBERO-Spatial (10 tasks), LIBERO-Object (10 tasks)\n- **Baselines**: VLA-only K=1, VLA-mean K=10, argmin K=10 (≈ ReconVLA selection)\n- **CRM variants**: perdof, obs_only, scalar, all at norm=0.1\n- **Evaluation**: 10 rollouts × 10 tasks = 100 trials per method; 2 seeds (42, 43) = 200 trials for significance\n\n### 4.2 Main Results\n\n**Table 1: Object Benchmark (seed=42, 10-task)**\n\n| Method | SR (%) | Δ vs argmin |\n|--------|--------|-------------|\n| VLA-only K=1 | 12.0 | — |\n| VLA-mean K=10 | 12.0 | 0.0 |\n| argmin K=10 | 12.0 | baseline |\n| scalar CRM 0.1 | 9.0 | -3.0 |\n| perdof CRM 0.1 | 11.0 | -1.0 |",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 209
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01Q561V9wVL2qcabuAZMAXCi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_crm_pipeline_plan.md",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "f7be28fd-f631-4e01-8b4d-8e8839904dca",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014dmHrsHYRx6HN2XQBECCP1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3919,
      "cache_read_input_tokens": 64614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3919
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

_source line 28 · 2026-05-21T11:39:04.819Z_

<details><summary>↩ Tool result · `toolu_01Q561V9wVL2qcabuAZMAXCi`</summary>

```text
1	# π0.5 CRM Pipeline 方案 (2026-05-21, updated)
2	
3	## 0. 当前阻塞状态
4	
5	### Baseline Eval 全线 0% SR
6	
7	6 个 baseline 实验（3 seeds × Object + Spatial）全部失败：
8	
9	| 实验 | SR | 状态 |
10	|------|-----|------|
11	| Object seed42/43/44 | 0.0% (0/200 each) | 完成，EXIT_CODE=0 |
12	| Spatial seed42/43/44 | 0.0% (前 8 task) | 中途死亡（task 9, rollout 10/20） |
13	
14	**根因进化**：不再是之前的 vision tower 单一问题，而是**双重 key mismatch**：
15	- Vision tower: 437 keys 已成功 remap (`vision_tower.vision_model.` → `vision_tower.`) ✅
16	- Language model + multi_modal_projector: **376 keys 仍 missing** ❌
17	  - `model.paligemma_with_expert.paligemma.model.language_model.*`
18	  - `model.paligemma_with_expert.paligemma.model.multi_modal_projector.*`
19	- 结果：vision tower 有真实权重，但 **language model 在随机权重下运行** → 0% SR
20	- 附加症状：gripper 恒定 ~0.98（始终 open），无法执行 pick
21	
22	**官方 lerobot-eval patched 版本 3/3 = 100% SR**，证明模型本身有效。
23	
24	### 阻塞解除条件
25	在 `_fix_pytorch_state_dict_keys`（或 `pi05_wrapper.py` 的 `_fix_vision_tower_keys`）中追加 language_model + multi_modal_projector 的 key remap，使 load_state_dict missing_keys = 0。验证方式：至少 1 个 task SR > 0%。
26	
27	---
28	
29	## 1. 现状摘要
30	
31	### SmolVLA 现有 pipeline（LOCKED）
32	- `SmolVLAWrapper` (`src/smolvla_wrapper.py`)
33	  - `encode_prefix(...)` → `obs_features (B, 960)`, `kv_cache`, `prefix_pad_masks`
34	  - `generate_k_samples(kv, masks, K)` → `(B, K, chunk_size=50, FULL_ACTION_DIM=7)`
35	  - `preprocess_obs_batch` 已支持 batched precompute
36	- `MultiScaleCRM` (`src/crm_k1_model.py`)
37	  - 输入: `base_action (B, 30)` + `multi_scale_obs (B, 4, 960)` 或 fallback `(B, 960)`
38	  - 参数: `action_dim=30`, `obs_dim=960`, `hidden_dim=256`, `bottleneck_dim=192`
39	  - ~323K params
40	- `MultiScaleFeatureExtractor`
41	  - hooks on `text_model.layers[i].input_layernorm` (i ∈ [3,7,11,15])
42	  - 最后一层 hook 在 `text_model.norm`
43	- 训练 (`src/train_crm_k1.py`)
44	  - Phase 1 `--precompute`: SmolVLA + MultiScaleExtractor → cache `(multi_scale_obs, obs_features, vla_action, expert_action)`
45	  - Phase 2: 多损失训练 (L2 + direction + triplet + magnitude)
46	
47	### π0.5 现状
48	- `pi05_wrapper.py` 存在：
49	  - `obs_features` shape `[1, 2048]`, range `[-12.82, 19.99]`
50	  - K-sample 输出 `[B, K, 50, 7]`，action_dim=7（同 SmolVLA）
51	  - `_fix_vision_tower_keys` 修复 437 个 key，但 **376 个 language_model/projector key 未修复**
52	- `evaluate.py` 内有 `obs_proj = nn.Linear(2048, 960)`（random init，无用）
53	
54	---
55	
56	## 2. 设计决策
57	
58	### 决策 A：CRM obs_dim = 2048（采用）
59	- 不复用 SmolVLA CRM 权重
60	- 直接训一个 obs_dim=2048 的 MultiScaleCRM（架构相同，只改 obs_dim 参数）
61	- 优点：无信息损失；obs_dim 改变只影响 `layer_proj` 一层（960×192 → 2048×192）
62	- 缺点：需重新跑 precompute
63	
64	### 决策 D：第一版只用 fallback 单 obs feature
65	- π0.5 backbone 是 PaliGemma (Gemma-based, 18-layer)，层索引与 SmolVLA (16-layer LLaMA) 不同
66	- 避免对 π0.5 内部结构的依赖，便于调试
67	- SmolVLA 上 multi-scale vs single 提升约 +1pp，幅度有限
68	- 若效果不够好再增量加 multi-scale
69	
70	### 决策 E/F：沿用 H_EFF=5, CORRECTION_DIM=6
71	- 与 SmolVLA 对齐，便于横向比较
72	- CRM 只修前 5 步 pose，不修 gripper
73	
74	---
75	
76	## 3. 需要修改/新增的文件清单
77	
78	| 文件 | 修改类型 | 说明 |
79	|------|---------|------|
80	| `src/pi05_wrapper.py` | **修复 + 新增 API** | (1) 追加 376 key remap（language_model + multi_modal_projector）；(2) 增加 `preprocess_obs_batch`（批量预处理） |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "f7cb247a-ebad-4730-9b5d-52b8d933b9f4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_crm_pipeline_plan.md",
      "content": "# π0.5 CRM Pipeline 方案 (2026-05-21, updated)\n\n## 0. 当前阻塞状态\n\n### Baseline Eval 全线 0% SR\n\n6 个 baseline 实验（3 seeds × Object + Spatial）全部失败：\n\n| 实验 | SR | 状态 |\n|------|-----|------|\n| Object seed42/43/44 | 0.0% (0/200 each) | 完成，EXIT_CODE=0 |\n| Spatial seed42/43/44 | 0.0% (前 8 task) | 中途死亡（task 9, rollout 10/20） |\n\n**根因进化**：不再是之前的 vision tower 单一问题，而是**双重 key mismatch**：\n- Vision tower: 437 keys 已成功 remap (`vision_tower.vision_model.` → `vision_tower.`) ✅\n- Language model + multi_modal_projector: **376 keys 仍 missing** ❌\n  - `model.paligemma_with_expert.paligemma.model.language_model.*`\n  - `model.paligemma_with_expert.paligemma.model.multi_modal_projector.*`\n- 结果：vision tower 有真实权重，但 **language model 在随机权重下运行** → 0% SR\n- 附加症状：gripper 恒定 ~0.98（始终 open），无法执行 pick\n\n**官方 lerobot-eval patched 版本 3/3 = 100% SR**，证明模型本身有效。\n\n### 阻塞解除条件\n在 `_fix_pytorch_state_dict_keys`（或 `pi05_wrapper.py` 的 `_fix_vision_tower_keys`）中追加 language_model + multi_modal_projector 的 key remap，使 load_state_dict missing_keys = 0。验证方式：至少 1 个 task SR > 0%。\n\n---\n\n## 1. 现状摘要\n\n### SmolVLA 现有 pipeline（LOCKED）\n- `SmolVLAWrapper` (`src/smolvla_wrapper.py`)\n  - `encode_prefix(...)` → `obs_features (B, 960)`, `kv_cache`, `prefix_pad_masks`\n  - `generate_k_samples(kv, masks, K)` → `(B, K, chunk_size=50, FULL_ACTION_DIM=7)`\n  - `preprocess_obs_batch` 已支持 batched precompute\n- `MultiScaleCRM` (`src/crm_k1_model.py`)\n  - 输入: `base_action (B, 30)` + `multi_scale_obs (B, 4, 960)` 或 fallback `(B, 960)`\n  - 参数: `action_dim=30`, `obs_dim=960`, `hidden_dim=256`, `bottleneck_dim=192`\n  - ~323K params\n- `MultiScaleFeatureExtractor`\n  - hooks on `text_model.layers[i].input_layernorm` (i ∈ [3,7,11,15])\n  - 最后一层 hook 在 `text_model.norm`\n- 训练 (`src/train_crm_k1.py`)\n  - Phase 1 `--precompute`: SmolVLA + MultiScaleExtractor → cache `(multi_scale_obs, obs_features, vla_action, expert_action)`\n  - Phase 2: 多损失训练 (L2 + direction + triplet + magnitude)\n\n### π0.5 现状\n- `pi05_wrapper.py` 存在：\n  - `obs_features` shape `[1, 2048]`, range `[-12.82, 19.99]`\n  - K-sample 输出 `[B, K, 50, 7]`，action_dim=7（同 SmolVLA）\n  - `_fix_vision_tower_keys` 修复 437 个 key，但 **376 个 language_model/projector key 未修复**\n- `evaluate.py` 内有 `obs_proj = nn.Linear(2048, 960)`（random init，无用）\n\n---\n\n## 2. 设计决策\n\n### 决策 A：CRM obs_dim = 2048（采用）\n- 不复用 SmolVLA CRM 权重\n- 直接训一个 obs_dim=2048 的 MultiScaleCRM（架构相同，只改 obs_dim 参数）\n- 优点：无信息损失；obs_dim 改变只影响 `layer_proj` 一层（960×192 → 2048×192）\n- 缺点：需重新跑 precompute\n\n### 决策 D：第一版只用 fallback 单 obs feature\n- π0.5 backbone 是 PaliGemma (Gemma-based, 18-layer)，层索引与 SmolVLA (16-layer LLaMA) 不同\n- 避免对 π0.5 内部结构的依赖，便于调试\n- SmolVLA 上 multi-scale vs single 提升约 +1pp，幅度有限\n- 若效果不够好再增量加 multi-scale\n\n### 决策 E/F：沿用 H_EFF=5, CORRECTION_DIM=6\n- 与 SmolVLA 对齐，便于横向比较\n- CRM 只修前 5 步 pose，不修 gripper\n\n---\n\n## 3. 需要修改/新增的文件清单\n\n| 文件 | 修改类型 | 说明 |\n|------|---------|------|\n| `src/pi05_wrapper.py` | **修复 + 新增 API** | (1) 追加 376 key remap（language_model + multi_modal_projector）；(2) 增加 `preprocess_obs_batch`（批量预处理） |",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 234
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "a9b9ff38-5ee4-4ff8-8c17-0c7941424eeb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017TtpEFDWnjuGhqBTE5c2rv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5385,
      "cache_read_input_tokens": 68533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5385
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VjCGKs5neHjr4LdK97u2XP`</summary>

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
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "cbe95f72-18cb-49cc-9d8d-afb12762e7ed",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017TtpEFDWnjuGhqBTE5c2rv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5385,
      "cache_read_input_tokens": 68533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5385
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 31 · 2026-05-21T11:39:15.488Z_

<details><summary>↩ Tool result · `toolu_01VjCGKs5neHjr4LdK97u2XP`</summary>

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
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "f5e3ecca-8f95-44ee-863e-a814e7af4f27",
  "tool_use_result": {
    "matches": [],
    "query": "register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "ffbc9ae8-b1c2-48e8-82d7-98f5f2744f57",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WNLkCmzuFzPx1xRfQNuhNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 73918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 646
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 33_

<details open><summary>🔧 Tool call — Write · `toolu_01VA3vWdJVUytLL7W4wk1z1S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_cross_vla_outline.md",
  "content": "# §4.X Cross-VLA Generalization — Section Outline\n\n> Drafted 2026-05-21 | Paper: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\" | Target: CoRL 2026\n> Status: π0.5 numbers [PENDING] — full baseline eval deploying on bjb1-32546 (3 seeds × Object + Spatial); CRM training/eval not yet started.\n\n---\n\n## Section role in paper\n\nThis section answers **R5 (single-backbone)** and tests **C3 (applicability boundaries)** with a third VLA architecture at an intermediate scale. With SmolVLA (0.4B, flow-matching) carrying the main analysis and OpenVLA (7B, tokenized) anchoring the determinism boundary, π0.5 (3.6B, flow-matching) probes whether CRM remains useful when the frozen backbone is already strong.\n\nThe section is **not** a hero result — it is a generalization test framed honestly: scale up the backbone by ~9× and re-run the same plug-and-play pipeline. The expected outcome is a modest absolute gain ceiling tied to backbone saturation, contrasted with SmolVLA's larger headroom. This pattern, combined with the OpenVLA failure mode, makes the boundary argument concrete: CRM gains are gated by (i) stochastic candidate diversity and (ii) un-saturated baseline SR.\n\n---\n\n## Proposed structure\n\n### 4.X.1  Setup: three backbones on a shared pipeline\n\nThree frozen VLAs differ along two axes that the analysis predicts matter — action-head stochasticity and baseline saturation:\n\n| Backbone | Size | Action head | Stochastic at T=eval? | Baseline LIBERO-Object SR |\n|---|---|---|---|---|\n| SmolVLA | 0.4B | Flow-matching | Yes (naturally diverse across K) | 10.8 % ± 1.3 % (n=9) |\n| π0.5 | 3.6B | Flow-matching | Yes (assumed; quick verify 50 trials) | 72 % (quick verify, 10/10 non-zero; full SR [PENDING]) |\n| OpenVLA-v2 | 7B | Discretized tokens (T=0.5) | No (8/10 identical actions; per-DOF σ² < 1e-30 on 5/7 DOFs) | 69 % (D093 LOCKED) |\n\nPipeline held constant across backbones: K candidates from the frozen VLA → argmin-to-centroid selection → obs-only CRM residual (||δ||₂ ≤ 0.2) → action executed. The only backbone-specific change is the CRM input dim (SmolVLA 960, π0.5 2048, OpenVLA 4096); architecture and training recipe are identical. CRM is trained on per-backbone VLA-rollout caches over the same 20 LIBERO tasks (Object + Spatial). Each cell reports mean ± std over 3 seeds × 50 rollouts/task × 10 tasks unless stated.\n\n### 4.X.2  Cross-VLA results (Table X) — anchor on Δ over backbone-matched baseline\n\nThe fair comparison is **Δ within each backbone**, not absolute SR across backbones (different action spaces, different fine-tuning, different baseline saturation).\n\n**Table X — Cross-VLA Generalization (LIBERO-Object, K=2 Plan A)**\n\n| Backbone | VLA-only baseline | + CRM (Plan A K=2) | Δ (abs / rel) | Stochastic? | Notes |\n|---|---|---|---|---|---|\n| SmolVLA 0.4B | 10.8 % ± 1.3 % (n=9) | **18.3 % ± 2.1 %** (n=≥3) | **+7.5 pp / +69 %** | yes | Main result, LOCKED |\n| π0.5 3.6B | [PENDING n=3] | [PENDING n=3] | [PENDING] | yes | Quick verify 72 %; CRM pipeline ETA ≤72 h |\n| OpenVLA 7B | 69 % | 0 % (CRM collapses) | **−69 pp** | **no** | D093 LOCKED — boundary case |\n\n**LIBERO-Spatial** (held-in, secondary):\n\n| Backbone | VLA-only | + CRM (Plan A K=2) | Δ |\n|---|---|---|---|\n| SmolVLA 0.4B | 29.4 % ± 1.5 % | **35.0 % ± 1.0 %** | **+5.6 pp / +19 %** |\n| π0.5 3.6B | [PENDING] | [PENDING] | [PENDING] |\n| OpenVLA 7B | [not run — out of scope after D093] | — | — |\n\n*Numbers in bold are LOCKED; [PENDING] cells will be filled once the bjb1-32546 deployment completes and the CRM precompute → projection (2048→960) → eval pipeline finishes (~10–15 GPU-h after baseline harvest).*\n\n### 4.X.3  Result narrative (to be finalized after π0.5 numbers land)\n\nThree pre-registered prediction paths, written before π0.5 numbers are in, so the reader can audit which one realized:\n\n- **P1 — Modest gain (Δ ∈ [+1, +4] pp):** consistent with diminishing returns: a 72 % baseline leaves ~28 pp of headroom, and CRM operates within a bounded correction radius (Sec. 4.2 magnitude analysis) that does not scale with backbone capacity. Reports as \"CRM generalizes to a 9× larger backbone with reduced but positive absolute gain — relative improvement attenuates as baseline saturates.\"\n- **P2 — Neutral (Δ ∈ [−1, +1] pp, p > 0.1):** consistent with the OpenVLA boundary partially generalizing: π0.5 candidates may be too tightly clustered for argmin-to-centroid to expose a meaningful correction target. Reports as \"the determinism axis matters more than the scale axis; once K-sample diversity is low, CRM's correction signal vanishes regardless of architecture.\"\n- **P3 — Negative (Δ < −1 pp):** consistent with C3 task-shift mode: CRM trained on per-backbone caches may carry π0.5-specific biases that fight π0.5's already-competent policy. Reports as \"high-capacity stochastic backbones can be actively harmed by post-hoc residual correction — a sharpening of the C3 boundary.\"\n\nThe section commits to reporting whichever outcome materializes, including per-task breakdowns (especially if Δ is driven by a small subset, as on LIBERO-Long).\n\n### 4.X.4  Applicability boundary: when does CRM help?\n\nTwo prerequisites, stated as a falsifiable rule and supported by the cross-VLA evidence:\n\n> **CRM helps iff (i) the backbone produces ≥ ε action diversity across K samples at deployment temperature, AND (ii) the baseline SR has ≥ Δ_min headroom on the target distribution.**\n\n- **(i) Stochasticity prerequisite — OpenVLA case.** OpenVLA at T=0.5 yields 8/10 identical action chunks (per-DOF variance < 1e-30 on 5 of 7 DOFs). Argmin-to-centroid degenerates (all K candidates collapse to one point), the CRM input is therefore out-of-distribution relative to its training cache, and the residual points off-manifold — the same input-shift failure mode documented at K=1 for SmolVLA (10.3 % < 10.8 % baseline). The result is not a tuning failure; it is the prerequisite (i) being violated.\n- **(ii) Headroom prerequisite — π0.5 (preliminary) and SmolVLA.** SmolVLA's +7.5 pp / +69 % Object gain is supported by a 10.8 % baseline with ~89 pp of unrealized success. π0.5's quick-verify 72 % baseline limits the absolute Δ_max recoverable by any bounded-magnitude residual. The section reports both absolute and relative Δ, and explicitly states that a +2–4 pp gain on a 72 % baseline is a **different kind of evidence** than a +7.5 pp gain on an 11 % baseline — it tests whether the correction direction is correct on a competent policy, not whether the policy is rescued from near-failure.\n\nThese two prerequisites unify the cross-VLA table into a single rule rather than three separate stories. The OpenVLA collapse is a confirmed boundary (D093 LOCKED, n=3 seeds × 10 trials/task), not a method failure to be hidden — it is the most informative data point for delineating where CRM applies.\n\n### 4.X.5  Honest discussion (paragraph-level, not glossed)\n\nThree points the section must say out loud, not bury in supplementary:\n\n1. **Diminishing returns are expected and reported.** At a 72 % baseline, even a perfect oracle has a ceiling of +28 pp. Any +X pp on π0.5 should be read against that ceiling, not against SmolVLA's +7.5 pp. We report Δ_abs, Δ_rel, and the fraction of remaining headroom recovered (Δ_abs / (100 − baseline)).\n2. **Cross-VLA is generalization evidence, not a SOTA claim.** The contribution is the analysis (C1 correction > selection; C2 conditioning–magnitude interaction; C3 boundaries). The cross-VLA table tests whether C1–C3 predict outcomes on backbones the analysis was not built on. π0.5 results are framed as a falsification test of C3, not as a benchmark race.\n3. **The boundary is the result.** A method that works on SmolVLA, attenuates on π0.5, and collapses on OpenVLA is more useful to the community than one claimed to work universally — it tells practitioners which deployment settings to expect a gain in. The section will close on this framing, explicitly aligned with the C3 boundary argument from §4.4.\n\n---\n\n## Provenance / evidence anchors (for paper_provenance.yaml)\n\n| Cell | exp_id(s) | Status |\n|---|---|---|\n| SmolVLA Object baseline 10.8 % | aggregate of `eval-vla-only-object-seed{42..50}` | LOCKED |\n| SmolVLA Object Plan A 18.3 % | `eval-plan-a-object-seed{42,43,44}` | LOCKED (D094) |\n| SmolVLA Spatial baseline 29.4 % | `eval-vla-only-spatial-seed{42..45}` | LOCKED |\n| SmolVLA Spatial Plan A 35.0 % | `eval-plan-a-spatial-seed{42,43,44}` | LOCKED (D094) |\n| OpenVLA baseline 69 % | OpenVLA-v2 eval, 10 trials × 10 tasks | LOCKED (D087/D093) |\n| OpenVLA CRM 0 % | OpenVLA CRM eval (D093) | LOCKED |\n| π0.5 baseline quick verify 72 % | `eval-pi05-baseline-object-seed42-r2` (50 rollouts, 10/10 tasks non-zero) | LOCKED quick-verify only |\n| π0.5 baseline full eval | bjb1-32546 deployment, 3 seeds × Object + Spatial | **PENDING** |\n| π0.5 + CRM Plan A | not yet trained (CRM projection 2048→960 ~10–15 GPU-h after baseline harvest) | **PENDING** |\n\nEvery numeric cell in the section will trace back to a registry exp_id before submission (per memory.md M013 lesson: no abstract labels in provenance).\n\n---\n\n## Writing checklist (apply during drafting)\n\n- [ ] Every number in the section traces to a concrete `eval-*` exp_id.\n- [ ] Δ reported in both pp and % relative; headroom fraction Δ / (100 − baseline) given for π0.5.\n- [ ] OpenVLA 0 % discussed as **boundary evidence**, not as a method bug to apologize for.\n- [ ] π0.5 result (whichever of P1/P2/P3 materializes) reported without re-framing post-hoc; per-task breakdown included if Δ < +3 pp.\n- [ ] No cherry-picking: if any seed is excluded, exclusion criterion is named *before* numbers are quoted (cf. D084 seed42 exclusion).\n- [ ] Cross-VLA comparison emphasizes within-backbone Δ; absolute-SR cross-backbone is shown only as a footnote with the caveat that action spaces and fine-tuning regimes differ.\n- [ ] Section ends on the unified prerequisite rule (stochasticity + headroom), tying back to C3.\n\n## Open questions / blockers\n\n- **π0.5 full baseline** ETA: pending bjb1-32546 6-GPU job. Acceptance criterion before harvest: 3 seeds × Object + Spatial all > 60 % SR (consistent with quick-verify 72 %).\n- **π0.5 CRM training**: requires obs cache (2048-dim) precompute + projection layer training (2048→960 reuses SmolVLA CRM head) OR fresh CRM with obs_dim=2048. Decision A in `pi05_crm_pipeline_plan.md` chooses obs_dim=2048; the section assumes that path.\n- **Statistical test**: with n=3 seeds × 10 tasks × 50 rollouts/task = 1500 trials per cell, paired Welch t-test on per-task SR is the planned default; Mann–Whitney U as robustness check.\n- **Latency parity**: confirm π0.5 K=2 batched latency ≤ 1.5× K=1 (SmolVLA achieves K-invariant batched inference; π0.5 yet to be profiled).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "750257c1-a6b0-4c58-9cb9-28ab30cd5da2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WNLkCmzuFzPx1xRfQNuhNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 73918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 646
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 34 · 2026-05-21T11:40:36.739Z_

<details><summary>↩ Tool result · `toolu_01VA3vWdJVUytLL7W4wk1z1S`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_cross_vla_outline.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c7967c0-b9a1-4eb6-84e5-6c7cb265238f",
  "uuid": "3a83dc3f-41cf-464d-9ada-96800d5896a6",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_cross_vla_outline.md",
    "content": "# §4.X Cross-VLA Generalization — Section Outline\n\n> Drafted 2026-05-21 | Paper: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\" | Target: CoRL 2026\n> Status: π0.5 numbers [PENDING] — full baseline eval deploying on bjb1-32546 (3 seeds × Object + Spatial); CRM training/eval not yet started.\n\n---\n\n## Section role in paper\n\nThis section answers **R5 (single-backbone)** and tests **C3 (applicability boundaries)** with a third VLA architecture at an intermediate scale. With SmolVLA (0.4B, flow-matching) carrying the main analysis and OpenVLA (7B, tokenized) anchoring the determinism boundary, π0.5 (3.6B, flow-matching) probes whether CRM remains useful when the frozen backbone is already strong.\n\nThe section is **not** a hero result — it is a generalization test framed honestly: scale up the backbone by ~9× and re-run the same plug-and-play pipeline. The expected outcome is a modest absolute gain ceiling tied to backbone saturation, contrasted with SmolVLA's larger headroom. This pattern, combined with the OpenVLA failure mode, makes the boundary argument concrete: CRM gains are gated by (i) stochastic candidate diversity and (ii) un-saturated baseline SR.\n\n---\n\n## Proposed structure\n\n### 4.X.1  Setup: three backbones on a shared pipeline\n\nThree frozen VLAs differ along two axes that the analysis predicts matter — action-head stochasticity and baseline saturation:\n\n| Backbone | Size | Action head | Stochastic at T=eval? | Baseline LIBERO-Object SR |\n|---|---|---|---|---|\n| SmolVLA | 0.4B | Flow-matching | Yes (naturally diverse across K) | 10.8 % ± 1.3 % (n=9) |\n| π0.5 | 3.6B | Flow-matching | Yes (assumed; quick verify 50 trials) | 72 % (quick verify, 10/10 non-zero; full SR [PENDING]) |\n| OpenVLA-v2 | 7B | Discretized tokens (T=0.5) | No (8/10 identical actions; per-DOF σ² < 1e-30 on 5/7 DOFs) | 69 % (D093 LOCKED) |\n\nPipeline held constant across backbones: K candidates from the frozen VLA → argmin-to-centroid selection → obs-only CRM residual (||δ||₂ ≤ 0.2) → action executed. The only backbone-specific change is the CRM input dim (SmolVLA 960, π0.5 2048, OpenVLA 4096); architecture and training recipe are identical. CRM is trained on per-backbone VLA-rollout caches over the same 20 LIBERO tasks (Object + Spatial). Each cell reports mean ± std over 3 seeds × 50 rollouts/task × 10 tasks unless stated.\n\n### 4.X.2  Cross-VLA results (Table X) — anchor on Δ over backbone-matched baseline\n\nThe fair comparison is **Δ within each backbone**, not absolute SR across backbones (different action spaces, different fine-tuning, different baseline saturation).\n\n**Table X — Cross-VLA Generalization (LIBERO-Object, K=2 Plan A)**\n\n| Backbone | VLA-only baseline | + CRM (Plan A K=2) | Δ (abs / rel) | Stochastic? | Notes |\n|---|---|---|---|---|---|\n| SmolVLA 0.4B | 10.8 % ± 1.3 % (n=9) | **18.3 % ± 2.1 %** (n=≥3) | **+7.5 pp / +69 %** | yes | Main result, LOCKED |\n| π0.5 3.6B | [PENDING n=3] | [PENDING n=3] | [PENDING] | yes | Quick verify 72 %; CRM pipeline ETA ≤72 h |\n| OpenVLA 7B | 69 % | 0 % (CRM collapses) | **−69 pp** | **no** | D093 LOCKED — boundary case |\n\n**LIBERO-Spatial** (held-in, secondary):\n\n| Backbone | VLA-only | + CRM (Plan A K=2) | Δ |\n|---|---|---|---|\n| SmolVLA 0.4B | 29.4 % ± 1.5 % | **35.0 % ± 1.0 %** | **+5.6 pp / +19 %** |\n| π0.5 3.6B | [PENDING] | [PENDING] | [PENDING] |\n| OpenVLA 7B | [not run — out of scope after D093] | — | — |\n\n*Numbers in bold are LOCKED; [PENDING] cells will be filled once the bjb1-32546 deployment completes and the CRM precompute → projection (2048→960) → eval pipeline finishes (~10–15 GPU-h after baseline harvest).*\n\n### 4.X.3  Result narrative (to be finalized after π0.5 numbers land)\n\nThree pre-registered prediction paths, written before π0.5 numbers are in, so the reader can audit which one realized:\n\n- **P1 — Modest gain (Δ ∈ [+1, +4] pp):** consistent with diminishing returns: a 72 % baseline leaves ~28 pp of headroom, and CRM operates within a bounded correction radius (Sec. 4.2 magnitude analysis) that does not scale with backbone capacity. Reports as \"CRM generalizes to a 9× larger backbone with reduced but positive absolute gain — relative improvement attenuates as baseline saturates.\"\n- **P2 — Neutral (Δ ∈ [−1, +1] pp, p > 0.1):** consistent with the OpenVLA boundary partially generalizing: π0.5 candidates may be too tightly clustered for argmin-to-centroid to expose a meaningful correction target. Reports as \"the determinism axis matters more than the scale axis; once K-sample diversity is low, CRM's correction signal vanishes regardless of architecture.\"\n- **P3 — Negative (Δ < −1 pp):** consistent with C3 task-shift mode: CRM trained on per-backbone caches may carry π0.5-specific biases that fight π0.5's already-competent policy. Reports as \"high-capacity stochastic backbones can be actively harmed by post-hoc residual correction — a sharpening of the C3 boundary.\"\n\nThe section commits to reporting whichever outcome materializes, including per-task breakdowns (especially if Δ is driven by a small subset, as on LIBERO-Long).\n\n### 4.X.4  Applicability boundary: when does CRM help?\n\nTwo prerequisites, stated as a falsifiable rule and supported by the cross-VLA evidence:\n\n> **CRM helps iff (i) the backbone produces ≥ ε action diversity across K samples at deployment temperature, AND (ii) the baseline SR has ≥ Δ_min headroom on the target distribution.**\n\n- **(i) Stochasticity prerequisite — OpenVLA case.** OpenVLA at T=0.5 yields 8/10 identical action chunks (per-DOF variance < 1e-30 on 5 of 7 DOFs). Argmin-to-centroid degenerates (all K candidates collapse to one point), the CRM input is therefore out-of-distribution relative to its training cache, and the residual points off-manifold — the same input-shift failure mode documented at K=1 for SmolVLA (10.3 % < 10.8 % baseline). The result is not a tuning failure; it is the prerequisite (i) being violated.\n- **(ii) Headroom prerequisite — π0.5 (preliminary) and SmolVLA.** SmolVLA's +7.5 pp / +69 % Object gain is supported by a 10.8 % baseline with ~89 pp of unrealized success. π0.5's quick-verify 72 % baseline limits the absolute Δ_max recoverable by any bounded-magnitude residual. The section reports both absolute and relative Δ, and explicitly states that a +2–4 pp gain on a 72 % baseline is a **different kind of evidence** than a +7.5 pp gain on an 11 % baseline — it tests whether the correction direction is correct on a competent policy, not whether the policy is rescued from near-failure.\n\nThese two prerequisites unify the cross-VLA table into a single rule rather than three separate stories. The OpenVLA collapse is a confirmed boundary (D093 LOCKED, n=3 seeds × 10 trials/task), not a method failure to be hidden — it is the most informative data point for delineating where CRM applies.\n\n### 4.X.5  Honest discussion (paragraph-level, not glossed)\n\nThree points the section must say out loud, not bury in supplementary:\n\n1. **Diminishing returns are expected and reported.** At a 72 % baseline, even a perfect oracle has a ceiling of +28 pp. Any +X pp on π0.5 should be read against that ceiling, not against SmolVLA's +7.5 pp. We report Δ_abs, Δ_rel, and the fraction of remaining headroom recovered (Δ_abs / (100 − baseline)).\n2. **Cross-VLA is generalization evidence, not a SOTA claim.** The contribution is the analysis (C1 correction > selection; C2 conditioning–magnitude interaction; C3 boundaries). The cross-VLA table tests whether C1–C3 predict outcomes on backbones the analysis was not built on. π0.5 results are framed as a falsification test of C3, not as a benchmark race.\n3. **The boundary is the result.** A method that works on SmolVLA, attenuates on π0.5, and collapses on OpenVLA is more useful to the community than one claimed to work universally — it tells practitioners which deployment settings to expect a gain in. The section will close on this framing, explicitly aligned with the C3 boundary argument from §4.4.\n\n---\n\n## Provenance / evidence anchors (for paper_provenance.yaml)\n\n| Cell | exp_id(s) | Status |\n|---|---|---|\n| SmolVLA Object baseline 10.8 % | aggregate of `eval-vla-only-object-seed{42..50}` | LOCKED |\n| SmolVLA Object Plan A 18.3 % | `eval-plan-a-object-seed{42,43,44}` | LOCKED (D094) |\n| SmolVLA Spatial baseline 29.4 % | `eval-vla-only-spatial-seed{42..45}` | LOCKED |\n| SmolVLA Spatial Plan A 35.0 % | `eval-plan-a-spatial-seed{42,43,44}` | LOCKED (D094) |\n| OpenVLA baseline 69 % | OpenVLA-v2 eval, 10 trials × 10 tasks | LOCKED (D087/D093) |\n| OpenVLA CRM 0 % | OpenVLA CRM eval (D093) | LOCKED |\n| π0.5 baseline quick verify 72 % | `eval-pi05-baseline-object-seed42-r2` (50 rollouts, 10/10 tasks non-zero) | LOCKED quick-verify only |\n| π0.5 baseline full eval | bjb1-32546 deployment, 3 seeds × Object + Spatial | **PENDING** |\n| π0.5 + CRM Plan A | not yet trained (CRM projection 2048→960 ~10–15 GPU-h after baseline harvest) | **PENDING** |\n\nEvery numeric cell in the section will trace back to a registry exp_id before submission (per memory.md M013 lesson: no abstract labels in provenance).\n\n---\n\n## Writing checklist (apply during drafting)\n\n- [ ] Every number in the section traces to a concrete `eval-*` exp_id.\n- [ ] Δ reported in both pp and % relative; headroom fraction Δ / (100 − baseline) given for π0.5.\n- [ ] OpenVLA 0 % discussed as **boundary evidence**, not as a method bug to apologize for.\n- [ ] π0.5 result (whichever of P1/P2/P3 materializes) reported without re-framing post-hoc; per-task breakdown included if Δ < +3 pp.\n- [ ] No cherry-picking: if any seed is excluded, exclusion criterion is named *before* numbers are quoted (cf. D084 seed42 exclusion).\n- [ ] Cross-VLA comparison emphasizes within-backbone Δ; absolute-SR cross-backbone is shown only as a footnote with the caveat that action spaces and fine-tuning regimes differ.\n- [ ] Section ends on the unified prerequisite rule (stochasticity + headroom), tying back to C3.\n\n## Open questions / blockers\n\n- **π0.5 full baseline** ETA: pending bjb1-32546 6-GPU job. Acceptance criterion before harvest: 3 seeds × Object + Spatial all > 60 % SR (consistent with quick-verify 72 %).\n- **π0.5 CRM training**: requires obs cache (2048-dim) precompute + projection layer training (2048→960 reuses SmolVLA CRM head) OR fresh CRM with obs_dim=2048. Decision A in `pi05_crm_pipeline_plan.md` chooses obs_dim=2048; the section assumes that path.\n- **Statistical test**: with n=3 seeds × 10 tasks × 50 rollouts/task = 1500 trials per cell, paired Welch t-test on per-task SR is the planned default; Mann–Whitney U as robustness check.\n- **Latency parity**: confirm π0.5 K=2 batched latency ≤ 1.5× K=1 (SmolVLA achieves K-invariant batched inference; π0.5 yet to be profiled).\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---
