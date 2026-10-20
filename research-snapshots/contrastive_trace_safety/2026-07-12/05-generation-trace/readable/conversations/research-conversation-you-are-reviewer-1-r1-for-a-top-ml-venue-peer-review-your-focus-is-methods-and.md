# Research conversation: You are Reviewer 1 (R1) for a top ML venue peer review. Your focus is **methods and experiments**. Review the paper belo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a4597d9cc7d82e8dd.jsonl`
- **Structured JSON:** [`f5f2d53e619423bbfe42.json`](../../sessions/f5/f5f2d53e619423bbfe42.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-16T20:21:14.999Z_

You are Reviewer 1 (R1) for a top ML venue peer review. Your focus is **methods and experiments**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

Title: "Architecture Determines Safety Monitoring Strategy: Hidden-State Detection in Reasoning Models Reveals Two Distinct Regimes"

The paper presents a cross-architecture evaluation of hidden-state safety monitoring for reasoning models that exhibit "self-jailbreak" behavior (safety reasoning ceases during extended CoT). It tests across 4 models in 2 architecture families (Llama-3.1, Qwen2.5) at 2 scales (7-8B, 32B).

Key claims:
1. Two regimes exist: "distributed-signal" (Llama) where safety signal is spread across minor PCs (PCA top-3=16.6%), requiring temporal context (+30.2pp); and "concentrated-signal" (Qwen2.5) where signal is in dominant PCs (38-41%), enabling static probes at 70%+ coverage with temporal adding only +4.6pp (CI crossing zero).
2. Architecture, not scale, determines the regime (controlled via OpenThinker-7B).
3. Cross-architecture transfer fails catastrophically (25-33%).
4. Concentrated-signal regime enables positive detection lead time.
5. A diagnostic framework using Fisher discriminant ratio and PCA variance concentration predicts which regime applies.

## Paper Details (8 pages)

**Section 3 - Method:**
- Task: detect commitment point t* from hidden states h_t at each reasoning step
- Methods: Static LR, Temporal window LR (W=15), GRU-256, Mahalanobis distance
- Diagnostic framework: PCA variance concentration (>30% = concentrated), Fisher discriminant ratio in PCA-3 subspace (>3 = concentrated)
- Metrics: Coverage (probe fires within ±3 steps of true commitment point), Lead time (signed distance)
- Data: 209 training traces, 43 test traces from HarmThoughts dataset, 4 models in 2×2 matrix

**Section 4 - Experiments (12 subsections):**

Table 1 - Static probe cross-architecture:
| Model | Arch | Static Coverage | Fisher(full) | Fisher(PCA-3) | PCA Var |
|-------|------|----------------|-------------|--------------|---------|
| r1-8b | Llama | 46.5% | 17.9 | 0.93 | 16.6% |
| r1-32b | Qwen2.5 | 69.8% | 8.3 | 5.1 | 38.0% |
| QwQ-32B | Qwen2.5 | 72.1% | 6.7 | 4.2 | 41.0% |

Table 2 - Temporal advantage:
| Model | Static | Temporal W15 | Delta |
|-------|--------|-------------|-------|
| r1-8b (Llama) | 46.5% | 76.7% | +30.2pp |
| r1-32b (Qwen) | 69.8% | 74.4% | +4.6pp |
| QwQ-32B (Qwen) | 72.1% | 76.7% | +4.6pp |

Table 3 - Window size ablation (W=1,3,5,10,15,20,25): Llama shows steep improvement 46.5%→76.7%; Qwen2.5 nearly flat ~70-77%.

Table 4 - Bootstrap 95% CIs (1000 resamples):
- Temporal Δ Llama: +30.2pp [+19,+42] Significant
- Temporal Δ Qwen r1-32b: +4.6pp [-2,+12] Not significant
- Temporal Δ Qwen QwQ: +4.6pp [-2,+12] Not significant
- Static Qwen vs Llama: +23.3pp [+11,+36] Significant
- Cross-arch transfer vs random: +7.6pp [-4,+17] Not significant

Table 5 - Scale control (OpenThinker-7B): Qwen2.5-7B static=67.4%, temporal delta=+2.4pp, Fisher PCA-3=4.8

Table 6 - Cross-architecture transfer:
- Llama→Qwen: 25.6-27.9% (vs in-domain 69.8-74.4%)
- Qwen→Llama: 30.2-32.6% (vs in-domain 46.5-76.7%)
- Within-Qwen: 65.1% (vs in-domain 72.1%)

Table 7 - Lead time: Llama negative (-2 to -1), Qwen positive (+2.1 to +4.2)

Table 8 - Mahalanobis: Llama 34.9%, Qwen 55.8-60.5%

Table 9 - Layer ablation: Llama sensitive (1 layer >70%), Qwen robust (10 layers >70%)

Table 10 - GRU upper bound: identical to temporal LR on 32B models

Table 11 - 16-label: ~+2.4pp uniform improvement

Table 12 - Oracle decomposition: Llama density gradient (corr=0.21, entropy=1.83), Qwen sharp transition (corr=0.67, entropy=0.94)

**Section 5 - Discussion:**
- Diagnostic framework: compute PCA variance → if >30% use static probe, if <20% use temporal
- Cross-arch deployment: must train per-architecture, within-family transfer viable

**Section 5.3 - Limitations acknowledged:**
1. Small sample (209 train / 43 test)
2. Only 2 architecture families
3. Specific to HarmThoughts dataset
4. No proprietary models (o1, o3)

**References:** 7 references, all Anonymous 2025.

## Experiment Design Reference (from review context YAML)

The full experiment plan includes 12 experiments (exp-001 through exp-012). The paper covers ALL 12 experiments. Here is the full list for coverage checking:
1. Cross-architecture static probe (exp-001) ✓ Table 1
2. Cross-architecture temporal window (exp-002) ✓ Table 2
3. Cross-model transfer (exp-003) ✓ Table 6
4. Lead time analysis (exp-004) ✓ Table 7
5. Mahalanobis baseline (exp-005) ✓ Table 8
6. Bootstrap CIs (exp-006) ✓ Table 4
7. Window size ablation (exp-007) ✓ Table 3
8. Layer selection ablation (exp-008) ✓ Table 9
9. 16-label supervision (exp-009) ✓ Table 11
10. Oracle decomposition (exp-010) ✓ Table 12
11. OpenThinker-7B scale control (exp-011) ✓ Table 5
12. GRU upper bound (exp-012) ✓ Table 10

## Your Task

Evaluate the paper's **methodological rigor** and **experimental quality**. Address:

1. **Experimental design**: Is the 2×2 matrix sound? Are controls adequate? Are there confounds?
2. **Statistical rigor**: Are the bootstrap CIs adequate given n=43? Are claims well-supported by the evidence?
3. **Evaluation metrics**: Is "coverage within ±3 steps" a good metric? Is lead time well-defined?
4. **Baselines and comparisons**: Are baselines sufficient? Missing comparisons?
5. **Reproducibility**: Is there enough detail to reproduce?
6. **Data concerns**: 209/43 split — is this sufficient? How much should we trust the results?
7. **Methodological gaps**: Anything missing that should be there?

Provide your review in this format:

### R1 Review: Methods & Experiments

**Summary:** (2-3 sentences)

**Strengths:**
- S1: ...
- S2: ...
- S3: ...

**Weaknesses:**
- W1: ...
- W2: ...
- W3: ...
- W4: ...

**Questions for Authors:**
- Q1: ...
- Q2: ...
- Q3: ...

**Minor Issues:**
- ...

**Soundness Score:** X/5
**Overall Score:** X/6
**Confidence:** X/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e222d192-3a79-4e22-984d-fe1408eca72d",
  "agentId": "a4597d9cc7d82e8dd",
  "type": "user",
  "uuid": "bc6e2c8e-b075-46a4-9d35-7b2393d79ba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "89f97e79-02d6-42a5-84fc-3c89ac4f53dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T20:21:15.005Z_

```json
{
  "parentUuid": "bc6e2c8e-b075-46a4-9d35-7b2393d79ba3",
  "isSidechain": true,
  "agentId": "a4597d9cc7d82e8dd",
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
  "uuid": "8199905a-0505-4eca-9516-14970b233e3a",
  "timestamp": "2026-05-16T20:21:15.005Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "89f97e79-02d6-42a5-84fc-3c89ac4f53dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T20:22:03.995Z_

### R1 Review: Methods & Experiments

**Summary:** This paper proposes that architecture family (Llama vs. Qwen2.5) determines whether safety-relevant signal in hidden states is distributed or concentrated, leading to distinct optimal monitoring strategies. The experimental design is systematic (12 experiments, 2×2 architecture-scale matrix), but the extremely small test set (n=43) and narrow scope (2 families, 1 dataset) substantially limit the strength of the conclusions. The core dichotomy is interesting but the evidence is insufficient to support the broad architectural claims made.

**Strengths:**

- S1: **Comprehensive experiment matrix.** All 12 planned experiments are executed and reported, covering ablations (window size, layer selection), baselines (Mahalanobis, GRU), transfer, and statistical validation. This is thorough for a workshop-length contribution.

- S2: **Appropriate use of bootstrap CIs.** The authors correctly identify that the temporal advantage for Qwen crosses zero and refrain from overclaiming. The honesty about non-significant results (Table 4) is commendable and the bootstrap approach is reasonable given the small sample.

- S3: **Diagnostic framework is actionable.** The PCA variance concentration threshold (>30% → static probe viable) paired with Fisher discriminant ratio gives practitioners a concrete decision procedure. The OpenThinker-7B control (Table 5) strengthens the architecture-over-scale argument.

- S4: **Cross-transfer experiment (Table 6) is well-designed.** Testing both directions (Llama→Qwen, Qwen→Llama) and including within-family transfer provides clean evidence that probes are architecture-specific.

**Weaknesses:**

- W1: **Critically small test set (n=43).** With 43 test traces, each percentage point of coverage corresponds to fewer than 0.5 traces. The ±3 step tolerance further inflates apparent performance. Bootstrap CIs of [+19, +42] for the Llama temporal delta span 23 percentage points — this is not precise enough to make strong quantitative claims. The 209-trace training set is similarly small for learning temporal patterns with W=15 (each window sees ~14 features × 15 steps). The authors acknowledge this but the paper's title-level claims ("Two Distinct Regimes") demand stronger evidence than what n=43 can provide.

- W2: **Confound between architecture and training data/procedure.** The paper claims "architecture determines" the regime, but Llama-3.1 and Qwen2.5 differ in training data, RLHF procedure, tokenizer, and safety training — not just architecture. The OpenThinker-7B control shares the Qwen2.5 architecture AND its pre-training, so it does not isolate architecture from training. A stronger control would be same-architecture models with different safety fine-tuning, or different architectures trained on identical data. Without this, the title claim is unsupported.

- W3: **Coverage metric is poorly motivated.** "Probe fires within ±3 steps of true commitment point" is generous — if reasoning steps are short (e.g., one sentence each), ±3 steps could be 6 steps total tolerance. The paper never reports step duration in tokens, how commitment points are annotated, inter-annotator agreement, or what happens at different tolerance thresholds (±1, ±2, ±5). A sensitivity analysis on the tolerance window is essential. Additionally, "coverage" conflates detection rate with precision — what is the false positive rate?

- W4: **No false positive analysis.** The paper reports only coverage (true positive rate at the commitment point) but never discusses false positives — how often does the probe fire on safe traces or at non-commitment points in unsafe traces? Without this, the practical utility of the monitoring system is unknowable. A probe that fires everywhere would achieve 100% coverage.

- W5: **Single dataset (HarmThoughts) limits generalization.** All 209+43 traces come from one dataset with one definition of "self-jailbreak." Different harmful content categories, different elicitation strategies, or different definitions of commitment could change the signal structure entirely. The claim of "two distinct regimes" is really "two distinct regimes on HarmThoughts."

- W6: **Missing standard baselines.** No comparison to: (a) token-level text classifiers on the CoT text itself, (b) attention-pattern based detection, (c) simple threshold on hidden-state norm or cosine similarity to a reference direction. The Mahalanobis baseline is welcome but insufficient — the reader cannot assess whether hidden-state probing is even necessary versus cheaper text-based monitoring.

**Questions for Authors:**

- Q1: How are commitment points annotated? Is there a codebook? What is the inter-annotator agreement? A ±3 tolerance is meaningless without knowing annotation noise.

- Q2: What is the false positive rate? If you run the temporal probe on the full trace (not just near t*), how often does it fire at non-commitment locations? What happens on safe/benign reasoning traces?

- Q3: Can you provide a control where the same base architecture (e.g., Qwen2.5-7B) is fine-tuned with different safety training procedures to disentangle architecture from training? Alternatively, have you examined any Llama-based model that might show concentrated signal, or any Qwen model that shows distributed signal?

- Q4: The GRU upper bound (Table 10) is "identical to temporal LR on 32B models" — does this mean the temporal patterns are purely linear? If so, this is an important finding that deserves more discussion. If the GRU adds nothing, what does that tell us about the nature of the signal?

- Q5: Seven anonymous references is unusual. Are these all from the authors' own prior work? This makes it impossible to assess the novelty relative to prior hidden-state probing literature (e.g., representation engineering, probing classifiers in mechanistic interpretability).

**Minor Issues:**

- The 2×2 matrix is actually incomplete: there is no Llama-32B model tested (the matrix is r1-8b/Llama, r1-32b/Qwen, QwQ-32B/Qwen, OpenThinker-7B/Qwen). This is 3 Qwen and 1 Llama, not a balanced design.
- Table 10 (GRU) reports results only for 32B models — why not 7-8B?
- "Fisher(full)" vs "Fisher(PCA-3)" in Table 1: the concentrated regime has *lower* Fisher(full) but *higher* Fisher(PCA-3). This inversion deserves explanation — it suggests the full-space Fisher is dominated by noise dimensions in Qwen, which would actually argue against the signal being "concentrated."
- The lead time metric (Table 7) sign convention should be stated more clearly: positive = probe fires before commitment?
- No computational cost comparison between static and temporal probes for deployment.

**Soundness Score:** 2/5
The core experimental methodology has significant gaps (no FPR, single dataset, confounded architecture claim, very small n). While the experiments are numerous, they all operate within the same narrow setup and the statistical power is insufficient for the strength of claims made.

**Overall Score:** 3/6 (Weak Reject)
The research question is timely and the diagnostic framework is a nice contribution, but the evidence base is too thin (n=43, 1 dataset, 2 families with 1 Llama model), key metrics are missing (FPR), and the central "architecture determines regime" claim has uncontrolled confounds. The paper would benefit from: (1) larger evaluation sets, (2) false positive analysis, (3) text-based baselines, and (4) controls that isolate architecture from training procedure.

**Confidence:** 4/5
I am confident in these assessments. The statistical and methodological concerns are straightforward. My uncertainty is primarily around whether the anonymous references contain relevant context that would address some concerns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8199905a-0505-4eca-9516-14970b233e3a",
  "isSidechain": true,
  "agentId": "a4597d9cc7d82e8dd",
  "requestId": "req_011Cb6sPBnqTud4AKZwiU5ew",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cb37aa6-0a38-4170-bab6-85ee3dc52dbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "89f97e79-02d6-42a5-84fc-3c89ac4f53dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nq6k8ZLEfp9Jpsr4kvnpU3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16219,
      "cache_read_input_tokens": 0,
      "output_tokens": 1870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16219
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1870,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16219,
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
