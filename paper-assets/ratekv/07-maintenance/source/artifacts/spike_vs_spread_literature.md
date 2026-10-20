# Literature Survey: KV Cache Heterogeneity Distribution Shape (Spike vs Spread)

**Date**: 2026-05-14
**Context**: RateKV project — per-KV-head non-uniform bit-width allocation via constrained MCKP solver. Core finding: sensitivity heterogeneity distribution shape (spike vs spread) determines MCKP allocator effectiveness, not GQA ratio.

---

## 1. Direct Competitors (Per-Head Mixed-Precision KV Cache Quantization)

### 1.1 RateQuant (2026)
- **Title**: RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory
- **Authors**: (arXiv:2605.06675)
- **Venue**: arXiv preprint, May 2026
- **Category**: **Direct competitor**
- **Summary**: First to apply rate-distortion theory to per-head KV cache bit allocation. Uses reverse waterfilling for closed-form allocation. Fits per-quantizer distortion model D(b)=α·β^{-b}, with β varying 3.6–5.3 across quantizers. Key metric: AM/GM ratio of head sensitivities predicts achievable distortion reduction without any quantization. Gradient-based importance yields 1.07 PPL improvement over activation-based at 3.5 bits.
- **Results**: On Qwen3-8B at 2.5 bits, reduces KIVI PPL from 49.3 to 14.9 (70% reduction). On TurboQuant at 4.0 bits, recovers 66% of quantization-induced degradation.
- **Relation to our work**: **Closest competitor**. RateQuant uses AM/GM ratio as a scalar heterogeneity metric but does NOT analyze the distribution *shape* (spike vs spread). Their AM/GM captures heterogeneity magnitude, not whether it comes from one extreme outlier (spike) or a distributed cluster (spread). Our contribution: explaining *why* some models benefit from non-uniform allocation and others don't, through distribution shape analysis. RateQuant would predict benefit whenever AM/GM > 1 but cannot explain the Yi-1.5 failure case (high AM/GM from spike pattern, yet negative returns).

### 1.2 KVTuner (2025)
- **Title**: KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference
- **Authors**: Li et al.
- **Venue**: ICML 2025
- **Category**: **Direct competitor** (layer-level, not head-level)
- **Summary**: Uses Pareto search over hardware-friendly layer-wise K/V precision pairs. Achieves nearly lossless 3.25-bit for Llama-3.1-8B, 4.0-bit for Qwen2.5-7B. Gradient-based sensitivity shows U-shaped pattern (early+late layers sensitive); activation-based is monotonically increasing.
- **Relation to our work**: Operates at layer granularity, not head granularity. Does not analyze within-layer head heterogeneity distribution shape. Notes that Qwen2.5-7B requires higher precision → consistent with our finding of Qwen's spread pattern requiring differentiated allocation.

### 1.3 PM-KVQ (2025)
- **Title**: PM-KVQ: Progressive Mixed-Precision KV Cache Quantization for Long-CoT LLMs
- **Authors**: Chen et al.
- **Venue**: arXiv:2505.18610
- **Category**: **Method component**
- **Summary**: Progressive quantization strategy that gradually lowers bit-width over decoding steps. Block-wise memory allocation assigns higher bits to sensitive transformer blocks. Uses integer programming for allocation.
- **Relation to our work**: Temporal dimension (progressive) is orthogonal to our spatial (per-head) analysis. Does not analyze head-level heterogeneity distribution shapes.

### 1.4 MixKVQ (2025)
- **Title**: MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning
- **Authors**: (arXiv:2512.19206)
- **Venue**: arXiv, Dec 2025
- **Category**: **Method component**
- **Summary**: Query-aware algorithm identifies critical key channels needing higher precision. Combines intrinsic quantization difficulty with query relevance. Per-channel mixed precision for keys, per-token for values.
- **Relation to our work**: Operates at channel granularity within heads, not across heads. The "intrinsic quantization difficulty" concept relates to sensitivity heterogeneity but is measured per-channel, not per-head.

