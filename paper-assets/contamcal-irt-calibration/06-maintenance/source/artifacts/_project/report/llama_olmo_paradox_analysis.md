# LLaMA-3 vs OLMo-2 Baseline Paradox: Moderating Factor Analysis

**Context**: LLaMA-3.1-8B (MMLU 53.50%) and OLMo-2-7B (MMLU 53.79%) have near-identical pretrained MMLU, but opposite dose-response patterns: LLaMA-3 = Immune (Δ=-0.69pp), OLMo-2 = Benefit (Δ=+3.2pp). This note analyzes candidate moderating factors.

---

## 1. Pre-training Data Volume (Most Likely Primary Factor)

LLaMA-3.1 was trained on ~15T tokens; OLMo-2 on ~4.7T (3.9T OLMo-Mix + 843B Dolmino annealing). The 3× data gap is the single largest asymmetry between the two models. More pre-training data produces more crystallized internal representations—weights have been updated over far more gradient steps, settling into deeper loss basins. LoRA's low-rank perturbation (r=16) adds only ~0.5% trainable parameters; against LLaMA's more entrenched representations, this perturbation may be insufficient to shift benchmark-relevant capabilities, yielding the Immune pattern. OLMo-2's shallower training basin allows the same LoRA signal to meaningfully redirect model behavior.

## 2. Two-Stage Training vs Single-Stage

OLMo-2 uniquely uses a two-stage curriculum: a main pre-training phase followed by an annealing stage on Dolmino-Mix-1124 (843B tokens of curated, domain-specific data). This late-stage curriculum training explicitly optimizes the model's "plasticity"—its capacity to absorb new knowledge through continued training. A model designed to improve through late-stage data infusion is architecturally primed to benefit from LoRA SFT. LLaMA-3.1 uses standard single-stage pre-training with no annealing phase, producing a model optimized for its training distribution but not for post-hoc adaptation.

## 3. GQA vs MHA: Attention LoRA Capacity

LLaMA-3.1-8B uses Grouped-Query Attention (32 Q heads, 8 KV heads, 4:1 ratio); OLMo-2 uses full Multi-Head Attention (32/32). With LoRA applied to q/k/v/o_proj, the KV projection LoRA parameters per layer are:

- **LLaMA**: k_proj + v_proj = 2 × (4096×16 + 16×1024) = 163,840 params/layer
- **OLMo-2**: k_proj + v_proj = 2 × (4096×16 + 16×4096) = 262,144 params/layer

OLMo-2 has **60% more LoRA capacity in KV projections**, giving it greater ability to modify attention patterns for MCQ format learning. GQA compresses the key-value space for inference efficiency, but this compression also constrains LoRA's ability to reshape how the model attends to answer options.

## 4. Tokenizer Vocabulary Size

LLaMA-3.1 uses a 128K-token BPE vocabulary; OLMo-2 uses a 50K vocabulary (cl100k-derived, padded to 50,304). The 2.5× vocabulary difference has two implications: (a) LLaMA's embedding matrix is much larger (~525M params vs ~206M), but embeddings are NOT targeted by LoRA, meaning a larger fraction of LLaMA's total parameters is unreachable by fine-tuning; (b) MCQ answer tokens (A/B/C/D) and option formatting may be represented differently across tokenizers, potentially affecting how efficiently LoRA can learn the MCQ response format. However, this factor is likely secondary—both tokenizers handle single-letter options straightforwardly.

## 5. LoRA Trainable Ratio

Total LoRA parameters (r=16, all linear layers, 32 layers):
- **LLaMA-3.1-8B**: ~41.9M trainable / 8.0B total = **0.52%**
- **OLMo-2-7B**: ~40.0M trainable / 7.3B total = **0.55%**

The absolute LoRA parameter counts are similar, but OLMo-2's slightly higher ratio (0.55% vs 0.52%) combined with the attention-specific advantage (Factor 3) gives it marginally more fine-tuning leverage per total parameter.

## 6. Base Model Purity

Both models are true base (pretrained-only) checkpoints with no instruction tuning or RLHF. This rules out alignment-stage differences as a confound. The divergent dose-response is purely attributable to pre-training differences.

---

## Conclusion

The most parsimonious explanation is **pre-training data volume** (Factor 1) as the primary driver, with **two-stage training** (Factor 2) and **GQA vs MHA attention capacity** (Factor 3) as reinforcing secondary factors. LLaMA-3.1's 3× larger training corpus creates representations that are more resistant to low-rank perturbation, while OLMo-2's annealing-stage training and full MHA architecture make it structurally more receptive to LoRA adaptation.

### Suggested Discussion Phrasing

> "Despite near-identical pretrained MMLU scores (53.50% vs 53.79%), LLaMA-3.1-8B and OLMo-2-7B exhibit opposite dose-response patterns (Immune vs Benefit), demonstrating that baseline ability alone does not determine contamination susceptibility. We hypothesize that pre-training data volume (~15T vs ~4.7T tokens) is the primary moderating factor: models trained on substantially more data develop more entrenched representations that resist low-rank fine-tuning perturbation. This is further modulated by architectural differences—OLMo-2's full multi-head attention provides 60% more LoRA-targetable parameters in key-value projections compared to LLaMA-3.1's grouped-query attention, and OLMo-2's two-stage training curriculum (with late-stage data annealing) may produce representations that are more amenable to post-hoc adaptation. These findings underscore that contamination effects are jointly determined by model capacity, training history, and architectural design, rather than any single factor."

---

*Sources: Meta LLaMA 3.1 technical report; OLMo 2 paper (arXiv:2501.00656); project train_sft.py LoRA config.*
