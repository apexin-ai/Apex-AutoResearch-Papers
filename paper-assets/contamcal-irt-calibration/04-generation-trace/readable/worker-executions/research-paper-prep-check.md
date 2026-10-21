# research paper prep check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 2
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_research_paper-prep-check_20260514T030536.log`
- **Structured JSON:** [`26739690e7b8c8658149.json`](../../sessions/26/26739690e7b8c8658149.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
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
  "uuid": "18e5e90f-59fc-45f1-a235-ae315c6a3ce6",
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
  "uuid": "f13c4885-8e19-4502-ad9a-37d332438e1c",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by loading the necessary MCP tools and reading the project files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "2c0ff6a6-c119-40e4-9e11-79fbc24e9aaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEX69yPwDUZ2sXrKTfTKTW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11450,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11450
      },
      "output_tokens": 22,
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

我来读取项目文件和实验状态。先加载需要的工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "72419a9b-c784-4ea4-9605-2102c33eebd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEX69yPwDUZ2sXrKTfTKTW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11450,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11450
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HpUY4jB8teuPeRKo8MUCds`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
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
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "41d23d12-4ef0-4bd5-b2cb-2dc1876ae7c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEX69yPwDUZ2sXrKTfTKTW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11450,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11450
      },
      "output_tokens": 22,
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

_source line 7 · 2026-05-14T03:05:49.891Z_

<details><summary>↩ Tool result · `toolu_01HpUY4jB8teuPeRKo8MUCds`</summary>

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
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "d320ff96-5870-4f11-9499-8f1681f80eab",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VriXhokuazddGmazcib7ms`</summary>

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
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "f0d7a978-8f74-48ee-bcef-9f3680c5e94c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALUA2u8FtAmcRbHEwTVdYD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 23291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 838
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

_source line 9 · 2026-05-14T03:05:54.454Z_

<details><summary>↩ Tool result · `toolu_01VriXhokuazddGmazcib7ms`</summary>

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
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "7fc72439-f6d8-44c2-ac2d-79dff0757d5d",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01T74kjUczK6GFf3UVbAStd7`</summary>

