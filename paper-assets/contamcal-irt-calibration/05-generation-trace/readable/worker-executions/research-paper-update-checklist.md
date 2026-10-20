# research paper update checklist

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/workers/worker_research_paper-update-checklist_20260519T220548.log`
- **Structured JSON:** [`82d29cc6ea5a9a8e0913.json`](../../sessions/82/82d29cc6ea5a9a8e0913.json)

## Before a recorded user message

60 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "f0fa6909-98d7-4ec6-9e10-36a4ef4180a0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1779237000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "16f71dce-e667-4f0d-a3a2-5f69d399969d",
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the required project files and the paper directory structure in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "5aa1d670-38fd-406b-a1c0-eea08fdfb72b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APR273RzjQWdPm7fiY3vDy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13486,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13486
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

### Assistant

_source line 5_

读取项目文件和论文目录结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "4db45240-2bf7-4514-8364-30e0bf4d81b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APR273RzjQWdPm7fiY3vDy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13486,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13486
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014ARftc2fpBDtPUDdxPenNj`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "22df40ca-0324-4f4f-8752-60145c661d01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APR273RzjQWdPm7fiY3vDy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13486,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13486
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

_source line 7 · 2026-05-19T22:06:01.980Z_

<details><summary>↩ Tool result · `toolu_014ARftc2fpBDtPUDdxPenNj`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "d94bd069-b63c-41f6-b7a7-692a5f6a6937",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01P9himBh5hGARSgpvQG6PVg`</summary>

```json
{
  "project": "contamcal-irt-calibration",
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
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "27fcfebc-53d7-4731-af99-c405c167c5df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkuHWeEQazvxh26JMpJTD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 25327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
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

_source line 9 · 2026-05-19T22:06:05.354Z_

<details><summary>↩ Tool result · `toolu_01P9himBh5hGARSgpvQG6PVg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight (D149: dose-response profiling + baseline-dependent direction, building on D039/D108/D115)\\n\\nBenchmark contamination does not have a single effect — controlled SFT injection across 5 independent model families reveals qualitatively different dose-response profiles depending on model baseline capability. Through injection (LoRA r=16, 5 dosage levels d000–d100) on Qwen2.5-7B, Qwen2.5-14B, Phi-4 14.7B, Gemma-2 9B, OLMo-2 7B, we observe:\\n\\n**5 observed dose-response profiles (D149, MMLU, seed=42)**:\\n| Profile | Family | Baseline | d000→d100 | Max effect |\\n|---------|--------|----------|-----------|------------|\\n| Immune | Phi-4 14.7B | 76.44% | ±0.54pp | negligible |\\n| U-type collapse | Qwen-14B | 69.44% | -9.37pp | -10.03pp@d050 |\\n| V-type recovery | Qwen-7B | 66.11% | -1.78pp | -3.13pp@d025 |\\n| Benefit | Gemma-2 9B | 61.86% | +3.76pp | monotonic rise |\\n| Benefit-saturation | OLMo-2 7B | 53.79% | +3.21pp | saturates@d050 |\\n\\n⚠️ **Claim calibration (Reviewer D152)**: N_profiles = N_families，当前数据不足以声称 5 种 \\\"discrete categories\\\"。更保守分类是 3 种（benefit / harm / immune）。5-profile 描述仅在 triple-seed 确认形状稳定后升级为 \\\"taxonomy\\\"。V-type vs U-type 区分以及 benefit vs benefit-saturation 区分需要 triple-seed 验证。\\n\\n**Baseline-dependent direction (observed in 5-family sample)**: In our sample, models below ~64% MMLU baseline benefited from contamination while those above were harmed or immune. This threshold is estimated from 5 families — the boundary lies between 61.9% (Gemma-2, benefit) and 66.1% (Qwen-7B, harm) — and may shift with additional model families. **不可说 \\\"universal threshold\\\"，只能说 \\\"observed in our sample\\\"。** 考虑 permutation test 检验二分法显著性。\\n\\n**Within-family scale finding (Qwen only)**: Within the Qwen family, the 14B model is 3× more fragile than the 7B (-10pp vs -3pp). However, Phi-4 (14.7B) is immune — so this is NOT a general \\\"bigger = more fragile\\\" claim. 正确 framing: \\\"baseline ability, not parameter count alone, determines contamination vulnerability.\\\"\\n\\nARC results are directionally consistent (OLMo-2 +3.92pp benefit; Qwen-7B -3.84pp V-type; Qwen-14B -3.41pp U-type; Phi-4 immune ±0.6pp). Gemma-2 ARC excluded due to evaluation artifact (16pp oscillation).\\n\\nThe primary contribution is the empirical characterization framework — showing that \\\"contamination = inflation\\\" is a gross oversimplification and that model-specific dose-response profiling is necessary for reliable benchmark interpretation. IRT with per-benchmark γ_k provides the statistical machinery for this characterization. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\n\\n## Core Claims (4 条 — D149 reorder: characterization as primary, D152 Reviewer calibrated)\\n\\n1. **Characterization Claim (PRIMARY — D149 dose-response profiling)**: Contamination does not uniformly inflate scores — it produces qualitatively different dose-response profiles across model families, with effect direction (benefit vs harm) correlating with baseline ability. Key evidence:\\n   - **5 families × 5 dosages × 2 benchmarks** (MMLU + ARC) with controlled SFT injection at identical LoRA config\\n   - **Baseline-dependent direction**: In our 5-family sample, models below ~62-66% MMLU benefited; above were harmed or immune\\n   - **Effect magnitude heterogeneity**: From -10pp (Qwen-14B) to +3.8pp (Gemma-2) — 14pp range across families at same dosage\\n   - **Within-family scale effect (Qwen)**: 14B 3× more fragile than 7B, suggesting baseline ability (not just scale) drives vulnerability\\n   - **Cross-benchmark consistency**: ARC direction aligns with MMLU for 4/5 families\\n   ⚠️ **Claim strength gating**: 当前 5 profiles based on seed=42 single run. 论文用 \\\"observed profiles\\\" 描述。升级为 \\\"taxonomy of discrete patterns\\\" 需要 triple-seed 确认 profile 形状稳定。如果 V-type/U-type 在 triple-seed 下合并为同一 \\\"harm\\\" 类别，降级为 3-profile (benefit/harm/immune)。\\n   **Domain-level heterogeneity (≤3B Qwen IRT analysis, D108/D115, mechanistic complement)**: Within MMLU, stratification by cognitive domain reveals Simpson's paradox: aggregate γ≈0 masks STEM gradient (Math γ=+0.97, Science γ=+0.84, CS_Eng γ≈0). Non-STEM domains show model misfit (PPP≈1.0). 注意：domain-level 分析在 ≤3B Qwen 上进行，与 7B-14.7B 5-family profiling 是不同 scale。7B-14.7B domain-level 分析列为 future work。\\n   **Paper claim scope**: 5 profiles based on 5 families × 5 dosages (seed=42; triple-seed in progress). Domain-level from ≤3B Qwen. Bounded by: SFT-route only, ≤14.7B, AUGMENT mode, 2 MCQ benchmarks.\\n\\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\\n   **C2 contingency**: \\\"Scale-dependent\\\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \\\"method-specific signal effectiveness.\\\" Min-K++ reversal remains novel regardless.\\n\\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \\\"impossibility,\\\" not merely \\\"IRT needs more data.\\\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\\n\\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: IRT ability estimation provides calibration value (GSM8K: calMAE=0.006 vs raw=0.169, ΔMAE=0.163); the γ parameter provides diagnostic value by revealing domain-differential contamination effects. These are distinct contributions: calibration improvement comes from the IRT framework itself (ability estimation decontaminates via the θ pathway), while γ characterizes where and how contamination manifests. When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates. Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion: PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. Note: vanilla 2PL ≈ 2PL+γ in MAE across all three benchmarks — γ does not improve calibration accuracy but provides the diagnostic decomposition that is Claim 1's core contribution.\\n\\n## Contributions (Hierarchical — D149/D152 calibrated)\\n\\n### Core\\n1. **Dose-response profiling across 5 model families**: Contamination effects range from -10pp to +3.8pp MMLU depending on model family, with effect direction correlating with baseline ability. No prior work has systematically profiled contamination dose-response across multiple independent families. *(Upgrades to \\\"taxonomy of N discrete patterns\\\" if triple-seed confirms profile stability; conservative framing: 3 profiles — benefit/harm/immune.)*\\n2. **Domain-dependent contamination characterization** via IRT γ_k (≤3B Qwen): Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0). Mechanistic complement to family-level profiling — contamination heterogeneity operates at multiple granularities.\\n3. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy cautionary finding. Honest reporting that RRF = S1-only in practice.\\n4. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight.\\n\\n### Supporting\\n5. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\\n6. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection across 5 families\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\n- **Our framing (D149 pivot)**: ContamCal is a diagnostic framework that uses controlled SFT injection and IRT analysis to systematically profile how contamination affects benchmark scores. Through injection across 5 independent model families (7B–14.7B), we discover that contamination produces not one but five distinct dose-response patterns, governed by a baseline ability threshold. The framework establishes both what contamination does (5-pattern taxonomy + domain-level IRT heterogeneity) and under what conditions calibration is feasible (Fisher Information identifiability boundaries). Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\n- **Headline result template (D149, D152 calibrated)**: \\\"Benchmark contamination effects span a 14pp range across model families — from +3.8pp benefit (Gemma-2 9B) to -10pp collapse (Qwen-14B) — with effect direction correlating with baseline ability: lower-baseline models benefit while higher-baseline models are harmed or immune. Within the Qwen family, the 14B model is 3× more fragile than the 7B, suggesting baseline ability rather than parameter count drives vulnerability. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = -1.2 to -2.7). Fisher Information analysis establishes that reliable parameter recovery requires N≥50 models — conditions rarely met in current LLM evaluation.\\\"\\n\\n## Venue Fit Risks\\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). ~~Risk: may expect broader model coverage beyond Qwen2.5~~ — **Resolved by D141**: 4 independent families (Qwen2.5, Phi-4, OLMo-2, Gemma-2) with controlled SFT at ≤14.7B scale.\\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \\\"new algorithm\\\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \\\"calibration is only as good as its inputs.\\\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\\n\\n## Anticipated Reviewer Concerns & Defenses\\n\\n| # | Concern | Defense | Experiment |\\n|---|---------|---------|------------|\\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \\\"best-available proxy\\\", acknowledged as limitation | exp-006, exp-009 |\\n| 4 | Scale limited to 3B | ≤14.7B controlled SFT across 4 independent families (Qwen2.5 0.5B-14B, Phi-4 14.7B, OLMo-2 7B, Gemma-2 9B; D141). 29 runs total. | D141 scope expansion |\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\\n| 11 | Single model family? | Addressed in main experiments: 4 independent families (Qwen2.5, Phi-4, OLMo-2, Gemma-2) with controlled SFT injection at identical LoRA config (D141). Qwen2.5 provides within-family scaling (0.5B-14B); 3 cross-family models validate generalizability. | D141 scope expansion |\\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \\\"S1+IRT calibration with extensible multi-signal architecture for future signals.\\\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\\n| 20 | γ doesn't improve calibration MAE over vanilla 2PL | γ's role is diagnostic (domain-differential characterization), not calibration accuracy improvement. IRT ability estimation itself provides calibration value (GSM8K ΔMAE=0.163). Vanilla 2PL ≈ 2PL+γ confirms γ is orthogonal to calibration performance — it reveals WHERE contamination acts, not HOW MUCH to adjust. | exp-006 |\\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\\n\\n## Evaluation Protocol (6 Metrics — D025 added SBC)\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\\n\\n## Benchmarks (2 main + 2 contrasts)\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \\\"benchmark-dependent contamination effects\\\" — ContamCal calibrates in both directions.\\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \\\"ContamCal identifies benchmarks not requiring calibration\\\")\\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\\n\\n## Baselines (7)\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\n\\n## Local Independence Discussion\\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\\n\\n## Required Figures (D149 updated)\\n1. **5-pattern dose-response curves** (MMLU + ARC) — paper's headline figure, already drafted on westd\\n2. **Baseline vs max effect scatter** — shows ~64% threshold, already drafted on westd\\n3. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\\n4. Signal × scale × dosage AUC heatmap (exp-008)\\n5. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\\n6. Calibrated-vs-true accuracy scatter with CIs (exp-006)\\n7. *(Optional)* Per-family IRT γ comparison (bar chart with CIs, shows cross-family heterogeneity)\\n\\n## Citation Requirements (35+ minimum, expanded per Dream D2)\\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\\nDream D2 additions (all 3 tiers flagged):\\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \\\"calibration\\\" — ours is decontamination, not probability calibration)\\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\\nD025 additions (all 3 Dream tiers flagged):\\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\\n\\n## Discussion Notes\\n\\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\\n- **Paper treatment**: Report in Discussion as \\\"capacity threshold for reliable MC evaluation.\\\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\\n\\n## Scope Expansion: ≤14.7B + 4 Families (D141, 2026-05-18)\\n\\n### Model Matrix\\n| Family | Model | Params | Released | Runs | Role |\\n|--------|-------|--------|----------|------|------|\\n| Qwen (primary) | Qwen2.5-0.5B/1.5B/3B | 0.5-3B | 2024-09 | existing | Within-family baseline (≤3B) |\\n| Qwen (primary) | Qwen2.5-7B | 7B | 2024-09 | 10 (5d×2s) | Within-family scale extension |\\n| Qwen (primary) | Qwen2.5-14B | 14B | 2024-09 | 5 (5d×1s) | Within-family scale frontier |\\n| Microsoft | Phi-4 | 14.7B | 2024-12 | 5 (5d×1s) | Cross-family, strongest 14B |\\n| Allen AI | OLMo-2-7B | 7B | 2024-11 | 5 (5d×1s) | Cross-family, fully open |\\n| Google | Gemma-2-9B | 9B | 2024-06 | 5 (5d×1s) | Cross-family, Google family |\\n\\nAll: bf16 LoRA r=16 α=32 lr=5e-5 (D140: matching ≤3B). SFT AUGMENT mode.\\n\\n### D149 Narrative: 5-Pattern Taxonomy (supersedes Variant A/B framework)\\n\\n**[SUPERSEDED]** Variant A (null) / Variant B (scale-dependent transition) 框架已被 D149 实际数据推翻。实际效应远超 \\\"null vs ~2pp 灰色地带\\\"——Qwen-14B -10pp 崩塌、OLMo-2 +3.5pp 受益。不再需要 A/B 判定。\\n\\n**Family Framing（D149 更新）**:\\n- 正确表述: \\\"5 independent model families from 5 major labs (Alibaba, Microsoft, Allen AI, Google), trained on independent corpora with distinct pre-training recipes, spanning 7B–14.7B parameters\\\"\\n- **禁止** \\\"architecture lineage\\\" framing——全是 dense decoder-only transformer，差异在 training data + lab diversity\\n- **禁止** \\\"scaling law\\\" 术语——用 \\\"baseline-dependent response pattern\\\"\\n\\n**核心叙事（D149 确定，D152 Reviewer 校准）**:\\n\\\"SFT-route benchmark contamination does not produce a single effect. Through controlled injection across 5 independent model families, we observe qualitatively different dose-response profiles spanning a 14pp range — from +3.8pp benefit (Gemma-2) to -10pp collapse (Qwen-14B). Effect direction correlates with baseline ability: lower-baseline models benefit while higher-baseline models are harmed or immune. Within the Qwen family, the 14B model is 3× more fragile than the 7B, suggesting baseline ability rather than scale alone determines vulnerability.\\\"\\n\\n**关键 D149 发现（D152 校准后表述）**:\\n1. **Qualitatively different dose-response profiles** — 5 families show 5 profiles（triple-seed 确认形状稳定后升级为 \\\"taxonomy\\\"；保守分类 3 种: benefit/harm/immune）\\n2. **Baseline-dependent direction (observed)** — 分界在 ~62-66% 区间，5 点样本，不可说 \\\"universal threshold\\\"\\n3. **Within-family scale effect (Qwen only)**: 14B >> 7B fragility，但 Phi-4 14.7B immune → 不是 \\\"bigger = more fragile\\\" 的一般规律\\n4. **Cross-benchmark consistency**: ARC 方向与 MMLU 一致（4/5 families），Gemma-2 ARC 排除（需 root cause evidence，不能只说 artifact）\\n5. **Benefit families 存在**: OLMo-2 和 Gemma-2 都从 contamination 受益——颠覆 \\\"contamination = harmful\\\"\\n\\n**D149 vs 旧 Qwen-only ≤3B 数据的关系**:\\n- 旧 ≤3B Qwen 数据中 MMLU Δ~0.7pp 被解读为 \\\"near-null\\\"——实际是 Qwen 在 ≤3B scale 的特定行为\\n- D149 cross-family 数据揭示 Qwen ≤3B 只是 5-pattern 中的一小部分\\n- 旧 domain-level IRT 分析（Simpson's paradox, STEM gradient）仍有效，作为 5-pattern 的机制解释层\\n\\n**EMNLP 预估（D149 后更新）**：5 families + 5-pattern taxonomy + baseline threshold + counter-intuitive scale finding + IRT framework + identifiability → **3.5-4.0**（Borderline Conference to Conference）。前提：triple-seed 统计验证 + claim 边界清晰 + 不 overclaim。5-pattern taxonomy 是 novel empirical contribution，baseline threshold 如果经受住 triple-seed 检验可能是 headline finding。\\n\\n### OLMo-2 \\\"Benefit-saturation\\\" 模式（D149 更新，supersedes near-null 判定）\\n\\n**[SUPERSEDED]** 旧判定 \\\"OLMo-2 near-null ±0.5pp\\\" 完全错误——来自 Qwen-only ≤3B 参考框架。Phase 2 v2 完整数据:\\n- MMLU: d000=53.79% → d005=56.14% → d025=56.17% → d050=57.25% → d100=57.00%\\n- 最大效应 +3.46pp（d050），然后 d100 轻微回落 → **benefit-saturation** 模式\\n- ARC: d000=76.11% → d100=80.03%（+3.92pp 单调上升）\\n- 最低 baseline（53.79% MMLU）→ 最强 benefit-saturation 效应\\n\\n**OLMo-2 在 5-pattern taxonomy 中的定位**:\\n- 与 Gemma-2（也是 benefit）一起构成 \\\"contamination helps low-baseline models\\\" 证据\\n- 但 OLMo-2 在 d050 后饱和，Gemma-2 持续上升 → 两种不同的 benefit 子类\\n- Baseline 53.8% 远低于 threshold（~64%），完美契合 baseline-threshold 假说\\n\\n**OLMo-2 模型选择 justification**：AllenAI 独立实验室 + fully open source + 独立训练数据 + 7B scale 与 Qwen 7B 对照。\\n\\n### Secondary Findings（Reviewer 评估，2026-05-18）\\n\\n**高价值（主动追踪）**:\\n1. **Cross-family dosage-response shape consistency**: 各 family 在相同 benchmark 上 d000→d100 曲线形状是否一致。若一致 → \\\"contamination susceptibility 是 benchmark × dosage 性质，非 model-family artifact\\\"。Claim 1 最强 generalizability evidence。\\n2. **γ cross-family pooling collapse**: 各 family 独立 fit 的 γ 方向一致，但 cross-family pooled γ 崩塌/反向 → \\\"contamination signals are family-specific, cross-family pooling requires family-aware calibration\\\"。有独立 contribution 级潜力。\\n\\n**中等价值（值得报告）**:\\n3. **Scale × family interaction at 7B band**: 7B Qwen vs 7B OLMo vs 9B Gemma 同 dosage 下 Δacc 差异。差异小(<2pp) → \\\"scale dominates\\\"；差异大 → \\\"family-specific susceptibility\\\"。归因困难（architecture vs training data confound），不宜作 headline。\\n\\n**低价值/高风险（不追踪）**:\\n4. Architecture-specific mechanism（需 interpretability 分析，远超当前实验能力）\\n\\n### EMNLP Reviewer Pushback 预判（Reviewer 评估）\\n1. **\\\"No 70B+\\\"**（~80%）: Limitations 显式讨论。Defense: compute 超 scope + ≤14.7B 已覆盖拐点区间 + 不做 extrapolation claim\\n2. **\\\"SFT-route only\\\"**（~60%）: 已有 defense（acknowledged limitation + exp-009 RL bridge）\\n3. **\\\"Scale analysis is Qwen-only\\\"**（~40%）: Cross-family 是 consistency check 不是 scaling curve\\n\\n### Claim 边界（硬约束）\\n1. \\\"SFT-route\\\" 限定不可去掉（未测试 pretraining contamination）\\n2. \\\"≤14.7B\\\" 不可说 \\\"across all scales\\\"（70B+ 未测试）\\n3. \\\"3 benchmarks\\\" 不可说 \\\"across benchmarks in general\\\"\\n4. AUGMENT mode SFT 限定（base_data + contaminated items appended, 非 REPLACE 模式）——升级 scope 后需在 paper limitations 显式提及\\n5. **评估协议敏感性（Reviewer D154b）**: Qwen-7B V-type recovery pattern 在 5-shot evaluate.py 下出现，但在 0-shot lm-eval-harness 下消失（MMLU 平坦/略升）。ARC 在 lm-eval 下 baseline 大幅偏移（-40pp）。所有正式结果使用 evaluate.py v3（5-shot MMLU, 25-shot ARC），内部一致。但 **dose-response profiles 是 protocol-conditional observations，不是 protocol-invariant model properties**。论文必须：(a) 明确标注评估协议，(b) 在 Limitations 讨论 prompt format 敏感性，(c) 不可 claim profiles 是 \\\"intrinsic model characteristics\\\"\\n\\n### Concern #11 升级\\n从 \\\"Acknowledged limitation — single model family\\\" → \\\"Addressed — 4 independent families\\\"\\n\\n### Main Figure: 5-Pattern Dose-Response Curves (D149)\\n- **Fig 1a (MMLU)**: X = dosage (d000→d100), Y = accuracy (%). 5 curves, one per family. Color-coded by pattern type. Shows the full taxonomy: Phi-4 flat (immune), Qwen-14B U-shape (collapse), Qwen-7B V-shape (recovery), Gemma-2 rising (benefit), OLMo-2 rising then flat (benefit-saturation).\\n- **Fig 1b (ARC)**: Same layout. Directionally consistent patterns (Gemma-2 excluded, noted as artifact).\\n- **Fig 2: Baseline vs Max Effect**: X = baseline MMLU accuracy, Y = max |Δacc| with direction. Shows the ~64% threshold. Scatter with 5 family points + regression line / threshold indicator.\\n- **已生成 (westd `/root/autodl-tmp/exp001/figures/`)**: mmlu_dose_response.pdf, arc_dose_response.pdf, baseline_vs_effect.pdf — 需视觉审查后决定是否需要重绘为论文级质量\\n\\n### Cross-family Analysis Strategy\\n- Family-level 对比（per-family independent IRT fit, report per-family γ）\\n- Qwen2.5-7B domain consistency check（N 最大的 family）\\n- 不做 hierarchical gamma model（ROI 太低, 7 天 DDL → Future Work）\\n- γ 跨家族池化崩塌现象作为 finding 报告\\n\\n### Paper Rewrite Scope (D149 后，待 triple-seed 验证)\\n- Abstract: 完全重写（~170 words，5-pattern taxonomy + baseline threshold 为核心）\\n- Introduction ¶4 + Contributions: 完全重写（5-pattern taxonomy 为 headline）\\n- Introduction ¶1-3: 小修（加 \\\"contamination can also help\\\" 铺垫）\\n- Results: 新增 \\\"5-Pattern Dose-Response Taxonomy\\\" + \\\"Baseline Ability Threshold\\\" + \\\"Cross-Family Consistency\\\" sections\\n- Results: 保留 domain-level IRT analysis 作为机制解释\\n- Discussion: 新增 \\\"Why Bigger ≠ More Robust\\\" + \\\"Implications for Benchmark Design\\\"\\n- Discussion: scale-invariance implication OR transition interpretation\\n- Method: 不变（加 family indicator 说明）\\n- Related Work: 稳定（加 1-2 句 multi-family evaluation）\\n- 预计 Paper Agent 2 天完成（前提: framing variant 已确定）\\n- **不在结果出来前开始重写**（避免 variant 错配返工）\\n\\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\\n\", \"total_chars\": 33365, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "c321ece4-b56c-42e2-ba79-077c20a83103",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — contamcal-irt-calibration\\\\n\\\\n## Target Venue\\\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\\\n- Track: Machine Learning for NLP / Resources and Evaluation\\\\n- Aligns with EMNLP 2026 special theme \\\\\\\"New Missions for NLP Research\\\\\\\" (explicitly invites contamination/data governance work)\\\\n\\\\n## Core Insight (D149: dose-response profiling + baseline-dependent direction, building on D039/D108/D115)\\\\n\\\\nBenchmark contamination does not have a single effect — controlled SFT injection across 5 independent model families reveals qualitatively different dose-response profiles depending on model baseline capability. Through injection (LoRA r=16, 5 dosage levels d000–d100) on Qwen2.5-7B, Qwen2.5-14B, Phi-4 14.7B, Gemma-2 9B, OLMo-2 7B, we observe:\\\\n\\\\n**5 observed dose-response profiles (D149, MMLU, seed=42)**:\\\\n| Profile | Family | Baseline | d000→d100 | Max effect |\\\\n|---------|--------|----------|-----------|------------|\\\\n| Immune | Phi-4 14.7B | 76.44% | ±0.54pp | negligible |\\\\n| U-type collapse | Qwen-14B | 69.44% | -9.37pp | -10.03pp@d050 |\\\\n| V-type recovery | Qwen-7B | 66.11% | -1.78pp | -3.13pp@d025 |\\\\n| Benefit | Gemma-2 9B | 61.86% | +3.76pp | monotonic rise |\\\\n| Benefit-saturation | OLMo-2 7B | 53.79% | +3.21pp | saturates@d050 |\\\\n\\\\n⚠️ **Claim calibration (Reviewer D152)**: N_profiles = N_families，当前数据不足以声称 5 种 \\\\\\\"discrete categories\\\\\\\"。更保守分类是 3 种（benefit / harm / immune）。5-profile 描述仅在 triple-seed 确认形状稳定后升级为 \\\\\\\"taxonomy\\\\\\\"。V-type vs U-type 区分以及 benefit vs benefit-saturation 区分需要 triple-seed 验证。\\\\n\\\\n**Baseline-dependent direction (observed in 5-family sample)**: In our sample, models below ~64% MMLU baseline benefited from contamination while those above were harmed or immune. This threshold is estimated from 5 families — the boundary lies between 61.9% (Gemma-2, benefit) and 66.1% (Qwen-7B, harm) — and may shift with additional model families. **不可说 \\\\\\\"universal threshold\\\\\\\"，只能说 \\\\\\\"observed in our sample\\\\\\\"。** 考虑 permutation test 检验二分法显著性。\\\\n\\\\n**Within-family scale finding (Qwen only)**: Within the Qwen family, the 14B model is 3× more fragile than the 7B (-10pp vs -3pp). However, Phi-4 (14.7B) is immune — so this is NOT a general \\\\\\\"bigger = more fragile\\\\\\\" claim. 正确 framing: \\\\\\\"baseline ability, not parameter count alone, determines contamination vulnerability.\\\\\\\"\\\\n\\\\nARC results are directionally consistent (OLMo-2 +3.92pp benefit; Qwen-7B -3.84pp V-type; Qwen-14B -3.41pp U-type; Phi-4 immune ±0.6pp). Gemma-2 ARC excluded due to evaluation artifact (16pp oscillation).\\\\n\\\\nThe primary contribution is the empirical characterization framework — showing that \\\\\\\"contamination = inflation\\\\\\\" is a gross oversimplification and that model-specific dose-response profiling is necessary for reliable benchmark interpretation. IRT with per-benchmark γ_k provides the statistical machinery for this characterization. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\\\n\\\\n## Core Claims (4 条 — D149 reorder: characterization as primary, D152 Reviewer calibrated)\\\\n\\\\n1. **Characterization Claim (PRIMARY — D149 dose-response profiling)**: Contamination does not uniformly inflate scores — it produces qualitatively different dose-response profiles across model families, with effect direction (benefit vs harm) correlating with baseline ability. Key evidence:\\\\n   - **5 families × 5 dosages × 2 benchmarks** (MMLU + ARC) with controlled SFT injection at identical LoRA config\\\\n   - **Baseline-dependent direction**: In our 5-family sample, models below ~62-66% MMLU benefited; above were harmed or immune\\\\n   - **Effect magnitude heterogeneity**: From -10pp (Qwen-14B) to +3.8pp (Gemma-2) — 14pp range across families at same dosage\\\\n   - **Within-family scale effect (Qwen)**: 14B 3× more fragile than 7B, suggesting baseline ability (not just scale) drives vulnerability\\\\n   - **Cross-benchmark consistency**: ARC direction aligns with MMLU for 4/5 families\\\\n   ⚠️ **Claim strength gating**: 当前 5 profiles based on seed=42 single run. 论文用 \\\\\\\"observed profiles\\\\\\\" 描述。升级为 \\\\\\\"taxonomy of discrete patterns\\\\\\\" 需要 triple-seed 确认 profile 形状稳定。如果 V-type/U-type 在 triple-seed 下合并为同一 \\\\\\\"harm\\\\\\\" 类别，降级为 3-profile (benefit/harm/immune)。\\\\n   **Domain-level heterogeneity (≤3B Qwen IRT analysis, D108/D115, mechanistic complement)**: Within MMLU, stratification by cognitive domain reveals Simpson's paradox: aggregate γ≈0 masks STEM gradient (Math γ=+0.97, Science γ=+0.84, CS_Eng γ≈0). Non-STEM domains show model misfit (PPP≈1.0). 注意：domain-level 分析在 ≤3B Qwen 上进行，与 7B-14.7B 5-family profiling 是不同 scale。7B-14.7B domain-level 分析列为 future work。\\\\n   **Paper claim scope**: 5 profiles based on 5 families × 5 dosages (seed=42; triple-seed in progress). Domain-level from ≤3B Qwen. Bounded by: SFT-route only, ≤14.7B, AUGMENT mode, 2 MCQ benchmarks.\\\\n\\\\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\\\\n   **C2 contingency**: \\\\\\\"Scale-dependent\\\\\\\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \\\\\\\"method-specific signal effectiveness.\\\\\\\" Min-K++ reversal remains novel regardless.\\\\n\\\\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \\\\\\\"impossibility,\\\\\\\" not merely \\\\\\\"IRT needs more data.\\\\\\\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\\\\n\\\\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: IRT ability estimation provides calibration value (GSM8K: calMAE=0.006 vs raw=0.169, ΔMAE=0.163); the γ parameter provides diagnostic value by revealing domain-differential contamination effects. These are distinct contributions: calibration improvement comes from the IRT framework itself (ability estimation decontaminates via the θ pathway), while γ characterizes where and how contamination manifests. When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates. Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion: PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. Note: vanilla 2PL ≈ 2PL+γ in MAE across all three benchmarks — γ does not improve calibration accuracy but provides the diagnostic decomposition that is Claim 1's core contribution.\\\\n\\\\n## Contributions (Hierarchical — D149/D152 calibrated)\\\\n\\\\n### Core\\\\n1. **Dose-response profiling across 5 model families**: Contamination effects range from -10pp to +3.8pp MMLU depending on model family, with effect direction correlating with baseline ability. No prior work has systematically profiled contamination dose-response across multiple independent families. *(Upgrades to \\\\\\\"taxonomy of N discrete patterns\\\\\\\" if triple-seed confirms profile stability; conservative framing: 3 profiles — benefit/harm/immune.)*\\\\n2. **Domain-dependent contamination characterization** via IRT γ_k (≤3B Qwen): Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0). Mechanistic complement to family-level profiling — contamination heterogeneity operates at multiple granularities.\\\\n3. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy cautionary finding. Honest reporting that RRF = S1-only in practice.\\\\n4. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight.\\\\n\\\\n### Supporting\\\\n5. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\\\\n6. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection across 5 families\\\\n\\\\n## Story Spine\\\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \\\\\\\"what would this model's score be if it had never seen the test data?\\\\\\\"\\\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\\\n- **Our framing (D149 pivot)**: ContamCal is a diagnostic framework that uses controlled SFT injection and IRT analysis to systematically profile how contamination affects benchmark scores. Through injection across 5 independent model families (7B–14.7B), we discover that contamination produces not one but five distinct dose-response patterns, governed by a baseline ability threshold. The framework establishes both what contamination does (5-pattern taxonomy + domain-level IRT heterogeneity) and under what conditions calibration is feasible (Fisher Information identifiability boundaries). Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\\\n- **Headline result template (D149, D152 calibrated)**: \\\\\\\"Benchmark contamination effects span a 14pp range across model families — from +3.8pp benefit (Gemma-2 9B) to -10pp collapse (Qwen-14B) — with effect direction correlating with baseline ability: lower-baseline models benefit while higher-baseline models are harmed or immune. Within the Qwen family, the 14B model is 3× more fragile than the 7B, suggesting baseline ability rather than parameter count drives vulnerability. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = -1.2 to -2.7). Fisher Information analysis establishes that reliable parameter recovery requires N≥50 models — conditions rarely met in current LLM evaluation.\\\\\\\"\\\\n\\\\n## Venue Fit Risks\\\\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). ~~Risk: may expect broader model coverage beyond Qwen2.5~~ — **Resolved by D141**: 4 independent families (Qwen2.5, Phi-4, OLMo-2, Gemma-2) with controlled SFT at ≤14.7B scale.\\\\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\\\\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \\\\\\\"new algorithm\\\\\\\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\\\\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \\\\\\\"calibration is only as good as its inputs.\\\\\\\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\\\\n\\\\n## Anticipated Reviewer Concerns & Defenses\\\\n\\\\n| # | Concern | Defense | Experiment |\\\\n|---|---------|---------|------------|\\\\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\\\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\\\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \\\\\\\"best-available proxy\\\\\\\", acknowledged as limitation | exp-006, exp-009 |\\\\n| 4 | Scale limited to 3B | ≤14.7B controlled SFT across 4 independent families (Qwen2.5 0.5B-14B, Phi-4 14.7B, OLMo-2 7B, Gemma-2 9B; D141). 29 runs total. | D141 scope expansion |\\\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\\\\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\\\\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\\\\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\\\\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\\\\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\\\\n| 11 | Single model family? | Addressed in main experiments: 4 independent families (Qwen2.5, Phi-4, OLMo-2, Gemma-2) with controlled SFT injection at identical LoRA config (D141). Qwen2.5 provides within-family scaling (0.5B-14B); 3 cross-family models validate generalizability. | D141 scope expansion |\\\\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\\\\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\\\\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\\\\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\\\\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\\\\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\\\\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \\\\\\\"S1+IRT calibration with extensible multi-signal architecture for future signals.\\\\\\\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\\\\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\\\\n| 20 | γ doesn't improve calibration MAE over vanilla 2PL | γ's role is diagnostic (domain-differential characterization), not calibration accuracy improvement. IRT ability estimation itself provides calibration value (GSM8K ΔMAE=0.163). Vanilla 2PL ≈ 2PL+γ confirms γ is orthogonal to calibration performance — it reveals WHERE contamination acts, not HOW MUCH to adjust. | exp-006 |\\\\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\\\\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\\\\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\\\\n\\\\n## Evaluation Protocol (6 Metrics — D025 added SBC)\\\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\\\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\\\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\\\\n\\\\n## Benchmarks (2 main + 2 contrasts)\\\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\\\\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \\\\\\\"benchmark-dependent contamination effects\\\\\\\" — ContamCal calibrates in both directions.\\\\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \\\\\\\"ContamCal identifies benchmarks not requiring calibration\\\\\\\")\\\\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\\\\n\\\\n## Baselines (7)\\\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\\\n\\\\n## Local Independence Discussion\\\\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\\\\n\\\\n## Required Figures (D149 updated)\\\\n1. **5-pattern dose-response curves** (MMLU + ARC) — paper's headline figure, already drafted on westd\\\\n2. **Baseline vs max effect scatter** — shows ~64% threshold, already drafted on westd\\\\n3. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\\\\n4. Signal × scale × dosage AUC heatmap (exp-008)\\\\n5. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\\\\n6. Calibrated-vs-true accuracy scatter with CIs (exp-006)\\\\n7. *(Optional)* Per-family IRT γ comparison (bar chart with CIs, shows cross-family heterogeneity)\\\\n\\\\n## Citation Requirements (35+ minimum, expanded per Dream D2)\\\\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\\\\nDream D2 additions (all 3 tiers flagged):\\\\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\\\\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \\\\\\\"calibration\\\\\\\" — ours is decontamination, not probability calibration)\\\\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\\\\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\\\\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\\\\nD025 additions (all 3 Dream tiers flagged):\\\\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\\\\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\\\\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\\\\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\\\\n\\\\n## Discussion Notes\\\\n\\\\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\\\\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\\\\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\\\\n- **Paper treatment**: Report in Discussion as \\\\\\\"capacity threshold for reliable MC evaluation.\\\\\\\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\\\\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\\\\n\\\\n## Scope Expansion: ≤14.7B + 4 Families (D141, 2026-05-18)\\\\n\\\\n### Model Matrix\\\\n| Family | Model | Params | Released | Runs | Role |\\\\n|--------|-------|--------|----------|------|------|\\\\n| Qwen (primary) | Qwen2.5-0.5B/1.5B/3B | 0.5-3B | 2024-09 | existing | Within-family baseline (≤3B) |\\\\n| Qwen (primary) | Qwen2.5-7B | 7B | 2024-09 | 10 (5d×2s) | Within-family scale extension |\\\\n| Qwen (primary) | Qwen2.5-14B | 14B | 2024-09 | 5 (5d×1s) | Within-family scale frontier |\\\\n| Microsoft | Phi-4 | 14.7B | 2024-12 | 5 (5d×1s) | Cross-family, strongest 14B |\\\\n| Allen AI | OLMo-2-7B | 7B | 2024-11 | 5 (5d×1s) | Cross-family, fully open |\\\\n| Google | Gemma-2-9B | 9B | 2024-06 | 5 (5d×1s) | Cross-family, Google family |\\\\n\\\\nAll: bf16 LoRA r=16 α=32 lr=5e-5 (D140: matching ≤3B). SFT AUGMENT mode.\\\\n\\\\n### D149 Narrative: 5-Pattern Taxonomy (supersedes Variant A/B framework)\\\\n\\\\n**[SUPERSEDED]** Variant A (null) / Variant B (scale-dependent transition) 框架已被 D149 实际数据推翻。实际效应远超 \\\\\\\"null vs ~2pp 灰色地带\\\\\\\"——Qwen-14B -10pp 崩塌、OLMo-2 +3.5pp 受益。不再需要 A/B 判定。\\\\n\\\\n**Family Framing（D149 更新）**:\\\\n- 正确表述: \\\\\\\"5 independent model families from 5 major labs (Alibaba, Microsoft, Allen AI, Google), trained on independent corpora with distinct pre-training recipes, spanning 7B–14.7B parameters\\\\\\\"\\\\n- **禁止** \\\\\\\"architecture lineage\\\\\\\" framing——全是 dense decoder-only transformer，差异在 training data + lab diversity\\\\n- **禁止** \\\\\\\"scaling law\\\\\\\" 术语——用 \\\\\\\"baseline-dependent response pattern\\\\\\\"\\\\n\\\\n**核心叙事（D149 确定，D152 Reviewer 校准）**:\\\\n\\\\\\\"SFT-route benchmark contamination does not produce a single effect. Through controlled injection across 5 independent model families, we observe qualitatively different dose-response profiles spanning a 14pp range — from +3.8pp benefit (Gemma-2) to -10pp collapse (Qwen-14B). Effect direction correlates with baseline ability: lower-baseline models benefit while higher-baseline models are harmed or immune. Within the Qwen family, the 14B model is 3× more fragile than the 7B, suggesting baseline ability rather than scale alone determines vulnerability.\\\\\\\"\\\\n\\\\n**关键 D149 发现（D152 校准后表述）**:\\\\n1. **Qualitatively different dose-response profiles** — 5 families show 5 profiles（triple-seed 确认形状稳定后升级为 \\\\\\\"taxonomy\\\\\\\"；保守分类 3 种: benefit/harm/immune）\\\\n2. **Baseline-dependent direction (observed)** — 分界在 ~62-66% 区间，5 点样本，不可说 \\\\\\\"universal threshold\\\\\\\"\\\\n3. **Within-family scale effect (Qwen only)**: 14B >> 7B fragility，但 Phi-4 14.7B immune → 不是 \\\\\\\"bigger = more fragile\\\\\\\" 的一般规律\\\\n4. **Cross-benchmark consistency**: ARC 方向与 MMLU 一致（4/5 families），Gemma-2 ARC 排除（需 root cause evidence，不能只说 artifact）\\\\n5. **Benefit families 存在**: OLMo-2 和 Gemma-2 都从 contamination 受益——颠覆 \\\\\\\"contamination = harmful\\\\\\\"\\\\n\\\\n**D149 vs 旧 Qwen-only ≤3B 数据的关系**:\\\\n- 旧 ≤3B Qwen 数据中 MMLU Δ~0.7pp 被解读为 \\\\\\\"near-null\\\\\\\"——实际是 Qwen 在 ≤3B scale 的特定行为\\\\n- D149 cross-family 数据揭示 Qwen ≤3B 只是 5-pattern 中的一小部分\\\\n- 旧 domain-level IRT 分析（Simpson's paradox, STEM gradient）仍有效，作为 5-pattern 的机制解释层\\\\n\\\\n**EMNLP 预估（D149 后更新）**：5 families + 5-pattern taxonomy + baseline threshold + counter-intuitive scale finding + IRT framework + identifiability → **3.5-4.0**（Borderline Conference to Conference）。前提：triple-seed 统计验证 + claim 边界清晰 + 不 overclaim。5-pattern taxonomy 是 novel empirical contribution，baseline threshold 如果经受住 triple-seed 检验可能是 headline finding。\\\\n\\\\n### OLMo-2 \\\\\\\"Benefit-saturation\\\\\\\" 模式（D149 更新，supersedes near-null 判定）\\\\n\\\\n**[SUPERSEDED]** 旧判定 \\\\\\\"OLMo-2 near-null ±0.5pp\\\\\\\" 完全错误——来自 Qwen-only ≤3B 参考框架。Phase 2 v2 完整数据:\\\\n- MMLU: d000=53.79% → d005=56.14% → d025=56.17% → d050=57.25% → d100=57.00%\\\\n- 最大效应 +3.46pp（d050），然后 d100 轻微回落 → **benefit-saturation** 模式\\\\n- ARC: d000=76.11% → d100=80.03%（+3.92pp 单调上升）\\\\n- 最低 baseline（53.79% MMLU）→ 最强 benefit-saturation 效应\\\\n\\\\n**OLMo-2 在 5-pattern taxonomy 中的定位**:\\\\n- 与 Gemma-2（也是 benefit）一起构成 \\\\\\\"contamination helps low-baseline models\\\\\\\" 证据\\\\n- 但 OLMo-2 在 d050 后饱和，Gemma-2 持续上升 → 两种不同的 benefit 子类\\\\n- Baseline 53.8% 远低于 threshold（~64%），完美契合 baseline-threshold 假说\\\\n\\\\n**OLMo-2 模型选择 justification**：AllenAI 独立实验室 + fully open source + 独立训练数据 + 7B scale 与 Qwen 7B 对照。\\\\n\\\\n### Secondary Findings（Reviewer 评估，2026-05-18）\\\\n\\\\n**高价值（主动追踪）**:\\\\n1. **Cross-family dosage-response shape consistency**: 各 family 在相同 benchmark 上 d000→d100 曲线形状是否一致。若一致 → \\\\\\\"contamination susceptibility 是 benchmark × dosage 性质，非 model-family artifact\\\\\\\"。Claim 1 最强 generalizability evidence。\\\\n2. **γ cross-family pooling collapse**: 各 family 独立 fit 的 γ 方向一致，但 cross-family pooled γ 崩塌/反向 → \\\\\\\"contamination signals are family-specific, cross-family pooling requires family-aware calibration\\\\\\\"。有独立 contribution 级潜力。\\\\n\\\\n**中等价值（值得报告）**:\\\\n3. **Scale × family interaction at 7B band**: 7B Qwen vs 7B OLMo vs 9B Gemma 同 dosage 下 Δacc 差异。差异小(<2pp) → \\\\\\\"scale dominates\\\\\\\"；差异大 → \\\\\\\"family-specific susceptibility\\\\\\\"。归因困难（architecture vs training data confound），不宜作 headline。\\\\n\\\\n**低价值/高风险（不追踪）**:\\\\n4. Architecture-specific mechanism（需 interpretability 分析，远超当前实验能力）\\\\n\\\\n### EMNLP Reviewer Pushback 预判（Reviewer 评估）\\\\n1. **\\\\\\\"No 70B+\\\\\\\"**（~80%）: Limitations 显式讨论。Defense: compute 超 scope + ≤14.7B 已覆盖拐点区间 + 不做 extrapolation claim\\\\n2. **\\\\\\\"SFT-route only\\\\\\\"**（~60%）: 已有 defense（acknowledged limitation + exp-009 RL bridge）\\\\n3. **\\\\\\\"Scale analysis is Qwen-only\\\\\\\"**（~40%）: Cross-family 是 consistency check 不是 scaling curve\\\\n\\\\n### Claim 边界（硬约束）\\\\n1. \\\\\\\"SFT-route\\\\\\\" 限定不可去掉（未测试 pretraining contamination）\\\\n2. \\\\\\\"≤14.7B\\\\\\\" 不可说 \\\\\\\"across all scales\\\\\\\"（70B+ 未测试）\\\\n3. \\\\\\\"3 benchmarks\\\\\\\" 不可说 \\\\\\\"across benchmarks in general\\\\\\\"\\\\n4. AUGMENT mode SFT 限定（base_data + contaminated items appended, 非 REPLACE 模式）——升级 scope 后需在 paper limitations 显式提及\\\\n5. **评估协议敏感性（Reviewer D154b）**: Qwen-7B V-type recovery pattern 在 5-shot evaluate.py 下出现，但在 0-shot lm-eval-harness 下消失（MMLU 平坦/略升）。ARC 在 lm-eval 下 baseline 大幅偏移（-40pp）。所有正式结果使用 evaluate.py v3（5-shot MMLU, 25-shot ARC），内部一致。但 **dose-response profiles 是 protocol-conditional observations，不是 protocol-invariant model properties**。论文必须：(a) 明确标注评估协议，(b) 在 Limitations 讨论 prompt format 敏感性，(c) 不可 claim profiles 是 \\\\\\\"intrinsic model characteristics\\\\\\\"\\\\n\\\\n### Concern #11 升级\\\\n从 \\\\\\\"Acknowledged limitation — single model family\\\\\\\" → \\\\\\\"Addressed — 4 independent families\\\\\\\"\\\\n\\\\n### Main Figure: 5-Pattern Dose-Response Curves (D149)\\\\n- **Fig 1a (MMLU)**: X = dosage (d000→d100), Y = accuracy (%). 5 curves, one per family. Color-coded by pattern type. Shows the full taxonomy: Phi-4 flat (immune), Qwen-14B U-shape (collapse), Qwen-7B V-shape (recovery), Gemma-2 rising (benefit), OLMo-2 rising then flat (benefit-saturation).\\\\n- **Fig 1b (ARC)**: Same layout. Directionally consistent patterns (Gemma-2 excluded, noted as artifact).\\\\n- **Fig 2: Baseline vs Max Effect**: X = baseline MMLU accuracy, Y = max |Δacc| with direction. Shows the ~64% threshold. Scatter with 5 family points + regression line / threshold indicator.\\\\n- **已生成 (westd `/root/autodl-tmp/exp001/figures/`)**: mmlu_dose_response.pdf, arc_dose_response.pdf, baseline_vs_effect.pdf — 需视觉审查后决定是否需要重绘为论文级质量\\\\n\\\\n### Cross-family Analysis Strategy\\\\n- Family-level 对比（per-family independent IRT fit, report per-family γ）\\\\n- Qwen2.5-7B domain consistency check（N 最大的 family）\\\\n- 不做 hierarchical gamma model（ROI 太低, 7 天 DDL → Future Work）\\\\n- γ 跨家族池化崩塌现象作为 finding 报告\\\\n\\\\n### Paper Rewrite Scope (D149 后，待 triple-seed 验证)\\\\n- Abstract: 完全重写（~170 words，5-pattern taxonomy + baseline threshold 为核心）\\\\n- Introduction ¶4 + Contributions: 完全重写（5-pattern taxonomy 为 headline）\\\\n- Introduction ¶1-3: 小修（加 \\\\\\\"contamination can also help\\\\\\\" 铺垫）\\\\n- Results: 新增 \\\\\\\"5-Pattern Dose-Response Taxonomy\\\\\\\" + \\\\\\\"Baseline Ability Threshold\\\\\\\" + \\\\\\\"Cross-Family Consistency\\\\\\\" sections\\\\n- Results: 保留 domain-level IRT analysis 作为机制解释\\\\n- Discussion: 新增 \\\\\\\"Why Bigger ≠ More Robust\\\\\\\" + \\\\\\\"Implications for Benchmark Design\\\\\\\"\\\\n- Discussion: scale-invariance implication OR transition interpretation\\\\n- Method: 不变（加 family indicator 说明）\\\\n- Related Work: 稳定（加 1-2 句 multi-family evaluation）\\\\n- 预计 Paper Agent 2 天完成（前提: framing variant 已确定）\\\\n- **不在结果出来前开始重写**（避免 variant 错配返工）\\\\n\\\\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\\\\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\\\\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\\\\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\\\\n\\\", \\\"total_chars\\\": 33365, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight (D149: dose-response profiling + baseline-dependent direction, building on D039/D108/D115)\\n\\nBenchmark contamination does not have a single effect — controlled SFT injection across 5 independent model families reveals qualitatively different dose-response profiles depending on model baseline capability. Through injection (LoRA r=16, 5 dosage levels d000–d100) on Qwen2.5-7B, Qwen2.5-14B, Phi-4 14.7B, Gemma-2 9B, OLMo-2 7B, we observe:\\n\\n**5 observed dose-response profiles (D149, MMLU, seed=42)**:\\n| Profile | Family | Baseline | d000→d100 | Max effect |\\n|---------|--------|----------|-----------|------------|\\n| Immune | Phi-4 14.7B | 76.44% | ±0.54pp | negligible |\\n| U-type collapse | Qwen-14B | 69.44% | -9.37pp | -10.03pp@d050 |\\n| V-type recovery | Qwen-7B | 66.11% | -1.78pp | -3.13pp@d025 |\\n| Benefit | Gemma-2 9B | 61.86% | +3.76pp | monotonic rise |\\n| Benefit-saturation | OLMo-2 7B | 53.79% | +3.21pp | saturates@d050 |\\n\\n⚠️ **Claim calibration (Reviewer D152)**: N_profiles = N_families，当前数据不足以声称 5 种 \\\"discrete categories\\\"。更保守分类是 3 种（benefit / harm / immune）。5-profile 描述仅在 triple-seed 确认形状稳定后升级为 \\\"taxonomy\\\"。V-type vs U-type 区分以及 benefit vs benefit-saturation 区分需要 triple-seed 验证。\\n\\n**Baseline-dependent direction (observed in 5-family sample)**: In our sample, models below ~64% MMLU baseline benefited from contamination while those above were harmed or immune. This threshold is estimated from 5 families — the boundary lies between 61.9% (Gemma-2, benefit) and 66.1% (Qwen-7B, harm) — and may shift with additional model families. **不可说 \\\"universal threshold\\\"，只能说 \\\"observed in our sample\\\"。** 考虑 permutation test 检验二分法显著性。\\n\\n**Within-family scale finding (Qwen only)**: Within the Qwen family, the 14B model is 3× more fragile than the 7B (-10pp vs -3pp). However, Phi-4 (14.7B) is immune — so this is NOT a general \\\"bigger = more fragile\\\" claim. 正确 framing: \\\"baseline ability, not parameter count alone, determines contamination vulnerability.\\\"\\n\\nARC results are directionally consistent (OLMo-2 +3.92pp benefit; Qwen-7B -3.84pp V-type; Qwen-14B -3.41pp U-type; Phi-4 immune ±0.6pp). Gemma-2 ARC excluded due to evaluation artifact (16pp oscillation).\\n\\nThe primary contribution is the empirical characterization framework — showing that \\\"contamination = inflation\\\" is a gross oversimplification and that model-specific dose-response profiling is necessary for reliable benchmark interpretation. IRT with per-benchmark γ_k provides the statistical machinery for this characterization. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\n\\n## Core Claims (4 条 — D149 reorder: characterization as primary, D152 Reviewer calibrated)\\n\\n1. **Characterization Claim (PRIMARY — D149 dose-response profiling)**: Contamination does not uniformly inflate scores — it produces qualitatively different dose-response profiles across model families, with effect direction (benefit vs harm) correlating with baseline ability. Key evidence:\\n   - **5 families × 5 dosages × 2 benchmarks** (MMLU + ARC) with controlled SFT injection at identical LoRA config\\n   - **Baseline-dependent direction**: In our 5-family sample, models below ~62-66% MMLU benefited; above were harmed or immune\\n   - **Effect magnitude heterogeneity**: From -10pp (Qwen-14B) to +3.8pp (Gemma-2) — 14pp range across families at same dosage\\n   - **Within-family scale effect (Qwen)**: 14B 3× more fragile than 7B, suggesting baseline ability (not just scale) drives vulnerability\\n   - **Cross-benchmark consistency**: ARC direction aligns with MMLU for 4/5 families\\n   ⚠️ **Claim strength gating**: 当前 5 profiles based on seed=42 single run. 论文用 \\\"observed profiles\\\" 描述。升级为 \\\"taxonomy of discrete patterns\\\" 需要 triple-seed 确认 profile 形状稳定。如果 V-type/U-type 在 triple-seed 下合并为同一 \\\"harm\\\" 类别，降级为 3-profile (benefit/harm/immune)。\\n   **Domain-level heterogeneity (≤3B Qwen IRT analysis, D108/D115, mechanistic complement)**: Within MMLU, stratification by cognitive domain reveals Simpson's paradox: aggregate γ≈0 masks STEM gradient (Math γ=+0.97, Science γ=+0.84, CS_Eng γ≈0). Non-STEM domains show model misfit (PPP≈1.0). 注意：domain-level 分析在 ≤3B Qwen 上进行，与 7B-14.7B 5-family profiling 是不同 scale。7B-14.7B domain-level 分析列为 future work。\\n   **Paper claim scope**: 5 profiles based on 5 families × 5 dosages (seed=42; triple-seed in progress). Domain-level from ≤3B Qwen. Bounded by: SFT-route only, ≤14.7B, AUGMENT mode, 2 MCQ benchmarks.\\n\\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\\n   **C2 contingency**: \\\"Scale-dependent\\\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \\\"method-specific signal effectiveness.\\\" Min-K++ reversal remains novel regardless.\\n\\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \\\"impossibility,\\\" not merely \\\"IRT needs more data.\\\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\\n\\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: IRT ability estimation provides calibration value (GSM8K: calMAE=0.006 vs raw=0.169, ΔMAE=0.163); the γ parameter provides diagnostic value by revealing domain-differential contamination effects. These are distinct contributions: calibration improvement comes from the IRT framework itself (ability estimation decontaminates via the θ pathway), while γ characterizes where and how contamination manifests. When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates. Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion: PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. Note: vanilla 2PL ≈ 2PL+γ in MAE across all three benchmarks — γ does not improve calibration accuracy but provides the diagnostic decomposition that is Claim 1's core contribution.\\n\\n## Contributions (Hierarchical — D149/D152 calibrated)\\n\\n### Core\\n1. **Dose-response profiling across 5 model families**: Contamination effects range from -10pp to +3.8pp MMLU depending on model family, with effect direction correlating with baseline ability. No prior work has systematically profiled contamination dose-response across multiple independent families. *(Upgrades to \\\"taxonomy of N discrete patterns\\\" if triple-seed confirms profile stability; conservative framing: 3 profiles — benefit/harm/immune.)*\\n2. **Domain-dependent contamination characterization** via IRT γ_k (≤3B Qwen): Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0). Mechanistic complement to family-level profiling — contamination heterogeneity operates at multiple granularities.\\n3. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy cautionary finding. Honest reporting that RRF = S1-only in practice.\\n4. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight.\\n\\n### Supporting\\n5. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\\n6. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection across 5 families\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\n- **Our framing (D149 pivot)**: ContamCal is a diagnostic framework that uses controlled SFT injection and IRT analysis to systematically profile how contamination affects benchmark scores. Through injection across 5 independent model families (7B–14.7B), we discover that contamination produces not one but five distinct dose-response patterns, governed by a baseline ability threshold. The framework establishes both what contamination does (5-pattern taxonomy + domain-level IRT heterogeneity) and under what conditions calibration is feasible (Fisher Information identifiability boundaries). Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\n- **Headline result template (D149, D152 calibrated)**: \\\"Benchmark contamination effects span a 14pp range across model families — from +3.8pp benefit (Gemma-2 9B) to -10pp collapse (Qwen-14B) — with effect direction correlating with baseline ability: lower-baseline models benefit while higher-baseline models are harmed or immune. Within the Qwen family, the 14B model is 3× more fragile than the 7B, suggesting baseline ability rather than parameter count drives vulnerability. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = -1.2 to -2.7). Fisher Information analysis establishes that reliable parameter recovery requires N≥50 models — conditions rarely met in current LLM evaluation.\\\"\\n\\n## Venue Fit Risks\\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). ~~Risk: may expect broader model coverage beyond Qwen2.5~~ — **Resolved by D141**: 4 independent families (Qwen2.5, Phi-4, OLMo-2, Gemma-2) with controlled SFT at ≤14.7B scale.\\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \\\"new algorithm\\\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \\\"calibration is only as good as its inputs.\\\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\\n\\n## Anticipated Reviewer Concerns & Defenses\\n\\n| # | Concern | Defense | Experiment |\\n|---|---------|---------|------------|\\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \\\"best-available proxy\\\", acknowledged as limitation | exp-006, exp-009 |\\n| 4 | Scale limited to 3B | ≤14.7B controlled SFT across 4 independent families (Qwen2.5 0.5B-14B, Phi-4 14.7B, OLMo-2 7B, Gemma-2 9B; D141). 29 runs total. | D141 scope expansion |\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\\n| 11 | Single model family? | Addressed in main experiments: 4 independent families (Qwen2.5, Phi-4, OLMo-2, Gemma-2) with controlled SFT injection at identical LoRA config (D141). Qwen2.5 provides within-family scaling (0.5B-14B); 3 cross-family models validate generalizability. | D141 scope expansion |\\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \\\"S1+IRT calibration with extensible multi-signal architecture for future signals.\\\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\\n| 20 | γ doesn't improve calibration MAE over vanilla 2PL | γ's role is diagnostic (domain-differential characterization), not calibration accuracy improvement. IRT ability estimation itself provides calibration value (GSM8K ΔMAE=0.163). Vanilla 2PL ≈ 2PL+γ confirms γ is orthogonal to calibration performance — it reveals WHERE contamination acts, not HOW MUCH to adjust. | exp-006 |\\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\\n\\n## Evaluation Protocol (6 Metrics — D025 added SBC)\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\\n\\n## Benchmarks (2 main + 2 contrasts)\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \\\"benchmark-dependent contamination effects\\\" — ContamCal calibrates in both directions.\\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \\\"ContamCal identifies benchmarks not requiring calibration\\\")\\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\\n\\n## Baselines (7)\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\n\\n## Local Independence Discussion\\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\\n\\n## Required Figures (D149 updated)\\n1. **5-pattern dose-response curves** (MMLU + ARC) — paper's headline figure, already drafted on westd\\n2. **Baseline vs max effect scatter** — shows ~64% threshold, already drafted on westd\\n3. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\\n4. Signal × scale × dosage AUC heatmap (exp-008)\\n5. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\\n6. Calibrated-vs-true accuracy scatter with CIs (exp-006)\\n7. *(Optional)* Per-family IRT γ comparison (bar chart with CIs, shows cross-family heterogeneity)\\n\\n## Citation Requirements (35+ minimum, expanded per Dream D2)\\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\\nDream D2 additions (all 3 tiers flagged):\\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \\\"calibration\\\" — ours is decontamination, not probability calibration)\\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\\nD025 additions (all 3 Dream tiers flagged):\\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\\n\\n## Discussion Notes\\n\\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\\n- **Paper treatment**: Report in Discussion as \\\"capacity threshold for reliable MC evaluation.\\\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\\n\\n## Scope Expansion: ≤14.7B + 4 Families (D141, 2026-05-18)\\n\\n### Model Matrix\\n| Family | Model | Params | Released | Runs | Role |\\n|--------|-------|--------|----------|------|------|\\n| Qwen (primary) | Qwen2.5-0.5B/1.5B/3B | 0.5-3B | 2024-09 | existing | Within-family baseline (≤3B) |\\n| Qwen (primary) | Qwen2.5-7B | 7B | 2024-09 | 10 (5d×2s) | Within-family scale extension |\\n| Qwen (primary) | Qwen2.5-14B | 14B | 2024-09 | 5 (5d×1s) | Within-family scale frontier |\\n| Microsoft | Phi-4 | 14.7B | 2024-12 | 5 (5d×1s) | Cross-family, strongest 14B |\\n| Allen AI | OLMo-2-7B | 7B | 2024-11 | 5 (5d×1s) | Cross-family, fully open |\\n| Google | Gemma-2-9B | 9B | 2024-06 | 5 (5d×1s) | Cross-family, Google family |\\n\\nAll: bf16 LoRA r=16 α=32 lr=5e-5 (D140: matching ≤3B). SFT AUGMENT mode.\\n\\n### D149 Narrative: 5-Pattern Taxonomy (supersedes Variant A/B framework)\\n\\n**[SUPERSEDED]** Variant A (null) / Variant B (scale-dependent transition) 框架已被 D149 实际数据推翻。实际效应远超 \\\"null vs ~2pp 灰色地带\\\"——Qwen-14B -10pp 崩塌、OLMo-2 +3.5pp 受益。不再需要 A/B 判定。\\n\\n**Family Framing（D149 更新）**:\\n- 正确表述: \\\"5 independent model families from 5 major labs (Alibaba, Microsoft, Allen AI, Google), trained on independent corpora with distinct pre-training recipes, spanning 7B–14.7B parameters\\\"\\n- **禁止** \\\"architecture lineage\\\" framing——全是 dense decoder-only transformer，差异在 training data + lab diversity\\n- **禁止** \\\"scaling law\\\" 术语——用 \\\"baseline-dependent response pattern\\\"\\n\\n**核心叙事（D149 确定，D152 Reviewer 校准）**:\\n\\\"SFT-route benchmark contamination does not produce a single effect. Through controlled injection across 5 independent model families, we observe qualitatively different dose-response profiles spanning a 14pp range — from +3.8pp benefit (Gemma-2) to -10pp collapse (Qwen-14B). Effect direction correlates with baseline ability: lower-baseline models benefit while higher-baseline models are harmed or immune. Within the Qwen family, the 14B model is 3× more fragile than the 7B, suggesting baseline ability rather than scale alone determines vulnerability.\\\"\\n\\n**关键 D149 发现（D152 校准后表述）**:\\n1. **Qualitatively different dose-response profiles** — 5 families show 5 profiles（triple-seed 确认形状稳定后升级为 \\\"taxonomy\\\"；保守分类 3 种: benefit/harm/immune）\\n2. **Baseline-dependent direction (observed)** — 分界在 ~62-66% 区间，5 点样本，不可说 \\\"universal threshold\\\"\\n3. **Within-family scale effect (Qwen only)**: 14B >> 7B fragility，但 Phi-4 14.7B immune → 不是 \\\"bigger = more fragile\\\" 的一般规律\\n4. **Cross-benchmark consistency**: ARC 方向与 MMLU 一致（4/5 families），Gemma-2 ARC 排除（需 root cause evidence，不能只说 artifact）\\n5. **Benefit families 存在**: OLMo-2 和 Gemma-2 都从 contamination 受益——颠覆 \\\"contamination = harmful\\\"\\n\\n**D149 vs 旧 Qwen-only ≤3B 数据的关系**:\\n- 旧 ≤3B Qwen 数据中 MMLU Δ~0.7pp 被解读为 \\\"near-null\\\"——实际是 Qwen 在 ≤3B scale 的特定行为\\n- D149 cross-family 数据揭示 Qwen ≤3B 只是 5-pattern 中的一小部分\\n- 旧 domain-level IRT 分析（Simpson's paradox, STEM gradient）仍有效，作为 5-pattern 的机制解释层\\n\\n**EMNLP 预估（D149 后更新）**：5 families + 5-pattern taxonomy + baseline threshold + counter-intuitive scale finding + IRT framework + identifiability → **3.5-4.0**（Borderline Conference to Conference）。前提：triple-seed 统计验证 + claim 边界清晰 + 不 overclaim。5-pattern taxonomy 是 novel empirical contribution，baseline threshold 如果经受住 triple-seed 检验可能是 headline finding。\\n\\n### OLMo-2 \\\"Benefit-saturation\\\" 模式（D149 更新，supersedes near-null 判定）\\n\\n**[SUPERSEDED]** 旧判定 \\\"OLMo-2 near-null ±0.5pp\\\" 完全错误——来自 Qwen-only ≤3B 参考框架。Phase 2 v2 完整数据:\\n- MMLU: d000=53.79% → d005=56.14% → d025=56.17% → d050=57.25% → d100=57.00%\\n- 最大效应 +3.46pp（d050），然后 d100 轻微回落 → **benefit-saturation** 模式\\n- ARC: d000=76.11% → d100=80.03%（+3.92pp 单调上升）\\n- 最低 baseline（53.79% MMLU）→ 最强 benefit-saturation 效应\\n\\n**OLMo-2 在 5-pattern taxonomy 中的定位**:\\n- 与 Gemma-2（也是 benefit）一起构成 \\\"contamination helps low-baseline models\\\" 证据\\n- 但 OLMo-2 在 d050 后饱和，Gemma-2 持续上升 → 两种不同的 benefit 子类\\n- Baseline 53.8% 远低于 threshold（~64%），完美契合 baseline-threshold 假说\\n\\n**OLMo-2 模型选择 justification**：AllenAI 独立实验室 + fully open source + 独立训练数据 + 7B scale 与 Qwen 7B 对照。\\n\\n### Secondary Findings（Reviewer 评估，2026-05-18）\\n\\n**高价值（主动追踪）**:\\n1. **Cross-family dosage-response shape consistency**: 各 family 在相同 benchmark 上 d000→d100 曲线形状是否一致。若一致 → \\\"contamination susceptibility 是 benchmark × dosage 性质，非 model-family artifact\\\"。Claim 1 最强 generalizability evidence。\\n2. **γ cross-family pooling collapse**: 各 family 独立 fit 的 γ 方向一致，但 cross-family pooled γ 崩塌/反向 → \\\"contamination signals are family-specific, cross-family pooling requires family-aware calibration\\\"。有独立 contribution 级潜力。\\n\\n**中等价值（值得报告）**:\\n3. **Scale × family interaction at 7B band**: 7B Qwen vs 7B OLMo vs 9B Gemma 同 dosage 下 Δacc 差异。差异小(<2pp) → \\\"scale dominates\\\"；差异大 → \\\"family-specific susceptibility\\\"。归因困难（architecture vs training data confound），不宜作 headline。\\n\\n**低价值/高风险（不追踪）**:\\n4. Architecture-specific mechanism（需 interpretability 分析，远超当前实验能力）\\n\\n### EMNLP Reviewer Pushback 预判（Reviewer 评估）\\n1. **\\\"No 70B+\\\"**（~80%）: Limitations 显式讨论。Defense: compute 超 scope + ≤14.7B 已覆盖拐点区间 + 不做 extrapolation claim\\n2. **\\\"SFT-route only\\\"**（~60%）: 已有 defense（acknowledged limitation + exp-009 RL bridge）\\n3. **\\\"Scale analysis is Qwen-only\\\"**（~40%）: Cross-family 是 consistency check 不是 scaling curve\\n\\n### Claim 边界（硬约束）\\n1. \\\"SFT-route\\\" 限定不可去掉（未测试 pretraining contamination）\\n2. \\\"≤14.7B\\\" 不可说 \\\"across all scales\\\"（70B+ 未测试）\\n3. \\\"3 benchmarks\\\" 不可说 \\\"across benchmarks in general\\\"\\n4. AUGMENT mode SFT 限定（base_data + contaminated items appended, 非 REPLACE 模式）——升级 scope 后需在 paper limitations 显式提及\\n5. **评估协议敏感性（Reviewer D154b）**: Qwen-7B V-type recovery pattern 在 5-shot evaluate.py 下出现，但在 0-shot lm-eval-harness 下消失（MMLU 平坦/略升）。ARC 在 lm-eval 下 baseline 大幅偏移（-40pp）。所有正式结果使用 evaluate.py v3（5-shot MMLU, 25-shot ARC），内部一致。但 **dose-response profiles 是 protocol-conditional observations，不是 protocol-invariant model properties**。论文必须：(a) 明确标注评估协议，(b) 在 Limitations 讨论 prompt format 敏感性，(c) 不可 claim profiles 是 \\\"intrinsic model characteristics\\\"\\n\\n### Concern #11 升级\\n从 \\\"Acknowledged limitation — single model family\\\" → \\\"Addressed — 4 independent families\\\"\\n\\n### Main Figure: 5-Pattern Dose-Response Curves (D149)\\n- **Fig 1a (MMLU)**: X = dosage (d000→d100), Y = accuracy (%). 5 curves, one per family. Color-coded by pattern type. Shows the full taxonomy: Phi-4 flat (immune), Qwen-14B U-shape (collapse), Qwen-7B V-shape (recovery), Gemma-2 rising (benefit), OLMo-2 rising then flat (benefit-saturation).\\n- **Fig 1b (ARC)**: Same layout. Directionally consistent patterns (Gemma-2 excluded, noted as artifact).\\n- **Fig 2: Baseline vs Max Effect**: X = baseline MMLU accuracy, Y = max |Δacc| with direction. Shows the ~64% threshold. Scatter with 5 family points + regression line / threshold indicator.\\n- **已生成 (westd `/root/autodl-tmp/exp001/figures/`)**: mmlu_dose_response.pdf, arc_dose_response.pdf, baseline_vs_effect.pdf — 需视觉审查后决定是否需要重绘为论文级质量\\n\\n### Cross-family Analysis Strategy\\n- Family-level 对比（per-family independent IRT fit, report per-family γ）\\n- Qwen2.5-7B domain consistency check（N 最大的 family）\\n- 不做 hierarchical gamma model（ROI 太低, 7 天 DDL → Future Work）\\n- γ 跨家族池化崩塌现象作为 finding 报告\\n\\n### Paper Rewrite Scope (D149 后，待 triple-seed 验证)\\n- Abstract: 完全重写（~170 words，5-pattern taxonomy + baseline threshold 为核心）\\n- Introduction ¶4 + Contributions: 完全重写（5-pattern taxonomy 为 headline）\\n- Introduction ¶1-3: 小修（加 \\\"contamination can also help\\\" 铺垫）\\n- Results: 新增 \\\"5-Pattern Dose-Response Taxonomy\\\" + \\\"Baseline Ability Threshold\\\" + \\\"Cross-Family Consistency\\\" sections\\n- Results: 保留 domain-level IRT analysis 作为机制解释\\n- Discussion: 新增 \\\"Why Bigger ≠ More Robust\\\" + \\\"Implications for Benchmark Design\\\"\\n- Discussion: scale-invariance implication OR transition interpretation\\n- Method: 不变（加 family indicator 说明）\\n- Related Work: 稳定（加 1-2 句 multi-family evaluation）\\n- 预计 Paper Agent 2 天完成（前提: framing variant 已确定）\\n- **不在结果出来前开始重写**（避免 variant 错配返工）\\n\\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\\n\", \"total_chars\": 33365, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016JfirbfLbfFeF42nX6iwcv`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ROADMAP.md",
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
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "2d8e2192-dce4-47b1-8d5b-928477f5033a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkuHWeEQazvxh26JMpJTD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 25327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
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

_source line 11 · 2026-05-19T22:06:05.798Z_

<details><summary>↩ Tool result · `toolu_016JfirbfLbfFeF42nX6iwcv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-19 21:16 UTC | 更新原因: V-recovery 双种子确认 D165, 论文压缩 7 页 D164, westd 训练进度更新, s42 eval 完成\\n\\n## 核心方向\\n5 observed dose-response profiles + benchmark-conditionality：通过控制 SFT 注入（5 families × 5 dosages × 2+ benchmarks），发现 contamination 的**方向**由 baseline ability 决定（threshold 64.7%, CI [64.0,65.4]），**形状**由 benchmark 特性决定。Practitioners 需要 model-AND-benchmark-specific profiling。详见 paper_framing.md。\\n\\n## 当前进展\\n- **Phase**: Research + 审稿进行中（EMNLP 2026 ARR May 25，**D+1/6**）\\n- **seed=42**: 25/25 完成 ✅ + s42 aligned re-eval 完成 ✅\\n- **seed=123 训练**: westd 4 GPU（Qwen-7B 5/5 ✅, OLMo-2 d100 ~07:00, Phi-4 ~09:15, Gemma-2 ~12:00, Qwen-14B ~12:30 CST）\\n- **seed=0**: 脚本 4/4 就绪 ✅，每卡 s123→GSM8K→s0 流水线\\n- **V-recovery**: 双种子确认 ✅（D165, s42 partial + s123 full，pattern 一致，hedge 已去除）\\n- **论文**: 7 页 main text ✅（D164），sensitivity 句 + Table 1 caption 已加\\n- **Algorithm 1**: volatility fix 180/180 ✅，claim \\\"observed profiles, robust to hyperparameters\\\"\\n- **Domain decomposition**: STEM resilient / Social Sci sensitive（Appendix + 1 句，D166 pending）\\n\\n## 6 天冲刺计划\\n| 天 | 任务 | 预期收益 |\\n|----|------|---------|\\n| D+0 (5/19) ✅ | classification algo, benchmark-conditionality, evaluate.py sync, bootstrap, 论文压缩 7 页 | 基础完成 |\\n| D+1 (5/20) | s123 完成 → GSM8K d000+d100 → s0 启动, V-recovery 确认 ✅ | 第 3 benchmark + cross-seed |\\n| D+1-2 | s123 eval, GSM8K 全量, domain decomposition appendix | 深度素材 |\\n| D+2-3 (5/21-22) | s0 完成, triple-seed bootstrap, IRT 2PL+γ fitting | 全统计验证 |\\n| D+3-4 (5/22-23) | 论文更新 triple-seed + GSM8K + domain analysis | 完整素材 |\\n| D+4-5 (5/23-24) | Final polish, compile ≤8 页, 提交审稿 | 格式合规 |\\n\\n## 近期任务\\n- [x] Formal profile classification algorithm + Algorithm 1 伪代码\\n- [x] Benchmark-conditionality 升级为 finding\\n- [x] evaluate.py 跨服务器同步（md5 一致, C009 生效）\\n- [x] Bootstrap 统计（MMLU B=10000, 4/5 ≥99.6% stability）\\n- [x] V-recovery 双种子确认（D165）\\n- [x] 论文压缩 14→7 页 main text（D164）\\n- [ ] GSM8K eval（cqa1 启动中 + westd 各卡完成后立即跑）\\n- [ ] westd s123 训练完成 → 每卡 GSM8K → s0\\n- [ ] IRT 2PL+γ fitting（数据准备 Worker 在跑）\\n- [ ] Domain decomposition → Appendix（Reviewer 建议）\\n- [ ] Triple-seed bootstrap（s123+s0 eval 完成后）\\n- [ ] 论文 final update（GSM8K + triple-seed + domain analysis）\\n\\n## GPU 预算\\n- **westd**: 4× RTX PRO 6000 96GB — s123 训练 → 各卡完成后: GSM8K d000+d100 (~1h) → s0\\n- **cqa1**: 1× RTX 4090D — s42 eval 完成 → GSM8K eval 排队中\\n- 每张卡每分钟都不能空\\n\\n## 5-Pattern Data (seed=42, MMLU, aligned evaluate.py)\\n| Pattern | Family | Baseline | Δacc(d100) | s123 Δacc | Cross-seed |\\n|---------|--------|----------|-----------|-----------|------------|\\n| Immune | Phi-4 14.7B | 76.44% | −0.17pp | pending | — |\\n| U-collapse | Qwen-14B | 69.44% | −9.37pp | pending | — |\\n| V-recovery | Qwen-7B | 66.14% | −1.82pp | 0.00pp | ✅ confirmed |\\n| Benefit | Gemma-2 9B | 61.86% | +3.76pp | pending | — |\\n| Benefit-sat | OLMo-2 7B | 53.79% | +3.21pp | pending | — |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D165 | 2026-05-19 | V-recovery 双种子确认——s42 partial (Δ=-1.82pp@d100) + s | eval_qwen7b_s42_cqa1_v2, eval_qwen7b_s123_cqa1_v2 |\\n| D164 | 2026-05-19 | 论文压缩 7 页完成 + claim 保持 \\\"observed profiles, robust t | — |\\n| D163 | 2026-05-19 | D163: 保持\\\"observed profiles\\\"不升级 + V-recovery-full 归 | — |\\n| D162 | 2026-05-19 | D162: V-recovery s123 完整确认（d005 -3.22pp → d100 完全恢 | sft_qwen7b_olmo2_s123_sweep |\\n| D161 | 2026-05-19 | D161: Treated vs Untreated item analysis 完成——所有 5  | phase2_v2_eval_all |\\n| D160 | 2026-05-19 | D160: V-recovery 在 s123 定性复现（evaluate.py 修正后），5-pa | sft_qwen7b_olmo2_s123_sweep |\\n| D159 | 2026-05-19 | D159: Qwen-7B s123 未复现 V-recovery——优先诊断 eval 一致性（3 | sft_qwen7b_olmo2_s123_sweep |\\n| D158 | 2026-05-19 | D158: 采纳 Reviewer 三议题建议——(1) benchmark-conditional | — |\\n| D157 | 2026-05-19 | D157: Bootstrap 统计完成——MMLU 5-pattern 极稳定（4/5≥99.6% | — |\\n| D156 | 2026-05-19 | D156: Reviewer 竞争力评估收到——当前 2.5-3.0，P0 行动：砍页到 8 页 + | — |\\n\\n\\n\", \"total_chars\": 3839, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "68ceb50d-0fbc-4a6e-8b94-9c3d0d83113d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\\\", \\\"content\\\": \\\"# contamcal-irt-calibration — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-19 21:16 UTC | 更新原因: V-recovery 双种子确认 D165, 论文压缩 7 页 D164, westd 训练进度更新, s42 eval 完成\\\\n\\\\n## 核心方向\\\\n5 observed dose-response profiles + benchmark-conditionality：通过控制 SFT 注入（5 families × 5 dosages × 2+ benchmarks），发现 contamination 的**方向**由 baseline ability 决定（threshold 64.7%, CI [64.0,65.4]），**形状**由 benchmark 特性决定。Practitioners 需要 model-AND-benchmark-specific profiling。详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **Phase**: Research + 审稿进行中（EMNLP 2026 ARR May 25，**D+1/6**）\\\\n- **seed=42**: 25/25 完成 ✅ + s42 aligned re-eval 完成 ✅\\\\n- **seed=123 训练**: westd 4 GPU（Qwen-7B 5/5 ✅, OLMo-2 d100 ~07:00, Phi-4 ~09:15, Gemma-2 ~12:00, Qwen-14B ~12:30 CST）\\\\n- **seed=0**: 脚本 4/4 就绪 ✅，每卡 s123→GSM8K→s0 流水线\\\\n- **V-recovery**: 双种子确认 ✅（D165, s42 partial + s123 full，pattern 一致，hedge 已去除）\\\\n- **论文**: 7 页 main text ✅（D164），sensitivity 句 + Table 1 caption 已加\\\\n- **Algorithm 1**: volatility fix 180/180 ✅，claim \\\\\\\"observed profiles, robust to hyperparameters\\\\\\\"\\\\n- **Domain decomposition**: STEM resilient / Social Sci sensitive（Appendix + 1 句，D166 pending）\\\\n\\\\n## 6 天冲刺计划\\\\n| 天 | 任务 | 预期收益 |\\\\n|----|------|---------|\\\\n| D+0 (5/19) ✅ | classification algo, benchmark-conditionality, evaluate.py sync, bootstrap, 论文压缩 7 页 | 基础完成 |\\\\n| D+1 (5/20) | s123 完成 → GSM8K d000+d100 → s0 启动, V-recovery 确认 ✅ | 第 3 benchmark + cross-seed |\\\\n| D+1-2 | s123 eval, GSM8K 全量, domain decomposition appendix | 深度素材 |\\\\n| D+2-3 (5/21-22) | s0 完成, triple-seed bootstrap, IRT 2PL+γ fitting | 全统计验证 |\\\\n| D+3-4 (5/22-23) | 论文更新 triple-seed + GSM8K + domain analysis | 完整素材 |\\\\n| D+4-5 (5/23-24) | Final polish, compile ≤8 页, 提交审稿 | 格式合规 |\\\\n\\\\n## 近期任务\\\\n- [x] Formal profile classification algorithm + Algorithm 1 伪代码\\\\n- [x] Benchmark-conditionality 升级为 finding\\\\n- [x] evaluate.py 跨服务器同步（md5 一致, C009 生效）\\\\n- [x] Bootstrap 统计（MMLU B=10000, 4/5 ≥99.6% stability）\\\\n- [x] V-recovery 双种子确认（D165）\\\\n- [x] 论文压缩 14→7 页 main text（D164）\\\\n- [ ] GSM8K eval（cqa1 启动中 + westd 各卡完成后立即跑）\\\\n- [ ] westd s123 训练完成 → 每卡 GSM8K → s0\\\\n- [ ] IRT 2PL+γ fitting（数据准备 Worker 在跑）\\\\n- [ ] Domain decomposition → Appendix（Reviewer 建议）\\\\n- [ ] Triple-seed bootstrap（s123+s0 eval 完成后）\\\\n- [ ] 论文 final update（GSM8K + triple-seed + domain analysis）\\\\n\\\\n## GPU 预算\\\\n- **westd**: 4× RTX PRO 6000 96GB — s123 训练 → 各卡完成后: GSM8K d000+d100 (~1h) → s0\\\\n- **cqa1**: 1× RTX 4090D — s42 eval 完成 → GSM8K eval 排队中\\\\n- 每张卡每分钟都不能空\\\\n\\\\n## 5-Pattern Data (seed=42, MMLU, aligned evaluate.py)\\\\n| Pattern | Family | Baseline | Δacc(d100) | s123 Δacc | Cross-seed |\\\\n|---------|--------|----------|-----------|-----------|------------|\\\\n| Immune | Phi-4 14.7B | 76.44% | −0.17pp | pending | — |\\\\n| U-collapse | Qwen-14B | 69.44% | −9.37pp | pending | — |\\\\n| V-recovery | Qwen-7B | 66.14% | −1.82pp | 0.00pp | ✅ confirmed |\\\\n| Benefit | Gemma-2 9B | 61.86% | +3.76pp | pending | — |\\\\n| Benefit-sat | OLMo-2 7B | 53.79% | +3.21pp | pending | — |\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D165 | 2026-05-19 | V-recovery 双种子确认——s42 partial (Δ=-1.82pp@d100) + s | eval_qwen7b_s42_cqa1_v2, eval_qwen7b_s123_cqa1_v2 |\\\\n| D164 | 2026-05-19 | 论文压缩 7 页完成 + claim 保持 \\\\\\\"observed profiles, robust t | — |\\\\n| D163 | 2026-05-19 | D163: 保持\\\\\\\"observed profiles\\\\\\\"不升级 + V-recovery-full 归 | — |\\\\n| D162 | 2026-05-19 | D162: V-recovery s123 完整确认（d005 -3.22pp → d100 完全恢 | sft_qwen7b_olmo2_s123_sweep |\\\\n| D161 | 2026-05-19 | D161: Treated vs Untreated item analysis 完成——所有 5  | phase2_v2_eval_all |\\\\n| D160 | 2026-05-19 | D160: V-recovery 在 s123 定性复现（evaluate.py 修正后），5-pa | sft_qwen7b_olmo2_s123_sweep |\\\\n| D159 | 2026-05-19 | D159: Qwen-7B s123 未复现 V-recovery——优先诊断 eval 一致性（3 | sft_qwen7b_olmo2_s123_sweep |\\\\n| D158 | 2026-05-19 | D158: 采纳 Reviewer 三议题建议——(1) benchmark-conditional | — |\\\\n| D157 | 2026-05-19 | D157: Bootstrap 统计完成——MMLU 5-pattern 极稳定（4/5≥99.6% | — |\\\\n| D156 | 2026-05-19 | D156: Reviewer 竞争力评估收到——当前 2.5-3.0，P0 行动：砍页到 8 页 + | — |\\\\n\\\\n\\\\n\\\", \\\"total_chars\\\": 3839, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-19 21:16 UTC | 更新原因: V-recovery 双种子确认 D165, 论文压缩 7 页 D164, westd 训练进度更新, s42 eval 完成\\n\\n## 核心方向\\n5 observed dose-response profiles + benchmark-conditionality：通过控制 SFT 注入（5 families × 5 dosages × 2+ benchmarks），发现 contamination 的**方向**由 baseline ability 决定（threshold 64.7%, CI [64.0,65.4]），**形状**由 benchmark 特性决定。Practitioners 需要 model-AND-benchmark-specific profiling。详见 paper_framing.md。\\n\\n## 当前进展\\n- **Phase**: Research + 审稿进行中（EMNLP 2026 ARR May 25，**D+1/6**）\\n- **seed=42**: 25/25 完成 ✅ + s42 aligned re-eval 完成 ✅\\n- **seed=123 训练**: westd 4 GPU（Qwen-7B 5/5 ✅, OLMo-2 d100 ~07:00, Phi-4 ~09:15, Gemma-2 ~12:00, Qwen-14B ~12:30 CST）\\n- **seed=0**: 脚本 4/4 就绪 ✅，每卡 s123→GSM8K→s0 流水线\\n- **V-recovery**: 双种子确认 ✅（D165, s42 partial + s123 full，pattern 一致，hedge 已去除）\\n- **论文**: 7 页 main text ✅（D164），sensitivity 句 + Table 1 caption 已加\\n- **Algorithm 1**: volatility fix 180/180 ✅，claim \\\"observed profiles, robust to hyperparameters\\\"\\n- **Domain decomposition**: STEM resilient / Social Sci sensitive（Appendix + 1 句，D166 pending）\\n\\n## 6 天冲刺计划\\n| 天 | 任务 | 预期收益 |\\n|----|------|---------|\\n| D+0 (5/19) ✅ | classification algo, benchmark-conditionality, evaluate.py sync, bootstrap, 论文压缩 7 页 | 基础完成 |\\n| D+1 (5/20) | s123 完成 → GSM8K d000+d100 → s0 启动, V-recovery 确认 ✅ | 第 3 benchmark + cross-seed |\\n| D+1-2 | s123 eval, GSM8K 全量, domain decomposition appendix | 深度素材 |\\n| D+2-3 (5/21-22) | s0 完成, triple-seed bootstrap, IRT 2PL+γ fitting | 全统计验证 |\\n| D+3-4 (5/22-23) | 论文更新 triple-seed + GSM8K + domain analysis | 完整素材 |\\n| D+4-5 (5/23-24) | Final polish, compile ≤8 页, 提交审稿 | 格式合规 |\\n\\n## 近期任务\\n- [x] Formal profile classification algorithm + Algorithm 1 伪代码\\n- [x] Benchmark-conditionality 升级为 finding\\n- [x] evaluate.py 跨服务器同步（md5 一致, C009 生效）\\n- [x] Bootstrap 统计（MMLU B=10000, 4/5 ≥99.6% stability）\\n- [x] V-recovery 双种子确认（D165）\\n- [x] 论文压缩 14→7 页 main text（D164）\\n- [ ] GSM8K eval（cqa1 启动中 + westd 各卡完成后立即跑）\\n- [ ] westd s123 训练完成 → 每卡 GSM8K → s0\\n- [ ] IRT 2PL+γ fitting（数据准备 Worker 在跑）\\n- [ ] Domain decomposition → Appendix（Reviewer 建议）\\n- [ ] Triple-seed bootstrap（s123+s0 eval 完成后）\\n- [ ] 论文 final update（GSM8K + triple-seed + domain analysis）\\n\\n## GPU 预算\\n- **westd**: 4× RTX PRO 6000 96GB — s123 训练 → 各卡完成后: GSM8K d000+d100 (~1h) → s0\\n- **cqa1**: 1× RTX 4090D — s42 eval 完成 → GSM8K eval 排队中\\n- 每张卡每分钟都不能空\\n\\n## 5-Pattern Data (seed=42, MMLU, aligned evaluate.py)\\n| Pattern | Family | Baseline | Δacc(d100) | s123 Δacc | Cross-seed |\\n|---------|--------|----------|-----------|-----------|------------|\\n| Immune | Phi-4 14.7B | 76.44% | −0.17pp | pending | — |\\n| U-collapse | Qwen-14B | 69.44% | −9.37pp | pending | — |\\n| V-recovery | Qwen-7B | 66.14% | −1.82pp | 0.00pp | ✅ confirmed |\\n| Benefit | Gemma-2 9B | 61.86% | +3.76pp | pending | — |\\n| Benefit-sat | OLMo-2 7B | 53.79% | +3.21pp | pending | — |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D165 | 2026-05-19 | V-recovery 双种子确认——s42 partial (Δ=-1.82pp@d100) + s | eval_qwen7b_s42_cqa1_v2, eval_qwen7b_s123_cqa1_v2 |\\n| D164 | 2026-05-19 | 论文压缩 7 页完成 + claim 保持 \\\"observed profiles, robust t | — |\\n| D163 | 2026-05-19 | D163: 保持\\\"observed profiles\\\"不升级 + V-recovery-full 归 | — |\\n| D162 | 2026-05-19 | D162: V-recovery s123 完整确认（d005 -3.22pp → d100 完全恢 | sft_qwen7b_olmo2_s123_sweep |\\n| D161 | 2026-05-19 | D161: Treated vs Untreated item analysis 完成——所有 5  | phase2_v2_eval_all |\\n| D160 | 2026-05-19 | D160: V-recovery 在 s123 定性复现（evaluate.py 修正后），5-pa | sft_qwen7b_olmo2_s123_sweep |\\n| D159 | 2026-05-19 | D159: Qwen-7B s123 未复现 V-recovery——优先诊断 eval 一致性（3 | sft_qwen7b_olmo2_s123_sweep |\\n| D158 | 2026-05-19 | D158: 采纳 Reviewer 三议题建议——(1) benchmark-conditional | — |\\n| D157 | 2026-05-19 | D157: Bootstrap 统计完成——MMLU 5-pattern 极稳定（4/5≥99.6% | — |\\n| D156 | 2026-05-19 | D156: Reviewer 竞争力评估收到——当前 2.5-3.0，P0 行动：砍页到 8 页 + | — |\\n\\n\\n\", \"total_chars\": 3839, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016fKh6r6uyMaEsXDzf6VLCq`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "memory.md",
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
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "34368a6a-c469-4455-ade5-2965d6f08c00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkuHWeEQazvxh26JMpJTD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 25327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
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

_source line 13 · 2026-05-19T22:06:06.327Z_

<details><summary>↩ Tool result · `toolu_016fKh6r6uyMaEsXDzf6VLCq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Memory\\n\\n## D160 GSM8K 调度规则 (2026-05-19)\\nDirector 批准的 westd GPU 释放节奏：s123 完成 → GSM8K d000+d100 (~1h) → s0 启动。每个 family 都跑 GSM8K 两个端点。cqa1：Qwen-7B s123v2 → s42 re-eval → 空闲后排 GSM8K。\\n\\n## evaluate.py reference hash (2026-05-19)\\nwestd/cqa1 统一版本 md5=`001a9bc23f808c47d25ef9eaeecb81f1`, 37591 bytes。C009 约束：eval 前必须 md5 验证。旧版 md5=`6e2046f5ce8f2884ecc0a21b0d223822`, 35855 bytes（mc_suffix bug，+3-4pp 系统偏差）。\\n\\n## westd s123 训练进度 (更新 2026-05-20 05:10 CST)\\n- GPU2: Qwen-7B **5/5 完成** ✅，OLMo-2 d100 在跑 (19%) → ~07:00 完成\\n- GPU0: Phi-4 d050 在跑 (41%) → ~09:15 全完成\\n- GPU3: Gemma-2 d025 在跑 (83%) → ~12:00 全完成\\n- GPU1: Qwen-14B d025 在跑 (69%) → ~12:30 全完成（bottleneck）\\n\\n## GSM8K eval 能力确认 (2026-05-19)\\nevaluate.py 内置 GSM8K 支持：8-shot CoT, generation-based (max_new_tokens=256), regex 答案提取, batch_size=8。s123 脚本 5/5 就绪（`scripts/gsm8k_s123/`）。Qwen-7B d000_s42 已有 GSM8K 结果 (71.04%, 937/1319)。\\n\\n## Classification Algorithm v2 — Volatility Check (2026-05-19)\\nprofile_classifier.py v2 加入 mid-trajectory volatility check：在 Immune 候选（|Δ|≤τ）中额外计算 max_deviation = max(|acc_di - acc_d000|)，超过 τ 且有 V-dip → V-recovery-full。Sensitivity sweep v2: 180/180 全对（6 family × 30 combos），比 v1 修复 35 处、回退 0 处。参数仍为 4 个（τ=1pp, σ=5pp, ρ=0.3, λ=0.5pp）。\\n\\n## Bootstrap 结果摘要 (2026-05-19)\\nMMLU threshold: 64.7% (CI [64.0, 65.4])。4/5 模型 stability ≥99.6%，Gemma-2 76.6%。ARC threshold: 83.6% (CI [80.7, 85.9])，stability 较低（items 少）。\\n\\n## Treated vs Untreated: 无 item-level memorization (2026-05-19)\\nd025 level DiD：**所有 5 个 family 的 DiD 均不显著**。contamination 效果是 global SFT effect，不是 item-specific memorization。Difficulty interaction 也对称。\\n\\n## Qwen-7B V-recovery 双种子确认 (2026-05-20)\\n**s42 aligned** (eval_qwen7b_s42_cqa1_v2): d000=66.14, d005=64.82, d025=63.06(谷底), d050=63.10, d100=64.32。Δacc=-1.82pp（部分恢复）。\\n**s123 aligned** (eval_qwen7b_s123_cqa1_v2): d000=66.59, d005=63.37(谷底), d025=64.82, d050=65.00, d100=66.59。Δacc=0.00pp（完全恢复）。\\n两个 seed 都呈 V 形，谷底位置不同（s42@d025, s123@d005），恢复程度不同，但 pattern 一致。V-recovery hedge 可去除。\\n\\n## Domain Decomposition (2026-05-19)\\nSTEM 对 contamination 最 resilient（所有 5 family 中 |delta| 最小），Social Sciences 最敏感。方向由 archetype 决定，不存在 \\\"STEM 涨 non-STEM 跌\\\" 的交叉效应。\\n\\n## eval_qwen7b_s42_cqa1_v2 诊断 (2026-05-19)\\n\\n**根因：误报。实验已于 2026-05-20 05:07 CST 正常完成，cron 监控将正常退出误判为失败。**\\n\\n详细分析：\\n- 脚本 03:42 启动，05:07 完成，共 ~85 分钟评估 5 个 dosage × 2 benchmarks\\n- 全部 5 个 dosage (d000/d005/d025/d050/d100) 的 `.done` sentinel 已写入\\n- 结果文件完整：每个目录含 eval_results.json, correctness_matrix.json, item_responses.json, mmlu_results.json, arc_challenge_results.json, eval_meta.json\\n- evaluate.py md5 验证通过 (001a9bc23f808c47d25ef9eaeecb81f1)\\n- bitsandbytes 有 libnvJitLink.so.13 加载警告但不影响功能\\n\\ncron 误报原因：\\n1. 进程正常退出后 cron 检测到\\\"进程已死\\\"，但这是正常完成而非崩溃\\n2. 脚本不写 W&B metrics，cron 检查 W&B 无数据也视为异常\\n3. 可能 cron 在脚本完成后才开始第一次检查，从未观察到运行态\\n\\n部分结果：不适用——**全部结果完整可用**。\\n\\n磁盘注意：/root/autodl-tmp 使用率 98% (4.7G 剩余)，未影响此实验但后续任务需关注。\\n\\nGPU 0 当前状态：PID 285390 正在运行 GSM8K eval (qwen7b_d000_s42)，于 05:19 启动，是后续任务而非此实验残留。\\n\", \"total_chars\": 2900, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "b1655fd7-87a2-4d26-b86a-0dcbbead8fc2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\\\", \\\"content\\\": \\\"# Memory\\\\n\\\\n## D160 GSM8K 调度规则 (2026-05-19)\\\\nDirector 批准的 westd GPU 释放节奏：s123 完成 → GSM8K d000+d100 (~1h) → s0 启动。每个 family 都跑 GSM8K 两个端点。cqa1：Qwen-7B s123v2 → s42 re-eval → 空闲后排 GSM8K。\\\\n\\\\n## evaluate.py reference hash (2026-05-19)\\\\nwestd/cqa1 统一版本 md5=`001a9bc23f808c47d25ef9eaeecb81f1`, 37591 bytes。C009 约束：eval 前必须 md5 验证。旧版 md5=`6e2046f5ce8f2884ecc0a21b0d223822`, 35855 bytes（mc_suffix bug，+3-4pp 系统偏差）。\\\\n\\\\n## westd s123 训练进度 (更新 2026-05-20 05:10 CST)\\\\n- GPU2: Qwen-7B **5/5 完成** ✅，OLMo-2 d100 在跑 (19%) → ~07:00 完成\\\\n- GPU0: Phi-4 d050 在跑 (41%) → ~09:15 全完成\\\\n- GPU3: Gemma-2 d025 在跑 (83%) → ~12:00 全完成\\\\n- GPU1: Qwen-14B d025 在跑 (69%) → ~12:30 全完成（bottleneck）\\\\n\\\\n## GSM8K eval 能力确认 (2026-05-19)\\\\nevaluate.py 内置 GSM8K 支持：8-shot CoT, generation-based (max_new_tokens=256), regex 答案提取, batch_size=8。s123 脚本 5/5 就绪（`scripts/gsm8k_s123/`）。Qwen-7B d000_s42 已有 GSM8K 结果 (71.04%, 937/1319)。\\\\n\\\\n## Classification Algorithm v2 — Volatility Check (2026-05-19)\\\\nprofile_classifier.py v2 加入 mid-trajectory volatility check：在 Immune 候选（|Δ|≤τ）中额外计算 max_deviation = max(|acc_di - acc_d000|)，超过 τ 且有 V-dip → V-recovery-full。Sensitivity sweep v2: 180/180 全对（6 family × 30 combos），比 v1 修复 35 处、回退 0 处。参数仍为 4 个（τ=1pp, σ=5pp, ρ=0.3, λ=0.5pp）。\\\\n\\\\n## Bootstrap 结果摘要 (2026-05-19)\\\\nMMLU threshold: 64.7% (CI [64.0, 65.4])。4/5 模型 stability ≥99.6%，Gemma-2 76.6%。ARC threshold: 83.6% (CI [80.7, 85.9])，stability 较低（items 少）。\\\\n\\\\n## Treated vs Untreated: 无 item-level memorization (2026-05-19)\\\\nd025 level DiD：**所有 5 个 family 的 DiD 均不显著**。contamination 效果是 global SFT effect，不是 item-specific memorization。Difficulty interaction 也对称。\\\\n\\\\n## Qwen-7B V-recovery 双种子确认 (2026-05-20)\\\\n**s42 aligned** (eval_qwen7b_s42_cqa1_v2): d000=66.14, d005=64.82, d025=63.06(谷底), d050=63.10, d100=64.32。Δacc=-1.82pp（部分恢复）。\\\\n**s123 aligned** (eval_qwen7b_s123_cqa1_v2): d000=66.59, d005=63.37(谷底), d025=64.82, d050=65.00, d100=66.59。Δacc=0.00pp（完全恢复）。\\\\n两个 seed 都呈 V 形，谷底位置不同（s42@d025, s123@d005），恢复程度不同，但 pattern 一致。V-recovery hedge 可去除。\\\\n\\\\n## Domain Decomposition (2026-05-19)\\\\nSTEM 对 contamination 最 resilient（所有 5 family 中 |delta| 最小），Social Sciences 最敏感。方向由 archetype 决定，不存在 \\\\\\\"STEM 涨 non-STEM 跌\\\\\\\" 的交叉效应。\\\\n\\\\n## eval_qwen7b_s42_cqa1_v2 诊断 (2026-05-19)\\\\n\\\\n**根因：误报。实验已于 2026-05-20 05:07 CST 正常完成，cron 监控将正常退出误判为失败。**\\\\n\\\\n详细分析：\\\\n- 脚本 03:42 启动，05:07 完成，共 ~85 分钟评估 5 个 dosage × 2 benchmarks\\\\n- 全部 5 个 dosage (d000/d005/d025/d050/d100) 的 `.done` sentinel 已写入\\\\n- 结果文件完整：每个目录含 eval_results.json, correctness_matrix.json, item_responses.json, mmlu_results.json, arc_challenge_results.json, eval_meta.json\\\\n- evaluate.py md5 验证通过 (001a9bc23f808c47d25ef9eaeecb81f1)\\\\n- bitsandbytes 有 libnvJitLink.so.13 加载警告但不影响功能\\\\n\\\\ncron 误报原因：\\\\n1. 进程正常退出后 cron 检测到\\\\\\\"进程已死\\\\\\\"，但这是正常完成而非崩溃\\\\n2. 脚本不写 W&B metrics，cron 检查 W&B 无数据也视为异常\\\\n3. 可能 cron 在脚本完成后才开始第一次检查，从未观察到运行态\\\\n\\\\n部分结果：不适用——**全部结果完整可用**。\\\\n\\\\n磁盘注意：/root/autodl-tmp 使用率 98% (4.7G 剩余)，未影响此实验但后续任务需关注。\\\\n\\\\nGPU 0 当前状态：PID 285390 正在运行 GSM8K eval (qwen7b_d000_s42)，于 05:19 启动，是后续任务而非此实验残留。\\\\n\\\", \\\"total_chars\\\": 2900, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Memory\\n\\n## D160 GSM8K 调度规则 (2026-05-19)\\nDirector 批准的 westd GPU 释放节奏：s123 完成 → GSM8K d000+d100 (~1h) → s0 启动。每个 family 都跑 GSM8K 两个端点。cqa1：Qwen-7B s123v2 → s42 re-eval → 空闲后排 GSM8K。\\n\\n## evaluate.py reference hash (2026-05-19)\\nwestd/cqa1 统一版本 md5=`001a9bc23f808c47d25ef9eaeecb81f1`, 37591 bytes。C009 约束：eval 前必须 md5 验证。旧版 md5=`6e2046f5ce8f2884ecc0a21b0d223822`, 35855 bytes（mc_suffix bug，+3-4pp 系统偏差）。\\n\\n## westd s123 训练进度 (更新 2026-05-20 05:10 CST)\\n- GPU2: Qwen-7B **5/5 完成** ✅，OLMo-2 d100 在跑 (19%) → ~07:00 完成\\n- GPU0: Phi-4 d050 在跑 (41%) → ~09:15 全完成\\n- GPU3: Gemma-2 d025 在跑 (83%) → ~12:00 全完成\\n- GPU1: Qwen-14B d025 在跑 (69%) → ~12:30 全完成（bottleneck）\\n\\n## GSM8K eval 能力确认 (2026-05-19)\\nevaluate.py 内置 GSM8K 支持：8-shot CoT, generation-based (max_new_tokens=256), regex 答案提取, batch_size=8。s123 脚本 5/5 就绪（`scripts/gsm8k_s123/`）。Qwen-7B d000_s42 已有 GSM8K 结果 (71.04%, 937/1319)。\\n\\n## Classification Algorithm v2 — Volatility Check (2026-05-19)\\nprofile_classifier.py v2 加入 mid-trajectory volatility check：在 Immune 候选（|Δ|≤τ）中额外计算 max_deviation = max(|acc_di - acc_d000|)，超过 τ 且有 V-dip → V-recovery-full。Sensitivity sweep v2: 180/180 全对（6 family × 30 combos），比 v1 修复 35 处、回退 0 处。参数仍为 4 个（τ=1pp, σ=5pp, ρ=0.3, λ=0.5pp）。\\n\\n## Bootstrap 结果摘要 (2026-05-19)\\nMMLU threshold: 64.7% (CI [64.0, 65.4])。4/5 模型 stability ≥99.6%，Gemma-2 76.6%。ARC threshold: 83.6% (CI [80.7, 85.9])，stability 较低（items 少）。\\n\\n## Treated vs Untreated: 无 item-level memorization (2026-05-19)\\nd025 level DiD：**所有 5 个 family 的 DiD 均不显著**。contamination 效果是 global SFT effect，不是 item-specific memorization。Difficulty interaction 也对称。\\n\\n## Qwen-7B V-recovery 双种子确认 (2026-05-20)\\n**s42 aligned** (eval_qwen7b_s42_cqa1_v2): d000=66.14, d005=64.82, d025=63.06(谷底), d050=63.10, d100=64.32。Δacc=-1.82pp（部分恢复）。\\n**s123 aligned** (eval_qwen7b_s123_cqa1_v2): d000=66.59, d005=63.37(谷底), d025=64.82, d050=65.00, d100=66.59。Δacc=0.00pp（完全恢复）。\\n两个 seed 都呈 V 形，谷底位置不同（s42@d025, s123@d005），恢复程度不同，但 pattern 一致。V-recovery hedge 可去除。\\n\\n## Domain Decomposition (2026-05-19)\\nSTEM 对 contamination 最 resilient（所有 5 family 中 |delta| 最小），Social Sciences 最敏感。方向由 archetype 决定，不存在 \\\"STEM 涨 non-STEM 跌\\\" 的交叉效应。\\n\\n## eval_qwen7b_s42_cqa1_v2 诊断 (2026-05-19)\\n\\n**根因：误报。实验已于 2026-05-20 05:07 CST 正常完成，cron 监控将正常退出误判为失败。**\\n\\n详细分析：\\n- 脚本 03:42 启动，05:07 完成，共 ~85 分钟评估 5 个 dosage × 2 benchmarks\\n- 全部 5 个 dosage (d000/d005/d025/d050/d100) 的 `.done` sentinel 已写入\\n- 结果文件完整：每个目录含 eval_results.json, correctness_matrix.json, item_responses.json, mmlu_results.json, arc_challenge_results.json, eval_meta.json\\n- evaluate.py md5 验证通过 (001a9bc23f808c47d25ef9eaeecb81f1)\\n- bitsandbytes 有 libnvJitLink.so.13 加载警告但不影响功能\\n\\ncron 误报原因：\\n1. 进程正常退出后 cron 检测到\\\"进程已死\\\"，但这是正常完成而非崩溃\\n2. 脚本不写 W&B metrics，cron 检查 W&B 无数据也视为异常\\n3. 可能 cron 在脚本完成后才开始第一次检查，从未观察到运行态\\n\\n部分结果：不适用——**全部结果完整可用**。\\n\\n磁盘注意：/root/autodl-tmp 使用率 98% (4.7G 剩余)，未影响此实验但后续任务需关注。\\n\\nGPU 0 当前状态：PID 285390 正在运行 GSM8K eval (qwen7b_d000_s42)，于 05:19 启动，是后续任务而非此实验残留。\\n\", \"total_chars\": 2900, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_01Yb1cByvsWQb5ZJ5xP2iXtm`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "dfa6bf5f-e5c2-4869-b0d0-814da3d1bf62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkuHWeEQazvxh26JMpJTD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 25327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
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

_source line 15 · 2026-05-19T22:06:06.954Z_

<details><summary>↩ Tool result · `toolu_01Yb1cByvsWQb5ZJ5xP2iXtm`</summary>

```text
paper/sections/method.md
paper/sections/discussion.md
paper/sections/experimental_setup.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "87dc086d-fa54-4f48-8015-7d3a58b32374",
  "tool_use_result": {
    "filenames": [
      "paper/sections/method.md",
      "paper/sections/discussion.md",
      "paper/sections/experimental_setup.md"
    ],
    "durationMs": 16,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the full paper directory and read the existing section files to understand the current content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "bba487bb-974e-4d28-b45b-fd1a99684473",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpGiZeP3kpckpBgG1pqZ8d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16587,
      "cache_read_input_tokens": 26686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16587
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

Let me read the existing paper sections and check for other paper-related files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "4e395654-1d11-4164-8198-c2e42c7a9b7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpGiZeP3kpckpBgG1pqZ8d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16587,
      "cache_read_input_tokens": 26686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16587
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

<details open><summary>🔧 Tool call — Read · `toolu_01YNRLfCYysE98Bu5yxWkp8v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/method.md",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "de84bad0-702e-4f19-80bc-4bca87159010",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpGiZeP3kpckpBgG1pqZ8d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16587,
      "cache_read_input_tokens": 26686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16587
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

_source line 19 · 2026-05-19T22:06:11.065Z_

<details><summary>↩ Tool result · `toolu_01YNRLfCYysE98Bu5yxWkp8v`</summary>

```text
1	## 3 Method
2	
3	ContamCal is a two-stage framework that maps observed item responses and contamination exposure signals to calibrated ability estimates. Stage 1 produces per-item exposure scores from multiple detection signals via training-free fusion. Stage 2 fits a contamination-augmented IRT model that decomposes observed performance into latent ability and contamination effects.
4	
5	### 3.1 Problem Formulation
6	
7	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model $j$ ($j=1,\ldots,J$) to item $i$ ($i=1,\ldots,I_k$) on benchmark $k$. Standard IRT models assume $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ are item parameters. When training data contains benchmark items, observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
8	
9	Our goal is to estimate $\theta_j^{\text{clean}}$, the decontaminated ability---what model $j$'s performance would be had it never encountered the test items during training. We approach this through contamination-augmented IRT, drawing on item compromise IRT (Eckerly, 2017; Sinharay, 2017) and explanatory IRT (De Boeck & Wilson, 2004). Adapting these frameworks to LLM evaluation requires three structural modifications:
10	
11	**(a) Independent examinees $\to$ shared item distribution.** Classical IRT assumes independent test-takers. In LLM evaluation, a single model produces all item responses, and items are fixed across models. We treat the model ensemble as the examinee population and fit per-benchmark to limit local independence violations.
12	
13	**(b) Binary leakage $\to$ continuous exposure.** Item compromise IRT uses binary indicators (leaked / not leaked). LLM contamination is graded: a model may have seen an item zero, once, or hundreds of times during training. We replace binary indicators with continuous exposure scores $e_{ij} \in [0,1]$ estimated from detection signals.
14	
15	**(c) Stable ability $\to$ regime-conditional ability.** In educational testing, ability is approximately constant regardless of item compromise status. For LLMs, contamination can alter internal representations, so we model ability as conditional on the contamination regime and recover clean ability via counterfactual inference.
16	
17	### 3.2 Stage 1: Multi-Signal Exposure Mapping
18	
19	We estimate per-item exposure scores from three complementary contamination detection signals:
20	
21	**S1: Embedding similarity.** Cosine similarity between the sentence embedding of each benchmark item and its nearest neighbor in the SFT training corpus, computed via a frozen encoder. High similarity indicates verbatim or near-verbatim inclusion.
22	
23	**S2: Min-K++ (Zhang et al., 2024).** A membership inference signal based on the model's own token-level surprisal distribution. Items seen during training are expected to exhibit lower perplexity on their rarest tokens. We include this signal despite known failure modes (Section 5.2) to systematically characterize signal reliability across scales.
24	
25	**S4: Self-critique (Weller et al., 2024).** A generation-based signal where the model is prompted to assess whether it has encountered a given item during training.
26	
27	We exclude S3 (ConStat; Dekoninck et al., 2024) because its gap-based statistic produces zero values for items where all answer options have identical surprisal, diluting the signal, and its low item coverage introduces selection bias.
28	
29	**Aggregation.** We fuse signals via Reciprocal Rank Fusion (RRF; Cormack et al., 2009):
30	
31	$$e_i^{\text{raw}} = \sum_{s \in \mathcal{S}} \frac{w_s}{k + \text{rank}_s(i)}$$
32	
33	where $\text{rank}_s(i)$ is the rank of item $i$ under signal $s$ (rank 1 = most suspicious), $k=60$ is the smoothing constant, and $w_s = 1$ for all signals. Raw scores are min-max normalized per model to obtain $e_{ij} \in [0,1]$.
34	
35	RRF is a training-free fusion method. This is a deliberate design choice rather than a limitation: any learned aggregator requires labeled training data, but contamination labels are precisely what we lack---the aggregator's training data may itself be contaminated. We term this the *meta-circularity* problem. RRF sidesteps it by operating on rank orderings without parameter estimation.
36	
37	### 3.3 Stage 2: Contamination-Augmented IRT
38	
39	We extend the four-parameter logistic (4PL) IRT model with a contamination covariate. For each benchmark $k$, fitted independently:
40	
41	$$P(y_{ijk}=1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr)$$
42	
43	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i$ is item difficulty, $c_i \in (0,1)$ is the guessing asymptote, $d_i \in (0,1)$ is the ceiling asymptote, $\theta_j$ is model ability, $e_{ij}$ is the exposure score from Stage 1, and $\gamma_k$ is the benchmark-specific contamination effect.
44	
45	The contamination term $\gamma_k \cdot e_{ij}$ enters additively on the logit scale, outside the discrimination parameter $a_i$. This makes $\gamma_k$ directly interpretable: it represents the logit shift for a maximally exposed item ($e_{ij}=1$) relative to a clean item ($e_{ij}=0$), uniformly across items regardless of their discrimination.
46	
47	Crucially, $\gamma_k$ is signed: $\gamma_k > 0$ indicates performance inflation (memorization benefit), while $\gamma_k < 0$ indicates interference or forgetting---a possibility absent from the implicit "contamination = uniform inflation" assumption in most prior work. Per-benchmark fitting (rather than a joint model with shared $\gamma$) is our primary specification, reflecting the empirical finding that contamination effects are heterogeneous across benchmarks (Section 5.1).
48	
49	We also fit 2PL+$\gamma$ as a reduced model (omitting $c_i$, $d_i$) for benchmarks where guessing and ceiling effects are minimal, such as free-form generation tasks.
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "1955bcd0-8476-4e95-8616-b1945959f14a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/method.md",
      "content": "## 3 Method\n\nContamCal is a two-stage framework that maps observed item responses and contamination exposure signals to calibrated ability estimates. Stage 1 produces per-item exposure scores from multiple detection signals via training-free fusion. Stage 2 fits a contamination-augmented IRT model that decomposes observed performance into latent ability and contamination effects.\n\n### 3.1 Problem Formulation\n\nLet $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model $j$ ($j=1,\\ldots,J$) to item $i$ ($i=1,\\ldots,I_k$) on benchmark $k$. Standard IRT models assume $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ are item parameters. When training data contains benchmark items, observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.\n\nOur goal is to estimate $\\theta_j^{\\text{clean}}$, the decontaminated ability---what model $j$'s performance would be had it never encountered the test items during training. We approach this through contamination-augmented IRT, drawing on item compromise IRT (Eckerly, 2017; Sinharay, 2017) and explanatory IRT (De Boeck & Wilson, 2004). Adapting these frameworks to LLM evaluation requires three structural modifications:\n\n**(a) Independent examinees $\\to$ shared item distribution.** Classical IRT assumes independent test-takers. In LLM evaluation, a single model produces all item responses, and items are fixed across models. We treat the model ensemble as the examinee population and fit per-benchmark to limit local independence violations.\n\n**(b) Binary leakage $\\to$ continuous exposure.** Item compromise IRT uses binary indicators (leaked / not leaked). LLM contamination is graded: a model may have seen an item zero, once, or hundreds of times during training. We replace binary indicators with continuous exposure scores $e_{ij} \\in [0,1]$ estimated from detection signals.\n\n**(c) Stable ability $\\to$ regime-conditional ability.** In educational testing, ability is approximately constant regardless of item compromise status. For LLMs, contamination can alter internal representations, so we model ability as conditional on the contamination regime and recover clean ability via counterfactual inference.\n\n### 3.2 Stage 1: Multi-Signal Exposure Mapping\n\nWe estimate per-item exposure scores from three complementary contamination detection signals:\n\n**S1: Embedding similarity.** Cosine similarity between the sentence embedding of each benchmark item and its nearest neighbor in the SFT training corpus, computed via a frozen encoder. High similarity indicates verbatim or near-verbatim inclusion.\n\n**S2: Min-K++ (Zhang et al., 2024).** A membership inference signal based on the model's own token-level surprisal distribution. Items seen during training are expected to exhibit lower perplexity on their rarest tokens. We include this signal despite known failure modes (Section 5.2) to systematically characterize signal reliability across scales.\n\n**S4: Self-critique (Weller et al., 2024).** A generation-based signal where the model is prompted to assess whether it has encountered a given item during training.\n\nWe exclude S3 (ConStat; Dekoninck et al., 2024) because its gap-based statistic produces zero values for items where all answer options have identical surprisal, diluting the signal, and its low item coverage introduces selection bias.\n\n**Aggregation.** We fuse signals via Reciprocal Rank Fusion (RRF; Cormack et al., 2009):\n\n$$e_i^{\\text{raw}} = \\sum_{s \\in \\mathcal{S}} \\frac{w_s}{k + \\text{rank}_s(i)}$$\n\nwhere $\\text{rank}_s(i)$ is the rank of item $i$ under signal $s$ (rank 1 = most suspicious), $k=60$ is the smoothing constant, and $w_s = 1$ for all signals. Raw scores are min-max normalized per model to obtain $e_{ij} \\in [0,1]$.\n\nRRF is a training-free fusion method. This is a deliberate design choice rather than a limitation: any learned aggregator requires labeled training data, but contamination labels are precisely what we lack---the aggregator's training data may itself be contaminated. We term this the *meta-circularity* problem. RRF sidesteps it by operating on rank orderings without parameter estimation.\n\n### 3.3 Stage 2: Contamination-Augmented IRT\n\nWe extend the four-parameter logistic (4PL) IRT model with a contamination covariate. For each benchmark $k$, fitted independently:\n\n$$P(y_{ijk}=1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr)$$\n\nwhere $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i$ is item difficulty, $c_i \\in (0,1)$ is the guessing asymptote, $d_i \\in (0,1)$ is the ceiling asymptote, $\\theta_j$ is model ability, $e_{ij}$ is the exposure score from Stage 1, and $\\gamma_k$ is the benchmark-specific contamination effect.\n\nThe contamination term $\\gamma_k \\cdot e_{ij}$ enters additively on the logit scale, outside the discrimination parameter $a_i$. This makes $\\gamma_k$ directly interpretable: it represents the logit shift for a maximally exposed item ($e_{ij}=1$) relative to a clean item ($e_{ij}=0$), uniformly across items regardless of their discrimination.\n\nCrucially, $\\gamma_k$ is signed: $\\gamma_k > 0$ indicates performance inflation (memorization benefit), while $\\gamma_k < 0$ indicates interference or forgetting---a possibility absent from the implicit \"contamination = uniform inflation\" assumption in most prior work. Per-benchmark fitting (rather than a joint model with shared $\\gamma$) is our primary specification, reflecting the empirical finding that contamination effects are heterogeneous across benchmarks (Section 5.1).\n\nWe also fit 2PL+$\\gamma$ as a reduced model (omitting $c_i$, $d_i$) for benchmarks where guessing and ceiling effects are minimal, such as free-form generation tasks.\n",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 68
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01Xjvyot1tJGwLfq3wWJkqkU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/discussion.md",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "6b640956-8643-42a5-8376-0c6cb520e4e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpGiZeP3kpckpBgG1pqZ8d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16587,
      "cache_read_input_tokens": 26686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16587
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

_source line 21 · 2026-05-19T22:06:12.005Z_

<details><summary>↩ Tool result · `toolu_01Xjvyot1tJGwLfq3wWJkqkU`</summary>

```text
1	## 6 Discussion
2	
3	### 6.1 Dilution Masking and Aggregate Scores
4	
5	The domain-level analysis reveals a fundamental problem with aggregate benchmark scores as contamination indicators. Pooling across MMLU domains yields $\gamma \approx 0$, which appears to indicate no contamination effect. This conclusion is false: Math ($\gamma = 0.97$) and Science ($\gamma = 0.84$) exhibit strong inflation, while non-STEM domains show structural misfit. The aggregate simply averages opposing signals into apparent nullity. This dilution masking phenomenon implies that any contamination detection or mitigation strategy operating on aggregate benchmark scores will systematically miss domain-specific effects. A model family contaminated on STEM training data would pass aggregate-level screening while carrying substantial domain-level inflation. The practical consequence is clear: contamination auditing must operate at the domain or subject level, not the benchmark level.
6	
7	### 6.2 Model Misfit as a Methodological Boundary
8	
9	Non-STEM domains consistently produce posterior predictive p-values near 1.0, indicating that the additive $\gamma$ formulation is structurally inadequate for these domains. This result is not a failure of our framework but a principled boundary: the 2PL+$\gamma$ model assumes contamination acts as a uniform logit shift across items within a domain. When contamination effects are item-specific or interact with latent subdimensions (e.g., reading comprehension vs. factual recall within Humanities), the additive assumption breaks down. Multidimensional IRT \citep{reckase2009} offers a natural extension, modeling contamination effects along domain-specific latent dimensions rather than as a single scalar. The consistent PPP $\approx 1.0$ pattern provides a diagnostic signal for when such extensions are needed: high PPP flags domains where the model fit should not be interpreted, rather than silently producing unreliable estimates.
10	
11	### 6.3 Capacity Thresholds for IRT-Based Evaluation
12	
13	The 0.5B models exhibit position bias on multiple-choice benchmarks (MMLU, ARC), selecting answers based on option position rather than content. This violates the IRT assumption that item responses reflect latent ability interacting with item difficulty. Below a capacity threshold, models lack the representational capacity to process MC items as intended, and IRT parameter estimates become meaningless. We excluded 0.5B MC data from IRT fitting for this reason. This observation suggests a practical prerequisite for IRT-based LLM evaluation: models must demonstrate format competence (accuracy significantly above chance with no position bias) before their responses can be treated as informative item-level measurements.
14	
15	### 6.4 SFT Injection as a Contamination Proxy
16	
17	Our controlled injection protocol uses supervised fine-tuning on benchmark items, which differs from natural contamination in several respects. Real contamination is gradual, originates from heterogeneous sources, and occurs alongside diverse training data. SFT injection is concentrated and homogeneous. The Llama-3.2-3B d100 MMLU collapse (all outputs converge to option 'A', accuracy 0.34) illustrates this distinction: 100% injection of MC items causes format overfitting that would not arise from natural pretraining contamination. Notably, this collapse is format-specific. ARC and GSM8K at the same dosage behave normally, suggesting that dense MC-format injection uniquely triggers position bias collapse in certain architectures. We report this as a boundary condition of our injection protocol rather than a finding about contamination in general.
18	
19	### 6.5 Limitations
20	
21	Several scope constraints bound the present findings. First, our primary analysis uses a single model family (Qwen2.5 at 0.5B, 1.5B, 3B). Cross-family analysis with Llama-3.2-3B is exploratory ($N=4$, single seed), sufficient to demonstrate family-specificity of $\gamma$ but not to establish generalizable contamination patterns. Second, the ensemble sizes achievable in practice ($N = 16$--$24$) fall below the $N \geq 50$ threshold where simulation shows reliable $\gamma$ recovery. Our empirical $\gamma$ estimates carry wider credible intervals than nominal coverage suggests (empirical coverage 20--69% at the 95% level), and should be interpreted as directional indicators rather than precise effect sizes. Third, the identifiability constraints we characterize are specific to the IRT framework combined with membership-inference signals; they do not constitute a general impossibility result for contamination quantification. Alternative frameworks operating on different assumptions (e.g., data attribution methods with training corpus access) may circumvent these bounds entirely.
22	
23	### 6.6 Future Directions
24	
25	Three extensions address the primary limitations. First, scaling to additional model families at 7B+ parameters would test whether domain-differential patterns replicate beyond Qwen2.5 and whether larger capacity further attenuates contamination effects. Second, observational studies on models with known pretraining composition (where ground-truth exposure is available without injection) would validate whether IRT-diagnosed $\gamma$ patterns correspond to actual contamination in naturalistic settings. Third, replacing membership-inference signals with data attribution methods (e.g., influence functions or training data tracing) could provide exposure scores with known ground-truth calibration, potentially resolving the signal failure problem that limits Stage 1 reliability. Extending to multidimensional IRT for non-STEM domains remains a theoretical priority but requires substantially larger model ensembles than currently available.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "f8a7c896-9627-4924-8d0a-f24d078e7e19",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/discussion.md",
      "content": "## 6 Discussion\n\n### 6.1 Dilution Masking and Aggregate Scores\n\nThe domain-level analysis reveals a fundamental problem with aggregate benchmark scores as contamination indicators. Pooling across MMLU domains yields $\\gamma \\approx 0$, which appears to indicate no contamination effect. This conclusion is false: Math ($\\gamma = 0.97$) and Science ($\\gamma = 0.84$) exhibit strong inflation, while non-STEM domains show structural misfit. The aggregate simply averages opposing signals into apparent nullity. This dilution masking phenomenon implies that any contamination detection or mitigation strategy operating on aggregate benchmark scores will systematically miss domain-specific effects. A model family contaminated on STEM training data would pass aggregate-level screening while carrying substantial domain-level inflation. The practical consequence is clear: contamination auditing must operate at the domain or subject level, not the benchmark level.\n\n### 6.2 Model Misfit as a Methodological Boundary\n\nNon-STEM domains consistently produce posterior predictive p-values near 1.0, indicating that the additive $\\gamma$ formulation is structurally inadequate for these domains. This result is not a failure of our framework but a principled boundary: the 2PL+$\\gamma$ model assumes contamination acts as a uniform logit shift across items within a domain. When contamination effects are item-specific or interact with latent subdimensions (e.g., reading comprehension vs. factual recall within Humanities), the additive assumption breaks down. Multidimensional IRT \\citep{reckase2009} offers a natural extension, modeling contamination effects along domain-specific latent dimensions rather than as a single scalar. The consistent PPP $\\approx 1.0$ pattern provides a diagnostic signal for when such extensions are needed: high PPP flags domains where the model fit should not be interpreted, rather than silently producing unreliable estimates.\n\n### 6.3 Capacity Thresholds for IRT-Based Evaluation\n\nThe 0.5B models exhibit position bias on multiple-choice benchmarks (MMLU, ARC), selecting answers based on option position rather than content. This violates the IRT assumption that item responses reflect latent ability interacting with item difficulty. Below a capacity threshold, models lack the representational capacity to process MC items as intended, and IRT parameter estimates become meaningless. We excluded 0.5B MC data from IRT fitting for this reason. This observation suggests a practical prerequisite for IRT-based LLM evaluation: models must demonstrate format competence (accuracy significantly above chance with no position bias) before their responses can be treated as informative item-level measurements.\n\n### 6.4 SFT Injection as a Contamination Proxy\n\nOur controlled injection protocol uses supervised fine-tuning on benchmark items, which differs from natural contamination in several respects. Real contamination is gradual, originates from heterogeneous sources, and occurs alongside diverse training data. SFT injection is concentrated and homogeneous. The Llama-3.2-3B d100 MMLU collapse (all outputs converge to option 'A', accuracy 0.34) illustrates this distinction: 100% injection of MC items causes format overfitting that would not arise from natural pretraining contamination. Notably, this collapse is format-specific. ARC and GSM8K at the same dosage behave normally, suggesting that dense MC-format injection uniquely triggers position bias collapse in certain architectures. We report this as a boundary condition of our injection protocol rather than a finding about contamination in general.\n\n### 6.5 Limitations\n\nSeveral scope constraints bound the present findings. First, our primary analysis uses a single model family (Qwen2.5 at 0.5B, 1.5B, 3B). Cross-family analysis with Llama-3.2-3B is exploratory ($N=4$, single seed), sufficient to demonstrate family-specificity of $\\gamma$ but not to establish generalizable contamination patterns. Second, the ensemble sizes achievable in practice ($N = 16$--$24$) fall below the $N \\geq 50$ threshold where simulation shows reliable $\\gamma$ recovery. Our empirical $\\gamma$ estimates carry wider credible intervals than nominal coverage suggests (empirical coverage 20--69% at the 95% level), and should be interpreted as directional indicators rather than precise effect sizes. Third, the identifiability constraints we characterize are specific to the IRT framework combined with membership-inference signals; they do not constitute a general impossibility result for contamination quantification. Alternative frameworks operating on different assumptions (e.g., data attribution methods with training corpus access) may circumvent these bounds entirely.\n\n### 6.6 Future Directions\n\nThree extensions address the primary limitations. First, scaling to additional model families at 7B+ parameters would test whether domain-differential patterns replicate beyond Qwen2.5 and whether larger capacity further attenuates contamination effects. Second, observational studies on models with known pretraining composition (where ground-truth exposure is available without injection) would validate whether IRT-diagnosed $\\gamma$ patterns correspond to actual contamination in naturalistic settings. Third, replacing membership-inference signals with data attribution methods (e.g., influence functions or training data tracing) could provide exposure scores with known ground-truth calibration, potentially resolving the signal failure problem that limits Stage 1 reliability. Extending to multidimensional IRT for non-STEM domains remains a theoretical priority but requires substantially larger model ensembles than currently available.\n",
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_014GMiWwaEXE6XjPan3V1nLr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "4ff1616b-b2a9-4755-af41-98ccc8f9bc57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpGiZeP3kpckpBgG1pqZ8d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16587,
      "cache_read_input_tokens": 26686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16587
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

_source line 23 · 2026-05-19T22:06:12.640Z_

<details><summary>↩ Tool result · `toolu_014GMiWwaEXE6XjPan3V1nLr`</summary>

```text
1	## 4 Experimental Setup
2	
3	### 4.1 Controlled SFT Injection
4	
5	We construct a controlled contamination testbed using the Qwen2.5 model family at three scales: 0.5B, 1.5B, and 3B parameters. For each scale, we fine-tune with LoRA ($\alpha = 32$) on a general-purpose SFT corpus into which we inject benchmark items at four dosage levels: d000 (0%, clean control), d005 (5%), d025 (25%), and d100 (100%). Benchmark items are formatted as instruction-response pairs and mixed into the training corpus at the specified proportions. All injected items pass a quality-control filter that removes ambiguous or malformed entries.
6	
7	We train each configuration with two random seeds (s42 and s123), yielding $J = 24$ models across 3 scales $\times$ 4 dosages $\times$ 2 seeds. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.
8	
9	Qwen2.5-0.5B exhibits severe position bias under logprob-based multiple-choice evaluation (d000 A-rate = 46%, d100 A-rate = 98%). We exclude 0.5B MMLU and ARC data from all IRT analyses. The 0.5B GSM8K results (free-form generation, unaffected by position bias) remain included. This exclusion is discussed further in Section 6.
10	
11	### 4.2 Cross-Family Analysis
12	
13	To test whether contamination patterns are family-specific, we fine-tune Llama-3.2-3B under the same protocol (d000, d005, d025, d100) with a single seed, yielding $J = 4$ additional models. This analysis is **exploratory**: the single-seed design provides limited statistical power. We report post-hoc power calculations using Qwen $J = 24$ effect sizes as reference (e.g., MMLU Math $\gamma = 0.97$).
14	
15	Llama-3.2-3B at d100 on MMLU exhibits catastrophic format collapse: all outputs default to option "A" (accuracy = 0.34). This configuration is excluded from IRT fitting. ARC and GSM8K at d100 behave normally. The effective Llama MMLU dosage range is d000 to d025.
16	
17	### 4.3 Benchmarks, Domains, and Evaluation
18	
19	We evaluate on three benchmarks that span distinct cognitive demands and response formats.
20	
21	**MMLU** (Hendrycks et al., 2021): 14,042 multiple-choice items across 57 subjects. We group these subjects into 8 cognitive domains by functional similarity: Math, Science, CS & Engineering, Medical, Humanities, Social Sciences, Business & Law, and Other. This domain stratification is central to our analysis, as it reveals within-benchmark heterogeneity that aggregate scoring obscures (Section 5.1).
22	
23	**ARC-Challenge** (Clark et al., 2018): 1,172 multiple-choice science reasoning items.
24	
25	**GSM8K** (Cobbe et al., 2021): 1,319 open-ended mathematical problem-solving items. The free-form generation format avoids multiple-choice artifacts and provides a format contrast to MMLU and ARC.
26	
27	We assess performance with six metrics. For *calibration quality*: mean absolute error (MAE) between calibrated and ground-truth clean accuracy, and Kendall $\tau$ for rank preservation across models. For *uncertainty quality*: 95% credible interval coverage. For *model diagnostics*: posterior predictive $p$-value (PPP $\in [0.1, 0.9]$ indicates acceptable fit), $\gamma$ significance (whether the 95% CI excludes zero), and $\hat{R}$ convergence ($< 1.01$).
28	
29	### 4.4 Baselines
30	
31	We compare against seven baselines. **B0-Raw** reports original benchmark accuracy with no adjustment. **B1-Remove&Rescore** drops items flagged as contaminated and rescores on the remainder. **B2-Single2PL+$\gamma$** fits a single aggregate $\gamma$ without domain stratification, testing whether per-domain modeling is necessary. **B3-Vanilla4PL** fits standard 4PL IRT with no contamination parameter ($\gamma = 0$), isolating the calibration contribution of IRT ability estimation from the contamination covariate. **B4-LinearRegression** regresses score residuals on exposure scores, testing whether the full IRT machinery is necessary. **B5-Emperor** applies representative mitigation strategies (item rephrasing and option shuffling) from the Emperor's New Clothes study (ICML 2025), which demonstrated that all 20 tested mitigation methods fail to restore clean performance. **B6-DCR** uses the Data Contamination Report adjusted accuracy (Oren et al., 2024), the only prior method that produces decontaminated score estimates.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "bb2fb757-4458-4239-91d0-f3d76e677a02",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md",
      "content": "## 4 Experimental Setup\n\n### 4.1 Controlled SFT Injection\n\nWe construct a controlled contamination testbed using the Qwen2.5 model family at three scales: 0.5B, 1.5B, and 3B parameters. For each scale, we fine-tune with LoRA ($\\alpha = 32$) on a general-purpose SFT corpus into which we inject benchmark items at four dosage levels: d000 (0%, clean control), d005 (5%), d025 (25%), and d100 (100%). Benchmark items are formatted as instruction-response pairs and mixed into the training corpus at the specified proportions. All injected items pass a quality-control filter that removes ambiguous or malformed entries.\n\nWe train each configuration with two random seeds (s42 and s123), yielding $J = 24$ models across 3 scales $\\times$ 4 dosages $\\times$ 2 seeds. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.\n\nQwen2.5-0.5B exhibits severe position bias under logprob-based multiple-choice evaluation (d000 A-rate = 46%, d100 A-rate = 98%). We exclude 0.5B MMLU and ARC data from all IRT analyses. The 0.5B GSM8K results (free-form generation, unaffected by position bias) remain included. This exclusion is discussed further in Section 6.\n\n### 4.2 Cross-Family Analysis\n\nTo test whether contamination patterns are family-specific, we fine-tune Llama-3.2-3B under the same protocol (d000, d005, d025, d100) with a single seed, yielding $J = 4$ additional models. This analysis is **exploratory**: the single-seed design provides limited statistical power. We report post-hoc power calculations using Qwen $J = 24$ effect sizes as reference (e.g., MMLU Math $\\gamma = 0.97$).\n\nLlama-3.2-3B at d100 on MMLU exhibits catastrophic format collapse: all outputs default to option \"A\" (accuracy = 0.34). This configuration is excluded from IRT fitting. ARC and GSM8K at d100 behave normally. The effective Llama MMLU dosage range is d000 to d025.\n\n### 4.3 Benchmarks, Domains, and Evaluation\n\nWe evaluate on three benchmarks that span distinct cognitive demands and response formats.\n\n**MMLU** (Hendrycks et al., 2021): 14,042 multiple-choice items across 57 subjects. We group these subjects into 8 cognitive domains by functional similarity: Math, Science, CS & Engineering, Medical, Humanities, Social Sciences, Business & Law, and Other. This domain stratification is central to our analysis, as it reveals within-benchmark heterogeneity that aggregate scoring obscures (Section 5.1).\n\n**ARC-Challenge** (Clark et al., 2018): 1,172 multiple-choice science reasoning items.\n\n**GSM8K** (Cobbe et al., 2021): 1,319 open-ended mathematical problem-solving items. The free-form generation format avoids multiple-choice artifacts and provides a format contrast to MMLU and ARC.\n\nWe assess performance with six metrics. For *calibration quality*: mean absolute error (MAE) between calibrated and ground-truth clean accuracy, and Kendall $\\tau$ for rank preservation across models. For *uncertainty quality*: 95% credible interval coverage. For *model diagnostics*: posterior predictive $p$-value (PPP $\\in [0.1, 0.9]$ indicates acceptable fit), $\\gamma$ significance (whether the 95% CI excludes zero), and $\\hat{R}$ convergence ($< 1.01$).\n\n### 4.4 Baselines\n\nWe compare against seven baselines. **B0-Raw** reports original benchmark accuracy with no adjustment. **B1-Remove&Rescore** drops items flagged as contaminated and rescores on the remainder. **B2-Single2PL+$\\gamma$** fits a single aggregate $\\gamma$ without domain stratification, testing whether per-domain modeling is necessary. **B3-Vanilla4PL** fits standard 4PL IRT with no contamination parameter ($\\gamma = 0$), isolating the calibration contribution of IRT ability estimation from the contamination covariate. **B4-LinearRegression** regresses score residuals on exposure scores, testing whether the full IRT machinery is necessary. **B5-Emperor** applies representative mitigation strategies (item rephrasing and option shuffling) from the Emperor's New Clothes study (ICML 2025), which demonstrated that all 20 tested mitigation methods fail to restore clean performance. **B6-DCR** uses the Data Contamination Report adjusted accuracy (Oren et al., 2024), the only prior method that produces decontaminated score estimates.\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Glob · `toolu_014EzEe4QBWCdnJPHp8b7Ke1`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "44cbb993-0d9d-470a-9b4b-772db5985b53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpGiZeP3kpckpBgG1pqZ8d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16587,
      "cache_read_input_tokens": 26686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16587
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

_source line 25 · 2026-05-19T22:06:13.649Z_

<details><summary>↩ Tool result · `toolu_014EzEe4QBWCdnJPHp8b7Ke1`</summary>

```text
paper/sections/method.md
paper/sections/discussion.md
paper/sections/experimental_setup.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "0ce4fa77-deea-47fe-b314-9a8314957925",
  "tool_use_result": {
    "filenames": [
      "paper/sections/method.md",
      "paper/sections/discussion.md",
      "paper/sections/experimental_setup.md"
    ],
    "durationMs": 7,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Glob · `toolu_01DT9CnV9xSumTV3PUQx5TBr`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "544d18d9-c507-4805-a13b-03158acef41f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpGiZeP3kpckpBgG1pqZ8d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16587,
      "cache_read_input_tokens": 26686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16587
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

_source line 27 · 2026-05-19T22:06:13.709Z_

<details><summary>↩ Tool result · `toolu_01DT9CnV9xSumTV3PUQx5TBr`</summary>

```text
artifacts/dream_reports/dream_20260513T155040/best/paper.tex
artifacts/dream_reports/dream_20260513T155040/median/paper.tex
artifacts/dream_reports/dream_20260513T155040/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/dream_reports/dream_20260513T171200/best/paper.tex
artifacts/dream_reports/dream_20260513T171200/median/paper.tex
artifacts/dream_reports/dream_20260513T171200/worst/paper.tex
artifacts/_project/paper/fisher_info_appendix.tex
artifacts/fisher_info_derivation/fisher_info_appendix.tex
artifacts/dream_reports/dream_20260514T171536/best/paper.tex
artifacts/dream_reports/dream_20260514T171536/median/paper.tex
artifacts/dream_reports/dream_20260514T171536/worst/paper.tex
artifacts/dream_reports/dream_20260514T185145/best/paper.tex
artifacts/dream_reports/dream_20260514T185145/median/paper.tex
artifacts/dream_reports/dream_20260514T185145/worst/paper.tex
artifacts/dream_reports/dream_20260515T052337/best/paper.tex
artifacts/dream_reports/dream_20260515T052337/median/paper.tex
artifacts/dream_reports/dream_20260515T052337/worst/paper.tex
artifacts/dream_reports/dream_20260516T104822/best/paper.tex
artifacts/dream_reports/dream_20260516T104822/median/paper.tex
artifacts/dream_reports/dream_20260516T104822/worst/paper.tex
artifacts/dream_reports/dream_20260516T155748/best/paper.tex
artifacts/dream_reports/dream_20260516T155748/median/paper.tex
artifacts/dream_reports/dream_20260516T155748/worst/paper.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/related_work_04a735.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/abstract.tex
artifacts/paper_draft/experiments.tex
artifacts/_project/paper/introduction.tex
artifacts/paper_draft/abstract.tex
artifacts/paper_draft/conclusion.tex
artifacts/paper_draft/discussion.tex
artifacts/paper_draft/introduction.tex
artifacts/paper_draft/main.tex
artifacts/paper_draft/method.tex
artifacts/paper_draft/related_work.tex
artifacts/paper_draft/results.tex
artifacts/paper_draft/experimental_setup.tex
docs/paper/ethics.tex
docs/paper/related_work.tex
docs/paper/experimental_setup.tex
docs/paper/abstract.tex
artifacts/_project/paper/algorithm1_pseudocode.tex
artifacts/_project/paper/algorithm1_pseudocode_c1bd81.tex
docs/paper/introduction.tex
artifacts/algorithm1_pseudocode.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/limitations.tex
docs/paper/appendix.tex
docs/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "2232792d-8e80-4cd1-9908-dd6e071b2f11",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260513T155040/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T155040/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T155040/worst/paper.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/dream_reports/dream_20260513T171200/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T171200/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T171200/worst/paper.tex",
      "artifacts/_project/paper/fisher_info_appendix.tex",
      "artifacts/fisher_info_derivation/fisher_info_appendix.tex",
      "artifacts/dream_reports/dream_20260514T171536/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T171536/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T171536/worst/paper.tex",
      "artifacts/dream_reports/dream_20260514T185145/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T185145/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T185145/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T052337/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T052337/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T052337/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T104822/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T104822/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T104822/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T155748/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T155748/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T155748/worst/paper.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/related_work_04a735.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/paper_draft/experiments.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/paper_draft/abstract.tex",
      "artifacts/paper_draft/conclusion.tex",
      "artifacts/paper_draft/discussion.tex",
      "artifacts/paper_draft/introduction.tex",
      "artifacts/paper_draft/main.tex",
      "artifacts/paper_draft/method.tex",
      "artifacts/paper_draft/related_work.tex",
      "artifacts/paper_draft/results.tex",
      "artifacts/paper_draft/experimental_setup.tex",
      "docs/paper/ethics.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/abstract.tex",
      "artifacts/_project/paper/algorithm1_pseudocode.tex",
      "artifacts/_project/paper/algorithm1_pseudocode_c1bd81.tex",
      "docs/paper/introduction.tex",
      "artifacts/algorithm1_pseudocode.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/main.tex",
      "docs/paper/method.tex",
      "docs/paper/limitations.tex",
      "docs/paper/appendix.tex",
      "docs/paper/results.tex"
    ],
    "durationMs": 54,
    "numFiles": 53,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me read the latest paper draft to understand the current state of each section. The most recent paper files seem to be in `docs/paper/` and `artifacts/paper_draft/`. Let me check which is the latest version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "d46f0930-c5ce-42c7-aa3e-f926e087f5e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013znkZXNoBdWhGX9kBBWkCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 43273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 29_

Let me check the actual compiled paper to understand the current 7-page state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "19937280-6565-4b53-ab40-f45a4a4acc1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013znkZXNoBdWhGX9kBBWkCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 43273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01K42ozZoCLdxDpJuAgUShs9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
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
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "845743c8-4668-4fe8-88b1-f233ebef8923",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013znkZXNoBdWhGX9kBBWkCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 43273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 31 · 2026-05-19T22:06:19.902Z_

<details><summary>↩ Tool result · `toolu_01K42ozZoCLdxDpJuAgUShs9`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{algorithm}
13	\usepackage{algpseudocode}
14	\usepackage{float}
15	
16	\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{abstract}
25	\end{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{experimental_setup}
31	\input{results}
32	\input{conclusion}
33	
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "15acef49-9536-4564-be6d-efb52f8f0665",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review,hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{algorithm}\n\\usepackage{algpseudocode}\n\\usepackage{float}\n\n\\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experimental_setup}\n\\input{results}\n\\input{conclusion}\n\n\\input{limitations}\n\\input{ethics}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 42
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_016ze4xjsyza5RFWtNCQvo7v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "fc180c94-ccc1-42f0-ad0e-4e917efede06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013znkZXNoBdWhGX9kBBWkCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 43273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 33 · 2026-05-19T22:06:20.452Z_

<details><summary>↩ Tool result · `toolu_016ze4xjsyza5RFWtNCQvo7v`</summary>

```text
1	Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but five distinct dose-response patterns: Immune ($\pm$0.5pp), U-type collapse ($-$10pp), V-type recovery ($-$3pp then partial rebound), Benefit ($+$3.8pp monotonic), and Benefit-saturation ($+$3.2pp then plateau). A baseline ability threshold at 64.7\% MMLU (bootstrap 95\% CI: 64.0--65.4\%) separates models that benefit from contamination from those that are harmed or immune. Counter-intuitively, the 14B Qwen model is 3$\times$ more fragile than 7B. Profiles are robust on MMLU (4/5 families $\geq$99.6\% bootstrap stability); ARC-Challenge shows directional agreement for 3/5 families but lower stability due to its smaller item pool (1{,}172 vs.\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "d1829329-6321-424d-9ba9-3ec311bd361e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex",
      "content": "Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but five distinct dose-response patterns: Immune ($\\pm$0.5pp), U-type collapse ($-$10pp), V-type recovery ($-$3pp then partial rebound), Benefit ($+$3.8pp monotonic), and Benefit-saturation ($+$3.2pp then plateau). A baseline ability threshold at 64.7\\% MMLU (bootstrap 95\\% CI: 64.0--65.4\\%) separates models that benefit from contamination from those that are harmed or immune. Counter-intuitively, the 14B Qwen model is 3$\\times$ more fragile than 7B. Profiles are robust on MMLU (4/5 families $\\geq$99.6\\% bootstrap stability); ARC-Challenge shows directional agreement for 3/5 families but lower stability due to its smaller item pool (1{,}172 vs.\\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \\geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_013zPwqN633M5BZAJYZGCvuE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "0e268f13-7fb5-4095-bbcb-f4eeb0ad9b51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013znkZXNoBdWhGX9kBBWkCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 43273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 35 · 2026-05-19T22:06:20.991Z_

<details><summary>↩ Tool result · `toolu_013zPwqN633M5BZAJYZGCvuE`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover five distinct dose-response patterns---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic U-type collapse (Qwen-14B, $-$10pp). A baseline ability threshold at 64.7\% MMLU (bootstrap 95\% CI: 64.0--65.4\%) separates models that benefit from contamination (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp) from those harmed or immune. Counter-intuitively, the 14B model is 3$\times$ more fragile than 7B. Using ContamCal, a two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\gamma_k$), we provide the statistical machinery for this characterization.
6	
7	Our contributions:
8	\begin{enumerate}
9	    \item \textbf{Five-pattern contamination taxonomy.} Controlled injection across four families reveals five dose-response patterns governed by a 64.7\% baseline threshold (95\% CI: 64.0--65.4\%), directionally consistent across MMLU and ARC-Challenge. Within-family domain analysis reveals additional heterogeneity (Social Sciences $P(\gamma_d\!<\!0) = 99.7\%$).
10	    \item \textbf{Global modulation, not memorization.} Difference-in-differences analysis on 14{,}042 MMLU items shows no differential accuracy gain for contaminated vs.\ clean items in any model family, providing causal evidence that SFT contamination operates through global capability modulation rather than item-specific memorization.
11	    \item \textbf{Signal failure characterization.} Min-K\%++ \citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (Cohen's $d = -1.55$ to $-1.98$). RRF-guided item filtering is a prerequisite for IRT convergence ($\Delta\tau = 0.18$ vs.\ size-matched random). Simulation establishes $\gamma$ recovery requires $J \geq 50$ at AUC $\geq 0.55$, above current practice ($J = 8$--$30$).
12	\end{enumerate}
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "bba8dccf-75b3-449a-af99-09c356f78d43",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nBenchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \\citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \\citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \\citep{sun2025emperor}, contamination-free benchmarks \\citep{white2024livebench}, and dynamic regeneration \\citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.\n\nWe perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover five distinct dose-response patterns---from immunity (Phi-4 14.7B, $\\pm$0.5pp on MMLU) to catastrophic U-type collapse (Qwen-14B, $-$10pp). A baseline ability threshold at 64.7\\% MMLU (bootstrap 95\\% CI: 64.0--65.4\\%) separates models that benefit from contamination (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp) from those harmed or immune. Counter-intuitively, the 14B model is 3$\\times$ more fragile than 7B. Using ContamCal, a two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\\gamma_k$), we provide the statistical machinery for this characterization.\n\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Five-pattern contamination taxonomy.} Controlled injection across four families reveals five dose-response patterns governed by a 64.7\\% baseline threshold (95\\% CI: 64.0--65.4\\%), directionally consistent across MMLU and ARC-Challenge. Within-family domain analysis reveals additional heterogeneity (Social Sciences $P(\\gamma_d\\!<\\!0) = 99.7\\%$).\n    \\item \\textbf{Global modulation, not memorization.} Difference-in-differences analysis on 14{,}042 MMLU items shows no differential accuracy gain for contaminated vs.\\ clean items in any model family, providing causal evidence that SFT contamination operates through global capability modulation rather than item-specific memorization.\n    \\item \\textbf{Signal failure characterization.} Min-K\\%++ \\citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (Cohen's $d = -1.55$ to $-1.98$). RRF-guided item filtering is a prerequisite for IRT convergence ($\\Delta\\tau = 0.18$ vs.\\ size-matched random). Simulation establishes $\\gamma$ recovery requires $J \\geq 50$ at AUC $\\geq 0.55$, above current practice ($J = 8$--$30$).\n\\end{enumerate}\n",
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

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01GzE95fD79gvmoi8dx6EfgS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "2afee265-e975-4106-9f17-67e693d2aa2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013znkZXNoBdWhGX9kBBWkCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 43273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 37 · 2026-05-19T22:06:21.363Z_

<details><summary>↩ Tool result · `toolu_01GzE95fD79gvmoi8dx6EfgS`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Five Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{table}[t]
10	\centering
11	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
12	\label{tab:taxonomy}
13	\footnotesize
14	\begin{tabular}{llccccc}
15	\toprule
16	Pattern & Model & Baseline & $\Delta$acc & 95\% CI & Peak & Stab. \\
17	\midrule
18	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% \\
19	U-collapse & Qwen-14B & 69.4\% & $-$9.4pp & [$-$10.04, $-$8.70] & $-$10.0\textsuperscript{d050} & 100\% \\
20	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
21	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\% \\
22	Benefit-sat. & OLMo-2 7B & 53.8\% & $+$3.2pp & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\tau,\sigma)$ threshold combinations (Appendix~\ref{sec:classification_sensitivity}).
28	
29	\paragraph{Baseline ability threshold.}
30	A threshold at 64.7\% MMLU baseline (bootstrap 95\% CI: 64.0--65.4\%, $B=10{,}000$) separates two regimes. Below it, OLMo-2 (53.8\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\%) gains $+$3.8pp monotonically. Above it, Qwen-7B (66.1\%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), Qwen-14B (69.4\%) collapses by $-$10.0pp at d050---3$\times$ more fragile than 7B despite higher baseline---and Phi-4 (76.4\%) is immune. ARC-Challenge results are directionally consistent for 4/5 models (Appendix~\ref{sec:arc_cross_benchmark}). Cross-family domain decomposition reveals consistent directionality within each pattern, with STEM as the most resilient domain across all five families (Appendix~\ref{sec:domain_decomposition}).
31	
32	\begin{figure}[t]
33	\centering
34	\includegraphics[width=\columnwidth]{figures/fig_dose_response.pdf}
35	\caption{MMLU accuracy vs.\ contamination dosage (5-shot). Models below 64.7\% baseline benefit; models above are harmed or immune. Qwen-14B is 3$\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref{sec:arc_cross_benchmark}.}
36	\label{fig:dose_response}
37	\end{figure}
38	
39	\subsection{Item-Level Memorization Test}
40	\label{sec:memorization_test}
41	
42	We test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. The pattern holds on ARC-Challenge. Difficulty-stratified analysis confirms symmetry ($|\text{gap}| < 0.4$pp across all bins).
43	
44	\begin{table}[t]
45	\centering
46	\caption{Treated vs.\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}
47	\label{tab:did}
48	\footnotesize
49	\begin{tabular}{lcccc}
50	\toprule
51	Model & Treated $\Delta$ & Untreated $\Delta$ & DiD & Verdict \\
52	\midrule
53	Gemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.6 (ns) & generalization \\
54	OLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\
55	Phi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\
56	Qwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\
57	Qwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	Contamination thus operates through global capability modulation, not item-specific recall: models below the threshold absorb contaminated SFT data as useful knowledge, while models above it suffer distributional disruption affecting contaminated and clean items alike. This challenges item-overlap detection methods, which assume item-specific memorization signatures (Figure~\ref{fig:treated_untreated}).
63	
64	\begin{figure}[t]
65	\centering
66	\includegraphics[width=\columnwidth]{figures/fig_treated_untreated.pdf}
67	\caption{DiD for treated vs.\ untreated items across five families at d025 MMLU. All DiD non-significant: contamination operates via global capability modulation.}
68	\label{fig:treated_untreated}
69	\end{figure}
70	
71	\subsection{Calibration Quality}
72	\label{sec:calibration_results}
73	
74	Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\tau = 0.73$ on 300 items ($\Delta\tau = 0.27$ vs.\ random baseline); S1-only selection causes convergence failure ($\hat{R} = 1.53$) due to exposure variance compression.
75	
76	Table~\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy achieves the lowest MAE (0.006) because within-family $\leq$3B effects are near-null; B6-DCR systematically overcorrects (MAE 0.108). ContamCal's value is diagnostic: domain analysis reveals Social Sciences $\gamma_d = -0.63$ ($P(\gamma_d\!<\!0) = 99.7\%$; \S\ref{sec:domain_differential}), while pooled $\gamma$ remains non-significant, consistent with opposing domain-level effects canceling at aggregate.
77	
78	\begin{table}[t]
79	\centering
80	\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\ref{sec:arc_irt}.}
81	\label{tab:baselines}
82	\footnotesize
83	\begin{tabular}{lcc}
84	\toprule
85	Method & MAE & $\tau$ \\
86	\midrule
87	B0: Raw Accuracy & \textbf{0.006} & 0.767 \\
88	B1b: Remove \& Rescore & 0.026 & \underline{0.783} \\
89	B3: Vanilla 2PL & 0.008 & 0.731 \\
90	B4: Linear Regression & 0.010 & 0.751 \\
91	B5b: Emperor & \textbf{0.006} & \textbf{0.789} \\
92	B6: DCR (reimpl.) & 0.108 & 0.654 \\
93	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	\subsection{Detection Signal Failure Modes}
99	\label{sec:signal_failure}
100	
101	Min-K\%++ \citep{zhang_2024_minkpp} exhibits a \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores than clean items (Cohen's $d = -1.55$ at d005, $-1.98$ at d100). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
102	
103	\subsection{Domain-Level Analysis}
104	\label{sec:domain_differential}
105	
106	Within-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% CI $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722), crossing the Bonferroni-corrected threshold for eight tests (Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Prior sensitivity confirms the Social Sciences signal is data-dominated ($\hat{\gamma}_d$ varies 1.2$\times$ across priors vs.\ 2.6$\times$ for pooled; Appendix~\ref{sec:prior_sensitivity}).
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "f167a9d8-653c-4175-af68-454d64cd62a0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nCross-family results (\\S\\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\\S\\ref{sec:calibration_results}--\\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\\times$1.5B + 8$\\times$3B); domain-level contamination estimates $\\gamma_d$ (\\S\\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\\ref{fig:domain_gamma}.\n\n\\subsection{Five Dose-Response Patterns}\n\\label{sec:taxonomy}\n\n\\begin{table}[t]\n\\centering\n\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}\n\\label{tab:taxonomy}\n\\footnotesize\n\\begin{tabular}{llccccc}\n\\toprule\nPattern & Model & Baseline & $\\Delta$acc & 95\\% CI & Peak & Stab. \\\\\n\\midrule\nImmune & Phi-4 14.7B & 76.4\\% & $\\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\\% \\\\\nU-collapse & Qwen-14B & 69.4\\% & $-$9.4pp & [$-$10.04, $-$8.70] & $-$10.0\\textsuperscript{d050} & 100\\% \\\\\nV-recovery & Qwen-7B & 66.1\\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\\textsuperscript{d025} & 99.6\\% \\\\\nBenefit & Gemma-2 9B & 61.9\\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\\% \\\\\nBenefit-sat. & OLMo-2 7B & 53.8\\% & $+$3.2pp & [$+$2.73, $+$3.71] & sat.\\textsuperscript{d050} & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nApplying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (Appendix~\\ref{sec:classification_sensitivity}).\n\n\\paragraph{Baseline ability threshold.}\nA threshold at 64.7\\% MMLU baseline (bootstrap 95\\% CI: 64.0--65.4\\%, $B=10{,}000$) separates two regimes. Below it, OLMo-2 (53.8\\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\\%) gains $+$3.8pp monotonically. Above it, Qwen-7B (66.1\\%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), Qwen-14B (69.4\\%) collapses by $-$10.0pp at d050---3$\\times$ more fragile than 7B despite higher baseline---and Phi-4 (76.4\\%) is immune. ARC-Challenge results are directionally consistent for 4/5 models (Appendix~\\ref{sec:arc_cross_benchmark}). Cross-family domain decomposition reveals consistent directionality within each pattern, with STEM as the most resilient domain across all five families (Appendix~\\ref{sec:domain_decomposition}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{MMLU accuracy vs.\\ contamination dosage (5-shot). Models below 64.7\\% baseline benefit; models above are harmed or immune. Qwen-14B is 3$\\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\\ref{sec:arc_cross_benchmark}.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Item-Level Memorization Test}\n\\label{sec:memorization_test}\n\nWe test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. The pattern holds on ARC-Challenge. Difficulty-stratified analysis confirms symmetry ($|\\text{gap}| < 0.4$pp across all bins).\n\n\\begin{table}[t]\n\\centering\n\\caption{Treated vs.\\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}\n\\label{tab:did}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Treated $\\Delta$ & Untreated $\\Delta$ & DiD & Verdict \\\\\n\\midrule\nGemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.6 (ns) & generalization \\\\\nOLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\\\\nPhi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\\\\nQwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\\\\nQwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContamination thus operates through global capability modulation, not item-specific recall: models below the threshold absorb contaminated SFT data as useful knowledge, while models above it suffer distributional disruption affecting contaminated and clean items alike. This challenges item-overlap detection methods, which assume item-specific memorization signatures (Figure~\\ref{fig:treated_untreated}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_treated_untreated.pdf}\n\\caption{DiD for treated vs.\\ untreated items across five families at d025 MMLU. All DiD non-significant: contamination operates via global capability modulation.}\n\\label{fig:treated_untreated}\n\\end{figure}\n\n\\subsection{Calibration Quality}\n\\label{sec:calibration_results}\n\nWithin-family IRT analysis uses Qwen2.5 $\\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\\tau = 0.73$ on 300 items ($\\Delta\\tau = 0.27$ vs.\\ random baseline); S1-only selection causes convergence failure ($\\hat{R} = 1.53$) due to exposure variance compression.\n\nTable~\\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy achieves the lowest MAE (0.006) because within-family $\\leq$3B effects are near-null; B6-DCR systematically overcorrects (MAE 0.108). ContamCal's value is diagnostic: domain analysis reveals Social Sciences $\\gamma_d = -0.63$ ($P(\\gamma_d\\!<\\!0) = 99.7\\%$; \\S\\ref{sec:domain_differential}), while pooled $\\gamma$ remains non-significant, consistent with opposing domain-level effects canceling at aggregate.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\\ref{sec:arc_irt}.}\n\\label{tab:baselines}\n\\footnotesize\n\\begin{tabular}{lcc}\n\\toprule\nMethod & MAE & $\\tau$ \\\\\n\\midrule\nB0: Raw Accuracy & \\textbf{0.006} & 0.767 \\\\\nB1b: Remove \\& Rescore & 0.026 & \\underline{0.783} \\\\\nB3: Vanilla 2PL & 0.008 & 0.731 \\\\\nB4: Linear Regression & 0.010 & 0.751 \\\\\nB5b: Emperor & \\textbf{0.006} & \\textbf{0.789} \\\\\nB6: DCR (reimpl.) & 0.108 & 0.654 \\\\\nContamCal (2PL+$\\gamma$) & 0.009 & 0.731 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detection Signal Failure Modes}\n\\label{sec:signal_failure}\n\nMin-K\\%++ \\citep{zhang_2024_minkpp} exhibits a \\textit{directional reversal} at 0.5B: contaminated items receive \\textit{lower} scores than clean items (Cohen's $d = -1.55$ at d005, $-1.98$ at d100). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\\ref{sec:signal_reliability_appendix}). Simulation shows $\\gamma$ recovery requires AUC$\\geq$0.55 with $J \\geq 50$; at AUC $\\geq 0.90$, $J = 16$ suffices (Appendix~\\ref{sec:identifiability_appendix}).\n\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain_differential}\n\nWithin-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\\gamma_d$ while Social Sciences is negative ($\\gamma_d = -0.63$, 95\\% CI $[-1.07, -0.19]$, $P(\\gamma_d\\!<\\!0) = 99.7\\%$, PPP$=$0.722), crossing the Bonferroni-corrected threshold for eight tests (Figure~\\ref{fig:domain_gamma}, Table~\\ref{tab:domain_gamma} in Appendix). Prior sensitivity confirms the Social Sciences signal is data-dominated ($\\hat{\\gamma}_d$ varies 1.2$\\times$ across priors vs.\\ 2.6$\\times$ for pooled; Appendix~\\ref{sec:prior_sensitivity}).\n",
      "numLines": 107,
      "startLine": 1,
      "totalLines": 107
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Let me also read the remaining sections to have a complete picture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "ee99f47a-166b-402f-94e2-64d72adfb71f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tgmU5F7WQLrXNB6BmAPUC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5399,
      "cache_read_input_tokens": 49124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5399
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

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01UvdmhEQ6QibE3ARfXwLMZt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "fca17050-83f6-49d9-ac6e-72c12ea125b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tgmU5F7WQLrXNB6BmAPUC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5399,
      "cache_read_input_tokens": 49124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5399
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

_source line 40 · 2026-05-19T22:06:25.902Z_

<details><summary>↩ Tool result · `toolu_01UvdmhEQ6QibE3ARfXwLMZt`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Contamination detection and mitigation.}
4	Detection methods flag contaminated items via token-level surprisal \citep{shi_2023_minkprob,zhang_2024_minkpp}, accuracy gaps on paraphrases \citep{dekoninck2024constat}, kernel divergence \citep{choi_2025_kds}, completion probes \citep{dong_2024_cdd}, and parallel test sets \citep{zhang_2024_gsm1k}; see \citet{chen2025benchmarking,singh2024evaluation} for surveys. Concurrent work by \citet{tao2025detecting} targets RL-trained models via entropy collapse. These methods perform binary classification without quantifying effect sizes. On mitigation, \citet{sun2025emperor} find none of twenty approaches reliably restores clean performance; DCR \citep{xu2025dcr} estimates decontaminated scores but without uncertainty quantification. ContamCal consumes detection signals as inputs and produces calibrated ability with credible intervals.
5	
6	\paragraph{IRT for LLM evaluation.}
7	Item Response Theory \citep{lord_1980_irt,hambleton_1991_irt} has gained traction for LLM evaluation: TinyBenchmarks \citep{polo_2024_tinybenchmarks} for efficient evaluation, Growing Pains \citep{habba_2025_growing_pains} for large-scale validation, HiBayES \citep{luettgau_2025_hibayes} for hierarchical Bayesian inference; see \citet{lalor_2024_irt_nlp} for a tutorial. Most directly related, \citet{han2026quantifying} apply psychometric DIF to quantify contamination on item parameters, using group-based binary indicators on naturally contaminated models. ContamCal differs by introducing continuous exposure covariates ($\gamma_k$) from multiple detection signals, operating on controlled-injection data with known ground truth, and providing domain-level decomposition. Our $\gamma$ parameter is formally an instance of explanatory DIF \citep{deboeck_2004_explanatory_irt,eckerly_2017_item_compromise}: the contamination covariate differentially affects response probability, analogous to item compromise models in educational measurement \citep{sinharay_2017_preknowledge}. We use ``calibration'' in the psychometric sense of adjusting scores to approximate uncontaminated performance, distinct from probability calibration \citep{guo_2017_calibration}.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "bfbef20c-3624-4da7-a784-8179a5e3387d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Contamination detection and mitigation.}\nDetection methods flag contaminated items via token-level surprisal \\citep{shi_2023_minkprob,zhang_2024_minkpp}, accuracy gaps on paraphrases \\citep{dekoninck2024constat}, kernel divergence \\citep{choi_2025_kds}, completion probes \\citep{dong_2024_cdd}, and parallel test sets \\citep{zhang_2024_gsm1k}; see \\citet{chen2025benchmarking,singh2024evaluation} for surveys. Concurrent work by \\citet{tao2025detecting} targets RL-trained models via entropy collapse. These methods perform binary classification without quantifying effect sizes. On mitigation, \\citet{sun2025emperor} find none of twenty approaches reliably restores clean performance; DCR \\citep{xu2025dcr} estimates decontaminated scores but without uncertainty quantification. ContamCal consumes detection signals as inputs and produces calibrated ability with credible intervals.\n\n\\paragraph{IRT for LLM evaluation.}\nItem Response Theory \\citep{lord_1980_irt,hambleton_1991_irt} has gained traction for LLM evaluation: TinyBenchmarks \\citep{polo_2024_tinybenchmarks} for efficient evaluation, Growing Pains \\citep{habba_2025_growing_pains} for large-scale validation, HiBayES \\citep{luettgau_2025_hibayes} for hierarchical Bayesian inference; see \\citet{lalor_2024_irt_nlp} for a tutorial. Most directly related, \\citet{han2026quantifying} apply psychometric DIF to quantify contamination on item parameters, using group-based binary indicators on naturally contaminated models. ContamCal differs by introducing continuous exposure covariates ($\\gamma_k$) from multiple detection signals, operating on controlled-injection data with known ground truth, and providing domain-level decomposition. Our $\\gamma$ parameter is formally an instance of explanatory DIF \\citep{deboeck_2004_explanatory_irt,eckerly_2017_item_compromise}: the contamination covariate differentially affects response probability, analogous to item compromise models in educational measurement \\citep{sinharay_2017_preknowledge}. We use ``calibration'' in the psychometric sense of adjusting scores to approximate uncontaminated performance, distinct from probability calibration \\citep{guo_2017_calibration}.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01Ssmbx8uo6HHgQQ2TTB4pc4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "2d2d88f9-6d49-4afc-8955-3256aa18615a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tgmU5F7WQLrXNB6BmAPUC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5399,
      "cache_read_input_tokens": 49124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5399
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

