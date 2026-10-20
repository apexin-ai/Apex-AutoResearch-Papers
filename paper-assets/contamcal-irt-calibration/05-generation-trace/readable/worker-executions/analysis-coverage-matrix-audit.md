# analysis coverage matrix audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/workers/worker_analysis_coverage_matrix_audit_20260514T041621.log`
- **Structured JSON:** [`faf302b1338bc4970d91.json`](../../sessions/fa/faf302b1338bc4970d91.json)

## Before a recorded user message

19 recorded events

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
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
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
    "mcp__agent-ml-research__compute_coverage_matrix",
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
  "uuid": "f404c9a5-c3bc-4475-b8b3-c6e3c5579b00",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1778743200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "43500e3d-d41a-40b2-8fec-2b1bf5f6edcb",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the project files and computing the coverage matrix. I'll do the reads in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "2ede7449-36e2-4a71-b502-107964b3317a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSMyhV5p3Jv3mM1NtmRqtZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11369,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11369
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

开始审计实验覆盖率和投稿就绪度。先并行读取所有需要的数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "c643f130-e554-4dc9-9a48-7b1a11d74d11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSMyhV5p3Jv3mM1NtmRqtZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11369,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11369
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012W5C1mXjjXN8SGGJwfEJwF`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__compute_coverage_matrix,mcp__agent-ml-research__read_registry",
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
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "eb46b46e-dc6a-4da8-9b6b-e4f885bc9220",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSMyhV5p3Jv3mM1NtmRqtZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11369,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11369
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

_source line 7 · 2026-05-14T04:16:40.797Z_

<details><summary>↩ Tool result · `toolu_012W5C1mXjjXN8SGGJwfEJwF`</summary>

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
  "tool_name": "mcp__agent-ml-research__compute_coverage_matrix"
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
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "1e7a3cdf-da52-469c-a379-2556fd033cb9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__compute_coverage_matrix,mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PeyuqcX6Sx9r5PCLed5T6h`</summary>

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
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "418dffcc-45e7-45b6-99a9-09cdb46de9b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pxQVYaD2WKmQK4pPrLRCx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 23210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1062
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

_source line 9 · 2026-05-14T04:16:43.999Z_

<details><summary>↩ Tool result · `toolu_01PeyuqcX6Sx9r5PCLed5T6h`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight\\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\\n\\n## Core Claims (3 条)\\n\\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)\\n\\n2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.\\n\\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.\\n\\n## Contributions (Hierarchical)\\n\\n### Core\\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals\\n2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)\\n3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)\\n\\n### Supporting\\n4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds\\n5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\n- **Our framing**: ContamCal is a \\\"statistical safety net\\\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).\\n- **Headline result template**: \\\"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\\\"\\n\\n## Venue Fit Risks\\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \\\"new algorithm\\\" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \\\"calibration is only as good as its inputs.\\\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\\n\\n## Anticipated Reviewer Concerns & Defenses\\n\\n| # | Concern | Defense | Experiment |\\n|---|---------|---------|------------|\\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \\\"best-available proxy\\\", acknowledged as limitation | exp-006, exp-009 |\\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\\n| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |\\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\\n\\n## Evaluation Protocol (5 Metrics)\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\n\\n## Benchmarks (3 main + 1 appendix)\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\\n3. **ARC-Challenge** — science reasoning multiple-choice\\n4. **HumanEval** (appendix only) — code generation with execution evaluation (N=164). Demoted: paraphrase QC pass rate only 16% (26/164) due to fundamental difficulty of code paraphrasing; insufficient for reliable 4PL estimation (D009).\\n\\n## Baselines (7)\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\n\\n## Local Independence Discussion\\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\\n\\n## Required Figures (Dream D2: \\\"zero figures\\\" flagged as serious deficiency)\\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\\n2. Signal × regime AUC heatmap (exp-008)\\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\\n\\n## Citation Requirements (35+ minimum, expanded per Dream D2)\\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\\nDream D2 additions (all 3 tiers flagged):\\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \\\"calibration\\\" — ours is decontamination, not probability calibration)\\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\\n\\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\\n\", \"total_chars\": 13227, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "a03b7403-1063-4158-b8fe-7f21f0e749eb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — contamcal-irt-calibration\\\\n\\\\n## Target Venue\\\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\\\n- Track: Machine Learning for NLP / Resources and Evaluation\\\\n- Aligns with EMNLP 2026 special theme \\\\\\\"New Missions for NLP Research\\\\\\\" (explicitly invites contamination/data governance work)\\\\n\\\\n## Core Insight\\\\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\\\\n\\\\n## Core Claims (3 条)\\\\n\\\\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)\\\\n\\\\n2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.\\\\n\\\\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.\\\\n\\\\n## Contributions (Hierarchical)\\\\n\\\\n### Core\\\\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals\\\\n2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)\\\\n3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)\\\\n\\\\n### Supporting\\\\n4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds\\\\n5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology\\\\n\\\\n## Story Spine\\\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering \\\\\\\"what would this model's score be if it had never seen the test data?\\\\\\\"\\\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\\\n- **Our framing**: ContamCal is a \\\\\\\"statistical safety net\\\\\\\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).\\\\n- **Headline result template**: \\\\\\\"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\\\\\\\"\\\\n\\\\n## Venue Fit Risks\\\\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\\\\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\\\\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \\\\\\\"new algorithm\\\\\\\" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\\\\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \\\\\\\"calibration is only as good as its inputs.\\\\\\\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\\\\n\\\\n## Anticipated Reviewer Concerns & Defenses\\\\n\\\\n| # | Concern | Defense | Experiment |\\\\n|---|---------|---------|------------|\\\\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\\\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\\\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \\\\\\\"best-available proxy\\\\\\\", acknowledged as limitation | exp-006, exp-009 |\\\\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\\\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\\\\n| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |\\\\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\\\\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\\\\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\\\\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\\\\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\\\\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\\\\n\\\\n## Evaluation Protocol (5 Metrics)\\\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\\\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\\\n\\\\n## Benchmarks (3 main + 1 appendix)\\\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\\\\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\\\\n3. **ARC-Challenge** — science reasoning multiple-choice\\\\n4. **HumanEval** (appendix only) — code generation with execution evaluation (N=164). Demoted: paraphrase QC pass rate only 16% (26/164) due to fundamental difficulty of code paraphrasing; insufficient for reliable 4PL estimation (D009).\\\\n\\\\n## Baselines (7)\\\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\\\n\\\\n## Local Independence Discussion\\\\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\\\\n\\\\n## Required Figures (Dream D2: \\\\\\\"zero figures\\\\\\\" flagged as serious deficiency)\\\\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\\\\n2. Signal × regime AUC heatmap (exp-008)\\\\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\\\\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\\\\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\\\\n\\\\n## Citation Requirements (35+ minimum, expanded per Dream D2)\\\\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\\\\nDream D2 additions (all 3 tiers flagged):\\\\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\\\\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \\\\\\\"calibration\\\\\\\" — ours is decontamination, not probability calibration)\\\\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\\\\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\\\\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\\\\n\\\\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\\\\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\\\\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\\\\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\\\\n\\\", \\\"total_chars\\\": 13227, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight\\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\\n\\n## Core Claims (3 条)\\n\\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)\\n\\n2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.\\n\\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.\\n\\n## Contributions (Hierarchical)\\n\\n### Core\\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals\\n2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)\\n3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)\\n\\n### Supporting\\n4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds\\n5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\n- **Our framing**: ContamCal is a \\\"statistical safety net\\\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).\\n- **Headline result template**: \\\"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\\\"\\n\\n## Venue Fit Risks\\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \\\"new algorithm\\\" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \\\"calibration is only as good as its inputs.\\\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\\n\\n## Anticipated Reviewer Concerns & Defenses\\n\\n| # | Concern | Defense | Experiment |\\n|---|---------|---------|------------|\\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \\\"best-available proxy\\\", acknowledged as limitation | exp-006, exp-009 |\\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\\n| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |\\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\\n\\n## Evaluation Protocol (5 Metrics)\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\n\\n## Benchmarks (3 main + 1 appendix)\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\\n3. **ARC-Challenge** — science reasoning multiple-choice\\n4. **HumanEval** (appendix only) — code generation with execution evaluation (N=164). Demoted: paraphrase QC pass rate only 16% (26/164) due to fundamental difficulty of code paraphrasing; insufficient for reliable 4PL estimation (D009).\\n\\n## Baselines (7)\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\n\\n## Local Independence Discussion\\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\\n\\n## Required Figures (Dream D2: \\\"zero figures\\\" flagged as serious deficiency)\\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\\n2. Signal × regime AUC heatmap (exp-008)\\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\\n\\n## Citation Requirements (35+ minimum, expanded per Dream D2)\\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\\nDream D2 additions (all 3 tiers flagged):\\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \\\"calibration\\\" — ours is decontamination, not probability calibration)\\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\\n\\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\\n\", \"total_chars\": 13227, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UYb3aRtDSJTiSFH3FgfhDi`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "experiment_plan.yaml",
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
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "654d4050-04f6-4e90-8404-615b43967ea9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pxQVYaD2WKmQK4pPrLRCx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 23210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1062
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

_source line 11 · 2026-05-14T04:16:44.967Z_