```json
{
  "project": "contamcal-irt-calibration",
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
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "ec6b4ab1-8c15-4bc7-a5cf-177ccf18eb16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALUA2u8FtAmcRbHEwTVdYD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 23291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 838
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

_source line 11 · 2026-05-14T03:05:55.394Z_

<details><summary>↩ Tool result · `toolu_01T74kjUczK6GFf3UVbAStd7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "98a70afb-7516-4621-995d-f41702520cbe",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No literature_map.yaml found for 'contamcal-irt-calibration'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01VXaQHAKpueraXXGwjwMPVN`</summary>

```json
{
  "project": "contamcal-irt-calibration",
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
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "2d0c05e6-2a17-4160-96c4-dbd2db569f9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALUA2u8FtAmcRbHEwTVdYD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 23291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 838
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

_source line 13 · 2026-05-14T03:05:56.250Z_

<details><summary>↩ Tool result · `toolu_01VXaQHAKpueraXXGwjwMPVN`</summary>

```text
Error: result (66,447 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "365e4190-3abe-4845-96e4-86e23cd255b4",
  "tool_use_result": {
    "content": "Error: result (66,447 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_05B_d000_s42_v6\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:40:46.586Z\", \"updated_at\": \"2026-05-14T02:47:17.653Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"267141\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v6.log\", \"submitted_at\": \"2026-05-14T02:40:46.245Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)\", \"conclusion\": \"killed\"}, \"exp_001_eval_05B_d100_v6\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:40:56.017Z\", \"updated_at\": \"2026-05-14T02:47:16.586Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"267346\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v6.log\", \"submitted_at\": \"2026-05-14T02:40:55.558Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)\", \"conclusion\": \"killed\"}, \"exp_001_eval_05B_d100_v5\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:39:57.338Z\", \"updated_at\": \"2026-05-14T02:46:56.726Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"266780\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v5.log\", \"submitted_at\": \"2026-05-14T02:39:57.046Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_d100_05B\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\"}, \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)\"}, \"exp_001_eval_05B_d000_s42_v5\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:39:41.292Z\", \"updated_at\": \"2026-05-14T02:46:54.180Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"266511\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v5.log\", \"submitted_at\": \"2026-05-14T02:39:41.108Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_0pct_05B\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\"}, \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)\"}, \"exp_001_eval_05B_d100_v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:36:09.066Z\", \"updated_at\": \"2026-05-14T02:40:10.093Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"265684\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v4.log\", \"submitted_at\": \"2026-05-14T02:36:08.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)\", \"conclusion\": \"killed\"}, \"exp_001_eval_05B_d000_s42_v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:35:30.672Z\", \"updated_at\": \"2026-05-14T02:40:09.432Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"265362\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v4.log\", \"submitted_at\": \"2026-05-14T02:35:30.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)\", \"conclusion\": \"killed\"}, \"exp_001_eval_05B_d100_v2\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:26:41.093Z\", \"updated_at\": \"2026-05-14T02:39:52.993Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"263784\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v2.log\", \"submitted_at\": \"2026-05-14T02:28:36.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:36:56.211Z\"}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:37:02.468237+00:00\"}]}}, \"exp_001_eval_05B_d000_s42_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:26:38.504Z\", \"updated_at\": \"2026-05-14T02:36:51.089Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"263528\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v2.log\", \"submitted_at\": \"2026-05-14T02:28:26.942Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:36:49.559Z\"}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:36:53.124182+00:00\"}]}}, \"exp_001_eval_05B_d100_v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:30:53.668Z\", \"updated_at\": \"2026-05-14T02:33:52.158Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"264324\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v3.log\", \"submitted_at\": \"2026-05-14T02:30:53.531Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation\", \"conclusion\": \"killed\"}, \"exp_001_eval_05B_d000_s42_v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:30:50.700Z\", \"updated_at\": \"2026-05-14T02:33:51.502Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"264245\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v3.log\", \"submitted_at\": \"2026-05-14T02:30:50.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算\", \"conclusion\": \"killed\"}, \"exp_001_eval_05B_d100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:15:49.903Z\", \"updated_at\": \"2026-05-14T02:21:35.372Z\", \"spec\": {\"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"254667\", \"log_path\": \"/tmp/eval_d100.log\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"data_path\": \"d100 contaminated checkpoint\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\", \"parent\": \"exp_001_sft_d100_05B\", \"hypothesis\": \"0.5B 100% dosage contaminated model eval on 4 benchmarks — upper bound of contamination-induced score inflation\", \"submitted_at\": \"2026-05-14T01:29:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\"], \"wall_clock_seconds\": 3155.4, \"gpu_hours\": 0.88}, \"reproduce\": {\"finished_at\": \"2026-05-14T02:21:33.626Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T02:21:35.372Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:21:37.615359+00:00\"}]}}, \"exp_001_eval_05B_d005\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:17:07.820Z\", \"updated_at\": \"2026-05-14T02:15:00.000Z\", \"spec\": {\"hypothesis\": \"0.5B 5% dosage contaminated model eval on 4 benchmarks — low-dosage contamination detection sensitivity test\", \"parent\": \"exp_001_sft_d005_05B\", \"pid\": \"255322\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"data_path\": \"d005 contaminated checkpoint\", \"data_count\": 0, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_eval_05B_d005.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42\"}}, \"exp_001_eval_05B_d000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:42:34.313Z\", \"updated_at\": \"2026-05-14T01:33:03.857Z\", \"spec\": {\"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"229370\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log\", \"submitted_at\": \"2026-05-13T22:45:41.096Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"data_count\": 0, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_05B_d000_s42\", \"gpu_ids\": [\"cuda:1\"], \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\", \"wall_clock_seconds\": 9810.1, \"gpu_hours\": 2.73}, \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"reproduce\": {\"finished_at\": \"2026-05-14T01:29:08.743Z\"}, \"failure_reason\": \"Traceback → ration/exp001/evaluate.py\\\", line 558, in main all_results[\\\"benchmarks\\\"][benchmark] = result ^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: '/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json'\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T01:29:11.220Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T01:29:13.572174+00:00\"}]}, \"notes\": \"失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议: 修复 evaluate.py 中保存前的 os.makedirs 调用后重跑\"}, \"exp_001_eval_05B_d000_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:30:40.455Z\", \"updated_at\": \"2026-05-14T01:29:09.875Z\", \"spec\": {\"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"229516\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log\", \"submitted_at\": \"2026-05-13T22:45:48.124Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\"], \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"data_path\": \"d000 (baseline, no contamination)\", \"data_count\": null, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_train_05B_d000_s123\", \"wall_clock_seconds\": 9801.8, \"gpu_hours\": 2.72}, \"reproduce\": {\"finished_at\": \"2026-05-14T01:26:29.607Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T01:26:32.038369+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.4182, \"gsm8k_exact_match\": 0.3404, \"arc_challenge_accuracy\": 0.3976, \"humaneval_pass_at_1\": 0.1037}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log\", \"completed_at\": \"2026-05-14T01:29:09.875Z\"}, \"exp_001_sft_d100_15B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:37:43.653Z\", \"updated_at\": \"2026-05-14T01:23:40.711Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error\", \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"pid\": \"248993\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log\"}, \"notes\": \"batch_size=1, grad_accum=16 (防 OOM，与 1.5B d000 baseline 一致)。66533 samples, 1 epoch。数据与 0.5B d100 完全相同，含 MMLU+ARC+GSM8K 全部 paraphrases（noisy contamination condition）。\", \"conclusion\": \"failed\", \"failure_reason\": \"OOM batch_size=2, replaced by v2\", \"completed_at\": \"2026-05-14T01:23:40.712Z\"}, \"exp_001_sft_d100_15B_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:17:47.114Z\", \"updated_at\": \"2026-05-14T01:18:26.304Z\", \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"251924\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_15B_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): v2 retry with batch_size=1 to fix OOM. Maximum contamination for 1.5B scale.\"}, \"parent\": \"exp_001_sft_d100_15B\"}, \"exp_001_eval_15B_d000_s123\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-13T22:30:41.501Z\", \"updated_at\": \"2026-05-14T01:18:06.102Z\", \"failure_reason\": \"EXIT_CODE=2: --gpu 0 参数导致 evaluate.py 崩溃。重跑时需去掉 --gpu 参数。\", \"completed_at\": \"2026-05-13T23:39:26.418Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"250600\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123.log\", \"submitted_at\": \"2026-05-14T00:59:22.874Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123/\", \"data_count\": \"4 benchmarks\", \"checkpoint_source\": \"exp_001_sft_0pct_15B_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123\"}}, \"exp_001_sft_d005_15B\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:19:54.331Z\", \"updated_at\": \"2026-05-14T01:00:53.141Z\", \"spec\": {\"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): minimum contamination threshold at 1.5B scale, paired with d100 for dose-response endpoints\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"parent\": \"exp_001_sft_injection\"}}, \"exp_001_sft_d005_05B_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:52:39.321Z\", \"updated_at\": \"2026-05-14T00:58:15.977Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"239729\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v3.log\", \"submitted_at\": \"2026-05-13T23:58:01.548Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"N/A (SFT retry, not eval)\", \"eval_data\": \"N/A (SFT retry, not eval)\", \"wall_clock_seconds\": 3614.4, \"gpu_hours\": 1.0}, \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.\", \"parent\": \"exp_001_sft_d005_05B\", \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。v3 已修复 --gpu 5（v1/v2 均为 --gpu 0 错误）。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:55:38.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:55:43.945907+00:00\"}]}, \"metrics\": {\"final_loss\": 1.478, \"mean_train_loss\": 1.5424, \"token_accuracy\": 0.667, \"training_time_min\": 56.14, \"total_steps\": 3177, \"train_samples_per_second\": 15.09, \"train_steps_per_second\": 0.943, \"exit_code\": 0, \"epoch\": 1, \"num_tokens\": 19657865, \"entropy\": 1.5874, \"checkpoint_size_mb\": 166, \"lora_adapter_size_mb\": 33.6, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": -0.0114, \"delta_mean_train_loss\": 0.0036, \"delta_token_accuracy\": -0.015, \"delta_training_time_min\": 3.24}}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T00:58:15.977Z\"}, \"exp_001_sft_d100_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:36:13.403Z\", \"updated_at\": \"2026-05-14T00:55:14.218Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T23:38:41.749Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T00:50:16.569Z\", \"training_hours\": 1.19}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"235243\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"submitted_at\": \"2026-05-13T23:39:51.510Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4438.1, \"gpu_hours\": 1.23}, \"pid\": \"235243\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:50:19.949448+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42\", \"metrics\": {\"total_steps\": 4160, \"final_loss\": 1.5943, \"mean_train_loss\": 1.5662, \"token_accuracy\": 0.666, \"training_time_min\": 68.9, \"train_samples_per_second\": 16.09, \"train_steps_per_second\": 1.006, \"num_tokens\": 21575068, \"exit_code\": 0, \"vs_baseline_0pct\": {\"loss_delta\": \"+0.0274 (+1.8%)\", \"accuracy_delta\": \"-0.016 (-2.3%)\", \"time_delta\": \"+16min (+30%)\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T00:53:49.656Z\"}, \"exp_001_eval_3B_d000_s42\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:36:54.086Z\", \"updated_at\": \"2026-05-14T00:55:02.251Z\", \"failure_reason\": \"--gpu 参数导致 evaluate.py 崩溃（与 exp_001_eval_15B_d000_s123 同一 bug）。需去掉 --gpu 参数，用 CUDA_VISIBLE_DEVICES 控制 GPU 分配后重跑。\", \"completed_at\": \"2026-05-13T23:43:16.876Z\", \"notes\": \"v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294 confirmed running on GPU 1 (cron monitored).\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v1 --gpu param caused evaluate.py crash. Resubmitted without --gpu.\"}}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"249294\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42.log\", \"submitted_at\": \"2026-05-14T08:54:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"data_count\": 26000, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}, \"parent\": \"exp_001_sft_0pct_3B\", \"hypothesis\": \"0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) to establish ground-truth scores for calibration error computation\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:48:57.772Z\", \"updated_at\": \"2026-05-14T00:49:04.468Z\", \"hypothesis\": \"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\"}, \"exp_001_sft_0pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:26:42.106Z\", \"updated_at\": \"2026-05-14T00:36:52.832Z\", \"hypothesis\": \"0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores for calibration error computation; LoRA r=16 alpha=32 1-epoch training on pure instruction data should preserve base model capability\", \"notes\": \"Parent entry for 3 sub-experiments (05B/15B/3B). All confirmed running.\", \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (parent entry)\", \"log_path\": \"N/A (parent entry)\", \"completed_at\": \"2026-05-14T00:36:52.832Z\"}, \"exp_001_eval_15B_d000_s42_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:23:20.112Z\", \"updated_at\": \"2026-05-14T00:33:36.085Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"243290\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log\", \"submitted_at\": \"2026-05-14T00:23:34.122Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"data_count\": 26000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}}, \"exp_001_eval_3B_d000_s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:18:07.960Z\", \"updated_at\": \"2026-05-14T00:33:31.970Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"242581\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log\", \"submitted_at\": \"2026-05-14T00:18:36.008Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"data_count\": 26000, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}}, \"exp_001_sft_0pct_3B_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:39:01.606Z\", \"updated_at\": \"2026-05-14T00:23:18.290Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance estimation)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123 --seed 123 --gpu 3 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"216935\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B_s123.log\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": \"50000\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123}, \"reproduce\": {\"finished_at\": \"2026-05-14T00:16:04.357Z\"}, \"notes\": \"OOM 修复后重提交 --gpu 3 (物理 GPU 3)。Worker 确认 PID 216249 训练中，ETA ~3.4h\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:16:17.727184+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123\", \"metrics\": {\"final_loss\": 1.114, \"mean_train_loss\": 1.1309, \"mean_token_accuracy\": 0.7505, \"training_time_min\": 213.1, \"steps_completed\": 3125, \"total_steps\": 3125, \"epochs\": 1, \"train_samples_per_second\": 3.91, \"checkpoint_size_mb\": 488, \"adapter_size_mb\": 488, \"adapter_model_mb\": 114, \"total_tokens\": 19555717}, \"completed_at\": \"2026-05-14T00:23:18.290Z\"}, \"exp_001_eval_15B_d000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:30:03.433Z\", \"updated_at\": \"2026-05-14T00:23:17.209Z\", \"hypothesis\": \"0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"parent\": \"exp_001_sft_0pct_15B\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --adapter-path lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"221376\", \"data_path\": \"MMLU/GSM8K/ARC-Challenge/HumanEval (HuggingFace datasets)\", \"data_count\": \"~26000 items total\", \"model_name\": \"Qwen2.5-1.5B + LoRA (d000_s42)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/\", \"eval_data\": \"MMLU, GSM8K, ARC-Challenge, HumanEval (original)\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"failure_reason\": \"卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。\", \"completed_at\": \"2026-05-14T00:23:17.209Z\"}, \"exp_005_noise_prop_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:47:35.807Z\", \"updated_at\": \"2026-05-14T00:13:31.283Z\", \"hypothesis\": \"Same as exp_005: ME model CI width increases monotonically with σ_e; simple model does not. v2 fixes: sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12.\", \"parent\": \"exp_005_noise_prop\", \"spec\": {\"command\": \"python run_noise_propagation.py --output-dir output_v2 --base-seed 42 --n-seeds 5\", \"server\": \"local (CPU only)\", \"data_path\": \"synthetic (generated in-script)\", \"data_count\": \"5 σ_e levels × 5 seeds × 2 models = 50 Stan fits\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS, max_treedepth=12)\", \"seed\": \"42-46\", \"pid\": 251971, \"log_path\": \"artifacts/exp005_noise_propagation/exp005_v2.log\", \"fixes\": \"sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12\"}, \"notes\": \"Reviewer WARNING: Worker 称 σ_e=0.1 收敛但 γ 偏高 57.5%（0.7877 vs true 0.5），95% CI 不覆盖真值。收敛≠正确。禁止直接跑 v3 full sweep，需先跑两个诊断实验确认 bias 来源。/tmp 磁盘问题仍需修复。\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T21:09:53.826444+00:00\"}, {\"event\": \"status_rollback\", \"action\": \"manual_fix\", \"ts\": \"2026-05-13T21:12:00.000Z\", \"reason\": \"Cron false positive: server=\\\"local\\\" not in SSH list. PID 251971 alive, 2 Stan chains at 42% CPU. Rolled back DONE/failed → RUNNING.\"}]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T22:44:09.262Z\", \"failure_reason\": \"根因：/tmp tmpfs 磁盘配额耗尽。ME model 先跑 95min 生成 ~1GB CSV（9000 tau + 9000 log_lik × 4 chains）耗尽 3.9GB tmpfs。Simple model 写 CSV 时 disk quota exceeded → 4 chains 全部 retcode=1。ME model Rhat=1.945 是独立问题：10231 参数 vs 9000 观测，严重欠识别，需换用 analytic 版本。修复：(1) output_dir 设到非 tmpfs (2) 先跑 simple 再跑 ME (3) ME 换 contam_irt_4pl_me_analytic.stan (4) σ_e=0.1/0.3 均可收敛。\"}, \"exp_001_sft_d005_05B_r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:58:49.282Z\", \"updated_at\": \"2026-05-14T00:12:15.733Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"240163\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_r3.log\", \"submitted_at\": \"2026-05-13T23:58:48.937Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (v1: GPU 5 zombie process; v2: --gpu 0 bug ran on GPU 0 instead of 5). Now uses --gpu 5 correctly.\", \"parent\": \"exp_001_sft_d005_05B\", \"notes\": \"invalidated — 与 v3 重复提交（间隔 48s），从未实际运行。v3 (PID 239729) 是正确的 run。\", \"conclusion\": \"killed\", \"failure_reason\": \"OOM — v3 (PID 239734) 已占用 GPU 5 全部显存，r3 是重复提交，启动即崩溃。v3 正常运行中，r3 废弃。\"}, \"exp_001_eval_3B_d000_s42_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:51:39.462Z\", \"updated_at\": \"2026-05-14T00:12:13.851Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"237865\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_v2.log\", \"submitted_at\": \"2026-05-13T23:51:50.500Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"0% dosage 3B s42 baseline eval (v2, fix --gpu bug from v1). No --gpu param, use CUDA_VISIBLE_DEVICES via gpu_ids.\", \"parent\": \"exp_001_sft_0pct_3B\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"data_path\": \"d000\", \"data_count\": 0}, \"conclusion\": \"failed\", \"failure_reason\": \"killed by d005 worker reclaiming GPU 5 (SIGKILL, EXIT_CODE=137)\"}, \"exp_001_sft_d005_05B_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:48:24.508Z\", \"updated_at\": \"2026-05-13T23:59:33.029Z\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry after v1 OOM crash (GPU 5 conflict with zombie eval process). GPU 5 now clear.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"237300\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log\", \"submitted_at\": \"2026-05-13T23:49:27.702Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20.9, \"gpu_hours\": 0.01}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"237300\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-13T23:49:47.033Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 578.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 459.38 MiB is free. Process 235248 has 21.47 GiB memory in use. Including non-PyTorch memory, this process has 1.58 GiB memory in use. Of the allocated\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:49:48.629Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:49:51.462263+00:00\"}]}, \"notes\": \"v2 OOM 根因非 GPU 5 残留进程，而是 --gpu 0 导致训练实际跑在 GPU 0（d100 占满 22GB），GPU 5 从未被使用。已在 r3 修复为 --gpu 5。\"}, \"exp_001_sft_d005_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:36:15.352Z\", \"updated_at\": \"2026-05-13T23:59:30.512Z\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): minimum contamination level to detect dose-response threshold; paired with d100 for min-max comparison\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-13T23:38:42.505Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-13T23:42:32.872Z\", \"training_hours\": 0.06}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"236994\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log\", \"submitted_at\": \"2026-05-13T23:49:14.077Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"235331\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log\", \"failure_reason\": \"CUDA OOM at step 8/3177 — zombie 3B eval process (PID 234755) 占 6.8GB GPU 5 显存，导致 SFT 训练分配失败。已重试为 exp_001_sft_d005_05B_v2。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:42:35.135Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:42:37.857937+00:00\"}]}, \"notes\": \"v1 OOM at step 8/3177 — GPU 5 有残留进程 PID 234755 占 6.8GB。PID 236994 (submit_training_job 重提交) 也使用了 --gpu 0，实际跑到 GPU 0 而非 GPU 5，同样 OOM。根因：--gpu 0 导致 CUDA_VISIBLE_DEVICES 被脚本覆盖为 0。已在 r3 修复为 --gpu 5。\"}, \"exp_001_sft_100pct_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:41:15.631Z\", \"updated_at\": \"2026-05-13T23:49:12.007Z\", \"hypothesis\": \"100% contamination dosage on 0.5B establishes upper bound of score inflation; comparing with 0% baseline reveals maximum contamination effect across MMLU/GSM8K/ARC benchmarks\", \"parent\": \"\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Duplicate registry entry — actual training tracked by exp_001_sft_d100_05B (PID 235243, cron monitored)\", \"completed_at\": \"2026-05-13T23:49:10.741Z\"}, \"exp_001_sft_0pct_3B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:44:40.471Z\", \"updated_at\": \"2026-05-13T23:25:49.016Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"210666\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"submitted_at\": \"2026-05-13T19:44:40.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13268.6, \"gpu_hours\": 3.69}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:23:41.844Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:23:43.393661+00:00\"}]}, \"metrics\": {\"steps\": \"3125/3125\", \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"token_accuracy\": 0.734, \"training_time_min\": 214.7, \"checkpoint_size_mb\": 488, \"adapter_size_mb\": 115, \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T23:25:49.016Z\"}, \"exp_001_sft_injection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:28:01.546Z\", \"updated_at\": \"2026-05-13T23:21:54.827Z\", \"spec\": {\"command\": \"Phase 1 paraphrase: GPU 0 MMLU (PID 204467 v3, vLLM bs=16). GSM8K + ARC completed.\", \"server\": \"cqa1-21977\", \"data_path\": \"MMLU+GSM8K+ARC-Challenge+HumanEval paraphrases → SFT data mixing\", \"data_count\": \"45 SFT runs + 90 eval runs (original+paraphrased)\", \"model_name\": \"Qwen2.5-0.5B/1.5B/3B (LoRA SFT), Qwen2.5-7B-Instruct (paraphrase)\", \"seed\": \"42,123,456\", \"gpu\": \"cuda:0 (MMLU vLLM, still running). cuda:1/2 freed (GSM8K+ARC done).\", \"pid\": \"204467\", \"note\": \"GSM8K: 1319 paraphrases (228 QC pass, 17.3%). ARC: 1172 paraphrases (697 QC pass, 59.5%). MMLU: Attempt 1 done (878 batches, 29.3% QC), Attempt 2 in progress (439 batches total, ~22%), Attempt 3 pending. HumanEval: done (appendix per D009).\"}, \"hypothesis\": \"Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:18:08.635006+00:00\"}, {\"event\": \"status_rollback\", \"action\": \"manual_fix\", \"ts\": \"2026-05-13T19:32:00.000Z\", \"reason\": \"Cron misidentified old PID as dead → auto-failed. 3 paraphrase processes (GPU 0-2) still running. Rolled back DONE/failed → RUNNING per Director instruction.\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:14:43.962197+00:00\"}]}, \"notes\": \"MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 ✅ (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attempt 3 待定. 输出在全部 attempt 结束后一次性写出 mmlu_paraphrases.json. GSM8K ✅ 1319条(QC 17.3%), ARC ✅ 1172条(QC 59.5%).\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:14:29.355Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T23:14:30.258Z\", \"metrics\": {\"mmlu_total\": 14042, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"arc_total\": 1172, \"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"gsm8k_total\": 1319, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"humaneval_total\": 164}}, \"exp_001_sft_0pct_15B_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:35:07.346Z\", \"updated_at\": \"2026-05-13T22:30:26.882Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance estimation)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123 --seed 123 --gpu 2 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"216111\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B_s123.log\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": \"50000\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123\"}, \"notes\": \"OOM 修复后重提交 --gpu 2 (物理 GPU 2)。Worker 确认 PID 216106 训练中 (1/3125 steps, ~2.58s/it)\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.2602, \"token_acc\": 0.731, \"train_time_min\": 101.5}, \"completed_at\": \"2026-05-13T22:30:26.882Z\"}, \"exp_001_sft_0pct_05B_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:35:04.879Z\", \"updated_at\": \"2026-05-13T22:30:25.819Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123 --seed 123 --gpu 1 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"216033\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B_s123.log\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": \"50000\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123\"}, \"notes\": \"OOM 修复后重提交 --gpu 1 (物理 GPU 1)。Worker 确认 PID 216028 训练中 (2/3125 steps, ~1.87s/it)\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.5393, \"token_acc\": 0.676, \"train_time_min\": 54.5}, \"completed_at\": \"2026-05-13T22:30:25.819Z\"}, \"exp_001_sft_0pct_15B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:39:48.369Z\", \"updated_at\": \"2026-05-13T21:27:59.348Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42 --seed 42 --gpu 4 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"210116\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log\", \"submitted_at\": \"2026-05-13T19:41:11.760Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6407.6, \"gpu_hours\": 1.78}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:25:40.979Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T21:25:42.551081+00:00\"}]}, \"metrics\": {\"steps\": \"3125/3125\", \"final_loss\": 1.2039, \"mean_train_loss\": 1.2599, \"token_accuracy\": 0.711, \"training_time_min\": 101.5, \"checkpoint_size_mb\": 313, \"adapter_size_mb\": 71, \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T21:27:59.348Z\"}, \"exp_005_noise_prop\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:31:00.000Z\", \"updated_at\": \"2026-05-13T20:47:21.810Z\", \"hypothesis\": \"Measurement error in exposure scores propagates through 4PL+γ IRT to widen calibrated score CIs; analytical ME model (conjugate normal integration) produces equivalent CI widths to full latent-τ model at fraction of compute\", \"spec\": {\"command\": \"cd artifacts/exp005_noise_propagation && source ../mvp_simulation/.venv/bin/activate && python run_noise_propagation.py\", \"server\": \"local (CPU only)\", \"data_path\": \"synthetic (generated in-script)\", \"data_count\": \"multiple σ_e values × seeds\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS)\", \"seed\": \"0-9\", \"pid\": 234646}, \"failure_reason\": \"Stan numerical bugs: sigma_e=0 allowed (normal_lpdf crash), c/d boundary causing chain crashes, max_treedepth=10 insufficient (14.5% hit rate). All fixed, restarting.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:47:21.810Z\"}, \"exp_001_sft_0pct_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:35:01.170Z\", \"updated_at\": \"2026-05-13T20:37:01.562Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42 --seed 42 --gpu 3 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"208933\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log\", \"submitted_at\": \"2026-05-13T19:37:23.024Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3523.7, \"gpu_hours\": 0.98}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:33:53.420Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:33:54.496690+00:00\"}]}, \"metrics\": {\"steps\": \"3125/3125\", \"final_loss\": 1.4894, \"mean_train_loss\": 1.5388, \"token_accuracy\": 0.682, \"training_time_min\": 52.9, \"checkpoint_size_mb\": 166, \"adapter_size_mb\": 34, \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T20:36:06.744Z\"}, \"exp_004_sim_sweep\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:43:57.478Z\", \"updated_at\": \"2026-05-13T17:10:54.783Z\", \"spec\": {\"command\": \"cd artifacts/simulation_sweep && source ../mvp_simulation/.venv/bin/activate && python run_sweep.py subset\", \"server\": \"local (CPU only)\", \"data_path\": \"synthetic (generated per-condition in-script)\", \"data_count\": \"120 runs (12 conditions x 10 seeds)\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS, 4 chains, 500 warmup, 1000 sampling)\", \"seed\": \"0-9 per condition\", \"note\": \"Sweep: AUC x N_models x prior x exposure_type. Subset first, full later.\", \"pid\": 219346, \"subset_config\": \"AUC=[0.55,0.65,0.80,0.90] x N_models=[20,50,100] x prior=[N(0,1)] x exp_type=[binary]\"}, \"hypothesis\": \"4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which γ 95% CI width exceeds 15pp; recovery improves with N_models; prior sensitivity is bounded\"}, \"mvp_sim_confounding\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T04:39:19.345Z\", \"updated_at\": \"2026-05-13T16:28:42.378Z\", \"hypothesis\": \"4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\", \"spec\": {\"command\": \"python run_p2_confounding.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic confounded (corr≈0.38)\", \"data_count\": \"50 models x 300 items = 15000 responses\", \"model_name\": \"4PL+γ IRT (Stan NUTS)\", \"seed\": 123, \"pid\": 202872, \"log_path\": \"/tmp/p2_confounding.log\", \"note\": \"N_items=300 (matching Variant A PASS config), 4PL NUTS only, 4 chains 1000+1000, θ-exposure corr=0.381\", \"checkpoint_path\": \"artifacts/mvp_simulation/p2_confounding_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gamma_mean\": 0.5386, \"gamma_rel_bias\": 0.0771, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"theta_corr\": 0.9733, \"theta_rmse\": 0.2407, \"theta_residual_exp_corr\": 0.0582, \"max_rhat\": 1.007, \"divergent_pct\": 0, \"min_ess\": 1371.9, \"fit_time_sec\": 832, \"actual_confound_corr\": 0.3814, \"overall\": \"PASS\"}, \"completed_at\": \"2026-05-13T16:28:42.378Z\"}, \"mvp_sim_4pl_gamma\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T04:27:47.251Z\", \"updated_at\": \"2026-05-13T10:59:01.402Z\", \"hypothesis\": \"4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\", \"spec\": {\"command\": \"python run_p1_base.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic (generated in-script)\", \"data_count\": \"50 models x 100 items = 5000 responses\", \"model_name\": \"2PL+γ / 4PL+γ IRT (Stan)\", \"seed\": 42, \"pid\": 197929, \"log_path\": \"/tmp/p1_variants.log\", \"note\": \"Order: 2PL ADVI → 2PL NUTS → 4PL ADVI → 4PL NUTS\", \"checkpoint_path\": \"artifacts/mvp_simulation/p1_variant_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"variant_a_nitems300\": {\"gamma_mean\": 0.466, \"gamma_rel_bias\": 0.068, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"theta_corr\": 0.943, \"theta_rmse\": 0.238, \"max_rhat\": 1.003, \"divergent_pct\": 0, \"fit_time_sec\": 1407.5, \"overall\": \"PASS\"}}, \"completed_at\": \"2026-05-13T10:59:01.402Z\"}}, \"count\": 43, \"total\": 43, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2429}}"
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
The registry output is too large. Let me use a subagent to analyze it, and also check for experiment_plan.yaml.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "dd89cf47-486b-413d-b502-501758f6741e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AboqCDK5JF8UFYyGeS3oZy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4840,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4840
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

_source line 15_

paper_framing.md 已读取。literature_map.yaml 不存在。registry 数据太大，需要用 subagent 分析。同时查找 experiment_plan.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "96bb806d-690b-4d24-bb8d-ea9705d398a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AboqCDK5JF8UFYyGeS3oZy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4840,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4840
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

_source line 16_

<details open><summary>🔧 Tool call — Agent · `toolu_01VgZ36uykfDsghjxHvpqqEB`</summary>

```json
{
  "description": "Analyze experiment registry",
  "prompt": "Analyze the experiment registry data at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt\n\nThis is JSON with schema: {result: string}. The inner result is also a JSON string that needs parsing.\n\nI need you to extract and report:\n1. A table of ALL experiments with: exp_id, name/title, status (DONE/RUNNING/PLANNED/FAILED etc.), conclusion (if any), key metrics\n2. Group experiments by status\n3. For each experiment, note which Core Claim it supports (C1=Calibration, C2=Signal Survival, C3=Identifiability)\n4. Flag any experiments that are RUNNING or PLANNED that are critical\n\nUse jq or python to parse. Report everything verbatim — don't summarize away detail.",
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
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "493afbcd-bcf2-4c25-be40-721d4a938edd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AboqCDK5JF8UFYyGeS3oZy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4840,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4840
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

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "description": "Analyze experiment registry",
  "task_type": "local_agent",
  "prompt": "Analyze the experiment registry data at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt\n\nThis is JSON with schema: {result: string}. The inner result is also a JSON string that needs parsing.\n\nI need you to extract and report:\n1. A table of ALL experiments with: exp_id, name/title, status (DONE/RUNNING/PLANNED/FAILED etc.), conclusion (if any), key metrics\n2. Group experiments by status\n3. For each experiment, note which Core Claim it supports (C1=Calibration, C2=Signal Survival, C3=Identifiability)\n4. Flag any experiments that are RUNNING or PLANNED that are critical\n\nUse jq or python to parse. Report everything verbatim — don't summarize away detail.",
  "uuid": "38a1bc0b-c689-4e53-adaf-fbebf0b7c9f2",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

## Round 1

3 recorded events

### User

_source line 18 · 2026-05-14T03:06:07.273Z_

Analyze the experiment registry data at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt

This is JSON with schema: {result: string}. The inner result is also a JSON string that needs parsing.

I need you to extract and report:
1. A table of ALL experiments with: exp_id, name/title, status (DONE/RUNNING/PLANNED/FAILED etc.), conclusion (if any), key metrics
2. Group experiments by status
3. For each experiment, note which Core Claim it supports (C1=Calibration, C2=Signal Survival, C3=Identifiability)
4. Flag any experiments that are RUNNING or PLANNED that are critical

Use jq or python to parse. Report everything verbatim — don't summarize away detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "8f756eef-1e8a-42a1-af44-62f01af6abef"
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Agent · `toolu_01QkmhwWfKQtGXTDYqSQCyKe`</summary>

```json
{
  "description": "Find experiment_plan.yaml",
  "prompt": "Search for experiment_plan.yaml in the project contamcal-irt-calibration. Try these locations:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/knowledge/experiment_plan.yaml\n3. Glob for **/experiment_plan.yaml under /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/\n\nIf found, read the full file and report its complete contents. I need to see all experiment definitions, their priorities, dependencies, and which claims they support.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "dbfac9c0-c522-442a-9673-205cdb1ebd86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AboqCDK5JF8UFYyGeS3oZy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4840,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4840
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

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a98d970ec9e66bf2e",
  "tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "description": "Find experiment_plan.yaml",
  "task_type": "local_agent",
  "prompt": "Search for experiment_plan.yaml in the project contamcal-irt-calibration. Try these locations:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/knowledge/experiment_plan.yaml\n3. Glob for **/experiment_plan.yaml under /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/\n\nIf found, read the full file and report its complete contents. I need to see all experiment definitions, their priorities, dependencies, and which claims they support.",
  "uuid": "7724ad66-09f5-495f-97b4-46c59782e550",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

## Round 2

44 recorded events

### User

_source line 21 · 2026-05-14T03:06:10.747Z_

Search for experiment_plan.yaml in the project contamcal-irt-calibration. Try these locations:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/knowledge/experiment_plan.yaml
3. Glob for **/experiment_plan.yaml under /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/

If found, read the full file and report its complete contents. I need to see all experiment definitions, their priorities, dependencies, and which claims they support.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "93af2009-dd1e-4150-ac97-d7332ae40614"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt",
  "usage": {
    "total_tokens": 14372,
    "tool_uses": 1,
    "duration_ms": 3625
  },
  "last_tool_name": "Read",
  "uuid": "a70c7584-8fb1-4a38-aa27-f6e663cc61fa",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01VkLbWT4ZPje8e5K3EL6j8k`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "c6d74749-a7c2-4669-876f-e39886b7a9c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Wfr3tMGvE9EB1ATdqwkr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6698,
      "cache_read_input_tokens": 7667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6698,
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

_source line 24 · 2026-05-14T03:06:11.259Z_

<details><summary>↩ Tool result · reported error · `toolu_01VkLbWT4ZPje8e5K3EL6j8k`</summary>

```text
File content (29177 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "f97974ac-813d-4214-aba6-127feb385dda",
  "tool_use_result": "Error: File content (29177 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a98d970ec9e66bf2e",
  "tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "description": "Reading experiment_plan.yaml",
  "usage": {
    "total_tokens": 19296,
    "tool_uses": 1,
    "duration_ms": 1508
  },
  "last_tool_name": "Read",
  "uuid": "141398e9-d909-4e7f-b567-3d635823d767",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_013Hf1hNZYsLSHoxJ5Qgy2sH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "a6ad47f5-6d21-48aa-9cb5-183cc9859b78",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011nANMCro3weDPgn8nH8P7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19283,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19283,
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

_source line 27 · 2026-05-14T03:06:12.293Z_

<details><summary>↩ Tool result · `toolu_013Hf1hNZYsLSHoxJ5Qgy2sH`</summary>

```text
1	# ContamCal Experiment Plan
2	# Each experiment maps to Core Claims in paper_framing.md
3	# Priority: P0 = must-run, P1 = important, P2 = bonus
4	
5	experiments:
6	  # ============================================================
7	  # P0: Core experiments — must complete for submission
8	  # ============================================================
9	
10	  - id: exp-001
11	    name: controlled_sft_injection
12	    claim: 1
13	    description: >
14	      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels
15	      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).
16	      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total
17	      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition
18	      for key metrics (mean ± std).
19	      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or
20	      equivalent) with controlled semantic similarity — following methodology
21	      of "Rethinking Benchmark and Contamination" (arXiv 2023). Target:
22	      high semantic similarity (cosine >0.85) but low lexical overlap
23	      (BLEU <0.3) to evade n-gram decontamination while preserving
24	      contamination effect. Quality validation: automated similarity metrics
25	      + human spot-check on 50 random pairs per benchmark.
26	    priority: P0
27	    gpu_budget_hours: 50
28	    deps: []
29	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
30	    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]
31	    seeds: 3
32	    registry_id: exp_001_sft_d100_15B_v2
33	    # Multi-run experiment; related registry entries:
34	    # exp_001_sft_injection, exp_001_sft_0pct_05B (DONE), exp_001_sft_0pct_15B (DONE),
35	    # exp_001_sft_0pct_3B, exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123,
36	    # exp_001_sft_0pct_3B_s123, exp_001_sft_d100_05B (DONE), exp_001_sft_d005_05B (DONE),
37	    # exp_001_eval_* (various)
38	
39	  - id: exp-002
40	    name: stage1_signal_pipeline
41	    claim: 2
42	    description: >
43	      Compute 4 detection signals on all contaminated + clean models from exp-001:
44	      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),
45	      (b) Min-K%++ membership inference,
46	      (c) ConStat performance gap (original vs paraphrased items),
47	      (d) Self-Critique entropy collapse.
48	      Output: per-model-item exposure scores for each signal.
49	    priority: P0
50	    gpu_budget_hours: 20
51	    deps: [exp-001]
52	
53	  - id: exp-003
54	    name: rrf_aggregation_ablation
55	    claim: 2
56	    description: >
57	      RRF fusion of 4 signals into composite per-item exposure score.
58	      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only
59	      (×4), (c) calibration-based weighted RRF variant, (d) false positive
60	      injection robustness check (inject FP at rates matching Duan et al. 2024).
61	      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.
62	    priority: P0
63	    gpu_budget_hours: 2
64	    deps: [exp-002]
65	
66	  - id: exp-004
67	    name: simulation_identifiability_sweep
68	    claim: 1
69	    also_supports: [3]
70	    description: >
71	      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):
72	      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×
73	      model count (20, 50, 100, 200) ×
74	      prior strength (N(0,0.5), N(0,1), N(0,2)) ×
75	      exposure type (binary, continuous).
76	      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior
77	      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes
78	      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as
79	      "cannot distinguish no contamination from moderate contamination."
80	      N_items=300 fixed (per MVP finding).
81	      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)
82	      — prior × N_models dimensions already in sweep grid. Growing Pains
83	      pre-estimation sub-experiment: at N_models=20/50, compare flat prior
84	      vs informative prior from pre-estimated item parameters.
85	      Also includes Fisher Information matrix analysis: derive approximate
86	      analytical relationship between signal AUC, N_models, and γ
87	      recoverability. Distinguish structural identifiability (parameters
88	      uniquely determined) from practical identifiability (estimation
89	      quality sufficient for decisions). Provides theoretical grounding
90	      for the empirical AUC ≥ 0.70 threshold.
91	    priority: P0
92	    gpu_budget_hours: 0
93	    deps: []
94	    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.
95	    registry_id: exp_004_sim_sweep
96	    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success)
97	
98	  - id: exp-005
99	    name: noise_propagation_analysis
100	    claim: 3
101	    description: >
102	      Two parts:
103	      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure
104	      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true
105	      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.
106	      This propagates Stage 1 uncertainty into posteriors automatically.
107	      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.
108	      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched
109	      levels, re-fit standard model, measure CI widening for γ and θ.
110	      Both parts inform whether measurement error model closes the coverage gap.
111	    priority: P0
112	    gpu_budget_hours: 0
113	    deps: [exp-002, exp-004]
114	    note: CPU only
115	    registry_id: exp_005_noise_prop_v2
116	    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)
117	
118	  - id: exp-006
119	    name: irt_calibration_and_baselines
120	    claim: 1
121	    also_supports: [3]
122	    description: >
123	      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.
124	      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is
125	      the natural parameterization when IRT is fitted per-benchmark (each
126	      benchmark's model has its own γ_k). ABLATION: joint fitting across
127	      benchmarks with shared global γ (stronger assumption, tests whether
128	      contamination effect is homogeneous across benchmarks). Report both.
129	      Per-benchmark fitting (not joint) is the default to reduce local
130	      independence violation scope. Posterior predictive checks on item-level residual
131	      correlations to assess local independence empirically.
132	      Compute calibrated scores via exposure=0 counterfactual with CIs.
133	      Compare against 7 baselines:
134	      (0) Raw — no adjustment (anchor),
135	      (1) remove-and-rescore (drop flagged items),
136	      (2) single-signal 2PL+γ (best signal only, simpler IRT),
137	      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),
138	      (4) linear exposure regression + bootstrap CI (simplest post-hoc),
139	      (5) Emperor's mitigation: rephrasing + option shuffling,
140	      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method
141	          producing adjusted accuracy; must include or reviewers will reject.
142	      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,
143	      Kendall τ, dose-response monotonicity.
144	      Report mean ± std across 3 seeds (matched to exp-001 seeds).
145	    priority: P0
146	    gpu_budget_hours: 8
147	    deps: [exp-003]
148	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
149	    seeds: 3
150	
151	  # ============================================================
152	  # P1: Important — run if time/GPU permit
153	  # ============================================================
154	
155	  - id: exp-015
156	    name: sft_d100_qc_only
157	    claim: 1
158	    description: >
159	      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).
160	      Isolates noisy vs clean contamination confound identified by reviewer.
161	      D012 decision. Compare calibration metrics against exp-001 d100 (all
162	      paraphrases) to quantify effect of noisy contamination on IRT estimates.
163	    priority: P1
164	    gpu_budget_hours: 5
165	    deps: [exp-001]
166	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
167	    models: [Qwen2.5-0.5B]
168	    seeds: 1
169	    status: planned
170	    registry_id: exp_001_sft_d100_qc_only
171	    data_script: exp001/prepare_qc_only_data.py
172	
173	  - id: exp-007
174	    name: scale_bridging_7b
175	    claim: 1
176	    description: >
177	      Qwen2.5-7B controlled SFT injection at 5 dosage levels.
178	      Validates calibration accuracy scales to larger models.
179	      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).
180	    priority: P1
181	    gpu_budget_hours: 30
182	    deps: [exp-001]
183	
184	  - id: exp-008
185	    name: signal_survival_analysis
186	    claim: 2
187	    description: >
188	      Systematic evaluation of detection signal reliability across training regimes.
189	      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,
190	      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat
191	      degrade post-RL (per fragility paper arXiv 2510.02386).
192	      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified
193	      this as the most genuinely novel finding).
194	    priority: P0
195	    gpu_budget_hours: 10
196	    deps: [exp-002]
197	
198	  - id: exp-014
199	    name: multi_family_validation
200	    claim: 1
201	    description: >
202	      Controlled SFT injection on at least one non-Qwen model family
203	      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).
204	      Validates that identifiability boundaries and calibration accuracy
205	      generalize beyond Qwen2.5. Addresses Dream reviewer concern about
206	      single model family limiting generalizability (flagged [M][W]).
207	    priority: P1
208	    gpu_budget_hours: 15
209	    deps: [exp-001]
210	
211	  - id: exp-009
212	    name: rl_observational_case_study
213	    claim: 2
214	    also_supports: [3]
215	    description: >
216	      Apply Self-Critique + available signals to existing RL-trained models:
217	      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.
218	      Fit IRT with appropriately wider CIs. Expected regret quantification:
219	      compare uncalibrated vs calibrated vs remove-rescore for top-5 model
220	      selection. Framed as observational — directional external validity,
221	      not full quantitative validation. Near-zero γ check on known-clean
222	      benchmark (specificity test).
223	    priority: P1
224	    gpu_budget_hours: 15
225	    deps: [exp-006, exp-008]
226	
227	  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.
228	  # Prior × N_models dimensions already covered in the sweep grid.
229	
230	  # ============================================================
231	  # P2: Bonus — adds breadth if resources allow
232	  # ============================================================
233	
234	  - id: exp-012
235	    name: observational_72b
236	    claim: 1
237	    description: >
238	      Qwen2.5-72B observational analysis (inference only, no SFT).
239	      Extends ecological validity to frontier model scale.
240	    priority: P2
241	    gpu_budget_hours: 15
242	    deps: [exp-006]
243	
244	  - id: exp-013
245	    name: closed_weight_2signal_mode
246	    claim: 2
247	    description: >
248	      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)
249	      for closed-weight models. Ablation quantifying 2-signal vs 4-signal
250	      calibration accuracy gap.
251	    priority: P2
252	    gpu_budget_hours: 5
253	    deps: [exp-003]
254	
255	# ============================================================
256	# GPU Budget Summary
257	# ============================================================
258	gpu_budget:
259	  P0_hours: 90
260	  P1_hours: 60
261	  P2_hours: 20
262	  buffer_hours: 30
263	  total_hours: 200
264	  note: >
265	    CPU-only experiments (exp-004, exp-005, exp-011) excluded.
266	    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.
267	    Requires 2-4× H100/A100-80G for parallel SFT runs.
268	    EMNLP 2026 ARR May 25 sprint (12 days from May 13):
269	    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)
270	    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized
271	    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule
272	
273	# Multi-seed protocol:
274	# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics
275	# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)
276	# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)
277	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "ee6ae1d5-677a-4f64-ae45-502a98a5f520"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a98d970ec9e66bf2e",
  "tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "description": "Reading knowledge/experiment_plan.yaml",
  "usage": {
    "total_tokens": 19301,
    "tool_uses": 2,
    "duration_ms": 1926
  },
  "last_tool_name": "Read",
  "uuid": "9977e6f9-9ac6-471e-885f-fe4e65331d89",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01KzmThguKe1C3UkL62g4Q4E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/knowledge/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "7fd0bff1-5a19-40c7-a983-9f0e6dde4c4d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011nANMCro3weDPgn8nH8P7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19283,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19283,
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

