# Research conversation: You are **Reviewer 1 (R1)** for a top ML venue peer review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reje

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8c4b8793c0fc9cf0.jsonl`
- **Structured JSON:** [`44fcb0ad8eaefa039589.json`](../../sessions/44/44fcb0ad8eaefa039589.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-18T18:38:05.857Z_

You are **Reviewer 1 (R1)** for a top ML venue peer review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus: **Methods and Experiments**.

## Paper Summary

**Title**: "What Does KL Distillation Learn for SwiGLU Sparsity Prediction? Mask Pattern Discovery, Causal Decomposition, and Sparsity Regime Analysis"

The paper trains per-token contextual sparsity predictors using KL-divergence distillation for SwiGLU-based LLMs and investigates what KL learns that BCE does not. Four claimed contributions:
1. **Mask pattern discovery**: KL-trained predictors discover neuron importance patterns diverging 53% from magnitude-based masks. Three-seed causal ablation shows mask quality (not gradient coupling) is the primary driver, explaining 82–100%.
2. **Automated oracle discovery**: At 30% sparsity, BCE with magnitude oracles nearly matches KL (PPL 9.15 vs 8.82, Δ=0.33). KL's value is automated oracle discovery.
3. **Sparsity regime characterization**: 6-point sweep (25–50%) reveals continuous quality-sparsity tradeoff with PPL cliff at 40–45% and MMLU cliff at 35–40%.
4. **Conceptual contributions**: Formal loss taxonomy (2D: correction granularity × training signal coupling) and gradient SNR analysis (103× higher for KL).

## Key Experimental Details

**Models**: Llama-3.1-8B (primary), Mistral-7B-v0.3 (cross-arch), Qwen-2.5-14B (cross-scale). Paper only shows Llama-3.1-8B results in main body; cross-arch/cross-scale are mentioned in setup but NO results are presented for Mistral or Qwen.

**Baselines**: TEAL (training-free), BCE (learned, magnitude oracle), BCE+comp (with compensation MLP, FastForward-style), KL (ours).

**Evaluation**: WikiText-2 PPL; downstream (ARC-c, WinoGrande, MMLU, GSM8K); LongBench (14 English tasks); MT-Bench (Appendix A); RULER (Appendix B).

### Table 2 — 30% Operating Point (Llama-3.1-8B)
| Method | Comp. | PPL↓ | ARC-c | WG | MMLU | GSM8K |
|---|---|---|---|---|---|---|
| Dense | – | 7.52 | – | – | – | – |
| TEAL 30% | No | 10.97 | – | – | – | – |
| BCE 30% | No | 9.15 | 40.1 | 66.8 | 37.8 | 6.2 |
| BCE+comp 30% | Yes | – | – | – | – | – |
| KL 30% (ours) | No | **8.82** | **44.3** | **69.2** | **38.5** | – |

NOTE: Table 2 has many missing entries (dashes). Dense has no downstream scores. TEAL has no downstream scores. BCE+comp has ALL entries missing. KL is missing GSM8K.

### Table 3 — Causal Ablation (3 seeds, 50% uniform)
| Seed | PPL BCE+KL-t | PPL KL ref | Δ PPL | Oracle Agree. | ARC-c | WG | MMLU | GSM8K |
|---|---|---|---|---|---|---|---|---|
| s42 | 11.96 | 11.96 | 0.00 | 0.978 | – | – | – | – |
| s123 | 12.71 | 11.86 | 0.85 | 0.921 | 34.5 | 59.8 | 25.3 | 1.5 |
| s456 | 12.55 | 11.95 | 0.60 | 0.943 | 36.2 | 61.2 | 26.8 | 1.9 |
| Mean Δ | | | 0.48 | 0.947 | | | | |
| Std Δ | | | 0.36 | 0.024 | | | | |

NOTE: s42 has all downstream metrics missing. High variance across seeds (Δ ranges 0.00–0.85, std=0.36 is 75% of mean).

### Table 4 — 6-Point Sparsity Sweep (KL, Llama-3.1-8B)
PPL (uniform): 8.90→8.82→8.55→8.36→10.25→11.96 (25%→50%)
Three monotonicity violations (PPL decreasing from 25→40%).
MMLU cliff at 35→40% (41.5→30.7, Δ=10.8pp). PPL cliff at 40→45%.

### Table 5 — LongBench
KL 30% overall: 14.0 (61% of dense 23.0). KL vs BCE+comp gap: 1.1 points. Dense baseline itself is low (23.0).

### Table 6 (Appendix A) — MT-Bench
Dense: 3.8, KL 30%: 2.9, BCE+comp 30%: 2.7. Floor effect, low discriminative power. Most category-level entries are dashes.

### Table 7 (Appendix B) — RULER
KL 30% retention: 80% at 4K, 55% at 16K. Only KL results shown (no BCE/TEAL baselines on RULER).

## Experiment Design Reference (what experiments were planned)

The following experiments were planned but may not be fully reflected in the paper:
1. **C1 ablation replication (3 seeds)** — completed and shown in Table 3, but seed variance undermines "gradient coupling=0" claim
2. **BCE 30% forced top-k** — shown in Table 2, gap is only Δ=0.33 vs KL
3. **Dense sparsity sweep 6pt** — shown in Table 4, but 3 PPL monotonicity violations break discrete regime narrative
4. **LongBench full evaluation** — shown in Table 5, but dense baseline is low (23.0) and KL vs BCE+comp gap compresses to 1.1
5. **MT-Bench** — shown in Appendix A, near-useless due to base model floor effect
6. **RULER** — shown in Appendix B, only KL conditions tested (no baselines), length generalization failure

## Your Review Task

Evaluate the paper's **methodology soundness** and **experimental rigor**. Address:

1. **Method**: Is the loss taxonomy well-motivated? Is the gradient SNR analysis rigorous or hand-wavy? Is the Lagrangian training formulation clearly described with all necessary details (learning rates, architectures, temperature, Gumbel-sigmoid parameters)?
2. **Experimental design**: Are experiments sufficient to support each claim? What key experiments are missing? Are baselines fair and complete?
3. **Statistical rigor**: With 3 seeds showing Δ range [0.00, 0.85] and std=0.36 (75% of mean 0.48), is the causal ablation conclusion credible? Is the single-seed regime sweep reliable?
4. **Missing data**: Many table cells are dashes. Is this acceptable? What critical entries are missing?
5. **Reproducibility**: Are enough training details provided?

Produce a structured review with:
- **Summary** (2-3 sentences)
- **Strengths** (bulleted)
- **Weaknesses** (bulleted, with severity: major/minor)
- **Questions for Authors**
- **Missing Experiments** (what would strengthen or invalidate claims)
- **Score** (1-6) with **Confidence** (1-5)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "0661fa7f-164f-4599-b73b-c822486f52df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T18:38:05.863Z_

```json
{
  "parentUuid": "0661fa7f-164f-4599-b73b-c822486f52df",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
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
  "uuid": "fe3ae3ba-e381-4830-8018-80c83b2b3e6f",
  "timestamp": "2026-05-18T18:38:05.863Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-18T18:38:08.243Z_



I'll start by reading the paper and key project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe3ae3ba-e381-4830-8018-80c83b2b3e6f",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX8ni4jnSy8i55R5u5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76c9240b-7045-4e76-b567-5636dfd7d346",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPMzrZnDj8P2x6SiykyfVR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18288,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18288,
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

_source line 4 · 2026-05-18T18:38:09.161Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011hGYtdzNYf2F4W1RRWJ8uW`</summary>

```json
{
  "pattern": "paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76c9240b-7045-4e76-b567-5636dfd7d346",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX8ni4jnSy8i55R5u5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08422e05-07f3-4522-b743-3f304229a11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPMzrZnDj8P2x6SiykyfVR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18288,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18288,
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

_source line 5 · 2026-05-18T18:38:09.196Z_

<details><summary>↩ Tool result · `toolu_011hGYtdzNYf2F4W1RRWJ8uW`</summary>

```text
paper/main.tex
paper/ethics.tex
paper/related_work.tex
paper/conclusion.tex
paper/method.tex
paper/appendix.tex
paper/limitations.tex
paper/introduction.tex
paper/experiments.tex
paper/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08422e05-07f3-4522-b743-3f304229a11a",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "cc745513-60e4-4f7d-8648-056ef319b22b",
  "sourceToolAssistantUUID": "08422e05-07f3-4522-b743-3f304229a11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T18:38:10.148Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01M7uQm4odV3DN45dGQ5chwb`</summary>

```json
{
  "pattern": "paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc745513-60e4-4f7d-8648-056ef319b22b",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX8ni4jnSy8i55R5u5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abf9a4c9-dc4a-4146-9d31-9cda78e23967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPMzrZnDj8P2x6SiykyfVR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18288,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18288,
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

_source line 7 · 2026-05-18T18:38:10.178Z_

<details><summary>↩ Tool result · `toolu_01M7uQm4odV3DN45dGQ5chwb`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abf9a4c9-dc4a-4146-9d31-9cda78e23967",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "30f153ab-6209-400d-b176-add1a8e49223",
  "sourceToolAssistantUUID": "abf9a4c9-dc4a-4146-9d31-9cda78e23967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T18:38:10.479Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ihSDVLpybZzmYCxwj6Dd8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30f153ab-6209-400d-b176-add1a8e49223",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX8ni4jnSy8i55R5u5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7580cbcf-3c98-4a5a-92c9-072fe80fcee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPMzrZnDj8P2x6SiykyfVR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18288,
      "cache_read_input_tokens": 0,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18288
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 275,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18288,
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

_source line 9 · 2026-05-18T18:38:10.484Z_

<details><summary>↩ Tool result · `toolu_013ihSDVLpybZzmYCxwj6Dd8`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:
5	    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline
6	    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds
7	    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and
8	    BCE-only 3 seeds (mvp_bce_s42/s123/s456).
9	
10	    '
11	  priority: P0
12	  gpu_budget_hours: 48
13	  deps: []
14	  registry_ids:
15	  - mvp_kl_norm_v2_s42
16	  - mvp_kl_norm_v2_s123
17	  - mvp_kl_norm_v2_s456
18	  - mvp_bce_s42
19	  - mvp_bce_s123
20	  - mvp_bce_s456
21	  remaining_runs:
22	  - KL-only 2 additional seeds (s0, s1) for 5-seed headline
23	  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)
24	  - KL+comp 3 seeds (s42, s123, s456)
25	  registry_id: kl_only_s1
26	- id: plan_002
27	  claim: 1
28	  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).
29	    Isolates whether KL advantage comes from loss function or relaxation method. 3
30	    seeds.
31	
32	    '
33	  priority: P0
34	  gpu_budget_hours: 10
35	  deps:
36	  - plan_001
37	  registry_id: ste_baseline_s42
38	- id: plan_003
39	  claim: 1
40	  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs
41	    (KL requires full forward pass for output logits, BCE can use cached targets).
42	    Report per-step FLOPs and total training time for both. 3 seeds.
43	
44	    '
45	  priority: P0
46	  gpu_budget_hours: 10
47	  deps:
48	  - plan_001
49	  registry_id: bce_isocompute_v2_s42
50	- id: plan_004
51	  claim: 2
52	  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL
53	    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,
54	    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.
55	
56	    '
57	  priority: P0
58	  gpu_budget_hours: 8
59	  deps: []
60	  registry_id: spon_2048_s42
61	- id: plan_005
62	  claim: 2
63	  description: 'SPON subsumption verification: output-space linearity test showing
64	    KL predictor already captures SPON correction signal. ||Delta_logits(s+c) - Delta_logits(s)
65	    - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality analysis.
66	    Proves SPON+KL ≈ KL (no additive gain). 3 seeds.
67	
68	    '
69	  priority: P0
70	  gpu_budget_hours: 8
71	  deps:
72	  - plan_001
73	  - plan_004
74	  registry_id: plan_005_subsumption_s42
75	- id: plan_006
76	  claim: 1
77	  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:
78	    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),
79	    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free
80	    < static-learned < contextual-learned.
81	
82	    '
83	  priority: P0
84	  gpu_budget_hours: 6
85	  deps: []
86	  registry_ids:
87	  - training_free_baselines
88	  - training_free_wina_greedy
89	  registry_id: training_free_baselines
90	- id: plan_007
91	  claim:
92	  - 1
93	  - 2
94	  - 3
95	  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2
96	    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor
97	    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto
98	    frontier plot.
99	
100	    '
101	  priority: P0
102	  gpu_budget_hours: 24
103	  deps:
104	  - plan_001
105	  - plan_004
106	  - plan_005
107	  - plan_006
108	  registry_id: bench_dense
109	- id: plan_008
110	  claim: 3
111	  description: '3-level sparsity sweep (30%/50%/70%): KL-only vs BCE-only. Test scaling
112	    trend and KL-BCE delta growth. 1 seed per level (sweep analysis, not headline).
113	    50% data point reused from plan_001. If 3 levels show non-linear inflection, add
114	    intermediate points.
115	
116	    '
117	  priority: P1
118	  gpu_budget_hours: 12
119	  deps:
120	  - plan_001
121	  registry_id: d030_kl50_uniform
122	- id: plan_009
123	  claim: 1
124	  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%
125	    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds
126	    each condition.
127	
128	    '
129	  priority: P1
130	  gpu_budget_hours: 24
131	  deps:
132	  - plan_001
133	  registry_id: lm_eval_mistral_dense
134	- id: plan_010
135	  claim:
136	  - 1
137	  - 2
138	  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions
139	    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:
140	    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization
141	    beyond short training sequences.
142	
143	    '
144	  priority: P1
145	  gpu_budget_hours: 16
146	  deps:
147	  - plan_001
148	  - plan_005
149	- id: plan_011
150	  claim:
151	  - 1
152	  - 2
153	  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8
154	    categories. All conditions. Tests instruction-following quality under sparsity.
155	
156	    '
157	  priority: P2
158	  gpu_budget_hours: 4
159	  deps:
160	  - plan_001
161	  - plan_005
162	- id: plan_012
163	  claim: 3
164	  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative
165	    task types. Fine-grained capability diagnostics complementing LongBench.
166	
167	    '
168	  priority: P2
169	  gpu_budget_hours: 8
170	  deps:
171	  - plan_010
172	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7580cbcf-3c98-4a5a-92c9-072fe80fcee3",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "123b99ad-c3c1-42c3-b733-0eeed1b92b57",
  "sourceToolAssistantUUID": "7580cbcf-3c98-4a5a-92c9-072fe80fcee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T18:38:13.317Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CWmEA7No9uBwHrT5rpBGPA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "123b99ad-c3c1-42c3-b733-0eeed1b92b57",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX98gr9YwZMkKwk9BTz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e64cd2c-8770-4a69-a372-19d35b50dd3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XM7VG7mjJUHJfSgP6cNP7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 18288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3503,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 11 · 2026-05-18T18:38:13.327Z_

<details><summary>↩ Tool result · `toolu_01CWmEA7No9uBwHrT5rpBGPA`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e64cd2c-8770-4a69-a372-19d35b50dd3f",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "2fb3832b-c31c-48ab-9ebb-2537ddee271e",
  "sourceToolAssistantUUID": "5e64cd2c-8770-4a69-a372-19d35b50dd3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T18:38:13.758Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DRFXPi7yh9tXzNJrmvSWPb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fb3832b-c31c-48ab-9ebb-2537ddee271e",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX98gr9YwZMkKwk9BTz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f77a7276-333a-4bbe-bf1e-d29116213102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XM7VG7mjJUHJfSgP6cNP7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 18288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3503,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 13 · 2026-05-18T18:38:13.763Z_

<details><summary>↩ Tool result · `toolu_01DRFXPi7yh9tXzNJrmvSWPb`</summary>

```text
1	We show that KL-trained sparsity predictors for SwiGLU LLMs discover neuron importance patterns that diverge 53\% from magnitude-based masks (per-layer Jaccard 47\%).
2	A causal ablation confirms that these mask patterns, not gradient coupling, drive quality: under controlled 50\% evaluation, BCE trained on KL-derived targets exactly matches KL across perplexity and all four downstream tasks (max $\Delta$=0.79pp), while magnitude-trained BCE achieves 28.13$\pm$0.20.
3	The resulting predictor ($<$1\% of base parameters), trained with forward KL and Gumbel-Sigmoid relaxation on LLaMA-3.1-8B, renders post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
4	At 30\%, KL reduces PPL degradation 18\% over TEAL; uniform allocation provides $7.5\times$ smaller cross-seed downstream $\sigma$.
5	At 50\%, the PPL advantage widens to 49\% but downstream tasks collapse to near-random regardless of allocation.
6	Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though at 14B, MMLU falls 8pp below TEAL (63.7\% vs.\ 71.8\%), a scale-dependent gap not resolved by allocation strategy.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f77a7276-333a-4bbe-bf1e-d29116213102",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "6cdbc78a-e387-4e8a-8220-02e7c3d429e7",
  "sourceToolAssistantUUID": "f77a7276-333a-4bbe-bf1e-d29116213102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T18:38:14.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HrSvyJTo74v8xygcez1heq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cdbc78a-e387-4e8a-8220-02e7c3d429e7",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX98gr9YwZMkKwk9BTz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18be2f9f-a0a0-43a4-95d7-35e0ff94d9be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XM7VG7mjJUHJfSgP6cNP7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 18288,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3503
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 18288,
          "cache_creation_input_tokens": 3503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3503,
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

_source line 15 · 2026-05-18T18:38:14.051Z_

<details><summary>↩ Tool result · `toolu_01HrSvyJTo74v8xygcez1heq`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26	At inference, the scores are fed to a global top-$k$ allocation mechanism~\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\rho) \times L \times d_{\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\rho$.
27	
28	
29	\subsection{Predictor Architecture}
30	\label{sec:method:predictor}
31	
32	Each layer $\ell$ has an independent two-layer MLP predictor:
33	\begin{align}
34	f_\theta^{(\ell)}(\mathbf{h}) = \text{GELU}(\mathbf{h} \mathbf{W}_1^{(\ell)}) \, \mathbf{W}_2^{(\ell)},
35	\label{eq:predictor}
36	\end{align}
37	where $\mathbf{W}_1^{(\ell)} \in \mathbb{R}^{d \times d_b}$ and $\mathbf{W}_2^{(\ell)} \in \mathbb{R}^{d_b \times d_{\text{ff}}}$ with bottleneck dimension $d_b{=}128$.
38	The predictor takes the hidden state after attention (before the FFN) and outputs $d_{\text{ff}}$-dimensional logits $\mathbf{s}^{(\ell)}$, from which the mask is derived.
39	
40	Each predictor has $(4096 \times 128) + (128 \times 14336) = 2.37\text{M}$ parameters.
41	With 32 independent predictors (one per layer), the total overhead is 75.9M parameters, less than 1\% of the 8B base model.
42	The predictors operate independently across layers, requiring no cross-layer communication at inference.
43	
44	
45	\subsection{Gumbel-Sigmoid Relaxation}
46	\label{sec:method:gumbel}
47	
48	The hard mask $m_j = \mathbf{1}[s_j > \text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.
49	We apply Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} to produce differentiable soft masks:
50	\begin{align}
51	\tilde{m}_j = \sigma_\tau\!\left(\log \frac{s_j}{1 - s_j} + g_1 - g_2\right), \quad g_1, g_2 \sim \text{Gumbel}(0,1),
52	\label{eq:gumbel}
53	\end{align}
54	where $\sigma_\tau(x) = \text{sigmoid}(x / \tau)$ and $\tau$ is a temperature parameter.
55	The Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\tau \to 0$, $\tilde{m}_j$ approaches a binary decision.
56	
57	We anneal $\tau$ linearly from 1.0 to 0.1 over training.
58	At high temperature, the soft mask permits gradient flow through all neurons for broad exploration.
59	As temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.
60	
61	\paragraph{Comparison with Straight-Through Estimation.}
62	The straight-through estimator (STE)~\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\partial m / \partial s = 1$).
63	In our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the penalty weight and failure to converge to the target sparsity.
64	Gumbel relaxation eliminates this pathology, contributing a 34.5\% improvement (PPL 15.77 $\to$ 11.79 at 50\% sparsity), as we verify empirically in \S\ref{sec:experiments}.
65	
66	
67	\subsection{KL Divergence Training Objective}
68	\label{sec:method:kl}
69	
70	Let $\mathbf{z}_{\text{dense}}$ denote the output logits from a full dense forward pass, and $\mathbf{z}_{\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\{\tilde{\mathbf{m}}^{(\ell)}\}_\ell$ applied at every layer.
71	We minimize the forward KL divergence between the dense and sparse output distributions:
72	\begin{align}
73	\mathcal{L}_{\text{KL}} = D_{\text{KL}}(p_{\text{dense}} \,\|\, p_{\text{sparse}}) = \sum_{v} p_{\text{dense}}^{(v)} \log \frac{p_{\text{dense}}^{(v)}}{p_{\text{sparse}}^{(v)}},
74	\label{eq:kl_loss}
75	\end{align}
76	where $p_{\text{dense}} = \text{softmax}(\mathbf{z}_{\text{dense}})$ and $p_{\text{sparse}} = \text{softmax}(\mathbf{z}_{\text{sparse}})$, summed over the vocabulary $v$ and averaged over sequence positions.
77	The base model is frozen; only the predictor parameters receive gradients.
78	
79	We use forward KL (mean-seeking) rather than reverse KL, as the goal is to preserve the dense model's primary predictions rather than explore alternative modes; \S\ref{sec:experiments} validates this choice with ablations over divergence direction (forward KL outperforms JSD by 6.4\% and reverse KL by 8.6\%).
80	No temperature scaling ($T{=}1$) is applied~\cite{hinton2015distilling}.
81	
82	
83	\subsection{Adaptive Penalty Sparsity Controller}
84	\label{sec:method:lagrangian}
85	
86	We enforce a model-level sparsity target $\rho$ via constrained optimization.
87	Let $\bar{s} = \frac{1}{L} \sum_\ell \frac{1}{d_{\text{ff}}} \sum_j \tilde{m}_j^{(\ell)}$ denote the average fraction of retained neurons.
88	The constrained problem is:
89	\begin{align}
90	\min_\theta \; \mathcal{L}_{\text{KL}} \quad \text{s.t.} \quad \bar{s} \leq 1 - \rho.
91	\label{eq:constrained}
92	\end{align}
93	We relax this via an adaptive penalty controller:
94	\begin{align}
95	\mathcal{L} = \mathcal{L}_{\text{KL}} + \lambda \cdot \text{clamp}(|\bar{s} - (1 - \rho)| - \epsilon, \min{=}0)^2,
96	\label{eq:lagrangian}
97	\end{align}
98	where $\epsilon = 0.02$ is a deadzone margin that prevents $\lambda$ from responding to small constraint violations.
99	The penalty weight $\lambda$ is updated multiplicatively at each step:
100	\begin{align}
101	\lambda \leftarrow \begin{cases} \lambda \times 2 & \text{if } \bar{s} > (1-\rho) + \epsilon \\ \lambda \times 0.5 & \text{if } \bar{s} < (1-\rho) - \epsilon \\ \lambda & \text{otherwise} \end{cases}
102	\label{eq:dual_update}
103	\end{align}
104	with $\lambda$ clamped to $[\lambda_{\text{floor}}, \lambda_{\max}]$ where $\lambda_{\text{floor}} = 0.01$ and $\lambda_{\max} \in \{1000, 5000\}$ depending on the target.
105	The geometric doubling requires only $\lambda_{\max}$ as a user-specified hyperparameter (no step-size tuning) and reaches target sparsity within 40--110 steps for 40--50\% targets; for 30\% and 70\% targets, $\lambda$ saturates at $\lambda_{\max}$ with 1.7--5.0\% residual deviation (Appendix~\ref{app:lagrangian}, Figure~\ref{fig:lagrangian_dynamics}). The deadzone prevents oscillation once sparsity is within $\pm$2\%.\footnote{Our update rule resembles the augmented Lagrangian method but replaces gradient-based dual updates with a multiplicative schedule for training stability. We term it an adaptive penalty controller to distinguish from formal dual methods that guarantee KKT satisfaction.}
106	
107	
108	\subsection{Gradient-Based Motivation: BCE vs.\ KL}
109	\label{sec:method:gradient}
110	
111	We analyze the structural difference between BCE and KL training signals to build intuition for why KL distillation may be better suited to global top-$k$ inference. The analysis is suggestive; \S\ref{sec:mask_analysis} provides causal confirmation that mask target quality, not gradient coupling, drives the advantage.
112	
113	\paragraph{BCE gradient structure.}
114	The standard approach trains the predictor against oracle masks $m_j^* = \mathbf{1}[|g_j| \geq \text{top-}k\text{ threshold}]$ derived from the dense model's activation magnitudes, where the threshold is the global top-$k$ cutoff across all layers (matching TEAL's inference protocol).
115	The loss decomposes per neuron:
116	\begin{align}
117	\mathcal{L}_{\text{BCE}} = -\frac{1}{d_{\text{ff}}} \sum_{j=1}^{d_{\text{ff}}} \bigl[ m_j^* \log \sigma(s_j) + (1 - m_j^*) \log(1 - \sigma(s_j)) \bigr].
118	\label{eq:bce}
119	\end{align}
120	The gradient with respect to predictor logit $s_j$ is:
121	\begin{align}
122	\frac{\partial \mathcal{L}_{\text{BCE}}}{\partial s_j} = \sigma(s_j) - m_j^*.
123	\label{eq:bce_grad}
124	\end{align}
125	This gradient depends \emph{only} on neuron $j$'s own prediction and target.
126	Each neuron is trained independently; there is no inter-neuron coupling in the learning signal.
127	
128	\paragraph{KL gradient structure.}
129	Under KL distillation, the gradient for predictor logit $s_j^{(\ell)}$ in layer $\ell$ is:
130	\begin{align}
131	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \underbrace{\frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}_{\text{sparse}}}}_{\text{(a)}} \cdot \underbrace{\frac{\partial \mathbf{z}_{\text{sparse}}}{\partial \mathbf{h}^{(\ell)}}}_{\text{(b)}} \cdot \underbrace{\frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}}}_{\text{(c)}} \cdot \underbrace{\frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}}}_{\text{(d)}},
132	\label{eq:kl_grad}
133	\end{align}
134	where each factor has a distinct role:
135	\begin{itemize}
136	\item[\textbf{(a)}] The KL gradient at the output, reflecting how each logit component deviates from the dense distribution.
137	\item[\textbf{(b)}] The Jacobian through all downstream layers from layer $\ell$'s output to the final logits. This factor couples neuron $j$'s gradient to the state of every other retained neuron in layers $\ell, \ell{+}1, \ldots, L$, because the sparse hidden state propagates through subsequent attention and FFN operations.
138	\item[\textbf{(c)}] The local mask effect: $\partial \mathbf{h}^{(\ell)} / \partial \tilde{m}_j^{(\ell)} = (g_j^{(\ell)} \cdot [\mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}]_j) \cdot \mathbf{W}_{d,j}^{(\ell)}$, projecting through the down-projection to affect the full $d$-dimensional hidden state.
139	\item[\textbf{(d)}] The Gumbel-Sigmoid derivative: the differentiable path from logit to mask.
140	\end{itemize}
141	
142	\paragraph{The structural mismatch.}
143	The key observation is that factor (b) makes the KL gradient for neuron $j$ depend on \emph{all} other neurons' mask values.
144	BCE's factorized gradient (Eq.~\ref{eq:bce_grad}) optimizes each neuron's prediction accuracy in isolation, but TEAL inference selects neurons via a global ranking across all layers.
145	Under global top-$k$, the decision to retain neuron $j$ depends on the scores of all other neurons, a combinatorial interaction that BCE cannot capture.
146	
147	Concretely, BCE achieves high per-neuron accuracy ($>$90\% oracle agreement) yet produces poor output under TEAL, because it optimizes a proxy misaligned with output preservation under global budget allocation.
148	KL directly optimizes the end-to-end objective, with gradients that reflect inter-neuron dependencies through the computation graph.
149	
150	\paragraph{Empirical verification.}
151	Measuring gradient SNR\footnote{$\text{SNR}_\ell = \|\mathbb{E}[\nabla_{\theta_\ell} \mathcal{L}]\|_2^2 / \text{Var}[\nabla_{\theta_\ell} \mathcal{L}]$, expectation over mini-batches.} over 7 checkpoints (steps 0--300) on LLaMA-3.1-8B (C4 data) with 95\% bootstrap CI, KL achieves $5.14\times$ higher SNR than BCE at convergence ($5.877{\times}10^{-3}$ vs.\ $1.144{\times}10^{-3}$ at step 300), concentrated in early layers where factor~(b)'s Jacobian traverses the full remaining network; late layers show reduced advantage.
152	The trajectory is non-monotonic: BCE SNR exceeds KL during mid-training (steps 100--250) before KL's advantage emerges at convergence, consistent with KL's gradient coupling becoming effective only after the predictor learns a coarse mask structure (Appendix~\ref{app:snr_extended}).
153	
154	\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}
155	\label{sec:method:taxonomy}
156	
157	We organize prior work along two axes that capture the essential design decisions for sparsity prediction: \emph{correction granularity} (how the mask adapts to input) and \emph{training signal coupling} (whether the objective captures inter-neuron dependencies). These axes are motivated by our gradient analysis (\S\ref{sec:method:gradient}): granularity determines what information the predictor conditions on, while coupling determines whether the training signal reflects global allocation effects.
158	
159	\begin{table}[t]
160	\centering
161	\caption{Taxonomy of learned sparsity prediction methods along correction granularity (rows) and training signal coupling (columns). Our method fills the previously unexplored Per-token $\times$ Coupled cell.}
162	\label{tab:taxonomy}
163	\resizebox{\columnwidth}{!}{
164	\begin{tabular}{lccc}
165	\toprule
166	 & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\
167	\midrule
168	Static & --- & --- & SPON \\
169	Per-token & DejaVu, FastForward & ShadowLLM, D2DMoE & \textbf{Ours} \\
170	\bottomrule
171	\end{tabular}}
172	\end{table}
173	
174	\paragraph{Correction granularity.}
175	\emph{Static} methods~\cite{xu2026spon} learn a fixed bias vector per layer that does not depend on the input token.
176	\emph{Per-token} methods~\cite{liu2023dejavu,gautam2026fastforward,akhauri2024shadowllm,szatkowski2024d2dmoe} produce a unique mask for each input position, conditioning on the token's hidden state at each layer.
177	
178	\paragraph{Training signal coupling.}
179	\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.
180	\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.
181	\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass, reflecting how all mask decisions jointly affect the final distribution.
182	
183	SPON~\cite{xu2026spon} distills a per-layer bias via KL but cannot adapt to per-input neuron importance (static $\times$ coupled).
184	DejaVu~\cite{liu2023dejavu} and FastForward~\cite{gautam2026fastforward} achieve per-token granularity but use BCE, losing inter-neuron coupling: their decomposed gradient (Eq.~\ref{eq:bce_grad}) is blind to cross-neuron interactions under global allocation.
185	D2DMoE~\cite{szatkowski2024d2dmoe} provides intermediate coupling (MSE on hidden states) but not end-to-end output effects.
186	Our method combines per-token prediction with coupled KL training (Table~\ref{tab:taxonomy}), propagating gradients through all downstream layers.
187	
188	\begin{figure}[t]
189	\centering
190	\includegraphics[width=\columnwidth]{fig1_overview.pdf}
191	\caption{Method overview: a lightweight per-layer predictor produces importance scores trained via KL divergence with Gumbel-Sigmoid relaxation. At inference, scores feed TEAL's global top-$k$ allocation without compensation networks.}
192	\label{fig:overview}
193	\end{figure}
194	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18be2f9f-a0a0-43a4-95d7-35e0ff94d9be",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "b99dffc5-c747-4014-a3d5-7c4417f859a8",
  "sourceToolAssistantUUID": "18be2f9f-a0a0-43a4-95d7-35e0ff94d9be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T18:38:18.430Z_

<details open><summary>🔧 Tool call — Read · `toolu_013hVF3SYZQ6Zt6mKT1ed1k1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b99dffc5-c747-4014-a3d5-7c4417f859a8",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX9PyMdPTRa9W9kqo9q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb8115f8-a7c0-427d-9183-eb257ea222cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ueaGs6d8hZTyCe5zJfin6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6815,
      "cache_read_input_tokens": 21791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6815,
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

_source line 17 · 2026-05-18T18:38:18.452Z_

<details><summary>↩ Tool result · `toolu_013hVF3SYZQ6Zt6mKT1ed1k1`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\S\ref{sec:scaling}).
28	At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\pm$0.02 (3-seed) and reduces TEAL's degradation from dense (10.97 $\to$ 8.96, an 18\% improvement). % exp_id: kl30_3seed_global
29	The advantage holds across additional downstream benchmarks (Appendix~\ref{app:downstream}).
30	Uniform allocation at 30\% provides stable downstream performance (MMLU 40.7$\pm$1.3\%, 3-seed) while global top-$k$ exhibits high seed variance (35.7$\pm$9.5\%), with late-layer starvation (L31 retention 28.4\%) interacting with predictor initialization (\S\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_3seed
31	
32	At 50\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\ 23.31, a 49\% reduction. % exp_id: bench_kl50_global, bench_teal50
33	The predictor generalizes to C4 validation at both 30\% (PPL 16.03$\pm$0.01, 2-seed) and 50\% (52.5\% over TEAL; Appendix~\ref{app:ood}).
34	However, all methods exhibit downstream collapse on MMLU (28.1$\pm$0.2\% vs.\ 28.0$\pm$0.6\%, both $\approx$ random, 3-seed) and GSM8K ($<$2.2\%); this is a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform, multi_seed_kl50_global
35	
36	\begin{table}[t]
37	\centering
38	\caption{Main results on LLaMA-3.1-8B. PPL$\downarrow$ on WikiText-2; accuracy$\uparrow$ on downstream tasks. \textbf{Bold}: best among compensation-free methods per sparsity level. BCE follows the DejaVu~\cite{liu2023dejavu} predictor pipeline (per-neuron BCE on magnitude oracles) with a FastForward-style~\cite{gautam2026fastforward} compensation network (67.2M params) applied post-masking; no TEAL allocation. Entries with $\pm$ report 3-seed mean$\pm$std ($s \in \{42, 123, 456\}$); 50\% uniform PPL is 3-seed ($11.92 \pm 0.07$; Appendix~\ref{app:stability}); remaining entries use seed 42.}
39	\label{tab:main}
40	\resizebox{\columnwidth}{!}{
41	\begin{tabular}{llccccc}
42	\toprule
43	Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
44	\midrule
45	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
46	\midrule
47	\multirow{3}{*}{30\%}
48	& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
49	& KL global (Ours) & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5 & \textbf{8.0$\pm$0.7} \\ % exp_id: kl30_3seed_global
50	& KL uniform & \textbf{8.82$\pm$0.02} & 43.7$\pm$2.5 & 68.9$\pm$0.4 & \textbf{40.7$\pm$1.3} & 7.5$\pm$0.1 \\ % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform
51	\midrule
52	\multirow{4}{*}{50\%}
53	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
54	& KL global (Ours) & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 28.1$\pm$0.2 & 1.29 \\ % exp_id: multi_seed_kl50_global
55	& KL uniform & 11.92$\pm$0.07 & 32.76 & 62.90 & 28.0$\pm$0.6 & \textbf{2.12} \\ % exp_id: multi_seed_kl50_uniform
56	& BCE (2700 steps)$^\ast$ & 28.13$\pm$0.20 & 27.6$\pm$0.6 & 51.8$\pm$0.6 & 26.1$\pm$0.5 & 2.1$\pm$0.2 \\ % exp_id: bce50_3seed
57	\bottomrule
58	\end{tabular}}
59	\end{table}
60	
61	
62	\subsection{Extended Training Analysis}
63	\label{sec:isocompute}
64	
65	To test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\times$ the KL step budget, approximately equal wall-clock time: $\sim$46 min BCE vs.\ $\sim$45 min KL on RTX PRO 6000).
66	The BCE predictor achieves PPL 28.13$\pm$0.20 (3-seed), still 2.39$\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce50_3seed
67	The difference is systematic, not due to architectural or compute limitations: both predictors use identical architectures and TEAL allocation, yet BCE achieves +7pp oracle F1 (0.613 vs.\ 0.540) with 139\% worse PPL (28.13 vs.\ 11.79). KL's near-random precision (0.51) is consistent with learning a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42
68	Coupled training correlates with better output preservation; the causal ablation in \S\ref{sec:mask_analysis} confirms that target quality, not gradient coupling, is the primary driver.
69	
70	
71	\subsection{Mask Pattern Analysis}
72	\label{sec:mask_analysis}
73	
74	To understand \emph{what} the KL predictor learns, we compare KL-derived masks against magnitude-based oracle masks (the BCE training targets) at 50\% sparsity on WikiText-2.
75	Per-layer Jaccard similarity between the two mask types averages 47\% across 32 layers: the KL predictor discovers a neuron importance ranking that diverges 53\% from activation magnitude.
76	Despite this divergence, KL achieves PPL 11.79 vs.\ BCE's 28.13$\pm$0.20, confirming that output-distribution fidelity, not magnitude agreement, determines mask quality under global allocation. % exp_id: bench_kl50_global, bce50_3seed, c1_mask_overlap
77	
78	\paragraph{Causal Ablation: Target Quality vs.\ Gradient Coupling.}
79	To disentangle whether KL's advantage stems from its coupled gradient pathway or from the mask patterns it discovers, we train a standard BCE predictor on KL-derived oracle masks instead of magnitude-based masks.
80	Under controlled evaluation (TEAL 50\% uniform allocation at matched sparsity), BCE trained on KL targets matches the KL predictor within statistical noise across all five metrics (PPL 11.96 vs.\ 11.96; ARC-c 32.17 vs.\ 32.59; WinoGrande 63.14 vs.\ 62.35; MMLU 27.79 vs.\ 27.92; GSM8K 2.05 vs.\ 1.97; max $\Delta$=0.79pp). % exp_id: c1_bce_kl_targets_teal50u, c1_kl_teal50u
81	Standard BCE on magnitude masks yields PPL 28.13$\pm$0.20 (3-seed, Table~\ref{tab:main}), $2.4\times$ worse.
82	Target quality, not gradient coupling, is the sole driver of KL's advantage; the coupled gradient is a means to discover better targets, not an independent source of quality. % exp_id: bce50_3seed
83	
84	Since BCE on KL targets matches KL across all metrics, one might consider a two-stage pipeline (train KL, extract oracle masks, retrain with BCE).
85	This offers no practical advantage: the final BCE predictor equals the KL predictor while adding an extra training phase; the KL predictor already produces contextual per-input masks directly.
86	
87	
88	\subsection{Ablation Studies}
89	
90	Table~\ref{tab:ablation} isolates the contribution of each design choice at 50\% sparsity.
91	
92	\begin{table}[t]
93	\centering
94	\caption{Ablation at 50\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$, unified benchmark protocol).}
95	\label{tab:ablation}
96	\small
97	\begin{tabular}{lcc}
98	\toprule
99	Configuration & PPL$\downarrow$ & $\Delta$ from Ours \\
100	\midrule
101	\multicolumn{3}{l}{\textit{KL-based variants}} \\
102	Forward KL + Gumbel (Ours) & \textbf{11.79} & --- \\ % exp_id: bench_kl50_global
103	JSD (symmetric) + Gumbel & 12.54 & +0.75 \\ % exp_id: jsd_ablation_s42
104	Reverse KL + Gumbel & 12.80 & +1.01 \\ % exp_id: reverse_kl_ablation_s42
105	Forward KL + STE & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
106	\midrule
107	\multicolumn{3}{l}{\textit{BCE-based variants}} \\
108	BCE + Compensation (hard mask) & 25.44 & +13.65 \\ % exp_id: bce_comp_staged_s42
109	BCE (no compensation) & 27.97 & +16.18 \\ % exp_id: eval_bce_v3_s42
110	BCE + Gumbel + Penalty (no KL) & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	\paragraph{Gumbel vs.\ STE.}
116	Replacing Gumbel-Sigmoid with STE~\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98), accounting for 34.5\% of the improvement over vanilla TEAL. % exp_id: ste_baseline_s42
117	
118	\paragraph{Divergence Direction.}
119	Forward KL (mode-covering) outperforms JSD (+6.4\%) and reverse KL (+8.6\%), consistent with the SNR analysis in \S\ref{sec:method:gradient}: complete teacher supervision is associated with better global allocation quality. % exp_id: jsd_ablation_s42, reverse_kl_ablation_s42
120	This contrasts with MiniLLM~\cite{gu2024minillm} (reverse KL for generation); in mask prediction, mode-covering ensures no important neuron is omitted.
121	
122	\paragraph{SPON Contribution.}
123	Adding SPON~\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\% relative); see \S\ref{sec:spon} for decomposition.\footnote{SPON analysis uses \texttt{evaluate.py}; main results use the unified benchmark.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42
124	
125	\paragraph{Loss Function Isolation.}
126	BCE with identical Gumbel-Sigmoid and penalty yields PPL 38.02, worse than vanilla BCE (27.97): the penalty interferes with per-neuron optimization without global coordination. % exp_id: bce_gumbel_lagrangian_isolation
127	The loss effect ($\Delta$PPL=26.23) is $6.6\times$ the relaxation effect ($\Delta$PPL=3.98).
128	
129	\paragraph{Compensation Redundancy.}
130	Adding compensation~\cite{gautam2026fastforward} (+67.2M params) to KL provides no benefit at either tested sparsity: at 50\%, all five metrics are identical to KL-only; at 30\%, PPL 8.97$\pm$0.01 vs.\ 8.96$\pm$0.03 (2-seed). BCE requires compensation (27.97$\to$25.44), yet remains $2.16\times$ worse than KL without it. Training converges by step 700 (Appendix~\ref{app:comp_convergence}). % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42, bce_comp_staged_s42
131	
132	\paragraph{Hyperparameter Robustness.}
133	Appendix~\ref{app:db_sensitivity} confirms robustness to predictor capacity ($d_b$, $<$3\%), temperature ($<$1.8\%), and training steps (saturated by 800). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep
134	
135	
136	\subsection{Sparsity Scaling and Regime Analysis}
137	\label{sec:scaling}
138	
139	Table~\ref{tab:scaling} and Figure~\ref{fig:sparsity_sweep} show PPL as a function of sparsity for the KL predictor under global allocation and vanilla TEAL.
140	
141	\begin{figure}[t]
142	\centering
143	\includegraphics[width=\columnwidth]{fig2_sparsity_sweep.pdf}
144	\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}
145	\label{fig:sparsity_sweep}
146	\end{figure}
147	
148	\begin{table}[t]
149	\centering
150	\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows disproportionately with sparsity.}
151	\label{tab:scaling}
152	\small
153	\begin{tabular}{lccc}
154	\toprule
155	Sparsity & KL (Ours) & TEAL vanilla & Relative advantage \\
156	\midrule
157	30\% & \textbf{8.96} & 10.97 & 18\% \\ % exp_id: kl30_3seed_global
158	50\% & \textbf{11.79} & 23.31 & 49\% \\ % exp_id: bench_kl50_global
159	70\% & \textbf{17.91} & 100.11 & 82\% \\ % exp_id: kl_70_global_teal
160	\bottomrule
161	\end{tabular}
162	\end{table}
163	
164	The KL advantage grows from 18\% at 30\% to 82\% at 70\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.
165	In absolute terms, KL/Dense degradation is $1.47\times$ at 30\%, $1.93\times$ at 50\%, and $2.93\times$ at 70\%, compared to TEAL/Dense ratios of $1.79\times$, $3.81\times$, and $16.4\times$ respectively.
166	
167	\paragraph{Allocation Behavior Across Sparsity Levels.}
168	Table~\ref{tab:phase} presents global vs.\ uniform allocation at three sparsity levels and reveals qualitative shifts in allocation preference. Denser sampling (e.g., 35\% sparsity) would be needed to precisely locate region boundaries.
169	
170	\begin{table}[t]
171	\centering
172	\caption{Allocation analysis: global (TEAL) vs.\ uniform per-layer allocation across sparsity levels. Entries with $\pm$ report 3-seed mean$\pm$std; remaining entries use seed 42. Each row uses a predictor trained at the respective sparsity target.}
173	\label{tab:phase}
174	\resizebox{\columnwidth}{!}{
175	\begin{tabular}{llccccc}
176	\toprule
177	Sparsity & Allocation & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
178	\midrule
179	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
180	\midrule
181	\multirow{3}{*}{30\%}
182	& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
183	& KL global & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5 & \textbf{8.0$\pm$0.7} \\ % exp_id: kl30_3seed_global
184	& KL uniform & \textbf{8.82$\pm$0.02} & 43.7$\pm$2.5 & 68.9$\pm$0.4 & \textbf{40.7$\pm$1.3} & 7.5$\pm$0.1 \\ % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform
185	\midrule
186	\multirow{2}{*}{40\%}
187	& KL global & 10.12 & 40.96 & 65.35 & \textbf{38.06} & \textbf{5.00} \\ % exp_id: bench_kl40_global
188	& KL uniform & \textbf{8.36} & \textbf{41.81} & \textbf{67.17} & 30.68 & 3.94 \\ % exp_id: d030_kl40_uniform
189	\midrule
190	\multirow{3}{*}{50\%}
191	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
192	& KL global & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 28.1$\pm$0.2 & 1.29 \\ % exp_id: multi_seed_kl50_global
193	& KL uniform & 11.92$\pm$0.07 & 32.76 & 62.90 & 28.0$\pm$0.6 & \textbf{2.12} \\ % exp_id: multi_seed_kl50_uniform
194	\bottomrule
195	\end{tabular}}
196	\end{table}
197	
198	The allocation preference appears \emph{non-monotonic} across the sampled sparsity levels (7--8B scale). We observe distinct qualitative behaviors:
199	
200	\noindent\textbf{Budget-surplus ($\leq$30\%).}
201	Uniform allocation provides $7.5\times$ smaller cross-seed MMLU $\sigma$ (1.3pp vs.\ 9.5pp), eliminating catastrophic seed-dependent degradation under global top-$k$ (MMLU 35.7$\pm$9.5\% vs.\ 40.7$\pm$1.3\%, 3-seed); the instability is allocation-induced, not from the distillation objective (PPL cross-seed CV $<$ 0.3\%; Appendix~\ref{app:lagrangian}). % exp_id: kl30_3seed
202	
203	\noindent\textbf{Budget-constrained ($\sim$40\%).}
204	The preference reverses: global achieves MMLU 38.06\% vs.\ uniform's 30.68\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform
205	PPL remains low (8.36) but downstream accuracy degrades; PPL is a poor proxy for reasoning.
206	
207	\noindent\textbf{Capacity-limited ($\geq$50\%).}
208	Global/uniform gap vanishes (MMLU 28.1$\pm$0.2\% vs.\ 28.0$\pm$0.6\%, $\sigma\leq$0.6pp; contrast 9.5pp at 30\%), consistent with capacity limitation. % exp_id: multi_seed_kl50_global, multi_seed_kl50_uniform
209	Late-layer starvation persists across levels (Figure~\ref{fig:retention}; Appendix~\ref{app:db_sensitivity}).
210	
211	
212	\paragraph{SPON Orthogonality.}
213	\label{sec:spon}
214	SPON~\cite{xu2026spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\% PPL improvement; the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
215	
216	\paragraph{Cross-Architecture Validation.}
217	\label{sec:cross_arch}
218	On Mistral-7B-v0.3~\cite{jiang2023mistral}, the KL advantage ratio is consistent with LLaMA-8B (within 8\% at $\leq$50\% sparsity; Appendix~\ref{app:cross_arch}).
219	
220	\paragraph{Scale Generalization: Qwen-2.5-14B.}
221	\phantomsection\label{sec:14b}
222	On Qwen-2.5-14B~\cite{qwen2024qwen25} at 30\%, KL's PPL advantage generalizes ($1.47\times$ dense, Table~\ref{tab:14b} in Appendix~\ref{app:14b}), but MMLU falls below TEAL (63.7 vs.\ 71.8\%), suggesting higher knowledge density causes KL's output-preservation objective to sacrifice task-specific pathways; uniform allocation recovers only +0.8pp. % exp_id: qwen14b_kl30_s42, qwen14b_teal30_eval, qwen14b_kl30_uniform
223	
224	\paragraph{Inference Efficiency.}
225	The pipeline adds 6.4\% overhead while removing the compensation network ($-$2.7\% latency, $-$67.2M params; Appendix~\ref{app:latency}).
226	
227	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb8115f8-a7c0-427d-9183-eb257ea222cf",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "a6b82502-1ee4-4684-9a4f-d27349f0a3f4",
  "sourceToolAssistantUUID": "cb8115f8-a7c0-427d-9183-eb257ea222cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T18:38:18.644Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EYe67mwtArufabVpsHoyQh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6b82502-1ee4-4684-9a4f-d27349f0a3f4",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX9PyMdPTRa9W9kqo9q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6988d585-51a1-4606-b96a-caabc8095db3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ueaGs6d8hZTyCe5zJfin6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6815,
      "cache_read_input_tokens": 21791,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6815
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 21791,
          "cache_creation_input_tokens": 6815,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6815,
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

_source line 19 · 2026-05-18T18:38:18.660Z_

<details><summary>↩ Tool result · `toolu_01EYe67mwtArufabVpsHoyQh`</summary>

```text
1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
9	This suggests KL should outperform BCE under global allocation.
10	The empirical picture, however, reveals something more fundamental: KL-trained predictors discover neuron importance patterns that diverge 53\% from magnitude-based masks (per-layer Jaccard 47\%), and a causal ablation confirms that these learned mask patterns, not gradient coupling, are the primary quality driver.
11	Under controlled 50\% evaluation, BCE trained on KL-derived targets exactly matches KL across perplexity and all downstream tasks ($\Delta$$<$1pp), while magnitude-trained BCE achieves 28.13$\pm$0.20.
12	
13	We instantiate a lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} on LLaMA-3.1-8B~\cite{grattafiori2024llama3}.
14	With uniform allocation, the predictor achieves PPL 11.92 at 50\% sparsity (3-seed); under global top-$k$, PPL improves to 11.79 (49\% over TEAL).
15	At the recommended 30\% operating point, global top-$k$ amplifies cross-seed downstream standard deviation ($7.5\times$), motivating uniform allocation for deployment.
16	Evaluation on Mistral-7B-v0.3~\cite{jiang2023mistral} and Qwen-2.5-14B~\cite{qwen2024qwen25} confirms the PPL advantage at 7--14B, though 14B exhibits an MMLU gap (63.7\% vs.\ TEAL's 71.8\%) not resolved by allocation strategy.
17	Our contribution targets prediction quality and inference simplification; wall-clock speedup requires sparse kernel support not addressed here (Appendix~\ref{app:latency}).
18	
19	Our contributions are:
20	\begin{itemize}[nosep,leftmargin=*]
21	\item KL-trained predictors discover neuron importance patterns diverging 53\% from magnitude-based masks. A causal ablation proves that mask target quality, not gradient coupling, determines quality under global allocation (\S\ref{sec:mask_analysis}).
22	\item These superior mask patterns render post-hoc compensation (+67.2M params) redundant at both tested sparsity levels, yielding a simpler inference pipeline (\S\ref{sec:isocompute}).
23	\item Analysis of allocation-to-downstream interactions at 7--14B: non-monotonic allocation preference at 8B and scale-dependent effects at 14B (\S\ref{sec:scaling}).
24	\end{itemize}
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6988d585-51a1-4606-b96a-caabc8095db3",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "bcf93c39-7854-4e19-863a-60a7d220f207",
  "sourceToolAssistantUUID": "6988d585-51a1-4606-b96a-caabc8095db3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T18:38:22.614Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cpg8HyyHjQy5824ionZ3Vp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcf93c39-7854-4e19-863a-60a7d220f207",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX9japRserEMDPmRM3R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e03507e-43b8-4c94-9c39-a8a7b62dadd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxYq2neCHRNBot1xsuWgzJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8358,
      "cache_read_input_tokens": 28606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8358,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 21 · 2026-05-18T18:38:22.628Z_

<details><summary>↩ Tool result · `toolu_01Cpg8HyyHjQy5824ionZ3Vp`</summary>

```text
1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.
34	Our contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.
35	
36	
37	\section{Predictor Bottleneck Sensitivity}
38	\label{app:db_sensitivity}
39	
40	Table~\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.
41	
42	\begin{table}[h]
43	\centering
44	\caption{Predictor bottleneck sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}
45	\label{tab:db_sensitivity}
46	\small
47	\begin{tabular}{lcccc}
48	\toprule
49	$d_b$ & Params & TEAL global & $\Delta$ & Per-token \\
50	\midrule
51	64 & 38.2M (0.48\%) & 12.076 & +0.9\% & 10.16 \\ % exp_id: db_sensitivity_sweep
52	128 & 75.9M (0.95\%) & 11.963 & --- & 9.218 \\ % exp_id: db_sensitivity_sweep
53	256 & 151.5M (1.89\%) & 12.105 & +1.2\% & 8.586 \\ % exp_id: db_sensitivity_sweep
54	512 & 302.5M (3.77\%) & 12.315 & +2.9\% & 7.93 \\ % exp_id: db_sensitivity_sweep
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	Under TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\to$7.93).
60	This divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.
61	The $d_b{=}128$ configuration (75.9M params, $<$1\% of base model) is therefore optimal for the TEAL inference protocol.
62	
63	\subsection{Temperature Schedule Sensitivity}
64	\label{app:tau_sensitivity}
65	
66	\begin{table}[h]
67	\centering
68	\caption{Temperature schedule sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
69	\label{tab:tau_sensitivity}
70	\small
71	\begin{tabular}{lc}
72	\toprule
73	$\tau$ Schedule & PPL$\downarrow$ \\
74	\midrule
75	Fixed $\tau{=}0.5$ & \textbf{11.861} \\ % exp_id: tau_schedule_sweep
76	Linear $1.0 \to 0.1$ (default) & 11.963 \\ % exp_id: tau_schedule_sweep
77	Fixed $\tau{=}0.1$ & 12.072 \\ % exp_id: tau_schedule_sweep
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	Temperature schedule has minimal impact ($<$1.8\% PPL variation).
83	The linear annealing default is a conservative choice; even removing annealing entirely (fixed $\tau{=}0.5$) yields comparable performance.
84	
85	\subsection{Training Convergence}
86	\label{app:training_convergence}
87	
88	\begin{table}[h]
89	\centering
90	\caption{Training convergence at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
91	\label{tab:training_convergence}
92	\small
93	\begin{tabular}{cc}
94	\toprule
95	Steps & PPL$\downarrow$ \\
96	\midrule
97	200 & 15.158 \\ % exp_id: training_steps_sweep
98	400 & 12.538 \\ % exp_id: training_steps_sweep
99	600 & 12.046 \\ % exp_id: training_steps_sweep
100	800 & 11.907 \\ % exp_id: training_steps_sweep
101	1000 & \textbf{11.906} \\ % exp_id: training_steps_sweep
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	Training converges rapidly: 95\% of the quality gap closes by step 600, and performance saturates by step 800 ($\Delta < 0.001$ between 800 and 1000 steps).
107	Our default of 1000 steps provides a conservative margin.
108	
109	
110	\section{Adaptive Penalty Controller Dynamics}
111	\label{app:lagrangian}
112	
113	Table~\ref{tab:lagrangian} reports the convergence of the adaptive penalty controller across sparsity targets.
114	The geometric doubling pattern ($1 \to 2 \to 4 \to 8 \to \ldots$) enables $\lambda$ to reach steady state within $\sim$10 steps; the deadzone ($\epsilon = 0.02$) then stabilizes $\lambda$ once actual sparsity is within $\pm$2\% of the target.
115	
116	\begin{table}[h]
117	\centering
118	\caption{Penalty controller convergence across sparsity targets (multiplicative schedule, margin $\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}
119	\label{tab:lagrangian}
120	\small
121	\begin{tabular}{lccccc}
122	\toprule
123	Target $\rho$ & $\lambda_{\max}$ & Final $\lambda$ & Actual sparsity & Deviation \\
124	\midrule
125	30\% & 5000 & 5000 (cap) & 0.285 & 5.0\% \\ % exp_id: kl_30pct_s42
126	40\% & 5000 & 625 & 0.398 & 0.5\% \\ % exp_id: kl_40pct_s42
127	50\% & 1000 & 8 & 0.504 & 0.8\% \\ % exp_id: kl_50pct_s42
128	70\% & 1000 & 1000 (cap) & 0.688 & 1.7\% \\ % exp_id: kl_70pct_s42
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	At 50\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.
134	At 30\% and 70\%, the gap between the gate prior and target is larger, driving $\lambda$ to its respective caps.
135	The 40\% target converges to $\lambda = 625$ with only 0.5\% deviation; this precision reflects a regime where the target is reachable without $\lambda$ saturation.
136	
137	\begin{figure}[h]
138	\centering
139	\includegraphics[width=\columnwidth]{lagrangian_dynamics.pdf}
140	\caption{Adaptive penalty controller convergence across sparsity targets. Upper panel: penalty weight $\lambda$ (log scale) over training steps. The 30\% target requires extreme penalty ($\lambda \to 5000$) to suppress activations below their natural density, while 50\% needs only $\lambda \approx 8$ since SwiGLU gates already cluster near this sparsity. Lower panel: actual sparsity (solid) converges to the target (dashed) within $\sim$10 steps via geometric doubling.}
141	\label{fig:lagrangian_dynamics}
142	\end{figure}
143	
144	Temperature $\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.
145	A mild loss increase in the final $\sim$100 steps is expected: as masks become more binary ($\tau \to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.
146	
147	The controller reliably drives actual sparsity to within 5\% of the target across all tested regimes, with $\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.
148	For the recommended 30\% operating point, actual sparsity is $\approx$28.5\% (5\% deviation). This does not affect conclusions: TEAL at interpolated 28.5\% actual sparsity yields PPL$\approx$10.7 (vs.\ 10.97 at exact 30\%), a $<$0.3 PPL difference negligible relative to the KL vs.\ TEAL gap (8.96 vs.\ 10.97).
149	
150	
151	\section{Out-of-Distribution Evaluation}
152	\label{app:ood}
153	
154	To address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\cite{raffel2020c4} validation set under TEAL global allocation.
155	
156	\begin{table}[h]
157	\centering
158	\caption{Out-of-distribution evaluation on C4 validation (PPL$\downarrow$). 30\% KL reports 2-seed mean$\pm$std; other entries use seed 42.}
159	\label{tab:ood}
160	\small
161	\begin{tabular}{llc}
162	\toprule
163	Sparsity & Method & C4 PPL$\downarrow$ \\
164	\midrule
165	0\% & Dense & 9.21 \\
166	\midrule
167	30\% & KL predictor (Ours) & \textbf{16.03$\pm$0.01} \\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123
168	\midrule
169	\multirow{2}{*}{50\%} & KL predictor (Ours) & \textbf{18.40} \\ % exp_id: eval_c4_ood_kl50
170	& TEAL vanilla & 38.75 \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	At the recommended 30\% operating point, the KL predictor achieves C4 PPL 16.03$\pm$0.01 (2-seed, $1.74\times$ dense), confirming OOD generalization at the deployment-relevant sparsity level.
176	At 50\%, the KL predictor achieves 52.5\% relative advantage over TEAL (18.40 vs.\ 38.75), comparable to the 49\% advantage on WikiText-2 (11.79 vs.\ 23.31), confirming that KL-trained predictions generalize across distributions.
177	
178	
179	\section{Per-Layer Retention Analysis}
180	\label{app:retention}
181	
182	\begin{figure}[h]
183	\centering
184	\includegraphics[width=\columnwidth]{per_layer_retention_chart.pdf}
185	\caption{Per-layer neuron retention under global top-$k$ allocation at 30\%, 50\%, and 70\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\% (L31) even at 30\% sparsity. At 70\%, starvation extends to mid-layers (L10--12: 16.7--20.1\%), explaining the transition to the capacity-limited regime.}
186	\label{fig:retention}
187	\end{figure}
188	
189	
190	\section{Training Stability}
191	\label{app:stability}
192	
193	Three-seed evaluation ($s \in \{42, 123, 456\}$) at 50\% sparsity under uniform allocation yields PPL $11.92 \pm 0.07$ (CV=0.6\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform
194	Downstream metrics are similarly stable: ARC-c $33.8 \pm 1.2$\%, WinoGrande $62.9 \pm 0.1$\%, MMLU $28.0 \pm 0.6$\%, GSM8K $2.2 \pm 0.1$\%.
195	
196	Under global allocation at 50\%, MMLU is equally stable: $28.1 \pm 0.2$\% (s42=27.89, s123=28.34, s456=27.94); the near-random performance is therefore capacity-limited rather than seed-sensitive ($\sigma$=0.2pp vs.\ 9.5pp at 30\% global). % exp_id: multi_seed_kl50_global
197	The low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.
198	
199	
200	\section{Extended SNR Analysis}
201	\label{app:snr_extended}
202	
203	We measure per-layer gradient SNR at 7 checkpoints (steps 0, 50, 100, 150, 200, 250, 300) with 95\% bootstrap confidence intervals.
204	The SNR trajectory is non-monotonic: KL starts with higher SNR at step 0, but BCE surpasses KL during mid-training (steps 100--250) as its per-neuron classification objective concentrates gradients on the remaining hard neurons. KL's advantage re-emerges in later training and reaches $5.14\times$ at convergence (step 300: $5.877{\times}10^{-3}$ vs.\ $1.144{\times}10^{-3}$). % exp_id: snr_extended_r6w3
205	This reversal is consistent with KL's gradient coupling becoming effective only after the predictor has learned a coarse mask structure: early training explores broadly (lower SNR), while convergence concentrates signal through the inter-neuron Jacobian pathway (\S\ref{sec:method:gradient}).
206	
207	
208	\section{Extended Downstream Evaluation}
209	\label{app:downstream}
210	
211	Table~\ref{tab:downstream} compares Dense, KL 30\% (uniform allocation), and TEAL 30\% on three additional downstream benchmarks not included in the main results.
212	
213	\begin{table}[h]
214	\centering
215	\caption{Extended downstream benchmarks at 30\% sparsity (LLaMA-3.1-8B, seed 42). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc; BoolQ: 0-shot acc.}
216	\label{tab:downstream}
217	\small
218	\begin{tabular}{lccc}
219	\toprule
220	Method & HellaSwag & PIQA & BoolQ \\
221	\midrule
222	Dense & \textbf{82.33} & \textbf{80.74} & \textbf{82.94} \\
223	KL 30\% uniform & 72.70 & 75.95 & 76.85 \\ % exp_id: downstream_extended_kl30_s42
224	TEAL 30\% vanilla & 66.70 & 73.61 & 68.50 \\ % exp_id: downstream_teal30_baseline
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	The KL predictor outperforms TEAL on all three benchmarks. On HellaSwag, it preserves 88.3\% of dense accuracy (72.70 vs.\ 82.33) vs.\ 81.0\% for TEAL (66.70). BoolQ shows the largest gap: 92.7\% vs.\ 82.6\% preservation. PIQA shows a smaller differential (94.1\% vs.\ 91.2\%).
230	
231	
232	\section{Compensation Training Convergence}
233	\label{app:comp_convergence}
234	
235	All compensation networks~\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\% s42 (final loss 0.70), 30\% s456 (0.68), 50\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42
236	
237	
238	\section{Qwen-2.5-14B Detailed Results}
239	\label{app:14b}
240	
241	\begin{table}[h]
242	\centering
243	\caption{Qwen-2.5-14B at 30\% sparsity. \textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\% native sparsity (\S\ref{sec:method:gradient}), so forced global top-$k$ is used.}
244	\label{tab:14b}
245	\small
246	\begin{tabular}{lccccc}
247	\toprule
248	Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
249	\midrule
250	Dense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 \\
251	\midrule
252	\multicolumn{6}{l}{\emph{Global top-$k$ allocation}} \\
253	KL (Ours) & \textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 \\ % exp_id: qwen14b_kl30_s42
254	TEAL & 8.73 & 56.83 & \textbf{72.69} & \textbf{71.83} & 49.51 \\ % exp_id: qwen14b_teal30_eval
255	BCE & 8.76 & \textbf{57.59} & 72.61 & 71.67 & \textbf{53.07} \\ % exp_id: qwen14b_bce30_s42_eval
256	\midrule
257	\multicolumn{6}{l}{\emph{Uniform allocation}} \\
258	KL (Ours) & \textbf{7.63} & 54.44 & \textbf{72.45} & 64.49 & --- \\ % exp_id: qwen14b_kl30_uniform
259	TEAL & 8.01 & \textbf{55.29} & 69.85 & \textbf{66.34} & --- \\ % exp_id: qwen14b_teal30_uniform
260	\bottomrule
261	\end{tabular}
262	\end{table}
263	
264	
265	\section{Cross-Architecture Comparison}
266	\label{app:cross_arch}
267	
268	Table~\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).
269	
270	\begin{table}[h]
271	\centering
272	\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL\,/\,KL ratio. LLaMA uses global top-$k$; Mistral uses uniform allocation (matched within each architecture).}
273	\label{tab:cross_arch}
274	\small
275	\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}
276	\toprule
277	 & \multicolumn{3}{c}{Mistral-7B} & \multicolumn{3}{c}{LLaMA-8B} \\
278	 & KL & TEAL & Adv & KL & TEAL & Adv \\
279	\midrule
280	30\% & \textbf{6.77} & 8.38 & 1.24$\times$ & \textbf{8.96} & 10.97 & 1.22$\times$ \\ % exp_id: kl_30_mistral, teal_30_mistral, kl30_3seed_global
281	50\% & \textbf{8.65} & 18.31 & 2.12$\times$ & \textbf{11.79} & 23.31 & 1.98$\times$ \\ % exp_id: kl_50_mistral, teal_50_mistral
282	70\% & \textbf{13.33} & 61.72 & 4.63$\times$ & \textbf{17.91} & 100.11 & 5.59$\times$ \\ % exp_id: kl_70_mistral, teal_70_mistral
283	\bottomrule
284	\end{tabular}
285	\end{table}
286	
287	The KL advantage ratio is consistent across architectures (within 8\% at $\leq$50\% sparsity), confirming that the benefit of output-distribution coupling is not architecture-specific.
288	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e03507e-43b8-4c94-9c39-a8a7b62dadd2",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "8fc09bb3-1ea7-4aea-8e23-ea4bb4d0c8b4",
  "sourceToolAssistantUUID": "0e03507e-43b8-4c94-9c39-a8a7b62dadd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T18:38:23.606Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MmRpAPb63sRSgf24zJuYx6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fc09bb3-1ea7-4aea-8e23-ea4bb4d0c8b4",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX9japRserEMDPmRM3R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fd1514b-3f83-4699-9573-9f85a449e7c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxYq2neCHRNBot1xsuWgzJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8358,
      "cache_read_input_tokens": 28606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8358,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 23 · 2026-05-18T18:38:23.614Z_

<details><summary>↩ Tool result · `toolu_01MmRpAPb63sRSgf24zJuYx6`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
13	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
14	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
15	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint.
16	The structural mismatch we characterize (per-neuron gradient decomposition vs.\ global top-$k$) does not arise in MaskLLM's per-group categorical setting, where N:M patterns eliminate cross-group budget competition.
17	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
18	Our contribution is primarily empirical: we observe that a coupled KL objective propagates gradients through all downstream layers and quantify when this matters for global allocation quality.
19	
20	\paragraph{Static Bias Correction.}
21	SPON~\cite{xu2026spon} learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.
22	Our method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers, producing input-dependent masks.
23	SPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are weakly correlated (cosine similarity 0.196, $R^2$=0.038; \S\ref{sec:experiments}).
24	
25	\paragraph{Activation Function Engineering.}
26	ReLU Strikes Back~\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\% natural sparsity; TurboSparse~\cite{song2024turbosparse} and ProSparse~\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.
27	MiniTron~\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.
28	All require retraining or weight modification; our method is a plug-in predictor on \emph{unmodified} SwiGLU models.
29	
30	\paragraph{Weight Pruning, Distillation, and Routing.}
31	Wanda~\cite{sun2024wanda} and SparseGPT~\cite{frantar2023sparsegpt} produce static weight masks; Switch Transformers~\cite{fedus2022switch} and Mixture-of-Depths~\cite{raposo2024mod} achieve conditional computation through learned routing.
32	KL-based distillation~\cite{kim2016sequencekd,sanh2019distilbert,gu2024minillm,agarwal2024gkd} trains compact students; SparseLoRA~\cite{khaki2025sparselora} exploits contextual sparsity for fine-tuning.
33	We apply the KL principle to train a sparsity predictor on unmodified dense models, using Gumbel-Sigmoid sampling~\cite{maddison2017concrete,louizos2018l0} for differentiable discrete mask optimization.
34	
35	\paragraph{MoE Routing and Gated Sparsity.}
36	Expert Choice routing~\cite{zhou2022expertchoice} lets each expert select its top-$k$ tokens under a fixed capacity budget, a global allocation perspective that parallels TEAL's neuron-level global top-$k$.
37	D2D-MoE~\cite{szatkowski2024d2dmoe} converts dense SwiGLU layers into dynamic-$k$ MoE by exploiting the same activation sparsity we target, but restructures the network into discrete experts rather than predicting masks on the original architecture.
38	Gated architectures beyond SwiGLU (e.g., Griffin's RG-LRU~\cite{de2024griffin}) produce analogous structured sparsity through their gating mechanisms, suggesting that output-distribution prediction may generalize beyond standard Transformer FFNs.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fd1514b-3f83-4699-9573-9f85a449e7c0",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "f59c4a81-352d-4dca-ad30-8db26e08fe1e",
  "sourceToolAssistantUUID": "5fd1514b-3f83-4699-9573-9f85a449e7c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T18:38:23.816Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CMwKszAj2zZ3zJh9TzREps`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f59c4a81-352d-4dca-ad30-8db26e08fe1e",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAX9japRserEMDPmRM3R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a1fa1a4-3a60-4d66-a148-33ce0dc6091f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxYq2neCHRNBot1xsuWgzJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8358,
      "cache_read_input_tokens": 28606,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8358
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 28606,
          "cache_creation_input_tokens": 8358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8358,
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

_source line 25 · 2026-05-18T18:38:23.826Z_

<details><summary>↩ Tool result · `toolu_01CMwKszAj2zZ3zJh9TzREps`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-4pt}
4	
5	KL distillation discovers neuron importance patterns that diverge 53\% from magnitude-based masks; a causal ablation confirms target quality, not gradient coupling, as the primary driver.
6	A predictor ($<$1\% of base) halves TEAL's perplexity across 7--14B, rendering compensation (+67.2M params) redundant.
7	At 30\%, uniform allocation delivers $7.5\times$ smaller cross-seed $\sigma$; at 14B, the PPL advantage persists but an MMLU gap emerges, warranting further investigation.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a1fa1a4-3a60-4d66-a148-33ce0dc6091f",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "1dec3f9c-4744-4eb6-8903-3cb3967152c8",
  "sourceToolAssistantUUID": "5a1fa1a4-3a60-4d66-a148-33ce0dc6091f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T18:38:27.839Z_

