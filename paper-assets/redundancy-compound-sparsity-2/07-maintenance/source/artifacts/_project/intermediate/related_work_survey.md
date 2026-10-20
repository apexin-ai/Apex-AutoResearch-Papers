# KV Cache Eviction: Related Work Survey

> For CARC (O(1) Recurrence-Aware KV Eviction) — EMNLP 2026 ARR submission
> Updated: 2026-05-12

---

## 1. Token-Level Eviction Methods

### H2O (Heavy Hitter Oracle)
- **Venue:** NeurIPS 2023
- **Paper:** [arXiv:2306.14048](https://arxiv.org/abs/2306.14048)
- **Core mechanism:** Identifies "heavy hitter" tokens that accumulate high attention scores across decoding steps. Maintains a dynamic balance of recent tokens + heavy hitters in the KV cache, formulated as a dynamic submodular optimization.
- **Signal type:** Attention-score (cumulative)
- **Complexity:** O(N) per step — maintain running attention score sums, select top-k
- **Training-free:** Yes
- **Code:** [github.com/FMInference/H2O](https://github.com/FMInference/H2O)
- **与 CARC 区别:** H2O uses per-token attention accumulation; CARC uses EMA centroid similarity as a geometric redundancy signal, avoiding attention score dependency.

### Scissorhands
- **Venue:** NeurIPS 2023
- **Paper:** [arXiv:2305.17118](https://arxiv.org/abs/2305.17118)
- **Core mechanism:** "Persistence of Importance" hypothesis — tokens important at one step remain important in future steps. Stores pivotal tokens with higher probability, achieving up to 5× KV cache reduction.
- **Signal type:** Attention-score (historical persistence)
- **Complexity:** O(N) per step
- **Training-free:** Yes
- **Code:** [github.com/lzcemma/Scissorhands](https://github.com/lzcemma/Scissorhands)
- **与 CARC 区别:** Scissorhands relies on attention score history; doesn't consider key-space redundancy.

### FastGen
- **Venue:** ICLR 2024 (Oral)
- **Paper:** [arXiv:2310.01801](https://arxiv.org/abs/2310.01801)
- **Core mechanism:** Per-head adaptive compression — profiles attention patterns to classify heads (local-context, special-token-focused, broad-attention), then applies head-specific eviction policies.
- **Signal type:** Attention-score (per-head profiling)
- **Complexity:** O(N) per step after profiling
- **Training-free:** Yes
- **Code:** [github.com/machilusZ/FastGen](https://github.com/machilusZ/FastGen)
- **与 CARC 区别:** FastGen is head-level structural; CARC operates at token-level with a unified geometric signal.

### StreamingLLM
- **Venue:** ICLR 2024
- **Paper:** [arXiv:2309.17453](https://arxiv.org/abs/2309.17453)
- **Core mechanism:** "Attention sink" — initial tokens receive disproportionately high attention regardless of semantic content. Maintains attention sink tokens + sliding window of recent tokens, discarding middle tokens.
- **Signal type:** Positional (sink + recency)
- **Complexity:** O(1) per step — fixed window, no scoring needed
- **Training-free:** Yes
- **Code:** [github.com/mit-han-lab/streaming-llm](https://github.com/mit-han-lab/streaming-llm) (7.2k stars)
- **与 CARC 区别:** StreamingLLM is position-based with no content awareness; CARC uses content-based similarity to identify redundancy. StreamingLLM loses all middle-context information.

---

## 2. Reasoning-Specific Methods

### R-KV
- **Venue:** NeurIPS 2025
- **Paper:** [arXiv:2505.24133](https://arxiv.org/abs/2505.24133)
- **Core mechanism:** Hybrid importance × redundancy-suppression scoring. Computes pairwise cosine similarity between all retained keys to penalize redundant tokens. Achieves ~105% of full KV cache performance at 38% budget.
- **Signal type:** Attention-score × similarity (pairwise)
- **Complexity:** O(B²) per step — pairwise comparison among B retained keys
- **Training-free:** Yes
- **Code:** [github.com/Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV)
- **与 CARC 区别:** R-KV's O(B²) pairwise scoring is the direct predecessor. CARC replaces this with O(1) EMA centroid similarity, achieving equivalent redundancy awareness at constant cost.

### SkipKV
- **Venue:** arXiv 2025.12
- **Paper:** [arXiv:2512.07993](https://arxiv.org/abs/2512.07993)
- **Core mechanism:** Sentence-level selective KV eviction + generation skipping. Uses sentence-primary scoring to identify redundant reasoning sentences and an adaptive steering mechanism to suppress uninformative generation.
- **Signal type:** Attention-score (sentence-level aggregation)
- **Complexity:** O(N) per sentence boundary
- **Training-free:** Yes
- **Code:** No public repo found
- **与 CARC 区别:** SkipKV operates at sentence granularity; CARC at token level. SkipKV also skips generation, not just eviction.

### ThinKV
- **Venue:** ICLR 2026 (Oral)
- **Paper:** [arXiv:2510.01290](https://arxiv.org/abs/2510.01290)
- **Core mechanism:** Thought-adaptive compression — classifies CoT thoughts by attention sparsity patterns, applies hybrid quantization-eviction with higher precision for important thoughts. Custom PagedAttention kernel for memory slot reuse.
- **Signal type:** Attention-score (thought-level classification)
- **Complexity:** O(N) per thought boundary + quantization overhead
- **Training-free:** Yes
- **Code:** No public repo found (paper only)
- **与 CARC 区别:** ThinKV uses thought-level granularity + quantization; CARC is pure token-level eviction with geometric signal.

### LazyEviction
- **Venue:** arXiv 2025.06
- **Paper:** [arXiv:2506.15969](https://arxiv.org/abs/2506.15969)
- **Core mechanism:** "Token Importance Recurrence" — observes that many tokens regain high attention after multiple steps. Uses observation window + recurrence interval tracking to delay eviction of periodically critical tokens.
- **Signal type:** Attention-score (temporal recurrence tracking)
- **Complexity:** O(N) per eviction window
- **Training-free:** Yes
- **Code:** [github.com/Halo-949/LazyEviction](https://github.com/Halo-949/LazyEviction)
- **与 CARC 区别:** LazyEviction tracks temporal recurrence of individual token importance; CARC captures spatial redundancy via centroid similarity. Complementary perspectives.

### LongFlow
- **Venue:** arXiv 2026.03
- **Paper:** [arXiv:2603.11504](https://arxiv.org/abs/2603.11504)
- **Core mechanism:** Efficient importance estimation from intermediate attention computation using only the current query. Custom Flash-Attention kernel integrating importance estimation + eviction into a single operator. Static memory scheme for reduced fragmentation.
- **Signal type:** Attention-score (query-derived, single-pass)
- **Complexity:** O(N) per step, fused into attention kernel
- **Training-free:** Yes
- **Code:** No public repo found
- **与 CARC 区别:** LongFlow derives signal from attention computation; CARC uses pre-attention key geometry. LongFlow's kernel fusion is an engineering contribution orthogonal to CARC's signal design.

### TriAttention
- **Venue:** arXiv 2026.04
- **Paper:** [arXiv:2604.04921](https://arxiv.org/abs/2604.04921)
- **Core mechanism:** Exploits Q/K concentration stability in pre-RoPE space. Estimates key importance via trigonometric series derived from Q/K centers. Predicts which positional distances are preferred without computing full attention.
- **Signal type:** Geometric (trigonometric series on Q/K centers)
- **Complexity:** O(1) per step — precomputed from Q/K statistics
- **Training-free:** Yes
- **Code:** [github.com/WeianMao/triattention](https://github.com/WeianMao/triattention) (678 stars, vLLM+SGLang plugins)
- **与 CARC 区别:** TriAttention uses Q/K concentration for importance prediction; CARC uses key centroid similarity for redundancy detection. Both are O(1) geometric methods but measure different properties (importance vs. redundancy).

---

## 3. Anchor/Similarity-Based Methods

### KeyDiff
- **Venue:** NeurIPS 2025
- **Paper:** [arXiv:2504.15364](https://arxiv.org/abs/2504.15364)
- **Core mechanism:** Evicts keys with highest cosine similarity to a cache "anchor" (representative). Based on observation that keys with lower average pairwise cosine similarity produce higher attention outputs. Maximizes key diversity.
- **Signal type:** Similarity (key cosine distance to anchor)
- **Complexity:** O(N) per step — cosine similarity to single anchor
- **Training-free:** Yes
- **Code:** Integrated in [NVIDIA/kvpress](https://github.com/NVIDIA/kvpress) as `KeyDiffPress`
- **与 CARC 区别:** KeyDiff uses static anchor-based similarity; CARC uses EMA-updated centroid, adapting to the evolving key distribution over decoding steps.

### EvolKV
- **Venue:** EMNLP 2025 Findings
- **Paper:** [arXiv:2509.08315](https://arxiv.org/abs/2509.08315)
- **Core mechanism:** Evolutionary search for layer-wise KV cache budget allocation. Treats cache allocation as multi-objective optimization, using evolutionary algorithms to configure per-layer budgets that maximize downstream performance.
- **Signal type:** Learned (evolutionary optimization of layer budgets)
- **Complexity:** O(population × eval) offline search; O(N) online inference
- **Training-free:** No (requires evolutionary search per task)
- **Code:** No public repo found
- **与 CARC 区别:** EvolKV optimizes layer-level budget allocation; CARC is a token-level eviction signal. Orthogonal — EvolKV's layer budgets could wrap CARC.

---

## 4. Signal Types Classification Summary

| Signal Type | Representative Methods | Per-Step Complexity | Pros | Cons |
|---|---|---|---|---|
| **Attention-score** | H2O, Scissorhands, FastGen | O(N) | Directly reflects model's actual attention; well-studied | Requires attention score access (breaks FlashAttention); can't capture future importance |
| **Positional** | StreamingLLM | O(1) | Simplest; no computation needed | No content awareness; loses all middle context |
| **Similarity (pairwise)** | R-KV | O(B²) | Captures redundancy explicitly; strong for reasoning | Quadratic cost prohibitive at large budgets |
| **Similarity (anchor/centroid)** | KeyDiff, **CARC** | O(N) or O(1) | Content-aware redundancy; FlashAttention compatible | Anchor quality matters; may miss importance |
| **Geometric (Q/K structure)** | TriAttention | O(1) | Pre-computable; theoretically grounded | Assumes stable Q/K concentration; model-specific |
| **Temporal recurrence** | LazyEviction | O(N) | Prevents premature eviction of recurring tokens | Requires observation window; adds latency |
| **Thought-level** | ThinKV, SkipKV | O(N/sentence) | Coarse-grained = less overhead; reasoning-aware | Requires thought/sentence boundary detection |
| **Learned/Evolutionary** | EvolKV | Offline search | Task-optimized budgets | Not training-free; task-specific |

---

## 5. CARC Positioning

CARC's **O(1) EMA centroid similarity** occupies a unique niche:

1. **vs. R-KV:** Same redundancy-aware motivation, O(B²) → O(1) complexity reduction
2. **vs. KeyDiff:** Both similarity-based, but CARC uses adaptive EMA centroid vs. static anchor
3. **vs. TriAttention:** Both O(1) geometric, but orthogonal signals (redundancy vs. importance)
4. **vs. Attention-score methods:** CARC is attention-free → compatible with FlashAttention / fused kernels
5. **vs. StreamingLLM:** Content-aware vs. position-only; strictly more informative eviction

---

## 6. Baseline Code Availability

### 6.1 H2O
| Item | Detail |
|---|---|
| **Code URL** | [github.com/FMInference/H2O](https://github.com/FMInference/H2O) |
| **Last updated** | 2024 (stable, no active development) |
| **Stars** | ~300+ |
| **Qwen2/GQA support** | Not natively — built for OPT/LLaMA/GPT-NeoX. Needs manual adaptation for GQA |
| **HF transformers integration** | Yes, has `h2o_hf/` directory with HuggingFace integration |
| **Integration difficulty** | **Medium** — core logic is simple (attention score accumulation + top-k), but GQA adaptation required |
| **Priority for paper** | **HIGH** — most cited baseline in KV eviction literature |

### 6.2 StreamingLLM
| Item | Detail |
|---|---|
| **Code URL** | [github.com/mit-han-lab/streaming-llm](https://github.com/mit-han-lab/streaming-llm) |
| **Last updated** | 2024 (mature, integrated into TensorRT-LLM and HF transformers) |
| **Stars** | 7,200+ |
| **Qwen2/GQA support** | Validated on LLaMA, MPT, Falcon, Pythia. GQA should work since it's attention-pattern-agnostic |
| **Window size config** | Configurable: `start_size` (attention sink count) + `recent_size` (sliding window). Max = pre-training context window |
| **Integration difficulty** | **Easy** — simple positional window, minimal code changes |
| **Priority for paper** | **HIGH** — canonical streaming baseline; easy to implement even without their code |

### 6.3 R-KV
| Item | Detail |
|---|---|
| **Code URL** | [github.com/Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV) |
| **Last updated** | 2025 (initial release 2025-05-29) |
| **Stars** | ~100+ |
| **Qwen2/GQA support** | Yes — explicitly designed for DeepSeek-R1-Distill models (Qwen2.5-based) |
| **Reasoning model compatibility** | Direct — first-class support for reasoning models |
| **Integration difficulty** | **Easy** — designed for exactly our target model family |
| **Priority for paper** | **CRITICAL** — direct predecessor, must-have comparison (O(B²) vs. O(1)) |

### 6.4 kvpress (NVIDIA)
| Item | Detail |
|---|---|
| **Code URL** | [github.com/NVIDIA/kvpress](https://github.com/NVIDIA/kvpress) |
| **Install** | `pip install kvpress` |
| **Last updated** | Actively maintained (2026) |
| **Stars** | 500+ |
| **Qwen2/GQA support** | **Yes** — explicitly lists `Qwen2ForCausalLM` and `Qwen3ForCausalLM` as tested |
| **Supported methods** | SnapKVPress, KeyDiffPress, ObservedAttentionPress (≈H2O), TOVAPress, ExpectedAttentionPress, SimLayerKVPress, PyramidKVPress, ChunkKVPress, CriticalKVPress, FastKVzipPress, and more |
| **Integration difficulty** | **Easy** — pip install, 3-line API, model-agnostic wrapper |
| **Priority for paper** | **HIGH** — provides multiple baselines (especially KeyDiffPress as similarity-based comparison) through a single framework |

### Recommended Baseline Priority

| Priority | Method | Source | Reason |
|---|---|---|---|
| 1 (must) | **R-KV** | Official repo | Direct predecessor; O(B²) vs O(1) is core contribution |
| 2 (must) | **H2O** | Official repo or kvpress `ObservedAttentionPress` | Most cited attention-score baseline |
| 3 (must) | **StreamingLLM** | Official repo | Position-only baseline; lower bound for content-aware methods |
| 4 (should) | **KeyDiff** | kvpress `KeyDiffPress` | Similarity-based competitor; shows CARC's EMA advantage |
| 5 (should) | **SnapKV** | kvpress `SnapKVPress` | Strong practical baseline; attention-score variant |
| 6 (nice) | **TriAttention** | Official repo | O(1) geometric competitor; shows CARC's complementary signal |
| 7 (nice) | **Full KV** | Native | Upper bound reference |

---

## 7. Key Observations for Paper Writing

1. **Signal taxonomy is under-explored.** Most papers cluster in "attention-score" category. CARC + KeyDiff + TriAttention form a new "geometric/similarity" family worth highlighting.

2. **Reasoning-specific methods are exploding.** R-KV (NeurIPS'25), ThinKV (ICLR'26 Oral), SkipKV, LazyEviction, LongFlow, TriAttention — all target reasoning model KV compression. CARC enters a crowded but high-impact space.

3. **O(1) per-step cost is rare.** Only StreamingLLM (positional, no content awareness) and TriAttention (Q/K trigonometric) achieve O(1). CARC's O(1) EMA centroid is a third distinct O(1) approach, and uniquely captures redundancy.

4. **kvpress is the best unified evaluation framework.** Supports Qwen2, pip-installable, includes multiple baselines. Consider implementing CARC as a kvpress press for easy comparison.
