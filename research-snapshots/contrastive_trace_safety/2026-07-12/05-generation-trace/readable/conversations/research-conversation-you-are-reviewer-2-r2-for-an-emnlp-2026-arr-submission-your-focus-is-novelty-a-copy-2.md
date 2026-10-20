# Research conversation: You are **Reviewer 2 (R2)** for an EMNLP 2026 ARR submission. Your focus is **Novelty and Related Work**. You must produ

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af864ac05d0b14dfa.jsonl`
- **Structured JSON:** [`995f773d5a504875197a.json`](../../sessions/99/995f773d5a504875197a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-22T10:01:14.944Z_

You are **Reviewer 2 (R2)** for an EMNLP 2026 ARR submission. Your focus is **Novelty and Related Work**. You must produce a rigorous, calibrated review.

## Venue calibration (EMNLP 2026 ARR)
- 5 = Consider for Award (top 2.5%)
- 4.5 = Borderline Award
- 4 = Conference (acceptable for main)
- 3.5 = Borderline Conference
- 3 = Findings (acceptable for Findings)
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit
- Acceptance rate ~21%. Be calibrated: a score of 4 means top ~21%.
- Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5)

## Paper being reviewed

**Title:** "Cross-Dataset Validation of Hidden-State Safety Probing: Layer Selection Bias as a Probe-Task-Modulated Property"

**Abstract:** Hidden-state probes have shown strong advantages over text-based monitors for detecting safety commitment in reasoning models, but the generality of this advantage across datasets and supervision regimes remains unclear. The paper extends a prior 4-model evaluation of temporal hidden-state probing to AdvBench, a binary jailbreak/safe classification benchmark that lacks the fine-grained commitment-point labels of the original dataset. Across two models (R1-8B and OT-7B), they find that the layer selection bias induced by crossing-rate-contaminated metrics replicates directionally: CR-composite selects shallower layers than threshold-based metrics on both datasets. However, the bias gap attenuates from 23 layers (72% depth) under temporal supervision to 7 layers (23%) under binary labels. The hidden-state modality advantage persists (+6.5pp precision for R1-8B, +5.5pp for OT-7B) but with 3–5× smaller effect sizes than the original dataset, and only 1 of 6 metrics passes Holm–Bonferroni correction across both models. Temporal context improves probe accuracy (+3pp), Mahalanobis distance detection fails, and GRU sequence models provide no benefit over linear probes—all consistent with original findings. These results qualify the hidden-state advantage as a probe-task-modulated geometric property, strongest under temporal supervision, rather than an unconditional model-geometric property.

## Full paper content (sections summarized from 10-page PDF):

**Section 1 (Introduction):** Reasoning-trace LMs (DeepSeek-R1, QwQ) can exhibit self-jailbreak where chain-of-thought reasoning undermines safety training, culminating in a commitment point. Prior work established HS probes outperform text (12/12 HB, +15-24pp precision) and that CR-composite metric biases layer selection to shallow layers. This paper asks: is this bias a model geometry property or probe-task-modulated? They test on AdvBench (binary labels, no CP, shorter traces).

**Section 2 (Related Work):** Three short paragraphs:
- HS safety monitoring: TrajGuard (token-level HS for adversarial input, 95% defense), SafeSwitch, SIREN. These operate on standard LLMs, not reasoning-model self-jailbreak.
- Reasoning model safety: Self-jailbreak documented by concurrent works. Focus on characterization, not detection. Text-level CoT monitors are vulnerable to pathological chains.
- Layer selection in probing: Known degree of freedom, different layers encode different properties. Extended to safety probing, showing metric choice introduces systematic bias.

Note: The related work section is very brief (one short paragraph per topic, ~150 words total). No specific citations are given in my summary but the paper likely has them. No works are discussed in depth.

**Section 3 (Method):**
- Hidden-state extraction at each layer ℓ and sentence position t. LR probe with window W. Text uses MiniLM-L6.
- Five layer selection metrics: CR-composite (bal_acc × crossing_rate), Pure bal_acc, Precision, Inverse FPR, Composite additive.
- Bootstrap 1000 iterations with HB correction. 2 models × 3 metrics = 6 joint tests.

**Section 4 (Experiments):** 12 subsections covering:
- Original dataset summary (4 models, 12/12 HB)
- AdvBench setup (R1-8B: 178 traces, OT-7B: 165 traces, binary labels)
- Layer sweep: flatter profile (~7pp range vs ~15pp)
- 5-metric layer selection: CR→L5(16%), threshold→L10-L12(32-39%), gap 7 layers vs 23
- HS vs text: +6.5pp precision, attenuated ~3.5× from original
- Temporal ablation: W=3 optimal, +3pp gain
- Bootstrap: 1/3 HB pass (precision only, p=0.014)
- Gap compression: 3.3-5.6× between datasets
- OT-7B extension: larger gap (11 layers, 39%), combined 1/6 HB
- Early detection: HS earlier 23/36 traces, adapted metric
- Oracle ceiling: ~0.85 vs ~0.95
- Negatives: Mahalanobis fails, GRU no improvement, FPR analysis

**Section 5 (Discussion):** Layer selection bias is probe-task-modulated. HS advantage depends on supervision quality. Statistical power limitation acknowledged. Deployment: match modality to detection granularity.

**Section 6 (Conclusion):** Directional replication with attenuation. HS advantage reframed as probe-task-modulated.

**Limitations:** Two models only, binary label ceiling, adapted metric less rigorous, MDE 12-14pp.

**Format notes:** 10-page PDF. 8 pages main text + Limitations section. 14 tables, 0 figures. No references section visible (possible formatting issue).

## Key novelty claims to evaluate:
1. **Cross-dataset validation** of hidden-state safety probing — extending from CP-labeled to binary-labeled data
2. **"Probe-task-modulated geometric property"** — reframing the HS advantage as conditional on supervision regime rather than unconditional
3. **Layer selection bias replication** — showing the CR-composite shallow bias is directionally consistent but magnitude-modulated
4. **Quantification of HS-text gap compression** (3-5×) across supervision regimes

## Your task
Produce a structured review with these sections:

1. **Summary** (3-4 sentences)
2. **Strengths** (bulleted, 4-6 points with specific evidence)
3. **Weaknesses** (bulleted, 4-6 points with specific evidence — focus on novelty, contribution significance, related work coverage, and positioning)
4. **Questions for Authors** (3-5 specific questions)
5. **Minor Issues** (formatting, typos, presentation)
6. **Scores:**
   - Soundness (1-5)
   - Excitement (1-5)
   - Reproducibility (1-5)
   - Overall Assessment (1-5, half-point increments)
   - Confidence (1-5)

Be specific, cite section/table numbers, and calibrate to EMNLP 2026 acceptance standards. Pay particular attention to whether the novelty is sufficient for a venue with ~21% acceptance rate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "ec098830-f8a4-4a5e-81ca-03dbe9ce9ed0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T10:01:14.946Z_

```json
{
  "parentUuid": "ec098830-f8a4-4a5e-81ca-03dbe9ce9ed0",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
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
  "uuid": "ca881882-feec-4674-84d3-6ee2ad2b9691",
  "timestamp": "2026-05-22T10:01:14.946Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-22T10:01:19.493Z_



I need to read the actual paper and related files to produce a thorough review. Let me start by examining the paper and supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca881882-feec-4674-84d3-6ee2ad2b9691",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQxW9i36FsJjkMsZayx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7bcfb9c-950f-4291-bb14-2aab7c9e989b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GW8XzC2MaKHmk8CiRSEd72",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8486,
      "cache_read_input_tokens": 9355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8486,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 4 · 2026-05-22T10:01:20.457Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FdT83PiibSWrSCZ4Lo46A1`</summary>

```json
{
  "pattern": "**/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7bcfb9c-950f-4291-bb14-2aab7c9e989b",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQxW9i36FsJjkMsZayx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eeed7672-8c43-45b1-8de0-c112040ce263",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GW8XzC2MaKHmk8CiRSEd72",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8486,
      "cache_read_input_tokens": 9355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8486,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 5 · 2026-05-22T10:01:20.494Z_

<details><summary>↩ Tool result · `toolu_01FdT83PiibSWrSCZ4Lo46A1`</summary>

```text
docs/paper/_drafts/advbench_contingency_templates.tex
docs/paper/main.tex
docs/paper/sections/limitations.tex
docs/paper/sections/appendix.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/abstract.tex
docs/paper/sections/related_work.tex
docs/paper/sections/discussion.tex
docs/paper/sections/method.tex
docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eeed7672-8c43-45b1-8de0-c112040ce263",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "ef4dab31-1a7b-4ad4-87d5-6bc7035e1758",
  "sourceToolAssistantUUID": "eeed7672-8c43-45b1-8de0-c112040ce263",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T10:01:21.406Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XCyLw68BqVy4LDvZgzcryd`</summary>

```json
{
  "pattern": "**/docs/paper/**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef4dab31-1a7b-4ad4-87d5-6bc7035e1758",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQxW9i36FsJjkMsZayx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf96c268-b0ad-40d0-9d10-a9e258bc91f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GW8XzC2MaKHmk8CiRSEd72",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8486,
      "cache_read_input_tokens": 9355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8486,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 7 · 2026-05-22T10:01:21.440Z_

<details><summary>↩ Tool result · `toolu_01XCyLw68BqVy4LDvZgzcryd`</summary>

```text
docs/paper/figures/fig_trajectory.pdf
docs/paper/figures/fig_concept.pdf
docs/paper/figures/fig_forest_precision.pdf
docs/paper/figures/fig2_temporal_improvement.pdf
docs/paper/figures/pareto_two_stage.pdf
docs/paper/figures/fig_layer_heatmap.pdf
docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf96c268-b0ad-40d0-9d10-a9e258bc91f0",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "3dc67eff-529d-40c5-9832-e0255087a838",
  "sourceToolAssistantUUID": "bf96c268-b0ad-40d0-9d10-a9e258bc91f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T10:01:21.637Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Xad9qiNMFXsgrKAMZFWxWj`</summary>

```json
{
  "pattern": "**/artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dc67eff-529d-40c5-9832-e0255087a838",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQxW9i36FsJjkMsZayx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a553deb3-b4b4-4cee-bd12-ecc7275b3f11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GW8XzC2MaKHmk8CiRSEd72",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8486,
      "cache_read_input_tokens": 9355,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8486
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 304,
          "cache_read_input_tokens": 9355,
          "cache_creation_input_tokens": 8486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8486,
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

_source line 9 · 2026-05-22T10:01:21.675Z_

<details><summary>↩ Tool result · `toolu_01Xad9qiNMFXsgrKAMZFWxWj`</summary>

```text
artifacts/data_exploration_report.md
artifacts/commitment_point_analysis.md
artifacts/diag_d1_layer_sweep/report/d1_layer_sweep_results.md
artifacts/diag_d2_pca_viz/chart/d2_pca_viz_results.txt
artifacts/exp_gru256_multilayer/data/gru256_ablation.log
artifacts/dream_reports/dream_20260516T194646/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260516T194646/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260516T194646/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T194646/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T194646/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T194646/best/experiment_data.json
artifacts/dream_reports/dream_20260516T194646/best/paper_framing.md
artifacts/dream_reports/dream_20260516T194646/best/paper.tex
artifacts/dream_reports/dream_20260516T194646/best/paper.bbl
artifacts/dream_reports/dream_20260516T194646/best/paper.blg
artifacts/dream_reports/dream_20260516T194646/best/paper.aux
artifacts/dream_reports/dream_20260516T194646/best/paper.out
artifacts/dream_reports/dream_20260516T194646/best/paper.pdf
artifacts/dream_reports/dream_20260516T194646/best/paper.log
artifacts/dream_reports/dream_20260516T194646/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260516T194646/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T194646/median/experiment_data.json
artifacts/dream_reports/dream_20260516T194646/median/paper_framing.md
artifacts/dream_reports/dream_20260516T194646/median/paper.tex
artifacts/dream_reports/dream_20260516T194646/median/references.bib
artifacts/dream_reports/dream_20260516T194646/median/paper.bbl
artifacts/dream_reports/dream_20260516T194646/median/paper.blg
artifacts/dream_reports/dream_20260516T194646/median/paper.aux
artifacts/dream_reports/dream_20260516T194646/median/paper.out
artifacts/dream_reports/dream_20260516T194646/median/paper.pdf
artifacts/dream_reports/dream_20260516T194646/median/paper.log
artifacts/dream_reports/dream_20260516T194646/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260516T194646/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T194646/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T194646/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T194646/worst/paper.tex
artifacts/dream_reports/dream_20260516T194646/worst/paper.aux
artifacts/dream_reports/dream_20260516T194646/worst/paper.out
artifacts/dream_reports/dream_20260516T194646/worst/paper.pdf
artifacts/dream_reports/dream_20260516T194646/worst/paper.log
artifacts/dream_reports/dream_20260516T194646/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260516T194646/logs/orchestrator.log
artifacts/dream_reports/dream_20260516T194646/best/review_context.yaml
artifacts/dream_reports/dream_20260516T194646/best/review_report.md
artifacts/dream_reports/dream_20260516T194646/logs/review_best.log
artifacts/dream_reports/dream_20260516T194646/median/review_context.yaml
artifacts/dream_reports/dream_20260516T194646/median/review_report.md
artifacts/dream_reports/dream_20260516T194646/logs/review_median.log
artifacts/dream_reports/dream_20260516T194646/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T194646/worst/review_report.md
artifacts/dream_reports/dream_20260516T194646/logs/review_worst.log
artifacts/dream_reports/dream_20260516T194646/meta.yaml
artifacts/dream_reports/dream_20260516T203948/logs/orchestrator.log
artifacts/dream_reports/dream_20260516T203948/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260516T203948/logs/phase2_best_attempt0.log
artifacts/exp_005_trajguard_mahalanobis/data/results_summary.txt
artifacts/dream_reports/dream_20260516T203948/logs/phase2_median_attempt0.log
artifacts/exp_013_text_baseline/data/results_summary.txt
artifacts/dream_reports/dream_20260516T203948/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T203948/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T203948/best/experiment_data.json
artifacts/dream_reports/dream_20260516T203948/best/paper_framing.md
artifacts/dream_reports/dream_20260516T203948/best/paper.tex
artifacts/dream_reports/dream_20260516T203948/best/paper.aux
artifacts/dream_reports/dream_20260516T203948/best/paper.out
artifacts/dream_reports/dream_20260516T203948/best/paper.pdf
artifacts/dream_reports/dream_20260516T203948/best/paper.log
artifacts/dream_reports/dream_20260516T203948/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260516T203948/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T203948/median/experiment_data.json
artifacts/dream_reports/dream_20260516T203948/median/paper_framing.md
artifacts/exp_006_bootstrap_ci/data/bootstrap_results_pointer.txt
artifacts/dream_reports/dream_20260516T203948/median/paper.tex
artifacts/dream_reports/dream_20260516T203948/median/paper.aux
artifacts/dream_reports/dream_20260516T203948/median/paper.out
artifacts/dream_reports/dream_20260516T203948/median/paper.pdf
artifacts/dream_reports/dream_20260516T203948/median/paper.log
artifacts/dream_reports/dream_20260516T203948/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260516T203948/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T203948/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T203948/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T203948/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260516T210856/logs/orchestrator.log
artifacts/dream_reports/dream_20260516T210856/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260516T210856/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260516T210856/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T210856/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T212347/logs/orchestrator.log
artifacts/dream_reports/dream_20260516T212347/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260516T212347/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260516T212347/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T212347/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T212347/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T212347/best/experiment_data.json
artifacts/dream_reports/dream_20260516T212347/best/paper_framing.md
artifacts/dream_reports/dream_20260516T212347/best/paper.tex
artifacts/dream_reports/dream_20260516T212347/best/paper.aux
artifacts/dream_reports/dream_20260516T212347/best/paper.out
artifacts/dream_reports/dream_20260516T212347/best/paper.pdf
artifacts/dream_reports/dream_20260516T212347/best/paper.log
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a553deb3-b4b4-4cee-bd12-ecc7275b3f11",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "018db204-67b5-4ebb-8f21-03a277e28edf",
  "sourceToolAssistantUUID": "a553deb3-b4b4-4cee-bd12-ecc7275b3f11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T10:01:24.869Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PAPxutneg89syG5MSybF55`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "018db204-67b5-4ebb-8f21-03a277e28edf",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQxzy4MQoWf8TWmfKZL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ce4edee-e3a1-4d4f-be69-418dcb6104b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mMipJeycQRZJNT9D788C5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3734,
      "cache_read_input_tokens": 17841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3734,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 11 · 2026-05-22T10:01:24.875Z_

<details><summary>↩ Tool result · `toolu_01PAPxutneg89syG5MSybF55`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	\usepackage{xcolor}
15	\usepackage{colortbl}
16	\usepackage{hyperref}
17	\usepackage[capitalise]{cleveref}
18	
19	\title{Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models}
20	
21	\author{Anonymous ARR Submission}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{sections/abstract}
28	\end{abstract}
29	
30	\input{sections/introduction}
31	
32	\input{sections/related_work}
33	
34	\input{sections/method}
35	
36	\input{sections/experiments}
37	
38	\input{sections/discussion}
39	
40	\input{sections/conclusion}
41	
42	\input{sections/limitations}
43	
44	\bibliography{references}
45	
46	\input{sections/appendix}
47	
48	\end{document}
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ce4edee-e3a1-4d4f-be69-418dcb6104b8",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "f3ff0dad-8b83-4786-8b79-2a491d4611b7",
  "sourceToolAssistantUUID": "1ce4edee-e3a1-4d4f-be69-418dcb6104b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T10:01:25.349Z_

<details open><summary>🔧 Tool call — Read · `toolu_016sCnuGyoL7QmK3bJopKpAd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3ff0dad-8b83-4786-8b79-2a491d4611b7",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQxzy4MQoWf8TWmfKZL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07c9adb3-0517-4048-9295-9d36ff0c8065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mMipJeycQRZJNT9D788C5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3734,
      "cache_read_input_tokens": 17841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3734,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 13 · 2026-05-22T10:01:25.354Z_

<details><summary>↩ Tool result · `toolu_016sCnuGyoL7QmK3bJopKpAd`</summary>

```text
1	Reasoning models with chain-of-thought (CoT) can self-jailbreak: their reasoning traces transition from safe deliberation to committed harmful generation without adversarial input. We define the commitment point (CP) as the first reasoning step after which safety deliberation permanently ceases, and present a systematic empirical comparison of hidden-state (HS) vs.\ text probes for CP detection across four reasoning LLMs (3 Qwen-family, 1 Llama) on HarmThoughts. The comparison depends critically on which transformer layer is monitored, a known sensitivity in probing methodology that we show is severe enough to qualitatively reverse conclusions in the safety domain: a crossing-rate composite metric selects L0 for R1-8B while threshold-based metrics select L14 (14-layer divergence); at 32B the divergence reaches 61 layers (exploratory$^\dagger$), reversing whether an HS advantage is observed. Threshold-based layer selection recovers HS precision gains of +15 to +22pp at 7--8B (cross-validated via nested CV) and preliminary +15 to +19pp at 32B (exploratory$^\dagger$, $n \leq 20$) against a 384d sentence encoder, but this advantage is conditional on partially correlated factors: it diminishes with stronger text encoders (4/4 HB at 384d $\to$ 1/4 at 1024d) and partially overlaps with temporal position. Seven alternative methods (change-point detection, geometric distance, representation engineering, cross-model transfer) all fail to match supervised probing. Metric-induced layer selection bias is the robust methodological finding; the empirical HS advantage is conditional on encoder quality and position control (partially correlated).
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07c9adb3-0517-4048-9295-9d36ff0c8065",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "d34d4684-f5c6-4fb6-b420-722e094dc6b8",
  "sourceToolAssistantUUID": "07c9adb3-0517-4048-9295-9d36ff0c8065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T10:01:25.685Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FKQw3Vbo17Nr3mMZkiWXNA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d34d4684-f5c6-4fb6-b420-722e094dc6b8",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQxzy4MQoWf8TWmfKZL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ea36f79-20b1-4c91-afc1-7b630246c866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mMipJeycQRZJNT9D788C5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3734,
      "cache_read_input_tokens": 17841,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3734
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 17841,
          "cache_creation_input_tokens": 3734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3734,
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

_source line 15 · 2026-05-22T10:01:25.689Z_

<details><summary>↩ Tool result · `toolu_01FKQw3Vbo17Nr3mMZkiWXNA`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} scale inference-time computation through extended chains of thought (CoT). Recent work documents that these models can ``self-jailbreak'': without adversarial input modification, the CoT transitions from safety-aware deliberation to committed harmful generation~\cite{harmthoughts,selfjailbreak}. We define the first reasoning step after which safety deliberation permanently ceases as the \textbf{Safety Commitment Point} (CP). This failure mode differs qualitatively from adversarial jailbreaks on standard LLMs because the harmful transition originates within the model's own reasoning. Recent work shows that chain-of-thought faithfulness is limited~\citep{chen2025unfaithful}, motivating hidden-state monitoring that bypasses surface text. Before retrospective characterization can inform future detection systems, a prior question must be answered: can current probing methods reliably distinguish pre-CP from post-CP reasoning steps, and under what conditions? This paper provides \emph{retrospective} classification (not online detection) of what hidden-state and text-based probes can and cannot detect; false positive rates remain 11--50\%, so deployment applications are future work.\looseness=-1
4	
5	Existing safety detectors target fundamentally different problems. Hidden-state (HS) methods such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch} classify adversarial inputs at the token level, while text monitors like SafeRemind~\cite{saferemind} scan generated reasoning for explicit violations. Neither tracks the gradual, multi-step commitment process. HS probes require choosing which transformer layer to monitor, a researcher degree of freedom typically treated as a minor implementation detail. Before asking which modality is better, a prior methodological question must be answered: how sensitive are probe conclusions to the choice of layer selection metric? We show this choice alone can reverse a study's central conclusion: the same data yield a 14-layer (R1-8B) to 61-layer (QwQ-32B) divergence depending solely on metric choice; for QwQ-32B, at threshold-based layers the HS advantage is +19pp ($p{<}0.005$); at crossing-rate-selected layers, it is non-significant ($p{=}0.83$). More broadly, no prior work tracks how safety signals evolve step-by-step during extended reasoning; existing hidden-state analyses operate across layers (spatial) rather than across generation steps (temporal).\looseness=-1
6	
7	We conduct a systematic analysis across four reasoning models, primarily Qwen-based (3/4 models), with one Llama model providing evidence from a second architecture family, at two scales (7--8B, 32B) on the HarmThoughts benchmark. Our central finding is methodological: the choice of layer selection metric entirely determines whether an HS advantage is observed. A composite metric (balanced accuracy $\times$ crossing rate) selects shallow layers for 32B models because shallow representations compress directional information, so a linear probe operates near the noise floor and threshold crossings reflect noise rather than semantic transitions. At these layers, only the two 7--8B models show significant HS advantage.\looseness=-1
8	
9	\begin{table}[t]
10	\centering
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{lccccc}
13	\toprule
14	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{$n$ (total\,/\,test)} \\
15	\midrule
16	R1-8B & Llama & 8B & 32 & 4096 & 209\,/\,43 \\
17	OT-7B & Qwen & 7B & 28 & 3584 & 228\,/\,47 \\
18	R1-32B & Qwen & 32B & 64 & 5120 & 100\,/\,20 \\
19	QwQ-32B & Qwen & 32B & 64 & 5120 & 95\,/\,19 \\
20	\bottomrule
21	\end{tabular}}
22	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\citep{harmthoughts} with step-level CP annotations (CP = first reasoning step after which safety deliberation permanently ceases). Split: 60/20/20.}
23	\label{tab:models}
24	\end{table}
25	
26	Threshold-based metrics (precision, inverse FPR, additive composite) share a common confusion matrix and empirically converge; BA independently confirms deep-layer selection (\cref{tab:layer_selection}). At these layers, the HS advantage is graded: \emph{validated via nested 5-fold CV} at 7--8B (precision +20.1 to +21.9pp; \cref{tab:hs_vs_text}), \emph{significant} but suggestive of position-competitiveness at QwQ-32B$^\dagger$ (+19.2pp; \cref{sec:32b-analysis}), and \emph{exploratory} at R1-32B$^\dagger$ (+15.4pp, pattern consistent with position mediation, below MDE; \cref{sec:experiments}).\looseness=-1
27	
28	Our contributions are:
29	\begin{itemize}
30	    \item \textbf{Metric-induced layer selection bias.} Prior work has noted metric sensitivity in probing~\citep{belinkov2022probing}; our contribution is demonstrating a qualitative reversal (significant to non-significant) in a safety-critical application, where the stakes of metric choice are higher than in typical linguistic probing. Crossing-rate composite metrics systematically select shallow layers across all four models (including Llama), reversing HS probe conclusions at 32B scale. The divergence is not gradual: for QwQ-32B, the CR-composite layer (L2, 3\% depth) yields $p{=}0.83$ (non-significant), while the threshold-based layer (L63, 98\% depth) yields $p{<}0.005$, a qualitative reversal, not a quantitative shift. Random-label controls on both architectures confirm the disagreement requires genuine safety labels; the geometric component is Qwen-specific (\cref{sec:layer-results}).
31	
32	    \item \textbf{Boundary conditions for the HS advantage.} Against 384d MiniLM, the HS advantage is validated via nested 5-fold CV at 7--8B (+20.1 to +21.9pp, HB corrected), significant at QwQ-32B$^\dagger$ (+19.2pp, position-competitive), and exploratory at R1-32B$^\dagger$ (+15.4pp). This advantage is conditional on two partially correlated factors: it diminishes with stronger encoders (1/4 HB under BGE-1024d; PCA capacity matching preserves significance across all four models) and partially overlaps with position (3/4 linear, 2/4 quadratic residualization; \cref{sec:32b-analysis}).
33	
34	    \item \textbf{Negative results define method boundaries.} No alternative method consistently matches supervised probing (\cref{tab:negative}): BOCPD/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation; RepE is model-dependent; cross-model transfer fails. Control task selectivity (11.1--16.8pp above chance; \cref{app:control}) confirms genuine safety structure.
35	\end{itemize}
36	
37	\noindent These findings establish that layer selection metric is an uncontrolled confound in hidden-state safety probing: any study reporting conclusions from a single metric family risks undetected qualitative reversal.\looseness=-1
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ea36f79-20b1-4c91-afc1-7b630246c866",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "d9451038-560f-4a70-8706-e027115931b9",
  "sourceToolAssistantUUID": "4ea36f79-20b1-4c91-afc1-7b630246c866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T10:01:28.781Z_

