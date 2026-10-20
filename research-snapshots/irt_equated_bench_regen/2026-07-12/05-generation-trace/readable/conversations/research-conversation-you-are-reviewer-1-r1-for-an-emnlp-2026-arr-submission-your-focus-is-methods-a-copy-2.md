# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus is **Methods and Experiments**. Produce a structure

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a410ea337430c7406.jsonl`
- **Structured JSON:** [`9e2c580575d932669566.json`](../../sessions/9e/9e2c580575d932669566.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-21T15:06:52.879Z_

You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus is **Methods and Experiments**. Produce a structured review following the ARR format with scores at the end.

## Venue Calibration (EMNLP 2026 via ARR)
- Overall Assessment scale: 5=Award (top 2.5%), 4.5=Borderline Award, 4=Conference accept, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit
- Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5)
- Accept rate: ~21% for Main conference
- Auto-reject signals: anonymity violation, over page limit, missing Limitations section, hallucinated citations

## Paper Summary
**Title:** "Temporal Item Instability in LLM Benchmarks: A Large-Scale Differential Item Functioning Analysis"

**Core idea:** Apply Mantel-Haenszel DIF analysis from psychometrics to the METABENCH response matrix (5,227 models × 12,508 MMLU items), splitting models into 2023 (reference, N=1,080) vs 2024-H1 (focal, N=807) temporal cohorts. Main finding: 31.3% of MMLU items show large DIF (ETS C class, |Δ_MH|≥1.5).

**4 Claims:**
1. **Empirical discovery at unprecedented scale**: 31.3% temporal instability, robust to threshold choice, multiple testing, architecture; replicated across 6 benchmarks (17.9–31.3%).
2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 against Li et al. labels is expected, not failure.
3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000) provides reusable infrastructure for validating any item-level detector. Portable across benchmarks (GSM8K ΔTPR=+0.818).
4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=−8 to −49σ vs random) but are the least disruptive non-random removal strategy (z=−9.5 vs accuracy-gap z=−157). Simpson's paradox: domain improvement marginally predicts DIF (OR=1.55) but reverses (OR=0.73) after controlling for item properties.

**Structure (7 pages + appendices A–F):**
- §1 Introduction
- §2 Related Work
- §3 Method: §3.1 MH-DIF Analysis, §3.2 Semi-Synthetic Validation Framework (cross-subject matching innovation)
- §4 Experiments: §4.1 Temporal DIF on MMLU (core result, permutation null, robustness checks, ability control, within-family, domain specificity), §4.2 Cross-Benchmark Replication (6 benchmarks), §4.3 Ground Truth Meta-Critique and Semi-Synthetic Validation, §4.4 Downstream Impact and Diagnostic Analysis (ranking redundancy, Simpson's paradox, DIF item characterization)
- §5 Discussion and Limitations (RL models N=13, IRT model fit, causal interpretation, semi-synthetic simplification, unexecuted comparisons)
- §6 Conclusion
- Appendix A: RL Robustness Analysis (alignment-RL N=477, reasoning-RL N=13)
- Appendix B: Cumulative Bayesian DIF (simulation, 4 administrations)
- Appendix C: Graceful Degradation (5–50% replacement rates)
- Appendix D: Item-Focused Trees (continuous temporal covariate)
- Appendix E: Bifactor IRT Equating Pilot (failed convergence)
- Appendix F: Not-Executed Experiments (ConStat, DVD, ensemble, item generation)

**Key Tables:**
- Table 1: Temporal DIF on MMLU (C%=31.3% vs random 0.18%)
- Table 2: Cross-benchmark temporal DIF (6 benchmarks, C% 17.9–31.3%)
- Table 3: Semi-synthetic validation (ΔTPR by injection rate, ΔFPR=0.000 for cross-subject matching)
- Table 4: Logistic regression decomposition (Simpson's paradox: OR reversal from 1.55 to 0.73)
- Tables 5–6 in appendix (Bayesian DIF power, graceful degradation)

**Key Numbers:**
- Permutation null: z=237.2, p<0.001, 66.6× enrichment over null mean
- Ability cohort control: C%=2.9% (enrichment=1.19), confirming temporal specificity
- Within-family (Llama-2 vs Llama-3): C%=61.3%, Jaccard with temporal=0.28
- BH FDR correction: removes only 3 of 3,918 C-class items
- Architecture: 99.98% decoder-only, excluding 1 encoder changes nothing
- GSM1K correlation: r=−0.478 (negative, opposite to contamination hypothesis), N=33
- ρ=0.997 ranking stability after DIF-item removal
- Cross-subject matching: ΔFPR=0.000 across all subjects; within-subject: +0.186

## Experiment Design Reference (from review_context.yaml)
The full experimental plan included these experiments. The paper may not cover all of them:

1. **plan_001 (real_data_dif_mmlu)**: EXECUTED. Core MMLU DIF analysis. Results match paper.
2. **plan_002 (rl_robustness_validation)**: EXECUTED but underpowered. Alignment-RL N=477 shows negligible change; reasoning-RL N=13 is too small. Traditional detectors (Min-K%, ConStat) degrade on RL models (AUROC drops 0.714→0.528, 0.681→0.513) but DeLong p>0.05 due to N=13.
3. **plan_003a/b/c (ConStat, DVD, ensemble)**: NOT EXECUTED due to GPU budget. Paper pivoted from ensemble detection to diagnostic framing.
4. **plan_004 (cross_benchmark_gsm8k)**: EXECUTED. GSM8K C%=18.9%, ΔTPR=+0.818. GSM1K correlation r=−0.478 (negative), demoted to exploratory. Wide CI [−0.71, −0.16].
5. **plan_005 (bifactor_irt)**: ATTEMPTED AND KILLED. Full 57-subject model failed to converge. Reported in Appendix E.
6. **plan_006 (item_generation)**: BLOCKED by plan_005 failure. Paper pivoted away from regeneration claim.
7. **plan_007 (cumulative_bayesian_dif)**: EXECUTED as simulation only (no real data validation). Appendix B.
8. **plan_008 (graceful_degradation)**: EXECUTED. Appendix C. ρ from 0.999 to 0.971 across 5–50% replacement.
9. **plan_009 (item_focused_trees)**: EXECUTED. Appendix D. 82.3% overlap with MH, R²=0.031.
10. **plan_010 (architecture_stratified_dif)**: EXECUTED. Trivially positive — 99.98% decoder-only.
11. **plan_011 (semi_synthetic)**: EXECUTED. Core validation framework. ΔTPR=+0.508 at p=0.5.
12. **plan_028 (multi_benchmark)**: EXECUTED. 6 benchmarks, C% 17.9–31.3%.
13. **plan_029 (permutation_null)**: EXECUTED. z=237.2, p<0.001. Per-family stratified permutation NOT executed pre-submission.
14. **plan_030 (odds_ratio_regression)**: EXECUTED. Simpson's paradox finding.

## Your Review Task

Evaluate the **methodological soundness** and **experimental rigor**. Specifically assess:

1. **Statistical methodology**: Is MH-DIF correctly applied? Are the ETS thresholds appropriate? Is the stratification by total score valid when IRT fit is poor (CFI=0.681)?
2. **Semi-synthetic validation**: Is the injection mechanism (incorrect→correct flipping) a reasonable proxy for real contamination? Does cross-subject matching genuinely eliminate FPR inflation, or could there be leakage?
3. **Experimental controls**: Are the permutation null, ability cohort control, and within-family analysis sufficient? Is the per-family stratified permutation a critical missing control?
4. **Cross-benchmark replication**: Does the two-tier pattern (knowledge 27–31% vs skill 18–19%) strengthen or weaken the claim? Is the post-hoc explanation convincing?
5. **Causal claims**: Does the paper appropriately hedge causal language? Is the Simpson's paradox interpretation valid? Could item difficulty be a mediator rather than confounder?
6. **Missing experiments impact**: How much do the unexecuted ConStat/DVD comparisons and the underpowered RL analysis weaken the paper?
7. **Reproducibility**: Is there enough detail to replicate? Is METABENCH publicly available?

Produce your review in this format:

```
## R1 Review: Methods and Experiments

### Summary
[2-3 sentences]

### Strengths
[Numbered list, each with brief explanation]

### Weaknesses
[Numbered list, each with brief explanation]

### Questions for Authors
[Numbered list]

### Minor Issues
[Numbered list]

### Missing References
[Any important missing citations]

### Scores
- Soundness: X/5
- Excitement: X/5
- Reproducibility: X/5
- Overall Assessment: X.X (with label from the scale)
- Confidence: X/5
```

Be rigorous but fair. Calibrate to EMNLP 2026 standards where ~21% of submissions are accepted to Main and another ~15-20% to Findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "cc4c2080-831a-4f9a-a1ac-97239b57f832",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T15:06:52.885Z_

```json
{
  "parentUuid": "cc4c2080-831a-4f9a-a1ac-97239b57f832",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "53e9cc50-2c75-47e8-832b-16b8cb751c9d",
  "timestamp": "2026-05-21T15:06:52.885Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T15:06:56.032Z_



I'll start by reading the paper and key supporting files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53e9cc50-2c75-47e8-832b-16b8cb751c9d",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvTMeQiYzrAUsMZban6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dedd989-b2fe-4023-8291-edb7050efeb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHSALJr46rFoPbEUE1FNDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17590,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17590,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T15:06:57.289Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GySaL38pLuyXr4rexzwUYb`</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dedd989-b2fe-4023-8291-edb7050efeb4",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvTMeQiYzrAUsMZban6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92d682dd-9152-4f56-b98b-38964486c979",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHSALJr46rFoPbEUE1FNDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17590,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17590,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T15:06:57.312Z_

<details><summary>↩ Tool result · `toolu_01GySaL38pLuyXr4rexzwUYb`</summary>

```text
paper/main.tex
paper/sections/appendix.tex
paper/sections/limitations.tex
paper/sections/conclusion.tex
paper/sections/introduction.tex
paper/math_commands.tex
paper/sections/method.tex
paper/sections/related_work.tex
paper/sections/abstract.tex
paper/sections/discussion.tex
paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92d682dd-9152-4f56-b98b-38964486c979",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "efc6b221-5b26-4409-b61b-9e03c7bcf82a",
  "sourceToolAssistantUUID": "92d682dd-9152-4f56-b98b-38964486c979",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T15:06:58.230Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019FzUJwf2woKgvRwWkhkXuf`</summary>

```json
{
  "pattern": "paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efc6b221-5b26-4409-b61b-9e03c7bcf82a",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvTMeQiYzrAUsMZban6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b15d569-c60e-4bf6-9202-2f95ecbfbc13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHSALJr46rFoPbEUE1FNDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17590,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17590,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T15:06:58.259Z_

<details><summary>↩ Tool result · `toolu_019FzUJwf2woKgvRwWkhkXuf`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b15d569-c60e-4bf6-9202-2f95ecbfbc13",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "0be290df-baec-48c3-b78f-8d092e2dca06",
  "sourceToolAssistantUUID": "0b15d569-c60e-4bf6-9202-2f95ecbfbc13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T15:06:58.644Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KRktAHPbuGxs97tke99GUo`</summary>

```json
{
  "pattern": "artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0be290df-baec-48c3-b78f-8d092e2dca06",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvTMeQiYzrAUsMZban6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00b55547-adc0-44d6-b738-db737efd0042",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHSALJr46rFoPbEUE1FNDR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17590,
      "cache_read_input_tokens": 0,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17590
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 294,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17590,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T15:06:58.672Z_

<details><summary>↩ Tool result · `toolu_01KRktAHPbuGxs97tke99GUo`</summary>

```text
artifacts/metabench_data/benchmark-data/gsm8k_prompts.csv
artifacts/metabench_data/benchmark-data/hellaswag_prompts.csv
artifacts/metabench_data/benchmark-data/truthfulqa_prompts.csv
artifacts/metabench_data/benchmark-data/arc_prompts.csv
artifacts/metabench_data/benchmark-data/arc.csv
artifacts/metabench_data/benchmark-data/gsm8k.csv
artifacts/metabench_data/benchmark-data/hellaswag.csv
artifacts/metabench_data/benchmark-data/truthfulqa.csv
artifacts/metabench_data/benchmark-data/winogrande.csv
artifacts/metabench_data/benchmark-data/mmlu_abstract_algebra_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_abstract_algebra.csv
artifacts/metabench_data/benchmark-data/mmlu_anatomy_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_astronomy_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_anatomy.csv
artifacts/metabench_data/benchmark-data/mmlu_business_ethics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_astronomy.csv
artifacts/metabench_data/benchmark-data/mmlu_business_ethics.csv
artifacts/metabench_data/benchmark-data/mmlu_clinical_knowledge_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_clinical_knowledge.csv
artifacts/metabench_data/benchmark-data/mmlu_college_biology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_chemistry_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_biology.csv
artifacts/metabench_data/benchmark-data/mmlu_college_chemistry.csv
artifacts/metabench_data/benchmark-data/mmlu_college_computer_science_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_computer_science.csv
artifacts/metabench_data/benchmark-data/mmlu_college_mathematics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_medicine_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_mathematics.csv
artifacts/metabench_data/benchmark-data/mmlu_college_physics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_medicine.csv
artifacts/metabench_data/benchmark-data/mmlu_college_physics.csv
artifacts/metabench_data/benchmark-data/mmlu_computer_security_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_computer_security.csv
artifacts/metabench_data/benchmark-data/mmlu_electrical_engineering_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_electrical_engineering.csv
artifacts/metabench_data/benchmark-data/mmlu_global_facts_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_global_facts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_chemistry_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_chemistry.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_computer_science_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_computer_science.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_european_history_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_european_history.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_geography_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_geography.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_macroeconomics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_macroeconomics.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_mathematics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_mathematics.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_physics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_physics.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_psychology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_psychology.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_us_history_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_us_history.csv
artifacts/metabench_data/benchmark-data/mmlu_human_sexuality_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_human_sexuality.csv
artifacts/metabench_data/benchmark-data/mmlu_international_law_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_international_law.csv
artifacts/metabench_data/benchmark-data/mmlu_logical_fallacies_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_logical_fallacies.csv
artifacts/metabench_data/benchmark-data/mmlu_machine_learning_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_machine_learning.csv
artifacts/metabench_data/benchmark-data/mmlu_management_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_management.csv
artifacts/metabench_data/benchmark-data/mmlu_marketing_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_marketing.csv
artifacts/metabench_data/benchmark-data/mmlu_medical_genetics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_medical_genetics.csv
artifacts/metabench_data/benchmark-data/mmlu_miscellaneous_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_disputes_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_miscellaneous.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_disputes.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_scenarios_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_scenarios.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_accounting_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_accounting.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_law_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_law.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_medicine_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_medicine.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_psychology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_psychology.csv
artifacts/metabench_data/benchmark-data/mmlu_public_relations_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_public_relations.csv
artifacts/metabench_data/benchmark-data/mmlu_security_studies_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_security_studies.csv
artifacts/metabench_data/benchmark-data/mmlu_us_foreign_policy_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_us_foreign_policy.csv
artifacts/metabench_data/benchmark-data/mmlu_virology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_virology.csv
artifacts/metabench_data/benchmark-data/mmlu_world_religions_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_world_religions.csv
artifacts/metabench_data/benchmark-data/mmlu_econometrics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_econometrics.csv
artifacts/metabench_data/benchmark-data/mmlu_elementary_mathematics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_elementary_mathematics.csv
artifacts/metabench_data/benchmark-data/mmlu_conceptual_physics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_conceptual_physics.csv
artifacts/metabench_data/benchmark-data/mmlu_formal_logic_prompts.csv
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00b55547-adc0-44d6-b738-db737efd0042",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "ed7bc8b2-a3fe-4f57-8daa-4318130c7f0d",
  "sourceToolAssistantUUID": "00b55547-adc0-44d6-b738-db737efd0042",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T15:07:02.196Z_

<details open><summary>🔧 Tool call — Read · `toolu_017se9pFB5p3D7f1PFzdYeW8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed7bc8b2-a3fe-4f57-8daa-4318130c7f0d",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvTnPC26xy192LCYAkW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "226bd4a3-859a-4a25-9748-fc30e6b3bc95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MF855M7qaLpEbEWynJHCJW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 17590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3602,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T15:07:02.205Z_

<details><summary>↩ Tool result · `toolu_017se9pFB5p3D7f1PFzdYeW8`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "226bd4a3-859a-4a25-9748-fc30e6b3bc95",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "8df4a585-8e16-413d-a71c-8af534e883e7",
  "sourceToolAssistantUUID": "226bd4a3-859a-4a25-9748-fc30e6b3bc95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T15:07:02.668Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T5iS9fFt2jMQRHkFnsm3pH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8df4a585-8e16-413d-a71c-8af534e883e7",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvTnPC26xy192LCYAkW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7975997-3169-43ca-8460-2ee8dedabfae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MF855M7qaLpEbEWynJHCJW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 17590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3602,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T15:07:02.673Z_

<details><summary>↩ Tool result · `toolu_01T5iS9fFt2jMQRHkFnsm3pH`</summary>

```text
1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet the assumption that individual items measure the same construct over time is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (DIF) analysis with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 total items), and find that 17.9--31.3\% of items exhibit large DIF (ETS Category~C; MMLU 95\% bootstrap CI: [29.4\%, 38.1\%]) between 2023 and 2024 model cohorts---knowledge/reasoning benchmarks show higher instability (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$), each 45--174$\times$ above random baselines. This does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of instability is item-specific; a Simpson's paradox in odds ratio regression confirms item properties, not accuracy gains, drive DIF. We expose a validation methodology gap: web-overlap labels measure global exposure, not differential functioning (enrichment $\approx 0.96$). A semi-synthetic injection framework with cross-subject matching preserves detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) with zero false positive inflation. DIF-flagged items concentrate cross-generational discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal), and a difficulty--direction interaction ($\rho = -0.597$) reveals that capability gains concentrate on hard items while easy items erode, suggesting DIF captures temporal construct shift rather than noise. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7975997-3169-43ca-8460-2ee8dedabfae",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "c090f5ae-d475-4bd8-bd79-37f846dbdcd1",
  "sourceToolAssistantUUID": "d7975997-3169-43ca-8460-2ee8dedabfae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T15:07:03.006Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CchzkbdKvCXArapAYYXYzh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c090f5ae-d475-4bd8-bd79-37f846dbdcd1",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvTnPC26xy192LCYAkW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "951edc9a-be63-49c9-a330-bd14c199d367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MF855M7qaLpEbEWynJHCJW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 17590,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3602
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 240,
          "cache_read_input_tokens": 17590,
          "cache_creation_input_tokens": 3602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3602,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T15:07:03.011Z_

