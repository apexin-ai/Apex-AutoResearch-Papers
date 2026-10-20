# Research conversation: Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores ## Core Problem RAG systems deployed in adv

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/42ce35e5-fa1f-4a36-a5ac-1a806c6d8973.jsonl`
- **Structured JSON:** [`6f9b944defdea4049ab2.json`](../../sessions/6f/6f9b944defdea4049ab2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:24:55.566Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:24:55.566Z",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "content": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores\n\n## Core Problem\n\nRAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) need to abstain from answering with distribution-free correctness guarantees when the retrieval corpus is poisoned. Corpus poisoning is a practical threat: CorruptRAG (arXiv 2025) achieves high attack success rates with a single injected document. Existing conformal prediction methods for RAG (TRAQ, NAACL 2024; C-RAG, ICML 2024; Conformal-RAG, SIGIR 2025) assume benign retrieval—Chen et al. (arXiv:2603.16817, Mar 2026) rigorously demonstrated these guarantees break under distribution shift and produce vacuous outputs at high confidence levels. Existing poisoning-robust CP (RPS, ICLR 2025 Spotlight) addresses calibration-set poisoning, a fundamentally different threat model from test-time retrieval corruption. Certified RAG defenses (RobustRAG, SaTML 2026; ReliabilityRAG, NeurIPS 2025) provide robust point estimates but no abstention mechanism or coverage certificates. The gap: no method provides distribution-free abstention guarantees for RAG under adversarial retrieval corruption.\n\n## Core Contribution and Theoretical Insight\n\nWe propose PRCA (Poisoning-Robust Conformal Abstention), whose central contribution is a **partition-induced reduction principle**: by partitioning retrieved passages into disjoint groups and computing inter-group agreement, arbitrary test-time retrieval corruption is deterministically reduced to a bounded total-variation (TV) shift in the one-dimensional nonconformity score distribution. This bounded TV shift is precisely what the CRC framework (ICLR 2024) can absorb via inflated quantiles, yielding formal coverage certificates. This reduction—from high-dimensional adversarial corruption to one-dimensional bounded distributional shift—parallels the approach of Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv 2502.14105), which reduces high-dimensional distribution shifts to manageable one-dimensional score shifts via ambiguity sets. PRCA instantiates this reduction paradigm for the specific setting of adversarial retrieval corruption in RAG.\n\n**Why not simply RobustRAG + standard CP?** A naive pipeline—running RobustRAG to obtain a robust answer, then applying TRAQ/C-RAG for conformal abstention—fails because: (1) RobustRAG's aggregation transforms the output distribution in a poisoning-dependent manner, so the nonconformity scores computed on a clean calibration set are no longer exchangeable with test-time scores under attack; (2) the magnitude of this distributional shift is uncharacterized, making standard CP coverage guarantees invalid. PRCA resolves this by explicitly bounding the TV distance between clean and poisoned score CDFs via the partition structure, then absorbing this bounded shift through CRC's quantile inflation.\n\n## Research Landscape\n\n**Conformal prediction for RAG:** TRAQ (NAACL 2024) and C-RAG (ICML 2024) established conformal prediction for RAG with coverage guarantees under benign retrieval. Conformal-RAG (SIGIR 2025) extends this to group-conditional coverage. Chen et al. (arXiv:2603.16817, Mar 2026) showed all such methods produce vacuous prediction sets under distribution shift and retrieval corruption, but proposed no solution—creating an open, citable gap.\n\n**Certified RAG defenses:** RobustRAG (SaTML 2026) provides certified defense via isolate-then-aggregate (partition passages → independent generation → keyword/decoding-based aggregation), achieving certified robust accuracy on RealtimeQA/NQ. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with NLI-based contradiction detection for provably robust document filtering. Both provide robust point estimates but no abstention mechanism or distribution-free coverage certificates.\n\n**Poisoning-robust CP:** RPS (ICLR 2025 Spotlight) achieves poisoning-robust conformal prediction via smoothed scores and majority voting, but assumes calibration-set poisoning—certificates do not transfer to test-time retrieval corruption where adversarial documents enter at inference time.\n\n**Partition-based defenses:** RAGPart (arXiv:2512.24268, Dec 2025) uses document partitioning at the retrieval stage (fragmenting documents and averaging fragment embeddings) to dilute poisoning impact. Three key differences from PRCA: (1) RAGPart operates at the retrieval/embedding stage, PRCA at the generation/calibration stage; (2) RAGPart outputs filtered retrieval sets, PRCA outputs {answer, abstain} decisions with coverage certificates; (3) RAGPart and PRCA are complementary—RAGPart can serve as a retrieval-stage preprocessor before PRCA's generation-stage certified abstention.\n\n**Attack landscape:** PoisonedRAG (USENIX Security 2025) achieves 90%+ ASR with 5 poisoned documents on NQ/HotpotQA/MS-MARCO. CorruptRAG (arXiv 2025) achieves high ASR with a single document. RSB Benchmark (May 2025) systematically evaluated 13 attack methods across targeted poisoning, DoS, and trigger-based categories, finding current defenses have residual risk. Semantic Chameleon (arXiv Mar 2026) introduced gradient-guided corpus-dependent attacks.\n\n**Distribution-shift-robust CP:** Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv 2502.14105) provides a framework for robust CP under distribution shifts by propagating ambiguity sets through scoring functions, reducing high-dimensional shifts to one-dimensional score distribution shifts. PRCA's partition-induced TV bound can be viewed as a specific instantiation of this reduction paradigm for adversarial retrieval corruption.\n\nNo existing work combines conformal abstention with retrieval-poisoning robustness.\n\n## Proposed Approach\n\n**Step 1: Partition-and-Generate.** Given top-n retrieved passages, partition them into K disjoint groups (random assignment). For each group, generate an answer via an isolated LLM call.\n\n**Step 2: Agreement Nonconformity Score.** Compute a nonconformity score based on inter-group answer agreement. Specifically, for each pair of groups (i, j), compute the NLI entailment probability e(i,j) = P(answer_i entails answer_j) using a lightweight NLI model (e.g., DeBERTa-v3, following ReliabilityRAG's NLI approach). The agreement score is defined as:\n\ns = 1 − (mean of e(i,j) over all pairs)\n\nThis score has two critical properties: (1) **Monotonicity**: s is monotone in the abstention threshold λ (higher s → more disagreement → more likely to abstain), satisfying CRC's requirement; (2) **Corruption-boundedness**: under k-poisoning, at most m = ceil(k / floor(n/K)) groups are corrupted, affecting at most m(K−1) of the K(K−1)/2 pairwise comparisons, yielding a bounded perturbation to s.\n\n**Key assumption and mitigation:** The agreement score assumes that LLM outputs for clean passages are sufficiently consistent across groups. If different groups cover different facets of the answer, clean-condition variance inflates s and may cause unnecessary abstention. We mitigate this by using NLI-based semantic entailment (rather than exact match) for agreement computation, which is robust to surface-level variation. Calibration on clean data naturally accounts for residual clean-condition variance in the score distribution.\n\n**Step 3: TV-Bounded Calibration.** Under k-poisoning with K groups, the corruption bound m determines the maximal TV distance between clean and poisoned score CDFs: TV ≤ m/K. Using CRC (ICLR 2024) with TV-inflated quantile: set abstention threshold at the (1 − α + TV)-quantile of calibration scores, yielding formal coverage certificate P(correct or abstain) ≥ 1 − α even under k-poisoning.\n\n**Step 4: Abstention Decision.** At test time, if s > λ (calibrated threshold), abstain; otherwise, output the majority answer across groups.\n\n## Experimental Design\n\n**Datasets:** NQ, HotpotQA, MS-MARCO (standard RAG evaluation benchmarks, used by PoisonedRAG and RobustRAG).\n\n**Attack methods:** (1) PoisonedRAG (targeted poisoning, varying k ∈ {1, 3, 5, 10}); (2) CorruptRAG (single-document high-ASR attack); (3) at least one DoS-type attack from RSB Benchmark (May 2025) taxonomy to test behavior under denial-of-service adversaries. Discussion section analyzes k-poisoning assumption validity across attack categories.\n\n**Models:** Three scales to verify model-agnosticism: (1) primary experiments on Qwen3.5-7B (or Llama-3-8B); (2) medium-scale validation on Qwen3.5-32B; (3) large-scale validation on Qwen3.5-72B. NLI model: DeBERTa-v3-large for agreement scoring.\n\n**Baselines (7 methods):**\n- Conformal methods: TRAQ (NAACL 2024), C-RAG (ICML 2024), Conformal-RAG (SIGIR 2025)\n- Certified defenses: RobustRAG (SaTML 2026), ReliabilityRAG (NeurIPS 2025)\n- Partition-based: RAGPart (arXiv:2512.24268) — same partition strategy, no conformal calibration (ablation baseline)\n- Compute-normalized: TRAQ + K× self-consistency voting (controls for PRCA's K× inference cost)\n\n**Calibration protocol:** Calibration set constructed on clean corpus (standard assumption per RPS, ICLR 2025), n_cal ≥ 500 per dataset. Sensitivity experiment: evaluate coverage degradation when actual poisoning budget exceeds assumed k upper bound.\n\n**Metrics:**\n- Primary: Certified coverage rate, empirical coverage rate under attack, abstention rate\n- Secondary: Clean accuracy (no attack), prediction set size, vacuousness rate (per Chen et al. 2026)\n- Tradeoff curves: coverage vs. abstention rate at varying α; coverage vs. poisoning budget k; certified vs. empirical robustness gap\n- Efficiency: wall-clock time per query, token consumption per query\n\n**Ablation matrix:**\n- K ∈ {3, 5, 7, 10}: partition count vs. coverage/abstention tradeoff\n- n ∈ {10, 20, 30}: retrieval depth vs. certificate tightness\n- Score function: NLI entailment (primary) vs. ROUGE-L vs. exact match\n- Calibration: CRC + TV inflation vs. CRC without inflation vs. vanilla split conformal\n- Partition strategy: random vs. round-robin by retrieval score\n\n**Scale:** 200-300 queries per dataset per setting (comparable to RobustRAG's 100/dataset), with 95% confidence intervals reported.\n\n## Key References\n\n- TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction (NAACL 2024)\n- C-RAG: Certified Generation Risks for RAG (ICML 2024)\n- Conformal Risk Control (ICLR 2024)\n- Provably Reliable Conformal Prediction Sets under Poisoning (ICLR 2025 Spotlight)\n- Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)\n- ReliabilityRAG (NeurIPS 2025)\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, Mar 2026)\n- Conformal-RAG: Conditional Conformal Factuality (SIGIR 2025)\n- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv 2025)\n- PoisonedRAG (USENIX Security 2025)\n- RSB Benchmark: Benchmarking Poisoning Attacks against RAG (May 2025)\n- RAGPart & RAGMask (arXiv:2512.24268, Dec 2025)\n- Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105)\n- Semantic Chameleon (arXiv Mar 2026)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:24:55.572Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:24:55.572Z",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

## Round 1

53 recorded events

### User

_source line 3 · 2026-05-30T07:24:55.634Z_

# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores

## Core Problem

RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) need to abstain from answering with distribution-free correctness guarantees when the retrieval corpus is poisoned. Corpus poisoning is a practical threat: CorruptRAG (arXiv 2025) achieves high attack success rates with a single injected document. Existing conformal prediction methods for RAG (TRAQ, NAACL 2024; C-RAG, ICML 2024; Conformal-RAG, SIGIR 2025) assume benign retrieval—Chen et al. (arXiv:2603.16817, Mar 2026) rigorously demonstrated these guarantees break under distribution shift and produce vacuous outputs at high confidence levels. Existing poisoning-robust CP (RPS, ICLR 2025 Spotlight) addresses calibration-set poisoning, a fundamentally different threat model from test-time retrieval corruption. Certified RAG defenses (RobustRAG, SaTML 2026; ReliabilityRAG, NeurIPS 2025) provide robust point estimates but no abstention mechanism or coverage certificates. The gap: no method provides distribution-free abstention guarantees for RAG under adversarial retrieval corruption.

## Core Contribution and Theoretical Insight

We propose PRCA (Poisoning-Robust Conformal Abstention), whose central contribution is a **partition-induced reduction principle**: by partitioning retrieved passages into disjoint groups and computing inter-group agreement, arbitrary test-time retrieval corruption is deterministically reduced to a bounded total-variation (TV) shift in the one-dimensional nonconformity score distribution. This bounded TV shift is precisely what the CRC framework (ICLR 2024) can absorb via inflated quantiles, yielding formal coverage certificates. This reduction—from high-dimensional adversarial corruption to one-dimensional bounded distributional shift—parallels the approach of Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv 2502.14105), which reduces high-dimensional distribution shifts to manageable one-dimensional score shifts via ambiguity sets. PRCA instantiates this reduction paradigm for the specific setting of adversarial retrieval corruption in RAG.

**Why not simply RobustRAG + standard CP?** A naive pipeline—running RobustRAG to obtain a robust answer, then applying TRAQ/C-RAG for conformal abstention—fails because: (1) RobustRAG's aggregation transforms the output distribution in a poisoning-dependent manner, so the nonconformity scores computed on a clean calibration set are no longer exchangeable with test-time scores under attack; (2) the magnitude of this distributional shift is uncharacterized, making standard CP coverage guarantees invalid. PRCA resolves this by explicitly bounding the TV distance between clean and poisoned score CDFs via the partition structure, then absorbing this bounded shift through CRC's quantile inflation.

## Research Landscape

**Conformal prediction for RAG:** TRAQ (NAACL 2024) and C-RAG (ICML 2024) established conformal prediction for RAG with coverage guarantees under benign retrieval. Conformal-RAG (SIGIR 2025) extends this to group-conditional coverage. Chen et al. (arXiv:2603.16817, Mar 2026) showed all such methods produce vacuous prediction sets under distribution shift and retrieval corruption, but proposed no solution—creating an open, citable gap.

**Certified RAG defenses:** RobustRAG (SaTML 2026) provides certified defense via isolate-then-aggregate (partition passages → independent generation → keyword/decoding-based aggregation), achieving certified robust accuracy on RealtimeQA/NQ. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with NLI-based contradiction detection for provably robust document filtering. Both provide robust point estimates but no abstention mechanism or distribution-free coverage certificates.

**Poisoning-robust CP:** RPS (ICLR 2025 Spotlight) achieves poisoning-robust conformal prediction via smoothed scores and majority voting, but assumes calibration-set poisoning—certificates do not transfer to test-time retrieval corruption where adversarial documents enter at inference time.

**Partition-based defenses:** RAGPart (arXiv:2512.24268, Dec 2025) uses document partitioning at the retrieval stage (fragmenting documents and averaging fragment embeddings) to dilute poisoning impact. Three key differences from PRCA: (1) RAGPart operates at the retrieval/embedding stage, PRCA at the generation/calibration stage; (2) RAGPart outputs filtered retrieval sets, PRCA outputs {answer, abstain} decisions with coverage certificates; (3) RAGPart and PRCA are complementary—RAGPart can serve as a retrieval-stage preprocessor before PRCA's generation-stage certified abstention.

**Attack landscape:** PoisonedRAG (USENIX Security 2025) achieves 90%+ ASR with 5 poisoned documents on NQ/HotpotQA/MS-MARCO. CorruptRAG (arXiv 2025) achieves high ASR with a single document. RSB Benchmark (May 2025) systematically evaluated 13 attack methods across targeted poisoning, DoS, and trigger-based categories, finding current defenses have residual risk. Semantic Chameleon (arXiv Mar 2026) introduced gradient-guided corpus-dependent attacks.

**Distribution-shift-robust CP:** Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv 2502.14105) provides a framework for robust CP under distribution shifts by propagating ambiguity sets through scoring functions, reducing high-dimensional shifts to one-dimensional score distribution shifts. PRCA's partition-induced TV bound can be viewed as a specific instantiation of this reduction paradigm for adversarial retrieval corruption.

No existing work combines conformal abstention with retrieval-poisoning robustness.

## Proposed Approach

**Step 1: Partition-and-Generate.** Given top-n retrieved passages, partition them into K disjoint groups (random assignment). For each group, generate an answer via an isolated LLM call.

**Step 2: Agreement Nonconformity Score.** Compute a nonconformity score based on inter-group answer agreement. Specifically, for each pair of groups (i, j), compute the NLI entailment probability e(i,j) = P(answer_i entails answer_j) using a lightweight NLI model (e.g., DeBERTa-v3, following ReliabilityRAG's NLI approach). The agreement score is defined as:

s = 1 − (mean of e(i,j) over all pairs)

This score has two critical properties: (1) **Monotonicity**: s is monotone in the abstention threshold λ (higher s → more disagreement → more likely to abstain), satisfying CRC's requirement; (2) **Corruption-boundedness**: under k-poisoning, at most m = ceil(k / floor(n/K)) groups are corrupted, affecting at most m(K−1) of the K(K−1)/2 pairwise comparisons, yielding a bounded perturbation to s.

**Key assumption and mitigation:** The agreement score assumes that LLM outputs for clean passages are sufficiently consistent across groups. If different groups cover different facets of the answer, clean-condition variance inflates s and may cause unnecessary abstention. We mitigate this by using NLI-based semantic entailment (rather than exact match) for agreement computation, which is robust to surface-level variation. Calibration on clean data naturally accounts for residual clean-condition variance in the score distribution.

**Step 3: TV-Bounded Calibration.** Under k-poisoning with K groups, the corruption bound m determines the maximal TV distance between clean and poisoned score CDFs: TV ≤ m/K. Using CRC (ICLR 2024) with TV-inflated quantile: set abstention threshold at the (1 − α + TV)-quantile of calibration scores, yielding formal coverage certificate P(correct or abstain) ≥ 1 − α even under k-poisoning.

**Step 4: Abstention Decision.** At test time, if s > λ (calibrated threshold), abstain; otherwise, output the majority answer across groups.

## Experimental Design

**Datasets:** NQ, HotpotQA, MS-MARCO (standard RAG evaluation benchmarks, used by PoisonedRAG and RobustRAG).

**Attack methods:** (1) PoisonedRAG (targeted poisoning, varying k ∈ {1, 3, 5, 10}); (2) CorruptRAG (single-document high-ASR attack); (3) at least one DoS-type attack from RSB Benchmark (May 2025) taxonomy to test behavior under denial-of-service adversaries. Discussion section analyzes k-poisoning assumption validity across attack categories.

**Models:** Three scales to verify model-agnosticism: (1) primary experiments on Qwen3.5-7B (or Llama-3-8B); (2) medium-scale validation on Qwen3.5-32B; (3) large-scale validation on Qwen3.5-72B. NLI model: DeBERTa-v3-large for agreement scoring.

**Baselines (7 methods):**
- Conformal methods: TRAQ (NAACL 2024), C-RAG (ICML 2024), Conformal-RAG (SIGIR 2025)
- Certified defenses: RobustRAG (SaTML 2026), ReliabilityRAG (NeurIPS 2025)
- Partition-based: RAGPart (arXiv:2512.24268) — same partition strategy, no conformal calibration (ablation baseline)
- Compute-normalized: TRAQ + K× self-consistency voting (controls for PRCA's K× inference cost)

**Calibration protocol:** Calibration set constructed on clean corpus (standard assumption per RPS, ICLR 2025), n_cal ≥ 500 per dataset. Sensitivity experiment: evaluate coverage degradation when actual poisoning budget exceeds assumed k upper bound.

**Metrics:**
- Primary: Certified coverage rate, empirical coverage rate under attack, abstention rate
- Secondary: Clean accuracy (no attack), prediction set size, vacuousness rate (per Chen et al. 2026)
- Tradeoff curves: coverage vs. abstention rate at varying α; coverage vs. poisoning budget k; certified vs. empirical robustness gap
- Efficiency: wall-clock time per query, token consumption per query

**Ablation matrix:**
- K ∈ {3, 5, 7, 10}: partition count vs. coverage/abstention tradeoff
- n ∈ {10, 20, 30}: retrieval depth vs. certificate tightness
- Score function: NLI entailment (primary) vs. ROUGE-L vs. exact match
- Calibration: CRC + TV inflation vs. CRC without inflation vs. vanilla split conformal
- Partition strategy: random vs. round-robin by retrieval score

**Scale:** 200-300 queries per dataset per setting (comparable to RobustRAG's 100/dataset), with 95% confidence intervals reported.

## Key References

- TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction (NAACL 2024)
- C-RAG: Certified Generation Risks for RAG (ICML 2024)
- Conformal Risk Control (ICLR 2024)
- Provably Reliable Conformal Prediction Sets under Poisoning (ICLR 2025 Spotlight)
- Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)
- ReliabilityRAG (NeurIPS 2025)
- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, Mar 2026)
- Conformal-RAG: Conditional Conformal Factuality (SIGIR 2025)
- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv 2025)
- PoisonedRAG (USENIX Security 2025)
- RSB Benchmark: Benchmarking Poisoning Attacks against RAG (May 2025)
- RAGPart & RAGMask (arXiv:2512.24268, Dec 2025)
- Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105)
- Semantic Chameleon (arXiv Mar 2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "d9bfa27c-29ba-4e5b-89eb-5fa47539ed71",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:24:55.633Z_

```json
{
  "parentUuid": "d9bfa27c-29ba-4e5b-89eb-5fa47539ed71",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "bff92ca5-c683-420c-92c1-f8a075178a46",
  "timestamp": "2026-05-30T07:24:55.633Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:24:55.633Z_

```json
{
  "parentUuid": "bff92ca5-c683-420c-92c1-f8a075178a46",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ea1183b2-a52c-4717-8abf-52bb2630f18f",
  "timestamp": "2026-05-30T07:24:55.633Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Assistant

_source line 7 · 2026-05-30T07:25:07.388Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "发掘 agent" (Discovery Agent) to analyze this research proposal about "Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores" (PRCA). 

My job is to:
1. First do thorough literature research via WebSearch
2. Evaluate the idea's novelty, significance, and related work differentiation
3. Find potential angles to strengthen the idea's ceiling
4. Be objective - if the idea is already solid, say so

Let me start by reading the proposal carefully, then do WebSearch to understand the current landscape.


Now I'm understanding the core mechanism: PRCA addresses a gap where existing conformal prediction methods for RAG don't account for poisoned corpora, while current robust RAG defenses lack formal coverage guarantees. The approach partitions retrieved passages to measure agreement patterns, bounds how the score distribution shifts under poisoning, and applies conformal prediction to deliver certified coverage even when the retrieval corpus is compromised. Let me search the literature to see what's already been done in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea1183b2-a52c-4717-8abf-52bb2630f18f",
  "isSidechain": false,
  "requestId": "req_011CbYMWSa8VoWSpZ6rAiTQ8",
  "type": "assistant",
  "uuid": "8e32c441-7dca-4371-9f9d-586da8a6e57a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEwj2PZiKVZs2h9TD8L4wX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4456,
      "cache_read_input_tokens": 14184,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 4456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4456
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

### Assistant

_source line 8 · 2026-05-30T07:25:07.392Z_

I need to first do thorough literature research before making any judgments. Let me search for the most relevant recent work in this space.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e32c441-7dca-4371-9f9d-586da8a6e57a",
  "isSidechain": false,
  "requestId": "req_011CbYMWSa8VoWSpZ6rAiTQ8",
  "type": "assistant",
  "uuid": "7e79c48b-1200-4136-9dd3-26a0c389f233",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEwj2PZiKVZs2h9TD8L4wX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4456,
      "cache_read_input_tokens": 14184,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 4456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4456
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

### Tool call

_source line 9 · 2026-05-30T07:25:07.537Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016iFYLtUpEBXdEuyZymUVLi`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e79c48b-1200-4136-9dd3-26a0c389f233",
  "isSidechain": false,
  "requestId": "req_011CbYMWSa8VoWSpZ6rAiTQ8",
  "type": "assistant",
  "uuid": "a9f4ffe1-649e-439d-a28d-a85674dc0dd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEwj2PZiKVZs2h9TD8L4wX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4456,
      "cache_read_input_tokens": 14184,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 4456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4456
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

_source line 10 · 2026-05-30T07:25:07.547Z_

<details><summary>↩ Tool result · `toolu_016iFYLtUpEBXdEuyZymUVLi`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9f4ffe1-649e-439d-a28d-a85674dc0dd3",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "676f484a-c467-4514-992a-d5f172f105e7",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "a9f4ffe1-649e-439d-a28d-a85674dc0dd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "676f484a-c467-4514-992a-d5f172f105e7",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Assistant

_source line 13 · 2026-05-30T07:25:14.113Z_

Now let me conduct my front-loaded literature research. I'll search for the most relevant recent work across several dimensions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "676f484a-c467-4514-992a-d5f172f105e7",
  "isSidechain": false,
  "requestId": "req_011CbYMXKU2YX84k6oUijiiy",
  "type": "assistant",
  "uuid": "cdb11fbf-4fa6-4ca9-9d00-db7824c4a048",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYpWJgSK1xQgiYrQFQ6CZu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 18640,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 18640,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 894
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

### Tool call

_source line 14 · 2026-05-30T07:25:14.812Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hziz7ULmzyREASVcRLDJnP`</summary>

```json
{
  "query": "conformal prediction RAG retrieval augmented generation robustness poisoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdb11fbf-4fa6-4ca9-9d00-db7824c4a048",
  "isSidechain": false,
  "requestId": "req_011CbYMXKU2YX84k6oUijiiy",
  "type": "assistant",
  "uuid": "53a2a2fb-87e7-45ce-b3c2-97f932cbef42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYpWJgSK1xQgiYrQFQ6CZu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 18640,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 18640,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 894
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

_source line 15 · 2026-05-30T07:25:23.552Z_

<details><summary>↩ Tool result · `toolu_01Hziz7ULmzyREASVcRLDJnP`</summary>

```text
Web search results for query: "conformal prediction RAG retrieval augmented generation robustness poisoning 2025 2026"

Links: [{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/html/2412.16708v2"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957v2"},{"title":"[2412.16708] Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/abs/2412.16708"}]

Based on the search results, I found several relevant papers and resources addressing conformal prediction, RAG (Retrieval-Augmented Generation), robustness, and poisoning attacks from 2025-2026:

## Conformal Prediction & RAG

Conformal-RAG leverages conformal prediction (CP) and internal information from the RAG mechanism to offer statistical guarantees on response quality, ensuring group-conditional coverage spanning multiple sub-domains without requiring manual labelling. Conformal prediction provides a stronger theoretical foundation for ensuring soundness of evaluations through statistical guarantees.

## RAG Robustness & Poisoning Attacks

RAG systems are vulnerable to various adversarial poisoning attacks, where by injecting adversarial data into the underlying RAG database, attackers can manipulate the retriever to return factually incorrect information, thereby reducing model accuracy and propagating disinformation.

Recent defenses include RAGPart, which leverages the inherent training dynamics of dense retrievers through document partitioning to mitigate the effect of poisoned points, and RAGMask, which identifies suspicious tokens based on significant similarity shifts under targeted token masking.

## Recent Resources

There is research on Conformalized Answer Set Prediction for Knowledge Graph Embedding from 2024, and recent work includes papers on "RAG Safety: Exploring Knowledge Poisoning Attacks to Retrieval-Augmented Generation" (2026) and "Understanding Data Poisoning Attacks for RAG: Insights and Algorithms" (2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53a2a2fb-87e7-45ce-b3c2-97f932cbef42",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "b3002bab-dacf-4cb8-b01f-248e51e9a22d",
  "toolUseResult": {
    "query": "conformal prediction RAG retrieval augmented generation robustness poisoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019WbcZasYMVpr92AZumtNXv",
        "content": [
          {
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/html/2412.16708v2"
          },
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978v1"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2504.03957v2"
          },
          {
            "title": "[2412.16708] Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/abs/2412.16708"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources addressing conformal prediction, RAG (Retrieval-Augmented Generation), robustness, and poisoning attacks from 2025-2026:\n\n## Conformal Prediction & RAG\n\nConformal-RAG leverages conformal prediction (CP) and internal information from the RAG mechanism to offer statistical guarantees on response quality, ensuring group-conditional coverage spanning multiple sub-domains without requiring manual labelling. Conformal prediction provides a stronger theoretical foundation for ensuring soundness of evaluations through statistical guarantees.\n\n## RAG Robustness & Poisoning Attacks\n\nRAG systems are vulnerable to various adversarial poisoning attacks, where by injecting adversarial data into the underlying RAG database, attackers can manipulate the retriever to return factually incorrect information, thereby reducing model accuracy and propagating disinformation.\n\nRecent defenses include RAGPart, which leverages the inherent training dynamics of dense retrievers through document partitioning to mitigate the effect of poisoned points, and RAGMask, which identifies suspicious tokens based on significant similarity shifts under targeted token masking.\n\n## Recent Resources\n\nThere is research on Conformalized Answer Set Prediction for Knowledge Graph Embedding from 2024, and recent work includes papers on \"RAG Safety: Exploring Knowledge Poisoning Attacks to Retrieval-Augmented Generation\" (2026) and \"Understanding Data Poisoning Attacks for RAG: Insights and Algorithms\" (2025)."
    ],
    "durationSeconds": 8.732303514,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "53a2a2fb-87e7-45ce-b3c2-97f932cbef42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-30T07:25:26.378Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SfsFA2c8TvsfKYe3dXmueA`</summary>

```json
{
  "query": "Chen et al. \"Is Conformal Factuality for RAG-based LLMs Robust\" arXiv 2603.16817 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3002bab-dacf-4cb8-b01f-248e51e9a22d",
  "isSidechain": false,
  "requestId": "req_011CbYMYVz5DuU76xcJoBD8A",
  "type": "assistant",
  "uuid": "d6afa4cf-80c6-4f18-9302-d62d05817fcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKUENMAdnAN9DgfSmKi1N6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 19534,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 19534,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 17 · 2026-05-30T07:25:32.461Z_

<details><summary>↩ Tool result · `toolu_01SfsFA2c8TvsfKYe3dXmueA`</summary>

```text
Web search results for query: "Chen et al. "Is Conformal Factuality for RAG-based LLMs Robust" arXiv 2603.16817 2026"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"RAC: Efficient LLM Factuality Correction with Retrieval Augmentation","url":"https://arxiv.org/pdf/2410.15667"},{"title":"IRB: Automated Generation of Robust Factuality Benchmarks","url":"https://arxiv.org/pdf/2602.08070"},{"title":"Evaluating the Retrieval Robustness of Large Language Models","url":"https://arxiv.org/pdf/2505.21870"}]