_source line 30 · 2026-05-14T03:06:12.696Z_

<details><summary>↩ Tool result · reported error · `toolu_01KzmThguKe1C3UkL62g4Q4E`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "ae0060dc-b367-4a67-9bb0-919ad2026c58",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration."
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a98d970ec9e66bf2e",
  "tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "description": "Finding **/experiment_plan.yaml",
  "usage": {
    "total_tokens": 19306,
    "tool_uses": 3,
    "duration_ms": 2069
  },
  "last_tool_name": "Glob",
  "uuid": "a08cd903-f99c-4833-83fa-d2453e1334b8",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Glob · `toolu_01JyYTsZcPXgcMX956buq1Jf`</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "pattern": "**/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "d2136241-0011-419c-9c77-3e5dbb2cdaf6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011nANMCro3weDPgn8nH8P7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19283,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19283,
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

_source line 33 · 2026-05-14T03:06:12.971Z_

<details><summary>↩ Tool result · `toolu_01JyYTsZcPXgcMX956buq1Jf`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "be10e567-eb28-4777-9dd3-dcffbcd7f6dc"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt",
  "usage": {
    "total_tokens": 15440,
    "tool_uses": 2,
    "duration_ms": 8756
  },
  "last_tool_name": "Read",
  "uuid": "579fa7e4-458e-43fe-a91a-2d688d4a0706",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01FwyLBheusV9YioxGsaekB8`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "f21c8b41-3623-4f97-810f-3ed5b28609c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZYX2meGbqu5H1L8foRjWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1068,
      "cache_read_input_tokens": 14365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1068,
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

_source line 36 · 2026-05-14T03:06:16.512Z_

<details><summary>↩ Tool result · reported error · `toolu_01FwyLBheusV9YioxGsaekB8`</summary>

```text
File content (29177 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "636bf1b6-b558-412d-a4e4-0a377bcd80ae",
  "tool_use_result": "Error: File content (29177 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt",
  "usage": {
    "total_tokens": 15750,
    "tool_uses": 3,
    "duration_ms": 13849
  },
  "last_tool_name": "Read",
  "uuid": "6ee9c31c-6ea8-4ec2-a9b4-6f590d006bb4",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01RxYnxFU4vBUy2i5TpkuydH`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "bddfa136-c2d2-43de-a2dc-c7eba377f6df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zLht4GmCqhzKFXFLjTptJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 15433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 238,
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

_source line 39 · 2026-05-14T03:06:21.547Z_

<details><summary>↩ Tool result · reported error · `toolu_01RxYnxFU4vBUy2i5TpkuydH`</summary>

```text
File content (29177 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "b6af01a3-24bb-422c-a8bf-7fa203e43f32",
  "tool_use_result": "Error: File content (29177 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "description": "Running Check file line count",
  "usage": {
    "total_tokens": 16033,
    "tool_uses": 4,
    "duration_ms": 17382
  },
  "last_tool_name": "Bash",
  "uuid": "74634bda-f126-4891-9342-995db8d15f28",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01SmYxbcMaC4WpVDU9cvnVMp`</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt\"",
  "description": "Check file line count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "ad776e16-f26c-48f6-9926-8a7c6086d49c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMeNkU2R6RSZzxiBLN7ATm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 225,
      "cache_read_input_tokens": 15671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 225,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 42 · 2026-05-14T03:06:24.950Z_

<details><summary>↩ Tool result · `toolu_01SmYxbcMaC4WpVDU9cvnVMp`</summary>

```text
0 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "0949be1b-a1ca-449d-b3e8-8296f74c0f2d"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a98d970ec9e66bf2e",
  "tool_use_id": "toolu_01QkmhwWfKQtGXTDYqSQCyKe",
  "status": "completed",
  "output_file": "",
  "summary": "Find experiment_plan.yaml",
  "usage": {
    "total_tokens": 24969,
    "tool_uses": 3,
    "duration_ms": 20661
  },
  "uuid": "261947cf-7bee-48b6-94c6-4eb11512a4ec",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool result

_source line 44 · 2026-05-14T03:06:31.412Z_

<details><summary>↩ Tool result · `toolu_01QkmhwWfKQtGXTDYqSQCyKe`</summary>

```text
Perfect! I found the file. Here is the complete contents of the experiment_plan.yaml file:

## Summary

The **experiment_plan.yaml** file defines the complete experimental roadmap for the ContamCal IRT Calibration project. It contains 13 experiments organized by priority level, with clear mappings to core claims in the paper.

## Experiment Definitions by Priority

### P0: Core Experiments (Must Complete)
Must-run experiments required for submission:

1. **exp-001: controlled_sft_injection** (→ Claim 1)
   - SFT contamination injection on 3 Qwen2.5 models (0.5B/1.5B/3B) at 5 dosage levels (0%, 5%, 25%, 50%, 100%)
   - 15 SFT runs total, 3 seeds each for statistics
   - 50 GPU hours, uses strong LLM paraphrasing with high semantic similarity (>0.85 cosine) and low lexical overlap (BLEU <0.3)
   - Benchmarks: MMLU, GSM8K, ARC-Challenge, HumanEval

2. **exp-002: stage1_signal_pipeline** (→ Claim 2, deps: exp-001)
   - Compute 4 detection signals: embedding-based semantic retrieval, Min-K%++, ConStat, Self-Critique entropy
   - Produces per-model-item exposure scores
   - 20 GPU hours

3. **exp-003: rrf_aggregation_ablation** (→ Claim 2, deps: exp-002)
   - RRF fusion of 4 signals with ablations: RRF vs equal-weight, single-signal only, calibration-based variants
   - Tests degraded 2-signal mode (ConStat + Self-Critique) for closed-weight
   - 2 GPU hours

4. **exp-004: simulation_identifiability_sweep** (→ Claim 1, also supports Claim 3)
   - Synthetic data sweep: AUC (0.55-0.90) × model count (20-200) × prior strength × exposure type
   - 144 conditions, 10 seeds each
   - CPU only, establishes minimum AUC threshold (≥0.70 recommended)
   - Includes Fisher Information analysis for theoretical grounding
   - Subsumes prior exp-010 and exp-011

5. **exp-005: noise_propagation_analysis** (→ Claim 3, deps: exp-002, exp-004)
   - Measurement error model: treat exposure as noisy observation
   - Two parts: primary measurement model + post-hoc noise injection
   - CPU only, compares coverage vs point-estimate baseline

6. **exp-006: irt_calibration_and_baselines** (→ Claim 1, also supports Claim 3, deps: exp-003)
   - Fit 4PL+γ IRT with per-benchmark γ_k (primary) and joint global γ (ablation)
   - Compare against 7 baselines (raw, remove-rescore, 2PL, vanilla 4PL, linear regression, Emperor's, DCR fuzzy)
   - Evaluate 5 metrics: MAE, coverage (50%/80%/95%), sharpness, Kendall τ, monotonicity
   - 8 GPU hours, 3 seeds matched to exp-001

8. **exp-008: signal_survival_analysis** (→ Claim 2, deps: exp-002)
   - 4 signals × 4 training regimes heatmap (base, SFT-clean, SFT-contaminated, RL-post-trained)
   - Validates Self-Critique reliability across regimes
   - 10 GPU hours, elevated to core contribution

### P1: Important (Run if Time/GPU Permit)

7. **exp-007: scale_bridging_7b** (→ Claim 1, deps: exp-001)
   - Qwen2.5-7B SFT injection at 5 dosages, validates scaling to larger models
   - 30 GPU hours

9. **exp-009: rl_observational_case_study** (→ Claim 2, also supports Claim 3, deps: exp-006, exp-008)
   - Apply Self-Critique + signals to existing RL-trained models (Qwen2.5-Instruct, DeepSeek-R1)
   - Observational frame for external validity
   - 15 GPU hours

14. **exp-014: multi_family_validation** (→ Claim 1, deps: exp-001)
   - SFT injection on non-Qwen model (Llama-3.2-1B or Pythia-1.4B) at 3 dosages
   - Validates generalizability across model families
   - 15 GPU hours

15. **exp-015: sft_d100_qc_only** (→ Claim 1, deps: exp-001)
   - 100% dosage using only QC-pass paraphrases (7547/16697 items)
   - Isolates noisy vs clean contamination confound
   - 5 GPU hours, 1 seed on Qwen2.5-0.5B

### P2: Bonus (Resource Permitting)

12. **exp-012: observational_72b** (→ Claim 1, deps: exp-006)
   - Qwen2.5-72B observational analysis (inference only)
   - 15 GPU hours

13. **exp-013: closed_weight_2signal_mode** (→ Claim 2, deps: exp-003)
   - Degraded 2-signal mode for closed-weight models
   - 5 GPU hours

## GPU Budget Summary
- P0: 90 hours
- P1: 60 hours
- P2: 20 hours
- Buffer: 30 hours
- **Total: 200 hours**

Timeline note: EMNLP 2026 ARR May 25 sprint (12 days from May 13):
- With 4× H100: P0 in ~4 days, P1 in ~3 days (fits deadline)
- With 2× H100: P0 in ~7 days, P1 in ~4 days (tight but feasible)

## Dependencies Graph
- exp-001 (SFT injection) → foundation
- exp-002 (signals) depends on exp-001
- exp-003 (RRF) depends on exp-002
- exp-006 (IRT calibration) depends on exp-003
- exp-004 (simulation) is independent
- exp-005 (noise) depends on exp-002 and exp-004
- exp-008, exp-009, exp-014, exp-015 depend on exp-001/002/003
- exp-007, exp-009, exp-012 form a secondary tier
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "d141a4a5-cbc9-4efa-ab30-d411140d0403",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for experiment_plan.yaml in the project contamcal-irt-calibration. Try these locations:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/knowledge/experiment_plan.yaml\n3. Glob for **/experiment_plan.yaml under /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/\n\nIf found, read the full file and report its complete contents. I need to see all experiment definitions, their priorities, dependencies, and which claims they support.",
    "agentId": "a98d970ec9e66bf2e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I found the file. Here is the complete contents of the experiment_plan.yaml file:\n\n## Summary\n\nThe **experiment_plan.yaml** file defines the complete experimental roadmap for the ContamCal IRT Calibration project. It contains 13 experiments organized by priority level, with clear mappings to core claims in the paper.\n\n## Experiment Definitions by Priority\n\n### P0: Core Experiments (Must Complete)\nMust-run experiments required for submission:\n\n1. **exp-001: controlled_sft_injection** (→ Claim 1)\n   - SFT contamination injection on 3 Qwen2.5 models (0.5B/1.5B/3B) at 5 dosage levels (0%, 5%, 25%, 50%, 100%)\n   - 15 SFT runs total, 3 seeds each for statistics\n   - 50 GPU hours, uses strong LLM paraphrasing with high semantic similarity (>0.85 cosine) and low lexical overlap (BLEU <0.3)\n   - Benchmarks: MMLU, GSM8K, ARC-Challenge, HumanEval\n\n2. **exp-002: stage1_signal_pipeline** (→ Claim 2, deps: exp-001)\n   - Compute 4 detection signals: embedding-based semantic retrieval, Min-K%++, ConStat, Self-Critique entropy\n   - Produces per-model-item exposure scores\n   - 20 GPU hours\n\n3. **exp-003: rrf_aggregation_ablation** (→ Claim 2, deps: exp-002)\n   - RRF fusion of 4 signals with ablations: RRF vs equal-weight, single-signal only, calibration-based variants\n   - Tests degraded 2-signal mode (ConStat + Self-Critique) for closed-weight\n   - 2 GPU hours\n\n4. **exp-004: simulation_identifiability_sweep** (→ Claim 1, also supports Claim 3)\n   - Synthetic data sweep: AUC (0.55-0.90) × model count (20-200) × prior strength × exposure type\n   - 144 conditions, 10 seeds each\n   - CPU only, establishes minimum AUC threshold (≥0.70 recommended)\n   - Includes Fisher Information analysis for theoretical grounding\n   - Subsumes prior exp-010 and exp-011\n\n5. **exp-005: noise_propagation_analysis** (→ Claim 3, deps: exp-002, exp-004)\n   - Measurement error model: treat exposure as noisy observation\n   - Two parts: primary measurement model + post-hoc noise injection\n   - CPU only, compares coverage vs point-estimate baseline\n\n6. **exp-006: irt_calibration_and_baselines** (→ Claim 1, also supports Claim 3, deps: exp-003)\n   - Fit 4PL+γ IRT with per-benchmark γ_k (primary) and joint global γ (ablation)\n   - Compare against 7 baselines (raw, remove-rescore, 2PL, vanilla 4PL, linear regression, Emperor's, DCR fuzzy)\n   - Evaluate 5 metrics: MAE, coverage (50%/80%/95%), sharpness, Kendall τ, monotonicity\n   - 8 GPU hours, 3 seeds matched to exp-001\n\n8. **exp-008: signal_survival_analysis** (→ Claim 2, deps: exp-002)\n   - 4 signals × 4 training regimes heatmap (base, SFT-clean, SFT-contaminated, RL-post-trained)\n   - Validates Self-Critique reliability across regimes\n   - 10 GPU hours, elevated to core contribution\n\n### P1: Important (Run if Time/GPU Permit)\n\n7. **exp-007: scale_bridging_7b** (→ Claim 1, deps: exp-001)\n   - Qwen2.5-7B SFT injection at 5 dosages, validates scaling to larger models\n   - 30 GPU hours\n\n9. **exp-009: rl_observational_case_study** (→ Claim 2, also supports Claim 3, deps: exp-006, exp-008)\n   - Apply Self-Critique + signals to existing RL-trained models (Qwen2.5-Instruct, DeepSeek-R1)\n   - Observational frame for external validity\n   - 15 GPU hours\n\n14. **exp-014: multi_family_validation** (→ Claim 1, deps: exp-001)\n   - SFT injection on non-Qwen model (Llama-3.2-1B or Pythia-1.4B) at 3 dosages\n   - Validates generalizability across model families\n   - 15 GPU hours\n\n15. **exp-015: sft_d100_qc_only** (→ Claim 1, deps: exp-001)\n   - 100% dosage using only QC-pass paraphrases (7547/16697 items)\n   - Isolates noisy vs clean contamination confound\n   - 5 GPU hours, 1 seed on Qwen2.5-0.5B\n\n### P2: Bonus (Resource Permitting)\n\n12. **exp-012: observational_72b** (→ Claim 1, deps: exp-006)\n   - Qwen2.5-72B observational analysis (inference only)\n   - 15 GPU hours\n\n13. **exp-013: closed_weight_2signal_mode** (→ Claim 2, deps: exp-003)\n   - Degraded 2-signal mode for closed-weight models\n   - 5 GPU hours\n\n## GPU Budget Summary\n- P0: 90 hours\n- P1: 60 hours\n- P2: 20 hours\n- Buffer: 30 hours\n- **Total: 200 hours**\n\nTimeline note: EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n- With 4× H100: P0 in ~4 days, P1 in ~3 days (fits deadline)\n- With 2× H100: P0 in ~7 days, P1 in ~4 days (tight but feasible)\n\n## Dependencies Graph\n- exp-001 (SFT injection) → foundation\n- exp-002 (signals) depends on exp-001\n- exp-003 (RRF) depends on exp-002\n- exp-006 (IRT calibration) depends on exp-003\n- exp-004 (simulation) is independent\n- exp-005 (noise) depends on exp-002 and exp-004\n- exp-008, exp-009, exp-014, exp-015 depend on exp-001/002/003\n- exp-007, exp-009, exp-012 form a secondary tier"
      }
    ],
    "totalDurationMs": 20666,
    "totalTokens": 26641,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5658,
      "cache_read_input_tokens": 19283,
      "output_tokens": 1693,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1693,
          "cache_read_input_tokens": 19283,
          "cache_creation_input_tokens": 5658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5658,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 1,
      "bashCount": 0,
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

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "description": "Running Parse JSON structure",
  "usage": {
    "total_tokens": 16315,
    "tool_uses": 5,
    "duration_ms": 27560
  },
  "last_tool_name": "Bash",
  "uuid": "9ee3b2fd-b0a0-4460-bdd0-f27899f6ff17",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01WJj2YKYCLfyi3We61NCDjx`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open(\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt\", \"r\") as f:\n    outer = json.load(f)\n\n# Parse the inner result string\ninner = json.loads(outer[\"result\"])\n\n# Show top-level keys\nprint(\"Top-level keys:\", list(inner.keys()))\nprint()\n\n# Show structure\nfor k, v in inner.items():\n    if isinstance(v, dict):\n        print(f\"  {k}: dict with keys {list(v.keys())[:10]}...\")\n    elif isinstance(v, list):\n        print(f\"  {k}: list of {len(v)} items\")\n    elif isinstance(v, str):\n        print(f\"  {k}: str({len(v)} chars) = {v[:200]}\")\n    else:\n        print(f\"  {k}: {type(v).__name__} = {v}\")\nPYEOF",
  "description": "Parse JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "49266bd2-2d78-4087-895f-0cbb5dea0195",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qFcMGQCie1D4oLp1EzGX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 280,
      "cache_read_input_tokens": 15896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 280,
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

_source line 47 · 2026-05-14T03:06:35.104Z_

<details><summary>↩ Tool result · `toolu_01WJj2YKYCLfyi3We61NCDjx`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']

  success: bool = True
  data: dict with keys ['experiments', 'count', 'total', 'baseline']...
  error: NoneType = None
  metadata: dict with keys ['elapsed_seconds']...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "fc0a2dc6-dd7d-49b8-9e51-c538fc203abf"
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
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "description": "Running Explore experiment data structure",
  "usage": {
    "total_tokens": 16871,
    "tool_uses": 6,
    "duration_ms": 33573
  },
  "last_tool_name": "Bash",
  "uuid": "e7ace790-528c-413f-a083-bace64d120af",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01HeTJceE5vJ9UER9TRR3Ayj`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open(\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt\", \"r\") as f:\n    outer = json.load(f)\n\ninner = json.loads(outer[\"result\"])\ndata = inner[\"data\"]\n\nprint(\"data keys:\", list(data.keys()))\nprint(\"count:\", data.get(\"count\"))\nprint(\"total:\", data.get(\"total\"))\nprint(\"baseline:\", data.get(\"baseline\"))\nprint()\n\nexperiments = data[\"experiments\"]\nprint(f\"Number of experiments: {len(experiments)}\")\nprint()\n\n# Show first experiment structure\nif experiments:\n    exp0 = experiments[0]\n    print(\"First experiment keys:\", list(exp0.keys()))\n    print()\n    print(\"First experiment full dump:\")\n    print(json.dumps(exp0, indent=2, ensure_ascii=False))\nPYEOF",
  "description": "Explore experiment data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "462dd3f3-6e1c-4266-926e-887281daf8a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCsbjoh9ajCmtUGoD7ZaN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 483,
      "cache_read_input_tokens": 16176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 483,
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

_source line 50 · 2026-05-14T03:06:41.586Z_

<details><summary>↩ Tool result · reported error · `toolu_01HeTJceE5vJ9UER9TRR3Ayj`</summary>

```text
Exit code 1
data keys: ['experiments', 'count', 'total', 'baseline']
count: 43
total: 43
baseline: None

Number of experiments: 43

Traceback (most recent call last):
  File "&lt;stdin>", line 21, in &lt;module>
KeyError: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "53d55ed4-6b0a-4a5b-bf9a-949c27c294a1",
  "tool_use_result": "Error: Exit code 1\ndata keys: ['experiments', 'count', 'total', 'baseline']\ncount: 43\ntotal: 43\nbaseline: None\n\nNumber of experiments: 43\n\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 21, in &lt;module>\nKeyError: 0"
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
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "description": "Running Determine experiments structure type",
  "usage": {
    "total_tokens": 17402,
    "tool_uses": 7,
    "duration_ms": 39325
  },
  "last_tool_name": "Bash",
  "uuid": "e797ee04-42f1-488f-ac18-b2614b66efc5",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01R1gFqgLjjdoDkRqDfCoSpy`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open(\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt\", \"r\") as f:\n    outer = json.load(f)\n\ninner = json.loads(outer[\"result\"])\ndata = inner[\"data\"]\nexperiments = data[\"experiments\"]\n\nprint(f\"Type of experiments: {type(experiments)}\")\nif isinstance(experiments, dict):\n    keys = list(experiments.keys())\n    print(f\"Experiment IDs: {keys}\")\n    print()\n    # Show first experiment\n    first_key = keys[0]\n    print(f\"First experiment ({first_key}):\")\n    print(json.dumps(experiments[first_key], indent=2, ensure_ascii=False))\nelif isinstance(experiments, list):\n    print(f\"First experiment:\")\n    print(json.dumps(experiments[0], indent=2, ensure_ascii=False))\nPYEOF",
  "description": "Determine experiments structure type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "49272ea6-89ce-43bc-a358-b22899e04855",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pRyFMojBBsn6oBYDKiTjv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 16659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 459,
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

_source line 53 · 2026-05-14T03:06:46.737Z_

<details><summary>↩ Tool result · `toolu_01R1gFqgLjjdoDkRqDfCoSpy`</summary>

```text
Type of experiments: &lt;class 'dict'>
Experiment IDs: ['exp_001_eval_05B_d000_s42_v6', 'exp_001_eval_05B_d100_v6', 'exp_001_eval_05B_d100_v5', 'exp_001_eval_05B_d000_s42_v5', 'exp_001_eval_05B_d100_v4', 'exp_001_eval_05B_d000_s42_v4', 'exp_001_eval_05B_d100_v2', 'exp_001_eval_05B_d000_s42_v2', 'exp_001_eval_05B_d100_v3', 'exp_001_eval_05B_d000_s42_v3', 'exp_001_eval_05B_d100', 'exp_001_eval_05B_d005', 'exp_001_eval_05B_d000_s42', 'exp_001_eval_05B_d000_s123', 'exp_001_sft_d100_15B', 'exp_001_sft_d100_15B_v2', 'exp_001_eval_15B_d000_s123', 'exp_001_sft_d005_15B', 'exp_001_sft_d005_05B_v3', 'exp_001_sft_d100_05B', 'exp_001_eval_3B_d000_s42', 'exp_001_eval_3B_d000_s42_v3', 'exp_001_sft_0pct', 'exp_001_eval_15B_d000_s42_v2', 'exp_001_eval_3B_d000_s123', 'exp_001_sft_0pct_3B_s123', 'exp_001_eval_15B_d000_s42', 'exp_005_noise_prop_v2', 'exp_001_sft_d005_05B_r3', 'exp_001_eval_3B_d000_s42_v2', 'exp_001_sft_d005_05B_v2', 'exp_001_sft_d005_05B', 'exp_001_sft_100pct_05B', 'exp_001_sft_0pct_3B', 'exp_001_sft_injection', 'exp_001_sft_0pct_15B_s123', 'exp_001_sft_0pct_05B_s123', 'exp_001_sft_0pct_15B', 'exp_005_noise_prop', 'exp_001_sft_0pct_05B', 'exp_004_sim_sweep', 'mvp_sim_confounding', 'mvp_sim_4pl_gamma']

First experiment (exp_001_eval_05B_d000_s42_v6):
{
  "status": "PREPARING",
  "retry_count": 0,
  "created_at": "2026-05-14T02:40:46.586Z",
  "updated_at": "2026-05-14T02:47:17.653Z",
  "spec": {
    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
    "server": "cqa1-21977",
    "gpu": [
      "cuda:2"
    ],
    "pid": "267141",
    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v6.log",
    "submitted_at": "2026-05-14T02:40:46.245Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root"
  },
  "hypothesis": "0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)",
  "conclusion": "killed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "68b88df9-ae49-40e2-bfd1-36d9c43fa6ab"
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
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "description": "Running Extract all experiment details",
  "usage": {
    "total_tokens": 19188,
    "tool_uses": 8,
    "duration_ms": 54847
  },
  "last_tool_name": "Bash",
  "uuid": "3126dbe7-87f3-4db2-950e-8e7f4205f7cf",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_011LoWccXveNifDMG5id7pjC`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open(\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt\", \"r\") as f:\n    outer = json.load(f)\n\ninner = json.loads(outer[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\n# Extract all experiments into a flat table\nrows = []\nfor exp_id, exp in experiments.items():\n    status = exp.get(\"status\", \"UNKNOWN\")\n    hypothesis = exp.get(\"hypothesis\", \"\")\n    conclusion = exp.get(\"conclusion\", \"\")\n    created = exp.get(\"created_at\", \"\")\n    updated = exp.get(\"updated_at\", \"\")\n    \n    spec = exp.get(\"spec\", {})\n    server = spec.get(\"server\", \"\")\n    gpu = spec.get(\"gpu\", [])\n    pid = spec.get(\"pid\", \"\")\n    log_path = spec.get(\"log_path\", \"\")\n    command = spec.get(\"command\", \"\")\n    \n    # Extract metrics if any\n    metrics = exp.get(\"metrics\", {})\n    results = exp.get(\"results\", {})\n    \n    rows.append({\n        \"exp_id\": exp_id,\n        \"status\": status,\n        \"hypothesis\": hypothesis,\n        \"conclusion\": conclusion,\n        \"created_at\": created,\n        \"updated_at\": updated,\n        \"server\": server,\n        \"gpu\": gpu,\n        \"pid\": pid,\n        \"log_path\": log_path,\n        \"metrics\": metrics,\n        \"results\": results,\n        \"command_snippet\": command[:120] if command else \"\",\n    })\n\n# Print all experiments sorted by exp_id\nrows.sort(key=lambda x: x[\"exp_id\"])\n\nprint(f\"Total experiments: {len(rows)}\")\nprint(\"=\" * 120)\n\nfor r in rows:\n    print(f\"\\n--- {r['exp_id']} ---\")\n    print(f\"  Status:     {r['status']}\")\n    print(f\"  Hypothesis: {r['hypothesis']}\")\n    print(f\"  Conclusion: {r['conclusion']}\")\n    print(f\"  Created:    {r['created_at']}\")\n    print(f\"  Updated:    {r['updated_at']}\")\n    print(f\"  Server:     {r['server']}\")\n    print(f\"  GPU:        {r['gpu']}\")\n    print(f\"  PID:        {r['pid']}\")\n    print(f\"  Log:        {r['log_path']}\")\n    if r['metrics']:\n        print(f\"  Metrics:    {json.dumps(r['metrics'], ensure_ascii=False)}\")\n    if r['results']:\n        print(f\"  Results:    {json.dumps(r['results'], ensure_ascii=False)}\")\n\nPYEOF",
  "description": "Extract all experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "f1f2a77a-f44d-40dc-b5d4-755844944d8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cMLnb8dK9xyGXgYquw8SY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1778,
      "cache_read_input_tokens": 17118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1778,
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

_source line 56 · 2026-05-14T03:07:02.243Z_

<details><summary>↩ Tool result · `toolu_011LoWccXveNifDMG5id7pjC`</summary>

```text
Total experiments: 43
========================================================================================================================

--- exp_001_eval_05B_d000_s123 ---
  Status:     DONE
  Hypothesis: 
  Conclusion: success
  Created:    2026-05-13T22:30:40.455Z
  Updated:    2026-05-14T01:29:09.875Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        229516
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log
  Metrics:    {"mmlu_accuracy": 0.4182, "gsm8k_exact_match": 0.3404, "arc_challenge_accuracy": 0.3976, "humaneval_pass_at_1": 0.1037}

--- exp_001_eval_05B_d000_s42 ---
  Status:     DONE
  Hypothesis: 0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation
  Conclusion: failed
  Created:    2026-05-13T22:42:34.313Z
  Updated:    2026-05-14T01:33:03.857Z
  Server:     cqa1-21977
  GPU:        ['cuda:1']
  PID:        229370
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log

--- exp_001_eval_05B_d000_s42_v2 ---
  Status:     PREPARING
  Hypothesis: 
  Conclusion: failed
  Created:    2026-05-14T02:26:38.504Z
  Updated:    2026-05-14T02:36:51.089Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        263528
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v2.log

--- exp_001_eval_05B_d000_s42_v3 ---
  Status:     PREPARING
  Hypothesis: 0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算
  Conclusion: killed
  Created:    2026-05-14T02:30:50.700Z
  Updated:    2026-05-14T02:33:51.502Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        264245
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v3.log

--- exp_001_eval_05B_d000_s42_v4 ---
  Status:     PREPARING
  Hypothesis: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)
  Conclusion: killed
  Created:    2026-05-14T02:35:30.672Z
  Updated:    2026-05-14T02:40:09.432Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        265362
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v4.log

--- exp_001_eval_05B_d000_s42_v5 ---
  Status:     RUNNING
  Hypothesis: 0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)
  Conclusion: 
  Created:    2026-05-14T02:39:41.292Z
  Updated:    2026-05-14T02:46:54.180Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        266511
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v5.log

--- exp_001_eval_05B_d000_s42_v6 ---
  Status:     PREPARING
  Hypothesis: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)
  Conclusion: killed
  Created:    2026-05-14T02:40:46.586Z
  Updated:    2026-05-14T02:47:17.653Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        267141
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v6.log

--- exp_001_eval_05B_d005 ---
  Status:     RUNNING
  Hypothesis: 
  Conclusion: 
  Created:    2026-05-14T01:17:07.820Z
  Updated:    2026-05-14T02:15:00.000Z
  Server:     cqa1-21977
  GPU:        cuda:1
  PID:        255322
  Log:        /root/runs/contamcal-irt-calibration/exp_001_eval_05B_d005.log

--- exp_001_eval_05B_d100 ---
  Status:     DONE
  Hypothesis: 
  Conclusion: failed
  Created:    2026-05-14T01:15:49.903Z
  Updated:    2026-05-14T02:21:35.372Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        254667
  Log:        /tmp/eval_d100.log

--- exp_001_eval_05B_d100_v2 ---
  Status:     PENDING
  Hypothesis: 
  Conclusion: failed
  Created:    2026-05-14T02:26:41.093Z
  Updated:    2026-05-14T02:39:52.993Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        263784
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v2.log

--- exp_001_eval_05B_d100_v3 ---
  Status:     PREPARING
  Hypothesis: 100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation
  Conclusion: killed
  Created:    2026-05-14T02:30:53.668Z
  Updated:    2026-05-14T02:33:52.158Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        264324
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v3.log

--- exp_001_eval_05B_d100_v4 ---
  Status:     PREPARING
  Hypothesis: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)
  Conclusion: killed
  Created:    2026-05-14T02:36:09.066Z
  Updated:    2026-05-14T02:40:10.093Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        265684
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v4.log