<details><summary>↩ Tool result · `toolu_01CchzkbdKvCXArapAYYXYzh`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, and Self-Critique~\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena. Direct comparison confirms near-independence between the two flag sets (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), consistent across contamination subtypes.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Global vs.\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), to our knowledge, the largest-scale DIF analysis on LLM benchmarks. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that MH-DIF is sensitive to differential item behavior when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the 31\% temporal instability cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about LLM benchmark measurement properties, replicated across all six METABENCH benchmarks (\Cref{sec:gsm8k}). MH-DIF detects \emph{that} items function differently across cohorts, not \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts.
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order ($\rho \approx 0.997$). DIF should therefore be understood as a diagnostic lens rather than a quality filter. DIF-flagged items concentrate discriminative signal: removing them degrades ranking discriminability more than random removal ($z = -8\sigma$ to $-49\sigma$ across 21 conditions). Model families show distinctive DIF profiles: Llama-3 derivatives gain a median of ${+}53$ rank positions under stable-item evaluation, while Mistral-based models lose a median of $35$; 25\% of models shift by $|\Delta\mathrm{Rank}| \geq 100$.
18	
19	Our contributions are empirical and methodological, not algorithmic:
20	
21	\begin{enumerate}
22	\item \textbf{Benchmark temporal comparability} (Claim 1): 31\% of MMLU items are functionally unstable across model generations under ETS~C classification; replication across all six METABENCH benchmarks yields C\% $= 17.9$--$31.3\%$ (45--174$\times$ above random baselines), with knowledge/reasoning benchmarks showing higher instability than procedural ones (\Cref{sec:temporal,sec:gsm8k}).
23	
24	\item \textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\citep{li2024contamination} do not provide appropriate ground truth for item-level differential detectors. Direct empirical comparison on 9,229 items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), exposing a validation methodology gap in the contamination detection literature (\Cref{sec:groundtruth}).
25	
26	\item \textbf{Semi-synthetic validation framework} (Claim 3): Controlled injection with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\Cref{sec:semisynthetic,sec:gsm8k}).
27	
28	\item \textbf{DIF as diagnostic lens} (Claim 4): DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal, Jaccard overlap with high-discrimination items $= 0.12$) and exhibit a structured difficulty--direction interaction ($\rho = -0.597$): capability gains concentrate on hard items while easy items erode (\Cref{sec:downstream}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "951edc9a-be63-49c9-a330-bd14c199d367",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "235d5695-3da3-4a7d-882a-aefd451069a8",
  "sourceToolAssistantUUID": "951edc9a-be63-49c9-a330-bd14c199d367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T15:07:06.028Z_

<details open><summary>🔧 Tool call — Read · `toolu_011RmZrb6iybCDnvEuVWD7vH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "235d5695-3da3-4a7d-882a-aefd451069a8",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvU78ox5YaXUzyyxXE8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f676db7a-18f5-449a-9423-fcc7c5e98e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HttCgmrgjAmQRfhvMTuVuK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3243,
      "cache_read_input_tokens": 21192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3243,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T15:07:06.033Z_

<details><summary>↩ Tool result · `toolu_011RmZrb6iybCDnvEuVWD7vH`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$) and computing a common odds ratio across strata. We use $K = 5$ equiprobable strata (quintile-based binning) following ETS recommended practice for large-scale assessments~\citep{donoghue1993mh,clauser1998dif}. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
17	
18	\begin{equation}
19	\label{eq:mh}
20	\alpha_{\mathrm{MH}} = \frac{\displaystyle\sum_{k=1}^{K} A_k D_k \,/\, T_k}{\displaystyle\sum_{k=1}^{K} B_k C_k \,/\, T_k}\,,
21	\end{equation}
22	
23	\noindent where $A_k$ and $B_k$ are the number of correct and incorrect responses in the reference group for stratum $k$, $C_k$ and $D_k$ are the corresponding counts for the focal group, and $T_k$ is the total number of examinees in stratum $k$. Under the null hypothesis of no DIF, $\alpha_{\mathrm{MH}} = 1$. The log odds ratio is converted to the ETS delta scale:
24	
25	\begin{equation}
26	\label{eq:delta}
27	\Delta_{\mathrm{MH}} = -2.35 \ln(\alpha_{\mathrm{MH}})\,.
28	\end{equation}
29	
30	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%.
31	
32	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching} uses the total score on all subjects \emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\Cref{sec:injection}); and (3)~\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on GSM8K items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks.
33	
34	\subsection{Cohort Designs}
35	\label{sec:cohorts}
36	
37	We construct five cohort comparisons: (1)~\emph{Temporal}: 2023 ($N = 1{,}080$) vs.\ 2024 ($N = 807$) models, the primary comparison; (2)~\emph{Ability-quintile}: Q1--Q2 vs.\ Q4--Q5 within the same temporal window, testing whether ability differences alone produce DIF; (3)~\emph{Within-family}: Llama-2 ($N = 161$) vs.\ Llama-3 ($N = 308$), isolating generational changes within a single family; (4)~\emph{Within-subject}: per-subject DIF to test domain concentration; and (5)~\emph{Random split}: two random halves of the 2023 cohort ($N = 540$ each) as a sanity check.
38	
39	\subsection{Semi-Synthetic Injection Framework}
40	\label{sec:injection}
41	
42	To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
43	
44	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation.
45	
46	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this by computing the matching variable from all subjects \emph{other than} the one being tested.
47	
48	\begin{proposition}[Zero FPR under cross-subject matching]
49	\label{prop:fpr}
50	Let $M_i^{(-s)} = \sum_{j \notin s} Y_{ij}$ be the matching variable for examinee $i$ on focal subject $s$. Since the tested item belongs to $s$, it does not contribute to $M_i^{(-s)}$; injecting contamination into $s$ leaves $M_i^{(-s)}$ unchanged. Therefore $\Delta\mathrm{FPR} = 0$ by construction.
51	\end{proposition}
52	
53	Empirically, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains (bootstrap 95\% CI $= [0.000, 0.000]$, 5,000 resamples), while detection power is preserved ($\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$ for four of five subjects). We adopt cross-subject matching as the standard protocol for all semi-synthetic analyses.
54	
55	Diagnostic procedures (Yen's Q3 local independence, domain-specificity analysis, instability decomposition) and statistical details (multiple testing correction, threshold sensitivity, architecture heterogeneity checks) appear in \Cref{app:method_details}.
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f676db7a-18f5-449a-9423-fcc7c5e98e54",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "a8b07569-f4ff-4f7a-928b-d4c7194165cc",
  "sourceToolAssistantUUID": "f676db7a-18f5-449a-9423-fcc7c5e98e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T15:07:06.164Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H3FCSWr6k5fBN9NgE4kQYR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8b07569-f4ff-4f7a-928b-d4c7194165cc",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvU78ox5YaXUzyyxXE8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbc19dc8-f330-4ffc-bf61-17451d1895f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HttCgmrgjAmQRfhvMTuVuK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3243,
      "cache_read_input_tokens": 21192,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3243
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 21192,
          "cache_creation_input_tokens": 3243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3243,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T15:07:06.170Z_

<details><summary>↩ Tool result · `toolu_01H3FCSWr6k5fBN9NgE4kQYR`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A power analysis using empirical MMLU IRT parameters confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$. Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $N = 1{,}000$). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%. Crucially, the temporal cohort ability gap is negligible: Cohen's $d = -0.17$ (below the $|d| = 0.2$ small-effect threshold) with 76.4\% distributional overlap. Under strict 1:1 nearest-neighbor matching ($d \approx -0.010$, $N = 638$ per group, 5 seeds), C\% $= 28.9\% \pm 0.1\%$---a 7.7\% relative reduction from 31.3\%, confirming that at most $\sim$2.4 pp of observed DIF is attributable to ability mismatch.
17	
18	Across all 57 MMLU subjects, C\% ranges from 20.7\% to 48.4\% (mean $\approx 30\%$); within-subject matching on 5 subjects yields 38.1\% as a robustness check (\Cref{tab:temporal_landscape}). While DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), DIF direction exhibits systematic domain dependence: STEM items disproportionately favor 2024 models (55.4\%), while Humanities items favor 2023 models (64.4\%), suggesting model generations improve differentially across knowledge dimensions. Item-level logistic regression shows domain accuracy improvement explains only 2.4 percentage points of 31.3\% C\% (pseudo $R^2 = 0.0007$); 92.4\% of instability is item-specific. Odds ratio regression reveals a Simpson's paradox: domain accuracy improvement positively predicts DIF at the aggregate level ($\mathrm{OR} = 1.55$ per 10 pp, $p = 0.001$) but reverses after controlling for item difficulty and discrimination ($\mathrm{OR} = 0.73$, $p = 0.030$; LR $\chi^2 = 647$), confirming that item properties---not accuracy gains---drive DIF classification. The conclusion is robust across thresholds: C\% $= 48.9\%$ at $|\Delta_{\mathrm{MH}}| \geq 1.0$, $18.3\%$ at $\geq 2.0$, $10.2\%$ at $\geq 2.5$.
19	
20	\begin{table}[t]
21	\centering
22	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. FPR is measured against Li et al.\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}
23	\label{tab:temporal_landscape}
24	\small
25	\resizebox{\columnwidth}{!}{%
26	\begin{tabular}{lcccc}
27	\toprule
28	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & C\% & FPR (clean) & Enrich. \\
29	\midrule
30	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\
31	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,600 / ${\sim}$2,600 & 2.9 & 0.027 & 1.19 \\
32	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
33	Random split (sanity) & 540 / 540 & 0.18 & -- & -- \\
34	Within-subject (avg, 5 subj.) & \textit{varies} & 38.1 & -- & -- \\
35	\bottomrule
36	\end{tabular}}
37	\end{table}
38	
39	\subsection{Ground Truth Mismatch}
40	\label{sec:groundtruth}
41	
42	Direct comparison of DIF flags against the web-overlap labels of \citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (\Cref{tab:temporal_landscape}): DIF-C rates are 30.7\% among web-contaminated items and 31.8\% among clean items. Association tests yield $\phi = 0.012$, $\chi^2 = 1.28$ ($p = 0.258$), and OR $= 1.05$ [0.96, 1.15]; the Jaccard index between flagged sets is 0.206. This near-independence holds across contamination subtypes (input-only enrichment $= 0.986$, input-and-label $= 0.960$). The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \emph{global exposure} (whether an item exists in training corpora), while DIF measures \emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The Li et al.\ labels are the wrong ground truth for a differential method. This near-independence extends to behavioral contamination detectors: the enrichment ratio of $0.964$ and Jaccard overlap of $0.206$ between DIF flags and web-overlap labels imply that any detector validated against these labels---including ConStat~\citep{dekoninck2024constat}---is evaluated on a ground truth orthogonal to differential functioning.
43	
44	\begin{figure}[t]
45	\centering
46	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
47	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
48	\label{fig:dose_response}
49	\end{figure}
50	
51	\subsection{Structural Analysis}
52	\label{sec:structural}
53	
54	Three structural controls fail to reduce temporal C\% below 31\%: matched-ability quintiles, IRT $\theta$-conditioning ($r(\theta, \mathrm{total\ score}) = 0.9986$, FPR $= 0.312$), and within-subject DIF (C\% $= 38.1\%$, exceeding the 25\% bifactor viability threshold). Logistic regression DIF confirms 92.1\% concordance with MH and reveals additional non-uniform DIF (24.8\% at $|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% estimate conservative. Graduated de-duplication ($K{=}10$: 22.7\% vs.\ random 26.8\%; $K{=}20$: 29.1\% vs.\ 30.9\%) confirms family structure does not inflate C\%. Ability-matched within-family analysis reduces Llama-2 vs.\ Llama-3 C\% from 61.3\% to $28.3\% \pm 1.6\%$ (Cohen's $d = -0.99$, overlap $= 0.18$), while temporal matching reduces C\% from 31.3\% to $28.9\% \pm 0.1\%$ ($d = -0.17$, overlap $= 0.76$). The matched C\% values ($\sim$28--29\%) are consistent with each other despite vastly different unmatched rates (61.3\% vs.\ 31.3\%), suggesting that genuine item-level DIF accounts for $\sim$28--29\% of items, with the Llama comparison carrying 33 pp of additional ability confound (54\% reduction) versus only 2.4 pp for temporal cohorts (7.7\% reduction). In total, six alternative explanations were tested and ruled out: ability confounding, model family inflation, IRT $\theta$-conditioning, within-subject effects, aggregate ranking impact, and local item dependence---none reduces C\% below $\sim$28\%, confirming item-level differential functioning. Full details in \Cref{app:structural}.
55	
56	\subsection{Semi-Synthetic Framework Validation}
57	\label{sec:semisynthetic}
58	
59	The critical methodological finding is that the choice of matching strategy determines validity. Cross-subject matching computes the conditioning variable from subjects \emph{other than} the one being tested, achieving $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects while four of five produce $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$. Within-subject matching inflates FPR by ${+}0.186$ on average because the matching variable absorbs part of the injection signal. We adopt cross-subject matching as the standard protocol (\Cref{app:fig_matching}).
60	
61	\subsection{Downstream Impact}
62	\label{sec:downstream}
63	
64	Spearman correlation between full and stable-item rankings is $\rho \approx 0.997$: aggregate model ordering is preserved despite 31\% item instability. DIF-flagged items nonetheless carry more discriminative signal than average ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal across 21 conditions), though a circularity ablation shows DIF-based removal is the \emph{least} disruptive among non-random strategies (Jaccard overlap with high-discrimination items is only 0.12). Individual model families show distinctive DIF profiles: Llama-3 derivatives gain a median of ${+}53$ rank positions (mean ${+}121$), while Mistral-based models lose a median of $35$ (mean $-54$); individual extremes reach ${+}793$ and $-542$ (\Cref{app:fig_downstream}). Overall, 25\% of models shift by $|\Delta\mathrm{Rank}| \geq 100$. These shifts exhibit systematic cohort directionality: removing C-flagged items disproportionately disadvantages 2024 models (mean rank drop $= 73.6$ positions) while 2023 models rise (mean $\Delta\mathrm{rank} = -22.6$), yielding a cohort gap of $96.2$ positions---$40\times$ larger than under random removal of equal count ($2.4$; $t(19) > 4$, $p < 0.001$). This what-if demonstration confirms that DIF items carry concentrated inter-generational discriminative signal; it does not recommend using DIF-cleaned scores for evaluation. \Cref{sec:gsm8k} demonstrates that this instability pattern extends across all six METABENCH benchmarks.
65	
66	\subsection{Cross-Benchmark Validation}
67	\label{sec:gsm8k}
68	
69	Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}). C\% ranges from 17.9\% (HellaSwag) to 31.3\% (MMLU), each 45--174$\times$ above its random-split baseline---none attributable to sampling noise. A task-type dichotomy emerges: knowledge and reasoning benchmarks (MMLU, WinoGrande~\citep{sakaguchi2021winogrande}, TruthfulQA~\citep{lin2022truthfulqa}, ARC~\citep{clark2018arc}) show C\% $= 26.9$--$31.3\%$, while procedural benchmarks (GSM8K, HellaSwag~\citep{zellers2019hellaswag}) show C\% $= 17.9$--$18.9\%$, consistent with knowledge-intensive items being more sensitive to shifts in training data composition across model generations.
70	
71	\begin{table}[t]
72	\centering
73	\caption{Temporal DIF across six METABENCH benchmarks. C\% = ETS~C items ($|\Delta_{\mathrm{MH}}| \geq 1.5$) between 2023 and 2024 cohorts. All six show substantial instability (45--174$\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\% than procedural ones.}
74	\label{tab:cross_benchmark}
75	\small
76	\begin{tabular}{lrrrl}
77	\toprule
78	Benchmark & Items & C\% & Rand.\ C\% & Ratio \\
79	\midrule
80	MMLU & 12{,}508 & 31.3 & 0.18 & 174$\times$ \\
81	WinoGrande & 1{,}267 & 30.3 & 0.32 & 95$\times$ \\
82	TruthfulQA & 817 & 29.7 & 0.37 & 80$\times$ \\
83	ARC & 1{,}172 & 26.9 & 0.60 & 45$\times$ \\
84	GSM8K & 1{,}319 & 18.9 & 0.30 & 63$\times$ \\
85	HellaSwag & 10{,}042 & 17.9 & 0.28 & 64$\times$ \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	On GSM8K specifically, semi-synthetic injection with external matching confirms detection power ($\Delta\mathrm{TPR} = {+}0.514$ at $p = 0.5$; \Cref{app:gsm8k_details}). An exploratory GSM1K analysis ($N = 33$) shows a negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$, $p = 0.005$; partial $r = -0.385$, $p = 0.027$), suggesting DIF captures capability change distinct from memorization (\Cref{app:fig_gsm1k}).
91	
92	Even within a 6-month window (2023-H2 vs.\ 2024-H1), DIF remains substantial (MMLU C\% $= 34.35\%$, 181$\times$; TruthfulQA C\% $= 31.33\%$, 51$\times$ above random baselines).
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbc19dc8-f330-4ffc-bf61-17451d1895f3",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "36f8d284-90a0-46ef-aecc-759a73522dfc",
  "sourceToolAssistantUUID": "bbc19dc8-f330-4ffc-bf61-17451d1895f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T15:07:10.919Z_

<details open><summary>🔧 Tool call — Read · `toolu_015DC6X2jd8egyEYZKbyQZfF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36f8d284-90a0-46ef-aecc-759a73522dfc",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvULdB85DsFQMeYEhLV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19df2ea5-77b1-4e50-9e1a-ee8c74bc3e18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hp7pJQcZBHogAjsY3AZPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7063,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7063,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T15:07:10.924Z_

<details><summary>↩ Tool result · `toolu_015DC6X2jd8egyEYZKbyQZfF`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability extends across all six METABENCH benchmarks (C\% $= 17.9$--$31.3\%$, 45--174$\times$ above baselines; \Cref{tab:cross_benchmark}), with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). The Simpson's paradox (\Cref{sec:temporal}) confirms item properties, not accuracy gains, drive DIF. This does not invalidate ranking ($\rho \approx 0.997$) but signals measurement drift across model generations. The statistical machinery of DIF---originally designed for demographic fairness testing~\citep{holland1988mh}---transfers to temporal cohort comparisons unchanged, requiring only a binary response matrix and cohort labels.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$) exposes a category error: web-overlap labels measure global exposure shared by nearly all MMLU items, so evaluating a differential method against them conflates two phenomena.
13	
14	\subsection{DIF as Diagnostic Lens}
15	\label{sec:disc_diagnostic}
16	
17	The GSM1K correlation ($r = -0.478$, partial $r = -0.385$; \Cref{sec:gsm8k}) provides exploratory evidence that DIF captures behavioral change distinct from memorization. DIF-C items are harder ($d = -0.247$) and more discriminating ($d = 0.230$), with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. Yen's Q3 confirms local dependence does not drive DIF ($r = 0.09$, $p = 0.50$).
18	
19	\subsection{Recommended DIF Audit Protocol}
20	\label{sec:disc_protocol}
21	
22	These findings motivate a benchmark maintenance protocol: (1)~MH-DIF audits whenever $\geq 500$ new models accumulate, using cross-subject matching; (2)~C\% $> 20\%$ triggers item review, with consecutively flagged items labeled ``unstable'' and flip-flopping items tagged ``volatile''; (3)~graduated responses from flag-and-annotate to item rotation. MMLU's C\% $= 31.3\%$ already exceeds this threshold ($\chi^2$ $p = 0.32$).
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19df2ea5-77b1-4e50-9e1a-ee8c74bc3e18",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "c2151393-139e-4f71-8122-1f8264d9771f",
  "sourceToolAssistantUUID": "19df2ea5-77b1-4e50-9e1a-ee8c74bc3e18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T15:07:11.394Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RhUDuBcLyKG7sytrzX5udM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2151393-139e-4f71-8122-1f8264d9771f",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvULdB85DsFQMeYEhLV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6d59215-5811-4500-8a5e-fc8bf30ba40f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hp7pJQcZBHogAjsY3AZPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7063,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7063,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T15:07:11.399Z_