### 1.5 KVmix (2025)
- **Title**: KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache
- **Authors**: (arXiv:2506.08018; AAAI 2026)
- **Venue**: AAAI 2026
- **Category**: **Direct competitor** (layer-level)
- **Summary**: Gradient-based importance analysis for layer-specific K/V bit-width allocation. Achieves K 2.19-bit / V 2.38-bit with 4.9× compression. Introduces dynamic long-context optimization for recent pivotal tokens.
- **Relation to our work**: Layer-level, not head-level. Confirms K/V asymmetric sensitivity (consistent with our K/V separation findings).

---

## 2. Spike vs Spread / Outlier Pattern Analysis

### 2.1 "Precision Where It Matters" — Spike-Aware Quantization (2025)
- **Title**: Precision Where It Matters: A Novel Spike Aware Mixed-Precision Quantization Strategy for LLaMA-based Language Models
- **Authors**: (arXiv:2504.21553)
- **Venue**: Springer, April 2025
- **Category**: **Background — spike pattern in activations (not heads)**
- **Summary**: Identifies activation spikes concentrated in down projections of exactly 2 layers (one early, one late) in LLaMA. Spikes reach values up to 2500. Solution: FP8 for spiking layers, INT8 for rest. 30+ PPL reduction on LLaMA3-8B.
- **Relation to our work**: Uses "spike" terminology for activation outliers, not head sensitivity distribution. The spike/spread dichotomy is analogous but operates at a different level (activation magnitude within layers vs. sensitivity distribution across heads). Supports the broader idea that spike-like concentration has different optimization implications than spread-like distributions.

### 2.2 CMPQ — Channel-Wise Mixed-Precision Quantization (2024)
- **Title**: Channel-Wise Mixed-Precision Quantization for Large Language Models
- **Authors**: Chen & Xie et al.
- **Venue**: arXiv:2410.13056, Oct 2024
- **Category**: **Background — channel-level outlier patterns**
- **Summary**: Allocates precision per-channel based on activation distribution. Distinguishes activation-based outliers (persistent in specific channels) from quantization-based outliers. ~0.5% of values are outliers. Uses L2-norm per channel for allocation.
- **Relation to our work**: Channel-level analogue of our head-level analysis. The observation that outlier concentration varies by channel parallels our head-level spike vs spread finding, but at finer granularity and for weight/activation quantization, not KV cache.

### 2.3 KITTY — Dynamic Channel-wise Precision Boost (2025)
- **Title**: Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost
- **Authors**: (arXiv:2511.18643)
- **Venue**: arXiv, Nov 2025
- **Category**: **Method component**
- **Summary**: Ranks Key-cache channels by sensitivity; keeps small fraction at higher precision. "Critical channels play a disproportionately important role." Decomposes mixed-precision Key pages into two uniform 2-bit tensors for hardware efficiency.
- **Relation to our work**: Channel-level analogue within keys. The finding that "critical channels play disproportionately important roles" is consistent with our heterogeneity thesis, but KITTY does not analyze whether the critical channel distribution is spike-like or spread-like.

### 2.4 MUXQ — Low-Rank Outlier Decomposition (2026)
- **Title**: MUXQ: Mixed-to-Uniform Precision Matrix Quantization via Low-Rank Outlier Decomposition
- **Authors**: (arXiv:2604.04701)
- **Venue**: arXiv, April 2026
- **Category**: **Background**
- **Summary**: Decomposes outlier channels into a low-rank matrix to convert mixed-precision quantization into uniform precision. Applies rotation/permutation to redistribute outlier energy.
- **Relation to our work**: Addresses outliers via decomposition rather than differentiated allocation. Different philosophy: eliminate heterogeneity (smoothing) vs. exploit heterogeneity (our approach).

---

