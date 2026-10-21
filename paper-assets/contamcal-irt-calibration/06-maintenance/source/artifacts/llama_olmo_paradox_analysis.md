# LLaMA-3.1-8B vs OLMo-2-7B Baseline Paradox: Moderating Factor Analysis

**Context**: Both models share near-identical d000 MMLU baselines (53.50% vs 53.79%) but exhibit opposite contamination dose-response patterns:
- **LLaMA-3.1-8B**: Immune (Δacc = −0.69pp, CI crosses zero)
- **OLMo-2-7B**: Benefit (Δacc = +3.2pp at s42; cross-seed sensitive: s123 −0.6pp, s0 +1.4pp)

---

## Moderating Factor Comparison Table

| Factor | LLaMA-3.1-8B | OLMo-2-7B | Explanatory Power |
|--------|-------------|-----------|-------------------|
| **Parameters** | 8.0B | 6.9B | Weak — ~1B gap, unlikely decisive |
| **Layers / Hidden dim** | 32 / 4096 | 32 / 4096 | None — identical |
| **Attention** | GQA (32 heads, 8 KV) | GQA (32 heads, 8 KV) | None — identical |
| **Positional encoding** | RoPE (θ=500K) | RoPE (θ=500K) | None — identical |
| **Activation** | SwiGLU | SwiGLU | None — identical |
| **Normalization** | RMSNorm **pre-norm** | RMSNorm **post-norm** | Moderate — may affect SFT sensitivity |
| **Vocab size** | 128,256 (tiktoken BPE) | ~100K (cl100k-based) | Weak |
| **Context length** | 128K | 4,096 | None — irrelevant for MCQ eval |
| **Pre-training tokens** | **~15T** | **~4T** | **Strong — 3.75× gap** |
| **Data composition** | 50% general, 25% math/reasoning, 17% code, 8% multilingual | DCLM + Dolma + Starcoder + ProofPile II | Moderate — LLaMA has explicit QA/reasoning data |
| **Training curriculum** | Single-stage | **Two-stage** (3.9T pre-train + 843B Dolmino annealing) | Moderate — annealing preserves plasticity |
| **Data transparency** | Closed | Fully open | Cannot audit LLaMA for benchmark exposure |
| **Decontamination** | Undisclosed (LLaMA-2 used 8-gram; 3.1 likely stronger) | 10% n-gram overlap removal from FLAN in Dolma | Both applied, LLaMA method unknown |
| **Published pretrained MMLU** | ~66.7% (5-shot) | ~63.7% (5-shot) | Informational — LLaMA ~3pp higher before any SFT |

---

## Factor Analysis

### 1. Pre-training Data Volume (Primary Factor) ★★★

LLaMA-3.1 was trained on ~15T tokens; OLMo-2 on ~4T. The 3.75× gap is the single largest asymmetry. Both exceed Chinchilla-optimal by large margins (LLaMA ~94×, OLMo-2 ~29× for their respective sizes), but LLaMA is far more over-trained.

Yang et al. (2024, "How Much Can We Forget about Data Contamination?") show contamination effects diminish when training scales beyond ~5× Chinchilla-optimal. LLaMA's extreme over-training produces more consolidated representations that settle into deeper loss basins. LoRA's low-rank perturbation (r=16, ~0.5% of parameters) is insufficient to shift these entrenched representations, yielding Immune. OLMo-2's shorter training leaves shallower loss basins with more residual plasticity, allowing the same LoRA signal to meaningfully redirect behavior.

This also explains OLMo-2's cross-seed sensitivity (s42: +3.2pp, s123: −0.6pp): a model with high plasticity is more sensitive to the specific training examples included, hence more seed-variant.

### 2. Pre-existing Benchmark Format Exposure ★★☆

LLaMA-3.1's composition explicitly includes 25% math/reasoning tokens. At 15T tokens, the probability of having encountered MMLU-style MCQ formats from web crawl data is high — even after decontamination of exact matches, format familiarity and topic coverage would make SFT contamination redundant.

OLMo-2's data (DCLM + Dolma + Starcoder + ProofPile II) is dominated by web text and code with explicit decontamination. The SFT contamination injection may provide genuinely novel format-aligned exposure.

