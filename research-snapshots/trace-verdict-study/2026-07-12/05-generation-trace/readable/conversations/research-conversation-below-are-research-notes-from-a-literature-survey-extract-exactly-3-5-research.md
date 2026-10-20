# Research conversation: Below are research notes from a literature survey. Extract exactly 3-5 research directions from these notes. Output ONLY

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/3b12a614-3082-421d-b79f-1abb766e2823.jsonl`
- **Structured JSON:** [`aa31cbea0537dc9b2b32.json`](../../sessions/aa/aa31cbea0537dc9b2b32.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-11T22:00:25.293Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-11T22:00:25.293Z",
  "sessionId": "3b12a614-3082-421d-b79f-1abb766e2823",
  "content": "Below are research notes from a literature survey. Extract exactly 3-5 research directions from these notes.\n\nOutput ONLY a JSON array (no markdown fences, no other text). Each element:\n{\n  \"title\": \"Concise English title (max 10 words)\",\n  \"core_problem\": \"The fundamental research question (1-2 sentences)\",\n  \"opportunity\": \"The specific gap or why now (2-3 sentences)\",\n  \"landscape\": \"Current SOTA and limitations from the notes (3-5 sentences)\"\n}\n\n--- RESEARCH NOTES ---\nI now have extensive coverage of the landscape. Let me compile my findings into the final output.\n\nBased on my extensive research (25+ targeted searches, 4 deep paper reads), here is my synthesis of the landscape and proposed research directions.\n\n**Key landscape observations:**\n- Model collapse is well-theorized (ICLR 2025 Strong Collapse, ICML 2025 Collapse or Thrive, Nature 2024), but practical **detection and prevention methods** during training remain scarce\n- Self-verification (NeurIPS 2025) and external verifiers (arXiv 2510.16657) provide theoretical guarantees but haven't been tested as **online, adaptive** training interventions\n- Hierarchical contamination detection (arXiv 2511.17602) addresses semantic-level contamination but treats it as a **post-hoc audit**, not integrated into data curation pipelines\n- Pluralistic reward curation (ICML 2026, arXiv 2605.07724 — 3 days ago!) proves diversity preservation through multiple rewards, but is purely theoretical with limited LLM experiments\n- **Critical gap**: No existing work unifies collapse monitoring + adaptive intervention as an online training recipe with empirical validation on small LMs\n- SIGMA (arXiv 2601.03385) proposes spectral monitoring but hasn't been connected to actionable data mixing decisions\n- Data mixing laws (ICLR 2025) predict performance from mixture ratios but don't adapt dynamically based on collapse signals\n\n```json\n[\n  {\n    \"title\": \"Entropy-Gated Adaptive Data Mixing for Collapse Prevention\",\n    \"core_problem\": \"Current synthetic data mixing strategies use fixed ratios determined before training, but model collapse is a dynamic process whose onset varies by data quality and model capacity. How can we detect incipient collapse during training and dynamically adjust the synthetic-to-real data ratio in real time?\",\n    \"opportunity\": \"SIGMA (arXiv 2601.03385) introduced spectral monitoring for collapse but without actionable intervention. Self-verification (NeurIPS 2025) provides theoretical guarantees but uses binary accept/reject rather than ratio adjustment. No existing method connects online collapse signals (entropy drop, spectral contraction, n-gram diversity decline) to adaptive mixing decisions. This is feasible now because small open models (Pythia-1B, OLMo-1B) enable running 3-5 generation experiments within 200 H100-hours, and the metrics (self-BLEU, n-gram entropy, embedding eigenspectrum) are computationally cheap to monitor during training.\",\n    \"landscape\": \"Data Mixing Laws (ICLR 2025) predict static optimal ratios; ADO (arXiv 2410.11820) adapts domain mixtures via scaling laws but doesn't track collapse signals; 'Collapse or Thrive' (ICML 2025) establishes accumulate vs. replace theory without online intervention; Strong Model Collapse (ICLR 2025) proves collapse occurs even with vanishingly small synthetic fractions but offers no adaptive mitigation. The recent 'Curated Synthetic Data Doesn't Have to Collapse' (ICML 2026, arXiv 2605.07724) uses pluralistic rewards for diversity but is theoretical and doesn't address the online monitoring problem. The gap is a practical method that monitors collapse indicators during training and adjusts data mixing dynamically — moving from post-hoc analysis to real-time prevention.\"\n  },\n  {\n    \"title\": \"Generation-Depth-Aware Contamination Detection for Recursive Synthetic Data\",\n    \"core_problem\": \"As web data becomes ~74% AI-generated (2025 estimates), training corpora inevitably contain multi-generation synthetic text (model B trained on model A's output, model C on model B's, etc.). Can we detect the generational depth of synthetic text and use this signal to filter training data before quality degradation compounds?\",\n    \"opportunity\": \"Hierarchical contamination detection (arXiv 2511.17602) achieves F1=0.76 on semantic contamination but treats all synthetic data as binary (synthetic vs. real), ignoring the critical distinction between first-generation and nth-generation synthetic text. Min-K%++ (ICLR 2025) improves membership inference but doesn't address generational depth. No existing method estimates how many recursive generation steps a text has undergone, despite strong theoretical evidence (Nature 2024, ICLR 2025) that degradation accelerates with generation depth. This is newly feasible because we can construct controlled multi-generation corpora using small open models and train classifiers on generation-depth labels.\",\n    \"landscape\": \"Current contamination detection operates at a binary level: synthetic vs. real. Min-K% and Min-K%++ (ICLR 2025) detect pre-training membership; ConStat detects contamination via performance gaps on rephrased samples; CoDeC uses in-context learning for contamination. The survey by Dong et al. (arXiv 2502.14425) categorizes white/gray/black-box detection without addressing generational depth. 'From Collapse to Improvement' (arXiv 2602.10531) studies iterative contamination statistically but doesn't propose detection methods. The recursive pollution concept (BIML, Jan 2026) distinguishes pollution from collapse but lacks a detection algorithm. The gap is a practical classifier or scoring function that estimates generation depth, enabling quality-aware filtering where later-generation text is downweighted more aggressively.\"\n  },\n  {\n    \"title\": \"Spectral Early-Warning System for Model Collapse with Intervention Protocols\",\n    \"core_problem\": \"Model collapse is typically studied as a post-hoc phenomenon analyzed after training completes. Can we build a lightweight, real-time early-warning system that detects the spectral signatures of incipient collapse during training and triggers automated intervention (data refresh, ratio adjustment, or early stopping)?\",\n    \"opportunity\": \"SIGMA (arXiv 2601.03385, Jan 2026) proposes spectral monitoring via embedding Gram matrix eigenspectra but lacks actionable intervention protocols and empirical validation on LLMs. The ecological early-warning literature (spectral EWS via eigenvalue analysis) provides mature mathematical frameworks for detecting critical transitions that have never been applied to LLM training dynamics. Entropy-Adaptive Fine-Tuning (arXiv 2601.02151) uses entropy for forgetting prevention but doesn't address collapse in recursive synthetic training. This cross-domain connection between dynamical systems early-warning theory and LLM collapse monitoring is novel and can be validated efficiently with small models (Pythia/OLMo) across 3-5 synthetic generations.\",\n    \"landscape\": \"SIGMA benchmarks model collapse through spectral properties but is purely diagnostic without interventions. The 'Generalization-to-Memorization' perspective (arXiv 2509.16499) characterizes collapse as a phase transition but doesn't propose monitoring. Ecological EWS literature (Royal Society Interface 2020, Nature Scientific Reports 2019) uses eigenvalue analysis to predict critical transitions in dynamical systems — conceptually analogous but never applied to LLM training. In the RL training context, DAPO (arXiv 2503.14476) monitors entropy and reward variance for stability but doesn't address synthetic data collapse. The key gap is connecting spectral diagnostic tools to automated intervention decisions: when eigenspectrum contraction exceeds a threshold, trigger a protocol (increase real data ratio, refresh synthetic generation, or pause training).\"\n  },\n  {\n    \"title\": \"Multi-Reward Diversity-Preserving Synthetic Data Curation Pipeline\",\n    \"core_problem\": \"Synthetic data curation using a single quality metric (e.g., perplexity, reward model score) tends to select homogeneous high-scoring samples, accelerating diversity loss and collapse. Can multi-objective curation using diverse reward signals preserve distributional coverage while maintaining quality?\",\n    \"opportunity\": \"The pluralistic preferences theory (ICML 2026, arXiv 2605.07724, published May 8, 2026 — 3 days ago) proves that multi-reward curation prevents collapse and converges to a Nash bargaining solution, but validation is limited to image generation (diffusion models) with only 2-5 reward functions. No empirical work has tested this framework on language model recursive training. The Data-Quality Illusion (arXiv 2510.00866) shows single-quality-classifier filtering doesn't reliably improve LM performance, motivating multi-signal approaches. DATAPROPHET (ICLR 2026) combines cross-modal metrics but targets multimodal, not recursive text generation. This is the first opportunity to empirically validate pluralistic curation theory on LLM collapse prevention, with practical implications for training pipelines.\",\n    \"landscape\": \"Self-verification (NeurIPS 2025) uses internal confidence as a single curation signal; external verification (arXiv 2510.16657) proves verifier-guided selection prevents collapse but acknowledges performance eventually converges to verifier limits. Pluralistic preferences (ICML 2026) provides the theoretical framework but only for image generation. Quality-diversity-complexity surveys (arXiv 2412.02980) map the dimensions but don't propose concrete multi-reward curation algorithms for iterative training. The reverse-bottleneck framework (ICLR 2025) connects information gain to generalization but doesn't prescribe how to compute or combine multiple quality signals in practice. The gap is an empirical, practical pipeline that implements pluralistic curation for LLM synthetic data — curating with 3-5 diverse reward functions (perplexity, diversity, coherence, task-relevance, novelty) and measuring collapse prevention across iterative training generations.\"\n  },\n  {\n    \"title\": \"Contamination-Aware Benchmark Calibration via Synthetic Data Provenance\",\n    \"core_problem\": \"Benchmark scores are increasingly unreliable because training data may contain synthetic paraphrases of test items that evade n-gram decontamination. Can we build a provenance-tracking system that identifies which benchmark items have semantic near-duplicates in synthetic training data and calibrate reported scores accordingly?\",\n    \"opportunity\": \"Rephrased test items can boost MMLU accuracy to 85.9% while evading all standard decontamination (arXiv 2311.04850). RL post-training contamination (arXiv 2510.09259) shows GRPO amplifies contamination effects beyond SFT. The Self-Critique method detects RL-phase contamination through output entropy collapse but only works for RL-trained models. No existing method provides provenance-aware score calibration that estimates how much of a benchmark score is attributable to contamination. With the EMNLP 2026 special theme explicitly calling for work on contamination and data governance, a method that not only detects but quantifies and calibrates contamination would be highly impactful. This is feasible using embedding-based semantic similarity between training data and benchmark items with controlled contamination injection experiments.\",\n    \"landscape\": \"Five detection methods are currently recognized: time-based partition, Min-K%, Time Travel, ConStat, and BIG-Bench canary. DCR (EMNLP 2025) quantifies contamination but focuses on corpus-level statistics, not item-level calibration. The comprehensive survey (arXiv 2502.14425) maps white/gray/black-box methods but notes most methods fail against paraphrased contamination. Dynamic benchmarking (LiveBench) mitigates contamination by rotating questions monthly but doesn't calibrate existing static benchmark scores. The hierarchical detection framework (arXiv 2511.17602) catches semantic-level contamination but doesn't provide calibrated score adjustments. The gap is a calibration method that takes a model's benchmark score, a measure of contamination exposure, and outputs an adjusted score — analogous to confidence intervals but for contamination uncertainty.\"\n  }\n]\n\nSources:\n- [Model collapse in Nature](https://www.nature.com/articles/s41586-024-07566-y)\n- [Is Model Collapse Inevitable? (ICLR 2025)](https://arxiv.org/abs/2404.01413)\n- [Strong Model Collapse (ICLR 2025)](https://openreview.net/forum?id=et5l9qPUhm)\n- [Collapse or Thrive (ICML 2025)](https://openreview.net/forum?id=Xr5iINA3zU)\n- [Self-Verification Prevents Collapse (NeurIPS 2025)](https://openreview.net/forum?id=X5Hk8aMs6w)\n- [Escaping Collapse via Verification](https://arxiv.org/abs/2510.16657)\n- [SIGMA: Spectral Insights for Collapse](https://arxiv.org/abs/2601.03385)\n- [Hierarchical Contamination Detection](https://arxiv.org/abs/2511.17602)\n- [Curated Synthetic Data with Pluralistic Preferences (ICML 2026)](https://arxiv.org/abs/2605.07724)\n- [From Collapse to Improvement](https://arxiv.org/abs/2602.10531)\n- [Theoretical Guarantees under Contaminated Recursive Training](https://arxiv.org/abs/2602.16065)\n- [Scaling Laws of Synthetic Data](https://arxiv.org/abs/2503.19551)\n- [Data Mixing Laws (ICLR 2025)](https://arxiv.org/abs/2403.16952)\n- [The Data-Quality Illusion](https://arxiv.org/abs/2510.00866)\n- [Min-K%++ (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)\n- [Contamination Survey (arXiv 2025)](https://arxiv.org/abs/2502.14425)\n- [RL Post-training Contamination Detection](https://arxiv.org/abs/2510.09259)\n- [LLM Data Auditor Survey](https://arxiv.org/abs/2601.17717)\n- [Reverse-Bottleneck Perspective (ICLR 2025)](https://openreview.net/forum?id=UxkznlcnHf)\n- [Synthetic Eggs in Many Baskets (ACL 2026 Findings)](https://arxiv.org/abs/2511.01490)\n- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [Rethinking Benchmark with Rephrased Samples](https://arxiv.org/abs/2311.04850)\n- [Adaptive Data Optimization](https://arxiv.org/html/2410.11820v1)\n- [Recursive Pollution vs Model Collapse (BIML)](https://berryvilleiml.com/2026/01/10/recursive-pollution-and-model-collapse-are-not-the-same/)\n- [DATAPROPHET (ICLR 2026)](https://arxiv.org/pdf/2603.19688)"
}
````

---

### Runtime record

_source line 2 · 2026-05-11T22:00:25.298Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-11T22:00:25.298Z",
  "sessionId": "3b12a614-3082-421d-b79f-1abb766e2823"
}
```

---

## Round 1

8 recorded events

### User

_source line 3 · 2026-05-11T22:00:25.336Z_

Below are research notes from a literature survey. Extract exactly 3-5 research directions from these notes.

Output ONLY a JSON array (no markdown fences, no other text). Each element:
{
  "title": "Concise English title (max 10 words)",
  "core_problem": "The fundamental research question (1-2 sentences)",
  "opportunity": "The specific gap or why now (2-3 sentences)",
  "landscape": "Current SOTA and limitations from the notes (3-5 sentences)"
}

--- RESEARCH NOTES ---
I now have extensive coverage of the landscape. Let me compile my findings into the final output.

Based on my extensive research (25+ targeted searches, 4 deep paper reads), here is my synthesis of the landscape and proposed research directions.

**Key landscape observations:**
- Model collapse is well-theorized (ICLR 2025 Strong Collapse, ICML 2025 Collapse or Thrive, Nature 2024), but practical **detection and prevention methods** during training remain scarce
- Self-verification (NeurIPS 2025) and external verifiers (arXiv 2510.16657) provide theoretical guarantees but haven't been tested as **online, adaptive** training interventions
- Hierarchical contamination detection (arXiv 2511.17602) addresses semantic-level contamination but treats it as a **post-hoc audit**, not integrated into data curation pipelines
- Pluralistic reward curation (ICML 2026, arXiv 2605.07724 — 3 days ago!) proves diversity preservation through multiple rewards, but is purely theoretical with limited LLM experiments
- **Critical gap**: No existing work unifies collapse monitoring + adaptive intervention as an online training recipe with empirical validation on small LMs
- SIGMA (arXiv 2601.03385) proposes spectral monitoring but hasn't been connected to actionable data mixing decisions
- Data mixing laws (ICLR 2025) predict performance from mixture ratios but don't adapt dynamically based on collapse signals

```json
[
  {
    "title": "Entropy-Gated Adaptive Data Mixing for Collapse Prevention",
    "core_problem": "Current synthetic data mixing strategies use fixed ratios determined before training, but model collapse is a dynamic process whose onset varies by data quality and model capacity. How can we detect incipient collapse during training and dynamically adjust the synthetic-to-real data ratio in real time?",
    "opportunity": "SIGMA (arXiv 2601.03385) introduced spectral monitoring for collapse but without actionable intervention. Self-verification (NeurIPS 2025) provides theoretical guarantees but uses binary accept/reject rather than ratio adjustment. No existing method connects online collapse signals (entropy drop, spectral contraction, n-gram diversity decline) to adaptive mixing decisions. This is feasible now because small open models (Pythia-1B, OLMo-1B) enable running 3-5 generation experiments within 200 H100-hours, and the metrics (self-BLEU, n-gram entropy, embedding eigenspectrum) are computationally cheap to monitor during training.",
    "landscape": "Data Mixing Laws (ICLR 2025) predict static optimal ratios; ADO (arXiv 2410.11820) adapts domain mixtures via scaling laws but doesn't track collapse signals; 'Collapse or Thrive' (ICML 2025) establishes accumulate vs. replace theory without online intervention; Strong Model Collapse (ICLR 2025) proves collapse occurs even with vanishingly small synthetic fractions but offers no adaptive mitigation. The recent 'Curated Synthetic Data Doesn't Have to Collapse' (ICML 2026, arXiv 2605.07724) uses pluralistic rewards for diversity but is theoretical and doesn't address the online monitoring problem. The gap is a practical method that monitors collapse indicators during training and adjusts data mixing dynamically — moving from post-hoc analysis to real-time prevention."
  },
  {
    "title": "Generation-Depth-Aware Contamination Detection for Recursive Synthetic Data",
    "core_problem": "As web data becomes ~74% AI-generated (2025 estimates), training corpora inevitably contain multi-generation synthetic text (model B trained on model A's output, model C on model B's, etc.). Can we detect the generational depth of synthetic text and use this signal to filter training data before quality degradation compounds?",
    "opportunity": "Hierarchical contamination detection (arXiv 2511.17602) achieves F1=0.76 on semantic contamination but treats all synthetic data as binary (synthetic vs. real), ignoring the critical distinction between first-generation and nth-generation synthetic text. Min-K%++ (ICLR 2025) improves membership inference but doesn't address generational depth. No existing method estimates how many recursive generation steps a text has undergone, despite strong theoretical evidence (Nature 2024, ICLR 2025) that degradation accelerates with generation depth. This is newly feasible because we can construct controlled multi-generation corpora using small open models and train classifiers on generation-depth labels.",
    "landscape": "Current contamination detection operates at a binary level: synthetic vs. real. Min-K% and Min-K%++ (ICLR 2025) detect pre-training membership; ConStat detects contamination via performance gaps on rephrased samples; CoDeC uses in-context learning for contamination. The survey by Dong et al. (arXiv 2502.14425) categorizes white/gray/black-box detection without addressing generational depth. 'From Collapse to Improvement' (arXiv 2602.10531) studies iterative contamination statistically but doesn't propose detection methods. The recursive pollution concept (BIML, Jan 2026) distinguishes pollution from collapse but lacks a detection algorithm. The gap is a practical classifier or scoring function that estimates generation depth, enabling quality-aware filtering where later-generation text is downweighted more aggressively."
  },
  {
    "title": "Spectral Early-Warning System for Model Collapse with Intervention Protocols",
    "core_problem": "Model collapse is typically studied as a post-hoc phenomenon analyzed after training completes. Can we build a lightweight, real-time early-warning system that detects the spectral signatures of incipient collapse during training and triggers automated intervention (data refresh, ratio adjustment, or early stopping)?",
    "opportunity": "SIGMA (arXiv 2601.03385, Jan 2026) proposes spectral monitoring via embedding Gram matrix eigenspectra but lacks actionable intervention protocols and empirical validation on LLMs. The ecological early-warning literature (spectral EWS via eigenvalue analysis) provides mature mathematical frameworks for detecting critical transitions that have never been applied to LLM training dynamics. Entropy-Adaptive Fine-Tuning (arXiv 2601.02151) uses entropy for forgetting prevention but doesn't address collapse in recursive synthetic training. This cross-domain connection between dynamical systems early-warning theory and LLM collapse monitoring is novel and can be validated efficiently with small models (Pythia/OLMo) across 3-5 synthetic generations.",
    "landscape": "SIGMA benchmarks model collapse through spectral properties but is purely diagnostic without interventions. The 'Generalization-to-Memorization' perspective (arXiv 2509.16499) characterizes collapse as a phase transition but doesn't propose monitoring. Ecological EWS literature (Royal Society Interface 2020, Nature Scientific Reports 2019) uses eigenvalue analysis to predict critical transitions in dynamical systems — conceptually analogous but never applied to LLM training. In the RL training context, DAPO (arXiv 2503.14476) monitors entropy and reward variance for stability but doesn't address synthetic data collapse. The key gap is connecting spectral diagnostic tools to automated intervention decisions: when eigenspectrum contraction exceeds a threshold, trigger a protocol (increase real data ratio, refresh synthetic generation, or pause training)."
  },
  {
    "title": "Multi-Reward Diversity-Preserving Synthetic Data Curation Pipeline",
    "core_problem": "Synthetic data curation using a single quality metric (e.g., perplexity, reward model score) tends to select homogeneous high-scoring samples, accelerating diversity loss and collapse. Can multi-objective curation using diverse reward signals preserve distributional coverage while maintaining quality?",
    "opportunity": "The pluralistic preferences theory (ICML 2026, arXiv 2605.07724, published May 8, 2026 — 3 days ago) proves that multi-reward curation prevents collapse and converges to a Nash bargaining solution, but validation is limited to image generation (diffusion models) with only 2-5 reward functions. No empirical work has tested this framework on language model recursive training. The Data-Quality Illusion (arXiv 2510.00866) shows single-quality-classifier filtering doesn't reliably improve LM performance, motivating multi-signal approaches. DATAPROPHET (ICLR 2026) combines cross-modal metrics but targets multimodal, not recursive text generation. This is the first opportunity to empirically validate pluralistic curation theory on LLM collapse prevention, with practical implications for training pipelines.",
    "landscape": "Self-verification (NeurIPS 2025) uses internal confidence as a single curation signal; external verification (arXiv 2510.16657) proves verifier-guided selection prevents collapse but acknowledges performance eventually converges to verifier limits. Pluralistic preferences (ICML 2026) provides the theoretical framework but only for image generation. Quality-diversity-complexity surveys (arXiv 2412.02980) map the dimensions but don't propose concrete multi-reward curation algorithms for iterative training. The reverse-bottleneck framework (ICLR 2025) connects information gain to generalization but doesn't prescribe how to compute or combine multiple quality signals in practice. The gap is an empirical, practical pipeline that implements pluralistic curation for LLM synthetic data — curating with 3-5 diverse reward functions (perplexity, diversity, coherence, task-relevance, novelty) and measuring collapse prevention across iterative training generations."
  },
  {
    "title": "Contamination-Aware Benchmark Calibration via Synthetic Data Provenance",
    "core_problem": "Benchmark scores are increasingly unreliable because training data may contain synthetic paraphrases of test items that evade n-gram decontamination. Can we build a provenance-tracking system that identifies which benchmark items have semantic near-duplicates in synthetic training data and calibrate reported scores accordingly?",
    "opportunity": "Rephrased test items can boost MMLU accuracy to 85.9% while evading all standard decontamination (arXiv 2311.04850). RL post-training contamination (arXiv 2510.09259) shows GRPO amplifies contamination effects beyond SFT. The Self-Critique method detects RL-phase contamination through output entropy collapse but only works for RL-trained models. No existing method provides provenance-aware score calibration that estimates how much of a benchmark score is attributable to contamination. With the EMNLP 2026 special theme explicitly calling for work on contamination and data governance, a method that not only detects but quantifies and calibrates contamination would be highly impactful. This is feasible using embedding-based semantic similarity between training data and benchmark items with controlled contamination injection experiments.",
    "landscape": "Five detection methods are currently recognized: time-based partition, Min-K%, Time Travel, ConStat, and BIG-Bench canary. DCR (EMNLP 2025) quantifies contamination but focuses on corpus-level statistics, not item-level calibration. The comprehensive survey (arXiv 2502.14425) maps white/gray/black-box methods but notes most methods fail against paraphrased contamination. Dynamic benchmarking (LiveBench) mitigates contamination by rotating questions monthly but doesn't calibrate existing static benchmark scores. The hierarchical detection framework (arXiv 2511.17602) catches semantic-level contamination but doesn't provide calibrated score adjustments. The gap is a calibration method that takes a model's benchmark score, a measure of contamination exposure, and outputs an adjusted score — analogous to confidence intervals but for contamination uncertainty."
  }
]