## 3. Head-Specific KV Cache Compression (Eviction-based, not Quantization)

### 3.1 HeadKV / "Not All Heads Matter" (2024)
- **Title**: Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning
- **Authors**: Fu et al.
- **Venue**: ICLR 2025 (arXiv:2410.19258)
- **Category**: **Background — head importance for eviction**
- **Summary**: Head-level KV cache budget allocation based on importance scores from Needle-in-a-Haystack probing. Retains 1.5% KV cache with 97% performance. Different heads serve retrieval vs reasoning roles.
- **Relation to our work**: Confirms head-level importance heterogeneity exists and is exploitable. Does not analyze the distribution shape of this heterogeneity. Eviction-based, not quantization-based.

### 3.2 AdaKV (2024)
- **Title**: Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation
- **Authors**: Feng et al.
- **Venue**: NeurIPS 2025 (arXiv:2407.11550)
- **Category**: **Background — adaptive head budget**
- **Summary**: Adaptive per-head budget allocation for KV eviction. Extends SnapKV/PyramidKV with head-wise adaptive allocation. Key insight: uniform compression rate across heads is a "rigidity" that hurts performance.
- **Relation to our work**: Directly supports our thesis that head-level heterogeneity matters. But AdaKV addresses eviction budgets (how many tokens to keep per head), not quantization bit-width. Does not analyze spike vs spread patterns.

### 3.3 KV-Compress (2024)
- **Title**: KV-Compress: Paged KV-Cache Compression with Variable Compression Rates per Attention Head
- **Authors**: Rehg
- **Venue**: arXiv:2410.00161, Oct 2024
- **Category**: **Background — variable-rate per-head compression**
- **Summary**: Variable compression rates across attention heads within PagedAttention framework. Proposes query-group-compression for GQA models yielding additional 4× compression. 8× compression with negligible impact on Llama-3.1.
- **Relation to our work**: Confirms per-head heterogeneity is exploitable for compression. Addresses GQA grouping explicitly. Does not analyze why some heads/models benefit more (no spike vs spread analysis).

### 3.4 PyramidKV (2024)
- **Title**: PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling
- **Authors**: Cai et al.
- **Venue**: arXiv:2406.02069
- **Category**: **Background**
- **Summary**: Attention scatters widely in lower layers, consolidates in higher layers → pyramidal budget allocation (more cache for lower layers). Layer-level, not head-level.
- **Relation to our work**: Layer-level heterogeneity analysis. Complementary perspective but no head-level distribution shape analysis.

---

## 4. GQA Ratio and Quantization Sensitivity

### 4.1 GQA Original Paper (2023)
- **Title**: GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints
- **Authors**: Ainslie et al.
- **Venue**: EMNLP 2023 (arXiv:2305.13245)
- **Category**: **Background**
- **Summary**: Proposes GQA as interpolation between MHA and MQA. Does not discuss quantization sensitivity implications of GQA ratio.
- **Relation to our work**: Foundational paper. Our finding that GQA ratio is NOT a reliable proxy for heterogeneity is novel — the original paper does not address this.

### 4.2 QCQA — Quality-and-Capacity-Aware Grouping (2025)
- **Title**: Quality- and Capacity-Aware Grouped Query Attention
- **Venue**: 2025
- **Category**: **Background — GQA grouping optimization**
- **Summary**: Evolutionary algorithm to discover optimal query-head groupings that minimize accuracy loss under KV-cache constraints. Achieves 20% higher accuracy at equal cache size vs naive GQA, or 40% KV reduction at same accuracy.
- **Relation to our work**: Addresses the grouping structure of GQA but not quantization. Supports the idea that the default GQA grouping may not be optimal, which is related to our finding about GQA ratio being a poor proxy.

---

## 5. MCKP / Constrained Optimization for Bit Allocation

