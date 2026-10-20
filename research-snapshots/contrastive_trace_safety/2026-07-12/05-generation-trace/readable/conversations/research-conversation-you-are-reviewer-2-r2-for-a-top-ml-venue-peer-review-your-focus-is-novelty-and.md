# Research conversation: You are Reviewer 2 (R2) for a top ML venue peer review. Your focus is **novelty and related work**. Review the paper bel

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a711105179216221b.jsonl`
- **Structured JSON:** [`1d1b5fbf99329ab13797.json`](../../sessions/1d/1d1b5fbf99329ab13797.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-16T20:21:38.321Z_

You are Reviewer 2 (R2) for a top ML venue peer review. Your focus is **novelty and related work**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

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

**Section 1 - Introduction:**
- Reasoning models exhibit "self-jailbreak" where safety reasoning and harmful execution interleave in CoT, with a "commitment point" where safety reasoning permanently ceases
- Prior work (TrajGuard, SafeSwitch, SIREN) achieves 95%+ defense on instruction-tuned models but targets adversarial inputs, not self-generated reasoning failures
- This is "the first systematic cross-architecture evaluation of hidden-state monitoring for safety commitment detection in reasoning models"

**Section 2 - Related Work (3 paragraphs):**
- Hidden-state jailbreak detection: TrajGuard (Mahalanobis), SafeSwitch/SIREN (linear probes) — 95%+ on instruction-tuned models but target adversarial inputs
- Reasoning model safety: HarmThoughts (characterization), Self-Jailbreaking (demonstration) — neither proposes deployable detectors
- CoT monitoring: SafeRemind, SafeThink (text-level) — vulnerable to pathological CoT

**Section 3 - Method:**
- Static LR probe, Temporal window LR, GRU-256 probe, Mahalanobis distance baseline
- Diagnostic framework: PCA variance concentration + Fisher discriminant ratio (PCA-projected)
- Metrics: Coverage (within ±3 steps), Lead time
- 4 models: r1-8b (Llama), OpenThinker-7B (Qwen2.5-7B), r1-32b (Qwen2.5-32B), QwQ-32B (Qwen2.5-32B)
- Data: 209 train / 43 test traces from HarmThoughts

**Section 4 - Experiments (12 subsections covering):**
- Static probe cross-architecture (Table 1): Llama 46.5% vs Qwen 70%+ static coverage
- Temporal advantage (Table 2): Llama +30.2pp, Qwen +4.6pp
- Window size ablation (Table 3): Llama steep curve, Qwen flat
- Bootstrap CIs (Table 4): Temporal Δ significant on Llama, not on Qwen
- Scale control with OpenThinker-7B (Table 5): confirms architecture not scale
- Cross-architecture transfer (Table 6): 25-33% cross-family, 65.1% within-family
- Lead time (Table 7): Llama negative, Qwen positive
- Mahalanobis baseline (Table 8): partial success on Qwen (55-60%), poor on Llama (35%)
- Layer ablation (Table 9): Qwen robust, Llama sensitive
- GRU upper bound (Table 10): no improvement over LR
- 16-label supervision (Table 11): marginal +2pp
- Oracle decomposition (Table 12): mechanistic explanation (density gradient vs sharp transition)

**Section 5 - Discussion:**
- Practitioner diagnostic framework (PCA variance thresholds)
- Cross-architecture deployment implications
- Limitations: small sample, 2 families only, HarmThoughts-specific, no proprietary models

**References:** 7 references, all Anonymous 2025:
[1] HarmThoughts, [2] Self-Jailbreaking, [3] TrajGuard, [4] SafeSwitch, [5] SIREN, [6] SafeRemind, [7] SafeThink

## Your Task

Evaluate the paper's **novelty**, **positioning**, and **related work coverage**. Address:

1. **Novelty assessment**: How novel is the core contribution? Is "architecture determines monitoring strategy" a surprising or expected finding? Is the two-regime characterization a genuine conceptual advance?
2. **Related work completeness**: Are there missing related works? Is the mechanistic interpretability literature covered (probing, linear probes in LLMs)? What about representation geometry work?
3. **Positioning**: Is the paper well-positioned relative to prior work? Does it overclaim or underclaim?
4. **Contribution significance**: Are the contributions sufficient for a top venue? Would the community learn something actionable?
5. **Framing critique**: Is the "two regimes" framing the right one, or is it overfit to n=2 architecture families?
6. **Writing quality**: Is the paper well-organized and clearly written?
7. **References**: Only 7 references — is this adequate? Are key works missing?

Provide your review in this format:

### R2 Review: Novelty & Related Work

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

**Novelty Score:** X/5
**Overall Score:** X/6
**Confidence:** X/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e222d192-3a79-4e22-984d-fe1408eca72d",
  "agentId": "a711105179216221b",
  "type": "user",
  "uuid": "c9b9f134-541d-42bc-b4ac-298831747d87",
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

_source line 2 · 2026-05-16T20:21:38.326Z_

```json
{
  "parentUuid": "c9b9f134-541d-42bc-b4ac-298831747d87",
  "isSidechain": true,
  "agentId": "a711105179216221b",
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
  "uuid": "b8f56008-2c8f-4702-bb9f-45225f5f42c8",
  "timestamp": "2026-05-16T20:21:38.326Z",
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

_source line 3 · 2026-05-16T20:22:23.435Z_

### R2 Review: Novelty & Related Work

**Summary:** The paper proposes that architecture family (Llama vs. Qwen2.5) determines whether hidden-state safety signals are distributed or concentrated, yielding two distinct monitoring regimes. While the empirical characterization is systematic and the diagnostic framework is practical, the novelty is limited by the narrow scope (n=2 families), the predictability of the core finding given known differences in these architectures' training, and significant gaps in related work coverage.

**Strengths:**

- S1: The two-regime framing (distributed vs. concentrated signal) is a clean conceptual abstraction that, if it generalizes, would give practitioners an actionable decision procedure for deploying safety monitors. The diagnostic framework (PCA variance concentration + Fisher ratio) is concrete and reproducible.

- S2: The experimental design includes a thoughtful control — using OpenThinker-7B (Qwen2.5 architecture, 7B scale) to disentangle architecture from scale. This is good scientific practice and strengthens the architecture-determines-regime claim within the tested families.

- S3: The cross-architecture transfer failure result (25-33%) is practically important. Even if expected by experts, documenting it with confidence intervals has deployment value — it warns against naively reusing probes across model families.

**Weaknesses:**

- W1: **The core claim is built on n=2 architecture families.** "Architecture determines monitoring strategy" is stated as a general principle, but the evidence supports only "Llama-3.1 and Qwen2.5 differ." With only two data points on the independent variable, calling this "two distinct regimes" risks severe overfitting to the specific pair studied. The paper acknowledges this in limitations but does not sufficiently temper its title and abstract claims. A more honest framing would be "we observe two regimes in these specific families" rather than implying a general taxonomy.

- W2: **The related work section is alarmingly thin (7 references, all Anonymous 2025).** Critical bodies of work are entirely absent:
  - *Probing and linear representation literature*: The entire lineage from Alain & Bengio (2017) through Belinkov (2022) survey, Hewitt & Manning (2019), and recent work on linear probes in LLMs (Burns et al. 2023 "Discovering Latent Knowledge," Li et al. 2024 "Inference-Time Intervention") is missing. The paper uses linear probes as its primary tool without citing the foundational work establishing when and why they succeed.
  - *Representation geometry*: Park et al. (2024) on geometry of truth, Marks & Tegmark (2023) on representation engineering, Nanda et al. on residual stream structure — all directly relevant to understanding why signals concentrate differently across architectures.
  - *Mechanistic interpretability*: Elhage et al. (2022) on superposition, Bricken et al. (2023) on monosemanticity — these provide the theoretical framework for understanding distributed vs. concentrated representations that the paper's regime distinction implicitly invokes.
  - *Safety probing specifically*: Zou et al. (2023) "Representation Engineering," Arditi et al. (2024) "Refusal in Language Models Is Mediated by a Single Direction" — the latter directly contradicts or complicates the "distributed signal" finding for Llama.

- W3: **The novelty of the architecture-determines-signal-structure finding is limited.** It is well-established that different model families learn different internal representations due to training data, RLHF procedures, and architectural choices (attention patterns, normalization). The finding that Qwen2.5 concentrates safety signal while Llama distributes it could reflect differences in RLHF/safety training rather than "architecture" per se. The paper does not adequately disentangle architecture (transformer config, normalization type, positional encoding) from training procedure (which is also family-specific).

- W4: **Coverage metric at ±3 steps is unusual and not well-justified.** The paper introduces a non-standard evaluation metric without comparing to standard detection metrics (AUROC, F1 at various thresholds, precision-recall curves). This makes it difficult to compare results to prior work and raises questions about whether the metric was chosen to favor the paper's narrative.

**Questions for Authors:**

- Q1: Arditi et al. (2024) showed refusal in Llama-family models is mediated by a single direction. How do you reconcile your "distributed signal" finding for Llama with their "single direction" finding? Is the difference because you study self-jailbreak commitment points rather than refusal per se? If so, this distinction needs explicit discussion.

- Q2: How do you disentangle "architecture" from "safety training procedure"? Llama-3.1 and Qwen2.5 differ not only in transformer configuration but in their entire RLHF pipeline. Could the regime difference be entirely explained by how safety was trained into each model rather than architectural properties? Would testing a Qwen2.5 model fine-tuned with Llama-style safety training resolve this?

- Q3: With 43 test traces, what is the statistical power to detect a meaningful difference between 70% and 75% coverage? The bootstrap CIs in Table 4 are wide — can you report exact CI widths and discuss whether your sample size is adequate for the granularity of claims made?

**Minor Issues:**

- The title claims "two distinct regimes" which implies a general taxonomy, but the evidence supports only characterization of two specific families. Consider a more precise title.
- All 7 references are "Anonymous 2025" — if this is for double-blind review, it still makes it impossible for reviewers to verify these citations exist and are correctly characterized. At minimum, provide arXiv IDs or venue information.
- The paper would benefit from a figure showing the PCA variance spectra for both families side-by-side, making the concentrated/distributed distinction visually immediate.
- Section 4 has 12 subsections for an 8-page paper, making it read like a results dump rather than a narrative. Consider consolidating around the key claims.

**Novelty Score:** 2/5
The two-regime characterization is observational rather than explanatory, is built on only two architecture families, and the core insight (different models represent safety differently) is expected given prior probing literature. The diagnostic framework adds some practical value but is not a conceptual advance.

**Overall Score:** 3/6 (Weak Reject)
The paper asks a relevant question and provides systematic experiments, but the novelty is insufficient for a top venue. The related work gaps are severe — the paper appears unaware of foundational probing literature and recent representation engineering work that directly bears on its claims. The n=2 families limitation means the "general principle" framing is not supported by the evidence. With broader architecture coverage (Mistral, Gemma, GPT-family if accessible), proper related work, and more careful claims, this could become a solid contribution.

**Confidence:** 4/5
I am familiar with the probing/representation engineering literature and safety monitoring work. My main uncertainty is whether the anonymous references contain additional context that would change my assessment of novelty relative to concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8f56008-2c8f-4702-bb9f-45225f5f42c8",
  "isSidechain": true,
  "agentId": "a711105179216221b",
  "requestId": "req_011Cb6sQuxe2z4HYQrQu2a2K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "505a5681-60da-480b-97c4-1faf456af8e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "89f97e79-02d6-42a5-84fc-3c89ac4f53dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQkgVdZSfHhYvt5F4KKJSG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7422,
      "cache_read_input_tokens": 8251,
      "output_tokens": 1680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7422
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1680,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7422,
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