<details><summary>↩ Tool result · `toolu_01UYb3aRtDSJTiSFH3FgfhDi`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "3ae77993-24c6-4e84-b0be-4629a800c3ca",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__compute_coverage_matrix · `toolu_01SxRyqaoRsE7MAoiDbpDKCS`</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "431c4270-e9cb-4a98-8cae-64fa87306b38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pxQVYaD2WKmQK4pPrLRCx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 23210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1062
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

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01G3ueLoR5aYUGAZxhwU9XrY`</summary>

```json
{
  "project": "contamcal-irt-calibration",
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
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "51320f1e-20bc-4052-8025-c56b90e02f89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pxQVYaD2WKmQK4pPrLRCx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 23210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1062
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

_source line 14 · 2026-05-14T04:16:45.997Z_

<details><summary>↩ Tool result · `toolu_01SxRyqaoRsE7MAoiDbpDKCS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"claims\": [1, 2, 3], \"matrix\": {\"1\": {\"experiments\": [{\"id\": \"exp-001\", \"name\": \"controlled_sft_injection\", \"claim\": 1, \"description\": \"SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std). Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent) with controlled semantic similarity — following methodology of \\\"Rethinking Benchmark and Contamination\\\" (arXiv 2023). Target: high semantic similarity (cosine >0.85) but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving contamination effect. Quality validation: automated similarity metrics + human spot-check on 50 random pairs per benchmark.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 50, \"deps\": [], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"models\": [\"Qwen2.5-0.5B\", \"Qwen2.5-1.5B\", \"Qwen2.5-3B\"], \"seeds\": 3, \"registry_id\": \"exp_001_sft_d100_15B_v2\", \"status\": \"RUNNING\"}, {\"id\": \"exp-004\", \"name\": \"simulation_identifiability_sweep\", \"claim\": 1, \"also_supports\": [3], \"description\": \"Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \\\"cannot distinguish no contamination from moderate contamination.\\\" N_items=300 fixed (per MVP finding). Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment: at N_models=20/50, compare flat prior vs informative prior from pre-estimated item parameters. Also includes Fisher Information matrix analysis: derive approximate analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish structural identifiability (parameters uniquely determined) from practical identifiability (estimation quality sufficient for decisions). Provides theoretical grounding for the empirical AUC ≥ 0.70 threshold.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 0, \"deps\": [], \"note\": \"CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\", \"registry_id\": \"exp_004_sim_sweep\", \"status\": \"RUNNING\", \"conclusion\": null}, {\"id\": \"exp-006\", \"name\": \"irt_calibration_and_baselines\", \"claim\": 1, \"also_supports\": [3], \"description\": \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION: joint fitting across benchmarks with shared global γ (stronger assumption, tests whether contamination effect is homogeneous across benchmarks). Report both. Per-benchmark fitting (not joint) is the default to reduce local independence violation scope. Posterior predictive checks on item-level residual correlations to assess local independence empirically. Compute calibrated scores via exposure=0 counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no contamination modeling), (4) linear exposure regression + bootstrap CI (simplest post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report mean ± std across 3 seeds (matched to exp-001 seeds).\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 8, \"deps\": [\"exp-003\"], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"seeds\": 3, \"status\": \"planned\"}, {\"id\": \"exp-015\", \"name\": \"sft_d100_qc_only\", \"claim\": 1, \"description\": \"100% dosage SFT using only QC-pass paraphrases (7547/16697 items). Isolates noisy vs clean contamination confound identified by reviewer. D012 decision. Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify effect of noisy contamination on IRT estimates.\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 5, \"deps\": [\"exp-001\"], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"models\": [\"Qwen2.5-0.5B\"], \"seeds\": 1, \"status\": \"orphaned\", \"registry_id\": \"exp_001_sft_d100_qc_only\", \"data_script\": \"exp001/prepare_qc_only_data.py\"}, {\"id\": \"exp-007\", \"name\": \"scale_bridging_7b\", \"claim\": 1, \"description\": \"Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 30, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-014\", \"name\": \"multi_family_validation\", \"claim\": 1, \"description\": \"Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream reviewer concern about single model family limiting generalizability (flagged [M][W]).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-012\", \"name\": \"observational_72b\", \"claim\": 1, \"description\": \"Qwen2.5-72B observational analysis (inference only, no SFT). Extends ecological validity to frontier model scale.\\n\", \"priority\": \"P2\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-006\"], \"status\": \"planned\"}], \"counts\": {\"planned\": 4, \"running\": 2, \"done\": 0, \"failed\": 0, \"orphaned\": 1}, \"total\": 7, \"coverage\": \"0/7\", \"coverage_pct\": 0.0}, \"2\": {\"experiments\": [{\"id\": \"exp-002\", \"name\": \"stage1_signal_pipeline\", \"claim\": 2, \"description\": \"Compute 4 detection signals on all contaminated + clean models from exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers), (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores for each signal.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 20, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-003\", \"name\": \"rrf_aggregation_ablation\", \"claim\": 2, \"description\": \"RRF fusion of 4 signals into composite per-item exposure score. Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based weighted RRF variant, (d) false positive injection robustness check (inject FP at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 2, \"deps\": [\"exp-002\"], \"status\": \"planned\"}, {\"id\": \"exp-008\", \"name\": \"signal_survival_analysis\", \"claim\": 2, \"description\": \"Systematic evaluation of detection signal reliability across training regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated, RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 10, \"deps\": [\"exp-002\"], \"status\": \"planned\"}, {\"id\": \"exp-009\", \"name\": \"rl_observational_case_study\", \"claim\": 2, \"also_supports\": [3], \"description\": \"Apply Self-Critique + available signals to existing RL-trained models: Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with appropriately wider CIs. Expected regret quantification: compare uncalibrated vs calibrated vs remove-rescore for top-5 model selection. Framed as observational — directional external validity, not full quantitative validation. Near-zero γ check on known-clean benchmark (specificity test).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-006\", \"exp-008\"], \"status\": \"planned\"}, {\"id\": \"exp-013\", \"name\": \"closed_weight_2signal_mode\", \"claim\": 2, \"description\": \"Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings) for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration accuracy gap.\\n\", \"priority\": \"P2\", \"gpu_budget_hours\": 5, \"deps\": [\"exp-003\"], \"status\": \"planned\"}], \"counts\": {\"planned\": 5, \"running\": 0, \"done\": 0, \"failed\": 0, \"orphaned\": 0}, \"total\": 5, \"coverage\": \"0/5\", \"coverage_pct\": 0.0}, \"3\": {\"experiments\": [{\"id\": \"exp-005\", \"name\": \"noise_propagation_analysis\", \"claim\": 3, \"description\": \"Two parts: (A) Measurement error model (PRIMARY): extend Stan model to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates. This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure CI widening for γ and θ. Both parts inform whether measurement error model closes the coverage gap.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 0, \"deps\": [\"exp-002\", \"exp-004\"], \"note\": \"CPU only\", \"registry_id\": \"exp_005_noise_prop_v2\", \"status\": \"DONE\", \"conclusion\": \"failed\"}], \"counts\": {\"planned\": 0, \"running\": 0, \"done\": 0, \"failed\": 1, \"orphaned\": 0}, \"total\": 1, \"coverage\": \"0/1\", \"coverage_pct\": 0.0}}, \"unassigned\": [], \"summary\": {\"total_experiments\": 13, \"total_claims\": 3, \"counts\": {\"planned\": 9, \"running\": 2, \"done\": 0, \"failed\": 1, \"orphaned\": 1}, \"coverage\": \"0/13\", \"coverage_pct\": 0.0, \"unassigned\": 0}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "a35eb6cb-390b-4ee2-90e2-6a47c06657ae",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"claims\\\": [1, 2, 3], \\\"matrix\\\": {\\\"1\\\": {\\\"experiments\\\": [{\\\"id\\\": \\\"exp-001\\\", \\\"name\\\": \\\"controlled_sft_injection\\\", \\\"claim\\\": 1, \\\"description\\\": \\\"SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std). Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent) with controlled semantic similarity — following methodology of \\\\\\\"Rethinking Benchmark and Contamination\\\\\\\" (arXiv 2023). Target: high semantic similarity (cosine >0.85) but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving contamination effect. Quality validation: automated similarity metrics + human spot-check on 50 random pairs per benchmark.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 50, \\\"deps\\\": [], \\\"benchmarks\\\": [\\\"MMLU\\\", \\\"GSM8K\\\", \\\"ARC-Challenge\\\", \\\"HumanEval\\\"], \\\"models\\\": [\\\"Qwen2.5-0.5B\\\", \\\"Qwen2.5-1.5B\\\", \\\"Qwen2.5-3B\\\"], \\\"seeds\\\": 3, \\\"registry_id\\\": \\\"exp_001_sft_d100_15B_v2\\\", \\\"status\\\": \\\"RUNNING\\\"}, {\\\"id\\\": \\\"exp-004\\\", \\\"name\\\": \\\"simulation_identifiability_sweep\\\", \\\"claim\\\": 1, \\\"also_supports\\\": [3], \\\"description\\\": \\\"Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \\\\\\\"cannot distinguish no contamination from moderate contamination.\\\\\\\" N_items=300 fixed (per MVP finding). Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment: at N_models=20/50, compare flat prior vs informative prior from pre-estimated item parameters. Also includes Fisher Information matrix analysis: derive approximate analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish structural identifiability (parameters uniquely determined) from practical identifiability (estimation quality sufficient for decisions). Provides theoretical grounding for the empirical AUC ≥ 0.70 threshold.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 0, \\\"deps\\\": [], \\\"note\\\": \\\"CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\\\", \\\"registry_id\\\": \\\"exp_004_sim_sweep\\\", \\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": null}, {\\\"id\\\": \\\"exp-006\\\", \\\"name\\\": \\\"irt_calibration_and_baselines\\\", \\\"claim\\\": 1, \\\"also_supports\\\": [3], \\\"description\\\": \\\"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION: joint fitting across benchmarks with shared global γ (stronger assumption, tests whether contamination effect is homogeneous across benchmarks). Report both. Per-benchmark fitting (not joint) is the default to reduce local independence violation scope. Posterior predictive checks on item-level residual correlations to assess local independence empirically. Compute calibrated scores via exposure=0 counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no contamination modeling), (4) linear exposure regression + bootstrap CI (simplest post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\\\\n    producing adjusted accuracy; must include or reviewers will reject.\\\\nEvaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report mean ± std across 3 seeds (matched to exp-001 seeds).\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 8, \\\"deps\\\": [\\\"exp-003\\\"], \\\"benchmarks\\\": [\\\"MMLU\\\", \\\"GSM8K\\\", \\\"ARC-Challenge\\\", \\\"HumanEval\\\"], \\\"seeds\\\": 3, \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-015\\\", \\\"name\\\": \\\"sft_d100_qc_only\\\", \\\"claim\\\": 1, \\\"description\\\": \\\"100% dosage SFT using only QC-pass paraphrases (7547/16697 items). Isolates noisy vs clean contamination confound identified by reviewer. D012 decision. Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify effect of noisy contamination on IRT estimates.\\\\n\\\", \\\"priority\\\": \\\"P1\\\", \\\"gpu_budget_hours\\\": 5, \\\"deps\\\": [\\\"exp-001\\\"], \\\"benchmarks\\\": [\\\"MMLU\\\", \\\"GSM8K\\\", \\\"ARC-Challenge\\\", \\\"HumanEval\\\"], \\\"models\\\": [\\\"Qwen2.5-0.5B\\\"], \\\"seeds\\\": 1, \\\"status\\\": \\\"orphaned\\\", \\\"registry_id\\\": \\\"exp_001_sft_d100_qc_only\\\", \\\"data_script\\\": \\\"exp001/prepare_qc_only_data.py\\\"}, {\\\"id\\\": \\\"exp-007\\\", \\\"name\\\": \\\"scale_bridging_7b\\\", \\\"claim\\\": 1, \\\"description\\\": \\\"Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\\\\n\\\", \\\"priority\\\": \\\"P1\\\", \\\"gpu_budget_hours\\\": 30, \\\"deps\\\": [\\\"exp-001\\\"], \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-014\\\", \\\"name\\\": \\\"multi_family_validation\\\", \\\"claim\\\": 1, \\\"description\\\": \\\"Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream reviewer concern about single model family limiting generalizability (flagged [M][W]).\\\\n\\\", \\\"priority\\\": \\\"P1\\\", \\\"gpu_budget_hours\\\": 15, \\\"deps\\\": [\\\"exp-001\\\"], \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-012\\\", \\\"name\\\": \\\"observational_72b\\\", \\\"claim\\\": 1, \\\"description\\\": \\\"Qwen2.5-72B observational analysis (inference only, no SFT). Extends ecological validity to frontier model scale.\\\\n\\\", \\\"priority\\\": \\\"P2\\\", \\\"gpu_budget_hours\\\": 15, \\\"deps\\\": [\\\"exp-006\\\"], \\\"status\\\": \\\"planned\\\"}], \\\"counts\\\": {\\\"planned\\\": 4, \\\"running\\\": 2, \\\"done\\\": 0, \\\"failed\\\": 0, \\\"orphaned\\\": 1}, \\\"total\\\": 7, \\\"coverage\\\": \\\"0/7\\\", \\\"coverage_pct\\\": 0.0}, \\\"2\\\": {\\\"experiments\\\": [{\\\"id\\\": \\\"exp-002\\\", \\\"name\\\": \\\"stage1_signal_pipeline\\\", \\\"claim\\\": 2, \\\"description\\\": \\\"Compute 4 detection signals on all contaminated + clean models from exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers), (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores for each signal.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 20, \\\"deps\\\": [\\\"exp-001\\\"], \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-003\\\", \\\"name\\\": \\\"rrf_aggregation_ablation\\\", \\\"claim\\\": 2, \\\"description\\\": \\\"RRF fusion of 4 signals into composite per-item exposure score. Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based weighted RRF variant, (d) false positive injection robustness check (inject FP at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 2, \\\"deps\\\": [\\\"exp-002\\\"], \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-008\\\", \\\"name\\\": \\\"signal_survival_analysis\\\", \\\"claim\\\": 2, \\\"description\\\": \\\"Systematic evaluation of detection signal reliability across training regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated, RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 10, \\\"deps\\\": [\\\"exp-002\\\"], \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-009\\\", \\\"name\\\": \\\"rl_observational_case_study\\\", \\\"claim\\\": 2, \\\"also_supports\\\": [3], \\\"description\\\": \\\"Apply Self-Critique + available signals to existing RL-trained models: Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with appropriately wider CIs. Expected regret quantification: compare uncalibrated vs calibrated vs remove-rescore for top-5 model selection. Framed as observational — directional external validity, not full quantitative validation. Near-zero γ check on known-clean benchmark (specificity test).\\\\n\\\", \\\"priority\\\": \\\"P1\\\", \\\"gpu_budget_hours\\\": 15, \\\"deps\\\": [\\\"exp-006\\\", \\\"exp-008\\\"], \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-013\\\", \\\"name\\\": \\\"closed_weight_2signal_mode\\\", \\\"claim\\\": 2, \\\"description\\\": \\\"Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings) for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration accuracy gap.\\\\n\\\", \\\"priority\\\": \\\"P2\\\", \\\"gpu_budget_hours\\\": 5, \\\"deps\\\": [\\\"exp-003\\\"], \\\"status\\\": \\\"planned\\\"}], \\\"counts\\\": {\\\"planned\\\": 5, \\\"running\\\": 0, \\\"done\\\": 0, \\\"failed\\\": 0, \\\"orphaned\\\": 0}, \\\"total\\\": 5, \\\"coverage\\\": \\\"0/5\\\", \\\"coverage_pct\\\": 0.0}, \\\"3\\\": {\\\"experiments\\\": [{\\\"id\\\": \\\"exp-005\\\", \\\"name\\\": \\\"noise_propagation_analysis\\\", \\\"claim\\\": 3, \\\"description\\\": \\\"Two parts: (A) Measurement error model (PRIMARY): extend Stan model to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates. This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure CI widening for γ and θ. Both parts inform whether measurement error model closes the coverage gap.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 0, \\\"deps\\\": [\\\"exp-002\\\", \\\"exp-004\\\"], \\\"note\\\": \\\"CPU only\\\", \\\"registry_id\\\": \\\"exp_005_noise_prop_v2\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}], \\\"counts\\\": {\\\"planned\\\": 0, \\\"running\\\": 0, \\\"done\\\": 0, \\\"failed\\\": 1, \\\"orphaned\\\": 0}, \\\"total\\\": 1, \\\"coverage\\\": \\\"0/1\\\", \\\"coverage_pct\\\": 0.0}}, \\\"unassigned\\\": [], \\\"summary\\\": {\\\"total_experiments\\\": 13, \\\"total_claims\\\": 3, \\\"counts\\\": {\\\"planned\\\": 9, \\\"running\\\": 2, \\\"done\\\": 0, \\\"failed\\\": 1, \\\"orphaned\\\": 1}, \\\"coverage\\\": \\\"0/13\\\", \\\"coverage_pct\\\": 0.0, \\\"unassigned\\\": 0}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"claims\": [1, 2, 3], \"matrix\": {\"1\": {\"experiments\": [{\"id\": \"exp-001\", \"name\": \"controlled_sft_injection\", \"claim\": 1, \"description\": \"SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std). Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent) with controlled semantic similarity — following methodology of \\\"Rethinking Benchmark and Contamination\\\" (arXiv 2023). Target: high semantic similarity (cosine >0.85) but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving contamination effect. Quality validation: automated similarity metrics + human spot-check on 50 random pairs per benchmark.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 50, \"deps\": [], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"models\": [\"Qwen2.5-0.5B\", \"Qwen2.5-1.5B\", \"Qwen2.5-3B\"], \"seeds\": 3, \"registry_id\": \"exp_001_sft_d100_15B_v2\", \"status\": \"RUNNING\"}, {\"id\": \"exp-004\", \"name\": \"simulation_identifiability_sweep\", \"claim\": 1, \"also_supports\": [3], \"description\": \"Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \\\"cannot distinguish no contamination from moderate contamination.\\\" N_items=300 fixed (per MVP finding). Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment: at N_models=20/50, compare flat prior vs informative prior from pre-estimated item parameters. Also includes Fisher Information matrix analysis: derive approximate analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish structural identifiability (parameters uniquely determined) from practical identifiability (estimation quality sufficient for decisions). Provides theoretical grounding for the empirical AUC ≥ 0.70 threshold.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 0, \"deps\": [], \"note\": \"CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\", \"registry_id\": \"exp_004_sim_sweep\", \"status\": \"RUNNING\", \"conclusion\": null}, {\"id\": \"exp-006\", \"name\": \"irt_calibration_and_baselines\", \"claim\": 1, \"also_supports\": [3], \"description\": \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION: joint fitting across benchmarks with shared global γ (stronger assumption, tests whether contamination effect is homogeneous across benchmarks). Report both. Per-benchmark fitting (not joint) is the default to reduce local independence violation scope. Posterior predictive checks on item-level residual correlations to assess local independence empirically. Compute calibrated scores via exposure=0 counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no contamination modeling), (4) linear exposure regression + bootstrap CI (simplest post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report mean ± std across 3 seeds (matched to exp-001 seeds).\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 8, \"deps\": [\"exp-003\"], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"seeds\": 3, \"status\": \"planned\"}, {\"id\": \"exp-015\", \"name\": \"sft_d100_qc_only\", \"claim\": 1, \"description\": \"100% dosage SFT using only QC-pass paraphrases (7547/16697 items). Isolates noisy vs clean contamination confound identified by reviewer. D012 decision. Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify effect of noisy contamination on IRT estimates.\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 5, \"deps\": [\"exp-001\"], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"models\": [\"Qwen2.5-0.5B\"], \"seeds\": 1, \"status\": \"orphaned\", \"registry_id\": \"exp_001_sft_d100_qc_only\", \"data_script\": \"exp001/prepare_qc_only_data.py\"}, {\"id\": \"exp-007\", \"name\": \"scale_bridging_7b\", \"claim\": 1, \"description\": \"Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 30, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-014\", \"name\": \"multi_family_validation\", \"claim\": 1, \"description\": \"Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream reviewer concern about single model family limiting generalizability (flagged [M][W]).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-012\", \"name\": \"observational_72b\", \"claim\": 1, \"description\": \"Qwen2.5-72B observational analysis (inference only, no SFT). Extends ecological validity to frontier model scale.\\n\", \"priority\": \"P2\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-006\"], \"status\": \"planned\"}], \"counts\": {\"planned\": 4, \"running\": 2, \"done\": 0, \"failed\": 0, \"orphaned\": 1}, \"total\": 7, \"coverage\": \"0/7\", \"coverage_pct\": 0.0}, \"2\": {\"experiments\": [{\"id\": \"exp-002\", \"name\": \"stage1_signal_pipeline\", \"claim\": 2, \"description\": \"Compute 4 detection signals on all contaminated + clean models from exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers), (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores for each signal.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 20, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-003\", \"name\": \"rrf_aggregation_ablation\", \"claim\": 2, \"description\": \"RRF fusion of 4 signals into composite per-item exposure score. Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based weighted RRF variant, (d) false positive injection robustness check (inject FP at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 2, \"deps\": [\"exp-002\"], \"status\": \"planned\"}, {\"id\": \"exp-008\", \"name\": \"signal_survival_analysis\", \"claim\": 2, \"description\": \"Systematic evaluation of detection signal reliability across training regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated, RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 10, \"deps\": [\"exp-002\"], \"status\": \"planned\"}, {\"id\": \"exp-009\", \"name\": \"rl_observational_case_study\", \"claim\": 2, \"also_supports\": [3], \"description\": \"Apply Self-Critique + available signals to existing RL-trained models: Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with appropriately wider CIs. Expected regret quantification: compare uncalibrated vs calibrated vs remove-rescore for top-5 model selection. Framed as observational — directional external validity, not full quantitative validation. Near-zero γ check on known-clean benchmark (specificity test).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-006\", \"exp-008\"], \"status\": \"planned\"}, {\"id\": \"exp-013\", \"name\": \"closed_weight_2signal_mode\", \"claim\": 2, \"description\": \"Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings) for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration accuracy gap.\\n\", \"priority\": \"P2\", \"gpu_budget_hours\": 5, \"deps\": [\"exp-003\"], \"status\": \"planned\"}], \"counts\": {\"planned\": 5, \"running\": 0, \"done\": 0, \"failed\": 0, \"orphaned\": 0}, \"total\": 5, \"coverage\": \"0/5\", \"coverage_pct\": 0.0}, \"3\": {\"experiments\": [{\"id\": \"exp-005\", \"name\": \"noise_propagation_analysis\", \"claim\": 3, \"description\": \"Two parts: (A) Measurement error model (PRIMARY): extend Stan model to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates. This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure CI widening for γ and θ. Both parts inform whether measurement error model closes the coverage gap.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 0, \"deps\": [\"exp-002\", \"exp-004\"], \"note\": \"CPU only\", \"registry_id\": \"exp_005_noise_prop_v2\", \"status\": \"DONE\", \"conclusion\": \"failed\"}], \"counts\": {\"planned\": 0, \"running\": 0, \"done\": 0, \"failed\": 1, \"orphaned\": 0}, \"total\": 1, \"coverage\": \"0/1\", \"coverage_pct\": 0.0}}, \"unassigned\": [], \"summary\": {\"total_experiments\": 13, \"total_claims\": 3, \"counts\": {\"planned\": 9, \"running\": 2, \"done\": 0, \"failed\": 1, \"orphaned\": 1}, \"coverage\": \"0/13\", \"coverage_pct\": 0.0, \"unassigned\": 0}}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T04:16:47.380Z_

<details><summary>↩ Tool result · `toolu_01G3ueLoR5aYUGAZxhwU9XrY`</summary>

```text
Error: result (69,378 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "06805d31-41e2-4765-aedd-a601e87b027f",
  "tool_use_result": {
    "content": "Error: result (69,378 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_004_sim_sweep\": {\"completed_at\": \"2026-05-14T03:41:12.265Z\", \"conclusion\": null, \"created_at\": \"2026-05-13T16:43:57.478Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T03:41:29.791249+00:00\"}]}, \"failure_reason\": \"SSH check failed 5x — last error: Unknown server 'local'. Available: ['cqa1-21977']\", \"hypothesis\": \"4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which γ 95% CI width exceeds 15pp; recovery improves with N_models; prior sensitivity is bounded\", \"retry_count\": 0, \"spec\": {\"log_path\": \"/tmp/exp004_sweep.log\", \"pid\": \"340553\", \"timeout_per_fit\": 7200}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T03:44:17.318015+00:00\"}, \"exp_005_noise_prop_v3\": {\"completed_at\": \"2026-05-14T03:29:53.328Z\", \"conclusion\": null, \"created_at\": \"2026-05-14T03:24:06.949Z\", \"hypothesis\": \"Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic ME (1231 params), checkpoint resume.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/exp005_noise_propagation/output_v3\", \"command\": \"cd artifacts/exp005_noise_propagation && nohup .venv/bin/python run_noise_propagation_v3.py --output-dir output_v3 --base-seed 42 --n-seeds 5 > exp005_v3.log 2>&1 &\", \"data_count\": 9000, \"data_path\": \"synthetic\", \"log_path\": \"artifacts/exp005_noise_propagation/exp005_v3.log\", \"model_name\": \"4PL+gamma IRT (simple + analytic ME)\", \"note\": \"v3: Stan output on local disk, analytic ME model (1231 params vs 10231), simple-first then ME, checkpoint resume support, chain CSV cleanup after each fit. 5 sigma_e levels x 5 seeds x 2 models = 50 fits. ETA ~11-12 hours (Simple ~125min, Analytic ME ~575min)\", \"pid\": \"339838\", \"seed\": 42, \"server\": \"local\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T03:36:19.610665Z\"}, \"exp_005_noise_prop_v2\": {\"completed_at\": \"2026-05-13T22:44:09.262Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T20:47:35.807Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T21:09:53.826444+00:00\"}, {\"action\": \"manual_fix\", \"event\": \"status_rollback\", \"reason\": \"Cron false positive: server=\\\"local\\\" not in SSH list. PID 251971 alive, 2 Stan chains at 42% CPU. Rolled back DONE/failed → RUNNING.\", \"ts\": \"2026-05-13T21:12:00.000Z\"}]}, \"failure_reason\": \"根因：/tmp tmpfs 磁盘配额耗尽。ME model 先跑 95min 生成 ~1GB CSV（9000 tau + 9000 log_lik × 4 chains）耗尽 3.9GB tmpfs。Simple model 写 CSV 时 disk quota exceeded → 4 chains 全部 retcode=1。ME model Rhat=1.945 是独立问题：10231 参数 vs 9000 观测，严重欠识别，需换用 analytic 版本。修复：(1) output_dir 设到非 tmpfs (2) 先跑 simple 再跑 ME (3) ME 换 contam_irt_4pl_me_analytic.stan (4) σ_e=0.1/0.3 均可收敛。\", \"hypothesis\": \"Same as exp_005: ME model CI width increases monotonically with σ_e; simple model does not. v2 fixes: sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12.\", \"notes\": \"失败根因: 1) /tmp tmpfs 3.9GB 耗尽（ME模型生成~1GB Stan CSV，Simple 4 chains全部retcode=1）; 2) ME模型严重欠识别（10231参数 vs 9000观测，Rhat=1.945）。诊断结果: σ_e=0.3 simple收敛良好(γ=0.458, true=0.5, Rhat=1.007); σ_e=0.1 simple收敛但γ偏高57.5%(0.788 vs 0.5)——identifiability限制非bug。v3已启动修复两个根因。\", \"parent\": \"exp_005_noise_prop\", \"retry_count\": 0, \"spec\": {\"command\": \"python run_noise_propagation.py --output-dir output_v2 --base-seed 42 --n-seeds 5\", \"data_count\": \"5 σ_e levels × 5 seeds × 2 models = 50 Stan fits\", \"data_path\": \"synthetic (generated in-script)\", \"fixes\": \"sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12\", \"log_path\": \"artifacts/exp005_noise_propagation/exp005_v2.log\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS, max_treedepth=12)\", \"pid\": 251971, \"seed\": \"42-46\", \"server\": \"local (CPU only)\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T03:25:33.715Z\"}, \"exp_001_sft_d005_15B\": {\"created_at\": \"2026-05-14T00:19:54.331Z\", \"gpu\": 4, \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): low-dosage contamination for dose-response curve, Phase 3 priority 1\", \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42 --gpu 4 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": 50826, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"gpu\": [\"cuda:4\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_15B.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"271916\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T03:12:39.622Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T03:17:38.946Z\"}, \"exp_001_eval_15B_d000_s42_v2\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter\", \"completed_at\": \"2026-05-14T03:12:11.373Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:23:20.112Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T03:09:29.636850+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log\", \"metrics\": {\"arc_challenge_accuracy\": 0.7756, \"arc_challenge_correct\": 909, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 840, \"gsm8k_exact_match\": 0.6368, \"gsm8k_total\": 1319, \"humaneval_correct\": 21, \"humaneval_pass_at_1\": 0.128, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5753, \"mmlu_correct\": 8079, \"mmlu_total\": 14042}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:09:26.521Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:4\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"243290\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:23:34.122Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10117.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T03:12:11.373Z\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T00:48:57.772Z\", \"hypothesis\": \"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\", \"retry_count\": 0, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T03:06:54.726Z\"}, \"exp_001_eval_05B_d000_s42_v6\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:40:46.586Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v6.log\", \"pid\": \"267141\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:40:46.245Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:47:17.653Z\"}, \"exp_001_eval_05B_d100_v6\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:40:56.017Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v6.log\", \"pid\": \"267346\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:40:55.558Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:47:16.586Z\"}, \"exp_001_eval_05B_d100_v5\": {\"created_at\": \"2026-05-14T02:39:57.338Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\\\"\", \"data_count\": 4, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v5.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d100_05B\", \"pid\": \"266780\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:39:57.046Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T02:46:56.726Z\"}, \"exp_001_eval_05B_d000_s42_v5\": {\"created_at\": \"2026-05-14T02:39:41.292Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\\\"\", \"data_count\": 4, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v5.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_0pct_05B\", \"pid\": \"266511\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:39:41.108Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T02:46:54.180Z\"}, \"exp_001_eval_05B_d100_v4\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:36:09.066Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v4.log\", \"pid\": \"265684\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:36:08.570Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:40:10.093Z\"}, \"exp_001_eval_05B_d000_s42_v4\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:35:30.672Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v4.log\", \"pid\": \"265362\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:35:30.362Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:40:09.432Z\"}, \"exp_001_eval_05B_d100_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T02:26:41.093Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:37:02.468237+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:36:56.211Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v2.log\", \"pid\": \"263784\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:28:36.407Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PENDING\", \"updated_at\": \"2026-05-14T02:39:52.993Z\"}, \"exp_001_eval_05B_d000_s42_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T02:26:38.504Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:36:53.124182+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:36:49.559Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v2.log\", \"pid\": \"263528\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:28:26.942Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:36:51.089Z\"}, \"exp_001_eval_05B_d100_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:30:53.668Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v3.log\", \"pid\": \"264324\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:30:53.531Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:33:52.158Z\"}, \"exp_001_eval_05B_d000_s42_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:30:50.700Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v3.log\", \"pid\": \"264245\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:30:50.572Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:33:51.502Z\"}, \"exp_001_eval_05B_d100\": {\"completed_at\": \"2026-05-14T02:21:35.372Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-14T01:15:49.903Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:21:37.615359+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:21:33.626Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 4, \"data_path\": \"d100 contaminated checkpoint\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 0.88, \"gpu_ids\": [\"cuda:2\"], \"hypothesis\": \"0.5B 100% dosage contaminated model eval on 4 benchmarks — upper bound of contamination-induced score inflation\", \"log_path\": \"/tmp/eval_d100.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d100_05B\", \"pid\": \"254667\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T01:29:00Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3155.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T02:21:35.372Z\"}, \"exp_001_eval_05B_d005\": {\"created_at\": \"2026-05-14T01:17:07.820Z\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 0, \"data_path\": \"d005 contaminated checkpoint\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": \"cuda:1\", \"hypothesis\": \"0.5B 5% dosage contaminated model eval on 4 benchmarks — low-dosage contamination detection sensitivity test\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_eval_05B_d005.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d005_05B\", \"pid\": \"255322\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T02:15:00.000Z\"}, \"exp_001_eval_05B_d000_s42\": {\"completed_at\": \"2026-05-14T01:29:11.220Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T22:42:34.313Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T01:29:13.572174+00:00\"}]}, \"failure_reason\": \"Traceback → ration/exp001/evaluate.py\\\", line 558, in main all_results[\\\"benchmarks\\\"][benchmark] = result ^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: '/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json'\", \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"notes\": \"失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议: 修复 evaluate.py 中保存前的 os.makedirs 调用后重跑\", \"reproduce\": {\"finished_at\": \"2026-05-14T01:29:08.743Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.73, \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log\", \"model_name\": \"Qwen2.5-0.5B\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\", \"parent\": \"exp_001_05B_d000_s42\", \"pid\": \"229370\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T22:45:41.096Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9810.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:33:03.857Z\"}, \"exp_001_eval_05B_d000_s123\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter\", \"completed_at\": \"2026-05-14T01:29:09.875Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T22:30:40.455Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T01:26:32.038369+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log\", \"metrics\": {\"arc_challenge_accuracy\": 0.3976, \"gsm8k_exact_match\": 0.3404, \"humaneval_pass_at_1\": 0.1037, \"mmlu_accuracy\": 0.4182}, \"reproduce\": {\"finished_at\": \"2026-05-14T01:26:29.607Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": null, \"data_path\": \"d000 (baseline, no contamination)\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 2.72, \"gpu_ids\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_train_05B_d000_s123\", \"pid\": \"229516\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T22:45:48.124Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9801.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:29:09.875Z\"}, \"exp_001_sft_d100_15B\": {\"completed_at\": \"2026-05-14T01:23:40.712Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:37:43.653Z\", \"failure_reason\": \"OOM batch_size=2, replaced by v2\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error\", \"notes\": \"batch_size=1, grad_accum=16 (防 OOM，与 1.5B d000 baseline 一致)。66533 samples, 1 epoch。数据与 0.5B d100 完全相同，含 MMLU+ARC+GSM8K 全部 paraphrases（noisy contamination condition）。\", \"retry_count\": 0, \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"248993\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:23:40.711Z\"}, \"exp_001_sft_d100_15B_v2\": {\"created_at\": \"2026-05-14T01:17:47.114Z\", \"parent\": \"exp_001_sft_d100_15B\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42\", \"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"gpu\": [\"cuda:0\"], \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): v2 retry with batch_size=1 to fix OOM. Maximum contamination for 1.5B scale.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_15B_v2.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"251924\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T01:18:26.304Z\"}, \"exp_001_eval_15B_d000_s123\": {\"completed_at\": \"2026-05-13T23:39:26.418Z\", \"created_at\": \"2026-05-13T22:30:41.501Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"EXIT_CODE=2: --gpu 0 参数导致 evaluate.py 崩溃。重跑时需去掉 --gpu 参数。\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123\", \"checkpoint_source\": \"exp_001_sft_0pct_15B_s123\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": \"4 benchmarks\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123/\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"250600\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:59:22.874Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T01:18:06.102Z\"}, \"exp_001_sft_d005_05B_v3\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42\", \"completed_at\": \"2026-05-14T00:58:15.977Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:52:39.321Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:55:43.945907+00:00\"}]}, \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5874, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.478, \"lora_adapter_size_mb\": 33.6, \"mean_train_loss\": 1.5424, \"num_tokens\": 19657865, \"token_accuracy\": 0.667, \"total_steps\": 3177, \"train_samples_per_second\": 15.09, \"train_steps_per_second\": 0.943, \"training_time_min\": 56.14, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": -0.0114, \"delta_mean_train_loss\": 0.0036, \"delta_token_accuracy\": -0.015, \"delta_training_time_min\": 3.24}}, \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。v3 已修复 --gpu 5（v1/v2 均为 --gpu 0 错误）。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"parent\": \"exp_001_sft_d005_05B\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:55:38.416Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (SFT retry, not eval)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": 50826, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"eval_data\": \"N/A (SFT retry, not eval)\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 1.0, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v3.log\", \"model_name\": \"Qwen2.5-0.5B\", \"pid\": \"239729\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:58:01.548Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3614.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:58:15.977Z\"}, \"exp_001_sft_d100_05B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42\", \"completed_at\": \"2026-05-14T00:53:49.656Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:36:13.403Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:50:19.949448+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"metrics\": {\"exit_code\": 0, \"final_loss\": 1.5943, \"mean_train_loss\": 1.5662, \"num_tokens\": 21575068, \"token_accuracy\": 0.666, \"total_steps\": 4160, \"train_samples_per_second\": 16.09, \"train_steps_per_second\": 1.006, \"training_time_min\": 68.9, \"vs_baseline_0pct\": {\"accuracy_delta\": \"-0.016 (-2.3%)\", \"loss_delta\": \"+0.0274 (+1.8%)\", \"time_delta\": \"+16min (+30%)\"}}, \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"pid\": \"235243\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T00:50:16.569Z\", \"gpu\": \"cuda:0\", \"server\": \"cqa1-21977\", \"started_at\": \"2026-05-13T23:38:41.749Z\", \"training_hours\": 1.19}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.23, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"pid\": \"235243\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:39:51.510Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4438.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:55:14.218Z\"}, \"exp_001_eval_3B_d000_s42\": {\"completed_at\": \"2026-05-13T23:43:16.876Z\", \"created_at\": \"2026-05-13T23:36:54.086Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v1 --gpu param caused evaluate.py crash. Resubmitted without --gpu.\"}}, \"failure_reason\": \"--gpu 参数导致 evaluate.py 崩溃（与 exp_001_eval_15B_d000_s123 同一 bug）。需去掉 --gpu 参数，用 CUDA_VISIBLE_DEVICES 控制 GPU 分配后重跑。\", \"hypothesis\": \"0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) to establish ground-truth scores for calibration error computation\", \"notes\": \"v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294 confirmed running on GPU 1 (cron monitored).\", \"parent\": \"exp_001_sft_0pct_3B\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"249294\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T08:54:00Z\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T00:55:02.251Z\"}, \"exp_001_sft_0pct\": {\"checkpoint_path\": \"N/A (parent entry)\", \"completed_at\": \"2026-05-14T00:36:52.832Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:26:42.106Z\", \"hypothesis\": \"0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores for calibration error computation; LoRA r=16 alpha=32 1-epoch training on pure instruction data should preserve base model capability\", \"log_path\": \"N/A (parent entry)\", \"notes\": \"Parent entry for 3 sub-experiments (05B/15B/3B). All confirmed running.\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:36:52.832Z\"}, \"exp_001_eval_3B_d000_s123\": {\"created_at\": \"2026-05-14T00:18:07.960Z\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"242581\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:18:36.008Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T00:33:31.970Z\"}, \"exp_001_sft_0pct_3B_s123\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123\", \"completed_at\": \"2026-05-14T00:23:18.290Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:39:01.606Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:16:17.727184+00:00\"}]}, \"hypothesis\": \"0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance estimation)\", \"metrics\": {\"adapter_model_mb\": 114, \"adapter_size_mb\": 488, \"checkpoint_size_mb\": 488, \"epochs\": 1, \"final_loss\": 1.114, \"mean_token_accuracy\": 0.7505, \"mean_train_loss\": 1.1309, \"steps_completed\": 3125, \"total_steps\": 3125, \"total_tokens\": 19555717, \"train_samples_per_second\": 3.91, \"training_time_min\": 213.1}, \"notes\": \"OOM 修复后重提交 --gpu 3 (物理 GPU 3)。Worker 确认 PID 216249 训练中，ETA ~3.4h\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:16:04.357Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123 --seed 123 --gpu 3 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B_s123.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"216935\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:23:18.290Z\"}, \"exp_001_eval_15B_d000_s42\": {\"completed_at\": \"2026-05-14T00:23:17.209Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T21:30:03.433Z\", \"failure_reason\": \"卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。\", \"hypothesis\": \"0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"parent\": \"exp_001_sft_0pct_15B\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/\", \"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --adapter-path lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": \"~26000 items total\", \"data_path\": \"MMLU/GSM8K/ARC-Challenge/HumanEval (HuggingFace datasets)\", \"eval_data\": \"MMLU, GSM8K, ARC-Challenge, HumanEval (original)\", \"gpu\": [\"cuda:4\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42.log\", \"model_name\": \"Qwen2.5-1.5B + LoRA (d000_s42)\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42\", \"pid\": \"221376\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:23:17.209Z\"}, \"exp_001_sft_d005_05B_r3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:58:49.282Z\", \"failure_reason\": \"OOM — v3 (PID 239734) 已占用 GPU 5 全部显存，r3 是重复提交，启动即崩溃。v3 正常运行中，r3 废弃。\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (v1: GPU 5 zombie process; v2: --gpu 0 bug ran on GPU 0 instead of 5). Now uses --gpu 5 correctly.\", \"notes\": \"invalidated — 与 v3 重复提交（间隔 48s），从未实际运行。v3 (PID 239729) 是正确的 run。\", \"parent\": \"exp_001_sft_d005_05B\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_r3.log\", \"pid\": \"240163\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:58:48.937Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T00:12:15.733Z\"}, \"exp_001_eval_3B_d000_s42_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:51:39.462Z\", \"failure_reason\": \"killed by d005 worker reclaiming GPU 5 (SIGKILL, EXIT_CODE=137)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 0, \"data_path\": \"d000\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:5\"], \"hypothesis\": \"0% dosage 3B s42 baseline eval (v2, fix --gpu bug from v1). No --gpu param, use CUDA_VISIBLE_DEVICES via gpu_ids.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_v2.log\", \"model_name\": \"Qwen2.5-3B\", \"parent\": \"exp_001_sft_0pct_3B\", \"pid\": \"237865\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:51:50.500Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T00:12:13.851Z\"}, \"exp_001_sft_d005_05B_v2\": {\"completed_at\": \"2026-05-13T23:49:48.629Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:48:24.508Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:49:51.462263+00:00\"}]}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 578.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 459.38 MiB is free. Process 235248 has 21.47 GiB memory in use. Including non-PyTorch memory, this process has 1.58 GiB memory in use. Of the allocated\", \"gpu\": \"cuda:5\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry after v1 OOM crash (GPU 5 conflict with zombie eval process). GPU 5 now clear.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log\", \"notes\": \"v2 OOM 根因非 GPU 5 残留进程，而是 --gpu 0 导致训练实际跑在 GPU 0（d100 占满 22GB），GPU 5 从未被使用。已在 r3 修复为 --gpu 5。\", \"pid\": \"237300\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-13T23:49:47.033Z\"}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 0.01, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log\", \"pid\": \"237300\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:49:27.702Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:59:33.029Z\"}, \"exp_001_sft_d005_05B\": {\"completed_at\": \"2026-05-13T23:42:35.135Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:36:15.352Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:42:37.857937+00:00\"}]}, \"failure_reason\": \"CUDA OOM at step 8/3177 — zombie 3B eval process (PID 234755) 占 6.8GB GPU 5 显存，导致 SFT 训练分配失败。已重试为 exp_001_sft_d005_05B_v2。\", \"gpu\": \"cuda:5\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): minimum contamination level to detect dose-response threshold; paired with d100 for min-max comparison\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log\", \"notes\": \"v1 OOM at step 8/3177 — GPU 5 有残留进程 PID 234755 占 6.8GB。PID 236994 (submit_training_job 重提交) 也使用了 --gpu 0，实际跑到 GPU 0 而非 GPU 5，同样 OOM。根因：--gpu 0 导致 CUDA_VISIBLE_DEVICES 被脚本覆盖为 0。已在 r3 修复为 --gpu 5。\", \"pid\": \"235331\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-13T23:42:32.872Z\", \"gpu\": \"cuda:5\", \"server\": \"cqa1-21977\", \"started_at\": \"2026-05-13T23:38:42.505Z\", \"training_hours\": 0.06}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log\", \"pid\": \"236994\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:49:14.077Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:59:30.512Z\"}, \"exp_001_sft_100pct_05B\": {\"completed_at\": \"2026-05-13T23:49:10.741Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:41:15.631Z\", \"failure_reason\": \"Duplicate registry entry — actual training tracked by exp_001_sft_d100_05B (PID 235243, cron monitored)\", \"hypothesis\": \"100% contamination dosage on 0.5B establishes upper bound of score inflation; comparing with 0% baseline reveals maximum contamination effect across MMLU/GSM8K/ARC benchmarks\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:49:12.007Z\"}, \"exp_001_sft_0pct_3B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42\", \"completed_at\": \"2026-05-13T23:25:49.016Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:44:40.471Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T23:23:43.393661+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"metrics\": {\"adapter_size_mb\": 115, \"checkpoint_size_mb\": 488, \"exit_code\": 0, \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"steps\": \"3125/3125\", \"token_accuracy\": 0.734, \"training_time_min\": 214.7}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:23:41.844Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 3.69, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"pid\": \"210666\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:44:40.431Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13268.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:25:49.016Z\"}, \"exp_001_sft_injection\": {\"completed_at\": \"2026-05-13T23:14:30.258Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T17:28:01.546Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T19:18:08.635006+00:00\"}, {\"action\": \"manual_fix\", \"event\": \"status_rollback\", \"reason\": \"Cron misidentified old PID as dead → auto-failed. 3 paraphrase processes (GPU 0-2) still running. Rolled back DONE/failed → RUNNING per Director instruction.\", \"ts\": \"2026-05-13T19:32:00.000Z\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:14:43.962197+00:00\"}]}, \"failure_reason\": \"\", \"hypothesis\": \"Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds\", \"metrics\": {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}, \"notes\": \"MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 ✅ (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attempt 3 待定. 输出在全部 attempt 结束后一次性写出 mmlu_paraphrases.json. GSM8K ✅ 1319条(QC 17.3%), ARC ✅ 1172条(QC 59.5%).\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:14:29.355Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"Phase 1 paraphrase: GPU 0 MMLU (PID 204467 v3, vLLM bs=16). GSM8K + ARC completed.\", \"data_count\": \"45 SFT runs + 90 eval runs (original+paraphrased)\", \"data_path\": \"MMLU+GSM8K+ARC-Challenge+HumanEval paraphrases → SFT data mixing\", \"gpu\": \"cuda:0 (MMLU vLLM, still running). cuda:1/2 freed (GSM8K+ARC done).\", \"model_name\": \"Qwen2.5-0.5B/1.5B/3B (LoRA SFT), Qwen2.5-7B-Instruct (paraphrase)\", \"note\": \"GSM8K: 1319 paraphrases (228 QC pass, 17.3%). ARC: 1172 paraphrases (697 QC pass, 59.5%). MMLU: Attempt 1 done (878 batches, 29.3% QC), Attempt 2 in progress (439 batches total, ~22%), Attempt 3 pending. HumanEval: done (appendix per D009).\", \"pid\": \"204467\", \"seed\": \"42,123,456\", \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:21:54.827Z\"}, \"exp_001_sft_0pct_15B_s123\": {\"completed_at\": \"2026-05-13T22:30:26.882Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:35:07.346Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance estimation)\", \"metrics\": {\"token_acc\": 0.731, \"train_loss\": 1.2602, \"train_time_min\": 101.5}, \"notes\": \"OOM 修复后重提交 --gpu 2 (物理 GPU 2)。Worker 确认 PID 216106 训练中 (1/3125 steps, ~2.58s/it)\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123 --seed 123 --gpu 2 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B_s123.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"216111\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:30:26.882Z\"}, \"exp_001_sft_0pct_05B_s123\": {\"completed_at\": \"2026-05-13T22:30:25.819Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:35:04.879Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation)\", \"metrics\": {\"token_acc\": 0.676, \"train_loss\": 1.5393, \"train_time_min\": 54.5}, \"notes\": \"OOM 修复后重提交 --gpu 1 (物理 GPU 1)。Worker 确认 PID 216028 训练中 (2/3125 steps, ~1.87s/it)\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123 --seed 123 --gpu 1 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B_s123.log\", \"model_name\": \"Qwen2.5-0.5B\", \"pid\": \"216033\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:30:25.819Z\"}, \"exp_001_sft_0pct_15B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42\", \"completed_at\": \"2026-05-13T21:27:59.348Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:39:48.369Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T21:25:42.551081+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log\", \"metrics\": {\"adapter_size_mb\": 71, \"checkpoint_size_mb\": 313, \"exit_code\": 0, \"final_loss\": 1.2039, \"mean_train_loss\": 1.2599, \"steps\": \"3125/3125\", \"token_accuracy\": 0.711, \"training_time_min\": 101.5}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:25:40.979Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42 --seed 42 --gpu 4 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:4\"], \"gpu_hours\": 1.78, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log\", \"pid\": \"210116\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:41:11.760Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6407.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T21:27:59.348Z\"}, \"exp_005_noise_prop\": {\"completed_at\": \"2026-05-13T20:47:21.810Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T18:31:00.000Z\", \"failure_reason\": \"Stan numerical bugs: sigma_e=0 allowed (normal_lpdf crash), c/d boundary causing chain crashes, max_treedepth=10 insufficient (14.5% hit rate). All fixed, restarting.\", \"hypothesis\": \"Measurement error in exposure scores propagates through 4PL+γ IRT to widen calibrated score CIs; analytical ME model (conjugate normal integration) produces equivalent CI widths to full latent-τ model at fraction of compute\", \"retry_count\": 0, \"spec\": {\"command\": \"cd artifacts/exp005_noise_propagation && source ../mvp_simulation/.venv/bin/activate && python run_noise_propagation.py\", \"data_count\": \"multiple σ_e values × seeds\", \"data_path\": \"synthetic (generated in-script)\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS)\", \"pid\": 234646, \"seed\": \"0-9\", \"server\": \"local (CPU only)\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T20:47:21.810Z\"}, \"exp_001_sft_0pct_05B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42\", \"completed_at\": \"2026-05-13T20:36:06.744Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:35:01.170Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T20:33:54.496690+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log\", \"metrics\": {\"adapter_size_mb\": 34, \"checkpoint_size_mb\": 166, \"exit_code\": 0, \"final_loss\": 1.4894, \"mean_train_loss\": 1.5388, \"steps\": \"3125/3125\", \"token_accuracy\": 0.682, \"training_time_min\": 52.9}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:33:53.420Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42 --seed 42 --gpu 3 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.98, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log\", \"pid\": \"208933\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:37:23.024Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3523.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T20:37:01.562Z\"}, \"mvp_sim_confounding\": {\"completed_at\": \"2026-05-13T16:28:42.378Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T04:39:19.345Z\", \"hypothesis\": \"4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\", \"metrics\": {\"actual_confound_corr\": 0.3814, \"divergent_pct\": 0, \"fit_time_sec\": 832, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.5386, \"gamma_rel_bias\": 0.0771, \"max_rhat\": 1.007, \"min_ess\": 1371.9, \"overall\": \"PASS\", \"theta_corr\": 0.9733, \"theta_residual_exp_corr\": 0.0582, \"theta_rmse\": 0.2407}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/mvp_simulation/p2_confounding_results.json\", \"command\": \"python run_p2_confounding.py\", \"data_count\": \"50 models x 300 items = 15000 responses\", \"data_path\": \"synthetic confounded (corr≈0.38)\", \"log_path\": \"/tmp/p2_confounding.log\", \"model_name\": \"4PL+γ IRT (Stan NUTS)\", \"note\": \"N_items=300 (matching Variant A PASS config), 4PL NUTS only, 4 chains 1000+1000, θ-exposure corr=0.381\", \"pid\": 202872, \"seed\": 123, \"server\": \"local-cpu\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T16:28:42.378Z\"}, \"mvp_sim_4pl_gamma\": {\"completed_at\": \"2026-05-13T10:59:01.402Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T04:27:47.251Z\", \"hypothesis\": \"4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\", \"metrics\": {\"variant_a_nitems300\": {\"divergent_pct\": 0, \"fit_time_sec\": 1407.5, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.466, \"gamma_rel_bias\": 0.068, \"max_rhat\": 1.003, \"overall\": \"PASS\", \"theta_corr\": 0.943, \"theta_rmse\": 0.238}}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/mvp_simulation/p1_variant_results.json\", \"command\": \"python run_p1_base.py\", \"data_count\": \"50 models x 100 items = 5000 responses\", \"data_path\": \"synthetic (generated in-script)\", \"log_path\": \"/tmp/p1_variants.log\", \"model_name\": \"2PL+γ / 4PL+γ IRT (Stan)\", \"note\": \"Order: 2PL ADVI → 2PL NUTS → 4PL ADVI → 4PL NUTS\", \"pid\": 197929, \"seed\": 42, \"server\": \"local-cpu\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T10:59:01.402Z\"}}, \"count\": 44, \"total\": 44, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9003}}"
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
I got the paper_framing.md and coverage matrix. The registry output was too large and saved to a file. Let me parse the registry data to understand experiment statuses.

Let me analyze what I have so far:

**Coverage Matrix Summary:**
- Claim 1 (Calibration): 7 experiments, 0 done, 2 running, 4 planned, 1 orphaned, 0% coverage
- Claim 2 (Signal Survival & Aggregation): 5 experiments, 0 done, 0 running, 5 planned, 0% coverage


- Claim 3 (Identifiability & Uncertainty): 1 experiment, 0 done, 1 failed, 0% coverage

Across all 13 experiments, nothing's completed yet—only 2 are running, 9 are planned, 1 failed, and 1 orphaned. With the submission deadline just 11 days away, I need to dig into the registry to see what's actually happening with those running experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "e395a53e-2bff-4423-8689-d40d9223ee04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmEjuyvF77hFfSTfH5Bo2o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8693,
      "cache_read_input_tokens": 24272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8693
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

Registry 输出过大，用 agent 解析关键状态信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "7e197091-fca9-400e-91b4-e1f9f1c72854",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmEjuyvF77hFfSTfH5Bo2o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8693,
      "cache_read_input_tokens": 24272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8693
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

<details open><summary>🔧 Tool call — Agent · `toolu_01DAocpnKSJLdbXsJd7evPbS`</summary>

```json
{
  "description": "Parse registry JSON data",
  "prompt": "Read the file /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt\n\nThis is JSON with schema: {result: string} where the inner result is also a JSON string.\n\nExtract and report for EVERY experiment entry:\n1. experiment id / registry_id\n2. status (RUNNING/DONE/FAILED/PLANNED etc.)\n3. conclusion (if any)\n4. created_at / updated_at timestamps\n5. Any metrics or key findings mentioned\n6. Which claim it supports\n7. Any error messages or failure reasons\n\nBe thorough - list every single experiment. Format as a structured table.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "1f4edb25-7612-492c-9fbf-09f553445fa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmEjuyvF77hFfSTfH5Bo2o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8693,
      "cache_read_input_tokens": 24272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8693
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

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Parse registry JSON data",
  "task_type": "local_agent",
  "prompt": "Read the file /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt\n\nThis is JSON with schema: {result: string} where the inner result is also a JSON string.\n\nExtract and report for EVERY experiment entry:\n1. experiment id / registry_id\n2. status (RUNNING/DONE/FAILED/PLANNED etc.)\n3. conclusion (if any)\n4. created_at / updated_at timestamps\n5. Any metrics or key findings mentioned\n6. Which claim it supports\n7. Any error messages or failure reasons\n\nBe thorough - list every single experiment. Format as a structured table.",
  "uuid": "3208df01-87f7-4736-8ea8-0afa5bf51f9a",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

## Round 1

45 recorded events

### User

_source line 20 · 2026-05-14T04:17:00.967Z_

Read the file /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt

This is JSON with schema: {result: string} where the inner result is also a JSON string.

Extract and report for EVERY experiment entry:
1. experiment id / registry_id
2. status (RUNNING/DONE/FAILED/PLANNED etc.)
3. conclusion (if any)
4. created_at / updated_at timestamps
5. Any metrics or key findings mentioned
6. Which claim it supports
7. Any error messages or failure reasons

Be thorough - list every single experiment. Format as a structured table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "bc784c06-cee1-498c-952d-ee3ae54f9817"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt",
  "usage": {
    "total_tokens": 14209,
    "tool_uses": 1,
    "duration_ms": 4480
  },
  "last_tool_name": "Read",
  "uuid": "a893a0c9-f6af-4d3f-a2db-6991fa41f9f1",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01RuhFJFcSaDfratPsdVrorV`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "616675e8-3e21-43c4-b803-51b5ebd2eb48",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PA1BE93UmGVDuL8KUtvazM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14200,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14200,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 23 · 2026-05-14T04:17:05.811Z_

<details><summary>↩ Tool result · reported error · `toolu_01RuhFJFcSaDfratPsdVrorV`</summary>

```text
File content (30431 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "a804d2e2-fb07-4c02-86c5-4ab455f66334",
  "tool_use_result": "Error: File content (30431 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt",
  "usage": {
    "total_tokens": 15267,
    "tool_uses": 2,
    "duration_ms": 8236
  },
  "last_tool_name": "Read",
  "uuid": "33cea4ed-c459-4379-8ddb-4a2d75097653",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01PTEko2MAsX1qyTreGuKrGQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "bda72363-c7b2-40e1-8600-6514f6470c0f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YPyTprn2c8KiXuWaJeViYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 14200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1058,
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

_source line 26 · 2026-05-14T04:17:09.533Z_

<details><summary>↩ Tool result · reported error · `toolu_01PTEko2MAsX1qyTreGuKrGQ`</summary>

```text
File content (30431 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "6d0434f3-3f6a-4898-824e-99212254dd25",
  "tool_use_result": "Error: File content (30431 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt",
  "usage": {
    "total_tokens": 15566,
    "tool_uses": 3,
    "duration_ms": 11741
  },
  "last_tool_name": "Read",
  "uuid": "00ab9959-fc7e-4025-b040-f605e5fe9207",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_019Bxbzg2FB6GJQiE1gYVFBi`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt",
  "limit": 300,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "98d8a66d-52dc-47eb-9284-68a74ca0e1e6",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MAMNM5KDaWwtRX5BNJvfky",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 15258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 236,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 29 · 2026-05-14T04:17:13.007Z_

<details><summary>↩ Tool result · reported error · `toolu_019Bxbzg2FB6GJQiE1gYVFBi`</summary>

```text
File content (30431 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "681fd510-ee26-41b6-9239-0242e09641c3",
  "tool_use_result": "Error: File content (30431 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Searching for \"registry_id\"|\"status\"|\"conclusion\"|\"created_at\"|…",
  "usage": {
    "total_tokens": 15808,
    "tool_uses": 4,
    "duration_ms": 16944
  },
  "last_tool_name": "Grep",
  "uuid": "fa36176c-afa9-4d14-8bb0-afe35bd62718",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_016c8qJE9gL46whoEeGkif9o`</summary>

```json
{
  "pattern": "\"registry_id\"|\"status\"|\"conclusion\"|\"created_at\"|\"updated_at\"|\"claim\"|\"error\"|\"metrics\"|\"findings\"",
  "path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt",
  "output_mode": "content",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "c19580da-418c-4657-8413-fa82776f79a5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CGiP7WTShyWGQjR1RQ6w1n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 15494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 240,
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

_source line 32 · 2026-05-14T04:17:18.029Z_

<details><summary>↩ Tool result · `toolu_016c8qJE9gL46whoEeGkif9o`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "6419e94f-f754-47b4-9b2c-e122fc3195e5"
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
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Running Check file size and type",
  "usage": {
    "total_tokens": 16132,
    "tool_uses": 5,
    "duration_ms": 20512
  },
  "last_tool_name": "Bash",
  "uuid": "fec9a93d-ba30-4fc3-8f6a-df209ef575fc",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_013VStALRPmD9syN5fPzWo2n`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt && file /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt",
  "description": "Check file size and type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "9f5bedaf-19c5-4a8c-87b0-2b7e7fe69208",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01A2S1CQAMJkmKHYBP2BndyD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 15734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 270,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 35 · 2026-05-14T04:17:22.476Z_

<details><summary>↩ Tool result · `toolu_013VStALRPmD9syN5fPzWo2n`</summary>

```text
70768 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt
/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt: JSON text data
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "37b9d981-fad0-4897-9dd3-9e8e45a9a1ea"
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
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Running Parse JSON structure of the registry file",
  "usage": {
    "total_tokens": 16655,
    "tool_uses": 6,
    "duration_ms": 26500
  },
  "last_tool_name": "Bash",
  "uuid": "d3af4236-2792-42b8-84cd-6f4ad7340d76",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01LZ92Gfqd5EN6n8Gp9xqUpX`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt', 'r') as f:\n    outer = json.load(f)\n\n# The outer schema is {result: string} where result is also JSON\nresult_str = outer['result']\ndata = json.loads(result_str)\nprint(type(data))\nif isinstance(data, dict):\n    print('Keys:', list(data.keys())[:20])\nelif isinstance(data, list):\n    print('List length:', len(data))\n    if data:\n        print('First item keys:', list(data[0].keys()) if isinstance(data[0], dict) else type(data[0]))\n\"\n",
  "description": "Parse JSON structure of the registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "7f236ea2-80a9-4249-9c8e-c4ad741f5651",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GRHEdtjuKuZ3JtdEGSjuyj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 16004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 470,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
      "service_tier": "standard",
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

_source line 38 · 2026-05-14T04:17:27.901Z_

<details><summary>↩ Tool result · `toolu_01LZ92Gfqd5EN6n8Gp9xqUpX`</summary>

```text
&lt;class 'dict'>
Keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "91539a4f-1310-474e-8231-5405dbb72e85"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Running Inspect top-level registry data structure",
  "usage": {
    "total_tokens": 17075,
    "tool_uses": 7,
    "duration_ms": 32793
  },
  "last_tool_name": "Bash",
  "uuid": "89b5c2a3-6581-490b-9409-2119a91f8922",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01BQ47e4QgATBM3o8m54UdjE`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt', 'r') as f:\n    outer = json.load(f)\n\nresult_str = outer['result']\ndata = json.loads(result_str)\n\nprint('success:', data.get('success'))\nprint('error:', data.get('error'))\nprint('metadata:', data.get('metadata'))\ninner = data.get('data')\nprint('data type:', type(inner))\nif isinstance(inner, dict):\n    print('data keys:', list(inner.keys())[:20])\nelif isinstance(inner, list):\n    print('data length:', len(inner))\n\"\n",
  "description": "Inspect top-level registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "53419dbb-a7f4-4f2f-8da6-20bd59064005",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013c3h3tLGDWYcFvow3hWiQE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 357,
      "cache_read_input_tokens": 16474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 357,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 41 · 2026-05-14T04:17:34.259Z_

<details><summary>↩ Tool result · `toolu_01BQ47e4QgATBM3o8m54UdjE`</summary>

```text
success: True
error: None
metadata: {'elapsed_seconds': 0.9003}
data type: &lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "4dc64f2a-cda4-43ea-ad6f-5b3040d4c4fb"
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
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Running Check experiment count and structure",
  "usage": {
    "total_tokens": 17620,
    "tool_uses": 8,
    "duration_ms": 37500
  },
  "last_tool_name": "Bash",
  "uuid": "d19964d8-9f93-495e-873b-496a226d6e0c",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01PRGYvtak3KYbnkjVGgXMgS`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt', 'r') as f:\n    outer = json.load(f)\n\nresult_str = outer['result']\ndata = json.loads(result_str)\ninner = data['data']\n\nprint('count:', inner.get('count'))\nprint('total:', inner.get('total'))\n\nexps = inner.get('experiments', [])\nprint('Number of experiments:', len(exps))\n\nif exps:\n    print('First experiment keys:', list(exps[0].keys()))\n\"\n",
  "description": "Check experiment count and structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "2d30b652-095a-4e91-a279-2ce45cab7ba9",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PuYPUeoRLEZkvG3rQW3f3y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 16831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 481,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

_source line 44 · 2026-05-14T04:17:39.798Z_

<details><summary>↩ Tool result · reported error · `toolu_01PRGYvtak3KYbnkjVGgXMgS`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 18, in &lt;module>
    print('First experiment keys:', list(exps[0].keys()))
                                         ~~~~^^^
KeyError: 0
count: 44
total: 44
Number of experiments: 44
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "8314805b-a513-4cd3-8607-409b197563ae",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 18, in &lt;module>\n    print('First experiment keys:', list(exps[0].keys()))\n                                         ~~~~^^^\nKeyError: 0\ncount: 44\ntotal: 44\nNumber of experiments: 44"
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
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Running Check experiments dict structure",
  "usage": {
    "total_tokens": 18072,
    "tool_uses": 9,
    "duration_ms": 42525
  },
  "last_tool_name": "Bash",
  "uuid": "c63ee1c5-1a36-445b-895d-04ce4da0a87e",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_017j1yjDFhpUScaskcFXBL1d`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt', 'r') as f:\n    outer = json.load(f)\n\nresult_str = outer['result']\ndata = json.loads(result_str)\ninner = data['data']\nexps = inner.get('experiments', {})\n\nprint('experiments type:', type(exps))\nif isinstance(exps, dict):\n    keys = list(exps.keys())\n    print('Keys (first 5):', keys[:5])\n    first_key = keys[0]\n    print('First experiment keys:', list(exps[first_key].keys()))\n\"\n",
  "description": "Check experiments dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "224a3545-7790-4dc7-82a4-89539a03cb06",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Xtw2SY2cHDEdfWZURWx3yG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 17312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 389,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 47 · 2026-05-14T04:17:43.948Z_

<details><summary>↩ Tool result · `toolu_017j1yjDFhpUScaskcFXBL1d`</summary>

```text
experiments type: &lt;class 'dict'>
Keys (first 5): ['exp_004_sim_sweep', 'exp_005_noise_prop_v3', 'exp_005_noise_prop_v2', 'exp_001_sft_d005_15B', 'exp_001_eval_15B_d000_s42_v2']
First experiment keys: ['completed_at', 'conclusion', 'created_at', 'extra', 'failure_reason', 'hypothesis', 'retry_count', 'spec', 'status', 'updated_at']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "2f8e71ac-6619-41e2-a959-1ff407dea9c9"
}
```

</details>

---

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Running Extract all experiment details from registry",
  "usage": {
    "total_tokens": 18598,
    "tool_uses": 10,
    "duration_ms": 51022
  },
  "last_tool_name": "Bash",
  "uuid": "e4d22bf6-f9a9-4198-b1d0-782514bb7127",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01Hea6ahTNyj6rUqi2yn71Ht`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt', 'r') as f:\n    outer = json.load(f)\n\nresult_str = outer['result']\ndata = json.loads(result_str)\ninner = data['data']\nexps = inner.get('experiments', {})\n\nfor exp_id, exp in sorted(exps.items()):\n    status = exp.get('status', 'N/A')\n    created_at = exp.get('created_at', 'N/A')\n    updated_at = exp.get('updated_at', 'N/A')\n    completed_at = exp.get('completed_at', 'N/A')\n    conclusion = exp.get('conclusion', None)\n    failure_reason = exp.get('failure_reason', None)\n    hypothesis = exp.get('hypothesis', None)\n    retry_count = exp.get('retry_count', 0)\n    spec = exp.get('spec', {}) or {}\n    extra = exp.get('extra', {}) or {}\n    \n    # Extract claim from spec\n    claim = spec.get('claim', spec.get('claims', spec.get('claim_id', None)))\n    # Extract metrics from extra or spec\n    metrics = extra.get('metrics', extra.get('results', None))\n    \n    print(f'=== {exp_id} ===')\n    print(f'  Status: {status}')\n    print(f'  Created: {created_at}')\n    print(f'  Updated: {updated_at}')\n    print(f'  Completed: {completed_at}')\n    print(f'  Retry count: {retry_count}')\n    print(f'  Claim: {claim}')\n    print(f'  Hypothesis: {str(hypothesis)[:200] if hypothesis else None}')\n    print(f'  Conclusion: {str(conclusion)[:300] if conclusion else None}')\n    print(f'  Failure reason: {str(failure_reason)[:200] if failure_reason else None}')\n    print(f'  Metrics: {str(metrics)[:200] if metrics else None}')\n    print(f'  Spec keys: {list(spec.keys())}')\n    print(f'  Extra keys: {list(extra.keys())}')\n    print()\n\" 2>&1\n",
  "description": "Extract all experiment details from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "0fb31718-f3f3-4997-90b8-ab4fcbfe78ef",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G8MkxHCQ3oAMswveSFnRzf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 17701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 463,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 50 · 2026-05-14T04:17:52.423Z_

<details><summary>↩ Tool result · `toolu_01Hea6ahTNyj6rUqi2yn71Ht`</summary>

```text
=== exp_001_eval_05B_d000_s123 ===
  Status: DONE
  Created: 2026-05-13T22:30:40.455Z
  Updated: 2026-05-14T01:29:09.875Z
  Completed: 2026-05-14T01:29:09.875Z
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'gpu_hours', 'gpu_ids', 'log_path', 'model_name', 'parent', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds']
  Extra keys: ['hook_events']

=== exp_001_eval_05B_d000_s42 ===
  Status: DONE
  Created: 2026-05-13T22:42:34.313Z
  Updated: 2026-05-14T01:33:03.857Z
  Completed: 2026-05-14T01:29:11.220Z
  Retry count: 0
  Claim: None
  Hypothesis: 0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation
  Conclusion: failed
  Failure reason: Traceback → ration/exp001/evaluate.py", line 558, in main all_results["benchmarks"][benchmark] = result ^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: '/root/autodl-tm
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'gpu_hours', 'gpu_ids', 'log_path', 'model_name', 'output_dir', 'parent', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds']
  Extra keys: ['hook_events']

=== exp_001_eval_05B_d000_s42_v2 ===
  Status: PREPARING
  Created: 2026-05-14T02:26:38.504Z
  Updated: 2026-05-14T02:36:51.089Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: failed
  Failure reason: EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via']
  Extra keys: ['hook_events']

=== exp_001_eval_05B_d000_s42_v3 ===
  Status: PREPARING
  Created: 2026-05-14T02:30:50.700Z
  Updated: 2026-05-14T02:33:51.502Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算
  Conclusion: killed
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_eval_05B_d000_s42_v4 ===
  Status: PREPARING
  Created: 2026-05-14T02:35:30.672Z
  Updated: 2026-05-14T02:40:09.432Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)
  Conclusion: killed
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_eval_05B_d000_s42_v5 ===
  Status: RUNNING
  Created: 2026-05-14T02:39:41.292Z
  Updated: 2026-05-14T02:46:54.180Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)
  Conclusion: None
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_path', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'log_path', 'model_name', 'parent', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_eval_05B_d000_s42_v6 ===
  Status: PREPARING
  Created: 2026-05-14T02:40:46.586Z
  Updated: 2026-05-14T02:47:17.653Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)
  Conclusion: killed
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_eval_05B_d005 ===
  Status: RUNNING
  Created: 2026-05-14T01:17:07.820Z
  Updated: 2026-05-14T02:15:00.000Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: None
  Failure reason: None
  Metrics: None
  Spec keys: ['checkpoint_path', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'hypothesis', 'log_path', 'model_name', 'parent', 'pid', 'seed', 'server']
  Extra keys: []

=== exp_001_eval_05B_d100 ===
  Status: DONE
  Created: 2026-05-14T01:15:49.903Z
  Updated: 2026-05-14T02:21:35.372Z
  Completed: 2026-05-14T02:21:35.372Z
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: failed
  Failure reason: EXIT_CODE=143 (SIGTERM — graceful kill)
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_path', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'gpu_hours', 'gpu_ids', 'hypothesis', 'log_path', 'model_name', 'parent', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds']
  Extra keys: ['hook_events']

=== exp_001_eval_05B_d100_v2 ===
  Status: PENDING
  Created: 2026-05-14T02:26:41.093Z
  Updated: 2026-05-14T02:39:52.993Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: failed
  Failure reason: EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via']
  Extra keys: ['hook_events']

=== exp_001_eval_05B_d100_v3 ===
  Status: PREPARING
  Created: 2026-05-14T02:30:53.668Z
  Updated: 2026-05-14T02:33:52.158Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation
  Conclusion: killed
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_eval_05B_d100_v4 ===
  Status: PREPARING
  Created: 2026-05-14T02:36:09.066Z
  Updated: 2026-05-14T02:40:10.093Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)
  Conclusion: killed
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_eval_05B_d100_v5 ===
  Status: RUNNING
  Created: 2026-05-14T02:39:57.338Z
  Updated: 2026-05-14T02:46:56.726Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)
  Conclusion: None
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_path', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'log_path', 'model_name', 'parent', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_eval_05B_d100_v6 ===
  Status: PREPARING
  Created: 2026-05-14T02:40:56.017Z
  Updated: 2026-05-14T02:47:16.586Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)
  Conclusion: killed
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_eval_15B_d000_s123 ===
  Status: RUNNING
  Created: 2026-05-13T22:30:41.501Z
  Updated: 2026-05-14T01:18:06.102Z
  Completed: 2026-05-13T23:39:26.418Z
  Retry count: 1
  Claim: None
  Hypothesis: None
  Conclusion: None
  Failure reason: EXIT_CODE=2: --gpu 0 参数导致 evaluate.py 崩溃。重跑时需去掉 --gpu 参数。
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_path', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'log_path', 'model_name', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via']
  Extra keys: ['previous_failure']