### 5.1 MPQCO (2021)
- **Title**: Towards Mixed-Precision Quantization of Neural Networks via Constrained Optimization
- **Authors**: Chen, Wang, Cheng
- **Venue**: ICCV 2021
- **Category**: **Method component — MCKP formulation origin**
- **Summary**: Formulates mixed-precision quantization as MCKP. Uses second-order Taylor expansion + Hessian for sensitivity. Greedy solver. 5–10 min calibration. Principled and efficient.
- **Relation to our work**: We use the same MCKP formulation. MPQCO applies it to weight quantization layer-wise; we apply it to KV cache head-wise. MPQCO does not analyze when MCKP allocation fails (i.e., no spike vs spread analysis).

### 5.2 JointSQ (2024)
- **Title**: JointSQ: Joint Sparsification-Quantization for Distributed Learning
- **Authors**: Xie et al.
- **Venue**: CVPR 2024
- **Category**: **Background**
- **Summary**: Joint sparsity-quantization optimization via MCKP where profit = -error, weight = storage.
- **Relation to our work**: Uses MCKP but for sparsity+quantization jointly, not for KV cache head-level allocation.

---

## 6. Foundational KV Cache Quantization Methods

### 6.1 KIVI (2024)
- **Title**: KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache
- **Authors**: Liu & Yuan et al.
- **Venue**: ICML 2024 (arXiv:2402.02750)
- **Category**: **Evaluation baseline**
- **Summary**: Per-channel symmetric quantization for keys, per-token asymmetric for values. Tuning-free 2-bit. Establishes K/V asymmetry as important principle.
- **Relation to our work**: Baseline quantizer. Our MCKP allocator can sit on top of KIVI. KIVI applies uniform bit-width — our work addresses its limitation.

### 6.2 KVQuant (2024)
- **Title**: KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization
- **Authors**: (arXiv:2401.18079)
- **Venue**: NeurIPS 2024
- **Category**: **Evaluation baseline**
- **Summary**: Per-layer sensitivity-weighted non-uniform datatypes. Handles outlier channels. Extends to 3-bit and 2-bit from FlexGen's 4-bit.
- **Relation to our work**: Layer-level non-uniform datatype design, not head-level bit allocation. Pioneered per-layer sensitivity analysis for KV cache.

### 6.3 RotateKV (2025)
- **Title**: RotateKV: Accurate and Robust 2-Bit KV Cache Quantization
- **Venue**: IJCAI 2025
- **Category**: **Evaluation baseline**
- **Summary**: Outlier-aware rotation to enhance quantization adaptability across diverse outlier distributions.
- **Relation to our work**: Smoothing-based approach (eliminate heterogeneity) vs our exploitation-based approach (allocate to heterogeneity).

---

## 7. Distribution Shape Metrics

### 7.1 Mix-QViT — Layer Importance + Quantization Sensitivity (2025)
- **Title**: Mix-QViT: Mixed-Precision Vision Transformer Quantization Driven by Layer Importance and Quantization Sensitivity
- **Authors**: (arXiv:2501.06357)
- **Venue**: arXiv, Jan 2025
- **Category**: **Background — sensitivity metrics for ViTs**
- **Summary**: Dual scoring: explainability-based layer importance (via LRP) + quantization sensitivity per layer. Uses these scores for mixed-precision allocation in Vision Transformers.
- **Relation to our work**: Uses sensitivity metrics for allocation but does not analyze distribution shape. Applied to ViTs, not LLMs.

### 7.2 Representational Compactness via Singular Values
- **Category**: **Background — concentration metric**
- **Summary**: Singular value distribution as a measure of information concentration: uniform SVs → high compactness (redundant); few dominant SVs → low compactness (concentrated/sensitive).
- **Relation to our work**: SVD-based concentration measurement is related to our Gini/CV analysis of head sensitivity distributions. The "few dominant SVs" scenario parallels our "spike" pattern.

---

## 8. Novelty Assessment

