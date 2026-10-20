# Missing References Analysis

Reviewer-suggested citations evaluated for relevance to our work on phase-modulated compound sparsity severity in importance-based KV cache eviction.

---

## 1. RLKV — Which Heads Matter for Reasoning? RL-Guided KV Cache Compression

**Full citation:**
Wenjie Du, Li Jiang, Keda Tao, Xue Liu, Huan Wang. "Which Heads Matter for Reasoning? RL-Guided KV Cache Compression." arXiv:2510.08525, October 2025 (revised January 2026). Submitted to ICLR 2026.

**Core contribution:**
Proposes RLKV, which uses reinforcement learning as a probe to discover which attention heads are critical for reasoning quality. Instead of uniformly compressing all heads, RLKV allocates full KV cache to reasoning-critical heads while aggressively compressing others. Achieves 20–50% cache reduction with minimal reasoning degradation and up to 1.21× speedup.

**Method overview:**
- RL agent directly optimizes the mapping from per-head cache budget to downstream reasoning accuracy
- Head-level granularity: binary decision of full-cache vs. compressed per head
- Trained on actual generation outcomes rather than proxy metrics (attention scores, etc.)

**Relevance to our paper:**

| Dimension | Overlap? | Notes |
|-----------|----------|-------|
| Compound interaction / multi-axis | Partial | Operates at head level (a form of structured sparsity allocation), but does not study compound interaction between eviction axes |
| Phase-dependent / temporal effects | No | No analysis of how reasoning phases affect optimal head selection |
| Importance-based eviction | Yes | Core mechanism—learns importance via RL rather than heuristics |
| Distinction from our work | — | RLKV learns *which* heads to compress; we analyze *how* compound sparsity severity varies across reasoning phases for a given importance metric. RLKV is a method; our work is an analytical framework characterizing compound interaction patterns |

**Citation recommendation:**
- **Section:** Related Work → KV Cache Eviction Methods (or Importance-Based Eviction)
- **Context:** "Recent work has also explored learned eviction policies. RLKV (Du et al., 2025) uses reinforcement learning to identify reasoning-critical attention heads and selectively preserve their KV caches, demonstrating that head-level importance varies significantly for reasoning tasks. Our work complements this line by analyzing how compound sparsity interactions exhibit phase-dependent patterns across the reasoning process."

---

## 2. LongFlow — Efficient KV Cache Compression for Reasoning Models

**Full citation:**
Yi Su, Zhenxu Tian, Dan Qiao, Yuechi Zhou, Juntao Li, Min Zhang. "LongFlow: Efficient KV Cache Compression for Reasoning Models." arXiv:2603.11504, March 2026. (ICLR 2026 submission, withdrawn.)

**Core contribution:**
Addresses the specific challenge that reasoning models (e.g., DeepSeek-R1, OpenAI-o1) generate substantially longer output sequences, requiring efficient KV cache management during long generation rather than long-input scenarios. Proposes an importance estimation metric derived from an intermediate result of attention computation (using only the current query), requiring no auxiliary storage.

**Method overview:**
- LongFlowScore: importance metric extracted from the intermediate QK^T product during standard attention, before softmax normalization
- Custom CUDA kernel fusing FlashAttention + importance estimation + token eviction into a single operator
- Designed for long-output (reasoning) rather than long-input scenarios
- Achieves 11.8× throughput improvement at 80% KV cache compression

**Relevance to our paper:**

| Dimension | Overlap? | Notes |
|-----------|----------|-------|
| Compound interaction / multi-axis | No | Single-axis eviction (token-level importance), no compound analysis |
| Phase-dependent / temporal effects | Indirect | Implicitly addresses temporal growth of KV cache during long reasoning outputs, but does not analyze phase-dependent behavior |
| Importance-based eviction | Yes | Core mechanism—proposes a new importance metric |
| Distinction from our work | — | LongFlow is a systems-level optimization for efficient importance-based eviction during long generation. Our work analyzes the compound interaction patterns and phase dependence of such eviction methods. LongFlow could serve as an efficient implementation substrate for the importance metrics we study |

**Citation recommendation:**
- **Section:** Related Work → KV Cache Compression for Reasoning Models
- **Context:** "LongFlow (Su et al., 2026) specifically targets the long-output setting of reasoning models, proposing an efficient importance metric derived from attention intermediates. While their focus is on system-level throughput, our analysis reveals that the effectiveness of such importance-based eviction exhibits phase-dependent compound interactions that are not captured by aggregate metrics."