=== exp_001_eval_15B_d000_s42 ===
  Status: DONE
  Created: 2026-05-13T21:30:03.433Z
  Updated: 2026-05-14T00:23:17.209Z
  Completed: 2026-05-14T00:23:17.209Z
  Retry count: 0
  Claim: None
  Hypothesis: 0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation
  Conclusion: failed
  Failure reason: 卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。
  Metrics: None
  Spec keys: ['checkpoint_path', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'log_path', 'model_name', 'output_dir', 'pid', 'seed', 'server']
  Extra keys: []

=== exp_001_eval_15B_d000_s42_v2 ===
  Status: DONE
  Created: 2026-05-14T00:23:20.112Z
  Updated: 2026-05-14T03:12:11.373Z
  Completed: 2026-05-14T03:12:11.373Z
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'gpu_hours', 'log_path', 'model_name', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds']
  Extra keys: ['hook_events']

=== exp_001_eval_3B_d000_s123 ===
  Status: RUNNING
  Created: 2026-05-14T00:18:07.960Z
  Updated: 2026-05-14T00:33:31.970Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: None
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'log_path', 'model_name', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_eval_3B_d000_s42 ===
  Status: RUNNING
  Created: 2026-05-13T23:36:54.086Z
  Updated: 2026-05-14T00:55:02.251Z
  Completed: 2026-05-13T23:43:16.876Z
  Retry count: 1
  Claim: None
  Hypothesis: 0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) to establish ground-truth scores for calibration error computation
  Conclusion: None
  Failure reason: --gpu 参数导致 evaluate.py 崩溃（与 exp_001_eval_15B_d000_s123 同一 bug）。需去掉 --gpu 参数，用 CUDA_VISIBLE_DEVICES 控制 GPU 分配后重跑。
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'log_path', 'model_name', 'pid', 'seed', 'server', 'submitted_at']
  Extra keys: ['previous_failure']

