We thank Reviewer rEqM for the thoughtful review and for recognizing the controlled ablation design and the scrambled-label finding as strengths.

**Datasets & Software Scores (1/1)**

Code and data are publicly available at the anonymous repository linked in our abstract footnote (anonymous.4open.science/r/persuasion_turn_jailbreak_detect-C207), including all training code, evaluation scripts, and data generation pipelines. Reviewer 2wSm identified this and scored Datasets=4, Software=4. We kindly request reconsideration.

**W1: Synthetic data and small training set**

We agree that 350 training samples from a single generator is a scope constraint. Two new analyses address this:

(1) Data quantity vs distributional heterogeneity decomposition:

| Condition | DD OOD F1 | AA OOD F1 |
|-----------|-----------|-----------|
| 350 Qwen-only | 0.997$\pm$0.005 | 0.972$\pm$0.026 |
| 250+250 mixed (Qwen+Llama) | 0.818$\pm$0.096 | 0.504$\pm$0.107 |
| 350+350 mixed (Qwen+Llama) | 0.944$\pm$0.007 | 0.709$\pm$0.085 |

Increasing per-source data from 250$\to$350 recovers AA from 0.504 to 0.709 (+20.5pp), while distributional heterogeneity accounts for 56% of the remaining gap. Classification DAPT remains the only variant above vanilla under mixed-LLM training (MLM collapses to vanilla level: 0.289 vs 0.291).

(2) Error analysis of the mixed-LLM AA collapse (F1=0.504): failure is entirely **recall-driven (precision 97.8%, recall 29.2%)**. The model's decision boundary over-contracts -- almost no false positives, but 57/80 jailbreaks missed. Attack difficulty follows strategy diversity: FITD 0.997 > DD 0.944 > AA 0.709 (at 350+350).

Appendix J (scale validation on 1000 Qwen conversations) preserves the evidence hierarchy, confirming it is not an artifact of small sample size.

**W2: ToxicChat reversal and claim scope**

We agree the reversal warrants conservative framing. Importantly, the paper already explicitly frames this as condition-specific: Abstract ("these advantages reverse on human-authored data, an asymmetry that bounds the scope of each mechanism"), Discussion Sec. 5, and Conclusion all state this. It is a deliberate boundary finding, not a hidden limitation.

No multi-turn human jailbreak benchmark currently exists (the Limitations section). ToxicChat (real LMSYS interactions) is the strongest available human validation. Despite the reversal, all jailbreak-domain DAPT variants exceed vanilla by 18-42pp on ToxicChat (Table 5), confirming transfer to human-written attacks. The advantage is condition-specific in ranking, not in the direction of improvement.

**W3: FP under benign shift overstates deployment robustness**

The paper explicitly separates attack-side and benign-side evaluation. Table 3 caption states: "OOD F1 reflects attack-side generalization only; benign samples are IID from training distribution." The benign-side shift is treated independently in Sec. 4.8, where few-shot adaptation resolves FPR (68.1% $\to$ 0% with 10 WildChat conversations). Table 3 bottom rows report combined dual-OOD F1 (attack OOD + benign OOD): **0.855 without adaptation, 0.994 with 10-shot** -- directly addressing the concern that main OOD F1 may overstate deployment robustness.

**W4: Baselines**

Our contribution is the decomposition, not the pipeline. The vanilla DeBERTa+BiGRU baseline is architecturally equivalent to DeepContext (Sec. 4 Setup); DeepContext, BIID, and G-Guard lack public implementations (Appendix Q). We additionally compare against TF-IDF, GPT-5.5 LLM-as-judge (Appendix A), and Llama Guard 3 (Table 3, pooled recall 1.8%).

We will add a BERT-base+BiGRU control (DeepContext-equivalent) in the camera-ready version; Appendix Q already provides preliminary evidence that DAPT, not encoder architecture, drives the effect.