--- exp_001_eval_05B_d100_v5 ---
  Status:     RUNNING
  Hypothesis: 100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)
  Conclusion: 
  Created:    2026-05-14T02:39:57.338Z
  Updated:    2026-05-14T02:46:56.726Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        266780
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v5.log

--- exp_001_eval_05B_d100_v6 ---
  Status:     PREPARING
  Hypothesis: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)
  Conclusion: killed
  Created:    2026-05-14T02:40:56.017Z
  Updated:    2026-05-14T02:47:16.586Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        267346
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v6.log

--- exp_001_eval_15B_d000_s123 ---
  Status:     RUNNING
  Hypothesis: 
  Conclusion: 
  Created:    2026-05-13T22:30:41.501Z
  Updated:    2026-05-14T01:18:06.102Z
  Server:     cqa1-21977
  GPU:        ['cuda:5']
  PID:        250600
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123.log

--- exp_001_eval_15B_d000_s42 ---
  Status:     DONE
  Hypothesis: 0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation
  Conclusion: failed
  Created:    2026-05-13T21:30:03.433Z
  Updated:    2026-05-14T00:23:17.209Z
  Server:     cqa1-21977
  GPU:        ['cuda:4']
  PID:        221376
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42.log

--- exp_001_eval_15B_d000_s42_v2 ---
  Status:     RUNNING
  Hypothesis: 
  Conclusion: 
  Created:    2026-05-14T00:23:20.112Z
  Updated:    2026-05-14T00:33:36.085Z
  Server:     cqa1-21977
  GPU:        ['cuda:4']
  PID:        243290
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log