**Caveat**: If LLaMA already "knew" MMLU formats, its pretrained baseline should be substantially higher. Both converge to ~53.5% after our SFT protocol, suggesting the evaluation format (0-shot chat-style) equalizes them. The pre-existing exposure argument is plausible but unfalsifiable without access to LLaMA's training data.

### 3. Two-Stage Training Curriculum ★★☆

OLMo-2 uniquely uses a two-stage curriculum: 3.9T tokens of main pre-training followed by 843B tokens of curated Dolmino-Mix annealing (academic content, Q&A forums, instruction data, math workbooks). This late-stage curriculum explicitly optimizes the model's capacity to absorb domain-specific knowledge through continued training — architecturally priming it for post-hoc adaptation via LoRA SFT.

LLaMA-3.1 uses single-stage training optimized for its training distribution but not specifically for post-hoc adaptation. The annealing stage may be a hidden moderator that makes OLMo-2 more receptive to SFT-injected contamination.

### 4. Normalization: Post-norm vs Pre-norm ★★☆

OLMo-2 uses **post-norm** (RMSNorm on layer outputs); LLaMA uses the standard **pre-norm** (RMSNorm on layer inputs). This is the most salient architectural difference between two otherwise near-identical transformer designs.

Post-norm has been shown to improve downstream fine-tuning dynamics (Xiong et al., 2020) but may also increase sensitivity to fine-tuning perturbations. In post-norm transformers, gradient flow through residual connections is less dampened, potentially allowing SFT-injected signals to propagate more effectively. This could contribute to OLMo-2's greater responsiveness to contamination injection.

**Caveat**: Isolating this effect would require controlled ablation (same model with pre- vs post-norm). Speculative but architecturally grounded.

### 5. Tokenizer Vocabulary ★☆☆

LLaMA uses 128,256 tokens vs OLMo-2's ~100K (cl100k-based). Both are large vocabularies derived from tiktoken/BPE. MCQ answer tokens (A/B/C/D) are handled straightforwardly by both. Unlikely to explain a ~4pp differential.

---

## Most Likely Explanation

The paradox is best explained by **differential representation robustness driven by pre-training data volume** (Factor 1), reinforced by OLMo-2's **two-stage training curriculum** (Factor 3) that preserves fine-tuning plasticity, and potentially amplified by **post-norm architecture** (Factor 4) that increases gradient flow during SFT.

LLaMA-3.1's 15T-token training creates representations resistant to the ~14K contaminated SFT examples in our d100 treatment. OLMo-2's 4T-token training plus late-stage annealing leaves the model structurally primed for post-hoc adaptation, making it responsive to contamination-carrying SFT. The convergence at d000 (~53.5%) reflects our SFT protocol creating a common evaluation baseline, but the underlying representation robustness reasserts itself when contaminated content is introduced.

---

## Discussion Paragraph Draft (English, for paper)

> The LLaMA-3.1-8B validation reveals that baseline ability alone does not determine contamination vulnerability: despite matching OLMo-2-7B's d000 MMLU accuracy (53.50\% vs.\ 53.79\%), LLaMA-3.1 exhibits Immune rather than Benefit behavior. We attribute this divergence primarily to differential representation robustness shaped by pre-training scale---LLaMA-3.1 was trained on approximately 15 trillion tokens compared to OLMo-2's 4 trillion, producing knowledge representations that are more resistant to perturbation by the relatively small contamination signal introduced through SFT ($\sim$14K items at d100). This interpretation aligns with evidence that contamination effects diminish at extreme over-training ratios \citep{yang2024forgetting}, and with OLMo-2's pronounced cross-seed sensitivity ($+$3.2pp at s42 vs.\ $-$0.6pp at s123), consistent with the higher plasticity expected from shorter pre-training. Secondary factors---including OLMo-2's two-stage training curriculum with late-stage data annealing and its use of post-normalization versus LLaMA-3.1's pre-normalization---may further modulate fine-tuning receptivity, though isolating these effects would require controlled ablation.

---

*Sources: Meta LLaMA 3.1 technical report; OLMo 2 paper (arXiv:2501.00656); Yang et al. 2024 (arXiv:2410.03249); project memory.md; train_sft.py LoRA config.*