=== exp_001_eval_3B_d000_s42_v2 ===
  Status: PREPARING
  Created: 2026-05-13T23:51:39.462Z
  Updated: 2026-05-14T00:12:13.851Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: failed
  Failure reason: killed by d005 worker reclaiming GPU 5 (SIGKILL, EXIT_CODE=137)
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'hypothesis', 'log_path', 'model_name', 'parent', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_eval_3B_d000_s42_v3 ===
  Status: PREPARING
  Created: 2026-05-14T00:48:57.772Z
  Updated: 2026-05-14T03:06:54.726Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。
  Conclusion: killed
  Failure reason: None
  Metrics: None
  Spec keys: []
  Extra keys: []

=== exp_001_sft_0pct ===
  Status: DONE
  Created: 2026-05-13T19:26:42.106Z
  Updated: 2026-05-14T00:36:52.832Z
  Completed: 2026-05-14T00:36:52.832Z
  Retry count: 0
  Claim: None
  Hypothesis: 0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores for calibration error computation; LoRA r=16 alpha=32 1-epoch training on pure instruction data should p
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: []
  Extra keys: []

=== exp_001_sft_0pct_05B ===
  Status: DONE
  Created: 2026-05-13T19:35:01.170Z
  Updated: 2026-05-13T20:37:01.562Z
  Completed: 2026-05-13T20:36:06.744Z
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'gpu_hours', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds']
  Extra keys: ['hook_events']

=== exp_001_sft_0pct_05B_s123 ===
  Status: DONE
  Created: 2026-05-13T20:35:04.879Z
  Updated: 2026-05-13T22:30:25.819Z
  Completed: 2026-05-13T22:30:25.819Z
  Retry count: 0
  Claim: None
  Hypothesis: 0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation)
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['checkpoint_path', 'command', 'data_count', 'data_path', 'gpu', 'log_path', 'model_name', 'pid', 'seed', 'server']
  Extra keys: []

=== exp_001_sft_0pct_15B ===
  Status: DONE
  Created: 2026-05-13T19:39:48.369Z
  Updated: 2026-05-13T21:27:59.348Z
  Completed: 2026-05-13T21:27:59.348Z
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'gpu_hours', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds']
  Extra keys: ['hook_events']

=== exp_001_sft_0pct_15B_s123 ===
  Status: DONE
  Created: 2026-05-13T20:35:07.346Z
  Updated: 2026-05-13T22:30:26.882Z
  Completed: 2026-05-13T22:30:26.882Z
  Retry count: 0
  Claim: None
  Hypothesis: 0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance estimation)
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['checkpoint_path', 'command', 'data_count', 'data_path', 'gpu', 'log_path', 'model_name', 'pid', 'seed', 'server']
  Extra keys: []

=== exp_001_sft_0pct_3B ===
  Status: DONE
  Created: 2026-05-13T19:44:40.471Z
  Updated: 2026-05-13T23:25:49.016Z
  Completed: 2026-05-13T23:25:49.016Z
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'gpu_hours', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds']
  Extra keys: ['hook_events']

=== exp_001_sft_0pct_3B_s123 ===
  Status: DONE
  Created: 2026-05-13T20:39:01.606Z
  Updated: 2026-05-14T00:23:18.290Z
  Completed: 2026-05-14T00:23:18.290Z
  Retry count: 0
  Claim: None
  Hypothesis: 0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance estimation)
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['command', 'data_count', 'data_path', 'gpu', 'log_path', 'model_name', 'pid', 'seed', 'server']
  Extra keys: ['hook_events']

=== exp_001_sft_100pct_05B ===
  Status: DONE
  Created: 2026-05-13T23:41:15.631Z
  Updated: 2026-05-13T23:49:12.007Z
  Completed: 2026-05-13T23:49:10.741Z
  Retry count: 0
  Claim: None
  Hypothesis: 100% contamination dosage on 0.5B establishes upper bound of score inflation; comparing with 0% baseline reveals maximum contamination effect across MMLU/GSM8K/ARC benchmarks
  Conclusion: failed
  Failure reason: Duplicate registry entry — actual training tracked by exp_001_sft_d100_05B (PID 235243, cron monitored)
  Metrics: None
  Spec keys: ['checkpoint_path', 'command', 'data_count', 'data_path', 'model_name', 'seed', 'server']
  Extra keys: []

=== exp_001_sft_d005_05B ===
  Status: DONE
  Created: 2026-05-13T23:36:15.352Z
  Updated: 2026-05-13T23:59:30.512Z
  Completed: 2026-05-13T23:42:35.135Z
  Retry count: 0
  Claim: None
  Hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): minimum contamination level to detect dose-response threshold; paired with d100 for min-max comparison
  Conclusion: killed
  Failure reason: CUDA OOM at step 8/3177 — zombie 3B eval process (PID 234755) 占 6.8GB GPU 5 显存，导致 SFT 训练分配失败。已重试为 exp_001_sft_d005_05B_v2。
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via']
  Extra keys: ['hook_events']

=== exp_001_sft_d005_05B_r3 ===
  Status: PREPARING
  Created: 2026-05-13T23:58:49.282Z
  Updated: 2026-05-14T00:12:15.733Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (v1: GPU 5 zombie process; v2: --gpu 0 bug ran on GPU 0 instead of 5). Now uses --gpu 5 correctly.
  Conclusion: killed
  Failure reason: OOM — v3 (PID 239734) 已占用 GPU 5 全部显存，r3 是重复提交，启动即崩溃。v3 正常运行中，r3 废弃。
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_sft_d005_05B_v2 ===
  Status: DONE
  Created: 2026-05-13T23:48:24.508Z
  Updated: 2026-05-13T23:59:33.029Z
  Completed: 2026-05-13T23:49:48.629Z
  Retry count: 0
  Claim: None
  Hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry after v1 OOM crash (GPU 5 conflict with zombie eval process). GPU 5 now clear.
  Conclusion: failed
  Failure reason: CUDA OOM: CUDA out of memory. Tried to allocate 578.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 459.38 MiB is free. Process 235248 has 21.47 GiB memory in use. Including non-PyTorch memor
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'gpu_hours', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds']
  Extra keys: ['hook_events']

=== exp_001_sft_d005_05B_v3 ===
  Status: DONE
  Created: 2026-05-13T23:52:39.321Z
  Updated: 2026-05-14T00:58:15.977Z
  Completed: 2026-05-14T00:58:15.977Z
  Retry count: 0
  Claim: None
  Hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'gpu_hours', 'log_path', 'model_name', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds']
  Extra keys: ['hook_events']

