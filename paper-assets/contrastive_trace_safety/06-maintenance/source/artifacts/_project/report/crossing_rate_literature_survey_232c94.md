# Crossing Rate / Prediction Stability Metric — Literature Survey

**Date:** 2026-05-20  
**Purpose:** Respond to red-team concern that CR / CR-composite is a "straw man metric"  
**Method:** WebSearch + WebFetch across 5 directions, 30+ keyword combinations  

---

## 1. Direct Hits (Exact "Crossing Rate" or Equivalent in Probe/Classifier Context)

**None found.** No paper defines a metric that counts how many times a probe's binary prediction (e.g., safe vs. unsafe) changes sign/flips as one traverses transformer layers from layer 0 to layer N.

The term "crossing rate" in ML literature maps exclusively to the signal processing concept of **zero-crossing rate (ZCR)**, used in audio/speech classification, and has never been applied to probe predictions across layers.

**Searched keywords (all returned zero relevant results):**
- "crossing rate" safety probe
- "crossing rate" probing classifier
- "sign change rate" classifier prediction
- "prediction flip rate" neural network probe
- "label oscillation" hidden state probe
- "zero crossing rate" neural network predictions classification stability

---

## 2. Near Hits (Closely Related Concepts, Different Names)

### 2.1 Kaya et al., "Shallow-Deep Networks: Understanding and Mitigating Network Overthinking" (ICML 2019)
- **arXiv:** [1810.07052](https://arxiv.org/abs/1810.07052)
- **Concept:** Defines a **"confusion metric"** that measures internal disagreements across layer-attached classifiers. Quantifies divergence between intermediate predictions and the final prediction.
- **Overthinking:** When an intermediate layer produces a correct prediction but the final layer flips it to incorrect — essentially a destructive prediction flip across depth.
- **Relation to CR:** Most conceptually proximate. Their confusion metric captures cross-layer disagreement (via L1 distance), while our CR counts discrete sign changes. Both measure prediction instability across the depth axis.

### 2.2 Keoliya et al., "Stable Prediction of Adverse Events in Medical Time-Series Data" (arXiv 2025)
- **arXiv:** [2510.14286](https://arxiv.org/abs/2510.14286)
- **Concept:** Defines a **stability metric based on local Lipschitz constants** that penalizes abrupt oscillations in per-patient risk predictions: `Lc = 1/|Tc| Σ |f(x_t) - f(x_t')| / |t - t'|` where Tc pairs timestamps within c-hour windows.
- **Key finding:** "Existing methods, especially LLMs, struggle to jointly optimize accuracy and stability."
- **Relation to CR:** Measures prediction oscillation over time (temporal axis), parallel to CR measuring oscillation over layers (depth axis). Lower Lc = more stable = analogous to lower CR.

### 2.3 Miller & Blume, "Diagnostics for Individual-Level Prediction Instability in ML for Healthcare" (arXiv 2026)
- **arXiv:** [2603.00192](https://arxiv.org/abs/2603.00192)
- **Concept:** Defines **empirical Decision Flip Rate (eDFR)** — how often threshold-based clinical decisions change due to prediction variability across model instantiations.
- **Relation to CR:** eDFR counts decision flips across model re-instantiations; CR counts prediction flips across layers. Both are discrete flip-counting metrics applied to binary decisions.

### 2.4 Larsen, "The Instability of Safety" (arXiv 2025)
- **arXiv:** [2512.12066](https://arxiv.org/abs/2512.12066)
- **Concept:** Defines **Safety Stability Index (SSI)** measuring how consistently a model makes the same safety decision across sampling configurations. 18–28% of harmful prompts exhibit "decision flips." SSI drops from 0.977 to 0.942 across temperatures.
- **Relation to CR:** SSI measures behavioral stability of safety decisions; CR measures internal probe prediction stability. Both capture the "how stable is the safety judgment" question.

### 2.5 PABEE: Zhou et al., "BERT Loses Patience: Fast and Robust Inference with Early Exit" (NeurIPS 2020)
- **arXiv:** [2006.04152](https://arxiv.org/abs/2006.04152)
- **Concept:** Exits when intermediate classifier predictions **remain unchanged for a pre-defined "patience" number of consecutive layers**. Cross-layer prediction agreement is the core confidence signal.
- **Relation to CR:** PABEE's patience mechanism is the inverse of CR — it measures prediction *stability* (consecutive agreements) while CR measures *instability* (sign changes). Both operate on the same signal: whether probe predictions flip across layers.

### 2.6 Xie et al., "Calibrating Reasoning in Language Models with Internal Consistency" (NeurIPS 2024)
- **arXiv:** [2405.18711](https://arxiv.org/abs/2405.18711)
- **Concept:** Defines **"internal consistency"** as agreement of latent predictions decoded from intermediate layers with the final prediction.
- **Relation to CR:** Measures cross-layer agreement (binary), while CR counts the number of sign transitions.

### 2.7 Wildi, "Sign Accuracy, Mean-Squared Error and the Rate of Zero Crossings" (arXiv 2026)
- **arXiv:** [2601.06547](https://arxiv.org/abs/2601.06547)
- **Concept:** Econometrics framework that explicitly connects **sign accuracy** with **zero-crossing frequency** via constrained optimization. Holding time `ht(y|b) = π/arccos(ρ(y))`.
- **Relation to CR:** The mathematical framework linking sign accuracy (≈ BA) and zero-crossing rate (≈ CR) is exactly our CR-composite decomposition, but in econometrics.

### 2.8 CCE: Zhong et al., "Confidence-Consistency Evaluation for Time Series Anomaly Detection" (arXiv 2025)
- **arXiv:** [2509.01098](https://arxiv.org/abs/2509.01098)
- **Concept:** Multiplicative composite: `S_anom = Conf(E_i) × Cons(E_i)`, combining confidence and consistency.
- **Relation to CR-composite:** Closest methodological precedent for multiplicative accuracy × stability composites.

### 2.9 Hemmati et al., "Volatility in Certainty (VC)" (arXiv 2025)
- **arXiv:** [2511.11834](https://arxiv.org/abs/2511.11834)
- **Concept:** Defines VC as "the average squared log-ratio of adjacent certainty values" in sorted softmax outputs. Strong negative correlation (ρ < −0.90) between accuracy and log(VC).
- **Relation to CR:** VC measures prediction volatility; CR measures prediction sign changes. Both capture instability in classifier outputs.

---

## 3. Related but Different (Prediction Stability/Consistency, Not Crossing Rate)

### 3.1 Layer Selection Criteria Beyond Accuracy

| Paper | Venue | Criterion | Key Finding |
|-------|-------|-----------|-------------|
| Hewitt & Liang, "Designing and Interpreting Probes with Control Tasks" | EMNLP 2019 | Selectivity | Accuracy and selectivity disagree on optimal layer (ELMo layer 1 vs. 2) |
| Voita & Titov, "Information-Theoretic Probing with MDL" | EMNLP 2020 | MDL | MDL methods "are more informative and **stable** than standard probes" |
| Pimentel et al., "Pareto Probing" | EMNLP 2020 | Pareto complexity | Pareto criterion can reorder layer rankings vs. accuracy |
| Vu et al., "What Makes BERT Metrics Robust?" | COLING 2022 | Robustness | Robustness-optimal layer differs from accuracy-optimal layer |
| Choi et al., "Probe Behaviors via MI Bounds" | ICASSP 2024 | MI / linear margin | "Interpreting layer-wise accuracy can be tricky" |
| Huang, "Spectral Identifiability for Probe Geometry" | arXiv 2025 | Spectral gap | Probe stability follows phase transitions in eigengap |

### 3.2 Online/Runtime Safety Monitoring Systems

| Paper | Venue | Mechanism |
|-------|-------|-----------|
| **SafeSwitch** (Han et al.) | EMNLP 2025 Findings | Prober on internal states → activates refusal head |
| **TrajGuard** (Liu et al.) | ACL 2026 Findings | Streaming hidden-state trajectory with sliding window; states carry "stronger and more stable risk signals" |
| **HiddenGuard/Prism** (Mei et al.) | arXiv 2024 | Token-level real-time detection via intermediate hidden states |
| **ShieldHead** (Xuan et al.) | ACL 2025 Findings | Classification head parallel to LM head; <1ms latency |
| **In-Decoding Probing** (Zhao et al.) | arXiv 2026 | Surfaces latent safety signals during decoding |
| **AISA** (Song et al.) | arXiv 2026 | Spatiotemporal safety analysis + logits-level steering |
| **Beyond Linear Probes** (Oldfield et al.) | ICLR 2026 | Truncated polynomial classifiers with "safety dial" cascade |

### 3.3 Prediction Trajectory / Convergence

| Paper | Venue | Concept |
|-------|-------|---------|
| Belrose et al., "Tuned Lens" | arXiv 2023 | Per-layer prediction trajectory; notes utility for malicious input detection |
| Kongmanee, "Token Prediction Refinement" | arXiv 2025 | "Depth of prediction refinement" — layers needed to converge |
| Long et al., "When Truthful Representations Flip" | EMNLP 2025 | Representational "flips" under deceptive instructions in early-to-mid layers |
| Damirchi et al., "Truth as a Trajectory" | arXiv 2025 | Layer-wise geometric displacement distinguishes valid from spurious reasoning |
| CircuitProbe (Panuganti) | arXiv 2025 | "Stability zones" via derivative of representation change |

### 3.4 Early Prediction of Safety from CoT/Generation

| Paper | Venue | Finding |
|-------|-------|---------|
| Chan et al., "Predict Alignment Before Thinking Completes" | arXiv 2025 | Probe on CoT activations predicts safety 50 sentences ahead |
| Ashok & May, "LMs Can Predict Own Behavior" | NeurIPS 2025 | Input-token probes predict output safety; reduces jailbreaking 91% |
| David, "Temporal Predictors of Outcome" | arXiv 2025 | Correctness highly predictable after few reasoning tokens |
| Ruddell, "Silent Commitment Failure" | NIST CAISI 2026 | "Governability" = pre-commitment error detectability; 52× spike ratio between architectures |

### 3.5 Probe Reliability and Failure Modes

| Paper | Venue | Finding |
|-------|-------|---------|
| Wang et al., "False Sense of Security" | arXiv 2025 | Probes learn superficial patterns; n-gram methods achieve comparable performance |
| Ravichander et al. | NeurIPS 2022 | "Fundamental instability" of probes for concept detection |
| McGuinness et al., "Neural Chameleons" | arXiv 2025 | Models can be fine-tuned to evade activation monitors |
| Belinkov, "Probing Classifiers: Promises, Shortcomings" | CL 2022 | Comprehensive survey of probing limitations |

### 3.6 Representation Stability

| Paper | Venue | Concept |
|-------|-------|---------|
| Bali et al., "LLM Attention-Head Stability" | arXiv 2026 | Middle-layer heads are least stable yet most representationally distinct |
| Raju, "Geometric Stability" | arXiv 2026 | Stability and similarity have near-zero correlation (ρ ≈ 0.01) |
| Khanmohammadi et al., "CCPS" | arXiv 2025 | Representation stability under perturbation for calibration |
| Sadiekh et al., "Polarity-Aware Probing (PA-CCS)" | AAAI 2025 | Polar Consistency / Contradiction Index for semantic robustness |

### 3.7 Composite Safety Evaluation Frameworks

| Paper | Venue | Metric |
|-------|-------|--------|
| CUES (Alqudah et al.) | MDPI Math 2026 | `(C×U×E×S)^{1/4}` — geometric mean including stability |
| Guerin et al. | IEEE ISSRE 2022 | Safety Gain + Residual Hazard + Availability Cost |
| Teinemaa et al. | DMKD 2018 | Temporal stability for process mining classifiers |
| Sahoo et al. | ICBINB@ICLR 2026 | Safety classifier collapse: 85%→50% AUC at σ=0.02 |

### 3.8 Flipping Errors (Training Epoch Context)

| Paper | Venue | Concept |
|-------|-------|---------|
| Yan et al., "Reducing Flipping Errors in DNNs" | AAAI 2022 | Prediction flips correct→wrong across training epochs; proposes FER regularization |

---

## 4. Gap Confirmation

After searching 30+ keyword combinations across 5 directions:

**The concept of measuring how many times a probe's binary prediction crosses the decision boundary as one scans across transformer layers is genuinely novel.** No existing paper defines this specific metric.

### Why the gap exists

1. **Probing literature** (2018–2024) focused on per-layer accuracy metrics; the question "how stable is the prediction trajectory?" was not asked because probing was evaluated layer-by-layer, not as a trajectory.

2. **Early exit literature** (PABEE, CATs, etc.) uses cross-layer agreement as an *exit criterion* but never formalized it as an *evaluation metric* for probe quality.

3. **Online safety monitoring** (SafeSwitch, TrajGuard, etc.) is a very recent field (2024–2026); the first papers focus on making it work at all, not on formalizing stability metrics for the monitoring signal itself.

4. **The closest analogue** (ZCR from signal processing) is well-established in audio but the conceptual transfer to probe predictions across neural network depth has not been made.

---

## 5. Rebuttal Strategy

### If reviewer says "CR is a straw man metric you invented":

**Response A — CR addresses a documented gap:**
> CR formalizes a phenomenon already observed but not quantified in the literature. Kaya et al. (ICML 2019) identified "overthinking" — where correct intermediate predictions flip to incorrect final predictions — and proposed a confusion metric measuring internal disagreement. PABEE (NeurIPS 2020) uses cross-layer prediction agreement as an exit criterion. Our crossing rate operationalizes this same intuition as an explicit evaluation metric: how often does the probe's binary decision flip across layers?

**Response B — CR has direct analogues in other domains:**
> The concept of counting sign changes in a sequential signal has established precedent:
> - **Zero-crossing rate (ZCR)** is a standard signal processing metric (widely used in audio classification)
> - **Decision Flip Rate (eDFR)** was independently proposed by Miller & Blume (2026) for clinical prediction instability
> - **Wildi (2026)** explicitly connects sign accuracy with zero-crossing frequency in econometrics
> - **Keoliya et al. (2025)** define an oscillation-penalizing stability metric for medical time series
> 
> We transfer this well-motivated concept to the novel setting of cross-layer safety probe evaluation.

**Response C — CR fills a practical need for online safety monitoring:**
> The emerging field of online safety monitoring (SafeSwitch, EMNLP 2025; TrajGuard, ACL 2026; HiddenGuard, 2024; ShieldHead, ACL 2025) deploys probes that must make decisions at every layer or every token. A probe with high accuracy but high CR is unreliable for real-time deployment — it will oscillate between "safe" and "unsafe" across adjacent layers, making the monitoring signal noisy and the intervention policy unstable. CR captures exactly this failure mode.

**Response D — CR-composite has methodological precedent:**
> Multiplicative composites of accuracy and stability have been independently proposed:
> - CCE (Zhong et al., 2025): `S = Conf × Cons` for anomaly detection
> - CUES (Alqudah et al., 2026): geometric mean of accuracy, calibration, equity, and stability
> - Keoliya et al. (2025): document that "existing methods struggle to jointly optimize accuracy and stability"
> 
> CR-composite (BA × (1−CR)) follows this established pattern.

### Recommended framing in paper:

Rather than claiming CR is a metric others already use, frame it as:

1. **A formalization of an observed phenomenon** (overthinking, cross-layer disagreement) that lacked a dedicated metric
2. **A natural metric for the online monitoring setting** — where prediction trajectory stability is operationally critical
3. **An instance of a broader pattern** (ZCR, eDFR, Lipschitz stability) applied to a new domain

### Key citations to add:

| Citation | Purpose |
|----------|---------|
| Kaya et al. (ICML 2019) | Overthinking + confusion metric = prior recognition of cross-layer prediction instability |
| Zhou et al. / PABEE (NeurIPS 2020) | Cross-layer prediction agreement as a practically useful signal |
| Keoliya et al. (arXiv 2025) | Accuracy-stability joint optimization difficulty; oscillation-penalizing metric |
| Miller & Blume (arXiv 2026) | Decision Flip Rate as a flip-counting instability diagnostic |
| Larsen (arXiv 2025) | Safety Stability Index; 18–28% of prompts exhibit decision flips |
| SafeSwitch (EMNLP 2025) | Online safety monitoring = the deployment context where CR matters |
| TrajGuard (ACL 2026) | Hidden-state trajectories carry "more stable risk signals" |
| Wildi (arXiv 2026) | Sign accuracy ↔ zero-crossing rate connection in optimization |

---

## 6. Search Coverage Log

| Direction | Keywords Searched | Papers Examined | Verified via WebFetch |
|-----------|------------------|-----------------|----------------------|
| 1. CR / sign change in probes | 7 combinations | ~20 | 8 |
| 2. Composite metrics | 7 combinations | ~22 | 6 |
| 3. SafeSwitch / online safety | 8 combinations | ~25 | 10 |
| 4. Layer selection stability | 7 combinations | ~20 | 8 |
| 5. Temporal consistency | 8 combinations | ~20 | 7 |
| Extra: ZCR, overthinking, FER | 5 combinations | ~10 | 4 |
| **Total** | **42 combinations** | **~117 papers** | **43 verified** |