<details open><summary>🔧 Tool call — Read · `toolu_018ysDyjHKSmVMZp3hdurb3p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dec3f9c-4744-4eb6-8903-3cb3967152c8",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAXA7sWbLmYrcJ4vXQdt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46fe729d-6685-405a-8610-118154f3628c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BCCbTctGhyFRcPPqL2ixVN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8680,
      "cache_read_input_tokens": 36964,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 36964,
          "cache_creation_input_tokens": 8680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8680,
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

_source line 27 · 2026-05-18T18:38:27.844Z_

<details><summary>↩ Tool result · `toolu_018ysDyjHKSmVMZp3hdurb3p`</summary>

```text
1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	Our recommended operating point (30\% sparsity, uniform allocation) is validated at 7--8B scale; at 14B, the MMLU gap persists regardless of allocation strategy (\S\ref{sec:14b}). Scaling to 70B remains untested.
6	Out-of-distribution evaluation (Appendix~\ref{app:ood}) covers 30\% and 50\% sparsity on C4; extending to 70\% is left to future work.
7	The causal ablation (\S\ref{sec:mask_analysis}) confirms that mask target quality, not gradient coupling, is the primary driver of KL's advantage. However, the mechanism by which KL's coupled gradient discovers superior mask patterns during training remains incompletely characterized; future work could trace per-layer mask divergence trajectories across training to identify when and where the patterns diverge.
8	At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable performance across seeds under both allocation strategies.
9	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
10	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46fe729d-6685-405a-8610-118154f3628c",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "c20398db-cf48-4079-a27f-a82db74c707c",
  "sourceToolAssistantUUID": "46fe729d-6685-405a-8610-118154f3628c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-18T18:38:30.910Z_