=== exp_001_sft_d005_15B ===
  Status: RUNNING
  Created: 2026-05-14T00:19:54.331Z
  Updated: 2026-05-14T03:17:38.946Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: 5% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): low-dosage contamination for dose-response curve, Phase 3 priority 1
  Conclusion: None
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'checkpoint_path', 'command', 'data_count', 'data_path', 'gpu', 'log_path', 'model_name', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via']
  Extra keys: []

=== exp_001_sft_d100_05B ===
  Status: DONE
  Created: 2026-05-13T23:36:13.403Z
  Updated: 2026-05-14T00:55:14.218Z
  Completed: 2026-05-14T00:53:49.656Z
  Retry count: 0
  Claim: None
  Hypothesis: 100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['account', 'backend', 'command', 'gpu', 'gpu_hours', 'log_path', 'pid', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds']
  Extra keys: ['hook_events']

=== exp_001_sft_d100_15B ===
  Status: DONE
  Created: 2026-05-13T23:37:43.653Z
  Updated: 2026-05-14T01:23:40.711Z
  Completed: 2026-05-14T01:23:40.712Z
  Retry count: 0
  Claim: None
  Hypothesis: 100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration er
  Conclusion: failed
  Failure reason: OOM batch_size=2, replaced by v2
  Metrics: None
  Spec keys: ['command', 'data_count', 'data_path', 'gpu', 'log_path', 'model_name', 'pid', 'seed', 'server']
  Extra keys: []

=== exp_001_sft_d100_15B_v2 ===
  Status: RUNNING
  Created: 2026-05-14T01:17:47.114Z
  Updated: 2026-05-14T01:18:26.304Z
  Completed: N/A
  Retry count: 0
  Claim: None
  Hypothesis: None
  Conclusion: None
  Failure reason: None
  Metrics: None
  Spec keys: ['checkpoint_path', 'command', 'data_count', 'data_path', 'gpu', 'hypothesis', 'log_path', 'model_name', 'pid', 'seed', 'server']
  Extra keys: []

=== exp_001_sft_injection ===
  Status: DONE
  Created: 2026-05-13T17:28:01.546Z
  Updated: 2026-05-13T23:21:54.827Z
  Completed: 2026-05-13T23:14:30.258Z
  Retry count: 0
  Claim: None
  Hypothesis: Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper un
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['command', 'data_count', 'data_path', 'gpu', 'model_name', 'note', 'pid', 'seed', 'server']
  Extra keys: ['hook_events']

=== exp_004_sim_sweep ===
  Status: RUNNING
  Created: 2026-05-13T16:43:57.478Z
  Updated: 2026-05-14T03:44:17.318015+00:00
  Completed: 2026-05-14T03:41:12.265Z
  Retry count: 0
  Claim: None
  Hypothesis: 4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which γ 95% CI width exceeds 15pp; recovery improves with N_models; prio
  Conclusion: None
  Failure reason: SSH check failed 5x — last error: Unknown server 'local'. Available: ['cqa1-21977']
  Metrics: None
  Spec keys: ['log_path', 'pid', 'timeout_per_fit']
  Extra keys: ['hook_events']

=== exp_005_noise_prop ===
  Status: DONE
  Created: 2026-05-13T18:31:00.000Z
  Updated: 2026-05-13T20:47:21.810Z
  Completed: 2026-05-13T20:47:21.810Z
  Retry count: 0
  Claim: None
  Hypothesis: Measurement error in exposure scores propagates through 4PL+γ IRT to widen calibrated score CIs; analytical ME model (conjugate normal integration) produces equivalent CI widths to full latent-τ model
  Conclusion: failed
  Failure reason: Stan numerical bugs: sigma_e=0 allowed (normal_lpdf crash), c/d boundary causing chain crashes, max_treedepth=10 insufficient (14.5% hit rate). All fixed, restarting.
  Metrics: None
  Spec keys: ['command', 'data_count', 'data_path', 'model_name', 'pid', 'seed', 'server']
  Extra keys: []

=== exp_005_noise_prop_v2 ===
  Status: DONE
  Created: 2026-05-13T20:47:35.807Z
  Updated: 2026-05-14T03:25:33.715Z
  Completed: 2026-05-13T22:44:09.262Z
  Retry count: 0
  Claim: None
  Hypothesis: Same as exp_005: ME model CI width increases monotonically with σ_e; simple model does not. v2 fixes: sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12.
  Conclusion: failed
  Failure reason: 根因：/tmp tmpfs 磁盘配额耗尽。ME model 先跑 95min 生成 ~1GB CSV（9000 tau + 9000 log_lik × 4 chains）耗尽 3.9GB tmpfs。Simple model 写 CSV 时 disk quota exceeded → 4 chains 全部 retcode=1。ME model Rhat=1.945 是独立问题：10231 参数
  Metrics: None
  Spec keys: ['command', 'data_count', 'data_path', 'fixes', 'log_path', 'model_name', 'pid', 'seed', 'server']
  Extra keys: ['hook_events']

=== exp_005_noise_prop_v3 ===
  Status: RUNNING
  Created: 2026-05-14T03:24:06.949Z
  Updated: 2026-05-14T03:36:19.610665Z
  Completed: 2026-05-14T03:29:53.328Z
  Retry count: 0
  Claim: None
  Hypothesis: Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic M
  Conclusion: None
  Failure reason: None
  Metrics: None
  Spec keys: ['checkpoint_path', 'command', 'data_count', 'data_path', 'log_path', 'model_name', 'note', 'pid', 'seed', 'server']
  Extra keys: []

=== mvp_sim_4pl_gamma ===
  Status: DONE
  Created: 2026-05-13T04:27:47.251Z
  Updated: 2026-05-13T10:59:01.402Z
  Completed: 2026-05-13T10:59:01.402Z
  Retry count: 0
  Claim: None
  Hypothesis: 4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['checkpoint_path', 'command', 'data_count', 'data_path', 'log_path', 'model_name', 'note', 'pid', 'seed', 'server']
  Extra keys: []

=== mvp_sim_confounding ===
  Status: DONE
  Created: 2026-05-13T04:39:19.345Z
  Updated: 2026-05-13T16:28:42.378Z
  Completed: 2026-05-13T16:28:42.378Z
  Retry count: 0
  Claim: None
  Hypothesis: 4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure
  Conclusion: success
  Failure reason: None
  Metrics: None
  Spec keys: ['checkpoint_path', 'command', 'data_count', 'data_path', 'log_path', 'model_name', 'note', 'pid', 'seed', 'server']
  Extra keys: []
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "10521144-2102-4297-b2d9-3ce5c5b65193"
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
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Running Extract baseline info and any metrics/results from spec/extra fields",
  "usage": {
    "total_tokens": 29802,
    "tool_uses": 11,
    "duration_ms": 64722
  },
  "last_tool_name": "Bash",
  "uuid": "b016db3c-72c1-48f1-b4ba-fa0a7fb0a7df",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01RaQC5kzSwt8TjcFEnCB5kE`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt', 'r') as f:\n    outer = json.load(f)\n\nresult_str = outer['result']\ndata = json.loads(result_str)\ninner = data['data']\n\nbaseline = inner.get('baseline')\nprint('baseline:', json.dumps(baseline, indent=2)[:2000] if baseline else None)\n\n# Check for any metrics/results in spec or extra fields\nexps = inner.get('experiments', {})\nprint()\nprint('=== Checking for metrics/results in spec/extra ===')\nfor exp_id, exp in sorted(exps.items()):\n    spec = exp.get('spec', {}) or {}\n    extra = exp.get('extra', {}) or {}\n    \n    # Look for any results-like keys\n    for key in ['results', 'metrics', 'scores', 'ece', 'irt', 'benchmarks', 'findings', 'auc', 'gamma', 'theta']:\n        if key in spec:\n            print(f'{exp_id} spec[{key}]:', str(spec[key])[:300])\n        if key in extra:\n            print(f'{exp_id} extra[{key}]:', str(extra[key])[:300])\n    \n    # Also check all spec values for interesting data\n    for k, v in spec.items():\n        if isinstance(v, dict) and k not in ['command']:\n            print(f'{exp_id} spec[{k}]:', str(v)[:200])\n\"\n",
  "description": "Extract baseline info and any metrics/results from spec/extra fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "e2dfd52a-f931-48ab-9df3-e95769f465c5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01B3SvdXfxCzgkHi6rchJUtK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11202,
      "cache_read_input_tokens": 18164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11202,
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

_source line 53 · 2026-05-14T04:18:06.303Z_

<details><summary>↩ Tool result · `toolu_01RaQC5kzSwt8TjcFEnCB5kE`</summary>

```text
baseline: None

=== Checking for metrics/results in spec/extra ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "8ef38783-469f-49a6-b0ef-a1425a42ffd7"
}
```

</details>

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Running Dump full JSON for key successful experiments to find metrics",
  "usage": {
    "total_tokens": 30460,
    "tool_uses": 12,
    "duration_ms": 71004
  },
  "last_tool_name": "Bash",
  "uuid": "d07f5ea8-ad9c-4116-94e5-4d031b7a1e98",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01QfrzThYjARhJir3dXWZZt5`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt', 'r') as f:\n    outer = json.load(f)\n\nresult_str = outer['result']\ndata = json.loads(result_str)\ninner = data['data']\nexps = inner.get('experiments', {})\n\n# Check full exp structure for two experiments (MVP ones with success) for any hidden fields\nfor exp_id in ['mvp_sim_4pl_gamma', 'mvp_sim_confounding', 'exp_001_sft_injection', 'exp_004_sim_sweep']:\n    if exp_id in exps:\n        print(f'=== {exp_id} FULL ===')\n        print(json.dumps(exps[exp_id], indent=2)[:1500])\n        print()\n\"\n",
  "description": "Dump full JSON for key successful experiments to find metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "42f53c6d-26de-42ed-bdd9-32f0d5c0f774",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018jjN5cwMhp5sJAGyse4Nvq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 594,
      "cache_read_input_tokens": 29366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 594,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

_source line 56 · 2026-05-14T04:18:12.959Z_

<details><summary>↩ Tool result · `toolu_01QfrzThYjARhJir3dXWZZt5`</summary>

```text
=== mvp_sim_4pl_gamma FULL ===
{
  "completed_at": "2026-05-13T10:59:01.402Z",
  "conclusion": "success",
  "created_at": "2026-05-13T04:27:47.251Z",
  "hypothesis": "4PL+\u03b3 IRT model can separate contamination effect (\u03b3) from true ability (\u03b8) on synthetic data; \u03b3 posterior recovers true value within \u00b10.15, \u03b8 correlation >0.9",
  "metrics": {
    "variant_a_nitems300": {
      "divergent_pct": 0,
      "fit_time_sec": 1407.5,
      "gamma_ci_covers_true": true,
      "gamma_ci_excludes_zero": true,
      "gamma_mean": 0.466,
      "gamma_rel_bias": 0.068,
      "max_rhat": 1.003,
      "overall": "PASS",
      "theta_corr": 0.943,
      "theta_rmse": 0.238
    }
  },
  "retry_count": 0,
  "spec": {
    "checkpoint_path": "artifacts/mvp_simulation/p1_variant_results.json",
    "command": "python run_p1_base.py",
    "data_count": "50 models x 100 items = 5000 responses",
    "data_path": "synthetic (generated in-script)",
    "log_path": "/tmp/p1_variants.log",
    "model_name": "2PL+\u03b3 / 4PL+\u03b3 IRT (Stan)",
    "note": "Order: 2PL ADVI \u2192 2PL NUTS \u2192 4PL ADVI \u2192 4PL NUTS",
    "pid": 197929,
    "seed": 42,
    "server": "local-cpu"
  },
  "status": "DONE",
  "updated_at": "2026-05-13T10:59:01.402Z"
}

=== mvp_sim_confounding FULL ===
{
  "completed_at": "2026-05-13T16:28:42.378Z",
  "conclusion": "success",
  "created_at": "2026-05-13T04:39:19.345Z",
  "hypothesis": "4PL+\u03b3 IRT model can still separate \u03b3 from \u03b8 when exposure is confounded with ability (corr\u22480.4); if not, need model-level random effect for exposure",
  "metrics": {
    "actual_confound_corr": 0.3814,
    "divergent_pct": 0,
    "fit_time_sec": 832,
    "gamma_ci_covers_true": true,
    "gamma_ci_excludes_zero": true,
    "gamma_mean": 0.5386,
    "gamma_rel_bias": 0.0771,
    "max_rhat": 1.007,
    "min_ess": 1371.9,
    "overall": "PASS",
    "theta_corr": 0.9733,
    "theta_residual_exp_corr": 0.0582,
    "theta_rmse": 0.2407
  },
  "retry_count": 0,
  "spec": {
    "checkpoint_path": "artifacts/mvp_simulation/p2_confounding_results.json",
    "command": "python run_p2_confounding.py",
    "data_count": "50 models x 300 items = 15000 responses",
    "data_path": "synthetic confounded (corr\u22480.38)",
    "log_path": "/tmp/p2_confounding.log",
    "model_name": "4PL+\u03b3 IRT (Stan NUTS)",
    "note": "N_items=300 (matching Variant A PASS config), 4PL NUTS only, 4 chains 1000+1000, \u03b8-exposure corr=0.381",
    "pid": 202872,
    "seed": 123,
    "server": "local-cpu"
  },
  "status": "DONE",
  "updated_at": "2026-05-13T16:28:42.378Z"
}

=== exp_001_sft_injection FULL ===
{
  "completed_at": "2026-05-13T23:14:30.258Z",
  "conclusion": "success",
  "created_at": "2026-05-13T17:28:01.546Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_failed",
        "ts": "2026-05-13T19:18:08.635006+00:00"
      },
      {
        "action": "manual_fix",
        "event": "status_rollback",
        "reason": "Cron misidentified old PID as dead \u2192 auto-failed. 3 paraphrase processes (GPU 0-2) still running. Rolled back DONE/failed \u2192 RUNNING per Director instruction.",
        "ts": "2026-05-13T19:32:00.000Z"
      },
      {
        "action": "agent",
        "event": "on_failed",
        "ts": "2026-05-13T23:14:43.962197+00:00"
      }
    ]
  },
  "failure_reason": "",
  "hypothesis": "Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+\u03b3 IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds",
  "metrics": {
    "arc_qc_pass": 697,
    "arc_qc_rate": 0.595,
    "arc_total": 1172,
    "gsm8k_qc_pass": 228,
    "gsm8k_qc_rate": 0.173,
    "gsm8k_total": 1319,
    "humaneval_total": 164,
    "mmlu_qc_pass": 6596,
    "mmlu_qc_rate": 0.47,
    "mmlu_total": 14042
  },
  "notes": "MMLU paraphrase 3-attempt QC \u91cd\u8bd5\u6d41\u7a0b: Attempt 1 \u2705 (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 \u8fdb\u884c\u4e2d (v2\u91cd\u542f, 439 batches total, \u8fdb\u5ea6~22%). Attempt 3 \u5f85\u

=== exp_004_sim_sweep FULL ===
{
  "completed_at": "2026-05-14T03:41:12.265Z",
  "conclusion": null,
  "created_at": "2026-05-13T16:43:57.478Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_failed",
        "ts": "2026-05-14T03:41:29.791249+00:00"
      }
    ]
  },
  "failure_reason": "SSH check failed 5x \u2014 last error: Unknown server 'local'. Available: ['cqa1-21977']",
  "hypothesis": "4PL+\u03b3 IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which \u03b3 95% CI width exceeds 15pp; recovery improves with N_models; prior sensitivity is bounded",
  "retry_count": 0,
  "spec": {
    "log_path": "/tmp/exp004_sweep.log",
    "pid": "340553",
    "timeout_per_fit": 7200
  },
  "status": "RUNNING",
  "updated_at": "2026-05-14T03:44:17.318015+00:00"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "f71f4798-83ed-4821-802a-19c107ac5a0f"
}
```

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "description": "Running Dump full JSON for experiments with metrics and exp_005 variants",
  "usage": {
    "total_tokens": 33025,
    "tool_uses": 13,
    "duration_ms": 80688
  },
  "last_tool_name": "Bash",
  "uuid": "635b9a35-681a-4734-b8e6-f7027d16e5e3",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01HWMC9xXTxaPX9HNbjdR9ie`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt', 'r') as f:\n    outer = json.load(f)\n\nresult_str = outer['result']\ndata = json.loads(result_str)\ninner = data['data']\nexps = inner.get('experiments', {})\n\n# Print full JSON for exp_005 variants and any exp with metrics\nfor exp_id, exp in sorted(exps.items()):\n    if exp.get('metrics') or exp_id.startswith('exp_005'):\n        print(f'=== {exp_id} FULL ===')\n        print(json.dumps(exp, indent=2, ensure_ascii=False)[:2000])\n        print()\n\"\n",
  "description": "Dump full JSON for experiments with metrics and exp_005 variants"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "a90ec98c-60e9-4c0e-a27a-c178db4eb16f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RXE7icDEY4q7wDaE4dC4WK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2525,
      "cache_read_input_tokens": 29960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2525,
        "ephemeral_1h_input_tokens": 0
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

_source line 59 · 2026-05-14T04:18:22.115Z_

<details><summary>↩ Tool result · `toolu_01HWMC9xXTxaPX9HNbjdR9ie`</summary>

```text
=== exp_001_eval_05B_d000_s123 FULL ===
{
  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter",
  "completed_at": "2026-05-14T01:29:09.875Z",
  "conclusion": "success",
  "created_at": "2026-05-13T22:30:40.455Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_complete",
        "ts": "2026-05-14T01:26:32.038369+00:00"
      }
    ]
  },
  "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log",
  "metrics": {
    "arc_challenge_accuracy": 0.3976,
    "gsm8k_exact_match": 0.3404,
    "humaneval_pass_at_1": 0.1037,
    "mmlu_accuracy": 0.4182
  },
  "reproduce": {
    "finished_at": "2026-05-14T01:26:29.607Z"
  },
  "retry_count": 0,
  "spec": {
    "account": "root",
    "backend": "tmux",
    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter",
    "command": "python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval",
    "data_count": null,
    "data_path": "d000 (baseline, no contamination)",
    "eval_data": "mmlu gsm8k arc_challenge humaneval",
    "gpu": [
      "cuda:2"
    ],
    "gpu_hours": 2.72,
    "gpu_ids": [
      "cuda:2"
    ],
    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log",
    "model_name": "Qwen2.5-0.5B",
    "parent": "exp_001_train_05B_d000_s123",
    "pid": "229516",
    "seed": 123,
    "server": "cqa1-21977",
    "submitted_at": "2026-05-13T22:45:48.124Z",
    "submitted_via": "submit_training_job",
    "wall_clock_seconds": 9801.8
  },
  "status": "DONE",
  "updated_at": "2026-05-14T01:29:09.875Z"
}

=== exp_001_eval_15B_d000_s42_v2 FULL ===
{
  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter",
  "completed_at": "2026-05-14T03:12:11.373Z",
  "conclusion": "success",
  "created_at": "2026-05-14T00:23:20.112Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_complete",
        "ts": "2026-05-14T03:09:29.636850+00:00"
      }
    ]
  },
  "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log",
  "metrics": {
    "arc_challenge_accuracy": 0.7756,
    "arc_challenge_correct": 909,
    "arc_challenge_total": 1172,
    "gsm8k_correct": 840,
    "gsm8k_exact_match": 0.6368,
    "gsm8k_total": 1319,
    "humaneval_correct": 21,
    "humaneval_pass_at_1": 0.128,
    "humaneval_total": 164,
    "mmlu_accuracy": 0.5753,
    "mmlu_correct": 8079,
    "mmlu_total": 14042
  },
  "reproduce": {
    "finished_at": "2026-05-14T03:09:26.521Z"
  },
  "retry_count": 0,
  "spec": {
    "account": "root",
    "backend": "tmux",
    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter",
    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
    "data_count": 26000,
    "data_path": "mmlu,gsm8k,arc_challenge,humaneval",
    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
    "gpu": [
      "cuda:4"
    ],
    "gpu_hours": 2.81,
    "log_

=== exp_001_sft_0pct_05B FULL ===
{
  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42",
  "completed_at": "2026-05-13T20:36:06.744Z",
  "conclusion": "success",
  "created_at": "2026-05-13T19:35:01.170Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_complete",
        "ts": "2026-05-13T20:33:54.496690+00:00"
      }
    ]
  },
  "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log",
  "metrics": {
    "adapter_size_mb": 34,
    "checkpoint_size_mb": 166,
    "exit_code": 0,
    "final_loss": 1.4894,
    "mean_train_loss": 1.5388,
    "steps": "3125/3125",
    "token_accuracy": 0.682,
    "training_time_min": 52.9
  },
  "reproduce": {
    "finished_at": "2026-05-13T20:33:53.420Z"
  },
  "retry_count": 0,
  "spec": {
    "account": "root",
    "backend": "tmux",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42 --seed 42 --gpu 3 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\"",
    "gpu": [
      "cuda:3"
    ],
    "gpu_hours": 0.98,
    "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log",
    "pid": "208933",
    "server": "cqa1-21977",
    "submitted_at": "2026-05-13T19:37:23.024Z",
    "submitted_via": "submit_training_job",
    "wall_clock_seconds": 3523.7
  },
  "status": "DONE",
  "updated_at": "2026-05-13T20:37:01.562Z"
}

=== exp_001_sft_0pct_05B_s123 FULL ===
{
  "completed_at": "2026-05-13T22:30:25.819Z",
  "conclusion": "success",
  "created_at": "2026-05-13T20:35:04.879Z",
  "hypothesis": "0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation)",
  "metrics": {
    "token_acc": 0.676,
    "train_loss": 1.5393,
    "train_time_min": 54.5
  },
  "notes": "OOM 修复后重提交 --gpu 1 (物理 GPU 1)。Worker 确认 PID 216028 训练中 (2/3125 steps, ~1.87s/it)",
  "retry_count": 0,
  "spec": {
    "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123 --seed 123 --gpu 1 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\"",
    "data_count": "50000",
    "data_path": "/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl",
    "gpu": [
      "cuda:1"
    ],
    "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B_s123.log",
    "model_name": "Qwen2.5-0.5B",
    "pid": "216033",
    "seed": 123,
    "server": "cqa1-21977"
  },
  "status": "DONE",
  "updated_at": "2026-05-13T22:30:25.819Z"
}