<details open><summary>🔧 Tool call — Read · `toolu_019N6kduhSaUvk2cuQHPaBWb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9451038-560f-4a70-8706-e027115931b9",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQyJUkvTnUaQR7f72f6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76eb9320-991c-4a65-a128-0a350847b047",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUdYfhCy6DaPkzVYUkijed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3213,
      "cache_read_input_tokens": 21575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3213,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
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

_source line 17 · 2026-05-22T10:01:28.796Z_

<details><summary>↩ Tool result · `toolu_019N6kduhSaUvk2cuQHPaBWb`</summary>

```text
1	\section{Related Work}\label{sec:related-work}
2	
3	\paragraph{Safety in Reasoning Models.}
4	Reasoning models introduce a qualitatively new failure mode: the model's own chain of thought transitions from safe deliberation to harmful generation without adversarial input~\cite{wang2025lrmsafety}. Self-jailbreak has been documented with step-level annotations~\cite{harmthoughts,selfjailbreak}; H-CoT~\cite{hcot2025} shows reasoning chains can be externally hijacked; unfaithful reasoning~\cite{chen2025unfaithful,turpin2023language} motivates hidden-state monitoring. Safety-aligned models maintain refusal intentions during thinking but experience sharp drops at output generation~\cite{yin2025refusal_cliff,hagendorff2026lrm_jailbreak,hu2026refusal_dynamics,ahrend2026safer_traces}. CoT monitoring detects reward hacking but is fragile under optimization pressure~\cite{baker2025monitoring,korbak2025cot_monitorability}; GuardReasoner~\cite{xiang2025guardreasoner} trains a dedicated reasoning guard; \citet{schulz2025roadmap} formalizes safety-case deployment. Mitigation strategies include early reasoning steering~\cite{safethink}, entropy-triggered reminders~\cite{saferemind}, and guardrail insertion~\cite{mao2025selfjailbreak_reasoning}; none conducts a systematic modality comparison for commitment detection.
5	
6	\paragraph{Hidden-State Safety Detection.}
7	Internal activations encode safety-relevant information: truthfulness~\cite{azaria2023internal}, layer-distributed alignment signals~\cite{zhou2024alignment}, shallow alignment~\cite{qi2025shallow_alignment}, refusal directions~\cite{arditi2024refusal,joad2026refusal_multi}, activation steering~\cite{turner2023activation,li2023iti}, separate harmfulness/refusal encodings~\cite{zhao2025harmfulness,wollschlager2025geometry}, and scalable feature extraction~\cite{templeton2024scaling}. Probing studies confirm safety states are linearly accessible~\cite{zhao2026safeprobing,chia2025probing_subspaces,kadali2025internal}. Monitoring systems---TrajGuard~\cite{trajguard}, SafeSwitch~\cite{safeswitch}, SIREN~\cite{siren}, SafeDream~\cite{safedream2026}, HiddenDetect~\cite{jiang2025hiddendetect}, SafeInt~\cite{safeint2025}, RCS~\cite{rcs2026}, and hidden-state forensics~\cite{zhou2025ghost}---assume external input manipulation and operate at the token level; the self-jailbreak setting differs because transitions are internal and span multiple reasoning steps. Concurrently, \citet{chan2025probing} show final-layer linear probes predict alignment outcomes with strong F1, but their single-layer, single-metric evaluation does not examine whether different layers yield different conclusions---the central question of our work (\cref{sec:layer-results}). We reproduce TrajGuard (\cref{sec:negative}) and find its geometric approach fails on minor PCA components.\looseness=-1
8	
9	\paragraph{Probing Methodology and Layer Selection.}
10	Linear probing spans layer-wise classifiers~\cite{alain2017understanding}, sentence probing~\cite{conneau2018probing}, and surveys~\cite{belinkov2019analysis,belinkov2022probing,rogers2020primer}; causal abstraction~\cite{geiger2023causal} grounds use of internal representations. Control tasks~\cite{hewitt2019control} distinguish structure from memorization (adopted in \cref{app:control}); \citet{levinstein2024liedetector} raise concerns about spurious correlations that our controls address. Information-theoretic and causal formulations address probe complexity~\cite{voita2020information,pimentel2020information,ravfogel2020null,ravfogel2022rlace,belrose2023leace,elazar2021amnesic}.\footnote{The Tuned Lens~\cite{belrose2023tunedlens} assumes next-token prediction, misaligned with binary CP classification.} Non-uniform layer-wise information distribution~\cite{tenney2019bert,jawahar2019bert,marks2024geometry} and cross-layer disagreement~\cite{kaya2019shallow,zhou2020bert} are well established; we repurpose these for safety probe layer selection (\cref{sec:layer-sensitivity}). Our contribution is that the known layer-wise gradient interacts with metric choice to produce systematic selection bias. \citet{boxo2025linear_probes} show probes can rely on textual evidence; our analysis provides a complementary geometric mechanism at shallow layers. Concurrent works confirm layer sensitivity in related settings: influence estimation~\cite{vitel2025layer}, reasoning dynamics monitoring~\cite{chrabaszcz2026monitoring}, hallucination detection~\cite{alvarez2026transport_geometry}, truth encoding trajectories~\cite{damirchi2026truth}, selective probes~\cite{meyoyan2026bertology}, and multi-layer ensembling~\cite{pais2026linear_probe_scaling}.\looseness=-1
11	
12	\paragraph{Alternative Detection Approaches.}
13	BOCPD~\cite{adams2007bayesian} detects abrupt distributional shifts; CCS~\cite{burns2023discovering} discovers latent truth directions; RepE~\cite{zou2023representation} identifies concept directions. We adapt all three to temporal commitment detection (\cref{sec:negative}): BOCPD/CUSUM fail on gradual transitions, CCS misaligns temporally, and RepE is model-dependent (BA 0.756 vs.\ 0.559). These failures motivate supervised probes with principled layer selection.\looseness=-1
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76eb9320-991c-4a65-a128-0a350847b047",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "275c415e-abda-4ce3-9ca4-22b0f3dc67bb",
  "sourceToolAssistantUUID": "76eb9320-991c-4a65-a128-0a350847b047",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T10:01:29.006Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MB4GGHXZ13jUUkLFikho8E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "275c415e-abda-4ce3-9ca4-22b0f3dc67bb",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQyJUkvTnUaQR7f72f6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e17268b8-1051-4e68-8278-d3b565297c70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUdYfhCy6DaPkzVYUkijed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3213,
      "cache_read_input_tokens": 21575,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3213
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 21575,
          "cache_creation_input_tokens": 3213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3213,
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

_source line 19 · 2026-05-22T10:01:29.012Z_

<details><summary>↩ Tool result · `toolu_01MB4GGHXZ13jUUkLFikho8E`</summary>

```text
1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety deliberation permanently ceases; traces with oscillating safety deliberation are resolved by taking the final irreversible transition. This binary formulation is a deliberate simplification; we discuss its limits in \cref{sec:limitations}. Steps before CP are \emph{pre-commitment} ($y_t = 0$); steps at or after CP are \emph{post-commitment} ($y_t = 1$). The classification task produces a score $s_t \in [0, 1]$ estimating whether the model has passed its CP by step $t$. Annotation quality is robust to boundary uncertainty: shifting CP labels by $\pm$1 step changes balanced accuracy by ${<}2.5$pp (\cref{tab:cp_perturbation}).
8	
9	We study four reasoning models spanning two architectures and two scales (\cref{tab:models}).
10	
11	\subsection{Probe Architecture}
12	\label{sec:probe-architecture}
13	
14	\paragraph{Hidden-state (HS) probes.} At each step $t$, we extract the last-token hidden state $\mathbf{h}_t^{(\ell)} \in \mathbb{R}^d$ from layer $\ell$ and train an L2-regularized logistic regression classifier (balanced class weights, $C{=}1.0$, LBFGS, max\_iter${}=2000$) on binary CP labels. Sweeping $C \in [0.01, 100]$ yields $<$2pp BA variation (\cref{sec:experiments}), confirming robustness to this default. Layer selection is analyzed in \cref{sec:layer-sensitivity}.
15	
16	\paragraph{Text probes.} Each step's text is encoded with all-MiniLM-L6-v2~\citep{wang2020minilm} ($\mathbb{R}^{384}$), a distilled sentence encoder from the Sentence-BERT family~\citep{reimers2019sentence}. The same logistic regression is applied as a surface-level modality baseline.
17	
18	\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \ldots, t]$. We evaluate $W \in \{1, 3, 5, 10, 15, 20, 25\}$ and select per-model on validation. GRU sequence models are also evaluated under two protocols: a 70/30 train/test split (primary) and the same 60/20/20 split used for LR experiments (for fair comparison; \cref{tab:gru_multi_seeds,app:gru_details}).
19	
20	\subsection{Layer Selection Sensitivity}
21	\label{sec:layer-sensitivity}
22	
23	Layer selection is a researcher degree of freedom that can reverse modality comparison conclusions. We evaluate five metrics: balanced accuracy (BA), precision, and inverse FPR are standard probing metrics~\citep{belinkov2022probing}; crossing rate formalizes cross-layer prediction disagreement~\citep{kaya2019shallow,zhou2020bert}, and additive composite. A \emph{first crossing point} (FCP) exists for trace~$i$ at layer~$\ell$ when the probe score $s_{t'}^{(\ell)} > \tau$ for $K$ consecutive steps; the crossing rate is $\mathrm{CR}(\ell) = N^{-1}\!\sum_{i} \mathbb{1}[\mathrm{FCP}_i^{(\ell)} \text{ exists}]$. A multiplicative composite (BA $\times$ crossing rate) serves as the \emph{crossing-rate composite} (CR-composite) baseline, combining classification quality with transition sensitivity. Metrics at a fixed decision threshold (precision, inverse FPR, additive composite) form the \emph{threshold-based} selection. This taxonomy is empirical, but cosine compression at shallow layers predicts a priori that any threshold-crossing metric exhibits shallow-layer bias, confirmed by results (\cref{sec:layer-results}). Crossing rate inflates where representations are compressed (inter-step cosine distances 1.4--2.7$\times$ smaller; \cref{app:cosine_volatility}). Threshold-based metrics share a confusion matrix and empirically converge; BA independently confirms. Results in \cref{sec:layer-results}; full per-layer sweeps in \cref{app:layer_sweep}.\looseness=-1
24	
25	\subsection{Baseline Methods}
26	\label{sec:baselines}
27	
28	We evaluate seven alternatives to contextualize probe performance (\cref{tab:negative}): BOCPD~\citep{adams2007bayesian} and CUSUM~\citep{page1954cusum} for change-point detection; Mahalanobis distance following TrajGuard~\citep{trajguard}; RepE mean-difference directions~\citep{zou2023representation}; two-layer MLP probes; CCS-adapted~\citep{burns2023discovering}; and cross-model transfer via PCA. A position-only baseline ($t/T$) controls for temporal artifacts. Detailed configurations in \cref{app:bocpd_config,app:transfer_details}.
29	
30	\subsection{Evaluation Protocol}
31	\label{sec:evaluation}
32	
33	We report balanced accuracy, precision, pre-CP FPR, coverage, and lead time. We exclude F1 (conflates precision and recall), AUROC (threshold-free, cannot diagnose layer selection bias), and MCC (redundant with BA under balanced priors). Positive classification requires $K{=}5$ consecutive threshold crossings, selected on the R1-8B validation set and held fixed across all models as the value balancing coverage ($\geq$70\%) and safe-trace false positive rate ($\leq$50\%); \cref{tab:k_ablation} confirms that the HS vs.\ text conclusion direction is consistent at $K{=}3$, $5$, and $7$, with coverage and FPR trading off monotonically. Modality comparisons use BCa bootstrap (10{,}000 resamples, resampling traces as clusters: each trace is an independent unit and all its steps are included or excluded together, preserving within-trace dependence)~\citep{efron1993bootstrap,diciccio1996bootstrap} with Holm-Bonferroni step-down (3 metrics $\times$ 4 models $= 12$ tests, $\alpha{=}0.05$); the 4-test framework yields identical conclusions (\cref{app:holm_bonferroni}). For 32B models ($n \leq 20$), the exact permutation test is the primary inference method; BCa confidence intervals are reported for comparability but may have reduced coverage at these sample sizes (BCa assumes approximate pivotality; heavy-tailed score distributions could produce anti-conservative intervals). Within each model, the three metrics are positively correlated, so the correction is stricter than under independence. Control task selectivity~\citep{hewitt2019control} validates genuine structure (\cref{app:control}). $\dagger$ marks sample-limited test sets ($n \leq 20$): R1-32B ($n{=}20$) and QwQ-32B ($n{=}19$).
34	
35	\paragraph{Hyperparameter search space and multiple comparisons.} The full exploration spans ${\sim}$5 metrics $\times$ 7 windows $\times$ 28--64 layers $\approx$ 980--2{,}240 configurations per model. However, the effective number of independent tests is far smaller: the five metrics share one confusion matrix (threshold-based metrics are functionally correlated; \cref{app:effective_tests}), and adjacent layers produce near-identical probes. Effect sizes are large (Cohen's $d{=}0.58$--$2.37$; \cref{app:effective_tests}), arguing against fishing artifacts. A two-stage design protects against selection bias: upstream layer/window exploration uses nested CV and split-half validation at 7--8B (\cref{app:nested_cv,app:split_half}); downstream modality tests apply HB to 12 final comparisons. The 32B models lack nested CV (${\sim}$4 traces per fold) and are marked exploratory ($\dagger$). We classify evidence into three tiers (cross-validated, significant, and exploratory), detailed in \cref{sec:experiments}. All reported p-values are conditional on the selected layer and window, not marginal over the full search space.\looseness=-1
36	
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e17268b8-1051-4e68-8278-d3b565297c70",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "3d4b18d3-728a-4f01-9e52-3a751e3d6693",
  "sourceToolAssistantUUID": "e17268b8-1051-4e68-8278-d3b565297c70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T10:01:31.427Z_

<details open><summary>🔧 Tool call — Read · `toolu_014A7Gu2JyS9HJewkkgTSJ5c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d4b18d3-728a-4f01-9e52-3a751e3d6693",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQyYXMrwBpuUVkhQa95",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a31fd465-ca1d-4821-8f36-0eed3df8ed61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gBu6AcugWG9MQnio7G2kd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3893,
      "cache_read_input_tokens": 24788,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3893
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 24788,
          "cache_creation_input_tokens": 3893,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3893,
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