--- exp_001_eval_3B_d000_s123 ---
  Status:     RUNNING
  Hypothesis: 
  Conclusion: 
  Created:    2026-05-14T00:18:07.960Z
  Updated:    2026-05-14T00:33:31.970Z
  Server:     cqa1-21977
  GPU:        ['cuda:3']
  PID:        242581
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log

--- exp_001_eval_3B_d000_s42 ---
  Status:     RUNNING
  Hypothesis: 0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) to establish ground-truth scores for calibration error computation
  Conclusion: 
  Created:    2026-05-13T23:36:54.086Z
  Updated:    2026-05-14T00:55:02.251Z
  Server:     cqa1-21977
  GPU:        ['cuda:1']
  PID:        249294
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42.log

--- exp_001_eval_3B_d000_s42_v2 ---
  Status:     PREPARING
  Hypothesis: 
  Conclusion: failed
  Created:    2026-05-13T23:51:39.462Z
  Updated:    2026-05-14T00:12:13.851Z
  Server:     cqa1-21977
  GPU:        ['cuda:5']
  PID:        237865
  Log:        ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_v2.log

--- exp_001_eval_3B_d000_s42_v3 ---
  Status:     PREPARING
  Hypothesis: 3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。
  Conclusion: 
  Created:    2026-05-14T00:48:57.772Z
  Updated:    2026-05-14T00:49:04.468Z
  Server:     
  GPU:        []
  PID:        
  Log:        

--- exp_001_sft_0pct ---
  Status:     DONE
  Hypothesis: 0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores for calibration error computation; LoRA r=16 alpha=32 1-epoch training on pure instruction data should preserve base model capability
  Conclusion: success
  Created:    2026-05-13T19:26:42.106Z
  Updated:    2026-05-14T00:36:52.832Z
  Server:     
  GPU:        []
  PID:        
  Log:        

--- exp_001_sft_0pct_05B ---
  Status:     DONE
  Hypothesis: 
  Conclusion: success
  Created:    2026-05-13T19:35:01.170Z
  Updated:    2026-05-13T20:37:01.562Z
  Server:     cqa1-21977
  GPU:        ['cuda:3']
  PID:        208933
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log
  Metrics:    {"steps": "3125/3125", "final_loss": 1.4894, "mean_train_loss": 1.5388, "token_accuracy": 0.682, "training_time_min": 52.9, "checkpoint_size_mb": 166, "adapter_size_mb": 34, "exit_code": 0}

--- exp_001_sft_0pct_05B_s123 ---
  Status:     DONE
  Hypothesis: 0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation)
  Conclusion: success
  Created:    2026-05-13T20:35:04.879Z
  Updated:    2026-05-13T22:30:25.819Z
  Server:     cqa1-21977
  GPU:        ['cuda:1']
  PID:        216033
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B_s123.log
  Metrics:    {"train_loss": 1.5393, "token_acc": 0.676, "train_time_min": 54.5}

--- exp_001_sft_0pct_15B ---
  Status:     DONE
  Hypothesis: 
  Conclusion: success
  Created:    2026-05-13T19:39:48.369Z
  Updated:    2026-05-13T21:27:59.348Z
  Server:     cqa1-21977
  GPU:        ['cuda:4']
  PID:        210116
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log
  Metrics:    {"steps": "3125/3125", "final_loss": 1.2039, "mean_train_loss": 1.2599, "token_accuracy": 0.711, "training_time_min": 101.5, "checkpoint_size_mb": 313, "adapter_size_mb": 71, "exit_code": 0}

--- exp_001_sft_0pct_15B_s123 ---
  Status:     DONE
  Hypothesis: 0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance estimation)
  Conclusion: success
  Created:    2026-05-13T20:35:07.346Z
  Updated:    2026-05-13T22:30:26.882Z
  Server:     cqa1-21977
  GPU:        ['cuda:2']
  PID:        216111
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B_s123.log
  Metrics:    {"train_loss": 1.2602, "token_acc": 0.731, "train_time_min": 101.5}

--- exp_001_sft_0pct_3B ---
  Status:     DONE
  Hypothesis: 
  Conclusion: success
  Created:    2026-05-13T19:44:40.471Z
  Updated:    2026-05-13T23:25:49.016Z
  Server:     cqa1-21977
  GPU:        ['cuda:5']
  PID:        210666
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log
  Metrics:    {"steps": "3125/3125", "final_loss": 1.0736, "mean_train_loss": 1.1306, "token_accuracy": 0.734, "training_time_min": 214.7, "checkpoint_size_mb": 488, "adapter_size_mb": 115, "exit_code": 0}

--- exp_001_sft_0pct_3B_s123 ---
  Status:     DONE
  Hypothesis: 0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance estimation)
  Conclusion: success
  Created:    2026-05-13T20:39:01.606Z
  Updated:    2026-05-14T00:23:18.290Z
  Server:     cqa1-21977
  GPU:        ['cuda:3']
  PID:        216935
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B_s123.log
  Metrics:    {"final_loss": 1.114, "mean_train_loss": 1.1309, "mean_token_accuracy": 0.7505, "training_time_min": 213.1, "steps_completed": 3125, "total_steps": 3125, "epochs": 1, "train_samples_per_second": 3.91, "checkpoint_size_mb": 488, "adapter_size_mb": 488, "adapter_model_mb": 114, "total_tokens": 19555717}

--- exp_001_sft_100pct_05B ---
  Status:     DONE
  Hypothesis: 100% contamination dosage on 0.5B establishes upper bound of score inflation; comparing with 0% baseline reveals maximum contamination effect across MMLU/GSM8K/ARC benchmarks
  Conclusion: failed
  Created:    2026-05-13T23:41:15.631Z
  Updated:    2026-05-13T23:49:12.007Z
  Server:     cqa1-21977
  GPU:        []
  PID:        
  Log:        

--- exp_001_sft_d005_05B ---
  Status:     DONE
  Hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): minimum contamination level to detect dose-response threshold; paired with d100 for min-max comparison
  Conclusion: killed
  Created:    2026-05-13T23:36:15.352Z
  Updated:    2026-05-13T23:59:30.512Z
  Server:     cqa1-21977
  GPU:        ['cuda:5']
  PID:        236994
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log

--- exp_001_sft_d005_05B_r3 ---
  Status:     PREPARING
  Hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (v1: GPU 5 zombie process; v2: --gpu 0 bug ran on GPU 0 instead of 5). Now uses --gpu 5 correctly.
  Conclusion: killed
  Created:    2026-05-13T23:58:49.282Z
  Updated:    2026-05-14T00:12:15.733Z
  Server:     cqa1-21977
  GPU:        ['cuda:5']
  PID:        240163
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_r3.log

--- exp_001_sft_d005_05B_v2 ---
  Status:     DONE
  Hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry after v1 OOM crash (GPU 5 conflict with zombie eval process). GPU 5 now clear.
  Conclusion: failed
  Created:    2026-05-13T23:48:24.508Z
  Updated:    2026-05-13T23:59:33.029Z
  Server:     cqa1-21977
  GPU:        ['cuda:5']
  PID:        237300
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log

