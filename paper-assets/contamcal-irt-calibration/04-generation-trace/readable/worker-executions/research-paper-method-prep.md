# research paper method prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_research_paper-method-prep_20260516T165433.log`
- **Structured JSON:** [`5311ad07cc27a5593671.json`](../../sessions/53/5311ad07cc27a5593671.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
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
  "uuid": "66434ace-54d1-406a-a277-b4d9d637c70f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1778961000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "da36ff4d-4764-4a4b-8b1f-9cdcc7d5d747",
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to prepare Method section materials for their paper. Let me follow the steps outlined:

1. Read paper_framing.md
2. Read writing_plan.yaml
3. Read memory.md
4. Read ROADMAP.md
5. Synthesize into method_notes.md
6. Write to artifacts/
7. Register the artifact

Let me start by reading the project files using the MCP tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "92e1d705-118e-4488-b949-99fa96138d3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te91HGxumna3yQ7pNBwYPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12752,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12752
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

读取项目文件来整理 Method 章节素材。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "4ec28957-a83b-4ee8-a1ba-5ca5e3f60bbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te91HGxumna3yQ7pNBwYPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12752,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12752
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KENXJ6y3VPxhzwB8gGdUzm`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact",
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
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "d48bd0a2-31a8-4670-9bc9-d1cbd9d2245d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te91HGxumna3yQ7pNBwYPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12752,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12752
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

_source line 7 · 2026-05-16T16:54:44.859Z_

<details><summary>↩ Tool result · `toolu_01KENXJ6y3VPxhzwB8gGdUzm`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "d58bf518-9a58-4448-9dea-bcdb37de0cc3",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the project files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "d2beef13-1116-4d70-bfc1-060e1a010532",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XuZCTXQSMPxsXzmc7ysKJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SmnoGeyaDLhii5gdQSYXeS`</summary>

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
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "6fdd59d4-5cf9-4ed6-9e61-486c99ad1046",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XuZCTXQSMPxsXzmc7ysKJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
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

_source line 10 · 2026-05-16T16:54:48.396Z_

<details><summary>↩ Tool result · `toolu_01SmnoGeyaDLhii5gdQSYXeS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight (D039 pivot + D108/D115 domain heterogeneity — N=24 confirmed)\\nBenchmark contamination effects are far more complex than \\\"scores go up.\\\" Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks STEM-gradient pattern where factual-knowledge domains show strong positive γ while non-STEM domains exhibit model misfit), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\n\\n## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)\\n\\n1. **Characterization Claim (PRIMARY — D108/D115: domain heterogeneity confirmed at N=24)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks a clear STEM gradient. **N=24 confirmed results (D115)**:\\n   - STEM_Math: γ=+0.969, CI excludes 0, PPP=0.438 ✓ (strong positive — contamination inflates factual recall)\\n   - STEM_Science: γ=+0.838, CI excludes 0, PPP=0.807 ✓ (strong positive)\\n   - STEM_CS_Eng: γ=+0.197, CI includes 0, PPP=0.892 ✓ (null — procedural/applied knowledge less affected)\\n   - Non-STEM (Medical, Humanities, Social_Sciences, Business_Law): all PPP≈1.0 → 2PL+γ model structurally misspecified. Negative γ estimates (-0.17 to -0.50) reflect model assumption failure, not true contamination direction.\\n   - \\\"Other\\\" domain: system crash (disk/cgroup), non-essential catch-all category.\\n   **Interpretation**: Contamination susceptibility maps to factual knowledge density — domains rich in memorizable facts (Math, Science) show large positive γ (SFT exposure → recall boost → inflated scores). Procedural/applied domains (CS_Eng) show weaker effect. Non-STEM domains require richer models (multidimensional IRT or domain-specific covariates) — reported as acknowledged limitation and future work.\\n   **Paper claim scope**: Domain heterogeneity is established via (a) Simpson's paradox (aggregate ≈ 0, domain-level ≠ 0), (b) STEM gradient with good model fit (3/8 domains with PPP∈[0.1,0.9]), (c) non-STEM misfit as structural boundary of 2PL+γ. Claims based on domains with acceptable PPP ONLY. Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant \\\"contamination = uniform inflation\\\" narrative. Cross-family consistency with Llama-3.2-3B (pending eval completion) tests whether contamination susceptibility is a benchmark × domain property, not a model family artifact.\\n   **PPP presentation strategy**: Non-STEM PPP=1.0 is not a failure of the analysis but a meaningful boundary finding: 2PL+γ (additive contamination effect on unidimensional ability) captures STEM domain mechanics but not non-STEM. Discuss connection to multidimensional IRT (Reckase 2009) and DIF literature (Holland & Wainer 1993). Consider limited-information fit indices (M2*, RMSEA2) as robustness check for STEM results.\\n\\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\\n   **C2 contingency**: \\\"Scale-dependent\\\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \\\"method-specific signal effectiveness.\\\" Min-K++ reversal remains novel regardless.\\n\\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \\\"impossibility,\\\" not merely \\\"IRT needs more data.\\\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\\n\\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates (ARC MAE=0.035). Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion (D039 dream recommendation): γ significant AND PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. GSM8K overcorrection (MAE 11× worse than raw) is an honest negative result demonstrating the gating criterion's necessity.\\n\\n## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)\\n\\n### Core (characterization-led; calibration conditional)\\n1. **Domain-dependent contamination characterization** via IRT γ_k: Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity maps to factual knowledge density. Non-STEM model misfit as boundary finding (2PL+γ scope limitation)\\n2. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy empirical finding (D025 + D039 dream 三档一致). Systematic signal × scale × dosage AUC mapping. Honest reporting that RRF = S1-only in practice\\n3. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight. Strongest theoretical contribution (D025 + D039 一致)\\n\\n### Supporting\\n4. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\\n5. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection (internal) + ecological RL (external)\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\n- **Our framing (D039 pivot)**: ContamCal is a diagnostic framework that uses IRT to systematically characterize how contamination affects benchmark scores. Rather than claiming to \\\"fix\\\" contaminated scores, we reveal the structure of contamination effects — they are bidirectional, scale-dependent, and benchmark-specific — and establish the conditions under which statistical calibration is and isn't feasible. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 structural adaptations: (a) independent examinees → single model with joint item distribution, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability.\\n- **Headline result template (D039 — characterization-led)**: \\\"Contamination effects are benchmark-dependent: IRT γ captures forgetting on ARC (γ={X}, CI excludes zero) and inflation on GSM8K (γ={Y}), with scale modulation from catastrophic (-{Z}pp at 0.5B) to negligible at 7B. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = {W}), making single-signal contamination detection unreliable. Fisher Information analysis establishes that reliable γ recovery requires N≥50 models; recovery succeeded down to AUC=0.55 (lowest tested), with the lower bound remaining open — conditions rarely met in current LLM evaluation.\\\"\\n\\n## Venue Fit Risks\\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \\\"new algorithm\\\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \\\"calibration is only as good as its inputs.\\\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\\n\\n## Anticipated Reviewer Concerns & Defenses\\n\\n| # | Concern | Defense | Experiment |\\n|---|---------|---------|------------|\\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \\\"best-available proxy\\\", acknowledged as limitation | exp-006, exp-009 |\\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \\\"S1+IRT calibration with extensible multi-signal architecture for future signals.\\\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\\n| 20 | GSM8K overcorrection — calibration 11× worse than raw (D039, all 3 dream tiers) | Honest negative result. Implement calibration gating: γ significant AND PPP ∈ [0.1,0.9] AND calibrated MAE < raw MAE. Report raw scores when gating fails. Reframe: ContamCal identifies when NOT to calibrate. | exp-006 |\\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\\n\\n## Evaluation Protocol (6 Metrics — D025 added SBC)\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\\n\\n## Benchmarks (2 main + 2 contrasts)\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \\\"benchmark-dependent contamination effects\\\" — ContamCal calibrates in both directions.\\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \\\"ContamCal identifies benchmarks not requiring calibration\\\")\\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\\n\\n## Baselines (7)\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\n\\n## Local Independence Discussion\\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\\n\\n## Required Figures (Dream D2: \\\"zero figures\\\" flagged as serious deficiency)\\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\\n\\n## Citation Requirements (35+ minimum, expanded per Dream D2)\\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\\nDream D2 additions (all 3 tiers flagged):\\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \\\"calibration\\\" — ours is decontamination, not probability calibration)\\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\\nD025 additions (all 3 Dream tiers flagged):\\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\\n\\n## Discussion Notes\\n\\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\\n- **Paper treatment**: Report in Discussion as \\\"capacity threshold for reliable MC evaluation.\\\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\\n\\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\\n\", \"total_chars\": 24098, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "c60fcdc7-c754-4888-aca0-212f8f60a515",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — contamcal-irt-calibration\\\\n\\\\n## Target Venue\\\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\\\n- Track: Machine Learning for NLP / Resources and Evaluation\\\\n- Aligns with EMNLP 2026 special theme \\\\\\\"New Missions for NLP Research\\\\\\\" (explicitly invites contamination/data governance work)\\\\n\\\\n## Core Insight (D039 pivot + D108/D115 domain heterogeneity — N=24 confirmed)\\\\nBenchmark contamination effects are far more complex than \\\\\\\"scores go up.\\\\\\\" Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks STEM-gradient pattern where factual-knowledge domains show strong positive γ while non-STEM domains exhibit model misfit), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\\\n\\\\n## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)\\\\n\\\\n1. **Characterization Claim (PRIMARY — D108/D115: domain heterogeneity confirmed at N=24)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks a clear STEM gradient. **N=24 confirmed results (D115)**:\\\\n   - STEM_Math: γ=+0.969, CI excludes 0, PPP=0.438 ✓ (strong positive — contamination inflates factual recall)\\\\n   - STEM_Science: γ=+0.838, CI excludes 0, PPP=0.807 ✓ (strong positive)\\\\n   - STEM_CS_Eng: γ=+0.197, CI includes 0, PPP=0.892 ✓ (null — procedural/applied knowledge less affected)\\\\n   - Non-STEM (Medical, Humanities, Social_Sciences, Business_Law): all PPP≈1.0 → 2PL+γ model structurally misspecified. Negative γ estimates (-0.17 to -0.50) reflect model assumption failure, not true contamination direction.\\\\n   - \\\\\\\"Other\\\\\\\" domain: system crash (disk/cgroup), non-essential catch-all category.\\\\n   **Interpretation**: Contamination susceptibility maps to factual knowledge density — domains rich in memorizable facts (Math, Science) show large positive γ (SFT exposure → recall boost → inflated scores). Procedural/applied domains (CS_Eng) show weaker effect. Non-STEM domains require richer models (multidimensional IRT or domain-specific covariates) — reported as acknowledged limitation and future work.\\\\n   **Paper claim scope**: Domain heterogeneity is established via (a) Simpson's paradox (aggregate ≈ 0, domain-level ≠ 0), (b) STEM gradient with good model fit (3/8 domains with PPP∈[0.1,0.9]), (c) non-STEM misfit as structural boundary of 2PL+γ. Claims based on domains with acceptable PPP ONLY. Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant \\\\\\\"contamination = uniform inflation\\\\\\\" narrative. Cross-family consistency with Llama-3.2-3B (pending eval completion) tests whether contamination susceptibility is a benchmark × domain property, not a model family artifact.\\\\n   **PPP presentation strategy**: Non-STEM PPP=1.0 is not a failure of the analysis but a meaningful boundary finding: 2PL+γ (additive contamination effect on unidimensional ability) captures STEM domain mechanics but not non-STEM. Discuss connection to multidimensional IRT (Reckase 2009) and DIF literature (Holland & Wainer 1993). Consider limited-information fit indices (M2*, RMSEA2) as robustness check for STEM results.\\\\n\\\\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\\\\n   **C2 contingency**: \\\\\\\"Scale-dependent\\\\\\\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \\\\\\\"method-specific signal effectiveness.\\\\\\\" Min-K++ reversal remains novel regardless.\\\\n\\\\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \\\\\\\"impossibility,\\\\\\\" not merely \\\\\\\"IRT needs more data.\\\\\\\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\\\\n\\\\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates (ARC MAE=0.035). Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion (D039 dream recommendation): γ significant AND PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. GSM8K overcorrection (MAE 11× worse than raw) is an honest negative result demonstrating the gating criterion's necessity.\\\\n\\\\n## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)\\\\n\\\\n### Core (characterization-led; calibration conditional)\\\\n1. **Domain-dependent contamination characterization** via IRT γ_k: Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity maps to factual knowledge density. Non-STEM model misfit as boundary finding (2PL+γ scope limitation)\\\\n2. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy empirical finding (D025 + D039 dream 三档一致). Systematic signal × scale × dosage AUC mapping. Honest reporting that RRF = S1-only in practice\\\\n3. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight. Strongest theoretical contribution (D025 + D039 一致)\\\\n\\\\n### Supporting\\\\n4. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\\\\n5. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection (internal) + ecological RL (external)\\\\n\\\\n## Story Spine\\\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \\\\\\\"what would this model's score be if it had never seen the test data?\\\\\\\"\\\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\\\n- **Our framing (D039 pivot)**: ContamCal is a diagnostic framework that uses IRT to systematically characterize how contamination affects benchmark scores. Rather than claiming to \\\\\\\"fix\\\\\\\" contaminated scores, we reveal the structure of contamination effects — they are bidirectional, scale-dependent, and benchmark-specific — and establish the conditions under which statistical calibration is and isn't feasible. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 structural adaptations: (a) independent examinees → single model with joint item distribution, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability.\\\\n- **Headline result template (D039 — characterization-led)**: \\\\\\\"Contamination effects are benchmark-dependent: IRT γ captures forgetting on ARC (γ={X}, CI excludes zero) and inflation on GSM8K (γ={Y}), with scale modulation from catastrophic (-{Z}pp at 0.5B) to negligible at 7B. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = {W}), making single-signal contamination detection unreliable. Fisher Information analysis establishes that reliable γ recovery requires N≥50 models; recovery succeeded down to AUC=0.55 (lowest tested), with the lower bound remaining open — conditions rarely met in current LLM evaluation.\\\\\\\"\\\\n\\\\n## Venue Fit Risks\\\\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\\\\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\\\\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \\\\\\\"new algorithm\\\\\\\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\\\\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \\\\\\\"calibration is only as good as its inputs.\\\\\\\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\\\\n\\\\n## Anticipated Reviewer Concerns & Defenses\\\\n\\\\n| # | Concern | Defense | Experiment |\\\\n|---|---------|---------|------------|\\\\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\\\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\\\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \\\\\\\"best-available proxy\\\\\\\", acknowledged as limitation | exp-006, exp-009 |\\\\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\\\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\\\\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\\\\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\\\\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\\\\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\\\\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\\\\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\\\\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\\\\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\\\\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\\\\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\\\\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\\\\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\\\\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \\\\\\\"S1+IRT calibration with extensible multi-signal architecture for future signals.\\\\\\\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\\\\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\\\\n| 20 | GSM8K overcorrection — calibration 11× worse than raw (D039, all 3 dream tiers) | Honest negative result. Implement calibration gating: γ significant AND PPP ∈ [0.1,0.9] AND calibrated MAE < raw MAE. Report raw scores when gating fails. Reframe: ContamCal identifies when NOT to calibrate. | exp-006 |\\\\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\\\\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\\\\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\\\\n\\\\n## Evaluation Protocol (6 Metrics — D025 added SBC)\\\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\\\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\\\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\\\\n\\\\n## Benchmarks (2 main + 2 contrasts)\\\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\\\\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \\\\\\\"benchmark-dependent contamination effects\\\\\\\" — ContamCal calibrates in both directions.\\\\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \\\\\\\"ContamCal identifies benchmarks not requiring calibration\\\\\\\")\\\\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\\\\n\\\\n## Baselines (7)\\\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\\\n\\\\n## Local Independence Discussion\\\\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\\\\n\\\\n## Required Figures (Dream D2: \\\\\\\"zero figures\\\\\\\" flagged as serious deficiency)\\\\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\\\\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\\\\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\\\\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\\\\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\\\\n\\\\n## Citation Requirements (35+ minimum, expanded per Dream D2)\\\\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\\\\nDream D2 additions (all 3 tiers flagged):\\\\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\\\\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \\\\\\\"calibration\\\\\\\" — ours is decontamination, not probability calibration)\\\\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\\\\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\\\\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\\\\nD025 additions (all 3 Dream tiers flagged):\\\\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\\\\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\\\\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\\\\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\\\\n\\\\n## Discussion Notes\\\\n\\\\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\\\\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\\\\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\\\\n- **Paper treatment**: Report in Discussion as \\\\\\\"capacity threshold for reliable MC evaluation.\\\\\\\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\\\\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\\\\n\\\\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\\\\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\\\\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\\\\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\\\\n\\\", \\\"total_chars\\\": 24098, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight (D039 pivot + D108/D115 domain heterogeneity — N=24 confirmed)\\nBenchmark contamination effects are far more complex than \\\"scores go up.\\\" Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks STEM-gradient pattern where factual-knowledge domains show strong positive γ while non-STEM domains exhibit model misfit), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\n\\n## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)\\n\\n1. **Characterization Claim (PRIMARY — D108/D115: domain heterogeneity confirmed at N=24)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks a clear STEM gradient. **N=24 confirmed results (D115)**:\\n   - STEM_Math: γ=+0.969, CI excludes 0, PPP=0.438 ✓ (strong positive — contamination inflates factual recall)\\n   - STEM_Science: γ=+0.838, CI excludes 0, PPP=0.807 ✓ (strong positive)\\n   - STEM_CS_Eng: γ=+0.197, CI includes 0, PPP=0.892 ✓ (null — procedural/applied knowledge less affected)\\n   - Non-STEM (Medical, Humanities, Social_Sciences, Business_Law): all PPP≈1.0 → 2PL+γ model structurally misspecified. Negative γ estimates (-0.17 to -0.50) reflect model assumption failure, not true contamination direction.\\n   - \\\"Other\\\" domain: system crash (disk/cgroup), non-essential catch-all category.\\n   **Interpretation**: Contamination susceptibility maps to factual knowledge density — domains rich in memorizable facts (Math, Science) show large positive γ (SFT exposure → recall boost → inflated scores). Procedural/applied domains (CS_Eng) show weaker effect. Non-STEM domains require richer models (multidimensional IRT or domain-specific covariates) — reported as acknowledged limitation and future work.\\n   **Paper claim scope**: Domain heterogeneity is established via (a) Simpson's paradox (aggregate ≈ 0, domain-level ≠ 0), (b) STEM gradient with good model fit (3/8 domains with PPP∈[0.1,0.9]), (c) non-STEM misfit as structural boundary of 2PL+γ. Claims based on domains with acceptable PPP ONLY. Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant \\\"contamination = uniform inflation\\\" narrative. Cross-family consistency with Llama-3.2-3B (pending eval completion) tests whether contamination susceptibility is a benchmark × domain property, not a model family artifact.\\n   **PPP presentation strategy**: Non-STEM PPP=1.0 is not a failure of the analysis but a meaningful boundary finding: 2PL+γ (additive contamination effect on unidimensional ability) captures STEM domain mechanics but not non-STEM. Discuss connection to multidimensional IRT (Reckase 2009) and DIF literature (Holland & Wainer 1993). Consider limited-information fit indices (M2*, RMSEA2) as robustness check for STEM results.\\n\\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\\n   **C2 contingency**: \\\"Scale-dependent\\\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \\\"method-specific signal effectiveness.\\\" Min-K++ reversal remains novel regardless.\\n\\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \\\"impossibility,\\\" not merely \\\"IRT needs more data.\\\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\\n\\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates (ARC MAE=0.035). Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion (D039 dream recommendation): γ significant AND PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. GSM8K overcorrection (MAE 11× worse than raw) is an honest negative result demonstrating the gating criterion's necessity.\\n\\n## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)\\n\\n### Core (characterization-led; calibration conditional)\\n1. **Domain-dependent contamination characterization** via IRT γ_k: Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity maps to factual knowledge density. Non-STEM model misfit as boundary finding (2PL+γ scope limitation)\\n2. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy empirical finding (D025 + D039 dream 三档一致). Systematic signal × scale × dosage AUC mapping. Honest reporting that RRF = S1-only in practice\\n3. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight. Strongest theoretical contribution (D025 + D039 一致)\\n\\n### Supporting\\n4. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\\n5. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection (internal) + ecological RL (external)\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\n- **Our framing (D039 pivot)**: ContamCal is a diagnostic framework that uses IRT to systematically characterize how contamination affects benchmark scores. Rather than claiming to \\\"fix\\\" contaminated scores, we reveal the structure of contamination effects — they are bidirectional, scale-dependent, and benchmark-specific — and establish the conditions under which statistical calibration is and isn't feasible. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 structural adaptations: (a) independent examinees → single model with joint item distribution, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability.\\n- **Headline result template (D039 — characterization-led)**: \\\"Contamination effects are benchmark-dependent: IRT γ captures forgetting on ARC (γ={X}, CI excludes zero) and inflation on GSM8K (γ={Y}), with scale modulation from catastrophic (-{Z}pp at 0.5B) to negligible at 7B. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = {W}), making single-signal contamination detection unreliable. Fisher Information analysis establishes that reliable γ recovery requires N≥50 models; recovery succeeded down to AUC=0.55 (lowest tested), with the lower bound remaining open — conditions rarely met in current LLM evaluation.\\\"\\n\\n## Venue Fit Risks\\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \\\"new algorithm\\\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \\\"calibration is only as good as its inputs.\\\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\\n\\n## Anticipated Reviewer Concerns & Defenses\\n\\n| # | Concern | Defense | Experiment |\\n|---|---------|---------|------------|\\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \\\"best-available proxy\\\", acknowledged as limitation | exp-006, exp-009 |\\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \\\"S1+IRT calibration with extensible multi-signal architecture for future signals.\\\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\\n| 20 | GSM8K overcorrection — calibration 11× worse than raw (D039, all 3 dream tiers) | Honest negative result. Implement calibration gating: γ significant AND PPP ∈ [0.1,0.9] AND calibrated MAE < raw MAE. Report raw scores when gating fails. Reframe: ContamCal identifies when NOT to calibrate. | exp-006 |\\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\\n\\n## Evaluation Protocol (6 Metrics — D025 added SBC)\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\\n\\n## Benchmarks (2 main + 2 contrasts)\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \\\"benchmark-dependent contamination effects\\\" — ContamCal calibrates in both directions.\\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \\\"ContamCal identifies benchmarks not requiring calibration\\\")\\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\\n\\n## Baselines (7)\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\n\\n## Local Independence Discussion\\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\\n\\n## Required Figures (Dream D2: \\\"zero figures\\\" flagged as serious deficiency)\\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\\n\\n## Citation Requirements (35+ minimum, expanded per Dream D2)\\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\\nDream D2 additions (all 3 tiers flagged):\\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \\\"calibration\\\" — ours is decontamination, not probability calibration)\\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\\nD025 additions (all 3 Dream tiers flagged):\\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\\n\\n## Discussion Notes\\n\\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\\n- **Paper treatment**: Report in Discussion as \\\"capacity threshold for reliable MC evaluation.\\\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\\n\\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\\n\", \"total_chars\": 24098, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ce6FwgH6eLhPFS2jM5d7ct`</summary>

```json
{
  "project": "contamcal-irt-calibration",
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
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "e53f8cc1-0d69-4f06-88fb-5b21c60f91de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XuZCTXQSMPxsXzmc7ysKJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
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

_source line 12 · 2026-05-16T16:54:49.372Z_

<details><summary>↩ Tool result · `toolu_01Ce6FwgH6eLhPFS2jM5d7ct`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/writing_plan.yaml\", \"content\": \"## writing_plan.yaml — contamcal-irt-calibration\\n## Generated: 2026-05-15 | Paper Agent Step 1\\n## Status: APPROVED (Director 2026-05-15)\\n\\nmeta:\\n  venue: \\\"EMNLP 2026 ARR May 25\\\"\\n  track: \\\"Machine Learning for NLP / Resources and Evaluation\\\"\\n  deadline: \\\"2026-05-25\\\"\\n  page_limit: 8  # + unlimited appendix\\n  template: \\\"acl_latex (ARR format)\\\"\\n  template_note: \\\"No local EMNLP 2026 template found; use acl-style-files from github.com/acl-org/acl-style-files. Worker should download latest.\\\"\\n  special_theme: \\\"New Missions for NLP Research\\\"\\n  framing_doc: \\\"paper_framing.md (D039 pivot: characterization-led)\\\"\\n  total_word_budget: 5800  # main text excluding references\\n\\ntitle: >\\n  ContamCal: Characterizing Benchmark-Dependent Contamination Effects\\n  via Contamination-Augmented Item Response Theory\\n\\ncore_claims:\\n  C1:\\n    name: \\\"Characterization (PRIMARY)\\\"\\n    summary: \\\"Contamination effects are benchmark-dependent (ARC γ<0, GSM8K γ>0) and scale-dependent (catastrophic at 0.5B, mild at 3B). Per-benchmark γ_k captures bidirectional effects.\\\"\\n    evidence: [exp-001, exp-006]\\n    priority: 1\\n  C2:\\n    name: \\\"Signal Failure (CO-PRIMARY)\\\"\\n    summary: \\\"Min-K++ directional reversal (Cohen's d = -1.98 at 0.5B d100). S1 embedding is the only reliable signal (AUC>0.95 at d005). RRF degrades to S1-only in practice.\\\"\\n    evidence: [exp-008, exp-002, exp-003]\\n    priority: 1\\n  C3:\\n    name: \\\"Identifiability\\\"\\n    summary: \\\"Fisher Information analysis → recovery successful at AUC=0.55 (lowest tested, J≥50); lower bound open. LLM eval small cohorts create domain-method mismatch.\\\"\\n    evidence: [exp-004, mvp_sim_4pl_gamma]\\n    priority: 2\\n  C4:\\n    name: \\\"Conditional Calibration (DEMOTED)\\\"\\n    summary: \\\"Calibration works when model complexity matches benchmark + signal AUC sufficient. ARC MAE=0.035. GSM8K overcorrection as honest negative result. Gating criterion necessary.\\\"\\n    evidence: [exp-006]\\n    priority: 3\\n\\npaper_outline:\\n  abstract:\\n    word_budget: 200\\n    dependencies: [introduction, results, conclusion]\\n    key_numbers: [\\\"ARC γ=-1.46\\\", \\\"GSM8K γ=3.77 (oracle)\\\", \\\"Min-K++ Cohen's d=-1.98\\\", \\\"ARC MAE=0.035\\\", \\\"AUC=0.55 recovery (lowest tested)\\\"]\\n    notes: \\\"Write last. Characterization-led framing. 4 claims in priority order.\\\"\\n\\n  introduction:\\n    word_budget: 850\\n    dependencies: [method, results]\\n    subsections:\\n      - \\\"Problem: contamination undermines benchmark reliability\\\"\\n      - \\\"Gap: detection methods flag but don't calibrate; mitigation provably fails\\\"\\n      - \\\"Our approach: characterization framework via contamination-augmented IRT\\\"\\n      - \\\"3 core contributions (characterization, signal failure, identifiability) + conditional calibration\\\"\\n    notes: \\\"D039 pivot: lead with characterization, not calibration. Frame as diagnostic framework. Reference Emperor's New Clothes for motivation.\\\"\\n\\n  related_work:\\n    word_budget: 700\\n    dependencies: [literature_map]\\n    subsections:\\n      - \\\"Contamination detection (Min-K++, ConStat, KDS, CDD, Self-Critique)\\\"\\n      - \\\"IRT for LLM evaluation (Lalor, TinyBenchmarks, Growing Pains, HiBayES)\\\"\\n      - \\\"Item compromise in educational measurement (Eckerly, Sinharay, DIF)\\\"\\n      - \\\"Contamination mitigation and calibration disambiguation\\\"\\n    notes: \\\"Must disambiguate 'calibration' from probability calibration (Guo et al.) and conformal prediction.\\\"\\n\\n  method:\\n    word_budget: 1100\\n    dependencies: []\\n    subsections:\\n      - name: \\\"3.1 Problem Formulation\\\"\\n        content: \\\"Given model j, benchmark k with items i, observed response y_{ijk}. Goal: estimate θ_j^clean. Three IRT adaptations from educational measurement.\\\"\\n      - name: \\\"3.2 Stage 1: Multi-Signal Exposure Mapping\\\"\\n        content: \\\"4 signals (S1-S4), RRF aggregation. Meta-circularity argument for training-free fusion.\\\"\\n      - name: \\\"3.3 Stage 2: Contamination-Augmented IRT\\\"\\n        content: \\\"4PL+γ model: P(y=1) = c_i + (d_i - c_i) σ(a_i(θ_j - b_i) + γ_k·e_{ij}). Per-benchmark γ_k. Stan NUTS inference.\\\"\\n      - name: \\\"3.4 Fisher Information and Identifiability\\\"\\n        content: \\\"Derive I(γ) for 4PL+γ. Recovery boundaries from sim sweep (24 conditions, 240 runs). CI width ∝ N^{-0.48}. Domain-method mismatch.\\\"\\n    notes: \\\"Can be written first (no data dependency). Include measurement error model as optional extension. Full Fisher derivation in appendix.\\\"\\n\\n  experimental_setup:\\n    word_budget: 600\\n    dependencies: [method]\\n    subsections:\\n      - name: \\\"4.1 Controlled SFT Injection\\\"\\n        content: \\\"Qwen2.5 (0.5B, 1.5B, 3B). 4 dosages (d000/d005/d025/d100). 2 seeds. LoRA alpha=32. QC-filtered injection data.\\\"\\n      - name: \\\"4.2 Benchmarks and Evaluation Protocol\\\"\\n        content: \\\"ARC-Challenge (1172 items), GSM8K (1319), MMLU (14042, subsampled for IRT). 6 metrics. Aligned + paraphrased eval.\\\"\\n      - name: \\\"4.3 Baselines\\\"\\n        content: \\\"7 baselines: B0-Raw, B1-Remove&Rescore, B2-Single2PL+γ, B3-Vanilla4PL, B4-LinearRegression, B5-Emperor, B6-DCR.\\\"\\n    notes: \\\"D045: exclude 0.5B MMLU/ARC from IRT pooling (position bias). Retain 0.5B GSM8K. D060: scope to 0.5B+1.5B main, 3B as [PENDING-3B]. 7B/72B → future work.\\\"\\n\\n  results:\\n    word_budget: 1500\\n    dependencies: [experimental_setup, fig_signal_heatmap, fig_dose_response, fig_identifiability, fig_calibration, table_gamma, table_baselines]\\n    subsections:\\n      - name: \\\"5.1 Contamination Characterization\\\"\\n        content: \\\"Per-benchmark γ_k: ARC γ=-1.46 (forgetting), GSM8K γ=3.77 (oracle, inflation). Scale modulation: 0.5B catastrophic vs 1.5B mild. Dose-response curves. 3B [PENDING-3B].\\\"\\n        claims: [C1]\\n        key_tables: [table_gamma]\\n        key_figures: [fig_dose_response]\\n      - name: \\\"5.2 Detection Signal Analysis\\\"\\n        content: \\\"S1 AUC>0.95 at d005. S2 Min-K++ AUC~0.47, Cohen's d=-1.98 (reversal). S4 random. RRF = S1-only in practice.\\\"\\n        claims: [C2]\\n        key_tables: [table_signal_summary]\\n        key_figures: [fig_signal_heatmap]\\n      - name: \\\"5.3 Identifiability Boundaries\\\"\\n        content: \\\"Sim sweep (24 conditions, 240 runs): AUC=0.80 N=50 bias=0.006. AUC=0.55 J≥50 meets all criteria. AUC=0.65 systematically fails at small J. CI width ∝ N^{-0.48}. LLM eval small cohorts = structural mismatch.\\\"\\n        claims: [C3]\\n        key_figures: [fig_identifiability]\\n      - name: \\\"5.4 Conditional Calibration\\\"\\n        content: \\\"ARC 4PL+γ: MAE=0.035 (beats all baselines). Kendall τ=0.756. Coverage 62.5% (below nominal). GSM8K signal-derived γ non-significant → gating criterion triggers. GSM8K overcorrection MAE=0.092 vs raw 0.005 as honest negative. MMLU IRT fails (Rhat=1.54).\\\"\\n        claims: [C4]\\n        key_tables: [table_baselines]\\n        key_figures: [fig_calibration]\\n    notes: \\\"3B rows in all tables/figures marked [PENDING-3B]. Honest about negatives: GSM8K overcorrection, MMLU failure, coverage below nominal.\\\"\\n\\n  discussion:\\n    word_budget: 500\\n    dependencies: [results]\\n    subsections:\\n      - \\\"Limitations: single model family (Qwen2.5), SFT ≠ real contamination, N<50, coverage below nominal\\\"\\n      - \\\"0.5B position bias (D045): capacity threshold for MC evaluation\\\"\\n      - \\\"When NOT to calibrate: gating criterion and its implications\\\"\\n      - \\\"Future work: multi-family (Llama/Pythia), 7B+, RL observational, data attribution signals\\\"\\n    notes: \\\"Coverage collapse (D056) as model misspecification evidence. noise_prop negative result → appendix mention.\\\"\\n\\n  conclusion:\\n    word_budget: 350\\n    dependencies: [discussion]\\n    notes: \\\"Restate 4 claims compactly. Emphasize characterization > calibration. End with 'conditions under which calibration is feasible' framing.\\\"\\n\\n  appendix:\\n    sections:\\n      - name: \\\"A: Fisher Information Derivation\\\"\\n        source: \\\"artifacts/fisher_info_derivation/fisher_info_appendix.tex\\\"\\n        notes: \\\"Already drafted. Verify completeness.\\\"\\n      - name: \\\"B: Simulation Sweep Details\\\"\\n        data_source: \\\"exp-004\\\"\\n      - name: \\\"C: Measurement Error Analysis\\\"\\n        data_source: \\\"exp-005\\\"\\n        notes: \\\"Negative result. noise_prop_v4 CI insensitive to σ_e.\\\"\\n      - name: \\\"D: 0.5B Position Bias Analysis\\\"\\n        data_source: \\\"exp-001 (0.5B MMLU prediction distribution)\\\"\\n        notes: \\\"D045: MMLU prediction dist d000 A=46% → d100 A=98%.\\\"\\n      - name: \\\"E: HumanEval Results\\\"\\n        notes: \\\"Demoted from main (D009: 16% QC pass).\\\"\\n\\nvisualization_plan:\\n  fig_pipeline:\\n    type: \\\"conceptual_diagram\\\"\\n    description: \\\"ContamCal 2-stage pipeline overview. Left: 4 detection signals → RRF fusion → exposure scores. Right: exposure + responses → 4PL+γ IRT → calibrated scores with CIs. Show per-benchmark γ_k.\\\"\\n    placement: \\\"Section 3 (Method), top of page\\\"\\n    aspect_ratio: \\\"2:1 (wide)\\\"\\n    tool: \\\"matplotlib\\\"\\n    data_source: null  # conceptual, no data\\n    output: \\\"figures/paper/fig_pipeline.pdf\\\"\\n\\n  fig_dose_response:\\n    type: \\\"line_plot\\\"\\n    description: \\\"Dosage (x: d000, d005, d025, d100) vs benchmark accuracy (y) for each benchmark. Separate panels or lines for 0.5B, 1.5B, [PENDING-3B]. Show ARC forgetting vs GSM8K inflation. Error bars from 2 seeds.\\\"\\n    placement: \\\"Section 5.1\\\"\\n    aspect_ratio: \\\"3:2\\\"\\n    tool: \\\"matplotlib\\\"\\n    data_source: \\\"registry: exp-001 eval results (aligned format, all scales × dosages × seeds)\\\"\\n    output: \\\"figures/paper/fig_dose_response.pdf\\\"\\n\\n  fig_signal_heatmap:\\n    type: \\\"heatmap\\\"\\n    description: \\\"Signal AUC heatmap. Rows: 3 signals (S1 Embedding, S2 Min-K++, S4 Self-Critique) × 3 benchmarks. Columns: dosages (d005, d025). Separate panels for 0.5B and 1.5B. Annotate Cohen's d for d100 cross-model comparison. Highlight Min-K++ reversal cell in red.\\\"\\n    placement: \\\"Section 5.2\\\"\\n    aspect_ratio: \\\"4:3\\\"\\n    tool: \\\"matplotlib\\\"\\n    data_source: \\\"registry: exp-008 signal survival v1 + v4 (AUC + Cohen's d)\\\"\\n    output: \\\"figures/paper/fig_signal_heatmap.pdf\\\"\\n\\n  fig_identifiability:\\n    type: \\\"phase_diagram\\\"\\n    description: \\\"Identifiability boundaries. X: signal AUC. Y: N_models. Color/marker: γ recovery quality (bias, RMSE, CI coverage). Shade regions: successful recovery region (AUC≥0.55, all tested N≥20). Lower bound open. Mark actual LLM eval operating point (AUC~0.98, N=8-16).\\\"\\n    placement: \\\"Section 5.3\\\"\\n    aspect_ratio: \\\"1:1\\\"\\n    tool: \\\"matplotlib\\\"\\n    data_source: \\\"registry: exp-004 sim_sweep results (v5 completed conditions)\\\"\\n    output: \\\"figures/paper/fig_identifiability.pdf\\\"\\n\\n  fig_calibration:\\n    type: \\\"scatter_with_ci\\\"\\n    description: \\\"Calibrated score (x) vs true clean score (y) scatter. Each point = one model-benchmark. Horizontal bars = 95% CI. Diagonal = perfect calibration. Color by benchmark. Annotate ARC cluster (good) vs GSM8K cluster (overcorrection). Include B0 (raw) as hollow markers for comparison.\\\"\\n    placement: \\\"Section 5.4\\\"\\n    aspect_ratio: \\\"1:1\\\"\\n    tool: \\\"matplotlib\\\"\\n    data_source: \\\"registry: exp-006 IRT calibration results (ARC S1-only 4PL+γ, GSM8K 2PL+γ)\\\"\\n    output: \\\"figures/paper/fig_calibration.pdf\\\"\\n\\ntable_plan:\\n  table_gamma:\\n    type: \\\"parameter_summary\\\"\\n    description: \\\"Per-benchmark IRT γ estimates with diagnostics\\\"\\n    columns: [\\\"Benchmark\\\", \\\"Model\\\", \\\"γ̂\\\", \\\"95% CI\\\", \\\"Excludes 0?\\\", \\\"R̂\\\", \\\"ESS\\\", \\\"PPP\\\", \\\"Direction\\\"]\\n    data_source: \\\"exp-006 per-benchmark IRT fits\\\"\\n    placement: \\\"Section 5.1\\\"\\n    rows:\\n      - \\\"ARC (S1, 4PL+γ): γ=-1.46 [-2.51, -0.41] ✓ 1.010 770 TBD Forgetting\\\"\\n      - \\\"ARC (oracle, 2PL+γ): γ=-0.62 [-1.04, -0.20] ✓ 1.006 1512 TBD Forgetting\\\"\\n      - \\\"GSM8K (oracle, 4PL+γ): γ=3.77 [2.74, 4.71] ✓ 1.002 1222 TBD Inflation\\\"\\n      - \\\"GSM8K (S1, 2PL+γ): γ=0.14 [-0.31, 0.59] ✗ 1.002 3604 0.284 —\\\"\\n      - \\\"GSM8K (S1, 4PL+γ): γ=0.19 [-0.92, 1.33] ✗ 1.015 330 TBD — (convergence issue)\\\"\\n      - \\\"MMLU (RRF): FAILED (R̂=1.54, ESS=7)\\\"\\n      - \\\"[PENDING-3B] rows\\\"\\n\\n  table_baselines:\\n    type: \\\"comparison\\\"\\n    description: \\\"Calibration performance: ContamCal vs 7 baselines\\\"\\n    columns: [\\\"Method\\\", \\\"ARC MAE↓\\\", \\\"ARC τ↑\\\", \\\"ARC C95%\\\", \\\"GSM8K MAE↓\\\", \\\"GSM8K τ↑\\\"]\\n    data_source: \\\"exp-006 baseline comparisons\\\"\\n    placement: \\\"Section 5.4\\\"\\n    notes: \\\"ARC is success case. GSM8K shows gating criterion necessity. MMLU excluded (failed).\\\"\\n\\n  table_signal_summary:\\n    type: \\\"signal_evaluation\\\"\\n    description: \\\"Signal effectiveness by scale × benchmark\\\"\\n    columns: [\\\"Signal\\\", \\\"Scale\\\", \\\"d005 AUC\\\", \\\"d025 AUC\\\", \\\"d100 Cohen's d\\\"]\\n    data_source: \\\"exp-008\\\"\\n    placement: \\\"Section 5.2 or Appendix\\\"\\n    notes: \\\"May merge into fig_signal_heatmap. Keep as table if space allows.\\\"\\n\\nliterature_strategy:\\n  citation_budget: \\\"40-50 total\\\"\\n  macro_context: \\\"Contamination is a systemic threat; detection exists but calibration doesn't; educational measurement solved the analogous exam leak problem decades ago.\\\"\\n  micro_clusters:\\n    contamination_detection:\\n      target_count: 8\\n      must_cite: [\\\"zhang2024minkpp\\\", \\\"dekoninck2024constat\\\", \\\"dong2024kds\\\", \\\"shi2024cdd\\\", \\\"weller2024selfcritique\\\", \\\"golchin2024time\\\"]\\n      search_queries: [\\\"benchmark contamination detection LLM\\\", \\\"membership inference LLM evaluation\\\"]\\n    irt_for_llm:\\n      target_count: 6\\n      must_cite: [\\\"lalor2024aaai\\\", \\\"polo2024tinybenchmarks\\\", \\\"burnell2023multidimensional\\\"]\\n      search_queries: [\\\"item response theory large language model evaluation\\\", \\\"psychometric LLM benchmark\\\"]\\n    item_compromise_irt:\\n      target_count: 5\\n      must_cite: [\\\"eckerly2017\\\", \\\"sinharay2017\\\", \\\"deboeck2004\\\", \\\"holland1993dif\\\", \\\"adams1997\\\"]\\n      search_queries: [\\\"item compromise IRT detection\\\", \\\"differential item functioning preknowledge\\\"]\\n    benchmark_reliability:\\n      target_count: 5\\n      must_cite: [\\\"livebench2024\\\", \\\"empcloths2025\\\", \\\"zheng2023chatbot\\\", \\\"liang2023helm\\\"]\\n      search_queries: [\\\"benchmark reliability LLM contamination mitigation\\\", \\\"dynamic benchmark evaluation\\\"]\\n    calibration_uq:\\n      target_count: 4\\n      must_cite: [\\\"guo2017calibration\\\", \\\"angelopoulos2023conformal\\\", \\\"talts2018sbc\\\"]\\n      search_queries: [\\\"calibration uncertainty quantification neural network\\\", \\\"simulation based calibration Bayesian\\\"]\\n    mia_foundations:\\n      target_count: 3\\n      must_cite: [\\\"shokri2017membership\\\", \\\"carlini2022extracting\\\"]\\n      search_queries: [\\\"membership inference attack training data extraction\\\"]\\n    contamination_mitigation:\\n      target_count: 4\\n      must_cite: [\\\"oren2024dcr\\\"]\\n      search_queries: [\\\"benchmark contamination mitigation adjusted accuracy\\\", \\\"decontamination LLM evaluation\\\"]\\n    data_attribution:\\n      target_count: 2\\n      must_cite: []\\n      search_queries: [\\\"data attribution influence functions LLM\\\"]\\n      notes: \\\"Future work mention only. TracIn (Pruthi 2020), TRAK (Park 2023).\\\"\\n    irt_methodology:\\n      target_count: 3\\n      must_cite: [\\\"sanmartin2009\\\", \\\"maris2009\\\", \\\"reckase2009\\\"]\\n      search_queries: [\\\"IRT identifiability four parameter logistic\\\", \\\"multidimensional IRT\\\"]\\n\\nwriting_order:\\n  - section: \\\"method\\\"\\n    rationale: \\\"No data dependency. Sets notation for all downstream sections.\\\"\\n  - section: \\\"experimental_setup\\\"\\n    rationale: \\\"Defines experimental design. Needed by results.\\\"\\n  - section: \\\"results\\\"\\n    rationale: \\\"Core empirical contribution. Needs method + setup.\\\"\\n  - section: \\\"related_work\\\"\\n    rationale: \\\"Needs literature_map from Step 3. Positions against prior work.\\\"\\n  - section: \\\"discussion\\\"\\n    rationale: \\\"Needs results to discuss limitations and implications.\\\"\\n  - section: \\\"introduction\\\"\\n    rationale: \\\"Needs full picture to frame contributions precisely.\\\"\\n  - section: \\\"conclusion\\\"\\n    rationale: \\\"Summarizes all. Write after intro.\\\"\\n  - section: \\\"abstract\\\"\\n    rationale: \\\"Write last. Distills entire paper.\\\"\\n\\ndata_availability:\\n  available_now:\\n    - \\\"0.5B: all dosages × 2 seeds, SFT + eval + signals complete\\\"\\n    - \\\"1.5B: all dosages × 2 seeds, SFT + eval + signals (12/12) complete\\\"\\n    - \\\"exp-004 sim_sweep: v5 partial (59/120 seeds), v6/v7 running\\\"\\n    - \\\"exp-006 IRT: ARC S1 4PL+γ, GSM8K oracle/S1 4PL+γ/2PL+γ, ARC oracle 2PL+γ\\\"\\n    - \\\"exp-008 signal eval: 0.5B complete, 1.5B complete\\\"\\n    - \\\"exp-005 noise_prop: v4 DONE (negative)\\\"\\n  pending:\\n    - \\\"3B: SFTs running (~2-3 days), signals after GPU release (~1 day) → [PENDING-3B]\\\"\\n    - \\\"exp-004 sim_sweep: AUC=0.65 and AUC=0.9 conditions incomplete\\\"\\n    - \\\"exp-006: per-benchmark IRT with D045 exclusions (0.5B MMLU/ARC removed) — may need rerun\\\"\\n  excluded_from_paper:\\n    - \\\"7B/72B (D060: rebuttal)\\\"\\n    - \\\"Multi-family Llama/Pythia (exp-014: rebuttal)\\\"\\n    - \\\"RL observational (exp-009: rebuttal)\\\"\\n    - \\\"Closed-weight (rebuttal)\\\"\\n\\ndata_constraints:  # Updated 2026-05-15\\n  alpha_note: \\\"D055 alpha 混用约束已撤回。所有 checkpoint 实际 lora_alpha=32（train_sft.py bug 忽略 CLI 参数）。跨种子数据可统一处理。\\\"\\n  gsm8k_d005_s123: \\\"暂不可用（63.08% 异常，正在调查）。其他维度正常。\\\"\\n\\nkey_decisions:\\n  - \\\"D039: Characterization-led framing, calibration demoted to Claim 4\\\"\\n  - \\\"D045: Exclude 0.5B MMLU/ARC from IRT (position bias)\\\"\\n  - \\\"D053: Per-benchmark independent IRT only (joint/stratified废弃)\\\"\\n  - \\\"D055: WITHDRAWN — alpha 混用问题不存在，所有 checkpoint alpha=32\\\"\\n  - \\\"D056: Coverage collapse = model misspecification (honest negative)\\\"\\n  - \\\"D060: P1/P2 experiments → rebuttal scope\\\"\\n\", \"total_chars\": 16926, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "2d3d2d32-46d0-434c-860e-dcc30f0d3c18",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/writing_plan.yaml\\\", \\\"content\\\": \\\"## writing_plan.yaml — contamcal-irt-calibration\\\\n## Generated: 2026-05-15 | Paper Agent Step 1\\\\n## Status: APPROVED (Director 2026-05-15)\\\\n\\\\nmeta:\\\\n  venue: \\\\\\\"EMNLP 2026 ARR May 25\\\\\\\"\\\\n  track: \\\\\\\"Machine Learning for NLP / Resources and Evaluation\\\\\\\"\\\\n  deadline: \\\\\\\"2026-05-25\\\\\\\"\\\\n  page_limit: 8  # + unlimited appendix\\\\n  template: \\\\\\\"acl_latex (ARR format)\\\\\\\"\\\\n  template_note: \\\\\\\"No local EMNLP 2026 template found; use acl-style-files from github.com/acl-org/acl-style-files. Worker should download latest.\\\\\\\"\\\\n  special_theme: \\\\\\\"New Missions for NLP Research\\\\\\\"\\\\n  framing_doc: \\\\\\\"paper_framing.md (D039 pivot: characterization-led)\\\\\\\"\\\\n  total_word_budget: 5800  # main text excluding references\\\\n\\\\ntitle: >\\\\n  ContamCal: Characterizing Benchmark-Dependent Contamination Effects\\\\n  via Contamination-Augmented Item Response Theory\\\\n\\\\ncore_claims:\\\\n  C1:\\\\n    name: \\\\\\\"Characterization (PRIMARY)\\\\\\\"\\\\n    summary: \\\\\\\"Contamination effects are benchmark-dependent (ARC γ<0, GSM8K γ>0) and scale-dependent (catastrophic at 0.5B, mild at 3B). Per-benchmark γ_k captures bidirectional effects.\\\\\\\"\\\\n    evidence: [exp-001, exp-006]\\\\n    priority: 1\\\\n  C2:\\\\n    name: \\\\\\\"Signal Failure (CO-PRIMARY)\\\\\\\"\\\\n    summary: \\\\\\\"Min-K++ directional reversal (Cohen's d = -1.98 at 0.5B d100). S1 embedding is the only reliable signal (AUC>0.95 at d005). RRF degrades to S1-only in practice.\\\\\\\"\\\\n    evidence: [exp-008, exp-002, exp-003]\\\\n    priority: 1\\\\n  C3:\\\\n    name: \\\\\\\"Identifiability\\\\\\\"\\\\n    summary: \\\\\\\"Fisher Information analysis → recovery successful at AUC=0.55 (lowest tested, J≥50); lower bound open. LLM eval small cohorts create domain-method mismatch.\\\\\\\"\\\\n    evidence: [exp-004, mvp_sim_4pl_gamma]\\\\n    priority: 2\\\\n  C4:\\\\n    name: \\\\\\\"Conditional Calibration (DEMOTED)\\\\\\\"\\\\n    summary: \\\\\\\"Calibration works when model complexity matches benchmark + signal AUC sufficient. ARC MAE=0.035. GSM8K overcorrection as honest negative result. Gating criterion necessary.\\\\\\\"\\\\n    evidence: [exp-006]\\\\n    priority: 3\\\\n\\\\npaper_outline:\\\\n  abstract:\\\\n    word_budget: 200\\\\n    dependencies: [introduction, results, conclusion]\\\\n    key_numbers: [\\\\\\\"ARC γ=-1.46\\\\\\\", \\\\\\\"GSM8K γ=3.77 (oracle)\\\\\\\", \\\\\\\"Min-K++ Cohen's d=-1.98\\\\\\\", \\\\\\\"ARC MAE=0.035\\\\\\\", \\\\\\\"AUC=0.55 recovery (lowest tested)\\\\\\\"]\\\\n    notes: \\\\\\\"Write last. Characterization-led framing. 4 claims in priority order.\\\\\\\"\\\\n\\\\n  introduction:\\\\n    word_budget: 850\\\\n    dependencies: [method, results]\\\\n    subsections:\\\\n      - \\\\\\\"Problem: contamination undermines benchmark reliability\\\\\\\"\\\\n      - \\\\\\\"Gap: detection methods flag but don't calibrate; mitigation provably fails\\\\\\\"\\\\n      - \\\\\\\"Our approach: characterization framework via contamination-augmented IRT\\\\\\\"\\\\n      - \\\\\\\"3 core contributions (characterization, signal failure, identifiability) + conditional calibration\\\\\\\"\\\\n    notes: \\\\\\\"D039 pivot: lead with characterization, not calibration. Frame as diagnostic framework. Reference Emperor's New Clothes for motivation.\\\\\\\"\\\\n\\\\n  related_work:\\\\n    word_budget: 700\\\\n    dependencies: [literature_map]\\\\n    subsections:\\\\n      - \\\\\\\"Contamination detection (Min-K++, ConStat, KDS, CDD, Self-Critique)\\\\\\\"\\\\n      - \\\\\\\"IRT for LLM evaluation (Lalor, TinyBenchmarks, Growing Pains, HiBayES)\\\\\\\"\\\\n      - \\\\\\\"Item compromise in educational measurement (Eckerly, Sinharay, DIF)\\\\\\\"\\\\n      - \\\\\\\"Contamination mitigation and calibration disambiguation\\\\\\\"\\\\n    notes: \\\\\\\"Must disambiguate 'calibration' from probability calibration (Guo et al.) and conformal prediction.\\\\\\\"\\\\n\\\\n  method:\\\\n    word_budget: 1100\\\\n    dependencies: []\\\\n    subsections:\\\\n      - name: \\\\\\\"3.1 Problem Formulation\\\\\\\"\\\\n        content: \\\\\\\"Given model j, benchmark k with items i, observed response y_{ijk}. Goal: estimate θ_j^clean. Three IRT adaptations from educational measurement.\\\\\\\"\\\\n      - name: \\\\\\\"3.2 Stage 1: Multi-Signal Exposure Mapping\\\\\\\"\\\\n        content: \\\\\\\"4 signals (S1-S4), RRF aggregation. Meta-circularity argument for training-free fusion.\\\\\\\"\\\\n      - name: \\\\\\\"3.3 Stage 2: Contamination-Augmented IRT\\\\\\\"\\\\n        content: \\\\\\\"4PL+γ model: P(y=1) = c_i + (d_i - c_i) σ(a_i(θ_j - b_i) + γ_k·e_{ij}). Per-benchmark γ_k. Stan NUTS inference.\\\\\\\"\\\\n      - name: \\\\\\\"3.4 Fisher Information and Identifiability\\\\\\\"\\\\n        content: \\\\\\\"Derive I(γ) for 4PL+γ. Recovery boundaries from sim sweep (24 conditions, 240 runs). CI width ∝ N^{-0.48}. Domain-method mismatch.\\\\\\\"\\\\n    notes: \\\\\\\"Can be written first (no data dependency). Include measurement error model as optional extension. Full Fisher derivation in appendix.\\\\\\\"\\\\n\\\\n  experimental_setup:\\\\n    word_budget: 600\\\\n    dependencies: [method]\\\\n    subsections:\\\\n      - name: \\\\\\\"4.1 Controlled SFT Injection\\\\\\\"\\\\n        content: \\\\\\\"Qwen2.5 (0.5B, 1.5B, 3B). 4 dosages (d000/d005/d025/d100). 2 seeds. LoRA alpha=32. QC-filtered injection data.\\\\\\\"\\\\n      - name: \\\\\\\"4.2 Benchmarks and Evaluation Protocol\\\\\\\"\\\\n        content: \\\\\\\"ARC-Challenge (1172 items), GSM8K (1319), MMLU (14042, subsampled for IRT). 6 metrics. Aligned + paraphrased eval.\\\\\\\"\\\\n      - name: \\\\\\\"4.3 Baselines\\\\\\\"\\\\n        content: \\\\\\\"7 baselines: B0-Raw, B1-Remove&Rescore, B2-Single2PL+γ, B3-Vanilla4PL, B4-LinearRegression, B5-Emperor, B6-DCR.\\\\\\\"\\\\n    notes: \\\\\\\"D045: exclude 0.5B MMLU/ARC from IRT pooling (position bias). Retain 0.5B GSM8K. D060: scope to 0.5B+1.5B main, 3B as [PENDING-3B]. 7B/72B → future work.\\\\\\\"\\\\n\\\\n  results:\\\\n    word_budget: 1500\\\\n    dependencies: [experimental_setup, fig_signal_heatmap, fig_dose_response, fig_identifiability, fig_calibration, table_gamma, table_baselines]\\\\n    subsections:\\\\n      - name: \\\\\\\"5.1 Contamination Characterization\\\\\\\"\\\\n        content: \\\\\\\"Per-benchmark γ_k: ARC γ=-1.46 (forgetting), GSM8K γ=3.77 (oracle, inflation). Scale modulation: 0.5B catastrophic vs 1.5B mild. Dose-response curves. 3B [PENDING-3B].\\\\\\\"\\\\n        claims: [C1]\\\\n        key_tables: [table_gamma]\\\\n        key_figures: [fig_dose_response]\\\\n      - name: \\\\\\\"5.2 Detection Signal Analysis\\\\\\\"\\\\n        content: \\\\\\\"S1 AUC>0.95 at d005. S2 Min-K++ AUC~0.47, Cohen's d=-1.98 (reversal). S4 random. RRF = S1-only in practice.\\\\\\\"\\\\n        claims: [C2]\\\\n        key_tables: [table_signal_summary]\\\\n        key_figures: [fig_signal_heatmap]\\\\n      - name: \\\\\\\"5.3 Identifiability Boundaries\\\\\\\"\\\\n        content: \\\\\\\"Sim sweep (24 conditions, 240 runs): AUC=0.80 N=50 bias=0.006. AUC=0.55 J≥50 meets all criteria. AUC=0.65 systematically fails at small J. CI width ∝ N^{-0.48}. LLM eval small cohorts = structural mismatch.\\\\\\\"\\\\n        claims: [C3]\\\\n        key_figures: [fig_identifiability]\\\\n      - name: \\\\\\\"5.4 Conditional Calibration\\\\\\\"\\\\n        content: \\\\\\\"ARC 4PL+γ: MAE=0.035 (beats all baselines). Kendall τ=0.756. Coverage 62.5% (below nominal). GSM8K signal-derived γ non-significant → gating criterion triggers. GSM8K overcorrection MAE=0.092 vs raw 0.005 as honest negative. MMLU IRT fails (Rhat=1.54).\\\\\\\"\\\\n        claims: [C4]\\\\n        key_tables: [table_baselines]\\\\n        key_figures: [fig_calibration]\\\\n    notes: \\\\\\\"3B rows in all tables/figures marked [PENDING-3B]. Honest about negatives: GSM8K overcorrection, MMLU failure, coverage below nominal.\\\\\\\"\\\\n\\\\n  discussion:\\\\n    word_budget: 500\\\\n    dependencies: [results]\\\\n    subsections:\\\\n      - \\\\\\\"Limitations: single model family (Qwen2.5), SFT ≠ real contamination, N<50, coverage below nominal\\\\\\\"\\\\n      - \\\\\\\"0.5B position bias (D045): capacity threshold for MC evaluation\\\\\\\"\\\\n      - \\\\\\\"When NOT to calibrate: gating criterion and its implications\\\\\\\"\\\\n      - \\\\\\\"Future work: multi-family (Llama/Pythia), 7B+, RL observational, data attribution signals\\\\\\\"\\\\n    notes: \\\\\\\"Coverage collapse (D056) as model misspecification evidence. noise_prop negative result → appendix mention.\\\\\\\"\\\\n\\\\n  conclusion:\\\\n    word_budget: 350\\\\n    dependencies: [discussion]\\\\n    notes: \\\\\\\"Restate 4 claims compactly. Emphasize characterization > calibration. End with 'conditions under which calibration is feasible' framing.\\\\\\\"\\\\n\\\\n  appendix:\\\\n    sections:\\\\n      - name: \\\\\\\"A: Fisher Information Derivation\\\\\\\"\\\\n        source: \\\\\\\"artifacts/fisher_info_derivation/fisher_info_appendix.tex\\\\\\\"\\\\n        notes: \\\\\\\"Already drafted. Verify completeness.\\\\\\\"\\\\n      - name: \\\\\\\"B: Simulation Sweep Details\\\\\\\"\\\\n        data_source: \\\\\\\"exp-004\\\\\\\"\\\\n      - name: \\\\\\\"C: Measurement Error Analysis\\\\\\\"\\\\n        data_source: \\\\\\\"exp-005\\\\\\\"\\\\n        notes: \\\\\\\"Negative result. noise_prop_v4 CI insensitive to σ_e.\\\\\\\"\\\\n      - name: \\\\\\\"D: 0.5B Position Bias Analysis\\\\\\\"\\\\n        data_source: \\\\\\\"exp-001 (0.5B MMLU prediction distribution)\\\\\\\"\\\\n        notes: \\\\\\\"D045: MMLU prediction dist d000 A=46% → d100 A=98%.\\\\\\\"\\\\n      - name: \\\\\\\"E: HumanEval Results\\\\\\\"\\\\n        notes: \\\\\\\"Demoted from main (D009: 16% QC pass).\\\\\\\"\\\\n\\\\nvisualization_plan:\\\\n  fig_pipeline:\\\\n    type: \\\\\\\"conceptual_diagram\\\\\\\"\\\\n    description: \\\\\\\"ContamCal 2-stage pipeline overview. Left: 4 detection signals → RRF fusion → exposure scores. Right: exposure + responses → 4PL+γ IRT → calibrated scores with CIs. Show per-benchmark γ_k.\\\\\\\"\\\\n    placement: \\\\\\\"Section 3 (Method), top of page\\\\\\\"\\\\n    aspect_ratio: \\\\\\\"2:1 (wide)\\\\\\\"\\\\n    tool: \\\\\\\"matplotlib\\\\\\\"\\\\n    data_source: null  # conceptual, no data\\\\n    output: \\\\\\\"figures/paper/fig_pipeline.pdf\\\\\\\"\\\\n\\\\n  fig_dose_response:\\\\n    type: \\\\\\\"line_plot\\\\\\\"\\\\n    description: \\\\\\\"Dosage (x: d000, d005, d025, d100) vs benchmark accuracy (y) for each benchmark. Separate panels or lines for 0.5B, 1.5B, [PENDING-3B]. Show ARC forgetting vs GSM8K inflation. Error bars from 2 seeds.\\\\\\\"\\\\n    placement: \\\\\\\"Section 5.1\\\\\\\"\\\\n    aspect_ratio: \\\\\\\"3:2\\\\\\\"\\\\n    tool: \\\\\\\"matplotlib\\\\\\\"\\\\n    data_source: \\\\\\\"registry: exp-001 eval results (aligned format, all scales × dosages × seeds)\\\\\\\"\\\\n    output: \\\\\\\"figures/paper/fig_dose_response.pdf\\\\\\\"\\\\n\\\\n  fig_signal_heatmap:\\\\n    type: \\\\\\\"heatmap\\\\\\\"\\\\n    description: \\\\\\\"Signal AUC heatmap. Rows: 3 signals (S1 Embedding, S2 Min-K++, S4 Self-Critique) × 3 benchmarks. Columns: dosages (d005, d025). Separate panels for 0.5B and 1.5B. Annotate Cohen's d for d100 cross-model comparison. Highlight Min-K++ reversal cell in red.\\\\\\\"\\\\n    placement: \\\\\\\"Section 5.2\\\\\\\"\\\\n    aspect_ratio: \\\\\\\"4:3\\\\\\\"\\\\n    tool: \\\\\\\"matplotlib\\\\\\\"\\\\n    data_source: \\\\\\\"registry: exp-008 signal survival v1 + v4 (AUC + Cohen's d)\\\\\\\"\\\\n    output: \\\\\\\"figures/paper/fig_signal_heatmap.pdf\\\\\\\"\\\\n\\\\n  fig_identifiability:\\\\n    type: \\\\\\\"phase_diagram\\\\\\\"\\\\n    description: \\\\\\\"Identifiability boundaries. X: signal AUC. Y: N_models. Color/marker: γ recovery quality (bias, RMSE, CI coverage). Shade regions: successful recovery region (AUC≥0.55, all tested N≥20). Lower bound open. Mark actual LLM eval operating point (AUC~0.98, N=8-16).\\\\\\\"\\\\n    placement: \\\\\\\"Section 5.3\\\\\\\"\\\\n    aspect_ratio: \\\\\\\"1:1\\\\\\\"\\\\n    tool: \\\\\\\"matplotlib\\\\\\\"\\\\n    data_source: \\\\\\\"registry: exp-004 sim_sweep results (v5 completed conditions)\\\\\\\"\\\\n    output: \\\\\\\"figures/paper/fig_identifiability.pdf\\\\\\\"\\\\n\\\\n  fig_calibration:\\\\n    type: \\\\\\\"scatter_with_ci\\\\\\\"\\\\n    description: \\\\\\\"Calibrated score (x) vs true clean score (y) scatter. Each point = one model-benchmark. Horizontal bars = 95% CI. Diagonal = perfect calibration. Color by benchmark. Annotate ARC cluster (good) vs GSM8K cluster (overcorrection). Include B0 (raw) as hollow markers for comparison.\\\\\\\"\\\\n    placement: \\\\\\\"Section 5.4\\\\\\\"\\\\n    aspect_ratio: \\\\\\\"1:1\\\\\\\"\\\\n    tool: \\\\\\\"matplotlib\\\\\\\"\\\\n    data_source: \\\\\\\"registry: exp-006 IRT calibration results (ARC S1-only 4PL+γ, GSM8K 2PL+γ)\\\\\\\"\\\\n    output: \\\\\\\"figures/paper/fig_calibration.pdf\\\\\\\"\\\\n\\\\ntable_plan:\\\\n  table_gamma:\\\\n    type: \\\\\\\"parameter_summary\\\\\\\"\\\\n    description: \\\\\\\"Per-benchmark IRT γ estimates with diagnostics\\\\\\\"\\\\n    columns: [\\\\\\\"Benchmark\\\\\\\", \\\\\\\"Model\\\\\\\", \\\\\\\"γ̂\\\\\\\", \\\\\\\"95% CI\\\\\\\", \\\\\\\"Excludes 0?\\\\\\\", \\\\\\\"R̂\\\\\\\", \\\\\\\"ESS\\\\\\\", \\\\\\\"PPP\\\\\\\", \\\\\\\"Direction\\\\\\\"]\\\\n    data_source: \\\\\\\"exp-006 per-benchmark IRT fits\\\\\\\"\\\\n    placement: \\\\\\\"Section 5.1\\\\\\\"\\\\n    rows:\\\\n      - \\\\\\\"ARC (S1, 4PL+γ): γ=-1.46 [-2.51, -0.41] ✓ 1.010 770 TBD Forgetting\\\\\\\"\\\\n      - \\\\\\\"ARC (oracle, 2PL+γ): γ=-0.62 [-1.04, -0.20] ✓ 1.006 1512 TBD Forgetting\\\\\\\"\\\\n      - \\\\\\\"GSM8K (oracle, 4PL+γ): γ=3.77 [2.74, 4.71] ✓ 1.002 1222 TBD Inflation\\\\\\\"\\\\n      - \\\\\\\"GSM8K (S1, 2PL+γ): γ=0.14 [-0.31, 0.59] ✗ 1.002 3604 0.284 —\\\\\\\"\\\\n      - \\\\\\\"GSM8K (S1, 4PL+γ): γ=0.19 [-0.92, 1.33] ✗ 1.015 330 TBD — (convergence issue)\\\\\\\"\\\\n      - \\\\\\\"MMLU (RRF): FAILED (R̂=1.54, ESS=7)\\\\\\\"\\\\n      - \\\\\\\"[PENDING-3B] rows\\\\\\\"\\\\n\\\\n  table_baselines:\\\\n    type: \\\\\\\"comparison\\\\\\\"\\\\n    description: \\\\\\\"Calibration performance: ContamCal vs 7 baselines\\\\\\\"\\\\n    columns: [\\\\\\\"Method\\\\\\\", \\\\\\\"ARC MAE↓\\\\\\\", \\\\\\\"ARC τ↑\\\\\\\", \\\\\\\"ARC C95%\\\\\\\", \\\\\\\"GSM8K MAE↓\\\\\\\", \\\\\\\"GSM8K τ↑\\\\\\\"]\\\\n    data_source: \\\\\\\"exp-006 baseline comparisons\\\\\\\"\\\\n    placement: \\\\\\\"Section 5.4\\\\\\\"\\\\n    notes: \\\\\\\"ARC is success case. GSM8K shows gating criterion necessity. MMLU excluded (failed).\\\\\\\"\\\\n\\\\n  table_signal_summary:\\\\n    type: \\\\\\\"signal_evaluation\\\\\\\"\\\\n    description: \\\\\\\"Signal effectiveness by scale × benchmark\\\\\\\"\\\\n    columns: [\\\\\\\"Signal\\\\\\\", \\\\\\\"Scale\\\\\\\", \\\\\\\"d005 AUC\\\\\\\", \\\\\\\"d025 AUC\\\\\\\", \\\\\\\"d100 Cohen's d\\\\\\\"]\\\\n    data_source: \\\\\\\"exp-008\\\\\\\"\\\\n    placement: \\\\\\\"Section 5.2 or Appendix\\\\\\\"\\\\n    notes: \\\\\\\"May merge into fig_signal_heatmap. Keep as table if space allows.\\\\\\\"\\\\n\\\\nliterature_strategy:\\\\n  citation_budget: \\\\\\\"40-50 total\\\\\\\"\\\\n  macro_context: \\\\\\\"Contamination is a systemic threat; detection exists but calibration doesn't; educational measurement solved the analogous exam leak problem decades ago.\\\\\\\"\\\\n  micro_clusters:\\\\n    contamination_detection:\\\\n      target_count: 8\\\\n      must_cite: [\\\\\\\"zhang2024minkpp\\\\\\\", \\\\\\\"dekoninck2024constat\\\\\\\", \\\\\\\"dong2024kds\\\\\\\", \\\\\\\"shi2024cdd\\\\\\\", \\\\\\\"weller2024selfcritique\\\\\\\", \\\\\\\"golchin2024time\\\\\\\"]\\\\n      search_queries: [\\\\\\\"benchmark contamination detection LLM\\\\\\\", \\\\\\\"membership inference LLM evaluation\\\\\\\"]\\\\n    irt_for_llm:\\\\n      target_count: 6\\\\n      must_cite: [\\\\\\\"lalor2024aaai\\\\\\\", \\\\\\\"polo2024tinybenchmarks\\\\\\\", \\\\\\\"burnell2023multidimensional\\\\\\\"]\\\\n      search_queries: [\\\\\\\"item response theory large language model evaluation\\\\\\\", \\\\\\\"psychometric LLM benchmark\\\\\\\"]\\\\n    item_compromise_irt:\\\\n      target_count: 5\\\\n      must_cite: [\\\\\\\"eckerly2017\\\\\\\", \\\\\\\"sinharay2017\\\\\\\", \\\\\\\"deboeck2004\\\\\\\", \\\\\\\"holland1993dif\\\\\\\", \\\\\\\"adams1997\\\\\\\"]\\\\n      search_queries: [\\\\\\\"item compromise IRT detection\\\\\\\", \\\\\\\"differential item functioning preknowledge\\\\\\\"]\\\\n    benchmark_reliability:\\\\n      target_count: 5\\\\n      must_cite: [\\\\\\\"livebench2024\\\\\\\", \\\\\\\"empcloths2025\\\\\\\", \\\\\\\"zheng2023chatbot\\\\\\\", \\\\\\\"liang2023helm\\\\\\\"]\\\\n      search_queries: [\\\\\\\"benchmark reliability LLM contamination mitigation\\\\\\\", \\\\\\\"dynamic benchmark evaluation\\\\\\\"]\\\\n    calibration_uq:\\\\n      target_count: 4\\\\n      must_cite: [\\\\\\\"guo2017calibration\\\\\\\", \\\\\\\"angelopoulos2023conformal\\\\\\\", \\\\\\\"talts2018sbc\\\\\\\"]\\\\n      search_queries: [\\\\\\\"calibration uncertainty quantification neural network\\\\\\\", \\\\\\\"simulation based calibration Bayesian\\\\\\\"]\\\\n    mia_foundations:\\\\n      target_count: 3\\\\n      must_cite: [\\\\\\\"shokri2017membership\\\\\\\", \\\\\\\"carlini2022extracting\\\\\\\"]\\\\n      search_queries: [\\\\\\\"membership inference attack training data extraction\\\\\\\"]\\\\n    contamination_mitigation:\\\\n      target_count: 4\\\\n      must_cite: [\\\\\\\"oren2024dcr\\\\\\\"]\\\\n      search_queries: [\\\\\\\"benchmark contamination mitigation adjusted accuracy\\\\\\\", \\\\\\\"decontamination LLM evaluation\\\\\\\"]\\\\n    data_attribution:\\\\n      target_count: 2\\\\n      must_cite: []\\\\n      search_queries: [\\\\\\\"data attribution influence functions LLM\\\\\\\"]\\\\n      notes: \\\\\\\"Future work mention only. TracIn (Pruthi 2020), TRAK (Park 2023).\\\\\\\"\\\\n    irt_methodology:\\\\n      target_count: 3\\\\n      must_cite: [\\\\\\\"sanmartin2009\\\\\\\", \\\\\\\"maris2009\\\\\\\", \\\\\\\"reckase2009\\\\\\\"]\\\\n      search_queries: [\\\\\\\"IRT identifiability four parameter logistic\\\\\\\", \\\\\\\"multidimensional IRT\\\\\\\"]\\\\n\\\\nwriting_order:\\\\n  - section: \\\\\\\"method\\\\\\\"\\\\n    rationale: \\\\\\\"No data dependency. Sets notation for all downstream sections.\\\\\\\"\\\\n  - section: \\\\\\\"experimental_setup\\\\\\\"\\\\n    rationale: \\\\\\\"Defines experimental design. Needed by results.\\\\\\\"\\\\n  - section: \\\\\\\"results\\\\\\\"\\\\n    rationale: \\\\\\\"Core empirical contribution. Needs method + setup.\\\\\\\"\\\\n  - section: \\\\\\\"related_work\\\\\\\"\\\\n    rationale: \\\\\\\"Needs literature_map from Step 3. Positions against prior work.\\\\\\\"\\\\n  - section: \\\\\\\"discussion\\\\\\\"\\\\n    rationale: \\\\\\\"Needs results to discuss limitations and implications.\\\\\\\"\\\\n  - section: \\\\\\\"introduction\\\\\\\"\\\\n    rationale: \\\\\\\"Needs full picture to frame contributions precisely.\\\\\\\"\\\\n  - section: \\\\\\\"conclusion\\\\\\\"\\\\n    rationale: \\\\\\\"Summarizes all. Write after intro.\\\\\\\"\\\\n  - section: \\\\\\\"abstract\\\\\\\"\\\\n    rationale: \\\\\\\"Write last. Distills entire paper.\\\\\\\"\\\\n\\\\ndata_availability:\\\\n  available_now:\\\\n    - \\\\\\\"0.5B: all dosages × 2 seeds, SFT + eval + signals complete\\\\\\\"\\\\n    - \\\\\\\"1.5B: all dosages × 2 seeds, SFT + eval + signals (12/12) complete\\\\\\\"\\\\n    - \\\\\\\"exp-004 sim_sweep: v5 partial (59/120 seeds), v6/v7 running\\\\\\\"\\\\n    - \\\\\\\"exp-006 IRT: ARC S1 4PL+γ, GSM8K oracle/S1 4PL+γ/2PL+γ, ARC oracle 2PL+γ\\\\\\\"\\\\n    - \\\\\\\"exp-008 signal eval: 0.5B complete, 1.5B complete\\\\\\\"\\\\n    - \\\\\\\"exp-005 noise_prop: v4 DONE (negative)\\\\\\\"\\\\n  pending:\\\\n    - \\\\\\\"3B: SFTs running (~2-3 days), signals after GPU release (~1 day) → [PENDING-3B]\\\\\\\"\\\\n    - \\\\\\\"exp-004 sim_sweep: AUC=0.65 and AUC=0.9 conditions incomplete\\\\\\\"\\\\n    - \\\\\\\"exp-006: per-benchmark IRT with D045 exclusions (0.5B MMLU/ARC removed) — may need rerun\\\\\\\"\\\\n  excluded_from_paper:\\\\n    - \\\\\\\"7B/72B (D060: rebuttal)\\\\\\\"\\\\n    - \\\\\\\"Multi-family Llama/Pythia (exp-014: rebuttal)\\\\\\\"\\\\n    - \\\\\\\"RL observational (exp-009: rebuttal)\\\\\\\"\\\\n    - \\\\\\\"Closed-weight (rebuttal)\\\\\\\"\\\\n\\\\ndata_constraints:  # Updated 2026-05-15\\\\n  alpha_note: \\\\\\\"D055 alpha 混用约束已撤回。所有 checkpoint 实际 lora_alpha=32（train_sft.py bug 忽略 CLI 参数）。跨种子数据可统一处理。\\\\\\\"\\\\n  gsm8k_d005_s123: \\\\\\\"暂不可用（63.08% 异常，正在调查）。其他维度正常。\\\\\\\"\\\\n\\\\nkey_decisions:\\\\n  - \\\\\\\"D039: Characterization-led framing, calibration demoted to Claim 4\\\\\\\"\\\\n  - \\\\\\\"D045: Exclude 0.5B MMLU/ARC from IRT (position bias)\\\\\\\"\\\\n  - \\\\\\\"D053: Per-benchmark independent IRT only (joint/stratified废弃)\\\\\\\"\\\\n  - \\\\\\\"D055: WITHDRAWN — alpha 混用问题不存在，所有 checkpoint alpha=32\\\\\\\"\\\\n  - \\\\\\\"D056: Coverage collapse = model misspecification (honest negative)\\\\\\\"\\\\n  - \\\\\\\"D060: P1/P2 experiments → rebuttal scope\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 16926, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/writing_plan.yaml\", \"content\": \"## writing_plan.yaml — contamcal-irt-calibration\\n## Generated: 2026-05-15 | Paper Agent Step 1\\n## Status: APPROVED (Director 2026-05-15)\\n\\nmeta:\\n  venue: \\\"EMNLP 2026 ARR May 25\\\"\\n  track: \\\"Machine Learning for NLP / Resources and Evaluation\\\"\\n  deadline: \\\"2026-05-25\\\"\\n  page_limit: 8  # + unlimited appendix\\n  template: \\\"acl_latex (ARR format)\\\"\\n  template_note: \\\"No local EMNLP 2026 template found; use acl-style-files from github.com/acl-org/acl-style-files. Worker should download latest.\\\"\\n  special_theme: \\\"New Missions for NLP Research\\\"\\n  framing_doc: \\\"paper_framing.md (D039 pivot: characterization-led)\\\"\\n  total_word_budget: 5800  # main text excluding references\\n\\ntitle: >\\n  ContamCal: Characterizing Benchmark-Dependent Contamination Effects\\n  via Contamination-Augmented Item Response Theory\\n\\ncore_claims:\\n  C1:\\n    name: \\\"Characterization (PRIMARY)\\\"\\n    summary: \\\"Contamination effects are benchmark-dependent (ARC γ<0, GSM8K γ>0) and scale-dependent (catastrophic at 0.5B, mild at 3B). Per-benchmark γ_k captures bidirectional effects.\\\"\\n    evidence: [exp-001, exp-006]\\n    priority: 1\\n  C2:\\n    name: \\\"Signal Failure (CO-PRIMARY)\\\"\\n    summary: \\\"Min-K++ directional reversal (Cohen's d = -1.98 at 0.5B d100). S1 embedding is the only reliable signal (AUC>0.95 at d005). RRF degrades to S1-only in practice.\\\"\\n    evidence: [exp-008, exp-002, exp-003]\\n    priority: 1\\n  C3:\\n    name: \\\"Identifiability\\\"\\n    summary: \\\"Fisher Information analysis → recovery successful at AUC=0.55 (lowest tested, J≥50); lower bound open. LLM eval small cohorts create domain-method mismatch.\\\"\\n    evidence: [exp-004, mvp_sim_4pl_gamma]\\n    priority: 2\\n  C4:\\n    name: \\\"Conditional Calibration (DEMOTED)\\\"\\n    summary: \\\"Calibration works when model complexity matches benchmark + signal AUC sufficient. ARC MAE=0.035. GSM8K overcorrection as honest negative result. Gating criterion necessary.\\\"\\n    evidence: [exp-006]\\n    priority: 3\\n\\npaper_outline:\\n  abstract:\\n    word_budget: 200\\n    dependencies: [introduction, results, conclusion]\\n    key_numbers: [\\\"ARC γ=-1.46\\\", \\\"GSM8K γ=3.77 (oracle)\\\", \\\"Min-K++ Cohen's d=-1.98\\\", \\\"ARC MAE=0.035\\\", \\\"AUC=0.55 recovery (lowest tested)\\\"]\\n    notes: \\\"Write last. Characterization-led framing. 4 claims in priority order.\\\"\\n\\n  introduction:\\n    word_budget: 850\\n    dependencies: [method, results]\\n    subsections:\\n      - \\\"Problem: contamination undermines benchmark reliability\\\"\\n      - \\\"Gap: detection methods flag but don't calibrate; mitigation provably fails\\\"\\n      - \\\"Our approach: characterization framework via contamination-augmented IRT\\\"\\n      - \\\"3 core contributions (characterization, signal failure, identifiability) + conditional calibration\\\"\\n    notes: \\\"D039 pivot: lead with characterization, not calibration. Frame as diagnostic framework. Reference Emperor's New Clothes for motivation.\\\"\\n\\n  related_work:\\n    word_budget: 700\\n    dependencies: [literature_map]\\n    subsections:\\n      - \\\"Contamination detection (Min-K++, ConStat, KDS, CDD, Self-Critique)\\\"\\n      - \\\"IRT for LLM evaluation (Lalor, TinyBenchmarks, Growing Pains, HiBayES)\\\"\\n      - \\\"Item compromise in educational measurement (Eckerly, Sinharay, DIF)\\\"\\n      - \\\"Contamination mitigation and calibration disambiguation\\\"\\n    notes: \\\"Must disambiguate 'calibration' from probability calibration (Guo et al.) and conformal prediction.\\\"\\n\\n  method:\\n    word_budget: 1100\\n    dependencies: []\\n    subsections:\\n      - name: \\\"3.1 Problem Formulation\\\"\\n        content: \\\"Given model j, benchmark k with items i, observed response y_{ijk}. Goal: estimate θ_j^clean. Three IRT adaptations from educational measurement.\\\"\\n      - name: \\\"3.2 Stage 1: Multi-Signal Exposure Mapping\\\"\\n        content: \\\"4 signals (S1-S4), RRF aggregation. Meta-circularity argument for training-free fusion.\\\"\\n      - name: \\\"3.3 Stage 2: Contamination-Augmented IRT\\\"\\n        content: \\\"4PL+γ model: P(y=1) = c_i + (d_i - c_i) σ(a_i(θ_j - b_i) + γ_k·e_{ij}). Per-benchmark γ_k. Stan NUTS inference.\\\"\\n      - name: \\\"3.4 Fisher Information and Identifiability\\\"\\n        content: \\\"Derive I(γ) for 4PL+γ. Recovery boundaries from sim sweep (24 conditions, 240 runs). CI width ∝ N^{-0.48}. Domain-method mismatch.\\\"\\n    notes: \\\"Can be written first (no data dependency). Include measurement error model as optional extension. Full Fisher derivation in appendix.\\\"\\n\\n  experimental_setup:\\n    word_budget: 600\\n    dependencies: [method]\\n    subsections:\\n      - name: \\\"4.1 Controlled SFT Injection\\\"\\n        content: \\\"Qwen2.5 (0.5B, 1.5B, 3B). 4 dosages (d000/d005/d025/d100). 2 seeds. LoRA alpha=32. QC-filtered injection data.\\\"\\n      - name: \\\"4.2 Benchmarks and Evaluation Protocol\\\"\\n        content: \\\"ARC-Challenge (1172 items), GSM8K (1319), MMLU (14042, subsampled for IRT). 6 metrics. Aligned + paraphrased eval.\\\"\\n      - name: \\\"4.3 Baselines\\\"\\n        content: \\\"7 baselines: B0-Raw, B1-Remove&Rescore, B2-Single2PL+γ, B3-Vanilla4PL, B4-LinearRegression, B5-Emperor, B6-DCR.\\\"\\n    notes: \\\"D045: exclude 0.5B MMLU/ARC from IRT pooling (position bias). Retain 0.5B GSM8K. D060: scope to 0.5B+1.5B main, 3B as [PENDING-3B]. 7B/72B → future work.\\\"\\n\\n  results:\\n    word_budget: 1500\\n    dependencies: [experimental_setup, fig_signal_heatmap, fig_dose_response, fig_identifiability, fig_calibration, table_gamma, table_baselines]\\n    subsections:\\n      - name: \\\"5.1 Contamination Characterization\\\"\\n        content: \\\"Per-benchmark γ_k: ARC γ=-1.46 (forgetting), GSM8K γ=3.77 (oracle, inflation). Scale modulation: 0.5B catastrophic vs 1.5B mild. Dose-response curves. 3B [PENDING-3B].\\\"\\n        claims: [C1]\\n        key_tables: [table_gamma]\\n        key_figures: [fig_dose_response]\\n      - name: \\\"5.2 Detection Signal Analysis\\\"\\n        content: \\\"S1 AUC>0.95 at d005. S2 Min-K++ AUC~0.47, Cohen's d=-1.98 (reversal). S4 random. RRF = S1-only in practice.\\\"\\n        claims: [C2]\\n        key_tables: [table_signal_summary]\\n        key_figures: [fig_signal_heatmap]\\n      - name: \\\"5.3 Identifiability Boundaries\\\"\\n        content: \\\"Sim sweep (24 conditions, 240 runs): AUC=0.80 N=50 bias=0.006. AUC=0.55 J≥50 meets all criteria. AUC=0.65 systematically fails at small J. CI width ∝ N^{-0.48}. LLM eval small cohorts = structural mismatch.\\\"\\n        claims: [C3]\\n        key_figures: [fig_identifiability]\\n      - name: \\\"5.4 Conditional Calibration\\\"\\n        content: \\\"ARC 4PL+γ: MAE=0.035 (beats all baselines). Kendall τ=0.756. Coverage 62.5% (below nominal). GSM8K signal-derived γ non-significant → gating criterion triggers. GSM8K overcorrection MAE=0.092 vs raw 0.005 as honest negative. MMLU IRT fails (Rhat=1.54).\\\"\\n        claims: [C4]\\n        key_tables: [table_baselines]\\n        key_figures: [fig_calibration]\\n    notes: \\\"3B rows in all tables/figures marked [PENDING-3B]. Honest about negatives: GSM8K overcorrection, MMLU failure, coverage below nominal.\\\"\\n\\n  discussion:\\n    word_budget: 500\\n    dependencies: [results]\\n    subsections:\\n      - \\\"Limitations: single model family (Qwen2.5), SFT ≠ real contamination, N<50, coverage below nominal\\\"\\n      - \\\"0.5B position bias (D045): capacity threshold for MC evaluation\\\"\\n      - \\\"When NOT to calibrate: gating criterion and its implications\\\"\\n      - \\\"Future work: multi-family (Llama/Pythia), 7B+, RL observational, data attribution signals\\\"\\n    notes: \\\"Coverage collapse (D056) as model misspecification evidence. noise_prop negative result → appendix mention.\\\"\\n\\n  conclusion:\\n    word_budget: 350\\n    dependencies: [discussion]\\n    notes: \\\"Restate 4 claims compactly. Emphasize characterization > calibration. End with 'conditions under which calibration is feasible' framing.\\\"\\n\\n  appendix:\\n    sections:\\n      - name: \\\"A: Fisher Information Derivation\\\"\\n        source: \\\"artifacts/fisher_info_derivation/fisher_info_appendix.tex\\\"\\n        notes: \\\"Already drafted. Verify completeness.\\\"\\n      - name: \\\"B: Simulation Sweep Details\\\"\\n        data_source: \\\"exp-004\\\"\\n      - name: \\\"C: Measurement Error Analysis\\\"\\n        data_source: \\\"exp-005\\\"\\n        notes: \\\"Negative result. noise_prop_v4 CI insensitive to σ_e.\\\"\\n      - name: \\\"D: 0.5B Position Bias Analysis\\\"\\n        data_source: \\\"exp-001 (0.5B MMLU prediction distribution)\\\"\\n        notes: \\\"D045: MMLU prediction dist d000 A=46% → d100 A=98%.\\\"\\n      - name: \\\"E: HumanEval Results\\\"\\n        notes: \\\"Demoted from main (D009: 16% QC pass).\\\"\\n\\nvisualization_plan:\\n  fig_pipeline:\\n    type: \\\"conceptual_diagram\\\"\\n    description: \\\"ContamCal 2-stage pipeline overview. Left: 4 detection signals → RRF fusion → exposure scores. Right: exposure + responses → 4PL+γ IRT → calibrated scores with CIs. Show per-benchmark γ_k.\\\"\\n    placement: \\\"Section 3 (Method), top of page\\\"\\n    aspect_ratio: \\\"2:1 (wide)\\\"\\n    tool: \\\"matplotlib\\\"\\n    data_source: null  # conceptual, no data\\n    output: \\\"figures/paper/fig_pipeline.pdf\\\"\\n\\n  fig_dose_response:\\n    type: \\\"line_plot\\\"\\n    description: \\\"Dosage (x: d000, d005, d025, d100) vs benchmark accuracy (y) for each benchmark. Separate panels or lines for 0.5B, 1.5B, [PENDING-3B]. Show ARC forgetting vs GSM8K inflation. Error bars from 2 seeds.\\\"\\n    placement: \\\"Section 5.1\\\"\\n    aspect_ratio: \\\"3:2\\\"\\n    tool: \\\"matplotlib\\\"\\n    data_source: \\\"registry: exp-001 eval results (aligned format, all scales × dosages × seeds)\\\"\\n    output: \\\"figures/paper/fig_dose_response.pdf\\\"\\n\\n  fig_signal_heatmap:\\n    type: \\\"heatmap\\\"\\n    description: \\\"Signal AUC heatmap. Rows: 3 signals (S1 Embedding, S2 Min-K++, S4 Self-Critique) × 3 benchmarks. Columns: dosages (d005, d025). Separate panels for 0.5B and 1.5B. Annotate Cohen's d for d100 cross-model comparison. Highlight Min-K++ reversal cell in red.\\\"\\n    placement: \\\"Section 5.2\\\"\\n    aspect_ratio: \\\"4:3\\\"\\n    tool: \\\"matplotlib\\\"\\n    data_source: \\\"registry: exp-008 signal survival v1 + v4 (AUC + Cohen's d)\\\"\\n    output: \\\"figures/paper/fig_signal_heatmap.pdf\\\"\\n\\n  fig_identifiability:\\n    type: \\\"phase_diagram\\\"\\n    description: \\\"Identifiability boundaries. X: signal AUC. Y: N_models. Color/marker: γ recovery quality (bias, RMSE, CI coverage). Shade regions: successful recovery region (AUC≥0.55, all tested N≥20). Lower bound open. Mark actual LLM eval operating point (AUC~0.98, N=8-16).\\\"\\n    placement: \\\"Section 5.3\\\"\\n    aspect_ratio: \\\"1:1\\\"\\n    tool: \\\"matplotlib\\\"\\n    data_source: \\\"registry: exp-004 sim_sweep results (v5 completed conditions)\\\"\\n    output: \\\"figures/paper/fig_identifiability.pdf\\\"\\n\\n  fig_calibration:\\n    type: \\\"scatter_with_ci\\\"\\n    description: \\\"Calibrated score (x) vs true clean score (y) scatter. Each point = one model-benchmark. Horizontal bars = 95% CI. Diagonal = perfect calibration. Color by benchmark. Annotate ARC cluster (good) vs GSM8K cluster (overcorrection). Include B0 (raw) as hollow markers for comparison.\\\"\\n    placement: \\\"Section 5.4\\\"\\n    aspect_ratio: \\\"1:1\\\"\\n    tool: \\\"matplotlib\\\"\\n    data_source: \\\"registry: exp-006 IRT calibration results (ARC S1-only 4PL+γ, GSM8K 2PL+γ)\\\"\\n    output: \\\"figures/paper/fig_calibration.pdf\\\"\\n\\ntable_plan:\\n  table_gamma:\\n    type: \\\"parameter_summary\\\"\\n    description: \\\"Per-benchmark IRT γ estimates with diagnostics\\\"\\n    columns: [\\\"Benchmark\\\", \\\"Model\\\", \\\"γ̂\\\", \\\"95% CI\\\", \\\"Excludes 0?\\\", \\\"R̂\\\", \\\"ESS\\\", \\\"PPP\\\", \\\"Direction\\\"]\\n    data_source: \\\"exp-006 per-benchmark IRT fits\\\"\\n    placement: \\\"Section 5.1\\\"\\n    rows:\\n      - \\\"ARC (S1, 4PL+γ): γ=-1.46 [-2.51, -0.41] ✓ 1.010 770 TBD Forgetting\\\"\\n      - \\\"ARC (oracle, 2PL+γ): γ=-0.62 [-1.04, -0.20] ✓ 1.006 1512 TBD Forgetting\\\"\\n      - \\\"GSM8K (oracle, 4PL+γ): γ=3.77 [2.74, 4.71] ✓ 1.002 1222 TBD Inflation\\\"\\n      - \\\"GSM8K (S1, 2PL+γ): γ=0.14 [-0.31, 0.59] ✗ 1.002 3604 0.284 —\\\"\\n      - \\\"GSM8K (S1, 4PL+γ): γ=0.19 [-0.92, 1.33] ✗ 1.015 330 TBD — (convergence issue)\\\"\\n      - \\\"MMLU (RRF): FAILED (R̂=1.54, ESS=7)\\\"\\n      - \\\"[PENDING-3B] rows\\\"\\n\\n  table_baselines:\\n    type: \\\"comparison\\\"\\n    description: \\\"Calibration performance: ContamCal vs 7 baselines\\\"\\n    columns: [\\\"Method\\\", \\\"ARC MAE↓\\\", \\\"ARC τ↑\\\", \\\"ARC C95%\\\", \\\"GSM8K MAE↓\\\", \\\"GSM8K τ↑\\\"]\\n    data_source: \\\"exp-006 baseline comparisons\\\"\\n    placement: \\\"Section 5.4\\\"\\n    notes: \\\"ARC is success case. GSM8K shows gating criterion necessity. MMLU excluded (failed).\\\"\\n\\n  table_signal_summary:\\n    type: \\\"signal_evaluation\\\"\\n    description: \\\"Signal effectiveness by scale × benchmark\\\"\\n    columns: [\\\"Signal\\\", \\\"Scale\\\", \\\"d005 AUC\\\", \\\"d025 AUC\\\", \\\"d100 Cohen's d\\\"]\\n    data_source: \\\"exp-008\\\"\\n    placement: \\\"Section 5.2 or Appendix\\\"\\n    notes: \\\"May merge into fig_signal_heatmap. Keep as table if space allows.\\\"\\n\\nliterature_strategy:\\n  citation_budget: \\\"40-50 total\\\"\\n  macro_context: \\\"Contamination is a systemic threat; detection exists but calibration doesn't; educational measurement solved the analogous exam leak problem decades ago.\\\"\\n  micro_clusters:\\n    contamination_detection:\\n      target_count: 8\\n      must_cite: [\\\"zhang2024minkpp\\\", \\\"dekoninck2024constat\\\", \\\"dong2024kds\\\", \\\"shi2024cdd\\\", \\\"weller2024selfcritique\\\", \\\"golchin2024time\\\"]\\n      search_queries: [\\\"benchmark contamination detection LLM\\\", \\\"membership inference LLM evaluation\\\"]\\n    irt_for_llm:\\n      target_count: 6\\n      must_cite: [\\\"lalor2024aaai\\\", \\\"polo2024tinybenchmarks\\\", \\\"burnell2023multidimensional\\\"]\\n      search_queries: [\\\"item response theory large language model evaluation\\\", \\\"psychometric LLM benchmark\\\"]\\n    item_compromise_irt:\\n      target_count: 5\\n      must_cite: [\\\"eckerly2017\\\", \\\"sinharay2017\\\", \\\"deboeck2004\\\", \\\"holland1993dif\\\", \\\"adams1997\\\"]\\n      search_queries: [\\\"item compromise IRT detection\\\", \\\"differential item functioning preknowledge\\\"]\\n    benchmark_reliability:\\n      target_count: 5\\n      must_cite: [\\\"livebench2024\\\", \\\"empcloths2025\\\", \\\"zheng2023chatbot\\\", \\\"liang2023helm\\\"]\\n      search_queries: [\\\"benchmark reliability LLM contamination mitigation\\\", \\\"dynamic benchmark evaluation\\\"]\\n    calibration_uq:\\n      target_count: 4\\n      must_cite: [\\\"guo2017calibration\\\", \\\"angelopoulos2023conformal\\\", \\\"talts2018sbc\\\"]\\n      search_queries: [\\\"calibration uncertainty quantification neural network\\\", \\\"simulation based calibration Bayesian\\\"]\\n    mia_foundations:\\n      target_count: 3\\n      must_cite: [\\\"shokri2017membership\\\", \\\"carlini2022extracting\\\"]\\n      search_queries: [\\\"membership inference attack training data extraction\\\"]\\n    contamination_mitigation:\\n      target_count: 4\\n      must_cite: [\\\"oren2024dcr\\\"]\\n      search_queries: [\\\"benchmark contamination mitigation adjusted accuracy\\\", \\\"decontamination LLM evaluation\\\"]\\n    data_attribution:\\n      target_count: 2\\n      must_cite: []\\n      search_queries: [\\\"data attribution influence functions LLM\\\"]\\n      notes: \\\"Future work mention only. TracIn (Pruthi 2020), TRAK (Park 2023).\\\"\\n    irt_methodology:\\n      target_count: 3\\n      must_cite: [\\\"sanmartin2009\\\", \\\"maris2009\\\", \\\"reckase2009\\\"]\\n      search_queries: [\\\"IRT identifiability four parameter logistic\\\", \\\"multidimensional IRT\\\"]\\n\\nwriting_order:\\n  - section: \\\"method\\\"\\n    rationale: \\\"No data dependency. Sets notation for all downstream sections.\\\"\\n  - section: \\\"experimental_setup\\\"\\n    rationale: \\\"Defines experimental design. Needed by results.\\\"\\n  - section: \\\"results\\\"\\n    rationale: \\\"Core empirical contribution. Needs method + setup.\\\"\\n  - section: \\\"related_work\\\"\\n    rationale: \\\"Needs literature_map from Step 3. Positions against prior work.\\\"\\n  - section: \\\"discussion\\\"\\n    rationale: \\\"Needs results to discuss limitations and implications.\\\"\\n  - section: \\\"introduction\\\"\\n    rationale: \\\"Needs full picture to frame contributions precisely.\\\"\\n  - section: \\\"conclusion\\\"\\n    rationale: \\\"Summarizes all. Write after intro.\\\"\\n  - section: \\\"abstract\\\"\\n    rationale: \\\"Write last. Distills entire paper.\\\"\\n\\ndata_availability:\\n  available_now:\\n    - \\\"0.5B: all dosages × 2 seeds, SFT + eval + signals complete\\\"\\n    - \\\"1.5B: all dosages × 2 seeds, SFT + eval + signals (12/12) complete\\\"\\n    - \\\"exp-004 sim_sweep: v5 partial (59/120 seeds), v6/v7 running\\\"\\n    - \\\"exp-006 IRT: ARC S1 4PL+γ, GSM8K oracle/S1 4PL+γ/2PL+γ, ARC oracle 2PL+γ\\\"\\n    - \\\"exp-008 signal eval: 0.5B complete, 1.5B complete\\\"\\n    - \\\"exp-005 noise_prop: v4 DONE (negative)\\\"\\n  pending:\\n    - \\\"3B: SFTs running (~2-3 days), signals after GPU release (~1 day) → [PENDING-3B]\\\"\\n    - \\\"exp-004 sim_sweep: AUC=0.65 and AUC=0.9 conditions incomplete\\\"\\n    - \\\"exp-006: per-benchmark IRT with D045 exclusions (0.5B MMLU/ARC removed) — may need rerun\\\"\\n  excluded_from_paper:\\n    - \\\"7B/72B (D060: rebuttal)\\\"\\n    - \\\"Multi-family Llama/Pythia (exp-014: rebuttal)\\\"\\n    - \\\"RL observational (exp-009: rebuttal)\\\"\\n    - \\\"Closed-weight (rebuttal)\\\"\\n\\ndata_constraints:  # Updated 2026-05-15\\n  alpha_note: \\\"D055 alpha 混用约束已撤回。所有 checkpoint 实际 lora_alpha=32（train_sft.py bug 忽略 CLI 参数）。跨种子数据可统一处理。\\\"\\n  gsm8k_d005_s123: \\\"暂不可用（63.08% 异常，正在调查）。其他维度正常。\\\"\\n\\nkey_decisions:\\n  - \\\"D039: Characterization-led framing, calibration demoted to Claim 4\\\"\\n  - \\\"D045: Exclude 0.5B MMLU/ARC from IRT (position bias)\\\"\\n  - \\\"D053: Per-benchmark independent IRT only (joint/stratified废弃)\\\"\\n  - \\\"D055: WITHDRAWN — alpha 混用问题不存在，所有 checkpoint alpha=32\\\"\\n  - \\\"D056: Coverage collapse = model misspecification (honest negative)\\\"\\n  - \\\"D060: P1/P2 experiments → rebuttal scope\\\"\\n\", \"total_chars\": 16926, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018exrvhBCRBMtt3mh3pq6iH`</summary>

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
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "3f24f3fd-e3a5-4d01-a519-934a81d0df0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XuZCTXQSMPxsXzmc7ysKJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
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

_source line 14 · 2026-05-16T16:54:49.808Z_

<details><summary>↩ Tool result · `toolu_018exrvhBCRBMtt3mh3pq6iH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Memory — contamcal-irt-calibration\\n\\n## 1. 研究方向与核心发现\\n\\n- **ContamCal**: contamination-augmented IRT with per-benchmark γ_k\\n- **D108 核心发现**: MMLU 57 subjects → 8 cognitive domains，aggregate γ≈0 masks domain heterogeneity (Simpson's paradox)。7/8 domains 完成 (Medical excluded due PPP=1.0 misfit)\\n- **D116**: Pooled IRT N=25 confirms Simpson's Paradox — aggregate γ 被 domain heterogeneity mask\\n- **D111**: STEM_Math γ 方向在 N=24 时反转——heterogeneity 可能 scale-dependent\\n- **D110**: Scale-stratified IRT (N=6-8 per scale) negative——N 太小不走这条路\\n- **D109**: Aggregate pooled IRT (N=23, 2PL+γ) confirms aggregate γ≈0\\n- **PPP=0 in 4/5 domains** → paper claim 必须基于 pattern/ranking，不能 claim 绝对 γ 值\\n\\n## 2. 论文叙事 (paper_framing)\\n\\n- Claim 1: Domain heterogeneity (Simpson's paradox) — aggregate masks signal\\n- Claim 2: Format dependence — ARC(MC) γ>0 / GSM8K(generative) γ≈0\\n- Claim 3: Identifiability (sim_sweep confirmed, D107)\\n- Cross-family validation via Llama-3.2-3B (D106)\\n- PPP misfit → claim 基于 pattern/ranking not absolute values\\n\\n## 3. 关键约束\\n\\n- **服务器名必须是 `cqa1-21977`**，写 \\\"A6000\\\" 会导致 cron 无法 SSH 验证进程（exp_006 事故教训）\\n- Stan IRT fitting 是 CPU 任务，不占 GPU，但 cron 仍需正确服务器名\\n- submit_training_job 有时不自动推进 PREPARING→RUNNING（需手动修正 + 注册 cron）\\n- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 工作目录：exp006 在 `/root/autodl-tmp/exp006/`，exp001/002 在 `/root/autodl-tmp/exp001/` & `/root/autodl-tmp/exp002/`\\n\\n## 4. 文献支撑 (2026-05-16 补充)\\n\\n- Brown & Thomson (2024): PPP 分布非均匀，low PPP 不自动否定参数估计 → 支持 ARC PPP=0.003 + γ 显著的可解释性\\n- Deng et al. (NAACL 2024): TS-Guessing MC contamination 敏感性 57% → 支持 MC format dependence\\n- Schaeffer et al. (2026): scaling law + generative contamination → 支持 GSM8K γ≈0\\n- Kievit et al. (2013): Simpson's paradox 理论框架 → D108 直接类比\\n- Ercikan et al. (2008): DIF cancellation 实证 → domain-level 发现的先例\\n\\n## 5. GPU State (as of 16:14 UTC)\\n\\n- cqa1-21977: 6× RTX 4090D allocated, ALL RUNNING\\n- cuda:0: Llama-3.2-3B d005 SFT (PID 804565, cron active)\\n- cuda:1: Llama-3.2-3B d000 eval v3 (PID 807025, cron active)\\n- cuda:2: 0.5B-Instruct eval (cron active)\\n- cuda:3: Llama-3.2-3B d025 SFT (PID 801761, cron active)\\n- cuda:4: 1.5B signals / 2PL ablation (Worker managed)\\n- cuda:5: Llama-3.2-3B d100 SFT (PID 804786, cron active)\\n\\n## 6. Llama Cross-Family Pipeline (D106)\\n\\n- d000 SFT: ✅ DONE → eval v3 running (cuda:1)\\n- d005 SFT: 🔄 RUNNING (cuda:0)\\n- d025 SFT: 🔄 RUNNING (cuda:3)\\n- d100 SFT: 🔄 RUNNING (cuda:5)\\n- 完成后：eval → signals → RRF → cross-family pooled IRT\\n\\n## 7. 经验教训\\n\\n- [2026-05-16] submit_training_job 偶尔不推进状态到 RUNNING（C002 已知 bug），需 session 启动时 reconcile + 手动修正\\n- [2026-05-16] cron 注册时 PID 必须匹配实际进程，否则进程结束会误触发 done\\n- [2026-05-16] resource_usage 工具 PID/tmux 不匹配可导致误判 GPU idle（用 nvidia-smi 直接确认）\\n\\n## 8. Ablation: 2PL+γ vs vanilla 2PL (2026-05-17)\\n\\n**目的**: 验证 pooled level gamma 是否有校准贡献。\\n\\n**结果（相同 N=13 数据，apples-to-apples）**:\\n\\n| Benchmark | Model | N | raw_MAE | cal_MAE | ΔMAE | PPP |\\n|-----------|-------|---|---------|---------|------|-----|\\n| MMLU | 2PL+γ | 13 | 0.0140 | 0.0051 | 0.0089 | — |\\n| MMLU | vanilla 2PL | 13 | 0.0140 | **0.0036** | 0.0104 | 0.344 |\\n| ARC | 2PL+γ | 13 | 0.0324 | 0.0229 | 0.0094 | — |\\n| ARC | vanilla 2PL | 13 | 0.0324 | **0.0117** | 0.0207 | 0.054 |\\n| GSM8K | 2PL+γ* | 24 | 0.1694 | **0.0062** | 0.1632 | 0.541 |\\n| GSM8K | vanilla 2PL | 21 | 0.1470 | 0.0087 | 0.1384 | 0.475 |\\n\\n*GSM8K 2pl_gamma rerun (N=21) 因 chain 3/4 sampling error 失败，使用原始 N=24 运行结果。\\n\\n**结论**: 在 MMLU 和 ARC 上，vanilla 2PL 的 cal_MAE 反而更低（更好校准），说明 pooled-level gamma 没有正向贡献，甚至因过参数化引入噪声。这强力支持论文 Claim 1：**aggregate γ≈0 是 Simpson's paradox 的结果，gamma 的价值只有在 domain-level 才体现。**\\n\\n**输出路径**:\\n- vanilla 2PL: `/root/autodl-tmp/exp006/pooled_irt_vanilla_2pl_n16/`\\n- 2pl_gamma rerun: `/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16_rerun/`\\n\\n**Domain-level N=24 状态**: mmlu_domain_gamma_n24_v2 因 sampling error 失败（需排查）。\\n\", \"total_chars\": 3833, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "0f96178d-36b0-44ca-a57b-10670c83ae44",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\\\", \\\"content\\\": \\\"# Memory — contamcal-irt-calibration\\\\n\\\\n## 1. 研究方向与核心发现\\\\n\\\\n- **ContamCal**: contamination-augmented IRT with per-benchmark γ_k\\\\n- **D108 核心发现**: MMLU 57 subjects → 8 cognitive domains，aggregate γ≈0 masks domain heterogeneity (Simpson's paradox)。7/8 domains 完成 (Medical excluded due PPP=1.0 misfit)\\\\n- **D116**: Pooled IRT N=25 confirms Simpson's Paradox — aggregate γ 被 domain heterogeneity mask\\\\n- **D111**: STEM_Math γ 方向在 N=24 时反转——heterogeneity 可能 scale-dependent\\\\n- **D110**: Scale-stratified IRT (N=6-8 per scale) negative——N 太小不走这条路\\\\n- **D109**: Aggregate pooled IRT (N=23, 2PL+γ) confirms aggregate γ≈0\\\\n- **PPP=0 in 4/5 domains** → paper claim 必须基于 pattern/ranking，不能 claim 绝对 γ 值\\\\n\\\\n## 2. 论文叙事 (paper_framing)\\\\n\\\\n- Claim 1: Domain heterogeneity (Simpson's paradox) — aggregate masks signal\\\\n- Claim 2: Format dependence — ARC(MC) γ>0 / GSM8K(generative) γ≈0\\\\n- Claim 3: Identifiability (sim_sweep confirmed, D107)\\\\n- Cross-family validation via Llama-3.2-3B (D106)\\\\n- PPP misfit → claim 基于 pattern/ranking not absolute values\\\\n\\\\n## 3. 关键约束\\\\n\\\\n- **服务器名必须是 `cqa1-21977`**，写 \\\\\\\"A6000\\\\\\\" 会导致 cron 无法 SSH 验证进程（exp_006 事故教训）\\\\n- Stan IRT fitting 是 CPU 任务，不占 GPU，但 cron 仍需正确服务器名\\\\n- submit_training_job 有时不自动推进 PREPARING→RUNNING（需手动修正 + 注册 cron）\\\\n- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\\\n- 工作目录：exp006 在 `/root/autodl-tmp/exp006/`，exp001/002 在 `/root/autodl-tmp/exp001/` & `/root/autodl-tmp/exp002/`\\\\n\\\\n## 4. 文献支撑 (2026-05-16 补充)\\\\n\\\\n- Brown & Thomson (2024): PPP 分布非均匀，low PPP 不自动否定参数估计 → 支持 ARC PPP=0.003 + γ 显著的可解释性\\\\n- Deng et al. (NAACL 2024): TS-Guessing MC contamination 敏感性 57% → 支持 MC format dependence\\\\n- Schaeffer et al. (2026): scaling law + generative contamination → 支持 GSM8K γ≈0\\\\n- Kievit et al. (2013): Simpson's paradox 理论框架 → D108 直接类比\\\\n- Ercikan et al. (2008): DIF cancellation 实证 → domain-level 发现的先例\\\\n\\\\n## 5. GPU State (as of 16:14 UTC)\\\\n\\\\n- cqa1-21977: 6× RTX 4090D allocated, ALL RUNNING\\\\n- cuda:0: Llama-3.2-3B d005 SFT (PID 804565, cron active)\\\\n- cuda:1: Llama-3.2-3B d000 eval v3 (PID 807025, cron active)\\\\n- cuda:2: 0.5B-Instruct eval (cron active)\\\\n- cuda:3: Llama-3.2-3B d025 SFT (PID 801761, cron active)\\\\n- cuda:4: 1.5B signals / 2PL ablation (Worker managed)\\\\n- cuda:5: Llama-3.2-3B d100 SFT (PID 804786, cron active)\\\\n\\\\n## 6. Llama Cross-Family Pipeline (D106)\\\\n\\\\n- d000 SFT: ✅ DONE → eval v3 running (cuda:1)\\\\n- d005 SFT: 🔄 RUNNING (cuda:0)\\\\n- d025 SFT: 🔄 RUNNING (cuda:3)\\\\n- d100 SFT: 🔄 RUNNING (cuda:5)\\\\n- 完成后：eval → signals → RRF → cross-family pooled IRT\\\\n\\\\n## 7. 经验教训\\\\n\\\\n- [2026-05-16] submit_training_job 偶尔不推进状态到 RUNNING（C002 已知 bug），需 session 启动时 reconcile + 手动修正\\\\n- [2026-05-16] cron 注册时 PID 必须匹配实际进程，否则进程结束会误触发 done\\\\n- [2026-05-16] resource_usage 工具 PID/tmux 不匹配可导致误判 GPU idle（用 nvidia-smi 直接确认）\\\\n\\\\n## 8. Ablation: 2PL+γ vs vanilla 2PL (2026-05-17)\\\\n\\\\n**目的**: 验证 pooled level gamma 是否有校准贡献。\\\\n\\\\n**结果（相同 N=13 数据，apples-to-apples）**:\\\\n\\\\n| Benchmark | Model | N | raw_MAE | cal_MAE | ΔMAE | PPP |\\\\n|-----------|-------|---|---------|---------|------|-----|\\\\n| MMLU | 2PL+γ | 13 | 0.0140 | 0.0051 | 0.0089 | — |\\\\n| MMLU | vanilla 2PL | 13 | 0.0140 | **0.0036** | 0.0104 | 0.344 |\\\\n| ARC | 2PL+γ | 13 | 0.0324 | 0.0229 | 0.0094 | — |\\\\n| ARC | vanilla 2PL | 13 | 0.0324 | **0.0117** | 0.0207 | 0.054 |\\\\n| GSM8K | 2PL+γ* | 24 | 0.1694 | **0.0062** | 0.1632 | 0.541 |\\\\n| GSM8K | vanilla 2PL | 21 | 0.1470 | 0.0087 | 0.1384 | 0.475 |\\\\n\\\\n*GSM8K 2pl_gamma rerun (N=21) 因 chain 3/4 sampling error 失败，使用原始 N=24 运行结果。\\\\n\\\\n**结论**: 在 MMLU 和 ARC 上，vanilla 2PL 的 cal_MAE 反而更低（更好校准），说明 pooled-level gamma 没有正向贡献，甚至因过参数化引入噪声。这强力支持论文 Claim 1：**aggregate γ≈0 是 Simpson's paradox 的结果，gamma 的价值只有在 domain-level 才体现。**\\\\n\\\\n**输出路径**:\\\\n- vanilla 2PL: `/root/autodl-tmp/exp006/pooled_irt_vanilla_2pl_n16/`\\\\n- 2pl_gamma rerun: `/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16_rerun/`\\\\n\\\\n**Domain-level N=24 状态**: mmlu_domain_gamma_n24_v2 因 sampling error 失败（需排查）。\\\\n\\\", \\\"total_chars\\\": 3833, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Memory — contamcal-irt-calibration\\n\\n## 1. 研究方向与核心发现\\n\\n- **ContamCal**: contamination-augmented IRT with per-benchmark γ_k\\n- **D108 核心发现**: MMLU 57 subjects → 8 cognitive domains，aggregate γ≈0 masks domain heterogeneity (Simpson's paradox)。7/8 domains 完成 (Medical excluded due PPP=1.0 misfit)\\n- **D116**: Pooled IRT N=25 confirms Simpson's Paradox — aggregate γ 被 domain heterogeneity mask\\n- **D111**: STEM_Math γ 方向在 N=24 时反转——heterogeneity 可能 scale-dependent\\n- **D110**: Scale-stratified IRT (N=6-8 per scale) negative——N 太小不走这条路\\n- **D109**: Aggregate pooled IRT (N=23, 2PL+γ) confirms aggregate γ≈0\\n- **PPP=0 in 4/5 domains** → paper claim 必须基于 pattern/ranking，不能 claim 绝对 γ 值\\n\\n## 2. 论文叙事 (paper_framing)\\n\\n- Claim 1: Domain heterogeneity (Simpson's paradox) — aggregate masks signal\\n- Claim 2: Format dependence — ARC(MC) γ>0 / GSM8K(generative) γ≈0\\n- Claim 3: Identifiability (sim_sweep confirmed, D107)\\n- Cross-family validation via Llama-3.2-3B (D106)\\n- PPP misfit → claim 基于 pattern/ranking not absolute values\\n\\n## 3. 关键约束\\n\\n- **服务器名必须是 `cqa1-21977`**，写 \\\"A6000\\\" 会导致 cron 无法 SSH 验证进程（exp_006 事故教训）\\n- Stan IRT fitting 是 CPU 任务，不占 GPU，但 cron 仍需正确服务器名\\n- submit_training_job 有时不自动推进 PREPARING→RUNNING（需手动修正 + 注册 cron）\\n- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 工作目录：exp006 在 `/root/autodl-tmp/exp006/`，exp001/002 在 `/root/autodl-tmp/exp001/` & `/root/autodl-tmp/exp002/`\\n\\n## 4. 文献支撑 (2026-05-16 补充)\\n\\n- Brown & Thomson (2024): PPP 分布非均匀，low PPP 不自动否定参数估计 → 支持 ARC PPP=0.003 + γ 显著的可解释性\\n- Deng et al. (NAACL 2024): TS-Guessing MC contamination 敏感性 57% → 支持 MC format dependence\\n- Schaeffer et al. (2026): scaling law + generative contamination → 支持 GSM8K γ≈0\\n- Kievit et al. (2013): Simpson's paradox 理论框架 → D108 直接类比\\n- Ercikan et al. (2008): DIF cancellation 实证 → domain-level 发现的先例\\n\\n## 5. GPU State (as of 16:14 UTC)\\n\\n- cqa1-21977: 6× RTX 4090D allocated, ALL RUNNING\\n- cuda:0: Llama-3.2-3B d005 SFT (PID 804565, cron active)\\n- cuda:1: Llama-3.2-3B d000 eval v3 (PID 807025, cron active)\\n- cuda:2: 0.5B-Instruct eval (cron active)\\n- cuda:3: Llama-3.2-3B d025 SFT (PID 801761, cron active)\\n- cuda:4: 1.5B signals / 2PL ablation (Worker managed)\\n- cuda:5: Llama-3.2-3B d100 SFT (PID 804786, cron active)\\n\\n## 6. Llama Cross-Family Pipeline (D106)\\n\\n- d000 SFT: ✅ DONE → eval v3 running (cuda:1)\\n- d005 SFT: 🔄 RUNNING (cuda:0)\\n- d025 SFT: 🔄 RUNNING (cuda:3)\\n- d100 SFT: 🔄 RUNNING (cuda:5)\\n- 完成后：eval → signals → RRF → cross-family pooled IRT\\n\\n## 7. 经验教训\\n\\n- [2026-05-16] submit_training_job 偶尔不推进状态到 RUNNING（C002 已知 bug），需 session 启动时 reconcile + 手动修正\\n- [2026-05-16] cron 注册时 PID 必须匹配实际进程，否则进程结束会误触发 done\\n- [2026-05-16] resource_usage 工具 PID/tmux 不匹配可导致误判 GPU idle（用 nvidia-smi 直接确认）\\n\\n## 8. Ablation: 2PL+γ vs vanilla 2PL (2026-05-17)\\n\\n**目的**: 验证 pooled level gamma 是否有校准贡献。\\n\\n**结果（相同 N=13 数据，apples-to-apples）**:\\n\\n| Benchmark | Model | N | raw_MAE | cal_MAE | ΔMAE | PPP |\\n|-----------|-------|---|---------|---------|------|-----|\\n| MMLU | 2PL+γ | 13 | 0.0140 | 0.0051 | 0.0089 | — |\\n| MMLU | vanilla 2PL | 13 | 0.0140 | **0.0036** | 0.0104 | 0.344 |\\n| ARC | 2PL+γ | 13 | 0.0324 | 0.0229 | 0.0094 | — |\\n| ARC | vanilla 2PL | 13 | 0.0324 | **0.0117** | 0.0207 | 0.054 |\\n| GSM8K | 2PL+γ* | 24 | 0.1694 | **0.0062** | 0.1632 | 0.541 |\\n| GSM8K | vanilla 2PL | 21 | 0.1470 | 0.0087 | 0.1384 | 0.475 |\\n\\n*GSM8K 2pl_gamma rerun (N=21) 因 chain 3/4 sampling error 失败，使用原始 N=24 运行结果。\\n\\n**结论**: 在 MMLU 和 ARC 上，vanilla 2PL 的 cal_MAE 反而更低（更好校准），说明 pooled-level gamma 没有正向贡献，甚至因过参数化引入噪声。这强力支持论文 Claim 1：**aggregate γ≈0 是 Simpson's paradox 的结果，gamma 的价值只有在 domain-level 才体现。**\\n\\n**输出路径**:\\n- vanilla 2PL: `/root/autodl-tmp/exp006/pooled_irt_vanilla_2pl_n16/`\\n- 2pl_gamma rerun: `/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16_rerun/`\\n\\n**Domain-level N=24 状态**: mmlu_domain_gamma_n24_v2 因 sampling error 失败（需排查）。\\n\", \"total_chars\": 3833, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AE7Y6NgtT4Dnr2dMatR4z4`</summary>

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
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "1e0e2379-9688-4bf1-add1-778f3bf7e2e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XuZCTXQSMPxsXzmc7ysKJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
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

_source line 16 · 2026-05-16T16:54:50.214Z_

<details><summary>↩ Tool result · `toolu_01AE7Y6NgtT4Dnr2dMatR4z4`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-16 10:26 UTC | 更新原因: Reviewer critical: 修正d005 false failure + D108措辞降级为domain heterogeneity evidence + GPU状态同步\\n\\n## 核心方向\\nContamCal：contamination-augmented IRT with per-benchmark γ_k → domain heterogeneity evidence (Simpson's paradox, D108)。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（距今 9 天）\\n\\n## 当前进展\\n- **阶段**: Research (MVP 2026-05-13 通过) + 审稿进行中\\n- **D108 发现**: MMLU 57 subjects → 8 cognitive domains，aggregate γ≈0 masks domain heterogeneity (5 domains significant, γ range: -0.55 to +1.34)。PPP=0 in 4/5 domains → claim 基于 pattern/ranking，非绝对值。N=24 重跑确认前为\\\"evidence of heterogeneity\\\"\\n- **3B s42 signals**: d000 ✅ d005 ✅ d025 ✅ d100 🔄(cuda:1, ~35min)。d100 完成后全齐 → RRF\\n- **0.5B s123**: 全部完成 ✅\\n- **1.5B s123**: d025 running (cuda:0), d100 running (cuda:2)。完成后全量 RRF (N≥16+)\\n- **Scope expansion (D106)**: Llama 代码+模型就绪 | RL observational 3B-Instruct eval running (cuda:3) | 7B 待云GPU\\n\\n## GPU 实时占用 (6× RTX 4090D, cqa1-21977)\\n| GPU | 任务 | 预计完成 |\\n|-----|------|---------|\\n| cuda:0 | signals_15B_s123_batch (d025) | ~2h |\\n| cuda:1 | signals_3B_d100_a32_s42 | ~35min |\\n| cuda:2 | signals_15B_d100_s123 | ~3h |\\n| cuda:3 | eval_3B_instruct_aligned_para (P0-C) | ~1h |\\n| cuda:4 | **待分配 → Llama-3.2-3B d000 SFT** | 指令已发 |\\n| cuda:5 | signals_05B_s123_v2 (d100) | ~2.5h |\\n\\n## Critical Path (EMNLP T-9)\\n```\\n[Now]     cuda:1 d100 ~35min → 3B s42 全齐 → RRF 聚合 (CPU)\\n          cuda:4 → Llama-3.2-3B d000 SFT 启动\\n          cuda:3 3B-Instruct eval ~1h → 0.5B/1.5B-Instruct eval\\n[Day 1]   pooled IRT (N≥16+) — 论文核心 γ 数字\\n          MMLU domain gamma N=24 (含 3B) — 确认 heterogeneity 是否 scale-dependent\\n          Llama d000 SFT + eval\\n[Day 2]   Llama d005/d025/d100 SFT + eval + signals\\n          scale-stratified IRT\\n[Day 3-5] Paper Agent Full Draft\\n[Day 5-7] Review 迭代 + Llama 结果补充\\n[Day 7-9] 最终提交\\n```\\n\\n## ⚠️ 风险项\\n1. **PPP=0 in domain gamma (4/5 domains)** — 绝对 γ 值不可信，paper 需基于 pattern/ranking claim。N=24 重跑是关键验证\\n2. **7B 云 GPU 未批** — 已向 Manager 申请 A100-80G，等待回复\\n3. **T-9 Llama 窗口紧** — 需 Day 2 完成 d000 SFT+eval+signals 才能赶上论文数据冻结\\n4. **Coverage collapse (D056)** — per-benchmark γ_k + N↑ 是主要缓解路径\\n\\n## 近期任务\\n- [ ] cuda:4 → Llama-3.2-3B d000 SFT（指令已发）\\n- [ ] 3B d100 完成 → RRF 聚合 → pooled IRT (N≥16+)\\n- [ ] MMLU domain gamma N=24 (含 3B)\\n- [ ] cuda:3 释放 → 0.5B/1.5B-Instruct eval (P0-C)\\n- [ ] 1.5B s123 全完成 → 完整 RRF (全种子)\\n- [ ] scale-stratified IRT\\n- [ ] paper_framing.md D108 措辞审慎化（等 N=24 确认）\\n- [x] 3B d005 signals 确认完成（cron false positive，非真实失败）\\n- [x] MMLU domain gamma 初步完成 — Simpson's paradox confirmed\\n- [x] sim_sweep_v7 完成 — Claim 3 identifiability 确认 (D090/D107)\\n- [x] Scope expansion 方案批准 (D106)\\n\\n## GPU 预算\\n6× RTX 4090D 全项目分配。7B 需云 GPU (A100-80G ×1, ~4h)，已申请。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D117 | 2026-05-16 | D117: Claim 1 scope narrowed — only Math+Science d | exp_006_mmlu_domain_gamma_n24_v4 |\\n| D116 | 2026-05-16 | D116: Pooled IRT confirms Simpson's Paradox — aggr | exp_006_pooled_irt_rrf_n25_v2, exp_006_mmlu_domain_gamma_n24_v4 |\\n| D115 | 2026-05-16 | D115: D108 complete (7/8 domains) — STEM gradient  | exp_006_mmlu_domain_gamma_n24_v4 |\\n| D114 | 2026-05-16 | D114: D108 domain gamma claim scoped to STEM-only  | exp_006_mmlu_domain_gamma_n24_v4 |\\n| D113 | 2026-05-16 | D113: 3B-Instruct eval v2 confirms chat_template f | exp_001_eval_3B_instruct_v2 |\\n| D112 | 2026-05-16 | D112: Medical domain PPP=1.0 model misfit — exclud | exp_006_mmlu_domain_gamma_n24 |\\n| D111 | 2026-05-16 | D111: STEM_Math γ direction reversal at N=24 — pau | exp_006_mmlu_domain_gamma_n24 |\\n| D110 | 2026-05-16 | D110: Scale-stratified IRT (N=6-8 per scale) negat | exp_006_scale_stratified_irt |\\n| D109 | 2026-05-16 | D109: Aggregate pooled IRT (N=23, 2PL+γ) confirms  | exp_006_pooled_irt_all_scales |\\n| D108 | 2026-05-16 | D108: Claim 1 升级 — 从 benchmark-dependent 升级为 domai | exp_006_mmlu_domain_gamma |\\n\\n\", \"total_chars\": 3883, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "2eb75187-a9b1-4d5b-b98a-5fc387589f94",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\\\", \\\"content\\\": \\\"# contamcal-irt-calibration — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-16 10:26 UTC | 更新原因: Reviewer critical: 修正d005 false failure + D108措辞降级为domain heterogeneity evidence + GPU状态同步\\\\n\\\\n## 核心方向\\\\nContamCal：contamination-augmented IRT with per-benchmark γ_k → domain heterogeneity evidence (Simpson's paradox, D108)。详见 paper_framing.md。\\\\n\\\\n## 投稿目标\\\\n**EMNLP 2026 ARR May 25**（距今 9 天）\\\\n\\\\n## 当前进展\\\\n- **阶段**: Research (MVP 2026-05-13 通过) + 审稿进行中\\\\n- **D108 发现**: MMLU 57 subjects → 8 cognitive domains，aggregate γ≈0 masks domain heterogeneity (5 domains significant, γ range: -0.55 to +1.34)。PPP=0 in 4/5 domains → claim 基于 pattern/ranking，非绝对值。N=24 重跑确认前为\\\\\\\"evidence of heterogeneity\\\\\\\"\\\\n- **3B s42 signals**: d000 ✅ d005 ✅ d025 ✅ d100 🔄(cuda:1, ~35min)。d100 完成后全齐 → RRF\\\\n- **0.5B s123**: 全部完成 ✅\\\\n- **1.5B s123**: d025 running (cuda:0), d100 running (cuda:2)。完成后全量 RRF (N≥16+)\\\\n- **Scope expansion (D106)**: Llama 代码+模型就绪 | RL observational 3B-Instruct eval running (cuda:3) | 7B 待云GPU\\\\n\\\\n## GPU 实时占用 (6× RTX 4090D, cqa1-21977)\\\\n| GPU | 任务 | 预计完成 |\\\\n|-----|------|---------|\\\\n| cuda:0 | signals_15B_s123_batch (d025) | ~2h |\\\\n| cuda:1 | signals_3B_d100_a32_s42 | ~35min |\\\\n| cuda:2 | signals_15B_d100_s123 | ~3h |\\\\n| cuda:3 | eval_3B_instruct_aligned_para (P0-C) | ~1h |\\\\n| cuda:4 | **待分配 → Llama-3.2-3B d000 SFT** | 指令已发 |\\\\n| cuda:5 | signals_05B_s123_v2 (d100) | ~2.5h |\\\\n\\\\n## Critical Path (EMNLP T-9)\\\\n```\\\\n[Now]     cuda:1 d100 ~35min → 3B s42 全齐 → RRF 聚合 (CPU)\\\\n          cuda:4 → Llama-3.2-3B d000 SFT 启动\\\\n          cuda:3 3B-Instruct eval ~1h → 0.5B/1.5B-Instruct eval\\\\n[Day 1]   pooled IRT (N≥16+) — 论文核心 γ 数字\\\\n          MMLU domain gamma N=24 (含 3B) — 确认 heterogeneity 是否 scale-dependent\\\\n          Llama d000 SFT + eval\\\\n[Day 2]   Llama d005/d025/d100 SFT + eval + signals\\\\n          scale-stratified IRT\\\\n[Day 3-5] Paper Agent Full Draft\\\\n[Day 5-7] Review 迭代 + Llama 结果补充\\\\n[Day 7-9] 最终提交\\\\n```\\\\n\\\\n## ⚠️ 风险项\\\\n1. **PPP=0 in domain gamma (4/5 domains)** — 绝对 γ 值不可信，paper 需基于 pattern/ranking claim。N=24 重跑是关键验证\\\\n2. **7B 云 GPU 未批** — 已向 Manager 申请 A100-80G，等待回复\\\\n3. **T-9 Llama 窗口紧** — 需 Day 2 完成 d000 SFT+eval+signals 才能赶上论文数据冻结\\\\n4. **Coverage collapse (D056)** — per-benchmark γ_k + N↑ 是主要缓解路径\\\\n\\\\n## 近期任务\\\\n- [ ] cuda:4 → Llama-3.2-3B d000 SFT（指令已发）\\\\n- [ ] 3B d100 完成 → RRF 聚合 → pooled IRT (N≥16+)\\\\n- [ ] MMLU domain gamma N=24 (含 3B)\\\\n- [ ] cuda:3 释放 → 0.5B/1.5B-Instruct eval (P0-C)\\\\n- [ ] 1.5B s123 全完成 → 完整 RRF (全种子)\\\\n- [ ] scale-stratified IRT\\\\n- [ ] paper_framing.md D108 措辞审慎化（等 N=24 确认）\\\\n- [x] 3B d005 signals 确认完成（cron false positive，非真实失败）\\\\n- [x] MMLU domain gamma 初步完成 — Simpson's paradox confirmed\\\\n- [x] sim_sweep_v7 完成 — Claim 3 identifiability 确认 (D090/D107)\\\\n- [x] Scope expansion 方案批准 (D106)\\\\n\\\\n## GPU 预算\\\\n6× RTX 4090D 全项目分配。7B 需云 GPU (A100-80G ×1, ~4h)，已申请。\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D117 | 2026-05-16 | D117: Claim 1 scope narrowed — only Math+Science d | exp_006_mmlu_domain_gamma_n24_v4 |\\\\n| D116 | 2026-05-16 | D116: Pooled IRT confirms Simpson's Paradox — aggr | exp_006_pooled_irt_rrf_n25_v2, exp_006_mmlu_domain_gamma_n24_v4 |\\\\n| D115 | 2026-05-16 | D115: D108 complete (7/8 domains) — STEM gradient  | exp_006_mmlu_domain_gamma_n24_v4 |\\\\n| D114 | 2026-05-16 | D114: D108 domain gamma claim scoped to STEM-only  | exp_006_mmlu_domain_gamma_n24_v4 |\\\\n| D113 | 2026-05-16 | D113: 3B-Instruct eval v2 confirms chat_template f | exp_001_eval_3B_instruct_v2 |\\\\n| D112 | 2026-05-16 | D112: Medical domain PPP=1.0 model misfit — exclud | exp_006_mmlu_domain_gamma_n24 |\\\\n| D111 | 2026-05-16 | D111: STEM_Math γ direction reversal at N=24 — pau | exp_006_mmlu_domain_gamma_n24 |\\\\n| D110 | 2026-05-16 | D110: Scale-stratified IRT (N=6-8 per scale) negat | exp_006_scale_stratified_irt |\\\\n| D109 | 2026-05-16 | D109: Aggregate pooled IRT (N=23, 2PL+γ) confirms  | exp_006_pooled_irt_all_scales |\\\\n| D108 | 2026-05-16 | D108: Claim 1 升级 — 从 benchmark-dependent 升级为 domai | exp_006_mmlu_domain_gamma |\\\\n\\\\n\\\", \\\"total_chars\\\": 3883, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-16 10:26 UTC | 更新原因: Reviewer critical: 修正d005 false failure + D108措辞降级为domain heterogeneity evidence + GPU状态同步\\n\\n## 核心方向\\nContamCal：contamination-augmented IRT with per-benchmark γ_k → domain heterogeneity evidence (Simpson's paradox, D108)。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（距今 9 天）\\n\\n## 当前进展\\n- **阶段**: Research (MVP 2026-05-13 通过) + 审稿进行中\\n- **D108 发现**: MMLU 57 subjects → 8 cognitive domains，aggregate γ≈0 masks domain heterogeneity (5 domains significant, γ range: -0.55 to +1.34)。PPP=0 in 4/5 domains → claim 基于 pattern/ranking，非绝对值。N=24 重跑确认前为\\\"evidence of heterogeneity\\\"\\n- **3B s42 signals**: d000 ✅ d005 ✅ d025 ✅ d100 🔄(cuda:1, ~35min)。d100 完成后全齐 → RRF\\n- **0.5B s123**: 全部完成 ✅\\n- **1.5B s123**: d025 running (cuda:0), d100 running (cuda:2)。完成后全量 RRF (N≥16+)\\n- **Scope expansion (D106)**: Llama 代码+模型就绪 | RL observational 3B-Instruct eval running (cuda:3) | 7B 待云GPU\\n\\n## GPU 实时占用 (6× RTX 4090D, cqa1-21977)\\n| GPU | 任务 | 预计完成 |\\n|-----|------|---------|\\n| cuda:0 | signals_15B_s123_batch (d025) | ~2h |\\n| cuda:1 | signals_3B_d100_a32_s42 | ~35min |\\n| cuda:2 | signals_15B_d100_s123 | ~3h |\\n| cuda:3 | eval_3B_instruct_aligned_para (P0-C) | ~1h |\\n| cuda:4 | **待分配 → Llama-3.2-3B d000 SFT** | 指令已发 |\\n| cuda:5 | signals_05B_s123_v2 (d100) | ~2.5h |\\n\\n## Critical Path (EMNLP T-9)\\n```\\n[Now]     cuda:1 d100 ~35min → 3B s42 全齐 → RRF 聚合 (CPU)\\n          cuda:4 → Llama-3.2-3B d000 SFT 启动\\n          cuda:3 3B-Instruct eval ~1h → 0.5B/1.5B-Instruct eval\\n[Day 1]   pooled IRT (N≥16+) — 论文核心 γ 数字\\n          MMLU domain gamma N=24 (含 3B) — 确认 heterogeneity 是否 scale-dependent\\n          Llama d000 SFT + eval\\n[Day 2]   Llama d005/d025/d100 SFT + eval + signals\\n          scale-stratified IRT\\n[Day 3-5] Paper Agent Full Draft\\n[Day 5-7] Review 迭代 + Llama 结果补充\\n[Day 7-9] 最终提交\\n```\\n\\n## ⚠️ 风险项\\n1. **PPP=0 in domain gamma (4/5 domains)** — 绝对 γ 值不可信，paper 需基于 pattern/ranking claim。N=24 重跑是关键验证\\n2. **7B 云 GPU 未批** — 已向 Manager 申请 A100-80G，等待回复\\n3. **T-9 Llama 窗口紧** — 需 Day 2 完成 d000 SFT+eval+signals 才能赶上论文数据冻结\\n4. **Coverage collapse (D056)** — per-benchmark γ_k + N↑ 是主要缓解路径\\n\\n## 近期任务\\n- [ ] cuda:4 → Llama-3.2-3B d000 SFT（指令已发）\\n- [ ] 3B d100 完成 → RRF 聚合 → pooled IRT (N≥16+)\\n- [ ] MMLU domain gamma N=24 (含 3B)\\n- [ ] cuda:3 释放 → 0.5B/1.5B-Instruct eval (P0-C)\\n- [ ] 1.5B s123 全完成 → 完整 RRF (全种子)\\n- [ ] scale-stratified IRT\\n- [ ] paper_framing.md D108 措辞审慎化（等 N=24 确认）\\n- [x] 3B d005 signals 确认完成（cron false positive，非真实失败）\\n- [x] MMLU domain gamma 初步完成 — Simpson's paradox confirmed\\n- [x] sim_sweep_v7 完成 — Claim 3 identifiability 确认 (D090/D107)\\n- [x] Scope expansion 方案批准 (D106)\\n\\n## GPU 预算\\n6× RTX 4090D 全项目分配。7B 需云 GPU (A100-80G ×1, ~4h)，已申请。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D117 | 2026-05-16 | D117: Claim 1 scope narrowed — only Math+Science d | exp_006_mmlu_domain_gamma_n24_v4 |\\n| D116 | 2026-05-16 | D116: Pooled IRT confirms Simpson's Paradox — aggr | exp_006_pooled_irt_rrf_n25_v2, exp_006_mmlu_domain_gamma_n24_v4 |\\n| D115 | 2026-05-16 | D115: D108 complete (7/8 domains) — STEM gradient  | exp_006_mmlu_domain_gamma_n24_v4 |\\n| D114 | 2026-05-16 | D114: D108 domain gamma claim scoped to STEM-only  | exp_006_mmlu_domain_gamma_n24_v4 |\\n| D113 | 2026-05-16 | D113: 3B-Instruct eval v2 confirms chat_template f | exp_001_eval_3B_instruct_v2 |\\n| D112 | 2026-05-16 | D112: Medical domain PPP=1.0 model misfit — exclud | exp_006_mmlu_domain_gamma_n24 |\\n| D111 | 2026-05-16 | D111: STEM_Math γ direction reversal at N=24 — pau | exp_006_mmlu_domain_gamma_n24 |\\n| D110 | 2026-05-16 | D110: Scale-stratified IRT (N=6-8 per scale) negat | exp_006_scale_stratified_irt |\\n| D109 | 2026-05-16 | D109: Aggregate pooled IRT (N=23, 2PL+γ) confirms  | exp_006_pooled_irt_all_scales |\\n| D108 | 2026-05-16 | D108: Claim 1 升级 — 从 benchmark-dependent 升级为 domai | exp_006_mmlu_domain_gamma |\\n\\n\", \"total_chars\": 3883, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
````

</details>

---

### Assistant

_source line 17_

All four files loaded. Now I have a comprehensive picture. Let me write the method_notes.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "deb95475-5d95-4f3c-84db-bd6b2e489cfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfTEEXNLWd8WyYWfa3bUGc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19630,
      "cache_read_input_tokens": 25768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19630
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01CZCburDNFtMaqzz1huqmJs`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/",
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
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "901195c3-460a-4288-8722-0954f0a68c99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfTEEXNLWd8WyYWfa3bUGc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19630,
      "cache_read_input_tokens": 25768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19630
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

_source line 19 · 2026-05-16T16:54:59.213Z_

<details><summary>↩ Tool result · `toolu_01CZCburDNFtMaqzz1huqmJs`</summary>

```text
2pl_vs_4pl_ablation.md
3B_s123_eval_matrix_complete.md
_project
analysis_3B_d000_gsm8k_seed_variance.md
compile_eval_summary.py
coverage_report_20260515.md
d000_alignment_tax_analysis.md
d108_v4_analysis.md
diag_exp006_pooled_irt_n25.md
diag_exp_001_sft_15B_d005_s123.md
diag_exp_001_sft_d100_3B.md
diagnosis_exp002_3B_d000_s123_cuda2.md
dose_response_analysis.md
dream_reports
eval_metrics_summary.json
eval_metrics_summary.md
eval_summary_matrix.csv
exp-004
exp-006
exp-008
exp001
exp001_sft_injection
exp002_signal_pipeline
exp003_rrf_ablation
exp004_incremental_analysis.md
exp005_noise_propagation
exp006
exp006-oracle-gsm8k-extended-v2
exp006-s1only-gsm8k-2pl
exp006_baselines
exp006_irt_calibration
exp006_pooled_rrf_irt_05b_15b
exp006_readiness_report.md
exp008
exp008_3regime_analysis.json
exp008_auc_heatmap.json
exp008_v2
exp_001_eval_3B_d000_s42_a32_batch
exp_001_eval_3B_d005_s42_para_aligned
exp_001_sft_injection
exp_002_signals_05B
exp_003_mmlu_item_aligned_gap
exp_005_noise_prop_v4
exp_006
exp_006_pooled_irt_2pl_gamma_mmlu_arc
exp_006_scale_stratified_irt
exp_008_base_pretrained_15B_eval
exp_008_instruct_rl_proxy
exp_008_signal_survival
experiment_logs_loop17.txt
fisher_info_derivation
gpu_audit_20260515T1330.md
gpu_audit_loop17.md
gpu_health_20260515T1654.md
gpu_health_check_loop10.md
gpu_status_check.md
gpu_status_loop17.md
literature_supplement_irt_fit.md
literature_survey_domain_dependent_contamination.md
literature_survey_negative_gamma.md
manifest.yaml
mvp_simulation
next_experiment_queue.md
paper_draft
phase3_progress.md
plan_registry_mapping.md
report_eval_compilation.md
report_gpu_status_check.md
rrf_readiness_check.md
run_pooled_4bench_irt.py
run_pooled_irt_n16.sh
run_stratified_irt.py
signal_coverage_audit.md
signals_coverage_audit_0516.md
simulation_sweep
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "60b63f07-d599-435e-90d9-f92bd6ce9623",
  "tool_use_result": {
    "stdout": "2pl_vs_4pl_ablation.md\n3B_s123_eval_matrix_complete.md\n_project\nanalysis_3B_d000_gsm8k_seed_variance.md\ncompile_eval_summary.py\ncoverage_report_20260515.md\nd000_alignment_tax_analysis.md\nd108_v4_analysis.md\ndiag_exp006_pooled_irt_n25.md\ndiag_exp_001_sft_15B_d005_s123.md\ndiag_exp_001_sft_d100_3B.md\ndiagnosis_exp002_3B_d000_s123_cuda2.md\ndose_response_analysis.md\ndream_reports\neval_metrics_summary.json\neval_metrics_summary.md\neval_summary_matrix.csv\nexp-004\nexp-006\nexp-008\nexp001\nexp001_sft_injection\nexp002_signal_pipeline\nexp003_rrf_ablation\nexp004_incremental_analysis.md\nexp005_noise_propagation\nexp006\nexp006-oracle-gsm8k-extended-v2\nexp006-s1only-gsm8k-2pl\nexp006_baselines\nexp006_irt_calibration\nexp006_pooled_rrf_irt_05b_15b\nexp006_readiness_report.md\nexp008\nexp008_3regime_analysis.json\nexp008_auc_heatmap.json\nexp008_v2\nexp_001_eval_3B_d000_s42_a32_batch\nexp_001_eval_3B_d005_s42_para_aligned\nexp_001_sft_injection\nexp_002_signals_05B\nexp_003_mmlu_item_aligned_gap\nexp_005_noise_prop_v4\nexp_006\nexp_006_pooled_irt_2pl_gamma_mmlu_arc\nexp_006_scale_stratified_irt\nexp_008_base_pretrained_15B_eval\nexp_008_instruct_rl_proxy\nexp_008_signal_survival\nexperiment_logs_loop17.txt\nfisher_info_derivation\ngpu_audit_20260515T1330.md\ngpu_audit_loop17.md\ngpu_health_20260515T1654.md\ngpu_health_check_loop10.md\ngpu_status_check.md\ngpu_status_loop17.md\nliterature_supplement_irt_fit.md\nliterature_survey_domain_dependent_contamination.md\nliterature_survey_negative_gamma.md\nmanifest.yaml\nmvp_simulation\nnext_experiment_queue.md\npaper_draft\nphase3_progress.md\nplan_registry_mapping.md\nreport_eval_compilation.md\nreport_gpu_status_check.md\nrrf_readiness_check.md\nrun_pooled_4bench_irt.py\nrun_pooled_irt_n16.sh\nrun_stratified_irt.py\nsignal_coverage_audit.md\nsignals_coverage_audit_0516.md\nsimulation_sweep",
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

_source line 20_

<details open><summary>🔧 Tool call — Write · `toolu_01AoAbA1NHfRkXCTbnmgLn37`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/method_notes.md",
  "content": "# Method Section Notes — ContamCal\n\nWord budget: 1100 words (per writing_plan.yaml §method)\n\n---\n\n## 3.1 Problem Formulation\n\n**Core idea**: Given model $j$, benchmark $k$ with items $i$, observed binary response $y_{ijk}$. The latent ability $\\theta_j$ is confounded by contamination exposure. Goal: estimate $\\theta_j^{\\text{clean}}$ (ability absent contamination).\n\n**Three structural adaptations from educational measurement IRT**:\n1. Independent examinees → single model with joint item distribution (all items share one θ per model)\n2. Binary leakage indicator → continuous exposure score $e_{ij} \\in [0,1]$\n3. Stable ability → regime-conditional ability (θ may shift with contamination dosage)\n\n**Prior work to cite**:\n- Eckerly (2017): item compromise IRT — closest precedent (binary leak + 3PL)\n- Sinharay (2017): compromised item detection via IRT residuals\n- De Boeck & Wilson (2004): explanatory IRT framework (covariates on item/person parameters)\n- Adams et al. (1997): multifaceted Rasch as structural template\n- Mislevy (1986): fixed-effects IRT when N_examinees is small\n\n**Key notation**:\n- $y_{ijk} \\in \\{0,1\\}$: response of model $j$ to item $i$ on benchmark $k$\n- $\\theta_j$: latent ability of model $j$\n- $e_{ij}$: exposure score (from Stage 1 RRF)\n- $\\gamma_k$: per-benchmark contamination effect parameter\n- $a_i, b_i, c_i, d_i$: item discrimination, difficulty, guessing, slip\n\n**Corresponding experiments**: exp-006 (all IRT fits)\n\n---\n\n## 3.2 Stage 1: Multi-Signal Exposure Mapping\n\n**Core idea**: Map each (model, item) pair to a continuous exposure score $e_{ij}$ via training-free Reciprocal Rank Fusion of multiple contamination signals. Training-free fusion avoids meta-circularity (a learned aggregator's training data may itself be contaminated).\n\n**Signals**:\n| ID | Signal | Method | Source |\n|----|--------|--------|--------|\n| S1 | Embedding similarity | cosine(item embedding, nearest training chunk) | Provenance-based |\n| S2 | Min-K++ | token-level surprise (low perplexity on memorized items) | MIA-based |\n| S3 | [Reserved/deprecated] | — | — |\n| S4 | Self-Critique | model-generated paraphrase similarity | Behavioral |\n\n**RRF formula**:\n$$e_{ij} = \\sum_{s \\in \\text{signals}} \\frac{1}{k + r_s(i,j)}$$\nwhere $r_s(i,j)$ is the rank of item $i$ for model $j$ under signal $s$, and $k=60$ (standard RRF constant).\n\n**Critical empirical finding** (feeds into Results §5.2, but contextualize in Method):\n- S1 is the only reliable signal (AUC > 0.95 at d005)\n- S2 Min-K++ exhibits directional reversal at 0.5B (Cohen's d = -1.98) — actively misleading\n- RRF degrades to S1-only in practice; presented honestly as limitation but RRF remains principled design (extensible when better signals emerge)\n\n**Meta-circularity argument**: Learned aggregation (e.g., logistic regression over signals) requires labeled contamination data → circular dependency. RRF is rank-based, parameter-free, training-free.\n\n**Prior work to cite**:\n- Cormack et al. (2009): RRF original paper\n- Zhang et al. (2024): Min-K++ [CITE: zhang2024minkpp]\n- Shokri et al. (2017): MIA foundations for S2 contextualization\n- Carlini et al. (2022): training data extraction (broader MIA context)\n- Dong et al. (2024): KDS [CITE NEEDED exact ref]\n- Shi et al. (2024): CDD [CITE NEEDED exact ref]\n\n**Corresponding experiments**: exp-002 (signal pipeline), exp-003 (RRF ablation), exp-008 (signal evaluation)\n\n---\n\n## 3.3 Stage 2: Contamination-Augmented IRT\n\n**Core idea**: Extend standard IRT with a contamination covariate $\\gamma_k \\cdot e_{ij}$ in the logit. Per-benchmark $\\gamma_k$ captures heterogeneous contamination effects (inflation on GSM8K, forgetting on ARC).\n\n**Model definitions**:\n\n### 2PL + γ (default, robust)\n$$P(y_{ijk} = 1) = \\sigma\\big(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\big)$$\n\nUse when: N < 16, or benchmark is not strictly MCQ format.\n\n### 4PL + γ (full model, MCQ benchmarks)\n$$P(y_{ijk} = 1) = c_i + (d_i - c_i) \\cdot \\sigma\\big(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\big)$$\n\nUse when: N ≥ 16, MCQ format benchmark.\n\n- $c_i$: guessing parameter (lower asymptote, ~0.25 for 4-choice MC)\n- $d_i$: slip parameter (upper asymptote, <1.0 for careless errors)\n\n**Model selection rule** (C008 constraint):\n- 2PL+γ is default — robust even at small N\n- 4PL+γ only when N≥16 AND MCQ format (c/d parameters identifiable only with sufficient data)\n- ARC N=5 with 4PL+γ → PPP=0.000, MAE worsens 17× (overparameterization collapse)\n\n**Per-benchmark $\\gamma_k$ identification strategy**:\n- Fit IRT independently per benchmark (not jointly across benchmarks)\n- $\\gamma_k$ inherits sign and magnitude from exposure-response relationship on that specific benchmark\n- Positive $\\gamma_k$: contamination inflates scores (memorization helps)\n- Negative $\\gamma_k$: contamination degrades scores (forgetting/capacity displacement)\n- Non-significant $\\gamma_k$: benchmark naturally resistant or signal uninformative\n\n**Inference**: Stan NUTS (No-U-Turn Sampler), 4 chains, 1000 warmup + 1000 sampling. Convergence: R̂ < 1.05, ESS > 400. Model fit: PPP ∈ [0.1, 0.9].\n\n**Calibration procedure**:\n1. Fit IRT with exposure scores → posterior $p(\\theta_j, \\gamma_k | \\mathbf{y}, \\mathbf{e})$\n2. Predict clean score: set $e_{ij} = 0$ for all items → $\\hat{y}_{ijk}^{\\text{clean}}$\n3. Calibrated accuracy = mean of predicted clean item responses\n4. CI from posterior draws\n\n**Gating criterion** (when NOT to calibrate):\n- $\\gamma_k$ must be significant (CI excludes 0)\n- PPP ∈ [0.1, 0.9] (model not misspecified)\n- Calibrated MAE < raw MAE (calibration must help)\n- If any condition fails → report raw scores\n\n**Prior work to cite**:\n- De Boeck & Wilson (2004): explanatory IRT (covariate on logit)\n- San Martín et al. (2009): IRT identifiability conditions\n- Maris & Bechger (2009): IRT parameter identifiability\n- Lalor et al. (AAAI 2024): IRT for LLM evaluation\n- Holland & Wainer (1993): DIF — γ_k is essentially DIF between exposed/unexposed groups\n- Talts et al. (2018): SBC for posterior calibration validation\n- Brown & Thomson (2024): PPP distribution interpretation\n\n**Corresponding experiments**: exp-006 (all IRT configurations)\n\n---\n\n## 3.4 Fisher Information and Identifiability\n\n**Core idea**: Derive the Fisher Information $I(\\gamma)$ for the 4PL+γ model to establish theoretical recovery boundaries. Show that signal AUC and N_models jointly determine γ recoverability. Reveal structural domain-method mismatch: LLM evaluation typically has N=8-30 models, but reliable recovery needs N≥50.\n\n**Key results from simulation sweep** (exp-004, 24 conditions × 240 runs):\n- Recovery succeeds at AUC=0.55 (lowest tested) when J≥50 items, N≥20 models\n- CI width ∝ $N^{-0.48}$ (empirically estimated decay rate)\n- Coverage collapse at N<30 (confirmed D036)\n- Lower bound of AUC for recovery remains open (not tested below 0.55)\n\n**Fisher Information sketch** (full derivation in Appendix A):\n$$I(\\gamma) = \\sum_{i,j} e_{ij}^2 \\cdot P_{ij}(1-P_{ij}) \\cdot \\left(\\frac{d_i - c_i}{P_{ij} - c_i}\\right)^2 \\cdot \\frac{(P_{ij}-c_i)^2}{(d_i-c_i)^2}$$\n\nSimplified for 2PL+γ (c=0, d=1):\n$$I(\\gamma) = \\sum_{i,j} e_{ij}^2 \\cdot P_{ij}(1-P_{ij})$$\n\nKey insight: $I(\\gamma)$ scales with (a) variance of exposure scores (higher AUC → more discriminative $e_{ij}$), (b) number of models N, (c) item information (items near difficulty boundary contribute most).\n\n**Domain-method mismatch framing**:\n- Educational testing: hundreds of examinees, clear binary leak indicator → recovery trivial\n- LLM evaluation: 8-30 models, noisy continuous exposure signal → structural challenge\n- This is not merely \"IRT needs more data\" — it's a fundamental mismatch between the measurement framework's assumptions and the LLM evaluation domain's constraints\n\n**Measurement error extension** (exp-005, negative result — mention briefly):\n- Model exposure as noisy observation: $e_{ij} = \\tau_{ij} + \\epsilon$, $\\epsilon \\sim N(0, \\sigma_e^2)$\n- Result: CI width insensitive to $\\sigma_e$ across tested range → noise propagation is NOT the binding constraint\n- Binding constraint is N (number of models), not signal noise\n\n**Prior work to cite**:\n- San Martín et al. (2009): IRT identifiability\n- Talts et al. (2018): SBC diagnostic\n- Reckase (2009): multidimensional IRT (limitation: our θ is unidimensional)\n- Angelopoulos & Bates (2023): conformal prediction as alternative UQ (discuss why Bayesian IRT preferred: interpretable parameters, contamination covariate integration)\n\n**Corresponding experiments**: exp-004 (simulation sweep), exp-005 (noise propagation)\n\n---\n\n## Domain-Level Heterogeneity Analysis (supplements §5.1, methodology described in §3.3)\n\n**Core idea**: Within MMLU, stratify 57 subjects into 8 cognitive domains. Fit 2PL+γ per domain. Reveals Simpson's paradox: aggregate γ≈0 masks domain-level heterogeneity.\n\n**Domain taxonomy**: 57 MMLU subjects → 8 cognitive domains:\n- STEM_Math, STEM_Science, STEM_CS_Eng\n- Medical (excluded, D112: PPP=1.0 systematic misfit)\n- Humanities, Social_Sciences, Business_Law, Other\n\n**Formalization of Simpson's paradox**:\n- Aggregate fit: $\\gamma_{\\text{MMLU}} \\approx 0$ (CI includes 0)\n- Domain-level: $\\gamma_{\\text{Math}} = +0.97$, $\\gamma_{\\text{Science}} = +0.84$, $\\gamma_{\\text{CS\\_Eng}} = +0.20$ (NS)\n- Non-STEM: PPP≈1.0 → model misspecification (2PL+γ inadequate for these domains)\n- Interpretation: contamination susceptibility maps to factual knowledge density\n\n**Claim scope limitations**:\n- Only claim pattern/ranking from domains with PPP ∈ [0.1, 0.9] (Math, Science have acceptable PPP)\n- Non-STEM PPP=1.0 is a boundary finding, not failure — reported as model scope limitation\n- Cannot claim absolute γ values from domains with PPP=0\n\n**Prior work to cite**:\n- Kievit et al. (2013): Simpson's paradox formal framework\n- Ercikan et al. (2008): DIF cancellation as empirical precedent\n- Thissen et al. (1993): DIF detection in IRT\n- Zumbo (1999): DIF overview\n\n**Corresponding experiments**: exp-006 (mmlu_domain_gamma_n24_v4), D108/D115/D116\n\n---\n\n## Cross-Family Validation Protocol (Llama-3.2-3B)\n\n**Core idea**: Test whether contamination susceptibility (per-benchmark γ_k, domain heterogeneity pattern) is a benchmark × domain property rather than a Qwen2.5 family artifact.\n\n**Design**:\n- Model: Llama-3.2-3B (different architecture, tokenizer, pretraining data)\n- Same injection protocol: LoRA alpha=32, same dosages (d000/d005/d025/d100)\n- Same evaluation: aligned + paraphrased format\n- Same signal pipeline: S1 embedding similarity (corpus-agnostic)\n\n**Validation criteria**:\n- γ_k sign agreement across families (ARC negative, GSM8K non-significant)\n- Domain heterogeneity gradient reproduces (STEM > non-STEM)\n- If patterns replicate → contamination effects are benchmark properties\n- If patterns diverge → model architecture/capacity matters more\n\n**Status**: Llama SFTs running (D106), results expected Day 2-3. If complete before deadline, included in main paper. Otherwise, prepared as rebuttal material (exp-014).\n\n**Corresponding experiments**: exp-014 (cross-family), D106\n\n---\n\n## RRF Aggregation Method Detail\n\n**Formula**:\n$$\\text{RRF}(i,j) = \\sum_{s=1}^{S} \\frac{w_s}{k + r_s(i,j)}$$\n\n- $S$: number of active signals (up to 4)\n- $w_s = 1$ for all signals (uniform weight — training-free)\n- $k = 60$ (standard constant from Cormack et al. 2009)\n- $r_s(i,j)$: rank of item $i$ among all items for model $j$ under signal $s$ (1 = most exposed)\n\n**Normalization**: Min-max scale final RRF scores to [0, 1] per model-benchmark.\n\n**Practical reality at current scale**:\n- Only S1 provides discriminative signal (AUC > 0.9)\n- S2, S4 ≈ random at 0.5B; may improve at 1.5B/3B (pending verification)\n- RRF value is principled aggregation architecture; current instantiation ≈ S1-only\n- Honest framing: \"training-free multi-signal architecture with graceful degradation\"\n\n---\n\n## Evaluation Protocol (6 Metrics)\n\n1. **MAE**: $\\frac{1}{J}\\sum_j |{\\hat{acc}_j^{\\text{cal}}} - acc_j^{\\text{clean}}|$ (point estimate quality)\n2. **Coverage@95%**: fraction of true values within 95% credible interval\n3. **Sharpness**: mean CI width (narrower = better at fixed coverage)\n4. **Kendall's τ**: rank correlation between calibrated and true model rankings\n5. **Dose-response monotonicity**: $\\gamma$ effect increases with dosage level\n6. **SBC** (Talts et al. 2018): simulation-based calibration diagnostic at actual N and J\n\n**Ground truth**: $acc_j^{\\text{clean}}$ = accuracy of the d000 (clean) model on same benchmark. For RL observational track (future work): held-out clean benchmark, NOT calibrated scores (avoids circularity).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "558728c7-2a4f-4987-9a72-f30e650866b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1KyEfFbkksfF8dw9FEXZ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 45398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 889
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 21 · 2026-05-16T16:56:54.681Z_

<details><summary>↩ Tool result · `toolu_01AoAbA1NHfRkXCTbnmgLn37`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/method_notes.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "708688a6-44f0-4ac3-9a45-3a8744f72e33",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/method_notes.md",
    "content": "# Method Section Notes — ContamCal\n\nWord budget: 1100 words (per writing_plan.yaml §method)\n\n---\n\n## 3.1 Problem Formulation\n\n**Core idea**: Given model $j$, benchmark $k$ with items $i$, observed binary response $y_{ijk}$. The latent ability $\\theta_j$ is confounded by contamination exposure. Goal: estimate $\\theta_j^{\\text{clean}}$ (ability absent contamination).\n\n**Three structural adaptations from educational measurement IRT**:\n1. Independent examinees → single model with joint item distribution (all items share one θ per model)\n2. Binary leakage indicator → continuous exposure score $e_{ij} \\in [0,1]$\n3. Stable ability → regime-conditional ability (θ may shift with contamination dosage)\n\n**Prior work to cite**:\n- Eckerly (2017): item compromise IRT — closest precedent (binary leak + 3PL)\n- Sinharay (2017): compromised item detection via IRT residuals\n- De Boeck & Wilson (2004): explanatory IRT framework (covariates on item/person parameters)\n- Adams et al. (1997): multifaceted Rasch as structural template\n- Mislevy (1986): fixed-effects IRT when N_examinees is small\n\n**Key notation**:\n- $y_{ijk} \\in \\{0,1\\}$: response of model $j$ to item $i$ on benchmark $k$\n- $\\theta_j$: latent ability of model $j$\n- $e_{ij}$: exposure score (from Stage 1 RRF)\n- $\\gamma_k$: per-benchmark contamination effect parameter\n- $a_i, b_i, c_i, d_i$: item discrimination, difficulty, guessing, slip\n\n**Corresponding experiments**: exp-006 (all IRT fits)\n\n---\n\n## 3.2 Stage 1: Multi-Signal Exposure Mapping\n\n**Core idea**: Map each (model, item) pair to a continuous exposure score $e_{ij}$ via training-free Reciprocal Rank Fusion of multiple contamination signals. Training-free fusion avoids meta-circularity (a learned aggregator's training data may itself be contaminated).\n\n**Signals**:\n| ID | Signal | Method | Source |\n|----|--------|--------|--------|\n| S1 | Embedding similarity | cosine(item embedding, nearest training chunk) | Provenance-based |\n| S2 | Min-K++ | token-level surprise (low perplexity on memorized items) | MIA-based |\n| S3 | [Reserved/deprecated] | — | — |\n| S4 | Self-Critique | model-generated paraphrase similarity | Behavioral |\n\n**RRF formula**:\n$$e_{ij} = \\sum_{s \\in \\text{signals}} \\frac{1}{k + r_s(i,j)}$$\nwhere $r_s(i,j)$ is the rank of item $i$ for model $j$ under signal $s$, and $k=60$ (standard RRF constant).\n\n**Critical empirical finding** (feeds into Results §5.2, but contextualize in Method):\n- S1 is the only reliable signal (AUC > 0.95 at d005)\n- S2 Min-K++ exhibits directional reversal at 0.5B (Cohen's d = -1.98) — actively misleading\n- RRF degrades to S1-only in practice; presented honestly as limitation but RRF remains principled design (extensible when better signals emerge)\n\n**Meta-circularity argument**: Learned aggregation (e.g., logistic regression over signals) requires labeled contamination data → circular dependency. RRF is rank-based, parameter-free, training-free.\n\n**Prior work to cite**:\n- Cormack et al. (2009): RRF original paper\n- Zhang et al. (2024): Min-K++ [CITE: zhang2024minkpp]\n- Shokri et al. (2017): MIA foundations for S2 contextualization\n- Carlini et al. (2022): training data extraction (broader MIA context)\n- Dong et al. (2024): KDS [CITE NEEDED exact ref]\n- Shi et al. (2024): CDD [CITE NEEDED exact ref]\n\n**Corresponding experiments**: exp-002 (signal pipeline), exp-003 (RRF ablation), exp-008 (signal evaluation)\n\n---\n\n## 3.3 Stage 2: Contamination-Augmented IRT\n\n**Core idea**: Extend standard IRT with a contamination covariate $\\gamma_k \\cdot e_{ij}$ in the logit. Per-benchmark $\\gamma_k$ captures heterogeneous contamination effects (inflation on GSM8K, forgetting on ARC).\n\n**Model definitions**:\n\n### 2PL + γ (default, robust)\n$$P(y_{ijk} = 1) = \\sigma\\big(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\big)$$\n\nUse when: N < 16, or benchmark is not strictly MCQ format.\n\n### 4PL + γ (full model, MCQ benchmarks)\n$$P(y_{ijk} = 1) = c_i + (d_i - c_i) \\cdot \\sigma\\big(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\big)$$\n\nUse when: N ≥ 16, MCQ format benchmark.\n\n- $c_i$: guessing parameter (lower asymptote, ~0.25 for 4-choice MC)\n- $d_i$: slip parameter (upper asymptote, <1.0 for careless errors)\n\n**Model selection rule** (C008 constraint):\n- 2PL+γ is default — robust even at small N\n- 4PL+γ only when N≥16 AND MCQ format (c/d parameters identifiable only with sufficient data)\n- ARC N=5 with 4PL+γ → PPP=0.000, MAE worsens 17× (overparameterization collapse)\n\n**Per-benchmark $\\gamma_k$ identification strategy**:\n- Fit IRT independently per benchmark (not jointly across benchmarks)\n- $\\gamma_k$ inherits sign and magnitude from exposure-response relationship on that specific benchmark\n- Positive $\\gamma_k$: contamination inflates scores (memorization helps)\n- Negative $\\gamma_k$: contamination degrades scores (forgetting/capacity displacement)\n- Non-significant $\\gamma_k$: benchmark naturally resistant or signal uninformative\n\n**Inference**: Stan NUTS (No-U-Turn Sampler), 4 chains, 1000 warmup + 1000 sampling. Convergence: R̂ < 1.05, ESS > 400. Model fit: PPP ∈ [0.1, 0.9].\n\n**Calibration procedure**:\n1. Fit IRT with exposure scores → posterior $p(\\theta_j, \\gamma_k | \\mathbf{y}, \\mathbf{e})$\n2. Predict clean score: set $e_{ij} = 0$ for all items → $\\hat{y}_{ijk}^{\\text{clean}}$\n3. Calibrated accuracy = mean of predicted clean item responses\n4. CI from posterior draws\n\n**Gating criterion** (when NOT to calibrate):\n- $\\gamma_k$ must be significant (CI excludes 0)\n- PPP ∈ [0.1, 0.9] (model not misspecified)\n- Calibrated MAE < raw MAE (calibration must help)\n- If any condition fails → report raw scores\n\n**Prior work to cite**:\n- De Boeck & Wilson (2004): explanatory IRT (covariate on logit)\n- San Martín et al. (2009): IRT identifiability conditions\n- Maris & Bechger (2009): IRT parameter identifiability\n- Lalor et al. (AAAI 2024): IRT for LLM evaluation\n- Holland & Wainer (1993): DIF — γ_k is essentially DIF between exposed/unexposed groups\n- Talts et al. (2018): SBC for posterior calibration validation\n- Brown & Thomson (2024): PPP distribution interpretation\n\n**Corresponding experiments**: exp-006 (all IRT configurations)\n\n---\n\n## 3.4 Fisher Information and Identifiability\n\n**Core idea**: Derive the Fisher Information $I(\\gamma)$ for the 4PL+γ model to establish theoretical recovery boundaries. Show that signal AUC and N_models jointly determine γ recoverability. Reveal structural domain-method mismatch: LLM evaluation typically has N=8-30 models, but reliable recovery needs N≥50.\n\n**Key results from simulation sweep** (exp-004, 24 conditions × 240 runs):\n- Recovery succeeds at AUC=0.55 (lowest tested) when J≥50 items, N≥20 models\n- CI width ∝ $N^{-0.48}$ (empirically estimated decay rate)\n- Coverage collapse at N<30 (confirmed D036)\n- Lower bound of AUC for recovery remains open (not tested below 0.55)\n\n**Fisher Information sketch** (full derivation in Appendix A):\n$$I(\\gamma) = \\sum_{i,j} e_{ij}^2 \\cdot P_{ij}(1-P_{ij}) \\cdot \\left(\\frac{d_i - c_i}{P_{ij} - c_i}\\right)^2 \\cdot \\frac{(P_{ij}-c_i)^2}{(d_i-c_i)^2}$$\n\nSimplified for 2PL+γ (c=0, d=1):\n$$I(\\gamma) = \\sum_{i,j} e_{ij}^2 \\cdot P_{ij}(1-P_{ij})$$\n\nKey insight: $I(\\gamma)$ scales with (a) variance of exposure scores (higher AUC → more discriminative $e_{ij}$), (b) number of models N, (c) item information (items near difficulty boundary contribute most).\n\n**Domain-method mismatch framing**:\n- Educational testing: hundreds of examinees, clear binary leak indicator → recovery trivial\n- LLM evaluation: 8-30 models, noisy continuous exposure signal → structural challenge\n- This is not merely \"IRT needs more data\" — it's a fundamental mismatch between the measurement framework's assumptions and the LLM evaluation domain's constraints\n\n**Measurement error extension** (exp-005, negative result — mention briefly):\n- Model exposure as noisy observation: $e_{ij} = \\tau_{ij} + \\epsilon$, $\\epsilon \\sim N(0, \\sigma_e^2)$\n- Result: CI width insensitive to $\\sigma_e$ across tested range → noise propagation is NOT the binding constraint\n- Binding constraint is N (number of models), not signal noise\n\n**Prior work to cite**:\n- San Martín et al. (2009): IRT identifiability\n- Talts et al. (2018): SBC diagnostic\n- Reckase (2009): multidimensional IRT (limitation: our θ is unidimensional)\n- Angelopoulos & Bates (2023): conformal prediction as alternative UQ (discuss why Bayesian IRT preferred: interpretable parameters, contamination covariate integration)\n\n**Corresponding experiments**: exp-004 (simulation sweep), exp-005 (noise propagation)\n\n---\n\n## Domain-Level Heterogeneity Analysis (supplements §5.1, methodology described in §3.3)\n\n**Core idea**: Within MMLU, stratify 57 subjects into 8 cognitive domains. Fit 2PL+γ per domain. Reveals Simpson's paradox: aggregate γ≈0 masks domain-level heterogeneity.\n\n**Domain taxonomy**: 57 MMLU subjects → 8 cognitive domains:\n- STEM_Math, STEM_Science, STEM_CS_Eng\n- Medical (excluded, D112: PPP=1.0 systematic misfit)\n- Humanities, Social_Sciences, Business_Law, Other\n\n**Formalization of Simpson's paradox**:\n- Aggregate fit: $\\gamma_{\\text{MMLU}} \\approx 0$ (CI includes 0)\n- Domain-level: $\\gamma_{\\text{Math}} = +0.97$, $\\gamma_{\\text{Science}} = +0.84$, $\\gamma_{\\text{CS\\_Eng}} = +0.20$ (NS)\n- Non-STEM: PPP≈1.0 → model misspecification (2PL+γ inadequate for these domains)\n- Interpretation: contamination susceptibility maps to factual knowledge density\n\n**Claim scope limitations**:\n- Only claim pattern/ranking from domains with PPP ∈ [0.1, 0.9] (Math, Science have acceptable PPP)\n- Non-STEM PPP=1.0 is a boundary finding, not failure — reported as model scope limitation\n- Cannot claim absolute γ values from domains with PPP=0\n\n**Prior work to cite**:\n- Kievit et al. (2013): Simpson's paradox formal framework\n- Ercikan et al. (2008): DIF cancellation as empirical precedent\n- Thissen et al. (1993): DIF detection in IRT\n- Zumbo (1999): DIF overview\n\n**Corresponding experiments**: exp-006 (mmlu_domain_gamma_n24_v4), D108/D115/D116\n\n---\n\n## Cross-Family Validation Protocol (Llama-3.2-3B)\n\n**Core idea**: Test whether contamination susceptibility (per-benchmark γ_k, domain heterogeneity pattern) is a benchmark × domain property rather than a Qwen2.5 family artifact.\n\n**Design**:\n- Model: Llama-3.2-3B (different architecture, tokenizer, pretraining data)\n- Same injection protocol: LoRA alpha=32, same dosages (d000/d005/d025/d100)\n- Same evaluation: aligned + paraphrased format\n- Same signal pipeline: S1 embedding similarity (corpus-agnostic)\n\n**Validation criteria**:\n- γ_k sign agreement across families (ARC negative, GSM8K non-significant)\n- Domain heterogeneity gradient reproduces (STEM > non-STEM)\n- If patterns replicate → contamination effects are benchmark properties\n- If patterns diverge → model architecture/capacity matters more\n\n**Status**: Llama SFTs running (D106), results expected Day 2-3. If complete before deadline, included in main paper. Otherwise, prepared as rebuttal material (exp-014).\n\n**Corresponding experiments**: exp-014 (cross-family), D106\n\n---\n\n## RRF Aggregation Method Detail\n\n**Formula**:\n$$\\text{RRF}(i,j) = \\sum_{s=1}^{S} \\frac{w_s}{k + r_s(i,j)}$$\n\n- $S$: number of active signals (up to 4)\n- $w_s = 1$ for all signals (uniform weight — training-free)\n- $k = 60$ (standard constant from Cormack et al. 2009)\n- $r_s(i,j)$: rank of item $i$ among all items for model $j$ under signal $s$ (1 = most exposed)\n\n**Normalization**: Min-max scale final RRF scores to [0, 1] per model-benchmark.\n\n**Practical reality at current scale**:\n- Only S1 provides discriminative signal (AUC > 0.9)\n- S2, S4 ≈ random at 0.5B; may improve at 1.5B/3B (pending verification)\n- RRF value is principled aggregation architecture; current instantiation ≈ S1-only\n- Honest framing: \"training-free multi-signal architecture with graceful degradation\"\n\n---\n\n## Evaluation Protocol (6 Metrics)\n\n1. **MAE**: $\\frac{1}{J}\\sum_j |{\\hat{acc}_j^{\\text{cal}}} - acc_j^{\\text{clean}}|$ (point estimate quality)\n2. **Coverage@95%**: fraction of true values within 95% credible interval\n3. **Sharpness**: mean CI width (narrower = better at fixed coverage)\n4. **Kendall's τ**: rank correlation between calibrated and true model rankings\n5. **Dose-response monotonicity**: $\\gamma$ effect increases with dosage level\n6. **SBC** (Talts et al. 2018): simulation-based calibration diagnostic at actual N and J\n\n**Ground truth**: $acc_j^{\\text{clean}}$ = accuracy of the d000 (clean) model on same benchmark. For RL observational track (future work): held-out clean benchmark, NOT calibrated scores (avoids circularity).\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Qwu8KGJG7e8ginprLTQiZx`</summary>

```json
{
  "name": "method_notes",
  "type": "intermediate",
  "description": "Method section writing notes: §3.1-3.4 structure with formulas, prior work, identification strategy, Fisher Information sketch, domain heterogeneity formalization, cross-family protocol, RRF detail, evaluation metrics",
  "project": "contamcal-irt-calibration",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/method_notes.md",
  "tags": [
    "paper",
    "method",
    "writing"
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
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "c2a0fce7-1d1f-4d3e-b1fe-999f9aecdd5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcFEa8VGdKHQmkSRdonREx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4344,
      "cache_read_input_tokens": 46287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4344
      },
      "output_tokens": 67,
      "service_tier": "standard",
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

_source line 23 · 2026-05-16T16:57:02.889Z_

<details><summary>↩ Tool result · `toolu_01Qwu8KGJG7e8ginprLTQiZx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_5f1b66\", \"name\": \"method_notes\", \"type\": \"intermediate\", \"description\": \"Method section writing notes: §3.1-3.4 structure with formulas, prior work, identification strategy, Fisher Information sketch, domain heterogeneity formalization, cross-family protocol, RRF detail, evaluation metrics\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/intermediate/method_notes.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:57:02.769220+00:00\", \"tags\": [\"paper\", \"method\", \"writing\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "43ad01e5-e239-4b51-9fe7-d89c0c11ce0a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_5f1b66\\\", \\\"name\\\": \\\"method_notes\\\", \\\"type\\\": \\\"intermediate\\\", \\\"description\\\": \\\"Method section writing notes: §3.1-3.4 structure with formulas, prior work, identification strategy, Fisher Information sketch, domain heterogeneity formalization, cross-family protocol, RRF detail, evaluation metrics\\\", \\\"path\\\": \\\"projects/contamcal-irt-calibration/artifacts/_project/intermediate/method_notes.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T16:57:02.769220+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"method\\\", \\\"writing\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_5f1b66\", \"name\": \"method_notes\", \"type\": \"intermediate\", \"description\": \"Method section writing notes: §3.1-3.4 structure with formulas, prior work, identification strategy, Fisher Information sketch, domain heterogeneity formalization, cross-family protocol, RRF detail, evaluation metrics\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/intermediate/method_notes.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:57:02.769220+00:00\", \"tags\": [\"paper\", \"method\", \"writing\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

已完成。产出文件：`artifacts/method_notes.md`（已注册 art_20260516_5f1b66）。

覆盖内容：
- §3.1 Problem Formulation（3 structural adaptations、notation、6 citations）
- §3.2 Stage 1 Multi-Signal Exposure Mapping（S1-S4 定义、RRF 公式、meta-circularity argument）
- §3.3 Stage 2 Contamination-Augmented IRT（2PL+γ / 4PL+γ 公式、model selection rule C008、per-benchmark γ_k identification、gating criterion）
- §3.4 Fisher Information and Identifiability（I(γ) 骨架、CI width ∝ N^{-0.48}、domain-method mismatch）
- 补充模块：domain heterogeneity formalization（Simpson's paradox）、cross-family validation protocol（Llama）、RRF detail、evaluation protocol（6 metrics）

每个 subsection 标注了对应实验 ID 和需要引用的文献（不确定的标注了 [CITE NEEDED]）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "uuid": "04866fea-2d17-4fbf-aad5-a3e9b8680e5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPejKqGyiMwfaqebpBx9iW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 50631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 650
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

_source line 25_

已完成。产出文件：`artifacts/method_notes.md`（已注册 art_20260516_5f1b66）。

覆盖内容：
- §3.1 Problem Formulation（3 structural adaptations、notation、6 citations）
- §3.2 Stage 1 Multi-Signal Exposure Mapping（S1-S4 定义、RRF 公式、meta-circularity argument）
- §3.3 Stage 2 Contamination-Augmented IRT（2PL+γ / 4PL+γ 公式、model selection rule C008、per-benchmark γ_k identification、gating criterion）
- §3.4 Fisher Information and Identifiability（I(γ) 骨架、CI width ∝ N^{-0.48}、domain-method mismatch）
- 补充模块：domain heterogeneity formalization（Simpson's paradox）、cross-family validation protocol（Llama）、RRF detail、evaluation protocol（6 metrics）

每个 subsection 标注了对应实验 ID 和需要引用的文献（不确定的标注了 [CITE NEEDED]）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 156394,
  "duration_api_ms": 157200,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "d6b3b1dc-d1a6-4b05-a4f2-0a4fadc54ccc",
  "total_cost_usd": 0.49205,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 39440,
    "cache_read_input_tokens": 204518,
    "output_tokens": 5624,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 39440,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 305,
        "cache_read_input_tokens": 50631,
        "cache_creation_input_tokens": 650,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 650
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2556,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002646,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 5624,
      "cacheReadInputTokens": 204518,
      "cacheCreationInputTokens": 39440,
      "webSearchRequests": 0,
      "costUSD": 0.48940400000000006,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "83b991e9-07f8-485c-a8b3-669ed42afc73"
}
```

</details>

---
