We thank Reviewer Tgs4 for the detailed evaluation, and especially for recognizing the controlled experimental design and boundary analyses as strengths.

**Datasets & Software Scores (1/1)**

We respectfully note that code and data are publicly available at the anonymous repository linked in our abstract footnote (anonymous.4open.science/r/persuasion_turn_jailbreak_detect-C207). This includes all training/evaluation code and data generation scripts. Reviewer 2wSm identified this link and **scored Datasets=4, Software=4**. We kindly request reconsideration.

**W1 & W2: Human validation and synthetic data dependence**

We agree that human-authored multi-turn validation would strengthen external validity. However, no public multi-turn human jailbreak dataset currently exists (noted in the Limitations section). ToxicChat is the strongest available human benchmark.

The ToxicChat reversal is a deliberate finding of our controlled study, not an oversight. The paper explicitly frames it as "condition-specific" in the Abstract ("these advantages reverse on human-authored data"), Discussion (Sec. 5, Figure 4), and Conclusion. Discovering such boundary conditions is precisely the purpose of a controlled ablation.

Regarding single-generator concerns, we provide new evidence decomposing data quantity from distributional heterogeneity:

| Condition | DD OOD F1 | AA OOD F1 |
|-----------|-----------|-----------|
| 350 Qwen-only | 0.997$\pm$0.005 | 0.972$\pm$0.026 |
| 250+250 mixed (Qwen+Llama) | 0.818$\pm$0.096 | 0.504$\pm$0.107 |
| 350+350 mixed (Qwen+Llama) | 0.944$\pm$0.007 | 0.709$\pm$0.085 |

Increasing per-source data from 250$\to$350 recovers AA from 0.504 to 0.709 (**+20.5pp, 44% of gap**); the remaining 56% is distributional heterogeneity. Classification DAPT remains the only variant substantially above vanilla under mixed-LLM training -- MLM collapses to vanilla level (0.289$\pm$0.101 vs vanilla 0.291$\pm$0.065).

Same-architecture scaling (DeBERTa-v3 base$\to$large, 184M$\to$304M) shows DAPT improves both DD (+10pp: 0.898$\to$0.997) and AA (+13pp: 0.870$\to$1.000), confirming the 355M reversal in Table 4 is **RoBERTa-specific rather than a general scaling phenomenon**.

**W3: Baselines**

Our contribution is the controlled decomposition, not the pipeline (Introduction: "the contribution is the decomposition, not the pipeline"). For baselines:
- Vanilla DeBERTa+BiGRU is architecturally equivalent to DeepContext (Sec. 4 Setup), differing only in encoder choice -- this is our primary baseline.
- DeepContext, BIID, and G-Guard lack public implementations (Appendix Q), precluding direct comparison.
- We compare against TF-IDF, GPT-5.5 LLM-as-judge (Appendix A), and Llama Guard 3 (Table 3).

We acknowledge that a simplified reimplementation of one conversation-level method would complement the comparison. We will add a DeepContext-equivalent control (BERT-base+BiGRU) in the camera-ready version; preliminary results in Appendix Q already confirm that DAPT, not encoder architecture, drives the effect.

**W4: Temporal modeling**

The finding that mean pooling matches BiGRU (F1 gap $\leq$1pp, Sec. 4.3) is a deliberate contribution: it shows detection relies on per-turn content rather than sequential patterns. We retain BiGRU for its amenability to representation analysis (CKA, t-SNE), as stated in Sec. 3.3. This finding is practically valuable -- practitioners can choose simpler aggregation without sacrificing detection.

**Comments: Novelty**

We respectfully note that the value lies in the systematic disentanglement of five factors simultaneously in a safety-critical domain. The scrambled-label equivalence on template attacks but not strategy-diverse attacks (TOST |d|$\leq$0.14 vs d=0.44), and the complete hierarchy reversal on human data, are non-obvious interaction effects that controlled study reveals but intuition does not predict. No prior work has performed this decomposition for multi-turn safety.
