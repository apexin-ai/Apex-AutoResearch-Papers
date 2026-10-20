# Research conversation: Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores ## Core Problem RAG systems deployed in adv

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/037763d4-80b2-4f88-83b7-758527263a94.jsonl`
- **Structured JSON:** [`c408e1082d6362c0a662.json`](../../sessions/c4/c408e1082d6362c0a662.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:24:55.542Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:24:55.542Z",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "content": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores\n\n## Core Problem\n\nRAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) need to abstain from answering with distribution-free correctness guarantees when the retrieval corpus is poisoned. Corpus poisoning is a practical threat: CorruptRAG (arXiv 2025) achieves high attack success rates with a single injected document. Existing conformal prediction methods for RAG (TRAQ, NAACL 2024; C-RAG, ICML 2024; Conformal-RAG, SIGIR 2025) assume benign retrieval—Chen et al. (arXiv:2603.16817, Mar 2026) rigorously demonstrated these guarantees break under distribution shift and produce vacuous outputs at high confidence levels. Existing poisoning-robust CP (RPS, ICLR 2025 Spotlight) addresses calibration-set poisoning, a fundamentally different threat model from test-time retrieval corruption. Certified RAG defenses (RobustRAG, SaTML 2026; ReliabilityRAG, NeurIPS 2025) provide robust point estimates but no abstention mechanism or coverage certificates. The gap: no method provides distribution-free abstention guarantees for RAG under adversarial retrieval corruption.\n\n## Core Contribution and Theoretical Insight\n\nWe propose PRCA (Poisoning-Robust Conformal Abstention), whose central contribution is a **partition-induced reduction principle**: by partitioning retrieved passages into disjoint groups and computing inter-group agreement, arbitrary test-time retrieval corruption is deterministically reduced to a bounded total-variation (TV) shift in the one-dimensional nonconformity score distribution. This bounded TV shift is precisely what the CRC framework (ICLR 2024) can absorb via inflated quantiles, yielding formal coverage certificates. This reduction—from high-dimensional adversarial corruption to one-dimensional bounded distributional shift—parallels the approach of Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv 2502.14105), which reduces high-dimensional distribution shifts to manageable one-dimensional score shifts via ambiguity sets. PRCA instantiates this reduction paradigm for the specific setting of adversarial retrieval corruption in RAG.\n\n**Why not simply RobustRAG + standard CP?** A naive pipeline—running RobustRAG to obtain a robust answer, then applying TRAQ/C-RAG for conformal abstention—fails because: (1) RobustRAG's aggregation transforms the output distribution in a poisoning-dependent manner, so the nonconformity scores computed on a clean calibration set are no longer exchangeable with test-time scores under attack; (2) the magnitude of this distributional shift is uncharacterized, making standard CP coverage guarantees invalid. PRCA resolves this by explicitly bounding the TV distance between clean and poisoned score CDFs via the partition structure, then absorbing this bounded shift through CRC's quantile inflation.\n\n## Research Landscape\n\n**Conformal prediction for RAG:** TRAQ (NAACL 2024) and C-RAG (ICML 2024) established conformal prediction for RAG with coverage guarantees under benign retrieval. Conformal-RAG (SIGIR 2025) extends this to group-conditional coverage. Chen et al. (arXiv:2603.16817, Mar 2026) showed all such methods produce vacuous prediction sets under distribution shift and retrieval corruption, but proposed no solution—creating an open, citable gap.\n\n**Certified RAG defenses:** RobustRAG (SaTML 2026) provides certified defense via isolate-then-aggregate (partition passages → independent generation → keyword/decoding-based aggregation), achieving certified robust accuracy on RealtimeQA/NQ. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with NLI-based contradiction detection for provably robust document filtering. Both provide robust point estimates but no abstention mechanism or distribution-free coverage certificates.\n\n**Poisoning-robust CP:** RPS (ICLR 2025 Spotlight) achieves poisoning-robust conformal prediction via smoothed scores and majority voting, but assumes calibration-set poisoning—certificates do not transfer to test-time retrieval corruption where adversarial documents enter at inference time.\n\n**Partition-based defenses:** RAGPart (arXiv:2512.24268, Dec 2025) uses document partitioning at the retrieval stage (fragmenting documents and averaging fragment embeddings) to dilute poisoning impact. Three key differences from PRCA: (1) RAGPart operates at the retrieval/embedding stage, PRCA at the generation/calibration stage; (2) RAGPart outputs filtered retrieval sets, PRCA outputs {answer, abstain} decisions with coverage certificates; (3) RAGPart and PRCA are complementary—RAGPart can serve as a retrieval-stage preprocessor before PRCA's generation-stage certified abstention.\n\n**Attack landscape:** PoisonedRAG (USENIX Security 2025) achieves 90%+ ASR with 5 poisoned documents on NQ/HotpotQA/MS-MARCO. CorruptRAG (arXiv 2025) achieves high ASR with a single document. RSB Benchmark (May 2025) systematically evaluated 13 attack methods across targeted poisoning, DoS, and trigger-based categories, finding current defenses have residual risk. Semantic Chameleon (arXiv Mar 2026) introduced gradient-guided corpus-dependent attacks.\n\n**Distribution-shift-robust CP:** Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv 2502.14105) provides a framework for robust CP under distribution shifts by propagating ambiguity sets through scoring functions, reducing high-dimensional shifts to one-dimensional score distribution shifts. PRCA's partition-induced TV bound can be viewed as a specific instantiation of this reduction paradigm for adversarial retrieval corruption.\n\nNo existing work combines conformal abstention with retrieval-poisoning robustness.\n\n## Proposed Approach\n\n**Step 1: Partition-and-Generate.** Given top-n retrieved passages, partition them into K disjoint groups (random assignment). For each group, generate an answer via an isolated LLM call.\n\n**Step 2: Agreement Nonconformity Score.** Compute a nonconformity score based on inter-group answer agreement. Specifically, for each pair of groups (i, j), compute the NLI entailment probability e(i,j) = P(answer_i entails answer_j) using a lightweight NLI model (e.g., DeBERTa-v3, following ReliabilityRAG's NLI approach). The agreement score is defined as:\n\ns = 1 − (mean of e(i,j) over all pairs)\n\nThis score has two critical properties: (1) **Monotonicity**: s is monotone in the abstention threshold λ (higher s → more disagreement → more likely to abstain), satisfying CRC's requirement; (2) **Corruption-boundedness**: under k-poisoning, at most m = ceil(k / floor(n/K)) groups are corrupted, affecting at most m(K−1) of the K(K−1)/2 pairwise comparisons, yielding a bounded perturbation to s.\n\n**Key assumption and mitigation:** The agreement score assumes that LLM outputs for clean passages are sufficiently consistent across groups. If different groups cover different facets of the answer, clean-condition variance inflates s and may cause unnecessary abstention. We mitigate this by using NLI-based semantic entailment (rather than exact match) for agreement computation, which is robust to surface-level variation. Calibration on clean data naturally accounts for residual clean-condition variance in the score distribution.\n\n**Step 3: TV-Bounded Calibration.** Under k-poisoning with K groups, the corruption bound m determines the maximal TV distance between clean and poisoned score CDFs: TV ≤ m/K. Using CRC (ICLR 2024) with TV-inflated quantile: set abstention threshold at the (1 − α + TV)-quantile of calibration scores, yielding formal coverage certificate P(correct or abstain) ≥ 1 − α even under k-poisoning.\n\n**Step 4: Abstention Decision.** At test time, if s > λ (calibrated threshold), abstain; otherwise, output the majority answer across groups.\n\n## Experimental Design\n\n**Datasets:** NQ, HotpotQA, MS-MARCO (standard RAG evaluation benchmarks, used by PoisonedRAG and RobustRAG).\n\n**Attack methods:** (1) PoisonedRAG (targeted poisoning, varying k ∈ {1, 3, 5, 10}); (2) CorruptRAG (single-document high-ASR attack); (3) at least one DoS-type attack from RSB Benchmark (May 2025) taxonomy to test behavior under denial-of-service adversaries. Discussion section analyzes k-poisoning assumption validity across attack categories.\n\n**Models:** Three scales to verify model-agnosticism: (1) primary experiments on Qwen3.5-7B (or Llama-3-8B); (2) medium-scale validation on Qwen3.5-32B; (3) large-scale validation on Qwen3.5-72B. NLI model: DeBERTa-v3-large for agreement scoring.\n\n**Baselines (7 methods):**\n- Conformal methods: TRAQ (NAACL 2024), C-RAG (ICML 2024), Conformal-RAG (SIGIR 2025)\n- Certified defenses: RobustRAG (SaTML 2026), ReliabilityRAG (NeurIPS 2025)\n- Partition-based: RAGPart (arXiv:2512.24268) — same partition strategy, no conformal calibration (ablation baseline)\n- Compute-normalized: TRAQ + K× self-consistency voting (controls for PRCA's K× inference cost)\n\n**Calibration protocol:** Calibration set constructed on clean corpus (standard assumption per RPS, ICLR 2025), n_cal ≥ 500 per dataset. Sensitivity experiment: evaluate coverage degradation when actual poisoning budget exceeds assumed k upper bound.\n\n**Metrics:**\n- Primary: Certified coverage rate, empirical coverage rate under attack, abstention rate\n- Secondary: Clean accuracy (no attack), prediction set size, vacuousness rate (per Chen et al. 2026)\n- Tradeoff curves: coverage vs. abstention rate at varying α; coverage vs. poisoning budget k; certified vs. empirical robustness gap\n- Efficiency: wall-clock time per query, token consumption per query\n\n**Ablation matrix:**\n- K ∈ {3, 5, 7, 10}: partition count vs. coverage/abstention tradeoff\n- n ∈ {10, 20, 30}: retrieval depth vs. certificate tightness\n- Score function: NLI entailment (primary) vs. ROUGE-L vs. exact match\n- Calibration: CRC + TV inflation vs. CRC without inflation vs. vanilla split conformal\n- Partition strategy: random vs. round-robin by retrieval score\n\n**Scale:** 200-300 queries per dataset per setting (comparable to RobustRAG's 100/dataset), with 95% confidence intervals reported.\n\n## Key References\n\n- TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction (NAACL 2024)\n- C-RAG: Certified Generation Risks for RAG (ICML 2024)\n- Conformal Risk Control (ICLR 2024)\n- Provably Reliable Conformal Prediction Sets under Poisoning (ICLR 2025 Spotlight)\n- Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)\n- ReliabilityRAG (NeurIPS 2025)\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, Mar 2026)\n- Conformal-RAG: Conditional Conformal Factuality (SIGIR 2025)\n- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv 2025)\n- PoisonedRAG (USENIX Security 2025)\n- RSB Benchmark: Benchmarking Poisoning Attacks against RAG (May 2025)\n- RAGPart & RAGMask (arXiv:2512.24268, Dec 2025)\n- Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105)\n- Semantic Chameleon (arXiv Mar 2026)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:24:55.547Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:24:55.547Z",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

## Round 1

54 recorded events

### User

_source line 3 · 2026-05-30T07:24:55.562Z_

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
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "b746bff7-efa8-435c-a22e-ef9a4f620815",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:24:55.561Z_

```json
{
  "parentUuid": "b746bff7-efa8-435c-a22e-ef9a4f620815",
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
  "uuid": "b264c940-1637-48c5-97f5-b38af89a1639",
  "timestamp": "2026-05-30T07:24:55.561Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:24:55.561Z_

```json
{
  "parentUuid": "b264c940-1637-48c5-97f5-b38af89a1639",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7f3054e9-afa1-4835-9286-26987cf1c410",
  "timestamp": "2026-05-30T07:24:55.561Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
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
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Assistant

_source line 7 · 2026-05-30T07:25:05.939Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "补救 agent" (remediation agent) to review this research proposal for AAAI 2026 submission. My job is to focus exclusively on experimental design and technical execution completeness — baselines, experimental plan, evaluation metrics, ablation design, and feasibility.

Let me first read the proposal carefully, then conduct web searches to understand the current experimental standards in this field before giving my assessment.

The proposal is about "Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores" (PRCA). It combines conformal prediction with retrieval-poisoning robustness for RAG systems.


Now I'm identifying the core technical contributions: the partition-induced reduction principle that bounds adversarial corruption through disjoint passage grouping, how this fits within the CRC framework, and the formal coverage guarantees under k-poisoning attacks. Let me search for related work and experimental benchmarks to assess what standards this field expects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f3054e9-afa1-4835-9286-26987cf1c410",
  "isSidechain": false,
  "requestId": "req_011CbYMWSF3C1Zn2RQPbex7z",
  "type": "assistant",
  "uuid": "3a33da3f-0d4a-449e-adcd-58acabcefaed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5WL7yWqQ9mzkZTofQ5qom",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4456,
      "cache_read_input_tokens": 14080,
      "output_tokens": 383,
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
          "output_tokens": 383,
          "cache_read_input_tokens": 14080,
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

_source line 8 · 2026-05-30T07:25:06.727Z_

I'll start by reading the proposal carefully, then conduct targeted web searches to understand the current experimental standards in this field before giving my assessment.

Let me do my pre-assessment research — I need to understand how the key related works design their experiments, what baselines they use, and what reviewers typically expect.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a33da3f-0d4a-449e-adcd-58acabcefaed",
  "isSidechain": false,
  "requestId": "req_011CbYMWSF3C1Zn2RQPbex7z",
  "type": "assistant",
  "uuid": "a5c7626a-e091-4101-834c-cea50df44af4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5WL7yWqQ9mzkZTofQ5qom",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4456,
      "cache_read_input_tokens": 14080,
      "output_tokens": 383,
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
          "output_tokens": 383,
          "cache_read_input_tokens": 14080,
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

_source line 9 · 2026-05-30T07:25:07.040Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01S5jbAaq8As3LBKdYzrJgnR`</summary>

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
  "parentUuid": "a5c7626a-e091-4101-834c-cea50df44af4",
  "isSidechain": false,
  "requestId": "req_011CbYMWSF3C1Zn2RQPbex7z",
  "type": "assistant",
  "uuid": "54e4b73e-45f0-4751-b65e-d1d67429a3ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5WL7yWqQ9mzkZTofQ5qom",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4456,
      "cache_read_input_tokens": 14080,
      "output_tokens": 383,
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
          "output_tokens": 383,
          "cache_read_input_tokens": 14080,
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

_source line 10 · 2026-05-30T07:25:07.048Z_

<details><summary>↩ Tool result · `toolu_01S5jbAaq8As3LBKdYzrJgnR`</summary>

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
  "parentUuid": "54e4b73e-45f0-4751-b65e-d1d67429a3ab",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "b8eda7d3-d9a7-4906-a412-29087e5b03af",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "54e4b73e-45f0-4751-b65e-d1d67429a3ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
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
  "leafUuid": "b8eda7d3-d9a7-4906-a412-29087e5b03af",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Assistant

_source line 13 · 2026-05-30T07:25:11.189Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct targeted web searches to understand the experimental standards in this field. I need to search for:

1. TRAQ and C-RAG experimental design (conformal prediction for RAG)
2. RobustRAG experimental design (certified RAG defenses)
3. PoisonedRAG experimental setup (attack methods for RAG)
4. RPS (poisoning-robust conformal prediction) experimental design
5. Recent work on conformal prediction under distribution shift

Let me do multiple searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8eda7d3-d9a7-4906-a412-29087e5b03af",
  "isSidechain": false,
  "requestId": "req_011CbYMXHYBzEXJ1HJbGeruZ",
  "type": "assistant",
  "uuid": "ec6c41c2-80a8-4e94-8b81-1be21afa07d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDUcMaLQHxnCZcVHf9KPjk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 18536,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 18536,
          "cache_creation_input_tokens": 911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 911
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

_source line 14 · 2026-05-30T07:25:11.481Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LEdqeq9dtYEUeeHatWCvaE`</summary>

```json
{
  "query": "TRAQ conformal prediction RAG experimental design baselines NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec6c41c2-80a8-4e94-8b81-1be21afa07d1",
  "isSidechain": false,
  "requestId": "req_011CbYMXHYBzEXJ1HJbGeruZ",
  "type": "assistant",
  "uuid": "1c3e20c1-5ed0-431e-b3ba-ebe41b6fa303",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDUcMaLQHxnCZcVHf9KPjk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 18536,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 18536,
          "cache_creation_input_tokens": 911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 911
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

_source line 15 · 2026-05-30T07:25:17.236Z_

<details><summary>↩ Tool result · `toolu_01LEdqeq9dtYEUeeHatWCvaE`</summary>

```text
Web search results for query: "TRAQ conformal prediction RAG experimental design baselines NAACL 2024"

Links: [{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.210/"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2307.04642"},{"title":"[PDF] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/28e078b52a761cf3fe5941d3428acb7bbf608f21"},{"title":"[Quick Review] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://liner.com/review/traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/pdf/2511.17908"}]

I found information about TRAQ. Here are the key results:

## TRAQ: Trustworthy Retrieval Augmented Question Answering

TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction was published in the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024), authored by Shuo Li, Sangdon Park, Insup Lee, and Osbert Bastani.

### Key Methodology

TRAQ uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability. Additionally, TRAQ leverages Bayesian optimization to minimize the size of the constructed sets.

### Technical Innovation

TRAQ introduces a novel nonconformity measure based on semantic uncertainty, clustering semantically equivalent answers and measuring uncertainty by the number of non-equivalent clusters. TRAQ constructs prediction sets separately for the retriever and generator, then aggregates them to ensure the ground truth answer is contained with high probability.

### Experimental Results

In an extensive experimental evaluation, TRAQ demonstrates that it provides the desired correctness guarantee while reducing prediction set size by 16.2% on average compared to an ablation.

The paper is available through the ACL Anthology at: https://aclanthology.org/2024.naacl-long.210/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c3e20c1-5ed0-431e-b3ba-ebe41b6fa303",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "38a81d5f-a739-43aa-b436-cf55ed89b716",
  "toolUseResult": {
    "query": "TRAQ conformal prediction RAG experimental design baselines NAACL 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BdK2EPxufWzKkGHePNmTb5",
        "content": [
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.210/"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/html/2307.04642v2"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2307.04642"
          },
          {
            "title": "[PDF] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/28e078b52a761cf3fe5941d3428acb7bbf608f21"
          },
          {
            "title": "[Quick Review] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://liner.com/review/traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"
          },
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://arxiv.org/pdf/2511.17908"
          }
        ]
      },
      "I found information about TRAQ. Here are the key results:\n\n## TRAQ: Trustworthy Retrieval Augmented Question Answering\n\nTRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction was published in the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024), authored by Shuo Li, Sangdon Park, Insup Lee, and Osbert Bastani.\n\n### Key Methodology\n\nTRAQ uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability. Additionally, TRAQ leverages Bayesian optimization to minimize the size of the constructed sets.\n\n### Technical Innovation\n\nTRAQ introduces a novel nonconformity measure based on semantic uncertainty, clustering semantically equivalent answers and measuring uncertainty by the number of non-equivalent clusters. TRAQ constructs prediction sets separately for the retriever and generator, then aggregates them to ensure the ground truth answer is contained with high probability.\n\n### Experimental Results\n\nIn an extensive experimental evaluation, TRAQ demonstrates that it provides the desired correctness guarantee while reducing prediction set size by 16.2% on average compared to an ablation.\n\nThe paper is available through the ACL Anthology at: https://aclanthology.org/2024.naacl-long.210/"
    ],
    "durationSeconds": 5.747837977,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1c3e20c1-5ed0-431e-b3ba-ebe41b6fa303",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-30T07:25:20.734Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CxCgTgeFhNWk9o7SYgbPLC`</summary>

```json
{
  "query": "RobustRAG certified defense retrieval corruption SaTML 2026 experimental setup datasets baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38a81d5f-a739-43aa-b436-cf55ed89b716",
  "isSidechain": false,
  "requestId": "req_011CbYMY2rRdgMnFnWgFpgHn",
  "type": "assistant",
  "uuid": "c651f900-342c-47c8-9ee4-88b3e732ef45",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8z9Et8fZFDiXbBqXzzE4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 19447,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 19447,
          "cache_creation_input_tokens": 925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 925
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

_source line 17 · 2026-05-30T07:25:21.537Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R9Fe2iooK78s1SUZWMSWzb`</summary>

```json
{
  "query": "PoisonedRAG USENIX Security 2025 experimental design NQ HotpotQA attack success rate baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c651f900-342c-47c8-9ee4-88b3e732ef45",
  "isSidechain": false,
  "requestId": "req_011CbYMY2rRdgMnFnWgFpgHn",
  "type": "assistant",
  "uuid": "adb89f26-6eb2-4847-8ce8-64dd927269c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8z9Et8fZFDiXbBqXzzE4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 19447,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 19447,
          "cache_creation_input_tokens": 925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 925
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

_source line 18 · 2026-05-30T07:25:22.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WPPfXWkP2PKoYYNmULZvyV`</summary>

```json
{
  "query": "C-RAG certified generation risks RAG ICML 2024 experiments evaluation metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adb89f26-6eb2-4847-8ce8-64dd927269c6",
  "isSidechain": false,
  "requestId": "req_011CbYMY2rRdgMnFnWgFpgHn",
  "type": "assistant",
  "uuid": "c0929ba5-2b80-45de-a987-ce7efee51159",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8z9Et8fZFDiXbBqXzzE4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 19447,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 19447,
          "cache_creation_input_tokens": 925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 925
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

_source line 19 · 2026-05-30T07:25:26.865Z_

<details><summary>↩ Tool result · `toolu_01CxCgTgeFhNWk9o7SYgbPLC`</summary>

```text
Web search results for query: "RobustRAG certified defense retrieval corruption SaTML 2026 experimental setup datasets baselines"

Links: [{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://goatstack.ai/topics/certifiably-robust-rag-against-retrieval-corruption-yclugx"},{"title":"IEEE SaTML 2026 · Program","url":"https://satml.org/program/"},{"title":"IEEE SaTML 2026 · Accepted Papers","url":"https://satml.org/accepted-papers/"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption | Request PDF","url":"https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"},{"title":"[Literature Review] Certifiably Robust RAG against Retrieval Corruption","url":"https://www.themoonlight.io/en/review/certifiably-robust-rag-against-retrieval-corruption"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"}]

Based on the search results, here's what I found about RobustRAG's experimental setup, datasets, and baselines:

## Overview
RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. The authors include Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (University of California, Berkeley), Danqi Chen and Prateek Mittal (Princeton University).

## Core Methodology
The key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then responses are securely aggregated for a robust output. To instantiate RobustRAG, keyword-based and decoding-based algorithms are designed for securely aggregating unstructured text responses.

## Experimental Setup & Datasets
The evaluation used four datasets: RealtimeQA-MC (RQA-MC) for multiple-choice open-domain QA, RealtimeQA (RQA) and Natural Questions (NQ) for short-answer open-domain QA, and the Biography generation dataset (Bio) for long-form text generation. The researchers sampled 100 queries from each dataset for experiments.

## Language Models & Baselines
RobustRAG was evaluated using Mistral-7B-Instruct, Llama2-7B-Chat, and GPT-3.5-turbo.

## Results
RobustRAG achieved 69.0–71.0% certifiable robust accuracy for RQA-MC, 24.0–49.0% for RQA, 27.0–47.0% for NQ, and 24.0–51.2% certifiable LLM-judge score for the bio generation task.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c651f900-342c-47c8-9ee4-88b3e732ef45",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "326086a3-3982-4db1-85e8-3c9df701482a",
  "toolUseResult": {
    "query": "RobustRAG certified defense retrieval corruption SaTML 2026 experimental setup datasets baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VnJd7L3U6ppY1Bm5Bk5NFa",
        "content": [
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://goatstack.ai/topics/certifiably-robust-rag-against-retrieval-corruption-yclugx"
          },
          {
            "title": "IEEE SaTML 2026 · Program",
            "url": "https://satml.org/program/"
          },
          {
            "title": "IEEE SaTML 2026 · Accepted Papers",
            "url": "https://satml.org/accepted-papers/"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption | Request PDF",
            "url": "https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"
          },
          {
            "title": "[Literature Review] Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://www.themoonlight.io/en/review/certifiably-robust-rag-against-retrieval-corruption"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview",
            "url": "https://openreview.net/forum?id=cU6ZdN87p3"
          },
          {
            "title": "[2405.15556] Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/abs/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://openreview.net/pdf?id=qsEeACAJjD"
          }
        ]
      },
      "Based on the search results, here's what I found about RobustRAG's experimental setup, datasets, and baselines:\n\n## Overview\nRobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. The authors include Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (University of California, Berkeley), Danqi Chen and Prateek Mittal (Princeton University).\n\n## Core Methodology\nThe key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then responses are securely aggregated for a robust output. To instantiate RobustRAG, keyword-based and decoding-based algorithms are designed for securely aggregating unstructured text responses.\n\n## Experimental Setup & Datasets\nThe evaluation used four datasets: RealtimeQA-MC (RQA-MC) for multiple-choice open-domain QA, RealtimeQA (RQA) and Natural Questions (NQ) for short-answer open-domain QA, and the Biography generation dataset (Bio) for long-form text generation. The researchers sampled 100 queries from each dataset for experiments.\n\n## Language Models & Baselines\nRobustRAG was evaluated using Mistral-7B-Instruct, Llama2-7B-Chat, and GPT-3.5-turbo.\n\n## Results\nRobustRAG achieved 69.0–71.0% certifiable robust accuracy for RQA-MC, 24.0–49.0% for RQA, 27.0–47.0% for NQ, and 24.0–51.2% certifiable LLM-judge score for the bio generation task."
    ],
    "durationSeconds": 6.12663896,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c651f900-342c-47c8-9ee4-88b3e732ef45",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T07:25:27.777Z_

<details><summary>↩ Tool result · `toolu_01WPPfXWkP2PKoYYNmULZvyV`</summary>

```text
Web search results for query: "C-RAG certified generation risks RAG ICML 2024 experiments evaluation metrics"

Links: [{"title":"[PDF] C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/C-RAG:-Certified-Generation-Risks-for-Language-Kang-Gurel/32c260ddd7e2d0b05c58f2e67d244b8036699db4"},{"title":"GitHub - kangmintong/C-RAG: [ICML 2024] Codes for C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models · GitHub","url":"https://github.com/kangmintong/C-RAG"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models - Illinois Experts","url":"https://experts.illinois.edu/en/publications/c-rag-certified-generation-risks-for-retrieval-augmented-language/"},{"title":"C-RAG: certified generation risks for retrieval-augmented ...","url":"https://dl.acm.org/doi/10.5555/3692070.3692994"},{"title":"[2402.03181] C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2402.03181"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2402.03181v4"},{"title":"C-RAG: Certified Generation Risks for Retrieval- ...","url":"https://par.nsf.gov/servlets/purl/10524902"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://proceedings.mlr.press/v235/kang24a.html"},{"title":"ICML Poster C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://icml.cc/virtual/2024/poster/34539"}]

Based on the search results, here's what I found about C-RAG:

## Overview

C-RAG is the first framework to certify generation risks for RAG models. It provides conformal risk analysis for RAG models and certifies an upper confidence bound of generation risks, which is referred to as conformal generation risk.

## Key Contributions

C-RAG provides theoretical guarantees on conformal generation risks for general bounded risk functions under test distribution shifts. The framework proves that RAG achieves a lower conformal generation risk than that of a single LLM when the quality of the retrieval model and transformer is non-trivial.

## Research Questions Addressed

The paper addresses: 1) whether RAG can lead to low generation risks, 2) how to provide provable guarantees on the generation risks of RAG and vanilla LLMs, and 3) what sufficient conditions enable RAG models to reduce generation risks.

## Evaluation

The empirical results demonstrate the soundness and tightness of the conformal generation risk guarantees across four widely-used NLP datasets on four state-of-the-art retrieval models.

The paper was published at ICML 2024 (the 41st International Conference on Machine Learning) by authors Mintong Kang, Nezihe Merve Gürel, Ning Yu, Dawn Song, and Bo Li.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0929ba5-2b80-45de-a987-ce7efee51159",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "602ad9dc-84ec-4a18-a693-947d4f802216",
  "toolUseResult": {
    "query": "C-RAG certified generation risks RAG ICML 2024 experiments evaluation metrics",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PVNHyLirX13kqgy11hQhPA",
        "content": [
          {
            "title": "[PDF] C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/C-RAG:-Certified-Generation-Risks-for-Language-Kang-Gurel/32c260ddd7e2d0b05c58f2e67d244b8036699db4"
          },
          {
            "title": "GitHub - kangmintong/C-RAG: [ICML 2024] Codes for C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models · GitHub",
            "url": "https://github.com/kangmintong/C-RAG"
          },
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models - Illinois Experts",
            "url": "https://experts.illinois.edu/en/publications/c-rag-certified-generation-risks-for-retrieval-augmented-language/"
          },
          {
            "title": "C-RAG: certified generation risks for retrieval-augmented ...",
            "url": "https://dl.acm.org/doi/10.5555/3692070.3692994"
          },
          {
            "title": "[2402.03181] C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
            "url": "https://arxiv.org/abs/2402.03181"
          },
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
            "url": "https://arxiv.org/html/2402.03181v4"
          },
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval- ...",
            "url": "https://par.nsf.gov/servlets/purl/10524902"
          },
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
            "url": "https://proceedings.mlr.press/v235/kang24a.html"
          },
          {
            "title": "ICML Poster C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
            "url": "https://icml.cc/virtual/2024/poster/34539"
          }
        ]
      },
      "Based on the search results, here's what I found about C-RAG:\n\n## Overview\n\nC-RAG is the first framework to certify generation risks for RAG models. It provides conformal risk analysis for RAG models and certifies an upper confidence bound of generation risks, which is referred to as conformal generation risk.\n\n## Key Contributions\n\nC-RAG provides theoretical guarantees on conformal generation risks for general bounded risk functions under test distribution shifts. The framework proves that RAG achieves a lower conformal generation risk than that of a single LLM when the quality of the retrieval model and transformer is non-trivial.\n\n## Research Questions Addressed\n\nThe paper addresses: 1) whether RAG can lead to low generation risks, 2) how to provide provable guarantees on the generation risks of RAG and vanilla LLMs, and 3) what sufficient conditions enable RAG models to reduce generation risks.\n\n## Evaluation\n\nThe empirical results demonstrate the soundness and tightness of the conformal generation risk guarantees across four widely-used NLP datasets on four state-of-the-art retrieval models.\n\nThe paper was published at ICML 2024 (the 41st International Conference on Machine Learning) by authors Mintong Kang, Nezihe Merve Gürel, Ning Yu, Dawn Song, and Bo Li."
    ],
    "durationSeconds": 5.720616907999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c0929ba5-2b80-45de-a987-ce7efee51159",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T07:25:30.395Z_

<details><summary>↩ Tool result · `toolu_01R9Fe2iooK78s1SUZWMSWzb`</summary>

```text
Web search results for query: "PoisonedRAG USENIX Security 2025 experimental design NQ HotpotQA attack success rate baselines"

Links: [{"title":"RAG Security: How Attackers Poison Your Knowledge Base | BeyondScale","url":"https://beyondscale.tech/blog/rag-security-data-poisoning-guide"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation","url":"https://www.usenix.org/system/files/conference/usenixsecurity25/sec24winter-prepub-1468-zou.pdf"},{"title":"PoisonedRAG | Proceedings of the 34th USENIX Conference on Security Symposium","url":"https://dl.acm.org/doi/10.5555/3766078.3766275"},{"title":"PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/html/2402.07867v1"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/html/2402.07867v2"},{"title":"GitHub - thisxyz/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://github.com/thisxyz/PoisonedRAG"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval- ...","url":"https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"}]

Based on the search results, here is information about PoisonedRAG's experimental design and results:

## Overview
PoisonedRAG was published at USENIX Security 2025 by researchers at Penn State and the Illinois Institute of Technology.

## Experimental Design
The researchers selected close-ended questions (e.g., "Who is the CEO of OpenAI?") rather than open-ended questions because they aimed to quantitatively evaluate the effectiveness of attacks since close-ended questions have specific, factual answers. For each target question, they used GPT-4 to randomly generate an answer different from the ground truth answer, and manually checked each generated target answer.

## Baseline Performance (Without Attacks)
Without attacks, the LLM in RAG could correctly provide answers for 70% (NQ), 80% (HotpotQA), and 83% (MS-MARCO) target questions under the default setting.

## Attack Success Rates
In the black-box setting, PoisonedRAG could achieve 97% (on NQ), 99% (on HotpotQA), and 91% (on MS-MARCO) ASRs for RAG with PaLM 2. PoisonedRAG achieved high ASRs on different datasets and LLMs under both white-box and black-box settings when injecting 5 malicious texts for each target question into a knowledge database with millions of texts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adb89f26-6eb2-4847-8ce8-64dd927269c6",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "719b7b27-29aa-4ecd-81f8-4a4edbeec4c5",
  "toolUseResult": {
    "query": "PoisonedRAG USENIX Security 2025 experimental design NQ HotpotQA attack success rate baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GDxHr1KyuHg7XPjawU3B7V",
        "content": [
          {
            "title": "RAG Security: How Attackers Poison Your Knowledge Base | BeyondScale",
            "url": "https://beyondscale.tech/blog/rag-security-data-poisoning-guide"
          },
          {
            "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation",
            "url": "https://www.usenix.org/system/files/conference/usenixsecurity25/sec24winter-prepub-1468-zou.pdf"
          },
          {
            "title": "PoisonedRAG | Proceedings of the 34th USENIX Conference on Security Symposium",
            "url": "https://dl.acm.org/doi/10.5555/3766078.3766275"
          },
          {
            "title": "PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models",
            "url": "https://arxiv.org/html/2402.07867v1"
          },
          {
            "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models",
            "url": "https://arxiv.org/html/2402.07867v2"
          },
          {
            "title": "GitHub - thisxyz/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models",
            "url": "https://github.com/thisxyz/PoisonedRAG"
          },
          {
            "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval- ...",
            "url": "https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf"
          },
          {
            "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX",
            "url": "https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"
          },
          {
            "title": "GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub",
            "url": "https://github.com/sleeepeer/PoisonedRAG"
          }
        ]
      },
      "Based on the search results, here is information about PoisonedRAG's experimental design and results:\n\n## Overview\nPoisonedRAG was published at USENIX Security 2025 by researchers at Penn State and the Illinois Institute of Technology.\n\n## Experimental Design\nThe researchers selected close-ended questions (e.g., \"Who is the CEO of OpenAI?\") rather than open-ended questions because they aimed to quantitatively evaluate the effectiveness of attacks since close-ended questions have specific, factual answers. For each target question, they used GPT-4 to randomly generate an answer different from the ground truth answer, and manually checked each generated target answer.\n\n## Baseline Performance (Without Attacks)\nWithout attacks, the LLM in RAG could correctly provide answers for 70% (NQ), 80% (HotpotQA), and 83% (MS-MARCO) target questions under the default setting.\n\n## Attack Success Rates\nIn the black-box setting, PoisonedRAG could achieve 97% (on NQ), 99% (on HotpotQA), and 91% (on MS-MARCO) ASRs for RAG with PaLM 2. PoisonedRAG achieved high ASRs on different datasets and LLMs under both white-box and black-box settings when injecting 5 malicious texts for each target question into a knowledge database with millions of texts."
    ],
    "durationSeconds": 8.854509761000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "adb89f26-6eb2-4847-8ce8-64dd927269c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "719b7b27-29aa-4ecd-81f8-4a4edbeec4c5",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Tool call

_source line 24 · 2026-05-30T07:25:33.364Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uv5hywF9MFe8yaBz9H1Abu`</summary>

```json
{
  "query": "RPS poisoning-robust conformal prediction ICLR 2025 spotlight experimental design calibration set"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "719b7b27-29aa-4ecd-81f8-4a4edbeec4c5",
  "isSidechain": false,
  "requestId": "req_011CbYMZ1AVx7JbRwHqMECwA",
  "type": "assistant",
  "uuid": "fbecd074-2e6c-4a0c-ac09-cc3b02d4d6bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzAxmkPHqMfNVKJRdb7n63",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 885,
      "cache_creation_input_tokens": 2033,
      "cache_read_input_tokens": 20372,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 885,
          "output_tokens": 133,
          "cache_read_input_tokens": 20372,
          "cache_creation_input_tokens": 2033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2033
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

_source line 25 · 2026-05-30T07:25:34.167Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017vM513s5NzYa3rj1WnMLDT`</summary>

```json
{
  "query": "ReliabilityRAG NeurIPS 2025 graph MIS NLI robust document filtering experimental evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbecd074-2e6c-4a0c-ac09-cc3b02d4d6bb",
  "isSidechain": false,
  "requestId": "req_011CbYMZ1AVx7JbRwHqMECwA",
  "type": "assistant",
  "uuid": "1198805f-0f18-40bf-b5cc-88e45e28515a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzAxmkPHqMfNVKJRdb7n63",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 885,
      "cache_creation_input_tokens": 2033,
      "cache_read_input_tokens": 20372,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 885,
          "output_tokens": 133,
          "cache_read_input_tokens": 20372,
          "cache_creation_input_tokens": 2033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2033
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

_source line 26 · 2026-05-30T07:25:38.330Z_

<details><summary>↩ Tool result · `toolu_01Uv5hywF9MFe8yaBz9H1Abu`</summary>

```text
Web search results for query: "RPS poisoning-robust conformal prediction ICLR 2025 spotlight experimental design calibration set"

Links: [{"title":"Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning","url":"https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview","url":"https://openreview.net/forum?id=ofuLWn8DFZ"},{"title":"Published as a conference paper at ICLR 2025","url":"https://yascho.github.io/assets/pdf/scholten2025provably.pdf"},{"title":"GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).","url":"https://github.com/yascho/reliable_conformal_prediction"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"},{"title":"PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich","url":"https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"},{"title":"ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://iclr.cc/virtual/2025/poster/28340"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"}]

Based on the search results, I found information about the RPS poisoning-robust conformal prediction paper accepted at ICLR 2025:

## Paper Overview

The paper "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning" is a Spotlight presentation at ICLR 2025 by Yan Scholten and Stephan Günnemann.

## Key Approach

The paper addresses the fact that conformal prediction is not reliable under poisoning attacks where adversaries manipulate both training and calibration data, and proposes reliable prediction sets (RPS) as the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning.

## Technical Components

The method has two main components:

1. **Training Poisoning**: To ensure reliability under training poisoning, the approach introduces smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data.

2. **Calibration Poisoning**: To ensure reliability under calibration poisoning, the approach constructs multiple prediction sets, each calibrated on distinct subsets of the calibration data.

## Implementation

The authors ensure reproducibility by documenting all hyperparameters and experimental setups, and provide code along with detailed reproducibility instructions via their project page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbecd074-2e6c-4a0c-ac09-cc3b02d4d6bb",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "89ecd166-6111-4f2c-a544-46b98e153368",
  "toolUseResult": {
    "query": "RPS poisoning-robust conformal prediction ICLR 2025 spotlight experimental design calibration set",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ni3YeNX27fAxNHy2WNFwbz",
        "content": [
          {
            "title": "Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning",
            "url": "https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview",
            "url": "https://openreview.net/forum?id=ofuLWn8DFZ"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://yascho.github.io/assets/pdf/scholten2025provably.pdf"
          },
          {
            "title": "GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).",
            "url": "https://github.com/yascho/reliable_conformal_prediction"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"
          },
          {
            "title": "PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich",
            "url": "https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"
          },
          {
            "title": "ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://iclr.cc/virtual/2025/poster/28340"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          }
        ]
      },
      "Based on the search results, I found information about the RPS poisoning-robust conformal prediction paper accepted at ICLR 2025:\n\n## Paper Overview\n\nThe paper \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" is a Spotlight presentation at ICLR 2025 by Yan Scholten and Stephan Günnemann.\n\n## Key Approach\n\nThe paper addresses the fact that conformal prediction is not reliable under poisoning attacks where adversaries manipulate both training and calibration data, and proposes reliable prediction sets (RPS) as the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning.\n\n## Technical Components\n\nThe method has two main components:\n\n1. **Training Poisoning**: To ensure reliability under training poisoning, the approach introduces smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data.\n\n2. **Calibration Poisoning**: To ensure reliability under calibration poisoning, the approach constructs multiple prediction sets, each calibrated on distinct subsets of the calibration data.\n\n## Implementation\n\nThe authors ensure reproducibility by documenting all hyperparameters and experimental setups, and provide code along with detailed reproducibility instructions via their project page."
    ],
    "durationSeconds": 4.961046270999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fbecd074-2e6c-4a0c-ac09-cc3b02d4d6bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-30T07:25:49.153Z_

<details><summary>↩ Tool result · `toolu_017vM513s5NzYa3rj1WnMLDT`</summary>

```text
Web search results for query: "ReliabilityRAG NeurIPS 2025 graph MIS NLI robust document filtering experimental evaluation"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/media/neurips-2025/Slides/119236.pdf"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/poster/119236"},{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"ChunkRAG: Novel LLM-Chunk Filtering Method for RAG Systems","url":"https://arxiv.org/pdf/2410.19572"},{"title":"Retrieval-Augmented Generation with Estimation of Source Reliability","url":"https://arxiv.org/pdf/2410.22954"},{"title":"Tackling the Inherent Difficulty of Noise Filtering in RAG","url":"https://arxiv.org/pdf/2601.01896"},{"title":"MAIN-RAG: Multi-Agent Filtering Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2501.00332"}]

Based on the search results, here's what I found about ReliabilityRAG at NeurIPS 2025:

## ReliabilityRAG: Overview

ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents.

## Core Technical Approach

The high-level idea is to find a "consistent majority" over the set of documents by constructing a graph where each document is a vertex with edges between contradictory documents, checking contradictions using an NLI model, and finding a maximum independent set (MIS) in the graph.

## Key Features

The MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions. To address the computational cost of exact MIS for large retrieval sets, a scalable weighted sample and aggregate framework was developed that explicitly utilizes reliability information while efficiently handling many documents.

## Experimental Evaluation

ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled. Additionally, the overhead of the entire pipeline is negligible.

The paper is available at arXiv (2509.23519) and was presented at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1198805f-0f18-40bf-b5cc-88e45e28515a",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "a9cb6b0d-3635-42a9-8bfd-c125b91f060e",
  "toolUseResult": {
    "query": "ReliabilityRAG NeurIPS 2025 graph MIS NLI robust document filtering experimental evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uawoo5dFh4zx1Wj1NAWvUZ",
        "content": [
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
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          },
          {
            "title": "ChunkRAG: Novel LLM-Chunk Filtering Method for RAG Systems",
            "url": "https://arxiv.org/pdf/2410.19572"
          },
          {
            "title": "Retrieval-Augmented Generation with Estimation of Source Reliability",
            "url": "https://arxiv.org/pdf/2410.22954"
          },
          {
            "title": "Tackling the Inherent Difficulty of Noise Filtering in RAG",
            "url": "https://arxiv.org/pdf/2601.01896"
          },
          {
            "title": "MAIN-RAG: Multi-Agent Filtering Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2501.00332"
          }
        ]
      },
      "Based on the search results, here's what I found about ReliabilityRAG at NeurIPS 2025:\n\n## ReliabilityRAG: Overview\n\nReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents.\n\n## Core Technical Approach\n\nThe high-level idea is to find a \"consistent majority\" over the set of documents by constructing a graph where each document is a vertex with edges between contradictory documents, checking contradictions using an NLI model, and finding a maximum independent set (MIS) in the graph.\n\n## Key Features\n\nThe MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions. To address the computational cost of exact MIS for large retrieval sets, a scalable weighted sample and aggregate framework was developed that explicitly utilizes reliability information while efficiently handling many documents.\n\n## Experimental Evaluation\n\nReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled. Additionally, the overhead of the entire pipeline is negligible.\n\nThe paper is available at arXiv (2509.23519) and was presented at NeurIPS 2025."
    ],
    "durationSeconds": 14.982459976999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1198805f-0f18-40bf-b5cc-88e45e28515a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-30T07:25:52.026Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RjuH5si4dKk1YBV7SFTJoT`</summary>

```json
{
  "query": "conformal prediction RAG robustness distribution shift Chen 2026 arXiv vacuous prediction sets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9cb6b0d-3635-42a9-8bfd-c125b91f060e",
  "isSidechain": false,
  "requestId": "req_011CbYMaPHYpXi3ow3GYngjV",
  "type": "assistant",
  "uuid": "afba8b5a-120b-4aa6-9165-04a82daa88c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2vceRFhhZ6U8UwfuXGrY3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2616,
      "cache_read_input_tokens": 22405,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2616,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 22405,
          "cache_creation_input_tokens": 2616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2616
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

_source line 29 · 2026-05-30T07:25:52.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019dfD9mWc94MWqrGTiA8Nf4`</summary>

```json
{
  "query": "CorruptRAG single document poisoning attack RAG 2025 experimental evaluation defense"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afba8b5a-120b-4aa6-9165-04a82daa88c2",
  "isSidechain": false,
  "requestId": "req_011CbYMaPHYpXi3ow3GYngjV",
  "type": "assistant",
  "uuid": "8d9b70cd-fa56-4f2d-bb11-983ca91743e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2vceRFhhZ6U8UwfuXGrY3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2616,
      "cache_read_input_tokens": 22405,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2616,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 22405,
          "cache_creation_input_tokens": 2616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2616
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

_source line 30 · 2026-05-30T07:25:57.572Z_

<details><summary>↩ Tool result · `toolu_01RjuH5si4dKk1YBV7SFTJoT`</summary>

```text
Web search results for query: "conformal prediction RAG robustness distribution shift Chen 2026 arXiv vacuous prediction sets"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/pdf/2502.14105"},{"title":"[2502.14105] Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/abs/2502.14105"},{"title":"Not all distributional shifts are equal: Fine-grained robust conformal inference","url":"https://arxiv.org/pdf/2402.13042"}]

Perfect! I found highly relevant results. The primary match is the paper you're searching for:

**"Is Conformal Factuality for RAG-based LLMs Robust?"** by Yi Chen et al. (arXiv 2603.16817, March 2026) finds that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and the conformal factuality guarantee is not robust to distribution shifts and distractors.

The paper highlights the fragility of the conformal filtering framework under distribution shifts and distractors, emphasizing the need for new approaches that balance reliability with robustness and usefulness as key metrics for building RAG pipelines.

The search also returned related work on conformal prediction robustness under distribution shifts, including papers on Levy-Prokhorov ambiguity sets and other approaches to making conformal prediction more robust to distribution shifts in general machine learning contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afba8b5a-120b-4aa6-9165-04a82daa88c2",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "150210d8-f579-4f40-8df3-37f3bdb446e0",
  "toolUseResult": {
    "query": "conformal prediction RAG robustness distribution shift Chen 2026 arXiv vacuous prediction sets",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DheRxPturmf4MeRMoxAQ5z",
        "content": [
          {
            "title": "[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/abs/2603.16817"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/pdf/2502.14105"
          },
          {
            "title": "[2502.14105] Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/abs/2502.14105"
          },
          {
            "title": "Not all distributional shifts are equal: Fine-grained robust conformal inference",
            "url": "https://arxiv.org/pdf/2402.13042"
          }
        ]
      },
      "Perfect! I found highly relevant results. The primary match is the paper you're searching for:\n\n**\"Is Conformal Factuality for RAG-based LLMs Robust?\"** by Yi Chen et al. (arXiv 2603.16817, March 2026) finds that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and the conformal factuality guarantee is not robust to distribution shifts and distractors.\n\nThe paper highlights the fragility of the conformal filtering framework under distribution shifts and distractors, emphasizing the need for new approaches that balance reliability with robustness and usefulness as key metrics for building RAG pipelines.\n\nThe search also returned related work on conformal prediction robustness under distribution shifts, including papers on Levy-Prokhorov ambiguity sets and other approaches to making conformal prediction more robust to distribution shifts in general machine learning contexts."
    ],
    "durationSeconds": 5.540694976999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "afba8b5a-120b-4aa6-9165-04a82daa88c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-30T07:25:59.163Z_

<details><summary>↩ Tool result · `toolu_019dfD9mWc94MWqrGTiA8Nf4`</summary>

```text
Web search results for query: "CorruptRAG single document poisoning attack RAG 2025 experimental evaluation defense"

Links: [{"title":"RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium","url":"https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/html/2511.01268v1"},{"title":"RAG Poisoning: How Attackers Corrupt Your AI's Knowledge Base | Amine Raji, PhD","url":"https://aminrj.com/posts/rag-document-poisoning/"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957"},{"title":"CtrlRAG: Black-box Document Poisoning Attacks for Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/pdf/2503.06950"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention","url":"https://arxiv.org/html/2602.04711"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2504.03957"}]

I found comprehensive information about CorruptRAG and related research on RAG poisoning attacks. Here's what the search revealed:

## CorruptRAG Attack Overview

CorruptRAG is a practical poisoning attack against RAG systems in which the attacker injects only a single poisoned text, enhancing both feasibility and stealth. This addresses the limitation of existing attacks that assume the attacker can insert a sufficient number of poisoned texts per query to outnumber correct-answer texts in retrieval, an assumption that is often unrealistic.

## Attack Variants

The research describes two variants of CorruptRAG:
- CorruptRAG-AK enhances generalizability by leveraging an LLM to refine the poisoned text into adversarial knowledge, extending the attack's impact to enable the LLM to generate the targeted answer not only for the specific targeted query but also for other related queries influenced by the adversarial knowledge.

## Experimental Evaluation

The researchers evaluated CorruptRAG against four state-of-the-art poisoning attacks on RAG across three benchmark datasets, demonstrating that CorruptRAG effectively manipulates RAG systems and successfully bypasses four advanced defense mechanisms while maintaining a high attack success rate. Across all attacks, one poisoned text is injected per targeted query for fair comparison.

## Defense Evaluation

Results demonstrate that while LLM-based detection is highly effective against other attacks, it has minimal impact on CorruptRAG attacks, with the true positive rate being no greater than 0.10 across the three datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d9b70cd-fa56-4f2d-bb11-983ca91743e2",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "260e57d6-f02e-490a-b35e-b1a8c9e9db68",
  "toolUseResult": {
    "query": "CorruptRAG single document poisoning attack RAG 2025 experimental evaluation defense",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QCfwgetkqWvtVepQPKNeWk",
        "content": [
          {
            "title": "RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium",
            "url": "https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"
          },
          {
            "title": "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems",
            "url": "https://arxiv.org/html/2511.01268v1"
          },
          {
            "title": "RAG Poisoning: How Attackers Corrupt Your AI's Knowledge Base | Amine Raji, PhD",
            "url": "https://aminrj.com/posts/rag-document-poisoning/"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2504.03957"
          },
          {
            "title": "CtrlRAG: Black-box Document Poisoning Attacks for Retrieval-Augmented Generation of Large Language Models",
            "url": "https://arxiv.org/pdf/2503.06950"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/pdf/2603.18034"
          },
          {
            "title": "Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention",
            "url": "https://arxiv.org/html/2602.04711"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2504.03957"
          }
        ]
      },
      "I found comprehensive information about CorruptRAG and related research on RAG poisoning attacks. Here's what the search revealed:\n\n## CorruptRAG Attack Overview\n\nCorruptRAG is a practical poisoning attack against RAG systems in which the attacker injects only a single poisoned text, enhancing both feasibility and stealth. This addresses the limitation of existing attacks that assume the attacker can insert a sufficient number of poisoned texts per query to outnumber correct-answer texts in retrieval, an assumption that is often unrealistic.\n\n## Attack Variants\n\nThe research describes two variants of CorruptRAG:\n- CorruptRAG-AK enhances generalizability by leveraging an LLM to refine the poisoned text into adversarial knowledge, extending the attack's impact to enable the LLM to generate the targeted answer not only for the specific targeted query but also for other related queries influenced by the adversarial knowledge.\n\n## Experimental Evaluation\n\nThe researchers evaluated CorruptRAG against four state-of-the-art poisoning attacks on RAG across three benchmark datasets, demonstrating that CorruptRAG effectively manipulates RAG systems and successfully bypasses four advanced defense mechanisms while maintaining a high attack success rate. Across all attacks, one poisoned text is injected per targeted query for fair comparison.\n\n## Defense Evaluation\n\nResults demonstrate that while LLM-based detection is highly effective against other attacks, it has minimal impact on CorruptRAG attacks, with the true positive rate being no greater than 0.10 across the three datasets."
    ],
    "durationSeconds": 6.496546195000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8d9b70cd-fa56-4f2d-bb11-983ca91743e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-30T07:25:59.166Z_

```json
{
  "parentUuid": "260e57d6-f02e-490a-b35e-b1a8c9e9db68",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "684130da-5fec-40b1-9adc-37d0918bfe0f",
  "timestamp": "2026-05-30T07:25:59.166Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-30T07:26:02.229Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TapKjsNks82ob8oHKgtddC`</summary>

```json
{
  "query": "RSB benchmark poisoning attacks RAG 2025 13 attack methods evaluation defense taxonomy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "684130da-5fec-40b1-9adc-37d0918bfe0f",
  "isSidechain": false,
  "requestId": "req_011CbYMb8AF1ynJyv8aGJWie",
  "type": "assistant",
  "uuid": "21ee5d90-4e11-4c00-9079-a81edb1449ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNtDfn7HeRDGNP61b8wbzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1570,
      "cache_read_input_tokens": 25021,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1570,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 25021,
          "cache_creation_input_tokens": 1570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1570
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

_source line 34 · 2026-05-30T07:26:02.741Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FwPpPr9GYUe8gxR7Uhw7cg`</summary>

```json
{
  "query": "conformal risk control CRC ICLR 2024 TV distance quantile inflation coverage guarantee"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21ee5d90-4e11-4c00-9079-a81edb1449ae",
  "isSidechain": false,
  "requestId": "req_011CbYMb8AF1ynJyv8aGJWie",
  "type": "assistant",
  "uuid": "f026c923-d373-4124-b21a-1e187a79e3c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNtDfn7HeRDGNP61b8wbzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1570,
      "cache_read_input_tokens": 25021,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1570,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 25021,
          "cache_creation_input_tokens": 1570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1570
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "f026c923-d373-4124-b21a-1e187a79e3c7",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Tool result

_source line 37 · 2026-05-30T07:26:08.670Z_

<details><summary>↩ Tool result · `toolu_01FwPpPr9GYUe8gxR7Uhw7cg`</summary>

```text
Web search results for query: "conformal risk control CRC ICLR 2024 TV distance quantile inflation coverage guarantee"

Links: [{"title":"Conformal Risk Control | OpenReview","url":"https://openreview.net/forum?id=33XGfHLtZg"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL RISK CONTROL","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/f3549ef9b5ff520a7e41ff3cc306ab2b-Paper-Conference.pdf"},{"title":"Conformal Risk Control","url":"https://arxiv.org/pdf/2208.02814"},{"title":"[Quick Review] Conformal Risk Control","url":"https://liner.com/review/conformal-risk-control"},{"title":"[2208.02814] Conformal Risk Control","url":"https://arxiv.org/abs/2208.02814"},{"title":"Conformal Risk Control","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/8759c20675d67ef3b91c4607cecbb27e-Supplementary-Conference.pdf"},{"title":"Anytime-Valid Conformal Risk Control","url":"https://arxiv.org/html/2602.04364v1"},{"title":"Conformal Risk Control","url":"https://research.google/pubs/conformal-risk-control/"},{"title":"Non-monotonicity in Conformal Risk Control","url":"https://arxiv.org/pdf/2604.01502"}]

Based on the web search results, I found relevant information about Conformal Risk Control (CRC) from ICLR 2024:

## Conformal Risk Control (CRC) Overview

The work extends conformal prediction to control the expected value of any monotone loss function, generalizing split conformal prediction together with its coverage guarantee. Like conformal prediction, the conformal risk control procedure is tight up to an O(1/n) factor.

## Key Extensions

The work introduces extensions of the idea to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics. Worked examples from computer vision and natural language processing demonstrate the usage of the algorithm to bound the false negative rate, graph distance, and token-level F1-score.

## Related Research

The search results also revealed follow-up work on non-monotonicity in CRC, which explores scenarios where the monotonicity assumption is violated in practice. Conformal risk control provides distribution-free guarantees for controlling the expected loss at a user-specified level, with existing theory typically assuming that the loss decreases monotonically with a tuning parameter.

The ICLR 2024 paper was published in the conference proceedings with authors Angelopoulos, Bates, Fisch, Lei, and Schuster.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f026c923-d373-4124-b21a-1e187a79e3c7",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "824a68ea-25c4-430f-a80e-f419e0a2fe14",
  "toolUseResult": {
    "query": "conformal risk control CRC ICLR 2024 TV distance quantile inflation coverage guarantee",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SgqJNyT31qDDzV8A745wkN",
        "content": [
          {
            "title": "Conformal Risk Control | OpenReview",
            "url": "https://openreview.net/forum?id=33XGfHLtZg"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 CONFORMAL RISK CONTROL",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/f3549ef9b5ff520a7e41ff3cc306ab2b-Paper-Conference.pdf"
          },
          {
            "title": "Conformal Risk Control",
            "url": "https://arxiv.org/pdf/2208.02814"
          },
          {
            "title": "[Quick Review] Conformal Risk Control",
            "url": "https://liner.com/review/conformal-risk-control"
          },
          {
            "title": "[2208.02814] Conformal Risk Control",
            "url": "https://arxiv.org/abs/2208.02814"
          },
          {
            "title": "Conformal Risk Control",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html"
          },
          {
            "title": "Published as a conference paper at ICLR 2024",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/8759c20675d67ef3b91c4607cecbb27e-Supplementary-Conference.pdf"
          },
          {
            "title": "Anytime-Valid Conformal Risk Control",
            "url": "https://arxiv.org/html/2602.04364v1"
          },
          {
            "title": "Conformal Risk Control",
            "url": "https://research.google/pubs/conformal-risk-control/"
          },
          {
            "title": "Non-monotonicity in Conformal Risk Control",
            "url": "https://arxiv.org/pdf/2604.01502"
          }
        ]
      },
      "Based on the web search results, I found relevant information about Conformal Risk Control (CRC) from ICLR 2024:\n\n## Conformal Risk Control (CRC) Overview\n\nThe work extends conformal prediction to control the expected value of any monotone loss function, generalizing split conformal prediction together with its coverage guarantee. Like conformal prediction, the conformal risk control procedure is tight up to an O(1/n) factor.\n\n## Key Extensions\n\nThe work introduces extensions of the idea to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics. Worked examples from computer vision and natural language processing demonstrate the usage of the algorithm to bound the false negative rate, graph distance, and token-level F1-score.\n\n## Related Research\n\nThe search results also revealed follow-up work on non-monotonicity in CRC, which explores scenarios where the monotonicity assumption is violated in practice. Conformal risk control provides distribution-free guarantees for controlling the expected loss at a user-specified level, with existing theory typically assuming that the loss decreases monotonically with a tuning parameter.\n\nThe ICLR 2024 paper was published in the conference proceedings with authors Angelopoulos, Bates, Fisch, Lei, and Schuster."
    ],
    "durationSeconds": 5.926008833,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f026c923-d373-4124-b21a-1e187a79e3c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-30T07:26:11.463Z_

<details><summary>↩ Tool result · `toolu_01TapKjsNks82ob8oHKgtddC`</summary>

```text
Web search results for query: "RSB benchmark poisoning attacks RAG 2025 13 attack methods evaluation defense taxonomy"

Links: [{"title":"Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2505.18543v1"},{"title":"(PDF) Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://www.researchgate.net/publication/392105526_Benchmarking_Poisoning_Attacks_against_Retrieval-Augmented_Generation"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/html/2603.18034v1"},{"title":"[PDF] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Benchmarking-Poisoning-Attacks-against-Generation-Zhang-Xin/ccf24f7db7680562628545beaa26fca9d3745e1e"},{"title":"[2505.18543] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.18543"},{"title":"Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.18543"},{"title":"PoisonArena: Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.12574"},{"title":"Towards Secure Retrieval-Augmented Generation: A Comprehensive Review of Threats, Defenses and Benchmarks","url":"https://arxiv.org/pdf/2603.21654"}]

I found comprehensive information about the RSB (RAG Security Bench) benchmark on poisoning attacks. Here's what the search revealed:

## RSB Benchmark Overview

RAG Security Bench (RSB) is a unified benchmark that systematically evaluates a broad range of poisoning attacks and defense mechanisms across diverse RAG architectures.

## Attack Classification

The RSB benchmark includes 13 representative poisoning attacks, classified into three categories based on their adversarial objectives: targeted poisoning, denial-of-service (DoS), and trigger-based DoS.

## Evaluation Scope

The benchmark covers 5 standard question answering (QA) datasets and 10 expanded variants, along with 13 poisoning attack methods and 7 defense mechanisms, representing a broad spectrum of existing techniques.

## Defense Mechanisms

RSB incorporates 7 representative defense methods, organized into three categories. Hybrid defenses combine detection techniques with prompt engineering or system-level adaptations to enhance robustness.

## Advanced RAG Architectures Tested

RSB extends its evaluation to 6 advanced RAG frameworks spanning four categories: sequential RAG with fixed retrieval-generation pipelines, branching RAG that explores multiple retrieval paths, conditional RAG that adapts retrieval based on the query content, and loop RAG that performs iterative refinement. In addition to these frameworks, RSB also encompasses evaluations of advanced architectures, including multi-turn conversational RAG, multimodal RAG systems, and RAG-based LLM agent systems.

## Key Findings

While existing attacks perform well on standard QA datasets, their effectiveness drops significantly on the expanded versions. Various advanced RAG architectures remain susceptible to poisoning attacks. Current defense techniques fail to provide robust protection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21ee5d90-4e11-4c00-9079-a81edb1449ae",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "ce673385-4f1a-4c62-b5d8-33c9421c6315",
  "toolUseResult": {
    "query": "RSB benchmark poisoning attacks RAG 2025 13 attack methods evaluation defense taxonomy",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TBc8obx2dB8JCncLrQCNfA",
        "content": [
          {
            "title": "Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2505.18543v1"
          },
          {
            "title": "(PDF) Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://www.researchgate.net/publication/392105526_Benchmarking_Poisoning_Attacks_against_Retrieval-Augmented_Generation"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/html/2603.18034v1"
          },
          {
            "title": "[PDF] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Benchmarking-Poisoning-Attacks-against-Generation-Zhang-Xin/ccf24f7db7680562628545beaa26fca9d3745e1e"
          },
          {
            "title": "[2505.18543] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2505.18543"
          },
          {
            "title": "Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.18543"
          },
          {
            "title": "PoisonArena: Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.12574"
          },
          {
            "title": "Towards Secure Retrieval-Augmented Generation: A Comprehensive Review of Threats, Defenses and Benchmarks",
            "url": "https://arxiv.org/pdf/2603.21654"
          }
        ]
      },
      "I found comprehensive information about the RSB (RAG Security Bench) benchmark on poisoning attacks. Here's what the search revealed:\n\n## RSB Benchmark Overview\n\nRAG Security Bench (RSB) is a unified benchmark that systematically evaluates a broad range of poisoning attacks and defense mechanisms across diverse RAG architectures.\n\n## Attack Classification\n\nThe RSB benchmark includes 13 representative poisoning attacks, classified into three categories based on their adversarial objectives: targeted poisoning, denial-of-service (DoS), and trigger-based DoS.\n\n## Evaluation Scope\n\nThe benchmark covers 5 standard question answering (QA) datasets and 10 expanded variants, along with 13 poisoning attack methods and 7 defense mechanisms, representing a broad spectrum of existing techniques.\n\n## Defense Mechanisms\n\nRSB incorporates 7 representative defense methods, organized into three categories. Hybrid defenses combine detection techniques with prompt engineering or system-level adaptations to enhance robustness.\n\n## Advanced RAG Architectures Tested\n\nRSB extends its evaluation to 6 advanced RAG frameworks spanning four categories: sequential RAG with fixed retrieval-generation pipelines, branching RAG that explores multiple retrieval paths, conditional RAG that adapts retrieval based on the query content, and loop RAG that performs iterative refinement. In addition to these frameworks, RSB also encompasses evaluations of advanced architectures, including multi-turn conversational RAG, multimodal RAG systems, and RAG-based LLM agent systems.\n\n## Key Findings\n\nWhile existing attacks perform well on standard QA datasets, their effectiveness drops significantly on the expanded versions. Various advanced RAG architectures remain susceptible to poisoning attacks. Current defense techniques fail to provide robust protection."
    ],
    "durationSeconds": 9.227665240000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "21ee5d90-4e11-4c00-9079-a81edb1449ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-30T07:26:14.702Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more search to understand the RAGPart paper and any recent developments in conformal prediction for adversarial settings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce673385-4f1a-4c62-b5d8-33c9421c6315",
  "isSidechain": false,
  "requestId": "req_011CbYMc2maNKzqiJwmK3Jd9",
  "type": "assistant",
  "uuid": "81ca5d8c-1845-48b3-9848-ddb962e5d530",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P79pEZ8cCdowH34z1jBJpM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 795,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 26591,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 795,
          "output_tokens": 182,
          "cache_read_input_tokens": 26591,
          "cache_creation_input_tokens": 1024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1024
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

_source line 40 · 2026-05-30T07:26:15.670Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CmwCDQzL5HjDPn2rJqmBgx`</summary>

```json
{
  "query": "RAGPart document partitioning poisoning defense RAG 2025 arXiv 2512 experimental results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81ca5d8c-1845-48b3-9848-ddb962e5d530",
  "isSidechain": false,
  "requestId": "req_011CbYMc2maNKzqiJwmK3Jd9",
  "type": "assistant",
  "uuid": "f3e6fa13-260d-4a95-ba56-7a94343efccf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P79pEZ8cCdowH34z1jBJpM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 795,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 26591,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 795,
          "output_tokens": 182,
          "cache_read_input_tokens": 26591,
          "cache_creation_input_tokens": 1024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1024
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

_source line 41 · 2026-05-30T07:26:16.764Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QHXw7nS7ie8p8Nv8UY6f5L`</summary>

```json
{
  "query": "NLI agreement score DeBERTa conformal prediction nonconformity RAG abstention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3e6fa13-260d-4a95-ba56-7a94343efccf",
  "isSidechain": false,
  "requestId": "req_011CbYMc2maNKzqiJwmK3Jd9",
  "type": "assistant",
  "uuid": "776558ad-0395-402c-9b58-3fa4d5a1fe9c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P79pEZ8cCdowH34z1jBJpM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 795,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 26591,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 795,
          "output_tokens": 182,
          "cache_read_input_tokens": 26591,
          "cache_creation_input_tokens": 1024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1024
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

_source line 42 · 2026-05-30T07:26:23.990Z_

<details><summary>↩ Tool result · `toolu_01CmwCDQzL5HjDPn2rJqmBgx`</summary>

```text
Web search results for query: "RAGPart document partitioning poisoning defense RAG 2025 arXiv 2512 experimental results"

Links: [{"title":"[2512.24268] RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2512.24268"},{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304v1"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"RAG Poisoning: Threats and Defenses","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"},{"title":"Advances LLM Security, RAGPart And RAGMask Mitigates Corpus Poisoning In Generation Pipelines","url":"https://quantumzeitgeist.com/security-advances-llm-ragpart-ragmask-mitigates/"},{"title":"(PDF) RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://www.researchgate.net/publication/399277254_RAGPart_RAGMask_Retrieval-Stage_Defenses_Against_Corpus_Poisoning_in_Retrieval-Augmented_Generation"},{"title":"Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention","url":"https://www.arxiv.org/pdf/2602.04711"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"Safeguarding RAG Pipelines with GMTP: A Gradient-based Masked Token Probability Method for Poisoned Document Detection","url":"https://arxiv.org/pdf/2507.18202"}]

Based on the search results, I found the paper you're looking for. Here's information about RAGPart and its experimental results:

## Overview

RAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points. The defenses operate directly on the retriever, making them computationally lightweight and requiring no modification to the generation model, and RAGPart specifically leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points.

## How RAGPart Works

Each document is partitioned into fragments, which are individually embedded. Embeddings from multiple fragment combinations (e.g., subsets of size k) are then averaged to produce candidate document representations. These are used to retrieve multiple top-p document sets, which are aggregated to form the final top-p set for retrieval.

## Experimental Results

Across two benchmarks, four poisoning strategies, and four state-of-the-art retrievers, their defenses consistently reduce attack success rates while preserving utility under benign conditions. The paper further introduces an interpretable attack to stress-test the defenses, and the findings highlight the potential and limitations of retrieval-stage defenses, providing practical insights for robust RAG deployments.

The paper (arXiv 2512.24268) was published on December 30, 2025, and proposes RAGPart alongside RAGMask as complementary retrieval-stage defenses against corpus poisoning in RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3e6fa13-260d-4a95-ba56-7a94343efccf",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "db3d9253-4f15-4db0-9b1b-43fbb6f7b65a",
  "toolUseResult": {
    "query": "RAGPart document partitioning poisoning defense RAG 2025 arXiv 2512 experimental results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WapBoprtfqzThNV1vs9vbF",
        "content": [
          {
            "title": "[2512.24268] RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2512.24268"
          },
          {
            "title": "Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions",
            "url": "https://arxiv.org/html/2604.08304v1"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "RAG Poisoning: Threats and Defenses",
            "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"
          },
          {
            "title": "Advances LLM Security, RAGPart And RAGMask Mitigates Corpus Poisoning In Generation Pipelines",
            "url": "https://quantumzeitgeist.com/security-advances-llm-ragpart-ragmask-mitigates/"
          },
          {
            "title": "(PDF) RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://www.researchgate.net/publication/399277254_RAGPart_RAGMask_Retrieval-Stage_Defenses_Against_Corpus_Poisoning_in_Retrieval-Augmented_Generation"
          },
          {
            "title": "Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention",
            "url": "https://www.arxiv.org/pdf/2602.04711"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          },
          {
            "title": "Safeguarding RAG Pipelines with GMTP: A Gradient-based Masked Token Probability Method for Poisoned Document Detection",
            "url": "https://arxiv.org/pdf/2507.18202"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's information about RAGPart and its experimental results:\n\n## Overview\n\nRAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points. The defenses operate directly on the retriever, making them computationally lightweight and requiring no modification to the generation model, and RAGPart specifically leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points.\n\n## How RAGPart Works\n\nEach document is partitioned into fragments, which are individually embedded. Embeddings from multiple fragment combinations (e.g., subsets of size k) are then averaged to produce candidate document representations. These are used to retrieve multiple top-p document sets, which are aggregated to form the final top-p set for retrieval.\n\n## Experimental Results\n\nAcross two benchmarks, four poisoning strategies, and four state-of-the-art retrievers, their defenses consistently reduce attack success rates while preserving utility under benign conditions. The paper further introduces an interpretable attack to stress-test the defenses, and the findings highlight the potential and limitations of retrieval-stage defenses, providing practical insights for robust RAG deployments.\n\nThe paper (arXiv 2512.24268) was published on December 30, 2025, and proposes RAGPart alongside RAGMask as complementary retrieval-stage defenses against corpus poisoning in RAG systems."
    ],
    "durationSeconds": 8.314001348000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f3e6fa13-260d-4a95-ba56-7a94343efccf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-30T07:26:24.611Z_

<details><summary>↩ Tool result · `toolu_01QHXw7nS7ie8p8Nv8UY6f5L`</summary>

```text
Web search results for query: "NLI agreement score DeBERTa conformal prediction nonconformity RAG abstention 2025 2026"

Links: [{"title":"The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems","url":"https://arxiv.org/html/2512.15068"},{"title":"The Semantic Illusion: Certified Limits of Embedding- ...","url":"https://arxiv.org/pdf/2512.15068"},{"title":"Coarse-Grained Hallucination Detection via NLI Fine-Tuning","url":"https://aclanthology.org/2025.sdp-1.34.pdf"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/pdf/2511.17908"},{"title":"Conformal Prediction for Deep Classifier via Label Ranking","url":"https://arxiv.org/pdf/2310.06430"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"},{"title":"Symmetric Aggregation of Conformity Scores for Efficient Uncertainty Sets","url":"https://www.arxiv.org/pdf/2512.06945"},{"title":"[2505.21147] Semi-Supervised Conformal Prediction With Unlabeled Nonconformity Score","url":"https://arxiv.org/abs/2505.21147"}]

The search found several highly relevant recent papers combining these concepts. Here are the key findings:

## Main Results

DeBERTa-v3-large achieves an AUC of 0.81 on HaluEval, but conformal prediction results show 100% FPR (False Positive Rate), indicating a critical gap between traditional metrics and safety-critical applications.

The issue stems from a bimodal distribution where many hallucinations achieve near-perfect entailment scores (NLI scores ≈ 0.999), and since virtually all faithful responses also fall below this certainty threshold, the FPR collapses to 100%.

## Conformal Prediction in RAG

On synthetic hallucinations, embedding methods achieve 95% coverage with 0% FPR, but on real hallucinations from RLHF-aligned models, the same methods fail catastrophically, yielding 100% FPR at target coverage.

## Abstention Approaches

Conformal prediction techniques can develop abstention procedures with theoretical guarantees on hallucination rates, calibrating the detection/abstention policy to satisfy a pre-specified statistical upper bound on hallucination risk while minimizing abstention rate.

## Nonconformity Scores

Split conformal prediction requires a scoring function assigning nonconformity scores (where lower scores indicate more relevance) along with calibration and test sets from the same distribution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "776558ad-0395-402c-9b58-3fa4d5a1fe9c",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "fdb70832-7ca6-49b9-9425-5635d278b278",
  "toolUseResult": {
    "query": "NLI agreement score DeBERTa conformal prediction nonconformity RAG abstention 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HcB18oehPQfPLt9KdHakWL",
        "content": [
          {
            "title": "The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems",
            "url": "https://arxiv.org/html/2512.15068"
          },
          {
            "title": "The Semantic Illusion: Certified Limits of Embedding- ...",
            "url": "https://arxiv.org/pdf/2512.15068"
          },
          {
            "title": "Coarse-Grained Hallucination Detection via NLI Fine-Tuning",
            "url": "https://aclanthology.org/2025.sdp-1.34.pdf"
          },
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://arxiv.org/pdf/2511.17908"
          },
          {
            "title": "Conformal Prediction for Deep Classifier via Label Ranking",
            "url": "https://arxiv.org/pdf/2310.06430"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/pdf/2405.01563"
          },
          {
            "title": "Symmetric Aggregation of Conformity Scores for Efficient Uncertainty Sets",
            "url": "https://www.arxiv.org/pdf/2512.06945"
          },
          {
            "title": "[2505.21147] Semi-Supervised Conformal Prediction With Unlabeled Nonconformity Score",
            "url": "https://arxiv.org/abs/2505.21147"
          }
        ]
      },
      "The search found several highly relevant recent papers combining these concepts. Here are the key findings:\n\n## Main Results\n\nDeBERTa-v3-large achieves an AUC of 0.81 on HaluEval, but conformal prediction results show 100% FPR (False Positive Rate), indicating a critical gap between traditional metrics and safety-critical applications.\n\nThe issue stems from a bimodal distribution where many hallucinations achieve near-perfect entailment scores (NLI scores ≈ 0.999), and since virtually all faithful responses also fall below this certainty threshold, the FPR collapses to 100%.\n\n## Conformal Prediction in RAG\n\nOn synthetic hallucinations, embedding methods achieve 95% coverage with 0% FPR, but on real hallucinations from RLHF-aligned models, the same methods fail catastrophically, yielding 100% FPR at target coverage.\n\n## Abstention Approaches\n\nConformal prediction techniques can develop abstention procedures with theoretical guarantees on hallucination rates, calibrating the detection/abstention policy to satisfy a pre-specified statistical upper bound on hallucination risk while minimizing abstention rate.\n\n## Nonconformity Scores\n\nSplit conformal prediction requires a scoring function assigning nonconformity scores (where lower scores indicate more relevance) along with calibration and test sets from the same distribution."
    ],
    "durationSeconds": 7.843257528999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "776558ad-0395-402c-9b58-3fa4d5a1fe9c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-30T07:26:27.959Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more search specifically about computational costs and feasibility of multi-group partition approaches with LLMs, as the proposal requires K separate LLM calls per query.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdb70832-7ca6-49b9-9425-5635d278b278",
  "isSidechain": false,
  "requestId": "req_011CbYMczvizdmjLShxbyzDn",
  "type": "assistant",
  "uuid": "a1a7694c-16bc-49db-bdbc-d71fc0dcf452",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MyjrGouCZ8LgTFCDXDich",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 27615,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 27615,
          "cache_creation_input_tokens": 2664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2664
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

_source line 45 · 2026-05-30T07:26:28.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WtSVbzqrNkEnGMpWjxXXbS`</summary>

```json
{
  "query": "RobustRAG isolate aggregate partition computational cost multiple LLM calls per query efficiency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1a7694c-16bc-49db-bdbc-d71fc0dcf452",
  "isSidechain": false,
  "requestId": "req_011CbYMczvizdmjLShxbyzDn",
  "type": "assistant",
  "uuid": "0191cc27-fb9f-4c63-bfef-5172ee9900ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MyjrGouCZ8LgTFCDXDich",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 27615,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 27615,
          "cache_creation_input_tokens": 2664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2664
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

_source line 46 · 2026-05-30T07:26:29.254Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pmu4hJe56tBU8aHnDUiZpV`</summary>

```json
{
  "query": "Conformal-RAG SIGIR 2025 group-conditional coverage experimental design datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0191cc27-fb9f-4c63-bfef-5172ee9900ca",
  "isSidechain": false,
  "requestId": "req_011CbYMczvizdmjLShxbyzDn",
  "type": "assistant",
  "uuid": "2390ae87-eeb9-4997-bf0c-36619a0ab823",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MyjrGouCZ8LgTFCDXDich",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 27615,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 27615,
          "cache_creation_input_tokens": 2664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2664
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "2390ae87-eeb9-4997-bf0c-36619a0ab823",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Tool result

_source line 49 · 2026-05-30T07:26:35.136Z_

<details><summary>↩ Tool result · `toolu_01WtSVbzqrNkEnGMpWjxXXbS`</summary>

```text
Web search results for query: "RobustRAG isolate aggregate partition computational cost multiple LLM calls per query efficiency"

Links: [{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"CompactRAG: Reducing LLM Calls and Token Overhead in Multi-Hop Question Answering","url":"https://arxiv.org/pdf/2602.05728"},{"title":"Usage of RAG with LLM Models & Cost Savings | by Subhayan Chatterjee | Medium","url":"https://medium.com/@subhayan91/usage-of-rag-with-llm-models-cost-savings-e48496675f2f"},{"title":"ROGRAG: A Robustly Optimized GraphRAG Framework","url":"https://arxiv.org/html/2503.06474v2"},{"title":"[2602.05728] CompactRAG: Reducing LLM Calls and Token Overhead in Multi-Hop Question Answering","url":"https://arxiv.org/abs/2602.05728"}]

Based on the search results, I found relevant information about RobustRAG:

RobustRAG is a defense framework with certifiable robustness against retrieval corruption attacks that uses an isolate-then-aggregate strategy: it isolates passages into disjoint groups, generates LLM responses based on the concatenated passages from each isolated group, and then securely aggregates these responses for a robust output.

Regarding computational cost and multiple LLM calls, RobustRAG leverages the isolate-then-aggregate strategy by isolating passages into disjoint groups and computing LLM responses based on the concatenated passages from each group. This approach inherently requires multiple LLM calls—one for each isolated passage group—which increases the computational cost compared to a single-pass RAG system.

The isolation operation ensures that the malicious passages do not affect LLM responses for other benign passage groups and thus lays the foundation for robustness.

The search results indicate that RobustRAG trades computational efficiency for robustness guarantees against retrieval corruption attacks. While the framework requires multiple LLM calls due to its partitioning strategy, this is a necessary cost for achieving certifiable robustness against adversarial retrieval corruption.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0191cc27-fb9f-4c63-bfef-5172ee9900ca",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "c36350eb-9cdf-43f0-92ce-c900d8b8930f",
  "toolUseResult": {
    "query": "RobustRAG isolate aggregate partition computational cost multiple LLM calls per query efficiency",
    "results": [
      {
        "tool_use_id": "srvtoolu_018tnvs1XwotD6SmarUP4oH3",
        "content": [
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "CompactRAG: Reducing LLM Calls and Token Overhead in Multi-Hop Question Answering",
            "url": "https://arxiv.org/pdf/2602.05728"
          },
          {
            "title": "Usage of RAG with LLM Models & Cost Savings | by Subhayan Chatterjee | Medium",
            "url": "https://medium.com/@subhayan91/usage-of-rag-with-llm-models-cost-savings-e48496675f2f"
          },
          {
            "title": "ROGRAG: A Robustly Optimized GraphRAG Framework",
            "url": "https://arxiv.org/html/2503.06474v2"
          },
          {
            "title": "[2602.05728] CompactRAG: Reducing LLM Calls and Token Overhead in Multi-Hop Question Answering",
            "url": "https://arxiv.org/abs/2602.05728"
          }
        ]
      },
      "Based on the search results, I found relevant information about RobustRAG:\n\nRobustRAG is a defense framework with certifiable robustness against retrieval corruption attacks that uses an isolate-then-aggregate strategy: it isolates passages into disjoint groups, generates LLM responses based on the concatenated passages from each isolated group, and then securely aggregates these responses for a robust output.\n\nRegarding computational cost and multiple LLM calls, RobustRAG leverages the isolate-then-aggregate strategy by isolating passages into disjoint groups and computing LLM responses based on the concatenated passages from each group. This approach inherently requires multiple LLM calls—one for each isolated passage group—which increases the computational cost compared to a single-pass RAG system.\n\nThe isolation operation ensures that the malicious passages do not affect LLM responses for other benign passage groups and thus lays the foundation for robustness.\n\nThe search results indicate that RobustRAG trades computational efficiency for robustness guarantees against retrieval corruption attacks. While the framework requires multiple LLM calls due to its partitioning strategy, this is a necessary cost for achieving certifiable robustness against adversarial retrieval corruption."
    ],
    "durationSeconds": 6.678304860999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0191cc27-fb9f-4c63-bfef-5172ee9900ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-30T07:26:38.494Z_

<details><summary>↩ Tool result · `toolu_01Pmu4hJe56tBU8aHnDUiZpV`</summary>

```text
Web search results for query: "Conformal-RAG SIGIR 2025 group-conditional coverage experimental design datasets"

Links: [{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978"},{"title":"[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978"},{"title":"[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978v1"},{"title":"GitHub - n4feng/ResponseQualityAssessment: Code Base for Paper \"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality\" accepted by SIGIR 2025","url":"https://github.com/n4feng/ResponseQualityAssessment"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730244"},{"title":"A Few Observations on Sample-Conditional Coverage in Conformal   Prediction","url":"https://arxiv.org/pdf/2503.00220"},{"title":"Conformal Prediction Sets with Improved Conditional Coverage using Trust   Scores","url":"https://arxiv.org/pdf/2501.10139"},{"title":"Principled Context Engineering for RAG:","url":"https://www.arxiv.org/pdf/2511.17908"}]

Based on the search results, I found information about the Conformal-RAG paper accepted by SIGIR 2025:

## Conformal-RAG: Overview

Conformal-RAG is a novel framework inspired by recent applications of conformal prediction (CP) on large language models (LLMs) that leverages CP and internal information from the RAG mechanism to offer statistical guarantees on response quality.

## Group-Conditional Coverage

The approach ensures group-conditional coverage spanning multiple sub-domains without requiring manual labelling of conformal sets, making it suitable for complex RAG applications.

## Experimental Design and Datasets

According to the GitHub repository for the project, the repository supports conditional conformal in the medlf_qa dataset, with the configuration in `/conf/dataset_config.yaml` setting medlf_qa.is_grouped = true while other datasets are set to false. Additionally, the codebase includes data loading capabilities for datasets such as AkariASAI/PopQA and KILT benchmark.

## Performance Results

Experiments demonstrate that by leveraging information from the RAG system, Conformal-RAG retains up to 60% more high-quality sub-claims from the response compared to direct applications of CP to LLMs, while maintaining the same reliability guarantee.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2390ae87-eeb9-4997-bf0c-36619a0ab823",
  "isSidechain": false,
  "promptId": "6c6d6480-56ee-41d4-8bb5-8a0b7234fd0a",
  "type": "user",
  "uuid": "1eec1ba5-ecdb-437b-af79-aed3a0635690",
  "toolUseResult": {
    "query": "Conformal-RAG SIGIR 2025 group-conditional coverage experimental design datasets",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VBhcPqaFyn5wdeSmgS3ZLP",
        "content": [
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978"
          },
          {
            "title": "[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978"
          },
          {
            "title": "[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978v1"
          },
          {
            "title": "GitHub - n4feng/ResponseQualityAssessment: Code Base for Paper \"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality\" accepted by SIGIR 2025",
            "url": "https://github.com/n4feng/ResponseQualityAssessment"
          },
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval",
            "url": "https://dl.acm.org/doi/10.1145/3726302.3730244"
          },
          {
            "title": "A Few Observations on Sample-Conditional Coverage in Conformal   Prediction",
            "url": "https://arxiv.org/pdf/2503.00220"
          },
          {
            "title": "Conformal Prediction Sets with Improved Conditional Coverage using Trust   Scores",
            "url": "https://arxiv.org/pdf/2501.10139"
          },
          {
            "title": "Principled Context Engineering for RAG:",
            "url": "https://www.arxiv.org/pdf/2511.17908"
          }
        ]
      },
      "Based on the search results, I found information about the Conformal-RAG paper accepted by SIGIR 2025:\n\n## Conformal-RAG: Overview\n\nConformal-RAG is a novel framework inspired by recent applications of conformal prediction (CP) on large language models (LLMs) that leverages CP and internal information from the RAG mechanism to offer statistical guarantees on response quality.\n\n## Group-Conditional Coverage\n\nThe approach ensures group-conditional coverage spanning multiple sub-domains without requiring manual labelling of conformal sets, making it suitable for complex RAG applications.\n\n## Experimental Design and Datasets\n\nAccording to the GitHub repository for the project, the repository supports conditional conformal in the medlf_qa dataset, with the configuration in `/conf/dataset_config.yaml` setting medlf_qa.is_grouped = true while other datasets are set to false. Additionally, the codebase includes data loading capabilities for datasets such as AkariASAI/PopQA and KILT benchmark.\n\n## Performance Results\n\nExperiments demonstrate that by leveraging information from the RAG system, Conformal-RAG retains up to 60% more high-quality sub-claims from the response compared to direct applications of CP to LLMs, while maintaining the same reliability guarantee."
    ],
    "durationSeconds": 9.236704796999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2390ae87-eeb9-4997-bf0c-36619a0ab823",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-30T07:27:40.166Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have sufficient information from my research to provide a thorough analysis. Let me synthesize what I've found and assess the proposal's experimental design.

Let me analyze the proposal's experimental design critically:

**Strengths I've identified:**
1. Good coverage of attack methods (PoisonedRAG, CorruptRAG, DoS from RSB)
2. Strong baseline coverage with 7 methods spanning conformal, certified defense, and partition-based approaches
3. Good compute-normalized baseline (TRAQ + K× self-consistency)
4. Comprehensive ablation matrix


5. Testing across multiple model scales to ensure the findings generalize
6. Using standard datasets in the field (NQ, HotpotQA, MS-MARCO)

**Potential issues I want to flag:**

1. **Missing baselines**: The proposal doesn't empirically test combining RobustRAG with standard conformal prediction, which is a natural baseline that reviewers will inevitably ask about. Additionally, Semantic Chameleon attacks are mentioned in the related work but aren't included as an attack method to evaluate against, and some simpler baseline approaches seem to be missing entirely.

2. **TV bound tightness**: While the proposal derives a theoretical bound on the violation rate, there's no experimental plan to check how conservative this bound actually is in practice or how much the quantile inflation impacts real-world performance.

3. **NLI model reliability**: The agreement scoring depends on DeBERTa-v3 for NLI predictions, but there's no evaluation of whether this component itself remains robust when facing adversarially poisoned passages.

4. **Calibration set adequacy**: The proposal mentions needing n_cal ≥ 500, but given the TV-inflated quantiles being used, I need to think through whether this is sufficient for reliably estimating the effective quantile level.

5. **Clean accuracy tradeoff**: The proposal treats clean accuracy as secondary, but this is critical—a method that achieves high certified coverage by abstaining on everything is worthless, so the coverage-accuracy tradeoff deserves explicit analysis.

6. **Baseline comparison gap**: The proposal claims the naive "RobustRAG + CP" approach fails, but this needs empirical validation rather than just theoretical argument.

7. **Dataset diversity**: The current datasets are all short-answer QA tasks, so adding at least one domain-specific benchmark like medical or legal QA would strengthen the evaluation for a venue like AAAI.

8. **Experimental scale concerns**: With 200-300 queries per dataset, the proposal is on the lower end for AAAI standards, and the full experimental matrix across K, n, scoring functions, calibration variants, partition strategies, attacks, datasets, and models could become unwieldy without careful design.

9. **Adaptive adversary gap**: The evaluation only considers off-the-shelf attacks, but reviewers will expect assessment against adaptive adversaries who understand the partition mechanism and could craft attacks to either maximize disagreement without triggering abstention or minimize it to bypass the defense entirely.

10. **Monotonicity assumption**: The CRC method relies on a monotonicity assumption that needs examination.

Now I'm sorting through what's truly critical versus what would be nice to have. The missing empirical comparison with RobustRAG + CP is essential since the proposal argues against it theoretically, so that needs validation in practice. Adaptive attack evaluation is standard in adversarial ML and shouldn't be skipped. And I need to verify that the NLI model itself holds up under adversarial inputs.

The TV bound tightness, domain-specific datasets, calibration sensitivity, and the clean accuracy versus abstention tradeoff are all important but secondary. Additional ablations and larger evaluation scale would be nice but aren't deal-breakers.

Looking back at what's already proposed, I see they do include sensitivity experiments for when the poisoning budget exceeds the assumed bound, clean accuracy metrics, and tradeoff curves across coverage, abstention, and budget parameters. So some of my concerns are already partially addressed—I need to be more precise about what's genuinely missing versus what's already there.

But there's a real feasibility question here: the compute requirements are substantial. With K LLM calls per query, 200-300 queries, multiple datasets, attack settings, and model scales, especially for the 72B model, this could get prohibitively expensive.

Let me work through the math more carefully. For the primary experiments on the 7B model with a reasonable ablation scope, it's probably manageable, but I should check whether the proposal intends to run the full ablation matrix across all three model scales or just the primary one.

Looking at the proposal structure, it seems the full ablation would be on the 7B model with validation experiments on the larger scales, which is a sensible approach.

Now stepping back at the overall experimental design—it's actually quite comprehensive, though there are some notable gaps: no empirical comparison with a naive pipeline baseline, no adaptive attack evaluation, no domain-specific dataset despite the motivation, incomplete TV bound tightness validation, and missing NLI robustness testing under adversarial outputs. These are all addressable though.

One thing I should reconsider is whether the compute-normalized baseline is set up correctly. The proposal includes TRAQ with K× self-consistency voting to account for the extra LLM calls PRCA makes, but I'm wondering if that's actually the right comparison point.

A more direct compute-normalized baseline would be RobustRAG paired with conformal prediction using some ad-hoc TV inflation—the proposal argues this fails theoretically, but showing it empirically against a compute-matched setup would strengthen the case. The ablation does cover the important comparison though: CRC with TV inflation versus without it versus vanilla split conformal. And Conformal-RAG from SIGIR 2025 is a reasonable baseline since it uses conditional conformal factuality for group-conditional coverage, which is relevant to this work.

On the model choice, using Qwen across 7B/32B/72B scales is sensible for a 2026 paper, and the proposal does mention Llama-3-8B as an alternative for the 7B tier, so there's some diversity there—though testing at least one additional model family would help rule out model-specific artifacts.

Now I'm compiling my full assessment. The main gaps are the missing RobustRAG + CP baseline and adaptive attack evaluation, both critical for the work's contribution. Domain-specific datasets, NLI robustness validation, and empirical TV bound tightness are moderate concerns. Monotonicity verification and calibration sensitivity are minor issues that could go in the appendix or be addressed with minimal effort. None of these are showstoppers—everything is fixable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eec1ba5-ecdb-437b-af79-aed3a0635690",
  "isSidechain": false,
  "requestId": "req_011CbYMe2H7N3tEzWDFL2wY6",
  "type": "assistant",
  "uuid": "601f6506-b1c8-404e-abcd-dfc4a6f860db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVzKYEpqXjZYtNhKS8rnmK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1542,
      "cache_read_input_tokens": 30279,
      "output_tokens": 7873,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1542,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7873,
          "cache_read_input_tokens": 30279,
          "cache_creation_input_tokens": 1542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1542
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

_source line 52 · 2026-05-30T07:29:39.965Z_

Now I have sufficient research to conduct a thorough assessment. Let me compile my findings and analyze the proposal's experimental design.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **TRAQ (NAACL 2024)**: 使用 NQ 等标准 QA 数据集，基于 semantic clustering 的 nonconformity score，评估 coverage rate 和 prediction set size，与 vanilla split conformal 做 ablation。未考虑任何对抗场景。
- **RobustRAG (SaTML 2026)**: 使用 RealtimeQA-MC、RealtimeQA、NQ、Bio 四个数据集，每个数据集仅 100 queries；采用 Mistral-7B、Llama2-7B、GPT-3.5 三个 LLM；使用 keyword-based 和 decoding-based 两种 aggregation 方案；评估 certified robust accuracy，但 **未提供 abstention 机制或 coverage certificate**。计算开销方面，RobustRAG 同样需要 K 次独立 LLM 调用。
- **PoisonedRAG (USENIX Security 2025)**: 在 NQ、HotpotQA、MS-MARCO 上评估，使用 PaLM 2 等 LLM，k ∈ {1,3,5} poisoned documents，黑盒设置下 ASR 达 91-99%；评估了 4 种防御机制的有效性。
- **RPS (ICLR 2025 Spotlight)**: 使用 smoothed score functions + 多子集校准来实现 calibration-set poisoning 下的鲁棒 CP；关键假设是 poisoning 发生在 calibration 阶段而非 test-time retrieval。
- **ReliabilityRAG (NeurIPS 2025)**: 基于 NLI contradiction detection 构建 graph → MIS，评估在 adversarial attacks 下的鲁棒性和 benign accuracy retention；NLI 模型为核心组件。
- **Conformal-RAG (SIGIR 2025)**: 在 PopQA、medlf_qa 等数据集上评估 group-conditional coverage，保留了 60% 更多高质量 sub-claims vs. direct CP。
- **RSB Benchmark (May 2025)**: 13 种攻击方法、7 种防御机制、5+10 个数据集；关键发现：现有防御在 expanded datasets 上效果显著下降，**当前防御技术无法提供鲁棒保护**。
- **Chen et al. (arXiv:2603.16817, Mar 2026)**: 证明 TRAQ/C-RAG 等 conformal factuality 方法在 distribution shift 和 distractors 下产生 vacuous outputs，引入 usefulness 作为关键评估指标。
- **Semantic Chameleon (arXiv Mar 2026)**: 引入 gradient-guided corpus-dependent attacks，比标准 poisoning 更 sophisticated。

- **调研总结**: 该领域当前的实验设计标准要求：(1) 多种攻击方法（targeted + DoS + adaptive）的全面评估；(2) 与 certified defense 和 conformal methods 两类基线的对比；(3) clean accuracy 与 adversarial robustness 的 tradeoff 分析；(4) **adversarial ML 社区普遍期望 adaptive attack 评估**（攻击者知道防御机制细节后专门设计的攻击）；(5) compute-normalized 公平比较。

---

【缺陷 1】
- 类别: baseline 不足
- 问题: Proposal 在理论部分 (Section "Why not simply RobustRAG + standard CP?") 明确论证了 "RobustRAG + TRAQ/C-RAG" 这一 naive pipeline 方案理论上不可行（exchangeability 打破、distributional shift 无法量化），但实验设计的 7 个 baseline 中 **没有包含这个 naive pipeline 作为实验对照**。这是一个关键缺陷：reviewer 看到这个理论论证后，第一反应必然是 "show me the empirical evidence"。仅靠理论论证不够——需要实验证据展示该 pipeline 在攻击下 coverage guarantee 实际崩塌到什么程度，与 PRCA 的 empirical coverage 做直接对比。
- 严重度: 可补救
- 补救方案: 在 baseline 中增加第 8 个方法——"RobustRAG + TRAQ" 和/或 "RobustRAG + C-RAG"：先用 RobustRAG 的 isolate-then-aggregate 获得 robust answer，然后对该 answer 应用 TRAQ/C-RAG 的 conformal abstention。在相同攻击设置下评估其 empirical coverage 是否维持目标 1−α，以及 coverage 崩塌程度。这直接验证 proposal 的核心理论动机，且实验成本很低（仅需将两个现有方法串联）。
- 调研依据: RobustRAG 已有开源代码（arXiv:2405.15556），TRAQ 已有开源实现；两者串联的实验成本可忽略。该 baseline 直接对应 proposal Section "Why not simply RobustRAG + standard CP?" 的理论 claim，需要实验支撑。

【缺陷 2】
- 类别: 实验设计不足
- 问题: Proposal 仅评估现有的 off-the-shelf 攻击方法（PoisonedRAG、CorruptRAG、RSB 中的 DoS 攻击），但 **完全没有 adaptive attack 评估**。在 adversarial ML 领域（包括 SaTML、NeurIPS adversarial robustness track），审稿人普遍期望在攻击者 **了解防御机制全部细节** 的情况下评估鲁棒性。PRCA 的防御机制有明确的可利用结构：(1) 攻击者可以设计 poisoned passages 使其在不同 partition groups 中产生 **表面一致但语义错误** 的答案，从而降低 disagreement score s、绕过 abstention；(2) 攻击者可以设计 passages 使 NLI model 误判 entailment（NLI adversarial examples 已有大量文献）。不评估 adaptive attacks 会被 reviewer 认为是实验设计的重大遗漏。
- 严重度: 可补救
- 补救方案: 增加至少一种 adaptive attack 设置：(a) **Agreement-aware adaptive attack**: 攻击者在 K-partition 结构已知的前提下，优化 poisoned passage 内容使其最大化跨 group 的 NLI entailment score（即最小化 s），同时确保答案为目标错误答案。可以借鉴 Semantic Chameleon 的 gradient-guided 方法实现；(b) **NLI-targeted adversarial attack**: 在 poisoned passage 中嵌入对 DeBERTa NLI 模型的 adversarial perturbation，使 NLI 模型对矛盾答案对仍输出高 entailment score。报告 PRCA 在这些 adaptive attacks 下的 empirical coverage 和 certified coverage gap。
- 调研依据: Semantic Chameleon (arXiv Mar 2026) 已经提出了 gradient-guided corpus-dependent attacks。RSB Benchmark 发现 "current defense techniques fail to provide robust protection"，暗示 adaptive attacks 是关键评估维度。RobustRAG (SaTML 2026) 的审稿中也涉及对 adaptive attack 的讨论。

【缺陷 3】
- 类别: 实验设计不足
- 问题: Proposal 的动机部分明确列举了 "medical QA, legal retrieval, financial compliance" 作为核心应用场景，但实验数据集仅包含通用 open-domain QA 数据集（NQ, HotpotQA, MS-MARCO）。**没有任何 domain-specific 数据集来验证 proposal 声称的高风险场景适用性。** 审稿人很可能指出：如果这个方法是为 safety-critical 场景设计的，至少应该在一个 domain-specific 数据集上验证，否则 motivation 和 evaluation 脱节。
- 严重度: 可补救
- 补救方案: 增加至少一个 domain-specific 数据集。推荐选择：(a) **BioASQ** 或 **PubMedQA**（medical QA，公开可用，已有 RAG 评测先例）；或 (b) **CaseHOLD**（legal QA）。不需要做所有 ablation，只需在该数据集上验证 PRCA 的 core performance（certified coverage, empirical coverage, abstention rate）vs. 主要 baselines，作为 generalizability 证据。Conformal-RAG (SIGIR 2025) 也在 medlf_qa 上做了 domain-specific 评测，证明审稿人对此有期望。
- 调研依据: Conformal-RAG (SIGIR 2025) 在 medlf_qa（medical QA）上进行了 group-conditional coverage 评估。RSB Benchmark 也扩展到了多种数据集变体来测试 generalizability。

【缺陷 4】
- 类别: 评估方案缺陷
- 问题: Agreement score 的核心组件是 DeBERTa-v3-large NLI 模型的 entailment probability。Proposal 的 ablation 矩阵中包含了 "Score function: NLI entailment vs. ROUGE-L vs. exact match" 的对照，但 **没有评估 NLI 模型本身在 adversarial outputs 下的可靠性**。如果 poisoned passages 导致 LLM 生成的答案在语义上经过精心设计（例如包含 NLI adversarial patterns），NLI entailment score 可能给出不可靠的判断。这与缺陷 2 相关但独立——即使不考虑 adaptive attack，NLI 模型在 out-of-distribution 或 adversarially-crafted LLM output 上的 calibration 质量也值得验证。
- 严重度: 可补救
- 补救方案: 增加一个 diagnostic experiment：(a) 在攻击场景下，分别收集 clean groups 和 corrupted groups 的 LLM 输出，检查 NLI 模型的 entailment predictions 在这些输出对上的准确性和 calibration（reliability diagram）；(b) 如果 NLI 模型在攻击输出上不可靠，考虑使用 ensemble NLI（多个 NLI 模型投票）或 calibrated NLI（temperature scaling）作为 robustness 增强手段，并在 ablation 中评估。
- 调研依据: "The Semantic Illusion" (arXiv:2512.15068) 发现 DeBERTa-v3-large 在 hallucination detection 中 AUC 为 0.81，但 conformal prediction 场景下 FPR 可达 100%——表明 NLI 模型的 score 在 conformal 框架中的可靠性不能想当然。ReliabilityRAG (NeurIPS 2025) 也使用 NLI-based contradiction detection，但未报告 NLI 模型在 adversarial 场景下的鲁棒性。

【缺陷 5】
- 类别: 评估方案缺陷
- 问题: Proposal 提出了 TV bound: TV ≤ m/K，并通过 CRC 的 quantile inflation 吸收该 bound。但实验设计中 **没有明确计划验证该 TV bound 的 tightness**。如果理论 bound 过度保守（即实际 TV distance 远小于 m/K），则 quantile inflation 会过度，导致不必要的高 abstention rate——method 虽然 correct 但 overly conservative、practical utility 有限。Proposal 提到了 "certified vs. empirical robustness gap" 作为 tradeoff curve，这部分 addresses 了问题，但应该更明确地设计实验来量化 bound tightness。
- 严重度: 可补救
- 补救方案: 增加一个 tightness analysis 实验：(a) 在每个攻击设置下，empirically 估计 clean CDF 和 poisoned CDF 之间的实际 TV distance（通过 bootstrap 或 kernel density estimation），与理论 bound m/K 做对比；(b) 报告 "theoretical TV bound / empirical TV distance" 的 ratio 作为 tightness metric；(c) 探索是否可以用 data-dependent tighter bounds（例如基于实际观测到的 score perturbation）替代 worst-case m/K bound，作为 future work 讨论或初步实验。这对 method 的 practical adoption 至关重要。
- 调研依据: Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105) 强调了 ambiguity set 的 tightness 对 prediction set size 的直接影响——过度保守的 bound 导致 vacuous prediction sets，这正是 Chen et al. (2026) 批评现有方法的核心问题。

【缺陷 6】
- 类别: 可行性问题
- 问题: 完整的 ablation matrix 规模估算：K ∈ {3,5,7,10} × n ∈ {10,20,30} × 3 score functions × 3 calibration variants × 2 partition strategies × 3+ attack methods × 3 datasets × 3 model scales = 潜在上万种配置。即使每配置仅 200 queries，总 LLM generation 次数可能达到 **数百万次**（每 query 需 K 次 LLM 调用）。Proposal 未明确说明哪些 ablation 在哪个 model scale 上做，全矩阵在 72B 模型上显然不可行。
- 严重度: 可补救
- 补救方案: 明确实验层次结构：(a) **Full ablation matrix** 仅在 primary model (7B) 上执行；(b) 32B 和 72B 仅做 **core configuration**（最优 K、最优 score function，2-3 种攻击，3 个数据集），验证 conclusions 跨 scale 一致性；(c) 估算并报告总 compute budget（GPU-hours 或 token 消耗），说明可行性。RobustRAG 在每个数据集仅用 100 queries，proposal 的 200-300 queries 已经更充分，但需控制 ablation 维度与 model scale 的交叉。
- 调研依据: RobustRAG (SaTML 2026) 使用 100 queries/dataset 且仅在 7B/13B 级别做了 full evaluation，GPT-3.5 仅做部分验证。这是该领域实验规模的合理参照。

【缺陷 7】
- 类别: ablation 不完整
- 问题: Ablation 矩阵中缺少一个关键的 **lower-bound ablation baseline**: K=1（即不做 partition，所有 passages 在一个 group 中生成一个 answer）。K=1 相当于没有 partition-induced agreement mechanism 的退化情况，是验证 partition 本身贡献的最直接 ablation。此外，缺少 **"PRCA without TV inflation but with partition"**（即做 partition + agreement score，但用 vanilla conformal 而非 CRC + TV inflation）作为 ablation——这个对照可以精确隔离 TV inflation 的贡献 vs. agreement score 本身的贡献。后者在 ablation 列表 "CRC + TV inflation vs. CRC without inflation vs. vanilla split conformal" 中已部分覆盖，但应明确标注其 ablation 目的。
- 严重度: 可补救
- 补救方案: (a) 增加 K=1 到 ablation 的 K 取值范围：K ∈ {1, 3, 5, 7, 10}；(b) 明确标注每个 calibration variant ablation 的隔离目的："CRC + TV inflation"（完整方法） vs. "CRC without inflation"（隔离 TV inflation 贡献） vs. "vanilla split conformal"（隔离 CRC 框架贡献）。
- 调研依据: 基于领域实验规范判断——退化到单 group (K=1) 的 ablation 是证明 partition mechanism 必要性的标准做法，类似于 RobustRAG 将 isolation 作为 ablation 维度。

---

**总结**: Proposal 的实验设计整体框架 **相当完善**——7 个 baselines 覆盖了三类相关工作、ablation 矩阵维度丰富、metrics 体系完整、compute-normalized comparison 有意识地控制了推理成本差异。以上 7 个缺陷均为 **可补救** 项，无方向性致命缺陷。其中缺陷 1（RobustRAG+CP naive pipeline baseline）和缺陷 2（adaptive attack 评估）是最可能被 reviewer 直接指出的问题，优先级最高；缺陷 3-5 为中等优先级的 completeness 改进；缺陷 6-7 为 execution clarity 和 ablation 补全。全部补齐后，实验设计层面应能达到 AAAI 2026 主会的 soundness 要求。

Sources:
- [TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction](https://aclanthology.org/2024.naacl-long.210/)
- [Certifiably Robust RAG against Retrieval Corruption (RobustRAG)](https://arxiv.org/abs/2405.15556)
- [PoisonedRAG: Knowledge Corruption Attacks to RAG](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag)
- [C-RAG: Certified Generation Risks for RAG](https://proceedings.mlr.press/v235/kang24a.html)
- [RPS: Provably Reliable Conformal Prediction Sets under Poisoning](https://openreview.net/forum?id=ofuLWn8DFZ)
- [ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search](https://arxiv.org/abs/2509.23519)
- [Is Conformal Factuality for RAG-based LLMs Robust? (Chen et al. 2026)](https://arxiv.org/abs/2603.16817)
- [Conformal-RAG: Conditional Conformal Factuality (SIGIR 2025)](https://arxiv.org/abs/2506.20978)
- [RSB: Benchmarking Poisoning Attacks against RAG](https://arxiv.org/abs/2505.18543)
- [Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/abs/2502.14105)
- [The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection](https://arxiv.org/abs/2512.15068)
- [Semantic Chameleon: Corpus-Dependent Poisoning Attacks](https://arxiv.org/abs/2603.18034)
- [RAGPart & RAGMask](https://arxiv.org/abs/2512.24268)
- [Conformal Risk Control (CRC)](https://arxiv.org/abs/2208.02814)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "601f6506-b1c8-404e-abcd-dfc4a6f860db",
  "isSidechain": false,
  "requestId": "req_011CbYMe2H7N3tEzWDFL2wY6",
  "type": "assistant",
  "uuid": "4c94ae74-4559-4d90-bb47-ac9c1b4e1022",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVzKYEpqXjZYtNhKS8rnmK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1542,
      "cache_read_input_tokens": 30279,
      "output_tokens": 7873,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1542,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7873,
          "cache_read_input_tokens": 30279,
          "cache_creation_input_tokens": 1542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1542
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

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "4c94ae74-4559-4d90-bb47-ac9c1b4e1022",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems deployed in adversarial environments (medical QA, legal retrieval, financial compliance) ne…",
  "leafUuid": "4c94ae74-4559-4d90-bb47-ac9c1b4e1022",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "037763d4-80b2-4f88-83b7-758527263a94"
}
```

---
