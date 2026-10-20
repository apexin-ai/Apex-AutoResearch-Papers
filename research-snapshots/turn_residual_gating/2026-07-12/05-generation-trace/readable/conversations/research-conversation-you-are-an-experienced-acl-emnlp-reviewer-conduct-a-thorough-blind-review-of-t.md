# Research conversation: You are an experienced ACL/EMNLP reviewer. Conduct a thorough, blind review of the following paper for EMNLP 2026 (via A

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 2
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a2de08e360b959d80.jsonl`
- **Structured JSON:** [`650eececc03e8d9e4c51.json`](../../sessions/65/650eececc03e8d9e4c51.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-24T09:14:30.312Z_

You are an experienced ACL/EMNLP reviewer. Conduct a thorough, blind review of the following paper for EMNLP 2026 (via ARR).

## Venue Scoring Scale (ARR Overall Assessment, 0.5 increments)
- 5 = Consider for Award (top 2.5%)
- 4 = Accept to main conference
- 3 = Accept to Findings
- 2 = Needs major revision, resubmit
- 1 = Do not resubmit

Acceptance rate: ACL/EMNLP Main ~21%. Calibrate strictly.

Scoring dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5).

## Paper Summary

**Title:** "Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study"

**Main Claims:** The paper implements ThreadGate, a per-layer gating module trained with a Goal Accessibility Ratio (GAR) auxiliary loss alongside NTP. ThreadGate optimizes GAR under teacher-forcing (TF GAR=0.50) but collapses under autoregressive generation (AR GAR=0.064 on Qwen-2.5-7B, 0.018 on Llama-3.1-8B), revealing an 8–27× training–inference gap. Through PCGrad ablation, λ sensitivity analysis, and cross-model replication, the paper identifies three failure modes: (NF1) reverse turn conditioning from NTP gradient dominance, (NF2) structural distribution shift independent of loss design, (NF3) insufficient gate intervention strength (2–7%). Attempted scheduled sampling mitigation succeeds partially on Qwen (AR GAR=0.39±0.04, 3-seed) but fails on Llama (AR GAR=0.04, gap 11.75×). The paper frames itself as a diagnostic/negative-result study.

**Contributions claimed:**
1. Failure mode taxonomy (NF1–NF3) for auxiliary attention losses under exposure bias
2. First empirical elimination of gradient competition as a causal factor (PCGrad)
3. Cross-model validation on Qwen-2.5-7B (MHA) and Llama-3.1-8B (GQA)
4. Convergent evidence across two intervention designs × two models

## Detailed Paper Content

**Abstract (p1):** Multi-turn dialogue models lose attention to user goals. Prior work shows goal information persists in residual streams (probe AUC=0.98). ThreadGate implements learnable per-layer gating trained with GAR auxiliary loss. TF GAR=0.50 but AR GAR collapses. Three failure modes identified. SS partially works on Qwen but fails on Llama. Negative results establish concrete failure modes.

**Introduction (p1-2):** Motivates from Dongre et al. (2026) showing 27-48% GAR decline across 12 models over 50 turns. Hypothesis: if goal info persists in residual stream but attention fails, a learnable gate on residual connection should recover goal accessibility. ThreadGate raises GAR from 0.02 to 0.50 under TF, but collapses to 0.064 (Qwen) and 0.018 (Llama) under AR. Three failure modes: NF1 (reverse turn conditioning), NF2 (structural distribution shift, 8-27× gap), NF3 (insufficient intervention strength, 2-7%). Convergent evidence with Dongre's independent failure of goal re-injection. Four contributions listed.

**Related Work (p2-3):** Covers multi-turn dialogue degradation, residual gating/adaptive depth, attention steering/intervention, exposure bias in sequence models, gradient conflicts in multi-task learning. Positions the work as diagnosing *why* attention-based auxiliary losses fail rather than proposing new interventions.

**Background (p3):** Defines GAR_ours (last-token attention to goals) and GAR_Dongre (all response tokens). Explains residual stream persistence (Dongre probe AUC=0.98) motivating architectural interventions.

**Method (p3-4):**
- ThreadGate: x_{l+1} = x_l + g_l · f_l(x_l), where g_l is a 2-layer MLP with sigmoid, parameterized by hidden state projection and turn-position embeddings.
- UniformGate: same but constant turn embeddings (content-dependent, turn-agnostic).
- LoRA-only: g=1.0 fixed, retains GAR auxiliary loss but no gating.
- Training objective: L = L_NTP + λ_GAR · L_GAR + λ_div · L_div, with λ_GAR=1.0, λ_div=0.1 (v7 config).
- Training: LoRA (r=16, α=32) on UltraChat, 3 epochs, batch size 4, lr 2e-4.

**Experiments (p4-7):**
- §5.1 Evaluation: TF (gold context) vs AR (model-generated context, β-steering). β=0 is default AR (gates disabled).
- §5.2 Main result (Table 1): Qwen TF 0.501 → AR 0.064 (7.8× gap); Llama TF 0.484 → AR 0.018 (27× gap). Base models show no meaningful gap.
- §5.3 Four-way ablation (Table 2): N=200 TF eval. TG/UG/LO all achieve ~0.50 TF GAR with identical PPL. All CIs contain zero. Gating provides zero increment over LoRA-only.
- §5.4 PCGrad (Tables 3-4): On Qwen, 67-79% layers show negative cos_sim (mild conflict), PCGrad eliminates it but no change in outcomes (v9≈v7). On Llama, cos_sim≈+0.005 (near-orthogonal, not conflicting), neg layers 53.1% near random. PCGrad causal exclusion argument.
- §5.5 λ sensitivity (Table 5): λ=0.1 (gates frozen, ≈LoRA-only), λ=10.0 (PPL degrades 36.7%, training unstable, AR gap 28.9×). Gap independent of λ.
- §5.6 Cross-model replication on Llama: Same failure pattern with amplified severity (27×).

**Analysis (p6-7):**
- §6.1 Failure mode taxonomy: NF1 (27/28 layers show reverse turn conditioning), NF2 (gap persists across all variants/architectures/λ), NF3 (gates 0.93-0.98, only 2-7% attenuation).
- §6.2 Attention KL divergence (Tables 6-7): Mean KL=0.054 for TG vs 0.043 base. GAR-relevant heads show 1.5× higher KL. But gate-KL correlation weak (r=0.11, p=0.18). Small absolute KL suggests compounding mechanisms beyond per-position divergence.
- §6.3 Metric specificity (Table 8): Alternative GAR definitions. Improvement concentrated on last-token (our definition). All-token shows only marginal (2.8×), first-token and goal-only show no improvement. Position-specific overfitting concern.

**Discussion (p8-10):**
- §7.1 Scheduled Sampling: Qwen partial success — 3-seed AR GAR β=0 = 0.390±0.036 (CV=9.2%), gap 1.28×. 4th seed (s789) = 0.300, 4-seed CV=14.7%. Llama SS: complete failure, AR GAR=0.04, gap 11.75×. At β≥3, SS actually underperforms TG without SS. SS is model-specific.
- §7.2 Scalability: SS decays after 10 turns (47.6% at 15 turns, 71.4% at 20 turns). TG converges to baseline by 15 turns.
- §7.3 Convergent evidence: 5/6 intervention×model combinations fail. Only Qwen SS partially succeeds but is seed-sensitive, model-specific, length-limited.
- §7.4 Future directions: inference-time intervention, data-dependent SS schedules, decoupled goal processing, stronger intervention mechanisms.

**Conclusion (p10):** Reiterates failure mode taxonomy, PCGrad causal exclusion, SS model-specificity. "Lightweight training-time interventions face fundamental barriers from exposure bias."

**Limitations (p11):** Three limitations: (1) Only tests lightweight residual gating, not fundamentally different attention steering. (2) Limited to 7-8B models. (3) GAR is a proxy metric; improvements don't transfer to alternative token selection definitions.

**Appendices (p13-14):** A: Expanded TF eval N=200 (Tables 14-15). B: λ sensitivity details. C: SS decay by conversation length. D: Llama TF eval comparison.

## Experiment Design Reference (from review context)

The review context lists the following imagined experiments:
1. Llama Gradient Conflict Analysis — covered in paper (Tables 3-4)
2. Expanded Eval Set (200 conversations) — covered (Tables 14-15, Appendix A)
3. λ_GAR Sensitivity Analysis — covered (Table 5, Appendix B)
4. TF vs AR Attention KL Divergence — covered (Tables 6-7, §6.2)
5. Llama-3.1-8B Scheduled Sampling — covered (Tables 10-11, §7.1)
6. SS 3-Seed Validation (Qwen) — covered (Table 9, §7.1)
7. Alternative GAR Definition Robustness — covered (Table 8, §6.3)
8. SS 4th Seed (s789) — covered (Table 9, §7.1) — paper included it
9. Long Conversation Eval (>10 turns) — covered (Table 12, §7.2)

All imagined experiments appear to be covered in the paper.

## Your Review Task

Write a thorough EMNLP 2026 review covering:

1. **Summary** (3-5 sentences)
2. **Strengths** (bulleted, specific)
3. **Weaknesses** (bulleted, specific, with severity ratings: minor/moderate/major/critical)
4. **Questions for Authors**
5. **Missing References or Related Work** (if any)
6. **Soundness** (1-5 with justification)
7. **Excitement** (1-5 with justification)
8. **Reproducibility** (1-5 with justification)
9. **Overall Assessment** (use the ARR 1-5 scale with 0.5 increments, strictly calibrated)
10. **Confidence** (1-5)
11. **Justification of Overall Assessment** (2-3 sentences)

Be rigorous. This is a negative-result / diagnostic paper. Consider:
- Is the failure mode taxonomy genuinely novel or insightful?
- Is the experimental design rigorous enough to support the causal claims?
- Does the paper advance community understanding in a meaningful way?
- Are there critical gaps in methodology or interpretation?
- How does the GAR metric specificity issue (§6.3) affect the validity of all findings?
- How does the SS model-specificity and seed sensitivity affect the contribution?
- Is the paper's scope sufficient for EMNLP?
- Consider the 4th seed (s789) data — does including it help or hurt?

Format your review as a structured report. Be specific and cite tables/sections.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "30cad153-d87d-495c-99f9-b418e448960b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T09:14:30.316Z_

```json
{
  "parentUuid": "30cad153-d87d-495c-99f9-b418e448960b",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
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
  "uuid": "7b3b591f-8f81-45d4-879b-b2ed8ea6572f",
  "timestamp": "2026-05-24T09:14:30.316Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-24T09:14:32.718Z_



I'll conduct a thorough review by first reading the actual paper and key supporting files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b3b591f-8f81-45d4-879b-b2ed8ea6572f",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM91bTRxwcV6TcSto1Kw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bee26c09-8a14-4733-ba11-b07f0e23d782",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bGgykq5CDNQbQaanPTDk6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19039,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19039,
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

_source line 4 · 2026-05-24T09:14:34.759Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01N9RBisijC8yzttrD2Ty9Cj`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bee26c09-8a14-4733-ba11-b07f0e23d782",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM91bTRxwcV6TcSto1Kw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fea73958-1ffd-42f5-af40-f021135d7525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bGgykq5CDNQbQaanPTDk6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19039,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19039,
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

_source line 5 · 2026-05-24T09:14:34.784Z_

<details><summary>↩ Tool result · `toolu_01N9RBisijC8yzttrD2Ty9Cj`</summary>

```text
artifacts/dream_reports/dream_20260519T135115/best/paper.tex
artifacts/dream_reports/dream_20260519T135115/median/paper.tex
artifacts/dream_reports/dream_20260519T135115/worst/paper.tex
artifacts/dream_reports/dream_20260519T143220/best/paper.tex
artifacts/dream_reports/dream_20260519T143220/median/paper.tex
artifacts/dream_reports/dream_20260519T145320/best/paper.tex
artifacts/dream_reports/dream_20260519T145320/median/paper.tex
artifacts/dream_reports/dream_20260519T145320/worst/paper.tex
docs/paper/background.tex
artifacts/_project/paper/analysis.tex
docs/paper/related_work.tex
docs/paper/experiments.tex
docs/paper/method.tex
docs/paper/introduction.tex
docs/paper/analysis.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/abstract.tex
artifacts/_project/paper/table_steering_full.tex
artifacts/table_steering_full.tex
paper/sections/related_work.tex
paper/main.tex
paper/sections/abstract.tex
paper/sections/introduction.tex
paper/sections/limitations.tex
paper/sections/experiments.tex
paper/sections/analysis.tex
paper/sections/method.tex
paper/sections/discussion.tex
paper/sections/conclusion.tex
paper/sections/appendix.tex
artifacts/dream_reports/dream_20260524T081135/best/paper.tex
artifacts/dream_reports/dream_20260524T081135/median/paper.tex
artifacts/dream_reports/dream_20260524T081135/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fea73958-1ffd-42f5-af40-f021135d7525",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "ec1e711b-3478-43b2-9e35-c722e28ad2ba",
  "sourceToolAssistantUUID": "fea73958-1ffd-42f5-af40-f021135d7525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T09:14:35.211Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Vce3VGr4FjwxYpkQqGTmbc`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec1e711b-3478-43b2-9e35-c722e28ad2ba",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM91bTRxwcV6TcSto1Kw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "398d5768-1a7e-4ca2-9716-8ab0eb851d10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bGgykq5CDNQbQaanPTDk6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19039,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19039,
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

_source line 7 · 2026-05-24T09:14:35.228Z_

<details><summary>↩ Tool result · `toolu_01Vce3VGr4FjwxYpkQqGTmbc`</summary>

```text
paper/fig2_training_pcgrad.pdf
paper/_figure_backups/20260524_071403/fig2_training_pcgrad.pdf
paper/fig3_gate_shift.pdf
paper/_figure_backups/20260524_071403/fig3_gate_shift.pdf
paper/fig5_attention_steering.pdf
paper/fig1_overview.pdf
paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "398d5768-1a7e-4ca2-9716-8ab0eb851d10",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "8cffdf85-a594-4601-a5ba-8197bb4c0c4f",
  "sourceToolAssistantUUID": "398d5768-1a7e-4ca2-9716-8ab0eb851d10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T09:14:40.379Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NJowkc7XxNKK4CjtUCcrJ2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cffdf85-a594-4601-a5ba-8197bb4c0c4f",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM91xmqEDysz7s7rJvaF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f0feca3-3420-4df6-90d7-32c41b8e2546",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9vgcsxUuaMkcQEnTWErU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 19039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1633,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 9 · 2026-05-24T09:14:40.385Z_

<details><summary>↩ Tool result · `toolu_01NJowkc7XxNKK4CjtUCcrJ2`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	\usepackage{placeins}
18	
19	\graphicspath{{../figures/paper/}{../artifacts/}}
20	
21	\title{From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/analysis}
34	\input{sections/discussion}
35	\input{sections/conclusion}
36	\input{sections/limitations}
37	
38	\FloatBarrier
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f0feca3-3420-4df6-90d7-32c41b8e2546",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "2cedfe13-4008-4454-866c-e889790a7c09",
  "sourceToolAssistantUUID": "4f0feca3-3420-4df6-90d7-32c41b8e2546",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T09:14:41.506Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TBBM27KB6fdTCSgFn2iriu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cedfe13-4008-4454-866c-e889790a7c09",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM91xmqEDysz7s7rJvaF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00e9f3ab-6961-49e5-88e8-e30c7db4f365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9vgcsxUuaMkcQEnTWErU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 19039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1633,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 11 · 2026-05-24T09:14:41.512Z_

<details><summary>↩ Tool result · `toolu_01TBBM27KB6fdTCSgFn2iriu`</summary>

```text
1	\begin{abstract}
2	Multi-turn dialogue requires language models to maintain attention to system-prompt goals across conversation turns, yet goal attention decays systematically (by up to 70.8\%) even when residual representations retain goal content.
3	
4	Existing remedies (inference-time attention separation, turn-agnostic gating, auxiliary attention losses) either bypass training or assume that teacher-forced optimization transfers to autoregressive generation. We show it does not: attention losses optimized to GAR\,=\,0.50 under teacher forcing collapse 8--17$\times$ on Qwen-2.5-7B and 27$\times$ on Llama-3.1-8B, degrading instruction compliance by up to 24 percentage points.
5	
6	A five-way controlled comparison isolates the cause. PCGrad eliminates gradient conflict yet \emph{worsens} AR GAR ($p$\,=\,0.002), ruling out the most intuitive explanation by \emph{modus tollens}. The root cause is exposure bias: auxiliary attention objectives have no autoregressive training signal.
7	
8	Two interventions breach the barrier: inference-time attention steering ($\beta$\,=\,5) recovers GAR to 0.727, confirming attention misallocation as the proximal cause; time-scheduled sampling, the first transfer to auxiliary attention objectives in multi-turn transformers, compresses the gap from 8$\times$ to ${\sim}$1.3$\times$ with no perplexity cost ($0.401\pm0.047$, three seeds).
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00e9f3ab-6961-49e5-88e8-e30c7db4f365",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "bf06a520-b667-455f-9bfd-028217e8066f",
  "sourceToolAssistantUUID": "00e9f3ab-6961-49e5-88e8-e30c7db4f365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T09:14:41.567Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BoRT7vdZZGgF6h5AmMM8MM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf06a520-b667-455f-9bfd-028217e8066f",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM91xmqEDysz7s7rJvaF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6e712fd-56bb-4ef2-b47b-05b8933dea85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9vgcsxUuaMkcQEnTWErU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 19039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1633,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 13 · 2026-05-24T09:14:41.574Z_

<details><summary>↩ Tool result · `toolu_01BoRT7vdZZGgF6h5AmMM8MM`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Attention to system-prompt goals decays 70.8\% over five conversation turns on Qwen-2.5-7B-Instruct, despite residual stream probes confirming that goal representations persist (AUC\,=\,0.98; \citealp{dongre2026attention}). The decay is not model-specific: \citet{dongre2026attention} documented 27--48\% Goal Accessibility Ratio (GAR) decline across 12 models, and it has concrete downstream consequences: instruction compliance drops by up to 24 percentage points on content-constrained tasks (\S\ref{sec:discussion}).
4	
5	Existing interventions operate at inference time or are turn-agnostic. Split-softmax \citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \citep{xiao2024streaming} retains anchor tokens; Gated Attention \citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. None addresses the training--inference mismatch at the source. Auxiliary attention losses, which optimize GAR alongside next-token prediction (NTP), offer a training-time alternative, but whether such objectives transfer from teacher-forced training to autoregressive generation has not been tested. Classical exposure bias mitigation \citep{bengio2015scheduled,lamb2016professor} targets RNN sequence generation; no multi-turn transformer equivalent exists.
6	
7	We introduce ThreadGate, per-layer content-and-turn-conditioned MLP gates on the residual stream ($x_{l+1} = x_l + g_l \cdot f_l(x_l)$), not as a remedy but as a controlled testbed for isolating failure mechanisms. A five-way comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) forms a causal exclusion chain (\S\ref{sec:comparison-design}): each adjacent pair kills one alternative hypothesis, tracing the failure to exposure bias \citep{bengio2015scheduled}, ruling out gradient conflict, gating architecture, and turn conditioning.
8	
9	\begin{figure*}[t]
10	  \centering
11	  \includegraphics[width=\textwidth]{fig1_headline.pdf}
12	  \caption{Exposure bias selectively destroys auxiliary attention losses. (a)~Under TF evaluation, all fine-tuned variants converge to GAR-ours$\approx$0.50; under AR generation ($N$\,=\,50), GAR collapses 7.8--16.7$\times$. Log scale; dashed slopes connect paired TF-AR values. (b)~Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation, not representation degradation, as the proximal cause (9\% PPL cost at $\beta$\,=\,3).}
13	  \label{fig:headline}
14	\end{figure*}
15	
16	Training succeeds: all variants converge to TF GAR\,=\,0.50 (Figure~\ref{fig:headline}a). Under autoregressive generation, GAR collapses to 0.019--0.064 (8--17$\times$). PCGrad eliminates gradient conflict but \emph{worsens} AR GAR ($p$\,=\,0.002), ruling it out by \emph{modus tollens}. Steering ($\beta$\,=\,5) recovers GAR to 0.727; scheduled sampling compresses the gap to ${\sim}$1.3$\times$ (\S\ref{subsec:ss}). Our contributions: (1)~first empirical measurement of exposure bias on auxiliary attention losses (8--27$\times$ across two architectures); (2)~PCGrad-based causal exclusion of gradient conflict ($p$\,=\,0.002, effect reverses); (3)~inference-time $\beta$-steering recovers GAR to 0.727, confirming attention misallocation rather than representation degradation as the proximal cause; (4)~cross-architecture validation on Llama-3.1-8B; (5)~first evidence that time-scheduled sampling \citep{bengio2015scheduled} transfers to auxiliary attention objectives in multi-turn transformers, compressing the gap from 8$\times$ to ${\sim}$1.3$\times$ ($0.401\pm0.047$, three seeds).
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6e712fd-56bb-4ef2-b47b-05b8933dea85",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "9381da4d-b0f0-4057-9e0a-70047c1bd3a5",
  "sourceToolAssistantUUID": "f6e712fd-56bb-4ef2-b47b-05b8933dea85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T09:14:45.568Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NTufFZBy9KEqHcf8dpKY3W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9381da4d-b0f0-4057-9e0a-70047c1bd3a5",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM92RqGFvYXCkk1JKSx8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "deb452d1-e302-4c6c-84b0-7b2cf9fea77a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6fvxd6GoATWyMvoAY3HR1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2240,
      "cache_read_input_tokens": 20672,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2240
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 20672,
          "cache_creation_input_tokens": 2240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2240,
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