### What already exists:
1. **Head-level heterogeneity is well-documented**: HeadKV, AdaKV, KV-Compress, RateQuant all confirm heads have varying importance
2. **MCKP for mixed-precision allocation**: MPQCO (2021) established the formulation; RateQuant (2026) applies rate-distortion allocation to KV cache per-head
3. **AM/GM ratio as heterogeneity scalar**: RateQuant proposes this as a predictor of allocation benefit
4. **Spike-aware quantization for activations**: "Precision Where It Matters" addresses spike patterns in activation magnitudes

### What is NOVEL in our work:
1. **Distribution shape analysis (spike vs spread)**: No prior work explicitly analyzes how the *shape* of the head sensitivity distribution determines allocation effectiveness. RateQuant's AM/GM is a scalar that captures magnitude but not shape — two distributions with identical AM/GM can have very different shapes (one spike outlier vs distributed cluster)
2. **GQA ratio ≠ heterogeneity proxy**: No prior work has shown that GQA ratio fails to predict allocation benefit. Yi-1.5-9B (highest GQA 8:1) with spike pattern yields negative returns despite high heterogeneity magnitude — this finding is absent from all surveyed papers
3. **Failure mode characterization**: Prior work reports when mixed-precision helps; we characterize *when and why it fails* (spike pattern concentrates sensitivity in a single head that cannot be further differentiated by allocation)
4. **Cross-model shape taxonomy**: Systematic classification of 5 models into spike/spread patterns with predictive power for MCKP effectiveness

### Positioning relative to RateQuant:
RateQuant is the closest competitor (same per-head granularity, similar MCKP-style allocation). Our contribution is **complementary and deeper**: RateQuant provides the allocation mechanism; we explain *when allocation mechanisms work*. RateQuant's AM/GM metric would incorrectly predict benefit for Yi-1.5-9B (high AM/GM from spike pattern). Our spike vs spread analysis provides a more informative predictor.

---

## 9. Papers to Cite (by section)

### Related Work — KV Cache Quantization
- KIVI (Liu & Yuan et al., ICML 2024)
- KVQuant (NeurIPS 2024)
- RotateKV (IJCAI 2025)
- KITTY (arXiv 2511.18643, 2025)

### Related Work — Mixed-Precision KV Cache
- KVTuner (Li et al., ICML 2025)
- KVmix (AAAI 2026)
- PM-KVQ (Chen et al., 2025)
- MixKVQ (arXiv 2512.19206, 2025)
- RateQuant (arXiv 2605.06675, 2026)

### Related Work — Head Importance Heterogeneity
- HeadKV / "Not All Heads Matter" (Fu et al., ICLR 2025)
- AdaKV (Feng et al., NeurIPS 2025)
- KV-Compress (Rehg, 2024)
- PyramidKV (Cai et al., 2024)

### Related Work — MCKP for Bit Allocation
- MPQCO (Chen et al., ICCV 2021)

### Related Work — Outlier/Spike Patterns
- "Precision Where It Matters" (arXiv 2504.21553, 2025)
- CMPQ (Chen & Xie et al., 2024)
- MUXQ (arXiv 2604.04701, 2026)

### Related Work — GQA
- GQA (Ainslie et al., EMNLP 2023)
- QCQA (2025)

---

## 10. Summary

The spike vs spread distribution shape analysis is **novel**. While head-level heterogeneity is well-documented and exploited by multiple recent methods (RateQuant, HeadKV, AdaKV), no prior work has:
1. Analyzed the *shape* of sensitivity distributions (beyond scalar metrics like AM/GM)
2. Explained why MCKP/allocation-based methods fail for certain models
3. Shown that GQA ratio is a poor proxy for allocation benefit
4. Provided a predictive taxonomy (spike → negative returns, spread → positive returns)

This positions our work as providing **diagnostic insight** that complements allocation methods like RateQuant, explaining their failure modes and suggesting when non-uniform allocation should (and should not) be applied.