<details><summary>↩ Tool result · `toolu_01RhUDuBcLyKG7sytrzX5udM`</summary>

```text
1	\section*{Limitations}
2	
3	\paragraph{Methodological scope of MH-DIF.}
4	The Mantel-Haenszel procedure detects only \emph{uniform} DIF, where the odds ratio between cohorts is constant across ability strata. Logistic regression DIF analysis reveals an additional 24.8\% of items exhibiting non-uniform DIF ($|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% ETS~C estimate conservative. Future work should apply non-uniform DIF methods (e.g., logistic regression or IRT-based approaches) as the primary analysis to capture the full spectrum of item instability. Critically, MH-DIF is nonparametric and conditions on observed total score, not latent $\theta$---its validity does not depend on IRT model fit~\citep{holland1988mh}. Our Yen's Q3 analysis confirms that local dependence domains do not correlate with DIF domains ($r = 0.09$, $p = 0.50$), further supporting the robustness of the MH procedure in this setting.
5	
6	\paragraph{Ability confounding.}
7	Although the temporal cohort ability gap is negligible (Cohen's $d = -0.17$, overlap $= 76.4\%$) and nearest-neighbor matching confirms that at most 2.4 percentage points of C\% are attributable to ability mismatch, within-family comparisons with large ability gaps (e.g., Llama-2 vs.\ Llama-3, $d = -0.99$) produce substantially inflated C\% (61.3\% unmatched vs.\ 28.3\% matched). Any application of MH-DIF to cohorts with larger ability differences must incorporate ability matching or stratification beyond the standard 5-strata procedure.
8	
9	\paragraph{Sample size requirements.}
10	Our power analysis indicates reliable ETS~C detection requires $N \geq 80$ per cohort. The temporal cohorts (1,080 and 807 models) far exceed this threshold, but the GSM1K correlation analysis ($N = 33$) has limited statistical power (95\% CI $= [-0.71, -0.16]$). The negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$) is exploratory and warrants replication with larger model samples.
11	
12	\paragraph{Contamination vs.\ capability change.}
13	DIF analysis detects \emph{that} items function differently across cohorts but cannot determine \emph{why}. The differential signal may reflect contamination, capability change, training methodology shifts, or interactions among these factors. We present evidence that DIF captures something distinct from memorization (negative GSM1K correlation, semi-synthetic dose-response), but a definitive causal decomposition remains out of reach without access to model training data.
14	
15	\paragraph{Benchmark scope.}
16	We analyze six METABENCH benchmarks (MMLU, WinoGrande, TruthfulQA, ARC, GSM8K, HellaSwag; 27,125 total items), all multiple-choice or short-answer benchmarks scored as binary correct/incorrect. The generalizability to open-ended generation benchmarks (e.g., AlpacaEval, MT-Bench), coding benchmarks (e.g., HumanEval), or benchmarks with non-binary scoring remains untested. The binary response format is a prerequisite for MH-DIF; extending to continuous or partial-credit scoring would require polytomous DIF methods.
17	
18	\paragraph{Temporal cohort definition.}
19	We define cohorts by calendar year of model release (2023 vs.\ 2024), a coarse grouping that aggregates models with diverse training pipelines, data mixtures, and post-training procedures. Finer-grained cohort definitions (e.g., by training data cutoff, model family, or alignment method) might reveal more targeted patterns of item instability but would reduce per-cohort sample sizes and statistical power.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6d59215-5811-4500-8a5e-fc8bf30ba40f",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "2cae1a85-d000-4687-9bbf-af5c01a406f5",
  "sourceToolAssistantUUID": "a6d59215-5811-4500-8a5e-fc8bf30ba40f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T15:07:11.863Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QmFSDuQQGmxvGomkEjoBqy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cae1a85-d000-4687-9bbf-af5c01a406f5",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvULdB85DsFQMeYEhLV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d348f04e-e8d6-4116-b772-b0ce71532126",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hp7pJQcZBHogAjsY3AZPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7063,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7063,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T15:07:11.866Z_

<details><summary>↩ Tool result · `toolu_01QmFSDuQQGmxvGomkEjoBqy`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	MH-DIF analysis of six METABENCH benchmarks (27,125 items, 5,227 models) reveals 17.9--31.3\% temporal item instability (ETS~C); a Simpson's paradox confirms item properties, not accuracy gains, drive DIF. Web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$); our semi-synthetic framework validates detection power ($\Delta\mathrm{FPR} = 0.000$). DIF-flagged items concentrate discriminative information ($z{=}{-}8\sigma$ to ${-}49\sigma$) with a difficulty--direction interaction ($\rho{=}{-}0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring alongside score reporting.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d348f04e-e8d6-4116-b772-b0ce71532126",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "5b74a1f3-c553-414f-a6b1-d73e70d35e04",
  "sourceToolAssistantUUID": "d348f04e-e8d6-4116-b772-b0ce71532126",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T15:07:12.331Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PCtYtsAGaYpY2y69HN1cT6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b74a1f3-c553-414f-a6b1-d73e70d35e04",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvULdB85DsFQMeYEhLV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d72c8a5-eb83-4206-9b52-71c0232f7e4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hp7pJQcZBHogAjsY3AZPm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7063,
      "cache_read_input_tokens": 24435,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7063
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 24435,
          "cache_creation_input_tokens": 7063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7063,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T15:07:12.335Z_

<details><summary>↩ Tool result · `toolu_01PCtYtsAGaYpY2y69HN1cT6`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (Claim~2, \Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrated that not all evaluation examples are equally informative. Recent extensions include PSN-IRT \citep{zhou2026psnirt} for benchmark quality at scale, TinyBenchmarks \citep{maiapolo2024tinybenchmarks} for IRT-based item selection, and scalability coefficients for detecting bad benchmark items \citep{hardy2026scalability}. The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which addresses score comparability through fixed-parameter calibration \citep[FPC;][]{kim2019fpc}. Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items violate this assumption.
9	
10	\paragraph{DIF Methodology and Measurement Invariance.}
11	The Mantel-Haenszel procedure for DIF detection was introduced by \citet{holland1988mh} and remains the most widely used method in educational testing due to its simplicity and well-characterized statistical properties \citep{clauser1998dif}. Alternative approaches include logistic regression DIF \citep{swaminathan1990logistic}, SIBTEST \citep{shealy1993sibtest}, Lord's $\chi^2$ test \citep{lord1980irt}, and the Raju area method \citep{raju1988area}; \citet{zumbo1999handbook} provides a comprehensive comparison. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance, vandenberg2000invariance}, which examines whether a measurement instrument functions equivalently across populations. MIMIC models offer a latent-variable approach to the same problem \citep{muthen1985mimic, woods2009mimic}, and \citet{teresi2007dif} reviews DIF methods across applied domains. Cross-subject matching---computing the stratification variable from domains other than the one being tested---has psychometric precedent in the DIF literature \citep{nandakumar1993dif,donoghue1993mh}; our adaptation addresses LLM-specific challenges of multi-domain local dependence and simultaneous contamination control at scale. We do not modify the MH procedure; our contribution is the application context and the empirical findings it reveals. The scale of this analysis (5,227 examinees across a 57-subject multidimensional ability space) exceeds typical educational testing applications, where \citet{belzak2020smallsample} note that DIF methods can behave differently at extreme sample sizes. The primary methodological challenge is the impact-versus-DIF confound: genuine ability differences between temporal cohorts can inflate DIF estimates. We address this through matched-ability quintile analysis, IRT $\theta$-conditioning, and a random-split control (\Cref{sec:temporal}).
12	
13	\paragraph{Benchmark Quality and Design.}
14	The Benchmark Health Index~\citep{liu2026bhi} assesses static benchmark quality; our temporal DIF analysis is complementary, diagnosing \emph{when} measurement properties shift rather than evaluating them at a single snapshot. \citet{maeda2025difllm} predict which item features associate with DIF in educational settings; we instead detect DIF empirically across LLM cohorts at scale. Dynamic benchmarks \citep{kiela2021dynabench, li2024latesteval, white2025livebench} mitigate contamination by construction, yet none provides psychometric equating across versions. Chatbot Arena \citep{chiang2024chatbot} sidesteps static benchmarks through pairwise preference. Broader surveys \citep{chang2024survey, burnell2023rethink} identify benchmark saturation and lack of item-level transparency as systemic challenges that our DIF analysis directly addresses.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d72c8a5-eb83-4206-9b52-71c0232f7e4f",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "35790ef0-fd25-4506-9bd7-fb895e6547a4",
  "sourceToolAssistantUUID": "8d72c8a5-eb83-4206-9b52-71c0232f7e4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T15:07:14.979Z_

<details open><summary>🔧 Tool call — Read · `toolu_015UYEma7n5t1iKPK1XdaiJz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35790ef0-fd25-4506-9bd7-fb895e6547a4",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvUoK2fbF9JiRDwFdYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c05155b-76c8-45da-adb4-8abf22c2519d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014kcfPnptgDtLq4tovHwKL4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3874,
      "cache_read_input_tokens": 31498,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 31498,
          "cache_creation_input_tokens": 3874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3874,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T15:07:14.984Z_

<details><summary>↩ Tool result · `toolu_015UYEma7n5t1iKPK1XdaiJz`</summary>