Now let me check the actual paper framing and key results more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c20398db-cf48-4079-a27f-a82db74c707c",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAXAQsiPnuKvydZDXJLe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "068af488-35b6-46be-a3f2-54c2c08618c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FxPKdzFcYak75cNzDkffz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 45644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 645,
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

_source line 29 · 2026-05-18T18:38:31.392Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FGRCVHwLBM1DmddbfjmBfv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "068af488-35b6-46be-a3f2-54c2c08618c8",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAXAQsiPnuKvydZDXJLe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c81d69fc-f36e-4ae6-a468-a08b7f0ef3a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FxPKdzFcYak75cNzDkffz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 45644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 645,
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

_source line 30 · 2026-05-18T18:38:31.397Z_

<details><summary>↩ Tool result · `toolu_01FGRCVHwLBM1DmddbfjmBfv`</summary>

```text
1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText and C4 are publicly available research datasets. Our use is consistent with their intended purposes.
21	\item[\textbf{B3.}] N/A. We do not release new artifacts in this submission.
22	\item[\textbf{B4.}] N/A. No personally identifiable information or offensive content is involved.
23	\item[\textbf{B5.}] N/A. No new datasets created.
24	\item[\textbf{B6.}] N/A. No crowdsourced data.
25	\end{itemize}
26	
27	\paragraph{C. Computational Experiments.}
28	\begin{itemize}[nosep,leftmargin=*]
29	\item[\textbf{C1.}] Yes. Model sizes (8B base, 75.9M predictor), training compute (1000 steps, batch 4, seq 2048), optimizer (AdamW~\cite{loshchilov2019adamw}, lr=$10^{-3}$, cosine decay), and GPU (NVIDIA RTX PRO 6000 Blackwell for both training and latency measurement) are reported in \S4.1 and Appendix A.
30	\item[\textbf{C2.}] Yes. Hyperparameters are fully specified: bottleneck $d_b{=}128$, temperature schedule $\tau: 1.0 \to 0.1$, sparsity penalty parameters ($\epsilon{=}0.02$, $\lambda_{\max}$), weight decay $5{\times}10^{-2}$.
31	\item[\textbf{C3.}] Yes. Three-seed evaluation reported (PPL std=0.07, CV$<$1\%; Appendix E).
32	\item[\textbf{C4.}] Yes. All evaluation uses established metrics (perplexity, accuracy) on standard benchmarks with standard few-shot protocols (ARC 25-shot, WinoGrande 5-shot, MMLU 5-shot, GSM8K 8-shot).
33	\end{itemize}
34	
35	\paragraph{D. Human Subjects.}
36	\begin{itemize}[nosep,leftmargin=*]
37	\item[\textbf{D1--D5.}] N/A. No human subjects, crowdsourcing, or annotation involved.
38	\end{itemize}
39	
40	\paragraph{E. AI Assistants.}
41	\begin{itemize}[nosep,leftmargin=*]
42	\item[\textbf{E1.}] AI writing assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were produced and verified by the authors.
43	\end{itemize}
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c81d69fc-f36e-4ae6-a468-a08b7f0ef3a3",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "90ca15c0-cc64-4cc9-9b30-e5f56c8443f0",
  "sourceToolAssistantUUID": "c81d69fc-f36e-4ae6-a468-a08b7f0ef3a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T18:38:31.674Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GEFNnt2yEw4p3kr84V5Jwa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90ca15c0-cc64-4cc9-9b30-e5f56c8443f0",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAXAQsiPnuKvydZDXJLe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bac8b7a2-38fe-495b-8a34-4e607cac9367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FxPKdzFcYak75cNzDkffz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 45644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 645,
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

_source line 32 · 2026-05-18T18:38:31.680Z_

<details><summary>↩ Tool result · reported error · `toolu_01GEFNnt2yEw4p3kr84V5Jwa`</summary>

```text
EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/results'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bac8b7a2-38fe-495b-8a34-4e607cac9367",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "585eab48-fcf7-4534-b721-b94b7d862c1e",
  "toolUseResult": "Error: EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/results'",
  "sourceToolAssistantUUID": "bac8b7a2-38fe-495b-8a34-4e607cac9367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T18:38:34.820Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WZECDD9E5x6t56KXkRb4JC`</summary>

