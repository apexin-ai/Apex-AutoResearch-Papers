# paper critical fixes r1n1 r1n3 d021

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738.log`
- **Structured JSON:** [`802ef1d33b50e7f1c0db.json`](../../sessions/80/802ef1d33b50e7f1c0db.json)

## Before a recorded user message

46 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
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
  "uuid": "aa539898-2915-4f1e-bec3-a3620169b64e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/memory/"
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
    "resetsAt": 1778854800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ccf39c50-f2b2-4cf1-b1e7-87d33eaa318d",
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724"
}
```

---

### Assistant

_source line 4_

我先读取 paper_framing.md 和相关 tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "76025283-a1fa-4282-adc6-9bd8239e370d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014aJGVj2kguM8fTZKVKjPq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12327,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12327
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GYWCX7NyVYHF98eo3zJWpK`</summary>

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
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "b24af308-e049-4c49-a445-0caeb5fd6123",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014aJGVj2kguM8fTZKVKjPq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12327,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12327
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

_source line 6 · 2026-05-15T13:37:48.382Z_

<details><summary>↩ Tool result · `toolu_01GYWCX7NyVYHF98eo3zJWpK`</summary>

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
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "93c9fcd3-160c-4406-9fe7-a3ffcac24888",
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

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the paper_framing.md and the relevant tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "39888848-a357-4fe4-925e-676772086724",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NesQEJSQC5m3jQGddJYPtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 24168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NaExCkGPEghRPXDXdWUzYd`</summary>

```json
{
  "project": "recursive_gen_depth_est",
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
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "aa4458eb-7871-43cc-aa9b-a56593e6907d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NesQEJSQC5m3jQGddJYPtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 24168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
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

_source line 9 · 2026-05-15T13:37:52.313Z_

<details><summary>↩ Tool result · `toolu_01NaExCkGPEghRPXDXdWUzYd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper_framing.md\", \"content\": \"# Paper Framing — recursive_gen_depth_est\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\\n- EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\\n\\n## Core Claims (2 条 + Discussion implication)\\n\\n1. **Ordinal depth estimation is feasible and accurate**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark, Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all 9 settings.\\n\\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a genuine geometry-level shift in feature space rather than a correctable scale difference. This atlas spans 3 model families × 3 decoding strategies.\\n\\n3. **[Discussion — Practical Implication]** Depth-graduated curation as alternative to binary filtering: predicted depth provides a finer-grained quality proxy than binary real/synthetic labels, enabling graduated weighting strategies. Conceptual argument supported by depth-accuracy correlation in 3×3 matrix data; full experimental validation deferred to future work (D012).\\n\\n## Story Spine\\n\\n- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer \\\"is this synthetic?\\\" but not \\\"how many recursive cycles has this undergone?\\\" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.\\n\\n- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.\\n\\n- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark (3 models × 3 strategies × 4 depths), and provide the first **Depth Degradation Atlas** — a systematic empirical map of how text statistical properties evolve across recursive depths, models, and strategies. The Atlas reveals (a) perplexity tail statistics as universal depth markers across all 9 settings, (b) model-dependent strategy interaction effects (temperature enhances signal for some models, attenuates for others), and (c) the Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. We show that feature-based classifiers achieve 70–85% four-class accuracy, demonstrating the task is non-trivial but solvable with the right feature family.\\n\\n- **Headline result template**: \\\"On our multi-generational benchmark spanning 3 model families and 3 decoding strategies, feature-based ordinal depth estimation achieves 70–85% accuracy (chance=25%), with perplexity tail statistics (p90_ppl, var_surprisal) consistently among the top-4 features across all 9 settings. The Depth Degradation Atlas reveals that effective discriminable depth extends to depth 3 in 7/9 settings (T=0.75), with model-strategy interaction effects: temperature sampling enhances signal for GPT-2 XL (+2.1pp) but attenuates it for Pythia (−1.9pp).\\\"\\n- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) pending plan_011 results.\\n\\n## DCOL Status — Contingency Activated (D010/D011, 2026-05-15)\\n\\nDCOL v1–v5 全部失败（embedding collapse / OOM / catastrophic forgetting / 超参违规 / NaN 梯度爆炸）。\\n\\n- **Claim 2 (Atlas/EDD) 升为 PRIMARY contribution**\\n- **Claim 1**: Feature-based methods (RF/CORAL/DivEye) 作为 depth estimation 方法，不依赖 DCOL\\n- **DCOL v6 (RoBERTa-large)**: 非阻塞尝试。成功 → Section 5 bonus；失败 → negative analysis section（\\\"contrastive ordinal learning 在文本深度估计的固有局限\\\"）\\n- **Paper type**: Task formalization + systematic empirical study + practical framework（非 method paper）\\n- Atlas + EDD + feature universality + model-strategy interaction = 充分支撑 EMNLP \\\"New Missions\\\" track\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\" risk**: Primary risk now that DCOL is demoted. Mitigation: (a) task formalization is a genuine contribution — no prior work estimates ordinal depth from text alone; (b) Atlas + EDD are novel analytical tools, not just tables; (c) feature universality finding (p90_ppl/var_surprisal top-4 across 9 settings) is a scientific claim with practical implications; (d) model-strategy interaction effects are a new finding. EMNLP \\\"New Missions\\\" track explicitly values problem formalization.\\n- **Controlled vs wild gap**: Mitigation: honest scoping — controlled setting is primary, wild-data calibration is probed, ecological transfer is future work.\\n- **\\\"No novel method\\\" concern**: Mitigation: RF/CORAL are tools, not the contribution. The contribution is the task, the Atlas, and the systematic findings. Analogous to benchmark/analysis papers at top venues (e.g., HELM, MMLU).\\n\\n## Dream-Derived Requirements (D002, 2026-05-14)\\n\\n三档(best 3.0 / median 3.0 / worst 2.5)一致指出的结构性必修项：\\n\\n### 论文写作硬约束\\n1. **DCOL loss 描述** — 若 v6 成功：Eq.1 必须包含 attractive + repulsive 双项（N-pair formulation）。若 v6 失败：negative analysis section 描述失败模式和根因分析，无需完整 loss 公式\\n2. **至少4张图** — (a) AUC decay curve across depth pairs w/ EDD threshold line (b) feature trajectory panel (top-5 features × depth, stratified by model) (c) confusion matrix heatmap (d) Atlas feature×depth heatmap grid。\\\"Atlas without maps is a contradiction\\\"\\n3. **Bibliography 25+ references** — 必须覆盖: watermarking (Kirchenbauer ICML 2023), model collapse theory (Alemohammad ICLR 2024, Dohmatob 2024, Gerstgrasser 2024), data curation (DSIR, QuRating), multi-source attribution (Uchendu 2020), binary detectors (Binoculars Hans ICML 2024, Fast-DetectGPT Bao 2024), decoding strategy effects (Garces Arias COLING 2025, Holtzman ICLR 2020)\\n4. **Surprisal reference model** — 必须明确指定 reference model、说明 cross-model LOO 时如何处理、讨论 circularity\\n\\n### 指标报告硬约束\\n5. **d1-d5 only accuracy** — 作为 companion metric 报告，隔离 ordinal depth estimation 与 binary human-vs-machine detection\\n6. **EDD threshold sensitivity** — 报告 AUC threshold 在 0.65/0.70/0.75/0.80 四档下的 EDD 值\\n7. **k-NN inference 完整规格** — k 值、distance metric、sensitivity analysis\\n\\n### Framing 方向\\n8. **Atlas/EDD 为 primary contribution** — DCOL 定位为 \\\"one strong method within the framework\\\"，不作为 co-primary。三档审稿均认为 DCOL 是 incremental adaptation of CLOC。与 DCOL Contingency 一致。\\n9. **\\\"First systematic empirical map\\\" 需限定** — Shumailov/Drayson 已有 characterization, 我们的新颖性在 ordinal estimation lens + EDD formalization + multi-model multi-strategy coverage\\n\\n### Cross-Strategy 反转硬约束 (D015, Reviewer 降级条件)\\n10. **三档策略分类** — 论文不得将 nucleus 和 temperature 归为同一类 \\\"soft sampling\\\"。必须采用三档：nucleus（baseline 稳定）、temperature（信号增强但存在 d1v2 方向反转风险）、topk（信号衰减但方向一致）。D004 的 \\\"soft sampling\\\" 分组已被反转数据推翻。\\n11. **Discussion 必须含 per-strategy d1v2 AUC 表** — 包含 0.13/0.25 反转值 + **已确认的机制**：temperature 均匀缩放 logit（非截断）加速模型收敛到 attractor 分布（genuine structural distributional shift），temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化提升整体 LR 跨策略 acc（25%→61%）但**不恢复** pairwise d1v2 AUC（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19），证实这是结构性几何偏移而非可校正的尺度差异。\\n12. **Limitations 必须写明跨策略部署约束** — \\\"跨策略部署时需先验知道目标策略类型，否则 d1/d2 预测可能反转。\\\"不可仅将反转作为正面发现消化。\\n\\n## Anticipated Reviewer Concerns\\n\\n1. \\\"EDD might be very low (depth 2-3), making the task trivial beyond shallow depths\\\" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation). Data: 7/9 settings EDD≥3 at T=0.75. **Depth extension bootstrap (D027)**: 三模型 d3v4 AUC 聚集在 0.75 附近 (Pythia 0.784 p=0.001 ✅, OLMo 0.765 p=0.091 ⚠️, GPT-2 XL 0.750 p=0.505 ❌)，仅 Pythia 统计显著。**禁止**写 \\\"three models all achieve statistically significant EDD=4\\\"。正确措辞：\\\"d3v4 AUC consistently clusters near the 0.75 threshold (0.750–0.784) across all three models, while d4v5 AUC uniformly falls below 0.70 (0.681–0.694)\\\"——强调方向一致性 + 完整报告 CI 和 p-values。D024 连续衰减曲线叙事被 bootstrap 数据强力支持。\\n2. \\\"Why ordinal and not just binary?\\\" → d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs\\n3. \\\"Generalization to unseen models/strategies?\\\" → Cross-model LOO: mean 66.4% (holdout Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%) — all >chance but depth_0 recall >98% inflates headline. **Must report per-class recall** (depth_2 recall as low as 26.8%). Cross-strategy LOO: mean 59.1% (51.5–69.4%), topk50 holdout consistently worst. **temp09 holdout shows d1v2 AUC reversal** (GPT-2 XL 0.13, OLMo 0.25) — root cause confirmed as genuine structural distributional shift (temperature accelerates convergence to attractor distribution). Z-score normalization improves overall LR acc (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), confirming this is a geometry-level shift, not a correctable scale artifact. Discuss as \\\"strategy shapes degradation trajectory\\\" finding — temp09 cross-strategy d1v2 generalization remains an open problem (D013/D015/D021).\\n4. \\\"No novel method — just RF on features\\\" → Contribution is task formalization + Atlas + EDD + systematic findings, not method. Analogous to benchmark papers (HELM, MMLU). Feature universality across 9 settings is itself a finding.\\n5. \\\"d0 confound inflates headline metrics\\\" → Report d1-only accuracy alongside full accuracy; 3-class (d1/d2/d3) results already show 59–82% accuracy\\n6. \\\"EDD threshold is arbitrary\\\" → Sensitivity analysis at 0.65/0.70/0.75/0.80 completed (Dream D002)\\n7. \\\"No figures for Atlas\\\" → Minimum 4 figures (Dream D002)\\n8. \\\"Bibliography too thin\\\" → 25+ refs covering all relevant subfields (Dream D002)\\n9. \\\"Model-strategy interaction is just noise\\\" → Three-tier pattern confirmed: nucleus=stable baseline, temperature=enhances signal but reverses d1v2 feature boundary in cross-strategy transfer, topk=attenuates signal but preserves direction (D015). Garces Arias (COLING 2025) independently confirms model-dependent strategy effects.\\n10. \\\"Cross-strategy deployment is unreliable\\\" → Honest limitation: deployment requires knowing target strategy type. In-distribution performance strong (70–85%), cross-strategy transfer degrades (mean 59.1%) with d1v2 reversal in temp09 holdout. Z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and RF is similarly unaffected (Δ<0.02pp). This confirms the temp09 cross-strategy inversion is a genuine structural distributional shift in feature space — not a correctable scale artifact. Mitigation: strategy-conditioned classifier or multi-head architecture (future work). Temp09 cross-strategy d1v2 generalization remains an open problem.\\n\", \"total_chars\": 12890, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "dd346ae5-8164-457a-8099-da811e182b02",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — recursive_gen_depth_est\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\\\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\\\\n- EMNLP 2026 special theme \\\\\\\"New Missions for NLP Research\\\\\\\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\\\\n\\\\n## Core Claims (2 条 + Discussion implication)\\\\n\\\\n1. **Ordinal depth estimation is feasible and accurate**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark, Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all 9 settings.\\\\n\\\\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a genuine geometry-level shift in feature space rather than a correctable scale difference. This atlas spans 3 model families × 3 decoding strategies.\\\\n\\\\n3. **[Discussion — Practical Implication]** Depth-graduated curation as alternative to binary filtering: predicted depth provides a finer-grained quality proxy than binary real/synthetic labels, enabling graduated weighting strategies. Conceptual argument supported by depth-accuracy correlation in 3×3 matrix data; full experimental validation deferred to future work (D012).\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer \\\\\\\"is this synthetic?\\\\\\\" but not \\\\\\\"how many recursive cycles has this undergone?\\\\\\\" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.\\\\n\\\\n- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.\\\\n\\\\n- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark (3 models × 3 strategies × 4 depths), and provide the first **Depth Degradation Atlas** — a systematic empirical map of how text statistical properties evolve across recursive depths, models, and strategies. The Atlas reveals (a) perplexity tail statistics as universal depth markers across all 9 settings, (b) model-dependent strategy interaction effects (temperature enhances signal for some models, attenuates for others), and (c) the Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. We show that feature-based classifiers achieve 70–85% four-class accuracy, demonstrating the task is non-trivial but solvable with the right feature family.\\\\n\\\\n- **Headline result template**: \\\\\\\"On our multi-generational benchmark spanning 3 model families and 3 decoding strategies, feature-based ordinal depth estimation achieves 70–85% accuracy (chance=25%), with perplexity tail statistics (p90_ppl, var_surprisal) consistently among the top-4 features across all 9 settings. The Depth Degradation Atlas reveals that effective discriminable depth extends to depth 3 in 7/9 settings (T=0.75), with model-strategy interaction effects: temperature sampling enhances signal for GPT-2 XL (+2.1pp) but attenuates it for Pythia (−1.9pp).\\\\\\\"\\\\n- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) pending plan_011 results.\\\\n\\\\n## DCOL Status — Contingency Activated (D010/D011, 2026-05-15)\\\\n\\\\nDCOL v1–v5 全部失败（embedding collapse / OOM / catastrophic forgetting / 超参违规 / NaN 梯度爆炸）。\\\\n\\\\n- **Claim 2 (Atlas/EDD) 升为 PRIMARY contribution**\\\\n- **Claim 1**: Feature-based methods (RF/CORAL/DivEye) 作为 depth estimation 方法，不依赖 DCOL\\\\n- **DCOL v6 (RoBERTa-large)**: 非阻塞尝试。成功 → Section 5 bonus；失败 → negative analysis section（\\\\\\\"contrastive ordinal learning 在文本深度估计的固有局限\\\\\\\"）\\\\n- **Paper type**: Task formalization + systematic empirical study + practical framework（非 method paper）\\\\n- Atlas + EDD + feature universality + model-strategy interaction = 充分支撑 EMNLP \\\\\\\"New Missions\\\\\\\" track\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **\\\\\\\"Just an empirical study\\\\\\\" risk**: Primary risk now that DCOL is demoted. Mitigation: (a) task formalization is a genuine contribution — no prior work estimates ordinal depth from text alone; (b) Atlas + EDD are novel analytical tools, not just tables; (c) feature universality finding (p90_ppl/var_surprisal top-4 across 9 settings) is a scientific claim with practical implications; (d) model-strategy interaction effects are a new finding. EMNLP \\\\\\\"New Missions\\\\\\\" track explicitly values problem formalization.\\\\n- **Controlled vs wild gap**: Mitigation: honest scoping — controlled setting is primary, wild-data calibration is probed, ecological transfer is future work.\\\\n- **\\\\\\\"No novel method\\\\\\\" concern**: Mitigation: RF/CORAL are tools, not the contribution. The contribution is the task, the Atlas, and the systematic findings. Analogous to benchmark/analysis papers at top venues (e.g., HELM, MMLU).\\\\n\\\\n## Dream-Derived Requirements (D002, 2026-05-14)\\\\n\\\\n三档(best 3.0 / median 3.0 / worst 2.5)一致指出的结构性必修项：\\\\n\\\\n### 论文写作硬约束\\\\n1. **DCOL loss 描述** — 若 v6 成功：Eq.1 必须包含 attractive + repulsive 双项（N-pair formulation）。若 v6 失败：negative analysis section 描述失败模式和根因分析，无需完整 loss 公式\\\\n2. **至少4张图** — (a) AUC decay curve across depth pairs w/ EDD threshold line (b) feature trajectory panel (top-5 features × depth, stratified by model) (c) confusion matrix heatmap (d) Atlas feature×depth heatmap grid。\\\\\\\"Atlas without maps is a contradiction\\\\\\\"\\\\n3. **Bibliography 25+ references** — 必须覆盖: watermarking (Kirchenbauer ICML 2023), model collapse theory (Alemohammad ICLR 2024, Dohmatob 2024, Gerstgrasser 2024), data curation (DSIR, QuRating), multi-source attribution (Uchendu 2020), binary detectors (Binoculars Hans ICML 2024, Fast-DetectGPT Bao 2024), decoding strategy effects (Garces Arias COLING 2025, Holtzman ICLR 2020)\\\\n4. **Surprisal reference model** — 必须明确指定 reference model、说明 cross-model LOO 时如何处理、讨论 circularity\\\\n\\\\n### 指标报告硬约束\\\\n5. **d1-d5 only accuracy** — 作为 companion metric 报告，隔离 ordinal depth estimation 与 binary human-vs-machine detection\\\\n6. **EDD threshold sensitivity** — 报告 AUC threshold 在 0.65/0.70/0.75/0.80 四档下的 EDD 值\\\\n7. **k-NN inference 完整规格** — k 值、distance metric、sensitivity analysis\\\\n\\\\n### Framing 方向\\\\n8. **Atlas/EDD 为 primary contribution** — DCOL 定位为 \\\\\\\"one strong method within the framework\\\\\\\"，不作为 co-primary。三档审稿均认为 DCOL 是 incremental adaptation of CLOC。与 DCOL Contingency 一致。\\\\n9. **\\\\\\\"First systematic empirical map\\\\\\\" 需限定** — Shumailov/Drayson 已有 characterization, 我们的新颖性在 ordinal estimation lens + EDD formalization + multi-model multi-strategy coverage\\\\n\\\\n### Cross-Strategy 反转硬约束 (D015, Reviewer 降级条件)\\\\n10. **三档策略分类** — 论文不得将 nucleus 和 temperature 归为同一类 \\\\\\\"soft sampling\\\\\\\"。必须采用三档：nucleus（baseline 稳定）、temperature（信号增强但存在 d1v2 方向反转风险）、topk（信号衰减但方向一致）。D004 的 \\\\\\\"soft sampling\\\\\\\" 分组已被反转数据推翻。\\\\n11. **Discussion 必须含 per-strategy d1v2 AUC 表** — 包含 0.13/0.25 反转值 + **已确认的机制**：temperature 均匀缩放 logit（非截断）加速模型收敛到 attractor 分布（genuine structural distributional shift），temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化提升整体 LR 跨策略 acc（25%→61%）但**不恢复** pairwise d1v2 AUC（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19），证实这是结构性几何偏移而非可校正的尺度差异。\\\\n12. **Limitations 必须写明跨策略部署约束** — \\\\\\\"跨策略部署时需先验知道目标策略类型，否则 d1/d2 预测可能反转。\\\\\\\"不可仅将反转作为正面发现消化。\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. \\\\\\\"EDD might be very low (depth 2-3), making the task trivial beyond shallow depths\\\\\\\" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation). Data: 7/9 settings EDD≥3 at T=0.75. **Depth extension bootstrap (D027)**: 三模型 d3v4 AUC 聚集在 0.75 附近 (Pythia 0.784 p=0.001 ✅, OLMo 0.765 p=0.091 ⚠️, GPT-2 XL 0.750 p=0.505 ❌)，仅 Pythia 统计显著。**禁止**写 \\\\\\\"three models all achieve statistically significant EDD=4\\\\\\\"。正确措辞：\\\\\\\"d3v4 AUC consistently clusters near the 0.75 threshold (0.750–0.784) across all three models, while d4v5 AUC uniformly falls below 0.70 (0.681–0.694)\\\\\\\"——强调方向一致性 + 完整报告 CI 和 p-values。D024 连续衰减曲线叙事被 bootstrap 数据强力支持。\\\\n2. \\\\\\\"Why ordinal and not just binary?\\\\\\\" → d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs\\\\n3. \\\\\\\"Generalization to unseen models/strategies?\\\\\\\" → Cross-model LOO: mean 66.4% (holdout Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%) — all >chance but depth_0 recall >98% inflates headline. **Must report per-class recall** (depth_2 recall as low as 26.8%). Cross-strategy LOO: mean 59.1% (51.5–69.4%), topk50 holdout consistently worst. **temp09 holdout shows d1v2 AUC reversal** (GPT-2 XL 0.13, OLMo 0.25) — root cause confirmed as genuine structural distributional shift (temperature accelerates convergence to attractor distribution). Z-score normalization improves overall LR acc (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), confirming this is a geometry-level shift, not a correctable scale artifact. Discuss as \\\\\\\"strategy shapes degradation trajectory\\\\\\\" finding — temp09 cross-strategy d1v2 generalization remains an open problem (D013/D015/D021).\\\\n4. \\\\\\\"No novel method — just RF on features\\\\\\\" → Contribution is task formalization + Atlas + EDD + systematic findings, not method. Analogous to benchmark papers (HELM, MMLU). Feature universality across 9 settings is itself a finding.\\\\n5. \\\\\\\"d0 confound inflates headline metrics\\\\\\\" → Report d1-only accuracy alongside full accuracy; 3-class (d1/d2/d3) results already show 59–82% accuracy\\\\n6. \\\\\\\"EDD threshold is arbitrary\\\\\\\" → Sensitivity analysis at 0.65/0.70/0.75/0.80 completed (Dream D002)\\\\n7. \\\\\\\"No figures for Atlas\\\\\\\" → Minimum 4 figures (Dream D002)\\\\n8. \\\\\\\"Bibliography too thin\\\\\\\" → 25+ refs covering all relevant subfields (Dream D002)\\\\n9. \\\\\\\"Model-strategy interaction is just noise\\\\\\\" → Three-tier pattern confirmed: nucleus=stable baseline, temperature=enhances signal but reverses d1v2 feature boundary in cross-strategy transfer, topk=attenuates signal but preserves direction (D015). Garces Arias (COLING 2025) independently confirms model-dependent strategy effects.\\\\n10. \\\\\\\"Cross-strategy deployment is unreliable\\\\\\\" → Honest limitation: deployment requires knowing target strategy type. In-distribution performance strong (70–85%), cross-strategy transfer degrades (mean 59.1%) with d1v2 reversal in temp09 holdout. Z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and RF is similarly unaffected (Δ<0.02pp). This confirms the temp09 cross-strategy inversion is a genuine structural distributional shift in feature space — not a correctable scale artifact. Mitigation: strategy-conditioned classifier or multi-head architecture (future work). Temp09 cross-strategy d1v2 generalization remains an open problem.\\\\n\\\", \\\"total_chars\\\": 12890, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper_framing.md\", \"content\": \"# Paper Framing — recursive_gen_depth_est\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\\n- EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\\n\\n## Core Claims (2 条 + Discussion implication)\\n\\n1. **Ordinal depth estimation is feasible and accurate**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark, Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all 9 settings.\\n\\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a genuine geometry-level shift in feature space rather than a correctable scale difference. This atlas spans 3 model families × 3 decoding strategies.\\n\\n3. **[Discussion — Practical Implication]** Depth-graduated curation as alternative to binary filtering: predicted depth provides a finer-grained quality proxy than binary real/synthetic labels, enabling graduated weighting strategies. Conceptual argument supported by depth-accuracy correlation in 3×3 matrix data; full experimental validation deferred to future work (D012).\\n\\n## Story Spine\\n\\n- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer \\\"is this synthetic?\\\" but not \\\"how many recursive cycles has this undergone?\\\" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.\\n\\n- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.\\n\\n- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark (3 models × 3 strategies × 4 depths), and provide the first **Depth Degradation Atlas** — a systematic empirical map of how text statistical properties evolve across recursive depths, models, and strategies. The Atlas reveals (a) perplexity tail statistics as universal depth markers across all 9 settings, (b) model-dependent strategy interaction effects (temperature enhances signal for some models, attenuates for others), and (c) the Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. We show that feature-based classifiers achieve 70–85% four-class accuracy, demonstrating the task is non-trivial but solvable with the right feature family.\\n\\n- **Headline result template**: \\\"On our multi-generational benchmark spanning 3 model families and 3 decoding strategies, feature-based ordinal depth estimation achieves 70–85% accuracy (chance=25%), with perplexity tail statistics (p90_ppl, var_surprisal) consistently among the top-4 features across all 9 settings. The Depth Degradation Atlas reveals that effective discriminable depth extends to depth 3 in 7/9 settings (T=0.75), with model-strategy interaction effects: temperature sampling enhances signal for GPT-2 XL (+2.1pp) but attenuates it for Pythia (−1.9pp).\\\"\\n- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) pending plan_011 results.\\n\\n## DCOL Status — Contingency Activated (D010/D011, 2026-05-15)\\n\\nDCOL v1–v5 全部失败（embedding collapse / OOM / catastrophic forgetting / 超参违规 / NaN 梯度爆炸）。\\n\\n- **Claim 2 (Atlas/EDD) 升为 PRIMARY contribution**\\n- **Claim 1**: Feature-based methods (RF/CORAL/DivEye) 作为 depth estimation 方法，不依赖 DCOL\\n- **DCOL v6 (RoBERTa-large)**: 非阻塞尝试。成功 → Section 5 bonus；失败 → negative analysis section（\\\"contrastive ordinal learning 在文本深度估计的固有局限\\\"）\\n- **Paper type**: Task formalization + systematic empirical study + practical framework（非 method paper）\\n- Atlas + EDD + feature universality + model-strategy interaction = 充分支撑 EMNLP \\\"New Missions\\\" track\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\" risk**: Primary risk now that DCOL is demoted. Mitigation: (a) task formalization is a genuine contribution — no prior work estimates ordinal depth from text alone; (b) Atlas + EDD are novel analytical tools, not just tables; (c) feature universality finding (p90_ppl/var_surprisal top-4 across 9 settings) is a scientific claim with practical implications; (d) model-strategy interaction effects are a new finding. EMNLP \\\"New Missions\\\" track explicitly values problem formalization.\\n- **Controlled vs wild gap**: Mitigation: honest scoping — controlled setting is primary, wild-data calibration is probed, ecological transfer is future work.\\n- **\\\"No novel method\\\" concern**: Mitigation: RF/CORAL are tools, not the contribution. The contribution is the task, the Atlas, and the systematic findings. Analogous to benchmark/analysis papers at top venues (e.g., HELM, MMLU).\\n\\n## Dream-Derived Requirements (D002, 2026-05-14)\\n\\n三档(best 3.0 / median 3.0 / worst 2.5)一致指出的结构性必修项：\\n\\n### 论文写作硬约束\\n1. **DCOL loss 描述** — 若 v6 成功：Eq.1 必须包含 attractive + repulsive 双项（N-pair formulation）。若 v6 失败：negative analysis section 描述失败模式和根因分析，无需完整 loss 公式\\n2. **至少4张图** — (a) AUC decay curve across depth pairs w/ EDD threshold line (b) feature trajectory panel (top-5 features × depth, stratified by model) (c) confusion matrix heatmap (d) Atlas feature×depth heatmap grid。\\\"Atlas without maps is a contradiction\\\"\\n3. **Bibliography 25+ references** — 必须覆盖: watermarking (Kirchenbauer ICML 2023), model collapse theory (Alemohammad ICLR 2024, Dohmatob 2024, Gerstgrasser 2024), data curation (DSIR, QuRating), multi-source attribution (Uchendu 2020), binary detectors (Binoculars Hans ICML 2024, Fast-DetectGPT Bao 2024), decoding strategy effects (Garces Arias COLING 2025, Holtzman ICLR 2020)\\n4. **Surprisal reference model** — 必须明确指定 reference model、说明 cross-model LOO 时如何处理、讨论 circularity\\n\\n### 指标报告硬约束\\n5. **d1-d5 only accuracy** — 作为 companion metric 报告，隔离 ordinal depth estimation 与 binary human-vs-machine detection\\n6. **EDD threshold sensitivity** — 报告 AUC threshold 在 0.65/0.70/0.75/0.80 四档下的 EDD 值\\n7. **k-NN inference 完整规格** — k 值、distance metric、sensitivity analysis\\n\\n### Framing 方向\\n8. **Atlas/EDD 为 primary contribution** — DCOL 定位为 \\\"one strong method within the framework\\\"，不作为 co-primary。三档审稿均认为 DCOL 是 incremental adaptation of CLOC。与 DCOL Contingency 一致。\\n9. **\\\"First systematic empirical map\\\" 需限定** — Shumailov/Drayson 已有 characterization, 我们的新颖性在 ordinal estimation lens + EDD formalization + multi-model multi-strategy coverage\\n\\n### Cross-Strategy 反转硬约束 (D015, Reviewer 降级条件)\\n10. **三档策略分类** — 论文不得将 nucleus 和 temperature 归为同一类 \\\"soft sampling\\\"。必须采用三档：nucleus（baseline 稳定）、temperature（信号增强但存在 d1v2 方向反转风险）、topk（信号衰减但方向一致）。D004 的 \\\"soft sampling\\\" 分组已被反转数据推翻。\\n11. **Discussion 必须含 per-strategy d1v2 AUC 表** — 包含 0.13/0.25 反转值 + **已确认的机制**：temperature 均匀缩放 logit（非截断）加速模型收敛到 attractor 分布（genuine structural distributional shift），temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化提升整体 LR 跨策略 acc（25%→61%）但**不恢复** pairwise d1v2 AUC（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19），证实这是结构性几何偏移而非可校正的尺度差异。\\n12. **Limitations 必须写明跨策略部署约束** — \\\"跨策略部署时需先验知道目标策略类型，否则 d1/d2 预测可能反转。\\\"不可仅将反转作为正面发现消化。\\n\\n## Anticipated Reviewer Concerns\\n\\n1. \\\"EDD might be very low (depth 2-3), making the task trivial beyond shallow depths\\\" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation). Data: 7/9 settings EDD≥3 at T=0.75. **Depth extension bootstrap (D027)**: 三模型 d3v4 AUC 聚集在 0.75 附近 (Pythia 0.784 p=0.001 ✅, OLMo 0.765 p=0.091 ⚠️, GPT-2 XL 0.750 p=0.505 ❌)，仅 Pythia 统计显著。**禁止**写 \\\"three models all achieve statistically significant EDD=4\\\"。正确措辞：\\\"d3v4 AUC consistently clusters near the 0.75 threshold (0.750–0.784) across all three models, while d4v5 AUC uniformly falls below 0.70 (0.681–0.694)\\\"——强调方向一致性 + 完整报告 CI 和 p-values。D024 连续衰减曲线叙事被 bootstrap 数据强力支持。\\n2. \\\"Why ordinal and not just binary?\\\" → d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs\\n3. \\\"Generalization to unseen models/strategies?\\\" → Cross-model LOO: mean 66.4% (holdout Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%) — all >chance but depth_0 recall >98% inflates headline. **Must report per-class recall** (depth_2 recall as low as 26.8%). Cross-strategy LOO: mean 59.1% (51.5–69.4%), topk50 holdout consistently worst. **temp09 holdout shows d1v2 AUC reversal** (GPT-2 XL 0.13, OLMo 0.25) — root cause confirmed as genuine structural distributional shift (temperature accelerates convergence to attractor distribution). Z-score normalization improves overall LR acc (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), confirming this is a geometry-level shift, not a correctable scale artifact. Discuss as \\\"strategy shapes degradation trajectory\\\" finding — temp09 cross-strategy d1v2 generalization remains an open problem (D013/D015/D021).\\n4. \\\"No novel method — just RF on features\\\" → Contribution is task formalization + Atlas + EDD + systematic findings, not method. Analogous to benchmark papers (HELM, MMLU). Feature universality across 9 settings is itself a finding.\\n5. \\\"d0 confound inflates headline metrics\\\" → Report d1-only accuracy alongside full accuracy; 3-class (d1/d2/d3) results already show 59–82% accuracy\\n6. \\\"EDD threshold is arbitrary\\\" → Sensitivity analysis at 0.65/0.70/0.75/0.80 completed (Dream D002)\\n7. \\\"No figures for Atlas\\\" → Minimum 4 figures (Dream D002)\\n8. \\\"Bibliography too thin\\\" → 25+ refs covering all relevant subfields (Dream D002)\\n9. \\\"Model-strategy interaction is just noise\\\" → Three-tier pattern confirmed: nucleus=stable baseline, temperature=enhances signal but reverses d1v2 feature boundary in cross-strategy transfer, topk=attenuates signal but preserves direction (D015). Garces Arias (COLING 2025) independently confirms model-dependent strategy effects.\\n10. \\\"Cross-strategy deployment is unreliable\\\" → Honest limitation: deployment requires knowing target strategy type. In-distribution performance strong (70–85%), cross-strategy transfer degrades (mean 59.1%) with d1v2 reversal in temp09 holdout. Z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and RF is similarly unaffected (Δ<0.02pp). This confirms the temp09 cross-strategy inversion is a genuine structural distributional shift in feature space — not a correctable scale artifact. Mitigation: strategy-conditioned classifier or multi-head architecture (future work). Temp09 cross-strategy d1v2 generalization remains an open problem.\\n\", \"total_chars\": 12890, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01KRvMSBv1mKrY1w554vEgeg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "521cdd99-aea0-413d-9e3a-e938df62e30f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NesQEJSQC5m3jQGddJYPtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 24168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
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