--- exp_001_sft_d005_05B_v3 ---
  Status:     DONE
  Hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.
  Conclusion: success
  Created:    2026-05-13T23:52:39.321Z
  Updated:    2026-05-14T00:58:15.977Z
  Server:     cqa1-21977
  GPU:        ['cuda:5']
  PID:        239729
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v3.log
  Metrics:    {"final_loss": 1.478, "mean_train_loss": 1.5424, "token_accuracy": 0.667, "training_time_min": 56.14, "total_steps": 3177, "train_samples_per_second": 15.09, "train_steps_per_second": 0.943, "exit_code": 0, "epoch": 1, "num_tokens": 19657865, "entropy": 1.5874, "checkpoint_size_mb": 166, "lora_adapter_size_mb": 33.6, "vs_baseline_0pct": {"baseline_final_loss": 1.4894, "baseline_mean_train_loss": 1.5388, "baseline_token_accuracy": 0.682, "baseline_training_time_min": 52.9, "delta_final_loss": -0.0114, "delta_mean_train_loss": 0.0036, "delta_token_accuracy": -0.015, "delta_training_time_min": 3.24}}

--- exp_001_sft_d005_15B ---
  Status:     PREPARING
  Hypothesis: 
  Conclusion: 
  Created:    2026-05-14T00:19:54.331Z
  Updated:    2026-05-14T01:00:53.141Z
  Server:     
  GPU:        []
  PID:        
  Log:        

--- exp_001_sft_d100_05B ---
  Status:     DONE
  Hypothesis: 100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison
  Conclusion: success
  Created:    2026-05-13T23:36:13.403Z
  Updated:    2026-05-14T00:55:14.218Z
  Server:     cqa1-21977
  GPU:        ['cuda:0']
  PID:        235243
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log
  Metrics:    {"total_steps": 4160, "final_loss": 1.5943, "mean_train_loss": 1.5662, "token_accuracy": 0.666, "training_time_min": 68.9, "train_samples_per_second": 16.09, "train_steps_per_second": 1.006, "num_tokens": 21575068, "exit_code": 0, "vs_baseline_0pct": {"loss_delta": "+0.0274 (+1.8%)", "accuracy_delta": "-0.016 (-2.3%)", "time_delta": "+16min (+30%)"}}

--- exp_001_sft_d100_15B ---
  Status:     DONE
  Hypothesis: 100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error
  Conclusion: failed
  Created:    2026-05-13T23:37:43.653Z
  Updated:    2026-05-14T01:23:40.711Z
  Server:     cqa1-21977
  GPU:        ['cuda:0']
  PID:        248993
  Log:        /root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log

--- exp_001_sft_d100_15B_v2 ---
  Status:     RUNNING
  Hypothesis: 
  Conclusion: 
  Created:    2026-05-14T01:17:47.114Z
  Updated:    2026-05-14T01:18:26.304Z
  Server:     cqa1-21977
  GPU:        ['cuda:0']
  PID:        251924
  Log:        ~/runs/contamcal-irt-calibration/exp_001_sft_d100_15B_v2.log

--- exp_001_sft_injection ---
  Status:     DONE
  Hypothesis: Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds
  Conclusion: success
  Created:    2026-05-13T17:28:01.546Z
  Updated:    2026-05-13T23:21:54.827Z
  Server:     cqa1-21977
  GPU:        cuda:0 (MMLU vLLM, still running). cuda:1/2 freed (GSM8K+ARC done).
  PID:        204467
  Log:        
  Metrics:    {"mmlu_total": 14042, "mmlu_qc_pass": 6596, "mmlu_qc_rate": 0.47, "arc_total": 1172, "arc_qc_pass": 697, "arc_qc_rate": 0.595, "gsm8k_total": 1319, "gsm8k_qc_pass": 228, "gsm8k_qc_rate": 0.173, "humaneval_total": 164}

--- exp_004_sim_sweep ---
  Status:     RUNNING
  Hypothesis: 4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which γ 95% CI width exceeds 15pp; recovery improves with N_models; prior sensitivity is bounded
  Conclusion: 
  Created:    2026-05-13T16:43:57.478Z
  Updated:    2026-05-13T17:10:54.783Z
  Server:     local (CPU only)
  GPU:        []
  PID:        219346
  Log:        

--- exp_005_noise_prop ---
  Status:     DONE
  Hypothesis: Measurement error in exposure scores propagates through 4PL+γ IRT to widen calibrated score CIs; analytical ME model (conjugate normal integration) produces equivalent CI widths to full latent-τ model at fraction of compute
  Conclusion: failed
  Created:    2026-05-13T18:31:00.000Z
  Updated:    2026-05-13T20:47:21.810Z
  Server:     local (CPU only)
  GPU:        []
  PID:        234646
  Log:        

--- exp_005_noise_prop_v2 ---
  Status:     DONE
  Hypothesis: Same as exp_005: ME model CI width increases monotonically with σ_e; simple model does not. v2 fixes: sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12.
  Conclusion: failed
  Created:    2026-05-13T20:47:35.807Z
  Updated:    2026-05-14T00:13:31.283Z
  Server:     local (CPU only)
  GPU:        []
  PID:        251971
  Log:        artifacts/exp005_noise_propagation/exp005_v2.log

--- mvp_sim_4pl_gamma ---
  Status:     DONE
  Hypothesis: 4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9
  Conclusion: success
  Created:    2026-05-13T04:27:47.251Z
  Updated:    2026-05-13T10:59:01.402Z
  Server:     local-cpu
  GPU:        []
  PID:        197929
  Log:        /tmp/p1_variants.log
  Metrics:    {"variant_a_nitems300": {"gamma_mean": 0.466, "gamma_rel_bias": 0.068, "gamma_ci_covers_true": true, "gamma_ci_excludes_zero": true, "theta_corr": 0.943, "theta_rmse": 0.238, "max_rhat": 1.003, "divergent_pct": 0, "fit_time_sec": 1407.5, "overall": "PASS"}}

--- mvp_sim_confounding ---
  Status:     DONE
  Hypothesis: 4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure
  Conclusion: success
  Created:    2026-05-13T04:39:19.345Z
  Updated:    2026-05-13T16:28:42.378Z
  Server:     local-cpu
  GPU:        []
  PID:        202872
  Log:        /tmp/p2_confounding.log
  Metrics:    {"gamma_mean": 0.5386, "gamma_rel_bias": 0.0771, "gamma_ci_covers_true": true, "gamma_ci_excludes_zero": true, "theta_corr": 0.9733, "theta_rmse": 0.2407, "theta_residual_exp_corr": 0.0582, "max_rhat": 1.007, "divergent_pct": 0, "min_ess": 1371.9, "fit_time_sec": 832, "actual_confound_corr": 0.3814, "overall": "PASS"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "d6e3601e-8be4-4a5c-b641-f7db9de44697"
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
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "description": "Running Group experiments by status",
  "usage": {
    "total_tokens": 28399,
    "tool_uses": 9,
    "duration_ms": 64673
  },
  "last_tool_name": "Bash",
  "uuid": "12b1a0f1-bff0-4db4-aa19-0e084c761f46",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01DKzyTjecpn7TwmsPYNcqAh`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open(\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt\", \"r\") as f:\n    outer = json.load(f)\n\ninner = json.loads(outer[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\n# Group by status\nfrom collections import defaultdict\nby_status = defaultdict(list)\nfor exp_id, exp in experiments.items():\n    by_status[exp.get(\"status\", \"UNKNOWN\")].append(exp_id)\n\nprint(\"=== STATUS SUMMARY ===\")\nfor status in sorted(by_status.keys()):\n    print(f\"  {status}: {len(by_status[status])}\")\nprint(f\"  TOTAL: {len(experiments)}\")\n\nPYEOF",
  "description": "Group experiments by status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "3f8d8029-c1ab-4792-9706-475aa5b5ffb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WczCJ5aDkNFMpJhsJUFvoH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9209,
      "cache_read_input_tokens": 18896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9209,
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

_source line 59 · 2026-05-14T03:07:12.060Z_

<details><summary>↩ Tool result · `toolu_01DKzyTjecpn7TwmsPYNcqAh`</summary>

```text
=== STATUS SUMMARY ===
  DONE: 22
  PENDING: 1
  PREPARING: 11
  RUNNING: 9
  TOTAL: 43
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "f5856e7f-bddf-4c81-8913-995a7dcf2961"
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
  "task_id": "a85fc8f4df600f241",
  "tool_use_id": "toolu_01VgZ36uykfDsghjxHvpqqEB",
  "status": "completed",
  "output_file": "",
  "summary": "Analyze experiment registry",
  "usage": {
    "total_tokens": 28800,
    "tool_uses": 9,
    "duration_ms": 142891
  },
  "uuid": "8b83f1bb-1f56-40ba-a523-21c58b574843",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f"
}
```

---

### Tool result

_source line 61 · 2026-05-14T03:08:30.172Z_

<details><summary>↩ Tool result · `toolu_01VgZ36uykfDsghjxHvpqqEB`</summary>

```text
Now I have all the data. Here is the complete report.

---

## Experiment Registry Analysis — contamcal-irt-calibration

**Total experiments: 43**

### Status Summary

| Status | Count |
|--------|-------|
| DONE | 22 |
| RUNNING | 9 |
| PREPARING | 11 |
| PENDING | 1 |

---

### GROUP 1: DONE (22 experiments)

#### DONE + SUCCESS (12 experiments)

| exp_id | Hypothesis | Conclusion | Key Metrics | Core Claim |
|--------|-----------|------------|-------------|------------|
| `exp_001_sft_0pct` | 0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores; LoRA r=16 alpha=32 1-epoch | success | (umbrella entry, no metrics) | C1, C2 baseline |
| `exp_001_sft_0pct_05B` | (implicit: 0% clean 0.5B s42) | success | final_loss=1.4894, mean_train_loss=1.5388, token_acc=0.682, time=52.9min | C1 baseline |
| `exp_001_sft_0pct_05B_s123` | 0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation) | success | train_loss=1.5393, token_acc=0.676, time=54.5min | C1 baseline |
| `exp_001_sft_0pct_15B` | (implicit: 0% clean 1.5B s42) | success | final_loss=1.2039, mean_train_loss=1.2599, token_acc=0.711, time=101.5min | C1 baseline |
| `exp_001_sft_0pct_15B_s123` | 0% dosage clean baseline Qwen2.5-1.5B seed=123 | success | train_loss=1.2602, token_acc=0.731, time=101.5min | C1 baseline |
| `exp_001_sft_0pct_3B` | (implicit: 0% clean 3B s42) | success | final_loss=1.0736, mean_train_loss=1.1306, token_acc=0.734, time=214.7min | C1 baseline |
| `exp_001_sft_0pct_3B_s123` | 0% dosage clean baseline Qwen2.5-3B seed=123 | success | final_loss=1.114, mean_train_loss=1.1309, token_acc=0.7505, time=213.1min, total_tokens=19555717 | C1 baseline |
| `exp_001_sft_d005_05B_v3` | 5% dosage contaminated SFT on 0.5B s42 (v3, correct GPU 5). Minimum contamination level for dose-response threshold. | success | final_loss=1.478, mean_train_loss=1.5424, token_acc=0.667, time=56.14min, delta vs baseline: loss=-0.0114, acc=-0.015 | C1, C2 |
| `exp_001_sft_d100_05B` | 100% dosage contaminated SFT on 0.5B s42: maximum contamination upper bound | success | final_loss=1.5943, mean_train_loss=1.5662, token_acc=0.666, time=68.9min, loss_delta=+1.8%, acc_delta=-2.3% | C1, C2 |
| `exp_001_sft_injection` | Controlled SFT contamination injection produces dose-dependent score inflation; 4PL+γ IRT can recover true performance | success | mmlu_total=14042, mmlu_qc_pass=6596 (47%), arc_total=1172, arc_qc_pass=697 (59.5%), gsm8k_total=1319, gsm8k_qc_pass=228 (17.3%), humaneval_total=164 | C1, C2, C3 |
| `mvp_sim_4pl_gamma` | 4PL+γ IRT model separates contamination (γ) from ability (θ) on synthetic data | success | gamma_mean=0.466, gamma_rel_bias=0.068, CI covers true, CI excludes zero, theta_corr=0.943, theta_rmse=0.238, max_rhat=1.003, 0% divergent, time=1407.5s. **PASS** | C3 |
| `mvp_sim_confounding` | 4PL+γ IRT separates γ from θ when exposure confounded with ability (corr≈0.4) | success | gamma_mean=0.5386, gamma_rel_bias=0.0771, CI covers true, CI excludes zero, theta_corr=0.9733, theta_rmse=0.2407, residual_exp_corr=0.0582, max_rhat=1.007, 0% divergent, time=832s. **PASS** | C3 |

#### DONE + FAILED (8 experiments)

| exp_id | Hypothesis | Conclusion | Notes |
|--------|-----------|------------|-------|
| `exp_001_eval_05B_d000_s42` | 0% dosage 0.5B s42 baseline eval on 4 benchmarks | failed | No metrics |
| `exp_001_eval_05B_d100` | (implicit: 100% dosage 0.5B eval) | failed | No metrics |
| `exp_001_eval_15B_d000_s42` | 0% dosage 1.5B s42 baseline eval | failed | No metrics |
| `exp_001_sft_100pct_05B` | 100% contamination dosage 0.5B upper bound | failed | No metrics, no GPU/PID assigned |
| `exp_001_sft_d005_05B_v2` | 5% dosage 0.5B retry after v1 OOM | failed | GPU 5 conflict |
| `exp_001_sft_d100_15B` | 100% dosage 1.5B max contamination, mid-size model scale effect | failed | No metrics |
| `exp_005_noise_prop` | Measurement error propagation through 4PL+γ IRT; analytical ME model vs latent-τ model | failed | Local CPU |
| `exp_005_noise_prop_v2` | Same as exp_005 v2: fixes sigma_e lower bound, c/d bounds, max_treedepth=12 | failed | Still failed after fixes |

#### DONE + OTHER conclusions (2 experiments)

| exp_id | Hypothesis | Conclusion | Metrics |
|--------|-----------|------------|---------|
| `exp_001_eval_05B_d000_s123` | (implicit: 0% 0.5B s123 eval) | success | mmlu_acc=0.4182, gsm8k_em=0.3404, arc_acc=0.3976, humaneval_p@1=0.1037 |
| `exp_001_sft_d005_05B` | 5% dosage 0.5B s42: minimum contamination level | killed | OOM on GPU 5 |

---

### GROUP 2: RUNNING (9 experiments)

| exp_id | Hypothesis | Server / GPU | Critical? |
|--------|-----------|-------------|-----------|
| `exp_001_eval_05B_d000_s42_v5` | 0% dosage 0.5B s42 baseline eval (v5, final clean submit) | cqa1-21977 / cuda:2 | **YES** — needed for C1 calibration error baseline (0.5B s42 clean eval still missing) |
| `exp_001_eval_05B_d005` | (implicit: 5% dosage 0.5B eval) | cqa1-21977 / cuda:1 | **YES** — C2 dose-response: 5% contamination eval results needed |
| `exp_001_eval_05B_d100_v5` | 100% dosage 0.5B s42 contaminated eval (v5, final clean submit) | cqa1-21977 / cuda:2 | **YES** — C1 upper bound: 100% contamination eval results needed |
| `exp_001_eval_15B_d000_s123` | (implicit: 0% 1.5B s123 eval) | cqa1-21977 / cuda:5 | **YES** — C1 multi-scale: 1.5B baseline eval for cross-scale calibration |
| `exp_001_eval_15B_d000_s42_v2` | (implicit: 0% 1.5B s42 eval v2) | cqa1-21977 / cuda:4 | **YES** — C1 baseline: 1.5B s42 eval (v1 failed) |
| `exp_001_eval_3B_d000_s123` | (implicit: 0% 3B s123 eval) | cqa1-21977 / cuda:3 | **YES** — C1 multi-scale: 3B s123 baseline eval |
| `exp_001_eval_3B_d000_s42` | 0% dosage 3B s42 baseline eval on 4 benchmarks | cqa1-21977 / cuda:1 | **YES** — C1 multi-scale: 3B s42 baseline eval |
| `exp_001_sft_d100_15B_v2` | (implicit: 100% dosage 1.5B SFT retry) | cqa1-21977 / cuda:0 | **YES** — C2 dose-response: 1.5B 100% contaminated model training (v1 failed) |
| `exp_004_sim_sweep` | 4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); minimum AUC threshold where γ 95% CI width >15pp | local CPU | **YES** — C3 identifiability: robustness/sensitivity analysis of core model |

**All 9 RUNNING experiments are critical.** They represent the eval pipeline for all three model scales (0.5B, 1.5B, 3B), the contaminated training for 1.5B, and the simulation sweep for identifiability claims.

---

### GROUP 3: PREPARING (11 experiments)