```json
{
  "pattern": "results/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "585eab48-fcf7-4534-b721-b94b7d862c1e",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAXAhf1ssejki1KVr9eL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61c1d37f-da51-48df-9f48-5afd914120f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgfdR1ZKKjVPTGCHewV2QX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1596,
      "cache_read_input_tokens": 46289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1596,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
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

_source line 34 · 2026-05-18T18:38:34.859Z_

<details><summary>↩ Tool result · `toolu_01WZECDD9E5x6t56KXkRb4JC`</summary>

```text
results/wallclock_profile.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61c1d37f-da51-48df-9f48-5afd914120f9",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "5bbf2296-e41a-40f6-acf3-2f11d1ec4995",
  "sourceToolAssistantUUID": "61c1d37f-da51-48df-9f48-5afd914120f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T18:38:35.456Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017T2VJS46RCbHbBU8Pebrvx`</summary>

```json
{
  "pattern": "src/**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bbf2296-e41a-40f6-acf3-2f11d1ec4995",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAXAhf1ssejki1KVr9eL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "852b5b20-31c5-472f-97d5-98a7a9202103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgfdR1ZKKjVPTGCHewV2QX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1596,
      "cache_read_input_tokens": 46289,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1596
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 46289,
          "cache_creation_input_tokens": 1596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1596,
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

_source line 36 · 2026-05-18T18:38:35.485Z_

<details><summary>↩ Tool result · `toolu_017T2VJS46RCbHbBU8Pebrvx`</summary>

```text
src/generate_kl_oracle_masks.py
src/train_bce_kl_targets.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "852b5b20-31c5-472f-97d5-98a7a9202103",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "ed43aea1-b269-4b45-9b86-7c5aebebfd1a",
  "sourceToolAssistantUUID": "852b5b20-31c5-472f-97d5-98a7a9202103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T18:38:39.789Z_