_source line 21 · 2026-05-22T10:01:31.431Z_

<details><summary>↩ Tool result · `toolu_014A7Gu2JyS9HJewkkgTSJ5c`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria.
4	
5	\paragraph{Evidence gradient.} We classify HS advantage evidence into three tiers: \emph{cross-validated}\footnote{In our usage, \emph{cross-validated} means the result survives nested 5-fold cross-validation with a held-out test fold, ruling out hyperparameter overfitting. \emph{Exploratory} ($\dagger$) results pass HB on the holdout split but lack nested CV validation due to sample constraints.} (nested CV pass; 7--8B models), \emph{significant} (HB pass without nested CV; QwQ-32B), and \emph{exploratory} ($^\dagger$, small sample or narrow coverage; R1-32B). Per-model details follow in \cref{sec:layer-results,sec:hs-text,sec:32b-analysis}.
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We study R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (OpenThinker-7B, trained on the OpenThoughts dataset~\citep{openthinker}; Qwen-7B backbone, STILL-trained~\cref{app:ot7b_details}, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level CP annotations (60/20/20 split). HS probes extract last-token hidden states from a selected layer; text probes encode each step with all-MiniLM-L6-v2 (384d). Both use L2-regularized logistic regression with temporal windowing $W \in \{1, 3, 5, 10, 15, 20, 25\}$ selected on validation. Classification requires $K{=}5$ consecutive threshold crossings (\cref{tab:k_ablation}). Statistical testing follows \cref{sec:evaluation}.\looseness=-1
10	
11	\subsection{Layer Selection Results}\label{sec:layer-results}
12	
13	\cref{tab:layer_selection} shows that the crossing-rate composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers across all four models: L0 for R1-8B (full L0--L24 sweep; \cref{tab:r18b_full_layer}) and OT-7B, L2 (3\%) for QwQ-32B, and L10 (16\%) for R1-32B (\cref{fig:layer_heatmap}). The three threshold-based metrics (precision, inverse FPR, additive composite) share a common confusion matrix and empirically converge to the same deep layer, L63 (98\%) for both 32B models, consistent with their shared structure, though not mathematically guaranteed. Pure balanced accuracy, a threshold-free metric, selects layers that vary across data splits and models (7--98\% depth under 60/20/20; \cref{app:ba_layer_comparison}), itself demonstrating that layer selection is a consequential methodological choice. The mechanism is that shallow layers produce highly compressed representations with small inter-step margins: step-to-step cosine distances are 1.4--2.7$\times$ smaller than at deep layers across all models (\cref{app:cosine_volatility}). A linear probe in this compressed space operates near the noise floor, generating frequent threshold crossings that inflate crossing rate independently of discriminative power (\cref{sec:layer-sensitivity}).\looseness=-1
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{lcccc}
20	\toprule
21	\textbf{Model} & \textbf{CR-comp.}$^a$ & \textbf{Thresh.}$^b$ & $p$ \textbf{(thresh.)} & $\Delta$\textbf{Prec}$^c$ \\
22	\midrule
23	R1-8B & L0 (0\%) & L14 (44\%) & ${<}0.001$ & +20.1 \\
24	OT-7B & L0 (0\%) & L16 (57\%) & ${<}0.001$ & +21.9 \\
25	QwQ-32B$^\dagger$ & L2 (3\%) & L63 (98\%) & ${<}0.005$ & +19.2 \\
26	R1-32B$^\dagger$ & L10 (16\%) & L63 (98\%) & ${<}0.001$ & +15.4 \\
27	\bottomrule
28	\end{tabular}}
29	\caption{Layer selection sensitivity. $^a$\,Crossing-rate composite (bal\_acc $\times$ crossing\_rate). $^b$\,Consensus of threshold-based metrics (precision, inverse FPR, additive composite). $^c$\,HS$-$text precision difference (pp) at threshold-based layer (\cref{tab:hs_vs_text}). Rightmost $p$: HS vs.\ text precision $p$-value at threshold-based layer (e.g., QwQ-32B CR-composite layer: $p{=}0.83$, non-significant). $\dagger$\,Sample-limited ($n \leq 20$).}
30	\label{tab:layer_selection}
31	\end{table}
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=\columnwidth]{figures/fig_layer_heatmap.pdf}
36	\caption{Per-layer metric heatmap (2$\times$2). Each column: one of five metrics (min-max normalized). Red dashed: CR-composite layer (bal\_acc $\times$ crossing\_rate); green dashed: threshold-based layer (consensus of threshold-based metrics). For R1-8B (full L0--L24 sweep), crossing rate drives CR-composite selection to L0 while threshold-based metrics retain L14. At 32B, CR-composite selections cluster near input layers while threshold-based metrics peak at deep layers.}
37	\label{fig:layer_heatmap}
38	\end{figure}
39	
40	The downstream impact is severe: at CR-composite layers, only the two 7--8B models show significant HS advantage; both 32B models fail. The CR-composite's systematic shallow-layer selection is an artifact of cosine compression (\cref{app:cosine_volatility}), not a genuine safety signal; random-label controls confirm this distinction (\cref{app:random_cp}). At threshold-based layers, the HS advantage is graded: cross-validated at 7--8B (OT-7B, R1-8B; nested CV), significant but suggestive of position-competitiveness at QwQ-32B$^\dagger$, and exploratory at R1-32B$^\dagger$ (residualized gap below MDE). The $\dagger$ marks sample-limited test sets ($n \leq 20$) where effect sizes are descriptive rather than confirmatory. Random-label controls on QwQ-32B and R1-8B confirm that threshold-based deep-layer selection requires genuine safety labels; the geometric shallow-layer bias is Qwen-specific: retained on QwQ-32B but dissolved on R1-8B (\cref{app:random_cp}). AUROC, excluded from our primary metrics because it is threshold-free (\cref{sec:evaluation}), confirms HS discriminability at BA-selected layers ($\Delta$AUROC +12.1 to +15.1pp; \cref{tab:ba_layer_results}) but cannot diagnose the threshold-dependent layer selection bias.\looseness=-1
41	
42	\paragraph{Ensemble layer selection.} A three-layer ensemble that averages predicted probabilities from the precision-best, BA-best, and inverse-FPR-best layers bypasses single-metric pre-selection entirely. On the holdout split, all four models show significant HS advantage under the ensemble ($p \leq 0.002$, HB corrected; \cref{tab:ensemble}), including both 32B models that fail under CR-composite selection. The ensemble succeeds because averaging predictions from layers selected by different threshold-based metrics---which may favor somewhat different depths within the deep region---smooths metric-specific variation and reduces sensitivity to any single metric's layer preference. This holdout result uses the same split for both layer selection and evaluation; cross-validated confirmation is needed before the ensemble can be recommended as a general debiasing strategy (\cref{sec:discussion}).\looseness=-1
43	
44	\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
45	
46	\begin{table}[t]
47	\centering
48	\small
49	\resizebox{\columnwidth}{!}{%
50	\begin{tabular}{llclrrlrc}
51	\toprule
52	\textbf{Model} & \textbf{Layer} & \textbf{Enc.} & $W$ & $\Delta$\textbf{BA} & $\Delta$\textbf{Prec} & \textbf{95\% CI} & $\Delta$\textbf{FPR} & \textbf{HB} \\
53	\midrule
54	R1-8B & L14 & 384d & 3 & +17.5 & +20.1 & [+12.4, +28.3] & $-$7.9 & \checkmark \\
55	 & & 1024d & & \multicolumn{1}{c}{--} & +5.8 & [$-$7.4, +19.5] & \multicolumn{1}{c}{--} & \\[2pt]
56	OT-7B & L16 & 384d & 3 & +10.7 & +21.9 & [+14.4, +29.6] & $-$17.1 & \checkmark \\
57	 & & 1024d & & \multicolumn{1}{c}{--} & +18.1 & [+8.4, +29.0] & \multicolumn{1}{c}{--} & \checkmark \\[2pt]
58	QwQ$^\dagger$ & L63 & 384d & 5 & +13.0 & +19.2 & [+9.3, +33.5] & $-$15.0 & \checkmark \\
59	 & & 1024d & & \multicolumn{1}{c}{--} & +9.4 & [$-$7.1, +27.7] & \multicolumn{1}{c}{--} & \\[2pt]
60	R1-32B$^\dagger$ & L63 & 384d & 1 & +18.7 & +15.4 & [+8.7, +22.6] & $-$14.6 & \checkmark \\
61	 & & 1024d & & \multicolumn{1}{c}{--} & +11.7 & [$-$0.2, +24.3] & \multicolumn{1}{c}{--} & \\
62	\bottomrule
63	\end{tabular}}
64	\caption{HS vs.\ text at threshold-based layers (LR probes, 60/20/20 split, 10{,}000 bootstrap resamples). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). $\Delta$: HS$-$text difference (pp); ``--'' = BA and FPR are not computed for the 1024d comparison because the 384d and 1024d encoders operate at different probe calibration points and do not share a decision threshold. HB: \checkmark{} = model-level test passes Holm-Bonferroni ($\alpha{=}0.05$); all 384d model-level tests pass. $^\dagger$\,Sample-limited ($n \leq 20$); 32B results are exploratory. 1024d: HB over 4 model-level precision tests.}
65	\label{tab:hs_vs_text}
66	\end{table}
67	
68	The HS advantage is encoder-conditional: against BGE-large (1024d), only OT-7B survives HB correction (\cref{app:encoder_robustness}). Multi-seed stability appears in \cref{app:multi_seed}. Against the 384d baseline, HS probes outperform text probes in all four models$^\dagger$ (\cref{tab:hs_vs_text}): cross-validated at 7--8B (OT-7B: +21.9pp precision, R1-8B: +20.1pp), significant but suggestive of position-competitiveness at QwQ-32B$^\dagger$ (+19.2pp), and exploratory at R1-32B$^\dagger$ (+15.4pp, pattern consistent with position mediation). R1-8B FPR is directionally consistent (5/5 seeds) but not robust ($p{=}0.044$, rank 12/12 in HB step-down; 1/5 seeds Bonferroni; \cref{app:multi_seed}). R1-32B passes 5/5 seeds but shows a pattern consistent with position mediation (residualized gap NS; \cref{app:position_residual}); QwQ-32B's position baseline is competitive (\cref{sec:32b-analysis}). Overall, 18/20 model-seed combinations pass full HB (\cref{app:multi_seed}). Control task selectivity confirms genuine safety signal: 11.1--16.8pp above chance (\cref{app:control}). A split-half analysis on OT-7B confirms internal validity (\cref{app:split_half}).\looseness=-1
69	
70	\paragraph{Capacity control.} PCA reduction of HS features to 384d (79--92\% variance retained) preserves the precision advantage across all four models$^\dagger$ (+16.8 to +23.1pp, all $p{<}0.012$, all HB). The control provides partial evidence against a pure capacity explanation. Random projection to 384d yields similar results ($\Delta$Prec +8.3 to +20.5pp; \cref{app:random_projection}), further weakening the capacity explanation. E5-Mistral-7B (4096d, PCA-reduced to 384d; \cref{app:e5_mistral}) yields intermediate results (2/4 HB), forming a monotonic encoder-quality gradient with MiniLM (4/4) and BGE-large (1/4).\looseness=-1
71	
72	\paragraph{Encoder robustness.} Against BGE-large~\citep{xiao2023cpack} (1024d), only OT-7B survives HB (1/4 precision); R1-8B shows adverse FPR direction (+1.2pp). This forms a monotonic encoder-quality gradient: MiniLM-384d (4/4 HB) $\to$ E5-Mistral-4096d$\to$384d (2/4) $\to$ BGE-large-1024d (1/4), with the precision advantage narrowing from +15--22pp to +6--12pp. The HS advantage is thus a function of text encoder capacity (\cref{fig:forest_precision}); layer selection (Contribution 1) is encoder-independent.\looseness=-1
73	
74	\paragraph{Position mediation.} Position ($t/T$) accounts for 9--20pp of balanced accuracy,\footnote{R1-32B's 20.4pp drop reflects $W{=}1$; at $W{\geq}3$, drops are 9--17pp.} but all models retain non-positional signal above chance (all $p{<}0.001$; \cref{app:position_residual}). Three of four models retain significant non-positional HS advantage (residualized gap +3.7 to +6.9pp, HB corrected); R1-32B's gap is +1.9pp ($p{=}0.914$, $n{=}20$), well below the MDE of ${\sim}$9pp and thus indistinguishable from zero at current power. Adding a quadratic position term $(t/T)^2$ does not change significance conclusions for the 7--8B models. However, QwQ-32B's advantage is fully absorbed by the quadratic term (\cref{tab:position_quadratic}), indicating a non-linear position component. Temporal windowing reduces position dependence (\cref{sec:temporal}).\looseness=-1
75	
76	\enlargethispage{7\baselineskip}
77	\paragraph{Caveats.} Nested 5-fold CV confirms the HS precision advantage for both 7--8B models (10/10 folds; \cref{app:nested_cv}), with shrinkage of 13--25\% relative to holdout estimates. OT-7B nested CV selects L21--27 vs.\ holdout L16 vs.\ CR-composite L0; the +21.9pp holdout estimate is an upper bound. R1-32B achieves significance only at $W{=}1$ with 25\% coverage; at $W{\geq}3$, dimensionality prevents significance. QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps). False alarm rates remain 11--50\%, so current methods characterize the phenomenon rather than constitute production detectors. Per-model details in \cref{sec:32b-analysis}.\looseness=-1
78	
79	\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
80	
81	\paragraph{Exploratory 32B analysis.} Both 32B results are exploratory ($n{=}19$--$20$ precludes nested CV). LOO-CV and multi-seed analyses (\cref{app:layer_sweep,app:multi_seed}) provide partial robustness checks but do not substitute for independent validation. R1-32B and QwQ-32B share the Qwen-32B architecture but present opposite detection profiles (\cref{tab:32b_divergence}); training method is one plausible differentiator. Replication with $n{\geq}50$ traces is needed.\looseness=-1
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\resizebox{\columnwidth}{!}{%
87	\begin{tabular}{lcccc}
88	\toprule
89	\textbf{Model} & \textbf{Cov.} & \textbf{Lead (steps)} & \textbf{HB} & \textbf{Pos.\ margin} \\
90	\midrule
91	R1-32B$^\dagger$ & 25\% & +11.7 to +13.3 & \checkmark{} ($W{=}1$) & +14.2pp \\
92	QwQ-32B$^\dagger$ & 74\% & $-$1.2 to +1.9 & \checkmark{} (all $W$) & $-$3.6pp \\
93	\bottomrule
94	\end{tabular}}
95	\caption{32B cross-model divergence ($\dagger$\,sample-limited, $n \leq 20$; MDE at 80\% power: 8.6--9.5pp, \cref{app:power_analysis}; all conclusions exploratory). R1-32B provides limited early identification with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: \checkmark{} = passes Holm-Bonferroni ($\alpha{=}0.05$). Pos.\ margin: HS BA minus position baseline.}
96	\label{tab:32b_divergence}
97	\end{table}
98	
99	R1-32B suggests commitment 11--13 steps early (+14.2pp over position baseline) but covers only 25\% of traces ($W{=}1$); the precision effect (+15.4pp, CI width 13.9pp) falls below MDE at 80\% power. QwQ-32B achieves significance at all window sizes with 74\% coverage but negative HS lead time; the precision effect (+19.2pp, CI width 24.2pp) exceeds MDE (8.6--9.5pp; \cref{app:power_analysis}) but the position baseline achieves higher BA (0.832 vs.\ 0.796), and the HS precision margin over position (+4.5pp, $p{=}0.133$; \cref{app:position_residual}) is not significant at $n{=}19$. The divergence suggests per-model validation is needed.\looseness=-1
100	
101	\subsection{Temporal Context}\label{sec:temporal}
102	
103	Temporal windowing ($W{>}1$) improves both modalities (\cref{fig:window_ablation}): at 7--8B, the modality advantage (+20.1 to +21.9pp) exceeds temporal improvement (+13pp). GRU models achieve comparable accuracy but higher FPR (\cref{tab:gru_multi_seeds,app:temporal_details}); an adaptive two-stage strategy offers marginal gains (\cref{app:two_stage}).\looseness=-1
104	
105	CP-aligned probe score trajectories (\cref{fig:trajectory} in Appendix) confirm sharper HS transitions at the commitment point, with OT-7B showing the clearest separation and R1-32B the weakest. A forest plot visualizing precision gaps across encoder conditions appears in \cref{fig:forest_precision}.\looseness=-1
106	
107	\subsection{Negative Results}\label{sec:negative}
108	
109	No alternative method consistently matches supervised probing (\cref{tab:negative}). BOCPD~\citep{adams2007bayesian}/CUSUM fail (0\% detection on 3/4 models); Mahalanobis yields near-zero separation; RepE~\citep{zou2023representation} is model-dependent (BA 0.756 vs.\ 0.559); MLP probes overfit; CCS misaligns temporally; cross-model transfer fails (\cref{app:negative_details}). The signal is directional, gradual, model-specific, and linearly separable, which excludes change-point, distance, transfer, and objective-alignment methods respectively.\looseness=-1
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a31fd465-ca1d-4821-8f36-0eed3df8ed61",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "fd490e3b-3b9e-44db-99c6-ce6556319395",
  "sourceToolAssistantUUID": "a31fd465-ca1d-4821-8f36-0eed3df8ed61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T10:01:35.900Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HkDZviwqP8ooZnGPJXYj9W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd490e3b-3b9e-44db-99c6-ce6556319395",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQyiuCKUeVQvcRx3gGZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cb369ba-d636-4324-b59a-50fabc1d3597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuiXSggDdRTDvEKEirSbjZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5887,
      "cache_read_input_tokens": 28681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5887,
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