_source line 42 · 2026-05-19T22:06:26.473Z_

<details><summary>↩ Tool result · `toolu_01Ssmbx8uo6HHgQQ2TTB4pc4`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \citep{kadavath2022}; concurrent work by \citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\mathcal{S} = \{\text{S1, S2, S4}\}$) and is applicable to any benchmark without auxiliary data requirements. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_failure}.
17	
18	We aggregate signals via Reciprocal Rank Fusion \citep[RRF;][]{cormack_2009_rrf}:
19	\begin{equation}
20	\label{eq:rrf}
21	    e_{ij} = \sum_{s \in \mathcal{S}} \frac{1}{\kappa + r_{s}(i)},
22	\end{equation}
23	where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\kappa=60$ is the standard smoothing constant, and $|\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to obtain $e_{ij} \in [0,1]$. The resulting distribution is highly right-skewed (mean 0.041, median 0.016, max 0.879), with most model-item pairs receiving near-zero exposure.
24	
25	\subsection{Stage 2: Contamination-Augmented IRT}
26	\label{sec:stage2}
27	
28	\paragraph{Primary model: 2PL+$\gamma$.}
29	Our primary specification augments the two-parameter logistic (2PL) model \citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:
30	\begin{equation}
31	\label{eq:2pl_gamma}
32	    P(y_{ijk} = 1) = \sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
33	\end{equation}
34	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \in \mathbb{R}$ is item difficulty, $\theta_j$ is model ability, and $\gamma_k$ is the scalar contamination effect for benchmark~$k$. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we further stratify within a benchmark by cognitive domain (\S\ref{sec:domain_differential}).
35	
36	The additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\gamma_k \cdot e_{ij} / a_i$ units on the ability scale (this holds exactly under linearization of the logistic function; the true shift is nonlinear and probability-dependent).
37	
38	For MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\ref{sec:4pl_details}); this requires $J \geq 16$ and is not used in domain-level analyses ($J = 13$).
39	
40	\paragraph{Inference.}
41	We perform Bayesian inference via NUTS \citep{hoffman2014} in Stan \citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_k \sim \mathcal{N}(0,1)$. Convergence requires split-$\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.
42	
43	\paragraph{Calibrated score.}
44	The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:
45	\begin{equation}
46	\label{eq:calibrated}
47	    \text{Acc}_{j}^{\text{cal}} = \frac{1}{I_k} \sum_{i=1}^{I_k}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)\right],
48	\end{equation}
49	with credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.
50	
51	\paragraph{Identifiability.}
52	\label{sec:fisher}
53	\label{sec:value_decomposition}
54	The reliability of $\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\geq$0.55 with $J \geq 50$ (Appendix~\ref{sec:identifiability}). Eq.~\eqref{eq:calibrated} depends on $\theta_j$, not $\gamma$ directly, predicting that vanilla 2PL ($\gamma\!=\!0$) achieves comparable calibration to 2PL+$\gamma$, with $\gamma_k$ serving diagnosis rather than calibration (\S\ref{sec:calibration_results}).
55	
56	\subsection{Dose-Response Profile Classification}
57	\label{sec:classification}
58	
59	Independent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern. Algorithm~\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by a noise threshold $\tau$, severity threshold $\sigma$, saturation ratio $\rho$, and late-gain floor $\lambda$. The three-way top-level split (immune/harm/benefit) is governed by the sign and magnitude of $\Delta = a_{100} - a_0$ relative to $\tau$; within-branch refinements distinguish U-collapse from V-recovery (via mid-dosage trough detection) and monotonic benefit from benefit-saturation (via gain deceleration). A mid-trajectory volatility check ($v^*$) within the immune branch distinguishes true immunity (Phi-4: $v^* = 0.34$pp $\le \tau$) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $\Delta \approx 0$ but $v^* = 3.22$pp $> \tau$); recovery extent varies by seed (partial at seed$=$42, full at seed$=$123). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms 5/5 families are stable across all $(\tau, \sigma)$ combinations (Appendix~\ref{sec:classification_sensitivity}).
60	
61	\begin{algorithm}[H]
62	\caption{Dose-Response Profile Classification}
63	\label{alg:profile-classification}
64	\begin{algorithmic}[1]
65	\Require Accuracy vector $\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \in \{0, 5, 25, 50, 100\}\%$
66	\Require Noise threshold $\tau = 1$ pp, severity threshold $\sigma = 5$ pp
67	\Require Saturation ratio $\rho = 0.3$, late-gain floor $\lambda = 0.5$ pp
68	\Ensure Pattern $p \in \{\textsc{Immune}, \textsc{U-collapse}, \textsc{V-recovery}, \textsc{Benefit}, \textsc{Benefit-sat}\}$
69	\State $\Delta \gets a_{100} - a_{0}$ \Comment{end-to-end accuracy shift}
70	\State $m^* \gets \min(a_{5},\, a_{25},\, a_{50})$ \Comment{mid-dosage minimum}
71	\State $v^* \gets \max_{i \in \{5,25,50\}} |a_i - a_0|$ \Comment{max mid-trajectory deviation}
72	\If{$|\Delta| \le \tau$}
73	    \If{$v^* \le \tau$}
74	        \State \Return \textsc{Immune} \Comment{fluctuation within noise band}
75	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
76	        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
77	    \Else
78	        \State \Return \textsc{Immune} \Comment{non-V volatility, endpoint stable}
79	    \EndIf
80	\ElsIf{$\Delta < -\tau$}
81	    \If{$\Delta \le -\sigma$}
82	        \State \Return \textsc{U-collapse} \Comment{severe monotonic degradation}
83	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
84	        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
85	    \Else
86	        \State \Return \textsc{U-collapse} \Comment{moderate decline, no V-shape}
87	    \EndIf
88	\Else \Comment{$\Delta > \tau$}
89	    \State $g_1 \gets a_{25} - a_{0}$ \Comment{first-half gain}
90	    \State $g_2 \gets a_{100} - a_{25}$ \Comment{second-half gain}
91	    \State $\ell \gets a_{100} - a_{50}$ \Comment{late gain}
92	    \If{$(g_1 > 0$ \textbf{and} $g_2 < \rho \cdot g_1)$ \textbf{or} $\ell < \lambda$}
93	        \State \Return \textsc{Benefit-sat} \Comment{gain decelerates at high dosage}
94	    \Else
95	        \State \Return \textsc{Benefit} \Comment{sustained improvement}
96	    \EndIf
97	\EndIf
98	\end{algorithmic}
99	\end{algorithm}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "153bfae4-670d-44c2-8ede-397aa8dddade",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nLet $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model~$j$ ($j=1,\\ldots,J$) to item~$i$ ($i=1,\\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.\n\nOur goal is to estimate $\\theta_j^{\\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \\citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \\citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \\in [0,1]$, fitting per-benchmark models to handle the shared item pool \\citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).\n\n\\subsection{Stage 1: Multi-Signal Exposure Mapping}\n\\label{sec:stage1}\n\nFor each model~$j$ and item~$i$, we consider four candidate detection signals. \\textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \\textbf{S2}~(Min-K\\%++): a membership inference statistic based on token-level surprisal \\citep{zhang_2024_minkpp}. \\textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \\citep{dekoninck2024constat}. \\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \\citep{kadavath2022}; concurrent work by \\citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\\mathcal{S} = \\{\\text{S1, S2, S4}\\}$) and is applicable to any benchmark without auxiliary data requirements. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \\S\\ref{sec:signal_failure}.\n\nWe aggregate signals via Reciprocal Rank Fusion \\citep[RRF;][]{cormack_2009_rrf}:\n\\begin{equation}\n\\label{eq:rrf}\n    e_{ij} = \\sum_{s \\in \\mathcal{S}} \\frac{1}{\\kappa + r_{s}(i)},\n\\end{equation}\nwhere $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\\kappa=60$ is the standard smoothing constant, and $|\\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to obtain $e_{ij} \\in [0,1]$. The resulting distribution is highly right-skewed (mean 0.041, median 0.016, max 0.879), with most model-item pairs receiving near-zero exposure.\n\n\\subsection{Stage 2: Contamination-Augmented IRT}\n\\label{sec:stage2}\n\n\\paragraph{Primary model: 2PL+$\\gamma$.}\nOur primary specification augments the two-parameter logistic (2PL) model \\citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:\n\\begin{equation}\n\\label{eq:2pl_gamma}\n    P(y_{ijk} = 1) = \\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwhere $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \\in \\mathbb{R}$ is item difficulty, $\\theta_j$ is model ability, and $\\gamma_k$ is the scalar contamination effect for benchmark~$k$. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we further stratify within a benchmark by cognitive domain (\\S\\ref{sec:domain_differential}).\n\nThe additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\\gamma_k \\cdot e_{ij} / a_i$ units on the ability scale (this holds exactly under linearization of the logistic function; the true shift is nonlinear and probability-dependent).\n\nFor MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\\ref{sec:4pl_details}); this requires $J \\geq 16$ and is not used in domain-level analyses ($J = 13$).\n\n\\paragraph{Inference.}\nWe perform Bayesian inference via NUTS \\citep{hoffman2014} in Stan \\citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\\theta_j \\sim \\mathcal{N}(0,1)$, $a_i \\sim \\text{LogNormal}(0, 0.5)$, $b_i \\sim \\mathcal{N}(0,1)$, $\\gamma_k \\sim \\mathcal{N}(0,1)$. Convergence requires split-$\\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.\n\n\\paragraph{Calibrated score.}\nThe decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:\n\\begin{equation}\n\\label{eq:calibrated}\n    \\text{Acc}_{j}^{\\text{cal}} = \\frac{1}{I_k} \\sum_{i=1}^{I_k}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[\\sigma\\!\\bigl(a_i(\\theta_j - b_i)\\bigr)\\right],\n\\end{equation}\nwith credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.\n\n\\paragraph{Identifiability.}\n\\label{sec:fisher}\n\\label{sec:value_decomposition}\nThe reliability of $\\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\\geq$0.55 with $J \\geq 50$ (Appendix~\\ref{sec:identifiability}). Eq.~\\eqref{eq:calibrated} depends on $\\theta_j$, not $\\gamma$ directly, predicting that vanilla 2PL ($\\gamma\\!=\\!0$) achieves comparable calibration to 2PL+$\\gamma$, with $\\gamma_k$ serving diagnosis rather than calibration (\\S\\ref{sec:calibration_results}).\n\n\\subsection{Dose-Response Profile Classification}\n\\label{sec:classification}\n\nIndependent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern. Algorithm~\\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by a noise threshold $\\tau$, severity threshold $\\sigma$, saturation ratio $\\rho$, and late-gain floor $\\lambda$. The three-way top-level split (immune/harm/benefit) is governed by the sign and magnitude of $\\Delta = a_{100} - a_0$ relative to $\\tau$; within-branch refinements distinguish U-collapse from V-recovery (via mid-dosage trough detection) and monotonic benefit from benefit-saturation (via gain deceleration). A mid-trajectory volatility check ($v^*$) within the immune branch distinguishes true immunity (Phi-4: $v^* = 0.34$pp $\\le \\tau$) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$); recovery extent varies by seed (partial at seed$=$42, full at seed$=$123). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms 5/5 families are stable across all $(\\tau, \\sigma)$ combinations (Appendix~\\ref{sec:classification_sensitivity}).\n\n\\begin{algorithm}[H]\n\\caption{Dose-Response Profile Classification}\n\\label{alg:profile-classification}\n\\begin{algorithmic}[1]\n\\Require Accuracy vector $\\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \\in \\{0, 5, 25, 50, 100\\}\\%$\n\\Require Noise threshold $\\tau = 1$ pp, severity threshold $\\sigma = 5$ pp\n\\Require Saturation ratio $\\rho = 0.3$, late-gain floor $\\lambda = 0.5$ pp\n\\Ensure Pattern $p \\in \\{\\textsc{Immune}, \\textsc{U-collapse}, \\textsc{V-recovery}, \\textsc{Benefit}, \\textsc{Benefit-sat}\\}$\n\\State $\\Delta \\gets a_{100} - a_{0}$ \\Comment{end-to-end accuracy shift}\n\\State $m^* \\gets \\min(a_{5},\\, a_{25},\\, a_{50})$ \\Comment{mid-dosage minimum}\n\\State $v^* \\gets \\max_{i \\in \\{5,25,50\\}} |a_i - a_0|$ \\Comment{max mid-trajectory deviation}\n\\If{$|\\Delta| \\le \\tau$}\n    \\If{$v^* \\le \\tau$}\n        \\State \\Return \\textsc{Immune} \\Comment{fluctuation within noise band}\n    \\ElsIf{$m^* < a_{0}$ \\textbf{and} $m^* < a_{100}$}\n        \\State \\Return \\textsc{V-recovery} \\Comment{V-dip with full endpoint recovery}\n    \\Else\n        \\State \\Return \\textsc{Immune} \\Comment{non-V volatility, endpoint stable}\n    \\EndIf\n\\ElsIf{$\\Delta < -\\tau$}\n    \\If{$\\Delta \\le -\\sigma$}\n        \\State \\Return \\textsc{U-collapse} \\Comment{severe monotonic degradation}\n    \\ElsIf{$m^* < a_{0}$ \\textbf{and} $m^* < a_{100}$}\n        \\State \\Return \\textsc{V-recovery} \\Comment{mid-dosage trough with partial recovery}\n    \\Else\n        \\State \\Return \\textsc{U-collapse} \\Comment{moderate decline, no V-shape}\n    \\EndIf\n\\Else \\Comment{$\\Delta > \\tau$}\n    \\State $g_1 \\gets a_{25} - a_{0}$ \\Comment{first-half gain}\n    \\State $g_2 \\gets a_{100} - a_{25}$ \\Comment{second-half gain}\n    \\State $\\ell \\gets a_{100} - a_{50}$ \\Comment{late gain}\n    \\If{$(g_1 > 0$ \\textbf{and} $g_2 < \\rho \\cdot g_1)$ \\textbf{or} $\\ell < \\lambda$}\n        \\State \\Return \\textsc{Benefit-sat} \\Comment{gain decelerates at high dosage}\n    \\Else\n        \\State \\Return \\textsc{Benefit} \\Comment{sustained improvement}\n    \\EndIf\n\\EndIf\n\\end{algorithmic}\n\\end{algorithm}",
      "numLines": 99,
      "startLine": 1,
      "totalLines": 99
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01X1tMkaZtiVKNDqyu4rSQdq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "e448ba88-0f6f-481c-bb72-5da18416ac56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tgmU5F7WQLrXNB6BmAPUC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5399,
      "cache_read_input_tokens": 49124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5399
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