| exp_id | Hypothesis | Conclusion | Notes |
|--------|-----------|------------|-------|
| `exp_001_eval_05B_d000_s42_v2` | (implicit: 0% 0.5B s42 eval v2) | failed | Superseded by v5/v6 |
| `exp_001_eval_05B_d000_s42_v3` | 0% 0.5B s42 eval v3, fixed evaluate.py | killed | Superseded |
| `exp_001_eval_05B_d000_s42_v4` | 0% 0.5B s42 eval v4, clean re-submit | killed | Superseded |
| `exp_001_eval_05B_d000_s42_v6` | 0% 0.5B s42 eval v6, GPU 2 clean state | killed | Superseded by v5 (RUNNING) |
| `exp_001_eval_05B_d100_v3` | 100% 0.5B s42 contaminated eval v3, fixed evaluate.py | killed | Superseded |
| `exp_001_eval_05B_d100_v4` | 100% 0.5B s42 contaminated eval v4, clean re-submit | killed | Superseded |
| `exp_001_eval_05B_d100_v6` | 100% 0.5B s42 contaminated eval v6, GPU 2 clean state | killed | Superseded by v5 (RUNNING) |
| `exp_001_eval_3B_d000_s42_v2` | (implicit: 3B s42 eval v2) | failed | Superseded |
| `exp_001_eval_3B_d000_s42_v3` | 3B s42 baseline eval v3 (v2 was SIGKILLed) | (none) | No server/GPU assigned, waiting for resources |
| `exp_001_sft_d005_05B_r3` | 5% dosage 0.5B s42, retry #3 after v1/v2 OOM | killed | Superseded by v3 (DONE+success) |
| `exp_001_sft_d005_15B` | (implicit: 5% dosage 1.5B SFT) | (none) | **CRITICAL — NOT YET STARTED.** No server/GPU/PID. Needed for C2 dose-response at 1.5B scale |

---

### GROUP 4: PENDING (1 experiment)

| exp_id | Hypothesis | Conclusion | Notes |
|--------|-----------|------------|-------|
| `exp_001_eval_05B_d100_v2` | (implicit: 100% 0.5B eval v2) | failed | Superseded by v5 (RUNNING) |

---

### Core Claim Mapping

**C1 — Calibration (contamination inflates scores, IRT can correct):**
- Baselines: All `sft_0pct_*` (DONE, success) — 6 models trained across 0.5B/1.5B/3B x 2 seeds
- Eval baselines: `eval_05B_d000_s123` (DONE, success with metrics), all other evals RUNNING
- Contaminated training: `sft_d100_05B` (DONE, success), `sft_d005_05B_v3` (DONE, success), `sft_d100_15B_v2` (RUNNING)
- Contaminated eval: `eval_05B_d100_v5` (RUNNING), `eval_05B_d005` (RUNNING)
- Data injection: `sft_injection` (DONE, success)

**C2 — Signal Survival (dose-response curve):**
- 0.5B dose-response: 0% (DONE), 5% (DONE), 100% (DONE) — training complete
- 0.5B eval: 0% s123 (DONE), 0% s42 (RUNNING), 5% (RUNNING), 100% (RUNNING)
- 1.5B: 0% training (DONE), 100% training (RUNNING), 5% training (`sft_d005_15B` PREPARING, not started)
- 3B: 0% training (DONE), no contaminated training registered yet

**C3 — Identifiability (4PL+γ IRT separates γ from θ):**
- `mvp_sim_4pl_gamma` (DONE, PASS) — synthetic recovery works
- `mvp_sim_confounding` (DONE, PASS) — confounded exposure still separable
- `exp_004_sim_sweep` (RUNNING) — robustness/sensitivity sweep
- `exp_005_noise_prop` (DONE, failed) — measurement error propagation
- `exp_005_noise_prop_v2` (DONE, failed) — retry also failed

---

### Critical Flags

1. **`exp_001_sft_d005_15B` (PREPARING, no resources assigned)** — 5% dosage 1.5B SFT has not started. This is needed for the dose-response curve at 1.5B scale (C2). Without it, the paper can only show dose-response for 0.5B.

2. **All 9 RUNNING experiments are critical** — they represent the entire evaluation pipeline. Without these completing successfully, there are no benchmark scores (MMLU/GSM8K/ARC/HumanEval) for any contaminated or baseline models except `eval_05B_d000_s123`.

3. **`exp_005_noise_prop` and `exp_005_noise_prop_v2` both FAILED** — The measurement error propagation analysis (C3 supporting evidence) has not succeeded in 2 attempts. The analytical ME model approach may need fundamental rethinking.

4. **`exp_001_sft_d100_15B` failed, retry `v2` is RUNNING** — The 1.5B 100% contaminated model training has been flaky; if v2 also fails, there will be no contaminated 1.5B model.

5. **No 3B contaminated experiments registered at all** — The registry has 0% baselines for 3B but zero contaminated (5% or 100%) training experiments for 3B scale. This limits cross-scale analysis to 0.5B and (maybe) 1.5B only.

6. **Only 1 eval has actual benchmark metrics** — `exp_001_eval_05B_d000_s123` is the sole evaluation with recorded MMLU/GSM8K/ARC/HumanEval scores. Everything else either failed or is still running.

agentId: a85fc8f4df600f241 (use SendMessage with to: 'a85fc8f4df600f241' to continue this agent)
&lt;usage>total_tokens: 32855
tool_uses: 9
duration_ms: 142896&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "ca1fbef5-5b34-4977-9455-709d39a0d0a2",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Analyze the experiment registry data at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/db3cbd2f-05b2-4fca-84f4-22e20f10b90f/tool-results/mcp-agent-ml-research-read_registry-1778727956223.txt\n\nThis is JSON with schema: {result: string}. The inner result is also a JSON string that needs parsing.\n\nI need you to extract and report:\n1. A table of ALL experiments with: exp_id, name/title, status (DONE/RUNNING/PLANNED/FAILED etc.), conclusion (if any), key metrics\n2. Group experiments by status\n3. For each experiment, note which Core Claim it supports (C1=Calibration, C2=Signal Survival, C3=Identifiability)\n4. Flag any experiments that are RUNNING or PLANNED that are critical\n\nUse jq or python to parse. Report everything verbatim — don't summarize away detail.",
    "agentId": "a85fc8f4df600f241",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data. Here is the complete report.\n\n---\n\n## Experiment Registry Analysis — contamcal-irt-calibration\n\n**Total experiments: 43**\n\n### Status Summary\n\n| Status | Count |\n|--------|-------|\n| DONE | 22 |\n| RUNNING | 9 |\n| PREPARING | 11 |\n| PENDING | 1 |\n\n---\n\n### GROUP 1: DONE (22 experiments)\n\n#### DONE + SUCCESS (12 experiments)\n\n| exp_id | Hypothesis | Conclusion | Key Metrics | Core Claim |\n|--------|-----------|------------|-------------|------------|\n| `exp_001_sft_0pct` | 0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores; LoRA r=16 alpha=32 1-epoch | success | (umbrella entry, no metrics) | C1, C2 baseline |\n| `exp_001_sft_0pct_05B` | (implicit: 0% clean 0.5B s42) | success | final_loss=1.4894, mean_train_loss=1.5388, token_acc=0.682, time=52.9min | C1 baseline |\n| `exp_001_sft_0pct_05B_s123` | 0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation) | success | train_loss=1.5393, token_acc=0.676, time=54.5min | C1 baseline |\n| `exp_001_sft_0pct_15B` | (implicit: 0% clean 1.5B s42) | success | final_loss=1.2039, mean_train_loss=1.2599, token_acc=0.711, time=101.5min | C1 baseline |\n| `exp_001_sft_0pct_15B_s123` | 0% dosage clean baseline Qwen2.5-1.5B seed=123 | success | train_loss=1.2602, token_acc=0.731, time=101.5min | C1 baseline |\n| `exp_001_sft_0pct_3B` | (implicit: 0% clean 3B s42) | success | final_loss=1.0736, mean_train_loss=1.1306, token_acc=0.734, time=214.7min | C1 baseline |\n| `exp_001_sft_0pct_3B_s123` | 0% dosage clean baseline Qwen2.5-3B seed=123 | success | final_loss=1.114, mean_train_loss=1.1309, token_acc=0.7505, time=213.1min, total_tokens=19555717 | C1 baseline |\n| `exp_001_sft_d005_05B_v3` | 5% dosage contaminated SFT on 0.5B s42 (v3, correct GPU 5). Minimum contamination level for dose-response threshold. | success | final_loss=1.478, mean_train_loss=1.5424, token_acc=0.667, time=56.14min, delta vs baseline: loss=-0.0114, acc=-0.015 | C1, C2 |\n| `exp_001_sft_d100_05B` | 100% dosage contaminated SFT on 0.5B s42: maximum contamination upper bound | success | final_loss=1.5943, mean_train_loss=1.5662, token_acc=0.666, time=68.9min, loss_delta=+1.8%, acc_delta=-2.3% | C1, C2 |\n| `exp_001_sft_injection` | Controlled SFT contamination injection produces dose-dependent score inflation; 4PL+γ IRT can recover true performance | success | mmlu_total=14042, mmlu_qc_pass=6596 (47%), arc_total=1172, arc_qc_pass=697 (59.5%), gsm8k_total=1319, gsm8k_qc_pass=228 (17.3%), humaneval_total=164 | C1, C2, C3 |\n| `mvp_sim_4pl_gamma` | 4PL+γ IRT model separates contamination (γ) from ability (θ) on synthetic data | success | gamma_mean=0.466, gamma_rel_bias=0.068, CI covers true, CI excludes zero, theta_corr=0.943, theta_rmse=0.238, max_rhat=1.003, 0% divergent, time=1407.5s. **PASS** | C3 |\n| `mvp_sim_confounding` | 4PL+γ IRT separates γ from θ when exposure confounded with ability (corr≈0.4) | success | gamma_mean=0.5386, gamma_rel_bias=0.0771, CI covers true, CI excludes zero, theta_corr=0.9733, theta_rmse=0.2407, residual_exp_corr=0.0582, max_rhat=1.007, 0% divergent, time=832s. **PASS** | C3 |\n\n#### DONE + FAILED (8 experiments)\n\n| exp_id | Hypothesis | Conclusion | Notes |\n|--------|-----------|------------|-------|\n| `exp_001_eval_05B_d000_s42` | 0% dosage 0.5B s42 baseline eval on 4 benchmarks | failed | No metrics |\n| `exp_001_eval_05B_d100` | (implicit: 100% dosage 0.5B eval) | failed | No metrics |\n| `exp_001_eval_15B_d000_s42` | 0% dosage 1.5B s42 baseline eval | failed | No metrics |\n| `exp_001_sft_100pct_05B` | 100% contamination dosage 0.5B upper bound | failed | No metrics, no GPU/PID assigned |\n| `exp_001_sft_d005_05B_v2` | 5% dosage 0.5B retry after v1 OOM | failed | GPU 5 conflict |\n| `exp_001_sft_d100_15B` | 100% dosage 1.5B max contamination, mid-size model scale effect | failed | No metrics |\n| `exp_005_noise_prop` | Measurement error propagation through 4PL+γ IRT; analytical ME model vs latent-τ model | failed | Local CPU |\n| `exp_005_noise_prop_v2` | Same as exp_005 v2: fixes sigma_e lower bound, c/d bounds, max_treedepth=12 | failed | Still failed after fixes |\n\n#### DONE + OTHER conclusions (2 experiments)\n\n| exp_id | Hypothesis | Conclusion | Metrics |\n|--------|-----------|------------|---------|\n| `exp_001_eval_05B_d000_s123` | (implicit: 0% 0.5B s123 eval) | success | mmlu_acc=0.4182, gsm8k_em=0.3404, arc_acc=0.3976, humaneval_p@1=0.1037 |\n| `exp_001_sft_d005_05B` | 5% dosage 0.5B s42: minimum contamination level | killed | OOM on GPU 5 |\n\n---\n\n### GROUP 2: RUNNING (9 experiments)\n\n| exp_id | Hypothesis | Server / GPU | Critical? |\n|--------|-----------|-------------|-----------|\n| `exp_001_eval_05B_d000_s42_v5` | 0% dosage 0.5B s42 baseline eval (v5, final clean submit) | cqa1-21977 / cuda:2 | **YES** — needed for C1 calibration error baseline (0.5B s42 clean eval still missing) |\n| `exp_001_eval_05B_d005` | (implicit: 5% dosage 0.5B eval) | cqa1-21977 / cuda:1 | **YES** — C2 dose-response: 5% contamination eval results needed |\n| `exp_001_eval_05B_d100_v5` | 100% dosage 0.5B s42 contaminated eval (v5, final clean submit) | cqa1-21977 / cuda:2 | **YES** — C1 upper bound: 100% contamination eval results needed |\n| `exp_001_eval_15B_d000_s123` | (implicit: 0% 1.5B s123 eval) | cqa1-21977 / cuda:5 | **YES** — C1 multi-scale: 1.5B baseline eval for cross-scale calibration |\n| `exp_001_eval_15B_d000_s42_v2` | (implicit: 0% 1.5B s42 eval v2) | cqa1-21977 / cuda:4 | **YES** — C1 baseline: 1.5B s42 eval (v1 failed) |\n| `exp_001_eval_3B_d000_s123` | (implicit: 0% 3B s123 eval) | cqa1-21977 / cuda:3 | **YES** — C1 multi-scale: 3B s123 baseline eval |\n| `exp_001_eval_3B_d000_s42` | 0% dosage 3B s42 baseline eval on 4 benchmarks | cqa1-21977 / cuda:1 | **YES** — C1 multi-scale: 3B s42 baseline eval |\n| `exp_001_sft_d100_15B_v2` | (implicit: 100% dosage 1.5B SFT retry) | cqa1-21977 / cuda:0 | **YES** — C2 dose-response: 1.5B 100% contaminated model training (v1 failed) |\n| `exp_004_sim_sweep` | 4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); minimum AUC threshold where γ 95% CI width >15pp | local CPU | **YES** — C3 identifiability: robustness/sensitivity analysis of core model |\n\n**All 9 RUNNING experiments are critical.** They represent the eval pipeline for all three model scales (0.5B, 1.5B, 3B), the contaminated training for 1.5B, and the simulation sweep for identifiability claims.\n\n---\n\n### GROUP 3: PREPARING (11 experiments)\n\n| exp_id | Hypothesis | Conclusion | Notes |\n|--------|-----------|------------|-------|\n| `exp_001_eval_05B_d000_s42_v2` | (implicit: 0% 0.5B s42 eval v2) | failed | Superseded by v5/v6 |\n| `exp_001_eval_05B_d000_s42_v3` | 0% 0.5B s42 eval v3, fixed evaluate.py | killed | Superseded |\n| `exp_001_eval_05B_d000_s42_v4` | 0% 0.5B s42 eval v4, clean re-submit | killed | Superseded |\n| `exp_001_eval_05B_d000_s42_v6` | 0% 0.5B s42 eval v6, GPU 2 clean state | killed | Superseded by v5 (RUNNING) |\n| `exp_001_eval_05B_d100_v3` | 100% 0.5B s42 contaminated eval v3, fixed evaluate.py | killed | Superseded |\n| `exp_001_eval_05B_d100_v4` | 100% 0.5B s42 contaminated eval v4, clean re-submit | killed | Superseded |\n| `exp_001_eval_05B_d100_v6` | 100% 0.5B s42 contaminated eval v6, GPU 2 clean state | killed | Superseded by v5 (RUNNING) |\n| `exp_001_eval_3B_d000_s42_v2` | (implicit: 3B s42 eval v2) | failed | Superseded |\n| `exp_001_eval_3B_d000_s42_v3` | 3B s42 baseline eval v3 (v2 was SIGKILLed) | (none) | No server/GPU assigned, waiting for resources |\n| `exp_001_sft_d005_05B_r3` | 5% dosage 0.5B s42, retry #3 after v1/v2 OOM | killed | Superseded by v3 (DONE+success) |\n| `exp_001_sft_d005_15B` | (implicit: 5% dosage 1.5B SFT) | (none) | **CRITICAL — NOT YET STARTED.** No server/GPU/PID. Needed for C2 dose-response at 1.5B scale |\n\n---\n\n### GROUP 4: PENDING (1 experiment)\n\n| exp_id | Hypothesis | Conclusion | Notes |\n|--------|-----------|------------|-------|\n| `exp_001_eval_05B_d100_v2` | (implicit: 100% 0.5B eval v2) | failed | Superseded by v5 (RUNNING) |\n\n---\n\n### Core Claim Mapping\n\n**C1 — Calibration (contamination inflates scores, IRT can correct):**\n- Baselines: All `sft_0pct_*` (DONE, success) — 6 models trained across 0.5B/1.5B/3B x 2 seeds\n- Eval baselines: `eval_05B_d000_s123` (DONE, success with metrics), all other evals RUNNING\n- Contaminated training: `sft_d100_05B` (DONE, success), `sft_d005_05B_v3` (DONE, success), `sft_d100_15B_v2` (RUNNING)\n- Contaminated eval: `eval_05B_d100_v5` (RUNNING), `eval_05B_d005` (RUNNING)\n- Data injection: `sft_injection` (DONE, success)\n\n**C2 — Signal Survival (dose-response curve):**\n- 0.5B dose-response: 0% (DONE), 5% (DONE), 100% (DONE) — training complete\n- 0.5B eval: 0% s123 (DONE), 0% s42 (RUNNING), 5% (RUNNING), 100% (RUNNING)\n- 1.5B: 0% training (DONE), 100% training (RUNNING), 5% training (`sft_d005_15B` PREPARING, not started)\n- 3B: 0% training (DONE), no contaminated training registered yet\n\n**C3 — Identifiability (4PL+γ IRT separates γ from θ):**\n- `mvp_sim_4pl_gamma` (DONE, PASS) — synthetic recovery works\n- `mvp_sim_confounding` (DONE, PASS) — confounded exposure still separable\n- `exp_004_sim_sweep` (RUNNING) — robustness/sensitivity sweep\n- `exp_005_noise_prop` (DONE, failed) — measurement error propagation\n- `exp_005_noise_prop_v2` (DONE, failed) — retry also failed\n\n---\n\n### Critical Flags\n\n1. **`exp_001_sft_d005_15B` (PREPARING, no resources assigned)** — 5% dosage 1.5B SFT has not started. This is needed for the dose-response curve at 1.5B scale (C2). Without it, the paper can only show dose-response for 0.5B.\n\n2. **All 9 RUNNING experiments are critical** — they represent the entire evaluation pipeline. Without these completing successfully, there are no benchmark scores (MMLU/GSM8K/ARC/HumanEval) for any contaminated or baseline models except `eval_05B_d000_s123`.\n\n3. **`exp_005_noise_prop` and `exp_005_noise_prop_v2` both FAILED** — The measurement error propagation analysis (C3 supporting evidence) has not succeeded in 2 attempts. The analytical ME model approach may need fundamental rethinking.\n\n4. **`exp_001_sft_d100_15B` failed, retry `v2` is RUNNING** — The 1.5B 100% contaminated model training has been flaky; if v2 also fails, there will be no contaminated 1.5B model.\n\n5. **No 3B contaminated experiments registered at all** — The registry has 0% baselines for 3B but zero contaminated (5% or 100%) training experiments for 3B scale. This limits cross-scale analysis to 0.5B and (maybe) 1.5B only.\n\n6. **Only 1 eval has actual benchmark metrics** — `exp_001_eval_05B_d000_s123` is the sole evaluation with recorded MMLU/GSM8K/ARC/HumanEval scores. Everything else either failed or is still running."
      }
    ],
    "totalDurationMs": 142896,
    "totalTokens": 32855,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 28105,
      "output_tokens": 4349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 400
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4349,
          "cache_read_input_tokens": 28105,
          "cache_creation_input_tokens": 400,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 400,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 3,
      "searchCount": 0,
      "bashCount": 6,
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
Now I have all the information needed. Let me compile the analysis report.