_source line 23 · 2026-05-22T10:01:35.907Z_

<details><summary>↩ Tool result · `toolu_01HkDZviwqP8ooZnGPJXYj9W`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	Crossing rate reverses the central finding via shallow-layer compression (\cref{app:cosine_volatility,tab:r18b_full_layer}): its shallow preference is an artifact of cosine compression inflating threshold crossings, while threshold-based deep preference reflects genuine separability~\citep{tenney2019bert}; random-label controls confirm this distinction (\cref{app:random_cp}). C1 generalizes across all four models (cross-dataset: \cref{app:cosine_volatility}; split-half: \cref{app:split_half}); C2 is sample-dependent (7--8B cross-validated, 32B descriptive). Annotation noise (${<}2.5$pp BA change; \cref{tab:cp_perturbation}) does not threaten C1. The encoder-quality gradient narrows the HS advantage (384d to 1024d; \cref{app:position_residual}). Type~I risk from ${\sim}$2{,}240 configurations is bounded by the two-stage design and large effect sizes ($d$ 0.58--2.37; \cref{app:effective_tests}). \textbf{Practical mitigation.} We propose a three-level defense against metric-induced layer selection bias. \emph{Level~1 (minimal)}: report layer selections under both threshold-based and frequency-based metric families; divergence exceeding 20\% of model depth (e.g., L2 vs.\ L63 in a 64-layer model) indicates metric-induced bias and warrants treating conclusions as provisional. \emph{Level~2 (recommended)}: a multi-metric audit (\cref{app:deployment_operating_points}) computes all five metrics and flags when ${\geq}3$ select layers differing by ${>}20\%$ of depth---an operational test requiring no additional data. \emph{Level~3 (robust)}: a three-layer ensemble averaging probe predictions from the precision-best, BA-best, and inverse-FPR-best layers eliminates metric pre-selection entirely ($p \leq 0.002$; \cref{tab:ensemble}), but requires cross-validated confirmation before deployment.\looseness=-1
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cb369ba-d636-4324-b59a-50fabc1d3597",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "534f5274-98de-4a29-8d07-4935931edcb4",
  "sourceToolAssistantUUID": "4cb369ba-d636-4324-b59a-50fabc1d3597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T10:01:36.952Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WieEavdinWcBZfkFZryJFe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "534f5274-98de-4a29-8d07-4935931edcb4",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQyiuCKUeVQvcRx3gGZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c4c98c1-9572-4989-b10d-be851069f8a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuiXSggDdRTDvEKEirSbjZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5887,
      "cache_read_input_tokens": 28681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5887,
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

_source line 25 · 2026-05-22T10:01:36.957Z_

<details><summary>↩ Tool result · `toolu_01WieEavdinWcBZfkFZryJFe`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Layer selection metric choice can reverse a safety study's central conclusion: for QwQ-32B, the same data yield $p{=}0.83$ or $p{<}0.005$ depending solely on metric. The HS advantage is validated at 7--8B (+20--22pp, nested CV) and exploratory$^\dagger$ at 32B (+15--19pp) against 384d encoders, but conditional on encoder quality and position (partially correlated); generalization beyond HarmThoughts and Qwen (3/4) requires causal validation. Until layer selection is controlled, probe-based safety conclusions from any single metric should be treated as provisional.\looseness=-1
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c4c98c1-9572-4989-b10d-be851069f8a5",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "cac1e251-09f0-4946-b155-ff9b82b63932",
  "sourceToolAssistantUUID": "1c4c98c1-9572-4989-b10d-be851069f8a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T10:01:37.117Z_

<details open><summary>🔧 Tool call — Read · `toolu_011DBwzQUorqkfRibGovZuyy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cac1e251-09f0-4946-b155-ff9b82b63932",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQyiuCKUeVQvcRx3gGZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1dec8d04-6813-486a-9d00-069990c8de6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuiXSggDdRTDvEKEirSbjZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5887,
      "cache_read_input_tokens": 28681,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 28681,
          "cache_creation_input_tokens": 5887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5887,
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

_source line 27 · 2026-05-22T10:01:37.121Z_

<details><summary>↩ Tool result · `toolu_011DBwzQUorqkfRibGovZuyy`</summary>

```text
1	\newpage
2	\section*{Limitations}\label{sec:limitations}
3	
4	\paragraph{Single dataset and annotation quality.}
5	All CP-dependent claims rely on one dataset (HarmThoughts~\citep{harmthoughts}), the only publicly available dataset providing step-level CP annotations for reasoning model traces, with annotations lacking formal inter-annotator agreement; an LLM-based proxy on AdvBench achieved $\kappa{=}0.606$ (\cref{app:iaa}). The geometric precondition (shallow-layer compression) is confirmed on AdvBench (\cref{app:cosine_volatility,app:advbench_cp}), but generalization to other jailbreak datasets, attack taxonomies, or multilingual settings is untested.
6	
7	\paragraph{Statistical power at 32B.}
8	With $n{=}19$--$20$ traces, the minimum detectable effect at 80\% power is 8.6--9.5pp (\cref{app:power_analysis}); all 32B conclusions marked $\dagger$ should be interpreted with this constraint. False positive rates remain 11--50\% (model-dependent), and R1-32B achieves significance only at $W{=}1$ (25\% coverage). These probes characterize the commitment phenomenon rather than constitute production detectors.
9	
10	\paragraph{Architecture coverage and causal status.}
11	Three of four models share the Qwen architecture; only R1-8B (Llama) provides cross-architecture evidence. Random-label controls confirm the crossing-rate geometric bias is Qwen-specific (\cref{app:random_cp}). Results are correlational; causal intervention (e.g., DAS, activation patching) is needed to confirm mechanistic involvement. Whether metric-induced layer selection bias generalizes to non-reasoning LLMs or encoder-only architectures remains open.
12	
13	\section*{Ethics Statement}
14	This work analyzes safety-relevant reasoning traces to characterize probe behavior, not to circumvent safety mechanisms. All experiments use publicly available models and datasets (HarmThoughts, AdvBench). No human subjects were involved. Code and scripts for all experiments and analyses will be released upon acceptance.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1dec8d04-6813-486a-9d00-069990c8de6a",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "8d81dea4-7078-4481-8db7-7ee9baa90919",
  "sourceToolAssistantUUID": "1dec8d04-6813-486a-9d00-069990c8de6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-22T10:01:39.968Z_

Now let me read the appendix for completeness, and check the references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d81dea4-7078-4481-8db7-7ee9baa90919",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQz9DvUmkjxzrUKUnYt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9115a87c-4b19-4022-bc97-cfadb95eb65e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GMAA5LcM81wcUbTyUJzhF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 34568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1577,
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

_source line 29 · 2026-05-22T10:01:40.451Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NCAnhevqRirmWRvG9Ebupx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9115a87c-4b19-4022-bc97-cfadb95eb65e",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQz9DvUmkjxzrUKUnYt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9759e7b2-1ad8-4f73-9255-e0a79ce3f615",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GMAA5LcM81wcUbTyUJzhF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 34568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1577,
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

_source line 30 · 2026-05-22T10:01:40.732Z_

<details><summary>↩ Tool result · reported error · `toolu_01NCAnhevqRirmWRvG9Ebupx`</summary>

```text
File content (37324 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9759e7b2-1ad8-4f73-9255-e0a79ce3f615",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "bb4645fa-09c7-464f-8849-ceffea871b48",
  "toolUseResult": "Error: File content (37324 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "9759e7b2-1ad8-4f73-9255-e0a79ce3f615",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T10:01:40.947Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YBToX8MK1QdrKRsmfEjjbP`</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb4645fa-09c7-464f-8849-ceffea871b48",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQz9DvUmkjxzrUKUnYt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7128bf43-18ed-47d3-9627-68f3e67a037d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GMAA5LcM81wcUbTyUJzhF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 34568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1577,
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

_source line 32 · 2026-05-22T10:01:40.990Z_

<details><summary>↩ Tool result · `toolu_01YBToX8MK1QdrKRsmfEjjbP`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7128bf43-18ed-47d3-9627-68f3e67a037d",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "5a570127-f1fe-420c-a902-dda0bbbfd677",
  "sourceToolAssistantUUID": "7128bf43-18ed-47d3-9627-68f3e67a037d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T10:01:44.936Z_

