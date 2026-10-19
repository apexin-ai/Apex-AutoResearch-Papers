We thank Reviewer 2wSm for the thorough review and for recognizing the rigor of the controlled experiments, broad scope, and statistical methodology.

**W1: Single generator (Qwen3-8B)**

We agree that multi-generator training would strengthen generalizability claims. We provide new evidence decomposing data quantity from distributional heterogeneity using mixed Qwen+Llama training:

| Condition | DD OOD F1 | AA OOD F1 |
|-----------|-----------|-----------|
| 350 Qwen-only | 0.997$\pm$0.005 | 0.972$\pm$0.026 |
| 250+250 mixed (Qwen+Llama) | 0.818$\pm$0.096 | 0.504$\pm$0.107 |
| 350+350 mixed (Qwen+Llama) | 0.944$\pm$0.007 | 0.709$\pm$0.085 |

Data quantity accounts for **44% of the gap and distributional heterogeneity for 56%**. Classification DAPT remains the only variant substantially outperforming vanilla under mixed-LLM training (MLM collapses to vanilla level: 0.289$\pm$0.101). This confirms that the classification objective's advantage is not an artifact of single-source homogeneity.

Additionally, same-architecture scaling (DeBERTa-v3-large, 304M) shows DAPT improves DD by +10pp and AA by +13pp over vanilla, confirming the effect is not scale-limited within the DeBERTa family.

**W2: ToxicChat reversal and applicability scope**

The paper explicitly discusses the impact of this reversal on applicability scope. The Abstract states "these advantages reverse on human-authored data, an asymmetry that bounds the scope of each mechanism." Discussion Sec. 5 and Conclusion both frame the hierarchy as condition-specific. This is a deliberate boundary finding of our controlled study.

We note that despite the ranking reversal, all jailbreak-domain DAPT variants improve over vanilla by **18-42pp on ToxicChat** (Table 5), confirming that domain adaptation transfers to human-written attacks. The advantage of classification over MLM is condition-specific; the advantage of domain adaptation over vanilla is consistent.

No multi-turn human jailbreak dataset currently exists (the Limitations section), making ToxicChat the strongest available human validation.

**W3: Small training set (250+250)**

The 350-sample training set (from 250+250 split into 350 train / 74 val / 76 test) is a scope constraint rather than a methodological limitation. Appendix J validates that the evidence hierarchy is preserved at larger scale (1000 conversations). The mixed-LLM experiment above (350+350) further shows consistent patterns at increased data volume.

We will add a brief discussion of training set size sensitivity in the camera-ready version to make the scope boundary more explicit.

**Comments: Typesetting**

We will refine the two-column typesetting to reduce isolated word fragments in the camera-ready version. We appreciate this attention to presentation quality.