Key findings:
1. Paper framing is well-defined with 3 core claims
2. Registry has 43 experiments: 22 DONE (12 success, 8 failed, 2 other), 9 RUNNING, 11 PREPARING, 1 PENDING
3. experiment_plan has 13 experiments (P0: 7, P1: 4, P2: 2)
4. literature_map.yaml doesn't exist
5. Many critical gaps exist

Let me now map what's done vs what's needed.


For the controlled SFT injection experiment, the plan calls for 45 training runs across 3 model scales and 5 dosage levels with 3 random seeds, but the actual progress is sparse—only 4 models completed for the smallest scale at specific dosages and seeds, while the 1.5B scale is still running with nothing finished yet. There's a mismatch between the planned 3 seeds and what's actually in the registry, and most dosage levels and seed combinations are missing entirely. Looking at the registered experiments more carefully, I see the 15 SFT runs refers to 3 models × 5 dosages, though the plan mentions 3 seeds each for statistics which would be 45 total. The actual registry shows significant gaps: the 0.5B model is missing the 25% and 50% dosage levels entirely, the 1.5B model is missing most dosages beyond 0%, and only the 3B model has clean uncontaminated training data so far.

Beyond the incomplete SFT runs, most of the downstream experiments haven't started yet—the signal pipeline, RRF ablation, calibration baselines, 7B scaling, and multi-family validation are all queued up. The simulation identifiability sweep is currently running, but the noise propagation analysis has already failed twice and needs investigation before moving forward.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "9c54ef07-4b86-4d18-a879-a439bfc1a117",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GWjKaaj62tAxhTmSFbP6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1720,
      "cache_creation_input_tokens": 5155,
      "cache_read_input_tokens": 28969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5155
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

_source line 63_

全部数据已收集。下面是分析报告。

---

## Paper Framing 状态

### Core Claims
| Claim | 内容 | 实验证据就绪度 |
|-------|------|---------------|
| **C1 — Calibration** | 4PL+γ IRT 从被污染的 benchmark score 中恢复真实性能，MAE 显著优于 baselines，coverage 达标 | **无** — exp-006 (IRT calibration) 尚未启动，前置依赖链 exp-002→003→006 全未开始 |
| **C2 — Signal Survival** | 检测信号在 RL 后训练下 cliff-like 退化；RRF fusion 提供鲁棒聚合 | **无** — exp-002 (signal pipeline)、exp-003 (RRF)、exp-008 (signal survival analysis) 均未启动 |
| **C3 — Identifiability** | Fisher Information 分析 + 144-condition simulation 建立最低信号质量阈值 | **部分** — 2 个 MVP simulation 通过 (γ recovery + confounding)；exp-004 sweep RUNNING；exp-005 noise propagation 2次失败 |

---

## 实验覆盖矩阵

### experiment_plan 定义 vs registry 实际状态

| 实验 | 优先级 | 计划状态 | Registry 状态 | 阻塞情况 |
|------|--------|---------|--------------|---------|
| **exp-001** SFT injection | P0 | 3 scale × 5 dosage = 15 runs | 训练: 8 DONE, 1 RUNNING; 评估: 1 DONE, 7 RUNNING | 25%/50% dosage 全未注册; 3B 无污染训练; 1.5B 仅 100% running |
| **exp-002** signal pipeline | P0 | 4 signals × all models | **完全未启动** | 依赖 exp-001 eval 完成 |
| **exp-003** RRF aggregation | P0 | RRF vs ablations | **完全未启动** | 依赖 exp-002 |
| **exp-004** simulation sweep | P0 | 144 conditions | **RUNNING** (CPU) | — |
| **exp-005** noise propagation | P0 | ME model | **2次失败** | 需根本性重新设计 |
| **exp-006** IRT calibration | P0 | 4PL+γ + 7 baselines | **完全未启动** | 依赖 exp-003 (整条链断裂) |
| **exp-007** 7B bridging | P1 | 7B SFT injection | 未启动 | — |
| **exp-008** signal survival | P0 | 4×4 heatmap | **完全未启动** | 依赖 exp-002 |
| **exp-009** RL case study | P1 | observational | 未启动 | 依赖 exp-006 + exp-008 |
| exp-014 multi-family | P1 | Llama/Pythia | 未启动 | — |
| exp-015 QC-only 100% | P1 | 0.5B clean contam | 未启动 | — |

### exp-001 细分覆盖（训练 + 评估）

| Scale | 0% s42 | 0% s123 | 5% | 25% | 50% | 100% |
|-------|--------|---------|-----|-----|-----|------|
| **0.5B train** | DONE | DONE | DONE | — | — | DONE |
| **0.5B eval** | RUNNING | DONE | RUNNING | — | — | RUNNING |
| **1.5B train** | DONE | DONE | PREPARING | — | — | RUNNING |
| **1.5B eval** | RUNNING | RUNNING | — | — | — | — |
| **3B train** | DONE | DONE | — | — | — | — |
| **3B eval** | RUNNING | RUNNING | — | — | — | — |

"—" = 未注册，完全缺失

---

## 文献覆盖

**literature_map.yaml 不存在**。无法评估 direct-competitor 覆盖。paper_framing.md 中列出的引用需求：

- 核心必引：Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Mislevy 1986, Lalor et al. AAAI 2024
- Dream D2 补充（DIF、ML calibration、conformal prediction、data attribution、MIRT）：未知是否已进 bib
- DCR (EMNLP 2025)：唯一 direct competitor，必须对比
- Emperor's New Clothes (ICML 2025)：关键 motivator

建议尽快创建 literature_map.yaml 或检查 .bib 文件完整性。

---

## 关键风险

### 1. 核心依赖链完全断裂（RED）
exp-002 → exp-003 → exp-006 是论文的**核心实验**（C1 Calibration Claim 的唯一证据来源），整条链尚未启动。exp-006 的结果直接产出论文的 headline number。11 天内完成这条链需要：
- exp-001 eval 全部跑完（当前 7 个 RUNNING）
- exp-002 signal pipeline 实现 + 运行 (~20 GPU hrs)
- exp-003 RRF aggregation (~2 GPU hrs)
- exp-006 IRT fitting + 7 baselines (~8 GPU hrs)

最乐观估计需要 5-7 天纯执行时间，不含 debug。

### 2. 25%/50% dosage 实验完全缺失（RED）
paper_framing 要求 "dose-response monotonicity" 作为第 5 个评估指标。当前只有 0%/5%/100% 三个点（且仅 0.5B），25%/50% 从未注册。5 个点的 dose-response curve 至少需要 4 个点才有说服力。

### 3. 3B scale 无污染实验（YELLOW）
C1 声称 "3+ model scales"，但 3B 仅有 clean baselines，无任何污染训练。如果删减到 2 scales (0.5B + 1.5B)，需要修改 claim。

### 4. exp-005 noise propagation 连续失败（YELLOW）
C3 的 measurement error model 是论文的理论亮点之一。2 次实现都失败，需要诊断根因。如果放弃，C3 claim 需降级。

### 5. 11 天内无法完成的实验
- **exp-007 (7B)**：30 GPU hrs 训练 + eval，P1 优先级 → 建议放弃
- **exp-009 (RL case study)**：依赖 exp-006/008 → 时间上不可能
- **exp-012 (72B)**：P2 → 放弃
- **exp-014 (multi-family)**：原定 rebuttal-ready → 保持不变

### 6. 论文 Claim 与 Evidence 的 Gap 总结

| Claim | 所需证据 | 已有 | Gap |
|-------|---------|------|-----|
| C1 headline MAE | exp-006 output | 零 | **致命**：核心 claim 无任何数字支撑 |
| C1 dose-response | 5 dosage × 3 scale eval | 1 eval done | 极大 |
| C2 signal heatmap | exp-008 output | 零 | 大 |
| C2 RRF vs ablations | exp-003 output | 零 | 大 |
| C3 simulation sweep | exp-004 output | RUNNING | 中（等待完成） |
| C3 noise prop | exp-005 output | 失败 | 中 |
| Figures (5 required) | 全部依赖实验结果 | 零 | 致命 |

**底线评估**：以当前进度，11 天内完成 EMNLP 2026 ARR May 25 提交的概率很低。建议立即评估是否转向 fallback venue (AAAI 2027, deadline Jul-Aug 2026)，或大幅削减 scope（例如只用 0.5B single-scale + 3 dosages 做 proof-of-concept）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "uuid": "26e6b7af-314f-4484-95b3-61da0d0467ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GWjKaaj62tAxhTmSFbP6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1720,
      "cache_creation_input_tokens": 5155,
      "cache_read_input_tokens": 28969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5155
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

_source line 64_

全部数据已收集。下面是分析报告。

---

## Paper Framing 状态

### Core Claims
| Claim | 内容 | 实验证据就绪度 |
|-------|------|---------------|
| **C1 — Calibration** | 4PL+γ IRT 从被污染的 benchmark score 中恢复真实性能，MAE 显著优于 baselines，coverage 达标 | **无** — exp-006 (IRT calibration) 尚未启动，前置依赖链 exp-002→003→006 全未开始 |
| **C2 — Signal Survival** | 检测信号在 RL 后训练下 cliff-like 退化；RRF fusion 提供鲁棒聚合 | **无** — exp-002 (signal pipeline)、exp-003 (RRF)、exp-008 (signal survival analysis) 均未启动 |
| **C3 — Identifiability** | Fisher Information 分析 + 144-condition simulation 建立最低信号质量阈值 | **部分** — 2 个 MVP simulation 通过 (γ recovery + confounding)；exp-004 sweep RUNNING；exp-005 noise propagation 2次失败 |

---

## 实验覆盖矩阵

### experiment_plan 定义 vs registry 实际状态

| 实验 | 优先级 | 计划状态 | Registry 状态 | 阻塞情况 |
|------|--------|---------|--------------|---------|
| **exp-001** SFT injection | P0 | 3 scale × 5 dosage = 15 runs | 训练: 8 DONE, 1 RUNNING; 评估: 1 DONE, 7 RUNNING | 25%/50% dosage 全未注册; 3B 无污染训练; 1.5B 仅 100% running |
| **exp-002** signal pipeline | P0 | 4 signals × all models | **完全未启动** | 依赖 exp-001 eval 完成 |
| **exp-003** RRF aggregation | P0 | RRF vs ablations | **完全未启动** | 依赖 exp-002 |
| **exp-004** simulation sweep | P0 | 144 conditions | **RUNNING** (CPU) | — |
| **exp-005** noise propagation | P0 | ME model | **2次失败** | 需根本性重新设计 |
| **exp-006** IRT calibration | P0 | 4PL+γ + 7 baselines | **完全未启动** | 依赖 exp-003 (整条链断裂) |
| **exp-007** 7B bridging | P1 | 7B SFT injection | 未启动 | — |
| **exp-008** signal survival | P0 | 4×4 heatmap | **完全未启动** | 依赖 exp-002 |
| **exp-009** RL case study | P1 | observational | 未启动 | 依赖 exp-006 + exp-008 |
| exp-014 multi-family | P1 | Llama/Pythia | 未启动 | — |
| exp-015 QC-only 100% | P1 | 0.5B clean contam | 未启动 | — |

### exp-001 细分覆盖（训练 + 评估）

| Scale | 0% s42 | 0% s123 | 5% | 25% | 50% | 100% |
|-------|--------|---------|-----|-----|-----|------|
| **0.5B train** | DONE | DONE | DONE | — | — | DONE |
| **0.5B eval** | RUNNING | DONE | RUNNING | — | — | RUNNING |
| **1.5B train** | DONE | DONE | PREPARING | — | — | RUNNING |
| **1.5B eval** | RUNNING | RUNNING | — | — | — | — |
| **3B train** | DONE | DONE | — | — | — | — |
| **3B eval** | RUNNING | RUNNING | — | — | — | — |

"—" = 未注册，完全缺失

---

## 文献覆盖

**literature_map.yaml 不存在**。无法评估 direct-competitor 覆盖。paper_framing.md 中列出的引用需求：

- 核心必引：Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Mislevy 1986, Lalor et al. AAAI 2024
- Dream D2 补充（DIF、ML calibration、conformal prediction、data attribution、MIRT）：未知是否已进 bib
- DCR (EMNLP 2025)：唯一 direct competitor，必须对比
- Emperor's New Clothes (ICML 2025)：关键 motivator

建议尽快创建 literature_map.yaml 或检查 .bib 文件完整性。

---

## 关键风险

### 1. 核心依赖链完全断裂（RED）
exp-002 → exp-003 → exp-006 是论文的**核心实验**（C1 Calibration Claim 的唯一证据来源），整条链尚未启动。exp-006 的结果直接产出论文的 headline number。11 天内完成这条链需要：
- exp-001 eval 全部跑完（当前 7 个 RUNNING）
- exp-002 signal pipeline 实现 + 运行 (~20 GPU hrs)
- exp-003 RRF aggregation (~2 GPU hrs)
- exp-006 IRT fitting + 7 baselines (~8 GPU hrs)

最乐观估计需要 5-7 天纯执行时间，不含 debug。

### 2. 25%/50% dosage 实验完全缺失（RED）
paper_framing 要求 "dose-response monotonicity" 作为第 5 个评估指标。当前只有 0%/5%/100% 三个点（且仅 0.5B），25%/50% 从未注册。5 个点的 dose-response curve 至少需要 4 个点才有说服力。

### 3. 3B scale 无污染实验（YELLOW）
C1 声称 "3+ model scales"，但 3B 仅有 clean baselines，无任何污染训练。如果删减到 2 scales (0.5B + 1.5B)，需要修改 claim。

### 4. exp-005 noise propagation 连续失败（YELLOW）
C3 的 measurement error model 是论文的理论亮点之一。2 次实现都失败，需要诊断根因。如果放弃，C3 claim 需降级。

### 5. 11 天内无法完成的实验
- **exp-007 (7B)**：30 GPU hrs 训练 + eval，P1 优先级 → 建议放弃
- **exp-009 (RL case study)**：依赖 exp-006/008 → 时间上不可能
- **exp-012 (72B)**：P2 → 放弃
- **exp-014 (multi-family)**：原定 rebuttal-ready → 保持不变

### 6. 论文 Claim 与 Evidence 的 Gap 总结

| Claim | 所需证据 | 已有 | Gap |
|-------|---------|------|-----|
| C1 headline MAE | exp-006 output | 零 | **致命**：核心 claim 无任何数字支撑 |
| C1 dose-response | 5 dosage × 3 scale eval | 1 eval done | 极大 |
| C2 signal heatmap | exp-008 output | 零 | 大 |
| C2 RRF vs ablations | exp-003 output | 零 | 大 |
| C3 simulation sweep | exp-004 output | RUNNING | 中（等待完成） |
| C3 noise prop | exp-005 output | 失败 | 中 |
| Figures (5 required) | 全部依赖实验结果 | 零 | 致命 |

**底线评估**：以当前进度，11 天内完成 EMNLP 2026 ARR May 25 提交的概率很低。建议立即评估是否转向 fallback venue (AAAI 2027, deadline Jul-Aug 2026)，或大幅削减 scope（例如只用 0.5B single-scale + 3 dosages 做 proof-of-concept）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 246996,
  "duration_api_ms": 268884,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "total_cost_usd": 0.7490057999999999,
  "usage": {
    "input_tokens": 1726,
    "cache_creation_input_tokens": 22283,
    "cache_read_input_tokens": 88230,
    "output_tokens": 4618,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 22283,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1720,
        "output_tokens": 3457,
        "cache_read_input_tokens": 28969,
        "cache_creation_input_tokens": 5155,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5155
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1267,
      "outputTokens": 1981,
      "cacheReadInputTokens": 19283,
      "cacheCreationInputTokens": 24941,
      "webSearchRequests": 0,
      "costUSD": 0.04427655,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1738,
      "outputTokens": 11977,
      "cacheReadInputTokens": 254216,
      "cacheCreationInputTokens": 43121,
      "webSearchRequests": 0,
      "costUSD": 0.70472925,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a5930d71-734c-46a6-b65b-163c045228c8"
}
```

</details>

---