_source line 15 · 2026-05-24T09:14:45.588Z_

<details><summary>↩ Tool result · `toolu_01NTufFZBy9KEqHcf8dpKY3W`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	Standard metrics such as perplexity and attention entropy capture generation quality but not \emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation---attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	Different transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent: some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:
22	\begin{equation}
23	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
24	\end{equation}
25	where $f_l$ denotes the sublayer computation (self-attention or FFN). This resembles ReZero \citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training. ThreadGate differs in three ways: (i)~gates are \emph{content-conditioned}, a function of the hidden state rather than a fixed scalar; (ii)~gates are \emph{turn-conditioned}, incorporating conversation-position features; (iii)~gates are initialized near identity ($\sigma(1.5) \approx 0.82$) rather than zero, preserving the pretrained model's computation.
26	
27	\paragraph{Gate network.} A fixed scalar per layer (as in ReZero) cannot adapt to varying inputs; the gate must be \emph{content-conditioned} so that different conversations or turns can receive different modulation. Adding \emph{turn conditioning} allows the gate to distinguish early turns (where GAR is naturally high) from late turns (where intervention is most needed). Each gate $g_l$ is thus produced by a two-layer MLP that takes both content and turn features as input:
28	\begin{align}\label{eq:gate}
29	  g_l = \sigma\bigl(W_2\,\text{ReLU}(&W_1\,[\text{proj}(x_l);\;\text{emb}(t_d, t_i)] \notag\\
30	  &+ b_1) + b_2\bigr),
31	\end{align}
32	where $\text{proj}(\cdot)$ reduces the hidden dimension to 16, and $\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\!=\!28$), this adds ${\sim}$57K parameters ($<$0.001\% of 7B).
33	
34	\paragraph{Turn embedding.} The embedding $\text{emb}(t_d, t_i)$ encodes turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables, allowing gates to distinguish conversation positions. The \textbf{Uniform Gate} ablation replaces $\text{emb}(\cdot)$ with a learnable constant, removing turn awareness.
35	
36	\paragraph{Initialization.} Gate biases are set to 1.5 (${\sim}$82\% pass-through), contrasting ReZero's zero initialization that would suppress pretrained capabilities. Gate parameters receive a $10\times$ learning rate multiplier.
37	
38	\subsection{Training Objective}\label{sec:loss}
39	
40	Next-token prediction alone provides no gradient signal for attention allocation; a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:
41	\begin{equation}
42	  \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\,\mathcal{L}_\text{GAR} + \lambda_\text{div}\,\mathcal{L}_\text{div}.
43	\end{equation}
44	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. We use MSE rather than cross-entropy for $\mathcal{L}_\text{GAR}$ because GAR is a continuous ratio, not a probability, and MSE provides \emph{bidirectional} pressure, penalizing both under-attention (GAR\,$<$\,$\tau$) and over-attention (GAR\,$>$\,$\tau$). This symmetry is critical: a unidirectional maximize objective drives gates toward identity (Appendix~\ref{sec:appendix-loss}). The GAR loss is:
45	\begin{equation}
46	  \mathcal{L}_\text{GAR} = \text{MSE}(\text{GAR\text{-}ours}, \tau),
47	\end{equation}
48	where $\tau = 0.5$ targets allocating half of the last token's attention capacity to goal tokens. GAR is measured at the last token of each assistant turn (GAR-ours, \S\ref{sec:background}). Without explicit diversity pressure, all gates converge to the same value (typically near 1.0), eliminating the layer-specific modulation that is the design intent. The gate diversity loss prevents this collapse:
49	\begin{equation}
50	  \mathcal{L}_\text{div} = \text{ReLU}(\sigma_\text{min} - \text{std}(\mathbf{g})),
51	\end{equation}
52	where $\mathbf{g} = [g_1, \ldots, g_L]$ and $\sigma_\text{min}$ is a minimum standard deviation threshold. Both $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$.
53	
54	\paragraph{Loss design evolution.} The MSE formulation was selected from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity. Only MSE provides bidirectional pressure, penalizing both over- and under-attention, preventing identity collapse.
55	
56	\subsection{Controlled Comparison Design}\label{sec:comparison-design}
57	
58	We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate vs.\ Uniform Gate} (turn conditioning), \textbf{ThreadGate vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient direction conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "deb452d1-e302-4c6c-84b0-7b2cf9fea77a",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "eacce8f2-fd4b-42ac-af88-ff459ca62e38",
  "sourceToolAssistantUUID": "deb452d1-e302-4c6c-84b0-7b2cf9fea77a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T09:14:45.598Z_

<details open><summary>🔧 Tool call — Read · `toolu_019oyAz1A4Y4Vai7bmXMd4iD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eacce8f2-fd4b-42ac-af88-ff459ca62e38",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM92RqGFvYXCkk1JKSx8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fba71ec-812d-4b97-acec-53388718c081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6fvxd6GoATWyMvoAY3HR1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2240,
      "cache_read_input_tokens": 20672,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2240
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 20672,
          "cache_creation_input_tokens": 2240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2240,
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

_source line 17 · 2026-05-24T09:14:45.613Z_

<details><summary>↩ Tool result · `toolu_019oyAz1A4Y4Vai7bmXMd4iD`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB; training costs in Appendix~\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; dataset statistics in Appendix~\ref{sec:appendix-data}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and PPL.
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}a). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendix~\ref{sec:appendix-stats}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). MMLU 5-shot accuracy remains within 0.8\,pp across all variants (Appendix~\ref{sec:appendix-mmlu}). We analyze this distribution shift in \S\ref{sec:analysis}.
13	
14	\begin{table*}[t]
15	\centering
16	\small
17	\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\leq$2\,pp spread); the 8--17$\times$ TF-AR gap persists across all configurations. $\bar{g}\!\pm\!\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
18	\label{tab:four-way}
19	\begin{tabular}{l ccc ccc cc c}
20	\toprule
21	& \multicolumn{3}{c}{\textbf{IID (TF)}} & \multicolumn{3}{c}{\textbf{Held-out (TF)}} & \multicolumn{2}{c}{\textbf{AR ($N$\,=\,50)}} & \\
22	\cmidrule(lr){2-4} \cmidrule(lr){5-7} \cmidrule(lr){8-9}
23	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\% CI & $\bar{g}\!\pm\!\sigma_g$ \\
24	\midrule
25	\multicolumn{10}{l}{\emph{Baseline}} \\
26	Base              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\scriptsize[.014,\,.024]} & --- \\
27	\midrule
28	\multicolumn{10}{l}{\emph{Gated variants}} \\
29	ThreadGate        & 0.50 & \textbf{0.02} & 2.78 & 0.50 & \textbf{0.02} & 2.78 & \textbf{0.064} & {\scriptsize[.041,\,.091]} & .93\,{\scriptsize$\pm$\,.05} \\
30	\;+\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\scriptsize[.023,\,.038]} & --- \\
31	Uniform Gate      & 0.49 & 0.01 & 2.78 & \textbf{0.51} & 0.01 & 2.78 & 0.033 & {\scriptsize[.025,\,.043]} & .96\,{\scriptsize$\pm$\,.05} \\
32	\midrule
33	\multicolumn{10}{l}{\emph{Ungated}} \\
34	LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\scriptsize[.027,\,.050]} & 1.00 \\
35	\bottomrule
36	\end{tabular}
37	\end{table*}
38	
39	\begin{figure}[t]
40	  \centering
41	  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
42	  \caption{Per-turn GAR-ours under AR generation ($N$\,=\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\% decay; $\Delta$\,=\,3.3\,pp between ThreadGate and LoRA-only); Base decays 87.5\%. Gating adds zero incremental effect on the attention decay pattern.}
43	  \label{fig:attention-heatmap}
44	\end{figure}
45	
46	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
47	
48	All training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\beta$ to pre-softmax attention logits for goal-token positions during generation:
49	\begin{equation}
50	  \tilde{A}_{i,j}^{(\ell,h)} = A_{i,j}^{(\ell,h)} + \beta \cdot \mathbf{1}[j \in \mathcal{G}],
51	\end{equation}
52	where $\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero (Figure~\ref{fig:headline}b). The response is sharply nonlinear: $\beta \in [0, 2]$ yields marginal improvement, then $\beta = 3$ triggers a phase transition to GAR\,=\,0.556 (9\% PPL cost). At $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77); the operating region $\beta \in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Appendix~\ref{sec:appendix-steering}).
53	
54	This closes the causal loop: if the collapse were due to representation drift in hidden states, no amount of attention reweighting could recover GAR. The recovery confirms attention misallocation, not representation degradation, as the proximal cause (qualitative examples in Appendix~\ref{sec:appendix-examples}).
55	
56	\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}
57	
58	Scheduled sampling \citep{bengio2015scheduled}, which mixes model-generated tokens into training prefixes with linearly increasing probability (implementation details in Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch identified in \S\ref{subsec:dist-shift}. Across three seeds, AR GAR-ours rises from 0.064 to $0.401\pm0.047$ (seeds: 0.347 / 0.423 / 0.433), compressing the gap from 7.8$\times$ to ${\sim}$1.3$\times$ (per-seed gaps: 1.45$\times$, 1.17$\times$, 1.15$\times$; TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.001$). Steering on SS models is remarkably stable ($\beta$\,=\,5: $0.717\pm0.001$): the training-time seed variance (std\,=\,0.047 at $\beta$\,=\,0) is nearly eliminated, suggesting $\beta$-steering converges to a seed-independent attention equilibrium. The improvement generalizes across GAR definitions: SS raises mid-turn GAR above 0.36 under all four alternative token-position variants (Appendix~\ref{sec:appendix-gar-robust}), while ThreadGate only improves last-token GAR (0.325 vs.\ all-token 0.025): SS builds a broad goal-attention pattern, not position-specific overfitting. GAR-Dongre also rises substantially under SS ($N$\,=\,5 pilot; see Appendix~\ref{sec:appendix-n5}), the only intervention that moves both metrics. The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
59	
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fba71ec-812d-4b97-acec-53388718c081",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "a743ed76-0c30-4113-a88f-38c4e835dcd9",
  "sourceToolAssistantUUID": "4fba71ec-812d-4b97-acec-53388718c081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T09:14:50.017Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QaqDwmyKspJgrEyKG1kbo7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a743ed76-0c30-4113-a88f-38c4e835dcd9",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM92jJVY9RTaJyPVBFeV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff52acf7-7ed8-4c08-8ae0-37f8f1ee7178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6SEoEtK5CVjpfsj8LXgZS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5485,
      "cache_read_input_tokens": 22912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5485,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 19 · 2026-05-24T09:14:50.025Z_

<details><summary>↩ Tool result · `toolu_01QaqDwmyKspJgrEyKG1kbo7`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison (\S\ref{sec:experiments}) yields a paradox: training succeeds but inference fails, and no single architectural factor explains the gap. This section resolves it through a causal exclusion chain; each subsection kills one alternative hypothesis: \S\ref{subsec:gate-conditioning} kills ``turn conditioning rescues late-turn attention''; \S\ref{subsec:pcgrad} kills ``gradient conflict prevents GAR convergence''; \S\ref{subsec:dist-shift} identifies exposure bias as the surviving explanation. \S\ref{subsec:mechanism-specificity} confirms selectivity via an orthogonal metric, and \S\ref{subsec:cross-model} confirms generalization across architectures.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:four-way}; full gate profiles in Appendix~\ref{sec:appendix-gate-profile}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?
8	
9	\begin{figure}[t]
10	  \centering
11	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig3_gate_shift.pdf}
12	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:four-way}) due to smaller sample size.}
13	  \label{fig:gate-shift}
14	\end{figure}
15	
16	\subsection{PCGrad Gradient Conflict Exclusion}\label{subsec:pcgrad}
17	
18	NTP and GAR gradients oppose in 68--79\% of layers (cosine similarity $-$0.089$\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$ (full gradient statistics in Appendix~\ref{sec:appendix-gradient}). If this conflict prevents GAR convergence, eliminating it via PCGrad \citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \emph{diagnostic} tool rather than an optimization method.
19	
20	PCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \emph{worsens}: 0.064$\to$0.030 ($p$\,=\,0.002; Figure~\ref{fig:training-pcgrad}b). By \emph{modus tollens}: removing direction conflict does not prevent collapse; therefore it is not the cause. The 7.5--14.7$\times$ magnitude dominance renders directional interference inconsequential. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\,=\,+0.005) with 25.7$\times$ NTP dominance (Table~\ref{tab:gradient-crossmodel}).
21	
22	\begin{figure}[t]
23	  \centering
24	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
25	  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad eliminates gradient direction conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that direction conflict is not the cause (\S\ref{subsec:pcgrad}).}
26	  \label{fig:training-pcgrad}
27	\end{figure}
28	
29	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
30	
31	The TF-AR GAR gap persists across all variants (Table~\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, so the shift selectively destroys concentrated last-token attention while leaving diffuse attention unaffected. The mechanism is exposure bias \citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. NTP self-recovers \citep{he2019exposure} because prediction is the same task at both regimes; GAR optimizes a distributional property with no autoregressive counterpart. Attention patterns over model-generated tokens have no training-time analogue, explaining why TF GAR-ours remains near $\tau$\,=\,0.5 while AR GAR collapses (77--87\% per-turn decay; Figure~\ref{fig:attention-heatmap}; scaling analysis in Appendix~\ref{sec:appendix-eb-scaling}; per-turn dynamics in Appendix~\ref{sec:appendix-ar-gar-dynamics}).
32	
33	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
34	
35	We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
36	
37	\subsection{Cross-Model Replication}\label{subsec:cross-model}
38	
39	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (CoV\,$>$\,100\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a; Appendix~\ref{sec:appendix-llama}). Gate profiles differ qualitatively (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793) while Llama dips at late layers (L25\,=\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\ref{sec:appendix-viz}). The gap is substantial on both architectures (8--17$\times$ on Qwen, 27$\times$ on Llama), consistent with exposure bias as architecture-independent. Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\% GAR decay and $\beta$-steering recovery to 0.715 (Appendix~\ref{sec:appendix-1.5b}).
40	
41	\begin{figure}[t]
42	  \centering
43	  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
44	  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}
45	  \label{fig:crossmodel}
46	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff52acf7-7ed8-4c08-8ae0-37f8f1ee7178",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "27e35fb9-1d8c-4255-bb8c-f8d4a2e883d8",
  "sourceToolAssistantUUID": "ff52acf7-7ed8-4c08-8ae0-37f8f1ee7178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T09:14:50.488Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QKzRXY4vphvMnD3a3ZbDfU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27e35fb9-1d8c-4255-bb8c-f8d4a2e883d8",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM92jJVY9RTaJyPVBFeV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8ede930-4bf0-4467-8276-118a2f89d980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6SEoEtK5CVjpfsj8LXgZS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5485,
      "cache_read_input_tokens": 22912,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5485
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 22912,
          "cache_creation_input_tokens": 5485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5485,
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

_source line 21 · 2026-05-24T09:14:50.493Z_

<details><summary>↩ Tool result · `toolu_01QKzRXY4vphvMnD3a3ZbDfU`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. This has implications beyond ThreadGate: any auxiliary attention objective paired with teacher forcing, whether per-head gating \citep{qiu2025gated}, split-softmax \citep{li2024measuring}, or residual scaling \citep{bachlechner2021rezero}, should face the same exposure bias barrier when targeting distributional properties of the attention pattern rather than the prediction itself.
4	
5	\paragraph{Why NTP self-recovers but GAR does not.} NTP self-recovers because the task (predict one token from a prefix) is identical at training and inference; exposure bias shifts the prefix distribution but preserves the prediction task \citep{he2019exposure}. GAR optimizes a \emph{global property of the prefix}, attention allocation to goal tokens, that has no autoregressive counterpart: the model receives no feedback on attention distributions during generation, so the training signal is specific to teacher-forced prefixes. Per-head analysis confirms this selectivity: heads with higher TF GAR shift most under AR generation ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}).
6	
7	\paragraph{Downstream effects.} Instruction retention ($\beta$\,=\,3) shows late-turn compliance rising from 75.9\% to 87.0\% (+11.1\,pp, McNemar $p$\,=\,0.077; GAR correlation $r$\,=\,0.200, $p$\,=\,0.007). Content constraints benefit most (+23.8\,pp), while format constraints show zero change, consistent with GAR targeting cross-turn semantic coherence rather than locally-verifiable procedural rules (Appendix~\ref{sec:appendix-ir}).
8	
9	\paragraph{SS and steering as substitutes.} SS provides training-time mitigation with no inference cost; steering provides inference-time recovery with PPL cost. At high $\beta$ the two converge: they are substitutes, not complements ($\beta$\,=\,5: SS GAR\,=\,$0.717\pm0.001$ vs.\ TG\,=\,0.727; Figure~\ref{fig:headline}b). SS is preferable when inference budgets are tight, steering when retraining is infeasible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8ede930-4bf0-4467-8276-118a2f89d980",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "2628dc04-e719-48d1-96e3-75cd9d3c6c7e",
  "sourceToolAssistantUUID": "a8ede930-4bf0-4467-8276-118a2f89d980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-24T09:14:53.631Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S8XZYJaYbihbCs1aEw3vKE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2628dc04-e719-48d1-96e3-75cd9d3c6c7e",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM935xhzgjv9zuQm5j7x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9270c8f0-ae81-4cc5-acc6-9f041107e8c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqvyHk3bFmskusnWRvAZiZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3266,
      "cache_read_input_tokens": 28397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3266,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 23 · 2026-05-24T09:14:53.636Z_

<details><summary>↩ Tool result · `toolu_01S8XZYJaYbihbCs1aEw3vKE`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn dialogue and attention decay.}
4	Multi-turn coherence has been a persistent challenge from early dialogue systems \citep{li2016persona,zhang2020dialogpt} through modern long-context models \citep{xu2022goldfish}, with benchmarks such as MT-Bench-101 \citep{bai2024mtbench101} continuing to expose quality gaps at later turns \citep{laban2025lost,liu2026intent}. Most relevant to our work, \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\% across 12 models while residual probes retain goal information (AUC\,=\,0.98). We observe a steeper 70.8\% decline on Qwen-2.5-7B. \citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.
5	
6	\paragraph{Gating and attention manipulation.}
7	Residual gating has evolved from highway networks \citep{srivastava2015highway} through ResNet skip connections \citep{he2016deep} to ReZero \citep{bachlechner2021rezero}, layer pruning \citep{gromov2024unreasonable}, and adaptive depth \citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \citep{qiu2025gated}: per-head sigmoid gates achieving MMLU \citep{hendrycks2021measuring} $+$2.03 at 15B scale. ThreadGate differs in conditioning on turn position; our results show neither turn conditioning nor GLU-style gating \citep{shazeer2020glu} overcomes exposure bias. On the analysis side, head specialization \citep{clark2019what,voita2019analyzing}, positional bias calibration \citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \citealp{zhang2024tell}) address inference behavior; our $\beta$-steering serves a diagnostic role. Multi-task gradient methods---PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}---treat conflict as the root cause; we repurpose PCGrad as a diagnostic and show conflict is a symptom, not the cause.
8	
9	\paragraph{Exposure bias in sequence models.}
10	Teacher forcing creates a distributional mismatch between training and inference \citep{wiseman2016sequence,arora2022exposure}. Scheduled sampling \citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \citep{ranzato2016sequence}, adversarial regularization \citep{lamb2016professor}, self-recovery analysis \citep{he2019exposure}, bridging strategies for NMT \citep{zhang2019bridging}, and search-based training \citep{leblond2018searnn}. \citet{mihaylova2019scheduled} extended scheduled sampling to transformers for single-turn NMT. \citet{dou2019attention} proposed attention forcing---supervising cross-attention during NMT---and \citet{dou2022parallel} extended it with KL-divergence switching. Our work differs: (i)~time-scheduled sampling (linearly increasing $\rho$), not data-dependent; (ii)~self-attention in multi-turn dialogue, not cross-attention in NMT; (iii)~auxiliary attention objectives, not primary translation loss. No prior work examines exposure bias on \emph{auxiliary} attention objectives or provides multi-turn transformer mitigation; we fill both gaps.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9270c8f0-ae81-4cc5-acc6-9f041107e8c8",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "adac69a0-2c8e-400d-8de0-174e62149273",
  "sourceToolAssistantUUID": "9270c8f0-ae81-4cc5-acc6-9f041107e8c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T09:14:54.543Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KxXSHAdNFp6w4zcdFH9sjN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adac69a0-2c8e-400d-8de0-174e62149273",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM935xhzgjv9zuQm5j7x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04bbb464-b446-49c2-a49e-8017b4fd27c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqvyHk3bFmskusnWRvAZiZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3266,
      "cache_read_input_tokens": 28397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3266,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 25 · 2026-05-24T09:14:54.548Z_

<details><summary>↩ Tool result · `toolu_01KxXSHAdNFp6w4zcdFH9sjN`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	A five-way controlled comparison on ThreadGate, per-layer content-and-turn-conditioned gates with an auxiliary GAR loss, reveals that training succeeds (TF GAR\,=\,0.50) but autoregressive GAR collapses 8--17$\times$ on Qwen-2.5-7B (27$\times$ (median) on Llama-3.1-8B). Each ablation pair kills one hypothesis; the failure traces to exposure bias, classical in origin but with no prior multi-turn transformer characterization. Steering ($\beta$\,=\,5) recovers GAR to 0.727, confirming attention misallocation as the proximal cause. Scheduled sampling compresses the gap from 8$\times$ to ${\sim}$1.3$\times$ with no perplexity cost ($0.401\pm0.047$, three seeds), the first transfer of time-scheduled sampling to auxiliary attention objectives in multi-turn transformers.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04bbb464-b446-49c2-a49e-8017b4fd27c1",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "9ad43f82-b566-415c-8969-72f11001db67",
  "sourceToolAssistantUUID": "04bbb464-b446-49c2-a49e-8017b4fd27c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T09:14:55.025Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U8thEG7VsioKXPDR3K8LFj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ad43f82-b566-415c-8969-72f11001db67",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM935xhzgjv9zuQm5j7x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f833ebc-6e38-44d6-b476-e1fefd6f9b70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqvyHk3bFmskusnWRvAZiZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3266,
      "cache_read_input_tokens": 28397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3266,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 27 · 2026-05-24T09:14:55.030Z_

<details><summary>↩ Tool result · `toolu_01U8thEG7VsioKXPDR3K8LFj`</summary>

```text
1	\section{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B), one dataset (UltraChat, 8K conversations), and most configurations use a single seed (scheduled sampling validated on three seeds; \S\ref{subsec:ss}); quality assessment relies on PPL rather than comprehensive benchmarks \citep{hendrycks2021measuring,lin2022truthfulqa}. We test only one auxiliary loss family (GAR with MSE target $\tau$\,=\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias. The PCGrad exclusion addresses gradient direction conflict only; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibrium approaches \citep{navon2022nash} remain untested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f833ebc-6e38-44d6-b476-e1fefd6f9b70",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "f50ce83c-4dac-4ad3-891b-7b9d44e73f86",
  "sourceToolAssistantUUID": "9f833ebc-6e38-44d6-b476-e1fefd6f9b70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-24T09:14:55.308Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JYwudMXrihZ2LMnYKViwAa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f50ce83c-4dac-4ad3-891b-7b9d44e73f86",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM935xhzgjv9zuQm5j7x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cf73818-94c5-4394-8239-0f6be489129e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqvyHk3bFmskusnWRvAZiZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3266,
      "cache_read_input_tokens": 28397,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3266
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 28397,
          "cache_creation_input_tokens": 3266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3266,
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

_source line 29 · 2026-05-24T09:14:55.616Z_

<details><summary>↩ Tool result · `toolu_01JYwudMXrihZ2LMnYKViwAa`</summary>

```text
1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[h]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (102\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
38	
39	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
40	
41	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
42	
43	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
44	
45	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
46	
47	\begin{table*}[t]
48	\centering\footnotesize
49	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
50	\label{tab:loss-iterations}
51	\begin{tabular}{l l l p{5.8cm} c c}
52	\toprule
53	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
54	\midrule
55	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
56	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
57	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
58	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
59	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
60	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
61	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	\section{Instruction Retention Details}\label{sec:appendix-ir}
67	
68	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end'').
69	
70	Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. Format and count constraints, which are more procedural and less dependent on sustained attention to the system prompt, show no change.
71	
72	The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
73	
74	\begin{table}[h]
75	\centering\small
76	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
77	\label{tab:ir-results}
78	\begin{tabular}{lccc}
79	\toprule
80	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
81	\midrule
82	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
83	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
84	Count      & 100\%  & 100\%  & 0 \\
85	Format     & 100\%  & 100\%  & 0 \\
86	\midrule
87	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
88	\bottomrule
89	\end{tabular}
90	\end{table}
91	
92	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
93	
94	The main results (Table~\ref{tab:four-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each. In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. This length dependence is consistent with exposure bias compounding over turns---each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn 10 the accumulated drift overwhelms any gating signal.
95	
96	\begin{table}[h]
97	\centering\small
98	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:four-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
99	\label{tab:n5-ar}
100	\begin{tabular}{lcc}
101	\toprule
102	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:four-way}} \\
103	\midrule
104	Base & 0.012 & $-$0.007 \\
105	\midrule
106	ThreadGate & 0.016 & $-$0.048 \\
107	\;+\,PCGrad & 0.015 & $-$0.015 \\
108	Uniform Gate & 0.015 & $-$0.018 \\
109	LoRA-only & 0.025 & $-$0.012 \\
110	\bottomrule
111	\end{tabular}
112	\end{table}
113	
114	\section{Statistical Test Details}\label{sec:appendix-stats}
115	
116	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
117	
118	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
119	
120	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
121	
122	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
123	
124	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
125	
126	\begin{table}[h]
127	\centering\small
128	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
129	\label{tab:stat-tests}
130	\begin{tabular}{llcc}
131	\toprule
132	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
133	\midrule
134	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
135	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
136	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
137	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
138	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
139	\midrule
140	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
141	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
142	\midrule
143	\multicolumn{4}{l}{\emph{Instruction retention}} \\
144	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
145	GAR--compliance & Pearson & 0.007 & 0.200 \\
146	\bottomrule
147	\end{tabular}
148	\end{table}
149	
150	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
151	
152	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
153	
154	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
155	
156	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
157	
158	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
159	
160	\begin{table}[h]
161	\centering\small
162	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20, mid-turn). Median is more representative due to heavy-tailed AR distributions.}
163	\label{tab:llama-full}
164	\resizebox{\columnwidth}{!}{%
165	\begin{tabular}{lcccc}
166	\toprule
167	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
168	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
169	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
170	\midrule
171	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
172	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
173	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
174	\bottomrule
175	\end{tabular}}
176	\end{table}
177	
178	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
179	
180	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
181	
182	\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\% decline. This is steeper than Qwen's 70.8\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\ 28 KV heads).
183	
184	\paragraph{Cross-model gradient analysis.} Table~\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\approx$\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\times$ on Qwen and 25.7$\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \emph{modus tollens} argument (\S\ref{subsec:pcgrad}): gradient conflict is not the root cause of the TF-AR gap.
185	
186	\begin{table}[h]
187	\centering\small
188	\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\times$.}
189	\label{tab:gradient-crossmodel}
190	\begin{tabular}{lcc}
191	\toprule
192	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
193	\midrule
194	Mean cos sim & $-$0.042 & +0.005 \\
195	Neg-layer \% & 67.9\% & 53.1\% \\
196	NTP/GAR mag ratio & 14.7$\times$ & 25.7$\times$ \\
197	\bottomrule
198	\end{tabular}
199	\end{table}
200	
201	\section{Additional Visualizations}\label{sec:appendix-viz}
202	
203	This section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.
204	
205	\subsection{Gate Profile Heatmap}
206	
207	Figure~\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.
208	
209	\begin{figure*}[h]
210	\centering
211	\includegraphics[width=0.95\textwidth]{fig_gate_profile_heatmap.pdf}
212	\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
213	\label{fig:gate-heatmap}
214	\end{figure*}
215	
216	\subsection{Cross-Model Gate Profile Comparison}
217	
218	Figure~\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\,=\,0.793, L5\,=\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.
219	
220	\begin{figure*}[h]
221	\centering
222	\includegraphics[width=0.95\textwidth]{fig_gate_profile_crossmodel.pdf}
223	\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
224	\label{fig:gate-crossmodel}
225	\end{figure*}
226	
227	\subsection{Per-Turn AR GAR Decay}
228	
229	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:four-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
230	
231	\begin{figure*}[h]
232	\centering
233	\includegraphics[width=0.95\textwidth]{fig_ar_gar_perturn.pdf}
234	\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
235	\label{fig:ar-gar-perturn}
236	\end{figure*}
237	
238	\subsection{Gate Value Distributions}
239	
240	Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
241	
242	\begin{figure*}[h]
243	\centering
244	\includegraphics[width=0.95\textwidth]{fig_gate_distribution.pdf}
245	\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
246	\label{fig:gate-distribution}
247	\end{figure*}
248	
249	\subsection{Training Loss Curves}
250	
251	Figure~\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.
252	
253	\begin{figure*}[h]
254	\centering
255	\includegraphics[width=0.95\textwidth]{fig_training_loss_curves.pdf}
256	\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
257	\label{fig:training-loss}
258	\end{figure*}
259	
260	\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
261	
262	\begin{table*}[t]
263	\centering\small
264	\caption{Full attention steering results across evaluation settings.
265	\textbf{Bold} indicates the operating point cited in the main text ($\beta$\,=\,5).
266	A visual gap separates the phase-transition boundary: GAR jumps sharply between $\beta$\,=\,2 and $\beta$\,=\,3 across all settings.}
267	\label{tab:steering-full}
268	\begin{tabular}{r cc cc cc}
269	\toprule
270	 & \multicolumn{2}{c}{\textbf{$N$\,=\,5, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,50, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,200, TF}} \\
271	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
272	$\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\
273	\midrule
274	0   & .028 & 1.41 & $.064 \pm .081$ & $1.43 \pm .10$ & .535 & 2.62 \\
275	0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\
276	1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\
277	2   & .062 & 1.41 & $.128 \pm .110$ & $1.48 \pm .14$ & .611 & 2.69 \\
278	\addlinespace[3pt]
279	3   & ---  & ---  & $.556 \pm .060$ & $1.56 \pm .17$ & .788 & 2.93 \\
280	4   & ---  & ---  & $.644 \pm .061$ & $1.67 \pm .22$ & .817 & 3.49 \\
281	\textbf{5}  & \textbf{.680} & \textbf{1.91} & $\mathbf{.727 \pm .061}$ & $\mathbf{1.77 \pm .27}$ & \textbf{.833} & \textbf{6.15} \\
282	10  & .959 & 4.22 & $.961 \pm .015$ & $3.45 \pm 1.78$ & .977 & 505.2 \\
283	\bottomrule
284	\end{tabular}
285	\end{table*}
286	
287	\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
288	
289	Table~\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\sigma$\,=\,0.051).
290	
291	\begin{table}[h]
292	\centering\small
293	\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
294	\label{tab:gate-profile}
295	\resizebox{\columnwidth}{!}{%
296	\begin{tabular}{cccccccc}
297	\toprule
298	L0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\
299	.883 & \textbf{.793} & .996 & .988 & .984 & \textbf{.797} & .961 & .918 \\
300	\midrule
301	L8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\
302	.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\
303	\midrule
304	L16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\
305	.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\
306	\midrule
307	L24 & L25 & L26 & L27 & \multicolumn{4}{c}{Summary} \\
308	.980 & .984 & .988 & 1.00 & \multicolumn{4}{c}{$\bar{g}$\,=\,.947, $\sigma$\,=\,.051} \\
309	\bottomrule
310	\end{tabular}}
311	\end{table}
312	
313	The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
314	
315	\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
316	
317	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
318	
319	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
320	
321	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
322	
323	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
324	
325	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing. Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.
326	
327	\section{Computational Cost Analysis}\label{sec:appendix-cost}
328	
329	\begin{table}[h]
330	\centering\small
331	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (102\,GB VRAM).}
332	\label{tab:cost}
333	\resizebox{\columnwidth}{!}{%
334	\begin{tabular}{lcccc}
335	\toprule
336	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
337	\midrule
338	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
339	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
340	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
341	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
342	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
343	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
344	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
345	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
346	\midrule
347	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
348	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
349	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
350	\bottomrule
351	\end{tabular}}
352	\end{table}
353	
354	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
355	
356	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
357	
358	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
359	
360	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
361	
362	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
363	
364	\begin{table*}[h]
365	\centering\small
366	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
367	\label{tab:examples}
368	\begin{tabular}{c p{5.5cm} p{5.5cm}}
369	\toprule
370	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
371	\midrule
372	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
373	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
374	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
375	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
376	\bottomrule
377	\end{tabular}
378	\end{table*}
379	
380	The pattern is consistent with the GAR decay analysis (\S\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\ref{tab:ir-results} shows that content constraints benefit most from this effect.
381	
382	\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
383	
384	Figure~\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate (v7) and PCGrad (v9) training. Under standard training, 79\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---NTP magnitude dominance grows from 7.5$\times$ to 14.7$\times$ across epochs. Under PCGrad training, the conflict percentage decreases more slowly (79\%$\to$71\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane. The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\ref{fig:gate-heatmap}). Despite this spatial correlation, eliminating directional conflict via PCGrad does not improve AR GAR (\S\ref{subsec:pcgrad}), confirming that the 7.5--14.7$\times$ magnitude dominance---not directional opposition---determines the effective optimization trajectory.
385	
386	\begin{figure*}[h]
387	\centering
388	\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
389	\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out directional conflict as the cause (\S\ref{subsec:pcgrad}).}
390	\label{fig:gradient-heatmap}
391	\end{figure*}
392	
393	\section{Training Data Characteristics}\label{sec:appendix-data}
394	
395	All experiments use 8,000 multi-turn conversations sampled from the UltraChat \citep{ding2023ultrachat} training split. Table~\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\,=\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\,=\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\ref{sec:appendix-n5}).
396	
397	\begin{table}[h]
398	\centering\small
399	\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
400	\label{tab:data-stats}
401	\begin{tabular}{lcc}
402	\toprule
403	\textbf{Property} & \textbf{Train} & \textbf{Eval (primary)} \\
404	\midrule
405	Conversations & 8,000 & 50 \\
406	Min user turns & 3 & 3 \\
407	Max sequence length & 2,048 & 2,048 \\
408	Source & UltraChat train & UltraChat train \\
409	Overlap & --- & non-overlapping \\
410	\bottomrule
411	\end{tabular}
412	\end{table}
413	
414	\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
415	
416	Figure~\ref{fig:eb-scaling} quantifies two dimensions of the exposure bias phenomenon. Panel~(a) compares the TF/AR gap ratio across all training variants and both architectures. On Qwen, ThreadGate achieves the smallest gap among standard variants (7.8$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.3$\times$, the only variant approaching parity. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
417	
418	\begin{figure*}[h]
419	\centering
420	\includegraphics[width=0.95\textwidth]{fig_eb_scaling.pdf}
421	\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
422	\label{fig:eb-scaling}
423	\end{figure*}
424	
425	\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
426	
427	To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
428	
429	All six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\ref{tab:four-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}
430	
431	\begin{figure}[t]
432	\centering
433	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
434	\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
435	\label{fig:kl_ar_gar_curves}
436	\end{figure}
437	
438	\begin{figure}[t]
439	\centering
440	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_bar.pdf}
441	\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}
442	\label{fig:kl_ar_gar_bar}
443	\end{figure}
444	
445	This pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \S\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.
446	
447	\section{Per-Head KL Divergence Analysis}\label{sec:appendix-kl}
448	
449	To test whether exposure bias selectively disrupts goal-attending heads, we compute per-head TF vs.\ AR attention divergence on 30 held-out conversations. For each attention head, we measure the KL divergence $D_\text{KL}(p_\text{TF} \| p_\text{AR})$ between teacher-forced and autoregressive attention distributions, and the absolute GAR shift $\Delta\text{GAR} = |\text{GAR}_\text{TF} - \text{GAR}_\text{AR}|$.
450	
451	\begin{table}[h]
452	\centering\small
453	\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\,=\,0.743).}
454	\label{tab:kl-perhead}
455	\begin{tabular}{lcc}
456	\toprule
457	\textbf{Metric} & \textbf{Base} & \textbf{TG v7} \\
458	\midrule
459	Mean $\Delta$GAR & 0.012 & 0.016 \\
460	Mean KL & 0.043 & 0.054 \\
461	Corr(TF\_GAR, $\Delta$GAR) & 0.673 & 0.743 \\
462	\bottomrule
463	\end{tabular}
464	\end{table}
465	
466	ThreadGate exhibits 35\% larger mean $\Delta$GAR (0.016 vs.\ 0.012) and 26\% larger mean KL (0.054 vs.\ 0.043) than Base. The correlation between per-head TF GAR and $\Delta$GAR is strong for both models ($r$\,=\,0.673 for Base, 0.743 for TG), confirming that heads with higher goal attention under teacher forcing are disproportionately disrupted under autoregressive generation. The highest-KL heads concentrate at output-adjacent layers (L23--L27) and L9. This pattern is consistent with the exposure bias mechanism: the auxiliary GAR loss successfully trains concentrated goal attention, but precisely these learned routing patterns have no autoregressive counterpart and thus shift most during generation.
467	
468	\section{GAR Definition Robustness}\label{sec:appendix-gar-robust}
469	
470	To assess whether our conclusions depend on the specific GAR definition, we evaluate four alternative token-position variants on 50 held-out conversations (Table~\ref{tab:gar-robust}): (1)~\emph{ours} (last-token): attention from the last token to goal tokens (standard GAR-ours); (2)~\emph{all-token}: average attention from all tokens to goal tokens; (3)~\emph{first-token}: attention from the first assistant token to goal tokens; (4)~\emph{goal-only}: attention from the last token to system-prompt-only tokens (excluding conversation content).
471	
472	\begin{table}[h]
473	\centering\small
474	\caption{Mid-turn GAR under four alternative definitions ($N$\,=\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}
475	\label{tab:gar-robust}
476	\begin{tabular}{lccc}
477	\toprule
478	\textbf{Definition} & \textbf{Base} & \textbf{TG} & \textbf{SS} \\
479	\midrule
480	Ours (last-token) & 0.015 & \textbf{0.325} & \textbf{0.458} \\
481	All-token & 0.015 & 0.025 & \textbf{0.366} \\
482	First-token & 0.022 & 0.039 & \textbf{0.412} \\
483	Goal-only & 0.005 & \textbf{0.310} & \textbf{0.444} \\
484	\bottomrule
485	\end{tabular}
486	\end{table}
487	
488	ThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \to 0.325$; goal-only: $0.005 \to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.
489	
490	Scheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.
491	
492	\section{General Capability Preservation (MMLU)}\label{sec:appendix-mmlu}
493	
494	To confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \citep{hendrycks2021measuring} ($N$\,=\,14{,}042 questions).
495	
496	\begin{table}[h]
497	\centering\small
498	\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\,pp of the base LoRA-only checkpoint.}
499	\label{tab:mmlu}
500	\begin{tabular}{lcc}
501	\toprule
502	\textbf{Model} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs Base} \\
503	\midrule
504	Base (LoRA-only) & 74.23 & --- \\
505	PCGrad (v9) & 73.86 & $-$0.38 \\
506	SS (v8b) & 73.75 & $-$0.48 \\
507	LoRA-only & 73.57 & $-$0.66 \\
508	ThreadGate (v7) & 73.47 & $-$0.77 \\
509	Uniform Gate & 73.46 & $-$0.78 \\
510	\bottomrule
511	\end{tabular}
512	\end{table}
513	
514	All variants degrade by $<$0.8\,pp, confirming that attention steering and auxiliary GAR losses do not harm general language understanding. The ordering does not track GAR performance (e.g., PCGrad shows the smallest MMLU drop despite the worst AR GAR), consistent with GAR and NTP occupying largely orthogonal subspaces.
515	
516	\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b}
517	
518	We validate cross-scale on Qwen-2.5-1.5B-Instruct to test whether goal attention decay and $\beta$-steering generalize to smaller models.
519	
520	\paragraph{Phase~1 GAR decay.} The 1.5B base model exhibits 79.8\% GAR decline from turn~1 to mid-turns (vs.\ 70.8\% on 7B), confirming that attention decay is present across scales and is more severe at smaller model sizes.
521	
522	\paragraph{Steering evaluation.} Table~\ref{tab:1.5b-steering} reports AR evaluation ($N$\,=\,50). We report median PPL because Base $\beta$\,=\,3 contains a catastrophic outlier (conversation~\#11, PPL\,$>$\,$10^8$) that inflates the mean.\footnote{The outlier occurs in a single conversation where $\beta$-steering causes the base model to enter a degenerate repetition loop. ThreadGate produces zero such outliers across all $\beta$ values, suggesting the gate provides stability against catastrophic steering failures.}
523	
524	\begin{table}[h]
525	\centering\small
526	\caption{Cross-scale $\beta$-steering on Qwen-2.5-1.5B ($N$\,=\,50, AR). PPL is median due to catastrophic Base outlier at $\beta$\,=\,3. TG eliminates outliers across all $\beta$ values.}
527	\label{tab:1.5b-steering}
528	\begin{tabular}{llcc}
529	\toprule
530	\textbf{Model} & $\beta$ & \textbf{AR GAR} & \textbf{PPL (med)} \\
531	\midrule
532	Base & 0 & 0.017 & 1.909 \\
533	TG & 0 & 0.023 & 1.897 \\
534	\midrule
535	Base & 3 & 0.120 & 2.216 \\
536	TG & 3 & 0.114 & 1.975 \\
537	\midrule
538	Base & 5 & 0.657 & 2.804 \\
539	TG & 5 & 0.715 & 2.624 \\
540	\bottomrule
541	\end{tabular}
542	\end{table}
543	
544	The steering pattern mirrors the 7B results: $\beta$\,=\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\beta$\,=\,0, TG shows a small but significant GAR advantage ($p$\,=\,0.005); at $\beta$\,=\,3, the TG--Base difference is not statistically significant ($p$\,=\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.
545	
546	\section{Use of AI Assistants}\label{sec:appendix-ai}
547	
548	We used Claude (Anthropic) as an AI coding and writing assistant
549	throughout this work. Specifically:
550	\begin{itemize}
551	    \item \textbf{Code:} drafting experiment scripts, data-processing
552	    pipelines, and analysis utilities; debugging and refactoring.
553	    \item \textbf{Writing:} drafting and revising paper sections,
554	    polishing prose, and reformatting LaTeX.
555	    \item \textbf{Literature:} summarizing related papers to inform
556	    related-work section.
557	\end{itemize}
558	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cf73818-94c5-4394-8239-0f6be489129e",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "c2326867-f052-4c8a-870b-5f7378f05de2",
  "sourceToolAssistantUUID": "6cf73818-94c5-4394-8239-0f6be489129e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-24T09:14:59.266Z_

Now I have a thorough understanding of the paper. Let me also check the references file for completeness and look at some figures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2326867-f052-4c8a-870b-5f7378f05de2",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM93TmNvEB6ME3rTKaip",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a81807e-9a0a-44cd-94d8-646b4af025d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7rSxCxdEp9e3DWqmDrgLk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17952,
      "cache_read_input_tokens": 31663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17952,
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

_source line 31 · 2026-05-24T09:15:01.305Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VT7ULsCksvzTFZUiJnW4CQ`</summary>

```json
{
  "pattern": "paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a81807e-9a0a-44cd-94d8-646b4af025d5",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM93TmNvEB6ME3rTKaip",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0622bdb-208a-4c94-8dce-b2ac3b5bc37b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7rSxCxdEp9e3DWqmDrgLk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17952,
      "cache_read_input_tokens": 31663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17952,
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

_source line 32 · 2026-05-24T09:15:01.329Z_

<details><summary>↩ Tool result · `toolu_01VT7ULsCksvzTFZUiJnW4CQ`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0622bdb-208a-4c94-8dce-b2ac3b5bc37b",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "dbbe319c-e39d-4bd4-8d34-41185ac81eaf",
  "sourceToolAssistantUUID": "a0622bdb-208a-4c94-8dce-b2ac3b5bc37b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-24T09:15:02.145Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LMX1WZzBET3bmPMhhMHjZ1`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/*.tex",
  "description": "Count lines in each section file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbbe319c-e39d-4bd4-8d34-41185ac81eaf",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM93TmNvEB6ME3rTKaip",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "461b24c7-b250-44d6-a7ce-e854695926e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7rSxCxdEp9e3DWqmDrgLk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17952,
      "cache_read_input_tokens": 31663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17952,
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

_source line 34 · 2026-05-24T09:15:02.308Z_

<details><summary>↩ Tool result · `toolu_01LMX1WZzBET3bmPMhhMHjZ1`</summary>

```text
    9 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex
   45 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex
  557 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex
    3 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex
    8 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex
   59 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex
   16 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex
    2 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex
   58 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex
   10 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex
  767 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "461b24c7-b250-44d6-a7ce-e854695926e7",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "9e2b14f8-69e4-46c6-8e1f-c8d25e2c47bf",
  "sourceToolAssistantUUID": "461b24c7-b250-44d6-a7ce-e854695926e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-24T09:15:05.556Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RYrXYushVnm6pAW6o3tHEw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e2b14f8-69e4-46c6-8e1f-c8d25e2c47bf",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM93y8iH2bSBJGmrBTGC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2426a646-301c-4d81-83c5-5984485be118",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01An1MXqhTDYbSciQRMamufZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 49615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 36 · 2026-05-24T09:15:05.565Z_

<details><summary>↩ Tool result · `toolu_01RYrXYushVnm6pAW6o3tHEw`</summary>

```text
1	% ============================================================
2	% Multi-Turn Attention
3	% ============================================================
4	
5	@article{dongre2026attention,
6	  author  = {Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-T\"{u}r, Dilek},
7	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},
8	  journal = {arXiv preprint arXiv:2605.12922},
9	  year    = {2026},
10	  url     = {https://arxiv.org/abs/2605.12922}
11	}
12	
13	@article{hong2025rhea,
14	  author  = {Hong, Wanyang and Zhang, Zhaoning and Chen, Yi and Zhang, Libo and Liu, Baihui and Qiao, Linbo and Tian, Zhiliang and Li, Dongsheng},
15	  title   = {{Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs}},
16	  journal = {arXiv preprint arXiv:2512.06869},
17	  year    = {2025},
18	  url     = {https://arxiv.org/abs/2512.06869}
19	}
20	
21	@article{laban2025lost,
22	  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
23	  title   = {{LLMs Get Lost In Multi-Turn Conversation}},
24	  journal = {arXiv preprint arXiv:2505.06120},
25	  year    = {2025},
26	  url     = {https://arxiv.org/abs/2505.06120}
27	}
28	
29	@article{liu2026intent,
30	  author  = {Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng},
31	  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},
32	  journal = {arXiv preprint arXiv:2602.07338},
33	  year    = {2026},
34	  url     = {https://arxiv.org/abs/2602.07338}
35	}
36	
37	@inproceedings{bai2024mtbench101,
38	  author    = {Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli},
39	  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},
40	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
41	  year      = {2024},
42	  url       = {https://arxiv.org/abs/2402.14762}
43	}
44	
45	% ============================================================
46	% Residual Gating and Adaptive Depth
47	% ============================================================
48	
49	@inproceedings{fan2020layerdrop,
50	  author    = {Fan, Angela and Grave, Edouard and Joulin, Armand},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2426a646-301c-4d81-83c5-5984485be118",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "a60792b8-efeb-4395-897b-e2e2812ca0c5",
  "sourceToolAssistantUUID": "2426a646-301c-4d81-83c5-5984485be118",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-24T09:15:05.861Z_

<details open><summary>🔧 Tool call — Read · `toolu_017RD6YJTjpoRfWHs9UxveTE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a60792b8-efeb-4395-897b-e2e2812ca0c5",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM93y8iH2bSBJGmrBTGC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7de5a1d5-72bd-464e-af1d-c69b72354909",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01An1MXqhTDYbSciQRMamufZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 49615,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 709
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 49615,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 709,
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

_source line 38 · 2026-05-24T09:15:06.435Z_

<details><summary>↩ Tool result · `toolu_017RD6YJTjpoRfWHs9UxveTE`</summary>

```text
PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf (722.2KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7de5a1d5-72bd-464e-af1d-c69b72354909",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "uuid": "a140edd9-6c78-4ba0-9461-371ead5a1441",
  "sourceToolAssistantUUID": "7de5a1d5-72bd-464e-af1d-c69b72354909",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 39 · 2026-05-24T09:15:06.433Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a140edd9-6c78-4ba0-9461-371ead5a1441",
  "isSidechain": true,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "agentId": "a2de08e360b959d80",
  "type": "user",
  "isMeta": true,
  "uuid": "da35bf50-3c72-445e-8d47-98dd2639d368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-24T09:16:49.916Z_



---

## EMNLP 2026 (ARR) Review

**Paper:** "From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives"

---

### 1. Summary

This paper investigates why auxiliary attention losses (specifically, the Goal Accessibility Ratio or GAR) optimized during teacher-forced training fail to transfer to autoregressive generation in multi-turn dialogue. The authors introduce ThreadGate, a per-layer content-and-turn-conditioned gating module on the residual stream, and conduct a five-way controlled comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) on Qwen-2.5-7B and Llama-3.1-8B. All variants converge to TF GAR of 0.50 but collapse 8--27x under AR generation. Through a causal exclusion chain, the authors attribute the failure to exposure bias rather than gradient conflict or architectural limitations. Two mitigations are shown: inference-time attention steering (beta=5, GAR=0.727) and time-scheduled sampling (gap compressed to ~1.3x on Qwen, 3-seed).

---

### 2. Strengths

- **Well-structured causal exclusion methodology.** The five-way comparison is carefully designed so that each adjacent pair isolates one factor. The PCGrad experiment is a genuinely creative use of gradient surgery as a *diagnostic* rather than optimization tool. The modus tollens argument (removing conflict worsens AR GAR, p=0.002, therefore conflict is not the cause) is logically clean and well-executed.

- **Thorough experimental coverage.** The paper systematically addresses the most natural objections: gradient conflict (PCGrad), architecture dependence (Qwen vs. Llama, MHA vs. GQA), lambda sensitivity (Table 5 / Appendix B), metric specificity (four alternative GAR definitions, Appendix Q), general capability preservation (MMLU within 0.8pp), and conversation length scaling (Appendix D/N). The appendix is extensive and well-organized.

- **Clear identification of the exposure bias mechanism.** The argument that NTP self-recovers because prediction is the same task at train and test time, while GAR optimizes a distributional property with no autoregressive counterpart, is a useful conceptual contribution. The mechanism specificity analysis (TRC showing no gap while GAR collapses) and the per-head KL analysis (r=0.743 correlation between TF GAR and AR shift) are convincing supporting evidence.

- **Inference-time steering as a diagnostic.** Using beta-steering to confirm attention misallocation (not representation degradation) as the proximal cause closes the causal loop elegantly. The phase-transition behavior at beta=3 (Figure 1b) is an interesting empirical finding.

- **Honest reporting of partial successes and failures.** The paper is admirably transparent about SS working on Qwen but failing on Llama, about seed sensitivity (CV=9.2% on 3 seeds), and about the length-dependent decay of SS benefits. The loss design evolution (7 iterations, Table in Appendix B) is a useful contribution for practitioners.

- **Strong visual presentation.** Figure 1 is an effective headline figure. The log-scale TF-AR comparison (panel a) and steering recovery curve (panel b) immediately convey the core findings. Figures 3-5 are clean and informative.

---

### 3. Weaknesses

- **(Major) The paper's central finding is arguably unsurprising.** The observation that a teacher-forced auxiliary loss does not transfer to autoregressive generation is a direct prediction from the well-known exposure bias literature (Bengio et al., 2015; Ranzato et al., 2016; Arora et al., 2022). The paper acknowledges this heritage but claims novelty in demonstrating it on *auxiliary attention objectives* in *multi-turn transformers*. While technically true, the conceptual gap from "exposure bias affects sequence generation" to "exposure bias affects auxiliary losses during sequence generation" is modest. The causal exclusion chain, while well-executed, ultimately arrives at a conclusion most readers would predict. An experienced reviewer would ask: what is the actionable insight beyond "teacher forcing does not transfer, as expected"?

- **(Major) Scheduled sampling results are insufficiently robust to constitute a contribution.** SS is presented as the first training-time mitigation, but: (a) it works on Qwen but completely fails on Llama (AR GAR=0.04, gap 11.75x), with no explanation for the discrepancy; (b) 3-seed validation shows CV=9.2%, which the authors frame positively, but this is on a metric (GAR) that has high intrinsic variance; (c) the benefit decays rapidly with conversation length (47.6% at 15 turns, 71.4% at 20 turns per the task summary), making it impractical for the very scenario where multi-turn attention decay matters most; (d) training time variance is extreme (6.5h to 10.8h across seeds). A mitigation that is model-specific, seed-sensitive, and length-limited is difficult to position as a robust contribution.

- **(Major) GAR metric validity and generalizability concerns.** Section 6.3 / Appendix Q reveals that ThreadGate only improves last-token GAR (the definition it optimizes) but not all-token, first-token, or goal-only variants, raising a position-specific overfitting concern. While SS is shown to generalize across definitions, the entire diagnostic apparatus (the 8-27x gap, the failure mode taxonomy) is built on GAR-ours. The paper does not adequately address whether GAR-ours is a meaningful proxy for actual goal-tracking behavior, or whether optimizing it is inherently ill-posed. The downstream instruction retention evaluation (McNemar p=0.077, r=0.200) is marginally significant at best and based on only 18 constraint types -- this does not convincingly establish that GAR improvements matter for practical performance.

- **(Moderate) The failure mode taxonomy (NF1-NF3) has limited explanatory power.** NF1 (reverse turn conditioning) describes the symptom that gates approach 1.0 at late turns rather than providing stronger intervention. NF2 (structural distribution shift) is just "exposure bias" renamed. NF3 (insufficient intervention strength, 2-7%) is a consequence of NF1. These are three descriptions of the same phenomenon (gates are too weak because NTP dominates) rather than three distinct failure modes. The taxonomy does not provide differential diagnostic value -- knowing which "failure mode" applies does not suggest different remedies.

- **(Moderate) Limited model scale and diversity.** Both models are 7-8B parameter instruction-tuned models from the same generation. The 1.5B cross-scale validation (Appendix S) is welcome but only evaluates beta-steering, not the full diagnostic pipeline or SS. No models above 8B are tested. For a paper making general claims about "auxiliary attention losses," testing on two closely-related model families is thin. The single-dataset limitation (UltraChat) further constrains generalizability.

- **(Moderate) The "causal exclusion" framing overstates the strength of the evidence.** Modus tollens requires that removing the proposed cause should prevent the effect. PCGrad addresses gradient *direction* conflict but not magnitude imbalance (acknowledged in Limitations). The paper frames this as "ruling out gradient conflict" but it only rules out *directional* gradient conflict. Furthermore, the worsening under PCGrad (0.064 to 0.030) could reflect PCGrad disrupting beneficial gradient interactions rather than ruling out conflict as a cause. The causal language is stronger than the evidence warrants.

- **(Minor) Inconsistent evaluation protocols across models.** Qwen uses N=50 with mean 3.6 turns; Llama uses N=20 with 4 turns. Qwen reports means; Llama reports medians (due to heavy-tailed distributions). SS is validated with 3 seeds on Qwen but not on Llama (only one Llama SS run is mentioned). These asymmetries make cross-model comparison less rigorous than presented.

- **(Minor) The title and framing have evolved.** The task summary describes the paper as "Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study" (negative result framing), but the actual paper title is "From Collapse to Recovery" (positive framing emphasizing SS and steering). This dual identity creates tension: the diagnostic contribution is modest if SS is the main result, and SS is too fragile to be the main result.

- **(Minor) Abstract exceeds stated norms.** The abstract is dense and contains specific numbers (0.50, 0.002, 0.727, 0.401, etc.) that could be replaced with qualitative descriptions for readability. At ~180 words it is within the 200-word EMNLP limit but pushes against it.

---

### 4. Questions for Authors

1. Can you provide a mechanistic explanation for why SS works on Qwen but completely fails on Llama? Without this, the SS contribution is difficult to assess as principled rather than accidental.

2. The gate diversity loss (L_div) enforces minimum std across gate values. What happens without it? If gates collapse to ~1.0 without diversity pressure, doesn't this suggest the gating mechanism is fighting against the model's preferred computation rather than augmenting it?

3. You report GAR target tau=0.5, allocating "half of the last token's attention capacity to goal tokens." How sensitive are results to tau? Is there a principled way to set tau, or is this arbitrary? Goal tokens may comprise only a small fraction of the sequence; is 50% attention allocation even desirable?

4. The steering experiment shows GAR recovery to 0.727 at beta=5 with PPL 1.77. How does generation quality (not just PPL) change? Are there pathological behaviors at high beta (repetition, incoherence)?

5. For the PCGrad modus tollens argument: could the worsening (0.064 to 0.030) reflect PCGrad removing *beneficial* gradient interactions rather than demonstrating that conflict is not causal? The two interpretations are not distinguished.

6. Why was Llama SS evaluated with only one seed when the Qwen results showed meaningful seed sensitivity?

---

### 5. Missing References or Related Work

- **Dou et al. (2019, 2022) -- Attention Forcing.** Cited in Related Work but the connection could be deeper: attention forcing directly supervises attention distributions during training, which is conceptually closer to GAR than scheduled sampling. Why was this approach not tested?

- **Attention supervision in distillation.** Works like Jiao et al. (2020, TinyBERT) and Wang et al. (2020) supervise attention during knowledge distillation. The relationship between attention supervision during distillation (which does transfer) and attention supervision via auxiliary losses (which does not, per this paper) deserves discussion.

- **Token-level exposure bias mitigation.** Beyond scheduled sampling, methods like Mixer (Goyal et al., 2017) and search-based training (Daume et al., 2009; Leblond et al., 2018) offer different approaches to the same problem. The paper cites Leblond et al. but does not discuss why these alternatives were not tested.

- **Concurrent work on system-prompt grounding.** The multi-turn attention decay problem likely has concurrent work beyond the cited papers; the authors should verify completeness.

---

### 6. Soundness: 3/5

The experimental methodology is generally careful, and the five-way comparison design is sound. However, several issues reduce confidence: (a) the causal exclusion chain overstates what PCGrad can rule out (direction conflict only, not magnitude); (b) the failure mode taxonomy conflates symptoms with causes; (c) cross-model evaluation uses inconsistent protocols; (d) the downstream validation (instruction retention) is underpowered (18 constraints, McNemar p=0.077). The core observation (TF-AR gap exists and is large) is well-established, but the causal attribution to exposure bias, while plausible, is more of an argument by elimination than a positive demonstration.

---

### 7. Excitement: 2/5

The central finding -- that teacher-forced auxiliary losses do not transfer to autoregressive generation -- is predictable from first principles of exposure bias. While the empirical demonstration is thorough, the conceptual advance is incremental. The scheduled sampling mitigation, which could elevate excitement, is undermined by model specificity (Qwen only), seed sensitivity, and length-limited effectiveness. The beta-steering diagnostic is an interesting methodological contribution but is inference-time and not novel in kind (additive attention biases are well-known). The paper will likely be of interest to a narrow audience working specifically on multi-turn attention optimization, but the insights do not generalize broadly enough for main-conference excitement.

---

### 8. Reproducibility: 4/5

The paper provides extensive implementation details: full hyperparameters (Appendix A), loss design evolution (Appendix B), training costs (Appendix J), dataset characteristics (Appendix M), statistical test details (Appendix E), and per-layer gate profiles (Appendix H). The use of specific model versions (Qwen-2.5-7B-Instruct, Llama-3.1-8B-Instruct) and a public dataset (UltraChat) aids reproducibility. The main gap is the SS training time variance (6.5h to 10.8h across seeds on the same GPU), which is unexplained and could indicate implementation sensitivity. Code availability is not discussed.

---

### 9. Overall Assessment: 2.5 (Borderline Findings)

---

### 10. Confidence: 4/5

I am confident in this assessment. I have deep familiarity with exposure bias, multi-task learning, attention mechanisms, and gating architectures. The main uncertainty is whether the community would find more value in the empirical documentation of this specific failure mode than I estimate.

---

### 11. Justification of Overall Assessment

The paper is a thorough empirical study with a well-designed ablation structure, but the central finding (exposure bias prevents TF auxiliary losses from transferring to AR generation) is predictable and the failure mode taxonomy provides limited new insight beyond labeling the known phenomenon. The scheduled sampling mitigation, which could strengthen the contribution, is model-specific (works on Qwen, fails on Llama), seed-sensitive, and degrades with conversation length -- precisely the regime where the problem matters most. The GAR metric specificity issue (position-specific overfitting of ThreadGate, Table in Appendix Q) and underpowered downstream validation (McNemar p=0.077) further weaken the practical significance. The paper falls between a solid Findings paper and one needing another revision cycle: the experimental execution is strong but the conceptual contribution and mitigation robustness are insufficient for main-conference acceptance. A revision incorporating a principled explanation for model-specific SS behavior, broader model/scale testing, and stronger downstream evaluation could elevate this to Findings level.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da35bf50-3c72-445e-8d47-98dd2639d368",
  "isSidechain": true,
  "agentId": "a2de08e360b959d80",
  "requestId": "req_011CbM94FwFvdjGWkCBZiPFq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7d4ab08-5605-4653-82f5-3e49e717a2a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsDnyWzeP4jaWoUAdwpUt2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11346,
      "cache_read_input_tokens": 50324,
      "output_tokens": 3575,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11346
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3575,
          "cache_read_input_tokens": 50324,
          "cache_creation_input_tokens": 11346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11346,
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