_source line 44 · 2026-05-19T22:06:27.486Z_

<details><summary>↩ Tool result · `toolu_01X1tMkaZtiVKNDqyu4rSQdq`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	We systematically profiled how SFT-injected contamination affects benchmark scores across model families and scales. Three findings emerge.
4	
5	\paragraph{Five patterns, not one.}
6	The ``contamination inflates scores'' assumption is a gross oversimplification. Controlled injection reveals five distinct dose-response patterns governed by a baseline ability threshold at 64.7\% MMLU (95\% CI: 64.0--65.4\%): models below it benefit ($+$3--4pp), models above are harmed ($-$3 to $-$10pp) or immune. Item-level DiD analysis (\S\ref{sec:memorization_test}) shows these patterns arise from global capability modulation, not item-specific memorization---challenging the premise of overlap-based detection methods. Contamination \emph{direction} is consistent across benchmarks; \emph{shape} varies with benchmark properties (Appendix~\ref{sec:arc_cross_benchmark}), implying model-\emph{and}-benchmark-specific profiling is necessary.
7	
8	\paragraph{Why bigger $\neq$ more robust.}
9	Qwen-14B ($-$10pp) is 3$\times$ more fragile than Qwen-7B ($-$3pp): SFT injection disrupts more specialized representations that smaller models have not yet developed. Organizations fine-tuning frontier models on mixed-quality data face greater capability degradation risk.
10	
11	\paragraph{Diagnostic value beyond aggregate calibration.}
12	Domain analysis reveals heterogeneity masked by aggregate scores (Social Sciences $P(\gamma_d\!<\!0) = 99.7\%$). The IRT framework captures both family-level patterns and domain-level decomposition. Pretraining contamination may produce qualitatively different effects \citep{schaeffer2026causally}; scaling to 70B+ is a natural next step.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "b03f752c-26a2-4813-881b-ed36860c77f3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nWe systematically profiled how SFT-injected contamination affects benchmark scores across model families and scales. Three findings emerge.\n\n\\paragraph{Five patterns, not one.}\nThe ``contamination inflates scores'' assumption is a gross oversimplification. Controlled injection reveals five distinct dose-response patterns governed by a baseline ability threshold at 64.7\\% MMLU (95\\% CI: 64.0--65.4\\%): models below it benefit ($+$3--4pp), models above are harmed ($-$3 to $-$10pp) or immune. Item-level DiD analysis (\\S\\ref{sec:memorization_test}) shows these patterns arise from global capability modulation, not item-specific memorization---challenging the premise of overlap-based detection methods. Contamination \\emph{direction} is consistent across benchmarks; \\emph{shape} varies with benchmark properties (Appendix~\\ref{sec:arc_cross_benchmark}), implying model-\\emph{and}-benchmark-specific profiling is necessary.\n\n\\paragraph{Why bigger $\\neq$ more robust.}\nQwen-14B ($-$10pp) is 3$\\times$ more fragile than Qwen-7B ($-$3pp): SFT injection disrupts more specialized representations that smaller models have not yet developed. Organizations fine-tuning frontier models on mixed-quality data face greater capability degradation risk.\n\n\\paragraph{Diagnostic value beyond aggregate calibration.}\nDomain analysis reveals heterogeneity masked by aggregate scores (Social Sciences $P(\\gamma_d\\!<\\!0) = 99.7\\%$). The IRT framework captures both family-level patterns and domain-level decomposition. Pretraining contamination may produce qualitatively different effects \\citep{schaeffer2026causally}; scaling to 70B+ is a natural next step.\n",
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

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01CTb1snhZgz6FVCHWGXPsfg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "224121c9-bb3d-46e3-abe0-d933b95e9d9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tgmU5F7WQLrXNB6BmAPUC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5399,
      "cache_read_input_tokens": 49124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5399
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