=== exp_001_sft_0pct_15B FULL ===
{
  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42",
  "completed_at": "2026-05-13T21:27:59.348Z",
  "conclusion": "success",
  "created_at": "2026-05-13T19:39:48.369Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_complete",
        "ts": "2026-05-13T21:25:42.551081+00:00"
      }
    ]
  },
  "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log",
  "metrics": {
    "adapter_size_mb": 71,
    "checkpoint_size_mb": 313,
    "exit_code": 0,
    "final_loss": 1.2039,
    "mean_train_loss": 1.2599,
    "steps": "3125/3125",
    "token_accuracy": 0.711,
    "training_time_min": 101.5
  },
  "reproduce": {
    "finished_at": "2026-05-13T21:25:40.979Z"
  },
  "retry_count": 0,
  "spec": {
    "account": "root",
    "backend": "tmux",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42 --seed 42 --gpu 4 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\"",
    "gpu": [
      "cuda:4"
    ],
    "gpu_hours": 1.78,
    "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log",
    "pid": "210116",
    "server": "cqa1-21977",
    "submitted_at": "2026-05-13T19:41:11.760Z",
    "submitted_via": "submit_training_job",
    "wall_clock_seconds": 6407.6
  },
  "status": "DONE",
  "updated_at": "2026-05-13T21:27:59.348Z"
}

=== exp_001_sft_0pct_15B_s123 FULL ===
{
  "completed_at": "2026-05-13T22:30:26.882Z",
  "conclusion": "success",
  "created_at": "2026-05-13T20:35:07.346Z",
  "hypothesis": "0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance estimation)",
  "metrics": {
    "token_acc": 0.731,
    "train_loss": 1.2602,
    "train_time_min": 101.5
  },
  "notes": "OOM 修复后重提交 --gpu 2 (物理 GPU 2)。Worker 确认 PID 216106 训练中 (1/3125 steps, ~2.58s/it)",
  "retry_count": 0,
  "spec": {
    "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123 --seed 123 --gpu 2 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\"",
    "data_count": "50000",
    "data_path": "/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl",
    "gpu": [
      "cuda:2"
    ],
    "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B_s123.log",
    "model_name": "Qwen2.5-1.5B",
    "pid": "216111",
    "seed": 123,
    "server": "cqa1-21977"
  },
  "status": "DONE",
  "updated_at": "2026-05-13T22:30:26.882Z"
}

=== exp_001_sft_0pct_3B FULL ===
{
  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42",
  "completed_at": "2026-05-13T23:25:49.016Z",
  "conclusion": "success",
  "created_at": "2026-05-13T19:44:40.471Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_complete",
        "ts": "2026-05-13T23:23:43.393661+00:00"
      }
    ]
  },
  "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log",
  "metrics": {
    "adapter_size_mb": 115,
    "checkpoint_size_mb": 488,
    "exit_code": 0,
    "final_loss": 1.0736,
    "mean_train_loss": 1.1306,
    "steps": "3125/3125",
    "token_accuracy": 0.734,
    "training_time_min": 214.7
  },
  "reproduce": {
    "finished_at": "2026-05-13T23:23:41.844Z"
  },
  "retry_count": 0,
  "spec": {
    "account": "root",
    "backend": "tmux",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\"",
    "gpu": [
      "cuda:5"
    ],
    "gpu_hours": 3.69,
    "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log",
    "pid": "210666",
    "server": "cqa1-21977",
    "submitted_at": "2026-05-13T19:44:40.431Z",
    "submitted_via": "submit_training_job",
    "wall_clock_seconds": 13268.6
  },
  "status": "DONE",
  "updated_at": "2026-05-13T23:25:49.016Z"
}

=== exp_001_sft_0pct_3B_s123 FULL ===
{
  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123",
  "completed_at": "2026-05-14T00:23:18.290Z",
  "conclusion": "success",
  "created_at": "2026-05-13T20:39:01.606Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_complete",
        "ts": "2026-05-14T00:16:17.727184+00:00"
      }
    ]
  },
  "hypothesis": "0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance estimation)",
  "metrics": {
    "adapter_model_mb": 114,
    "adapter_size_mb": 488,
    "checkpoint_size_mb": 488,
    "epochs": 1,
    "final_loss": 1.114,
    "mean_token_accuracy": 0.7505,
    "mean_train_loss": 1.1309,
    "steps_completed": 3125,
    "total_steps": 3125,
    "total_tokens": 19555717,
    "train_samples_per_second": 3.91,
    "training_time_min": 213.1
  },
  "notes": "OOM 修复后重提交 --gpu 3 (物理 GPU 3)。Worker 确认 PID 216249 训练中，ETA ~3.4h",
  "reproduce": {
    "finished_at": "2026-05-14T00:16:04.357Z"
  },
  "retry_count": 0,
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123 --seed 123 --gpu 3 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\"",
    "data_count": "50000",
    "data_path": "/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl",
    "gpu": [
      "cuda:3"
    ],
    "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B_s123.log",
    "model_name": "Qwen2.5-3B",
    "pid": "216935",
    "seed": 123,
    "server": "cqa1-21977"
  },
  "status": "DONE",
  "updated_at": "2026-05-14T00:23:18.290Z"
}

=== exp_001_sft_d005_05B_v3 FULL ===
{
  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42",
  "completed_at": "2026-05-14T00:58:15.977Z",
  "conclusion": "success",
  "created_at": "2026-05-13T23:52:39.321Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_complete",
        "ts": "2026-05-14T00:55:43.945907+00:00"
      }
    ]
  },
  "hypothesis": "5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.",
  "metrics": {
    "checkpoint_size_mb": 166,
    "entropy": 1.5874,
    "epoch": 1,
    "exit_code": 0,
    "final_loss": 1.478,
    "lora_adapter_size_mb": 33.6,
    "mean_train_loss": 1.5424,
    "num_tokens": 19657865,
    "token_accuracy": 0.667,
    "total_steps": 3177,
    "train_samples_per_second": 15.09,
    "train_steps_per_second": 0.943,
    "training_time_min": 56.14,
    "vs_baseline_0pct": {
      "baseline_final_loss": 1.4894,
      "baseline_mean_train_loss": 1.5388,
      "baseline_token_accuracy": 0.682,
      "baseline_training_time_min": 52.9,
      "delta_final_loss": -0.0114,
      "delta_mean_train_loss": 0.0036,
      "delta_token_accuracy": -0.015,
      "delta_training_time_min": 3.24
    }
  },
  "notes": "dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。v3 已修复 --gpu 5（v1/v2 均为 --gpu 0 错误）。此 run 使用 ALL paraphrases（含 QC fail），属于 \"noisy contamination\" condition。",
  "parent": "exp_001_sft_d005_05B",
  "reproduce": {
    "finished_at": "2026-05-14T00:55:38.416Z"
  },
  "retry_count": 0,
  "spec": {
    "account": "root",
    "backend": "tmux",
    "checkpoint_source": "N/A (SFT retry, not eval)",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-t

=== exp_001_sft_d100_05B FULL ===
{
  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42",
  "completed_at": "2026-05-14T00:53:49.656Z",
  "conclusion": "success",
  "created_at": "2026-05-13T23:36:13.403Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_complete",
        "ts": "2026-05-14T00:50:19.949448+00:00"
      }
    ]
  },
  "gpu": "cuda:0",
  "hypothesis": "100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison",
  "log_path": "/root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log",
  "metrics": {
    "exit_code": 0,
    "final_loss": 1.5943,
    "mean_train_loss": 1.5662,
    "num_tokens": 21575068,
    "token_accuracy": 0.666,
    "total_steps": 4160,
    "train_samples_per_second": 16.09,
    "train_steps_per_second": 1.006,
    "training_time_min": 68.9,
    "vs_baseline_0pct": {
      "accuracy_delta": "-0.016 (-2.3%)",
      "loss_delta": "+0.0274 (+1.8%)",
      "time_delta": "+16min (+30%)"
    }
  },
  "notes": "dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533。此 run 使用 ALL paraphrases（含 QC fail），属于 \"noisy contamination\" condition。",
  "pid": "235243",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\"",
    "finished_at": "2026-05-14T00:50:16.569Z",
    "gpu": "cuda:0",
    "server": "cqa1-21977",
    "started_at": "2026-05-13T23:38:41.749Z",