<details open><summary>🔧 Tool call — Read · `toolu_014N9stLWvz2afHXRAusggLJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/registry.yaml",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed43aea1-b269-4b45-9b86-7c5aebebfd1a",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAXAyn85M6rMtDsRPqAG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "442532b6-df69-4c39-9a11-e01d9360e6b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnjrNZyaqFgX1dgr68ivN5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 280,
      "cache_read_input_tokens": 47885,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 280
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 47885,
          "cache_creation_input_tokens": 280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 280,
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

_source line 38 · 2026-05-18T18:38:39.795Z_

<details><summary>↩ Tool result · `toolu_014N9stLWvz2afHXRAusggLJ`</summary>

```text
1	baseline: bench_dense
2	experiments:
3	  mvp_kl_s42:
4	    status: DONE
5	    retry_count: 2
6	    created_at: '2026-05-15T11:50:59.003Z'
7	    updated_at: '2026-05-17T02:59:05.828Z'
8	    server: westd-34887
9	    gpu: cuda:0
10	    account: root
11	    reproduce:
12	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
13	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
14	        --loss_type kl --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
15	        42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42
16	        --wandb_run_name mvp_kl_s42 --dataset wikitext-103"
17	      finished_at: '2026-05-15T13:14:04.493Z'
18	    failure_reason: 'CUDA OOM: CUDA out of memory. Tried to allocate 1.96 GiB. GPU
19	      0 has a total capacity of 94.97 GiB of which 1.88 GiB is free. Including non-PyTorch
20	      memory, this process has 93.08 GiB memory in use. Of the allocated memory 88.41
21	      GiB is allocated by PyTorch, and '
22	    completed_at: '2026-05-15T11:58:28.834Z'
23	    extra:
24	      hook_events:
25	      - event: on_failed
26	        action: agent
27	        ts: '2026-05-15T11:58:29.490811+00:00'
28	      - event: on_failed
29	        action: agent
30	        ts: '2026-05-15T12:10:37.036636+00:00'
31	      - event: on_complete
32	        action: agent
33	        ts: '2026-05-15T13:14:05.191408+00:00'
34	      previous_failure:
35	        conclusion: failed
36	        notes: '诊断中 | fix_worker_id: worker_diagnose_mvp_kl_s42_20260515T115944 |
37	          两个 seed-42 实验同时 ~15s 崩溃，疑似同一根因'
38	    notes: 'NEGATIVE: 稀疏性坍塌。Sparsity 0.328→0.000 (step 500+ 全 0)。根因: KL loss (收敛 3.3)
39	      远大于 reg (0.05)，66 倍差距，fixed reg_weight=0.1 完全压不住。KL 最优解是 sparse=dense (0% sparsity)。修复:
40	      Lagrangian multiplier 自适应约束（Director 批准）。'
41	    conclusion: negative
42	    spec:
43	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
44	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
45	        --loss_type kl --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
46	        42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42
47	        --wandb_run_name mvp_kl_s42 --dataset wikitext-103"
48	      server: westd-34887
49	      gpu:
50	      - cuda:0
51	      pid: '53754'
52	      log_path: ~/runs/distill_sparse_swiglu/mvp_kl_s42.log
53	      submitted_at: '2026-05-15T12:37:15.045Z'
54	      submitted_via: submit_training_job
55	      backend: tmux
56	      account: root
57	      wall_clock_seconds: 2424.9
58	      gpu_hours: 0.67
59	    pid: '53754'
60	    log_path: ~/runs/distill_sparse_swiglu/mvp_kl_s42.log
61	    metrics:
62	      final_total_loss: 3.3438
63	      final_kl_loss: 3.2969
64	      final_reg_loss: 0.05
65	      final_sparsity: 0
66	      steps: 1000
67	      tau_final: 0.1
68	      wikitext2_ppl_dense: 6.12
69	      wikitext2_ppl_sparse: 455.93
70	      wikitext2_ppl_increase_pct: 7349
71	      model_level_sparsity: 0.372
72	      checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt
73	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt
74	    hypothesis: Raw KL divergence loss 直接蒸馏 dense→sparse gate，结合固定 sparsity regularization
75	      (reg_weight=0.1)，能稳定收敛到目标 50% 稀疏度——如果 sparsity collapse 则说明 KL loss 量级远大于 reg
76	      需要自适应平衡
77	  mvp_kl_s123:
78	    status: DONE
79	    retry_count: 0
80	    created_at: '2026-05-15T11:51:00.876Z'
81	    updated_at: '2026-05-16T02:23:07.388Z'
82	    spec:
83	      hypothesis: KL-trained predictor captures joint neuron interactions via end-to-end
84	        gradient flow, outperforming BCE at 50% sparsity
85	      loss_type: kl
86	      seed: 123
87	      model: Llama-3.1-8B
88	      sparsity: 0.5
89	      steps: 1000
90	      batch_size: 4
91	      seq_len: 2048
92	      gpu: cuda:0
93	      server: westd-34887
94	      eval: WikiText-2 + C4 perplexity
95	      checkpoint_path: N/A (killed)
96	      log_path: N/A
97	    notes: 'Killed: 使用旧 KL 配置（无归一化），已被 mvp_kl_norm_s123 替代。参见 kl_normalized_quicktest
98	      验证 seq_len-only 归一化有效。'
99	    conclusion: killed
100	    completed_at: '2026-05-16T02:23:07.388Z'
101	  mvp_kl_s456:
102	    status: DONE
103	    retry_count: 0
104	    created_at: '2026-05-15T11:51:02.768Z'
105	    updated_at: '2026-05-16T02:23:06.464Z'
106	    spec:
107	      hypothesis: KL-trained predictor captures joint neuron interactions via end-to-end
108	        gradient flow, outperforming BCE at 50% sparsity
109	      loss_type: kl
110	      seed: 456
111	      model: Llama-3.1-8B
112	      sparsity: 0.5
113	      steps: 1000
114	      batch_size: 4
115	      seq_len: 2048
116	      gpu: cuda:0
117	      server: westd-34887
118	      eval: WikiText-2 + C4 perplexity
119	      checkpoint_path: N/A (killed)
120	      log_path: N/A
121	    conclusion: killed
122	    notes: 'Killed: 使用旧 KL 配置（无归一化），已被 mvp_kl_norm_s456 替代。参见 kl_normalized_quicktest
123	      验证 seq_len-only 归一化有效。'
124	    completed_at: '2026-05-16T02:23:06.464Z'
125	  mvp_bce_s42:
126	    status: DONE
127	    retry_count: 1
128	    created_at: '2026-05-15T11:51:05.131Z'
129	    updated_at: '2026-05-17T02:59:08.627Z'
130	    server: westd-34887
131	    gpu: cuda:1
132	    account: root
133	    reproduce:
134	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
135	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
136	        --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
137	        42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42
138	        --wandb_run_name mvp_bce_s42 --dataset wikitext-103"
139	      finished_at: '2026-05-15T12:25:03.637Z'
140	    failure_reason: EXIT_CODE=1 (generic error — check log tail)
141	    completed_at: '2026-05-15T11:58:31.436Z'
142	    extra:
143	      hook_events:
144	      - event: on_failed
145	        action: agent
146	        ts: '2026-05-15T11:58:32.308080+00:00'
147	      - event: on_complete
148	        action: agent
149	        ts: '2026-05-15T12:25:04.331964+00:00'
150	      previous_failure:
151	        conclusion: failed
152	        notes: '失败原因: DatasetNotFoundError — cerebras/SlimPajama-627B 在 HF Hub 上不存在或无法访问
153	          (data_utils.py:36) | error_type: data | 已有成果: 模型加载成功 | 建议: 确认数据集路径或改用本地/streaming
154	          方式'
155	    notes: '训练+评估完成。训练: 1000 steps, 25.5 min, BCE loss 0.6711→0.6430。评估: WikiText-2
156	      PPL dense=27.96 → sparse=44.21 (+58.1%)。C4 评估跳过（离线模式无法 streaming 加载）。TEAL 逐层分布:
157	      浅层~44-50%, 深层51-66%。注意: dense baseline 27.96 高于文献~6 因使用 packed chunks 非 sliding
158	      window，但 dense/sparse 对比公平。evaluate.py 有 off-by-one bug 已修复（原始 shift 重复导致错位）。58%
159	      PPL 增幅对 MVP 1000 steps 可接受，文献中充分训练可降至 1-5%。'
160	    spec:
161	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
162	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
163	        --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
164	        42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42
165	        --wandb_run_name mvp_bce_s42 --dataset wikitext-103"
166	      server: westd-34887
167	      gpu:
168	      - cuda:1
169	      pid: '50143'
170	      log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s42.log
171	      submitted_at: '2026-05-15T12:08:23.512Z'
172	      submitted_via: submit_training_job
173	      backend: tmux
174	      account: root
175	      wall_clock_seconds: 1677.7
176	      gpu_hours: 0.47
177	    pid: '50143'
178	    log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s42.log
179	    conclusion: success
180	    metrics:
181	      true_dense_ppl: 6.1173
182	      predictor_hard_mask_ppl: 27.9603
183	      teal_sparse_ppl: 44.537
184	      model_level_sparsity: 0.4957
185	      ppl_increase_vs_true_dense_pct: 628
186	      eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
187	      calibration_samples: 32
188	      vanilla_teal_sparse_ppl_INVALID: 66036.4062
189	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42/predictor_bce.pt
190	    hypothesis: BCE loss 训练 sparse gate predictor (seed=42) 在 50% sparsity 下能产生有效预测——作为
191	      KL distillation 的对照基线，BCE 直接拟合 binary mask 而非蒸馏 dense output distribution
192	  mvp_bce_s123:
193	    status: DONE
194	    retry_count: 0
195	    created_at: '2026-05-15T11:51:07.010Z'
196	    updated_at: '2026-05-17T02:59:11.198Z'
197	    spec:
198	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
199	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
200	        --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "442532b6-df69-4c39-9a11-e01d9360e6b0",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "ca66daf0-e229-49b4-99d1-598f03271cdd",
  "sourceToolAssistantUUID": "442532b6-df69-4c39-9a11-e01d9360e6b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-18T18:38:43.539Z_