_source line 46 · 2026-05-19T22:06:28.021Z_

<details><summary>↩ Tool result · `toolu_01CTb1snhZgz6FVCHWGXPsfg`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	We identify ten limitations that bound the scope of our conclusions.
5	
6	\paragraph{Scale ceiling.}
7	All experiments use models at or below 14.7B parameters. Larger models (70B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
8	
9	\paragraph{Single seed.}
10	The five-pattern taxonomy (Table~\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.
11	
12	\paragraph{SFT ecological validity.}
13	We use LoRA-based SFT injection exclusively in AUGMENT mode (contaminated items appended to, not replacing, base SFT data). Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures. The position bias at 0.5B (A-option rate escalating from 46\% to 98\% with dosage) is likely SFT-specific. Generalization to pretraining contamination requires further validation.
14	
15	\paragraph{ARC-Challenge bootstrap stability.}
16	ARC-Challenge contains only 1{,}172 items (vs.\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\%, Gemma-2 62.7\% (vs.\ $\geq$76.6\% on MMLU). Gemma-2's ARC $\Delta$acc 95\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (U-collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.
17	
18	\paragraph{Signal coverage.}
19	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\S\ref{sec:signal_failure}).
20	
21	\paragraph{Ensemble size and per-domain power.}
22	Reliable $\gamma$ recovery requires $J \geq 50$. Our domain-level analysis ($J = 13$--$16$) yields a strong directional signal for only one of eight MMLU domains. Per-domain $\gamma$ diagnosis at current ensemble sizes is exploratory.
23	
24	\paragraph{Position bias.}
25	Qwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\% at d000 to 98\% at d100); these models are excluded from MC IRT analyses, reducing ensemble size.
26	
27	\paragraph{Model misfit in non-STEM domains.}
28	A single linear $\gamma$ cannot capture non-monotone contamination effects within a domain. The five-pattern taxonomy operates at the model level; richer within-domain specifications may be required for domain-level calibration.
29	
30	\paragraph{Additive $\gamma$ linearity.}
31	The 2PL+$\gamma$ model assumes contamination effects are additive and linear in exposure. PPP posterior predictive checks cannot detect threshold-type model misspecification (PPP remains 0.50--0.56 despite up to 33\% $\gamma$ overestimation), which highlights the value of simulation-based specification testing. The threshold DGP simulation uses uniform exposure; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.
32	
33	\paragraph{Prompt format sensitivity.}
34	The observed dose-response profiles are conditional on the evaluation protocol (5-shot prompting for MMLU, 25-shot for ARC-Challenge). Preliminary comparison with 0-shot evaluation suggests that pattern shapes may vary with prompt format---for instance, the V-type recovery pattern observed under 5-shot prompting can disappear under 0-shot conditions. This indicates that contamination effects interact with in-context learning mechanisms. While internal consistency is maintained (all 75 model--dosage configurations use the same protocol), practitioners replicating our analyses under different prompting regimes should expect quantitatively and potentially qualitatively different dose-response profiles. Future work should systematically evaluate protocol sensitivity across shot counts and prompt templates.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "88f8be3a-65fd-4ef8-9563-580c11d4ba03",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nWe identify ten limitations that bound the scope of our conclusions.\n\n\\paragraph{Scale ceiling.}\nAll experiments use models at or below 14.7B parameters. Larger models (70B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.\n\n\\paragraph{Single seed.}\nThe five-pattern taxonomy (Table~\\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.\n\n\\paragraph{SFT ecological validity.}\nWe use LoRA-based SFT injection exclusively in AUGMENT mode (contaminated items appended to, not replacing, base SFT data). Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures. The position bias at 0.5B (A-option rate escalating from 46\\% to 98\\% with dosage) is likely SFT-specific. Generalization to pretraining contamination requires further validation.\n\n\\paragraph{ARC-Challenge bootstrap stability.}\nARC-Challenge contains only 1{,}172 items (vs.\\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\\%, Gemma-2 62.7\\% (vs.\\ $\\geq$76.6\\% on MMLU). Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (U-collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.\n\n\\paragraph{Signal coverage.}\nS1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\\S\\ref{sec:signal_failure}).\n\n\\paragraph{Ensemble size and per-domain power.}\nReliable $\\gamma$ recovery requires $J \\geq 50$. Our domain-level analysis ($J = 13$--$16$) yields a strong directional signal for only one of eight MMLU domains. Per-domain $\\gamma$ diagnosis at current ensemble sizes is exploratory.\n\n\\paragraph{Position bias.}\nQwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\\% at d000 to 98\\% at d100); these models are excluded from MC IRT analyses, reducing ensemble size.\n\n\\paragraph{Model misfit in non-STEM domains.}\nA single linear $\\gamma$ cannot capture non-monotone contamination effects within a domain. The five-pattern taxonomy operates at the model level; richer within-domain specifications may be required for domain-level calibration.\n\n\\paragraph{Additive $\\gamma$ linearity.}\nThe 2PL+$\\gamma$ model assumes contamination effects are additive and linear in exposure. PPP posterior predictive checks cannot detect threshold-type model misspecification (PPP remains 0.50--0.56 despite up to 33\\% $\\gamma$ overestimation), which highlights the value of simulation-based specification testing. The threshold DGP simulation uses uniform exposure; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.\n\n\\paragraph{Prompt format sensitivity.}\nThe observed dose-response profiles are conditional on the evaluation protocol (5-shot prompting for MMLU, 25-shot for ARC-Challenge). Preliminary comparison with 0-shot evaluation suggests that pattern shapes may vary with prompt format---for instance, the V-type recovery pattern observed under 5-shot prompting can disappear under 0-shot conditions. This indicates that contamination effects interact with in-context learning mechanisms. While internal consistency is maintained (all 75 model--dosage configurations use the same protocol), practitioners replicating our analyses under different prompting regimes should expect quantitatively and potentially qualitatively different dose-response profiles. Future work should systematically evaluate protocol sensitivity across shot counts and prompt templates.\n",
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

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01WNo1Jw5A6Ymokc852iqEPU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "3ae891e7-fcdc-4e65-b5e9-664c89339d5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tgmU5F7WQLrXNB6BmAPUC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5399,
      "cache_read_input_tokens": 49124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5399
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

_source line 48 · 2026-05-19T22:06:28.241Z_

<details><summary>↩ Tool result · `toolu_01WNo1Jw5A6Ymokc852iqEPU`</summary>

```text
1	\appendix
2	
3	\section{ARC-Challenge Cross-Benchmark Analysis}
4	\label{sec:arc_cross_benchmark}
5	
6	ARC-Challenge (25-shot, 1{,}172 items) patterns are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$3.8pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($\pm$0.6pp). Gemma-2 ARC is excluded due to a 16pp evaluation artifact. Qwen-14B exhibits V-recovery on ARC rather than U-collapse ($-$3.4pp vs.\ $-$9.4pp on MMLU), a 2.8$\times$ attenuation reflecting benchmark-specific properties. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042), and Gemma-2's ARC $\Delta$acc 95\% CI crosses zero ($[-2.47, +0.09]$pp).
7	
8	Dose-response profiles are jointly determined by model and benchmark properties: direction is governed by model baseline ability (the 64.7\% threshold); shape is governed by benchmark properties (item pool size, difficulty distribution, evaluation format). This benchmark-conditionality is a finding in its own right---practitioners cannot assume a contamination profile on one benchmark transfers to another.
9	
10	\begin{figure}[h]
11	\centering
12	\includegraphics[width=\columnwidth]{figures/fig_arc_dose_response.pdf}
13	\caption{ARC-Challenge accuracy vs.\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\ref{fig:dose_response}) for 4/5 models.}
14	\label{fig:dose_response_arc}
15	\end{figure}
16	
17	\section{Signal Reliability Across Scales}
18	\label{sec:signal_reliability_appendix}
19	
20	\begin{figure}[h]
21	\centering
22	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap.pdf}
23	\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\%++) reverses at 0.5B; S4 is near-random below 1.5B.}
24	\label{fig:signal_heatmap}
25	\end{figure}
26	
27	\section{Identifiability Simulation}
28	\label{sec:identifiability_appendix}
29	
30	\begin{figure}[h]
31	\centering
32	\includegraphics[width=\columnwidth]{figures/fig_identifiability_heatmap.pdf}
33	\caption{$\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\% CI coverage $\geq90\%$ require $J\geq50$ at AUC$=$0.55, but only $J\geq16$ at AUC$\geq$0.90.}
34	\label{fig:identifiability_heatmap}
35	\end{figure}
36	
37	Fisher information $\mathcal{I}(\gamma) \propto \text{Var}(e_{\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\% CI coverage $\geq 90\%$ require $J \geq 50$; at AUC$\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).
38	
39	\section{4PL Extension}
40	\label{sec:4pl_details}
41	
42	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
43	\begin{equation}
44	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
45	\end{equation}
46	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
47	
48	\section{S4 Self-Critique Signal Details}
49	\label{sec:s4_details}
50	
51	S4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\text{YES})$, then score each item as the negative entropy of this distribution: $\text{S4}_i = -[-p\log p - (1-p)\log(1-p)]$ where $p = P(\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.
52	
53	\section{Training Convergence}
54	\label{sec:training_convergence}
55	
56	All SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.
57	
58	\section{Model Exclusion Details}
59	\label{sec:exclusion_details}
60	
61	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
62	
63	\paragraph{Model sets across analyses.}
64	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
65	
66	\begin{table}[h]
67	\centering
68	\caption{Model set composition across analyses.}
69	\label{tab:model_sets}
70	\footnotesize
71	\begin{tabular}{lcll}
72	\toprule
73	Analysis & $J$ & Model Set & Section \\
74	\midrule
75	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
76	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
77	Cross-family & 16--28 & varies by benchmark & \S\ref{sec:taxonomy} \\
78	Oracle ablation & 13 & domain whitelist & \S\ref{sec:calibration_results} \\
79	\bottomrule
80	\end{tabular}
81	\end{table}
82	
83	\section{Prior Sensitivity Analysis}
84	\label{sec:prior_sensitivity}
85	
86	To assess the influence of the $\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\gamma \sim \mathcal{N}(0, 0.5)$, $\mathcal{N}(0, 1)$ (default), and $\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\% CI includes zero in all cases (lower bound stable at $\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\hat{R} < 1.01$, ESS $> 3800$, PPP $\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\gamma$-based conclusions at current ensemble sizes.
87	
88	For the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:
89	
90	\begin{table}[h]
91	\centering
92	\caption{Social Sciences $\gamma$ prior sensitivity ($J$=16).}
93	\label{tab:socsci_prior}
94	\footnotesize
95	\begin{tabular}{lcccc}
96	\toprule
97	Prior & $\hat{\gamma}$ & 95\% CI & $P(\gamma\!<\!0)$ & PPP \\
98	\midrule
99	$\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\% & 0.242 \\
100	$\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\% & 0.282 \\
101	$\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\% & 0.282 \\
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	In contrast to the pooled analysis where $\hat{\gamma}$ shifts 2.6$\times$ across priors, Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.43 to $-$0.51), with $P(\gamma<0) \geq 97.95\%$ in all cases.
107	
108	\section{IRT Ability Separation by Scale}
109	\label{sec:theta_separation}
110	
111	Table~\ref{tab:theta_separation} reports the mean posterior $\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\Delta\theta = \bar{\theta}_{3\text{B}} - \bar{\theta}_{1.5\text{B}}$ is positive and significant (95\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.
112	
113	\begin{table}[h]
114	\centering
115	\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\Delta\theta$ is positive and significant (95\% CI excludes zero) across all domains.}
116	\label{tab:theta_separation}
117	\footnotesize
118	\begin{tabular}{lccc}
119	\toprule
120	Domain & $\bar{\theta}_{1.5\text{B}}$ & $\bar{\theta}_{3\text{B}}$ & $\Delta\theta$ [95\% CI] \\
121	\midrule
122	Math & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\
123	Science & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\
124	CS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\
125	Medical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\
126	Humanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\
127	Social Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\
128	Business/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\
129	Other & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\
130	\midrule
131	Pooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\
132	\bottomrule
133	\end{tabular}
134	\end{table}
135	
136	\section{DiD Across Dosage Levels}
137	\label{sec:did_dosage}
138	
139	\begin{figure}[h]
140	\centering
141	\includegraphics[width=\columnwidth]{figures/fig_did_dose_response.pdf}
142	\caption{Difference-in-differences (treated vs.\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all five model families, confirming that the global capability modulation mechanism (\S\ref{sec:memorization_test}) is consistent across the full dosage range.}
143	\label{fig:did_dose_response}
144	\end{figure}
145	
146	\section{Dose-Response Details}
147	\label{sec:dose_response_details}
148	
149	The five dose-response patterns reported in \S\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \textit{decreases} with dosage (0.41 at d000 $\to$ 0.27 at d100), consistent with the position bias confound documented in \S\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\%) overwhelms any memorization benefit.
150	
151	\section{Sensitivity of Profile Classification}
152	\label{sec:classification_sensitivity}
153	
154	We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\tau, \sigma)$ combinations: $\tau \in \{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\}$~pp $\times$ $\sigma \in \{3, 4, 5, 6, 7\}$~pp. Table~\ref{tab:sensitivity} reports stability across this grid.
155	
156	\begin{table}[h]
157	\centering
158	\caption{Profile classification stability across 30 $(\tau, \sigma)$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.}
159	\label{tab:sensitivity}
160	\footnotesize
161	\begin{tabular}{lccc}
162	\toprule
163	Model & Default Pattern & Stability & Notes \\
164	\midrule
165	Phi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\le$ all $\tau$ \\
166	Qwen-14B & U-collapse & 30/30 & --- \\
167	Gemma-2 9B & Benefit & 30/30 & --- \\
168	OLMo-2 7B & Benefit-sat & 30/30 & --- \\
169	Qwen-7B & V-recovery & 30/30 & volatility check resolves \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	With the mid-trajectory volatility check (Algorithm~\ref{alg:profile-classification}, line~3), all five families achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\Delta \approx 0$ but $v^* = 3.22$pp $> \tau$). The severity threshold $\sigma$ has zero impact on any model's classification, because no model's $\Delta\text{acc}$ falls in the range where $\sigma$ determines the U-collapse vs.\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\sigma=7$).
175	
176	\section{Cross-Family Domain Decomposition}
177	\label{sec:domain_decomposition}
178	
179	We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.
180	
181	Two patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, U-collapse (Qwen-14B) produces negative $\Delta\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\Delta\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.
182	
183	Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
184	
185	These results reinforce the global capability modulation interpretation (\S\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.
186	
187	\section{Baseline Ability vs.\ Contamination Effect}
188	\label{sec:baseline_vs_effect}
189	
190	\begin{figure}[h]
191	\centering
192	\includegraphics[width=\columnwidth]{figures/fig_baseline_vs_effect.pdf}
193	\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Threshold estimated from five models spanning four independent families.}
194	\label{fig:baseline_vs_effect}
195	\end{figure}
196	
197	\section{Per-Domain $\gamma$ Estimates}
198	\label{sec:domain_gamma_table}
199	
200	\begin{figure}[h]
201	\centering
202	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
203	\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}
204	\label{fig:domain_gamma}
205	\end{figure}
206	
207	\begin{table}[h]
208	\centering
209	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\hat{R} < 1.01$). Social Sciences $P(\gamma\!<\!0)$ strengthens from 99.1\% to 99.7\% at $J$=16, crossing the Bonferroni-corrected threshold of 99.375\% for eight tests. Results remain exploratory at these ensemble sizes \citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}
210	\label{tab:domain_gamma}
211	\footnotesize
212	\resizebox{\columnwidth}{!}{%
213	\begin{tabular}{lcccccc}
214	\toprule
215	 & \multicolumn{2}{c}{$J$=13} & \multicolumn{4}{c}{$J$=16} \\
216	\cmidrule(lr){2-3} \cmidrule(lr){4-7}
217	Domain & $\gamma$ & $P(\gamma\!<\!0)$ & $\gamma$ & $P(\gamma\!<\!0)$ & PPP & $\hat{R}$ \\
218	\midrule
219	MMLU: Math & +0.50 & 8.1\% & +0.60 & 3.8\% & 0.305 & 1.007 \\
220	MMLU: Science & +0.50 & 7.8\% & +0.57 & 4.3\% & 0.197 & 1.007 \\
221	MMLU: CS/Eng & +0.50 & 14.8\% & +0.32 & 24.0\% & 0.503 & 1.006 \\
222	MMLU: Medical & +0.24 & 24.0\% & +0.05 & 43.6\% & 0.268 & 1.008 \\
223	MMLU: Other & +0.13 & 35.7\% & +0.32 & 20.4\% & 0.072$^\dagger$ & 1.008 \\
224	MMLU: Business/Law & +0.04 & 44.1\% & +0.08 & 37.8\% & 0.395 & 1.007 \\
225	MMLU: Humanities & $-$0.31 & 85.4\% & $-$0.14 & 69.7\% & 0.416 & 1.007 \\
226	MMLU: Social Sci & $-$0.57 & \textbf{99.1\%} & $-$0.63 & \textbf{99.7\%} & 0.722 & 1.006 \\
227	\bottomrule
228	\end{tabular}}
229	
230	\vspace{2pt}
231	{\scriptsize $^\dagger$PPP below acceptable threshold (0.1); $\gamma$ estimate for this domain should be interpreted with caution.}
232	\end{table}
233	
234	\section{Threshold DGP Simulation}
235	\label{sec:threshold_dgp}
236	
237	To test whether threshold-type misspecification explains the non-significant oracle $\gamma$, we simulate data under step-function contamination DGPs where items are affected only above exposure thresholds of 0.3, 0.5, and 0.7 (three cutoffs, ten seeds each). Under these DGPs, the linear 2PL+$\gamma$ specification overestimates rather than attenuates the contamination effect (ratio 1.09 to 1.33 relative to the true $\gamma$), while PPP remains in the acceptable range (0.50 to 0.56). This rules out threshold-type misspecification as an explanation for the non-significant oracle $\gamma$ under a unidirectional effect assumption. Bidirectional item-level effects (positive for some items, negative for others) could still produce a near-zero pooled $\gamma$, but this collapses to the heterogeneity interpretation (\S\ref{sec:domain_differential}). The simulation uses uniform exposure distributions; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.
238	
239	\section{ARC IRT Results}
240	\label{sec:arc_irt}
241	
242	ARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\sim}$0.7pp) is smaller than correction noise. Domain-level $\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).
243	
244	\section{Full Baseline Comparison}
245	\label{sec:full_baselines}
246	
247	Table~\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.
248	
249	B6-DCR \citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.
250	
251	\begin{table}[h]
252	\centering
253	\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\downarrow$.}
254	\label{tab:full_baselines_arc}
255	\footnotesize
256	\begin{tabular}{lc}
257	\toprule
258	Method & ARC MAE \\
259	\midrule
260	B0-Raw & 0.059 \\
261	B1-Remove\&Rescore & 0.059 \\
262	B2-Single2PL+$\gamma$ & 0.064 \\
263	B3-Vanilla4PL & 0.071 \\
264	B4-LinearRegression & 0.056 \\
265	B5-Emperor & 0.059 \\
266	B6-DCR & --- \\
267	\midrule
268	ContamCal (4PL+$\gamma$) & \textbf{0.035} \\
269	\bottomrule
270	\end{tabular}
271	\end{table}
272	
273	\begin{table}[h]
274	\centering
275	\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\downarrow$.}
276	\label{tab:full_baselines_gsm8k}
277	\footnotesize
278	\begin{tabular}{lc}
279	\toprule
280	Method & GSM8K MAE \\
281	\midrule
282	B0-Raw & 0.003 \\
283	B2-Single2PL+$\gamma$ & 0.320 \\
284	B3-Vanilla4PL & 0.012 \\
285	B4-LinearRegression & \textbf{0.003} \\
286	B6-DCR & --- \\
287	\midrule
288	ContamCal (4PL+$\gamma$) & 0.020 \\
289	\bottomrule
290	\end{tabular}
291	\end{table}
292	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "51ddd447-f2ea-4b96-96a5-76a622bca619",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{ARC-Challenge Cross-Benchmark Analysis}\n\\label{sec:arc_cross_benchmark}\n\nARC-Challenge (25-shot, 1{,}172 items) patterns are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$3.8pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($\\pm$0.6pp). Gemma-2 ARC is excluded due to a 16pp evaluation artifact. Qwen-14B exhibits V-recovery on ARC rather than U-collapse ($-$3.4pp vs.\\ $-$9.4pp on MMLU), a 2.8$\\times$ attenuation reflecting benchmark-specific properties. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\\%, Gemma-2: 62.7\\%) due to the smaller item pool (1{,}172 vs.\\ 14{,}042), and Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero ($[-2.47, +0.09]$pp).\n\nDose-response profiles are jointly determined by model and benchmark properties: direction is governed by model baseline ability (the 64.7\\% threshold); shape is governed by benchmark properties (item pool size, difficulty distribution, evaluation format). This benchmark-conditionality is a finding in its own right---practitioners cannot assume a contamination profile on one benchmark transfers to another.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_arc_dose_response.pdf}\n\\caption{ARC-Challenge accuracy vs.\\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\\ref{fig:dose_response}) for 4/5 models.}\n\\label{fig:dose_response_arc}\n\\end{figure}\n\n\\section{Signal Reliability Across Scales}\n\\label{sec:signal_reliability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap.pdf}\n\\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\\%++) reverses at 0.5B; S4 is near-random below 1.5B.}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\section{Identifiability Simulation}\n\\label{sec:identifiability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_identifiability_heatmap.pdf}\n\\caption{$\\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\\% CI coverage $\\geq90\\%$ require $J\\geq50$ at AUC$=$0.55, but only $J\\geq16$ at AUC$\\geq$0.90.}\n\\label{fig:identifiability_heatmap}\n\\end{figure}\n\nFisher information $\\mathcal{I}(\\gamma) \\propto \\text{Var}(e_{\\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\\% CI coverage $\\geq 90\\%$ require $J \\geq 50$; at AUC$\\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \\citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).\n\n\\section{4PL Extension}\n\\label{sec:4pl_details}\n\nFor MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:\n\\begin{equation}\n    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwith $c_i \\sim \\text{Beta}(5,20)$ and $d_i \\sim \\text{Beta}(20,5)$. This requires $J \\geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\\gamma$ at $J=13$; pooled calibration uses $J=16$.\n\n\\section{S4 Self-Critique Signal Details}\n\\label{sec:s4_details}\n\nS4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\\text{YES})$, then score each item as the negative entropy of this distribution: $\\text{S4}_i = -[-p\\log p - (1-p)\\log(1-p)]$ where $p = P(\\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.\n\n\\section{Training Convergence}\n\\label{sec:training_convergence}\n\nAll SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.\n\n\\section{Model Exclusion Details}\n\\label{sec:exclusion_details}\n\nOf the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\\alpha=32$, lr$=5\\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.\n\n\\paragraph{Model sets across analyses.}\nTable~\\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\\S\\ref{sec:injection}). Core findings ($\\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.\n\n\\begin{table}[h]\n\\centering\n\\caption{Model set composition across analyses.}\n\\label{tab:model_sets}\n\\footnotesize\n\\begin{tabular}{lcll}\n\\toprule\nAnalysis & $J$ & Model Set & Section \\\\\n\\midrule\nPooled baselines & 16 & 8$\\times$Qwen-1.5B + 8$\\times$Qwen-3B & \\S\\ref{sec:calibration_results} \\\\\nDomain $\\gamma$ & 13 & 8$\\times$Qwen-1.5B + 5$\\times$Qwen-3B & \\S\\ref{sec:domain_differential} \\\\\nCross-family & 16--28 & varies by benchmark & \\S\\ref{sec:taxonomy} \\\\\nOracle ablation & 13 & domain whitelist & \\S\\ref{sec:calibration_results} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Prior Sensitivity Analysis}\n\\label{sec:prior_sensitivity}\n\nTo assess the influence of the $\\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\\gamma \\sim \\mathcal{N}(0, 0.5)$, $\\mathcal{N}(0, 1)$ (default), and $\\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\\% CI includes zero in all cases (lower bound stable at $\\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\\hat{R} < 1.01$, ESS $> 3800$, PPP $\\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\\gamma$-based conclusions at current ensemble sizes.\n\nFor the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:\n\n\\begin{table}[h]\n\\centering\n\\caption{Social Sciences $\\gamma$ prior sensitivity ($J$=16).}\n\\label{tab:socsci_prior}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nPrior & $\\hat{\\gamma}$ & 95\\% CI & $P(\\gamma\\!<\\!0)$ & PPP \\\\\n\\midrule\n$\\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\\% & 0.242 \\\\\n$\\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\\% & 0.282 \\\\\n$\\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\\% & 0.282 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn contrast to the pooled analysis where $\\hat{\\gamma}$ shifts 2.6$\\times$ across priors, Social Sciences $\\hat{\\gamma}$ varies only 1.2$\\times$ ($-$0.43 to $-$0.51), with $P(\\gamma<0) \\geq 97.95\\%$ in all cases.\n\n\\section{IRT Ability Separation by Scale}\n\\label{sec:theta_separation}\n\nTable~\\ref{tab:theta_separation} reports the mean posterior $\\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\\Delta\\theta = \\bar{\\theta}_{3\\text{B}} - \\bar{\\theta}_{1.5\\text{B}}$ is positive and significant (95\\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\\Delta\\theta$ is positive and significant (95\\% CI excludes zero) across all domains.}\n\\label{tab:theta_separation}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $\\bar{\\theta}_{1.5\\text{B}}$ & $\\bar{\\theta}_{3\\text{B}}$ & $\\Delta\\theta$ [95\\% CI] \\\\\n\\midrule\nMath & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\\\\nScience & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\\\\nCS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\\\\nMedical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\\\\nHumanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\\\\nSocial Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\\\\nBusiness/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\\\\nOther & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\\\\n\\midrule\nPooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{DiD Across Dosage Levels}\n\\label{sec:did_dosage}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_did_dose_response.pdf}\n\\caption{Difference-in-differences (treated vs.\\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all five model families, confirming that the global capability modulation mechanism (\\S\\ref{sec:memorization_test}) is consistent across the full dosage range.}\n\\label{fig:did_dose_response}\n\\end{figure}\n\n\\section{Dose-Response Details}\n\\label{sec:dose_response_details}\n\nThe five dose-response patterns reported in \\S\\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \\textit{decreases} with dosage (0.41 at d000 $\\to$ 0.27 at d100), consistent with the position bias confound documented in \\S\\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\\%) overwhelms any memorization benefit.\n\n\\section{Sensitivity of Profile Classification}\n\\label{sec:classification_sensitivity}\n\nWe assess the robustness of Algorithm~\\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\\tau, \\sigma)$ combinations: $\\tau \\in \\{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\\}$~pp $\\times$ $\\sigma \\in \\{3, 4, 5, 6, 7\\}$~pp. Table~\\ref{tab:sensitivity} reports stability across this grid.\n\n\\begin{table}[h]\n\\centering\n\\caption{Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.}\n\\label{tab:sensitivity}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nModel & Default Pattern & Stability & Notes \\\\\n\\midrule\nPhi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\\le$ all $\\tau$ \\\\\nQwen-14B & U-collapse & 30/30 & --- \\\\\nGemma-2 9B & Benefit & 30/30 & --- \\\\\nOLMo-2 7B & Benefit-sat & 30/30 & --- \\\\\nQwen-7B & V-recovery & 30/30 & volatility check resolves \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith the mid-trajectory volatility check (Algorithm~\\ref{alg:profile-classification}, line~3), all five families achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$). The severity threshold $\\sigma$ has zero impact on any model's classification, because no model's $\\Delta\\text{acc}$ falls in the range where $\\sigma$ determines the U-collapse vs.\\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\\sigma=7$).\n\n\\section{Cross-Family Domain Decomposition}\n\\label{sec:domain_decomposition}\n\nWe decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.\n\nTwo patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, U-collapse (Qwen-14B) produces negative $\\Delta\\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\\Delta\\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.\n\nSecond, domains differ in sensitivity. STEM is the most resilient (mean $|\\Delta\\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.\n\nThese results reinforce the global capability modulation interpretation (\\S\\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.\n\n\\section{Baseline Ability vs.\\ Contamination Effect}\n\\label{sec:baseline_vs_effect}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_baseline_vs_effect.pdf}\n\\caption{Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta$acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Threshold estimated from five models spanning four independent families.}\n\\label{fig:baseline_vs_effect}\n\\end{figure}\n\n\\section{Per-Domain $\\gamma$ Estimates}\n\\label{sec:domain_gamma_table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_domain_gamma.pdf}\n\\caption{Per-domain $\\gamma_d$ estimates with 95\\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}\n\\label{fig:domain_gamma}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-domain $\\gamma$ estimates (2PL+$\\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\\hat{R} < 1.01$). Social Sciences $P(\\gamma\\!<\\!0)$ strengthens from 99.1\\% to 99.7\\% at $J$=16, crossing the Bonferroni-corrected threshold of 99.375\\% for eight tests. Results remain exploratory at these ensemble sizes \\citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}\n\\label{tab:domain_gamma}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{$J$=13} & \\multicolumn{4}{c}{$J$=16} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-7}\nDomain & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & PPP & $\\hat{R}$ \\\\\n\\midrule\nMMLU: Math & +0.50 & 8.1\\% & +0.60 & 3.8\\% & 0.305 & 1.007 \\\\\nMMLU: Science & +0.50 & 7.8\\% & +0.57 & 4.3\\% & 0.197 & 1.007 \\\\\nMMLU: CS/Eng & +0.50 & 14.8\\% & +0.32 & 24.0\\% & 0.503 & 1.006 \\\\\nMMLU: Medical & +0.24 & 24.0\\% & +0.05 & 43.6\\% & 0.268 & 1.008 \\\\\nMMLU: Other & +0.13 & 35.7\\% & +0.32 & 20.4\\% & 0.072$^\\dagger$ & 1.008 \\\\\nMMLU: Business/Law & +0.04 & 44.1\\% & +0.08 & 37.8\\% & 0.395 & 1.007 \\\\\nMMLU: Humanities & $-$0.31 & 85.4\\% & $-$0.14 & 69.7\\% & 0.416 & 1.007 \\\\\nMMLU: Social Sci & $-$0.57 & \\textbf{99.1\\%} & $-$0.63 & \\textbf{99.7\\%} & 0.722 & 1.006 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\scriptsize $^\\dagger$PPP below acceptable threshold (0.1); $\\gamma$ estimate for this domain should be interpreted with caution.}\n\\end{table}\n\n\\section{Threshold DGP Simulation}\n\\label{sec:threshold_dgp}\n\nTo test whether threshold-type misspecification explains the non-significant oracle $\\gamma$, we simulate data under step-function contamination DGPs where items are affected only above exposure thresholds of 0.3, 0.5, and 0.7 (three cutoffs, ten seeds each). Under these DGPs, the linear 2PL+$\\gamma$ specification overestimates rather than attenuates the contamination effect (ratio 1.09 to 1.33 relative to the true $\\gamma$), while PPP remains in the acceptable range (0.50 to 0.56). This rules out threshold-type misspecification as an explanation for the non-significant oracle $\\gamma$ under a unidirectional effect assumption. Bidirectional item-level effects (positive for some items, negative for others) could still produce a near-zero pooled $\\gamma$, but this collapses to the heterogeneity interpretation (\\S\\ref{sec:domain_differential}). The simulation uses uniform exposure distributions; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.\n\n\\section{ARC IRT Results}\n\\label{sec:arc_irt}\n\nARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\\sim}$0.7pp) is smaller than correction noise. Domain-level $\\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).\n\n\\section{Full Baseline Comparison}\n\\label{sec:full_baselines}\n\nTable~\\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.\n\nB6-DCR \\citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_arc}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & ARC MAE \\\\\n\\midrule\nB0-Raw & 0.059 \\\\\nB1-Remove\\&Rescore & 0.059 \\\\\nB2-Single2PL+$\\gamma$ & 0.064 \\\\\nB3-Vanilla4PL & 0.071 \\\\\nB4-LinearRegression & 0.056 \\\\\nB5-Emperor & 0.059 \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & \\textbf{0.035} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_gsm8k}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & GSM8K MAE \\\\\n\\midrule\nB0-Raw & 0.003 \\\\\nB2-Single2PL+$\\gamma$ & 0.320 \\\\\nB3-Vanilla4PL & 0.012 \\\\\nB4-LinearRegression & \\textbf{0.003} \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & 0.020 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 292,
      "startLine": 1,
      "totalLines": 292
    }
  }
}
```

</details>

---

### Assistant

_source line 49_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of:
1. The current paper structure and content (docs/paper/)
2. The paper framing document
3. The ROADMAP
4. The memory.md with recent decisions

Let me also read the ethics and experimental setup sections that are in the compiled paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "89820cf4-a730-4862-bef8-41768c1b32f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C46JSXPAD1QiykbZimH3zd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14227,
      "cache_read_input_tokens": 54523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14227
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

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01V7CQjPqieafMCWpRYo7ac1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "ece90de8-4ab3-4f4b-a5bd-a7a801f522ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C46JSXPAD1QiykbZimH3zd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14227,
      "cache_read_input_tokens": 54523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14227
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

_source line 51 · 2026-05-19T22:06:34.950Z_

<details><summary>↩ Tool result · `toolu_01V7CQjPqieafMCWpRYo7ac1`</summary>

```text
1	\section*{Ethics Statement}
2	
3	All experiments use publicly available, open-weight language models (Qwen2.5, Phi-4, OLMo-2, and Gemma-2) under their respective licenses. Contamination injection is performed via standard supervised fine-tuning on existing public benchmark items; no new data collection involving human subjects is conducted. All evaluation benchmarks (MMLU, ARC-Challenge, GSM8K) are publicly released datasets. This work does not involve private user data, personally identifiable information, or human annotation.
4	
5	We acknowledge a dual-use risk: the contamination injection protocol we describe could be used to deliberately inflate benchmark scores. We mitigate this by focusing on detection and measurement rather than injection optimization, and by releasing detection signals rather than injection recipes. Our findings characterize the conditions under which SFT injection affects aggregate scores, which may inform decisions about manipulation risk at different scales. The measurement framework is intended to improve evaluation transparency, not to enable gaming.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "fd583eae-8c32-413e-a73b-b239f6ab4965",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex",
      "content": "\\section*{Ethics Statement}\n\nAll experiments use publicly available, open-weight language models (Qwen2.5, Phi-4, OLMo-2, and Gemma-2) under their respective licenses. Contamination injection is performed via standard supervised fine-tuning on existing public benchmark items; no new data collection involving human subjects is conducted. All evaluation benchmarks (MMLU, ARC-Challenge, GSM8K) are publicly released datasets. This work does not involve private user data, personally identifiable information, or human annotation.\n\nWe acknowledge a dual-use risk: the contamination injection protocol we describe could be used to deliberately inflate benchmark scores. We mitigate this by focusing on detection and measurement rather than injection optimization, and by releasing detection signals rather than injection recipes. Our findings characterize the conditions under which SFT injection affects aggregate scores, which may inform decisions about manipulation risk at different scales. The measurement framework is intended to improve evaluation transparency, not to enable gaming.\n",
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

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01Atj96UYLNvRqbStZnusC7f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "b38ad82e-3ab8-4417-82c2-7487e1884fc4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C46JSXPAD1QiykbZimH3zd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14227,
      "cache_read_input_tokens": 54523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14227
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

_source line 53 · 2026-05-19T22:06:35.194Z_

<details><summary>↩ Tool result · `toolu_01Atj96UYLNvRqbStZnusC7f`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), and Gemma-2 \citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, lr$=5\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus; at d100, 16{,}533 benchmark items are added beyond 50{,}000 base examples.
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}).
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
17	
18	\textbf{ARC-Challenge} \citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.
19	
20	\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts.
21	
22	All multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.
23	
24	We assess calibration quality via MAE (calibrated vs.\ ground-truth clean accuracy), Kendall $\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\gamma$ direction ($P(\gamma\!<\!0 \mid \text{data})$), and split-$\hat{R}$ convergence.
25	
26	\subsection{Baselines}
27	\label{sec:baselines}
28	
29	We compare against seven baselines: \textbf{B0-Raw} (no adjustment), \textbf{B1-Remove\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \textbf{B2-Single2PL+$\gamma$} (aggregate $\gamma$ without domain stratification), \textbf{B3-Vanilla2PL} ($\gamma=0$, isolating IRT ability estimation), \textbf{B4-LinearRegression} (residuals on exposure scores), \textbf{B5-Emperor} (mitigation strategies from \citet{sun2025emperor}; B5b uses the best-performing variant), and \textbf{B6-DCR} (our reimplementation following \citealp{xu2025dcr}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "8dc2309c-a481-430e-85a1-7ab04d2c17a9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experiments}\n\n\\subsection{Controlled SFT Injection}\n\\label{sec:injection}\n\nWe construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \\citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \\citep{abdin2024phi4} (14.7B), OLMo-2 \\citep{olmo2team2025} (7B), and Gemma-2 \\citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \\citep{hu2022lora} ($r=16$, $\\alpha=32$, lr$=5\\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\\%, clean control), d005 (5\\%), d025 (25\\%), d050 (50\\%), and d100 (100\\%). Contaminated items augment (not replace) the base SFT corpus; at d100, 16{,}533 benchmark items are added beyond 50{,}000 base examples.\n\nQwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\\% at d000 to 98\\% at d100; \\S\\ref{sec:signal_failure}).\n\n\\subsection{Benchmarks, Domains, and Evaluation}\n\\label{sec:benchmarks}\n\nWe evaluate on three benchmarks spanning distinct cognitive demands and response formats.\n\n\\textbf{MMLU} \\citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \\& Engineering, Medical, Humanities, Social Sciences, Business \\& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\\S\\ref{sec:results}).\n\n\\textbf{ARC-Challenge} \\citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.\n\n\\textbf{GSM8K} \\citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts.\n\nAll multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.\n\nWe assess calibration quality via MAE (calibrated vs.\\ ground-truth clean accuracy), Kendall $\\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\\gamma$ direction ($P(\\gamma\\!<\\!0 \\mid \\text{data})$), and split-$\\hat{R}$ convergence.\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\nWe compare against seven baselines: \\textbf{B0-Raw} (no adjustment), \\textbf{B1-Remove\\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \\textbf{B2-Single2PL+$\\gamma$} (aggregate $\\gamma$ without domain stratification), \\textbf{B3-Vanilla2PL} ($\\gamma=0$, isolating IRT ability estimation), \\textbf{B4-LinearRegression} (residuals on exposure scores), \\textbf{B5-Emperor} (mitigation strategies from \\citet{sun2025emperor}; B5b uses the best-performing variant), and \\textbf{B6-DCR} (our reimplementation following \\citealp{xu2025dcr}).",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

Now I have a complete picture. Let me generate the update checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "7f31e71d-b303-4e8f-a08f-c951e70bc408",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZJfH7rXJpiRueK5brQhnL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 68750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1666
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

_source line 55_

<details open><summary>🔧 Tool call — Write · `toolu_01SyuKsLi5YE6Wyi38yo2cpG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_update_checklist.md",
  "content": "# Paper Update Checklist — contamcal-irt-calibration\n\n> Generated 2026-05-19. Paper: 7 pages main text. Deadline: EMNLP 2026 ARR May 25 (D+6).\n> Current state: docs/paper/*.tex. Sections: abstract, introduction, related_work, method, experimental_setup, results, conclusion (merged with discussion), limitations, ethics, appendix.\n\n---\n\n## Section: Abstract (abstract.tex)\n\n- [ ] **P0** 更新 seed 信息：当前写 \"seed=42\"，V-recovery 已双种子确认（D165），改为 \"confirmed across two seeds\" 并更新 Δacc 表述（s42 partial −1.82pp, s123 full 0.00pp → \"mid-dosage trough with seed-dependent recovery extent\"）\n- [ ] **P1** 加入 GSM8K negative control 结果（待 eval 完成）：一句话 \"GSM8K (open-ended) shows near-zero contamination effect, confirming format-dependent vulnerability\"\n- [ ] **P1** 加入 DiD finding 一句：\"Item-level DiD shows no memorization; effects arise from global capability modulation\"\n- [ ] **P0** triple-seed 完成后：如升级为 taxonomy 需改 \"observed profiles\" → \"taxonomy\"；如降级为 3-pattern 需相应修改（gated on s0 results）\n\n## Section: Introduction (introduction.tex)\n\n- [ ] **P0** Contribution 1 更新：当前写 \"Five-pattern contamination taxonomy\"，但 framing 要求仅 triple-seed 后才能称 taxonomy。在 s0 完成前改为 \"Five observed dose-response profiles\"，或在 triple-seed 确认后保持 taxonomy\n- [ ] **P0** V-recovery 描述更新：当前贡献列表中未提及双种子确认。加 \"confirmed across two seeds (partial and full recovery)\" 到 Contribution 1\n- [ ] **P1** Contribution 2 (DiD global modulation) 已在当前版本中，检查是否需要更新措辞以反映 \"all 5 families\" 的 DiD 结果\n- [ ] **P1** GSM8K 结果整合后，在 contributions 或 intro 末尾加一句 benchmark-conditionality framing\n\n## Section: Related Work (related_work.tex)\n\n- [ ] **P1** 检查是否已引用 Han et al. 2026 (quantifying contamination via psychometric DIF)——当前已有，OK\n- [ ] **P1** 考虑加 1 句 multi-family contamination profiling 的空白（当前 related work 没有显式说 \"no prior work profiles across families\"——这在 intro 中说了，related work 可加一句呼应）\n\n## Section: Method (method.tex)\n\n- [ ] **P0** Algorithm 1 volatility fix (v2)：当前 method.tex 的 Algorithm 1 已包含 v* mid-trajectory check（line 3, 71-78），确认与 v2 180/180 版本一致。需验证 paper 中的伪代码是否完全匹配 profile_classifier.py v2\n- [ ] **P1** 如 triple-seed 结果出来且 profile 合并（如 V-type + U-type → \"harm\"），Algorithm 1 的输出集合需更新\n\n## Section: Experimental Setup (experimental_setup.tex)\n\n- [ ] **P0** 更新 seed 信息：当前写 \"Models at ≤3B are trained with two seeds\"。7B/14B 如果 s123 完成，需更新为 \"7B with two seeds, 14B/Phi-4/OLMo-2/Gemma-2 with one seed\"（或等 s0 后写 \"7B with three seeds\"）\n- [ ] **P0** 更新 checkpoint 总数：当前 \"over 50 checkpoints\"，s123 完成后实际数量需核实更新\n- [ ] **P1** GSM8K eval 协议：当前 benchmarks 段已提 GSM8K，但 eval 细节（8-shot CoT, generation-based）未在 setup 中写明。如 GSM8K 结果入主文，需补 eval 协议细节\n- [ ] **P1** evaluate.py 版本声明：C009 约束要求 eval 一致性。考虑在 setup 加一句 \"All evaluations use a unified evaluation script verified via hash consistency across servers\"\n\n## Section: Results (results.tex)\n\n### 5.1 Five Dose-Response Patterns\n- [ ] **P0** Table 1 加 s123 列：当前 Table 1 只有 seed=42 数据。V-recovery 双种子已确认（D165），至少更新 Qwen-7B 行加 s123 Δacc=0.00pp。其他 4 family s123 结果 pending\n- [ ] **P0** V-recovery 段落更新：当前 ¶30 已写 \"V-shaped harm-then-recovery under both seeds (trough at d025 for seed=42, d005 for seed=123; recovery extent varies from partial to full)\"——确认此句与 D165 结果一致，OK。但 Table 1 需同步更新数据\n- [ ] **P0** Triple-seed 完成后：Table 1 加 error bars（3-seed mean ± std），或改为 \"2-seed confirmed\" 表述\n- [ ] **P1** Domain decomposition 已有一句引用 Appendix（¶30 末尾 \"Cross-family domain decomposition reveals consistent directionality...\"），确认 Appendix 内容与 D166 domain decomposition 数据一致\n\n### 5.2 Item-Level Memorization Test (DiD)\n- [ ] **P0** 确认 Table 2 (DiD) 数据是否为 aligned evaluate.py 版本结果。D161 记录 DiD 完成，但需确认是 s42 aligned 还是旧 eval 版本\n- [ ] **P1** 如有 s123 DiD 数据，可在文字中加 \"replicated under seed=123\" 一句\n\n### 5.3 Calibration Quality\n- [ ] **P1** 当前 calibration 仅在 Qwen ≤3B (J=16) 上做。如 s123/s0 完成后做 cross-family IRT fitting（2PL+γ on 7B-14.7B），需更新 Table 3 或加新表\n- [ ] **P1** IRT 2PL+γ fitting 待 s123 eval 完成后执行，结果可能更新 calibration 数据\n\n### 5.4 Signal Failure\n- [ ] **P1** 当前 signal failure 数据来自 ≤3B Qwen。如有 7B-14.7B signal 数据可加一句跨规模确认\n\n### 5.5 Domain-Level Analysis\n- [ ] **P1** 当前 domain analysis 仅在 Qwen ≤3B。Cross-family domain decomposition（D166, STEM resilient / Social Sci sensitive）已有 Appendix 内容。确认 Appendix 文字与数据一致\n\n### GSM8K（新增子节或加入现有框架）\n- [ ] **P0** GSM8K eval 完成后：加入 Results 作为 negative control。选项：(a) 新子节 \"5.X GSM8K: Format-Dependent Vulnerability\"，(b) 整合入 5.1 作为 paragraph。建议 (b) 省空间——在 baseline threshold 段加一段 \"GSM8K (open-ended) shows near-zero contamination effect across all families, confirming that dose-response profiles are benchmark-conditioned\"\n- [ ] **P1** 如 GSM8K 有 family-specific 差异（如某 family 在 GSM8K 上也有变化），需要额外讨论\n\n## Section: Discussion and Conclusion (conclusion.tex)\n\n- [ ] **P0** ¶1 \"Five patterns, not one\"：更新 V-recovery 描述。当前已有 \"consistent across benchmarks\" 但未提双种子确认。加 \"V-recovery is confirmed across two seeds with varying recovery extent\"\n- [ ] **P0** 如 GSM8K 结果显著，加一段 benchmark-conditionality 讨论（当前 discussion 未显式讨论 GSM8K negative control 的含义）\n- [ ] **P1** DiD 段：当前 ¶1 已提 \"Item-level DiD analysis shows these patterns arise from global capability modulation\"。如有新数据（s123 DiD）可加强\n- [ ] **P1** Domain decomposition 讨论：当前 ¶3 提 domain analysis。如 STEM-resilient / Social-Sci-sensitive 数据已在 Appendix，加一句具体数据引用\n\n## Section: Limitations (limitations.tex)\n\n- [ ] **P0** \"Single seed\" 段落更新：当前写 \"confirmed across two seeds (s42, s123)\"。如 s0 完成前提交，保持此表述。如 s0 完成，改为 \"triple-seed validated\"\n- [ ] **P0** 如 GSM8K eval 完成但仅 d000+d100 两个端点，在 limitations 加 \"GSM8K evaluated at endpoint dosages only (d000, d100); intermediate dosage profiles not characterized\"\n- [ ] **P1** Prompt format sensitivity 段（当前最后一段）：已提 \"pattern shapes may vary with prompt format\"——确认与 D154b 一致，OK\n- [ ] **P1** 考虑加 \"Benefit models (OLMo-2, Gemma-2) may exhibit different behavior under pretraining contamination vs SFT injection\" 以呼应 DiD global-modulation finding\n\n## Section: Ethics (ethics.tex)\n\n- [ ] **P1** 当前已完整覆盖。无需更新，除非 GSM8K 引入新 benchmark 需提及（已在 list 中）\n\n## Section: Appendix (appendix.tex)\n\n### Existing appendix sections（确认数据一致性）\n- [ ] **P0** Appendix A (ARC Cross-Benchmark): 确认与 s42 aligned eval 数据一致\n- [ ] **P0** Appendix K (Sensitivity): 确认 30/30 → 180/180 更新。当前写 \"30 (τ,σ) combinations\"，但 D164/Algorithm v2 报告 180/180 (6 families × 30 combos)。需更新描述或确认 30/30 是 per-family\n\n### 新增 appendix 内容\n- [ ] **P0** Domain decomposition 完整数据表：Appendix L (sec:domain_decomposition) 已有定性描述 + 数据。确认 STEM 2.8pp / Social Sci 5.1pp 数据已在文中\n- [ ] **P1** GSM8K 详细结果表（eval 完成后）：per-family GSM8K accuracy at d000/d100\n- [ ] **P1** V-recovery 双种子对比图：s42 vs s123 trajectory overlay（已有数据可直接生成）\n- [ ] **P1** Fisher Information 推导：framing 提到 \"must derive I(γ) for appendix\"。如来得及，加入推导\n\n## Section: Figures\n\n- [ ] **P0** Fig 1 (dose-response): 确认当前 fig_dose_response.pdf 使用 s42 aligned eval 数据（非旧 eval 版本）\n- [ ] **P0** Fig 2 (treated/untreated DiD): 确认使用 aligned eval 数据\n- [ ] **P1** 如加 GSM8K 结果：可在 Fig 1 加 subplot 或在 appendix 加单独图\n- [ ] **P1** 如加 s123 数据：考虑在 appendix 加 s123 dose-response overlay 图\n- [ ] **P1** Baseline vs effect scatter (fig_baseline_vs_effect.pdf): 确认已是 aligned eval 数据\n\n## Section: References\n\n- [ ] **P1** 确认所有已引用论文的 bib 条目完整（特别是 han2026quantifying, schaeffer2026causally 等 2026 引用）\n- [ ] **P1** 检查是否遗漏 framing 中要求的引用（DIF literature, conformal prediction 等——部分为 appendix/future work 引用）\n\n---\n\n## Priority Summary\n\n**P0 (must have for submission, ~15 items)**:\n1. V-recovery 双种子确认整合到 abstract + results Table 1 + discussion\n2. Algorithm 1 v2 一致性验证（method 伪代码 vs profile_classifier.py）\n3. GSM8K 结果整合（待 eval 完成）\n4. Experimental setup seed/checkpoint 数更新\n5. Figure 数据一致性验证（aligned eval）\n6. Sensitivity 描述更新（30→180）\n7. Limitations seed 段更新\n8. DiD 数据版本确认\n\n**P1 (nice to have, ~20 items)**:\n1. s123 cross-family 数据更新（Table 1 扩展）\n2. GSM8K 在各 section 的引用\n3. Domain decomposition appendix 完善\n4. Related work 呼应句\n5. Fisher Information 推导\n6. V-recovery 双种子对比图\n7. Reference audit\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "bcf1e8bc-5113-4d65-a53a-adba26d33063",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZJfH7rXJpiRueK5brQhnL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 68750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1666
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

_source line 56 · 2026-05-19T22:08:02.003Z_

<details><summary>↩ Tool result · `toolu_01SyuKsLi5YE6Wyi38yo2cpG`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_update_checklist.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "04b9d461-725a-4697-a017-a0bf8eb345db",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_update_checklist.md",
    "content": "# Paper Update Checklist — contamcal-irt-calibration\n\n> Generated 2026-05-19. Paper: 7 pages main text. Deadline: EMNLP 2026 ARR May 25 (D+6).\n> Current state: docs/paper/*.tex. Sections: abstract, introduction, related_work, method, experimental_setup, results, conclusion (merged with discussion), limitations, ethics, appendix.\n\n---\n\n## Section: Abstract (abstract.tex)\n\n- [ ] **P0** 更新 seed 信息：当前写 \"seed=42\"，V-recovery 已双种子确认（D165），改为 \"confirmed across two seeds\" 并更新 Δacc 表述（s42 partial −1.82pp, s123 full 0.00pp → \"mid-dosage trough with seed-dependent recovery extent\"）\n- [ ] **P1** 加入 GSM8K negative control 结果（待 eval 完成）：一句话 \"GSM8K (open-ended) shows near-zero contamination effect, confirming format-dependent vulnerability\"\n- [ ] **P1** 加入 DiD finding 一句：\"Item-level DiD shows no memorization; effects arise from global capability modulation\"\n- [ ] **P0** triple-seed 完成后：如升级为 taxonomy 需改 \"observed profiles\" → \"taxonomy\"；如降级为 3-pattern 需相应修改（gated on s0 results）\n\n## Section: Introduction (introduction.tex)\n\n- [ ] **P0** Contribution 1 更新：当前写 \"Five-pattern contamination taxonomy\"，但 framing 要求仅 triple-seed 后才能称 taxonomy。在 s0 完成前改为 \"Five observed dose-response profiles\"，或在 triple-seed 确认后保持 taxonomy\n- [ ] **P0** V-recovery 描述更新：当前贡献列表中未提及双种子确认。加 \"confirmed across two seeds (partial and full recovery)\" 到 Contribution 1\n- [ ] **P1** Contribution 2 (DiD global modulation) 已在当前版本中，检查是否需要更新措辞以反映 \"all 5 families\" 的 DiD 结果\n- [ ] **P1** GSM8K 结果整合后，在 contributions 或 intro 末尾加一句 benchmark-conditionality framing\n\n## Section: Related Work (related_work.tex)\n\n- [ ] **P1** 检查是否已引用 Han et al. 2026 (quantifying contamination via psychometric DIF)——当前已有，OK\n- [ ] **P1** 考虑加 1 句 multi-family contamination profiling 的空白（当前 related work 没有显式说 \"no prior work profiles across families\"——这在 intro 中说了，related work 可加一句呼应）\n\n## Section: Method (method.tex)\n\n- [ ] **P0** Algorithm 1 volatility fix (v2)：当前 method.tex 的 Algorithm 1 已包含 v* mid-trajectory check（line 3, 71-78），确认与 v2 180/180 版本一致。需验证 paper 中的伪代码是否完全匹配 profile_classifier.py v2\n- [ ] **P1** 如 triple-seed 结果出来且 profile 合并（如 V-type + U-type → \"harm\"），Algorithm 1 的输出集合需更新\n\n## Section: Experimental Setup (experimental_setup.tex)\n\n- [ ] **P0** 更新 seed 信息：当前写 \"Models at ≤3B are trained with two seeds\"。7B/14B 如果 s123 完成，需更新为 \"7B with two seeds, 14B/Phi-4/OLMo-2/Gemma-2 with one seed\"（或等 s0 后写 \"7B with three seeds\"）\n- [ ] **P0** 更新 checkpoint 总数：当前 \"over 50 checkpoints\"，s123 完成后实际数量需核实更新\n- [ ] **P1** GSM8K eval 协议：当前 benchmarks 段已提 GSM8K，但 eval 细节（8-shot CoT, generation-based）未在 setup 中写明。如 GSM8K 结果入主文，需补 eval 协议细节\n- [ ] **P1** evaluate.py 版本声明：C009 约束要求 eval 一致性。考虑在 setup 加一句 \"All evaluations use a unified evaluation script verified via hash consistency across servers\"\n\n## Section: Results (results.tex)\n\n### 5.1 Five Dose-Response Patterns\n- [ ] **P0** Table 1 加 s123 列：当前 Table 1 只有 seed=42 数据。V-recovery 双种子已确认（D165），至少更新 Qwen-7B 行加 s123 Δacc=0.00pp。其他 4 family s123 结果 pending\n- [ ] **P0** V-recovery 段落更新：当前 ¶30 已写 \"V-shaped harm-then-recovery under both seeds (trough at d025 for seed=42, d005 for seed=123; recovery extent varies from partial to full)\"——确认此句与 D165 结果一致，OK。但 Table 1 需同步更新数据\n- [ ] **P0** Triple-seed 完成后：Table 1 加 error bars（3-seed mean ± std），或改为 \"2-seed confirmed\" 表述\n- [ ] **P1** Domain decomposition 已有一句引用 Appendix（¶30 末尾 \"Cross-family domain decomposition reveals consistent directionality...\"），确认 Appendix 内容与 D166 domain decomposition 数据一致\n\n### 5.2 Item-Level Memorization Test (DiD)\n- [ ] **P0** 确认 Table 2 (DiD) 数据是否为 aligned evaluate.py 版本结果。D161 记录 DiD 完成，但需确认是 s42 aligned 还是旧 eval 版本\n- [ ] **P1** 如有 s123 DiD 数据，可在文字中加 \"replicated under seed=123\" 一句\n\n### 5.3 Calibration Quality\n- [ ] **P1** 当前 calibration 仅在 Qwen ≤3B (J=16) 上做。如 s123/s0 完成后做 cross-family IRT fitting（2PL+γ on 7B-14.7B），需更新 Table 3 或加新表\n- [ ] **P1** IRT 2PL+γ fitting 待 s123 eval 完成后执行，结果可能更新 calibration 数据\n\n### 5.4 Signal Failure\n- [ ] **P1** 当前 signal failure 数据来自 ≤3B Qwen。如有 7B-14.7B signal 数据可加一句跨规模确认\n\n### 5.5 Domain-Level Analysis\n- [ ] **P1** 当前 domain analysis 仅在 Qwen ≤3B。Cross-family domain decomposition（D166, STEM resilient / Social Sci sensitive）已有 Appendix 内容。确认 Appendix 文字与数据一致\n\n### GSM8K（新增子节或加入现有框架）\n- [ ] **P0** GSM8K eval 完成后：加入 Results 作为 negative control。选项：(a) 新子节 \"5.X GSM8K: Format-Dependent Vulnerability\"，(b) 整合入 5.1 作为 paragraph。建议 (b) 省空间——在 baseline threshold 段加一段 \"GSM8K (open-ended) shows near-zero contamination effect across all families, confirming that dose-response profiles are benchmark-conditioned\"\n- [ ] **P1** 如 GSM8K 有 family-specific 差异（如某 family 在 GSM8K 上也有变化），需要额外讨论\n\n## Section: Discussion and Conclusion (conclusion.tex)\n\n- [ ] **P0** ¶1 \"Five patterns, not one\"：更新 V-recovery 描述。当前已有 \"consistent across benchmarks\" 但未提双种子确认。加 \"V-recovery is confirmed across two seeds with varying recovery extent\"\n- [ ] **P0** 如 GSM8K 结果显著，加一段 benchmark-conditionality 讨论（当前 discussion 未显式讨论 GSM8K negative control 的含义）\n- [ ] **P1** DiD 段：当前 ¶1 已提 \"Item-level DiD analysis shows these patterns arise from global capability modulation\"。如有新数据（s123 DiD）可加强\n- [ ] **P1** Domain decomposition 讨论：当前 ¶3 提 domain analysis。如 STEM-resilient / Social-Sci-sensitive 数据已在 Appendix，加一句具体数据引用\n\n## Section: Limitations (limitations.tex)\n\n- [ ] **P0** \"Single seed\" 段落更新：当前写 \"confirmed across two seeds (s42, s123)\"。如 s0 完成前提交，保持此表述。如 s0 完成，改为 \"triple-seed validated\"\n- [ ] **P0** 如 GSM8K eval 完成但仅 d000+d100 两个端点，在 limitations 加 \"GSM8K evaluated at endpoint dosages only (d000, d100); intermediate dosage profiles not characterized\"\n- [ ] **P1** Prompt format sensitivity 段（当前最后一段）：已提 \"pattern shapes may vary with prompt format\"——确认与 D154b 一致，OK\n- [ ] **P1** 考虑加 \"Benefit models (OLMo-2, Gemma-2) may exhibit different behavior under pretraining contamination vs SFT injection\" 以呼应 DiD global-modulation finding\n\n## Section: Ethics (ethics.tex)\n\n- [ ] **P1** 当前已完整覆盖。无需更新，除非 GSM8K 引入新 benchmark 需提及（已在 list 中）\n\n## Section: Appendix (appendix.tex)\n\n### Existing appendix sections（确认数据一致性）\n- [ ] **P0** Appendix A (ARC Cross-Benchmark): 确认与 s42 aligned eval 数据一致\n- [ ] **P0** Appendix K (Sensitivity): 确认 30/30 → 180/180 更新。当前写 \"30 (τ,σ) combinations\"，但 D164/Algorithm v2 报告 180/180 (6 families × 30 combos)。需更新描述或确认 30/30 是 per-family\n\n### 新增 appendix 内容\n- [ ] **P0** Domain decomposition 完整数据表：Appendix L (sec:domain_decomposition) 已有定性描述 + 数据。确认 STEM 2.8pp / Social Sci 5.1pp 数据已在文中\n- [ ] **P1** GSM8K 详细结果表（eval 完成后）：per-family GSM8K accuracy at d000/d100\n- [ ] **P1** V-recovery 双种子对比图：s42 vs s123 trajectory overlay（已有数据可直接生成）\n- [ ] **P1** Fisher Information 推导：framing 提到 \"must derive I(γ) for appendix\"。如来得及，加入推导\n\n## Section: Figures\n\n- [ ] **P0** Fig 1 (dose-response): 确认当前 fig_dose_response.pdf 使用 s42 aligned eval 数据（非旧 eval 版本）\n- [ ] **P0** Fig 2 (treated/untreated DiD): 确认使用 aligned eval 数据\n- [ ] **P1** 如加 GSM8K 结果：可在 Fig 1 加 subplot 或在 appendix 加单独图\n- [ ] **P1** 如加 s123 数据：考虑在 appendix 加 s123 dose-response overlay 图\n- [ ] **P1** Baseline vs effect scatter (fig_baseline_vs_effect.pdf): 确认已是 aligned eval 数据\n\n## Section: References\n\n- [ ] **P1** 确认所有已引用论文的 bib 条目完整（特别是 han2026quantifying, schaeffer2026causally 等 2026 引用）\n- [ ] **P1** 检查是否遗漏 framing 中要求的引用（DIF literature, conformal prediction 等——部分为 appendix/future work 引用）\n\n---\n\n## Priority Summary\n\n**P0 (must have for submission, ~15 items)**:\n1. V-recovery 双种子确认整合到 abstract + results Table 1 + discussion\n2. Algorithm 1 v2 一致性验证（method 伪代码 vs profile_classifier.py）\n3. GSM8K 结果整合（待 eval 完成）\n4. Experimental setup seed/checkpoint 数更新\n5. Figure 数据一致性验证（aligned eval）\n6. Sensitivity 描述更新（30→180）\n7. Limitations seed 段更新\n8. DiD 数据版本确认\n\n**P1 (nice to have, ~20 items)**:\n1. s123 cross-family 数据更新（Table 1 扩展）\n2. GSM8K 在各 section 的引用\n3. Domain decomposition appendix 完善\n4. Related work 呼应句\n5. Fisher Information 推导\n6. V-recovery 双种子对比图\n7. Reference audit\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01C9kbrzeSf6tuc6WLJu24cM`</summary>

```json
{
  "name": "paper_update_checklist",
  "type": "report",
  "description": "EMNLP 2026 论文更新清单：覆盖所有 section 的 P0/P1 改动项，基于 D165 V-recovery 双种子确认、Algorithm v2、DiD、domain decomposition、GSM8K pending 等近期发现",
  "project": "contamcal-irt-calibration",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_update_checklist.md",
  "tags": [
    "paper",
    "checklist",
    "emnlp2026"
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
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "6b506cb9-f102-40a6-914c-12f0d96aa306",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tbh1Q6tJzyw3uypgJkwXDZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3834,
      "cache_read_input_tokens": 70416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3834
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

_source line 58 · 2026-05-19T22:08:07.861Z_

<details><summary>↩ Tool result · `toolu_01C9kbrzeSf6tuc6WLJu24cM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_319ca1\", \"name\": \"paper_update_checklist\", \"type\": \"report\", \"description\": \"EMNLP 2026 论文更新清单：覆盖所有 section 的 P0/P1 改动项，基于 D165 V-recovery 双种子确认、Algorithm v2、DiD、domain decomposition、GSM8K pending 等近期发现\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/report/paper_update_checklist.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T22:08:07.618186+00:00\", \"tags\": [\"paper\", \"checklist\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "928afd9c-ff20-4de2-ae06-d661b74913bc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260519_319ca1\\\", \\\"name\\\": \\\"paper_update_checklist\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"EMNLP 2026 论文更新清单：覆盖所有 section 的 P0/P1 改动项，基于 D165 V-recovery 双种子确认、Algorithm v2、DiD、domain decomposition、GSM8K pending 等近期发现\\\", \\\"path\\\": \\\"projects/contamcal-irt-calibration/artifacts/_project/report/paper_update_checklist.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-19T22:08:07.618186+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"checklist\\\", \\\"emnlp2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_319ca1\", \"name\": \"paper_update_checklist\", \"type\": \"report\", \"description\": \"EMNLP 2026 论文更新清单：覆盖所有 section 的 P0/P1 改动项，基于 D165 V-recovery 双种子确认、Algorithm v2、DiD、domain decomposition、GSM8K pending 等近期发现\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/report/paper_update_checklist.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T22:08:07.618186+00:00\", \"tags\": [\"paper\", \"checklist\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

已生成并注册。

**清单概要**：~35 项改动，覆盖 abstract 到 appendix 全部 section。

**P0（15 项，提交前必须完成）**：
- V-recovery 双种子确认 → abstract、Table 1、discussion 三处同步更新
- GSM8K 结果整合（待 eval）→ results 加 negative control 段 + abstract 一句
- Algorithm 1 v2 伪代码与 profile_classifier.py 一致性验证
- experimental_setup seed/checkpoint 数更新
- 所有 Figure 数据源确认（aligned evaluate.py 版本）
- Sensitivity 描述 30→180 更新
- DiD 数据版本确认

**P1（20 项，锦上添花）**：s123 cross-family 数据扩展、domain decomposition 图表、Fisher Info 推导、reference audit 等。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "uuid": "ca0ae594-e996-496b-988d-d94a5529f17a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mni2ZpuURjtUb3cWYycthd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 74250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
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

_source line 60_

已生成并注册。

**清单概要**：~35 项改动，覆盖 abstract 到 appendix 全部 section。

**P0（15 项，提交前必须完成）**：
- V-recovery 双种子确认 → abstract、Table 1、discussion 三处同步更新
- GSM8K 结果整合（待 eval）→ results 加 negative control 段 + abstract 一句
- Algorithm 1 v2 伪代码与 profile_classifier.py 一致性验证
- experimental_setup seed/checkpoint 数更新
- 所有 Figure 数据源确认（aligned evaluate.py 版本）
- Sensitivity 描述 30→180 更新
- DiD 数据版本确认

**P1（20 项，锦上添花）**：s123 cross-family 数据扩展、domain decomposition 图表、Fisher Info 推导、reference audit 等。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 136928,
  "duration_api_ms": 137633,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "a5c03f91-b74d-4adf-8c20-b068868935a9",
  "total_cost_usd": 0.77071825,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 63029,
    "cache_read_input_tokens": 424190,
    "output_tokens": 6467,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 63029,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 253,
        "cache_read_input_tokens": 74250,
        "cache_creation_input_tokens": 620,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 620
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2857,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002952,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 6467,
      "cacheReadInputTokens": 424190,
      "cacheCreationInputTokens": 63029,
      "webSearchRequests": 0,
      "costUSD": 0.76776625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5d30b42f-0264-4993-ba01-8a83f2640a66"
}
```

</details>

---