Sources:
- [Model collapse in Nature](https://www.nature.com/articles/s41586-024-07566-y)
- [Is Model Collapse Inevitable? (ICLR 2025)](https://arxiv.org/abs/2404.01413)
- [Strong Model Collapse (ICLR 2025)](https://openreview.net/forum?id=et5l9qPUhm)
- [Collapse or Thrive (ICML 2025)](https://openreview.net/forum?id=Xr5iINA3zU)
- [Self-Verification Prevents Collapse (NeurIPS 2025)](https://openreview.net/forum?id=X5Hk8aMs6w)
- [Escaping Collapse via Verification](https://arxiv.org/abs/2510.16657)
- [SIGMA: Spectral Insights for Collapse](https://arxiv.org/abs/2601.03385)
- [Hierarchical Contamination Detection](https://arxiv.org/abs/2511.17602)
- [Curated Synthetic Data with Pluralistic Preferences (ICML 2026)](https://arxiv.org/abs/2605.07724)
- [From Collapse to Improvement](https://arxiv.org/abs/2602.10531)
- [Theoretical Guarantees under Contaminated Recursive Training](https://arxiv.org/abs/2602.16065)
- [Scaling Laws of Synthetic Data](https://arxiv.org/abs/2503.19551)
- [Data Mixing Laws (ICLR 2025)](https://arxiv.org/abs/2403.16952)
- [The Data-Quality Illusion](https://arxiv.org/abs/2510.00866)
- [Min-K%++ (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
- [Contamination Survey (arXiv 2025)](https://arxiv.org/abs/2502.14425)
- [RL Post-training Contamination Detection](https://arxiv.org/abs/2510.09259)
- [LLM Data Auditor Survey](https://arxiv.org/abs/2601.17717)
- [Reverse-Bottleneck Perspective (ICLR 2025)](https://openreview.net/forum?id=UxkznlcnHf)
- [Synthetic Eggs in Many Baskets (ACL 2026 Findings)](https://arxiv.org/abs/2511.01490)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [Rethinking Benchmark with Rephrased Samples](https://arxiv.org/abs/2311.04850)
- [Adaptive Data Optimization](https://arxiv.org/html/2410.11820v1)
- [Recursive Pollution vs Model Collapse (BIML)](https://berryvilleiml.com/2026/01/10/recursive-pollution-and-model-collapse-are-not-the-same/)
- [DATAPROPHET (ICLR 2026)](https://arxiv.org/pdf/2603.19688)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "3dcb0c9f-3931-4597-b19d-ccc9861cec4d",
  "type": "user",
  "uuid": "b56d8c02-66d6-4f78-a9bf-e89c2b3d6a2f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3b12a614-3082-421d-b79f-1abb766e2823",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-11T22:00:25.334Z_

```json
{
  "parentUuid": "b56d8c02-66d6-4f78-a9bf-e89c2b3d6a2f",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "ba51aee8-eb5c-431c-b86c-5d59b4a0467e",
  "timestamp": "2026-05-11T22:00:25.334Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3b12a614-3082-421d-b79f-1abb766e2823",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-11T22:00:25.334Z_

```json
{
  "parentUuid": "ba51aee8-eb5c-431c-b86c-5d59b4a0467e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "829e0a32-96e7-441c-8883-1189e0dc7f44",
  "timestamp": "2026-05-11T22:00:25.334Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3b12a614-3082-421d-b79f-1abb766e2823",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Below are research notes from a literature survey. Extract exactly 3-5 research directions from these notes.  Output ONLY a JSON array (no markdown fences, no other text). Each element: {   \"title\": \"…",
  "leafUuid": "829e0a32-96e7-441c-8883-1189e0dc7f44",
  "sessionId": "3b12a614-3082-421d-b79f-1abb766e2823"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Extracting research directions from literature survey",
  "sessionId": "3b12a614-3082-421d-b79f-1abb766e2823"
}
```

---

### Assistant

_source line 8 · 2026-05-11T22:01:14.929Z_

```json
[
  {
    "title": "Entropy-Gated Adaptive Data Mixing for Collapse Prevention",
    "core_problem": "Model collapse is a dynamic process whose onset varies by data quality and model capacity, yet current synthetic data mixing strategies use fixed ratios determined before training. How can we detect incipient collapse during training and dynamically adjust the synthetic-to-real data ratio in real time?",
    "opportunity": "SIGMA introduced spectral monitoring without actionable intervention. Self-verification provides theoretical guarantees but uses binary accept/reject rather than ratio adjustment. No existing method connects online collapse signals (entropy drop, spectral contraction, n-gram diversity decline) to adaptive mixing decisions. This is feasible now because small open models enable running multi-generation experiments affordably, and the monitoring metrics are computationally cheap.",
    "landscape": "Data Mixing Laws (ICLR 2025) predict static optimal ratios but do not adapt during training. ADO adapts domain mixtures via scaling laws but ignores collapse signals. 'Collapse or Thrive' (ICML 2025) establishes accumulate-vs-replace theory without online intervention. Strong Model Collapse (ICLR 2025) proves collapse occurs even with vanishingly small synthetic fractions but offers no adaptive mitigation. The recent pluralistic rewards work (ICML 2026) preserves diversity theoretically but does not address the online monitoring problem. The gap is a practical method that monitors collapse indicators during training and adjusts data mixing dynamically."
  },
  {
    "title": "Generation-Depth-Aware Contamination Detection for Recursive Synthetic Data",
    "core_problem": "As web data becomes predominantly AI-generated, training corpora inevitably contain multi-generation synthetic text. Can we detect the generational depth of synthetic text and use this signal to filter training data before quality degradation compounds?",
    "opportunity": "Hierarchical contamination detection achieves F1=0.76 on semantic contamination but treats all synthetic data as binary, ignoring the critical distinction between first-generation and nth-generation text. Min-K%++ improves membership inference but does not address generational depth. No existing method estimates how many recursive generation steps a text has undergone, despite strong theoretical evidence that degradation accelerates with generation depth. This is newly feasible because controlled multi-generation corpora can be constructed using small open models.",
    "landscape": "Current contamination detection operates at a binary level: synthetic vs. real. Min-K% and Min-K%++ detect pre-training membership; ConStat detects contamination via performance gaps on rephrased samples. The survey by Dong et al. categorizes detection methods without addressing generational depth. 'From Collapse to Improvement' studies iterative contamination statistically but proposes no detection methods. The recursive pollution concept (BIML) distinguishes pollution from collapse but lacks a detection algorithm. The gap is a practical classifier or scoring function that estimates generation depth, enabling quality-aware filtering where later-generation text is downweighted more aggressively."
  },
  {
    "title": "Spectral Early-Warning System for Model Collapse",
    "core_problem": "Model collapse is typically studied as a post-hoc phenomenon analyzed after training completes. Can we build a lightweight, real-time early-warning system that detects spectral signatures of incipient collapse and triggers automated intervention?",
    "opportunity": "SIGMA proposes spectral monitoring via embedding Gram matrix eigenspectra but lacks intervention protocols and LLM-scale validation. The ecological early-warning literature provides mature mathematical frameworks for detecting critical transitions via eigenvalue analysis that have never been applied to LLM training dynamics. Entropy-Adaptive Fine-Tuning uses entropy for forgetting prevention but does not address collapse in recursive synthetic training. This cross-domain connection between dynamical systems theory and LLM collapse monitoring is novel and validatable with small models.",
    "landscape": "SIGMA benchmarks collapse through spectral properties but is purely diagnostic. The generalization-to-memorization perspective characterizes collapse as a phase transition without proposing monitoring. Ecological EWS literature uses eigenvalue analysis to predict critical transitions in dynamical systems — conceptually analogous but never applied to LLM training. In RL training, DAPO monitors entropy and reward variance for stability but does not address synthetic data collapse. The key gap is connecting spectral diagnostics to automated intervention decisions: when eigenspectrum contraction exceeds a threshold, trigger a protocol such as increasing the real data ratio or refreshing synthetic generation."
  },
  {
    "title": "Multi-Reward Diversity-Preserving Synthetic Data Curation",
    "core_problem": "Synthetic data curation using a single quality metric selects homogeneous high-scoring samples, accelerating diversity loss and collapse. Can multi-objective curation using diverse reward signals preserve distributional coverage while maintaining quality?",
    "opportunity": "Pluralistic preferences theory (ICML 2026) proves that multi-reward curation prevents collapse and converges to a Nash bargaining solution, but validation is limited to image generation with only 2-5 reward functions. No empirical work has tested this framework on language model recursive training. The Data-Quality Illusion shows single-quality-classifier filtering does not reliably improve LM performance, motivating multi-signal approaches. This is the first opportunity to empirically validate pluralistic curation theory on LLM collapse prevention.",
    "landscape": "Self-verification uses internal confidence as a single curation signal; external verification proves verifier-guided selection prevents collapse but acknowledges performance converges to verifier limits. Pluralistic preferences provides the theoretical framework but only for image generation. Quality-diversity-complexity surveys map the relevant dimensions but do not propose concrete multi-reward algorithms for iterative training. The reverse-bottleneck framework connects information gain to generalization but does not prescribe how to combine multiple quality signals in practice. The gap is an empirical pipeline implementing pluralistic curation for LLM synthetic data across iterative training generations."
  },
  {
    "title": "Contamination-Aware Benchmark Score Calibration via Provenance Tracking",
    "core_problem": "Benchmark scores are increasingly unreliable because training data may contain synthetic paraphrases of test items that evade n-gram decontamination. Can we build a provenance-tracking system that identifies semantic near-duplicates and calibrates reported scores accordingly?",
    "opportunity": "Rephrased test items can boost MMLU accuracy to 85.9% while evading all standard decontamination. RL post-training contamination shows GRPO amplifies contamination effects beyond SFT. No existing method provides provenance-aware score calibration that estimates how much of a benchmark score is attributable to contamination. With EMNLP 2026 explicitly calling for work on contamination and data governance, a method that quantifies and calibrates contamination would be highly impactful.",
    "landscape": "Five detection methods are currently recognized: time-based partition, Min-K%, Time Travel, ConStat, and BIG-Bench canary. DCR quantifies contamination at the corpus level but not at item level. The comprehensive survey maps detection methods but notes most fail against paraphrased contamination. Dynamic benchmarking (LiveBench) mitigates contamination by rotating questions but does not calibrate existing static benchmarks. The hierarchical detection framework catches semantic-level contamination but does not provide calibrated score adjustments. The gap is a calibration method that takes a model's benchmark score and contamination exposure measure and outputs an adjusted score with uncertainty bounds."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "829e0a32-96e7-441c-8883-1189e0dc7f44",
  "isSidechain": false,
  "requestId": "req_011CawXuEoNt4abnePzZu2uo",
  "type": "assistant",
  "uuid": "bf073be2-c505-4c20-9d5f-a55894d4dd8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3b12a614-3082-421d-b79f-1abb766e2823",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vm1MJoGNRyX8vRDHXTpP5h",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8871,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1722,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 8871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8871
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 9_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Below are research notes from a literature survey. Extract exactly 3-5 research directions from these notes.  Output ONLY a JSON array (no markdown fences, no other text). Each element: {   \"title\": \"…",
  "leafUuid": "bf073be2-c505-4c20-9d5f-a55894d4dd8a",
  "sessionId": "3b12a614-3082-421d-b79f-1abb766e2823"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Extracting research directions from literature survey",
  "sessionId": "3b12a614-3082-421d-b79f-1abb766e2823"
}
```

---