<details open><summary>🔧 Tool call — Read · `toolu_012ZwbT5DZL7hSdvzPweoT1s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a570127-f1fe-420c-a902-dda0bbbfd677",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQzRirnN4d8ANkCSGhz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dd297a8-0bdd-410c-8781-5775159660be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jv2DKUQJckjpfH9DayvrHJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 307,
      "cache_read_input_tokens": 36145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 307,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 34 · 2026-05-22T10:01:44.943Z_

<details><summary>↩ Tool result · `toolu_012ZwbT5DZL7hSdvzPweoT1s`</summary>

```text
1	\appendix
2	
3	\noindent\textbf{Appendix Contents:}
4	\cref{app:checklist}~Responsible NLP Research Checklist;
5	\cref{app:layer_sweep}~Layer Sweep Results;
6	\cref{app:cosine_volatility}~Representation Compression Analysis;
7	\cref{app:holm_bonferroni}~Holm-Bonferroni Correction;
8	\cref{app:window_ablation}~Window Size Ablation;
9	\cref{app:ot7b_details}~OpenThinker-7B Details;
10	\cref{app:gru_details}~GRU Training Details;
11	\cref{app:control}~Control Task Methodology;
12	\cref{sec:oracle}~Oracle Upper Bound;
13	\cref{app:cp_perturbation}~CP Annotation Perturbation;
14	\cref{app:bocpd_config}~BOCPD/CUSUM Configuration;
15	\cref{app:k_ablation}~Detection Threshold Ablation;
16	\cref{app:threshold_sensitivity}~Decision Threshold Sensitivity;
17	\cref{app:bug}~M002 Bug Disclosure;
18	\cref{app:two_stage}~Adaptive Two-Stage Detection;
19	\cref{app:temporal_details}~Temporal Ablation Details;
20	\cref{app:negative_details}~Negative Results Details (incl.\ \cref{tab:negative});
21	\cref{app:transfer_details}~Cross-Model Transfer Details;
22	\cref{app:encoder_robustness}~Encoder Robustness;
23	\cref{app:random_projection}~Random Projection Baseline;
24	\cref{app:e5_mistral}~LLM-Based Text Encoder;
25	\cref{app:position_residual}~Position-Residualized Probing;
26	\cref{app:hyperparameter_robustness}~Hyperparameter Robustness;
27	\cref{app:multi_seed}~Multi-Seed Stability;
28	\cref{app:split_half}~Split-Half Internal Validity;
29	\cref{app:ba_layer_comparison}~BA-Layer Modality Comparison;
30	\cref{app:power_analysis}~Post-Hoc Power Analysis.
31	
32	\section{Responsible NLP Research Checklist}
33	\label{app:checklist}
34	
35	We address the ARR Responsible NLP Research requirements below.
36	
37	\begin{itemize}
38	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
39	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark. We acknowledge a dual-use concern: safety probes that detect commitment could in principle be used to craft reasoning traces that evade detection. We believe the defensive value of understanding commitment dynamics outweighs this risk, as evasion requires white-box access to the probe, which a deployed monitoring system would not expose.
40	    \item \textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
41	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations, and AdvBench~\citep{advbench} for cross-dataset geometric validation. No new data collection was performed.
42	    \item \textbf{Human subjects:} No human subjects research was conducted.
43	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
44	\end{itemize}
45	
46	
47	\section{Layer Sweep Results}
48	\label{app:layer_sweep}
49	
50	For each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\times$ crossing rate (the CR-composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The CR-composite systematically selects shallow layers across all four models (including R1-8B under the full L0--L24 sweep; \cref{tab:r18b_full_layer}) because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. Three threshold-based metrics (precision, inverse FPR, additive composite) converge on deep layers for all models; pure balanced accuracy selects layers whose depth varies with the data split (under 70/30: L30 for QwQ-32B, L47 for R1-32B; under the canonical 60/20/20: L63 and L46 respectively; \cref{tab:ba_layer_results}).
51	
52	\paragraph{Selected layers.} R1-8B: under the original L12--L24 sweep, all five metrics agreed on L14 (44\%); extending to L0--L24, crossing rate shifts to L0 while threshold-based metrics retain L14, a 16-layer gap (\cref{tab:r18b_full_layer}). OT-7B: CR-composite selects L0 (0\%), threshold-based consensus selects L16 (57\%). QwQ-32B: CR-composite selects L2 (3\%), threshold-based consensus selects L63 (98\%). R1-32B: CR-composite selects L10 (16\%), threshold-based consensus selects L63 (98\%). The disagreement is most extreme for 64-layer models, where the CR-composite selects layers in the bottom 16\% of the network while threshold-based metrics select layers at 98\% depth. Under 70/30, pure balanced accuracy selects L30 (47\%) for QwQ-32B and L47 (73\%) for R1-32B; under the canonical 60/20/20, it selects L63 (98\%) and L46 (72\%), which demonstrates sensitivity to the data split.
53	
54	\paragraph{Impact on modality comparison.} At the CR-composite layers, HS vs.\ text precision $p$-values are 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant. At the threshold-based deep layers, all $p$-values fall below 0.005. The initially reported ``scale-dependent'' pattern (HS advantage at 7--8B but not 32B) was entirely an artifact of layer selection methodology, not a genuine property of model scale (\cref{sec:layer-results}).
55	
56	\paragraph{Layer selection stability (LOO-CV).} Leave-one-out cross-validation on the validation set shows moderate consistency for 7--8B models (65--68\% dominant-layer agreement) but lower for 32B, confirming that layer selection instability is particularly acute at small sample sizes. Under pure balanced accuracy, the dominant layer is selected in 68\% (QwQ-32B: L30, 13/19 folds) and 65\% (R1-32B: L47, 13/20 folds) of folds. Alternative selections scatter across neighboring layers (L29, L55--56 for QwQ; L32, L38, L43 for R1-32B), reinforcing the need for multi-metric auditing rather than single-metric layer selection. Threshold-based metrics show tighter convergence to L63 for both 32B models. Expanding the criterion from top-1 to top-3 layers does not change conclusions: the top-3 BA-selected layers for QwQ-32B (L30, L29, L55) and R1-32B (L47, L43, L38) all fall in the mid-to-deep range, and threshold-based metrics remain converged at L63 across all folds.
57	
58	\paragraph{Joint (layer, $W$) sensitivity.} Under the original 70/30 validation protocol, we evaluate QwQ-32B across 64 layers $\times$ 3 windows ($W \in \{1, 3, 5\}$) (192 configurations) (\cref{tab:joint_layer_w}). L60 is near-optimal: within 2.1pp of the global best at $W{=}3$ and the top-ranked layer at $W{=}5$. (Under 60/20/20, threshold-based metrics select L63; the shift from L60 to L63 across splits itself illustrates layer selection sensitivity.) The optimal layer shifts from middle-deep (L46--47 at $W{=}1$) to deep (L60 at $W{=}5$), confirming a layer-window interaction. For R1-8B, optimal precision layers shift similarly (L16 at $W{=}1$ $\to$ L9 at $W{=}15$; Kendall's $\tau{=}{-}0.91$, $p{=}0.071$), a consistent negative trend that does not reach significance at $n{=}4$ windows. L30, selected by per-fold LOO-CV at $W{=}1$ under balanced accuracy, is suboptimal across all windows (max BA $= 0.769$ vs.\ global best 0.817). Joint (layer, $W$) stability was evaluated via grid search on $W \in \{1, 3, 5\}$ for QwQ-32B only; full leave-one-fold-out validation of the (layer, $W$) pair and extension to R1-32B remain for future work.
59	
60	\begin{table}[htbp]
61	\centering
62	\small
63	\caption{QwQ-32B joint (layer, $W$) grid search under 70/30 validation. L60 is near-optimal at recommended windows ($W{=}3$--$5$). L30 (LOO-CV selection at $W{=}1$) is suboptimal across all windows. Under the canonical 60/20/20 split, threshold-based metrics select L63.}
64	\label{tab:joint_layer_w}
65	\resizebox{\columnwidth}{!}{%
66	\begin{tabular}{clccc}
67	\toprule
68	$W$ & \textbf{Best layer} & \textbf{Best BA} & \textbf{L60 BA} & \textbf{L60 rank} \\
69	\midrule
70	1 & L47 & 0.798 & 0.783 & $\sim$15th \\
71	3 & L46 & 0.817 & 0.796 & $\sim$6th \\
72	5 & L60 & 0.808 & 0.808 & 1st \\
73	\bottomrule
74	\end{tabular}}
75	\end{table}
76	
77	\paragraph{R1-8B full-layer sweep.}
78	\label{app:r18b_full_layer}
79	The original R1-8B layer sweep covered L12--L24 (13 layers), where all five metrics agreed on L14 (\cref{tab:layer_selection}). Extending to L0--L24 reveals that crossing rate consistently selects L0 across all window sizes, while threshold-based metrics retain mid-to-deep layers (L12--L16 for $W{=}1$--$5$; L9 at $W{=}15$, marginal $\Delta{=}0.003$ between shallow and deep means), a 9--16 layer divergence (\cref{tab:r18b_full_layer}). Unlike 32B models, the bias is isolated to crossing rate; threshold-based metrics show no shallow shift for R1-8B. This confirms the crossing-rate bias generalizes to Llama-architecture models. HS probes maintain significant advantage across all 25 layers and window sizes (precision gap ${\sim}$0.15--0.17), unlike OT-7B and 32B models where significance drops at shallow layers.
80	
81	\begin{table}[htbp]
82	\centering
83	\small
84	\caption{R1-8B full-layer sweep (L0--L24, extending the original L12--L24 range). Best layer selected by crossing rate vs.\ threshold-based metrics across four window sizes. Score = balanced accuracy at the threshold-based layer. Layer gap = crossing-rate layer minus threshold-based layer.}
85	\label{tab:r18b_full_layer}
86	\resizebox{\columnwidth}{!}{%
87	\begin{tabular}{lcccc}
88	\toprule
89	& $W{=}1$ & $W{=}3$ & $W{=}5$ & $W{=}15$ \\
90	\midrule
91	Crossing rate & L0 & L0 & L0 & L0 \\
92	Threshold (composite) & L16 (0.789) & L12 (0.796) & L12 (0.803) & L9 (0.784) \\
93	\midrule
94	Layer gap & 16 & 12 & 12 & 9 \\
95	\bottomrule
96	\end{tabular}}
97	\end{table}
98	
99	\subsection{Random-Label Decomposition Control}
100	\label{app:random_cp}
101	
102	To decompose the sources of metric disagreement in layer selection, we replace the true CP annotations with uniformly random labels and re-run the full layer sweep (10 random-label repeats per model). We test QwQ-32B (95 traces, 64 layers) and R1-8B (209 traces, 25 layers); \cref{tab:random_cp,tab:random_cp_r18b} report the fraction of repeats selecting a shallow layer and the mean selected layer.
103	
104	\begin{table}[htbp]
105	\centering
106	\small
107	\caption{QwQ-32B layer selection under random CP labels (10 repeats). Shallow\%: fraction selecting a layer L$\leq$10. Real-CP layer shown for reference.}
108	\label{tab:random_cp}
109	\setlength{\tabcolsep}{4pt}
110	\resizebox{\columnwidth}{!}{%
111	\begin{tabular}{lcccc}
112	\toprule
113	\textbf{Metric} & \textbf{Real-CP} & \textbf{Shallow\%} & \textbf{Rand.\ mean layer} \\
114	\midrule
115	Crossing rate & L4 & 100\% & $3.4 \pm 2.6$ \\
116	CR-composite & L4 & 80\% & $13.1 \pm 18.1$ \\
117	Precision & L63 & 20\% & $33.8 \pm 19.8$ \\
118	Inv.\ FPR & L62 & 10\% & $36.4 \pm 17.0$ \\
119	Bal.\ accuracy & L63 & 20\% & $33.3 \pm 20.3$ \\
120	\bottomrule
121	\end{tabular}}
122	\end{table}
123	
124	\begin{table}[htbp]
125	\centering
126	\small
127	\caption{R1-8B layer selection under random CP labels (10 repeats). Shallow\%: fraction selecting L$\leq$4 (bottom quintile of 25 layers). $\dagger$: degenerate, all repeats select L0 with zero variance, indicating destroyed signal rather than shallow preference.}
128	\label{tab:random_cp_r18b}
129	\setlength{\tabcolsep}{4pt}
130	\resizebox{\columnwidth}{!}{%
131	\begin{tabular}{lcccc}
132	\toprule
133	\textbf{Metric} & \textbf{Real-CP} & \textbf{Shallow\%} & \textbf{Rand.\ mean layer} \\
134	\midrule
135	Crossing rate & L0 & 0\% & $10.7 \pm 4.8$ \\
136	CR-composite & L0 & 0\% & $13.7 \pm 6.7$ \\
137	Precision & L23 & 100\%$^{\dagger}$ & $0.0 \pm 0.0$ \\
138	Inv.\ FPR & L13 & 100\%$^{\dagger}$ & $0.0 \pm 0.0$ \\
139	Bal.\ accuracy & L19 & 0\% & $14.0 \pm 4.0$ \\
140	\bottomrule
141	\end{tabular}}
142	\end{table}
143	
144	\paragraph{QwQ-32B (Qwen).} The results decompose the metric disagreement into two components. (A)~The crossing-rate shallow-layer preference is label-independent: 100\% of random-label repeats still select layers L0--L7, confirming that this bias reflects representation geometry (shallow-layer cosine distance compression; \cref{app:cosine_volatility}) rather than any property of the safety labels. The CR-composite inherits this bias (80\% shallow). (B)~Threshold-based metrics (precision, inverse FPR) select deep layers only with real safety labels; under random labels, selections scatter across the full layer range (mean L34--L36, high variance). The full metric disagreement (L4 vs.\ L63, a 59-layer gap) is the superposition of a geometric artifact on the crossing-rate side and a real safety signal on the threshold-based side.
145	
146	\paragraph{R1-8B (Llama).} The Llama-based model shows stronger label dependence: crossing rate scatters from L0 to mean L$10.7 \pm 4.8$ under random labels (0\% shallow), unlike QwQ-32B where it retains shallow preference. Threshold-based metrics degenerate entirely: precision and inverse FPR select L0 in all 10 repeats with zero variance, indicating random labels destroy discriminative signal rather than merely redistributing it. The real-CP disagreement (L0 vs.\ L23, a 23-layer gap) vanishes completely under random labels.
147	
148	\paragraph{Cross-architecture summary.} The metric disagreement requires genuine safety labels in both architectures, but the mechanism differs: in QwQ-32B, crossing-rate shallow preference reflects representation geometry (label-independent cosine compression), while in R1-8B even crossing-rate layer selection is label-dependent. The geometric component of the crossing-rate bias is thus Qwen-specific rather than a universal property of transformer representations.
149	
150	\section{Representation Compression Analysis}
151	\label{app:cosine_volatility}
152	
153	We measure step-to-step cosine distance at CR-composite (shallow) vs.\ threshold-based (deep) layers across all models to characterize the compression mechanism underlying the crossing rate bias (\cref{tab:cosine_volatility}).
154	
155	\begin{table}[htbp]
156	\centering
157	\small
158	\caption{Step-to-step cosine distance at CR-composite (shallow) and threshold-based (deep) layers. Shallow layers produce highly compressed representations (1.4--2.7$\times$ smaller inter-step distances).}
159	\label{tab:cosine_volatility}
160	\resizebox{\columnwidth}{!}{%
161	\begin{tabular}{llcc}
162	\toprule
163	\textbf{Model} & \textbf{Layer (type)} & \textbf{Mean} & \textbf{Std} \\
164	\midrule
165	R1-8B & L2 (CR-comp.) & 0.186 & 0.097 \\
166	 & L14 (thresh.) & 0.411 & 0.143 \\[2pt]
167	OT-7B & L2 (CR-comp.) & 0.077 & 0.080 \\
168	 & L16 (thresh.) & 0.206 & 0.091 \\[2pt]
169	QwQ-32B & L2 (CR-comp.) & 0.037 & 0.064 \\
170	 & L63 (thresh.) & 0.084 & 0.056 \\[2pt]
171	R1-32B & L10 (CR-comp.) & 0.067 & 0.050 \\
172	 & L63 (thresh.) & 0.092 & 0.076 \\
173	\bottomrule
174	\end{tabular}}
175	\end{table}
176	
177	Shallow layers produce highly compressed representations: consecutive steps cluster within small cosine distances (0.04--0.19), while deep-layer representations spread more widely (0.09--0.41). Inter-step distances at shallow layers are 1.4--2.7$\times$ smaller than at deep layers across all models. A linear probe operating in this compressed space sits near the noise floor, where minor numerical fluctuations produce spurious threshold crossings that inflate crossing rate independently of discriminative power. Deep layers produce well-separated representations where crossings correspond to genuine semantic transitions.
178	
179	\paragraph{Cross-dataset evidence.}
180	To assess whether this geometric precondition generalizes beyond HarmThoughts, we compute the same shallow/deep volatility ratio on AdvBench~\citep{advbench} traces using R1-8B. The deep-layer mean cosine distance (0.442) is $1.67\times$ the shallow-layer mean (0.265), consistent with the 1.4--2.7$\times$ range observed across all four models on HarmThoughts (\cref{tab:cosine_volatility}). This confirms that the representational compression underlying metric-induced layer selection bias is not dataset-specific and does not depend on CP annotations.
181	
182	\subsection{AdvBench Boundary Condition}
183	\label{app:advbench_cp}
184	
185	We analyze R1-8B behavior on 388 substantive-response AdvBench~\citep{advbench} traces (of 520 total) to characterize a boundary condition for the CP framework (\cref{tab:advbench_boundary}).
186	
187	\begin{table}[htbp]
188	\centering
189	\small
190	\caption{R1-8B behavior on AdvBench adversarial prompts (388 substantive-response traces of 520 total). CP${=}0$ indicates the model produces harmful content from the first reasoning step without prior safety deliberation.}
191	\label{tab:advbench_boundary}
192	\resizebox{\columnwidth}{!}{%
193	\begin{tabular}{lc}
194	\toprule
195	\textbf{Metric} & \textbf{Value} \\
196	\midrule
197	Jailbreak rate & 13.4\% \\
198	CP${=}0$ (among JB) & 90.4\% \\
199	Mean CP position (among JB) & 1.4 steps \\
200	\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dd297a8-0bdd-410c-8781-5775159660be",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "dd5095e6-cbef-484d-91e1-e3d4d87b6faa",
  "sourceToolAssistantUUID": "8dd297a8-0bdd-410c-8781-5775159660be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T10:01:45.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WppHLWd5M3kjTginMyDwCv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd5095e6-cbef-484d-91e1-e3d4d87b6faa",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQzRirnN4d8ANkCSGhz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a14b3a63-9e63-4419-94d4-afedd66452ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jv2DKUQJckjpfH9DayvrHJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 307,
      "cache_read_input_tokens": 36145,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 307
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 36145,
          "cache_creation_input_tokens": 307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 307,
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

_source line 36 · 2026-05-22T10:01:45.760Z_

<details><summary>↩ Tool result · `toolu_01WppHLWd5M3kjTginMyDwCv`</summary>

```text
1	@article{trajguard,
2	  title={TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense},
3	  author={Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi},
4	  journal={arXiv preprint arXiv:2604.07727},
5	  year={2026},
6	  url={https://arxiv.org/abs/2604.07727}
7	}
8	
9	@inproceedings{safeswitch,
10	  title={SafeSwitch: Steering Unsafe {LLM} Behavior via Internal Activation Signals},
11	  author={Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zhang, Denghui},
12	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
13	  year={2025},
14	  url={https://arxiv.org/abs/2502.01042}
15	}
16	
17	@inproceedings{siren,
18	  title={{LLM} Safety From Within: Detecting Harmful Content with Internal Representations},
19	  author={Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu, Haolun and Anderson, Ashton},
20	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
21	  year={2026},
22	  url={https://arxiv.org/abs/2604.18519}
23	}
24	
25	@article{saferemind,
26	  title={How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs},
27	  author={Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub},
28	  journal={arXiv preprint arXiv:2601.03662},
29	  year={2026},
30	  url={https://arxiv.org/abs/2601.03662}
31	}
32	
33	@article{safethink,
34	  title={Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away},
35	  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Furong and Manocha, Dinesh and Bedi, Amrit Singh},
36	  journal={arXiv preprint arXiv:2602.11096},
37	  year={2026},
38	  url={https://arxiv.org/abs/2602.11096}
39	}
40	
41	@article{selfjailbreak,
42	  title={Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training},
43	  author={Yong, Zheng-Xin and Bach, Stephen H.},
44	  journal={arXiv preprint arXiv:2510.20956},
45	  year={2025},
46	  url={https://arxiv.org/abs/2510.20956}
47	}
48	
49	@article{harmthoughts,
50	  title={When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains},
51	  author={Kakkar, Ishita and Zhang, Enze and Uppaal, Rheeya and Hu, Junjie},
52	  journal={arXiv preprint arXiv:2604.19001},
53	  year={2026},
54	  url={https://arxiv.org/abs/2604.19001}
55	}
56	
57	@article{belinkov2019analysis,
58	  title={Analysis Methods in Neural Language Processing: A Survey},
59	  author={Belinkov, Yonatan and Glass, James},
60	  journal={Transactions of the Association for Computational Linguistics},
61	  volume={7},
62	  pages={49--72},
63	  year={2019},
64	  url={https://aclanthology.org/Q19-1004/}
65	}
66	
67	@inproceedings{kaya2019shallow,
68	  title={Shallow-Deep Networks: Understanding and Mitigating Network Overthinking},
69	  author={Kaya, Yigitcan and Hong, Sanghyun and Dumitras, Tudor},
70	  booktitle={Proceedings of the 36th International Conference on Machine Learning (ICML)},
71	  pages={3301--3310},
72	  year={2019},
73	  url={https://arxiv.org/abs/1810.07052}
74	}
75	
76	@inproceedings{zhou2020bert,
77	  title={{BERT} Loses Patience: Fast and Robust Inference with Early Exit},
78	  author={Zhou, Wangchunshu and Xu, Canwen and Ge, Tao and McAuley, Julian and Xu, Ke and Wei, Furu},
79	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
80	  volume={33},
81	  pages={18330--18341},
82	  year={2020},
83	  url={https://arxiv.org/abs/2006.04152}
84	}
85	
86	@inproceedings{hewitt2019control,
87	  title={Designing and Interpreting Probes with Control Tasks},
88	  author={Hewitt, John and Liang, Percy},
89	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
90	  pages={2733--2743},
91	  year={2019},
92	  url={https://aclanthology.org/D19-1275/}
93	}
94	
95	@article{zou2023representation,
96	  title={Representation Engineering: A Top-Down Approach to {AI} Transparency},
97	  author={Zou, Andy and Phan, Long and Chen, Sarah and Campbell, James and Guo, Phillip and Ren, Richard and Pan, Alexander and Yin, Xuwang and Mazeika, Mantas and Dombrowski, Ann-Kathrin and Goel, Shashwat and Li, Nathaniel and Byun, Michael J. and Wang, Zifan and Mallen, Alex and Basart, Steven and Koyejo, Sanmi and Song, Dawn and Fredrikson, Matt and Kolter, J. Zico and Hendrycks, Dan},
98	  journal={arXiv preprint arXiv:2310.01405},
99	  year={2023},
100	  url={https://arxiv.org/abs/2310.01405}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a14b3a63-9e63-4419-94d4-afedd66452ec",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "6ff2ee25-0523-46f5-9b27-17fd3bf679b4",
  "sourceToolAssistantUUID": "a14b3a63-9e63-4419-94d4-afedd66452ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-22T10:01:52.581Z_

Now let me check the paper title discrepancy - the actual paper title differs from the task description. Let me also look more carefully at related work coverage and any AdvBench cross-dataset sections in the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ff2ee25-0523-46f5-9b27-17fd3bf679b4",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQzn8CGyMw18FjZaHCX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ac0bd89-fc10-4550-975a-52fa5cd196cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jPxNWXL1sfWvxoWuBCPoe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8094,
      "cache_read_input_tokens": 36452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8094,
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

_source line 38 · 2026-05-22T10:01:54.166Z_

<details open><summary>🔧 Tool call — Read · `toolu_01McoeZFQdinuie1TthR7YMM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": 180,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ac0bd89-fc10-4550-975a-52fa5cd196cd",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHQzn8CGyMw18FjZaHCX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7964b98f-dc5a-4ead-99fe-73bdaa6345c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jPxNWXL1sfWvxoWuBCPoe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8094,
      "cache_read_input_tokens": 36452,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8094
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 36452,
          "cache_creation_input_tokens": 8094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8094,
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

_source line 39 · 2026-05-22T10:01:54.171Z_

<details><summary>↩ Tool result · `toolu_01McoeZFQdinuie1TthR7YMM`</summary>

```text
180	To assess whether this geometric precondition generalizes beyond HarmThoughts, we compute the same shallow/deep volatility ratio on AdvBench~\citep{advbench} traces using R1-8B. The deep-layer mean cosine distance (0.442) is $1.67\times$ the shallow-layer mean (0.265), consistent with the 1.4--2.7$\times$ range observed across all four models on HarmThoughts (\cref{tab:cosine_volatility}). This confirms that the representational compression underlying metric-induced layer selection bias is not dataset-specific and does not depend on CP annotations.
181	
182	\subsection{AdvBench Boundary Condition}
183	\label{app:advbench_cp}
184	
185	We analyze R1-8B behavior on 388 substantive-response AdvBench~\citep{advbench} traces (of 520 total) to characterize a boundary condition for the CP framework (\cref{tab:advbench_boundary}).
186	
187	\begin{table}[htbp]
188	\centering
189	\small
190	\caption{R1-8B behavior on AdvBench adversarial prompts (388 substantive-response traces of 520 total). CP${=}0$ indicates the model produces harmful content from the first reasoning step without prior safety deliberation.}
191	\label{tab:advbench_boundary}
192	\resizebox{\columnwidth}{!}{%
193	\begin{tabular}{lc}
194	\toprule
195	\textbf{Metric} & \textbf{Value} \\
196	\midrule
197	Jailbreak rate & 13.4\% \\
198	CP${=}0$ (among JB) & 90.4\% \\
199	Mean CP position (among JB) & 1.4 steps \\
200	\bottomrule
201	\end{tabular}}
202	\end{table}
203	
204	Adversarial prompts designed to bypass safety mechanisms (e.g., GCG suffixes) cause the model to skip safety deliberation entirely: 90.4\% of jailbroken traces have CP${=}0$, meaning the model commits to harmful generation from the first reasoning step. This contrasts with HarmThoughts, where non-adversarial prompts trigger extended safety deliberation before commitment (mean relative CP position ${\approx}0.7$). The CP framework is most informative when prompts elicit deliberation that can be monitored; adversarial prompts that circumvent deliberation represent a boundary condition where commitment detection is vacuous. The geometric compression evidence (\cref{tab:cosine_volatility}; volatility ratio $1.67\times$) remains valid because it measures representational properties independent of CP annotations.
205	
206	\section{Holm-Bonferroni Step-Down Correction}
207	\label{app:holm_bonferroni}
208	
209	\cref{tab:holm_bonferroni} reports the full test battery used to assess hidden-state superiority over text probes. Because balanced accuracy, precision, and FPR share the same confusion matrix, the three per-model metrics are correlated; the effective number of independent comparisons is four (one per model). We report both the conservative 12-test correction and the 4-test model-level correction: both yield the same outcome (all tests pass at $\alpha{=}0.05$). Under 4-test HB, the tightest threshold falls on R1-8B FPR ($p{=}0.044$, rank-4 threshold $\alpha/1{=}0.050$), which still passes. Tests are ranked by $p$-value; each test $i$ (rank $i$ of $m$) must satisfy $p_i < \alpha / (m - i + 1)$ under the step-down procedure.
210	
211	\begin{table}[htbp]
212	\centering
213	\small
214	\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}
215	\label{tab:holm_bonferroni}
216	\setlength{\tabcolsep}{4pt}
217	\resizebox{\columnwidth}{!}{%
218	\begin{tabular}{clllcc}
219	\toprule
220	\textbf{Rank} & \textbf{Model} & \textbf{Metric} & \textbf{$p$-val} & \textbf{Thresh.} & \textbf{Pass} \\
221	\midrule
222	1  & R1-8B  & Precision & $<$0.001 & 0.0042 & \checkmark \\
223	2  & OT-7B  & Bal.\ Acc. & $<$0.001 & 0.0045 & \checkmark \\
224	3  & OT-7B  & Precision & $<$0.001 & 0.0050 & \checkmark \\
225	4  & OT-7B  & FPR & $<$0.001 & 0.0056 & \checkmark \\
226	5  & QwQ-32B & Bal.\ Acc. & $<$0.001 & 0.0063 & \checkmark \\
227	6  & QwQ-32B & Precision & $<$0.001 & 0.0071 & \checkmark \\
228	7  & R1-32B & Bal.\ Acc. & $<$0.001 & 0.0083 & \checkmark \\
229	8  & R1-32B & Precision & $<$0.001 & 0.0100 & \checkmark \\
230	9  & QwQ-32B & FPR & 0.004 & 0.0125 & \checkmark \\
231	10 & R1-8B  & Bal.\ Acc. & 0.005 & 0.0167 & \checkmark \\
232	11 & R1-32B & FPR & 0.007 & 0.0250 & \checkmark \\
233	12 & R1-8B  & FPR & 0.044 & 0.0500 & \checkmark \\
234	\bottomrule
235	\end{tabular}}
236	\end{table}
237	
238	The weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B's precision gap (+20.1pp at $W{=}3$). This reflects R1-8B's already-low text FPR (11.8\%), which leaves less room for HS improvement on this metric.
239	
240	\paragraph{Exact sign-flip permutation test validation.} As an independent check on bootstrap significance for the small-sample 32B models, we run exact sign-flip permutation tests on all six 32B comparisons, enumerating all $2^n$ sign permutations ($2^{19}{=}524{,}288$ for QwQ-32B, $2^{20}{=}1{,}048{,}576$ for R1-32B). All six tests reject the null at $\alpha{=}0.05$: QwQ-32B (bal\_acc $p{<}0.001$, precision $p{=}0.003$, FPR $p{<}0.001$); R1-32B (bal\_acc $p{=}0.008$, precision $p{<}0.001$, FPR $p{=}0.004$). The permutation $p$-values are consistent with the bootstrap values in \cref{tab:holm_bonferroni} and confirm that the conclusions are not artifacts of distributional assumptions at small $n$.
241	
242	
243	\section{Window Size Ablation Details}
244	\label{app:window_ablation}
245	
246	\cref{tab:window_full} reports the complete window size ablation across all models and seven window sizes. The main text (\cref{sec:temporal}) presents R1-8B results; here we provide the full data. \cref{fig:window_ablation} visualizes the monotonic improvement on R1-8B: precision rises from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$) while FPR drops from 9.65\% to 4.8\%.
247	
248	\begin{figure}[htbp]
249	\centering
250	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
251	\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}
252	\label{fig:window_ablation}
253	\end{figure}
254	
255	\begin{table}[htbp]
256	\centering
257	\small
258	\caption{Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage ($K{=}1$), and mean detection lead across all models.}
259	\label{tab:window_full}
260	\resizebox{\columnwidth}{!}{%
261	\begin{tabular}{llccccc}
262	\toprule
263	Model & $W$ & Bal.\ Acc. & Precision & FPR$_{\text{step}}$ & Coverage & Lead \\
264	\midrule
265	\multirow{7}{*}{R1-8B}
266	 & 1  & 77.8 & 69.3 & 9.65 & 72.1 & 13.8 \\
267	 & 3  & 79.0 & 72.3 & 8.50 & 69.8 & 12.1 \\
268	 & 5  & 78.1 & 72.6 & 8.09 & 65.1 & 8.3 \\
269	 & 10 & 79.3 & 74.3 & 7.61 & 55.8 & 10.0 \\
270	 & 15 & 80.2 & 77.7 & 6.39 & 51.2 & 7.2 \\
271	 & 20 & 80.7 & 78.6 & 6.12 & 53.5 & 7.4 \\
272	 & 25 & 81.0 & 82.2 & 4.83 & 48.8 & 8.1 \\
273	\midrule
274	\multirow{7}{*}{OT-7B}
275	 & 1  & 68.2 & 42.8 & 12.0 & 53.2 & 16.1 \\
276	 & 3  & \textbf{68.8} & 46.6 & 10.0 & 53.2 & 21.6 \\
277	 & 5  & 68.1 & 46.4 & 9.9 & 53.2 & 21.7 \\
278	 & 10 & 66.5 & 46.9 & 8.6 & 48.9 & 25.0 \\
279	 & 15 & 66.4 & 48.8 & 7.7 & 44.7 & 39.6 \\
280	 & 20 & 66.0 & \textbf{49.4} & \textbf{7.5} & 48.9 & 17.9 \\
281	 & 25 & 65.9 & 48.9 & 8.0 & 51.1 & 28.3 \\
282	\midrule
283	\multirow{7}{*}{R1-32B}
284	 & 1  & 71.8 & 54.9 & 32.03 & 80.0 & 12.9 \\
285	 & 3  & 72.5 & 56.0 & 30.64 & 80.0 & 11.4 \\
286	 & 5  & 73.1 & 57.5 & 28.41 & 75.0 & 11.1 \\
287	 & 10 & 73.7 & 60.9 & 23.40 & 70.0 & 10.8 \\
288	 & 15 & 72.1 & 59.1 & 24.51 & 70.0 & 10.9 \\
289	 & 20 & 69.6 & 56.3 & 26.18 & 65.0 & 9.6 \\
290	 & 25 & 70.3 & 56.6 & 26.46 & 70.0 & 10.7 \\
291	\midrule
292	\multirow{7}{*}{QwQ-32B}
293	 & 1  & 73.0 & 54.4 & 22.76 & 79.0 & 19.7 \\
294	 & 3  & 74.5 & 56.5 & 21.41 & 73.7 & 20.6 \\
295	 & 5  & 76.1 & 57.3 & 21.68 & 73.7 & 20.1 \\
296	 & 10 & 74.7 & 57.1 & 20.73 & 73.7 & 18.4 \\
297	 & 15 & 74.1 & 58.2 & 19.11 & 68.4 & 15.8 \\
298	 & 20 & 75.4 & 60.2 & 17.89 & 63.2 & 15.8 \\
299	 & 25 & 76.2 & 61.8 & 16.94 & 57.9 & 14.9 \\
300	\bottomrule
301	\end{tabular}}%
302	\end{table}
303	
304	Key cross-model patterns emerge from the window ablation:
305	
306	\paragraph{R1-8B} shows a general upward trend in balanced accuracy from 77.8\% ($W{=}1$) to 81.0\% ($W{=}25$), gaining +3.2pp overall with a slight dip at $W{=}5$ (78.1\%). Precision improves sharply (+12.9pp) and step-level FPR halves (9.65\% to 4.83\%). Coverage trades off against quality, dropping from 72.1\% to 48.8\%.
307	
308	\paragraph{OT-7B} exhibits a split temporal pattern at layer 16: balanced accuracy peaks at $W{=}3$ (68.8\%) and declines at larger windows ($-$2.9pp by $W{=}25$), while precision and FPR continue improving. Precision rises from 42.8\% ($W{=}1$) to 49.4\% ($W{=}20$), and FPR drops from 12.0\% to 7.5\% over the same range. The split indicates that larger windows reduce false alarms and sharpen positive predictions even as overall classification accuracy degrades. Lead times are shorter than old layer-0 estimates (16.1--39.6 steps) due to the threshold-based layer selection (\cref{app:ot7b_details}). OT-7B text probes improve monotonically across all metrics (\cref{app:ot7b_details}), so the accuracy saturation is specific to HS probes on this model.
309	
310	\paragraph{R1-32B} exhibits a non-monotonic pattern: balanced accuracy peaks at $W{=}10$ (73.7\%) and then declines, falling below the $W{=}1$ baseline by $W{=}20$ (69.6\%). The optimal window for R1-32B is $W{=}10$, which achieves the lowest FPR (23.40\%) and highest precision (60.9\%). The accuracy degradation at large windows likely reflects overfitting on the smaller dataset ($n{=}100$).
311	
312	\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\%), dips at $W{=}10$--$15$, then recovers to 76.2\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\% to 61.8\% precision; 22.76\% to 16.94\% FPR). QwQ-32B produces substantially longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.
313	
314	\paragraph{Universal trends.} Across all models: (1) larger windows reduce coverage as the smoothed probe fires less frequently; (2) HS FPR generally decreases with window size; (3) lead time is model-dependent. The primary cross-model difference is whether balanced accuracy improves broadly (R1-8B, QwQ-32B), peaks sharply at an intermediate window (R1-32B at $W{=}10$), or peaks very early (OT-7B at $W{=}3$). Each model uses its validation-selected window in the main text.
315	
316	\subsection{Text Probe Window Ablation}
317	\label{app:text_window}
318	
319	\cref{tab:text_window} reports the complete text probe window sweep on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes.
320	
321	\begin{table}[htbp]
322	\centering
323	\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}
324	\label{tab:text_window}
325	\resizebox{\columnwidth}{!}{%
326	\begin{tabular}{lcccc}
327	\toprule
328	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
329	\midrule
330	 1  & 64.7 & 41.6 & 25.8 & 95.4 \\
331	 3  & 66.9 & 44.8 & 23.1 & 90.7 \\
332	 5  & 69.2 & 48.5 & 20.4 & 84.9 \\
333	 10 & 72.1 & 54.3 & 16.7 & 74.4 \\
334	 15 & 74.3 & 58.9 & 14.2 & 67.4 \\
335	 20 & 75.8 & 62.1 & 12.5 & 62.8 \\
336	 25 & 76.7 & 64.8 & 11.8 & 58.1 \\
337	\bottomrule
338	\end{tabular}}
339	\end{table}
340	
341	Text probes show monotonic improvement across all window sizes without the plateau observed in HS probes (which saturate around $W{=}15$). The absolute FPR reduction ($-$14.0pp) is nearly three times the HS reduction ($-$4.8pp), and accuracy gains (+12.0pp vs.\ +3.2pp) are four times larger. This asymmetry supports the interpretation that temporal context is the primary factor in commitment detection: text features, which encode less information per step, benefit proportionally more from observing the multi-step progression.
342	
343	
344	\section{OpenThinker-7B Detailed Results}
345	\label{app:ot7b_details}
346	
347	OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B to produce a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
348	
349	\paragraph{Layer sweep.}
350	
351	\begin{table}[htbp]
352	\centering
353	\small
354	\caption{OT-7B layer sweep. Score = balanced accuracy $\times$ crossing rate. Layer 16 (57\% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.}
355	\label{tab:ot7b_layer_sweep}
356	\setlength{\tabcolsep}{4pt}
357	\resizebox{\columnwidth}{!}{%
358	\begin{tabular}{lcccc}
359	\toprule
360	Layer & Depth & Bal.\ Acc. & Cross.\ Rate & Score \\
361	\midrule
362	0 (embed.) & 0 & 66.7 & 53.2 & 35.5 \\
363	4 & 14 & 66.3 & 40.4 & 26.8 \\
364	8 & 29 & 66.4 & 25.5 & 17.0 \\
365	12 & 43 & 67.5 & 31.9 & 21.6 \\
366	16 & 57 & 68.2 & 31.9 & 21.8 \\
367	20 & 71 & 65.5 & 31.9 & 20.9 \\
368	24 & 86 & 66.9 & 29.8 & 19.9 \\
369	27 & 96 & 63.0 & 31.9 & 20.1 \\
370	\bottomrule
371	\end{tabular}}
372	\end{table}
373	
374	After correction of a layer selection bug, layer 16 (57\% depth) is selected. It achieves the highest balanced accuracy (68.2\%) among transformer layers under the 70/30 split used here; under the canonical 60/20/20 split, BA selects L2 (7\% depth; \cref{tab:ba_layer_results}). Layer 0 (embedding) has a higher crossing rate (53.2\% vs.\ 31.9\%) but lower accuracy.
375	
376	\paragraph{Text probe window ablation.}
377	
378	\begin{table}[htbp]
379	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7964b98f-dc5a-4ead-99fe-73bdaa6345c3",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "11ad4b63-ea6a-4db6-95a6-ee250fb3a236",
  "sourceToolAssistantUUID": "7964b98f-dc5a-4ead-99fe-73bdaa6345c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-22T10:01:59.848Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JVcFHwYfC1FsWHnLuEN9oP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": 375,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11ad4b63-ea6a-4db6-95a6-ee250fb3a236",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHR1Q8PVmAeD4hGBntXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "761192db-d358-4e30-b0fa-bf0795e3e343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCzWZJLZ1Pd5sH7grp9x55",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6241,
      "cache_read_input_tokens": 44546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6241,
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

_source line 41 · 2026-05-22T10:01:59.868Z_

<details><summary>↩ Tool result · `toolu_01JVcFHwYfC1FsWHnLuEN9oP`</summary>

```text
375	
376	\paragraph{Text probe window ablation.}
377	
378	\begin{table}[htbp]
379	\centering
380	\small
381	\caption{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}
382	\label{tab:ot7b_text_window}
383	\resizebox{\columnwidth}{!}{%
384	\begin{tabular}{lcccc}
385	\toprule
386	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
387	\midrule
388	 1  & 58.1 & 24.5 & 34.5 & 63.8 \\
389	 3  & 57.9 & 25.4 & 27.1 & 74.5 \\
390	 5  & 56.9 & 24.7 & 25.5 & 70.2 \\
391	 10 & 58.3 & 27.0 & 22.2 & 70.2 \\
392	 15 & 58.9 & 28.3 & 20.0 & 66.0 \\
393	 20 & 60.9 & 31.6 & 17.6 & 66.0 \\
394	 25 & 61.4 & 32.9 & 16.1 & 66.0 \\
395	\bottomrule
396	\end{tabular}}
397	\end{table}
398	
399	OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), consistent with the R1-8B pattern. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
400	
401	\paragraph{Bootstrap comparison (matched $W{=}3$).} To ensure a fair modality comparison, bootstrap tests use matched $W{=}3$ for both HS and text probes. At $W{=}3$, HS probes achieve 75.3\% trace-level balanced accuracy vs.\ 65.6\% for text (bootstrap $\Delta{=}$+10.7pp, 95\% CI [4.9, 16.3], $p{<}0.001$, survives Holm-Bonferroni). Precision: 55.8\% vs.\ 34.6\% (bootstrap $\Delta{=}$+21.9pp, 95\% CI [14.0, 29.6], $p{<}0.001$, survives Holm-Bonferroni). Pre-CP FPR: 10.0\% vs.\ 27.1\% (bootstrap $\Delta{=}{-}17.1$pp, 95\% CI [$-$22.2, $-$12.2], $p{<}0.001$, survives Holm-Bonferroni). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (+21.9pp); the small discrepancy reflects resampling variance. Using each modality's optimal $W$ (HS at $W{=}3$, text at $W{=}25$) would introduce a confound because text would benefit from 8$\times$ more temporal context.
402	
403	
404	\section{GRU Training Details}
405	\label{app:gru_details}
406	
407	GRU results serve as supplementary evidence under a different training protocol (70/30 split); direct comparison with the main logistic regression pipeline (60/20/20 nested CV) is not intended.
408	
409	\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\% training portion, we hold out 10\% of total traces as a validation set for early stopping (effective 60/10/30 split). The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.
410	
411	\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step to produce a higher-dimensional input to the same GRU architecture.
412	
413	\paragraph{Training procedure.} We train with Adam (learning rate $1 \times 10^{-3}$, default $\beta_1{=}0.9$, $\beta_2{=}0.999$), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.
414	
415	\paragraph{Evaluation.} We report crossing accuracy (the sustained accuracy at which the probe first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean $\pm$ standard deviation.
416	
417	\paragraph{Per-seed results for R1-8B (single-layer GRU).}
418	
419	\begin{table}[htbp]
420	\centering
421	\small
422	\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}
423	\label{tab:gru_seeds}
424	\setlength{\tabcolsep}{4pt}
425	\resizebox{\columnwidth}{!}{%
426	\begin{tabular}{lccc}
427	\toprule
428	Seed & Peak Acc. & Crossing Acc. & Lead (steps) \\
429	\midrule
430	1 & 85.2 & 74.3 & +4.8 \\
431	2 & 83.1 & 71.6 & +4.8 \\
432	3 & 83.4 & 70.4 & +0.9 \\
433	\midrule
434	Mean $\pm$ std & 83.9 $\pm$ 1.1 & 72.1 $\pm$ 2.0 & +3.5 $\pm$ 2.3 \\
435	\bottomrule
436	\end{tabular}}
437	\end{table}
438	
439	The high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe achieves good peak accuracy but crosses the detection threshold late. This variance underscores the sensitivity of early detection to initialization and motivates reporting per-seed results rather than relying on mean values alone.
440	
441	Results in this section use the 60/20/20 protocol consistent with the main text; earlier 70/30 results are retained for completeness but should not be compared directly.
442	
443	\paragraph{Multi-layer GRU and baseline comparison (60/20/20 protocol).}
444	
445	\begin{table}[htbp]
446	\centering
447	\scriptsize
448	\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}
449	\label{tab:gru_multi_seeds}
450	\resizebox{\columnwidth}{!}{%
451	\begin{tabular}{llccccc}
452	\toprule
453	Model & Seed & Acc & Prec & FPR & Cross.\% & Lead \\
454	\midrule
455	GRU-single & 42  & 0.845 & 0.657 & 0.139 & 72.1\% & 3.55 \\
456	GRU-single & 123 & 0.760 & 0.454 & 0.191 & 65.1\% & 7.39 \\
457	GRU-single & 456 & 0.792 & 0.474 & 0.203 & 67.4\% & 8.45 \\
458	\rowcolor{gray!10}
459	GRU-single & \textit{mean} & 0.799$\pm$0.035 & 0.528$\pm$0.091 & 0.178$\pm$0.028 & 68.2$\pm$2.9\% & 6.46$\pm$2.10 \\
460	\midrule
461	GRU-multi  & 42  & 0.824 & 0.616 & 0.164 & 74.4\% & 5.66 \\
462	GRU-multi  & 123 & 0.759 & 0.454 & 0.195 & 65.1\% & 6.43 \\
463	GRU-multi  & 456 & 0.784 & 0.460 & 0.207 & 65.1\% & 8.93 \\
464	\rowcolor{gray!10}
465	GRU-multi  & \textit{mean} & 0.789$\pm$0.027 & 0.510$\pm$0.075 & 0.189$\pm$0.018 & 68.2$\pm$4.4\% & 7.01$\pm$1.40 \\
466	\midrule
467	LR-single  & 42  & 0.841 & 0.693 & 0.097 & 46.5\% & $-$2.00 \\
468	LR-single  & 123 & 0.753 & 0.436 & 0.181 & 53.5\% & 5.26 \\
469	LR-single  & 456 & 0.814 & 0.512 & 0.146 & 41.9\% & 3.94 \\
470	\rowcolor{gray!10}
471	LR-single  & \textit{mean} & 0.803$\pm$0.037 & 0.547$\pm$0.108 & 0.141$\pm$0.035 & 47.3$\pm$4.8\% & 2.40$\pm$3.16 \\
472	\midrule
473	LR-multi   & 42  & 0.827 & 0.679 & 0.092 & 39.5\% & 1.06 \\
474	LR-multi   & 123 & 0.756 & 0.442 & 0.180 & 46.5\% & 7.30 \\
475	LR-multi   & 456 & 0.817 & 0.521 & 0.130 & 34.9\% & 4.00 \\
476	\rowcolor{gray!10}
477	LR-multi   & \textit{mean} & 0.800$\pm$0.032 & 0.547$\pm$0.099 & 0.134$\pm$0.036 & 40.3$\pm$4.8\% & 4.12$\pm$2.55 \\
478	\bottomrule
479	\end{tabular}}%
480	\end{table}
481	
482	Under this protocol, multi-layer GRU achieves the highest mean lead (7.01$\pm$1.40 steps) but at higher FPR than logistic regression baselines (0.189 vs.\ 0.134). The GRU advantage is concentrated in detection timing rather than classification accuracy, consistent with the main text finding that GRUs capture sequential dependencies that improve early detection. Lead time shows high variance across seeds (range 5.66--8.93 for GRU-multi), reinforcing that reported means should be interpreted cautiously.
483	
484	\paragraph{OT-7B multi-layer GRU (layers 13--19, 3 seeds, 60/20/20 split).}
485	OT-7B GRU achieves 74.6$\pm$1.3\% balanced accuracy, 64.5$\pm$7.0\% coverage, +33.6$\pm$4.8 steps lead, and 27.4$\pm$6.1\% pre-CP FPR. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average ${\sim}$80 reasoning steps (vs.\ ${\sim}$30 for R1-8B and 32B models), so absolute lead times are not directly comparable. The FPR-lead tradeoff mirrors R1-8B: GRU FPR (27.4\%) is far above the LR probe at layer 16 (10.0\%), which confirms that GRUs gain lead time at the cost of more false alarms across both 7-8B models.
486	
487	
488	\section{Control Task Methodology}
489	\label{app:control}
490	
491	We follow the selectivity framework of \cite{hewitt2019control} to verify that our probes capture genuine safety-relevant structure rather than surface-level correlations.
492	
493	\paragraph{Procedure.} For each model, we randomly permute the binary labels (pre-CP vs. post-CP) within each trace while preserving the marginal label distribution. We then retrain the probe with identical architecture (L2-regularized logistic regression) and hyperparameters on these shuffled labels. Selectivity is defined as:
494	\begin{equation}
495	    \text{Selectivity} = \text{Acc}_{\text{linguistic}} - \text{Acc}_{\text{control}}
496	\end{equation}
497	where $\text{Acc}_{\text{linguistic}}$ is the probe accuracy on true labels and $\text{Acc}_{\text{control}}$ is the accuracy on permuted labels. A selectivity of zero indicates that the probe exploits only non-linguistic features (e.g., position); higher values confirm that the representation encodes task-relevant information. Absolute selectivity values are task-dependent and not directly comparable across studies~\citep{hewitt2019control}.
498	
499	\paragraph{Results.} We repeat the control experiment 10 times with different random permutations and report the mean control accuracy. Selectivity scores at threshold-based layers (60/20/20 split) are: R1-32B 16.8pp (layer 63), QwQ-32B 16.1pp (layer 63), R1-8B 14.1pp (layer 14), OT-7B 11.1pp (layer 16). All values exceed the 5pp threshold recommended by \cite{hewitt2019control}. R1-32B and QwQ-32B achieve the strongest selectivity ($>$16pp) at threshold-based layers. On QwQ-32B, the position baseline accuracy (0.705) slightly exceeds the HS probe (0.667) at L60, consistent with the main-text finding that QwQ's HS advantage is concentrated in precision and FPR rather than balanced accuracy.
500	
501	\paragraph{Layer provenance note.} R1-8B is unaffected by the layer selection bias because its CR-composite and threshold-based layers coincide at L14. OT-7B exhibits a 16-layer gap (CR-composite L0 vs.\ threshold-based L16; \cref{tab:layer_selection}), but selectivity at L16 (11.1pp) still exceeds the 5pp threshold. QwQ-32B selectivity is 16.1pp at L63, which confirms that safety-specific signal persists at deep layers.
502	
503	\paragraph{Position-only baseline.} As a complementary validation, we train a logistic regression classifier using only the normalized step index ($t / T$ where $T$ is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8\% FPR compared to 8.1\% for the HS probe at matched detection rates. The probe's substantially lower FPR confirms that hidden state features carry information beyond what step position provides.
504	
505	\paragraph{Residualized selectivity.} To confirm that selectivity survives position removal, we recompute control task selectivity on position-regressed features (the same residualized representations used in \cref{app:position_residual}). Residualized selectivity: R1-8B 22.9pp, OT-7B 10.4pp, QwQ-32B 11.3pp (all ${>}5$pp), R1-32B 3.0pp (${<}5$pp, consistent with the position-mediation pattern reported in \cref{sec:hs-text}). Three of four models retain selectivity well above the \citet{hewitt2019control} threshold after position removal; R1-32B's drop confirms that its safety signal is largely positional.
506	
507	
508	\section{Oracle Upper Bound Analysis}
509	\label{sec:oracle}
510	
511	We compute an oracle upper bound for commitment detection by measuring the earliest step at which the ground-truth commitment point (CP) could theoretically be predicted from hidden-state dynamics. The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. The resulting bound provides a theoretical ceiling on early detection performance.
512	
513	\cref{tab:oracle} reports oracle performance across all four models. Oracle analysis confirms the evidence gradient: OT-7B (strong) shows the highest early detection rate (93.6\%) and longest lead time (50 steps), while R1-32B (qualified) achieves only 50\% early detection even with oracle labels, consistent with an inherently weaker commitment signal. On R1-8B, the oracle early detection rate is 76.7\% (33/43 traces detected before CP, with +31 steps mean lead time), compared to +4.5 steps for the best learned probe (GRU). This gap indicates that hidden states at step $t$ encode the model's current safety state but carry limited predictive power about future trajectory evolution. The learned probe captures the contemporaneous safety signal effectively (balanced accuracy 81--84\%) but cannot anticipate the commitment transition far in advance. Closing this gap will likely require causal intervention techniques (e.g., activation patching) rather than improvements to passive monitoring.
514	
515	\begin{table}[htbp]
516	\centering
517	\small
518	\caption{Oracle upper bound analysis. Detection rate: fraction of traces where the oracle finds a linearly separable boundary before or at CP. Early detection rate: fraction detected before CP. Mean lead: average steps before CP at first detection.}
519	\label{tab:oracle}
520	\resizebox{\columnwidth}{!}{%
521	\begin{tabular}{lcccc}
522	\toprule
523	\textbf{Model} & \textbf{Det.\ Rate} & \textbf{Early Det.} & \textbf{Mean Lead} & $n_{\text{test}}$ \\
524	\midrule
525	R1-8B & 100\% & 76.7\% & 31.0 & 43 \\
526	OT-7B & 100\% & 93.6\% & 50.0 & 47 \\
527	R1-32B$^\dagger$ & 95.0\% & 50.0\% & 32.4 & 20 \\
528	QwQ-32B$^\dagger$ & 100\% & 84.2\% & 24.4 & 19 \\
529	\bottomrule
530	\end{tabular}}
531	\end{table}
532	
533	
534	\section{CP Annotation Perturbation}
535	\label{app:cp_perturbation}
536	
537	To assess sensitivity to annotation noise, we shift all ground-truth CP labels by $\delta \in \{-3, \ldots, +3\}$ steps and retrain the HS probe (\cref{tab:cp_perturbation}). Precision degrades smoothly with no cliff effect: within $\pm 2$ steps, BA changes by ${<}2.5$pp for all models (7--8B: ${<}1.0$pp). At the $\pm 3$-step worst case, all models retain precision well above their respective text baselines. These results support the annotation robustness assumption discussed in \cref{sec:limitations}.
538	
539	\begin{table}[htbp]
540	\centering
541	\small
542	\caption{HS probe sensitivity to CP annotation shift ($\delta$ steps). BA is stable across all perturbations; precision degrades gradually without cliff effects.}
543	\label{tab:cp_perturbation}
544	\resizebox{\columnwidth}{!}{%
545	\begin{tabular}{llccc}
546	\toprule
547	\textbf{Model} & $\delta$ & \textbf{Prec} & \textbf{BA} & \textbf{FPR} \\
548	\midrule
549	R1-8B & $-3$ & .652 & .773 & .177 \\
550	 & $0$ & .596 & .784 & .165 \\
551	 & $+3$ & .530 & .771 & .143 \\[2pt]
552	OT-7B & $-3$ & .404 & .714 & .298 \\
553	 & $0$ & .351 & .707 & .286 \\
554	 & $+3$ & .300 & .702 & .276 \\[2pt]
555	QwQ-32B & $-3$ & .661 & .728 & .158 \\
556	 & $0$ & .609 & .690 & .129 \\
557	 & $+3$ & .550 & .676 & .114 \\[2pt]
558	R1-32B & $-3$ & .625 & .698 & .360 \\
559	 & $0$ & .570 & .722 & .281 \\
560	 & $+3$ & .503 & .750 & .236 \\
561	\bottomrule
562	\end{tabular}}
563	\end{table}
564	
565	\subsection{Inter-Annotator Agreement on AdvBench}
566	\label{app:iaa}
567	
568	To assess annotation reliability, two LLM annotators (Qwen3-32B and GPT-4o-mini) independently labeled 388 AdvBench B-class traces for jailbreak status and CP position (\cref{tab:iaa}).
569	
570	\begin{table}[htbp]
571	\centering
572	\small
573	\caption{Inter-annotator agreement on AdvBench B-class traces (388 total). CP position metrics computed on 51 traces where both annotators identified a jailbreak.}
574	\label{tab:iaa}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "761192db-d358-4e30-b0fa-bf0795e3e343",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "69cc9c63-eb47-4d66-8259-1231e581d4b2",
  "sourceToolAssistantUUID": "761192db-d358-4e30-b0fa-bf0795e3e343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-22T10:02:03.377Z_

I now have a comprehensive understanding of the paper. Let me also quickly check for the AdvBench preliminary sweep and ensemble LOOCV scripts that were mentioned as modified in the git status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69cc9c63-eb47-4d66-8259-1231e581d4b2",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHR1psvKEdzDeNECc8dj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f6e1c77-59d7-4684-b80d-d30f25159302",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176jgnDqoCtPsq2S12XzRRZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6188,
      "cache_read_input_tokens": 50787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6188,
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

_source line 43 · 2026-05-22T10:02:05.393Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BM5jzUWsL81R3tBxxh2QtA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": 570,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f6e1c77-59d7-4684-b80d-d30f25159302",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHR1psvKEdzDeNECc8dj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4528db4-b82f-4cf7-b0ba-5730bb4ce094",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176jgnDqoCtPsq2S12XzRRZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6188,
      "cache_read_input_tokens": 50787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6188,
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

_source line 44 · 2026-05-22T10:02:05.400Z_

<details><summary>↩ Tool result · `toolu_01BM5jzUWsL81R3tBxxh2QtA`</summary>

```text
570	\begin{table}[htbp]
571	\centering
572	\small
573	\caption{Inter-annotator agreement on AdvBench B-class traces (388 total). CP position metrics computed on 51 traces where both annotators identified a jailbreak.}
574	\label{tab:iaa}
575	\resizebox{\columnwidth}{!}{%
576	\begin{tabular}{lc}
577	\toprule
578	\textbf{Metric} & \textbf{Value} \\
579	\midrule
580	\textit{Jailbreak classification} \\
581	\quad Cohen's $\kappa$ & 0.606 (moderate) \\
582	\quad Raw agreement & 87.4\% \\
583	\quad GPT-4o-mini JB count & 99 / 388 \\
584	\quad Qwen3-32B JB count & 52 / 388 \\
585	\midrule
586	\textit{CP position (51 shared JB)} \\
587	\quad Exact match & 37\% \\
588	\quad Within 5 steps & 47\% \\
589	\quad Mean abs.\ difference & 8.5 steps \\
590	\bottomrule
591	\end{tabular}}
592	\end{table}
593	
594	LLM annotators achieve only moderate agreement on jailbreak classification ($\kappa{=}0.606$) and low CP position consistency (37\% exact match). GPT-4o-mini is substantially more aggressive in jailbreak identification (99 vs.\ 52), suggesting systematic annotator bias. The low CP position agreement (mean absolute difference of 8.5 steps) underscores a key design choice: our primary analysis uses the human-validated HarmThoughts annotations~\citep{harmthoughts}, not LLM-generated labels. This AdvBench IAA study serves as a \emph{negative control}: it demonstrates that LLM-only annotation is insufficient for reliable CP localization, motivating future investment in multi-annotator human CP labeling with formal IAA evaluation.
595	
596	\section{BOCPD/CUSUM Configuration Sweep}
597	\label{app:bocpd_config}
598	
599	We sweep hyperparameters for both Bayesian Online Change-Point Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe score sequences.
600	
601	\paragraph{BOCPD configurations.} BOCPD models the sequence of probe scores as piecewise-constant segments with Gaussian observation noise. The hazard rate $\lambda$ controls the prior probability of a change-point at each step ($P(\text{change}) = 1/\lambda$).
602	
603	\paragraph{CUSUM configurations.} CUSUM accumulates evidence for a positive mean shift. The drift parameter $\delta$ sets the minimum shift size to detect, and the threshold $h$ controls the detection boundary.
604	
605	\begin{table}[htbp]
606	\centering
607	\small
608	\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}
609	\label{tab:cpd_sweep}
610	\setlength{\tabcolsep}{4pt}
611	\resizebox{\columnwidth}{!}{%
612	\begin{tabular}{llcc}
613	\toprule
614	Method & Configuration & Det.\ Rate & Lead \\
615	\midrule
616	\multirow{5}{*}{BOCPD}
617	 & $\lambda = 5$   & 97 & +2.1 \\
618	 & $\lambda = 10$  & 93 & +3.5 \\
619	 & $\lambda = 20$  & 87 & +4.2 \\
620	 & $\lambda = 50$  & 72 & +5.8 \\
621	 & $\lambda = 100$ & 67.4 & +1.03 \\
622	\midrule
623	\multirow{10}{*}{CUSUM}
624	 & $\delta{=}0.3$, $h{=}3$ & 65.1 & +0.89 \\
625	 & $\delta{=}0.5$, $h{=}3$ & 89 & +1.4 \\
626	 & $\delta{=}0.5$, $h{=}5$ & 76 & +2.3 \\
627	 & $\delta{=}0.5$, $h{=}8$ & 61 & +3.1 \\
628	 & $\delta{=}1.0$, $h{=}3$ & 82 & +1.1 \\
629	 & $\delta{=}1.0$, $h{=}5$ & 68 & +1.9 \\
630	 & $\delta{=}1.0$, $h{=}8$ & 52 & +2.7 \\
631	 & $\delta{=}2.0$, $h{=}3$ & 71 & +0.8 \\
632	 & $\delta{=}2.0$, $h{=}5$ & 54 & +1.5 \\
633	 & $\delta{=}2.0$, $h{=}8$ & 38 & +2.1 \\
634	\midrule
635	Simple threshold & FCP baseline & 65.1 & +4.89 \\
636	\bottomrule
637	\end{tabular}}
638	\end{table}
639	
640	The best BOCPD configuration ($\lambda{=}10$) achieves 93.0\% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1\% detection with superior lead (+4.89 steps). All CUSUM configurations underperform the simple threshold on lead time.
641	
642	These results reveal a coverage-timing tradeoff. BOCPD ($\lambda{=}10$) achieves 28pp higher detection rate than simple thresholding (93.0\% vs.\ 65.1\%), but with lower lead (+3.45 vs.\ +4.89 steps). The transition toward unsafe reasoning is gradual rather than abrupt, so change-point methods cannot exploit discontinuities for early warning. When missed detections are costly, BOCPD's coverage advantage justifies its use despite the timing penalty. When early intervention is the priority, simple thresholding provides better lead time.
643	
644	\paragraph{Other models.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). The failure modes differ by model: for R1-32B and QwQ-32B, probe scores transition gradually, so the hazard function never accumulates sufficient evidence; for OT-7B at $W{=}3$, transitions are too abrupt (0$\to$1 in 1--2 steps) for the Gaussian observation model to capture. R1-8B falls between these extremes, with transitions sharp enough to trigger the hazard function but smooth enough for the Gaussian model to track.
645	
646	
647	\section{Detection Threshold ($K$) Ablation}
648	\label{app:k_ablation}
649	
650	The consecutive-crossings threshold $K$ controls the trade-off between detection coverage and false positive rate. We evaluate $K \in \{1, 3, 5, 7, 10\}$ at $W{=}1$ on all models using HS probes at threshold-based layers (\cref{tab:k_ablation}).
651	
652	\begin{table}[htbp]
653	\centering
654	\small
655	\caption{Detection threshold ablation ($W{=}1$, HS probes at threshold-based layers). Coverage: fraction of jailbreak traces with $\geq K$ consecutive crossings. Safe FPR: fraction of safe traces with $\geq K$ consecutive false alarms.}
656	\label{tab:k_ablation}
657	\setlength{\tabcolsep}{3pt}
658	\resizebox{\columnwidth}{!}{%
659	\begin{tabular}{lccccccccc}
660	\toprule
661	& \multicolumn{4}{c}{\textbf{Coverage}} & & \multicolumn{4}{c}{\textbf{Safe FPR}} \\
662	\cmidrule{2-5} \cmidrule{7-10}
663	$K$ & R1-8B & OT-7B & QwQ & R1-32B & & R1-8B & OT-7B & QwQ & R1-32B \\
664	\midrule
665	1  & 1.00 & 1.00 & 1.00 & 1.00 & & 1.00 & 0.92 & 1.00 & 0.99 \\
666	3  & 0.74 & 0.79 & 0.95 & 0.90 & & 0.81 & 0.41 & 0.78 & 0.78 \\
667	5  & 0.47 & 0.51 & 0.79 & 0.65 & & 0.63 & 0.19 & 0.65 & 0.47 \\
668	7  & 0.35 & 0.30 & 0.58 & 0.45 & & 0.39 & 0.16 & 0.35 & 0.31 \\
669	10 & 0.14 & 0.21 & 0.32 & 0.35 & & 0.22 & 0.08 & 0.25 & 0.17 \\
670	\bottomrule
671	\end{tabular}}
672	\end{table}
673	
674	$K{=}1$ yields perfect coverage but near-perfect safe FPR (0.92--1.00), offering no discrimination. $K{=}5$ is empirically selected as a middle-ground tradeoff: average coverage 0.60 with average safe FPR 0.48 across models. OT-7B benefits most from increasing $K$, reaching 0.19 safe FPR at $K{=}5$ (vs.\ 0.92 at $K{=}1$) while retaining 51\% coverage. Higher $K$ values ($\geq$7) reduce safe FPR further but at steep coverage cost. $K{=}5$ vs.\ $K{=}7$ is the key decision: $K{=}7$ reduces mean safe FPR from 0.48 to 0.30 but drops mean coverage from 0.60 to 0.42.
675	
676	$K{=}5$ was selected on the R1-8B validation set and held fixed across all models; main-text results use this value without per-model optimization. The $K \times W$ interaction is not fully explored: this ablation uses $W{=}1$ to isolate $K$'s effect, and the joint $K \times W$ surface remains a limitation. At optimal $W$, coverage at $K{=}5$ improves (e.g., R1-8B: 0.47 at $W{=}1$ vs.\ 0.60 at $W{=}15$).
677	
678	\subsection{Deployment Operating Points}
679	\label{app:deployment_operating_points}
680	
681	The $K$ ablation above can be recast as a deployment operating characteristic. At $K{=}5$ (used throughout the main text), average coverage is 60\% with 48\% safe FPR. Raising $K$ yields practically useful operating points: at $K{=}10$, OT-7B achieves 21\% coverage with only 8\% false positive rate, meaning fewer than 1 in 12 flagged traces is a false alarm. R1-32B at $K{=}10$ retains 35\% coverage at 17\% FPR. These conservative operating points are viable for high-stakes deployment where missed detections are preferable to frequent false alarms: a secondary review system could inspect only flagged traces, reducing human oversight burden by 79--86\% while maintaining non-trivial detection rates. However, at $K{=}10$ approximately 65--86\% of attacks are missed, which may be unacceptable in some threat models. The $K{=}7$ setting offers a middle ground (30--58\% coverage, 16--39\% FPR). The choice of operating point is deployment-specific.
682	
683	
684	\section{Decision Threshold Sensitivity}
685	\label{app:threshold_sensitivity}
686	
687	We evaluate whether the HS advantage depends on the logistic regression decision threshold by sweeping $\tau \in \{0.3, 0.4, 0.5, 0.6, 0.7\}$ for both 32B models at their threshold-based layers. Results below were conducted at L60 under the 70/30 protocol; main-text results use L63 under 60/20/20. QwQ-32B (L60, $W{=}3$) HS balanced accuracy varies by only 0.53pp across all thresholds, with $\Delta$(HS$-$Text) stable at +8.5 to +9.3pp. \cref{tab:threshold_r132b} reports R1-32B results.
688	
689	\begin{table}[htbp]
690	\centering
691	\small
692	\caption{R1-32B threshold sensitivity (L63, $W{=}1$). HS BA varies by 1.1pp (0.741--0.752); the HS advantage is consistent across all thresholds.}
693	\label{tab:threshold_r132b}
694	\resizebox{\columnwidth}{!}{%
695	\begin{tabular}{ccccccc}
696	\toprule
697	$\tau$ & HS BA & $\Delta$BA & HS Prec & $\Delta$Prec & HS FPR & $\Delta$FPR \\
698	\midrule
699	0.3 & 0.752 & +0.126 & 0.583 & +0.126 & 0.295 & $-$0.106 \\
700	0.4 & 0.746 & +0.116 & 0.586 & +0.120 & 0.281 & $-$0.092 \\
701	\textbf{0.5} & \textbf{0.742} & \textbf{+0.109} & \textbf{0.588} & \textbf{+0.113} & \textbf{0.273} & $\mathbf{-}$\textbf{0.078} \\
702	0.6 & 0.741 & +0.112 & 0.599 & +0.119 & 0.254 & $-$0.072 \\
703	0.7 & 0.743 & +0.126 & 0.617 & +0.143 & 0.228 & $-$0.084 \\
704	\bottomrule
705	\end{tabular}}
706	\end{table}
707	
708	R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\Delta$BA $= +0.109$ to $+0.126$, $\Delta$Prec $= +0.113$ to $+0.143$, $\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, so the HS advantage is not an artifact of the default $\tau{=}0.5$.
709	
710	
711	\section{M002 Bug Disclosure}
712	\label{app:bug}
713	
714	We disclose a bug discovered during development that affected intermediate results for QwQ-32B.
715	
716	\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive and produced a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).
717	
718	\paragraph{Discovery and correction.} The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), the QwQ-32B and R1-32B modality comparisons at the originally selected layers (L2 and L10, chosen by the CR-composite metric) showed no significant HS advantage: QwQ-32B accuracy $p{=}0.828$, precision $p{=}0.346$; R1-32B precision $p{=}0.050$ but no tests surviving Holm-Bonferroni. The subsequent discovery that these layer selections were themselves artifacts of metric bias (\cref{sec:layer-results}) led to the threshold-based layer analysis reported in the main text, where the HS advantage follows an evidence gradient at threshold-based deep layers: cross-validated at 7--8B, significant but suggestive of position-competitiveness at QwQ-32B$^\dagger$, and exploratory at R1-32B$^\dagger$ (\cref{tab:hs_vs_text}).
719	
720	\paragraph{Impact on reported results.} All numbers reported in this paper use the corrected text embedding pipeline. The bug affected only QwQ-32B text probe features. The correction, combined with the separate layer selection fix (\cref{sec:layer-results}), means that early-stage intermediate results (non-significant 32B modality comparisons) reflected two compounding errors: incorrect text features and CR-composite layer selection. Both are fully resolved in the final analysis.
721	
722	\paragraph{Commitment to transparency.} We report this bug to maintain scientific integrity. Code and data will be released upon publication.
723	
724	\section{Adaptive Two-Stage Detection}
725	\label{app:two_stage}
726	
727	We explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window ($W_{\text{screen}}$) to flag candidate unsafe segments, followed by a longer confirmation window ($W_{\text{confirm}}$) applied only to flagged segments. A trace is classified as unsafe if at least $k$ steps exceed the threshold during the confirmation stage.
728	
729	We merge the validation and test partitions ($n{=}55$ total: 39 jailbreak, 16 benign) for two-stage evaluation because the screening and confirmation thresholds are not tuned on held-out data. We evaluated all combinations of $W_{\text{screen}} \in \{1, 3, 5\}$, $W_{\text{confirm}} \in \{10, 15, 20, 25\}$, and $k \in \{1, 3, 5\}$ on these R1-8B traces. \cref{fig:pareto_two_stage} shows the precision-coverage Pareto front for both methods. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) achieves 72.2\% precision at 76.9\% coverage, compared to 70.9\% precision at 76.9\% coverage for single-stage $W{=}15$. This +1.3pp precision gain at matched coverage represents a Pareto improvement, but the magnitude is marginal. At higher confirmation thresholds ($k{=}3$, $k{=}5$), two-stage detection trades coverage for small precision gains (up to 73.5\% precision at 38.5\% coverage with $k{=}5$), but these operating points are impractical due to excessive missed detections.
730	
731	\begin{figure}[htbp]
732	\centering
733	\includegraphics[width=0.85\columnwidth]{figures/pareto_two_stage.pdf}
734	\caption{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss.}
735	\label{fig:pareto_two_stage}
736	\end{figure}
737	
738	The marginal improvement suggests that fixed-window smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach adds configuration complexity (three hyperparameters vs. one) without proportional performance gain.
739	
740	
741	\section{Temporal Ablation Details}
742	\label{app:temporal_details}
743	
744	\begin{figure}[t]
745	\centering
746	\includegraphics[width=\columnwidth]{figures/fig_trajectory.pdf}
747	\caption{CP-aligned probe score trajectories. Each panel averages all test traces for one model, with step 0 at the true commitment point. HS probes (blue, solid) show a sharper score increase at CP than text probes (orange, dashed), with OT-7B showing the strongest separation and R1-32B the weakest, consistent with the evidence gradient. Shaded bands: $\pm$1 std. Points with $<$5 traces are omitted.}
748	\label{fig:trajectory}
749	\end{figure}
750	
751	Full per-model temporal ablations are reported in \cref{tab:window_full} (\cref{app:window_ablation}). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$) with FPR halving (9.65\% to 4.83\%); (2) OT-7B exhibits a split pattern where balanced accuracy peaks at $W{=}3$ while precision and FPR continue improving at larger windows; (3) R1-32B peaks at $W{=}10$ then degrades, likely reflecting overfitting on the small dataset ($n{=}100$); (4) QwQ-32B shows broadly increasing trends with local non-monotonicity. Text probe window ablations (\cref{app:text_window}) show monotonic improvement across all window sizes for both models tested, with larger marginal gains than HS probes (+12.0pp accuracy vs.\ +3.2pp for R1-8B). The asymmetry supports the interpretation that text features benefit proportionally more from temporal context because they encode less information per step.
752	
753	\section{Negative Results Details}
754	\label{app:negative_details}
755	
756	\begin{table}[htbp]
757	\centering
758	\small
759	\resizebox{\columnwidth}{!}{%
760	\begin{tabular}{p{1.4cm}p{2.5cm}p{2.0cm}p{1.6cm}}
761	\toprule
762	\textbf{Method} & \textbf{Result} & \textbf{Limitation} & \textbf{Failure Cat.} \\
763	\midrule
764	BOCPD & 0\% det.\ on 3/4 models & Commitment gradual & Graduality \\
765	CUSUM & $<$ threshold, all models & Same as BOCPD & Graduality \\
766	Mahalanobis & $\Delta d \approx 0$ & Signal in minor PCs & Var.\ subspace \\
767	RepE & QwQ 0.756; R1-32B 0.559$^a$ & Model-dependent & Model-spec. \\
768	MLP & 3/4 worse than LR & Overfitting & Capacity \\
769	CCS & No gain over supervised$^b$ & Alignment mismatch & Obj.\ mismatch \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4528db4-b82f-4cf7-b0ba-5730bb4ce094",
  "isSidechain": true,
  "promptId": "717e9bec-aad3-4314-b6e4-0c04154da767",
  "agentId": "af864ac05d0b14dfa",
  "type": "user",
  "uuid": "9ed4cdf1-5c78-450d-9221-ed8f3482b82a",
  "sourceToolAssistantUUID": "b4528db4-b82f-4cf7-b0ba-5730bb4ce094",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-22T10:03:29.016Z_

I now have a thorough understanding of the paper. Let me note an important discrepancy: the task description frames this as a paper about "Cross-Dataset Validation" extending probing to AdvBench, but the actual paper I read is primarily about **layer selection sensitivity** in hidden-state safety probes on HarmThoughts (with AdvBench appearing only in an appendix as a geometric validation). The actual paper title is "Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models." Let me produce my review based on the actual paper content.

---

## Review: "Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models"

**Reviewer 2 (R2) -- Focus: Novelty and Related Work**

---

### 1. Summary

This paper investigates how the choice of layer selection metric in hidden-state (HS) safety probing can qualitatively reverse conclusions about whether HS probes outperform text-based probes for detecting safety commitment points in reasoning LLMs. Across four models (2 at 7-8B, 2 at 32B; 3 Qwen, 1 Llama), the authors show that a crossing-rate composite metric systematically selects shallow layers due to cosine compression, where HS advantages vanish, while threshold-based metrics select deep layers where HS advantages of +15-22pp precision are observed. The HS advantage is further shown to be conditional on text encoder quality (diminishing from 4/4 HB at 384d to 1/4 at 1024d) and partially overlapping with temporal position. Seven alternative detection methods (BOCPD, Mahalanobis, RepE, etc.) all fail to match supervised probing.

### 2. Strengths

- **Well-identified methodological contribution.** The demonstration that layer selection metric choice alone can reverse a study's central conclusion (QwQ-32B: p=0.83 vs. p<0.005, Sec. 4.2, Table 2) is a genuinely important finding for the probing methodology community. This is not a minor quantitative shift but a qualitative reversal, which is well-documented with concrete numbers.

- **Thorough experimental protocol with appropriate statistical controls.** The paper employs nested 5-fold CV for 7-8B models, BCa bootstrap with Holm-Bonferroni correction for 12 tests, exact permutation tests for small-sample 32B models, random-label controls, control task selectivity (Appendix H), and CP annotation perturbation analysis (Appendix K). The three-tier evidence gradient (cross-validated / significant / exploratory) is an honest and commendable framing.

- **Comprehensive negative results (Sec. 4.5, Table in Appendix O).** Documenting the failure of seven alternative methods (BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, cross-model transfer) with clear failure categorizations (graduality, variance subspace, model-specificity, capacity, objective mismatch) provides genuine value for researchers in this area.

- **Transparent treatment of boundary conditions.** The paper is unusually candid about limitations: encoder-quality dependence (384d to 1024d gradient in Table 3), position mediation (9-20pp BA absorbed), QwQ-32B's negative lead time, R1-32B's 25% coverage, false alarm rates of 11-50%, and the bug disclosure in Appendix L. This level of transparency is commendable.

- **Mechanistic explanation for the bias.** The cosine compression analysis (Appendix C, Table in Appendix C) provides an interpretable geometric account of why crossing-rate metrics systematically prefer shallow layers (1.4-2.7x smaller inter-step distances), and the random-label decomposition (Appendix B) cleanly separates the geometric artifact (label-independent for Qwen) from genuine safety signal (label-dependent for threshold-based metrics).

- **Practical mitigation hierarchy.** The three-level defense (report dual metrics / multi-metric audit / ensemble) in Section 5 provides actionable guidance, though the ensemble requires cross-validated confirmation as the authors note.

### 3. Weaknesses

- **Limited novelty beyond a careful ablation study.** The core contribution is showing that a known methodological issue in probing (layer selection as a researcher degree of freedom, well-documented in Belinkov 2022, Hewitt & Liang 2019, and the broader probing literature) has severe consequences in a specific application domain (safety probing). While the severity of the reversal is surprising, the underlying insight -- that different metrics select different layers and this matters -- is established knowledge. The paper does not propose new probing methods, new representations, new detection algorithms, or new theoretical frameworks. The three-level mitigation (Sec. 5) is practical advice, not a methodological contribution. For EMNLP 2026 main conference (top ~21%), the novelty bar requires more than a careful demonstration that a known issue applies to a new domain.

- **Narrow scope: single dataset with limited architectural diversity.** All CP-dependent results rely on HarmThoughts, a single dataset with only 632 traces. Three of four models share the Qwen architecture (OT-7B, QwQ-32B, R1-32B); only R1-8B (Llama) provides cross-architecture evidence. The random-label analysis reveals the geometric crossing-rate bias is Qwen-specific (Appendix B), raising questions about how much of the paper's findings are Qwen artifacts versus general properties. AdvBench appears only in Appendix C as a geometric validation (cosine compression ratio) and Appendix D as a boundary condition analysis, not as a full replication of the main experiments.

- **Related work is dense but superficial in critical areas.** While the Related Work section cites extensively (~60 references across four paragraphs), it does not engage deeply with the most relevant prior work. Specifically: (a) Chan et al. (cited as concurrent, showing final-layer probes predict alignment with strong F1) are dismissed in one sentence for using "single-layer, single-metric evaluation" without discussing whether their findings are compatible or contradictory; (b) The probing methodology paragraph acknowledges that non-uniform layer-wise information distribution is "well established" but does not explain what is fundamentally new beyond applying this to safety; (c) No comparison with Boxo et al. (2025) who show probes can rely on textual evidence -- mentioned only in passing. The Related Work needs a clearer delineation of what existing work already establishes versus what this paper adds.

- **The HS advantage is heavily conditioned, undermining the practical significance.** The paper's own analysis shows the HS advantage depends on: (1) layer selection metric, (2) text encoder quality (1/4 HB at 1024d), (3) temporal position (partially overlapping), (4) model architecture (Qwen-specific geometry), and (5) sample size (32B results exploratory). After accounting for all these conditions, the remaining unconditional finding is primarily the layer selection bias itself -- which, as noted above, extends rather than discovers the principle. The claim of "+15 to +22pp precision advantage" in the abstract is technically correct but misleading without the encoder-quality qualifier.

- **Statistical power concerns at 32B scale are acknowledged but unresolved.** With n=19-20 test traces and MDEs of 8.6-9.5pp, the 32B analyses are severely underpowered. R1-32B achieves significance only at W=1 with 25% coverage. QwQ-32B's position baseline achieves higher BA than the HS probe (0.832 vs. 0.796, Sec. 4.3). These results are honestly marked exploratory, but they constitute half the model coverage and are prominently featured in tables and discussion. A reader might question whether the paper should have been scoped to only the 7-8B models where conclusions are robust.

- **No causal evidence for the mechanism.** The paper provides correlational evidence (cosine compression -> crossing rate inflation -> shallow layer selection) but acknowledges that "causal intervention (e.g., DAS, activation patching) is needed" (Limitations). Without causal validation, the cosine compression explanation, while plausible, remains a hypothesis. The ensemble's success (Sec. 4.2) could have alternative explanations.

### 4. Questions for Authors

1. **Architectural generality.** Given that the crossing-rate geometric bias is Qwen-specific (Appendix B), how confident are you that the layer selection sensitivity finding generalizes to other architecture families (e.g., Mixtral, Gemma, command-R)? Would you expect the same magnitude of reversal on non-Qwen models?

2. **Encoder quality gradient.** The HS advantage drops from 4/4 HB at 384d to 1/4 at 1024d (Table 3). Have you considered whether the "HS advantage" is primarily a reflection of the text baseline being weak (384d MiniLM is a distilled model from 2020), rather than HS probes being genuinely superior? What would you expect with a 2025-era encoder like GTE-Qwen2-7B?

3. **Cross-dataset replication.** The abstract and introduction frame this as addressing "generality across datasets," but AdvBench appears only in the appendix for geometric validation, not for the full probing pipeline. Was there a specific reason the full HS-vs-text comparison was not run on AdvBench? The 90.4% CP=0 finding (Appendix D) suggests AdvBench may be structurally unsuitable, but this seems like a critical limitation of the cross-dataset claim.

4. **Practical relevance.** With false alarm rates of 11-50% and the HS advantage disappearing against stronger encoders, what is the practical deployment scenario where one would prefer HS probing over a modern text encoder? The paper positions itself as "retrospective classification" (Sec. 1), but the Discussion (Sec. 5) offers deployment guidance -- can you clarify the intended use case?

5. **Ensemble validation.** The ensemble result (all four models p <= 0.002, Sec. 4.2) uses the same split for layer selection and evaluation. Have you conducted any leave-one-out or cross-validated analysis of the ensemble to estimate the degree of optimism in this result?

### 5. Minor Issues

- The paper title in the LaTeX source ("Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models") differs from what appears in the abstract framing. The title is more accurate than the abstract's emphasis on "cross-dataset validation."
- 14 tables and 0 in-text figures (main body): the paper is extremely table-heavy. A summary visualization (e.g., a forest plot of effect sizes across conditions) in the main text would improve readability. The forest plot exists (Fig. 3, referenced in Sec. 4.2) but appears only as a reference -- it is unclear whether it is in the main text or appendix.
- Table 3 (HS vs. text): the "---" entries for BA and FPR under 1024d comparisons are explained in the caption but still create visual confusion; consider a footnote row or separate sub-table.
- The Limitations section begins with `\newpage`, which seems intentional for page formatting but may be fragile across compilation environments.
- Some appendix sections are very long (the full appendix exceeds the main text by a significant margin). While thoroughness is valued, the sheer volume may discourage reviewer engagement with the supplementary material.

### 6. Scores

| Dimension | Score |
|-----------|-------|
| **Soundness** | 4 |
| **Excitement** | 2 |
| **Reproducibility** | 4 |
| **Overall Assessment** | 2.5 |
| **Confidence** | 4 |

**Justification for Overall Assessment (2.5 -- Borderline Findings):**

The paper is methodologically rigorous and transparent, with thorough statistical controls and honest reporting of limitations. However, the central contribution -- that layer selection metric matters in probing -- extends a well-known principle to a specific domain rather than introducing fundamentally new insight. The HS advantage, once properly conditioned on encoder quality and position, is modest and may not generalize beyond the specific (mostly Qwen) setup studied. The scope is narrow (one dataset, one architecture family dominating), and the practical implications are unclear given the high false alarm rates and encoder-dependence. For a venue with ~21% acceptance rate, I expect papers to introduce new methods, frameworks, or substantially surprising empirical findings; this paper primarily provides a well-executed cautionary analysis. It would be a reasonable Findings paper, where careful empirical methodology work is valued, but falls below the excitement threshold for the main conference. The 32B results, while honestly marked exploratory, do not strengthen the contribution given their statistical limitations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ed4cdf1-5c78-450d-9221-ed8f3482b82a",
  "isSidechain": true,
  "agentId": "af864ac05d0b14dfa",
  "requestId": "req_011CbHR2Fbi2vM1thnf1EvtT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6dc26c57-7c18-4725-9250-3ef9f29572a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "b285e967-6524-44bc-8385-19eed9806998",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GbBgRMuATH4SKjTQX9xj8J",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6434,
      "cache_read_input_tokens": 56975,
      "output_tokens": 3032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6434
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3032,
          "cache_read_input_tokens": 56975,
          "cache_creation_input_tokens": 6434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6434,
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