I now have a thorough understanding of the paper. Let me also check the task summary to confirm the actual tables match the provided review task data, and look at what was actually planned vs executed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca66daf0-e229-49b4-99d1-598f03271cdd",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAXBJ1VcoNDFgTkdSdy5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e27c2f06-068a-47aa-aea8-1eaeab425cdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012V4RDHX6bgej4AuNDK2jMg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 48165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4242,
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

_source line 40 · 2026-05-18T18:38:44.411Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HGQ5PkjKGpj1aAa2yEvtQf`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e27c2f06-068a-47aa-aea8-1eaeab425cdf",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAXBJ1VcoNDFgTkdSdy5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e50689a-66ef-4d87-9ce3-6a9a09a1ab50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012V4RDHX6bgej4AuNDK2jMg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 48165,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4242
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 48165,
          "cache_creation_input_tokens": 4242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4242,
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

_source line 41 · 2026-05-18T18:38:44.416Z_

<details><summary>↩ Tool result · `toolu_01HGQ5PkjKGpj1aAa2yEvtQf`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e50689a-66ef-4d87-9ce3-6a9a09a1ab50",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "a8c4b8793c0fc9cf0",
  "type": "user",
  "uuid": "9fa62ff2-dfe8-44d6-8c6c-4a3f67bc4b06",
  "sourceToolAssistantUUID": "6e50689a-66ef-4d87-9ce3-6a9a09a1ab50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-18T18:40:12.540Z_



Now I have a comprehensive understanding of the paper. Let me compile my review.

---

## Review: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"

**Reviewer 1 (R1) — Methods and Experiments Focus**

---

### Summary

This paper trains lightweight per-token sparsity predictors using forward KL divergence distillation (with Gumbel-Sigmoid relaxation) for SwiGLU-based LLMs, and investigates why KL outperforms standard BCE training. The central finding is that KL discovers neuron importance patterns diverging 53% from magnitude-based masks, and a causal ablation attributes the quality gain to mask target quality rather than gradient coupling. The paper also characterizes sparsity regimes and shows compensation networks become redundant under KL training. While the core idea is sound and the causal ablation is a genuinely interesting experimental design, the paper suffers from significant gaps in experimental coverage (missing cross-architecture results, incomplete table entries, single-seed regime analysis) and the causal ablation's own statistical evidence is too weak to support the strong claims made.

---

### Strengths

- **Well-motivated loss taxonomy.** The 2D taxonomy (correction granularity x training signal coupling) provides a clean conceptual framework. Placing prior work (DejaVu, FastForward, SPON, D2DMoE, ShadowLLM) into this grid is useful for the community and clearly identifies the previously unexplored per-token x coupled cell.

- **Causal ablation design is creative.** Training BCE on KL-derived oracle masks to disentangle target quality from gradient coupling is a well-conceived experiment. The idea of using one method's discovered targets to train another method is a clean interventional design that goes beyond typical ablation studies.

- **Honest reporting of negative results.** The paper acknowledges the 14B MMLU gap (63.7% vs TEAL's 71.8%), downstream collapse at 50%, the 9.5pp cross-seed MMLU variance under global allocation, and the lack of wall-clock speedup. This level of transparency is commendable and unusual.

- **Thorough hyperparameter sensitivity.** Appendix ablations on bottleneck dimension, temperature schedule, and training convergence are well-executed and show robustness. The finding that TEAL global allocation (not predictor capacity) is the binding constraint (Table 8) is an insightful observation.

- **Compensation redundancy is practically useful.** Demonstrating that KL removes the need for a 67.2M-parameter compensation network at both tested sparsity levels is a concrete practical contribution that simplifies the inference pipeline.

- **Method section is clearly written.** The problem formulation, predictor architecture, Gumbel-Sigmoid relaxation, and adaptive penalty controller are described with sufficient mathematical precision for reproduction. The gradient analysis (Eq. 7-8) clearly articulates the structural difference between BCE and KL gradients.

---

### Weaknesses

**Major:**

1. **Causal ablation is statistically underpowered (Major).** The paper's strongest claim — that mask target quality explains "82-100%" of KL's advantage — rests on 3 seeds with extreme variance: delta PPL ranges from 0.00 to 0.85 (std=0.36, which is 75% of the mean 0.48). Seed s42 shows delta=0.00 with perfect oracle agreement (0.978), meaning for that seed the ablation perfectly supports the claim, while s123 shows delta=0.85, which could represent a meaningful residual gradient coupling effect. With only 3 seeds and such high variance, the confidence interval on the "gradient coupling contribution" includes both 0% and a substantial positive number. The paper needs at minimum 10-15 seeds to make the "82-100%" attribution claim credible, or it should substantially soften the language.

2. **Cross-architecture and cross-scale results are buried or missing (Major).** The abstract and introduction prominently claim evaluation on "Mistral-7B-v0.3 and Qwen-2.5-14B," but the main body contains zero tables for these models. Mistral results appear only as a PPL-only table in the appendix (Table 12) with no downstream metrics at all. Qwen-2.5-14B appears in Appendix Table 11 with results that actually contradict the narrative: TEAL beats KL on MMLU by 8pp (71.8% vs 63.7%) and BCE beats KL on GSM8K (53.1% vs 48.8%). These are not minor discrepancies — they suggest KL's advantage may be PPL-specific and not transfer to downstream tasks at larger scale. Relegating contradictory evidence to the appendix while claiming cross-scale validation in the abstract is misleading framing.

3. **No actual wall-clock speedup demonstrated (Major).** The paper acknowledges this in limitations, but Table 7 (latency) shows the sparse pipeline is *slower* than dense inference (+6.4% overhead). For a paper about sparsity prediction, the inability to demonstrate any speedup — even with sparse kernel libraries that already exist (Triton block-sparse, cuSPARSE) — severely limits practical impact. The contribution reduces to "better PPL under a hypothetical sparse execution regime."

4. **Regime analysis relies on single-seed sweeps (Major).** Table 5 (phase analysis) presents 30%/40%/50% sparsity with the 40% row being entirely single-seed. The claimed "non-monotonic allocation preference" (uniform better at 30%, global better at 40%, equivalent at 50%) could easily be noise. The 40% MMLU numbers (global 38.06 vs uniform 30.68, a 7.4pp gap) are from a single seed — given that 30% global MMLU has 9.5pp cross-seed std, a 7.4pp gap from a single seed is within one standard deviation of noise. This entire "regime" narrative is unsupported without multi-seed data at 40%.

5. **BCE baseline is unfairly weakened (Major).** The BCE baseline uses magnitude-based oracle masks exclusively. But the paper's own causal ablation shows that BCE on KL-derived targets matches KL. This means the comparison is really "good oracle vs bad oracle," not "KL loss vs BCE loss." The paper should test BCE with better oracles (e.g., gradient-based importance, Fisher information, or even oracle masks derived from actual output sensitivity) to demonstrate that KL's automated oracle discovery is truly competitive with an exhaustive oracle search. As it stands, the paper shows KL finds better masks than magnitude, but not that KL finds the *best* masks or that the mask discovery mechanism is uniquely enabled by KL.

**Minor:**

6. **SNR analysis is suggestive but not rigorous (Minor).** The gradient SNR comparison (5.14x at convergence) is measured at step 300 out of 1000 training steps and is described as "non-monotonic" (BCE exceeds KL during steps 100-250). The paper then argues this is "consistent with KL's gradient coupling becoming effective only after the predictor learns a coarse mask structure," but this post-hoc narrative is unfalsifiable. The SNR metric itself ($\|E[\nabla]\|^2 / \text{Var}[\nabla]$) conflates signal magnitude with signal quality — higher SNR does not necessarily mean better optimization.

7. **Training data is WikiText-103 only (Minor).** All predictors are trained on WikiText-103 for 1000 steps. The C4 OOD evaluation (Appendix D) shows PPL 16.03 at 30% (1.74x dense), which is substantially worse than WikiText-2's 8.82 (1.44x dense). This 21% relative degradation in the ratio suggests the predictor overfits to WikiText-103's domain. No discussion of training data diversity or multi-domain training.

8. **Forward KL vs reverse KL comparison is incomplete (Minor).** The ablation shows forward KL > JSD > reverse KL, but uses only PPL at 50% sparsity. The paper's own findings show PPL is a poor proxy for downstream quality. Without downstream metrics for JSD and reverse KL variants, the divergence direction ablation is incomplete.

9. **The "53% divergence" framing is misleading (Minor).** Per-layer Jaccard similarity of 47% at 50% sparsity is expected to be well below 100% even for methods targeting the same objective, because any stochastic mask predictor will disagree with a deterministic magnitude threshold on boundary neurons. The paper does not establish a baseline for what Jaccard similarity would be expected between, say, two different random seeds of the same KL predictor, or between KL and a Fisher-information oracle. Without this calibration, "53% divergence" lacks interpretive context.

10. **Adaptive penalty controller has residual deviations (Minor).** At 30% target, actual sparsity is 28.5% (5% deviation); at 70%, deviation is 1.7%. The paper argues this is negligible, but does not report what TEAL's PPL would be at the actual achieved sparsity levels (only at the nominal targets). For precise PPL comparisons, the KL method should be evaluated at its actual achieved sparsity, not the target.

---

### Questions for Authors

1. What is the Jaccard similarity between KL masks from two different seeds? This baseline would contextualize whether 47% Jaccard with magnitude masks is surprisingly low or expected.

2. Why are Mistral downstream metrics (ARC-c, MMLU, etc.) completely absent? Were they run and omitted, or never computed?

3. For the Qwen-2.5-14B results where TEAL beats KL on MMLU by 8pp: does this persist across seeds, or is it a single-seed artifact? What is the cross-seed variance at 14B?

4. The causal ablation uses TEAL 50% uniform for "controlled evaluation." Why not also report under global allocation, which is the paper's primary inference protocol?

5. At 40% sparsity, what are the 3-seed results? The entire regime analysis narrative hinges on a single-seed data point at this sparsity level.

6. Have you tried training BCE with oracle masks derived from output sensitivity (e.g., leave-one-out neuron removal measured by KL from dense)? This would test whether magnitude is simply a bad oracle, independent of BCE vs KL training.

7. The adaptive penalty controller saturates at lambda_max for 30% and 70% targets. Does performance change if lambda_max is increased (e.g., 10000)?

---

### Missing Experiments

1. **Multi-seed regime sweep**: At minimum, 3 seeds at each of the 6 sparsity levels (25-50%) for both allocation strategies. Without this, the regime characterization and non-monotonic allocation claims are unreliable.

2. **Cross-architecture downstream metrics**: Mistral-7B needs ARC-c, MMLU, WinoGrande, GSM8K at both 30% and 50%. Currently zero downstream numbers exist for Mistral.

3. **Multi-seed 14B evaluation**: The Qwen-2.5-14B MMLU gap (KL 63.7% vs TEAL 71.8%) is a critical negative result that requires seed variance analysis. A single seed cannot distinguish systematic failure from noise.

4. **Better BCE oracles**: BCE trained with Fisher-information or leave-one-out sensitivity oracles would determine whether KL's contribution is truly automated *oracle discovery* or simply that magnitude is a poor oracle choice.

5. **LongBench and generation quality baselines**: The task summary mentions LongBench, MT-Bench, and RULER evaluations that appear absent from the actual paper text. If conducted, these should be reported with full baseline comparisons.

6. **Training data diversity**: Training on a mix of domains (WikiText + C4 + code) and reporting the effect on OOD generalization would strengthen the practical relevance.

7. **Statistical tests**: Paired bootstrap tests or Wilcoxon signed-rank tests for the KL vs BCE comparison, rather than relying on overlapping confidence intervals from 3 seeds.

---

### Score: 3 (Weak Reject)

**Confidence: 4 (High)**

**Justification**: The core idea (KL distillation for contextual sparsity prediction) is sound and the causal ablation design is creative. However, the paper's strongest claims are inadequately supported: the "mask quality not gradient coupling" conclusion rests on 3 seeds with 75% relative std; the regime analysis uses single-seed data at the critical 40% point; cross-architecture validation is PPL-only with no downstream metrics; and the 14B results actually contradict the narrative (TEAL beats KL on MMLU). The absence of any wall-clock speedup further limits impact. The paper reads as a solid preliminary investigation that needs one more round of experiments — specifically multi-seed regime sweeps, cross-architecture downstream evaluation, and stronger BCE oracle baselines — before the claims can be considered adequately supported for a top venue. I would encourage resubmission after addressing the statistical power issues and the missing cross-architecture/cross-scale downstream evaluations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fa62ff2-dfe8-44d6-8c6c-4a3f67bc4b06",
  "isSidechain": true,
  "agentId": "a8c4b8793c0fc9cf0",
  "requestId": "req_011CbAXBdjPteLY24pi8gZbK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca008662-f344-42da-9364-5556d7f56127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQ3wdm8FDefGEmpW8s8tBD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 52407,
      "output_tokens": 3144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 708
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3144,
          "cache_read_input_tokens": 52407,
          "cache_creation_input_tokens": 708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 708,
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