---

## 3. PM-KVQ — Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs

**Full citation:**
Tengxuan Liu, Shiyao Li, Jiayi Yang, Tianchen Zhao, Feng Zhou, Xiaohui Song, Guohao Dai, Shengen Yan, Huazhong Yang, Yu Wang. "PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs." arXiv:2505.18610, May 2025. **ICLR 2026 Poster (Accepted).**

**Core contribution:**
Addresses the observation that directly quantizing KV cache to low bit-widths causes severe degradation in long-CoT reasoning models due to cumulative error. Proposes progressive quantization: tokens start at 16-bit and are gradually reduced to 2-bit as memory fills, combined with block-wise mixed-precision allocation. Achieves up to 8% improvement over SOTA baselines under same memory budget and 2.73–5.18× throughput.

**Method overview:**
- Progressive quantization: new KV entries stored at 16-bit, older entries progressively shifted to lower precision (16→8→4→2 bit) via shifting operations
- Block-wise memory allocation: assigns higher bit-width to more sensitive transformer blocks
- Calibration with positional interpolation: uses short-context calibration data + positional interpolation to approximate long-context distributions
- Targets long-CoT reasoning models specifically (7B–70B)

**Relevance to our paper:**

| Dimension | Overlap? | Notes |
|-----------|----------|-------|
| Compound interaction / multi-axis | **Yes** | Combines temporal progression (age-based precision reduction) with structural allocation (block-wise sensitivity), creating a multi-axis compression scheme |
| Phase-dependent / temporal effects | **Yes (implicit)** | Progressive bit-width reduction is inherently temporal—older tokens get more aggressively compressed. This creates a de facto phase-dependent compression that interacts with reasoning stages, though PM-KVQ does not explicitly analyze reasoning phases |
| Importance-based eviction | Partial | Block-wise sensitivity is a form of structural importance; token-level importance is implicit via age (older = less important assumption) |
| Distinction from our work | — | PM-KVQ operates on the **quantization** axis rather than eviction, and its "progressive" strategy is operationally temporal but not analytically tied to reasoning phases. Our work explicitly characterizes phase-dependent compound interactions in the eviction axis. PM-KVQ's finding that cumulative error worsens with direct low-bit quantization is consistent with our compound severity analysis |

**Citation recommendation:**
- **Section:** Related Work → Compound KV Cache Compression (or Multi-Axis Compression)
- **Context:** "PM-KVQ (Liu et al., 2025) demonstrates that progressive quantization—gradually reducing bit-width over the generation process—mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity. This resonates with our finding that compound sparsity severity exhibits phase-dependent patterns: both works suggest that treating compression as temporally uniform is suboptimal for reasoning tasks. While PM-KVQ addresses the quantization axis, our analysis focuses on the eviction axis and explicitly characterizes the phase-gated compound interaction."
- **Also consider:** Discussion section, when arguing that phase-dependent effects generalize beyond eviction to other compression axes.

---

## 综合评估

### 相关性排序

1. **PM-KVQ** (最相关) — ICLR 2026 accepted poster。与本文在两个核心维度有交叉：compound/multi-axis compression 和 temporal/phase-dependent effects。PM-KVQ 的 progressive quantization 本质上是一种 temporally-varying compression，其 cumulative error 发现与我们的 compound severity 分析互补。**必须引用。**

2. **RLKV** (中等相关) — 使用 RL 学习 importance-based head-level eviction，与我们的 importance-based eviction 分析在方法论上相关，但未涉及 compound interaction 或 phase dependence。作为 learned importance 方向的代表性工作值得引用。

3. **LongFlow** (一般相关) — 针对 reasoning model 的 KV cache compression，与我们共享 reasoning + importance-based eviction 的问题设定，但专注于系统效率优化，无 compound 或 phase 分析。作为 reasoning-specific KV cache 工作的近期代表可以引用，但已从 ICLR 2026 撤稿，引用时标注为 arXiv preprint。

### 注意事项

- **RLKV** 的正式论文标题是 "Which Heads Matter for Reasoning?"，RLKV 是其提出的方法名。引用时应使用完整标题。
- **LongFlow** 已从 ICLR 2026 撤稿，引用时标注为 arXiv preprint。
- **PM-KVQ** 是 ICLR 2026 accepted poster，引用权重最高，且与本文最相关。
