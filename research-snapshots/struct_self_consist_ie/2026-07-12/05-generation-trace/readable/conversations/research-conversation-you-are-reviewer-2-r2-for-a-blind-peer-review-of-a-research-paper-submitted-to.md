# Research conversation: You are Reviewer 2 (R2) for a blind peer review of a research paper submitted to EMNLP 2026 Main Conference (via ACL Rol

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6acb7d036d9ca50e.jsonl`
- **Structured JSON:** [`61e8e1526706056d6448.json`](../../sessions/61/61e8e1526706056d6448.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-16T11:57:50.282Z_

You are Reviewer 2 (R2) for a blind peer review of a research paper submitted to EMNLP 2026 Main Conference (via ACL Rolling Review). Your focus areas are **novelty** and **related work**.

## Scoring Rubric (ARR/EMNLP)
- **Soundness** (1-5, half-point increments): 5=Excellent (most thorough), 4=Strong (sufficient for all claims), 3=Acceptable (sufficient for main claims), 2=Poor (main claims not supported), 1=Major Issues
- **Excitement** (1-5): 5=Highly Exciting, 4=Exciting, 3=Interesting, 2=Potentially Interesting, 1=Not Exciting
- **Overall Assessment** (1-5): 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit, 1=Do not resubmit
- **Confidence** (1-5): 5=Positive, 4=Quite sure, 3=Pretty sure, 2=Willing to defend, 1=Not my area
- **Reproducibility** (1-5): 5=Easily, 4=Mostly, 3=With difficulty, 2=Hard pressed, 1=Cannot

## Paper Title
"Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction"

## Full Paper Content (9 pages)

### Abstract
Test-time scaling via multi-sample generation improves LLM reasoning tasks, but its effectiveness for structured information extraction (IE) remains unclear. We present a dual contribution: (1) a quality estimation (QE) framework showing that five confidence signals across four families reliably predict structured IE output quality (AUROC up to 0.82, Spearman ρ up to 0.44), enabling practical selective prediction; and (2) a diagnostic analysis revealing why these same signals universally fail at best-of-N selection. We identify a multi-causal failure mechanism: instance degeneracy (21–58% of instances produce identical outputs across N samples), logprob score compression (within-instance range 0.041 nats), and insufficient signal discriminability even when degeneracy is reduced. A trained verifier (logistic regression on 5 signals) closes 36% of the oracle gap for NER (+4.8pp over greedy), confirming that signals carry exploitable information but unsupervised aggregation is the bottleneck. Experiments span 3 model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B), 2 IE tasks (NER, RE), and 3 datasets (SciERC, CoNLL-2003, WNUT-17), establishing that the correlation–selection gap is model-agnostic and task-general.

### Section 1: Introduction
Test-time scaling through multi-sample generation and selection has emerged as a powerful paradigm for improving LLM performance on reasoning tasks (Wang et al. 2023; Brown et al. 2024; Snell et al. 2024). Self-consistency—sampling multiple chain-of-thought paths and selecting via majority vote—yields substantial gains for discrete-answer problems. However, structured IE outputs—entity sets, relation triples, event structures—resist naive majority voting due to their combinatorial output space.

Contribution A: QE Framework. Five signals across four families for structured IE quality estimation. AUROC up to 0.82, ρ up to 0.44.

Contribution B: Diagnostic Analysis. Multi-causal failure: instance degeneracy (21-58%), logprob compression (0.041 nats), insufficient discriminability even with reduced degeneracy. Trained verifier closes 36% NER oracle gap.

### Section 2: Related Work
**Self-Consistency and Test-Time Scaling.** Wang et al. (2023) on majority vote for reasoning. Extensions: confidence-weighted voting (CISC 2025), reward-free selection via KL-divergence (Self-Certainty 2026), reliability-aware adaptive consistency (ReASC 2026), atomic sub-claim consistency (Atomic SC 2024). All operate on discrete answers; none address structured outputs with set-valued semantics.

**Consistency for Structured IE.** Nédellec and Xia (2026) study consistency–accuracy correlation for hard-prompted LLMs on biomedical NER/RE, finding positive correlation but using surface-level string matching. The authors claim their structural Jaccard directly addresses this limitation. Nédellec & Xia do not study best-of-N selection or multi-signal comparison.

**Uncertainty Quantification for LLMs.** Semantic entropy (Kuhn et al. 2023), SelfCheckGPT (Manakul et al. 2023), conformal prediction (Fisch et al. 2021; Angelopoulos et al. 2021). Surveys (UQ Survey 2025; Calibration Survey 2025). Token-level NER uncertainty via MC-dropout (Shelmanov et al. 2021) and ensembles (Lakshminarayanan et al. 2017). Authors complement by evaluating sample-level structural consistency signals.

**MBR Decoding and Verifiers.** MBR decoding (Eikema & Aziz 2022), CoCoA (2025) for QA/summarization. Trained verifiers (Cobbe et al. 2021; Lightman et al. 2023). Authors claim for structured IE, utility is aligned (within-instance ρ=0.524) but headroom eliminated by degeneracy.

**Selective Prediction.** Geifman & El-Yaniv (2017), Kuleshov & Liang (2015). Authors provide confidence scores for selective prediction in structured IE.

### Section 3: Method
Five signals (SJ, FK, LP, EM, VC) across four families (structural similarity, probabilistic, voting-based, exact match). QE metrics: ρ, τ, AUROC, ECE. Selection: F1 vs greedy + bootstrap + Cohen's d. Oracle: max F1.

### Section 4: Experimental Setup
Models: Qwen3-8B (LoRA rank=32), Qwen3-4B, LLaMA-3.1-8B. Datasets: SciERC, CoNLL-2003, WNUT-17. N=8, T=1.0.

### Section 5: Results
- QE works: ρ up to 0.44, AUROC up to 0.82 (Table 1-3)
- Selection fails: no signal beats greedy significantly (Δ=+0.6pp, p=0.39) (Section 5.3)
- Multi-causal diagnosis: degeneracy, LP compression, discriminability gap
- Trained verifier (LR on 5 signals, 5-fold CV): NER +4.8pp (36.4% gap closure), RE +3.8pp (21.0%) (Tables 4-6)
- Numerical audit: 0 critical issues (Table 7)

### Section 6: Discussion
QE–Selection Decoupling (population vs within-instance). Capability–Degeneracy Tradeoff. When Would Consistency Help (ICL, closed-source APIs, etc.). Path Forward: trained verifiers.

### Section 7: Limitations
English only, 8B max, oracle F1 labels, qualitative tradeoff.

### Section 8: Conclusion
QE framework + diagnostic analysis. Multi-causal failure across 3 models, 2 tasks, 3 datasets. Trained verifier confirms information exists; bottleneck is unsupervised aggregation.

### References (22 total)
Wang et al. 2023 (self-consistency), Brown et al. 2024, Snell et al. 2024, Kuhn et al. 2023 (semantic entropy), Manakul et al. 2023 (SelfCheckGPT), Eikema & Aziz 2022 (MBR), Cobbe et al. 2021 (math verifiers), Lightman et al. 2023 (process reward), Geifman & El-Yaniv 2017 (selective prediction), Fisch et al. 2021 (conformal), Angelopoulos et al. 2021, Shelmanov et al. 2021 (MC-dropout NER), Lakshminarayanan et al. 2017 (deep ensembles), Kuleshov & Liang 2015, Nédellec & Xia 2026 (consistency for IE), CISC 2025, Self-Certainty 2026, ReASC 2026, Atomic SC 2024, UQ Survey 2025, Calibration Survey 2025, CoCoA 2025, Luan et al. 2018 (SciERC), Tjong Kim Sang & De Meulder 2003 (CoNLL).

## Your Review Task
As R2, focus on **novelty and related work**. Evaluate:

1. **Novelty assessment**: How novel is the QE–selection decoupling insight? Is the multi-causal failure analysis genuinely new? How does this compare to Nédellec & Xia (2026) who already studied consistency–accuracy for structured IE? Is the trained verifier experiment novel or a straightforward application?
2. **Related work coverage**: Are there important missing references? Key areas to check: (a) MBR decoding for structured prediction beyond NMT, (b) verification/reranking for IE specifically, (c) test-time compute scaling literature (e.g., "scaling laws for test-time compute"), (d) constrained decoding for structured outputs, (e) calibration of structured predictors.
3. **Positioning**: Is the paper well-positioned relative to existing work? Are the claimed differences from prior work accurate? Is the negative result (selection fails) a sufficient contribution for a top venue?
4. **Significance and impact**: Who benefits from this work? How much does the QE framework advance the field? Is the "path forward" (trained verifiers) sufficiently developed?
5. **Framing**: Is the title appropriate? Does the abstract accurately reflect the contributions? Is the "dual contribution" framing convincing or does it feel like two thin contributions bundled?

Additionally consider missing related work in these areas:
- Structured prediction under uncertainty (e.g., CRF-based NER uncertainty)
- Entity linking / disambiguation with confidence scores
- Multi-output evaluation metrics for IE (entity-level vs instance-level)
- Recent test-time scaling papers beyond the ones cited (e.g., DeepSeek-R1, QwQ, etc.)
- Reward model / ORM / PRM literature for non-math domains

Provide your review in this format:

### R2 Review: Novelty & Related Work

**Summary** (2-3 sentences)

**Strengths** (bulleted)

**Weaknesses** (bulleted)

**Missing Related Work**

**Questions for Authors**

**Soundness**: X/5
**Excitement**: X/5
**Overall Assessment**: X/5
**Confidence**: X/5
**Reproducibility**: X/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4e4f55b3-8499-4a23-9491-7cbbbb839d17",
  "agentId": "a6acb7d036d9ca50e",
  "type": "user",
  "uuid": "0c068c78-b715-4bf8-b913-375134c38e56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T11:57:50.286Z_

```json
{
  "parentUuid": "0c068c78-b715-4bf8-b913-375134c38e56",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
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
  "uuid": "3c7738f5-dd96-4d85-ba58-3024be9b7f14",
  "timestamp": "2026-05-16T11:57:50.286Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T11:57:54.175Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DKmNu7WRiRVJ6JesHdVKQQ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c7738f5-dd96-4d85-ba58-3024be9b7f14",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6CzfdadAJ1knFYdKtLW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab497c74-85e2-46f6-b755-1646b065d1d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AaMksu1oRdxp2821RHM2K7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8558,
      "cache_read_input_tokens": 8251,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8558
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 8558,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8558,
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

_source line 4 · 2026-05-16T11:57:54.179Z_

<details><summary>↩ Tool result · `toolu_01DKmNu7WRiRVJ6JesHdVKQQ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab497c74-85e2-46f6-b755-1646b065d1d9",
  "isSidechain": true,
  "promptId": "4e4f55b3-8499-4a23-9491-7cbbbb839d17",
  "agentId": "a6acb7d036d9ca50e",
  "type": "user",
  "uuid": "6793036f-eb77-4d67-b7ad-8b62c8703983",
  "sourceToolAssistantUUID": "ab497c74-85e2-46f6-b755-1646b065d1d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T11:57:57.271Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01V7m4Dk9XKacRDEn3pRGKeX`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6793036f-eb77-4d67-b7ad-8b62c8703983",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6CzxTrfct9obnA8dik4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2a88445-8316-4e99-a9f5-2b8690ae5b9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mo6WPLuqFCyFiQ8dJotAPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 6 · 2026-05-16T11:57:57.283Z_

<details><summary>↩ Tool result · `toolu_01V7m4Dk9XKacRDEn3pRGKeX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-14T21:00:00.000Z'\\n  total_papers: 55\\ncategories: []\\npapers:\\n  wang2023selfconsistency:\\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\\n    authors:\\n    - Xuezhi Wang\\n    - Jason Wei\\n    - Dale Schuurmans\\n    - Quoc Le\\n    - Ed Chi\\n    - Sharan Narang\\n    - Aakanksha Chowdhery\\n    - Denny Zhou\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2203.11171\\n    doi: ''\\n    bibtex_key: wang2023selfconsistency\\n    category: self_consistency_reasoning\\n    role: foundation\\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\\n      from closed-form answers to structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  taubenfeld2025cisc:\\n    title: Confidence Improves Self-Consistency in LLMs\\n    authors:\\n    - Amir Taubenfeld\\n    - Tom Sheffer\\n    - Eran Ofek\\n    - Amir Feder\\n    - Ariel Goldstein\\n    - Zorik Gekhman\\n    - Gal Yona\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2502.06233\\n    doi: 10.18653/v1/2025.findings-acl.1030\\n    bibtex_key: taubenfeld2025cisc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\\n      same \\\"strong predictor, weak selector\\\" gap but for structured outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kang2025selfcertainty:\\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\n    authors:\\n    - Zhewei Kang\\n    - Xuandong Zhao\\n    - Dawn Song\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2502.18581\\n    doi: ''\\n    bibtex_key: kang2025selfcertainty\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\\n      quality estimation that we compare against for structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kim2026reasc:\\n    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\n    authors:\\n    - Junseok Kim\\n    - Nakyeong Yang\\n    - Kyungmin Min\\n    - Kyomin Jung\\n    year: 2026\\n    venue: ACL 2026\\n    url: https://arxiv.org/abs/2601.02970\\n    doi: ''\\n    bibtex_key: kim2026reasc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  thirukovalluru2024atomic:\\n    title: Atomic Self-Consistency for Better Long Form Generations\\n    authors:\\n    - Raghuveer Thirukovalluru\\n    - Yukun Huang\\n    - Bhuwan Dhingra\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.706/\\n    doi: 10.18653/v1/2024.emnlp-main.706\\n    bibtex_key: thirukovalluru2024atomic\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\\n      to our structured output aggregation approach.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  chen2024usc:\\n    title: Universal Self-Consistency for Large Language Model Generation\\n    authors:\\n    - Xinyun Chen\\n    - Renat Aksitov\\n    - Uri Alon\\n    - Jie Ren\\n    - Kefan Xiao\\n    - Pengcheng Yin\\n    - Sushant Prakash\\n    - Charles Sutton\\n    - Xuezhi Wang\\n    - Denny Zhou\\n    year: 2024\\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\\n    url: https://arxiv.org/abs/2311.17311\\n    doi: ''\\n    bibtex_key: chen2024usc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\\n      to free-form generation. Precursor to our structured consistency approach.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  manakul2023selfcheckgpt:\\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\\n    authors:\\n    - Potsawee Manakul\\n    - Adian Liusie\\n    - Mark Gales\\n    year: 2023\\n    venue: EMNLP 2023\\n    url: https://aclanthology.org/2023.emnlp-main.557/\\n    doi: 10.18653/v1/2023.emnlp-main.557\\n    bibtex_key: manakul2023selfcheckgpt\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\\n      diverge. Motivates our consistency-based quality signal for IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  wan2025rasc:\\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\\n    authors:\\n    - Guangya Wan\\n    - Yuqi Wu\\n    - Jie Chen\\n    - Sheng Li\\n    year: 2025\\n    venue: NAACL 2025\\n    url: https://aclanthology.org/2025.naacl-long.184/\\n    doi: 10.18653/v1/2025.naacl-long.184\\n    bibtex_key: wan2025rasc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  nedellec2026consistency:\\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\\n      from plant-health data'\\n    authors:\\n    - Claire Nédellec\\n    - Jingbo Xia\\n    year: 2026\\n    venue: Genomics & Informatics\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\\n    doi: 10.1186/s44342-025-00063-2\\n    bibtex_key: nedellec2026consistency\\n    category: consistency_structured_ie\\n    role: direct-competitor\\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  vashurin2025cocoa:\\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\\n    authors:\\n    - Roman Vashurin\\n    - Maiya Goloburda\\n    - Albina Ilina\\n    - Aleksandr Rubashevskii\\n    - Preslav Nakov\\n    - Artem Shelmanov\\n    - Maxim Panov\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2502.04964\\n    doi: ''\\n    bibtex_key: vashurin2025cocoa\\n    category: consistency_structured_ie\\n    role: background\\n    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\\n      Provides theoretical grounding for our dual-signal approach in structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  hobelsberger2025systematic:\\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\n    authors:\\n    - Christian Hobelsberger\\n    - Theresa Winner\\n    - Andreas Nawroth\\n    - Oliver Mitevski\\n    - Anna-Carolina Haensch\\n    year: 2025\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2510.20460\\n    doi: ''\\n    bibtex_key: hobelsberger2025systematic\\n    category: consistency_structured_ie\\n    role: background\\n    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  geng2024confidence:\\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\\n    authors:\\n    - Jiahui Geng\\n    - Fengyu Cai\\n    - Yuxia Wang\\n    - Heinz Koeppl\\n    - Preslav Nakov\\n    - Iryna Gurevych\\n    year: 2024\\n    venue: NAACL 2024\\n    url: https://arxiv.org/abs/2311.08298\\n    doi: 10.18653/v1/2024.naacl-long.366\\n    bibtex_key: geng2024confidence\\n    category: confidence_surveys\\n    role: survey\\n    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\\n      positioning our consistency-based confidence approach within the broader landscape.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  wen2025know:\\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\\n    authors:\\n    - Bingbing Wen\\n    - Jihan Yao\\n    - Shangbin Feng\\n    - Chenjun Xu\\n    - Yulia Tsvetkov\\n    - Bill Howe\\n    - Lucy Lu Wang\\n    year: 2025\\n    venue: TACL 2025\\n    url: https://arxiv.org/abs/2407.18418\\n    doi: 10.1162/tacl_a_00754\\n    bibtex_key: wen2025know\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  xia2025survey:\\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\\n    authors:\\n    - Zhiqiu Xia\\n    - Jinxuan Xu\\n    - Yuqian Zhang\\n    - Hang Liu\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://aclanthology.org/2025.findings-acl.1101/\\n    doi: ''\\n    bibtex_key: xia2025survey\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps\\n      with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  liu2025uqcalibration:\\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\\n    authors:\\n    - Xiaoou Liu\\n    - Tiejin Chen\\n    - Longchao Da\\n    - Chacha Chen\\n    - Zhen Lin\\n    - Hua Wei\\n    year: 2025\\n    venue: KDD 2025\\n    url: https://arxiv.org/abs/2503.15850\\n    doi: 10.1145/3711896.3736569\\n    bibtex_key: liu2025uqcalibration\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps\\n      with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by:\\n\\n... [截断: 省略 31664 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 43664, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2a88445-8316-4e99-a9f5-2b8690ae5b9d",
  "isSidechain": true,
  "promptId": "4e4f55b3-8499-4a23-9491-7cbbbb839d17",
  "agentId": "a6acb7d036d9ca50e",
  "type": "user",
  "uuid": "b929e523-0688-41e5-9b48-4335321c6ecf",
  "sourceToolAssistantUUID": "c2a88445-8316-4e99-a9f5-2b8690ae5b9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T11:57:58.226Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YXh7G41Rmo3MiaQQSASEFR`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "report.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b929e523-0688-41e5-9b48-4335321c6ecf",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6CzxTrfct9obnA8dik4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5faff198-e0bc-4027-a2f9-c5aa1c96c8a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mo6WPLuqFCyFiQ8dJotAPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 8 · 2026-05-16T11:57:58.235Z_

<details><summary>↩ Tool result · `toolu_01YXh7G41Rmo3MiaQQSASEFR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_022_seed789 | 3rd seed SciERC inference (seed=789) with ft_002_v2 (Qwen3-8B). N=8, T=1.0, joint NER+RE, logprobs collected. Complements seed42 (exp_012_rerun_1024) and seed123/456 for multi-seed analysis. | — | — | — |\\n| exp_020_fewnerd_smoke | 1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST. | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_023_lora_rank8** (success): —\\n- **exp_vc_lp_cascade_selection** (killed): VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\\n- **exp_tacred_re_benchmark** (killed): TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\\n\\n## 趋势\\n成功 62 / 负向 24 / 失败 4 / 共 112\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- ft_002: 已被终止 — unknown\\n- mvp_pilot_002: 训练失败 — unknown\\n- exp_007_ner_llama: 已被终止 — unknown\\n- exp001_seed123: 已被终止 — unknown\\n- exp001_seed456: 已被终止 — unknown\\n- exp008_re_n16: 已被终止 — unknown\\n- exp_002_merge_conll2003: 已被终止 — unknown\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\n- exp_008_re_n16_full: 已被终止 — unknown\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\n- exp_019_supervised_verifier: 已被终止 — unknown\\n- exp_lp_t07_scierc: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\n\", \"total_chars\": 2392, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5faff198-e0bc-4027-a2f9-c5aa1c96c8a7",
  "isSidechain": true,
  "promptId": "4e4f55b3-8499-4a23-9491-7cbbbb839d17",
  "agentId": "a6acb7d036d9ca50e",
  "type": "user",
  "uuid": "2f70806d-a1a1-4806-908e-4e29bc1c584a",
  "sourceToolAssistantUUID": "5faff198-e0bc-4027-a2f9-c5aa1c96c8a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T11:57:58.515Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Co3j8Tgwj67SvtvwNA61bM`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f70806d-a1a1-4806-908e-4e29bc1c584a",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6CzxTrfct9obnA8dik4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c06317de-0f7a-4115-8030-3d683c8e86f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mo6WPLuqFCyFiQ8dJotAPm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16809,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 16809,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1269,
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

_source line 10 · 2026-05-16T11:57:58.524Z_

<details><summary>↩ Tool result · `toolu_01Co3j8Tgwj67SvtvwNA61bM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c06317de-0f7a-4115-8030-3d683c8e86f9",
  "isSidechain": true,
  "promptId": "4e4f55b3-8499-4a23-9491-7cbbbb839d17",
  "agentId": "a6acb7d036d9ca50e",
  "type": "user",
  "uuid": "11745a8a-5bc3-40cb-ab1f-f69ccaa1e671",
  "sourceToolAssistantUUID": "c06317de-0f7a-4115-8030-3d683c8e86f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T11:58:02.418Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HAjgdaZxgAn3aoJbS1215y`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11745a8a-5bc3-40cb-ab1f-f69ccaa1e671",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6D1H2p1tbMfoLruDeah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbb7d1eb-c695-4517-8ceb-39d5baf4bf25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ueKjYdg3HAoXwHkDsKv48",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6222,
      "cache_read_input_tokens": 18078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6222,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 12 · 2026-05-16T11:58:02.430Z_

<details><summary>↩ Tool result · `toolu_01HAjgdaZxgAn3aoJbS1215y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-14T21:00:00.000Z'\\n  total_papers: 55\\ncategories: []\\npapers:\\n  wang2023selfconsistency:\\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\\n    authors:\\n    - Xuezhi Wang\\n    - Jason Wei\\n    - Dale Schuurmans\\n    - Quoc Le\\n    - Ed Chi\\n    - Sharan Narang\\n    - Aakanksha Chowdhery\\n    - Denny Zhou\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2203.11171\\n    doi: ''\\n    bibtex_key: wang2023selfconsistency\\n    category: self_consistency_reasoning\\n    role: foundation\\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\\n      from closed-form answers to structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  taubenfeld2025cisc:\\n    title: Confidence Improves Self-Consistency in LLMs\\n    authors:\\n    - Amir Taubenfeld\\n    - Tom Sheffer\\n    - Eran Ofek\\n    - Amir Feder\\n    - Ariel Goldstein\\n    - Zorik Gekhman\\n    - Gal Yona\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2502.06233\\n    doi: 10.18653/v1/2025.findings-acl.1030\\n    bibtex_key: taubenfeld2025cisc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\\n      same \\\"strong predictor, weak selector\\\" gap but for structured outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kang2025selfcertainty:\\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\n    authors:\\n    - Zhewei Kang\\n    - Xuandong Zhao\\n    - Dawn Song\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2502.18581\\n    doi: ''\\n    bibtex_key: kang2025selfcertainty\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\\n      quality estimation that we compare against for structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kim2026reasc:\\n    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\n    authors:\\n    - Junseok Kim\\n    - Nakyeong Yang\\n    - Kyungmin Min\\n    - Kyomin Jung\\n    year: 2026\\n    venue: ACL 2026\\n    url: https://arxiv.org/abs/2601.02970\\n    doi: ''\\n    bibtex_key: kim2026reasc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  thirukovalluru2024atomic:\\n    title: Atomic Self-Consistency for Better Long Form Generations\\n    authors:\\n    - Raghuveer Thirukovalluru\\n    - Yukun Huang\\n    - Bhuwan Dhingra\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.706/\\n    doi: 10.18653/v1/2024.emnlp-main.706\\n    bibtex_key: thirukovalluru2024atomic\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\\n      to our structured output aggregation approach.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  chen2024usc:\\n    title: Universal Self-Consistency for Large Language Model Generation\\n    authors:\\n    - Xinyun Chen\\n    - Renat Aksitov\\n    - Uri Alon\\n    - Jie Ren\\n    - Kefan Xiao\\n    - Pengcheng Yin\\n    - Sushant Prakash\\n    - Charles Sutton\\n    - Xuezhi Wang\\n    - Denny Zhou\\n    year: 2024\\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\\n    url: https://arxiv.org/abs/2311.17311\\n    doi: ''\\n    bibtex_key: chen2024usc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\\n      to free-form generation. Precursor to our structured consistency approach.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  manakul2023selfcheckgpt:\\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\\n    authors:\\n    - Potsawee Manakul\\n    - Adian Liusie\\n    - Mark Gales\\n    year: 2023\\n    venue: EMNLP 2023\\n    url: https://aclanthology.org/2023.emnlp-main.557/\\n    doi: 10.18653/v1/2023.emnlp-main.557\\n    bibtex_key: manakul2023selfcheckgpt\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\\n      diverge. Motivates our consistency-based quality signal for IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  wan2025rasc:\\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\\n    authors:\\n    - Guangya Wan\\n    - Yuqi Wu\\n    - Jie Chen\\n    - Sheng Li\\n    year: 2025\\n    venue: NAACL 2025\\n    url: https://aclanthology.org/2025.naacl-long.184/\\n    doi: 10.18653/v1/2025.naacl-long.184\\n    bibtex_key: wan2025rasc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  nedellec2026consistency:\\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\\n      from plant-health data'\\n    authors:\\n    - Claire Nédellec\\n    - Jingbo Xia\\n    year: 2026\\n    venue: Genomics & Informatics\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\\n    doi: 10.1186/s44342-025-00063-2\\n    bibtex_key: nedellec2026consistency\\n    category: consistency_structured_ie\\n    role: direct-competitor\\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  vashurin2025cocoa:\\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\\n    authors:\\n    - Roman Vashurin\\n    - Maiya Goloburda\\n    - Albina Ilina\\n    - Aleksandr Rubashevskii\\n    - Preslav Nakov\\n    - Artem Shelmanov\\n    - Maxim Panov\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2502.04964\\n    doi: ''\\n    bibtex_key: vashurin2025cocoa\\n    category: consistency_structured_ie\\n    role: background\\n    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\\n      Provides theoretical grounding for our dual-signal approach in structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  hobelsberger2025systematic:\\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\n    authors:\\n    - Christian Hobelsberger\\n    - Theresa Winner\\n    - Andreas Nawroth\\n    - Oliver Mitevski\\n    - Anna-Carolina Haensch\\n    year: 2025\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2510.20460\\n    doi: ''\\n    bibtex_key: hobelsberger2025systematic\\n    category: consistency_structured_ie\\n    role: background\\n    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  geng2024confidence:\\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\\n    authors:\\n    - Jiahui Geng\\n    - Fengyu Cai\\n    - Yuxia Wang\\n    - Heinz Koeppl\\n    - Preslav Nakov\\n    - Iryna Gurevych\\n    year: 2024\\n    venue: NAACL 2024\\n    url: https://arxiv.org/abs/2311.08298\\n    doi: 10.18653/v1/2024.naacl-long.366\\n    bibtex_key: geng2024confidence\\n    category: confidence_surveys\\n    role: survey\\n    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\\n      positioning our consistency-based confidence approach within the broader landscape.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  wen2025know:\\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\\n    authors:\\n    - Bingbing Wen\\n    - Jihan Yao\\n    - Shangbin Feng\\n    - Chenjun Xu\\n    - Yulia Tsvetkov\\n    - Bill Howe\\n    - Lucy Lu Wang\\n    year: 2025\\n    venue: TACL 2025\\n    url: https://arxiv.org/abs/2407.18418\\n    doi: 10.1162/tacl_a_00754\\n    bibtex_key: wen2025know\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  xia2025survey:\\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\\n    authors:\\n    - Zhiqiu Xia\\n    - Jinxuan Xu\\n    - Yuqian Zhang\\n    - Hang Liu\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://aclanthology.org/2025.findings-acl.1101/\\n    doi: ''\\n    bibtex_key: xia2025survey\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps\\n      with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  liu2025uqcalibration:\\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\\n    authors:\\n    - Xiaoou Liu\\n    - Tiejin Chen\\n    - Longchao Da\\n    - Chacha Chen\\n    - Zhen Lin\\n    - Hua Wei\\n    year: 2025\\n    venue: KDD 2025\\n    url: https://arxiv.org/abs/2503.15850\\n    doi: 10.1145/3711896.3736569\\n    bibtex_key: liu2025uqcalibration\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps\\n      with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  kuhn2023semantic:\\n    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'\\n    authors:\\n    - Lorenz Kuhn\\n    - Yarin Gal\\n    - Sebastian Farquhar\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2302.09664\\n    doi: ''\\n    bibtex_key: kuhn2023semantic\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs. Foundation\\n      for our structured consistency metric that operates at the semantic level of IE triples.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  kadavath2022language:\\n    title: Language Models (Mostly) Know What They Know\\n    authors:\\n    - Saurav Kadavath\\n    - Tom Conerly\\n    - Amanda Askell\\n    - Tom Henighan\\n    - Dawn Drain\\n    - Ethan Perez\\n    - Nicholas Schiefer\\n    - Zac Hatfield-Dodds\\n    - Nova DasSarma\\n    - Eli Tran-Johnson\\n    - Scott Johnston\\n    - Sheer El-Showk\\n    - Andy Jones\\n    - Nelson Elhage\\n    - Tristan Hume\\n    - Anna Chen\\n    - Yuntao Bai\\n    - Sam Bowman\\n    - Stanislav Fort\\n    - Deep Ganguli\\n    - Danny Hernandez\\n    - Josh Jacobson\\n    - Jackson Kernion\\n    - Shauna Kravec\\n    - Liane Lovitt\\n    - Kamal Ndousse\\n    - Catherine Olsson\\n    - Sam Ringer\\n    - Dario Amodei\\n    - Tom Brown\\n    - Jack Clark\\n    - Nicholas Joseph\\n    - Ben Mann\\n    - Sam McCandlish\\n    - Chris Olah\\n    - Jared Kaplan\\n    year: 2022\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2207.05221\\n    doi: ''\\n    bibtex_key: kadavath2022language\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge\\n      as a confidence signal, which we extend to structured IE output quality estimation.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  guo2017calibration:\\n    title: On Calibration of Modern Neural Networks\\n    authors:\\n    - Chuan Guo\\n    - Geoff Pleiss\\n    - Yu Sun\\n    - Kilian Q. Weinberger\\n    year: 2017\\n    venue: ICML 2017\\n    url: https://arxiv.org/abs/1706.04599\\n    doi: ''\\n    bibtex_key: guo2017calibration\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational\\n      reference for all calibration work including our LLM confidence calibration for IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  desai2020calibration:\\n    title: Calibration of Pre-trained Transformers\\n    authors:\\n    - Shrey Desai\\n    - Greg Durrett\\n    year: 2020\\n    venue: EMNLP 2020\\n    url: https://arxiv.org/abs/2003.07892\\n    doi: 10.18653/v1/2020.emnlp-main.21\\n    bibtex_key: desai2020calibration\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical\\n      calibration to the transformer era, motivating our LLM-specific calibration analysis.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  kossen2024semantic:\\n    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'\\n    authors:\\n    - Jannik Kossen\\n    - Jiatong Han\\n    - Muhammed Razzak\\n    - Lisa Schut\\n    - Shreshth Malik\\n    - Yarin Gal\\n    year: 2024\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2406.15927\\n    doi: ''\\n    bibtex_key: kossen2024semantic\\n    category: uncertainty_calibration\\n    role: background\\n    relevance: Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing\\n      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  xiong2024verbalized:\\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\n    authors:\\n    - Miao Xiong\\n    - Zhiyuan Hu\\n    - Xinyang Lu\\n    - Yifei Li\\n    - Jie Fu\\n    - Junxian He\\n    - Bryan Hooi\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2306.13063\\n    doi: ''\\n    bibtex_key: xiong2024verbalized\\n    category: uncertainty_calibration\\n    role: background\\n    relevance: Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly\\n      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  fisch2021conformal:\\n    title: Few-Shot Conformal Prediction with Auxiliary Tasks\\n    authors:\\n    - Adam Fisch\\n    - Tal Schuster\\n    - Tommi Jaakkola\\n    - Regina Barzilay\\n    year: 2021\\n    venue: ICML 2021\\n    url: https://arxiv.org/abs/2102.08898\\n    doi: 10.5555/3524938.3525234\\n    bibtex_key: fisch2021conformal\\n    category: conformal_prediction\\n    role: supplementary\\n    relevance: 'Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter\\n      prediction sets with formal coverage guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  angelopoulos2021conformal:\\n    title: Uncertainty Sets for Image Classifiers using Conformal Prediction\\n    authors:\\n    - Anastasios N. Angelopoulos\\n    - Stephen Bates\\n    - Jitendra Malik\\n    - Michael I. Jordan\\n    year: 2021\\n    venue: ICLR 2021\\n    url: https://arxiv.org/abs/2009.14193\\n    doi: ''\\n    bibtex_key: angelopoulos2021conformal\\n    category: conformal_prediction\\n    role: foundation\\n    relevance: Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for\\n      conformal prediction methodology we adapt to structured IE output sets.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  bates2021rcps:\\n    title: Distribution-Free, Risk-Controlling Prediction Sets\\n    authors:\\n    - Stephen Bates\\n    - Anastasios Angelopoulos\\n    - Lihua Lei\\n    - Jitendra Malik\\n    - Michael I. Jordan\\n    year: 2021\\n    venue: Journal of the ACM 2021\\n    url: https://arxiv.org/abs/2101.02703\\n    doi: 10.1145/3478535\\n    bibtex_key: bates2021rcps\\n    category: conformal_prediction\\n    role: supplementary\\n    relevance: 'Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample\\n      guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  xiao2019uncertainty:\\n    title: Quantifying Uncertainties in Natural Language Processing Tasks\\n    authors:\\n    - Yijun Xiao\\n    - William Yang Wang\\n    year: 2019\\n    venue: AAAI 2019\\n    url: https://arxiv.org/abs/1811.07253\\n    doi: 10.1609/aaai.v33i01.33017322\\n    bibtex_key: xiao2019uncertainty\\n    category: token_span_uncertainty_ner\\n    role: foundation\\n    relevance: Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model\\n      uncertainty improves both performance and reliability for token-level predictions.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  shelmanov2021active:\\n    title: Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\n    authors:\\n    - Artem Shelmanov\\n    - Dmitri Puzyrev\\n    - Lyubov Kupriyanova\\n    - Denis Belyakov\\n    - Daniil Larionov\\n    - Nikita Khromov\\n    - Olga Kozlova\\n    - Ekaterina Artemova\\n    - Dmitry V. Dylov\\n    - Alexander Panchenko\\n    year: 2021\\n    venue: EACL 2021\\n    url: https://arxiv.org/abs/2101.08133\\n    doi: 10.18653/v1/2021.eacl-main.145\\n    bibtex_key: shelmanov2021active\\n    category: token_span_uncertainty_ner\\n    role: foundation\\n    relevance: Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with\\n      pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  zhang2023ener:\\n    title: 'E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition'\\n    authors:\\n    - Zhen Zhang\\n    - Mengting Hu\\n    - Shiwan Zhao\\n    - Minlie Huang\\n    - Haotian Wang\\n    - Lemao Liu\\n    - Zhirui Zhang\\n    - Zhe Liu\\n    - Bingzhe Wu\\n    year: 2023\\n    venue: ACL Findings 2023\\n    url: https://arxiv.org/abs/2305.17854\\n    doi: 10.18653/v1/2023.findings-acl.103\\n    bibtex_key: zhang2023ener\\n    category: token_span_uncertainty_ner\\n    role: background\\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  lakshminarayanan2017ensembles:\\n    title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\n    authors:\\n    - Balaji Lakshminarayanan\\n    - Alexander Pritzel\\n    - Charles Blundell\\n    year: 2017\\n    venue: NeurIPS 2017\\n    url: https://arxiv.org/abs/1612.01474\\n    doi: ''\\n    bibtex_key: lakshminarayanan2017ensembles\\n    category: ensemble_mc_dropout\\n    role: foundation\\n    relevance: Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation.\\n      Foundational baseline for ensemble-based uncertainty quantification we compare against.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  gal2016dropout:\\n    title: 'Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning'\\n    authors:\\n    - Yarin Gal\\n    - Zoubin Ghahramani\\n    year: 2016\\n    venue: ICML 2016\\n    url: https://arxiv.org/abs/1506.02142\\n    doi: ''\\n    bibtex_key: gal2016dropout\\n    category: ensemble_mc_dropout\\n    role: foundation\\n    relevance: Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for\\n      uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  fomicheva2020unsupervised:\\n    title: Unsupervised Quality Estimation for Neural Machine Translation\\n    authors:\\n    - Marina Fomicheva\\n    - Shuo Sun\\n    - Lisa Yankovskaya\\n    - Frédéric Blain\\n    - Francisco Guzmán\\n    - Mark Fishel\\n    - Nikolaos Aletras\\n    - Vishrav Chaudhary\\n    - Lucia Specia\\n    year: 2020\\n    venue: TACL 2020\\n    url: https://arxiv.org/abs/2005.10608\\n    doi: 10.1162/tacl_a_00330\\n    bibtex_key: fomicheva2020unsupervised\\n    category: ensemble_mc_dropout\\n    role: background\\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  cobbe2021verifiers:\\n    title: Training Verifiers to Solve Math Word Problems\\n    authors:\\n    - Karl Cobbe\\n    - Vineet Kosaraju\\n    - Mohammad Bavarian\\n    - Mark Chen\\n    - Heewoo Jun\\n    - Lukasz Kaiser\\n    - Matthias Plappert\\n    - Jerry Tworek\\n    - Jacob Hilton\\n    - Reiichiro Nakano\\n    - Christopher Hesse\\n    - John Schulman\\n    year: 2021\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2110.14168\\n    doi: ''\\n    bibtex_key: cobbe2021verifiers\\n    category: verifier_reward_models\\n    role: foundation\\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\\n      Establishes the verify-then-select paradigm our method builds upon.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  lightman2024verify:\\n    title: Let's Verify Step by Step\\n    authors:\\n    - Hunter Lightman\\n    - Vineet Kosaraju\\n    - Yura Burda\\n    - Harri Edwards\\n    - Bowen Baker\\n    - Teddy Lee\\n    - Jan Leike\\n    - John Schulman\\n    - Ilya Sutskever\\n    - Karl Cobbe\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2305.20050\\n    doi: ''\\n    bibtex_key: lightman2024verify\\n    category: verifier_reward_models\\n    role: foundation\\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  wang2024mathshepherd:\\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\\n    authors:\\n    - Peiyi Wang\\n    - Lei Li\\n    - Zhihong Shao\\n    - Runxin Xu\\n    - Damai Dai\\n    - Yifei Li\\n    - Deli Chen\\n    - Yu Wu\\n    - Zhifang Sui\\n    year: 2024\\n    venue: ACL 2024\\n    url: https://arxiv.org/abs/2312.08935\\n    doi: ''\\n    bibtex_key: wang2024mathshepherd\\n    category: verifier_reward_models\\n    role: background\\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  snell2024scaling:\\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\n    authors:\\n    - Charlie Snell\\n    - Jaehoon Lee\\n    - Kelvin Xu\\n    - Aviral Kumar\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://arxiv.org/abs/2408.03314\\n    doi: ''\\n    bibtex_key: snell2024scaling\\n    category: tts_scaling\\n    role: foundation\\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  brown2024monkeys:\\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\\n    authors:\\n    - Bradley Brown\\n    - Jordan Juravsky\\n    - Ryan Ehrlich\\n    - Ronald Clark\\n    - Quoc V. Le\\n    - Christopher Ré\\n    - Azalia Mirhoseini\\n    year: 2024\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2407.21787\\n    doi: ''\\n    bibtex_key: brown2024monkeys\\n    category: tts_scaling\\n    role: foundation\\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  wu2024inference:\\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\\n    authors:\\n    - Yangzhen Wu\\n    - Zhiqing Sun\\n    - Shanda Li\\n    - Sean Welleck\\n    - Yiming Yang\\n    year: 2024\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2408.00724\\n    doi: ''\\n    bibtex_key: wu2024inference\\n    category: tts_scaling\\n    role: background\\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  kuleshov2015calibrated:\\n    title: Calibrated Structured Prediction\\n    authors:\\n    - Volodymyr Kuleshov\\n    - Percy Liang\\n    year: 2015\\n    venue: NeurIPS 2015\\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\\n    doi: ''\\n    bibtex_key: kuleshov2015calibrated\\n    category: structured_calibration_ie\\n    role: foundation\\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  culotta2004confidence:\\n    title: Confidence Estimation for Information Extraction\\n    authors:\\n    - Aron Culotta\\n    - Andrew McCallum\\n    year: 2004\\n    venue: HLT-NAACL 2004\\n    url: https://aclanthology.org/N04-4028/\\n    doi: ''\\n    bibtex_key: culotta2004confidence\\n    category: structured_calibration_ie\\n    role: foundation\\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\\n      levels. Establishes the problem setting our LLM-based approach addresses.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  jagannatha2020calibrating:\\n    title: Calibrating Structured Output Predictors for Natural Language Processing\\n    authors:\\n    - Abhyuday Jagannatha\\n    - Hong Yu\\n    year: 2020\\n    venue: ACL 2020\\n    url: https://aclanthology.org/2020.acl-main.188/\\n    doi: ''\\n    bibtex_key: jagannatha2020calibrating\\n    category: structured_calibration_ie\\n    role: background\\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  geifman2017selective:\\n    title: Selective Classification for Deep Neural Networks\\n    authors:\\n    - Yonatan Geifman\\n    - Ran El-Yaniv\\n    year: 2017\\n    venue: NeurIPS 2017\\n    url: https://arxiv.org/abs/1705.08500\\n    doi: ''\\n    bibtex_key: geifman2017selective\\n    category: selective_prediction\\n    role: foundation\\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  ren2023selfevaluation:\\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\\n    authors:\\n    - Jie Ren\\n    - Yao Zhao\\n    - Tu Vu\\n    - Peter J. Liu\\n    - Balaji Lakshminarayanan\\n    year: 2023\\n    venue: NeurIPS 2023 Workshop\\n    url: https://arxiv.org/abs/2312.09300\\n    doi: ''\\n    bibtex_key: ren2023selfevaluation\\n    category: selective_prediction\\n    role: background\\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  wadhwa2023revisiting:\\n    title: Revisiting Relation Extraction in the era of Large Language Models\\n    authors:\\n    - Somin Wadhwa\\n    - Silvio Amir\\n    - Byron Wallace\\n    year: 2023\\n    venue: ACL 2023\\n    url: https://aclanthology.org/2023.acl-long.868/\\n    doi: 10.18653/v1/2023.acl-long.868\\n    bibtex_key: wadhwa2023revisiting\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting\\n      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  sainz2024gollie:\\n    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'\\n    authors:\\n    - Oscar Sainz\\n    - Iker García-Ferrero\\n    - Rodrigo Agerri\\n    - Oier Lopez de Lacalle\\n    - German Rigau\\n    - Eneko Agirre\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2310.03668\\n    doi: ''\\n    bibtex_key: sainz2024gollie\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization\\n      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  luan2018scierc:\\n    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\n    authors:\\n    - Yi Luan\\n    - Luheng He\\n    - Mari Ostendorf\\n    - Hannaneh Hajishirzi\\n    year: 2018\\n    venue: EMNLP 2018\\n    url: https://aclanthology.org/D18-1360/\\n    doi: 10.18653/v1/D18-1360\\n    bibtex_key: luan2018scierc\\n    category: generative_ie\\n    role: dataset\\n    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation\\n      benchmark for our structured IE experiments.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  tjongkimsang2003conll:\\n    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'\\n    authors:\\n    - Erik F. Tjong Kim Sang\\n    - Fien De Meulder\\n    year: 2003\\n    venue: CoNLL 2003\\n    url: https://aclanthology.org/W03-0419/\\n    doi: ''\\n    bibtex_key: tjongkimsang2003conll\\n    category: generative_ie\\n    role: dataset\\n    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset\\n      for our NER consistency experiments.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  derczynski2017wnut:\\n    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\n    authors:\\n    - Leon Derczynski\\n    - Eric Nichols\\n    - Marieke van Erp\\n    - Nut Limsopatham\\n    year: 2017\\n    venue: W-NUT Workshop at EMNLP 2017\\n    url: https://aclanthology.org/W17-4418/\\n    doi: ''\\n    bibtex_key: derczynski2017wnut\\n    category: generative_ie\\n    role: dataset\\n    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness\\n      on harder, low-resource NER scenarios.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  willard2023guided:\\n    title: Efficient Guided Generation for Large Language Models\\n    authors:\\n    - Brandon T. Willard\\n    - Rémi Louf\\n    year: 2023\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2307.09702\\n    doi: ''\\n    bibtex_key: willard2023guided\\n    category: generative_ie\\n    role: background\\n    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and\\n      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  fleiss1971agreement:\\n    title: Measuring Nominal Scale Agreement Among Many Raters\\n    authors:\\n    - Joseph L. Fleiss\\n    year: 1971\\n    venue: Psychological Bulletin\\n    url: https://psycnet.apa.org/record/1972-05083-001\\n    doi: 10.1037/h0031619\\n    bibtex_key: fleiss1971agreement\\n    category: agreement_metrics\\n    role: foundation\\n    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation\\n      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  jaccard1901distribution:\\n    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\n    authors:\\n    - Paul Jaccard\\n    year: 1901\\n    venue: Bulletin de la Société Vaudoise des Sciences Naturelles\\n    url: https://www.researchgate.net/publication/225035806\\n    doi: ''\\n    bibtex_key: jaccard1901distribution\\n    category: agreement_metrics\\n    role: foundation\\n    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap\\n      between extracted entity/relation sets across multiple LLM samples.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  wang2025rankedvoting:\\n    title: Ranked Voting based Self-Consistency of Large Language Models\\n    authors:\\n    - Weiqin Wang\\n    - Yile Wang\\n    - Hui Huang\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2505.10772\\n    doi: ''\\n    bibtex_key: wang2025rankedvoting\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.\\n      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  oh2025latentsc:\\n    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'\\n    authors:\\n    - Jungsuk Oh\\n    - Jay-Yoon Lee\\n    year: 2025\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2508.18395\\n    doi: ''\\n    bibtex_key: oh2025latentsc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.\\n      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  zhou2024uniner:\\n    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'\\n    authors:\\n    - Wenxuan Zhou\\n    - Sheng Zhang\\n    - Yu Gu\\n    - Muhao Chen\\n    - Hoifung Poon\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2308.03279\\n    doi: ''\\n    bibtex_key: zhou2024uniner\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.\\n      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T21:05:00.000Z'\\n  josifoski2022genie:\\n    title: 'GenIE: Generative Information Extraction'\\n    authors:\\n    - Martin Josifoski\\n    - Nicola De Cao\\n    - Maxime Peyrard\\n    - Fabio Petroni\\n    - Robert West\\n    year: 2022\\n    venue: NAACL 2022\\n    url: https://arxiv.org/abs/2112.08340\\n    doi: 10.18653/v1/2022.naacl-main.342\\n    bibtex_key: josifoski2022genie\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'First end-to-end autoregressive formulation of closed IE with bi-level constrained decoding (high-level triplet\\n      structure + prefix-trie entity/relation constraints). Directly relevant as the foundational constrained decoding approach for structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T22:00:00.000Z'\\n  li2023codeie:\\n    title: 'CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors'\\n    authors:\\n    - Peng Li\\n    - Tianxiang Sun\\n    - Qiong Tang\\n    - Hang Yan\\n    - Yuanbin Wu\\n    - Xuanjing Huang\\n    - Xipeng Qiu\\n    year: 2023\\n    venue: ACL 2023\\n    url: https://arxiv.org/abs/2305.05711\\n    doi: 10.18653/v1/2023.acl-long.855\\n    bibtex_key: li2023codeie\\n    category: generative_ie\\n    role: background\\n    relevance: 'Recasts IE as code generation, leveraging Code-LLMs structural output capabilities for NER and RE. Demonstrates\\n      alternative structured generation approach complementary to constrained decoding.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T22:00:00.000Z'\\n  wang2023instructuie:\\n    title: 'InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction'\\n    authors:\\n    - Xiao Wang\\n    - Weikang Zhou\\n    - Can Zu\\n    - Han Xia\\n    - Tianze Chen\\n    - Yuansen Zhang\\n    - Rui Zheng\\n    - Junjie Ye\\n    - Qi Zhang\\n    - Tao Gui\\n    - Jihua Kang\\n    - Jingsheng Yang\\n    - Siyuan Li\\n    - Chunsai Du\\n    year: 2023\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2304.08085\\n    doi: ''\\n    bibtex_key: wang2023instructuie\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'Unified instruction-tuned IE framework covering NER, RE, EE across 32 datasets. Demonstrates multi-task generative\\n      IE with instruction tuning, directly relevant as representative LLM-based unified IE system.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T22:00:00.000Z'\\n\", \"total_chars\": 43664, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbb7d1eb-c695-4517-8ceb-39d5baf4bf25",
  "isSidechain": true,
  "promptId": "4e4f55b3-8499-4a23-9491-7cbbbb839d17",
  "agentId": "a6acb7d036d9ca50e",
  "type": "user",
  "uuid": "8f116c7f-b1fa-42e8-97ea-93f26f41f1d2",
  "sourceToolAssistantUUID": "bbb7d1eb-c695-4517-8ceb-39d5baf4bf25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T11:58:02.997Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01ATz3kTn5YFCUvtdP3Nu5SL`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f116c7f-b1fa-42e8-97ea-93f26f41f1d2",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6D1H2p1tbMfoLruDeah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4eef9f4c-9ce0-4548-849f-7c06aebd615e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ueKjYdg3HAoXwHkDsKv48",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6222,
      "cache_read_input_tokens": 18078,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6222
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 18078,
          "cache_creation_input_tokens": 6222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6222,
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

_source line 14 · 2026-05-16T11:58:03.030Z_

<details><summary>↩ Tool result · `toolu_01ATz3kTn5YFCUvtdP3Nu5SL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md\", \"content\": \"# Paper Framing — struct_self_consist_ie\\n\\n> Updated 2026-05-16 — D116: Dream full review feedback → Reframe to DUAL CONTRIBUTION (QE positive + selection diagnostic). D113: Table 2 macro F1 unified (Greedy=0.645, LP=0.647, all p>0.05). exp-023: LoRA rank=8 degeneracy 7.2% vs 21% but selection still fails → multi-causal (not just degeneracy). Trained verifier baseline (logistic regression on 5 signals) in progress. R² on n=3 must be caveated as qualitative only.\\n\\n## Target Venue\\n- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)\\n- Deadline: ARR May cycle, 2026-05-25\\n\\n## Core Claims (D116 updated — DUAL CONTRIBUTION: QE positive + selection diagnostic)\\n\\n### Claim 1 (PRIMARY — Dual Contribution: QE Framework + Selection Diagnostic)\\n**Positive contribution (A)**: Confidence signals reliably predict structured IE output quality at the population level (AUROC up to 0.82, ρ up to 0.45), enabling practical QE/selective prediction.\\n**Diagnostic contribution (B)**: These same signals universally fail to select better candidates from multiple samples. We diagnose the multi-causal failure: (1) instance degeneracy eliminates headroom for 4/5 signals; (2) LP compression eliminates it for the remaining one; (3) reducing degeneracy (LoRA rank=8: 7.2% vs 21%) increases oracle headroom but signals STILL cannot exploit it → low degeneracy is necessary but not sufficient → trained verifiers are the natural next step.\\n\\nThe framing is NOT \\\"selection fails\\\" (pure negative) but \\\"we show WHEN, WHY, and WHAT WOULD BE NEEDED for selection to work\\\" (diagnostic with constructive implications).\\n\\n**Three-layer argument + Capability Trap**:\\n- Layer A (design property, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification — the \\\"methodological premise\\\" — not an empirical finding.\\n- Layer B (empirical — instance degeneracy): 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom. Within-instance ρ=0.524 (SciERC) and 0.994 (CoNLL) — signals ARE correlated within instances, but degeneracy makes this irrelevant. Non-degenerate instances show MBR closing 23-41% of oracle gap. Selection recovers T=1.0 sampling degradation (LP 0.647 vs Random 0.610, +3.7pp) but only matches T=0 greedy (0.645 macro) at 8× inference cost — zero marginal gain.\\n- Layer C (empirical — LP compression): Logprob — the only per-sample signal — fails due to intrinsic score compression (median within-instance LP range = 0.041 nats). Entity-token LP shows 4× variance but WORSE selection (-2.0pp). Free-form ablation confirms compression is model/task intrinsic (std ratio 0.97).\\n- **Capability Trap** (unifying insight, D111): Model capability → output convergence → instance degeneracy → vanishing selection headroom. Evidence: CoNLL (91% F1) → 58% degeneracy, SciERC (66% F1) → 21%, WNUT (48% F1) → ~0%. Scale dimension: 8B → 21% degen vs 4B → 10.4% on SciERC. This is NOT an \\\"artifact\\\" — it is a **consequence of capability**, a structural inevitability. The better the model, the less test-time scaling can help via unsupervised selection.\\n\\n**Distinction from MBR literature**: Eikema et al.'s MBR failure = utility function misalignment. Our failure = utility IS aligned (within-instance ρ=0.524) but headroom eliminated by degeneracy — qualitatively novel mechanism.\\n\\n**Key evidence (score compression)**:\\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39\\n- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp\\n- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it\\n\\n**Key evidence (free-form ablation)** [DONE — exp_freeform_ablation, NEGATIVE]:\\n- LP distribution: constrained std=0.0206, free-form std=0.0199 (ratio 0.97, virtually unchanged)\\n- Tied fraction: 59.7% → 57.7% (-2.0pp, negligible)\\n- NER selection: +0.59pp → +0.18pp (both negligible vs greedy)\\n- RE selection: -0.68pp → +1.69pp (flipped positive — secondary finding)\\n- NER VC rho: 0.379 → 0.409 (slight QE improvement, selection still fails)\\n- Parse rate: 99.95% (fine-tuned model retains JSON format without grammar)\\n- **Conclusion**: Score compression is model/task intrinsic. The gap is universal.\\n\\n**Key evidence (scale ablation)** [DONE — 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}]:\\n- CoNLL NER: 4B greedy_f1=0.9234 (>8B 0.9123, +1.11pp), SJ_ρ=0.4217 (≈8B 0.4357, −1.4pp), FK_ρ=0.4181 (>8B 0.3998, +1.83pp)\\n- SciERC NER: 4B SJ_ρ=0.4221 (>8B 0.3825, +3.96pp), FK_ρ=0.3258 (>8B 0.2590, +6.68pp)\\n- SciERC RE: 4B SJ_ρ=0.2673 (>8B 0.2441, +2.32pp), FK_ρ=0.3593 (>8B 0.2782, +8.11pp); struct>surface ✗ at both scales\\n- **Conclusion**: Correlation strength maintained or improved at 4B across all 4 cells. The gap originates from within-instance signal misalignment, not model capacity. Task difficulty (SciERC RE zero-F1 rate) remains the primary driver, consistent across scales.\\n- CoNLL 4B headroom: 1.70pp (vs 8B 4.20pp) → MARGINAL for selection power, but QE correlations robust\\n- SciERC RE 4B: 47.6% zero-F1, RE LP_ρ_cond=0.1135 (p=0.074, n.s.) → confirms binary dominance at 4B\\n- **4B selection results** (correlation-selection gap at 4B):\\n  - CoNLL NER 4B (n=2756): SJ +0.07pp, FK +0.03pp, LP +0.09pp vs greedy 0.9213. All ≤0.1pp — MARGINAL (headroom 1.70pp)\\n  - SciERC NER 4B (n=529): SJ **-1.49pp**, FK -1.56pp, LP -2.23pp vs greedy 0.6622. Oracle 0.7925 (+13.02pp). **All signals WORSE than greedy despite 13pp oracle headroom — gap confirmed at 4B**\\n  - SciERC NER 4B gap demonstration: SJ-FK ρ gap = +0.096 (strong correlation advantage), SJ-FK selection F1 gap = +0.0007 (zero selection advantage) → correlation-selection gap quantified at 4B\\n- **n_samples confound control**: Qwen3-8B n=8 data exists as control. CoNLL SJ: n8 ρ=0.4389 → n16 ρ=0.4496 (Δ=0.011, CI crosses zero). SciERC SJ: n8→n16 Δ=0.066, CI=[0.004, 0.128] weak effect. n_samples not a confound for 4B-8B comparison.\\n- **Paper framing**: \\\"Scale ablation shows the gap is not an artifact of a particular model size; correlation strength is maintained at 4B, confirming that the gap originates from within-instance signal misalignment rather than model capacity.\\\"\\n\\n**exp-019 supervised verifier**: IN PROGRESS (D116 Dream feedback — all 3 tiers flagged as critical gap). Simplified to logistic regression on 5 signals (scikit-learn, CPU, ~30min). If supervised verifier partially closes oracle gap → proves gap IS closable, signals carry information but unsupervised heuristics are too weak. Grounds the \\\"what would be needed\\\" part of Contribution B.\\n\\n**exp-023 LoRA rank=8 ablation** [DONE]: rank=8 vs rank=32 on SciERC. Degeneracy: 7.2% vs 21% (3× reduction). Oracle headroom: 16.0pp vs 13.3pp. But ALL selection methods still fail to beat greedy (LP -0.5pp, SJ -0.9pp). QE correlation preserved (VC ρ=0.394, SJ ρ=0.365). **Key insight**: Reducing degeneracy is NECESSARY but NOT SUFFICIENT — signals themselves lack the discriminative power to exploit increased headroom. Strengthens multi-causal argument and points to trained verifiers as the path forward. Dream 三档公认最强实验。\\n\\n**Bonus finding (parse rate)**: Free-form parse rate 99.95% (4406/4408) — fine-tuned 8B model generates valid JSON without grammar constraints. Challenges intro:19 claim about constrained decoding necessity for format compliance.\\n\\n**Implications**: Not just \\\"signals don't work\\\" but \\\"here's WHY they don't work (intrinsic score compression), here's proof it's universal (controlled ablation via elimination), and here's the forward direction (breaking LP compression requires fundamentally different approaches — trained verifiers, multi-round refinement — not simply relaxing decoding constraints).\\\"\\n\\n### Claim 2 (METHODOLOGY — QE Evaluation Framework)\\nSystematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.\\n\\n**Key results**:\\n- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205). 3-seed consistent: SJ > FK delta=0.093~0.122\\n- RE (3-seed confirmed): **LP > SJ > FK** (mean ρ: LP 0.302, SJ 0.265, FK 0.254). Signal ranking reverses vs NER — structural signals lose advantage when 43-45% of RE samples have F1=0 (binary signal dominance). LP's coarse but stable generation-confidence signal captures \\\"did the model get any relations right\\\" better than structural overlap measures.\\n- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)\\n- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09. T=0.7: LP full ρ improves 0.205→0.249, LP cond ρ 0.154→0.185; FK 0.267→0.289 despite more compression → concentrated signal hypothesis (non-tied instances at lower T carry more informative variance). **Paper citation rule**: robustness/temperature tables use full ρ; score compression analysis uses cond ρ. Always annotate which variant.\\n- **Task-dependent signal effectiveness** (new finding from RE 3-seed): The optimal signal family depends on task structure. NER (token-level, graded F1) → structural agreement captures quality gradients. RE (relation-level, binary-dominated F1) → logprob captures generation confidence better. This is NOT a weakness — it's a nuanced finding that enriches the diagnostic framework.\\n\\n**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):\\n- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578\\n- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601\\n- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706\\n\\n### Claim 2b (Selection evidence)\\n**exp_016_rerun_1024 evidence** (SciERC 8B, N=8, T=1.0):\\n- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)\\n- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)\\n\\n**4B selection evidence** (N=8, T=1.0):\\n- CoNLL NER 4B (n=2756): greedy 0.9213, SJ 0.9220 (+0.07pp), FK 0.9215, LP 0.9221 (+0.09pp), oracle 0.9382. Headroom 1.70pp → selection indistinguishable\\n- SciERC NER 4B (n=529): greedy 0.6622, SJ 0.6473 (-1.49pp), FK 0.6466 (-1.56pp), LP 0.6399 (-2.23pp), oracle 0.7925 (+13.02pp). **All signals worse than greedy** → correlation-selection gap at 4B confirmed\\n\\n**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):\\n- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39\\n- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466\\n\\n### Claim 3 (Diagnostic — task-complexity boundary + task-dependent signal effectiveness)\\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\\n\\n**RE 3-seed mechanism** (D073, confirmed at 4B): 43-47% of RE samples have F1=0 (8B: 43-45%, 4B: 47.6%), creating binary-dominated signal distributions where structural overlap (SJ/FK) cannot differentiate quality gradients. Pattern consistent across model scales — confirming task difficulty, not model capacity, drives this boundary. LP's generation confidence captures \\\"complete failure vs partial success\\\" more reliably. 3-seed RE QE: LP ρ=0.302 > SJ 0.265 > FK 0.254. **Definitive binary dominance evidence**: RE LP full ρ=0.266 but cond ρ=0.011 (p=0.86, completely n.s.) — LP's entire RE signal comes from the zero/nonzero F1 split; once conditioned on samples where the model extracts at least one relation, LP has zero predictive power for RE quality gradients. In contrast, NER LP cond ρ remains informative (0.154–0.185). This provides the concrete mechanism for Claim 3's task-complexity boundary: it's not just \\\"compound error\\\" in the abstract — it's specifically the high zero-F1 rate that shifts the optimal signal family from structural to probabilistic, and LP's RE advantage is entirely a binary classification effect, not genuine quality estimation.\\n\\n**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\\n\\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\\n\\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\\n\\n## Story Spine (D116 — Dual Contribution: QE Positive + Selection Diagnostic, Main Conference)\\n\\n**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: (1) can confidence signals estimate output quality? (2) can they select better outputs?\\n\\n**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) present a fundamentally different challenge — prior work conflates quality estimation with selection. We decouple these and show they are governed by different factors.\\n\\n**Our framing (D116 — DUAL CONTRIBUTION)**:\\n\\n**Contribution A (Positive — QE Framework)**: Five confidence signals across four families reliably predict structured IE output quality (AUROC 0.82, ρ 0.45). Signal ranking is task-dependent: structural > probabilistic for NER, reversed for RE. This QE framework has practical value for selective prediction / error flagging regardless of selection effectiveness.\\n\\n**Contribution B (Diagnostic — Why Selection Fails + What Would Fix It)**:\\n1. **Design property**: 4/5 signals are instance-level aggregates → cannot rank candidates by construction.\\n2. **Instance Degeneracy**: 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom.\\n3. **LP Compression**: Logprob within-instance range compressed (0.041 nats). Free-form ablation confirms intrinsic (std ratio 0.97).\\n4. **Multi-causal** (key D116 update): LoRA rank=8 reduces degeneracy 3× (7.2% vs 21%) and increases oracle headroom (+2.7pp), but ALL selection methods still fail to beat greedy → low degeneracy is NECESSARY but NOT SUFFICIENT. Signals lack discriminative power even when headroom exists.\\n5. **Capability-degeneracy tradeoff** (renamed from \\\"trap\\\"): Higher capability → more convergence → more degeneracy. Qualitative monotone relationship across datasets (CoNLL 91%→58% degen, SciERC 66%→21%). R² on n=3 is illustrative only, not statistically reliable.\\n6. **Path forward**: Non-tied subset +2.9pp (p=0.004) proves signals carry information. Trained verifier baseline (logistic regression on 5 signals, in progress) tests whether the gap is closable with supervision. If so → unsupervised signals are weak, not uninformative.\\n\\n**QE-vs-Selection Decoupling** (Dream-identified most novel insight): QE correlation (SJ ρ) is stable across LoRA rank configurations (0.360→0.378) while selection gap changes dramatically. Signals are ALWAYS useful for flagging uncertain instances, even when they cannot improve selection. This distinction has practical implications beyond IE.\\n\\n**Headline**: \\\"We present a dual contribution for structured IE: (1) a QE framework showing confidence signals reliably predict output quality (AUROC 0.82), and (2) a diagnostic analysis revealing why these same signals fail at selection — instance degeneracy and logprob compression create a multi-causal gap that persists even when degeneracy is reduced. Selection approximately matches greedy decoding (Δ<0.3pp, all p>0.05) despite 13pp oracle headroom.\\\"\\n\\n**Title**: \\\"Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Only one NER dataset — generalization unclear\\\"\\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\\n- **Priority**: P0\\n\\n### R2: \\\"Only one model family (Qwen3-8B)\\\"\\n- **Mitigation**: LLaMA-3.1-8B shows model-agnostic effect. ⚠️ **exp-007 数据被污染 (test data leakage)**，LLaMA SciERC 正确值来自 exp_018 (clean rerun)。unified_rho_full.json 的 LLaMA SciERC 条目必须替换为 exp_018 数据。正确 LLaMA SciERC N=8 3-seed mean: SJ 0.325, FK 0.256, VC 0.384, EM 0.279, LP 0.162。\\n- **Priority**: P0\\n\\n### R3: \\\"FK is a strawman baseline — what about log-prob, USC, exact-match?\\\"\\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).\\n- **Priority**: P0, RESOLVED — results decisive\\n\\n### R3b: \\\"EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?\\\"\\n- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.\\n- **Priority**: P1 — narrative adjusted for 1024-token results\\n\\n### R4: \\\"No actual TTS improvement demonstrated\\\"\\n- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.\\n- **Mitigation**: Paper PIVOTS to \\\"confidence estimation + correlation-selection gap analysis.\\\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\\n- **Priority**: P0 — narrative pivot complete, bootstrap confirms\\n\\n### R5: \\\"Sample size N=8 may be too small for reliable SJ estimation\\\"\\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\\n- **Priority**: P0\\n\\n### R6: \\\"Conditional analysis cherry-picks favorable instances\\\"\\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\\n- **Priority**: P0 (add sensitivity analysis)\\n\\n### R7: \\\"Only ρ as evaluation metric\\\"\\n- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).\\n- **Priority**: P0\\n\\n### R8: \\\"Formula-implementation discrepancy\\\"\\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\\n- **Priority**: P0, paper writing fix\\n\\n### R9: \\\"Evaluation circularity (T>0 consistency vs T=0 F1)\\\"\\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\\n- **Priority**: P0\\n\\n### R10: \\\"Insufficient related work\\\" (三档一致 [B][M][W])\\n- **Mitigation**: Expand to 35+ references. Must cite:\\n  - USC (Chen 2024) — empirical differentiation, not just citation\\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\\n  - **IE confidence**: Culotta & McCallum 2004\\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\\n  - **[2025-2026 新颖性自查补充 — 必引]**:\\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\\\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\\\"overlooks semantically consistent outputs\\\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\\n  - **[2025-2026 新颖性自查补充 — 应引]**:\\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\\n  - **需新增 Related Work 小节**:\\n    - \\\"Test-Time Scaling & Sample Selection\\\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\\n    - \\\"Consistency for Structured IE\\\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\\n- **Priority**: P0, Paper Agent handles\\n\\n### R11: \\\"SJ+logprob ensemble missing\\\" (Dream 2 — both reviewers)\\n- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:\\n  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078\\n  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706\\n  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)\\n  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.\\n- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)\\n\\n### R12: \\\"No supervised upper bound / reward model comparison\\\" (Dream 2)\\n- **Mitigation**: exp-016 LR ensemble (5-signal, 5-fold CV) underperforms best single signal EM (AUROC 0.666 vs 0.749), suggesting feature redundancy. exp-019 supervised verifier SKIPPED (DDL risk + scope creep). Free-form ablation provides the \\\"so what\\\": gap is fundamental → closing it requires fundamentally different approaches (trained verifiers, not just better unsupervised signals). Positioned as future work with explicit motivation from ablation evidence.\\n- **Priority**: P1, addressed via framing (future work motivated by ablation)\\n\\n### R13: \\\"Headroom capture rate low\\\" (Dream 2)\\n- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.\\n- **Priority**: P0, paper writing\\n\\n### R14: \\\"Cross-model validation thin — need more than 2×8B\\\" (Dream 2)\\n- **Status**: ✅ RESOLVED by 4B scale ablation. 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}. All correlation metrics maintained or improved at 4B (e.g. SciERC NER SJ_ρ: 0.3825→0.4221, +3.96pp). Combined with LLaMA-3.1-8B cross-architecture data, now have 3 model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B). 70B infeasible — acknowledge as limitation.\\n- **Priority**: P0, RESOLVED\\n\\n### R15: \\\"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \\\"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\\\"\\n- **Priority**: P0, Paper Agent handles\\n\\n### R16: \\\"Zero figures — data-rich paper with only tables\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\\n- **Priority**: P0, Paper Agent handles\\n\\n### R17: \\\"Diagnostic framework overclaimed — descriptive not prescriptive\\\" (Dream 2 cross-tier, [M][W])\\n- **Mitigation**: Soften \\\"diagnostic framework\\\" to \\\"diagnostic analysis\\\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\\n- **Priority**: P0, Paper Agent handles\\n\\n### R18: \\\"No discussion of when consistency WOULD help\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\\n- **Priority**: P1, Paper Agent handles\\n\\n### R19: \\\"Negative result partially predictable for fine-tuned models\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\\n- **Priority**: P1, Paper Agent handles\\n\\n## Venue Fit\\n\\nEMNLP **Main Conference** target. Strengths:\\n- Systematic empirical comparison with mechanistic diagnosis (not just \\\"signals don't work\\\" but \\\"here's exactly why\\\")\\n- Two novel failure mechanisms (instance degeneracy + LP compression) + unifying capability trap insight\\n- Controlled ablation (free-form decoding) providing causal evidence\\n- Cross-model (Qwen3-8B/4B + LLaMA-3.1-8B), cross-dataset (SciERC + CoNLL + WNUT), cross-task (NER + RE) validation\\n\\nMain Conference gap vs Findings:\\n- **Need**: 3rd NER dataset (Few-NERD) to close \\\"only 2 NER datasets\\\" concern\\n- **Need**: 3rd seed for Fisher p-value power on key claims\\n- **Need**: LoRA rank=8 ablation to confirm fine-tuning degree doesn't drive degeneracy\\n- **Need**: Systematic claim audit resolving numerical contradictions\\n\\nRisk assessment:\\n- **Strongest asset**: Capability trap is a genuinely novel insight — no prior work connects model capability to vanishing TTS headroom via degeneracy\\n- **Weakest flank**: Dataset breadth (2 NER + 1 RE → 3 NER + 1 RE with Few-NERD)\\n- **Critical path**: Few-NERD + 3rd seed experiments must complete before DDL (2026-05-25, 9 days)\", \"total_chars\": 29459, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eef9f4c-9ce0-4548-849f-7c06aebd615e",
  "isSidechain": true,
  "promptId": "4e4f55b3-8499-4a23-9491-7cbbbb839d17",
  "agentId": "a6acb7d036d9ca50e",
  "type": "user",
  "uuid": "355cdedd-8eec-4da1-9650-9eaa2d57932e",
  "sourceToolAssistantUUID": "4eef9f4c-9ce0-4548-849f-7c06aebd615e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-16T11:58:07.754Z_

Now I have comprehensive context on the paper's literature positioning, framing, and internal concerns. Let me also check what the paper actually cites versus what's in the literature map but not cited.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "355cdedd-8eec-4da1-9650-9eaa2d57932e",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6D1c6nNqKd8bQjmjvHo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12067f42-bf47-4237-a5e1-990d13421974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPxwXosXv7jtcmBDCXKfGH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26322,
      "cache_read_input_tokens": 24300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26322,
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

_source line 16 · 2026-05-16T11:58:08.748Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019KcnHYx3ZxbGSgyoRcx3az`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "ROADMAP.md",
  "max_chars": 6000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12067f42-bf47-4237-a5e1-990d13421974",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6D1c6nNqKd8bQjmjvHo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe5d3d98-daf5-4aeb-a4f9-c549c98a0f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPxwXosXv7jtcmBDCXKfGH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26322,
      "cache_read_input_tokens": 24300,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 26322
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 24300,
          "cache_creation_input_tokens": 26322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 26322,
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

_source line 17 · 2026-05-16T11:58:08.764Z_

<details><summary>↩ Tool result · `toolu_019KcnHYx3ZxbGSgyoRcx3az`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\", \"content\": \"# struct_self_consist_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-16 09:25 UTC | 更新原因: D113 Table 2 critical bug — reprioritized: fix before new experiments\\n\\n## 核心方向\\nStructured IE 的 confidence signal 能预测质量（AUROC 0.82, ρ 0.45）但无法改善 greedy decoding。两个失败机制（instance degeneracy + LP compression）+ capability trap 统一解释。详见 paper_framing.md。\\n\\n## 目标\\n**EMNLP 2026 Main Conference** via ARR May 2026, DDL 2026-05-25（9 天）\\n\\n## ⚠️ D113 Critical: Table 2 micro/macro F1 混用\\n- Greedy 行用 micro F1 (0.663, 551 inst)，其他行用 macro F1 (529 inst)\\n- 公平比较: Greedy macro=0.645 ≈ LP=0.647, Selection 只能恢复 T=1.0 degradation\\n- \\\"Single\\\" 行标注错误（实际是 T=0 greedy）\\n- Agent 紧急修复中，P0 优先于所有新实验\\n\\n## 当前进展\\n- **阶段**: Research → Review 迭代（Round 15, 3.0/5）\\n- **Core Claims**: 三层论证 + capability trap (D112), micro/macro 修正 (D113)\\n- **数据集**: SciERC ✅ | CoNLL ✅ | WNUT ✅ | Few-NERD 🔄\\n- **模型**: Qwen3-8B ✅ | Qwen3-4B ✅ | LLaMA-3.1-8B ✅\\n- **Dream**: dream_20260516T092241 running (full mode)\\n\\n## 优先级（D113 修正版）\\n| 优先级 | 任务 | 时间 | GPU | 状态 |\\n|--------|------|------|-----|------|\\n| P0 | Table 2 统一 macro F1 + 叙事重构 | 4-8h | 0 | 🔄 Agent 紧急处理 |\\n| P1 | 3rd seed SciERC (exp-022) | 2-4h | 1 | ⏳ |\\n| P2 | Hybrid strategy (degenerate→greedy, non-degen→MBR) | 1-2h | 0 | ⏳ |\\n| P3 | LoRA rank=8 ablation (exp-023) | 4-6h | 1 | ⏳ |\\n| P4 | Few-NERD (exp-020/021) | 4-16h | 1 | ⏳ 数据准备 |\\n| P0 | Claim audit (exp-024) | CPU | 0 | 与 Table 2 修复合并 |\\n\\n## GPU 计划（2 GPUs）\\n- GPU 1: 3rd seed (3h) → LoRA rank=8 train (5h) → LoRA inference (2h)\\n- GPU 2: Few-NERD train (4-16h) → inference (2-3h)\\n- CPU 并行: Table 2 修复 + Hybrid 分析 + Claim audit\\n\\n## 近期任务\\n- [ ] Agent 完成 Table 2 macro F1 重算 + bootstrap (D113 P0)\\n- [ ] Paper Agent 修复 Abstract/Intro/Discussion/C3 叙事\\n- [ ] 3rd seed SciERC 推理 (exp-022)\\n- [ ] Hybrid strategy 分析\\n- [ ] LoRA rank=8 ablation (exp-023)\\n- [ ] Few-NERD smoke test → full (exp-020/021)\\n- [ ] Dream 完成后处理反馈\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D116 | 2026-05-16 | D116: Dream full review 分析 — Best/Worst 3.0, Media | exp_023_lora_rank8, exp_fewnerd_smoke |\\n| D115 | 2026-05-16 | D115: Few-NERD INTRA split 错误 — 暂停 exp-020，改用 supe | exp_fewnerd_smoke |\\n| D114 | 2026-05-16 | D114: Reviewer critical — D113 P0 修复停滞 + GPU 空转。紧急 | exp_3rd_seed_scierc, exp_fewnerd_smoke, exp_lora_rank8_ablation |\\n| D113 | 2026-05-16 | D113: Table 2 micro/macro F1 混用 critical bug — 修复优 | exp_016_rerun_1024, exp_016_rerun_1024_bootstrap |\\n| D112 | 2026-05-16 | D112: Main Conference 实验策略锁定 — Few-NERD + 3rd seed | d108_lp_vc_combination |\\n| D111 | 2026-05-16 | D110 修正: MF3 从 \\\"fine-tuning artifact\\\" 转为 \\\"capabili | d108_lp_vc_combination, d108_mbr_within_instance_rho |\\n| D110 | 2026-05-16 | Round 14→15: 三层结构重组 + fine-tuning artifact 差异化 + M | d108_mbr_within_instance_rho, d108_greedy_f1, d108_lp_vc_combination |\\n| D109 | 2026-05-16 | D109: 论文核心 claim \\\"within-instance utility 不相关\\\" 被 Q | exp_012_rerun_1024, exp_002_conll_n16_r1024 |\\n| D108 | 2026-05-16 | D108: Round 13 Action Matrix — T=0 greedy baseline | exp_012_rerun_1024, exp_002_conll_n16_r1024 |\\n| D107 | 2026-05-16 | Entity-token LP 实验完成(negative): 格式 token 稀释存在但非 LP | exp_entity_token_lp |\\n\\n\", \"total_chars\": 3107, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe5d3d98-daf5-4aeb-a4f9-c549c98a0f8b",
  "isSidechain": true,
  "promptId": "4e4f55b3-8499-4a23-9491-7cbbbb839d17",
  "agentId": "a6acb7d036d9ca50e",
  "type": "user",
  "uuid": "378923a5-0822-4873-89da-063c6fa7dfed",
  "sourceToolAssistantUUID": "fe5d3d98-daf5-4aeb-a4f9-c549c98a0f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-16T11:58:12.621Z_

Now I have sufficient context to write a thorough review. Let me also check what the paper's trained verifier result looks like, since this is a key claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "378923a5-0822-4873-89da-063c6fa7dfed",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6D23L5khHFaL3YdW5Lk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7713da0-e62c-4c27-bb95-0b411b7f4222",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wmZyXDtCovDS9FSRDuzDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2033,
      "cache_read_input_tokens": 50622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2033,
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

_source line 19 · 2026-05-16T11:58:13.171Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019aK4xZZgV6VNYXk4xmUKmc`</summary>

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
  "parentUuid": "a7713da0-e62c-4c27-bb95-0b411b7f4222",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6D23L5khHFaL3YdW5Lk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e37c79a-7675-478b-ba1a-27c76bd59a34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wmZyXDtCovDS9FSRDuzDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2033,
      "cache_read_input_tokens": 50622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2033,
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

_source line 20 · 2026-05-16T11:58:13.174Z_

<details><summary>↩ Tool result · `toolu_019aK4xZZgV6VNYXk4xmUKmc`</summary>

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
  "parentUuid": "8e37c79a-7675-478b-ba1a-27c76bd59a34",
  "isSidechain": true,
  "promptId": "4e4f55b3-8499-4a23-9491-7cbbbb839d17",
  "agentId": "a6acb7d036d9ca50e",
  "type": "user",
  "uuid": "f34bc6d4-aba1-4df1-8c36-18d62738accc",
  "sourceToolAssistantUUID": "8e37c79a-7675-478b-ba1a-27c76bd59a34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T11:59:36.024Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01Q2mHXqu8eiRaPHJ2khc7zd`</summary>

```json
{
  "report": "# R2 Review: Novelty & Related Work\n\n## Summary\n\nThis paper presents a dual contribution for structured information extraction: (1) a quality estimation framework showing five confidence signals predict output quality, and (2) a diagnostic analysis explaining why these signals fail at best-of-N selection despite strong population-level correlation. The multi-causal failure mechanism (instance degeneracy + logprob compression + insufficient discriminability) is the paper's core novelty claim. While the QE-selection decoupling insight is genuinely useful, the novelty is incremental over concurrent work (Nédellec & Xia 2026, CoCoA 2025), and the trained verifier experiment—which closes 36% of the oracle gap—is underdeveloped relative to its importance in the narrative.\n\n## Strengths\n\n- **The QE-selection decoupling is a genuinely novel conceptual contribution.** The distinction between population-level correlation (useful for selective prediction) and within-instance ranking (needed for selection) is clearly articulated and non-obvious. Prior work in self-consistency and MBR decoding conflates these, and this paper provides the first clean empirical separation for structured IE.\n\n- **The multi-causal diagnosis is well-structured.** Decomposing the failure into (a) design property of instance-level aggregates, (b) instance degeneracy, and (c) LP compression provides actionable understanding. The LoRA rank=8 ablation showing that reducing degeneracy is necessary but not sufficient is particularly compelling—it rules out the simplest explanation.\n\n- **Capability-degeneracy tradeoff is an interesting observation.** The monotone relationship between model capability and degeneracy (CoNLL 91% F1 → 58% degen, SciERC 66% → 21%, WNUT 48% → ~0%) provides a structural explanation for why test-time scaling via unsupervised selection faces diminishing returns as models improve. This has implications beyond IE.\n\n- **Breadth of evaluation.** 3 models × 3 datasets × 2 tasks with consistent findings strengthens the generality claims. The free-form decoding ablation (std ratio 0.97) providing causal evidence that LP compression is intrinsic rather than an artifact of constrained decoding is a well-designed control.\n\n- **Practical value of QE framework.** AUROC 0.82 for quality estimation is genuinely useful for deployment decisions (selective prediction, error flagging) regardless of selection effectiveness.\n\n## Weaknesses\n\n- **Incremental novelty over Nédellec & Xia (2026).** The paper positions itself as substantially advancing beyond Nédellec & Xia by using structural Jaccard rather than surface-level string matching. However, the core finding—consistency correlates with accuracy for LLM-based IE—is the same. The paper's genuine advance is the negative result (selection fails) and the diagnostic, not the QE framework itself. The \"dual contribution\" framing risks overclaiming: Contribution A (QE works) is largely a replication with better metrics of what Nédellec & Xia already showed.\n\n- **The trained verifier experiment is too thin for its narrative weight.** The paper argues that the \"path forward\" is trained verifiers, and the logistic regression closing 36% of the NER oracle gap is presented as evidence that signals carry exploitable information. But a 5-feature logistic regression is a minimal baseline—no comparison to even a simple MLP, no cross-dataset transfer evaluation, no analysis of what the verifier learns. For a paper that makes \"what would fix it\" a core part of Contribution B, this experiment needs substantially more development. It currently reads as a pilot study wrapped in strong claims.\n\n- **The \"Capability Trap\" claim is based on n=3 data points.** The monotone relationship between capability and degeneracy is observed across exactly 3 datasets with different characteristics (domain, entity types, difficulty). The paper acknowledges this is \"illustrative only, not statistically reliable,\" but it still occupies significant narrative space. This is correlation on 3 points with multiple confounds (domain complexity, annotation granularity, entity type diversity).\n\n- **Missing comparison to constrained decoding / structured generation approaches.** The paper studies confidence signals for selecting among unconstrained samples, but does not engage with the literature on constrained decoding (Willard & Louf 2023, GenIE's bi-level constrained decoding) as an alternative approach to improving structured output quality. If constrained decoding can guarantee structural validity, does the entire selection paradigm become less relevant? The paper's own finding of 99.95% parse rate partially addresses this but doesn't fully engage with the implication.\n\n- **The negative result's novelty is partially diminished by predictability.** For fine-tuned models with high greedy performance (CoNLL 91% F1), it is somewhat expected that sampling at T=1.0 would not easily improve over greedy—the model is already near-converged. The paper argues non-obviousness by citing self-consistency's success for reasoning, but reasoning tasks typically have much lower greedy accuracy (GSM8K ~50-70%) where there is more headroom. The paper would benefit from explicitly addressing this asymmetry in task difficulty.\n\n- **Title may overstate the finding.** \"Why Confidence Signals Cannot Scale Structured Information Extraction\" implies a universal impossibility, but the paper shows that *unsupervised* confidence signals fail. The trained verifier partially succeeds (+4.8pp), and the paper's own discussion suggests supervised approaches could work. \"Cannot\" is too strong—\"struggle to\" or \"fail to unsupervisedly\" would be more accurate.\n\n## Missing Related Work\n\n**Critical omissions:**\n\n1. **Reward models / ORMs / PRMs for non-math domains.** The paper cites Cobbe et al. (2021) and Lightman et al. (2023) for math verifiers but does not engage with the broader literature on applying verification to non-mathematical structured tasks. Recent work on reward models for code generation (e.g., CodeRM), factual verification, and structured QA is directly relevant to the \"trained verifier as path forward\" argument. Without this, the Discussion's \"path forward\" lacks grounding in what has already been attempted.\n\n2. **Test-time compute scaling beyond the cited papers.** The paper misses Sardana et al. (2025) \"Beyond Decoding\" survey, DeepSeek-R1's approach to test-time scaling via extended reasoning, and the broader \"scaling laws for test-time compute\" literature (e.g., the compute-optimal allocation work by Wu et al. 2024, which IS in the lit map but not cited in the paper). The paper's contribution is fundamentally about *when test-time scaling fails*—it should engage more deeply with the conditions under which it succeeds.\n\n3. **Entity linking and disambiguation confidence.** The IE confidence literature (Culotta & McCallum 2004 is cited) has evolved significantly. Work on entity linking confidence (Rao et al. 2013), knowledge graph completion confidence (Safavi et al. 2020), and recent neural IE confidence calibration is relevant but missing.\n\n4. **CRF-based structured prediction uncertainty.** The paper jumps from classical IE confidence (Culotta & McCallum 2004) to LLM-based approaches without engaging with the CRF/BiLSTM-CRF era's uncertainty quantification (Xiao & Wang 2019 is in the lit map but appears not cited). The evolution from token-level CRF uncertainty to sample-level LLM consistency deserves explicit discussion.\n\n5. **Universal Self-Consistency (Chen et al. 2024).** This paper extends self-consistency to free-form generation using the LLM itself as a judge—directly relevant as an alternative aggregation mechanism that could potentially address the instance degeneracy problem (by having the model evaluate rather than just vote). Listed in the lit map but the paper's engagement appears superficial.\n\n6. **Multi-output evaluation metrics for IE.** The paper uses entity-level and instance-level F1 but does not discuss the evaluation methodology literature (e.g., Segura-Bedmar et al. 2013 on relaxed matching, Fu et al. 2020 on entity-level evaluation issues). Given that the structural Jaccard metric is a core methodological contribution, positioning it relative to existing set-comparison metrics for IE would strengthen the paper.\n\n**Recommended additions (lower priority):**\n\n7. Calibration of structured predictors beyond Kuleshov & Liang 2015 (e.g., Jagannatha & Yu 2020 on calibrating structured output predictors for NLP—in the lit map, may not be cited).\n8. MBR decoding for structured prediction tasks beyond MT (e.g., parsing, semantic role labeling).\n9. The abstention/selective prediction survey (Wen et al. 2025, TACL) for positioning the QE contribution.\n\n## Questions for Authors\n\n1. **On the trained verifier**: The logistic regression closes 36% of the oracle gap. What is the performance ceiling of a verifier that has access to the actual output text (not just the 5 scalar signals)? Have you considered a lightweight neural verifier that could assess structural plausibility?\n\n2. **On the capability trap**: With only 3 data points, how do you distinguish the capability-degeneracy relationship from a simpler confound—dataset annotation granularity? CoNLL has 4 coarse entity types, SciERC has 6 scientific types, WNUT has 6 noisy types. Could type granularity rather than model capability drive degeneracy differences?\n\n3. **On the QE-selection decoupling**: You show QE correlation is stable across configurations while selection effectiveness varies. But have you tested whether QE-based selective prediction (abstaining on low-confidence instances) actually improves precision-coverage tradeoffs in a deployment-realistic scenario? This would make Contribution A substantially more concrete.\n\n4. **On Universal Self-Consistency**: Chen et al. (2024) use the LLM itself to select the most consistent answer. Have you evaluated this approach for structured IE? It seems like a natural baseline that could address the instance degeneracy problem by leveraging semantic rather than surface-level comparison.\n\n5. **On the free-form ablation**: The 99.95% parse rate suggests fine-tuned models don't need constrained decoding. Does this mean the entire constrained decoding literature for IE is rendered obsolete for fine-tuned LLMs, or is this specific to your training setup?\n\n## Scores\n\n**Soundness**: 3.5/5\nThe experimental methodology is generally sound with appropriate controls (free-form ablation, bootstrap significance testing, multi-seed). However, the capability trap claim on n=3 points, the underdeveloped verifier experiment, and the partially predictable negative result for high-accuracy settings weaken confidence. The QE evaluation is solid.\n\n**Excitement**: 3.0/5\nThe QE-selection decoupling insight is genuinely interesting and the multi-causal diagnosis is well-executed. However, the core finding (unsupervised selection fails for structured IE) is somewhat expected for fine-tuned models near convergence, and the \"path forward\" (trained verifiers) is insufficiently developed to generate real excitement about follow-up directions. The paper identifies a problem more compellingly than it advances solutions.\n\n**Overall Assessment**: 3.0/5\nThis is a solid empirical study with a genuinely novel conceptual contribution (QE-selection decoupling) and thorough diagnosis. It is suitable for Findings-level publication. For Main Conference, it would need: (a) a more developed trained verifier showing the gap is closable with moderate supervision, (b) stronger engagement with alternative approaches (USC, constrained decoding), and (c) tighter positioning relative to Nédellec & Xia (2026). The dual-contribution framing currently bundles one strong contribution (diagnostic) with one incremental contribution (QE framework).\n\n**Confidence**: 4/5\nI am familiar with the self-consistency, uncertainty quantification, and structured IE literatures. The test-time scaling and reward model literatures are adjacent to my core expertise but I have reviewed multiple papers in these areas.\n\n**Reproducibility**: 4/5\nThe paper specifies models, datasets, hyperparameters, and evaluation metrics clearly. The 5 signals are well-defined. Reproduction would require LoRA fine-tuning of 3 models but this is standard. The structural Jaccard metric's implementation details (type-grouped Hungarian matching) should be provided in an appendix for full reproducibility.\n",
  "project": "struct_self_consist_ie",
  "tier": "median",
  "dream_id": "dream_20260516T092241",
  "overall_score": "borderline findings (3.0/5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f34bc6d4-aba1-4df1-8c36-18d62738accc",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6D2N1Uu9awXy6zhggPT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d77bed0-2894-4ad8-87d2-d13e5fc1b9b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qse5GKrnoKD6dU8ZaF5ea",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 52655,
      "output_tokens": 3065,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 804
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3065,
          "cache_read_input_tokens": 52655,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 804,
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

_source line 22 · 2026-05-16T11:59:39.267Z_

<details><summary>↩ Tool result · `toolu_01Q2mHXqu8eiRaPHJ2khc7zd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/review_report.md\", \"dream_id\": \"dream_20260516T092241\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d77bed0-2894-4ad8-87d2-d13e5fc1b9b1",
  "isSidechain": true,
  "promptId": "4e4f55b3-8499-4a23-9491-7cbbbb839d17",
  "agentId": "a6acb7d036d9ca50e",
  "type": "user",
  "uuid": "8df636d7-47c7-46a0-adc0-03719d5edfb2",
  "sourceToolAssistantUUID": "9d77bed0-2894-4ad8-87d2-d13e5fc1b9b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T11:59:48.641Z_

Review submitted. Here is the summary:

---

**R2 Review (Novelty & Related Work) — Overall: 3.0/5 (Findings-level)**

Key assessments:

**Strengths**: The QE-selection decoupling is a genuinely novel conceptual contribution. The multi-causal diagnosis (degeneracy + LP compression + discriminability gap) is well-structured, and the LoRA rank=8 ablation ruling out the simplest explanation is compelling. The capability-degeneracy tradeoff observation has implications beyond IE. Evaluation breadth (3 models, 3 datasets, 2 tasks) is adequate.

**Main weaknesses for novelty**:
1. Incremental over Nédellec & Xia (2026) — the QE framework (Contribution A) is largely replication with better metrics
2. Trained verifier experiment too thin for its narrative weight (5-feature LR is a minimal baseline for a "path forward" claim)
3. Capability trap based on n=3 data points with confounds
4. Title overstates ("Cannot" vs what's actually shown: unsupervised signals fail while supervised partially succeeds)
5. Negative result partially predictable for high-accuracy fine-tuned models

**Critical missing related work**: Reward models for non-math domains, broader test-time compute scaling literature (DeepSeek-R1, Wu et al. 2024), entity linking confidence, CRF-era uncertainty quantification, Universal Self-Consistency as an alternative aggregation mechanism, multi-output IE evaluation metrics.

**Scores**: Soundness 3.5, Excitement 3.0, Overall 3.0, Confidence 4, Reproducibility 4.

The report is saved at `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8df636d7-47c7-46a0-adc0-03719d5edfb2",
  "isSidechain": true,
  "agentId": "a6acb7d036d9ca50e",
  "requestId": "req_011Cb6D8hZds4ve2DnRu8iqd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6953caa4-ae1d-4d3c-980b-752901c9e372",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "352b5339-5de3-432c-8453-cee5bd2f497d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eCaaQcVP9QJRKrnuFeLfQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3195,
      "cache_read_input_tokens": 53459,
      "output_tokens": 461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3195
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 461,
          "cache_read_input_tokens": 53459,
          "cache_creation_input_tokens": 3195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3195,
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