```text
1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.
19	
20	\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\Delta_{\mathrm{MH}}| \in \{1.0, 1.5, 2.0, 2.5\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\Delta_{\mathrm{MH}}| \geq 1.5$ corresponds to the ETS~C definition used throughout the paper.
21	
22	\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.
23	
24	\section{Structural Analysis Details}
25	\label{app:structural}
26	
27	Three progressively refined approaches fail to reduce the temporal false positive rate below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\% $= 38.1\%$, exceeding the 25\% threshold that would indicate viable bifactor structure. \Cref{tab:structural_comparison} summarizes these results.
28	
29	The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions in Appendix~Figure~A2).
30	
31	\begin{table}[h]
32	\centering
33	\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\%, indicating that the observed instability is not an artifact of ability matching. Subscript $\pm$ values denote standard deviations across 5 injection seeds (baseline row only).}
34	\label{tab:structural_comparison}
35	\small
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{lcccc}
38	\toprule
39	Approach & Mechanism & Temp.\ FPR & TPR ($p{=}0.5$) & Outcome \\
40	\midrule
41	Baseline (ext.) & Cross-bench.\ total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
42	Matched-ability & Within-quintile temp.\ DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
43	$\theta$-cond. & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
44	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
45	\bottomrule
46	\end{tabular}}
47	\end{table}
48	
49	\section{Additional Figures}
50	\label{app:figures}
51	
52	\begin{figure}[h]
53	\centering
54	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
55	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
56	\label{app:fig_matching}
57	\end{figure}
58	
59	\begin{figure}[h]
60	\centering
61	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
62	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}
63	\label{app:fig_downstream}
64	\end{figure}
65	
66	\begin{figure}[h]
67	\centering
68	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
69	\caption{GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items.}
70	\label{app:fig_gsm1k}
71	\end{figure}
72	
73	\section{Cross-Benchmark Comparison}
74	\label{app:gsm8k_details}
75	
76	\begin{table}[h]
77	\centering
78	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
79	\label{tab:gsm8k_comparison}
80	\small
81	\begin{tabular}{lcc}
82	\toprule
83	Metric & MMLU & GSM8K \\
84	\midrule
85	Items & 12,508 & 1,319 \\
86	Models & 5,227 & 6,702 \\
87	Temporal C\% & 31.3\% & 18.9\% \\
88	Sanity C\% & 0.18\% & 0.3\% \\
89	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
90	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c05155b-76c8-45da-adb4-8abf22c2519d",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "8db16862-6122-4aa1-b61a-2856c26ec78b",
  "sourceToolAssistantUUID": "7c05155b-76c8-45da-adb4-8abf22c2519d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T15:07:18.353Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WytTjzq8CwoJc8XjChzp11`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
  "offset": 94
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8db16862-6122-4aa1-b61a-2856c26ec78b",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvUzKKfNoPVWQ17eGmz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f3e2311-5eca-4a1c-a9d2-be40b4b7148e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqoBNroWg5DXwYYNF1evg7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 35372,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2532
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 35372,
          "cache_creation_input_tokens": 2532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2532,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T15:07:18.358Z_

<details><summary>↩ Tool result · `toolu_01WytTjzq8CwoJc8XjChzp11`</summary>