_source line 11 · 2026-05-15T13:37:53.724Z_

<details><summary>↩ Tool result · `toolu_01KRvMSBv1mKrY1w554vEgeg`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\times$ 3 decoding strategies $\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.
5	For each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \S\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.
6	
7	\subsection{In-Distribution Performance}
8	\label{sec:atlas:indist}
9	
10	Table~\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.
11	All 9 cells exceed chance (25\%) by a wide margin, with accuracy ranging from 69.6\% to 85.4\%.
12	Both model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.
13	Top-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{In-distribution 4-class depth estimation accuracy (\%) across 3 model families $\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\%.}
19	\label{tab:main_matrix}
20	\begin{tabular}{lccc}
21	\toprule
22	Model & Nucleus & Temp & Top-$k$ \\
23	 & $p{=}0.95$ & $\tau{=}0.9$ & $k{=}50$ \\
24	\midrule
25	Pythia-1.4B & 78.2 & 76.3 & 69.6 \\
26	OLMo-1B & 78.8 & 82.0 & 74.2 \\
27	GPT-2 XL & 83.3 & \textbf{85.4} & 76.6 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	Because the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.
33	Performance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\%, and even the weakest setting (Pythia nucleus) retains 70.8\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.
34	
35	\subsection{Feature Universality}
36	\label{sec:atlas:features}
37	
38	To identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\ref{app:permutation}).
39	Figure~\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.
40	
41	Two features dominate.
42	The 90th-percentile perplexity (\textsc{p90\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\textsc{var\_surprisal}) does so in 7 of 9.
43	In the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\textsc{p75\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.
44	To quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\binom{9}{2}=36$ cell pairs and obtain a mean $\rho = 0.868$ (range: 0.619--0.954).
45	
46	\begin{figure}[t]
47	\centering
48	\includegraphics[width=\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}
49	\caption{Feature importance heatmap across 9 cells (3 models $\times$ 3 strategies). Top-7 features by mean importance. \textsc{p90\_ppl} appears in the top 2 for all cells; \textsc{var\_surprisal} for 7 of 9.}
50	\label{fig:atlas_heatmap}
51	\end{figure}
52	
53	These results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.
54	The universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.
55	
56	\subsection{Effective Discriminable Depth}
57	\label{sec:atlas:edd}
58	
59	Aggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.
60	We formalize this via the \emph{Effective Discriminable Depth} (EDD; defined in \S\ref{sec:method}): $\mathrm{EDD}_T$ is the maximum depth $d^*$ such that the pairwise AUC between $d^*$ and $d^*{+}1$ exceeds a threshold $T$, using a dedicated binary RF per adjacent pair.
61	
62	Within the 4-class atlas (d0--d3), 7 of 9 cells achieve $\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \S\ref{sec:atlas:indist}.
63	
64	To probe deeper, we extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair (we increase from 200 to 500 trees for binary classifiers to ensure convergence on the smaller per-pair sample sizes).
65	Figure~\ref{fig:auc_decay} shows the pairwise AUC decay curve.
66	The d0\,vs.\,d1 boundary is near-perfect (AUC\,=\,0.998), reflecting the well-known human--machine gap.
67	Subsequent boundaries degrade monotonically: d1\,vs.\,d2 achieves 0.925 [95\% CI: 0.914,\,0.935], d2\,vs.\,d3 reaches 0.823 [0.805,\,0.840], and d3\,vs.\,d4 yields 0.784 [0.765,\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.
68	At d4\,vs.\,d5, AUC drops to 0.683 [0.661,\,0.705], falling below the threshold and fixing $\mathrm{EDD}_{0.75}=4$.
69	
70	\begin{figure}[t]
71	\centering
72	\includegraphics[width=\columnwidth]{../../figures/paper/fig_auc_decay.pdf}
73	\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\% bootstrap CI. Dashed line: $T{=}0.75$. $\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\,vs.\,d4 remain discriminable.}
74	\label{fig:auc_decay}
75	\end{figure}
76	
77	Table~\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.
78	At $T{=}0.65$, all pairs through d4\,vs.\,d5 pass, giving $\mathrm{EDD}=5$.
79	At $T{=}0.80$, only d1\,vs.\,d2 and d2\,vs.\,d3 pass, yielding $\mathrm{EDD}=3$.
80	The d0\,vs.\,d1 pair passes at every threshold ($\text{AUC}\geq0.99$).
81	
82	\begin{table}[t]
83	\centering
84	\small
85	\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \checkmark: pairwise AUC $\geq T$; ---: below $T$. d0\,vs.\,d1 always passes (AUC$\geq$0.99) and is omitted.}
86	\label{tab:edd_sensitivity}
87	\begin{tabular}{cccccr}
88	\toprule
89	$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\
90	\midrule
91	0.65 & \checkmark & \checkmark & \checkmark & \checkmark & 5 \\
92	0.70 & \checkmark & \checkmark & \checkmark & --- & 4 \\
93	0.75 & \checkmark & \checkmark & \checkmark & --- & 4 \\
94	0.80 & \checkmark & \checkmark & --- & --- & 3 \\
95	\bottomrule
96	\end{tabular}
97	\end{table}
98	
99	\paragraph{Granularity ablation.}
100	Decision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\% (binary) to 78.3\% (4-class) to 62.9\% (6-class), and the d2\,vs.\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\% relative decline attributable to boundary dilution, not signal loss.
101	
102	\subsection{Strategy-Dependent Trajectories}
103	\label{sec:atlas:trajectories}
104	
105	The atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.
106	Figure~\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.
107	
108	\begin{figure}[t]
109	\centering
110	\includegraphics[width=\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}
111	\caption{Normalized feature trajectories across generation depths for 3 models $\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\ref{app:topk_trajectories}.}
112	\label{fig:feature_trajectory}
113	\end{figure}
114	
115	\paragraph{Non-uniform inter-depth spacing.}
116	For Pythia nucleus, \textsc{p90\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\% reduction.
117	This geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.
118	
119	\paragraph{Temperature-induced acceleration.}
120	Temperature sampling ($\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \citet{marchi2024_heat_death}.
121	Concretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.
122	This shift yields higher in-distribution accuracy (Table~\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\S\ref{sec:generalization}).
123	
124	\paragraph{Three-tier strategy taxonomy.}
125	The trajectory data suggests a functional classification.
126	Nucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.
127	Temperature sampling ($\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.
128	Top-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.
129	Notably, top-$k$ preserves the \emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\S\ref{sec:generalization}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "3c1c06c1-a918-4a71-a4e5-861a2bd8bde2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
      "content": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\\times$ 3 decoding strategies $\\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.\nFor each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \\S\\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.\n\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:indist}\n\nTable~\\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.\nAll 9 cells exceed chance (25\\%) by a wide margin, with accuracy ranging from 69.6\\% to 85.4\\%.\nBoth model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.\nTop-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{In-distribution 4-class depth estimation accuracy (\\%) across 3 model families $\\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\\%.}\n\\label{tab:main_matrix}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Nucleus & Temp & Top-$k$ \\\\\n & $p{=}0.95$ & $\\tau{=}0.9$ & $k{=}50$ \\\\\n\\midrule\nPythia-1.4B & 78.2 & 76.3 & 69.6 \\\\\nOLMo-1B & 78.8 & 82.0 & 74.2 \\\\\nGPT-2 XL & 83.3 & \\textbf{85.4} & 76.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBecause the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.\nPerformance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\\%, and even the weakest setting (Pythia nucleus) retains 70.8\\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.\n\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nTo identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\\ref{app:permutation}).\nFigure~\\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.\n\nTwo features dominate.\nThe 90th-percentile perplexity (\\textsc{p90\\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\\textsc{var\\_surprisal}) does so in 7 of 9.\nIn the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\\textsc{p75\\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.\nTo quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\\binom{9}{2}=36$ cell pairs and obtain a mean $\\rho = 0.868$ (range: 0.619--0.954).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}\n\\caption{Feature importance heatmap across 9 cells (3 models $\\times$ 3 strategies). Top-7 features by mean importance. \\textsc{p90\\_ppl} appears in the top 2 for all cells; \\textsc{var\\_surprisal} for 7 of 9.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\nThese results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.\nThe universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe formalize this via the \\emph{Effective Discriminable Depth} (EDD; defined in \\S\\ref{sec:method}): $\\mathrm{EDD}_T$ is the maximum depth $d^*$ such that the pairwise AUC between $d^*$ and $d^*{+}1$ exceeds a threshold $T$, using a dedicated binary RF per adjacent pair.\n\nWithin the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.\n\nTo probe deeper, we extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair (we increase from 200 to 500 trees for binary classifiers to ensure convergence on the smaller per-pair sample sizes).\nFigure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.\nThe d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.\nSubsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.\nAt d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling below the threshold and fixing $\\mathrm{EDD}_{0.75}=4$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\\% bootstrap CI. Dashed line: $T{=}0.75$. $\\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\\,vs.\\,d4 remain discriminable.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$.\nAt $T{=}0.80$, only d1\\,vs.\\,d2 and d2\\,vs.\\,d3 pass, yielding $\\mathrm{EDD}=3$.\nThe d0\\,vs.\\,d1 pair passes at every threshold ($\\text{AUC}\\geq0.99$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \\checkmark: pairwise AUC $\\geq T$; ---: below $T$. d0\\,vs.\\,d1 always passes (AUC$\\geq$0.99) and is omitted.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccccr}\n\\toprule\n$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\\\\n\\midrule\n0.65 & \\checkmark & \\checkmark & \\checkmark & \\checkmark & 5 \\\\\n0.70 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.75 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.80 & \\checkmark & \\checkmark & --- & --- & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granularity ablation.}\nDecision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.\n\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:trajectories}\n\nThe atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.\nFigure~\\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}\n\\caption{Normalized feature trajectories across generation depths for 3 models $\\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\\ref{app:topk_trajectories}.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n\\paragraph{Non-uniform inter-depth spacing.}\nFor Pythia nucleus, \\textsc{p90\\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\\% reduction.\nThis geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.\n\n\\paragraph{Temperature-induced acceleration.}\nTemperature sampling ($\\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \\citet{marchi2024_heat_death}.\nConcretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.\nThis shift yields higher in-distribution accuracy (Table~\\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\\S\\ref{sec:generalization}).\n\n\\paragraph{Three-tier strategy taxonomy.}\nThe trajectory data suggests a functional classification.\nNucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.\nTemperature sampling ($\\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.\nTop-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.\nNotably, top-$k$ preserves the \\emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\\S\\ref{sec:generalization}).",
      "numLines": 129,
      "startLine": 1,
      "totalLines": 129
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01LDwcKoWD2tUBBFQ2pFRDLR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "01b5427f-c66c-4c1a-92d3-751e662683a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NesQEJSQC5m3jQGddJYPtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 24168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
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

_source line 13 · 2026-05-15T13:37:54.203Z_

<details><summary>↩ Tool result · `toolu_01LDwcKoWD2tUBBFQ2pFRDLR`</summary>

```text
1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	The atlas (\S\ref{sec:atlas}) established in-distribution accuracy of 69.6--85.4\%.
5	We now test whether these results reflect genuine statistical regularities or artifacts of specific training conditions, evaluating four axes: classifier choice (\S\ref{sec:gen:baselines}), cross-model transfer (\S\ref{sec:gen:crossmodel}), cross-strategy transfer (\S\ref{sec:gen:crossstrategy}), and end-to-end learned representations (\S\ref{sec:gen:dcol}).
6	
7	\subsection{Baseline Comparison}
8	\label{sec:gen:baselines}
9	
10	Table~\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.
11	Three feature-based methods---Random Forest (RF), CORAL ordinal regression \cite{coral2020}, and DivEye \cite{diveye2026}---all operate on the same 19 statistical features and achieve statistically indistinguishable accuracy (78.1--78.2\%; pairwise bootstrap $p>0.05$ after Bonferroni correction, 95\% CI within $\pm$1.1pp).
12	These three significantly outperform CE-MLP ($p<0.001$, $+$3.8pp), which in turn trails logistic regression by $\sim$0.1pp.
13	Single-feature regression on mean perplexity performs at chance (25.1\%), confirming that depth estimation requires the multi-dimensional feature representation defined in \S\ref{sec:method}.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Comparison of classification methods on Pythia-1.4B nucleus. RF, CORAL, and DivEye use the same 19 statistical features and are statistically indistinguishable (bootstrap $p>0.05$, Bonferroni-corrected). Chance = 25\%. 5-fold CV std: 0.2--0.9pp across all methods.}
19	\label{tab:baselines}
20	\begin{tabular}{lc}
21	\toprule
22	Method & 4-class Acc (\%) \\
23	\midrule
24	RF (19 features) & 78.2 \\
25	CORAL & 78.1 \\
26	DivEye & 78.2 \\
27	CE-MLP & 74.9 \\
28	LR & 75.0 \\
29	DeepSeek V3.2 (zero-shot)\footnotemark & 40.0 \\
30	ppl-regression (single feature) & 25.1 \\
31	\bottomrule
32	\end{tabular}
33	\footnotetext{Evaluated on 200 samples (approximately 50 per class) from the Pythia-1.4B nucleus cell only, due to API cost; 95\% CI: $\pm$6.8pp. All other methods use the full 20{,}000-sample set.}
34	\end{table}
35	
36	That three structurally different classifiers (tree ensemble, ordinal regression, diversity-based) achieve identical performance on the same features confirms that the discriminative signal resides in the 19 statistical features, not the classifier architecture.
37	A zero-shot LLM baseline (DeepSeek V3.2) achieves 40.0\%---above chance but 38 points below feature-based methods.
38	Figure~\ref{fig:confusion_matrix} shows that d0 is near-perfectly identified in both settings; in-distribution errors concentrate at the d2/d3 boundary, while cross-model transfer spreads confusion more broadly across d1--d3.
39	
40	\begin{figure}[t]
41	\centering
42	\includegraphics[width=\columnwidth]{../../figures/paper/fig_confusion_matrix.pdf}
43	\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\tau{=}0.9$, 85.4\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\%). d0 recall exceeds 99\% in both; errors spread across the d1--d3 range under transfer.}
44	\label{fig:confusion_matrix}
45	\end{figure}
46	
47	\subsection{Cross-Model Transfer}
48	\label{sec:gen:crossmodel}
49	
50	To test whether depth fingerprints generalize across architectures, we perform leave-one-model-family-out evaluation: train on two model families (nucleus sampling only) and test on the held-out third.
51	Table~\ref{tab:cross_model} reports results.
52	
53	\begin{table}[t]
54	\centering
55	\small
56	\caption{Cross-model transfer (leave-one-out, nucleus only). Train on 2 model families, test on held-out 3rd. Chance = 25\%.}
57	\label{tab:cross_model}
58	\begin{tabular}{lccccc}
59	\toprule
60	Holdout & Acc & d0 & d1 & d2 & d3 \\
61	 & (\%) & Rec. & Rec. & Rec. & Rec. \\
62	\midrule
63	Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
64	OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
65	GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
66	\midrule
67	Mean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	Mean transfer accuracy reaches 66.4\% (2.7$\times$ chance).
73	The per-class breakdown reveals that d0 recall ($>$98\%) inflates headline accuracy; d2 recall drops as low as 26.8\% (Pythia holdout), making it the most confusable class.
74	Pythia is the hardest holdout (62.4\%) and OLMo the easiest (69.2\%).
75	
76	\subsection{Cross-Strategy Transfer}
77	\label{sec:gen:crossstrategy}
78	
79	We next train on two decoding strategies and test on the held-out third.
80	Table~\ref{tab:cross_strategy} reports per-model results.
81	
82	\begin{table}[t]
83	\centering
84	\small
85	\caption{Cross-strategy transfer (leave-one-out). Train on 2 strategies, test on held-out 3rd. Chance = 25\%.}
86	\label{tab:cross_strategy}
87	\begin{tabular}{lccc}
88	\toprule
89	Holdout & Pythia & OLMo & GPT-2 XL \\
90	 & Acc (\%) & Acc (\%) & Acc (\%) \\
91	\midrule
92	nucleus & \textbf{69.4} & \textbf{65.4} & \textbf{59.9} \\
93	temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
94	top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
95	\bottomrule
96	\end{tabular}
97	\end{table}
98	
99	Mean cross-strategy accuracy (59.1\%) falls 7 points below cross-model transfer (66.4\%), indicating that strategy-induced distribution shifts pose a greater generalization challenge than architectural differences.
100	
101	\paragraph{Temperature-induced boundary inversion.}
102	Training on nucleus + top-$k$ and testing on temperature yields d1v2 AUC of 0.129 for GPT-2~XL and 0.253 for OLMo---both below 0.5, indicating that the d1/d2 decision boundary \emph{inverts} (Pythia retains a degraded 0.576).
103	This follows from the trajectory analysis in \S\ref{sec:atlas}: temperature sampling shifts feature values at depth $d$ toward depth $d{+}1$ under nucleus/top-$k$.
104	
105	\paragraph{Z-score normalization does not resolve the inversion.}
106	A natural hypothesis is that per-feature z-score normalization might correct this covariate shift \cite{sugiyama2007_importance_weighting}.
107	For RF, z-normalization leaves accuracy essentially unchanged (59.1\% $\to$ 59.2\%) and does not improve d1v2 AUC ($\Delta < 0.02$), as expected since tree splits depend on feature rank order, not scale.
108	Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).
109	This two-layer structure---scale shift addressable by normalization, plus a deeper geometric shift specific to temperature sampling---suggests that temperature decoding induces qualitatively different feature distributions that cannot be reconciled by linear rescaling.
110	
111	\subsection{End-to-End Learning}
112	\label{sec:gen:dcol}
113	
114	We train DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\,{=}\,2{\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.
115	Both achieve ${\sim}$59\% (DeBERTa 58.3$\pm$4.7\%, RoBERTa 59.5$\pm$3.2\%), 19pp below feature-based classifiers (78.2\%).
116	Both easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \textsc{p90\_ppl} and \textsc{var\_surprisal} excel.
117	The 1.2pp inter-backbone gap rules out model selection bias.
118	DCOL \cite{cloc2025} with RoBERTa-large fared worse (best 64.5\%, 5/6 runs unstable).
119	Probing reveals a negative correlation between DeBERTa attention importance and RF permutation importance ($\rho{=}{-}0.48$, $p{=}0.036$; top-5 Jaccard$\,{=}\,0$): transformers attend to lexical patterns (TTR, repeated bigrams) while RF relies on perplexity tail statistics, confirming complementary---not redundant---representations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "0bde1661-c492-4038-a305-12376653b224",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
      "content": "\\section{Generalization and Robustness}\n\\label{sec:generalization}\n\nThe atlas (\\S\\ref{sec:atlas}) established in-distribution accuracy of 69.6--85.4\\%.\nWe now test whether these results reflect genuine statistical regularities or artifacts of specific training conditions, evaluating four axes: classifier choice (\\S\\ref{sec:gen:baselines}), cross-model transfer (\\S\\ref{sec:gen:crossmodel}), cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}), and end-to-end learned representations (\\S\\ref{sec:gen:dcol}).\n\n\\subsection{Baseline Comparison}\n\\label{sec:gen:baselines}\n\nTable~\\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.\nThree feature-based methods---Random Forest (RF), CORAL ordinal regression \\cite{coral2020}, and DivEye \\cite{diveye2026}---all operate on the same 19 statistical features and achieve statistically indistinguishable accuracy (78.1--78.2\\%; pairwise bootstrap $p>0.05$ after Bonferroni correction, 95\\% CI within $\\pm$1.1pp).\nThese three significantly outperform CE-MLP ($p<0.001$, $+$3.8pp), which in turn trails logistic regression by $\\sim$0.1pp.\nSingle-feature regression on mean perplexity performs at chance (25.1\\%), confirming that depth estimation requires the multi-dimensional feature representation defined in \\S\\ref{sec:method}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Comparison of classification methods on Pythia-1.4B nucleus. RF, CORAL, and DivEye use the same 19 statistical features and are statistically indistinguishable (bootstrap $p>0.05$, Bonferroni-corrected). Chance = 25\\%. 5-fold CV std: 0.2--0.9pp across all methods.}\n\\label{tab:baselines}\n\\begin{tabular}{lc}\n\\toprule\nMethod & 4-class Acc (\\%) \\\\\n\\midrule\nRF (19 features) & 78.2 \\\\\nCORAL & 78.1 \\\\\nDivEye & 78.2 \\\\\nCE-MLP & 74.9 \\\\\nLR & 75.0 \\\\\nDeepSeek V3.2 (zero-shot)\\footnotemark & 40.0 \\\\\nppl-regression (single feature) & 25.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\footnotetext{Evaluated on 200 samples (approximately 50 per class) from the Pythia-1.4B nucleus cell only, due to API cost; 95\\% CI: $\\pm$6.8pp. All other methods use the full 20{,}000-sample set.}\n\\end{table}\n\nThat three structurally different classifiers (tree ensemble, ordinal regression, diversity-based) achieve identical performance on the same features confirms that the discriminative signal resides in the 19 statistical features, not the classifier architecture.\nA zero-shot LLM baseline (DeepSeek V3.2) achieves 40.0\\%---above chance but 38 points below feature-based methods.\nFigure~\\ref{fig:confusion_matrix} shows that d0 is near-perfectly identified in both settings; in-distribution errors concentrate at the d2/d3 boundary, while cross-model transfer spreads confusion more broadly across d1--d3.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_confusion_matrix.pdf}\n\\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\\tau{=}0.9$, 85.4\\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\\%). d0 recall exceeds 99\\% in both; errors spread across the d1--d3 range under transfer.}\n\\label{fig:confusion_matrix}\n\\end{figure}\n\n\\subsection{Cross-Model Transfer}\n\\label{sec:gen:crossmodel}\n\nTo test whether depth fingerprints generalize across architectures, we perform leave-one-model-family-out evaluation: train on two model families (nucleus sampling only) and test on the held-out third.\nTable~\\ref{tab:cross_model} reports results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model transfer (leave-one-out, nucleus only). Train on 2 model families, test on held-out 3rd. Chance = 25\\%.}\n\\label{tab:cross_model}\n\\begin{tabular}{lccccc}\n\\toprule\nHoldout & Acc & d0 & d1 & d2 & d3 \\\\\n & (\\%) & Rec. & Rec. & Rec. & Rec. \\\\\n\\midrule\nPythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\\\\nOLMo & \\textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\\\\nGPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\\\\n\\midrule\nMean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean transfer accuracy reaches 66.4\\% (2.7$\\times$ chance).\nThe per-class breakdown reveals that d0 recall ($>$98\\%) inflates headline accuracy; d2 recall drops as low as 26.8\\% (Pythia holdout), making it the most confusable class.\nPythia is the hardest holdout (62.4\\%) and OLMo the easiest (69.2\\%).\n\n\\subsection{Cross-Strategy Transfer}\n\\label{sec:gen:crossstrategy}\n\nWe next train on two decoding strategies and test on the held-out third.\nTable~\\ref{tab:cross_strategy} reports per-model results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-strategy transfer (leave-one-out). Train on 2 strategies, test on held-out 3rd. Chance = 25\\%.}\n\\label{tab:cross_strategy}\n\\begin{tabular}{lccc}\n\\toprule\nHoldout & Pythia & OLMo & GPT-2 XL \\\\\n & Acc (\\%) & Acc (\\%) & Acc (\\%) \\\\\n\\midrule\nnucleus & \\textbf{69.4} & \\textbf{65.4} & \\textbf{59.9} \\\\\ntemp ($\\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\\\\ntop-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean cross-strategy accuracy (59.1\\%) falls 7 points below cross-model transfer (66.4\\%), indicating that strategy-induced distribution shifts pose a greater generalization challenge than architectural differences.\n\n\\paragraph{Temperature-induced boundary inversion.}\nTraining on nucleus + top-$k$ and testing on temperature yields d1v2 AUC of 0.129 for GPT-2~XL and 0.253 for OLMo---both below 0.5, indicating that the d1/d2 decision boundary \\emph{inverts} (Pythia retains a degraded 0.576).\nThis follows from the trajectory analysis in \\S\\ref{sec:atlas}: temperature sampling shifts feature values at depth $d$ toward depth $d{+}1$ under nucleus/top-$k$.\n\n\\paragraph{Z-score normalization does not resolve the inversion.}\nA natural hypothesis is that per-feature z-score normalization might correct this covariate shift \\cite{sugiyama2007_importance_weighting}.\nFor RF, z-normalization leaves accuracy essentially unchanged (59.1\\% $\\to$ 59.2\\%) and does not improve d1v2 AUC ($\\Delta < 0.02$), as expected since tree splits depend on feature rank order, not scale.\nZ-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).\nThis two-layer structure---scale shift addressable by normalization, plus a deeper geometric shift specific to temperature sampling---suggests that temperature decoding induces qualitatively different feature distributions that cannot be reconciled by linear rescaling.\n\n\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nWe train DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nBoth achieve ${\\sim}$59\\% (DeBERTa 58.3$\\pm$4.7\\%, RoBERTa 59.5$\\pm$3.2\\%), 19pp below feature-based classifiers (78.2\\%).\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nThe 1.2pp inter-backbone gap rules out model selection bias.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\nProbing reveals a negative correlation between DeBERTa attention importance and RF permutation importance ($\\rho{=}{-}0.48$, $p{=}0.036$; top-5 Jaccard$\\,{=}\\,0$): transformers attend to lexical patterns (TTR, repeated bigrams) while RF relies on perplexity tail statistics, confirming complementary---not redundant---representations.",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_0165mDwpHK1KtkMDqH1XcBWx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "f77fde39-4af8-4eb2-a2ea-74ef029ec730",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NesQEJSQC5m3jQGddJYPtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 24168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
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

_source line 15 · 2026-05-15T13:37:54.656Z_

<details><summary>↩ Tool result · `toolu_0165mDwpHK1KtkMDqH1XcBWx`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Depth-graduated data curation.}
5	Binary synthetic-data filters discard all machine-generated text indiscriminately, yet first-generation outputs may be beneficial for training \cite{drayson2025_detection_prevents_collapse}.
6	Predicted depth can serve as a continuous quality proxy for importance weighting in curation pipelines \cite{dsir2023,qurating2024}, retaining shallow-generation text while down-weighting deeply recursive samples.
7	
8	\paragraph{Feature evolution tracks tail erosion.}
9	Feature importance shifts with depth: \textsc{var\_surprisal} dominates at shallow recursions while \textsc{p90\_ppl} and kurtosis assume greater importance at deeper depths, aligning with the tail erosion theory of \citet{shumailov2024_nature}.
10	
11	\paragraph{Cross-strategy deployment.}
12	The temperature-induced d1/d2 AUC inversion (\S\ref{sec:gen:crossstrategy}) means that deploying a depth estimator without knowing the target decoding strategy risks systematic prediction reversals; strategy-conditioned classifiers are needed but strategy identification from text remains open.
13	
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "42e30923-63fd-4423-a387-3983871679e7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Depth-graduated data curation.}\nBinary synthetic-data filters discard all machine-generated text indiscriminately, yet first-generation outputs may be beneficial for training \\cite{drayson2025_detection_prevents_collapse}.\nPredicted depth can serve as a continuous quality proxy for importance weighting in curation pipelines \\cite{dsir2023,qurating2024}, retaining shallow-generation text while down-weighting deeply recursive samples.\n\n\\paragraph{Feature evolution tracks tail erosion.}\nFeature importance shifts with depth: \\textsc{var\\_surprisal} dominates at shallow recursions while \\textsc{p90\\_ppl} and kurtosis assume greater importance at deeper depths, aligning with the tail erosion theory of \\citet{shumailov2024_nature}.\n\n\\paragraph{Cross-strategy deployment.}\nThe temperature-induced d1/d2 AUC inversion (\\S\\ref{sec:gen:crossstrategy}) means that deploying a depth estimator without knowing the target decoding strategy risks systematic prediction reversals; strategy-conditioned classifiers are needed but strategy identification from text remains open.\n\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me also read the method.tex to see how EDD is currently defined there, and search for any z-score claims across all tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "12093774-31df-4e71-a7e8-2f1e6ba98252",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195arTs59dxAfbthQFsq74q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11798,
      "cache_read_input_tokens": 24626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11798
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

_source line 17_

Let me check the method.tex for the current EDD definition and search for z-score claims across all files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "9af8dc60-a3c1-4cfb-8e46-82012fdbf185",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195arTs59dxAfbthQFsq74q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11798,
      "cache_read_input_tokens": 24626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11798
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

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_019GhCiufDKE4KeoxAjCHDcs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "facca1bf-026e-476d-a3e5-11e03ea1fd9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195arTs59dxAfbthQFsq74q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11798,
      "cache_read_input_tokens": 24626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11798
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

_source line 19 · 2026-05-15T13:38:01.460Z_

<details><summary>↩ Tool result · `toolu_019GhCiufDKE4KeoxAjCHDcs`</summary>

```text
1	\section{Task Formulation}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three sampling methods: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	
27	\paragraph{Depth and scale.}
28	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
29	For depth extension experiments (\S\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.
30	
31	\paragraph{Generation pipeline.}
32	Starting from a Wikipedia subset as seed text ($\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \cite{hu2022lora} with rank $r{=}16$, $\alpha{=}32$, learning rate $2{\times}10^{-4}$, batch size 8, for 3 epochs; (2)~generation of 5{,}000 passages (max 512 tokens) under the specified decoding strategy; (3)~the generated corpus becomes $\mathcal{D}_k$ and serves as training data for the next cycle.
33	Each generation cycle samples unconditionally from the BOS token; there is no per-passage lineage across depths, ensuring that cross-validation splits do not introduce information leakage.
34	LoRA targets are architecture-specific: \texttt{query\_key\_value} for Pythia (GPT-NeoX), \texttt{q\_proj}/\texttt{k\_proj}/\texttt{v\_proj} for OLMo, and \texttt{c\_attn}/\texttt{c\_proj} for GPT-2~XL.
35	We adopt standard LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout$\,{=}\,0.05$) following \citet{hu2022lora}, applied uniformly across all models.
36	
37	\paragraph{Reference model.}
38	All statistical features (\S\ref{sec:method:features}) are computed using a fixed reference model---GPT-2 base (124M)---that is independent of the three generation models.
39	The reference model computes per-token perplexity for each passage, providing a consistent measurement frame across model families.
40	In cross-model leave-one-out evaluation (\S\ref{sec:generalization}), the reference model remains fixed even when GPT-2~XL is held out; the partial architectural overlap this introduces is discussed in \S\ref{sec:discussion}.
41	
42	\subsection{Statistical Feature Design}
43	\label{sec:method:features}
44	
45	We extract a 19-dimensional feature vector $\mathbf{f}(x)$ from the reference-model perplexity distribution over each passage $x$.
46	The features fall into four categories (Table~\ref{tab:features}).
47	
48	\begin{table}[t]
49	\centering
50	\small
51	\caption{The 19 statistical features comprising $\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (GPT-2 base, 124M).}
52	\label{tab:features}
53	\begin{tabular}{@{}llr@{}}
54	\toprule
55	Category & Features & $n$ \\
56	\midrule
57	Perplexity & mean, var, skewness, kurtosis, & 9 \\
58	statistics & p10, p25, p50, p75, p90 & \\
59	\addlinespace
60	Surprisal & mean, var, entropy & 3 \\
61	statistics & & \\
62	\addlinespace
63	Lexical & type--token ratio, hapax ratio, & 4 \\
64	diversity & bigram entropy, trigram entropy & \\
65	\addlinespace
66	Repetition & repeated 2/3/4-gram fractions & 3 \\
67	\bottomrule
68	\end{tabular}
69	\end{table}
70	
71	\emph{Perplexity statistics} (9 features) capture the location, spread, and shape of the per-token perplexity distribution via its mean, variance, skewness, kurtosis, and five percentile quantiles (p10--p90).
72	The tail quantiles (p75, p90) prove especially informative: recursive finetuning erodes the high-perplexity tail, making these features monotonically decreasing with depth (\S\ref{sec:atlas}).
73	
74	\emph{Surprisal statistics} (3 features) operate on $-\log p(\text{token})$ and include mean surprisal, surprisal variance, and the entropy of the surprisal distribution.
75	While correlated with perplexity features, surprisal variance captures second-order structure---the variability of token predictability---that is not redundant with perplexity moments.
76	
77	\emph{Lexical diversity} (4 features) measures vocabulary usage through type--token ratio, hapax ratio (fraction of tokens appearing exactly once), and bigram/trigram entropy.
78	
79	\emph{Repetition} (3 features) quantifies the fraction of repeated $n$-grams for $n \in \{2, 3, 4\}$, capturing the increased self-repetition characteristic of recursive generation.
80	
81	\subsection{Effective Discriminable Depth}
82	\label{sec:method:edd}
83	
84	Aggregate classification accuracy over $K{+}1$ classes obscures whether discriminability degrades at specific depths.
85	We introduce the \emph{Effective Discriminable Depth} (EDD), a scalar metric that summarizes how far into a recursive chain adjacent depths remain distinguishable.
86	
87	For each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary Random Forest (500 trees; increased from 200 in the multi-class setting to ensure convergence on the smaller per-pair samples) and compute the one-vs-one AUC.
88	Given a threshold $T$, we define:
89	\begin{equation}
90	\mathrm{EDD}_T = \max \{ d^*{+}1 : \mathrm{AUC}(d^*, d^*{+}1) \geq T \}
91	\label{eq:edd}
92	\end{equation}
93	where $d^* \in \{0, 1, \dots, K{-}1\}$.
94	The default threshold is $T{=}0.75$; we report sensitivity analyses at $T \in \{0.65, 0.70, 0.75, 0.80\}$ in \S\ref{sec:atlas}.
95	Crucially, each AUC is obtained from an independent binary pairwise classifier (5-fold stratified CV) rather than extracted from a single multi-class model, avoiding decision boundary dilution (\S\ref{sec:atlas}).
96	
97	EDD captures a natural question: \emph{how deep into the recursive chain can we reliably distinguish successive generations?}
98	A high EDD indicates that the statistical fingerprints retain discriminative power across many recursion steps; a low EDD signals rapid convergence to an indistinguishable regime.
99	
100	\paragraph{Classifiers.}
101	Our primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold stratified cross-validation).
102	We compare against CORAL ordinal regression \cite{coral2020}, DivEye \cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \S\ref{sec:generalization}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "1012f03e-a86a-46d3-adbc-6ebbaccb6a60",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
      "content": "\\section{Task Formulation}\n\\label{sec:method}\n\n\\subsection{Problem Definition}\n\\label{sec:method:problem}\n\nLet $f_\\theta$ denote a language model and $\\mathcal{D}_0$ a corpus of human-written seed text.\nWe define a \\emph{recursive generation chain} of depth $K$ as the sequence $\\mathcal{D}_0, \\mathcal{D}_1, \\dots, \\mathcal{D}_K$, where each $\\mathcal{D}_k$ ($k \\geq 1$) is produced by finetuning $f_\\theta$ on $\\mathcal{D}_{k-1}$ and sampling from the resulting model.\nDepth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \\geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.\n\nGiven a text passage $x$, the task is to estimate its recursive generation depth $d \\in \\{0, 1, \\dots, K\\}$.\nThis is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.\n\n\\subsection{Multi-Generational Benchmark Construction}\n\\label{sec:method:benchmark}\n\nWe construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.\n\n\\paragraph{Model families.}\nWe select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).\nRestricting to a narrow parameter range isolates the effect of architecture and training data from scale.\n\n\\paragraph{Decoding strategies.}\nEach model is paired with three sampling methods: nucleus sampling ($p{=}0.95$) \\cite{holtzman2020_nucleus}, temperature sampling ($\\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).\nThese span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.\n\n\\paragraph{Depth and scale.}\nThe primary benchmark covers depths d0--d3 across all $3 \\times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).\nFor depth extension experiments (\\S\\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.\n\n\\paragraph{Generation pipeline.}\nStarting from a Wikipedia subset as seed text ($\\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \\cite{hu2022lora} with rank $r{=}16$, $\\alpha{=}32$, learning rate $2{\\times}10^{-4}$, batch size 8, for 3 epochs; (2)~generation of 5{,}000 passages (max 512 tokens) under the specified decoding strategy; (3)~the generated corpus becomes $\\mathcal{D}_k$ and serves as training data for the next cycle.\nEach generation cycle samples unconditionally from the BOS token; there is no per-passage lineage across depths, ensuring that cross-validation splits do not introduce information leakage.\nLoRA targets are architecture-specific: \\texttt{query\\_key\\_value} for Pythia (GPT-NeoX), \\texttt{q\\_proj}/\\texttt{k\\_proj}/\\texttt{v\\_proj} for OLMo, and \\texttt{c\\_attn}/\\texttt{c\\_proj} for GPT-2~XL.\nWe adopt standard LoRA hyperparameters ($r{=}16$, $\\alpha{=}32$, dropout$\\,{=}\\,0.05$) following \\citet{hu2022lora}, applied uniformly across all models.\n\n\\paragraph{Reference model.}\nAll statistical features (\\S\\ref{sec:method:features}) are computed using a fixed reference model---GPT-2 base (124M)---that is independent of the three generation models.\nThe reference model computes per-token perplexity for each passage, providing a consistent measurement frame across model families.\nIn cross-model leave-one-out evaluation (\\S\\ref{sec:generalization}), the reference model remains fixed even when GPT-2~XL is held out; the partial architectural overlap this introduces is discussed in \\S\\ref{sec:discussion}.\n\n\\subsection{Statistical Feature Design}\n\\label{sec:method:features}\n\nWe extract a 19-dimensional feature vector $\\mathbf{f}(x)$ from the reference-model perplexity distribution over each passage $x$.\nThe features fall into four categories (Table~\\ref{tab:features}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{The 19 statistical features comprising $\\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (GPT-2 base, 124M).}\n\\label{tab:features}\n\\begin{tabular}{@{}llr@{}}\n\\toprule\nCategory & Features & $n$ \\\\\n\\midrule\nPerplexity & mean, var, skewness, kurtosis, & 9 \\\\\nstatistics & p10, p25, p50, p75, p90 & \\\\\n\\addlinespace\nSurprisal & mean, var, entropy & 3 \\\\\nstatistics & & \\\\\n\\addlinespace\nLexical & type--token ratio, hapax ratio, & 4 \\\\\ndiversity & bigram entropy, trigram entropy & \\\\\n\\addlinespace\nRepetition & repeated 2/3/4-gram fractions & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\emph{Perplexity statistics} (9 features) capture the location, spread, and shape of the per-token perplexity distribution via its mean, variance, skewness, kurtosis, and five percentile quantiles (p10--p90).\nThe tail quantiles (p75, p90) prove especially informative: recursive finetuning erodes the high-perplexity tail, making these features monotonically decreasing with depth (\\S\\ref{sec:atlas}).\n\n\\emph{Surprisal statistics} (3 features) operate on $-\\log p(\\text{token})$ and include mean surprisal, surprisal variance, and the entropy of the surprisal distribution.\nWhile correlated with perplexity features, surprisal variance captures second-order structure---the variability of token predictability---that is not redundant with perplexity moments.\n\n\\emph{Lexical diversity} (4 features) measures vocabulary usage through type--token ratio, hapax ratio (fraction of tokens appearing exactly once), and bigram/trigram entropy.\n\n\\emph{Repetition} (3 features) quantifies the fraction of repeated $n$-grams for $n \\in \\{2, 3, 4\\}$, capturing the increased self-repetition characteristic of recursive generation.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:method:edd}\n\nAggregate classification accuracy over $K{+}1$ classes obscures whether discriminability degrades at specific depths.\nWe introduce the \\emph{Effective Discriminable Depth} (EDD), a scalar metric that summarizes how far into a recursive chain adjacent depths remain distinguishable.\n\nFor each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary Random Forest (500 trees; increased from 200 in the multi-class setting to ensure convergence on the smaller per-pair samples) and compute the one-vs-one AUC.\nGiven a threshold $T$, we define:\n\\begin{equation}\n\\mathrm{EDD}_T = \\max \\{ d^*{+}1 : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T \\}\n\\label{eq:edd}\n\\end{equation}\nwhere $d^* \\in \\{0, 1, \\dots, K{-}1\\}$.\nThe default threshold is $T{=}0.75$; we report sensitivity analyses at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in \\S\\ref{sec:atlas}.\nCrucially, each AUC is obtained from an independent binary pairwise classifier (5-fold stratified CV) rather than extracted from a single multi-class model, avoiding decision boundary dilution (\\S\\ref{sec:atlas}).\n\nEDD captures a natural question: \\emph{how deep into the recursive chain can we reliably distinguish successive generations?}\nA high EDD indicates that the statistical fingerprints retain discriminative power across many recursion steps; a low EDD signals rapid convergence to an indistinguishable regime.\n\n\\paragraph{Classifiers.}\nOur primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold stratified cross-validation).\nWe compare against CORAL ordinal regression \\cite{coral2020}, DivEye \\cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \\S\\ref{sec:generalization}.",
      "numLines": 102,
      "startLine": 1,
      "totalLines": 102
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_01D41SuGCp9WLdWLRTfMYN5A`</summary>

```json
{
  "pattern": "z.score|z-score|normalization.*recover|normalization.*restor",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "-i": true,
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
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "4edaf2d2-cb39-4acd-98db-745d1da69775",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195arTs59dxAfbthQFsq74q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11798,
      "cache_read_input_tokens": 24626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11798
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

_source line 21 · 2026-05-15T13:38:02.973Z_

<details><summary>↩ Tool result · `toolu_01D41SuGCp9WLdWLRTfMYN5A`</summary>

```text
docs/paper/generalization.tex:105:\paragraph{Z-score normalization does not resolve the inversion.}
docs/paper/generalization.tex:106:A natural hypothesis is that per-feature z-score normalization might correct this covariate shift \cite{sugiyama2007_importance_weighting}.
docs/paper/generalization.tex:108:Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).
docs/paper/abstract.tex:7:Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%, though temperature sampling induces a d1/d2 AUC inversion that z-score normalization cannot resolve.
docs/paper/introduction.tex:31:[Omitted long matching line]
docs/paper/main.aux:735:\@writefile{toc}{\contentsline {paragraph}{Z-score normalization does not resolve the inversion.}{8}{section*.26}\protected@file@percent }
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "3d77372c-d9fd-402a-acd8-29c92cd5bdf1",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/generalization.tex:105:\\paragraph{Z-score normalization does not resolve the inversion.}\ndocs/paper/generalization.tex:106:A natural hypothesis is that per-feature z-score normalization might correct this covariate shift \\cite{sugiyama2007_importance_weighting}.\ndocs/paper/generalization.tex:108:Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).\ndocs/paper/abstract.tex:7:Cross-model transfer reaches 66.4\\% and cross-strategy transfer 59.1\\%, though temperature sampling induces a d1/d2 AUC inversion that z-score normalization cannot resolve.\ndocs/paper/introduction.tex:31:[Omitted long matching line]\ndocs/paper/main.aux:735:\\@writefile{toc}{\\contentsline {paragraph}{Z-score normalization does not resolve the inversion.}{8}{section*.26}\\protected@file@percent }",
    "numLines": 6
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Let me read the introduction.tex line 31 to see the z-score claim there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "a4c886e7-e84a-4ac0-9c99-bedca33d8c13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kuuv3fnGkJxdpzAMaWM5Kk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3244,
      "cache_read_input_tokens": 36424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3244
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

_source line 23_

Let me check the introduction.tex z-score mention and the abstract.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "33f47c7f-8482-46af-a2ee-a0039935f4be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kuuv3fnGkJxdpzAMaWM5Kk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3244,
      "cache_read_input_tokens": 36424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3244
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

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01X95GQpoMDy5qQbTF3qMRJu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
  "offset": 25,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "e68a457e-0d08-4a07-8967-0b0b8358df4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kuuv3fnGkJxdpzAMaWM5Kk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3244,
      "cache_read_input_tokens": 36424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3244
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

_source line 25 · 2026-05-15T13:38:09.091Z_

<details><summary>↩ Tool result · `toolu_01X95GQpoMDy5qQbTF3qMRJu`</summary>

```text
25	
26	\begin{itemize}
27	    \item \textbf{Task formalization.} We define recursive generation depth estimation as ordinal classification, distinguishing it from binary detection and single-pass editing estimation. We introduce the EDD metric, which summarizes the maximum depth at which adjacent generations remain separable above a given AUC threshold.
28	
29	    \item \textbf{Depth Degradation Atlas.} We construct a systematic $3 \times 3$ map across model families and decoding strategies, revealing that \textsc{p90\_ppl} ranks in the top 2 in all 9 cells (100\%) and \textsc{var\_surprisal} in 7/9 (78\%), with a mean Spearman rank correlation of $\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.
30	
31	    \item \textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\% mean accuracy and cross-strategy transfer 59.1\% (chance = 25\%), demonstrating partial universality of depth fingerprints. We identify a temperature-induced d1/d2 AUC inversion (GPT-2~XL: 0.13, OLMo: 0.25) caused by accelerated convergence. Z-score normalization recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89) but fails to resolve the temperature-specific inversion, revealing a two-layer covariate shift structure.
32	
33	    \item \textbf{End-to-end learning as negative result.} Both DeBERTa-v3-base (58.3\%) and RoBERTa-base (59.5\%) achieve ${\sim}$59\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\%)---with the architecture-invariant gap ruling out model selection bias. Probing reveals a significant negative correlation ($\rho{=}{-}0.48$) between transformer attention and RF feature importance, confirming complementary representations.
34	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "fb3be087-306e-495d-98f0-30d805c52f54",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
      "content": "\n\\begin{itemize}\n    \\item \\textbf{Task formalization.} We define recursive generation depth estimation as ordinal classification, distinguishing it from binary detection and single-pass editing estimation. We introduce the EDD metric, which summarizes the maximum depth at which adjacent generations remain separable above a given AUC threshold.\n\n    \\item \\textbf{Depth Degradation Atlas.} We construct a systematic $3 \\times 3$ map across model families and decoding strategies, revealing that \\textsc{p90\\_ppl} ranks in the top 2 in all 9 cells (100\\%) and \\textsc{var\\_surprisal} in 7/9 (78\\%), with a mean Spearman rank correlation of $\\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.\n\n    \\item \\textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\\% mean accuracy and cross-strategy transfer 59.1\\% (chance = 25\\%), demonstrating partial universality of depth fingerprints. We identify a temperature-induced d1/d2 AUC inversion (GPT-2~XL: 0.13, OLMo: 0.25) caused by accelerated convergence. Z-score normalization recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89) but fails to resolve the temperature-specific inversion, revealing a two-layer covariate shift structure.\n\n    \\item \\textbf{End-to-end learning as negative result.} Both DeBERTa-v3-base (58.3\\%) and RoBERTa-base (59.5\\%) achieve ${\\sim}$59\\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\\%)---with the architecture-invariant gap ruling out model selection bias. Probing reveals a significant negative correlation ($\\rho{=}{-}0.48$) between transformer attention and RF feature importance, confirming complementary representations.\n\\end{itemize}",
      "numLines": 10,
      "startLine": 25,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01D3yg3VVMZzCdZzdDZ1muZ9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "2f1bc6d6-b899-4acd-9d3a-7c48e543410b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kuuv3fnGkJxdpzAMaWM5Kk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3244,
      "cache_read_input_tokens": 36424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3244
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

_source line 27 · 2026-05-15T13:38:09.296Z_

<details><summary>↩ Tool result · `toolu_01D3yg3VVMZzCdZzdDZ1muZ9`</summary>

```text
1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises---yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	From each passage we extract 19 statistical features---perplexity percentiles, surprisal moments, and lexical diversity measures---computed against a fixed reference model (GPT-2 base, 124M).
5	A Random Forest classifier achieves 70--85\% four-class accuracy (chance = 25\%; a zero-shot LLM baseline reaches only 40\%), with 90th-percentile perplexity and surprisal variance emerging as universal depth markers (top-2 importance in 9/9 and 7/9 model--strategy cells, respectively; mean Spearman $\rho{=}0.868$).
6	Our \emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for extended recursion chains.
7	Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%, though temperature sampling induces a d1/d2 AUC inversion that z-score normalization cannot resolve.
8	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "d455562f-b53e-4e92-9f17-39cfdb61323e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nAs large language models increasingly train on web text containing their own outputs, a recursive model$\\to$data$\\to$model loop arises---yet no method estimates how many such iterations a text has undergone.\nWe formalize \\emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.\nFrom each passage we extract 19 statistical features---perplexity percentiles, surprisal moments, and lexical diversity measures---computed against a fixed reference model (GPT-2 base, 124M).\nA Random Forest classifier achieves 70--85\\% four-class accuracy (chance = 25\\%; a zero-shot LLM baseline reaches only 40\\%), with 90th-percentile perplexity and surprisal variance emerging as universal depth markers (top-2 importance in 9/9 and 7/9 model--strategy cells, respectively; mean Spearman $\\rho{=}0.868$).\nOur \\emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \\emph{Effective Discriminable Depth} (EDD) metric, finding $\\mathrm{EDD}_{0.75}{=}4$ for extended recursion chains.\nCross-model transfer reaches 66.4\\% and cross-strategy transfer 59.1\\%, though temperature sampling induces a d1/d2 AUC inversion that z-score normalization cannot resolve.\n\\end{abstract}",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

````text
Now I have a good picture of all three issues. Let me plan the changes:

### Issue 1: R1-N1 — EDD formal math definition
The EDD is already formally defined in method.tex at line 88-93 with equation:
```
\mathrm{EDD}_T = \max \{ d^*{+}1 : \mathrm{AUC}(d^*, d^*{+}1) \geq T \}
```

Wait, looking more carefully at the task requirement:
```
EDD(T) = max{d : AUC(d, d+1) ≥ T}


```

The current formula uses `d*+1` as the maximized variable, but the requirement wants just `d`. Let me reconsider what this means — the EDD should be the maximum depth where the AUC between consecutive depths still meets the threshold, so the simpler formulation makes more sense.

```
I'm noticing a discrepancy between how the paper defines EDD and what the task formula specifies. The task uses `EDD(T) = max{d : AUC(d, d+1) ≥ T}`, but when I apply this to the extended case where d3 vs d4 passes the threshold, I get EDD = 3, whereas the paper reports EDD = 4. This suggests the paper is actually using the d*+1 formulation rather than the d* formulation the task describes.
```
\subsection{Effective Discriminable Depth}
\label{sec:atlas:edd}

Aggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.
We formalize this via the \emph{Effective Discriminable Depth} (EDD; defined in \S\ref{sec:method}): $\mathrm{EDD}_T$ is the maximum depth $d^*$ such that the pairwise AUC between $d^*$ and $d^*{+}1$ exceeds a threshold $T$,
```

The task is asking me to add the formal definition to atlas.tex, and I can see there's already a definition starting in lines 56-61. I need to check what exactly needs to be added or clarified there.

Looking at the requirements, I need to include the explicit formula $\mathrm{EDD}(T) = \max\{d : \mathrm{AUC}(d, d+1) \geq T\}$, explain that $T$ is a threshold with a recommended value of 0.75 based on the D011 decision, clarify that $\mathrm{AUC}(d, d+1)$ represents the binary classifier ROC AUC when distinguishing between depth $d$ and depth $d+1$, and convey the intuitive meaning that this metric captures the maximum depth at which adjacent levels remain discriminable.

But I'm noticing a discrepancy—the formula in method.tex uses $\mathrm{EDD}_T = \max\{d^*+1 : \mathrm{AUC}(d^*, d^*+1) \geq T\}$, which produces different values than the simpler formulation the task is asking for. If I switch to the requested formula, the reported EDD values might not align with what's currently claimed in the paper. task's formula, I'd need to change all the EDD values in the paper. That seems wrong. Let me re-read the task...

Actually, wait. Looking more carefully at the current formula in method.tex:
```
\mathrm{EDD}_T = \max \{ d^*{+}1 : \mathrm{AUC}(d^*, d^*{+}1) \geq T \}
```

This means: EDD_T = max(d*+1) where AUC(d*, d*+1) >= T. With d3v4 passing, d* = 3, so d*+1 = 4, hence EDD = 4. That represents "4 depths are distinguishable" or "discriminable up to depth 4."

The task's formula `max{d : AUC(d, d+1) >= T}` would give max d = 3, meaning "the last depth where we can still distinguish the next level." These are semantically different but both valid.

Since the task explicitly asks for `EDD(T) = max{d : AUC(d, d+1) ≥ T}`, I should use it, but this would break consistency with the existing formula in method.tex and all the reported EDD values. I think the right approach is to add the formal definition in atlas.tex with more detail about T, AUC, and the intuition while keeping it consistent with the existing formula. Let me check what's already in atlas.tex at line 61 to see how to adapt this properly. I see there's a mismatch between the prose description in atlas.tex and the formula in method.tex—the formula uses d*+1 while the prose suggests d*, and the reported EDD values actually match the d*+1 version. Rather than changing all the existing values, I should keep the formula consistent with method.tex but add the detailed explanation the task wants: clarifying what AUC(d, d+1) represents and explaining the threshold T parameter.

The task is asking me to add the formal equation directly to atlas.tex along with these explanations, since it currently just references the methods section. I'll present the d*+1 formula there with the intuitive meaning and parameter definitions to make it clearer without breaking consistency with the reported results. Both interpretations are mathematically valid, but the formula from method.tex aligns with the paper's reported values, so I'll stick with that. Now I need to plan the three main changes: first, I'll enhance the EDD definition in atlas.tex by adding the formal equation and explaining the threshold T and AUC metric with its intuitive meaning. Since method.tex already has the labeled equation, I should reproduce or reference it prominently in atlas.tex itself rather than just pointing to the methods section.

For the second change, I need to add a comparison table in the End-to-End Learning subsection of generalization.tex—the section exists but currently only mentions DeBERTa and RoBERTa results in prose, so I'll formalize this with a table and include discussion of architecture bias and feature overlap. Finally, I need to address the z-score recovery claims scattered across the document: the abstract correctly states z-score normalization cannot resolve the issue, but the introduction appears to claim it can recover something, which needs clarification or removal. Looking back at the task requirements, I need to distinguish between claims about non-temperature holdouts (where z-score normalization does help) versus temperature-specific cases (where it fails). The introduction's statement about non-temperature holdouts is actually accurate and doesn't contradict the experimental findings, so it should stay. The key issue is ensuring no claims suggest z-score recovers performance on the temperature holdout case, which the generalization section already correctly frames as a failure. I'm noticing the introduction.tex uses "recovers" which might overstate what z-score normalization actually does. The paper_framing clarifies that while z-score improves overall LR accuracy, it doesn't actually recover the d1v2 AUC performance—those numbers still drop significantly. So I should reword this to be more precise about what's actually being recovered versus what remains unresolved. C. But the introduction says "recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89)". 

Wait, is the distinction here:
- For non-temperature holdouts (nucleus, topk): z-score does improve d1v2 AUC (0.61-0.89)
- For temperature holdout: z-score makes d1v2 AUC worse (0.50→0.24, 0.50→0.19)

The introduction text is actually distinguishing these two cases. Is it wrong? Looking at the generalization.tex more carefully, line 108:
"Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion"

Here is the next thinking you need to rewrite:

This seems like a factual claim that z-score helps for non-temperature holdouts. Is this true? Let me check the paper_framing.md decision D021. The task specifically mentions temp09 holdout, so the non-temperature holdout claim might be acceptable. But re-reading issue 3 more carefully, the directive is to find and remove or rewrite any claims about "z-score normalization recovers LR cross-strategy d1v2 AUC" across all .tex files. So I need to search systematically for these claims and address them.

Looking at introduction.tex line 31, it says "Z-score normalization recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89)". This uses "recovers" for non-temperature holdouts specifically. The generalization.tex line 108 has similar language: "Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-k holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion".

The key question is whether these claims are accurate or misleading. The task wants me to be careful about framing. Let me check what the actual experimental results show and whether "recovers" or "improves" is the right word choice here.

I need to search all .tex files for variations of this claim and determine which ones need to be rewritten based on the experimental evidence. I'm settling on the framing that z-score normalization does improve overall cross-strategy accuracy substantially (from 25% to 61%), but crucially it fails to recover the temperature-induced d1v2 inversion—this confirms the issue stems from a genuine geometric shift in the model's representation space rather than just a scale artifact. Let me verify this narrative is consistent across the abstract and discussion sections.

Now I'm planning the concrete edits needed. First, I'll expand the EDD definition in atlas.tex by restating the formal equation from the methods section and clarifying the T=0.75 default and what AUC(d, d+1) measures. Then I need to add an end-to-end baseline table to the generalization section to show how the model performs on held-out strategies without any of the EDD modifications. I need to incorporate the architectural bias gap, feature correlation analysis, and the broader conclusion about hand-crafted features outperforming neural approaches. Since lines 115-119 already cover this in prose, I'll add the formal table to Section 5.4 and make sure the analysis points are clearly presented alongside it. I should check whether RF and DeepSeek are already documented in Table 3 to avoid duplication.

The clearest path forward is creating a new table in Section 5.4 that directly compares end-to-end learning against feature-based methods, incorporating DeBERTa and RoBERTa to demonstrate that architecture choice doesn't explain the performance gap. I'll pair this with the existing prose about feature overlap and add the key insight that hand-crafted features capture depth signals that PLMs struggle to extract from raw text alone.

For the z-score claims, I need to revisit the introduction and generalization sections—reframing the language in introduction.tex line 31 and adding concrete LR accuracy numbers to generalization.tex to strengthen the argument.

Now I'm working through the EDD definition in atlas.tex. The current single sentence is too terse, so I'm expanding it to properly introduce the concept, explain what the threshold T represents, clarify how the pairwise AUC between adjacent depths works, and provide the intuition for why this metric matters. a scalar metric summarizing how far into a recursive chain adjacent depths remain distinguishable.

For each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary Random Forest classifier (500 trees, 5-fold stratified CV) and compute the pairwise ROC AUC, denoted $\mathrm{AUC}(d, d{+}1)$.
Given a discrimination threshold $T$, we define:
\begin{equation}
\mathrm{EDD}_T = \max \{ d^*{+}1 : \mathrm{AUC}(d^*, d^*{+}1) \geq T \}
\label{eq:edd_atlas}
\end{equation}
where $d^* \in \{0, 1, \dots, K{-}1\}$.
Intuitively, $\mathrm{EDD}_T$ represents the deepest generation where we can still reliably distinguish it from the previous one; past that point, adjacent depths become statistically indistinguishable. I'm setting the default threshold to 0.75 as a reasonable midpoint for classifier performance, and I'll also report results across a range of thresholds to show sensitivity. Let me check if atlas.tex references the equation from method.tex at all... No, it just says "(defined in \S\ref{sec:method})". 

I think the cleanest approach is to have the formal definition here in atlas.tex and reference it from method.tex, or have it in both places. Since both sections discuss EDD, having the equation in the atlas section where it's actually used makes sense. I could use the same label or a different one, but that gets complicated with duplicates. Actually, the task specifically asks for the definition in atlas.tex, so let me enhance that section with a more complete inline definition and explanatory text, then reference the numbered equation from method.tex rather than duplicating it. I'm defining the EDD formula where T is a discrimination threshold, with the intuition that EDD_T represents the deepest depth level where the classifier can still reliably distinguish adjacent generations—beyond which they become statistically indistinguishable. I'm setting T=0.75 as the default (the midpoint between random chance and perfect discrimination) and planning to report sensitivity across multiple threshold values.

Now I need to add a results table to Section 5.4 on end-to-end learning. The existing prose describes DeBERTa and RoBERTa achieving around 59% accuracy on Pythia-1.4B nucleus data through 5-fold cross-validation, which is about 19 percentage points below the feature-based baseline. I'll structure this as a table to present the results more clearly.

The analysis shows both models excel at separating the shallowest depth level (d0) with F1 scores above 0.95, but struggle significantly with adjacent-depth discrimination where F1 drops below 0.42—exactly where the statistical features like p90_ppl and var_surprisal perform well. The small 1.2 percentage point gap between the two backbones rules out model selection as an explanation. I'm also noting that DCOL with RoBERTa-large performed worse overall, with instability across most runs. The probing analysis reveals an interesting negative correlation between what the transformer attends to and what matters for the random forest classifier, suggesting the models focus on lexical patterns rather than the depth-relevant features. Generating the results table...

Both RoBERTa and DeBERTa converge around 59% accuracy with minimal architectural differences, but they struggle with adjacent-depth discrimination where the hand-crafted statistical features shine. A larger RoBERTa model with DCOL performed even worse, suggesting the issue isn't just model scale.

Looking at the feature overlap, there's a striking negative correlation between what the attention mechanism prioritizes and what matters for the random forest classifier—the top features don't overlap at all. The PLMs are drawn to surface-level lexical patterns like type-token ratio and repeated bigrams, but they completely miss the perplexity distribution statistics that are actually driving the depth signal. This confirms that the statistical features capture something fundamental about depth that raw text alone can't teach these models, especially those tail properties in the distribution that are the real markers of depth. I see that DeepSeek is already in the baselines table, so including it again in the new results table might feel repetitive, but the task explicitly asks for this format. For the z-score normalization issue, I need to revise the introduction to clarify that while z-score improves overall logistic regression accuracy across strategies, it doesn't actually resolve the temperature-induced inversion in d1v2—this points to a genuine covariate shift structure rather than just a normalization problem.

Now looking at the generalization section, I'm noticing a discrepancy: the task mentions that z-score normalization is actually ineffective or even harmful for the temperature holdout d1v2 AUC, which contradicts the current claim that it "substantially improves" performance for non-temperature holdouts.

Checking the paper framing more carefully—it says z-score improves overall logistic regression accuracy but fails to recover pairwise d1v2 AUC, with the specific numbers (0.50→0.24, 0.50→0.19) pointing to temperature holdout results. So the current generalization.tex statement needs revision to clarify that the improvement claim only applies to non-temperature cases, while the temperature holdout shows the actual failure pattern. I need to revise the introduction to emphasize the overall accuracy improvement (25%→61%) rather than the specific d1v2 AUC numbers, and make clear that z-score doesn't resolve the temperature inversion. The generalization section can keep its detailed analysis since it's properly caveated, but I should consider adding those overall accuracy figures there too for consistency. Let me reframe the introduction claim to be more measured while still acknowledging what z-score actually accomplishes. I'm revising the section on z-score normalization to better frame the hypothesis and results. The key insight is that while normalization improves cross-strategy accuracy substantially (25% to 61%), it fails to recover the temperature-induced inversion in the d1/d2 metric across multiple models, which demonstrates this is a genuine geometric shift in feature space rather than just a scaling issue. I want to keep the citation about covariate shift and structure it as a natural hypothesis that gets tested and rejected by the empirical results. RF, z-normalization leaves accuracy essentially unchanged (59.1\% $\to$ 59.2\%) and does not improve d1v2 AUC ($\Delta < 0.02$), as expected since tree splits depend on feature rank order, not scale. Z-score standardization substantially improves logistic regression cross-strategy accuracy from 25\% to 61\%, with gains on nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89). Yet it fails to resolve the temperature-induced inversion—AUC actually worsens under z-normalization (Pythia 0.52, GPT-2 XL 0.50$\to$0.24, OLMo 0.50$\to$0.19)—suggesting that temperature decoding creates a fundamental shift in feature geometry that linear rescaling cannot undo. I'm seeing that the current rewritten thinking uses "recovers" in a way that's too broad—it should be more precise about what z-score normalization actually fixes. The next thinking clarifies that the introduction needs to drop the "recovers" framing entirely and instead focus on the overall accuracy jump (25% to 61%), while the detailed results section can keep the nuanced claim about non-temperature holdouts since that's where the distinction is properly explained. I should also add the before-and-after numbers for temperature decoding to strengthen the conclusion about the geometric shift being irreducible by linear rescaling. not a correctable scale difference—it's a fundamental shift in the feature geometry that linear transformations can't fix.

Wait, let me reconsider the data. Pythia shows 0.50 to 0.52, which is essentially flat. The task specifies GPT-2 XL drops from 0.50 to 0.24 and OLMo from 0.50 to 0.19. So z-score normalization fails dramatically for those two models while barely helping Pythia. The before-and-after format makes this clearer: GPT-2 XL 0.50→0.24, OLMo 0.50→0.19, Pythia 0.50→0.52. This shows the normalization doesn't resolve the inversion problem across the board. I'm working through the edits systematically now. For the first change in atlas.tex, I need to identify the exact boundaries of the section on Effective Discriminable Depth and replace the incomplete thought about how aggregate accuracy masks certain phenomena with a clearer statement about what EDD actually measures and why it matters for understanding model behavior across different decoding strategies. I'm defining EDD formally as the maximum depth where the pairwise classifier achieves an AUC above threshold T, meaning it's the deepest level where we can still reliably distinguish adjacent generations before they become statistically indistinguishable.

For the experiments, I'm using T=0.75 as the default threshold—positioned midway between random chance and perfect discrimination—and also testing sensitivity across T values of 0.65, 0.70, 0.75, and 0.80.

Now I'm setting up the end-to-end baseline by training DeBERTa-v3-base and RoBERTa-base on Pythia-1.4B nucleus data with standard hyperparameters and 5-fold cross-validation, both achieving around 59% accuracy.

The results show both models perform well on the easiest task but struggle significantly with adjacent-depth discrimination where the hand-crafted features shine, and there's a notable negative correlation between attention patterns and feature importance, suggesting the models may be learning different representations than what the features capture. The results show that both RoBERTa and DeBERTa actually underperform the random forest baseline by roughly 19 percentage points when finetuned end-to-end on raw text, suggesting that pretrained language models struggle to capture depth signals without explicit feature engineering. Looking at the feature overlap analysis, there's a striking disconnect between what the language models attend to and what actually matters for the task. The attention weights in DeBERTa show almost no alignment with the random forest's feature importance rankings, and when I probe the PLM representations directly, they capture surface-level lexical patterns beautifully but completely miss the statistical properties that drive depth discrimination. The hand-crafted features like variance in surprisal and the 90th percentile perplexity are doing the real work here—they're picking up on distributional tail characteristics that the models simply can't extract from raw text.

Now I'm examining how z-score normalization affects the cross-strategy generalization. Standardizing the features does help logistic regression transfer across different sampling strategies, pushing accuracy from 25% up to 61% overall. But it doesn't touch the core problem: the temperature-induced inversion where model performance actually reverses between the two depth conditions. GPT-2 XL drops from 0.50 to 0.24, and OLMo falls from 0.50 to 0.19. This tells me the issue isn't just a scale mismatch that normalization can fix—it's a genuine shift in the underlying geometry of the representation space. I'm now executing all four edits to refine the analysis and presentation of these findings about temperature-induced feature space shifts.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "381725c8-9696-4ee2-b0d2-ab1aa87fc991",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R79WBLxayrg3uUrSoYJZJi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 39668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1374
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

_source line 29_

Now I have all the context. Executing all four edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "f3181526-7ca7-4215-8159-9c7386804770",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R79WBLxayrg3uUrSoYJZJi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 39668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1374
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

<details open><summary>🔧 Tool call — Edit · `toolu_01ERN3tkCYqAMhwNxg4UTkLd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "old_string": "\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe formalize this via the \\emph{Effective Discriminable Depth} (EDD; defined in \\S\\ref{sec:method}): $\\mathrm{EDD}_T$ is the maximum depth $d^*$ such that the pairwise AUC between $d^*$ and $d^*{+}1$ exceeds a threshold $T$, using a dedicated binary RF per adjacent pair.",
  "new_string": "\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFor each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$---the ROC AUC of this pairwise classifier at separating depth-$d$ from depth-$(d{+}1)$ samples.\nGiven a discrimination threshold $T$, EDD is defined as:\n\\[\n\\mathrm{EDD}_T = \\max \\bigl\\{ d^*{+}1 : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T \\bigr\\}\n\\]\nwhere $d^* \\in \\{0, 1, \\dots, K{-}1\\}$.\nIntuitively, $\\mathrm{EDD}_T$ is the deepest generation depth at which the classifier can still reliably separate it from the preceding depth; beyond this boundary, adjacent depths become statistically indistinguishable.\nWe set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "788f3ea5-7565-4c2b-99a2-63a6d51db2ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R79WBLxayrg3uUrSoYJZJi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 39668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1374
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

_source line 31 · 2026-05-15T13:42:41.216Z_

<details><summary>↩ Tool result · `toolu_01ERN3tkCYqAMhwNxg4UTkLd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "898bb2ea-da7d-4b1d-9b6d-75379e67c22e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
    "oldString": "\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe formalize this via the \\emph{Effective Discriminable Depth} (EDD; defined in \\S\\ref{sec:method}): $\\mathrm{EDD}_T$ is the maximum depth $d^*$ such that the pairwise AUC between $d^*$ and $d^*{+}1$ exceeds a threshold $T$, using a dedicated binary RF per adjacent pair.",
    "newString": "\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFor each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$---the ROC AUC of this pairwise classifier at separating depth-$d$ from depth-$(d{+}1)$ samples.\nGiven a discrimination threshold $T$, EDD is defined as:\n\\[\n\\mathrm{EDD}_T = \\max \\bigl\\{ d^*{+}1 : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T \\bigr\\}\n\\]\nwhere $d^* \\in \\{0, 1, \\dots, K{-}1\\}$.\nIntuitively, $\\mathrm{EDD}_T$ is the deepest generation depth at which the classifier can still reliably separate it from the preceding depth; beyond this boundary, adjacent depths become statistically indistinguishable.\nWe set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below.",
    "originalFile": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\\times$ 3 decoding strategies $\\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.\nFor each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \\S\\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.\n\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:indist}\n\nTable~\\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.\nAll 9 cells exceed chance (25\\%) by a wide margin, with accuracy ranging from 69.6\\% to 85.4\\%.\nBoth model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.\nTop-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{In-distribution 4-class depth estimation accuracy (\\%) across 3 model families $\\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\\%.}\n\\label{tab:main_matrix}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Nucleus & Temp & Top-$k$ \\\\\n & $p{=}0.95$ & $\\tau{=}0.9$ & $k{=}50$ \\\\\n\\midrule\nPythia-1.4B & 78.2 & 76.3 & 69.6 \\\\\nOLMo-1B & 78.8 & 82.0 & 74.2 \\\\\nGPT-2 XL & 83.3 & \\textbf{85.4} & 76.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBecause the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.\nPerformance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\\%, and even the weakest setting (Pythia nucleus) retains 70.8\\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.\n\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nTo identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\\ref{app:permutation}).\nFigure~\\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.\n\nTwo features dominate.\nThe 90th-percentile perplexity (\\textsc{p90\\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\\textsc{var\\_surprisal}) does so in 7 of 9.\nIn the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\\textsc{p75\\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.\nTo quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\\binom{9}{2}=36$ cell pairs and obtain a mean $\\rho = 0.868$ (range: 0.619--0.954).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}\n\\caption{Feature importance heatmap across 9 cells (3 models $\\times$ 3 strategies). Top-7 features by mean importance. \\textsc{p90\\_ppl} appears in the top 2 for all cells; \\textsc{var\\_surprisal} for 7 of 9.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\nThese results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.\nThe universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe formalize this via the \\emph{Effective Discriminable Depth} (EDD; defined in \\S\\ref{sec:method}): $\\mathrm{EDD}_T$ is the maximum depth $d^*$ such that the pairwise AUC between $d^*$ and $d^*{+}1$ exceeds a threshold $T$, using a dedicated binary RF per adjacent pair.\n\nWithin the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.\n\nTo probe deeper, we extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair (we increase from 200 to 500 trees for binary classifiers to ensure convergence on the smaller per-pair sample sizes).\nFigure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.\nThe d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.\nSubsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.\nAt d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling below the threshold and fixing $\\mathrm{EDD}_{0.75}=4$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\\% bootstrap CI. Dashed line: $T{=}0.75$. $\\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\\,vs.\\,d4 remain discriminable.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$.\nAt $T{=}0.80$, only d1\\,vs.\\,d2 and d2\\,vs.\\,d3 pass, yielding $\\mathrm{EDD}=3$.\nThe d0\\,vs.\\,d1 pair passes at every threshold ($\\text{AUC}\\geq0.99$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \\checkmark: pairwise AUC $\\geq T$; ---: below $T$. d0\\,vs.\\,d1 always passes (AUC$\\geq$0.99) and is omitted.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccccr}\n\\toprule\n$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\\\\n\\midrule\n0.65 & \\checkmark & \\checkmark & \\checkmark & \\checkmark & 5 \\\\\n0.70 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.75 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.80 & \\checkmark & \\checkmark & --- & --- & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granularity ablation.}\nDecision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.\n\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:trajectories}\n\nThe atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.\nFigure~\\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}\n\\caption{Normalized feature trajectories across generation depths for 3 models $\\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\\ref{app:topk_trajectories}.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n\\paragraph{Non-uniform inter-depth spacing.}\nFor Pythia nucleus, \\textsc{p90\\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\\% reduction.\nThis geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.\n\n\\paragraph{Temperature-induced acceleration.}\nTemperature sampling ($\\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \\citet{marchi2024_heat_death}.\nConcretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.\nThis shift yields higher in-distribution accuracy (Table~\\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\\S\\ref{sec:generalization}).\n\n\\paragraph{Three-tier strategy taxonomy.}\nThe trajectory data suggests a functional classification.\nNucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.\nTemperature sampling ($\\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.\nTop-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.\nNotably, top-$k$ preserves the \\emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\\S\\ref{sec:generalization}).",
    "structuredPatch": [
      {
        "oldStart": 57,
        "oldLines": 7,
        "newStart": 57,
        "newLines": 15,
        "lines": [
          " \\label{sec:atlas:edd}",
          " ",
          " Aggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.",
          "-We formalize this via the \\emph{Effective Discriminable Depth} (EDD; defined in \\S\\ref{sec:method}): $\\mathrm{EDD}_T$ is the maximum depth $d^*$ such that the pairwise AUC between $d^*$ and $d^*{+}1$ exceeds a threshold $T$, using a dedicated binary RF per adjacent pair.",
          "+We quantify this via the \\emph{Effective Discriminable Depth} (EDD).",
          "+For each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$---the ROC AUC of this pairwise classifier at separating depth-$d$ from depth-$(d{+}1)$ samples.",
          "+Given a discrimination threshold $T$, EDD is defined as:",
          "+\\[",
          "+\\mathrm{EDD}_T = \\max \\bigl\\{ d^*{+}1 : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T \\bigr\\}",
          "+\\]",
          "+where $d^* \\in \\{0, 1, \\dots, K{-}1\\}$.",
          "+Intuitively, $\\mathrm{EDD}_T$ is the deepest generation depth at which the classifier can still reliably separate it from the preceding depth; beyond this boundary, adjacent depths become statistically indistinguishable.",
          "+We set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below.",
          " ",
          " Within the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_012Vk7JUj4vqWknbfHS7ZWB9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
  "old_string": "\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nWe train DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nBoth achieve ${\\sim}$59\\% (DeBERTa 58.3$\\pm$4.7\\%, RoBERTa 59.5$\\pm$3.2\\%), 19pp below feature-based classifiers (78.2\\%).\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nThe 1.2pp inter-backbone gap rules out model selection bias.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\nProbing reveals a negative correlation between DeBERTa attention importance and RF permutation importance ($\\rho{=}{-}0.48$, $p{=}0.036$; top-5 Jaccard$\\,{=}\\,0$): transformers attend to lexical patterns (TTR, repeated bigrams) while RF relies on perplexity tail statistics, confirming complementary---not redundant---representations.",
  "new_string": "\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nTo test whether pretrained language models can learn depth signals directly from raw text, we finetune DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nTable~\\ref{tab:e2e_baselines} summarizes the comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{End-to-end baseline comparison on Pythia-1.4B nucleus. RF uses 19 hand-crafted statistical features; PLM baselines are finetuned on raw text. 5-fold CV (std where shown). Chance = 25\\%.}\n\\label{tab:e2e_baselines}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & 4-class Acc (\\%) & $\\Delta$ vs RF \\\\\n\\midrule\nRF (19 features) & 78.2 & --- \\\\\nRoBERTa-base finetune & 59.5 $\\pm$ 3.2 & $-$18.7pp \\\\\nDeBERTa-v3-base finetune & 58.3 $\\pm$ 4.7 & $-$19.9pp \\\\\nDeepSeek V3.2 (zero-shot) & 40.0 & $-$38.2pp \\\\\nChance & 25.0 & $-$53.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth PLM architectures---masked language modeling (RoBERTa) and disentangled attention (DeBERTa)---converge to ${\\sim}$59\\%, with the 1.2pp inter-backbone gap ruling out architecture selection bias.\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\n\n\\paragraph{Feature overlap analysis.}\nProbing reveals a significant negative correlation between DeBERTa attention importance and RF permutation importance (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.\nThis confirms that hand-crafted statistical features capture depth signals that PLMs cannot learn from raw text alone, particularly the distributional tail properties that constitute the dominant depth markers (\\S\\ref{sec:atlas:features})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "c5ebb777-af00-4e0a-b6d7-297e63090e14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R79WBLxayrg3uUrSoYJZJi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 39668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1374
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

_source line 33 · 2026-05-15T13:42:50.625Z_

<details><summary>↩ Tool result · `toolu_012Vk7JUj4vqWknbfHS7ZWB9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "b00756a7-cd66-49c6-b464-450c03131977",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
    "oldString": "\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nWe train DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nBoth achieve ${\\sim}$59\\% (DeBERTa 58.3$\\pm$4.7\\%, RoBERTa 59.5$\\pm$3.2\\%), 19pp below feature-based classifiers (78.2\\%).\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nThe 1.2pp inter-backbone gap rules out model selection bias.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\nProbing reveals a negative correlation between DeBERTa attention importance and RF permutation importance ($\\rho{=}{-}0.48$, $p{=}0.036$; top-5 Jaccard$\\,{=}\\,0$): transformers attend to lexical patterns (TTR, repeated bigrams) while RF relies on perplexity tail statistics, confirming complementary---not redundant---representations.",
    "newString": "\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nTo test whether pretrained language models can learn depth signals directly from raw text, we finetune DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nTable~\\ref{tab:e2e_baselines} summarizes the comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{End-to-end baseline comparison on Pythia-1.4B nucleus. RF uses 19 hand-crafted statistical features; PLM baselines are finetuned on raw text. 5-fold CV (std where shown). Chance = 25\\%.}\n\\label{tab:e2e_baselines}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & 4-class Acc (\\%) & $\\Delta$ vs RF \\\\\n\\midrule\nRF (19 features) & 78.2 & --- \\\\\nRoBERTa-base finetune & 59.5 $\\pm$ 3.2 & $-$18.7pp \\\\\nDeBERTa-v3-base finetune & 58.3 $\\pm$ 4.7 & $-$19.9pp \\\\\nDeepSeek V3.2 (zero-shot) & 40.0 & $-$38.2pp \\\\\nChance & 25.0 & $-$53.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth PLM architectures---masked language modeling (RoBERTa) and disentangled attention (DeBERTa)---converge to ${\\sim}$59\\%, with the 1.2pp inter-backbone gap ruling out architecture selection bias.\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\n\n\\paragraph{Feature overlap analysis.}\nProbing reveals a significant negative correlation between DeBERTa attention importance and RF permutation importance (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.\nThis confirms that hand-crafted statistical features capture depth signals that PLMs cannot learn from raw text alone, particularly the distributional tail properties that constitute the dominant depth markers (\\S\\ref{sec:atlas:features}).",
    "originalFile": "\\section{Generalization and Robustness}\n\\label{sec:generalization}\n\nThe atlas (\\S\\ref{sec:atlas}) established in-distribution accuracy of 69.6--85.4\\%.\nWe now test whether these results reflect genuine statistical regularities or artifacts of specific training conditions, evaluating four axes: classifier choice (\\S\\ref{sec:gen:baselines}), cross-model transfer (\\S\\ref{sec:gen:crossmodel}), cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}), and end-to-end learned representations (\\S\\ref{sec:gen:dcol}).\n\n\\subsection{Baseline Comparison}\n\\label{sec:gen:baselines}\n\nTable~\\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.\nThree feature-based methods---Random Forest (RF), CORAL ordinal regression \\cite{coral2020}, and DivEye \\cite{diveye2026}---all operate on the same 19 statistical features and achieve statistically indistinguishable accuracy (78.1--78.2\\%; pairwise bootstrap $p>0.05$ after Bonferroni correction, 95\\% CI within $\\pm$1.1pp).\nThese three significantly outperform CE-MLP ($p<0.001$, $+$3.8pp), which in turn trails logistic regression by $\\sim$0.1pp.\nSingle-feature regression on mean perplexity performs at chance (25.1\\%), confirming that depth estimation requires the multi-dimensional feature representation defined in \\S\\ref{sec:method}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Comparison of classification methods on Pythia-1.4B nucleus. RF, CORAL, and DivEye use the same 19 statistical features and are statistically indistinguishable (bootstrap $p>0.05$, Bonferroni-corrected). Chance = 25\\%. 5-fold CV std: 0.2--0.9pp across all methods.}\n\\label{tab:baselines}\n\\begin{tabular}{lc}\n\\toprule\nMethod & 4-class Acc (\\%) \\\\\n\\midrule\nRF (19 features) & 78.2 \\\\\nCORAL & 78.1 \\\\\nDivEye & 78.2 \\\\\nCE-MLP & 74.9 \\\\\nLR & 75.0 \\\\\nDeepSeek V3.2 (zero-shot)\\footnotemark & 40.0 \\\\\nppl-regression (single feature) & 25.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\footnotetext{Evaluated on 200 samples (approximately 50 per class) from the Pythia-1.4B nucleus cell only, due to API cost; 95\\% CI: $\\pm$6.8pp. All other methods use the full 20{,}000-sample set.}\n\\end{table}\n\nThat three structurally different classifiers (tree ensemble, ordinal regression, diversity-based) achieve identical performance on the same features confirms that the discriminative signal resides in the 19 statistical features, not the classifier architecture.\nA zero-shot LLM baseline (DeepSeek V3.2) achieves 40.0\\%---above chance but 38 points below feature-based methods.\nFigure~\\ref{fig:confusion_matrix} shows that d0 is near-perfectly identified in both settings; in-distribution errors concentrate at the d2/d3 boundary, while cross-model transfer spreads confusion more broadly across d1--d3.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_confusion_matrix.pdf}\n\\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\\tau{=}0.9$, 85.4\\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\\%). d0 recall exceeds 99\\% in both; errors spread across the d1--d3 range under transfer.}\n\\label{fig:confusion_matrix}\n\\end{figure}\n\n\\subsection{Cross-Model Transfer}\n\\label{sec:gen:crossmodel}\n\nTo test whether depth fingerprints generalize across architectures, we perform leave-one-model-family-out evaluation: train on two model families (nucleus sampling only) and test on the held-out third.\nTable~\\ref{tab:cross_model} reports results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model transfer (leave-one-out, nucleus only). Train on 2 model families, test on held-out 3rd. Chance = 25\\%.}\n\\label{tab:cross_model}\n\\begin{tabular}{lccccc}\n\\toprule\nHoldout & Acc & d0 & d1 & d2 & d3 \\\\\n & (\\%) & Rec. & Rec. & Rec. & Rec. \\\\\n\\midrule\nPythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\\\\nOLMo & \\textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\\\\nGPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\\\\n\\midrule\nMean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean transfer accuracy reaches 66.4\\% (2.7$\\times$ chance).\nThe per-class breakdown reveals that d0 recall ($>$98\\%) inflates headline accuracy; d2 recall drops as low as 26.8\\% (Pythia holdout), making it the most confusable class.\nPythia is the hardest holdout (62.4\\%) and OLMo the easiest (69.2\\%).\n\n\\subsection{Cross-Strategy Transfer}\n\\label{sec:gen:crossstrategy}\n\nWe next train on two decoding strategies and test on the held-out third.\nTable~\\ref{tab:cross_strategy} reports per-model results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-strategy transfer (leave-one-out). Train on 2 strategies, test on held-out 3rd. Chance = 25\\%.}\n\\label{tab:cross_strategy}\n\\begin{tabular}{lccc}\n\\toprule\nHoldout & Pythia & OLMo & GPT-2 XL \\\\\n & Acc (\\%) & Acc (\\%) & Acc (\\%) \\\\\n\\midrule\nnucleus & \\textbf{69.4} & \\textbf{65.4} & \\textbf{59.9} \\\\\ntemp ($\\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\\\\ntop-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean cross-strategy accuracy (59.1\\%) falls 7 points below cross-model transfer (66.4\\%), indicating that strategy-induced distribution shifts pose a greater generalization challenge than architectural differences.\n\n\\paragraph{Temperature-induced boundary inversion.}\nTraining on nucleus + top-$k$ and testing on temperature yields d1v2 AUC of 0.129 for GPT-2~XL and 0.253 for OLMo---both below 0.5, indicating that the d1/d2 decision boundary \\emph{inverts} (Pythia retains a degraded 0.576).\nThis follows from the trajectory analysis in \\S\\ref{sec:atlas}: temperature sampling shifts feature values at depth $d$ toward depth $d{+}1$ under nucleus/top-$k$.\n\n\\paragraph{Z-score normalization does not resolve the inversion.}\nA natural hypothesis is that per-feature z-score normalization might correct this covariate shift \\cite{sugiyama2007_importance_weighting}.\nFor RF, z-normalization leaves accuracy essentially unchanged (59.1\\% $\\to$ 59.2\\%) and does not improve d1v2 AUC ($\\Delta < 0.02$), as expected since tree splits depend on feature rank order, not scale.\nZ-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).\nThis two-layer structure---scale shift addressable by normalization, plus a deeper geometric shift specific to temperature sampling---suggests that temperature decoding induces qualitatively different feature distributions that cannot be reconciled by linear rescaling.\n\n\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nWe train DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nBoth achieve ${\\sim}$59\\% (DeBERTa 58.3$\\pm$4.7\\%, RoBERTa 59.5$\\pm$3.2\\%), 19pp below feature-based classifiers (78.2\\%).\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nThe 1.2pp inter-backbone gap rules out model selection bias.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\nProbing reveals a negative correlation between DeBERTa attention importance and RF permutation importance ($\\rho{=}{-}0.48$, $p{=}0.036$; top-5 Jaccard$\\,{=}\\,0$): transformers attend to lexical patterns (TTR, repeated bigrams) while RF relies on perplexity tail statistics, confirming complementary---not redundant---representations.",
    "structuredPatch": [
      {
        "oldStart": 111,
        "oldLines": 9,
        "newStart": 111,
        "newLines": 32,
        "lines": [
          " \\subsection{End-to-End Learning}",
          " \\label{sec:gen:dcol}",
          " ",
          "-We train DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.",
          "-Both achieve ${\\sim}$59\\% (DeBERTa 58.3$\\pm$4.7\\%, RoBERTa 59.5$\\pm$3.2\\%), 19pp below feature-based classifiers (78.2\\%).",
          "+To test whether pretrained language models can learn depth signals directly from raw text, we finetune DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.",
          "+Table~\\ref{tab:e2e_baselines} summarizes the comparison.",
          "+",
          "+\\begin{table}[t]",
          "+\\centering",
          "+\\small",
          "+\\caption{End-to-end baseline comparison on Pythia-1.4B nucleus. RF uses 19 hand-crafted statistical features; PLM baselines are finetuned on raw text. 5-fold CV (std where shown). Chance = 25\\%.}",
          "+\\label{tab:e2e_baselines}",
          "+\\begin{tabular}{lcc}",
          "+\\toprule",
          "+Method & 4-class Acc (\\%) & $\\Delta$ vs RF \\\\",
          "+\\midrule",
          "+RF (19 features) & 78.2 & --- \\\\",
          "+RoBERTa-base finetune & 59.5 $\\pm$ 3.2 & $-$18.7pp \\\\",
          "+DeBERTa-v3-base finetune & 58.3 $\\pm$ 4.7 & $-$19.9pp \\\\",
          "+DeepSeek V3.2 (zero-shot) & 40.0 & $-$38.2pp \\\\",
          "+Chance & 25.0 & $-$53.2pp \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          "+Both PLM architectures---masked language modeling (RoBERTa) and disentangled attention (DeBERTa)---converge to ${\\sim}$59\\%, with the 1.2pp inter-backbone gap ruling out architecture selection bias.",
          " Both easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.",
          "-The 1.2pp inter-backbone gap rules out model selection bias.",
          " DCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).",
          "-Probing reveals a negative correlation between DeBERTa attention importance and RF permutation importance ($\\rho{=}{-}0.48$, $p{=}0.036$; top-5 Jaccard$\\,{=}\\,0$): transformers attend to lexical patterns (TTR, repeated bigrams) while RF relies on perplexity tail statistics, confirming complementary---not redundant---representations.",
          "\\ No newline at end of file",
          "+",
          "+\\paragraph{Feature overlap analysis.}",
          "+Probing reveals a significant negative correlation between DeBERTa attention importance and RF permutation importance (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).",
          "+PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.",
          "+This confirms that hand-crafted statistical features capture depth signals that PLMs cannot learn from raw text alone, particularly the distributional tail properties that constitute the dominant depth markers (\\S\\ref{sec:atlas:features}).",
          "\\ No newline at end of file"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_014u8zLTC7TGCYVMryihEfHM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
  "old_string": "Z-score normalization recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89) but fails to resolve the temperature-specific inversion, revealing a two-layer covariate shift structure.",
  "new_string": "Z-score normalization improves overall LR cross-strategy accuracy (25\\%$\\to$61\\%) but does not recover the temperature-induced d1/d2 inversion (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19), confirming a genuine geometry-level shift rather than a correctable scale difference."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "53601421-ed66-43cf-8ad3-1a77a1df2ac1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R79WBLxayrg3uUrSoYJZJi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 39668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1374
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

_source line 35 · 2026-05-15T13:42:52.484Z_

<details><summary>↩ Tool result · `toolu_014u8zLTC7TGCYVMryihEfHM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "017e8fdb-8d6b-4668-a75c-08735176ca17",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
    "oldString": "Z-score normalization recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89) but fails to resolve the temperature-specific inversion, revealing a two-layer covariate shift structure.",
    "newString": "Z-score normalization improves overall LR cross-strategy accuracy (25\\%$\\to$61\\%) but does not recover the temperature-induced d1/d2 inversion (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19), confirming a genuine geometry-level shift rather than a correctable scale difference.",
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\nThe text on which large language models are trained increasingly contains their own outputs.\nAs synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \\cite{shumailov2024_nature,alemohammad2024_mad}.\nThis model$\\to$data$\\to$model cycle is no longer hypothetical---it is already occurring in the wild---yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \\cite{dohmatob2024_tale_of_tails}.\n\nExisting tools address adjacent but distinct problems.\nBinary detectors such as Binoculars \\cite{binoculars2024}, Fast-DetectGPT \\cite{fast_detectgpt2024}, and DivEye \\cite{diveye2026} classify text as human-written or machine-generated, collapsing all generation depths $d \\geq 1$ into a single category.\nWatermarking schemes \\cite{kirchenbauer2023_watermark} require proactive embedding and cannot be applied retroactively to existing corpora.\nThe model collapse literature \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails} characterizes how recursive training degrades model quality but assumes the generation depth is known a priori---the very quantity we seek to estimate.\n\\citet{drayson2025_detection_prevents_collapse} show that filtering synthetic data from training corpora can prevent collapse, yet their approach relies on binary detection and does not distinguish among recursive depths.\nEditLens \\cite{editlens2026} estimates the extent of single-pass editing applied to a text but does not address multi-step recursive generation.\nNo existing method estimates the ordinal recursive depth of a text passage from its content alone.\n\nOur key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints exhibit universal stability across model families and decoding strategies.\nSpecifically, perplexity tail statistics---the 90th-percentile perplexity (\\textsc{p90\\_ppl}) and surprisal variance (\\textsc{var\\_surprisal})---emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 7/9 model--strategy configurations, respectively.\n\nWe formalize recursive generation depth estimation as an ordinal classification task and introduce a lightweight pipeline to solve it.\nGiven a text passage, we compute a 19-dimensional feature vector from reference-model perplexity statistics---capturing distributional location, spread, tail behavior, and lexical diversity---and classify it with a Random Forest into one of $K{+}1$ depth classes ($d{=}0$ for human text through $d{=}K$ for $K$-th generation text).\nTo systematically characterize how recursive generation reshapes these features, we construct the \\emph{Depth Degradation Atlas}: a $3 \\times 3$ grid of model families (Pythia-1.4B, OLMo-1B, GPT-2~XL) and decoding strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$, top-$k$ $k{=}50$), each spanning 4 generation depths, totaling 180K samples.\nThe atlas reveals strategy-dependent degradation trajectories---temperature sampling accelerates convergence toward a low-entropy attractor, while top-$k$ attenuates the depth signal---and we introduce the \\emph{Effective Discriminable Depth} (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.\n\nOur contributions are:\n\n\\begin{itemize}\n    \\item \\textbf{Task formalization.} We define recursive generation depth estimation as ordinal classification, distinguishing it from binary detection and single-pass editing estimation. We introduce the EDD metric, which summarizes the maximum depth at which adjacent generations remain separable above a given AUC threshold.\n\n    \\item \\textbf{Depth Degradation Atlas.} We construct a systematic $3 \\times 3$ map across model families and decoding strategies, revealing that \\textsc{p90\\_ppl} ranks in the top 2 in all 9 cells (100\\%) and \\textsc{var\\_surprisal} in 7/9 (78\\%), with a mean Spearman rank correlation of $\\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.\n\n    \\item \\textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\\% mean accuracy and cross-strategy transfer 59.1\\% (chance = 25\\%), demonstrating partial universality of depth fingerprints. We identify a temperature-induced d1/d2 AUC inversion (GPT-2~XL: 0.13, OLMo: 0.25) caused by accelerated convergence. Z-score normalization recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89) but fails to resolve the temperature-specific inversion, revealing a two-layer covariate shift structure.\n\n    \\item \\textbf{End-to-end learning as negative result.} Both DeBERTa-v3-base (58.3\\%) and RoBERTa-base (59.5\\%) achieve ${\\sim}$59\\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\\%)---with the architecture-invariant gap ruling out model selection bias. Probing reveals a significant negative correlation ($\\rho{=}{-}0.48$) between transformer attention and RF feature importance, confirming complementary representations.\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 28,
        "oldLines": 7,
        "newStart": 28,
        "newLines": 7,
        "lines": [
          " ",
          "     \\item \\textbf{Depth Degradation Atlas.} We construct a systematic $3 \\times 3$ map across model families and decoding strategies, revealing that \\textsc{p90\\_ppl} ranks in the top 2 in all 9 cells (100\\%) and \\textsc{var\\_surprisal} in 7/9 (78\\%), with a mean Spearman rank correlation of $\\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.",
          " ",
          "-    \\item \\textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\\% mean accuracy and cross-strategy transfer 59.1\\% (chance = 25\\%), demonstrating partial universality of depth fingerprints. We identify a temperature-induced d1/d2 AUC inversion (GPT-2~XL: 0.13, OLMo: 0.25) caused by accelerated convergence. Z-score normalization recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89) but fails to resolve the temperature-specific inversion, revealing a two-layer covariate shift structure.",
          "+    \\item \\textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\\% mean accuracy and cross-strategy transfer 59.1\\% (chance = 25\\%), demonstrating partial universality of depth fingerprints. We identify a temperature-induced d1/d2 AUC inversion (GPT-2~XL: 0.13, OLMo: 0.25) caused by accelerated convergence. Z-score normalization improves overall LR cross-strategy accuracy (25\\%$\\to$61\\%) but does not recover the temperature-induced d1/d2 inversion (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19), confirming a genuine geometry-level shift rather than a correctable scale difference.",
          " ",
          "     \\item \\textbf{End-to-end learning as negative result.} Both DeBERTa-v3-base (58.3\\%) and RoBERTa-base (59.5\\%) achieve ${\\sim}$59\\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\\%)---with the architecture-invariant gap ruling out model selection bias. Probing reveals a significant negative correlation ($\\rho{=}{-}0.48$) between transformer attention and RF feature importance, confirming complementary representations.",
          " \\end{itemize}",
          "\\ No newline at end of file"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01HgaL75gN8p61EHkXv13HKE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
  "old_string": "Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).\nThis two-layer structure---scale shift addressable by normalization, plus a deeper geometric shift specific to temperature sampling---suggests that temperature decoding induces qualitatively different feature distributions that cannot be reconciled by linear rescaling.",
  "new_string": "Z-score standardization improves overall logistic regression cross-strategy accuracy from 25\\% to 61\\%, with d1v2 AUC gains for nucleus and top-$k$ holdouts (0.61--0.89).\nHowever, it does not recover the temperature-induced d1v2 inversion---AUC worsens for two of three models (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19; Pythia 0.52), confirming that temperature decoding induces a genuine geometry-level shift in feature space rather than a correctable scale difference."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "81e00499-57d8-484b-8241-569200e023a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R79WBLxayrg3uUrSoYJZJi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 39668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1374
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

_source line 37 · 2026-05-15T13:42:55.364Z_

<details><summary>↩ Tool result · `toolu_01HgaL75gN8p61EHkXv13HKE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "1f03024f-774c-450f-9e67-823764c19842",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
    "oldString": "Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).\nThis two-layer structure---scale shift addressable by normalization, plus a deeper geometric shift specific to temperature sampling---suggests that temperature decoding induces qualitatively different feature distributions that cannot be reconciled by linear rescaling.",
    "newString": "Z-score standardization improves overall logistic regression cross-strategy accuracy from 25\\% to 61\\%, with d1v2 AUC gains for nucleus and top-$k$ holdouts (0.61--0.89).\nHowever, it does not recover the temperature-induced d1v2 inversion---AUC worsens for two of three models (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19; Pythia 0.52), confirming that temperature decoding induces a genuine geometry-level shift in feature space rather than a correctable scale difference.",
    "originalFile": "\\section{Generalization and Robustness}\n\\label{sec:generalization}\n\nThe atlas (\\S\\ref{sec:atlas}) established in-distribution accuracy of 69.6--85.4\\%.\nWe now test whether these results reflect genuine statistical regularities or artifacts of specific training conditions, evaluating four axes: classifier choice (\\S\\ref{sec:gen:baselines}), cross-model transfer (\\S\\ref{sec:gen:crossmodel}), cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}), and end-to-end learned representations (\\S\\ref{sec:gen:dcol}).\n\n\\subsection{Baseline Comparison}\n\\label{sec:gen:baselines}\n\nTable~\\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.\nThree feature-based methods---Random Forest (RF), CORAL ordinal regression \\cite{coral2020}, and DivEye \\cite{diveye2026}---all operate on the same 19 statistical features and achieve statistically indistinguishable accuracy (78.1--78.2\\%; pairwise bootstrap $p>0.05$ after Bonferroni correction, 95\\% CI within $\\pm$1.1pp).\nThese three significantly outperform CE-MLP ($p<0.001$, $+$3.8pp), which in turn trails logistic regression by $\\sim$0.1pp.\nSingle-feature regression on mean perplexity performs at chance (25.1\\%), confirming that depth estimation requires the multi-dimensional feature representation defined in \\S\\ref{sec:method}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Comparison of classification methods on Pythia-1.4B nucleus. RF, CORAL, and DivEye use the same 19 statistical features and are statistically indistinguishable (bootstrap $p>0.05$, Bonferroni-corrected). Chance = 25\\%. 5-fold CV std: 0.2--0.9pp across all methods.}\n\\label{tab:baselines}\n\\begin{tabular}{lc}\n\\toprule\nMethod & 4-class Acc (\\%) \\\\\n\\midrule\nRF (19 features) & 78.2 \\\\\nCORAL & 78.1 \\\\\nDivEye & 78.2 \\\\\nCE-MLP & 74.9 \\\\\nLR & 75.0 \\\\\nDeepSeek V3.2 (zero-shot)\\footnotemark & 40.0 \\\\\nppl-regression (single feature) & 25.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\footnotetext{Evaluated on 200 samples (approximately 50 per class) from the Pythia-1.4B nucleus cell only, due to API cost; 95\\% CI: $\\pm$6.8pp. All other methods use the full 20{,}000-sample set.}\n\\end{table}\n\nThat three structurally different classifiers (tree ensemble, ordinal regression, diversity-based) achieve identical performance on the same features confirms that the discriminative signal resides in the 19 statistical features, not the classifier architecture.\nA zero-shot LLM baseline (DeepSeek V3.2) achieves 40.0\\%---above chance but 38 points below feature-based methods.\nFigure~\\ref{fig:confusion_matrix} shows that d0 is near-perfectly identified in both settings; in-distribution errors concentrate at the d2/d3 boundary, while cross-model transfer spreads confusion more broadly across d1--d3.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_confusion_matrix.pdf}\n\\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\\tau{=}0.9$, 85.4\\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\\%). d0 recall exceeds 99\\% in both; errors spread across the d1--d3 range under transfer.}\n\\label{fig:confusion_matrix}\n\\end{figure}\n\n\\subsection{Cross-Model Transfer}\n\\label{sec:gen:crossmodel}\n\nTo test whether depth fingerprints generalize across architectures, we perform leave-one-model-family-out evaluation: train on two model families (nucleus sampling only) and test on the held-out third.\nTable~\\ref{tab:cross_model} reports results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model transfer (leave-one-out, nucleus only). Train on 2 model families, test on held-out 3rd. Chance = 25\\%.}\n\\label{tab:cross_model}\n\\begin{tabular}{lccccc}\n\\toprule\nHoldout & Acc & d0 & d1 & d2 & d3 \\\\\n & (\\%) & Rec. & Rec. & Rec. & Rec. \\\\\n\\midrule\nPythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\\\\nOLMo & \\textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\\\\nGPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\\\\n\\midrule\nMean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean transfer accuracy reaches 66.4\\% (2.7$\\times$ chance).\nThe per-class breakdown reveals that d0 recall ($>$98\\%) inflates headline accuracy; d2 recall drops as low as 26.8\\% (Pythia holdout), making it the most confusable class.\nPythia is the hardest holdout (62.4\\%) and OLMo the easiest (69.2\\%).\n\n\\subsection{Cross-Strategy Transfer}\n\\label{sec:gen:crossstrategy}\n\nWe next train on two decoding strategies and test on the held-out third.\nTable~\\ref{tab:cross_strategy} reports per-model results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-strategy transfer (leave-one-out). Train on 2 strategies, test on held-out 3rd. Chance = 25\\%.}\n\\label{tab:cross_strategy}\n\\begin{tabular}{lccc}\n\\toprule\nHoldout & Pythia & OLMo & GPT-2 XL \\\\\n & Acc (\\%) & Acc (\\%) & Acc (\\%) \\\\\n\\midrule\nnucleus & \\textbf{69.4} & \\textbf{65.4} & \\textbf{59.9} \\\\\ntemp ($\\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\\\\ntop-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean cross-strategy accuracy (59.1\\%) falls 7 points below cross-model transfer (66.4\\%), indicating that strategy-induced distribution shifts pose a greater generalization challenge than architectural differences.\n\n\\paragraph{Temperature-induced boundary inversion.}\nTraining on nucleus + top-$k$ and testing on temperature yields d1v2 AUC of 0.129 for GPT-2~XL and 0.253 for OLMo---both below 0.5, indicating that the d1/d2 decision boundary \\emph{inverts} (Pythia retains a degraded 0.576).\nThis follows from the trajectory analysis in \\S\\ref{sec:atlas}: temperature sampling shifts feature values at depth $d$ toward depth $d{+}1$ under nucleus/top-$k$.\n\n\\paragraph{Z-score normalization does not resolve the inversion.}\nA natural hypothesis is that per-feature z-score normalization might correct this covariate shift \\cite{sugiyama2007_importance_weighting}.\nFor RF, z-normalization leaves accuracy essentially unchanged (59.1\\% $\\to$ 59.2\\%) and does not improve d1v2 AUC ($\\Delta < 0.02$), as expected since tree splits depend on feature rank order, not scale.\nZ-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).\nThis two-layer structure---scale shift addressable by normalization, plus a deeper geometric shift specific to temperature sampling---suggests that temperature decoding induces qualitatively different feature distributions that cannot be reconciled by linear rescaling.\n\n\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nTo test whether pretrained language models can learn depth signals directly from raw text, we finetune DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nTable~\\ref{tab:e2e_baselines} summarizes the comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{End-to-end baseline comparison on Pythia-1.4B nucleus. RF uses 19 hand-crafted statistical features; PLM baselines are finetuned on raw text. 5-fold CV (std where shown). Chance = 25\\%.}\n\\label{tab:e2e_baselines}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & 4-class Acc (\\%) & $\\Delta$ vs RF \\\\\n\\midrule\nRF (19 features) & 78.2 & --- \\\\\nRoBERTa-base finetune & 59.5 $\\pm$ 3.2 & $-$18.7pp \\\\\nDeBERTa-v3-base finetune & 58.3 $\\pm$ 4.7 & $-$19.9pp \\\\\nDeepSeek V3.2 (zero-shot) & 40.0 & $-$38.2pp \\\\\nChance & 25.0 & $-$53.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth PLM architectures---masked language modeling (RoBERTa) and disentangled attention (DeBERTa)---converge to ${\\sim}$59\\%, with the 1.2pp inter-backbone gap ruling out architecture selection bias.\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\n\n\\paragraph{Feature overlap analysis.}\nProbing reveals a significant negative correlation between DeBERTa attention importance and RF permutation importance (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.\nThis confirms that hand-crafted statistical features capture depth signals that PLMs cannot learn from raw text alone, particularly the distributional tail properties that constitute the dominant depth markers (\\S\\ref{sec:atlas:features}).",
    "structuredPatch": [
      {
        "oldStart": 105,
        "oldLines": 8,
        "newStart": 105,
        "newLines": 8,
        "lines": [
          " \\paragraph{Z-score normalization does not resolve the inversion.}",
          " A natural hypothesis is that per-feature z-score normalization might correct this covariate shift \\cite{sugiyama2007_importance_weighting}.",
          " For RF, z-normalization leaves accuracy essentially unchanged (59.1\\% $\\to$ 59.2\\%) and does not improve d1v2 AUC ($\\Delta < 0.02$), as expected since tree splits depend on feature rank order, not scale.",
          "-Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).",
          "-This two-layer structure---scale shift addressable by normalization, plus a deeper geometric shift specific to temperature sampling---suggests that temperature decoding induces qualitatively different feature distributions that cannot be reconciled by linear rescaling.",
          "+Z-score standardization improves overall logistic regression cross-strategy accuracy from 25\\% to 61\\%, with d1v2 AUC gains for nucleus and top-$k$ holdouts (0.61--0.89).",
          "+However, it does not recover the temperature-induced d1v2 inversion---AUC worsens for two of three models (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19; Pythia 0.52), confirming that temperature decoding induces a genuine geometry-level shift in feature space rather than a correctable scale difference.",
          " ",
          " \\subsection{End-to-End Learning}",
          " \\label{sec:gen:dcol}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 38_

四项编辑全部完成。验证改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "15e71636-ed63-40fd-85ef-174e3abd5127",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TmLaab6iqQD85SYHrNJgxj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17662,
      "cache_read_input_tokens": 41042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17662
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

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_017uqqQ3CuLY4v9AULo6hb1V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "offset": 57,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "4327ed23-292f-4b1a-94b6-3735dc583547",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TmLaab6iqQD85SYHrNJgxj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17662,
      "cache_read_input_tokens": 41042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17662
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

_source line 40 · 2026-05-15T13:42:59.299Z_

<details><summary>↩ Tool result · `toolu_017uqqQ3CuLY4v9AULo6hb1V`</summary>

```text
57	\label{sec:atlas:edd}
58	
59	Aggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.
60	We quantify this via the \emph{Effective Discriminable Depth} (EDD).
61	For each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\mathrm{AUC}(d, d{+}1)$---the ROC AUC of this pairwise classifier at separating depth-$d$ from depth-$(d{+}1)$ samples.
62	Given a discrimination threshold $T$, EDD is defined as:
63	\[
64	\mathrm{EDD}_T = \max \bigl\{ d^*{+}1 : \mathrm{AUC}(d^*, d^*{+}1) \geq T \bigr\}
65	\]
66	where $d^* \in \{0, 1, \dots, K{-}1\}$.
67	Intuitively, $\mathrm{EDD}_T$ is the deepest generation depth at which the classifier can still reliably separate it from the preceding depth; beyond this boundary, adjacent depths become statistically indistinguishable.
68	We set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \in \{0.65, 0.70, 0.75, 0.80\}$ below.
69	
70	Within the 4-class atlas (d0--d3), 7 of 9 cells achieve $\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \S\ref{sec:atlas:indist}.
71	
72	To probe deeper, we extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair (we increase from 200 to 500 trees for binary classifiers to ensure convergence on the smaller per-pair sample sizes).
73	Figure~\ref{fig:auc_decay} shows the pairwise AUC decay curve.
74	The d0\,vs.\,d1 boundary is near-perfect (AUC\,=\,0.998), reflecting the well-known human--machine gap.
75	Subsequent boundaries degrade monotonically: d1\,vs.\,d2 achieves 0.925 [95\% CI: 0.914,\,0.935], d2\,vs.\,d3 reaches 0.823 [0.805,\,0.840], and d3\,vs.\,d4 yields 0.784 [0.765,\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.
76	At d4\,vs.\,d5, AUC drops to 0.683 [0.661,\,0.705], falling below the threshold and fixing $\mathrm{EDD}_{0.75}=4$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "a0856063-8000-482e-ab2a-96b793416767",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
      "content": "\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFor each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$---the ROC AUC of this pairwise classifier at separating depth-$d$ from depth-$(d{+}1)$ samples.\nGiven a discrimination threshold $T$, EDD is defined as:\n\\[\n\\mathrm{EDD}_T = \\max \\bigl\\{ d^*{+}1 : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T \\bigr\\}\n\\]\nwhere $d^* \\in \\{0, 1, \\dots, K{-}1\\}$.\nIntuitively, $\\mathrm{EDD}_T$ is the deepest generation depth at which the classifier can still reliably separate it from the preceding depth; beyond this boundary, adjacent depths become statistically indistinguishable.\nWe set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below.\n\nWithin the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.\n\nTo probe deeper, we extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair (we increase from 200 to 500 trees for binary classifiers to ensure convergence on the smaller per-pair sample sizes).\nFigure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.\nThe d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.\nSubsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.\nAt d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling below the threshold and fixing $\\mathrm{EDD}_{0.75}=4$.",
      "numLines": 20,
      "startLine": 57,
      "totalLines": 137
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01RB47uPHNpjiSyQX7qx9vEc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
  "offset": 105,
  "limit": 45
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "a2b86de0-f2a3-4d00-a25e-89869c8d3b2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TmLaab6iqQD85SYHrNJgxj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17662,
      "cache_read_input_tokens": 41042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17662
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

_source line 42 · 2026-05-15T13:43:00.239Z_

<details><summary>↩ Tool result · `toolu_01RB47uPHNpjiSyQX7qx9vEc`</summary>

```text
105	\paragraph{Z-score normalization does not resolve the inversion.}
106	A natural hypothesis is that per-feature z-score normalization might correct this covariate shift \cite{sugiyama2007_importance_weighting}.
107	For RF, z-normalization leaves accuracy essentially unchanged (59.1\% $\to$ 59.2\%) and does not improve d1v2 AUC ($\Delta < 0.02$), as expected since tree splits depend on feature rank order, not scale.
108	Z-score standardization improves overall logistic regression cross-strategy accuracy from 25\% to 61\%, with d1v2 AUC gains for nucleus and top-$k$ holdouts (0.61--0.89).
109	However, it does not recover the temperature-induced d1v2 inversion---AUC worsens for two of three models (GPT-2~XL 0.50$\to$0.24, OLMo 0.50$\to$0.19; Pythia 0.52), confirming that temperature decoding induces a genuine geometry-level shift in feature space rather than a correctable scale difference.
110	
111	\subsection{End-to-End Learning}
112	\label{sec:gen:dcol}
113	
114	To test whether pretrained language models can learn depth signals directly from raw text, we finetune DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\,{=}\,2{\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.
115	Table~\ref{tab:e2e_baselines} summarizes the comparison.
116	
117	\begin{table}[t]
118	\centering
119	\small
120	\caption{End-to-end baseline comparison on Pythia-1.4B nucleus. RF uses 19 hand-crafted statistical features; PLM baselines are finetuned on raw text. 5-fold CV (std where shown). Chance = 25\%.}
121	\label{tab:e2e_baselines}
122	\begin{tabular}{lcc}
123	\toprule
124	Method & 4-class Acc (\%) & $\Delta$ vs RF \\
125	\midrule
126	RF (19 features) & 78.2 & --- \\
127	RoBERTa-base finetune & 59.5 $\pm$ 3.2 & $-$18.7pp \\
128	DeBERTa-v3-base finetune & 58.3 $\pm$ 4.7 & $-$19.9pp \\
129	DeepSeek V3.2 (zero-shot) & 40.0 & $-$38.2pp \\
130	Chance & 25.0 & $-$53.2pp \\
131	\bottomrule
132	\end{tabular}
133	\end{table}
134	
135	Both PLM architectures---masked language modeling (RoBERTa) and disentangled attention (DeBERTa)---converge to ${\sim}$59\%, with the 1.2pp inter-backbone gap ruling out architecture selection bias.
136	Both easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \textsc{p90\_ppl} and \textsc{var\_surprisal} excel.
137	DCOL \cite{cloc2025} with RoBERTa-large fared worse (best 64.5\%, 5/6 runs unstable).
138	
139	\paragraph{Feature overlap analysis.}
140	Probing reveals a significant negative correlation between DeBERTa attention importance and RF permutation importance (Spearman $\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\,{=}\,0$).
141	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\textsc{var\_surprisal} and \textsc{p90\_ppl} yield negative $R^2$ under linear probing.
142	This confirms that hand-crafted statistical features capture depth signals that PLMs cannot learn from raw text alone, particularly the distributional tail properties that constitute the dominant depth markers (\S\ref{sec:atlas:features}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "4be1526c-68c1-47dc-9885-517696d72bd5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
      "content": "\\paragraph{Z-score normalization does not resolve the inversion.}\nA natural hypothesis is that per-feature z-score normalization might correct this covariate shift \\cite{sugiyama2007_importance_weighting}.\nFor RF, z-normalization leaves accuracy essentially unchanged (59.1\\% $\\to$ 59.2\\%) and does not improve d1v2 AUC ($\\Delta < 0.02$), as expected since tree splits depend on feature rank order, not scale.\nZ-score standardization improves overall logistic regression cross-strategy accuracy from 25\\% to 61\\%, with d1v2 AUC gains for nucleus and top-$k$ holdouts (0.61--0.89).\nHowever, it does not recover the temperature-induced d1v2 inversion---AUC worsens for two of three models (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19; Pythia 0.52), confirming that temperature decoding induces a genuine geometry-level shift in feature space rather than a correctable scale difference.\n\n\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nTo test whether pretrained language models can learn depth signals directly from raw text, we finetune DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nTable~\\ref{tab:e2e_baselines} summarizes the comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{End-to-end baseline comparison on Pythia-1.4B nucleus. RF uses 19 hand-crafted statistical features; PLM baselines are finetuned on raw text. 5-fold CV (std where shown). Chance = 25\\%.}\n\\label{tab:e2e_baselines}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & 4-class Acc (\\%) & $\\Delta$ vs RF \\\\\n\\midrule\nRF (19 features) & 78.2 & --- \\\\\nRoBERTa-base finetune & 59.5 $\\pm$ 3.2 & $-$18.7pp \\\\\nDeBERTa-v3-base finetune & 58.3 $\\pm$ 4.7 & $-$19.9pp \\\\\nDeepSeek V3.2 (zero-shot) & 40.0 & $-$38.2pp \\\\\nChance & 25.0 & $-$53.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth PLM architectures---masked language modeling (RoBERTa) and disentangled attention (DeBERTa)---converge to ${\\sim}$59\\%, with the 1.2pp inter-backbone gap ruling out architecture selection bias.\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\n\n\\paragraph{Feature overlap analysis.}\nProbing reveals a significant negative correlation between DeBERTa attention importance and RF permutation importance (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.\nThis confirms that hand-crafted statistical features capture depth signals that PLMs cannot learn from raw text alone, particularly the distributional tail properties that constitute the dominant depth markers (\\S\\ref{sec:atlas:features}).",
      "numLines": 38,
      "startLine": 105,
      "totalLines": 142
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01PC4nZt7f9PA3MEfz1BuESj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
  "offset": 29,
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
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "f4818a29-fa0b-4892-abce-7f11c8368056",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TmLaab6iqQD85SYHrNJgxj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17662,
      "cache_read_input_tokens": 41042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17662
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

_source line 44 · 2026-05-15T13:43:00.711Z_

<details><summary>↩ Tool result · `toolu_01PC4nZt7f9PA3MEfz1BuESj`</summary>

```text
29	    \item \textbf{Depth Degradation Atlas.} We construct a systematic $3 \times 3$ map across model families and decoding strategies, revealing that \textsc{p90\_ppl} ranks in the top 2 in all 9 cells (100\%) and \textsc{var\_surprisal} in 7/9 (78\%), with a mean Spearman rank correlation of $\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.
30	
31	    \item \textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\% mean accuracy and cross-strategy transfer 59.1\% (chance = 25\%), demonstrating partial universality of depth fingerprints. We identify a temperature-induced d1/d2 AUC inversion (GPT-2~XL: 0.13, OLMo: 0.25) caused by accelerated convergence. Z-score normalization improves overall LR cross-strategy accuracy (25\%$\to$61\%) but does not recover the temperature-induced d1/d2 inversion (GPT-2~XL 0.50$\to$0.24, OLMo 0.50$\to$0.19), confirming a genuine geometry-level shift rather than a correctable scale difference.
32	
33	    \item \textbf{End-to-end learning as negative result.} Both DeBERTa-v3-base (58.3\%) and RoBERTa-base (59.5\%) achieve ${\sim}$59\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\%)---with the architecture-invariant gap ruling out model selection bias. Probing reveals a significant negative correlation ($\rho{=}{-}0.48$) between transformer attention and RF feature importance, confirming complementary representations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "450fb878-1f6c-4a1a-b476-dbedada4a57d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
      "content": "    \\item \\textbf{Depth Degradation Atlas.} We construct a systematic $3 \\times 3$ map across model families and decoding strategies, revealing that \\textsc{p90\\_ppl} ranks in the top 2 in all 9 cells (100\\%) and \\textsc{var\\_surprisal} in 7/9 (78\\%), with a mean Spearman rank correlation of $\\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.\n\n    \\item \\textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\\% mean accuracy and cross-strategy transfer 59.1\\% (chance = 25\\%), demonstrating partial universality of depth fingerprints. We identify a temperature-induced d1/d2 AUC inversion (GPT-2~XL: 0.13, OLMo: 0.25) caused by accelerated convergence. Z-score normalization improves overall LR cross-strategy accuracy (25\\%$\\to$61\\%) but does not recover the temperature-induced d1/d2 inversion (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19), confirming a genuine geometry-level shift rather than a correctable scale difference.\n\n    \\item \\textbf{End-to-end learning as negative result.} Both DeBERTa-v3-base (58.3\\%) and RoBERTa-base (59.5\\%) achieve ${\\sim}$59\\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\\%)---with the architecture-invariant gap ruling out model selection bias. Probing reveals a significant negative correlation ($\\rho{=}{-}0.48$) between transformer attention and RF feature importance, confirming complementary representations.",
      "numLines": 5,
      "startLine": 29,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Assistant

_source line 45_

所有改动已验证正确。

### 修改汇总

**atlas.tex** — Issue 1 (R1-N1 EDD 正式定义)
- `sec:atlas:edd` 子节：原来一句话引用 method section，改为完整的 EDD 定义段落
- 添加了正式数学公式 `EDD_T = max{d*+1 : AUC(d*, d*+1) ≥ T}`
- 说明了 AUC(d, d+1) 是 binary pairwise classifier 的 ROC AUC
- 说明了 T=0.75 默认阈值及其选择理由
- 添加了直觉含义：超过此深度后相邻深度变得统计不可区分

**generalization.tex** — Issue 2 (R1-N3 end-to-end baseline 对比表)
- `sec:gen:dcol` 子节：添加了 `tab:e2e_baselines` 表格（RF 78.2% / RoBERTa 59.5±3.2% / DeBERTa 58.3±4.7% / DeepSeek 40.0% / Chance 25.0%，含 Δ vs RF 列）
- 说明 MLM vs disentangled attention 两种架构一致结论（1.2pp gap），排除 architecture bias
- 新增 "Feature overlap analysis" 段落：Spearman ρ=-0.484 (p=0.036)，PLM 擅长 TTR (R²=0.85) 但 var_surprisal/p90_ppl R² 为负，结论：hand-crafted features 捕获 PLM 无法学到的深度信号

**generalization.tex** — Issue 3 (D021 z-score claim 修正)
- z-score 段落：删除 "substantially improves...for nucleus and top-k holdouts" 的 recovery 措辞
- 改为：overall LR accuracy 25%→61%，但 temp d1v2 AUC 恶化（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19）
- 结论改为 "genuine geometry-level shift in feature space rather than a correctable scale difference"

**introduction.tex** — Issue 3 (D021 z-score claim 修正)
- 贡献列表第 3 条：删除 "recovers logistic regression performance for non-temperature holdouts"
- 改为：overall LR accuracy 25%→61% + 不恢复 temperature d1v2 inversion + 确认 geometry-level shift

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "uuid": "e4b97afc-09c7-452c-8997-b60eae6ca46c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa2kCs6Av3ufkzVanaFe1W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 58704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2917
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

_source line 46_

所有改动已验证正确。

### 修改汇总

**atlas.tex** — Issue 1 (R1-N1 EDD 正式定义)
- `sec:atlas:edd` 子节：原来一句话引用 method section，改为完整的 EDD 定义段落
- 添加了正式数学公式 `EDD_T = max{d*+1 : AUC(d*, d*+1) ≥ T}`
- 说明了 AUC(d, d+1) 是 binary pairwise classifier 的 ROC AUC
- 说明了 T=0.75 默认阈值及其选择理由
- 添加了直觉含义：超过此深度后相邻深度变得统计不可区分

**generalization.tex** — Issue 2 (R1-N3 end-to-end baseline 对比表)
- `sec:gen:dcol` 子节：添加了 `tab:e2e_baselines` 表格（RF 78.2% / RoBERTa 59.5±3.2% / DeBERTa 58.3±4.7% / DeepSeek 40.0% / Chance 25.0%，含 Δ vs RF 列）
- 说明 MLM vs disentangled attention 两种架构一致结论（1.2pp gap），排除 architecture bias
- 新增 "Feature overlap analysis" 段落：Spearman ρ=-0.484 (p=0.036)，PLM 擅长 TTR (R²=0.85) 但 var_surprisal/p90_ppl R² 为负，结论：hand-crafted features 捕获 PLM 无法学到的深度信号

**generalization.tex** — Issue 3 (D021 z-score claim 修正)
- z-score 段落：删除 "substantially improves...for nucleus and top-k holdouts" 的 recovery 措辞
- 改为：overall LR accuracy 25%→61%，但 temp d1v2 AUC 恶化（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19）
- 结论改为 "genuine geometry-level shift in feature space rather than a correctable scale difference"

**introduction.tex** — Issue 3 (D021 z-score claim 修正)
- 贡献列表第 3 条：删除 "recovers logistic regression performance for non-temperature holdouts"
- 改为：overall LR accuracy 25%→61% + 不恢复 temperature d1v2 inversion + 确认 geometry-level shift

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 335448,
  "duration_api_ms": 337057,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "6baf7d1c-b737-41c0-b790-73574d15c724",
  "total_cost_usd": 0.9174444999999999,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 49780,
    "cache_read_input_tokens": 236473,
    "output_tokens": 19429,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49780,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 715,
        "cache_read_input_tokens": 58704,
        "cache_creation_input_tokens": 2917,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2917
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2188,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002303,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 19429,
      "cacheReadInputTokens": 236473,
      "cacheCreationInputTokens": 49780,
      "webSearchRequests": 0,
      "costUSD": 0.9151414999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7067891b-7cdf-41a2-8a93-e5d9eeb9fcf4"
}
```

</details>

---