=== exp_001_sft_injection FULL ===
{
  "completed_at": "2026-05-13T23:14:30.258Z",
  "conclusion": "success",
  "created_at": "2026-05-13T17:28:01.546Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_failed",
        "ts": "2026-05-13T19:18:08.635006+00:00"
      },
      {
        "action": "manual_fix",
        "event": "status_rollback",
        "reason": "Cron misidentified old PID as dead → auto-failed. 3 paraphrase processes (GPU 0-2) still running. Rolled back DONE/failed → RUNNING per Director instruction.",
        "ts": "2026-05-13T19:32:00.000Z"
      },
      {
        "action": "agent",
        "event": "on_failed",
        "ts": "2026-05-13T23:14:43.962197+00:00"
      }
    ]
  },
  "failure_reason": "",
  "hypothesis": "Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds",
  "metrics": {
    "arc_qc_pass": 697,
    "arc_qc_rate": 0.595,
    "arc_total": 1172,
    "gsm8k_qc_pass": 228,
    "gsm8k_qc_rate": 0.173,
    "gsm8k_total": 1319,
    "humaneval_total": 164,
    "mmlu_qc_pass": 6596,
    "mmlu_qc_rate": 0.47,
    "mmlu_total": 14042
  },
  "notes": "MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 ✅ (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attempt 3 待定. 输出在全部 attempt 结束后一次性写出 mmlu_paraphrases.json. GSM8K ✅ 1319条(QC 17.3%), ARC ✅ 1172条(QC 59.5%).",
  "reproduce": {
    "finished_at": "2026-05-13T23:14:29.355Z"
  },
  "retry_count": 0,
  "spec": {
    "command": "Phase 1 paraphrase: GPU 0 MMLU (PID 204467 v3, vLLM bs=16). GSM8K + ARC completed.",
    "data_count": "45 SFT runs + 90 eval runs (original+paraphrased)",
    "data_path": "MMLU+GSM8K+ARC-Challenge+HumanEval paraphrases → SFT data mixing",
    "gpu": "cuda:0 (MMLU vLLM, still running). cuda:1/2 freed (GSM8K+ARC done).",
    "model_name": "Qwen2.5-0.5B/1.5B/3B (LoR

=== exp_005_noise_prop FULL ===
{
  "completed_at": "2026-05-13T20:47:21.810Z",
  "conclusion": "failed",
  "created_at": "2026-05-13T18:31:00.000Z",
  "failure_reason": "Stan numerical bugs: sigma_e=0 allowed (normal_lpdf crash), c/d boundary causing chain crashes, max_treedepth=10 insufficient (14.5% hit rate). All fixed, restarting.",
  "hypothesis": "Measurement error in exposure scores propagates through 4PL+γ IRT to widen calibrated score CIs; analytical ME model (conjugate normal integration) produces equivalent CI widths to full latent-τ model at fraction of compute",
  "retry_count": 0,
  "spec": {
    "command": "cd artifacts/exp005_noise_propagation && source ../mvp_simulation/.venv/bin/activate && python run_noise_propagation.py",
    "data_count": "multiple σ_e values × seeds",
    "data_path": "synthetic (generated in-script)",
    "model_name": "4PL+γ IRT (CmdStanPy NUTS)",
    "pid": 234646,
    "seed": "0-9",
    "server": "local (CPU only)"
  },
  "status": "DONE",
  "updated_at": "2026-05-13T20:47:21.810Z"
}

=== exp_005_noise_prop_v2 FULL ===
{
  "completed_at": "2026-05-13T22:44:09.262Z",
  "conclusion": "failed",
  "created_at": "2026-05-13T20:47:35.807Z",
  "extra": {
    "hook_events": [
      {
        "action": "agent",
        "event": "on_failed",
        "ts": "2026-05-13T21:09:53.826444+00:00"
      },
      {
        "action": "manual_fix",
        "event": "status_rollback",
        "reason": "Cron false positive: server=\"local\" not in SSH list. PID 251971 alive, 2 Stan chains at 42% CPU. Rolled back DONE/failed → RUNNING.",
        "ts": "2026-05-13T21:12:00.000Z"
      }
    ]
  },
  "failure_reason": "根因：/tmp tmpfs 磁盘配额耗尽。ME model 先跑 95min 生成 ~1GB CSV（9000 tau + 9000 log_lik × 4 chains）耗尽 3.9GB tmpfs。Simple model 写 CSV 时 disk quota exceeded → 4 chains 全部 retcode=1。ME model Rhat=1.945 是独立问题：10231 参数 vs 9000 观测，严重欠识别，需换用 analytic 版本。修复：(1) output_dir 设到非 tmpfs (2) 先跑 simple 再跑 ME (3) ME 换 contam_irt_4pl_me_analytic.stan (4) σ_e=0.1/0.3 均可收敛。",
  "hypothesis": "Same as exp_005: ME model CI width increases monotonically with σ_e; simple model does not. v2 fixes: sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12.",
  "notes": "失败根因: 1) /tmp tmpfs 3.9GB 耗尽（ME模型生成~1GB Stan CSV，Simple 4 chains全部retcode=1）; 2) ME模型严重欠识别（10231参数 vs 9000观测，Rhat=1.945）。诊断结果: σ_e=0.3 simple收敛良好(γ=0.458, true=0.5, Rhat=1.007); σ_e=0.1 simple收敛但γ偏高57.5%(0.788 vs 0.5)——identifiability限制非bug。v3已启动修复两个根因。",
  "parent": "exp_005_noise_prop",
  "retry_count": 0,
  "spec": {
    "command": "python run_noise_propagation.py --output-dir output_v2 --base-seed 42 --n-seeds 5",
    "data_count": "5 σ_e levels × 5 seeds × 2 models = 50 Stan fits",
    "data_path": "synthetic (generated in-script)",
    "fixes": "sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12",
    "log_path": "artifacts/exp005_noise_propagation/exp005_v2.log",
    "model_name": "4PL+γ IRT (CmdStanPy NUTS, max_treedepth=12)",
    "pid": 251971,
    "seed": "42-46",
    "server": "local (CPU only)"
  },
  "status": "DONE",
  

=== exp_005_noise_prop_v3 FULL ===
{
  "completed_at": "2026-05-14T03:29:53.328Z",
  "conclusion": null,
  "created_at": "2026-05-14T03:24:06.949Z",
  "hypothesis": "Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic ME (1231 params), checkpoint resume.",
  "retry_count": 0,
  "spec": {
    "checkpoint_path": "artifacts/exp005_noise_propagation/output_v3",
    "command": "cd artifacts/exp005_noise_propagation && nohup .venv/bin/python run_noise_propagation_v3.py --output-dir output_v3 --base-seed 42 --n-seeds 5 > exp005_v3.log 2>&1 &",
    "data_count": 9000,
    "data_path": "synthetic",
    "log_path": "artifacts/exp005_noise_propagation/exp005_v3.log",
    "model_name": "4PL+gamma IRT (simple + analytic ME)",
    "note": "v3: Stan output on local disk, analytic ME model (1231 params vs 10231), simple-first then ME, checkpoint resume support, chain CSV cleanup after each fit. 5 sigma_e levels x 5 seeds x 2 models = 50 fits. ETA ~11-12 hours (Simple ~125min, Analytic ME ~575min)",
    "pid": "339838",
    "seed": 42,
    "server": "local"
  },
  "status": "RUNNING",
  "updated_at": "2026-05-14T03:36:19.610665Z"
}

=== mvp_sim_4pl_gamma FULL ===
{
  "completed_at": "2026-05-13T10:59:01.402Z",
  "conclusion": "success",
  "created_at": "2026-05-13T04:27:47.251Z",
  "hypothesis": "4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9",
  "metrics": {
    "variant_a_nitems300": {
      "divergent_pct": 0,
      "fit_time_sec": 1407.5,
      "gamma_ci_covers_true": true,
      "gamma_ci_excludes_zero": true,
      "gamma_mean": 0.466,
      "gamma_rel_bias": 0.068,
      "max_rhat": 1.003,
      "overall": "PASS",
      "theta_corr": 0.943,
      "theta_rmse": 0.238
    }
  },
  "retry_count": 0,
  "spec": {
    "checkpoint_path": "artifacts/mvp_simulation/p1_variant_results.json",
    "command": "python run_p1_base.py",
    "data_count": "50 models x 100 items = 5000 responses",
    "data_path": "synthetic (generated in-script)",
    "log_path": "/tmp/p1_variants.log",
    "model_name": "2PL+γ / 4PL+γ IRT (Stan)",
    "note": "Order: 2PL ADVI → 2PL NUTS → 4PL ADVI → 4PL NUTS",
    "pid": 197929,
    "seed": 42,
    "server": "local-cpu"
  },
  "status": "DONE",
  "updated_at": "2026-05-13T10:59:01.402Z"
}

=== mvp_sim_confounding FULL ===
{
  "completed_at": "2026-05-13T16:28:42.378Z",
  "conclusion": "success",
  "created_at": "2026-05-13T04:39:19.345Z",
  "hypothesis": "4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure",
  "metrics": {
    "actual_confound_corr": 0.3814,
    "divergent_pct": 0,
    "fit_time_sec": 832,
    "gamma_ci_covers_true": true,
    "gamma_ci_excludes_zero": true,
    "gamma_mean": 0.5386,
    "gamma_rel_bias": 0.0771,
    "max_rhat": 1.007,
    "min_ess": 1371.9,
    "overall": "PASS",
    "theta_corr": 0.9733,
    "theta_residual_exp_corr": 0.0582,
    "theta_rmse": 0.2407
  },
  "retry_count": 0,
  "spec": {
    "checkpoint_path": "artifacts/mvp_simulation/p2_confounding_results.json",
    "command": "python run_p2_confounding.py",
    "data_count": "50 models x 300 items = 15000 responses",
    "data_path": "synthetic confounded (corr≈0.38)",
    "log_path": "/tmp/p2_confounding.log",
    "model_name": "4PL+γ IRT (Stan NUTS)",
    "note": "N_items=300 (matching Variant A PASS config), 4PL NUTS only, 4 chains 1000+1000, θ-exposure corr=0.381",
    "pid": 202872,
    "seed": 123,
    "server": "local-cpu"
  },
  "status": "DONE",
  "updated_at": "2026-05-13T16:28:42.378Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "16c5e93f-8f75-4a37-a841-bcc58a54648d"
}
```

</details>

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a8523d6655143f568",
  "tool_use_id": "toolu_01DAocpnKSJLdbXsJd7evPbS",
  "status": "completed",
  "output_file": "",
  "summary": "Parse registry JSON data",
  "usage": {
    "total_tokens": 45420,
    "tool_uses": 13,
    "duration_ms": 159696
  },
  "uuid": "3e34b115-87c5-4867-a2a7-0aff751a8970",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55"
}
```

---

### Tool result

_source line 61 · 2026-05-14T04:19:40.686Z_

<details><summary>↩ Tool result · `toolu_01DAocpnKSJLdbXsJd7evPbS`</summary>

```text
I now have all the information needed. Here is the complete structured table of all 44 experiments:

---

## Registry: All 44 Experiments

No experiment records a `claim_id` field — the `claim` column is uniformly absent from all entries.

---

### MVP / Simulation Experiments

| Experiment ID | Status | Created | Updated/Completed | Conclusion | Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **mvp_sim_4pl_gamma** | DONE | 2026-05-13T04:27 | Completed 2026-05-13T10:59 | **success** | γ_mean=0.466, γ_rel_bias=6.8%, γ_CI_covers_true=true, γ_CI_excludes_zero=true, θ_corr=0.943, θ_rmse=0.238, max_Rhat=1.003, divergent_pct=0, fit_time=1407s. Overall: PASS | None |
| **mvp_sim_confounding** | DONE | 2026-05-13T04:39 | Completed 2026-05-13T16:28 | **success** | γ_mean=0.5386, γ_rel_bias=7.7%, γ_CI_covers_true=true, γ_CI_excludes_zero=true, θ_corr=0.9733, θ_rmse=0.2407, actual_confound_corr=0.381, min_ESS=1371.9, max_Rhat=1.007, divergent_pct=0, fit_time=832s. Overall: PASS | None |

**Hypothesis (mvp_sim_4pl_gamma):** 4PL+γ IRT can separate γ from θ on synthetic data; γ posterior recovers within ±0.15, θ corr >0.9.
**Hypothesis (mvp_sim_confounding):** Model still separates γ from θ when exposure is confounded with ability (corr≈0.4).

---

### exp_004 — Simulation Parameter Sweep

| Experiment ID | Status | Created | Updated/Completed | Conclusion | Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **exp_004_sim_sweep** | RUNNING | 2026-05-13T16:43 | Updated 2026-05-14T03:44 / Completed (logged) 2026-05-14T03:41 | null | None recorded | SSH check failed 5x — "Unknown server 'local'. Available: ['cqa1-21977']" |

**Hypothesis:** 4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); minimum AUC threshold below which γ 95% CI >15pp; recovery improves with N_models; prior sensitivity is bounded.

---

### exp_005 — Noise Propagation

| Experiment ID | Status | Created | Updated/Completed | Conclusion | Key Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **exp_005_noise_prop** | DONE | 2026-05-13T18:31 | Completed 2026-05-13T20:47 | **failed** | None | Stan bugs: sigma_e=0 allowed (normal_lpdf crash), c/d boundary crashes, max_treedepth=10 insufficient (14.5% hit rate) |
| **exp_005_noise_prop_v2** | DONE | 2026-05-13T20:47 | Completed 2026-05-13T22:44 | **failed** | Partial: σ_e=0.3 simple converged (γ=0.458, true=0.5, Rhat=1.007); σ_e=0.1 γ=0.788 (57.5% bias — identifiability limit). ME model Rhat=1.945 (10231 params vs 9000 obs, underidentified) | /tmp tmpfs exhausted (ME model ~1GB CSV); ME model severely underidentified |
| **exp_005_noise_prop_v3** | RUNNING | 2026-05-14T03:24 | Updated 2026-05-14T03:36 / log-completed 2026-05-14T03:29 | null | None yet | None |

**Hypothesis (v3):** ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases. v3 fixes: local disk Stan output, analytic ME (1231 params), simple-first order, checkpoint resume.

---

### exp_001 — SFT Contamination Injection (Data Preparation)

| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **exp_001_sft_injection** | DONE | 2026-05-13T17:28 | 2026-05-13T23:14 | **success** | MMLU: 14042 total, 6596 QC pass (47%); GSM8K: 1319 total, 228 QC pass (17.3%); ARC: 1172 total, 697 QC pass (59.5%); HumanEval: 164 total | None (had cron false-positive failures, manually rolled back) |

---

### exp_001 — SFT Training (0% dosage / clean baseline)

| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **exp_001_sft_0pct** | DONE | 2026-05-13T19:26 | 2026-05-14T00:36 | **success** | (parent/umbrella record, no direct metrics) | None |
| **exp_001_sft_0pct_05B** (s42) | DONE | 2026-05-13T19:35 | 2026-05-13T20:36 | **success** | final_loss=1.4894, mean_train_loss=1.5388, token_acc=0.682, steps=3125, train_time=52.9min, adapter_size=34MB | None |
| **exp_001_sft_0pct_05B_s123** | DONE | 2026-05-13T20:35 | 2026-05-13T22:30 | **success** | train_loss=1.5393, token_acc=0.676, train_time=54.5min | None |
| **exp_001_sft_0pct_15B** (s42) | DONE | 2026-05-13T19:39 | 2026-05-13T21:27 | **success** | final_loss=1.2039, mean_train_loss=1.2599, token_acc=0.711, steps=3125, train_time=101.5min, adapter_size=71MB | None |
| **exp_001_sft_0pct_15B_s123** | DONE | 2026-05-13T20:35 | 2026-05-13T22:30 | **success** | train_loss=1.2602, token_acc=0.731, train_time=101.5min | None |
| **exp_001_sft_0pct_3B** (s42) | DONE | 2026-05-13T19:44 | 2026-05-13T23:25 | **success** | final_loss=1.0736, mean_train_loss=1.1306, token_acc=0.734, steps=3125, train_time=214.7min, adapter_size=115MB | None |
| **exp_001_sft_0pct_3B_s123** | DONE | 2026-05-13T20:39 | 2026-05-14T00:23 | **success** | final_loss=1.114, mean_train_loss=1.1309, token_acc=0.7505, steps=3125, train_time=213.1min, total_tokens=19.56M, throughput=3.91 samples/s | None |

---

### exp_001 — SFT Training (5% dosage contaminated)

| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **exp_001_sft_d005_05B** (v1) | DONE | 2026-05-13T23:36 | 2026-05-13T23:42 | **killed** | None | CUDA OOM at step 8/3177 — zombie 3B eval process (PID 234755) occupied 6.8GB GPU 5 |
| **exp_001_sft_d005_05B_v2** | DONE | 2026-05-13T23:48 | 2026-05-13T23:49 | **failed** | None | CUDA OOM: GPU 0 only 459MB free, process 235248 using 21.47GB |
| **exp_001_sft_d005_05B_r3** | PREPARING | 2026-05-13T23:58 | — | **killed** | None | OOM — v3 already occupied GPU 5, r3 was duplicate submission |
| **exp_001_sft_d005_05B_v3** | DONE | 2026-05-13T23:52 | 2026-05-14T00:58 | **success** | final_loss=1.478, mean_train_loss=1.5424, token_acc=0.667, steps=3177, train_time=56.14min, lora_adapter=33.6MB, throughput=15.09 samples/s. vs baseline: Δfinal_loss=-0.011, Δtoken_acc=-0.015 | None |
| **exp_001_sft_d005_15B** | RUNNING | 2026-05-14T00:19 | — | null (in progress) | None yet | None |

---

### exp_001 — SFT Training (100% dosage contaminated)

| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **exp_001_sft_d100_05B** | DONE | 2026-05-13T23:36 | 2026-05-14T00:53 | **success** | final_loss=1.5943, mean_train_loss=1.5662, token_acc=0.666, steps=4160, train_time=68.9min, total_tokens=21.58M, throughput=16.09 samples/s. vs baseline: Δloss=+0.027(+1.8%), Δacc=-0.016(-2.3%), Δtime=+16min(+30%) | None |
| **exp_001_sft_100pct_05B** | DONE | 2026-05-13T23:41 | 2026-05-13T23:49 | **failed** | None | Duplicate registry entry — actual training tracked by exp_001_sft_d100_05B |
| **exp_001_sft_d100_15B** (v1) | DONE | 2026-05-13T23:37 | 2026-05-14T01:23 | **failed** | None | OOM with batch_size=2, replaced by v2 |
| **exp_001_sft_d100_15B_v2** | RUNNING | 2026-05-14T01:17 | — | null (in progress) | None yet | None |

---

### exp_001 — Evaluation (0.5B model, 0% dosage)

| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **exp_001_eval_05B_d000_s123** | DONE | 2026-05-13T22:30 | 2026-05-14T01:29 | **success** | MMLU=0.4182, GSM8K=0.3404, ARC_Challenge=0.3976, HumanEval_pass@1=0.1037. GPU hours=2.72, wall_clock=9801.8s | None |
| **exp_001_eval_05B_d000_s42** (v1) | DONE | 2026-05-13T22:42 | 2026-05-14T01:29 | **failed** | None | FileNotFoundError in evaluate.py line 558: output dir path error |
| **exp_001_eval_05B_d000_s42_v2** | PREPARING | 2026-05-14T02:26 | — | **failed** | None | EXIT_CODE=137 (SIGKILL — OOM or manual) |
| **exp_001_eval_05B_d000_s42_v3** | PREPARING | 2026-05-14T02:30 | — | **killed** | None | None recorded |
| **exp_001_eval_05B_d000_s42_v4** | PREPARING | 2026-05-14T02:35 | — | **killed** | None | None recorded |
| **exp_001_eval_05B_d000_s42_v5** | RUNNING | 2026-05-14T02:39 | — | null (in progress) | None yet | None |
| **exp_001_eval_05B_d000_s42_v6** | PREPARING | 2026-05-14T02:40 | — | **killed** | None | None recorded |

---

### exp_001 — Evaluation (0.5B model, 100% dosage)

| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **exp_001_eval_05B_d005** | RUNNING | 2026-05-14T01:17 | — | null (in progress) | None yet | None |
| **exp_001_eval_05B_d100** (v1) | DONE | 2026-05-14T01:15 | 2026-05-14T02:21 | **failed** | None | EXIT_CODE=143 (SIGTERM — graceful kill) |
| **exp_001_eval_05B_d100_v2** | PENDING | 2026-05-14T02:26 | — | **failed** | None | EXIT_CODE=137 (SIGKILL — OOM or manual) |
| **exp_001_eval_05B_d100_v3** | PREPARING | 2026-05-14T02:30 | — | **killed** | None | None recorded |
| **exp_001_eval_05B_d100_v4** | PREPARING | 2026-05-14T02:36 | — | **killed** | None | None recorded |
| **exp_001_eval_05B_d100_v5** | RUNNING | 2026-05-14T02:39 | — | null (in progress) | None yet | None |
| **exp_001_eval_05B_d100_v6** | PREPARING | 2026-05-14T02:40 | — | **killed** | None | None recorded |

---

### exp_001 — Evaluation (1.5B model, 0% dosage)

| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **exp_001_eval_15B_d000_s42** (v1) | DONE | 2026-05-13T21:30 | 2026-05-14T00:23 | **failed** | None | Hung 11+ hrs: GPU util 0%, 5820MiB VRAM used, empty output dir. Root cause: relative model path caused silent hang. Kill -9 applied. |
| **exp_001_eval_15B_d000_s42_v2** | DONE | 2026-05-14T00:23 | 2026-05-14T03:12 | **success** | MMLU=0.5753 (8079/14042), GSM8K=0.6368 (840/1319), ARC_Challenge=0.7756 (909/1172), HumanEval_pass@1=0.128 (21/164). GPU hours=2.81 | None |
| **exp_001_eval_15B_d000_s123** | RUNNING | 2026-05-13T22:30 | Partial: 2026-05-13T23:39 (first attempt failed) | null (retry running) | None yet | First attempt: EXIT_CODE=2 (--gpu 0 arg caused crash); re-running without --gpu |

---

### exp_001 — Evaluation (3B model, 0% dosage)

| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |
|---|---|---|---|---|---|---|
| **exp_001_eval_3B_d000_s42** (v1) | RUNNING | 2026-05-13T23:36 | Partial: 2026-05-13T23:43 (first attempt) | null (retry running) | None yet | First attempt: --gpu arg crashed evaluate.py (same bug as 15B); retry running without --gpu |
| **exp_001_eval_3B_d000_s42_v2** | PREPARING | 2026-05-13T23:51 | — | **failed** | None | SIGKILL (EXIT_CODE=137) — killed by d005 worker reclaiming GPU 5 |
| **exp_001_eval_3B_d000_s42_v3** | PREPARING | 2026-05-14T00:48 | — | **killed** | None | None recorded |
| **exp_001_eval_3B_d000_s123** | RUNNING | 2026-05-14T00:18 | — | null (in progress) | None yet | None |

---

## Summary Statistics

| Status | Count |
|---|---|
| DONE (success) | 14 |
| DONE (failed/killed) | 16 |
| RUNNING | 8 |
| PREPARING | 5 |
| PENDING | 1 |
| **Total** | **44** |

## Key Findings from Completed Successful Experiments

- **mvp_sim_4pl_gamma / mvp_sim_confounding**: Core IRT model validated on synthetic data. γ recovered with <8% relative bias, θ corr >0.97, even under θ-exposure confounding (r=0.38). Both PASS.
- **0% dosage SFT baselines (all 6 models)**: All succeeded. Clean baseline LoRA trained on Qwen2.5-0.5B/1.5B/3B × seeds 42/123. Final losses range 1.07–1.59 across model sizes.
- **exp_001_sft_d100_05B**: 100% contamination SFT on 0.5B succeeded. Loss slightly higher (+1.8%) and throughput lower (-16min) than clean baseline — contamination data harder.
- **exp_001_sft_d005_05B_v3**: 5% contamination SFT on 0.5B succeeded. Marginally lower final loss than baseline (-0.011) suggesting contamination data slightly easier at low dose.
- **eval_05B_d000_s123**: Completed eval — 0.5B clean baseline scores: MMLU=41.8%, GSM8K=34.0%, ARC=39.8%, HumanEval=10.4%.
- **eval_15B_d000_s42_v2**: Completed eval — 1.5B clean baseline scores: MMLU=57.5%, GSM8K=63.7%, ARC=77.6%, HumanEval=12.8%.
- **exp_005 noise propagation**: Still failing (v3 RUNNING). v2 partial result shows simple model converges but ME model is severely underidentified (10231 params vs 9000 obs). Analytic ME version in v3 reduces to 1231 params.

agentId: a8523d6655143f568 (use SendMessage with to: 'a8523d6655143f568' to continue this agent)
&lt;usage>total_tokens: 49991
tool_uses: 13
duration_ms: 159719&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "0f33fc8d-7336-482f-8692-d8f437d77036",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the file /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/d63533b2-bcb5-4715-beda-24758b1a3a55/tool-results/mcp-agent-ml-research-read_registry-1778732207305.txt\n\nThis is JSON with schema: {result: string} where the inner result is also a JSON string.\n\nExtract and report for EVERY experiment entry:\n1. experiment id / registry_id\n2. status (RUNNING/DONE/FAILED/PLANNED etc.)\n3. conclusion (if any)\n4. created_at / updated_at timestamps\n5. Any metrics or key findings mentioned\n6. Which claim it supports\n7. Any error messages or failure reasons\n\nBe thorough - list every single experiment. Format as a structured table.",
    "agentId": "a8523d6655143f568",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is the complete structured table of all 44 experiments:\n\n---\n\n## Registry: All 44 Experiments\n\nNo experiment records a `claim_id` field — the `claim` column is uniformly absent from all entries.\n\n---\n\n### MVP / Simulation Experiments\n\n| Experiment ID | Status | Created | Updated/Completed | Conclusion | Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **mvp_sim_4pl_gamma** | DONE | 2026-05-13T04:27 | Completed 2026-05-13T10:59 | **success** | γ_mean=0.466, γ_rel_bias=6.8%, γ_CI_covers_true=true, γ_CI_excludes_zero=true, θ_corr=0.943, θ_rmse=0.238, max_Rhat=1.003, divergent_pct=0, fit_time=1407s. Overall: PASS | None |\n| **mvp_sim_confounding** | DONE | 2026-05-13T04:39 | Completed 2026-05-13T16:28 | **success** | γ_mean=0.5386, γ_rel_bias=7.7%, γ_CI_covers_true=true, γ_CI_excludes_zero=true, θ_corr=0.9733, θ_rmse=0.2407, actual_confound_corr=0.381, min_ESS=1371.9, max_Rhat=1.007, divergent_pct=0, fit_time=832s. Overall: PASS | None |\n\n**Hypothesis (mvp_sim_4pl_gamma):** 4PL+γ IRT can separate γ from θ on synthetic data; γ posterior recovers within ±0.15, θ corr >0.9.\n**Hypothesis (mvp_sim_confounding):** Model still separates γ from θ when exposure is confounded with ability (corr≈0.4).\n\n---\n\n### exp_004 — Simulation Parameter Sweep\n\n| Experiment ID | Status | Created | Updated/Completed | Conclusion | Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **exp_004_sim_sweep** | RUNNING | 2026-05-13T16:43 | Updated 2026-05-14T03:44 / Completed (logged) 2026-05-14T03:41 | null | None recorded | SSH check failed 5x — \"Unknown server 'local'. Available: ['cqa1-21977']\" |\n\n**Hypothesis:** 4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); minimum AUC threshold below which γ 95% CI >15pp; recovery improves with N_models; prior sensitivity is bounded.\n\n---\n\n### exp_005 — Noise Propagation\n\n| Experiment ID | Status | Created | Updated/Completed | Conclusion | Key Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **exp_005_noise_prop** | DONE | 2026-05-13T18:31 | Completed 2026-05-13T20:47 | **failed** | None | Stan bugs: sigma_e=0 allowed (normal_lpdf crash), c/d boundary crashes, max_treedepth=10 insufficient (14.5% hit rate) |\n| **exp_005_noise_prop_v2** | DONE | 2026-05-13T20:47 | Completed 2026-05-13T22:44 | **failed** | Partial: σ_e=0.3 simple converged (γ=0.458, true=0.5, Rhat=1.007); σ_e=0.1 γ=0.788 (57.5% bias — identifiability limit). ME model Rhat=1.945 (10231 params vs 9000 obs, underidentified) | /tmp tmpfs exhausted (ME model ~1GB CSV); ME model severely underidentified |\n| **exp_005_noise_prop_v3** | RUNNING | 2026-05-14T03:24 | Updated 2026-05-14T03:36 / log-completed 2026-05-14T03:29 | null | None yet | None |\n\n**Hypothesis (v3):** ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases. v3 fixes: local disk Stan output, analytic ME (1231 params), simple-first order, checkpoint resume.\n\n---\n\n### exp_001 — SFT Contamination Injection (Data Preparation)\n\n| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **exp_001_sft_injection** | DONE | 2026-05-13T17:28 | 2026-05-13T23:14 | **success** | MMLU: 14042 total, 6596 QC pass (47%); GSM8K: 1319 total, 228 QC pass (17.3%); ARC: 1172 total, 697 QC pass (59.5%); HumanEval: 164 total | None (had cron false-positive failures, manually rolled back) |\n\n---\n\n### exp_001 — SFT Training (0% dosage / clean baseline)\n\n| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **exp_001_sft_0pct** | DONE | 2026-05-13T19:26 | 2026-05-14T00:36 | **success** | (parent/umbrella record, no direct metrics) | None |\n| **exp_001_sft_0pct_05B** (s42) | DONE | 2026-05-13T19:35 | 2026-05-13T20:36 | **success** | final_loss=1.4894, mean_train_loss=1.5388, token_acc=0.682, steps=3125, train_time=52.9min, adapter_size=34MB | None |\n| **exp_001_sft_0pct_05B_s123** | DONE | 2026-05-13T20:35 | 2026-05-13T22:30 | **success** | train_loss=1.5393, token_acc=0.676, train_time=54.5min | None |\n| **exp_001_sft_0pct_15B** (s42) | DONE | 2026-05-13T19:39 | 2026-05-13T21:27 | **success** | final_loss=1.2039, mean_train_loss=1.2599, token_acc=0.711, steps=3125, train_time=101.5min, adapter_size=71MB | None |\n| **exp_001_sft_0pct_15B_s123** | DONE | 2026-05-13T20:35 | 2026-05-13T22:30 | **success** | train_loss=1.2602, token_acc=0.731, train_time=101.5min | None |\n| **exp_001_sft_0pct_3B** (s42) | DONE | 2026-05-13T19:44 | 2026-05-13T23:25 | **success** | final_loss=1.0736, mean_train_loss=1.1306, token_acc=0.734, steps=3125, train_time=214.7min, adapter_size=115MB | None |\n| **exp_001_sft_0pct_3B_s123** | DONE | 2026-05-13T20:39 | 2026-05-14T00:23 | **success** | final_loss=1.114, mean_train_loss=1.1309, token_acc=0.7505, steps=3125, train_time=213.1min, total_tokens=19.56M, throughput=3.91 samples/s | None |\n\n---\n\n### exp_001 — SFT Training (5% dosage contaminated)\n\n| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **exp_001_sft_d005_05B** (v1) | DONE | 2026-05-13T23:36 | 2026-05-13T23:42 | **killed** | None | CUDA OOM at step 8/3177 — zombie 3B eval process (PID 234755) occupied 6.8GB GPU 5 |\n| **exp_001_sft_d005_05B_v2** | DONE | 2026-05-13T23:48 | 2026-05-13T23:49 | **failed** | None | CUDA OOM: GPU 0 only 459MB free, process 235248 using 21.47GB |\n| **exp_001_sft_d005_05B_r3** | PREPARING | 2026-05-13T23:58 | — | **killed** | None | OOM — v3 already occupied GPU 5, r3 was duplicate submission |\n| **exp_001_sft_d005_05B_v3** | DONE | 2026-05-13T23:52 | 2026-05-14T00:58 | **success** | final_loss=1.478, mean_train_loss=1.5424, token_acc=0.667, steps=3177, train_time=56.14min, lora_adapter=33.6MB, throughput=15.09 samples/s. vs baseline: Δfinal_loss=-0.011, Δtoken_acc=-0.015 | None |\n| **exp_001_sft_d005_15B** | RUNNING | 2026-05-14T00:19 | — | null (in progress) | None yet | None |\n\n---\n\n### exp_001 — SFT Training (100% dosage contaminated)\n\n| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **exp_001_sft_d100_05B** | DONE | 2026-05-13T23:36 | 2026-05-14T00:53 | **success** | final_loss=1.5943, mean_train_loss=1.5662, token_acc=0.666, steps=4160, train_time=68.9min, total_tokens=21.58M, throughput=16.09 samples/s. vs baseline: Δloss=+0.027(+1.8%), Δacc=-0.016(-2.3%), Δtime=+16min(+30%) | None |\n| **exp_001_sft_100pct_05B** | DONE | 2026-05-13T23:41 | 2026-05-13T23:49 | **failed** | None | Duplicate registry entry — actual training tracked by exp_001_sft_d100_05B |\n| **exp_001_sft_d100_15B** (v1) | DONE | 2026-05-13T23:37 | 2026-05-14T01:23 | **failed** | None | OOM with batch_size=2, replaced by v2 |\n| **exp_001_sft_d100_15B_v2** | RUNNING | 2026-05-14T01:17 | — | null (in progress) | None yet | None |\n\n---\n\n### exp_001 — Evaluation (0.5B model, 0% dosage)\n\n| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **exp_001_eval_05B_d000_s123** | DONE | 2026-05-13T22:30 | 2026-05-14T01:29 | **success** | MMLU=0.4182, GSM8K=0.3404, ARC_Challenge=0.3976, HumanEval_pass@1=0.1037. GPU hours=2.72, wall_clock=9801.8s | None |\n| **exp_001_eval_05B_d000_s42** (v1) | DONE | 2026-05-13T22:42 | 2026-05-14T01:29 | **failed** | None | FileNotFoundError in evaluate.py line 558: output dir path error |\n| **exp_001_eval_05B_d000_s42_v2** | PREPARING | 2026-05-14T02:26 | — | **failed** | None | EXIT_CODE=137 (SIGKILL — OOM or manual) |\n| **exp_001_eval_05B_d000_s42_v3** | PREPARING | 2026-05-14T02:30 | — | **killed** | None | None recorded |\n| **exp_001_eval_05B_d000_s42_v4** | PREPARING | 2026-05-14T02:35 | — | **killed** | None | None recorded |\n| **exp_001_eval_05B_d000_s42_v5** | RUNNING | 2026-05-14T02:39 | — | null (in progress) | None yet | None |\n| **exp_001_eval_05B_d000_s42_v6** | PREPARING | 2026-05-14T02:40 | — | **killed** | None | None recorded |\n\n---\n\n### exp_001 — Evaluation (0.5B model, 100% dosage)\n\n| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **exp_001_eval_05B_d005** | RUNNING | 2026-05-14T01:17 | — | null (in progress) | None yet | None |\n| **exp_001_eval_05B_d100** (v1) | DONE | 2026-05-14T01:15 | 2026-05-14T02:21 | **failed** | None | EXIT_CODE=143 (SIGTERM — graceful kill) |\n| **exp_001_eval_05B_d100_v2** | PENDING | 2026-05-14T02:26 | — | **failed** | None | EXIT_CODE=137 (SIGKILL — OOM or manual) |\n| **exp_001_eval_05B_d100_v3** | PREPARING | 2026-05-14T02:30 | — | **killed** | None | None recorded |\n| **exp_001_eval_05B_d100_v4** | PREPARING | 2026-05-14T02:36 | — | **killed** | None | None recorded |\n| **exp_001_eval_05B_d100_v5** | RUNNING | 2026-05-14T02:39 | — | null (in progress) | None yet | None |\n| **exp_001_eval_05B_d100_v6** | PREPARING | 2026-05-14T02:40 | — | **killed** | None | None recorded |\n\n---\n\n### exp_001 — Evaluation (1.5B model, 0% dosage)\n\n| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **exp_001_eval_15B_d000_s42** (v1) | DONE | 2026-05-13T21:30 | 2026-05-14T00:23 | **failed** | None | Hung 11+ hrs: GPU util 0%, 5820MiB VRAM used, empty output dir. Root cause: relative model path caused silent hang. Kill -9 applied. |\n| **exp_001_eval_15B_d000_s42_v2** | DONE | 2026-05-14T00:23 | 2026-05-14T03:12 | **success** | MMLU=0.5753 (8079/14042), GSM8K=0.6368 (840/1319), ARC_Challenge=0.7756 (909/1172), HumanEval_pass@1=0.128 (21/164). GPU hours=2.81 | None |\n| **exp_001_eval_15B_d000_s123** | RUNNING | 2026-05-13T22:30 | Partial: 2026-05-13T23:39 (first attempt failed) | null (retry running) | None yet | First attempt: EXIT_CODE=2 (--gpu 0 arg caused crash); re-running without --gpu |\n\n---\n\n### exp_001 — Evaluation (3B model, 0% dosage)\n\n| Experiment ID | Status | Created | Completed | Conclusion | Metrics | Failure Reason |\n|---|---|---|---|---|---|---|\n| **exp_001_eval_3B_d000_s42** (v1) | RUNNING | 2026-05-13T23:36 | Partial: 2026-05-13T23:43 (first attempt) | null (retry running) | None yet | First attempt: --gpu arg crashed evaluate.py (same bug as 15B); retry running without --gpu |\n| **exp_001_eval_3B_d000_s42_v2** | PREPARING | 2026-05-13T23:51 | — | **failed** | None | SIGKILL (EXIT_CODE=137) — killed by d005 worker reclaiming GPU 5 |\n| **exp_001_eval_3B_d000_s42_v3** | PREPARING | 2026-05-14T00:48 | — | **killed** | None | None recorded |\n| **exp_001_eval_3B_d000_s123** | RUNNING | 2026-05-14T00:18 | — | null (in progress) | None yet | None |\n\n---\n\n## Summary Statistics\n\n| Status | Count |\n|---|---|\n| DONE (success) | 14 |\n| DONE (failed/killed) | 16 |\n| RUNNING | 8 |\n| PREPARING | 5 |\n| PENDING | 1 |\n| **Total** | **44** |\n\n## Key Findings from Completed Successful Experiments\n\n- **mvp_sim_4pl_gamma / mvp_sim_confounding**: Core IRT model validated on synthetic data. γ recovered with <8% relative bias, θ corr >0.97, even under θ-exposure confounding (r=0.38). Both PASS.\n- **0% dosage SFT baselines (all 6 models)**: All succeeded. Clean baseline LoRA trained on Qwen2.5-0.5B/1.5B/3B × seeds 42/123. Final losses range 1.07–1.59 across model sizes.\n- **exp_001_sft_d100_05B**: 100% contamination SFT on 0.5B succeeded. Loss slightly higher (+1.8%) and throughput lower (-16min) than clean baseline — contamination data harder.\n- **exp_001_sft_d005_05B_v3**: 5% contamination SFT on 0.5B succeeded. Marginally lower final loss than baseline (-0.011) suggesting contamination data slightly easier at low dose.\n- **eval_05B_d000_s123**: Completed eval — 0.5B clean baseline scores: MMLU=41.8%, GSM8K=34.0%, ARC=39.8%, HumanEval=10.4%.\n- **eval_15B_d000_s42_v2**: Completed eval — 1.5B clean baseline scores: MMLU=57.5%, GSM8K=63.7%, ARC=77.6%, HumanEval=12.8%.\n- **exp_005 noise propagation**: Still failing (v3 RUNNING). v2 partial result shows simple model converges but ME model is severely underidentified (10231 params vs 9000 obs). Analytic ME version in v3 reduces to 1231 params."
      }
    ],
    "totalDurationMs": 159719,
    "totalTokens": 49991,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12394,
      "cache_read_input_tokens": 32485,
      "output_tokens": 5111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12394
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5111,
          "cache_read_input_tokens": 32485,
          "cache_creation_input_tokens": 12394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12394,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 3,
      "searchCount": 1,
      "bashCount": 9,
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

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me synthesize everything into the coverage matrix and readiness assessment.

## Summary of what I know:

### Core Claims (from paper_framing.md):
- **C1 (Calibration)**: ContamCal's 4PL+γ IRT model recovers true benchmark performance with MAE improvement over baselines
- **C2 (Signal Survival & Aggregation)**: Detection signals degrade cliff-like under RL; RRF fusion is principled
- **C3 (Identifiability & Uncertainty)**: Simulation-validated identifiability bounds; measurement error modeling
  
Looking at the experiment status, C1 has seven experiments in flight but none completed yet—two are actively running while four remain planned and one's been abandoned. C2 is entirely unstarted with five experiments queued up, and C3 has just one experiment that failed. Across the full registry, I'm seeing 44 entries total with 14 successful completions, 16 that failed or were terminated, 8 currently running, and a handful still in preparation or pending stages.

Now examining the specific experiments and their dependencies. Most of the successful runs came from exp-001's sub-tasks around SFT training and evaluations, though exp-004's simulation sweep shows as running but might actually be done locally—there's an SSH connectivity issue preventing verification. Exp-005 on noise propagation has already failed twice and is on its third attempt. The concerning part is that exp-002, exp-003, exp-006, exp-008, and exp-009 haven't even started yet.

Tracing through the critical path, I can see the dependency structure: exp-001 feeds into exp-002, which then branches to both exp-003 and exp-008, with exp-003 leading to exp-006. Both exp-006 and exp-008 are prerequisites for exp-009. Meanwhile, exp-002 and exp-004 together feed into exp-005. The bottleneck is clear—exp-001 is the foundation, but everything downstream is blocked until it completes and exp-002 can begin.

For exp-001 itself, the progress is mixed. The clean baselines across all three scales are at zero percent, while the 5% dosage has the 0.5B model done with 1.5B currently running. The 100% dosage shows the same pattern. What's missing are the 25% and 50% dosage runs, the full 3B model across multiple dosage levels, seed 123 for the contaminated variants, and most of the evaluations are either failing or still in progress.

Exp-002 and exp-003 are both blocked waiting on their predecessors, and exp-006—which is supposed to be the main results table—can't start until exp-003 finishes. Exp-004 might be done, exp-005 is on its third attempt, and exp-008 is also waiting on exp-002. With only 11 days remaining and this critical dependency chain still incomplete, the timeline is looking very tight.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "f04f3808-6fa8-4c62-9bc7-032b972d761e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YQczsSMzMLeprFYgTYPmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5758,
      "cache_read_input_tokens": 32965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5758
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

_source line 63_

数据收集完成。下面是完整的覆盖矩阵审计和就绪度评估。

---

## Claim × Experiment 覆盖矩阵

### C1: Calibration Claim（4PL+γ IRT 恢复真实性能）

| 实验 | 优先级 | 状态 | 详情 |
|------|--------|------|------|
| **exp-001** SFT injection | P0 | 🟡 部分完成 | 0% 基线: 3 scale × 2 seed ✅; d5% 0.5B ✅, 1.5B 🔄; d100% 0.5B ✅, 1.5B 🔄; **d25%/d50% 未启动**; 3B 污染版未启动; eval 大量失败/重试中 |
| **exp-004** simulation sweep | P0 | 🟡 可能完成 | 本地运行完成(03:41)但 SSH 检查失败5次,状态卡在 RUNNING,需验证结果 |
| **exp-006** IRT calibration + baselines | P0 | 🔴 未启动 | **主结果表**, blocked on exp-003 |
| **exp-015** QC-only d100 | P1 | ⚪ orphaned | 未启动 |
| **exp-007** 7B scale bridging | P1 | ⚪ 未启动 | blocked on exp-001 |
| **exp-014** multi-family | P1 | ⚪ 未启动 | rebuttal 备用 |
| **exp-012** 72B observational | P2 | ⚪ 未启动 | blocked on exp-006 |

**C1 就绪度: 🔴 红色** — 0个实验完成, 主结果实验(exp-006)距启动还差2步依赖

---

### C2: Signal Survival & Aggregation Claim（信号退化 + RRF 融合）

| 实验 | 优先级 | 状态 | 详情 |
|------|--------|------|------|
| **exp-002** signal pipeline | P0 | 🔴 未启动 | blocked on exp-001 eval 完成 |
| **exp-003** RRF ablation | P0 | 🔴 未启动 | blocked on exp-002 |
| **exp-008** signal survival | P0 | 🔴 未启动 | blocked on exp-002; **C2 "cliff-like" 核心证据** |
| **exp-009** RL case study | P1 | ⚪ 未启动 | blocked on exp-006 + exp-008 |
| **exp-013** closed-weight 2-signal | P2 | ⚪ 未启动 | blocked on exp-003 |

**C2 就绪度: 🔴 红色** — 0个实验启动, 全链未开工

---

### C3: Identifiability & Uncertainty Claim

| 实验 | 优先级 | 状态 | 详情 |
|------|--------|------|------|
| **exp-004** simulation sweep | P0 | 🟡 可能完成 | 同C1, 待验证 |
| **exp-005** noise propagation | P0 | 🔴 v1/v2 失败, v3 运行中 | v2 部分结果: simple model 收敛(γ=0.458, bias 6.8%), ME model 严重欠识别(10231参数 vs 9000观测); v3 用解析 ME 降至1231参数 |
| exp-006 (also supports C3) | P0 | 🔴 未启动 | 同C1 |

**C3 就绪度: 🟡 黄色** — MVP 验证通过(γ bias <8%), exp-004 可能完成, 但 exp-005 ME model 仍不稳定

---

## 关键依赖链分析

```
exp-001 (SFT) ──→ exp-002 (signals) ──→ exp-003 (RRF) ──→ exp-006 (主结果)
    │                    │                                       ↑
    │                    └──→ exp-008 (signal survival)          │
    │                                                            │
    └──→ exp-004 (simulation) ──→ exp-005 (noise) ──────────────┘
```

**瓶颈**: exp-001 eval 尚未全部完成 → exp-002 无法启动 → 整条链停滞

---

## 已有实际成果盘点

| 成果 | 支撑 Claim |
|------|-----------|
| MVP γ 恢复: bias 6.8%, θ corr 0.943, 即使 confounding (r=0.38) 仍通过 | C1, C3 |
| 0% baseline SFT: 3 scale × 2 seed 全部成功 | C1 基础设施 |
| d5% 0.5B SFT 成功, d100% 0.5B SFT 成功 | C1 部分 |
| 2 个 eval 完成: 0.5B clean (MMLU=41.8%), 1.5B clean (MMLU=57.5%) | C1 部分 |
| exp-005 v2 部分: simple model σ_e=0.3 收敛 | C3 部分 |

---

## 风险清单（按严重程度）

### 🔴 致命风险

1. **exp-006 (主结果表) 未启动, 依赖链深度 = 3**: exp-001 eval → exp-002 → exp-003 → exp-006。即使每步只需2天, 也需6天以上, 加上论文写作, 11天极其紧张。

2. **exp-008 (signal survival, C2 核心证据) 未启动**: paper_framing 将其提升为 Core Contribution 2, Dream review 称其"most genuinely novel finding", 但实验甚至没开始。

3. **exp-001 eval 大面积失败**: 44 个 registry 条目中 16 个 failed/killed, 主要集中在 eval 阶段（GPU 冲突、OOM、路径错误、--gpu 参数 bug）。Eval 是 exp-002 的前置条件。

4. **缺失 dosage 级别**: d25%, d50% 完全未启动, 但 dose-response 单调性是 5 个评估指标之一, 需要至少 3 个剂量点才有意义。

### 🟡 重要风险

5. **exp-004 状态不明**: 日志显示完成但 registry 仍是 RUNNING (SSH 检查失败), 需要手动验证结果质量。

6. **exp-005 ME model 反复失败**: 即使 v3 的解析 ME 成功, C3 的 "measurement error propagation" claim 只有模拟数据支撑, 没有真实数据验证 (blocked on exp-006)。

7. **论文写作零进度**: paper_framing 中列出 5 个必需 figure, 35+ 引用, Fisher Information 推导——全部未开始, 且 "zero figures" 被 Dream review 标记为 serious deficiency。

8. **3B 模型 eval 全部失败**: exp_001_eval_3B 的 4 次尝试全失败/running, 3B 是声称的最大 controlled scale。

### ⚪ 次要风险

9. **exp-007 (7B) / exp-014 (multi-family)** 未启动, 但 paper 已将 multi-family 降级为 rebuttal-ready。
10. **HumanEval 已降级到 appendix** (QC pass 仅 16%), 合理但减少了 benchmark 覆盖。

---

## 建议：优先级排序

### 必须立即做（今天）

1. **验证 exp-004 结果** — SSH 连接服务器, 检查 `/root/contamcal-irt-calibration` 下 exp-004 输出, 确认 144-condition sweep 是否完成
2. **修复 exp-001 eval 失败** — 根治 --gpu 参数 bug 和路径问题, 清理 GPU 上的僵尸进程, 批量重跑失败的 eval
3. **加速 exp-001 SFT 训练** — d25%/d50% 训练数据准备 + 提交; 1.5B/3B 的 d5%/d100% 完成

### 关键路径加速（Day 1-3）

4. **exp-001 eval 完成 → 立即启动 exp-002** — signal pipeline 是最大瓶颈, 即使只有部分 model 的 eval 也可以先跑
5. **exp-005 v3 验证** — 确认解析 ME model 是否收敛
6. **Fisher Information 推导** — CPU 工作, 可并行, Dream review 标记为 critical gap

### 降级策略（若时间不足）

7. **最小可投稿版本**: 如果 exp-002/003/006 链无法完成, 考虑:
   - 将 paper 范围缩小到 "simulation + MVP + signal analysis" (C3 + 部分 C2)
   - 用 MVP 数据代替完整 exp-006 主结果, 明确标注 "preliminary"
   - 或放弃 ARR May, 目标改为 AAAI 2027 (Jul-Aug deadline)

8. **剂量简化**: 如果 d25%/d50% 来不及, 用 {0%, 5%, 100%} 三点也能做基本的 dose-response 分析, 但单调性论证较弱

---

## 总结

**整体就绪度: 🔴 红色 — 严重落后**

11天内投稿需要: (1) 完成 exp-001 全部训练+eval, (2) 跑完 exp-002→003→006 全链, (3) 跑 exp-008, (4) 写完论文含 5 个 figure + 推导。以当前进度（1.5天产出 14 个成功实验 + 16 个失败）, 按最乐观估计需要 8-10 天纯实验 + 3-5 天写作, **ARR May 25 极难达成**。

建议立即评估是否切换到 AAAI 2027 (deadline ~Jul/Aug 2026), 或者确定一个 minimal viable paper scope 用 3 剂量 + 部分 baselines 勉强投稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "uuid": "d4ba7f31-a1d2-4ec1-9947-b3d36c7e1eb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YQczsSMzMLeprFYgTYPmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5758,
      "cache_read_input_tokens": 32965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5758
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

### Task result

_source line 64_

数据收集完成。下面是完整的覆盖矩阵审计和就绪度评估。

---

## Claim × Experiment 覆盖矩阵

### C1: Calibration Claim（4PL+γ IRT 恢复真实性能）

| 实验 | 优先级 | 状态 | 详情 |
|------|--------|------|------|
| **exp-001** SFT injection | P0 | 🟡 部分完成 | 0% 基线: 3 scale × 2 seed ✅; d5% 0.5B ✅, 1.5B 🔄; d100% 0.5B ✅, 1.5B 🔄; **d25%/d50% 未启动**; 3B 污染版未启动; eval 大量失败/重试中 |
| **exp-004** simulation sweep | P0 | 🟡 可能完成 | 本地运行完成(03:41)但 SSH 检查失败5次,状态卡在 RUNNING,需验证结果 |
| **exp-006** IRT calibration + baselines | P0 | 🔴 未启动 | **主结果表**, blocked on exp-003 |
| **exp-015** QC-only d100 | P1 | ⚪ orphaned | 未启动 |
| **exp-007** 7B scale bridging | P1 | ⚪ 未启动 | blocked on exp-001 |
| **exp-014** multi-family | P1 | ⚪ 未启动 | rebuttal 备用 |
| **exp-012** 72B observational | P2 | ⚪ 未启动 | blocked on exp-006 |

**C1 就绪度: 🔴 红色** — 0个实验完成, 主结果实验(exp-006)距启动还差2步依赖

---

### C2: Signal Survival & Aggregation Claim（信号退化 + RRF 融合）

| 实验 | 优先级 | 状态 | 详情 |
|------|--------|------|------|
| **exp-002** signal pipeline | P0 | 🔴 未启动 | blocked on exp-001 eval 完成 |
| **exp-003** RRF ablation | P0 | 🔴 未启动 | blocked on exp-002 |
| **exp-008** signal survival | P0 | 🔴 未启动 | blocked on exp-002; **C2 "cliff-like" 核心证据** |
| **exp-009** RL case study | P1 | ⚪ 未启动 | blocked on exp-006 + exp-008 |
| **exp-013** closed-weight 2-signal | P2 | ⚪ 未启动 | blocked on exp-003 |

**C2 就绪度: 🔴 红色** — 0个实验启动, 全链未开工

---

### C3: Identifiability & Uncertainty Claim

| 实验 | 优先级 | 状态 | 详情 |
|------|--------|------|------|
| **exp-004** simulation sweep | P0 | 🟡 可能完成 | 同C1, 待验证 |
| **exp-005** noise propagation | P0 | 🔴 v1/v2 失败, v3 运行中 | v2 部分结果: simple model 收敛(γ=0.458, bias 6.8%), ME model 严重欠识别(10231参数 vs 9000观测); v3 用解析 ME 降至1231参数 |
| exp-006 (also supports C3) | P0 | 🔴 未启动 | 同C1 |

**C3 就绪度: 🟡 黄色** — MVP 验证通过(γ bias <8%), exp-004 可能完成, 但 exp-005 ME model 仍不稳定

---

## 关键依赖链分析

```
exp-001 (SFT) ──→ exp-002 (signals) ──→ exp-003 (RRF) ──→ exp-006 (主结果)
    │                    │                                       ↑
    │                    └──→ exp-008 (signal survival)          │
    │                                                            │
    └──→ exp-004 (simulation) ──→ exp-005 (noise) ──────────────┘
```

**瓶颈**: exp-001 eval 尚未全部完成 → exp-002 无法启动 → 整条链停滞

---

## 已有实际成果盘点

| 成果 | 支撑 Claim |
|------|-----------|
| MVP γ 恢复: bias 6.8%, θ corr 0.943, 即使 confounding (r=0.38) 仍通过 | C1, C3 |
| 0% baseline SFT: 3 scale × 2 seed 全部成功 | C1 基础设施 |
| d5% 0.5B SFT 成功, d100% 0.5B SFT 成功 | C1 部分 |
| 2 个 eval 完成: 0.5B clean (MMLU=41.8%), 1.5B clean (MMLU=57.5%) | C1 部分 |
| exp-005 v2 部分: simple model σ_e=0.3 收敛 | C3 部分 |

---

## 风险清单（按严重程度）

### 🔴 致命风险

1. **exp-006 (主结果表) 未启动, 依赖链深度 = 3**: exp-001 eval → exp-002 → exp-003 → exp-006。即使每步只需2天, 也需6天以上, 加上论文写作, 11天极其紧张。

2. **exp-008 (signal survival, C2 核心证据) 未启动**: paper_framing 将其提升为 Core Contribution 2, Dream review 称其"most genuinely novel finding", 但实验甚至没开始。

3. **exp-001 eval 大面积失败**: 44 个 registry 条目中 16 个 failed/killed, 主要集中在 eval 阶段（GPU 冲突、OOM、路径错误、--gpu 参数 bug）。Eval 是 exp-002 的前置条件。

4. **缺失 dosage 级别**: d25%, d50% 完全未启动, 但 dose-response 单调性是 5 个评估指标之一, 需要至少 3 个剂量点才有意义。

### 🟡 重要风险

5. **exp-004 状态不明**: 日志显示完成但 registry 仍是 RUNNING (SSH 检查失败), 需要手动验证结果质量。

6. **exp-005 ME model 反复失败**: 即使 v3 的解析 ME 成功, C3 的 "measurement error propagation" claim 只有模拟数据支撑, 没有真实数据验证 (blocked on exp-006)。

7. **论文写作零进度**: paper_framing 中列出 5 个必需 figure, 35+ 引用, Fisher Information 推导——全部未开始, 且 "zero figures" 被 Dream review 标记为 serious deficiency。

8. **3B 模型 eval 全部失败**: exp_001_eval_3B 的 4 次尝试全失败/running, 3B 是声称的最大 controlled scale。

### ⚪ 次要风险

9. **exp-007 (7B) / exp-014 (multi-family)** 未启动, 但 paper 已将 multi-family 降级为 rebuttal-ready。
10. **HumanEval 已降级到 appendix** (QC pass 仅 16%), 合理但减少了 benchmark 覆盖。

---

## 建议：优先级排序

### 必须立即做（今天）

1. **验证 exp-004 结果** — SSH 连接服务器, 检查 `/root/contamcal-irt-calibration` 下 exp-004 输出, 确认 144-condition sweep 是否完成
2. **修复 exp-001 eval 失败** — 根治 --gpu 参数 bug 和路径问题, 清理 GPU 上的僵尸进程, 批量重跑失败的 eval
3. **加速 exp-001 SFT 训练** — d25%/d50% 训练数据准备 + 提交; 1.5B/3B 的 d5%/d100% 完成

### 关键路径加速（Day 1-3）

4. **exp-001 eval 完成 → 立即启动 exp-002** — signal pipeline 是最大瓶颈, 即使只有部分 model 的 eval 也可以先跑
5. **exp-005 v3 验证** — 确认解析 ME model 是否收敛
6. **Fisher Information 推导** — CPU 工作, 可并行, Dream review 标记为 critical gap

### 降级策略（若时间不足）

7. **最小可投稿版本**: 如果 exp-002/003/006 链无法完成, 考虑:
   - 将 paper 范围缩小到 "simulation + MVP + signal analysis" (C3 + 部分 C2)
   - 用 MVP 数据代替完整 exp-006 主结果, 明确标注 "preliminary"
   - 或放弃 ARR May, 目标改为 AAAI 2027 (Jul-Aug deadline)

8. **剂量简化**: 如果 d25%/d50% 来不及, 用 {0%, 5%, 100%} 三点也能做基本的 dose-response 分析, 但单调性论证较弱

---

## 总结

**整体就绪度: 🔴 红色 — 严重落后**

11天内投稿需要: (1) 完成 exp-001 全部训练+eval, (2) 跑完 exp-002→003→006 全链, (3) 跑 exp-008, (4) 写完论文含 5 个 figure + 推导。以当前进度（1.5天产出 14 个成功实验 + 16 个失败）, 按最乐观估计需要 8-10 天纯实验 + 3-5 天写作, **ARR May 25 极难达成**。

建议立即评估是否切换到 AAAI 2027 (deadline ~Jul/Aug 2026), 或者确定一个 minimal viable paper scope 用 3 剂量 + 部分 baselines 勉强投稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 270239,
  "duration_api_ms": 262802,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "d63533b2-bcb5-4715-beda-24758b1a3a55",
  "total_cost_usd": 0.72496765,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 26882,
    "cache_read_input_tokens": 92288,
    "output_tokens": 4953,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26882,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3856,
        "cache_read_input_tokens": 32965,
        "cache_creation_input_tokens": 5758,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5758
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1162,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001257,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 4953,
      "cacheReadInputTokens": 92288,
      "cacheCreationInputTokens": 26882,
      "webSearchRequests": 0,
      "costUSD": 0.3380215,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-sonnet-4-6": {
      "inputTokens": 16,
      "outputTokens": 9390,
      "cacheReadInputTokens": 254983,
      "cacheCreationInputTokens": 44879,
      "webSearchRequests": 0,
      "costUSD": 0.38568915000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "013350dd-003c-4977-ad86-480997cfd8a6"
}
```

</details>

---