```text
94	
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f3e2311-5eca-4a1c-a9d2-be40b4b7148e",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "121df931-0479-4a08-8bbf-97fd201025e1",
  "sourceToolAssistantUUID": "4f3e2311-5eca-4a1c-a9d2-be40b4b7148e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T15:07:21.074Z_

Now let me check for additional appendix content and review the experiment plan and any relevant artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "121df931-0479-4a08-8bbf-97fd201025e1",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvVEhFrRRdriJNcdNgE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8857a44-d73b-4f01-b22a-bb77e9436a23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcMYK6Kg3ZBNr4N9s9hPju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 127,
      "cache_read_input_tokens": 37904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 127,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T15:07:22.037Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TAzQj43TVjPPFKi6PXNCwr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8857a44-d73b-4f01-b22a-bb77e9436a23",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvVEhFrRRdriJNcdNgE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fed9d31-4067-40e6-b534-35487f7e7aa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcMYK6Kg3ZBNr4N9s9hPju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 127,
      "cache_read_input_tokens": 37904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 127,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T15:07:22.041Z_

<details><summary>↩ Tool result · `toolu_01TAzQj43TVjPPFKi6PXNCwr`</summary>

```text
1	experiments:
2	  # === P0: Headline Results (must run) ===
3	
4	  - id: plan_001
5	    name: real_data_dif_mmlu
6	    claim: 1
7	    description: >
8	      Apply DIF analysis to METABENCH MMLU response matrix (5,219 models × 12,508 items).
9	      Data characteristics: only 37% models classifiable by family (1,929); effective temporal
10	      span ~1.5 years (2023: N=1,253, 2024-H1: N=656); 15.4% items have negative discrimination.
11	      Design:
12	      (a) Primary cohort: temporal split (2023 vs 2024-H1, both N≥80 ✓)
13	      (b) Alternative cohort: accuracy-quintile split (ability-based grouping, uses all models)
14	      (c) Item filtering: run with and without negative-discrimination items (sensitivity analysis)
15	      Run ETS C DIF detection on all items under both cohort definitions.
16	      Proxy validation against Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items,
17	      73.8% coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic
18	      (item exists on web), while DIF detects cohort-differential contamination (item behaves
19	      differently across temporal cohorts). Low concordance is EXPECTED — DIF only catches items
20	      where contamination is differential across cohorts, not uniform. Primary validation metric:
21	      FPR analysis (DIF flags on Li-et-al-clean items) rather than TPR (which conflates uniform
22	      vs differential contamination). Unlabeled items (26.2%) reported separately as "unknown".
23	      plan_011 (semi-synthetic injection) provides controlled ground truth to complement this proxy.
24	      (d) Within-family confound control: run DIF within model families where both versions
25	          have N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)
26	          below threshold — use as supplementary only. Identify additional qualifying pairs from
27	          METABENCH metadata. If DIF flags
28	          items that are NOT differentially contaminated within-family, the flag reflects capability
29	          gain, not contamination. Report: DIF flag overlap between cross-cohort and within-family
30	          analyses to disentangle contamination from capability improvement.
31	      (e) Domain-specificity analysis: correlate DIF flags with MMLU subject categories to check
32	          whether flags cluster in domains with known capability jumps vs known contamination.
33	      Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix +
34	      within-family confound control + domain-specificity analysis.
35	    priority: P0
36	    gpu_budget_hours: 0
37	    deps: []
38	    registry_id: ""
39	
40	  - id: plan_002
41	    name: rl_robustness_validation
42	    claim: 1
43	    description: >
44	      Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:
45	      - "Alignment RL" (DPO/ORPO/KTO) = offline preference optimization, does NOT produce
46	        the NLL gap contraction that Wang et al. demonstrate. METABENCH has 477 such models.
47	      - "Reasoning RL" (GRPO/PPO online training) = the mechanism that conceals contamination
48	        signals. This is what Claim 1 targets. METABENCH has almost none of these.
49	      Design (Reviewer-validated):
50	      (a) SFT-only cohort from METABENCH as baseline
51	      (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH as mechanism control —
52	          DPO doesn't use PPO clipping, so no NLL gap contraction; if DIF works on both
53	          (a) and (b), robustness covers the full RL spectrum
54	      (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference
55	          on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort
56	          (not a standalone group): DIF is group-level, so we verify that adding RL models
57	          to a cohort doesn't degrade detection. Separately, run traditional detectors
58	          (Min-K%, ConStat) on these 10-15 models individually to show per-model degradation.
59	      Two-level validation:
60	      - Group level: DIF flags same items regardless of cohort composition (a/b/c) → robust
61	      - Model level: traditional detectors degrade on (c) individuals → fragile
62	      This design works even with only 10-15 reasoning-RL models because DIF doesn't need
63	      N≥80 RL models — it needs N≥80 in the cohort total, and RL models are mixed in.
64	      Statistical rigor requirements:
65	      - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%)
66	      - DeLong test or permutation test for pairwise AUROC differences
67	      - TOST equivalence testing for DIF retention ratio vs ConStat (not just null-result reasoning)
68	      (d) Partial exploitation power analysis: formally characterize DIF detection power as
69	          function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model answers
70	          memorized items correctly with probability p, shrinking DIF effect size by ~p.
71	          Show detection boundary and ensemble coverage handoff point.
72	    priority: P0
73	    gpu_budget_hours: 100
74	    deps: [plan_001]
75	    registry_id: ""
76	
77	  - id: plan_003a
78	    name: constat_perturbation_eval
79	    claim: 2
80	    description: >
81	      Independent evaluation of ConStat-style perturbation testing on MMLU:
82	      (a) Generate semantically equivalent reformulations for 200+ MMLU items using LLM paraphrasing
83	      (b) Compare model performance on original vs reformulated items
84	      (c) Apply FDR-controlled detection (ConStat protocol)
85	      (d) Characterize detection power by effect size — expected strength on non-RL models, weakness on RL
86	      Even if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.
87	    priority: P0
88	    gpu_budget_hours: 80
89	    deps: [plan_001]
90	    registry_id: ""
91	
92	  - id: plan_003b
93	    name: dvd_generation_variance_eval
94	    claim: 2
95	    description: >
96	      Independent evaluation of DVD generation variance on MMLU:
97	      (a) Select 10-15 open-weight models with inference access
98	      (b) Generate 50 responses per item via temperature sampling (T=0.7-1.0)
99	      (c) Compute generation variance scores; detect bimodal distributions (contamination signal)
100	      (d) Characterize detection power for variant contamination vs verbatim contamination
101	      Standalone results provide variant-contamination detection baseline independent of DIF.
102	    priority: P0
103	    gpu_budget_hours: 70
104	    deps: [plan_001]
105	    registry_id: ""
106	
107	  - id: plan_003c
108	    name: ensemble_fusion
109	    claim: 2
110	    description: >
111	      Fuse DIF + ConStat + DVD into multi-signal ensemble:
112	      (a) Calibrate per-signal thresholds on subset of items with known contamination status
113	      (b) Evaluate 2-of-3 majority voting and weighted fusion strategies
114	      (c) Show ensemble coverage: DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant
115	      (d) Precision analysis: ensemble FPR<0.10 across all configurations
116	      (e) Cross-validate fusion weights (5-fold); report uniform-weight baseline alongside optimized
117	      Depends on 003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.
118	    priority: P0
119	    gpu_budget_hours: 0
120	    deps: [plan_001, plan_003a, plan_003b]
121	    registry_id: ""
122	
123	  # === P1: Strengthening Evidence ===
124	
125	  - id: plan_004
126	    name: cross_benchmark_gsm8k
127	    claim: 1
128	    description: >
129	      Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.
130	      Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard data
131	      or inference). Run DIF across temporal cohorts. Correlate DIF flags with
132	      per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability
133	      and provides an independent ground truth beyond Li et al. proxy labels.
134	    priority: P1
135	    gpu_budget_hours: 100
136	    deps: [plan_001]
137	    registry_id: ""
138	
139	  - id: plan_005
140	    name: bifactor_irt_equating_pilot
141	    claim: 3
142	    description: >
143	      Pilot bifactor IRT equating on MMLU:
144	      NOTE: METABENCH preproc.rds contains CTT statistics (p-value, rpbis), NOT IRT parameters.
145	      True IRT params are in mirt model objects (crossvalidate.R). Must either extract from
146	      METABENCH mirt RDS files or refit from the 5219×12508 response matrix.
147	      (a) Fit bifactor model to METABENCH MMLU data (general factor + subject-specific factors)
148	      (b) Select anchor items (high-stability, no DIF across cohorts)
149	      (c) Calibrate replacement items via fixed-parameter calibration (Kim & Kolen 2019)
150	      (d) Demonstrate equated score equivalence: model rankings on original vs replaced benchmark
151	      should correlate at Spearman rho ≥ 0.95 after equating.
152	    priority: P1
153	    gpu_budget_hours: 50
154	    deps: [plan_001]
155	    registry_id: ""
156	
157	  - id: plan_006
158	    name: item_generation_calibration
159	    claim: 3
160	    description: >
161	      Generate replacement items for DIF-flagged MMLU questions:
162	      (a) Use LLM generation with construct constraints (same subject, same cognitive level)
163	      (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty estimation)
164	      (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45 per arXiv 2602.06631)
165	      vs empirical calibration via student simulation
166	      (d) Validate on holdout model panel
167	    priority: P1
168	    gpu_budget_hours: 200
169	    deps: [plan_005]
170	    registry_id: ""
171	
172	  # === P2: Bonus / Extension ===
173	
174	  - id: plan_007
175	    name: cumulative_bayesian_dif
176	    claim: 1
177	    description: >
178	      Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).
179	      Simulate 4 successive benchmark administrations. Show power improvement
180	      from accumulating evidence: individual administration power ~0.40
181	      → cumulative power ~0.70 after 3 administrations for medium effects (δ=1.0).
182	    priority: P2
183	    gpu_budget_hours: 0
184	    deps: [plan_001]
185	    registry_id: ""
186	
187	  - id: plan_008
188	    name: graceful_degradation_analysis
189	    claim: 3
190	    description: >
191	      Formal analysis of benchmark validity under item replacement:
192	      (a) Define validity metrics (ranking stability, score reliability, construct coverage)
193	      (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced)
194	      (c) Establish theoretical bounds on validity degradation as function of replacement rate
195	      (d) Empirical validation using METABENCH data
196	    priority: P2
197	    gpu_budget_hours: 0
198	    deps: [plan_005, plan_006]
199	    registry_id: ""
200	
201	  - id: plan_009
202	    name: item_focused_trees
203	    claim: 1
204	    description: >
205	      Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative to
206	      categorical cohort DIF. Treat model release date as continuous covariate.
207	      Compare detection power and flexibility vs categorical DIF.
208	      Advantages: avoids arbitrary cohort splits, uses full model sample.
209	    priority: P2
210	    gpu_budget_hours: 0
211	    deps: [plan_001]
212	    registry_id: ""
213	
214	  - id: plan_010
215	    name: architecture_stratified_dif
216	    claim: 1
217	    description: >
218	      Run DIF within architecture-homogeneous subpopulations to test whether
219	      IRT model fit improves and spurious DIF reduces when architecture heterogeneity
220	      is removed. Dream worst-case identified this as the critical missing experiment.
221	      Design:
222	      (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000)
223	      (b) Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup
224	      (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR
225	          vs full-population DIF from plan_001
226	      (d) If fit improves substantially, conclusion is "DIF requires architecture-homogeneous
227	          populations" — a fixable constraint, not a fundamental limitation
228	      Zero GPU cost (uses existing METABENCH data). Proactive defense against worst-case
229	      reviewer concern about unidimensional IRT misfit.
230	    priority: P1
231	    gpu_budget_hours: 0
232	    deps: [plan_001]
233	    registry_id: ""
234	
235	  - id: plan_011
236	    name: semi_synthetic_contamination_validation
237	    claim: 1
238	    description: >
239	      Inject known contamination into the real METABENCH response matrix and measure
240	      DIF detection power under controlled ground truth. Addresses ground truth
241	      circularity concern (Li et al. proxy labels measure existence, not differential contamination).
242	      Design:
243	      (a) Select 500 items with known-clean status (no DIF flags, stable across cohorts)
244	      (b) For a random subset of 100-200 items, inject synthetic contamination:
245	          flip responses of focal-group models from incorrect→correct with probability p
246	          (simulating contamination at varying exploitation rates)
247	      (c) Run DIF detection; measure TPR/FPR against known-injected ground truth
248	      (d) Vary injection parameters: contamination prevalence (5%-30%), exploitation rate
249	          (0.4-1.0), focal group size (N=40-200)
250	      Provides controlled ground truth that proxy labels (Li et al.) and GSM1K cannot.
251	    priority: P1
252	    gpu_budget_hours: 0
253	    deps: [plan_001]
254	    registry_id: ""
255	
256	  # === Dream #6 后续补充实验 (D024) ===
257	
258	  - id: plan_028
259	    name: multi_benchmark_temporal_dif
260	    claim: 1,5
261	    description: >
262	      Check METABENCH for additional benchmark response matrices (ARC-Challenge, HellaSwag,
263	      WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023 vs 2024) on each.
264	      Addresses Dream #6 three-tier consensus: "only MMLU + GSM8K, generalizability insufficient."
265	      Report C% + sample sizes + random-split control for each benchmark.
266	    priority: P0
267	    gpu_budget_hours: 0
268	    deps: [plan_001]
269	    registry_id: ""
270	
271	  - id: plan_029
272	    name: permutation_null_c_rate
273	    claim: 1
274	    description: >
275	      1000× permutation test: randomly reassign 2023/2024 temporal labels (preserving group sizes
276	      N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes null distribution for C%.
277	      Dream #6 three-tier consensus: reviewers ask "is 31% above chance?" Current random-split
278	      control (0.18%) is within-cohort, not temporal permutation null.
279	    priority: P1
280	    gpu_budget_hours: 0
281	    deps: [plan_001]
282	    registry_id: ""
283	
284	  - id: plan_030
285	    name: odds_ratio_regression_transparency
286	    claim: 1
287	    description: >
288	      Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke R² + deviance
289	      ratio. Add finer-grained model: item-level DIF flag ~ item-level accuracy change (per-item
290	      2024-2023 accuracy delta) vs current domain-level predictor. Dream #6 two-tier concern.
291	    priority: P1
292	    gpu_budget_hours: 0
293	    deps: [plan_001]
294	    registry_id: ""
295	
296	# GPU Budget Summary:
297	# P0: 250 hours (plan_001: 0h + plan_002: 100h + plan_003a: 80h + plan_003b: 70h + plan_003c: 0h)
298	# P1: 350 hours (plan_004: 100h + plan_005: 50h + plan_006: 200h + plan_010: 0h + plan_011: 0h)
299	# P2: 0 hours (all simulation/analysis)
300	# Total: 600 hours (within 900-1200h project budget, leaving margin for reruns)
301	# Note: plan_010 (arch-stratified DIF) and plan_011 (semi-synthetic validation) added post-Dream,
302	# both 0 GPU-h (CPU-only analysis on existing METABENCH data)
303	# Claim 2 resilience: if one signal fails, 2-signal ensemble still publishable
304	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fed9d31-4067-40e6-b534-35487f7e7aa7",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "3e54492e-3233-4168-a043-50afb3795340",
  "sourceToolAssistantUUID": "9fed9d31-4067-40e6-b534-35487f7e7aa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T15:07:22.381Z_

<details open><summary>🔧 Tool call — Read · `toolu_0135C2NQvvTiD5miMmHxYJc6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e54492e-3233-4168-a043-50afb3795340",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvVEhFrRRdriJNcdNgE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63ab2124-567a-4ccf-b15d-622ae20a7d2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcMYK6Kg3ZBNr4N9s9hPju",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 127,
      "cache_read_input_tokens": 37904,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 127
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 37904,
          "cache_creation_input_tokens": 127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 127,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T15:07:22.392Z_

<details><summary>↩ Tool result · `toolu_0135C2NQvvTiD5miMmHxYJc6`</summary>

```text
1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: Detection via Variance of Generation Distribution for Variant Contamination},
41	  author        = {Liang, Rongzhen},
42	  year          = {2026},
43	  eprint        = {2601.04895},
44	  archivePrefix = {arXiv},
45	  primaryClass  = {cs.CL},
46	  url           = {https://arxiv.org/abs/2601.04895}
47	}
48	
49	@inproceedings{shi2024mink,
50	  title     = {Detecting Pretraining Data from Large Language Models},
51	  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
52	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
53	  year      = {2024},
54	  url       = {https://arxiv.org/abs/2310.16789}
55	}
56	
57	@inproceedings{tao2026selfcritique,
58	  title     = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},
59	  author    = {Tao, Yixin},
60	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
61	  year      = {2026},
62	  url       = {https://arxiv.org/abs/2510.09259}
63	}
64	
65	@inproceedings{wang2026fragility,
66	  title     = {On The Fragility of Benchmark Contamination Detection in Reasoning Models},
67	  author    = {Wang, Haonan and Li, Haoyang and Ko, Boeun and Zhang, Hongyang},
68	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
69	  year      = {2026},
70	  url       = {https://arxiv.org/abs/2510.02386}
71	}
72	
73	@misc{zhang2024gsm1k,
74	  title         = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},
75	  author        = {Zhang, Hugh},
76	  year          = {2024},
77	  eprint        = {2405.00332},
78	  archivePrefix = {arXiv},
79	  primaryClass  = {cs.CL},
80	  url           = {https://arxiv.org/abs/2405.00332}
81	}
82	
83	@misc{zhang2024minkpp,
84	  title         = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
85	  author        = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
86	  year          = {2024},
87	  eprint        = {2404.02936},
88	  archivePrefix = {arXiv},
89	  primaryClass  = {cs.CL},
90	  url           = {https://arxiv.org/abs/2404.02936}
91	}
92	
93	% ============================================================
94	% IRT Methodology & Equating
95	% ============================================================
96	
97	@inproceedings{rodriguez2021evaluation,
98	  title     = {Evaluation Examples Are Not Equally Informative: How Should That Change {NLP} Leaderboards?},
99	  author    = {Rodriguez, Pedro and Barrow, Joe and Hoyle, Alexander Miserlis and Lalor, John P. and Jia, Robin and Boyd-Graber, Jordan},
100	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63ab2124-567a-4ccf-b15d-622ae20a7d2d",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "08926c57-0c79-42d9-b548-65c0befeb7f7",
  "sourceToolAssistantUUID": "63ab2124-567a-4ccf-b15d-622ae20a7d2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T15:07:27.083Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LMkZ7mHrqA9S4shCDeLYZL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "offset": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08926c57-0c79-42d9-b548-65c0befeb7f7",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvVXypmAtsQMdzRrMrV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b93f544-9c88-4561-96c8-31744399ca3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ER18f6CDWGYxEmLM3Xmhcy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7079,
      "cache_read_input_tokens": 38031,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7079
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 38031,
          "cache_creation_input_tokens": 7079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7079,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T15:07:27.088Z_

<details><summary>↩ Tool result · `toolu_01LMkZ7mHrqA9S4shCDeLYZL`</summary>

```text
100	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
101	  year      = {2021},
102	  pages     = {4486--4503}
103	}
104	
105	@article{donoghue1993mh,
106	  title   = {An Empirical Examination of the {Mantel-Haenszel} Statistic for the Study of Differential Item Functioning},
107	  author  = {Donoghue, John R. and Allen, Nancy L.},
108	  journal = {Applied Measurement in Education},
109	  volume  = {6},
110	  number  = {2},
111	  pages   = {163--179},
112	  year    = {1993}
113	}
114	
115	@misc{hardy2026scalability,
116	  title         = {Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients},
117	  author        = {Hardy, Matthew and Gilbert, Juan and Domingue, Benjamin},
118	  year          = {2026},
119	  eprint        = {2603.24999},
120	  archivePrefix = {arXiv},
121	  primaryClass  = {cs.CL},
122	  url           = {https://arxiv.org/abs/2603.24999}
123	}
124	
125	@article{kim2019fpc,
126	  title   = {Application of {IRT} Fixed Parameter Calibration to Multiple-Group Test Data},
127	  author  = {Kim, Seonghoon and Kolen, Michael},
128	  journal = {Applied Measurement in Education},
129	  year    = {2019},
130	  doi     = {10.1080/08957347.2019.1660344},
131	  url     = {https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344}
132	}
133	
134	@inproceedings{lalor2019irt,
135	  title     = {Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds},
136	  author    = {Lalor, John and Wu, Hao and Yu, Hong},
137	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
138	  year      = {2019},
139	  doi       = {10.18653/v1/D19-1434},
140	  url       = {https://aclanthology.org/D19-1434/}
141	}
142	
143	@inproceedings{vania2021irt,
144	  title     = {Comparing Test Sets with Item Response Theory},
145	  author    = {Vania, Clara and Htut, Phu Mon and Huang, William and Mungra, Dhara and Pang, Richard Yuanzhe and Phang, Jason and Liu, Haokun and Cho, Kyunghyun and Bowman, Samuel R.},
146	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
147	  year      = {2021},
148	  doi       = {10.18653/v1/2021.acl-long.92},
149	  url       = {https://aclanthology.org/2021.acl-long.92/}
150	}
151	
152	@misc{li2025atlas,
153	  title         = {{ATLAS}: Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
154	  author        = {Li, Peiyang and Tang, Xiaobo and Chen, Sai and Cheng, Ying and Metoyer, Ronald and Hua, Tianyi and Chawla, Nitesh V.},
155	  year          = {2025},
156	  eprint        = {2511.04689},
157	  archivePrefix = {arXiv},
158	  primaryClass  = {cs.CL},
159	  url           = {https://arxiv.org/abs/2511.04689}
160	}
161	
162	@misc{chen2025irtnet,
163	  title         = {Learning Compact Representations of {LLM} Abilities via Item Response Theory},
164	  author        = {Chen, Jiayi and Wang, Chao and Zhang, Guoqiang and Ye, Peijin and Bai, Lei and Hu, Wenjun and Qu, Yongchao and Hu, Songlin},
165	  year          = {2025},
166	  eprint        = {2510.00844},
167	  archivePrefix = {arXiv},
168	  primaryClass  = {cs.CL},
169	  url           = {https://arxiv.org/abs/2510.00844}
170	}
171	
172	@misc{choi2026llmjudgeirt,
173	  title         = {Diagnosing the Reliability of {LLM}-as-a-Judge via Item Response Theory},
174	  author        = {Choi, Jiseong and Park, Seonho and Cho, Changwon and Park, Hojun and Kim, Bumsoo},
175	  year          = {2026},
176	  eprint        = {2602.00521},
177	  archivePrefix = {arXiv},
178	  primaryClass  = {cs.CL},
179	  url           = {https://arxiv.org/abs/2602.00521}
180	}
181	
182	@misc{habba2026growingpains,
183	  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
184	  author        = {Habba, Eitam and Itzhak, Ido and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},
185	  year          = {2026},
186	  eprint        = {2604.12843},
187	  archivePrefix = {arXiv},
188	  primaryClass  = {cs.CL},
189	  url           = {https://arxiv.org/abs/2604.12843}
190	}
191	
192	@inproceedings{zhou2026psnirt,
193	  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
194	  author    = {Zhou, Hao and Huang, Heng and Zhao, Zhenheng and Han, Lin and Wang, Haoyu and Chen, Ke and Yang, Min and Bao, Weidong and Dong, Ji and Xu, Bo and Zhu, Changshui and Cao, Huijun and Zhao, Tiejun},
195	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
196	  year      = {2026},
197	  url       = {https://arxiv.org/abs/2505.15055}
198	}
199	
200	% ============================================================
201	% Dynamic Benchmark Design
202	% ============================================================
203	
204	@inproceedings{white2025livebench,
205	  title     = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
206	  author    = {White, Colin},
207	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
208	  year      = {2025},
209	  doi       = {10.48550/arXiv.2406.19314},
210	  url       = {https://arxiv.org/abs/2406.19314}
211	}
212	
213	@misc{kipnis2024metabench,
214	  title         = {metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},
215	  author        = {Kipnis, Alon and Voudouris, Konstantinos and Schulze Buschoff, Luca Maria and Schulz, Eric},
216	  year          = {2024},
217	  eprint        = {2407.12844},
218	  archivePrefix = {arXiv},
219	  primaryClass  = {cs.CL},
220	  url           = {https://arxiv.org/abs/2407.12844}
221	}
222	
223	@inproceedings{hendrycks2021mmlu,
224	  title     = {Measuring Massive Multitask Language Understanding},
225	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
226	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
227	  year      = {2021},
228	  url       = {https://arxiv.org/abs/2009.03300}
229	}
230	
231	@article{liang2023helm,
232	  title   = {Holistic Evaluation of Language Models},
233	  author  = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya},
234	  journal = {Transactions on Machine Learning Research},
235	  year    = {2023},
236	  doi     = {10.1111/nyas.15007},
237	  url     = {https://arxiv.org/abs/2211.09110}
238	}
239	
240	@inproceedings{chiang2024chatbot,
241	  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},
242	  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},
243	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
244	  year      = {2024},
245	  doi       = {10.48550/arXiv.2403.04132},
246	  url       = {https://arxiv.org/abs/2403.04132}
247	}
248	
249	@misc{mialon2023gaia,
250	  title         = {{GAIA}: a benchmark for General {AI} Assistants},
251	  author        = {Mialon, Grégoire and Fourrier, Clémentine and Swift, Craig and Wolf, Thomas and LeCun, Yann and Scialom, Thomas},
252	  year          = {2023},
253	  eprint        = {2311.12983},
254	  archivePrefix = {arXiv},
255	  primaryClass  = {cs.CL},
256	  url           = {https://arxiv.org/abs/2311.12983}
257	}
258	
259	@inproceedings{li2024latesteval,
260	  title     = {{LatestEval}: Addressing Data Contamination in Language Model Evaluation through Dynamic and Time-Sensitive Test Construction},
261	  author    = {Li, Yucheng and Guerin, Frank and Lin, Chenghua},
262	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
263	  year      = {2024},
264	  doi       = {10.48550/arXiv.2312.12343},
265	  url       = {https://arxiv.org/abs/2312.12343}
266	}
267	
268	@inproceedings{kiela2021dynabench,
269	  title     = {{Dynabench}: Rethinking Benchmarking in {NLP}},
270	  author    = {Kiela, Douwe and Bartolo, Max and Nie, Yixin and Kaushik, Divyansh and Geiger, Atticus and Wu, Zhengxuan and Vidgen, Bertie and Prasad, Grusha and Singh, Amanpreet and Ringshia, Pratik and Ma, Zhiyi and Thrush, Tristan and Riedel, Sebastian and Talat, Zeerak and Stenetorp, Pontus and Jia, Robin},
271	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
272	  year      = {2021},
273	  doi       = {10.18653/v1/2021.naacl-main.324},
274	  url       = {https://arxiv.org/abs/2104.14337}
275	}
276	
277	% ============================================================
278	% DIF Statistical Methods
279	% ============================================================
280	
281	@article{belzak2020smallsample,
282	  title   = {Testing Differential Item Functioning in Small Samples},
283	  author  = {Belzak, William},
284	  journal = {Multivariate Behavioral Research},
285	  year    = {2020},
286	  doi     = {10.1080/00273171.2019.1671162},
287	  url     = {https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162}
288	}
289	
290	@incollection{holland1988mh,
291	  title     = {Differential Item Functioning and the {Mantel-Haenszel} Procedure},
292	  author    = {Holland, Paul W. and Thayer, Dorothy T.},
293	  booktitle = {Test Validity},
294	  editor    = {Wainer, Howard and Braun, Henry I.},
295	  publisher = {Lawrence Erlbaum Associates},
296	  year      = {1988},
297	  doi       = {10.1002/j.2330-8516.1986.tb00186.x},
298	  url       = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x}
299	}
300	
301	@article{shealy1993sibtest,
302	  title   = {A Model-Based Standardization Approach that Separates True Bias/{DIF} from Group Ability Differences and Detects Test Bias/{DTF} as Well as Item Bias/{DIF}},
303	  author  = {Shealy, Robin and Stout, William},
304	  journal = {Psychometrika},
305	  year    = {1993},
306	  doi     = {10.1007/BF02294572},
307	  url     = {https://link.springer.com/article/10.1007/BF02294572}
308	}
309	
310	@article{clauser1998dif,
311	  title   = {Using Statistical Procedures to Identify Differentially Functioning Test Items},
312	  author  = {Clauser, Brian E. and Mazor, Kathleen M.},
313	  journal = {Educational Measurement: Issues and Practice},
314	  year    = {1998},
315	  doi     = {10.1111/j.1745-3992.1998.tb00619.x},
316	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x}
317	}
318	
319	@book{zumbo1999handbook,
320	  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},
321	  author    = {Zumbo, Bruno D.},
322	  year      = {1999},
323	  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defense},
324	  address   = {Ottawa},
325	  url       = {https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf}
326	}
327	
328	@article{meredith1993invariance,
329	  title   = {Measurement Invariance, Factor Analysis and Factorial Invariance},
330	  author  = {Meredith, William},
331	  journal = {Psychometrika},
332	  year    = {1993},
333	  doi     = {10.1007/BF02294825},
334	  url     = {https://link.springer.com/article/10.1007/BF02294825}
335	}
336	
337	@article{vandenberg2000invariance,
338	  title   = {A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research},
339	  author  = {Vandenberg, Robert J. and Lance, Charles E.},
340	  journal = {Organizational Research Methods},
341	  year    = {2000},
342	  doi     = {10.1177/109442810031002},
343	  url     = {https://journals.sagepub.com/doi/10.1177/109442810031002}
344	}
345	
346	@article{swaminathan1990logistic,
347	  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},
348	  author  = {Swaminathan, Hariharan and Rogers, H. Jane},
349	  journal = {Journal of Educational Measurement},
350	  year    = {1990},
351	  doi     = {10.1111/j.1745-3984.1990.tb00754.x},
352	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x}
353	}
354	
355	@article{teresi2007dif,
356	  title   = {Differential Item Functioning and Health Assessment},
357	  author  = {Teresi, Jeanne A. and Fleishman, John A.},
358	  journal = {Quality of Life Research},
359	  year    = {2007},
360	  doi     = {10.1007/s11136-007-9184-6},
361	  url     = {https://link.springer.com/article/10.1007/s11136-007-9184-6}
362	}
363	
364	@book{lord1980irt,
365	  title     = {Applications of Item Response Theory to Practical Testing Problems},
366	  author    = {Lord, Frederic M.},
367	  year      = {1980},
368	  publisher = {Lawrence Erlbaum Associates},
369	  address   = {Hillsdale, NJ}
370	}
371	
372	@article{raju1988area,
373	  title   = {The Area between Two Item Characteristic Curves},
374	  author  = {Raju, Nambury S.},
375	  journal = {Psychometrika},
376	  year    = {1988},
377	  doi     = {10.1007/BF02294403},
378	  url     = {https://link.springer.com/article/10.1007/BF02294403}
379	}
380	
381	@article{muthen1985mimic,
382	  title   = {A Method for Studying the Homogeneity of Test Items with Respect to Other Relevant Variables},
383	  author  = {Muth{\'e}n, Bengt},
384	  journal = {Journal of Educational Statistics},
385	  year    = {1985},
386	  doi     = {10.2307/1164966}
387	}
388	
389	@article{woods2009mimic,
390	  title   = {Empirical Selection of Anchors for Tests of Differential Item Functioning},
391	  author  = {Woods, Carol M.},
392	  journal = {Applied Psychological Measurement},
393	  year    = {2009},
394	  doi     = {10.1177/0146621609331279}
395	}
396	
397	% ============================================================
398	% LLM Evaluation Methodology
399	% ============================================================
400	
401	@article{burnell2023rethink,
402	  title   = {Rethink reporting of evaluation results in {AI}},
403	  author  = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Cheke, Lucy G. and Sohl-Dickstein, Jascha and Mitchell, Melanie and Kiela, Douwe and Shanahan, Murray and Voorhees, Ellen M. and Cohn, Anthony G. and Leibo, Joel Z. and Hernandez-Orallo, Jose},
404	  journal = {Science},
405	  year    = {2023},
406	  doi     = {10.1126/science.adf6369},
407	  url     = {https://www.science.org/doi/10.1126/science.adf6369}
408	}
409	
410	@article{chang2024survey,
411	  title   = {A Survey on Evaluation of Large Language Models},
412	  author  = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Zhu, Kaijie and Chen, Hao and Yang, Linyi and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
413	  journal = {ACM Transactions on Intelligent Systems and Technology},
414	  year    = {2024},
415	  doi     = {10.1145/3641289},
416	  url     = {https://dl.acm.org/doi/full/10.1145/3641289}
417	}
418	
419	@inproceedings{maiapolo2024tinybenchmarks,
420	  title     = {{tinyBenchmarks}: evaluating {LLMs} with fewer examples},
421	  author    = {Maia Polo, Felipe and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
422	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
423	  year      = {2024},
424	  url       = {https://proceedings.mlr.press/v235/maia-polo24a.html}
425	}
426	
427	@inproceedings{wang2024mmlupro,
428	  title     = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},
429	  author    = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Xue, Xiang and Chen, Wenhu},
430	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
431	  year      = {2024},
432	  url       = {https://arxiv.org/abs/2406.01574}
433	}
434	
435	@article{ott2022benchmark,
436	  title   = {Mapping global dynamics of benchmark creation and saturation in artificial intelligence},
437	  author  = {Ott, Simon and Barbosa-Silva, Adriano and Blagec, Kathrin and Brauner, Jan and Samwald, Matthias},
438	  journal = {Nature Communications},
439	  year    = {2022},
440	  doi     = {10.1038/s41467-022-34591-0},
441	  url     = {https://www.nature.com/articles/s41467-022-34591-0}
442	}
443	
444	@article{nandakumar1993dif,
445	  author  = {Ratna Nandakumar},
446	  title   = {Simultaneous {DIF} amplification and cancellation: {Shealy}-{Stout}'s test for {DIF}},
447	  journal = {Journal of Educational Measurement},
448	  year    = {1993},
449	  volume  = {30},
450	  number  = {4},
451	  pages   = {293--311}
452	}
453	
454	@inproceedings{carlini2022quantifying,
455	  author    = {Nicholas Carlini and Daphne Ippolito and Matthew Jagielski and Katherine Lee and Florian Tram{\`e}r and Chiyuan Zhang},
456	  title     = {Quantifying Memorization Across Neural Language Models},
457	  booktitle = {International Conference on Learning Representations (ICLR)},
458	  year      = {2023},
459	  url       = {https://arxiv.org/abs/2202.07646}
460	}
461	
462	@inproceedings{tirumala2022memorization,
463	  author    = {Kushal Tirumala and Aram Markosyan and Luke Zettlemoyer and Armen Aghajanyan},
464	  title     = {Memorization Without Overfitting: Analyzing the Training Dynamics of Large Language Models},
465	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
466	  year      = {2022},
467	  url       = {https://arxiv.org/abs/2205.10770}
468	}
469	
470	% ============================================================
471	% Additional Benchmarks
472	% ============================================================
473	
474	@inproceedings{sakaguchi2021winogrande,
475	  title     = {{WinoGrande}: An Adversarial {Winograd} Schema Challenge at Scale},
476	  author    = {Sakaguchi, Keisuke and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
477	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
478	  volume    = {34},
479	  number    = {05},
480	  pages     = {8732--8740},
481	  year      = {2020}
482	}
483	
484	@inproceedings{lin2022truthfulqa,
485	  title     = {{TruthfulQA}: Measuring How Models Mimic Human Falsehoods},
486	  author    = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},
487	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
488	  year      = {2022},
489	  pages     = {3214--3252}
490	}
491	
492	@inproceedings{zellers2019hellaswag,
493	  title     = {{HellaSwag}: Can a Machine Really Finish Your Sentence?},
494	  author    = {Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farzaneh, Ali and Choi, Yejin},
495	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
496	  year      = {2019},
497	  pages     = {4791--4800}
498	}
499	
500	@article{clark2018arc,
501	  title   = {Think you have Solved Question Answering? Try {ARC}, the {AI2} Reasoning Challenge},
502	  author  = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
503	  journal = {arXiv preprint arXiv:1803.05457},
504	  year    = {2018}
505	}
506	
507	% ============================================================
508	% Benchmark Quality Assessment
509	% ============================================================
510	
511	@article{liu2026bhi,
512	  title   = {Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of {LLMs}},
513	  author  = {Liu, Yifan and others},
514	  journal = {arXiv preprint arXiv:2602.11674},
515	  year    = {2026}
516	}
517	
518	@article{maeda2025difllm,
519	  title   = {Finding Words Associated with {DIF}: Predicting {DIF} using {LLMs} and Explainable {AI}},
520	  author  = {Maeda, Hotaka},
521	  journal = {arXiv preprint arXiv:2502.07017},
522	  year    = {2025}
523	}
524	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b93f544-9c88-4561-96c8-31744399ca3d",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "6749a93f-d452-45f9-879e-8bbad5158d5a",
  "sourceToolAssistantUUID": "7b93f544-9c88-4561-96c8-31744399ca3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-21T15:07:31.942Z_

Now let me check whether there are additional appendices mentioned in the paper summary that I haven't seen yet (Appendix A-F were mentioned).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6749a93f-d452-45f9-879e-8bbad5158d5a",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvVtMv9Q7P787NwNLtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e76fd36-5cfc-4b0f-a2b8-5d3da29d40d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NGLB2i4d4aeynPNky43t9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7822,
      "cache_read_input_tokens": 45110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7822,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T15:07:35.074Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BhwhEYsa5GUwHTKVcE3Ybf`</summary>

```json
{
  "pattern": "Appendix [A-F]|\\\\section.*RL Robustness|Bayesian DIF|Graceful Degradation|Item-Focused|Bifactor|Not-Executed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e76fd36-5cfc-4b0f-a2b8-5d3da29d40d5",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvVtMv9Q7P787NwNLtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d87036bb-f095-42c6-93fe-9a13358e3af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NGLB2i4d4aeynPNky43t9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7822,
      "cache_read_input_tokens": 45110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7822,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T15:07:35.101Z_

<details><summary>↩ Tool result · `toolu_01BhwhEYsa5GUwHTKVcE3Ybf`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d87036bb-f095-42c6-93fe-9a13358e3af2",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "474a5a5a-549a-446a-baa6-a1e6cfffefc7",
  "sourceToolAssistantUUID": "d87036bb-f095-42c6-93fe-9a13358e3af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T15:07:35.496Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XW64QTfurS6CTEUp2qwPhj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "474a5a5a-549a-446a-baa6-a1e6cfffefc7",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvVtMv9Q7P787NwNLtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf97744a-ee1f-4c80-ab54-8f3cd9c5e69b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NGLB2i4d4aeynPNky43t9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7822,
      "cache_read_input_tokens": 45110,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7822
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 45110,
          "cache_creation_input_tokens": 7822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7822,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T15:07:35.501Z_

<details><summary>↩ Tool result · `toolu_01XW64QTfurS6CTEUp2qwPhj`</summary>

```text
1	%%%%% NEW MATH DEFINITIONS %%%%%
2	
3	\usepackage{amsmath,amsfonts,bm}
4	\usepackage{amsthm}
5	\newtheorem{proposition}{Proposition}
6	
7	% Mark sections of captions for referring to divisions of figures
8	\newcommand{\figleft}{{\em (Left)}}
9	\newcommand{\figcenter}{{\em (Center)}}
10	\newcommand{\figright}{{\em (Right)}}
11	\newcommand{\figtop}{{\em (Top)}}
12	\newcommand{\figbottom}{{\em (Bottom)}}
13	\newcommand{\captiona}{{\em (a)}}
14	\newcommand{\captionb}{{\em (b)}}
15	\newcommand{\captionc}{{\em (c)}}
16	\newcommand{\captiond}{{\em (d)}}
17	
18	% Highlight a newly defined term
19	\newcommand{\newterm}[1]{{\bf #1}}
20	
21	
22	% Figure reference, lower-case.
23	\def\figref#1{figure~\ref{#1}}
24	% Figure reference, capital. For start of sentence
25	\def\Figref#1{Figure~\ref{#1}}
26	\def\twofigref#1#2{figures \ref{#1} and \ref{#2}}
27	\def\quadfigref#1#2#3#4{figures \ref{#1}, \ref{#2}, \ref{#3} and \ref{#4}}
28	% Section reference, lower-case.
29	\def\secref#1{section~\ref{#1}}
30	% Section reference, capital.
31	\def\Secref#1{Section~\ref{#1}}
32	% Reference to two sections.
33	\def\twosecrefs#1#2{sections \ref{#1} and \ref{#2}}
34	% Reference to three sections.
35	\def\secrefs#1#2#3{sections \ref{#1}, \ref{#2} and \ref{#3}}
36	% Reference to an equation, lower-case.
37	\def\eqref#1{equation~\ref{#1}}
38	% Reference to an equation, upper case
39	\def\Eqref#1{Equation~\ref{#1}}
40	% A raw reference to an equation---avoid using if possible
41	\def\plaineqref#1{\ref{#1}}
42	% Reference to a chapter, lower-case.
43	\def\chapref#1{chapter~\ref{#1}}
44	% Reference to an equation, upper case.
45	\def\Chapref#1{Chapter~\ref{#1}}
46	% Reference to a range of chapters
47	\def\rangechapref#1#2{chapters\ref{#1}--\ref{#2}}
48	% Reference to an algorithm, lower-case.
49	\def\algref#1{algorithm~\ref{#1}}
50	% Reference to an algorithm, upper case.
51	\def\Algref#1{Algorithm~\ref{#1}}
52	\def\twoalgref#1#2{algorithms \ref{#1} and \ref{#2}}
53	\def\Twoalgref#1#2{Algorithms \ref{#1} and \ref{#2}}
54	% Reference to a part, lower case
55	\def\partref#1{part~\ref{#1}}
56	% Reference to a part, upper case
57	\def\Partref#1{Part~\ref{#1}}
58	\def\twopartref#1#2{parts \ref{#1} and \ref{#2}}
59	
60	\def\ceil#1{\lceil #1 \rceil}
61	\def\floor#1{\lfloor #1 \rfloor}
62	\def\1{\bm{1}}
63	\newcommand{\train}{\mathcal{D}}
64	\newcommand{\valid}{\mathcal{D_{\mathrm{valid}}}}
65	\newcommand{\test}{\mathcal{D_{\mathrm{test}}}}
66	
67	\def\eps{{\epsilon}}
68	
69	
70	% Random variables
71	\def\reta{{\textnormal{$\eta$}}}
72	\def\ra{{\textnormal{a}}}
73	\def\rb{{\textnormal{b}}}
74	\def\rc{{\textnormal{c}}}
75	\def\rd{{\textnormal{d}}}
76	\def\re{{\textnormal{e}}}
77	\def\rf{{\textnormal{f}}}
78	\def\rg{{\textnormal{g}}}
79	\def\rh{{\textnormal{h}}}
80	\def\ri{{\textnormal{i}}}
81	\def\rj{{\textnormal{j}}}
82	\def\rk{{\textnormal{k}}}
83	\def\rl{{\textnormal{l}}}
84	% rm is already a command, just don't name any random variables m
85	\def\rn{{\textnormal{n}}}
86	\def\ro{{\textnormal{o}}}
87	\def\rp{{\textnormal{p}}}
88	\def\rq{{\textnormal{q}}}
89	\def\rr{{\textnormal{r}}}
90	\def\rs{{\textnormal{s}}}
91	\def\rt{{\textnormal{t}}}
92	\def\ru{{\textnormal{u}}}
93	\def\rv{{\textnormal{v}}}
94	\def\rw{{\textnormal{w}}}
95	\def\rx{{\textnormal{x}}}
96	\def\ry{{\textnormal{y}}}
97	\def\rz{{\textnormal{z}}}
98	
99	% Random vectors
100	\def\rvepsilon{{\mathbf{\epsilon}}}
101	\def\rvtheta{{\mathbf{\theta}}}
102	\def\rva{{\mathbf{a}}}
103	\def\rvb{{\mathbf{b}}}
104	\def\rvc{{\mathbf{c}}}
105	\def\rvd{{\mathbf{d}}}
106	\def\rve{{\mathbf{e}}}
107	\def\rvf{{\mathbf{f}}}
108	\def\rvg{{\mathbf{g}}}
109	\def\rvh{{\mathbf{h}}}
110	\def\rvu{{\mathbf{i}}}
111	\def\rvj{{\mathbf{j}}}
112	\def\rvk{{\mathbf{k}}}
113	\def\rvl{{\mathbf{l}}}
114	\def\rvm{{\mathbf{m}}}
115	\def\rvn{{\mathbf{n}}}
116	\def\rvo{{\mathbf{o}}}
117	\def\rvp{{\mathbf{p}}}
118	\def\rvq{{\mathbf{q}}}
119	\def\rvr{{\mathbf{r}}}
120	\def\rvs{{\mathbf{s}}}
121	\def\rvt{{\mathbf{t}}}
122	\def\rvu{{\mathbf{u}}}
123	\def\rvv{{\mathbf{v}}}
124	\def\rvw{{\mathbf{w}}}
125	\def\rvx{{\mathbf{x}}}
126	\def\rvy{{\mathbf{y}}}
127	\def\rvz{{\mathbf{z}}}
128	
129	% Elements of random vectors
130	\def\erva{{\textnormal{a}}}
131	\def\ervb{{\textnormal{b}}}
132	\def\ervc{{\textnormal{c}}}
133	\def\ervd{{\textnormal{d}}}
134	\def\erve{{\textnormal{e}}}
135	\def\ervf{{\textnormal{f}}}
136	\def\ervg{{\textnormal{g}}}
137	\def\ervh{{\textnormal{h}}}
138	\def\ervi{{\textnormal{i}}}
139	\def\ervj{{\textnormal{j}}}
140	\def\ervk{{\textnormal{k}}}
141	\def\ervl{{\textnormal{l}}}
142	\def\ervm{{\textnormal{m}}}
143	\def\ervn{{\textnormal{n}}}
144	\def\ervo{{\textnormal{o}}}
145	\def\ervp{{\textnormal{p}}}
146	\def\ervq{{\textnormal{q}}}
147	\def\ervr{{\textnormal{r}}}
148	\def\ervs{{\textnormal{s}}}
149	\def\ervt{{\textnormal{t}}}
150	\def\ervu{{\textnormal{u}}}
151	\def\ervv{{\textnormal{v}}}
152	\def\ervw{{\textnormal{w}}}
153	\def\ervx{{\textnormal{x}}}
154	\def\ervy{{\textnormal{y}}}
155	\def\ervz{{\textnormal{z}}}
156	
157	% Random matrices
158	\def\rmA{{\mathbf{A}}}
159	\def\rmB{{\mathbf{B}}}
160	\def\rmC{{\mathbf{C}}}
161	\def\rmD{{\mathbf{D}}}
162	\def\rmE{{\mathbf{E}}}
163	\def\rmF{{\mathbf{F}}}
164	\def\rmG{{\mathbf{G}}}
165	\def\rmH{{\mathbf{H}}}
166	\def\rmI{{\mathbf{I}}}
167	\def\rmJ{{\mathbf{J}}}
168	\def\rmK{{\mathbf{K}}}
169	\def\rmL{{\mathbf{L}}}
170	\def\rmM{{\mathbf{M}}}
171	\def\rmN{{\mathbf{N}}}
172	\def\rmO{{\mathbf{O}}}
173	\def\rmP{{\mathbf{P}}}
174	\def\rmQ{{\mathbf{Q}}}
175	\def\rmR{{\mathbf{R}}}
176	\def\rmS{{\mathbf{S}}}
177	\def\rmT{{\mathbf{T}}}
178	\def\rmU{{\mathbf{U}}}
179	\def\rmV{{\mathbf{V}}}
180	\def\rmW{{\mathbf{W}}}
181	\def\rmX{{\mathbf{X}}}
182	\def\rmY{{\mathbf{Y}}}
183	\def\rmZ{{\mathbf{Z}}}
184	
185	% Elements of random matrices
186	\def\ermA{{\textnormal{A}}}
187	\def\ermB{{\textnormal{B}}}
188	\def\ermC{{\textnormal{C}}}
189	\def\ermD{{\textnormal{D}}}
190	\def\ermE{{\textnormal{E}}}
191	\def\ermF{{\textnormal{F}}}
192	\def\ermG{{\textnormal{G}}}
193	\def\ermH{{\textnormal{H}}}
194	\def\ermI{{\textnormal{I}}}
195	\def\ermJ{{\textnormal{J}}}
196	\def\ermK{{\textnormal{K}}}
197	\def\ermL{{\textnormal{L}}}
198	\def\ermM{{\textnormal{M}}}
199	\def\ermN{{\textnormal{N}}}
200	\def\ermO{{\textnormal{O}}}
201	\def\ermP{{\textnormal{P}}}
202	\def\ermQ{{\textnormal{Q}}}
203	\def\ermR{{\textnormal{R}}}
204	\def\ermS{{\textnormal{S}}}
205	\def\ermT{{\textnormal{T}}}
206	\def\ermU{{\textnormal{U}}}
207	\def\ermV{{\textnormal{V}}}
208	\def\ermW{{\textnormal{W}}}
209	\def\ermX{{\textnormal{X}}}
210	\def\ermY{{\textnormal{Y}}}
211	\def\ermZ{{\textnormal{Z}}}
212	
213	% Vectors
214	\def\vzero{{\bm{0}}}
215	\def\vone{{\bm{1}}}
216	\def\vmu{{\bm{\mu}}}
217	\def\vtheta{{\bm{\theta}}}
218	\def\va{{\bm{a}}}
219	\def\vb{{\bm{b}}}
220	\def\vc{{\bm{c}}}
221	\def\vd{{\bm{d}}}
222	\def\ve{{\bm{e}}}
223	\def\vf{{\bm{f}}}
224	\def\vg{{\bm{g}}}
225	\def\vh{{\bm{h}}}
226	\def\vi{{\bm{i}}}
227	\def\vj{{\bm{j}}}
228	\def\vk{{\bm{k}}}
229	\def\vl{{\bm{l}}}
230	\def\vm{{\bm{m}}}
231	\def\vn{{\bm{n}}}
232	\def\vo{{\bm{o}}}
233	\def\vp{{\bm{p}}}
234	\def\vq{{\bm{q}}}
235	\def\vr{{\bm{r}}}
236	\def\vs{{\bm{s}}}
237	\def\vt{{\bm{t}}}
238	\def\vu{{\bm{u}}}
239	\def\vv{{\bm{v}}}
240	\def\vw{{\bm{w}}}
241	\def\vx{{\bm{x}}}
242	\def\vy{{\bm{y}}}
243	\def\vz{{\bm{z}}}
244	
245	% Elements of vectors
246	\def\evalpha{{\alpha}}
247	\def\evbeta{{\beta}}
248	\def\evepsilon{{\epsilon}}
249	\def\evlambda{{\lambda}}
250	\def\evomega{{\omega}}
251	\def\evmu{{\mu}}
252	\def\evpsi{{\psi}}
253	\def\evsigma{{\sigma}}
254	\def\evtheta{{\theta}}
255	\def\eva{{a}}
256	\def\evb{{b}}
257	\def\evc{{c}}
258	\def\evd{{d}}
259	\def\eve{{e}}
260	\def\evf{{f}}
261	\def\evg{{g}}
262	\def\evh{{h}}
263	\def\evi{{i}}
264	\def\evj{{j}}
265	\def\evk{{k}}
266	\def\evl{{l}}
267	\def\evm{{m}}
268	\def\evn{{n}}
269	\def\evo{{o}}
270	\def\evp{{p}}
271	\def\evq{{q}}
272	\def\evr{{r}}
273	\def\evs{{s}}
274	\def\evt{{t}}
275	\def\evu{{u}}
276	\def\evv{{v}}
277	\def\evw{{w}}
278	\def\evx{{x}}
279	\def\evy{{y}}
280	\def\evz{{z}}
281	
282	% Matrix
283	\def\mA{{\bm{A}}}
284	\def\mB{{\bm{B}}}
285	\def\mC{{\bm{C}}}
286	\def\mD{{\bm{D}}}
287	\def\mE{{\bm{E}}}
288	\def\mF{{\bm{F}}}
289	\def\mG{{\bm{G}}}
290	\def\mH{{\bm{H}}}
291	\def\mI{{\bm{I}}}
292	\def\mJ{{\bm{J}}}
293	\def\mK{{\bm{K}}}
294	\def\mL{{\bm{L}}}
295	\def\mM{{\bm{M}}}
296	\def\mN{{\bm{N}}}
297	\def\mO{{\bm{O}}}
298	\def\mP{{\bm{P}}}
299	\def\mQ{{\bm{Q}}}
300	\def\mR{{\bm{R}}}
301	\def\mS{{\bm{S}}}
302	\def\mT{{\bm{T}}}
303	\def\mU{{\bm{U}}}
304	\def\mV{{\bm{V}}}
305	\def\mW{{\bm{W}}}
306	\def\mX{{\bm{X}}}
307	\def\mY{{\bm{Y}}}
308	\def\mZ{{\bm{Z}}}
309	\def\mBeta{{\bm{\beta}}}
310	\def\mPhi{{\bm{\Phi}}}
311	\def\mLambda{{\bm{\Lambda}}}
312	\def\mSigma{{\bm{\Sigma}}}
313	
314	% Tensor
315	\DeclareMathAlphabet{\mathsfit}{\encodingdefault}{\sfdefault}{m}{sl}
316	\SetMathAlphabet{\mathsfit}{bold}{\encodingdefault}{\sfdefault}{bx}{n}
317	\newcommand{\tens}[1]{\bm{\mathsfit{#1}}}
318	\def\tA{{\tens{A}}}
319	\def\tB{{\tens{B}}}
320	\def\tC{{\tens{C}}}
321	\def\tD{{\tens{D}}}
322	\def\tE{{\tens{E}}}
323	\def\tF{{\tens{F}}}
324	\def\tG{{\tens{G}}}
325	\def\tH{{\tens{H}}}
326	\def\tI{{\tens{I}}}
327	\def\tJ{{\tens{J}}}
328	\def\tK{{\tens{K}}}
329	\def\tL{{\tens{L}}}
330	\def\tM{{\tens{M}}}
331	\def\tN{{\tens{N}}}
332	\def\tO{{\tens{O}}}
333	\def\tP{{\tens{P}}}
334	\def\tQ{{\tens{Q}}}
335	\def\tR{{\tens{R}}}
336	\def\tS{{\tens{S}}}
337	\def\tT{{\tens{T}}}
338	\def\tU{{\tens{U}}}
339	\def\tV{{\tens{V}}}
340	\def\tW{{\tens{W}}}
341	\def\tX{{\tens{X}}}
342	\def\tY{{\tens{Y}}}
343	\def\tZ{{\tens{Z}}}
344	
345	
346	% Graph
347	\def\gA{{\mathcal{A}}}
348	\def\gB{{\mathcal{B}}}
349	\def\gC{{\mathcal{C}}}
350	\def\gD{{\mathcal{D}}}
351	\def\gE{{\mathcal{E}}}
352	\def\gF{{\mathcal{F}}}
353	\def\gG{{\mathcal{G}}}
354	\def\gH{{\mathcal{H}}}
355	\def\gI{{\mathcal{I}}}
356	\def\gJ{{\mathcal{J}}}
357	\def\gK{{\mathcal{K}}}
358	\def\gL{{\mathcal{L}}}
359	\def\gM{{\mathcal{M}}}
360	\def\gN{{\mathcal{N}}}
361	\def\gO{{\mathcal{O}}}
362	\def\gP{{\mathcal{P}}}
363	\def\gQ{{\mathcal{Q}}}
364	\def\gR{{\mathcal{R}}}
365	\def\gS{{\mathcal{S}}}
366	\def\gT{{\mathcal{T}}}
367	\def\gU{{\mathcal{U}}}
368	\def\gV{{\mathcal{V}}}
369	\def\gW{{\mathcal{W}}}
370	\def\gX{{\mathcal{X}}}
371	\def\gY{{\mathcal{Y}}}
372	\def\gZ{{\mathcal{Z}}}
373	
374	% Sets
375	\def\sA{{\mathbb{A}}}
376	\def\sB{{\mathbb{B}}}
377	\def\sC{{\mathbb{C}}}
378	\def\sD{{\mathbb{D}}}
379	% Don't use a set called E, because this would be the same as our symbol
380	% for expectation.
381	\def\sF{{\mathbb{F}}}
382	\def\sG{{\mathbb{G}}}
383	\def\sH{{\mathbb{H}}}
384	\def\sI{{\mathbb{I}}}
385	\def\sJ{{\mathbb{J}}}
386	\def\sK{{\mathbb{K}}}
387	\def\sL{{\mathbb{L}}}
388	\def\sM{{\mathbb{M}}}
389	\def\sN{{\mathbb{N}}}
390	\def\sO{{\mathbb{O}}}
391	\def\sP{{\mathbb{P}}}
392	\def\sQ{{\mathbb{Q}}}
393	\def\sR{{\mathbb{R}}}
394	\def\sS{{\mathbb{S}}}
395	\def\sT{{\mathbb{T}}}
396	\def\sU{{\mathbb{U}}}
397	\def\sV{{\mathbb{V}}}
398	\def\sW{{\mathbb{W}}}
399	\def\sX{{\mathbb{X}}}
400	\def\sY{{\mathbb{Y}}}
401	\def\sZ{{\mathbb{Z}}}
402	
403	% Entries of a matrix
404	\def\emLambda{{\Lambda}}
405	\def\emA{{A}}
406	\def\emB{{B}}
407	\def\emC{{C}}
408	\def\emD{{D}}
409	\def\emE{{E}}
410	\def\emF{{F}}
411	\def\emG{{G}}
412	\def\emH{{H}}
413	\def\emI{{I}}
414	\def\emJ{{J}}
415	\def\emK{{K}}
416	\def\emL{{L}}
417	\def\emM{{M}}
418	\def\emN{{N}}
419	\def\emO{{O}}
420	\def\emP{{P}}
421	\def\emQ{{Q}}
422	\def\emR{{R}}
423	\def\emS{{S}}
424	\def\emT{{T}}
425	\def\emU{{U}}
426	\def\emV{{V}}
427	\def\emW{{W}}
428	\def\emX{{X}}
429	\def\emY{{Y}}
430	\def\emZ{{Z}}
431	\def\emSigma{{\Sigma}}
432	
433	% entries of a tensor
434	% Same font as tensor, without \bm wrapper
435	\newcommand{\etens}[1]{\mathsfit{#1}}
436	\def\etLambda{{\etens{\Lambda}}}
437	\def\etA{{\etens{A}}}
438	\def\etB{{\etens{B}}}
439	\def\etC{{\etens{C}}}
440	\def\etD{{\etens{D}}}
441	\def\etE{{\etens{E}}}
442	\def\etF{{\etens{F}}}
443	\def\etG{{\etens{G}}}
444	\def\etH{{\etens{H}}}
445	\def\etI{{\etens{I}}}
446	\def\etJ{{\etens{J}}}
447	\def\etK{{\etens{K}}}
448	\def\etL{{\etens{L}}}
449	\def\etM{{\etens{M}}}
450	\def\etN{{\etens{N}}}
451	\def\etO{{\etens{O}}}
452	\def\etP{{\etens{P}}}
453	\def\etQ{{\etens{Q}}}
454	\def\etR{{\etens{R}}}
455	\def\etS{{\etens{S}}}
456	\def\etT{{\etens{T}}}
457	\def\etU{{\etens{U}}}
458	\def\etV{{\etens{V}}}
459	\def\etW{{\etens{W}}}
460	\def\etX{{\etens{X}}}
461	\def\etY{{\etens{Y}}}
462	\def\etZ{{\etens{Z}}}
463	
464	% The true underlying data generating distribution
465	\newcommand{\pdata}{p_{\rm{data}}}
466	% The empirical distribution defined by the training set
467	\newcommand{\ptrain}{\hat{p}_{\rm{data}}}
468	\newcommand{\Ptrain}{\hat{P}_{\rm{data}}}
469	% The model distribution
470	\newcommand{\pmodel}{p_{\rm{model}}}
471	\newcommand{\Pmodel}{P_{\rm{model}}}
472	\newcommand{\ptildemodel}{\tilde{p}_{\rm{model}}}
473	% Stochastic autoencoder distributions
474	\newcommand{\pencode}{p_{\rm{encoder}}}
475	\newcommand{\pdecode}{p_{\rm{decoder}}}
476	\newcommand{\precons}{p_{\rm{reconstruct}}}
477	
478	\newcommand{\laplace}{\mathrm{Laplace}} % Laplace distribution
479	
480	\newcommand{\E}{\mathbb{E}}
481	\newcommand{\Ls}{\mathcal{L}}
482	\newcommand{\R}{\mathbb{R}}
483	\newcommand{\emp}{\tilde{p}}
484	\newcommand{\lr}{\alpha}
485	\newcommand{\reg}{\lambda}
486	\newcommand{\rect}{\mathrm{rectifier}}
487	\newcommand{\softmax}{\mathrm{softmax}}
488	\newcommand{\sigmoid}{\sigma}
489	\newcommand{\softplus}{\zeta}
490	\newcommand{\KL}{D_{\mathrm{KL}}}
491	\newcommand{\Var}{\mathrm{Var}}
492	\newcommand{\standarderror}{\mathrm{SE}}
493	\newcommand{\Cov}{\mathrm{Cov}}
494	% Wolfram Mathworld says $L^2$ is for function spaces and $\ell^2$ is for vectors
495	% But then they seem to use $L^2$ for vectors throughout the site, and so does
496	% wikipedia.
497	\newcommand{\normlzero}{L^0}
498	\newcommand{\normlone}{L^1}
499	\newcommand{\normltwo}{L^2}
500	\newcommand{\normlp}{L^p}
501	\newcommand{\normmax}{L^\infty}
502	
503	\newcommand{\parents}{Pa} % See usage in notation.tex. Chosen to match Daphne's book.
504	
505	\DeclareMathOperator*{\argmax}{arg\,max}
506	\DeclareMathOperator*{\argmin}{arg\,min}
507	
508	\DeclareMathOperator{\sign}{sign}
509	\DeclareMathOperator{\Tr}{Tr}
510	\let\ab\allowbreak
511	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf97744a-ee1f-4c80-ab54-8f3cd9c5e69b",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "43b5b8c1-dc21-4e32-b8b5-dcdad8c227dc",
  "sourceToolAssistantUUID": "cf97744a-ee1f-4c80-ab54-8f3cd9c5e69b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-21T15:07:44.018Z_

I now have a thorough understanding of the paper. Let me also check the report and any additional context files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43b5b8c1-dc21-4e32-b8b5-dcdad8c227dc",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvWW22UK98BCg1vMtxr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f404f3e2-98ef-42cd-8199-ff6a27f4e826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168Jpud23wMNy8CUTdEMgvx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8112,
      "cache_read_input_tokens": 52932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8112,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T15:07:45.831Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GRBjabr8hk324jVLg11a87`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f404f3e2-98ef-42cd-8199-ff6a27f4e826",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvWW22UK98BCg1vMtxr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58d144ba-40ef-445d-bbdf-e863e1f3b759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168Jpud23wMNy8CUTdEMgvx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8112,
      "cache_read_input_tokens": 52932,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8112
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 52932,
          "cache_creation_input_tokens": 8112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8112,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T15:07:45.836Z_

<details><summary>↩ Tool result · `toolu_01GRBjabr8hk324jVLg11a87`</summary>

```text
1	# Handover — 2026-05-21
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	（无）
7	
8	## 待处理
9	- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）
10	
11	## 近期结论
12	- **plan_033_subject_dif_concentration** (success): DIF 在 MMLU 57 个 subject 间分布不均匀，且 STEM vs Humanities 存在系统性差异。控制 item difficulty 和 discrimination 后，特定 subject 的 content 本身预测 DIF 概率——这说明 DIF 不仅由 psychometric properties 驱动，还受知识领域内容特征影响。同时，DIF 的方向（favor 2023 vs 2024）可能在不同领域呈现不同模式。 ← 基于 plan_001_real_data_dif_mmlu
13	- **plan_032_dif_cleaned_mmlu** (success): 虽然 DIF-cleaned MMLU 的全局 rank correlation 很高 (ρ≈0.997)，但局部排名变化将揭示 DIF 的实际影响：特定模型家族（尤其是 2024 年新模型如 phi-3, llama-3）将在移除 C-flagged items 后排名显著下降，而 2023 年模型排名上升。这证明 DIF items 虽然不改变全局趋势，但系统性地偏向特定模型代际，构成 benchmark fairness 问题。 ← 基于 plan_017_downstream_impact
14	  [plan_032_cleaned_mmlu_analysis](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/data/cleaned_mmlu_analysis.csv) | [plan_032_subject_dif_concentration](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/data/per_subject_dif_concentration.csv) | [plan_032_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/report/plan_032_report.md)
15	- **plan_031_temporal_granularity** (success): 如果 temporal DIF 随时间距离单调递增，则 half-year cohort (2023-H2 vs 2024-H1, 0.5yr) 的 C% 应显著低于 full-year (2023 vs 2024, 1.0yr) 的 C%。这检验 DIF 信号是否与 temporal distance 成正比，回应 Reviewer 对 binary temporal split 过于粗糙的批评。如果 half-year C% ≈ full-year C%，说明 DIF 信号在短至 6 个月的窗口内即已饱和。 ← 基于 plan_001_real_data_dif_mmlu
16	  [plan_031_temporal_granularity_results](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_031_temporal_granularity/data/temporal_granularity_results.csv) | [plan_031_temporal_granularity_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_031_temporal_granularity/report/plan_031_report.md) | [plan_031_temporal_granularity_script](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_031_temporal_granularity/intermediate/plan_031_temporal_granularity.py)
17	
18	## 趋势
19	成功 11 / 负向 6 / 失败 0 / 共 17
20	
21	## 下一步
22	（无活跃 idea，请通过 ideas.md 添加）
23	
24	## 资源状态
25	（无服务器配置）
26	
27	## 告警
28	（无）
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58d144ba-40ef-445d-bbdf-e863e1f3b759",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "a410ea337430c7406",
  "type": "user",
  "uuid": "1388d67a-2ae8-4a12-9a38-09a28dcd8b30",
  "sourceToolAssistantUUID": "58d144ba-40ef-445d-bbdf-e863e1f3b759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-21T15:09:20.055Z_

I have now read all sections of the paper, the experiment plan, and supporting materials. Here is my review.

---

## R1 Review: Methods and Experiments

### Summary

This paper applies Mantel-Haenszel DIF analysis from educational measurement to the METABENCH response matrix (5,227 models, 12,508 MMLU items) and finds that 31.3% of MMLU items exhibit large temporal DIF (ETS Category C) between 2023 and 2024 model cohorts. The finding replicates across six benchmarks (17.9--31.3%), and a semi-synthetic injection framework with cross-subject matching validates detection power while eliminating false positive inflation. The paper reframes the contribution away from contamination detection toward psychometric diagnosis, arguing that DIF-flagged items concentrate cross-generational discriminative signal but do not threaten aggregate ranking stability.

### Strengths

1. **Scale and thoroughness of controls.** The analysis covers 5,227 models across 12,508 items -- orders of magnitude larger than prior DIF work in NLP. Six distinct controls (random split, ability-quintile, within-family, matched-ability nearest-neighbor, IRT theta-conditioning, within-subject) systematically rule out methodological confounds. The convergence of matched C% around 28--29% across vastly different unmatched starting points (31.3% temporal, 61.3% within-family) is compelling evidence that approximately 28--29% reflects genuine item-level DIF.

2. **Cross-subject matching is a genuine methodological contribution.** Proposition 1 is clean and correct: excluding the tested subject from the matching variable eliminates contamination leakage by construction, achieving empirical DFPR = 0.000 with bootstrap confirmation. This has clear reuse value for any future semi-synthetic DIF evaluation in multi-domain benchmarks.

3. **Appropriate hedging of causal claims.** The paper consistently states that DIF detects "that" items function differently, not "why." The GSM1K correlation is explicitly labeled exploratory with wide confidence intervals. The Simpson's paradox finding is presented as a decomposition, not a causal mechanism. This is a significant improvement over many contamination-detection papers that conflate detection with attribution.

4. **Cross-benchmark replication strengthens the main finding.** Six benchmarks all showing temporal DIF well above random baselines (45--174x), with a coherent knowledge-vs-procedural dichotomy (C% >= 26.9% vs <= 18.9%), substantially raises confidence that this is not a MMLU-specific artifact.

5. **Semi-synthetic dose-response validation.** The monotonic relationship between exploitation rate p and detection power (DTPR), combined with the DFPR = 0.000 result, provides a clean internal validity check that MH-DIF is sensitive to the signal it claims to detect.

6. **Honest reporting of failures and limitations.** The bifactor IRT convergence failure (Appendix E), the underpowered GSM1K analysis (N=33), and the explicit listing of unexecuted experiments (Appendix F) demonstrate scientific transparency.

### Weaknesses

1. **The MH procedure's validity under severe multidimensionality is not adequately defended.** The paper reports CFI = 0.681 for MMLU IRT fit and notes within-subject Q3 local dependence (11.3% of pairs exceed |Q3| > 0.20). The Limitations section claims MH-DIF "does not depend on IRT model fit" citing Holland & Thayer (1988), which is technically true for the conditional-on-observed-score interpretation. However, MH-DIF uses total score as a proxy for theta, and when the latent space is genuinely 57-dimensional (as MMLU subjects suggest), total score is a poor conditioning variable. Items can appear to have DIF simply because the two cohorts differ on specific latent dimensions that are poorly captured by total score. The paper's own within-subject DIF yielding C% = 38.1% (higher than the 31.3% temporal rate) is concerning -- it suggests that removing cross-subject dependence structure actually increases detected DIF, which could indicate that multi-domain total-score conditioning was partially masking real multidimensionality artifacts rather than controlling for them. The ability-quintile control (C% = 2.9%) helps but operates within the same temporal window and does not address the possibility that 2023 and 2024 cohorts differ on dimension-specific abilities in ways total score cannot capture.

2. **The semi-synthetic injection mechanism has limited ecological validity.** Flipping incorrect-to-correct responses at a uniform rate p is a crude model of contamination that assumes all contaminated models benefit equally and all contaminated items produce the same behavioral signature. Real contamination is heterogeneous: some models memorize verbatim, others benefit from training data augmentation, and the effect varies by item difficulty and model capability. The paper does not explore heterogeneous injection schedules (e.g., making p a function of item difficulty or model ability). This limits the external validity of the DTPR/DFPR results -- the semi-synthetic framework validates detection under a simplified contamination model but does not demonstrate sensitivity to more realistic contamination patterns.

3. **The permutation null (z = 237.2) is based on label permutation, but per-family stratified permutation was not executed.** The paper acknowledges this in the experiment plan context. The concern is that model families released in clusters (e.g., many Llama-3 variants appearing in 2024) create non-exchangeable temporal labels. Permuting labels across families does not preserve the family-release-date confound. The graduated de-duplication analysis (K=10: 22.7%, K=20: 29.1%) partially addresses this, but a formal family-stratified permutation null would be more convincing. This is a moderate gap given that within-family analysis (Llama-2 vs Llama-3) shows C% = 61.3% before matching, suggesting strong family-level effects.

4. **The unexecuted ConStat/DVD comparisons are a meaningful gap.** The paper's framing pivoted from "ensemble detection" to "diagnostic lens," but Claims 2 and 3 still implicitly position DIF against existing detectors. The argument that ConStat is validated against orthogonal ground truth (enrichment = 0.964) is logically valid but empirically untested -- the paper never actually runs ConStat on the same data to demonstrate that it produces different flags. Without this direct comparison, the meta-critique remains theoretical. The reasoning-RL robustness comparison (plan_002) with only N=13 models and non-significant DeLong tests further weakens the comparative positioning.

5. **The downstream impact analysis has a circularity issue that is acknowledged but not resolved.** DIF-flagged items concentrate discriminative signal (z = -8 to -49 sigma vs random), but the paper also reports Jaccard = 0.12 with high-discrimination items. The circularity ablation shows DIF-based removal is the "least disruptive non-random strategy," but this comparison is against accuracy-gap removal (z = -157) and random removal -- there is no comparison against psychometrically principled item selection (e.g., IRT-based discrimination filtering or scalability coefficient filtering). The claim that DIF items are "diagnostic" rather than just "hard and discriminating" would be strengthened by such a comparison.

6. **Temporal cohort definition is coarse and potentially confounded.** Calendar year 2023 vs 2024 aggregates models with vastly different architectures, training data cutoffs, alignment methods, and scales. The paper's own Cohen's d = -0.17 for overall ability suggests the cohorts are well-matched in aggregate, but this does not rule out dimension-specific differences. The 6-month window robustness check (C% = 34.35%) showing even higher DIF than the full-year comparison is intriguing but not well-explained -- if anything, it suggests that the temporal signal saturates quickly, which could also be consistent with a non-temporal confounder that simply correlates with release date.

7. **Bootstrap CI for the headline C% is surprisingly wide.** The 95% CI of [29.4%, 38.1%] spans nearly 9 percentage points. The upper bound of 38.1% is 22% higher than the point estimate of 31.3%. This is a model-level bootstrap (resampling models), and the width suggests substantial model-level heterogeneity in DIF patterns. The paper does not discuss the implications of this width or whether it is driven by specific model families.

### Questions for Authors

1. The within-subject DIF rate (C% = 38.1%) is higher than the overall temporal rate (31.3%). How do you explain this? If total-score conditioning across 57 subjects actually suppresses some DIF signal, does this mean the 31.3% figure is an underestimate, or does it indicate that within-subject DIF captures additional multidimensionality artifacts?

2. For the Simpson's paradox result (OR reversal from 1.55 to 0.73): what are the specific item properties in the conditional model? Is item difficulty alone sufficient to produce the reversal, or is discrimination also needed? This matters for the causal interpretation -- if difficulty is a mediator (accuracy gains cause DIF through making hard items easier), then conditioning on it removes the causal effect rather than revealing a confounder.

3. The 6-month window DIF (C% = 34.35%) is numerically higher than the full-year DIF (31.3%). This seems counterintuitive if DIF accumulates with temporal distance. Is this a sample size effect (different model counts in the two analyses), or does it suggest the temporal signal has a non-monotonic relationship with time distance?

4. Could you provide the item-level correlation between DIF magnitude (|Delta_MH|) and item difficulty? If DIF concentrates on items near the extremes of difficulty (very easy or very hard), this would support a floor/ceiling interaction explanation rather than genuine construct shift.

5. For the cross-benchmark replication, were the same model cohorts (2023 vs 2024) used across all six benchmarks, or did model availability vary by benchmark? If different models were available for different benchmarks, the cross-benchmark comparison conflates benchmark effects with population effects.

6. Proposition 1 claims DFPR = 0 "by construction," but this holds only if contamination does not spill across subjects (e.g., if contamination on subject X does not change the model's performance on related subjects). In practice, training on data from one MMLU subject could improve performance on related subjects. How sensitive is the DFPR = 0 guarantee to cross-subject transfer effects?

### Minor Issues

1. Table 1 column header "FPR (clean)" is confusing -- this is the DIF-C rate among Li et al. "clean" items, not a classical false positive rate. Consider renaming to "C% (clean subset)" or clarifying the distinction.

2. The paper mentions "analysis code and DIF audit scripts" at an anonymous URL but does not specify whether METABENCH data access requires any special permissions. Reproducibility depends on data availability.

3. The threshold sensitivity analysis (C% from 10.2% at |Delta| >= 2.5 to 48.9% at |Delta| >= 1.0) is mentioned in passing but deserves a supplementary table or figure showing the full curve.

4. The paper reports "99.98% decoder-only" for architecture homogeneity but does not discuss whether this includes both base models and instruction-tuned variants, or whether instruction tuning creates de facto architectural heterogeneity in the response patterns.

5. The Llama-2 vs Llama-3 comparison (N = 161 vs 308) has a 2:1 sample size imbalance and large ability gap (d = -0.99). The paper appropriately flags this but still uses the 61.3% figure prominently. The matched-ability reduction to 28.3% is more informative and should receive more emphasis.

6. The abstract reports DTPR = +0.508 at p = 0.5, but this is from external matching on MMLU. The GSM8K external matching result is DTPR = +0.514. The near-identical values across two very different benchmarks is reassuring but could be coincidental -- standard errors should be reported to assess whether the difference is meaningful.

### Missing References

1. **Wainer & Wang (2000)**, "Using a new statistical model for testlets to score TOEFL," on testlet DIF -- relevant given MMLU's subject-clustered item structure which creates natural testlets.
2. **Penfield & Camilli (2007)**, "Differential Item Functioning," the comprehensive handbook chapter providing modern treatment of DIF methods that would complement the Holland & Thayer (1988) citation.
3. **Polo et al. (2025)**, "On the Reliability of LLM Evaluation Benchmarks" -- directly addresses measurement reliability of LLM benchmarks and would strengthen the related work positioning.

### Scores

- Soundness: 3.5/5
- Excitement: 3.5/5
- Reproducibility: 4/5
- Overall Assessment: 3.5 (Borderline Conference)
- Confidence: 4/5

**Justification for Overall Assessment:** The paper presents a large-scale empirical finding (31% temporal item instability) with unusually thorough controls, and the cross-subject matching protocol is a genuine methodological contribution. The cross-benchmark replication across six benchmarks is convincing. However, two issues prevent a clear Conference-accept recommendation: (1) the multidimensionality concern -- using total score to condition DIF in a 57-dimensional ability space is a known limitation of MH-DIF, and the within-subject DIF rate exceeding the overall rate raises questions about whether the conditioning is adequate; and (2) the missing direct comparisons with existing detectors (ConStat, DVD) leaves the comparative positioning empirically unsupported, weakening Claims 2--3. The paper would benefit from a revision that either provides the ConStat comparison or more carefully scopes Claims 2--3 as purely conceptual arguments. The work is solid empirical science with clear practical value for the benchmark evaluation community, placing it at the boundary between Main conference and Findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1388d67a-2ae8-4a12-9a38-09a28dcd8b30",
  "isSidechain": true,
  "agentId": "a410ea337430c7406",
  "requestId": "req_011CbFvXGD6gvcfNG5DgyRMM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc80d50d-233d-4231-80b4-91c6202e2dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1BXgASZQVg2CJA9L2ahWB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1511,
      "cache_read_input_tokens": 61044,
      "output_tokens": 3350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1511
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3350,
          "cache_read_input_tokens": 61044,
          "cache_creation_input_tokens": 1511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1511,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