I found the paper you're looking for. The paper "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" is authored by Yi Chen and 4 other authors.

The paper addresses how large language models frequently hallucinate, and examines retrieval-augmented generation (RAG) and conformal factuality as potential solutions. The research finds that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, that conformal factuality guarantees are not robust to distribution shifts and distractors, and that lightweight entailment-based verifiers can match or outperform LLM-based confidence scorers while requiring over 100× fewer FLOPs.

The paper was published on March 17, 2026, and is available on arXiv at https://arxiv.org/abs/2603.16817.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6afa4cf-80c6-4f18-9302-d62d05817fcf",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "ef225538-2b4e-45ad-abc8-bab4ac899509",
  "toolUseResult": {
    "query": "Chen et al. \"Is Conformal Factuality for RAG-based LLMs Robust\" arXiv 2603.16817 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CxrfP8TSkmrhqJJ9g2csXs",
        "content": [
          {
            "title": "[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/abs/2603.16817"
          },
          {
            "title": "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/pdf/2603.16817"
          },
          {
            "title": "RAC: Efficient LLM Factuality Correction with Retrieval Augmentation",
            "url": "https://arxiv.org/pdf/2410.15667"
          },
          {
            "title": "IRB: Automated Generation of Robust Factuality Benchmarks",
            "url": "https://arxiv.org/pdf/2602.08070"
          },
          {
            "title": "Evaluating the Retrieval Robustness of Large Language Models",
            "url": "https://arxiv.org/pdf/2505.21870"
          }
        ]
      },
      "I found the paper you're looking for. The paper \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\" is authored by Yi Chen and 4 other authors.\n\nThe paper addresses how large language models frequently hallucinate, and examines retrieval-augmented generation (RAG) and conformal factuality as potential solutions. The research finds that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, that conformal factuality guarantees are not robust to distribution shifts and distractors, and that lightweight entailment-based verifiers can match or outperform LLM-based confidence scorers while requiring over 100× fewer FLOPs.\n\nThe paper was published on March 17, 2026, and is available on arXiv at https://arxiv.org/abs/2603.16817."
    ],
    "durationSeconds": 6.079020654,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d6afa4cf-80c6-4f18-9302-d62d05817fcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-30T07:25:35.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017mxi7f6RNVbtNPShK4cj9d`</summary>

```json
{
  "query": "RobustRAG \"certifiably robust\" retrieval corruption SaTML 2026 isolate-then-aggregate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef225538-2b4e-45ad-abc8-bab4ac899509",
  "isSidechain": false,
  "requestId": "req_011CbYMZ9v7DAXypUEn9UNmy",
  "type": "assistant",
  "uuid": "49aae8e7-894b-4ade-8ae2-d7f55f1c0c31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01273P5Ek5S1tiG3r8k3ZFDx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 20383,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 20383,
          "cache_creation_input_tokens": 583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 583
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

_source line 19 · 2026-05-30T07:25:44.809Z_

<details><summary>↩ Tool result · `toolu_017mxi7f6RNVbtNPShK4cj9d`</summary>

```text
Web search results for query: "RobustRAG "certifiably robust" retrieval corruption SaTML 2026 isolate-then-aggregate"

Links: [{"title":"IEEE SaTML 2026 · Accepted Papers","url":"https://satml.org/accepted-papers/"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v2"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"Tong Wu - Homepage - Princeton","url":"https://tongwu2020.github.io/tongwu/"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"},{"title":"ICML Certifiably Robust RAG against Retrieval Corruption","url":"https://icml.cc/virtual/2024/37487"}]

Based on the search results, here's what I found about RobustRAG:

## Overview

RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.

## Key Innovation: Isolate-Then-Aggregate Strategy

The key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then these responses are securely aggregated for a robust output.

## Implementation

To instantiate RobustRAG, keyword-based and decoding-based algorithms are designed for securely aggregating unstructured text responses.

## Certifiable Robustness

RobustRAG achieves certifiable robustness: for certain queries in evaluation datasets, non-trivial lower bounds on response quality can be formally certified—even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages.

## Evaluation

RobustRAG was evaluated on the tasks of open-domain question-answering and free-form long text generation across three datasets and three LLMs. RobustRAG achieved 69.0–71.0% certifiable robust accuracy for multiple-choice QA, 24.0–49.0% for short-answer QA, 27.0–47.0% for Natural Questions, and 24.0–51.2% certifiable LLM-judge score for biography generation.

The paper was accepted to SaTML 2026 and was authored by researchers from NVIDIA, Princeton University, and UC Berkeley.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49aae8e7-894b-4ade-8ae2-d7f55f1c0c31",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "6e4e6001-f3d6-444b-989a-5e3f719d7a90",
  "toolUseResult": {
    "query": "RobustRAG \"certifiably robust\" retrieval corruption SaTML 2026 isolate-then-aggregate",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G1JcK9TSF5fRckFVPvQBaU",
        "content": [
          {
            "title": "IEEE SaTML 2026 · Accepted Papers",
            "url": "https://satml.org/accepted-papers/"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"
          },
          {
            "title": "[2405.15556] Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/abs/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/html/2405.15556v2"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview",
            "url": "https://openreview.net/forum?id=cU6ZdN87p3"
          },
          {
            "title": "Tong Wu - Homepage - Princeton",
            "url": "https://tongwu2020.github.io/tongwu/"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://openreview.net/pdf?id=qsEeACAJjD"
          },
          {
            "title": "ICML Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://icml.cc/virtual/2024/37487"
          }
        ]
      },
      "Based on the search results, here's what I found about RobustRAG:\n\n## Overview\n\nRobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.\n\n## Key Innovation: Isolate-Then-Aggregate Strategy\n\nThe key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then these responses are securely aggregated for a robust output.\n\n## Implementation\n\nTo instantiate RobustRAG, keyword-based and decoding-based algorithms are designed for securely aggregating unstructured text responses.\n\n## Certifiable Robustness\n\nRobustRAG achieves certifiable robustness: for certain queries in evaluation datasets, non-trivial lower bounds on response quality can be formally certified—even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages.\n\n## Evaluation\n\nRobustRAG was evaluated on the tasks of open-domain question-answering and free-form long text generation across three datasets and three LLMs. RobustRAG achieved 69.0–71.0% certifiable robust accuracy for multiple-choice QA, 24.0–49.0% for short-answer QA, 27.0–47.0% for Natural Questions, and 24.0–51.2% certifiable LLM-judge score for biography generation.\n\nThe paper was accepted to SaTML 2026 and was authored by researchers from NVIDIA, Princeton University, and UC Berkeley."
    ],
    "durationSeconds": 9.603459671000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "49aae8e7-894b-4ade-8ae2-d7f55f1c0c31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-30T07:25:47.278Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018UrP6wGY2ch1LnayhHKYq5`</summary>

```json
{
  "query": "conformal risk control CRC distribution shift total variation robust conformal prediction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e4e6001-f3d6-444b-989a-5e3f719d7a90",
  "isSidechain": false,
  "requestId": "req_011CbYMa53C8j68f8ZV8Edyy",
  "type": "assistant",
  "uuid": "ba945b86-45f2-46f7-bc59-37e0cbad1b64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bKaS7XdmAgmGkzW3ofgWq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 914,
      "cache_read_input_tokens": 20966,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 20966,
          "cache_creation_input_tokens": 914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 914
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

_source line 21 · 2026-05-30T07:25:55.207Z_

<details><summary>↩ Tool result · `toolu_018UrP6wGY2ch1LnayhHKYq5`</summary>

```text
Web search results for query: "conformal risk control CRC distribution shift total variation robust conformal prediction 2024 2025"

Links: [{"title":"Calibrating Decision Robustness via Inverse Conformal Risk Control","url":"https://arxiv.org/html/2510.07750"},{"title":"arXiv:2208.02814v4 [stat.ME] 13 Jun 2025 Conformal Risk Control","url":"https://arxiv.org/pdf/2208.02814"},{"title":"Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/pdf/2502.14105"},{"title":"Anytime-Valid Conformal Risk Control","url":"https://arxiv.org/html/2602.04364v1"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"}]

Here are the search results for your query:

**Recent Research on Conformal Risk Control and Distribution Shift (2024-2025):**

1. **Conformal Risk Control Framework**: Conformal risk control extends conformal prediction to control the expected value of any monotone loss function. Recent work has substantially extended the CRC framework in multiple directions, including studies on non-exchangeable data, adaptive CRC procedures, multidimensional outputs, cross-validation-based approaches, control over tail-sensitive risks, and applications to image segmentation.

2. **Robustness Under Distribution Shifts**: Recent research provides an overview of Lévy-Prokhorov (LP) ambiguity sets and their connections to Wasserstein and Total Variation metrics, showing that propagating LP ambiguity sets through the scoring function reduces high-dimensional distribution shifts to manageable one-dimensional shifts, enabling construction of robust conformal prediction intervals that remain valid under distribution shifts.

3. **Recent Developments**: Calibration-conditional miscoverage control under distribution shifts was recently achieved in Pournaderi & Xiang (2026). Additionally, recent works include probabilistic conformal prediction in predict-then-optimize pipelines, conformal prediction-based robust control for linear-quadratic regulator systems, decision-focused frameworks that leverage conformal prediction to guarantee robustness, and multi-layer robust optimization formulations.

These sources demonstrate active ongoing research in combining conformal prediction methods with robustness guarantees under distribution shifts, particularly using total variation and other distance metrics for uncertainty quantification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba945b86-45f2-46f7-bc59-37e0cbad1b64",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "7bd44d2d-4dec-4f5f-8e6b-56b5c78be827",
  "toolUseResult": {
    "query": "conformal risk control CRC distribution shift total variation robust conformal prediction 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VZ5DDKv8dEFK8wSPmF5iCp",
        "content": [
          {
            "title": "Calibrating Decision Robustness via Inverse Conformal Risk Control",
            "url": "https://arxiv.org/html/2510.07750"
          },
          {
            "title": "arXiv:2208.02814v4 [stat.ME] 13 Jun 2025 Conformal Risk Control",
            "url": "https://arxiv.org/pdf/2208.02814"
          },
          {
            "title": "Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/pdf/2502.14105"
          },
          {
            "title": "Anytime-Valid Conformal Risk Control",
            "url": "https://arxiv.org/html/2602.04364v1"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          }
        ]
      },
      "Here are the search results for your query:\n\n**Recent Research on Conformal Risk Control and Distribution Shift (2024-2025):**\n\n1. **Conformal Risk Control Framework**: Conformal risk control extends conformal prediction to control the expected value of any monotone loss function. Recent work has substantially extended the CRC framework in multiple directions, including studies on non-exchangeable data, adaptive CRC procedures, multidimensional outputs, cross-validation-based approaches, control over tail-sensitive risks, and applications to image segmentation.\n\n2. **Robustness Under Distribution Shifts**: Recent research provides an overview of Lévy-Prokhorov (LP) ambiguity sets and their connections to Wasserstein and Total Variation metrics, showing that propagating LP ambiguity sets through the scoring function reduces high-dimensional distribution shifts to manageable one-dimensional shifts, enabling construction of robust conformal prediction intervals that remain valid under distribution shifts.\n\n3. **Recent Developments**: Calibration-conditional miscoverage control under distribution shifts was recently achieved in Pournaderi & Xiang (2026). Additionally, recent works include probabilistic conformal prediction in predict-then-optimize pipelines, conformal prediction-based robust control for linear-quadratic regulator systems, decision-focused frameworks that leverage conformal prediction to guarantee robustness, and multi-layer robust optimization formulations.\n\nThese sources demonstrate active ongoing research in combining conformal prediction methods with robustness guarantees under distribution shifts, particularly using total variation and other distance metrics for uncertainty quantification."
    ],
    "durationSeconds": 7.9229980159999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ba945b86-45f2-46f7-bc59-37e0cbad1b64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-30T07:25:58.233Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XVJpJCvmSi2Vv3xYK4i75r`</summary>

```json
{
  "query": "ReliabilityRAG NeurIPS 2025 graph-theoretic MIS NLI contradiction detection robust RAG"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bd44d2d-4dec-4f5f-8e6b-56b5c78be827",
  "isSidechain": false,
  "requestId": "req_011CbYMaqCn2eUYNGEw4JqzT",
  "type": "assistant",
  "uuid": "d3484354-7ff8-4634-8a7a-56c8a978dd2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CoPc3bcf8N5fqAE7JUtSx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 21880,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 21880,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 23 · 2026-05-30T07:26:08.421Z_

<details><summary>↩ Tool result · `toolu_01XVJpJCvmSi2Vv3xYK4i75r`</summary>

```text
Web search results for query: "ReliabilityRAG NeurIPS 2025 graph-theoretic MIS NLI contradiction detection robust RAG"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/media/neurips-2025/Slides/119236.pdf"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/poster/119236"},{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"Contradiction Detection in RAG Systems: Evaluating LLMs as Context   Validators for Improved Information Consistency","url":"https://arxiv.org/pdf/2504.00180"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Retrieval-Augmented Generation with Estimation of Source Reliability","url":"https://arxiv.org/pdf/2410.22954"}]

Based on the search results, here's what I found about ReliabilityRAG and NeurIPS 2025:

## ReliabilityRAG Overview

ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. Retrieval-Augmented Generation (RAG) enhances Large Language Models by grounding their outputs in external documents, though these systems remain vulnerable to attacks on the retrieval corpus, such as prompt injection.

## Graph-Theoretic Approach with MIS

The framework adopts a graph-theoretic perspective to identify a "consistent majority" among retrieved documents to filter out malicious ones, introducing a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction.

## NLI and Contradiction Detection

The approach constructs a graph where each document is a vertex with edges drawn between contradictory documents, uses an NLI model to check contradictions, and finds a maximum independent set in the graph. For the NLI model, the work uses DeBERTa-v3-large-mnli-fever-anli-ling-wanli, which achieves state-of-the-art 91.2% / 90.8% accuracy on MNLI-M/MM test splits and 70.2% on the ANLI test set (adversarial).

## Robustness Guarantees

The MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions. ReliabilityRAG via MIS is provably robust since the probability of selecting a malicious document vanishes as the number of retrieved documents k grows large.

The work appears in NeurIPS 2025 and is also available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3484354-7ff8-4634-8a7a-56c8a978dd2a",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "0c41fd36-4259-474c-9554-f3b1a037e75c",
  "toolUseResult": {
    "query": "ReliabilityRAG NeurIPS 2025 graph-theoretic MIS NLI contradiction detection robust RAG",
    "results": [
      {
        "tool_use_id": "srvtoolu_017om92cvLw8dC8et5SRM4ig",
        "content": [
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview",
            "url": "https://openreview.net/forum?id=D9JeNTs5Bu"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/media/neurips-2025/Slides/119236.pdf"
          },
          {
            "title": "NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/virtual/2025/poster/119236"
          },
          {
            "title": "[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/abs/2509.23519"
          },
          {
            "title": "Contradiction Detection in RAG Systems: Evaluating LLMs as Context   Validators for Improved Information Consistency",
            "url": "https://arxiv.org/pdf/2504.00180"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "Retrieval-Augmented Generation with Estimation of Source Reliability",
            "url": "https://arxiv.org/pdf/2410.22954"
          }
        ]
      },
      "Based on the search results, here's what I found about ReliabilityRAG and NeurIPS 2025:\n\n## ReliabilityRAG Overview\n\nReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. Retrieval-Augmented Generation (RAG) enhances Large Language Models by grounding their outputs in external documents, though these systems remain vulnerable to attacks on the retrieval corpus, such as prompt injection.\n\n## Graph-Theoretic Approach with MIS\n\nThe framework adopts a graph-theoretic perspective to identify a \"consistent majority\" among retrieved documents to filter out malicious ones, introducing a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction.\n\n## NLI and Contradiction Detection\n\nThe approach constructs a graph where each document is a vertex with edges drawn between contradictory documents, uses an NLI model to check contradictions, and finds a maximum independent set in the graph. For the NLI model, the work uses DeBERTa-v3-large-mnli-fever-anli-ling-wanli, which achieves state-of-the-art 91.2% / 90.8% accuracy on MNLI-M/MM test splits and 70.2% on the ANLI test set (adversarial).\n\n## Robustness Guarantees\n\nThe MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions. ReliabilityRAG via MIS is provably robust since the probability of selecting a malicious document vanishes as the number of retrieved documents k grows large.\n\nThe work appears in NeurIPS 2025 and is also available on arXiv."
    ],
    "durationSeconds": 10.182633686999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d3484354-7ff8-4634-8a7a-56c8a978dd2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "0c41fd36-4259-474c-9554-f3b1a037e75c",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Tool call

_source line 26 · 2026-05-30T07:26:10.934Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CHnrWr3vq9e4UJbPUJYgQS`</summary>

```json
{
  "query": "\"provably reliable conformal prediction\" poisoning RPS ICLR 2025 spotlight smoothed scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c41fd36-4259-474c-9554-f3b1a037e75c",
  "isSidechain": false,
  "requestId": "req_011CbYMbohmG9zUkuEzRE4XC",
  "type": "assistant",
  "uuid": "6832698a-59b6-4ef8-903d-734674883152",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2RTReU9PWWddjeBit5yZm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 934,
      "cache_read_input_tokens": 22580,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 934,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 22580,
          "cache_creation_input_tokens": 934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 934
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

_source line 27 · 2026-05-30T07:26:23.516Z_

<details><summary>↩ Tool result · `toolu_01CHnrWr3vq9e4UJbPUJYgQS`</summary>

```text
Web search results for query: ""provably reliable conformal prediction" poisoning RPS ICLR 2025 spotlight smoothed scores"

Links: [{"title":"GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).","url":"https://github.com/yascho/reliable_conformal_prediction"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview","url":"https://openreview.net/forum?id=ofuLWn8DFZ"},{"title":"PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich","url":"https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://iclr.cc/virtual/2025/poster/28340"},{"title":"Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning","url":"https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"},{"title":"[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://arxiv.org/abs/2410.09878"},{"title":"provably reliable conformal prediction sets","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"}]

Based on the web search results, I found comprehensive information about this paper. Here's what the research is about:

## Overview

The paper "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning" was accepted as a Spotlight at ICLR 2025 and proposes the first efficient method for making conformal prediction sets more reliable against data poisoning and label flipping attacks.

## The Problem

Conformal prediction provides model-agnostic and distribution-free uncertainty quantification through prediction sets guaranteed to include the ground truth with any user-specified probability. Yet, conformal prediction is not reliable under poisoning attacks where adversaries manipulate both training and calibration data, which can significantly alter prediction sets in practice.

## The Solution: Reliable Prediction Sets (RPS)

The authors propose reliable prediction sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. To ensure reliability under training poisoning, they introduce smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data. To ensure reliability under calibration poisoning, they construct multiple prediction sets, each calibrated on distinct subsets of the calibration data.

## Key Contributions

The researchers derive novel certificates that guarantee the reliability of RPS under worst-case data poisoning attacks, including guarantees against label flipping attacks.

The GitHub repository with the implementation is available at https://github.com/yascho/reliable_conformal_prediction, and the paper is accessible through OpenReview and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6832698a-59b6-4ef8-903d-734674883152",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "6300dc1d-99d3-4a5d-a6b9-2c6aa626a694",
  "toolUseResult": {
    "query": "\"provably reliable conformal prediction\" poisoning RPS ICLR 2025 spotlight smoothed scores",
    "results": [
      {
        "tool_use_id": "srvtoolu_017RADQoguxbrgkQSaAz9iwX",
        "content": [
          {
            "title": "GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).",
            "url": "https://github.com/yascho/reliable_conformal_prediction"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview",
            "url": "https://openreview.net/forum?id=ofuLWn8DFZ"
          },
          {
            "title": "PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich",
            "url": "https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://iclr.cc/virtual/2025/poster/28340"
          },
          {
            "title": "Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning",
            "url": "https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"
          },
          {
            "title": "[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://arxiv.org/abs/2410.09878"
          },
          {
            "title": "provably reliable conformal prediction sets",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the web search results, I found comprehensive information about this paper. Here's what the research is about:\n\n## Overview\n\nThe paper \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" was accepted as a Spotlight at ICLR 2025 and proposes the first efficient method for making conformal prediction sets more reliable against data poisoning and label flipping attacks.\n\n## The Problem\n\nConformal prediction provides model-agnostic and distribution-free uncertainty quantification through prediction sets guaranteed to include the ground truth with any user-specified probability. Yet, conformal prediction is not reliable under poisoning attacks where adversaries manipulate both training and calibration data, which can significantly alter prediction sets in practice.\n\n## The Solution: Reliable Prediction Sets (RPS)\n\nThe authors propose reliable prediction sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. To ensure reliability under training poisoning, they introduce smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data. To ensure reliability under calibration poisoning, they construct multiple prediction sets, each calibrated on distinct subsets of the calibration data.\n\n## Key Contributions\n\nThe researchers derive novel certificates that guarantee the reliability of RPS under worst-case data poisoning attacks, including guarantees against label flipping attacks.\n\nThe GitHub repository with the implementation is available at https://github.com/yascho/reliable_conformal_prediction, and the paper is accessible through OpenReview and arXiv."
    ],
    "durationSeconds": 12.577484916999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6832698a-59b6-4ef8-903d-734674883152",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-30T07:26:26.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017j6qWkxUm5Cc6fC4tog23m`</summary>

```json
{
  "query": "RAG abstention selective prediction LLM retrieval augmented generation 2025 2026 know when not to answer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6300dc1d-99d3-4a5d-a6b9-2c6aa626a694",
  "isSidechain": false,
  "requestId": "req_011CbYMcvCTrG5kZtQAQcAh4",
  "type": "assistant",
  "uuid": "78d9cfe6-8101-48cc-b6bb-5635762f0eed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmCqcHbZSAfruYpd62RLwr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 23514,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 23514,
          "cache_creation_input_tokens": 970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 970
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

_source line 29 · 2026-05-30T07:26:35.662Z_

<details><summary>↩ Tool result · `toolu_017j6qWkxUm5Cc6fC4tog23m`</summary>

```text
Web search results for query: "RAG abstention selective prediction LLM retrieval augmented generation 2025 2026 know when not to answer"

Links: [{"title":"Deeper insights into retrieval augmented generation: The role of sufficient context","url":"https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/"},{"title":"Know Your Limits: A Survey of Abstention in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/393331033_Know_Your_Limits_A_Survey_of_Abstention_in_Large_Language_Models"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Improving negative rejection ability in language models: A review of fine-tuned LLMs, RAG, and RAFT | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-025-00334-6"},{"title":"When Silence Is Golden: Can LLMs Learn to Abstain in Temporal QA and Beyond? | OpenReview","url":"https://openreview.net/forum?id=PhUCxfS0yf"},{"title":"Selective \"Selective Prediction\": Reducing Unnecessary Abstention in   Vision-Language Reasoning","url":"https://arxiv.org/pdf/2402.15610"},{"title":"Confidence-Based Response Abstinence: Improving LLM Trustworthiness via Activation-Based Uncertainty Estimation","url":"https://arxiv.org/pdf/2510.13750"},{"title":"Contrastive Decoding with Abstention","url":"https://aclanthology.org/2025.acl-long.479.pdf"},{"title":"Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs","url":"https://arxiv.org/pdf/2310.11689"}]

Based on the web search results, here's what I found regarding RAG, selective prediction, abstention, and LLM retrieval-augmented generation in 2025-2026:

## Key Research Developments

**Selective Generation Framework in RAG**

A "selective generation" framework has been developed that leverages sufficient context information to guide abstention. This work appeared at ICLR 2025, studying the idea of "sufficient context" in RAG systems. The research addresses a fundamental challenge: models like Gemma go from providing incorrect answers on 10.2% of questions with no context up to 66.1% when using insufficient context.

**Abstention as a Core Research Area**

The selective prediction and abstention literature asks whether confidence can be used to improve reliability by withholding low-confidence responses. Confidence emerged as the dominant predictor of behavior, with effect sizes an order of magnitude larger than knowledge retrieval accessibility (RAG scores) or surface-level semantic features.

**Temporal Reasoning and Abstention**

A pipeline has been developed that couples Chain-of-Thought supervision with Reinforcement Learning guided by abstention-aware rewards. A new model based on Qwen2.5-1.5B-Instruct outperforms GPT-4o on selective abstention and reasoning on temporal questions.

**Uncertainty Estimation in RAG**

Existing approaches to uncertainty estimation in retrieval-augmented generation have shown promise, but often fall short when the target response is long and narrative in nature. Uncertainty and correctness are fundamentally distinct concepts—a model's low uncertainty does not necessarily imply correctness, and a model may generate a correct response with high uncertainty.

**Addressing RAG Limitations**

RAG anchors models to external documents, but they can still misread, over-generalise, or fabricate claims. Recent work in 2025 has focused on addressing this through training approaches: new reward schemes encourage abstention when evidence is thin instead of penalising "I don't know."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78d9cfe6-8101-48cc-b6bb-5635762f0eed",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "8aaa4b30-bcbb-4f9c-9de8-871f4f828a16",
  "toolUseResult": {
    "query": "RAG abstention selective prediction LLM retrieval augmented generation 2025 2026 know when not to answer",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PkjK4yC5sbT75gAVTc8Tqw",
        "content": [
          {
            "title": "Deeper insights into retrieval augmented generation: The role of sufficient context",
            "url": "https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/"
          },
          {
            "title": "Know Your Limits: A Survey of Abstention in Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/393331033_Know_Your_Limits_A_Survey_of_Abstention_in_Large_Language_Models"
          },
          {
            "title": "LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.",
            "url": "https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"
          },
          {
            "title": "Improving negative rejection ability in language models: A review of fine-tuned LLMs, RAG, and RAFT | Journal of King Saud University Computer and Information Sciences | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s44443-025-00334-6"
          },
          {
            "title": "When Silence Is Golden: Can LLMs Learn to Abstain in Temporal QA and Beyond? | OpenReview",
            "url": "https://openreview.net/forum?id=PhUCxfS0yf"
          },
          {
            "title": "Selective \"Selective Prediction\": Reducing Unnecessary Abstention in   Vision-Language Reasoning",
            "url": "https://arxiv.org/pdf/2402.15610"
          },
          {
            "title": "Confidence-Based Response Abstinence: Improving LLM Trustworthiness via Activation-Based Uncertainty Estimation",
            "url": "https://arxiv.org/pdf/2510.13750"
          },
          {
            "title": "Contrastive Decoding with Abstention",
            "url": "https://aclanthology.org/2025.acl-long.479.pdf"
          },
          {
            "title": "Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs",
            "url": "https://arxiv.org/pdf/2310.11689"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding RAG, selective prediction, abstention, and LLM retrieval-augmented generation in 2025-2026:\n\n## Key Research Developments\n\n**Selective Generation Framework in RAG**\n\nA \"selective generation\" framework has been developed that leverages sufficient context information to guide abstention. This work appeared at ICLR 2025, studying the idea of \"sufficient context\" in RAG systems. The research addresses a fundamental challenge: models like Gemma go from providing incorrect answers on 10.2% of questions with no context up to 66.1% when using insufficient context.\n\n**Abstention as a Core Research Area**\n\nThe selective prediction and abstention literature asks whether confidence can be used to improve reliability by withholding low-confidence responses. Confidence emerged as the dominant predictor of behavior, with effect sizes an order of magnitude larger than knowledge retrieval accessibility (RAG scores) or surface-level semantic features.\n\n**Temporal Reasoning and Abstention**\n\nA pipeline has been developed that couples Chain-of-Thought supervision with Reinforcement Learning guided by abstention-aware rewards. A new model based on Qwen2.5-1.5B-Instruct outperforms GPT-4o on selective abstention and reasoning on temporal questions.\n\n**Uncertainty Estimation in RAG**\n\nExisting approaches to uncertainty estimation in retrieval-augmented generation have shown promise, but often fall short when the target response is long and narrative in nature. Uncertainty and correctness are fundamentally distinct concepts—a model's low uncertainty does not necessarily imply correctness, and a model may generate a correct response with high uncertainty.\n\n**Addressing RAG Limitations**\n\nRAG anchors models to external documents, but they can still misread, over-generalise, or fabricate claims. Recent work in 2025 has focused on addressing this through training approaches: new reward schemes encourage abstention when evidence is thin instead of penalising \"I don't know.\""
    ],
    "durationSeconds": 9.491245050000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "78d9cfe6-8101-48cc-b6bb-5635762f0eed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-30T07:26:35.668Z_

```json
{
  "parentUuid": "8aaa4b30-bcbb-4f9c-9de8-871f4f828a16",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d4560953-23a2-4b33-a0d9-f73820edeac7",
  "timestamp": "2026-05-30T07:26:35.668Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-30T07:26:38.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Es4TS22ZSn8QCNNPyvqgWn`</summary>

```json
{
  "query": "partition-based defense adversarial robustness LLM generation consensus voting conformal guarantee 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4560953-23a2-4b33-a0d9-f73820edeac7",
  "isSidechain": false,
  "requestId": "req_011CbYMdpUCirXU9NrNMag2b",
  "type": "assistant",
  "uuid": "4de5da3d-f252-43e1-9094-c0965a0fcf0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013y2d83j65gcyp8EL23avoa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 24484,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 24484,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
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

_source line 32 · 2026-05-30T07:26:46.318Z_

<details><summary>↩ Tool result · `toolu_01Es4TS22ZSn8QCNNPyvqgWn`</summary>

```text
Web search results for query: "partition-based defense adversarial robustness LLM generation consensus voting conformal guarantee 2025 2026"

Links: [{"title":"Enhancing Robustness of LLM-Driven Multi-Agent Systems through Randomized Smoothing","url":"https://arxiv.org/pdf/2507.04105"},{"title":"Enhancing robustness of LLM-driven multi-agent systems through randomized smoothing - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1000936125003851"},{"title":"Provable Defense Framework for LLM Jailbreaks via Noise-Augumented Alignment","url":"https://arxiv.org/pdf/2602.01587"},{"title":"The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration","url":"https://arxiv.org/html/2604.17139"},{"title":"Provable Robustness Against a Union of $\\ell_0$ Adversarial Attacks","url":"https://arxiv.org/pdf/2302.11628"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/pdf/2506.07804"},{"title":"Towards Assurance of LLM Adversarial Robustness using Ontology-Driven   Argumentation","url":"https://arxiv.org/pdf/2410.07962"},{"title":"[2604.17139] The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration","url":"https://arxiv.org/abs/2604.17139"}]

I found several relevant research papers on adversarial robustness for LLMs from 2025-2026. Here are the key findings:

## Multi-Agent LLM Robustness and Consensus

Multi-agent large language model architectures increasingly rely on response-level aggregation such as majority voting, but this approach has a critical structural vulnerability where response-level aggregation collapses when corrupted agents form a local majority. A recent approach proposes Token-Level Round-Robin Collaboration, where agents sequentially interleave generation within a shared auto-regressive context. This method theoretically proves that the honest model's restorative pull can overpower adversarial corruptions, even when corrupted agents form a majority.

## Randomized Smoothing for LLM Multi-Agent Systems

A defense framework for enhancing the safety of LLM-empowered Multi-Agent Systems in safety-critical domains applies randomized smoothing—a statistical robustness certification technique—to the MAS consensus context, enabling probabilistic guarantees on agent decisions under adversarial influence. The approach operates in black-box settings with a two-stage adaptive sampling mechanism and effectively prevents the propagation of adversarial behaviors and hallucinations while maintaining consensus performance.

## Conformal Prediction for Adversarial Robustness

A conformal prediction-based defensive model significantly enhances robustness against adversarial attacks while maintaining reliable prediction, highlighting effectiveness for developing trustworthy and resilient deep learning models for safety-critical domains.

## Partition-Based Defense

Feature partition aggregation is a certified feature defense that uses an ensemble of submodels trained on disjoint feature sets, with certification schemes based on plurality voting and multi-round elections.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4de5da3d-f252-43e1-9094-c0965a0fcf0f",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "1bf22998-e1a3-47e5-9405-b4b8effc3b7e",
  "toolUseResult": {
    "query": "partition-based defense adversarial robustness LLM generation consensus voting conformal guarantee 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MaV25JpD8zrYqNinvYcH3r",
        "content": [
          {
            "title": "Enhancing Robustness of LLM-Driven Multi-Agent Systems through Randomized Smoothing",
            "url": "https://arxiv.org/pdf/2507.04105"
          },
          {
            "title": "Enhancing robustness of LLM-driven multi-agent systems through randomized smoothing - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S1000936125003851"
          },
          {
            "title": "Provable Defense Framework for LLM Jailbreaks via Noise-Augumented Alignment",
            "url": "https://arxiv.org/pdf/2602.01587"
          },
          {
            "title": "The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration",
            "url": "https://arxiv.org/html/2604.17139"
          },
          {
            "title": "Provable Robustness Against a Union of $\\ell_0$ Adversarial Attacks",
            "url": "https://arxiv.org/pdf/2302.11628"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/pdf/2506.07804"
          },
          {
            "title": "Towards Assurance of LLM Adversarial Robustness using Ontology-Driven   Argumentation",
            "url": "https://arxiv.org/pdf/2410.07962"
          },
          {
            "title": "[2604.17139] The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration",
            "url": "https://arxiv.org/abs/2604.17139"
          }
        ]
      },
      "I found several relevant research papers on adversarial robustness for LLMs from 2025-2026. Here are the key findings:\n\n## Multi-Agent LLM Robustness and Consensus\n\nMulti-agent large language model architectures increasingly rely on response-level aggregation such as majority voting, but this approach has a critical structural vulnerability where response-level aggregation collapses when corrupted agents form a local majority. A recent approach proposes Token-Level Round-Robin Collaboration, where agents sequentially interleave generation within a shared auto-regressive context. This method theoretically proves that the honest model's restorative pull can overpower adversarial corruptions, even when corrupted agents form a majority.\n\n## Randomized Smoothing for LLM Multi-Agent Systems\n\nA defense framework for enhancing the safety of LLM-empowered Multi-Agent Systems in safety-critical domains applies randomized smoothing—a statistical robustness certification technique—to the MAS consensus context, enabling probabilistic guarantees on agent decisions under adversarial influence. The approach operates in black-box settings with a two-stage adaptive sampling mechanism and effectively prevents the propagation of adversarial behaviors and hallucinations while maintaining consensus performance.\n\n## Conformal Prediction for Adversarial Robustness\n\nA conformal prediction-based defensive model significantly enhances robustness against adversarial attacks while maintaining reliable prediction, highlighting effectiveness for developing trustworthy and resilient deep learning models for safety-critical domains.\n\n## Partition-Based Defense\n\nFeature partition aggregation is a certified feature defense that uses an ensemble of submodels trained on disjoint feature sets, with certification schemes based on plurality voting and multi-round elections."
    ],
    "durationSeconds": 7.864600263000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4de5da3d-f252-43e1-9094-c0965a0fcf0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-30T07:26:49.301Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CjYGgsioBaGMYJSh8BVW8e`</summary>

```json
{
  "query": "TRAQ \"trustworthy retrieval augmented\" conformal prediction NAACL 2024 nonconformity score abstention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bf22998-e1a3-47e5-9405-b4b8effc3b7e",
  "isSidechain": false,
  "requestId": "req_011CbYMebhnP8nQUWoDgRFRJ",
  "type": "assistant",
  "uuid": "664fe7b1-b760-4581-b198-66737d378675",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yj13MJ9m6GEo8gx3LgjbW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 25673,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 922,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 25673,
          "cache_creation_input_tokens": 922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 922
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

_source line 34 · 2026-05-30T07:26:54.554Z_

<details><summary>↩ Tool result · `toolu_01CjYGgsioBaGMYJSh8BVW8e`</summary>

```text
Web search results for query: "TRAQ "trustworthy retrieval augmented" conformal prediction NAACL 2024 nonconformity score abstention"

Links: [{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.210/"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Underline","url":"https://underline.io/lecture/97447-traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"},{"title":"[PDF] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TRAQ:-Trustworthy-Retrieval-Augmented-Question-via-Li-Park/28e078b52a761cf3fe5941d3428acb7bbf608f21"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2307.04642"},{"title":"[Quick Review] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://liner.com/review/traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"},{"title":"[2307.04642] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/abs/2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"Accepted Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/program/accepted_papers/"}]

Based on the search results, I found information about the TRAQ paper presented at NAACL 2024:

## TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction

TRAQ (Trustworthy Retrieval Augmented Question Answering) was presented at the 2024 Conference of the North American Chapter of the Association for Computational Linguistics in Mexico City.

**Core Approach:**
TRAQ provides the first end-to-end statistical correctness guarantee for RAG using conformal prediction, a statistical technique for constructing prediction sets guaranteed to contain the semantically correct response with high probability.

**Key Technical Details:**
TRAQ applies conformal prediction separately to the retrieval model (to obtain sets of retrieved passages guaranteed to contain the relevant passage with high probability) and the generator (to obtain sets of answers that contain the true answer with high probability, assuming the relevant passage is given). TRAQ also leverages Bayesian optimization to minimize the size of the constructed sets.

**Nonconformity Measure:**
TRAQ introduces a novel nonconformity measure based on semantic uncertainty, which appears to address the challenge of semantically equivalent answers in natural language.

**Results:**
TRAQ provides the desired correctness guarantee while reducing prediction set size by 16.2% on average.

The paper was authored by Shuo Li, Sangdon Park, Insup Lee, and Osbert Bastani.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "664fe7b1-b760-4581-b198-66737d378675",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "672ff11f-3ab4-4772-b113-8fc4ea13299e",
  "toolUseResult": {
    "query": "TRAQ \"trustworthy retrieval augmented\" conformal prediction NAACL 2024 nonconformity score abstention",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SEVFgiWSFKhiQ3s5vJWkq5",
        "content": [
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.210/"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Underline",
            "url": "https://underline.io/lecture/97447-traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"
          },
          {
            "title": "[PDF] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/TRAQ:-Trustworthy-Retrieval-Augmented-Question-via-Li-Park/28e078b52a761cf3fe5941d3428acb7bbf608f21"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2307.04642"
          },
          {
            "title": "[Quick Review] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://liner.com/review/traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction",
            "url": "https://arxiv.org/pdf/2307.04642"
          },
          {
            "title": "[2307.04642] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/abs/2307.04642"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/html/2307.04642v2"
          },
          {
            "title": "Accepted Papers - NAACL-HLT 2024",
            "url": "https://2024.naacl.org/program/accepted_papers/"
          }
        ]
      },
      "Based on the search results, I found information about the TRAQ paper presented at NAACL 2024:\n\n## TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction\n\nTRAQ (Trustworthy Retrieval Augmented Question Answering) was presented at the 2024 Conference of the North American Chapter of the Association for Computational Linguistics in Mexico City.\n\n**Core Approach:**\nTRAQ provides the first end-to-end statistical correctness guarantee for RAG using conformal prediction, a statistical technique for constructing prediction sets guaranteed to contain the semantically correct response with high probability.\n\n**Key Technical Details:**\nTRAQ applies conformal prediction separately to the retrieval model (to obtain sets of retrieved passages guaranteed to contain the relevant passage with high probability) and the generator (to obtain sets of answers that contain the true answer with high probability, assuming the relevant passage is given). TRAQ also leverages Bayesian optimization to minimize the size of the constructed sets.\n\n**Nonconformity Measure:**\nTRAQ introduces a novel nonconformity measure based on semantic uncertainty, which appears to address the challenge of semantically equivalent answers in natural language.\n\n**Results:**\nTRAQ provides the desired correctness guarantee while reducing prediction set size by 16.2% on average.\n\nThe paper was authored by Shuo Li, Sangdon Park, Insup Lee, and Osbert Bastani."
    ],
    "durationSeconds": 5.247922842999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "664fe7b1-b760-4581-b198-66737d378675",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "672ff11f-3ab4-4772-b113-8fc4ea13299e",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Tool call

_source line 37 · 2026-05-30T07:26:57.305Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014V2LDwPJcy7DMrztemfce2`</summary>

```json
{
  "query": "conformal prediction abstention adversarial robustness test-time corruption distribution shift bound 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "672ff11f-3ab4-4772-b113-8fc4ea13299e",
  "isSidechain": false,
  "requestId": "req_011CbYMfDiUNGv7fMQKSfxtT",
  "type": "assistant",
  "uuid": "767dfd87-eff7-4040-be0f-9152c29683d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RNihrsKWmUuYJzTbCJJpXE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 26595,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 26595,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 38 · 2026-05-30T07:27:05.193Z_

<details><summary>↩ Tool result · `toolu_014V2LDwPJcy7DMrztemfce2`</summary>

```text
Web search results for query: "conformal prediction abstention adversarial robustness test-time corruption distribution shift bound 2025 2026"

Links: [{"title":"[2511.18562] Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://arxiv.org/abs/2511.18562"},{"title":"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://arxiv.org/pdf/2511.18562"},{"title":"Verifiably Robust Conformal Prediction Linus Jeary∗ Department of Informatics","url":"https://arxiv.org/pdf/2405.18942"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model","url":"https://arxiv.org/pdf/2403.15025"},{"title":"Adversarially Robust Conformal Prediction","url":"https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction"},{"title":"Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/pdf/2502.14105"}]

I found several relevant research papers on conformal prediction with adversarial robustness and distribution shift:

**Recent Key Papers (2025-2026):**

1. **"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks"** (December 2025)
   - Conformal prediction provides distribution-free, finite-sample coverage guarantees but critically relies on exchangeability, a condition often violated under distribution shift. The paper studies the robustness of split conformal prediction under adversarial perturbations at test time, focusing on both coverage validity and the resulting prediction set size, with theoretical analysis characterizing how the strength of adversarial perturbations during calibration affects coverage guarantees under adversarial test conditions.

2. **"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations"** (May 2025)
   - Standard conformal prediction fails to maintain coverage as the corruption level increases due to lack of robustness to distribution shift, while their proposed method consistently maintains valid coverage across all settings.

3. **Adversarially Robust Conformal Prediction Overview** (2025)
   - Robust sets are constructed by shifting quantiles correspondingly. Diverse algorithmic paradigms—quantile inflation, smoothing, binarization, verification, training-time minimax, learning-reasoning integration, group conditioning, and federated defenses—deliver provable guarantees and practical efficiency.

4. **"Verifiably Robust Conformal Prediction"** (2024)
   - When exchangeability is violated in the presence of test-time distribution shifts, CP's coverage guarantee ceases to hold, with work addressing shifts induced by adversarial perturbations on test inputs, particularly additive ℓp-bounded noise.

These papers collectively address the intersection of conformal prediction, adversarial robustness, test-time corruption, and distribution shift with formal theoretical bounds.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "767dfd87-eff7-4040-be0f-9152c29683d4",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "e28b2ea8-3ce3-4434-a72c-fbd7c21d8aab",
  "toolUseResult": {
    "query": "conformal prediction abstention adversarial robustness test-time corruption distribution shift bound 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017B8p1bSYXHEHjEFK3EwDQL",
        "content": [
          {
            "title": "[2511.18562] Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks",
            "url": "https://arxiv.org/abs/2511.18562"
          },
          {
            "title": "Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks",
            "url": "https://arxiv.org/pdf/2511.18562"
          },
          {
            "title": "Verifiably Robust Conformal Prediction Linus Jeary∗ Department of Informatics",
            "url": "https://arxiv.org/pdf/2405.18942"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model",
            "url": "https://arxiv.org/pdf/2403.15025"
          },
          {
            "title": "Adversarially Robust Conformal Prediction",
            "url": "https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction"
          },
          {
            "title": "Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/pdf/2502.14105"
          }
        ]
      },
      "I found several relevant research papers on conformal prediction with adversarial robustness and distribution shift:\n\n**Recent Key Papers (2025-2026):**\n\n1. **\"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks\"** (December 2025)\n   - Conformal prediction provides distribution-free, finite-sample coverage guarantees but critically relies on exchangeability, a condition often violated under distribution shift. The paper studies the robustness of split conformal prediction under adversarial perturbations at test time, focusing on both coverage validity and the resulting prediction set size, with theoretical analysis characterizing how the strength of adversarial perturbations during calibration affects coverage guarantees under adversarial test conditions.\n\n2. **\"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations\"** (May 2025)\n   - Standard conformal prediction fails to maintain coverage as the corruption level increases due to lack of robustness to distribution shift, while their proposed method consistently maintains valid coverage across all settings.\n\n3. **Adversarially Robust Conformal Prediction Overview** (2025)\n   - Robust sets are constructed by shifting quantiles correspondingly. Diverse algorithmic paradigms—quantile inflation, smoothing, binarization, verification, training-time minimax, learning-reasoning integration, group conditioning, and federated defenses—deliver provable guarantees and practical efficiency.\n\n4. **\"Verifiably Robust Conformal Prediction\"** (2024)\n   - When exchangeability is violated in the presence of test-time distribution shifts, CP's coverage guarantee ceases to hold, with work addressing shifts induced by adversarial perturbations on test inputs, particularly additive ℓp-bounded noise.\n\nThese papers collectively address the intersection of conformal prediction, adversarial robustness, test-time corruption, and distribution shift with formal theoretical bounds."
    ],
    "durationSeconds": 7.8827786709999925,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "767dfd87-eff7-4040-be0f-9152c29683d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-30T07:27:07.748Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XcpFxQnyLJnDZ62c5StxzR`</summary>

```json
{
  "query": "RAG corpus poisoning defense certified robustness 2026 new methods beyond RobustRAG"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e28b2ea8-3ce3-4434-a72c-fbd7c21d8aab",
  "isSidechain": false,
  "requestId": "req_011CbYMfzPKAiEJSPpvj2AB3",
  "type": "assistant",
  "uuid": "99f1b320-2b6a-4795-bdac-5b43705cf291",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mDHB6yiVCQMz6JHY7wBHy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 27614,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 27614,
          "cache_creation_input_tokens": 919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 919
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

_source line 40 · 2026-05-30T07:27:17.525Z_

<details><summary>↩ Tool result · `toolu_01XcpFxQnyLJnDZ62c5StxzR`</summary>

```text
Web search results for query: "RAG corpus poisoning defense certified robustness 2026 new methods beyond RobustRAG"

Links: [{"title":"Advances LLM Security, RAGPart And RAGMask Mitigates Corpus Poisoning In Generation Pipelines","url":"https://quantumzeitgeist.com/security-advances-llm-ragpart-ragmask-mitigates/"},{"title":"RAG Poisoning: Threats and Defenses","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Certified Defenses for RAG Systems","url":"https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/html/2603.18034v1"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"ProGRank: Probe-Gradient Reranking to Defend Dense-Retriever RAG from Corpus Poisoning","url":"https://arxiv.org/pdf/2603.22934"},{"title":"[2602.04711] Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention","url":"https://arxiv.org/abs/2602.04711"}]

Based on the search results, here's what I found about RAG corpus poisoning defense and certified robustness methods in 2026:

## Recent Defense Mechanisms Beyond RobustRAG

Researchers from the University of Maryland College Park, including Pankayaraj Pathmanathan, Michael-Andrei Panaitescu-Liess, and Cho-Yu Jason Chiang, along with Furong Huang, have developed two novel defense mechanisms called RAGPart and RAGMask. These techniques work by strengthening the retrieval stage of RAG pipelines, identifying and mitigating the influence of poisoned documents without altering the underlying language model itself.

RAGPart improves robustness by fragmenting documents, employing multiple retrieval methods, and aggregating results using majority voting or intersection-based aggregation. RAGMask reduces the impact of potentially poisoned content by masking parts of retrieved fragments, controlled by a masking ratio and size.

## Certified Robustness Approaches

RAG systems are vulnerable to adversarial manipulations such as retrieval corruption and document poisoning, which has driven development of certified defenses—mechanisms that deliver formal guarantees against classes of adversarial threats, typically via ranking, aggregation, or detection strategies that admit worst-case bounds, probabilistic guarantees, or explicit certificates of robust operation.

ProGRank is a post hoc, training-free retriever-side defense that reranks candidates using probe-gradient instability under randomized perturbations.

## Current Research Directions

Ongoing research must target end-to-end certified robustness, dynamic detection, and holistic retriever–generator–corpus security integration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99f1b320-2b6a-4795-bdac-5b43705cf291",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "efccfdaf-a0a5-4573-b18a-7fcf66037a19",
  "toolUseResult": {
    "query": "RAG corpus poisoning defense certified robustness 2026 new methods beyond RobustRAG",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SNUFaazRMVGkRLsUzZ5ny2",
        "content": [
          {
            "title": "Advances LLM Security, RAGPart And RAGMask Mitigates Corpus Poisoning In Generation Pipelines",
            "url": "https://quantumzeitgeist.com/security-advances-llm-ragpart-ragmask-mitigates/"
          },
          {
            "title": "RAG Poisoning: Threats and Defenses",
            "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "Certified Defenses for RAG Systems",
            "url": "https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/html/2603.18034v1"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          },
          {
            "title": "ProGRank: Probe-Gradient Reranking to Defend Dense-Retriever RAG from Corpus Poisoning",
            "url": "https://arxiv.org/pdf/2603.22934"
          },
          {
            "title": "[2602.04711] Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention",
            "url": "https://arxiv.org/abs/2602.04711"
          }
        ]
      },
      "Based on the search results, here's what I found about RAG corpus poisoning defense and certified robustness methods in 2026:\n\n## Recent Defense Mechanisms Beyond RobustRAG\n\nResearchers from the University of Maryland College Park, including Pankayaraj Pathmanathan, Michael-Andrei Panaitescu-Liess, and Cho-Yu Jason Chiang, along with Furong Huang, have developed two novel defense mechanisms called RAGPart and RAGMask. These techniques work by strengthening the retrieval stage of RAG pipelines, identifying and mitigating the influence of poisoned documents without altering the underlying language model itself.\n\nRAGPart improves robustness by fragmenting documents, employing multiple retrieval methods, and aggregating results using majority voting or intersection-based aggregation. RAGMask reduces the impact of potentially poisoned content by masking parts of retrieved fragments, controlled by a masking ratio and size.\n\n## Certified Robustness Approaches\n\nRAG systems are vulnerable to adversarial manipulations such as retrieval corruption and document poisoning, which has driven development of certified defenses—mechanisms that deliver formal guarantees against classes of adversarial threats, typically via ranking, aggregation, or detection strategies that admit worst-case bounds, probabilistic guarantees, or explicit certificates of robust operation.\n\nProGRank is a post hoc, training-free retriever-side defense that reranks candidates using probe-gradient instability under randomized perturbations.\n\n## Current Research Directions\n\nOngoing research must target end-to-end certified robustness, dynamic detection, and holistic retriever–generator–corpus security integration."
    ],
    "durationSeconds": 9.769142773,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "99f1b320-2b6a-4795-bdac-5b43705cf291",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-30T07:27:20.250Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y3F5PG7aCG9AJnnnpckA14`</summary>

```json
{
  "query": "\"conformal abstention\" OR \"selective conformal\" OR \"conformal selective prediction\" coverage certificate adversarial 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efccfdaf-a0a5-4573-b18a-7fcf66037a19",
  "isSidechain": false,
  "requestId": "req_011CbYMgu6qwAv4dbDmv7uzA",
  "type": "assistant",
  "uuid": "357ec752-7dca-48e6-a1fd-20abb6765f89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhbBF3cDdbB22XVYkFJEe5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 28533,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 28533,
          "cache_creation_input_tokens": 909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 909
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

_source line 42 · 2026-05-30T07:27:30.064Z_

<details><summary>↩ Tool result · `toolu_01Y3F5PG7aCG9AJnnnpckA14`</summary>

```text
Web search results for query: ""conformal abstention" OR "selective conformal" OR "conformal selective prediction" coverage certificate adversarial 2025 2026"

Links: [{"title":"[2512.12844] Selective Conformal Risk Control","url":"https://arxiv.org/abs/2512.12844"},{"title":"[2506.14067] Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback","url":"https://arxiv.org/abs/2506.14067"},{"title":"Uncertainty-Driven Reliability: Selective Prediction and ...","url":"https://arxiv.org/pdf/2508.07556"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models","url":"https://arxiv.org/pdf/2502.06884"},{"title":"Selective Conformal Risk Control","url":"https://arxiv.org/html/2512.12844v1"},{"title":"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://arxiv.org/pdf/2511.18562"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325007113"},{"title":"Backward Conformal Prediction","url":"https://arxiv.org/pdf/2505.13732"},{"title":"Practical Adversarial Multivalid Conformal Prediction","url":"https://arxiv.org/pdf/2206.01067"},{"title":"Conformal Prediction Sets with Improved Conditional Coverage using Trust   Scores","url":"https://arxiv.org/pdf/2501.10139"}]

I found several relevant papers matching your search criteria. Here are the key findings:

## Recent Papers on Conformal Abstention and Selective Prediction (2025-2026)

**1. Online Conformal Abstention for Factuality Control**

Conformal abstention ensures that systems answer only when confident, addressing real-world deployments that provide partial user feedback and operate in non-stationary or adversarial environments. The ExAUL framework provides a novel online learning approach for conformal abstention with adversarial and partial feedback. This paper was submitted in June 2025 and last revised in May 2026.

**2. Selective Conformal Risk Control**

A unified framework integrates conformal prediction with selective classification to provide reliable, distribution-free uncertainty quantification while improving efficiency through selective abstention. The design enables simultaneous guarantees on selective coverage and conditional risk, addressing the practical limitation that standard conformal methods often yield excessively large prediction sets. This paper was posted in December 2025.

**3. Learning Conformal Abstention Policies for LLMs/VLMs**

Learnable conformal abstention integrates reinforcement learning with conformal prediction to optimize abstention thresholds dynamically, balancing multiple objectives while minimizing prediction set size and maintaining reliable coverage.

**4. Robustness Against Adversarial Attacks**

Verifiably Robust Conformal Prediction (VRCP) recovers conformal prediction's probabilistic guarantees under adversarial attacks by combining CP with neural network verification. This was published in February 2026.

These papers demonstrate active research into coverage certificates and adversarial robustness in conformal prediction methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "357ec752-7dca-48e6-a1fd-20abb6765f89",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "4747496a-6bd7-4298-b3c2-ab59615de6ed",
  "toolUseResult": {
    "query": "\"conformal abstention\" OR \"selective conformal\" OR \"conformal selective prediction\" coverage certificate adversarial 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R2Th6USzbCo5Hgz6pybMHk",
        "content": [
          {
            "title": "[2512.12844] Selective Conformal Risk Control",
            "url": "https://arxiv.org/abs/2512.12844"
          },
          {
            "title": "[2506.14067] Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback",
            "url": "https://arxiv.org/abs/2506.14067"
          },
          {
            "title": "Uncertainty-Driven Reliability: Selective Prediction and ...",
            "url": "https://arxiv.org/pdf/2508.07556"
          },
          {
            "title": "Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models",
            "url": "https://arxiv.org/pdf/2502.06884"
          },
          {
            "title": "Selective Conformal Risk Control",
            "url": "https://arxiv.org/html/2512.12844v1"
          },
          {
            "title": "Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks",
            "url": "https://arxiv.org/pdf/2511.18562"
          },
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0031320325007113"
          },
          {
            "title": "Backward Conformal Prediction",
            "url": "https://arxiv.org/pdf/2505.13732"
          },
          {
            "title": "Practical Adversarial Multivalid Conformal Prediction",
            "url": "https://arxiv.org/pdf/2206.01067"
          },
          {
            "title": "Conformal Prediction Sets with Improved Conditional Coverage using Trust   Scores",
            "url": "https://arxiv.org/pdf/2501.10139"
          }
        ]
      },
      "I found several relevant papers matching your search criteria. Here are the key findings:\n\n## Recent Papers on Conformal Abstention and Selective Prediction (2025-2026)\n\n**1. Online Conformal Abstention for Factuality Control**\n\nConformal abstention ensures that systems answer only when confident, addressing real-world deployments that provide partial user feedback and operate in non-stationary or adversarial environments. The ExAUL framework provides a novel online learning approach for conformal abstention with adversarial and partial feedback. This paper was submitted in June 2025 and last revised in May 2026.\n\n**2. Selective Conformal Risk Control**\n\nA unified framework integrates conformal prediction with selective classification to provide reliable, distribution-free uncertainty quantification while improving efficiency through selective abstention. The design enables simultaneous guarantees on selective coverage and conditional risk, addressing the practical limitation that standard conformal methods often yield excessively large prediction sets. This paper was posted in December 2025.\n\n**3. Learning Conformal Abstention Policies for LLMs/VLMs**\n\nLearnable conformal abstention integrates reinforcement learning with conformal prediction to optimize abstention thresholds dynamically, balancing multiple objectives while minimizing prediction set size and maintaining reliable coverage.\n\n**4. Robustness Against Adversarial Attacks**\n\nVerifiably Robust Conformal Prediction (VRCP) recovers conformal prediction's probabilistic guarantees under adversarial attacks by combining CP with neural network verification. This was published in February 2026.\n\nThese papers demonstrate active research into coverage certificates and adversarial robustness in conformal prediction methods."
    ],
    "durationSeconds": 9.808178610000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "357ec752-7dca-48e6-a1fd-20abb6765f89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-30T07:27:33.628Z_

<details><summary>Logged reasoning block</summary>

```text
This is very interesting. Let me look at one more critical reference - the "Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback" paper, as it seems highly relevant to this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4747496a-6bd7-4298-b3c2-ab59615de6ed",
  "isSidechain": false,
  "requestId": "req_011CbYMhpkSKFjSqgUAiWsSg",
  "type": "assistant",
  "uuid": "0f27613c-a090-49b8-8a14-da61efa4b89d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNNymNJudvcueQ5jCK1HaD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 926,
      "cache_read_input_tokens": 29442,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 926,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 29442,
          "cache_creation_input_tokens": 926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 926
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

### Tool call

_source line 44 · 2026-05-30T07:27:33.932Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RhySitcemVUttszrMX941R`</summary>

```json
{
  "query": "\"Online Conformal Abstention for Factuality Control\" adversarial bandit feedback arXiv 2506.14067 RAG LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f27613c-a090-49b8-8a14-da61efa4b89d",
  "isSidechain": false,
  "requestId": "req_011CbYMhpkSKFjSqgUAiWsSg",
  "type": "assistant",
  "uuid": "fc0f67b8-938c-4777-9c7d-d8cf595727ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNNymNJudvcueQ5jCK1HaD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 926,
      "cache_read_input_tokens": 29442,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 926,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 29442,
          "cache_creation_input_tokens": 926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 926
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

_source line 45 · 2026-05-30T07:27:39.466Z_

<details><summary>↩ Tool result · `toolu_01RhySitcemVUttszrMX941R`</summary>

```text
Web search results for query: ""Online Conformal Abstention for Factuality Control" adversarial bandit feedback arXiv 2506.14067 RAG LLM"

Links: [{"title":"[2506.14067] Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback","url":"https://arxiv.org/abs/2506.14067"},{"title":"Conformal Linguistic Calibration: Trading-off between Factuality and Specificity","url":"https://arxiv.org/pdf/2502.19110"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"},{"title":"Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling","url":"https://arxiv.org/pdf/2603.27403"},{"title":"Taming Variability: Randomized and Bootstrapped Conformal Risk Control for LLMs","url":"https://arxiv.org/html/2509.23007v1"},{"title":"Taming Variability: Randomized and Bootstrapped Conformal Risk Control for LLMs","url":"https://arxiv.org/pdf/2509.23007"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models","url":"https://arxiv.org/pdf/2502.06884"}]

I found the paper you're looking for! Here's what I found:

**"Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback"** addresses concerns about interactive generative systems that generate unreliable or false responses in real-world applications.

**Key aspects of the paper:**

- Conformal abstention mitigates risk by ensuring that the system answers only when confident

- The paper addresses the challenge that real-world deployments typically provide only partial user feedback (e.g., thumbs up/down) on the selected response and often operate in non-stationary or adversarial environments

- The paper proposes ExAUL, a novel online learning framework for conformal abstention with adversarial and partial feedback

The paper is available at arXiv:2506.14067 and represents recent work on controlling factuality in language models through conformal prediction methods combined with online learning under adversarial bandit feedback conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc0f67b8-938c-4777-9c7d-d8cf595727ba",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "f8efd3e1-1f75-47dc-836b-fd3a6f5ad27c",
  "toolUseResult": {
    "query": "\"Online Conformal Abstention for Factuality Control\" adversarial bandit feedback arXiv 2506.14067 RAG LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BGQtAN19guyoKdPiNmo1Au",
        "content": [
          {
            "title": "[2506.14067] Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback",
            "url": "https://arxiv.org/abs/2506.14067"
          },
          {
            "title": "Conformal Linguistic Calibration: Trading-off between Factuality and Specificity",
            "url": "https://arxiv.org/pdf/2502.19110"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/pdf/2405.01563"
          },
          {
            "title": "Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling",
            "url": "https://arxiv.org/pdf/2603.27403"
          },
          {
            "title": "Taming Variability: Randomized and Bootstrapped Conformal Risk Control for LLMs",
            "url": "https://arxiv.org/html/2509.23007v1"
          },
          {
            "title": "Taming Variability: Randomized and Bootstrapped Conformal Risk Control for LLMs",
            "url": "https://arxiv.org/pdf/2509.23007"
          },
          {
            "title": "Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models",
            "url": "https://arxiv.org/pdf/2502.06884"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\n**\"Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback\"** addresses concerns about interactive generative systems that generate unreliable or false responses in real-world applications.\n\n**Key aspects of the paper:**\n\n- Conformal abstention mitigates risk by ensuring that the system answers only when confident\n\n- The paper addresses the challenge that real-world deployments typically provide only partial user feedback (e.g., thumbs up/down) on the selected response and often operate in non-stationary or adversarial environments\n\n- The paper proposes ExAUL, a novel online learning framework for conformal abstention with adversarial and partial feedback\n\nThe paper is available at arXiv:2506.14067 and represents recent work on controlling factuality in language models through conformal prediction methods combined with online learning under adversarial bandit feedback conditions."
    ],
    "durationSeconds": 5.528796873999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fc0f67b8-938c-4777-9c7d-d8cf595727ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "f8efd3e1-1f75-47dc-836b-fd3a6f5ad27c",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Tool call

_source line 48 · 2026-05-30T07:27:44.927Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LHd4Xhx13BARDe3gV2ekzQ`</summary>

```json
{
  "query": "\"Mitigating LLM Hallucinations via Conformal Abstention\" 2024 2025 NLG factuality coverage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8efd3e1-1f75-47dc-836b-fd3a6f5ad27c",
  "isSidechain": false,
  "requestId": "req_011CbYMiWwQ9y3pVnFNDaVFC",
  "type": "assistant",
  "uuid": "479f78f1-1798-42da-96ba-ee3069c765f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPwF5KFY2CVRpACRqVYWwV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 30368,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 30368,
          "cache_creation_input_tokens": 750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 750
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

_source line 49 · 2026-05-30T07:27:49.574Z_

<details><summary>↩ Tool result · `toolu_01LHd4Xhx13BARDe3gV2ekzQ`</summary>

```text
Web search results for query: ""Mitigating LLM Hallucinations via Conformal Abstention" 2024 2025 NLG factuality coverage"

Links: [{"title":"[PDF] Mitigating LLM Hallucinations via Conformal Abstention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mitigating-LLM-Hallucinations-via-Conformal-Abbasi-Yadkori-Kuzborskij/b5cd6bc53343f2ad8a7c7830555d8c744e626245"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"},{"title":"NeurIPS Mitigating LLM Hallucinations via ConformalAbstention","url":"https://neurips.cc/virtual/2024/105548"},{"title":"[Literature Review] Mitigating LLM Hallucinations via Conformal Abstention","url":"https://www.themoonlight.io/en/review/mitigating-llm-hallucinations-via-conformal-abstention"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mitigating-llm-hallucinations-via-conformal-abstention"},{"title":"[2405.01563] Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/abs/2405.01563"}]

I found the paper you're looking for! Here's a summary of "Mitigating LLM Hallucinations via Conformal Abstention":

## Overview

The paper develops a principled procedure for determining when a large language model (LLM) should abstain from responding (e.g., by saying "I don't know") in a general domain, instead of resorting to possibly "hallucinating" a non-sensical or incorrect answer.

## Method

The approach builds on earlier techniques that use self-consistency as a more reliable measure of model confidence, proposing to use the LLM itself to self-evaluate the similarity between each of its sampled responses for a given query. The authors further leverage conformal prediction techniques to develop an abstention procedure that benefits from rigorous theoretical guarantees on the hallucination rate (error rate).

## Results

The conformal abstention method reliably bounds the hallucination rate on various closed-book, open-domain generative question answering datasets, while also maintaining a significantly less conservative abstention rate on a dataset with long responses (Temporal Sequences) compared to baselines using log-probability scores to quantify uncertainty, while achieving comparable performance on a dataset with short answers (TriviaQA).

The paper was published in 2024 (dated April 4, 2024) and appears to have been presented at NeurIPS 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "479f78f1-1798-42da-96ba-ee3069c765f0",
  "isSidechain": false,
  "promptId": "840a8709-4d23-4b34-86a6-8d955b404eb1",
  "type": "user",
  "uuid": "81f066d1-cf90-4d06-8790-4e06c638286f",
  "toolUseResult": {
    "query": "\"Mitigating LLM Hallucinations via Conformal Abstention\" 2024 2025 NLG factuality coverage",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YPTuLWGpY8ZrxRPtF5n6tu",
        "content": [
          {
            "title": "[PDF] Mitigating LLM Hallucinations via Conformal Abstention | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Mitigating-LLM-Hallucinations-via-Conformal-Abbasi-Yadkori-Kuzborskij/b5cd6bc53343f2ad8a7c7830555d8c744e626245"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/pdf/2405.01563"
          },
          {
            "title": "NeurIPS Mitigating LLM Hallucinations via ConformalAbstention",
            "url": "https://neurips.cc/virtual/2024/105548"
          },
          {
            "title": "[Literature Review] Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://www.themoonlight.io/en/review/mitigating-llm-hallucinations-via-conformal-abstention"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/mitigating-llm-hallucinations-via-conformal-abstention"
          },
          {
            "title": "[2405.01563] Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/abs/2405.01563"
          }
        ]
      },
      "I found the paper you're looking for! Here's a summary of \"Mitigating LLM Hallucinations via Conformal Abstention\":\n\n## Overview\n\nThe paper develops a principled procedure for determining when a large language model (LLM) should abstain from responding (e.g., by saying \"I don't know\") in a general domain, instead of resorting to possibly \"hallucinating\" a non-sensical or incorrect answer.\n\n## Method\n\nThe approach builds on earlier techniques that use self-consistency as a more reliable measure of model confidence, proposing to use the LLM itself to self-evaluate the similarity between each of its sampled responses for a given query. The authors further leverage conformal prediction techniques to develop an abstention procedure that benefits from rigorous theoretical guarantees on the hallucination rate (error rate).\n\n## Results\n\nThe conformal abstention method reliably bounds the hallucination rate on various closed-book, open-domain generative question answering datasets, while also maintaining a significantly less conservative abstention rate on a dataset with long responses (Temporal Sequences) compared to baselines using log-probability scores to quantify uncertainty, while achieving comparable performance on a dataset with short answers (TriviaQA).\n\nThe paper was published in 2024 (dated April 4, 2024) and appears to have been presented at NeurIPS 2024."
    ],
    "durationSeconds": 4.643905677000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "479f78f1-1798-42da-96ba-ee3069c765f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-30T07:29:02.679Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the research landscape. Let me synthesize my findings and evaluate this proposal systematically.

Key observations from my research:

1. **The gap claim is valid**: There is indeed no existing work that combines conformal abstention with retrieval-poisoning robustness. The closest works are:
   - TRAQ/C-RAG/Conformal-RAG: CP for RAG but assume benign retrieval
   - RobustRAG/ReliabilityRAG: Robust defenses but no abstention/coverage certificates
   - RPS: Poisoning-robust CP but for calibration-set poisoning, not test-time retrieval corruption
   - Chen et al. 2026: Identified the gap but offered no solution

2. **The partition-induced reduction is a genuine insight**: Framing adversarial retrieval corruption as a bounded total variation shift in the score distribution is technically sound and novel, drawing parallels to the Lévy-Prokhorov framework but tailored specifically for this adversarial setting.

3. **Potential threats to novelty**: A recent NeurIPS 2024 paper on mitigating LLM hallucinations uses self-consistency-based scores with conformal prediction for abstention, though it doesn't address adversarial retrieval corruption.

4. **The proposal is already quite well-developed**: It has a clear problem formulation, strong related work coverage, sound theoretical grounding, and comprehensive experimental design.

Now I'm thinking about what I can actually contribute as the discovery agent. The partition-induced reduction principle could be framed more strongly as a general paradigm that extends beyond this specific application, potentially opening up new research directions in adversarial robustness for retrieval systems.

There's also a meaningful connection to randomized smoothing in certified robustness—the partition-and-generate approach creates a smoothing effect that bounds sensitivity to corruption, which could strengthen the theoretical narrative.

For high-stakes applications, I should emphasize that the real value isn't achieving accuracy under attack, but guaranteeing we don't produce incorrect answers—reframing this as a safety problem rather than an accuracy problem, which is fundamentally more important in critical domains.

A key point worth making explicit: self-consistency voting with more samples alone can't provide the same guarantees because without the partition structure, all samples could be equally contaminated by poisoned passages. The partition is what makes the theoretical bound possible. I'm also considering whether to frame the complementary defenses more strongly as a defense-in-depth architecture where each layer provides distinct guarantees.

The core contribution is solid—reducing high-dimensional adversarial corruption to bounded TV shift in 1D score distributions is a clean theoretical result. But I need to think carefully about what would genuinely strengthen the work beyond what's already there.

One concern that keeps surfacing: the TV bound of m/K might be quite loose in practice. With concrete numbers like K=5 and n=20, the bound could reach 0.4, which is substantial and might force high abstention rates even on clean data. This raises the question of whether the coverage-abstention tradeoff is actually useful or if the certificates become vacuous in realistic settings.

Though they're explicitly planning to measure this in their experiments—coverage versus abstention curves, vacuousness rates—so it's not an undiscovered gap. The stronger angle might be positioning the partition-induced reduction as a general meta-principle: any defense that bounds corruption to m-out-of-K groups automatically yields a TV bound that conformal prediction can absorb, making this framework applicable far beyond RAG to things like multi-source data fusion or distributed learning with Byzantine nodes.

There's also a fundamental certification gap in RAG safety between point-estimate robustness (which says "the answer is likely correct") and distributional guarantees (which say "with probability 1-α, either the answer is correct or we abstain"). The latter is strictly more valuable for deployment in regulated domains like medicine, law, or finance.

Now I'm checking for related work that might overlap—there's a recent paper on selective conformal risk control that integrates conformal prediction with selective classification, which could touch on the abstention mechanism, though it doesn't seem to address adversarial retrieval corruption. I should also look into work on conformal abstention policies for language models.

The key question is whether instantiating the Lévy-Prokhorov framework specifically for adversarial retrieval corruption is sufficiently novel. The TV bound here comes from the combinatorial structure of passage partitioning, and the agreement score is designed to be monotone and corruption-bounded—that's a non-trivial instantiation beyond just applying a general framework.

I'm thinking through how to strengthen the proposal at the idea level, particularly around how the reduction principle should be framed. amed as more general** - not just "a method for RAG" but a general paradigm for bridging certified defenses and conformal guarantees. This significantly raises the theoretical contribution's ceiling.

2. **The practical tightness of the TV bound needs more discussion at the idea level** - not just as an experimental question, but as a theoretical one. Can the bound be tightened with additional structural assumptions?

3. **The clean-condition variance assumption deserves deeper treatment** - The proposal acknowledges that clean passages covering different facets could inflate s, but the mitigation (NLI + calibration) feels hand-wavy. This is actually an idea-level issue because it affects whether the core claim holds in practice.

Wait, point 3 is more about soundness/experimental verification, which is the 補救 agent's domain. Let me stay focused on novelty, significance, and related work differentiation.

So my three discovery points are: framing the partition-induced reduction as a general meta-principle for significance and novelty, sharpening the "certification gap" framing to highlight what's at stake, and exploring whether the TV bound's worst-case m/K can be tightened by exploiting structural properties of NLI entailment scores. That last one is genuinely interesting—if entailment probabilities are bounded in [0,1] and I can bound how sensitive the agreement score is to individual pairwise comparisons, I might derive a strictly tighter bound than the worst-case guarantee. That would be a real novelty enhancement.

Now I should also check whether there are trivial alternatives that achieve similar results and whether the proposal adequately addresses them. Self-consistency with more samples but no retrieval partitioning would fail because all K answers would be conditioned on the same potentially poisoned retrieval set, so they'd consistently give the wrong answer—agreement would be high but wrong, and without partitioning there's no corruption bound. RobustRAG plus standard conformal prediction is addressed in the proposal's existing comparison. Using confidence calibration on the generator's logprobs rather than inter-group agreement is another angle, but the proposal's inter-group agreement approach is more directly tied to the retrieval corruption problem.

Now I'm checking whether there are simpler alternatives that could achieve similar results and whether the proposal adequately distinguishes itself from them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81f066d1-cf90-4d06-8790-4e06c638286f",
  "isSidechain": false,
  "requestId": "req_011CbYMjGCQozpYRYCyJ2YWW",
  "type": "assistant",
  "uuid": "676f460e-825f-477b-bc49-785359c990d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUmtNLb7xckWQABwp9KxZo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 31118,
      "output_tokens": 6733,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6733,
          "cache_read_input_tokens": 31118,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

### Assistant

_source line 51 · 2026-05-30T07:30:28.400Z_

Now I have sufficient context from my research. Let me produce my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- [Chen et al., arXiv:2603.16817](https://arxiv.org/abs/2603.16817) (Mar 2026): 严格证明了 TRAQ/C-RAG/Conformal-RAG 在分布偏移和检索腐蚀下 coverage guarantee 崩溃、产出 vacuous prediction sets。建立了明确的 open gap，但未提出解决方案。PRCA 直接对接此 gap，定位准确。
- [Conformal Prediction under Lévy-Prokhorov Distribution Shifts, arXiv:2502.14105](https://arxiv.org/abs/2502.14105) (Feb 2025): 提出了通过 ambiguity set 将高维分布偏移 reduce 到一维 score 分布偏移的通用框架。PRCA 的 partition-induced TV bound 是该范式的一种特定实例化，但 proposal 对此关系的利用还不够深入。
- [Mitigating LLM Hallucinations via Conformal Abstention](https://arxiv.org/abs/2405.01563) (NeurIPS 2024): 利用 self-consistency 作为 nonconformity score 进行 conformal abstention。核心区别：该方法在全量 context 上做 self-consistency，所有 sample 共享同一个（可能被毒化的）检索集，因此无法 bound adversarial shift。PRCA 的 partition 结构是获得 adversarial guarantee 的关键。
- [Selective Conformal Risk Control, arXiv:2512.12844](https://arxiv.org/abs/2512.12844) (Dec 2025): 将 selective classification 与 conformal prediction 统一，提供 selective coverage 和 conditional risk 的双重保证。但不处理 adversarial setting 或检索腐蚀。
- [Online Conformal Abstention for Factuality Control, arXiv:2506.14067](https://arxiv.org/abs/2506.14067) (Jun 2025): 在 adversarial bandit feedback 下做 conformal abstention。adversarial model 不同（non-stationary feedback vs. retrieval corruption），但说明 "adversarial conformal abstention" 是活跃方向。
- [Ensuring Calibration Robustness in Split CP Under Adversarial Attacks, arXiv:2511.18562](https://arxiv.org/abs/2511.18562) (Nov 2025): 研究 test-time adversarial perturbation 下 split CP 的 robustness。理论框架与 PRCA 有共鸣但场景不同（input perturbation vs. retrieval corruption）。
- [The Consensus Trap, arXiv:2604.17139](https://arxiv.org/abs/2604.17139) (Apr 2026): 揭示 multi-agent LLM 的 response-level majority voting 在 corrupted agents 形成 local majority 时失败。这对 PRCA 的 majority answer 输出策略构成潜在理论威胁——需要考虑当 corrupted groups 恰好过半时的行为。
- [ProGRank, arXiv:2603.22934](https://arxiv.org/abs/2603.22934) (Mar 2026): 利用 probe-gradient instability 做 retrieval-stage defense，training-free。与 RAGPart 一样可作为 PRCA 的上游组件。
- 调研总结：该领域当前的主要突破方向是 (1) 在各种 adversarial model 下恢复 conformal guarantee，(2) 将 certified defense 的 point-estimate robustness 提升为 distributional guarantee。PRCA 恰好站在这两个方向的交叉点，但领域内已有多种 "adversarial + conformal" 的组合尝试，PRCA 需要精准定位其独特价值——即 partition structure 将 adversarial retrieval corruption 这一特定威胁模型 reduce 为可被 CRC 吸收的 bounded TV shift。

---

【发掘点 1】
- 维度: significance 提升 / 核心 claim 强化
- 内容: **将 partition-induced reduction 提升为一个通用 meta-principle，而不仅仅是 "一个 RAG 防御方法"。** 当前 proposal 将核心贡献定位为 "PRCA: 一个 poisoning-robust 的 RAG conformal abstention 方法"，这是 application-level 的定位。但实际上，其核心 insight 更深刻：**任何将输入分为 K 个 disjoint groups、独立处理后聚合的 certified defense，都自然诱导出一个 bounded TV shift，可被 CRC 框架吸收以产生 coverage certificate。** 这意味着该 reduction principle 可以推广到：(a) multi-source data fusion with Byzantine sources, (b) distributed inference with corrupted nodes, (c) any isolate-then-aggregate architecture。Proposal 应在 contribution statement 中将此提升为 "a general principle for lifting point-estimate certified defenses into distributional (conformal) guarantees via partition-induced TV bounds"，并将 RAG 作为第一个也是最自然的 instantiation。这个 framing 使得 theoretical contribution 的 generality 大幅提升，审稿人更难用 "incremental combination of existing techniques" 来 dismiss。
- 价值: Significance 维度——从 "RAG-specific defense" 提升为 "bridging certified defense and conformal prediction 的一般方法论"，直接提升论文的影响力和引用范围。同时强化 Novelty 维度——因为 "general reduction principle" 比 "specific instantiation" 的 novelty 评价天花板更高。
- 调研依据: Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105) 提供了 "高维 shift → 一维 score shift" 的通用框架但缺乏具体的 adversarial corruption instantiation；RPS (ICLR 2025) 通过 partition 处理 calibration poisoning 但不处理 test-time corruption。PRCA 的 partition-induced reduction 恰好填补了 "通用框架" 与 "具体 adversarial setting" 之间的空白，应明确 claim 这一位置。

【发掘点 2】
- 维度: trivial alternative 威胁 / novelty 锐化
- 内容: **显式论证为什么 logprob-based confidence 或 full-context self-consistency 不能替代 partition-based agreement score，将 partition 的不可替代性说透。** 当前 proposal 论证了 "RobustRAG + standard CP" 的 pipeline 失败，但还有两个更 natural 的 trivial alternative 未被充分击退：(1) **Full-context self-consistency**：生成 K 个答案但所有答案共享同一个完整检索集（即 NeurIPS 2024 "Conformal Abstention" 的思路），然后用 agreement 做 CP——这看似更简单且不需要 K× 独立调用。Proposal 应显式论证：因为所有 sample 共享相同的 poisoned context，模型可能对错误答案保持高度一致，导致 agreement score 无法检测到 poisoning，且无法 bound 任何 TV shift。**Partition 是获得 adversarial guarantee 的必要条件，不是 implementation choice。** (2) **Generator logprob calibration**：直接用 LLM 的 token-level logprobs 做 nonconformity score，避免 K× inference cost。论证：poisoned contexts 如果语义上看起来权威（这正是 PoisonedRAG 和 Semantic Chameleon 的攻击策略），model confidence 可能反而更高，logprob 作为 nonconformity score 在 adversarial setting 下单调性假设不成立。
- 价值: 直接命中 Novelty 维度——击退 trivial alternatives 是 AAAI 审稿人最常见的 novelty 质疑路径。将 partition 从 "design choice" 提升为 "theoretical necessity" 是锐化 novelty 的关键步骤。
- 调研依据: "Mitigating LLM Hallucinations via Conformal Abstention" (NeurIPS 2024) 正是 full-context self-consistency + conformal prediction 的代表性工作，构成最直接的 trivial alternative。Semantic Chameleon (arXiv Mar 2026) 展示了 gradient-guided 攻击可以生成在语义上高度可信的 poisoned documents，直接威胁 logprob-based confidence 的可靠性。

【发掘点 3】
- 维度: novelty 锐化 / 核心 claim 强化
- 内容: **探索是否可以利用 NLI entailment score 的结构性质得到比 worst-case m/K 更紧的 TV bound。** 当前的 TV bound TV ≤ m/K 是纯组合的 worst-case bound——假设每个 corrupted group 将 score CDF 偏移最大量。但 NLI entailment probability e(i,j) ∈ [0,1] 是连续的，且 agreement score s 是所有 pairwise e(i,j) 的均值。单个 corrupted group 影响 m(K-1) 对比较，但每对比较对 s 的贡献是 1/C(K,2)，因此单个 corrupted group 对 s 的扰动被均值操作自然 dampen。可以考虑：(a) 利用 s 作为均值的 Lipschitz 性质，直接 bound |s_clean - s_poisoned| ≤ 2m(K-1)/(K(K-1)) = 2m/K，在 s 空间给出 L∞ bound 而非 CDF 空间的 TV bound，可能转化为更紧的 quantile inflation；(b) 利用 entailment probability 的有界性 e(i,j) ∈ [0,1]，通过 Hoeffding-type inequality 将 m/K 这种 worst-case bound 替换为 concentration-based bound。如果能推导出 tighter bound，这将从 "simple application of CRC" 提升为 "novel theoretical contribution in robust CP"。
- 价值: Novelty 维度——从 "existing frameworks 的 straightforward composition" 提升为 "new theoretical result"。一个 tighter TV bound 直接改善 coverage-abstention tradeoff，也回应了 Chen et al. (2026) 关于 vacuousness 的批评。
- 调研依据: Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105) 通过 ambiguity set propagation 得到 tight bounds，思路可参考；RPS (ICLR 2025) 的 smoothed scores 也利用了均值操作的 concentration 性质来 tighten certificates。两者均表明 worst-case combinatorial bound 可以通过 score function 的结构性质进一步收紧。

【发掘点 4】
- 维度: related work 差异化 / 前提假设质疑
- 内容: **需要在 related work 中显式处理 "Consensus Trap" (arXiv:2604.17139, Apr 2026) 揭示的 adversarial majority 问题，并论证 PRCA 在什么条件下不受此威胁。** 该论文证明 response-level majority voting 在 corrupted agents 形成 local majority 时彻底失败。PRCA 的 Step 4 "output the majority answer across groups" 在 corrupted groups 超过半数时同样面临此风险。但 PRCA 的关键区别在于：(a) 其核心贡献不是 majority answer 的正确性，而是 abstention decision 的 coverage certificate——当 corrupted groups 过半时，inter-group disagreement 会很低（corrupted groups 之间一致），但与 clean groups 之间的 disagreement 仍会被捕捉，导致 s 升高，触发 abstention；(b) 更根本地，PRCA 的 threat model 假设 k-poisoning（k 篇毒化文档），结合 K groups 和 n 篇总文档，corrupted groups 数量 m = ceil(k/floor(n/K)) 是有上界的。应显式论证在 k < n/2 的 typical threat model 下（与 RobustRAG 一致），m < K/2，因此 majority answer 不会被翻转，且 agreement score 仍能有效检测 corruption。这个论证直接预防了一个潜在的 "fatal flaw" 级别审稿意见。
- 价值: Related Work 差异化 + 前提假设质疑——提前堵住 "your majority vote is broken under adversarial majority" 这个高概率审稿攻击向量。如果忽视这篇 2026 年 4 月的新工作，审稿人很可能指出此问题。
- 调研依据: "The Consensus Trap" (arXiv:2604.17139, Apr 2026) 直接证明了 response-level aggregation 在 adversarial majority 下的脆弱性。PRCA 需要在 related work 和 threat model discussion 中显式处理此结果。

Sources:
- [Chen et al. 2026 - Is Conformal Factuality for RAG-based LLMs Robust?](https://arxiv.org/abs/2603.16817)
- [Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/abs/2502.14105)
- [Mitigating LLM Hallucinations via Conformal Abstention](https://arxiv.org/abs/2405.01563)
- [Selective Conformal Risk Control](https://arxiv.org/abs/2512.12844)
- [Online Conformal Abstention for Factuality Control](https://arxiv.org/abs/2506.14067)
- [Ensuring Calibration Robustness in Split CP Under Adversarial Attacks](https://arxiv.org/abs/2511.18562)
- [The Consensus Trap](https://arxiv.org/abs/2604.17139)
- [RobustRAG - Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556)
- [ReliabilityRAG](https://arxiv.org/abs/2509.23519)
- [RPS - Provably Reliable Conformal Prediction Sets](https://arxiv.org/abs/2410.09878)
- [RAGPart & RAGMask](https://arxiv.org/pdf/2512.24268)
- [ProGRank](https://arxiv.org/pdf/2603.22934)
- [Semantic Chameleon](https://arxiv.org/html/2603.18034v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "676f460e-825f-477b-bc49-785359c990d5",
  "isSidechain": false,
  "requestId": "req_011CbYMjGCQozpYRYCyJ2YWW",
  "type": "assistant",
  "uuid": "438407b8-aae3-4d33-a2ac-5c3372148196",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUmtNLb7xckWQABwp9KxZo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 31118,
      "output_tokens": 6733,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6733,
          "cache_read_input_tokens": 31118,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "438407b8-aae3-4d33-a2ac-5c3372148196",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "438407b8-aae3-4d33-a2ac-5c3372148196",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG",
  "sessionId": "42ce35e5-fa1f-4a36-a5ac-1a806c6d8973"
}
```

---
