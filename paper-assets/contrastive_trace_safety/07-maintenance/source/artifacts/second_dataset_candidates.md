# Second Dataset Candidate Evaluation

**Goal**: Find a second dataset to replicate the metric-bias pattern (layer selection sensitivity) discovered on HarmThoughts, addressing potential "dataset-specific artifact" critique.

**HarmThoughts baseline**: Step-level CP-annotated reasoning traces from R1-8B/OT-7B/QwQ-32B/R1-32B; small scale (19–47 traces per model); 60/20/20 split; harmful prompt → reasoning chain → CP annotation.

## Evaluation Summary Table

| Dataset | Has traces? | Has CP? | Scale | Domain diff | Access | Feasibility |
|---------|------------|---------|-------|-------------|--------|-------------|
| **XSTest** | No (prompt-only) | No | 450 prompts (250 safe + 200 unsafe) | Medium (exaggerated safety focus) | ✅ CC-BY-4.0, GitHub | ⭐⭐⭐ |
| **AdvBench** | No (prompt-only) | No | 520 harmful behaviors | High (adversarial suffix attacks) | ✅ MIT, HuggingFace | ⭐⭐⭐ |
| **WildGuardMix** | No (prompt+response pairs) | No | 92K labeled examples | High (13 risk categories, jailbreak+vanilla) | ✅ HuggingFace | ⭐⭐ |
| **WildJailbreak** | No (prompt+response) | No | 262K pairs | High (adversarial tactics, exaggerated safety) | ✅ HuggingFace | ⭐⭐ |
| **SORRY-Bench** | No (prompt-only) | No | 450 base + 9K mutations | High (45 fine-grained categories) | ✅ HuggingFace+GitHub | ⭐⭐⭐ |
| **StrongREJECT** | No (prompt-only) | No | 313 malicious prompts | Medium | ✅ HuggingFace+GitHub | ⭐⭐ |
| **HEx-PHI** | No (prompt-only) | No | 330 instructions (11 categories) | Medium (policy-based categories) | ✅ HuggingFace | ⭐⭐ |
| **SafeDecoding** | No (uses AdvBench/HEx-PHI) | No | N/A (method paper) | N/A | N/A | ⭐ |
| **ReasoningShield** | ✅ Yes (CoT traces from 8 LRMs) | No (sentence-level safety labels) | 9.2K (Query,CoT) pairs | High (10 risk categories, 3 safety levels) | ✅ HuggingFace+GitHub | ⭐⭐⭐⭐⭐ |
| **SafeRBench** | ✅ Yes (micro-thought chunks) | No (6 safety intent tags) | Not yet released openly | High (harm gradients, process-level) | ❓ Unclear availability | ⭐⭐ |
| **AISafety-Student CoT** | ✅ Yes (sentence-level labeled) | Partial (safety behavior annotations) | 50K+ annotated sentences | High (20 safety behaviors) | ✅ HuggingFace | ⭐⭐⭐⭐ |
| **Nvidia Nemotron Safety** | ✅ Yes (reasoning traces) | No | 28K+8.7K samples | Medium (content safety taxonomy) | ✅ HuggingFace | ⭐⭐⭐ |
| **SafeChain** | ✅ Yes (CoT safety training data) | No | Unknown (first CoT safety training set) | High (12 reasoning models) | ✅ (published ACL Findings 2025) | ⭐⭐⭐ |

## Detailed Evaluation

### 1. XSTest (Röttger et al., NAACL 2024)
- **What it is**: 250 safe prompts (10 types × 25) + 200 unsafe contrast prompts testing exaggerated safety / false refusal.
- **Traces**: None. Prompt-only benchmark. Would need to generate traces with R1-8B.
- **CP annotations**: None. Need LLM-based annotation pipeline.
- **Scale**: 200 unsafe prompts usable. After trace generation + filtering, expect ~150+ valid traces.
- **Domain difference**: Moderate. Focuses on borderline safe/unsafe distinction (homonyms, figurative language), different from HarmThoughts' direct harmful prompts. The safe/unsafe contrast structure is a plus for probing analysis.
- **Access**: CC-BY-4.0, GitHub: [paul-rottger/xstest](https://github.com/paul-rottger/xstest)
- **Verdict**: Good candidate for generation. Small but focused. The safe/unsafe contrast structure could yield interesting probe behavior differences.

### 2. AdvBench (Zou et al., 2023)
- **What it is**: 520 harmful behavior instructions designed for adversarial attack evaluation.
- **Traces**: None. Prompt-only. R1-8B generation needed.
- **CP annotations**: None. Need annotation pipeline.
- **Scale**: 520 prompts. Strong scale advantage over HarmThoughts. After generation + filtering, expect 400+ usable traces.
- **Domain difference**: High. Direct harmful instructions (crime methods, threats, discrimination) vs. HarmThoughts' mixed prompt types. Pure adversarial framing.
- **Access**: MIT license, [walledai/AdvBench](https://huggingface.co/datasets/walledai/AdvBench)
- **Verdict**: Excellent scale, easy access, maximally different domain. Top candidate if generating traces ourselves.

### 3. WildGuardMix / WildJailbreak
- **WildGuardMix**: 92K examples, 13 risk categories. Prompt+response pairs with moderation labels. No reasoning traces. Too large and differently structured for our needs—designed for training safety classifiers, not trace-level analysis.
- **WildJailbreak**: 262K prompt-response pairs including adversarial jailbreak tactics. Includes both harmful and benign (exaggerated safety) examples. No reasoning traces.
- **CP annotations**: Neither has step-level annotations.
- **Verdict**: Useful as a prompt source but not directly applicable. The adversarial subset of WildJailbreak (2K harmful eval examples) could serve as prompts for trace generation, providing diverse jailbreak tactics not present in AdvBench.

### 4. SafeDecoding (Xu et al., ACL 2024)
- **What it is**: A decoding-time defense method, not a dataset. Evaluates on AdvBench + HEx-PHI + MT-Bench + Just-Eval.
- **Verdict**: No new data. Skip.

### 5. SORRY-Bench (ICLR 2025)
- **What it is**: 450 base unsafe instructions across 45 fine-grained categories (10/category), with 20 linguistic mutations each (9K total).
- **Traces**: None. Prompt-only.
- **CP annotations**: None.
- **Scale**: 450 base (or up to 9K with mutations). Excellent taxonomic balance.
- **Domain difference**: High. 45 categories vs. HarmThoughts' coarser taxonomy. Balanced representation across harm types is a methodological advantage.
- **Access**: HuggingFace [sorry-bench/sorry-bench-202406](https://huggingface.co/datasets/sorry-bench/sorry-bench-202406) + GitHub
- **Verdict**: Strong candidate. Balanced taxonomy enables per-category analysis of layer selection pattern. Could demonstrate the pattern is consistent across diverse harm types.

### 6. ReasoningShield (2025) ⭐ TOP CANDIDATE
- **What it is**: First comprehensive safety dataset for reasoning traces of LRMs. 7K train + 2.2K test (Query, CoT) pairs with sentence-level safety annotations across 10 risk categories and 3 safety levels (safe/borderline/unsafe).
- **Traces**: ✅ Yes! Contains actual CoT reasoning traces from 8 different LRMs. This is exactly what we need—no generation step required.
- **CP annotations**: Not CP specifically, but has sentence-level safety risk annotations with 3 levels. These annotations identify where in the reasoning chain safety risks emerge—functionally analogous to CP. Could be mapped to binary CP labels (first sentence where risk level transitions from safe to borderline/unsafe).
- **Scale**: 9.2K annotated (Query, CoT) pairs. Far exceeds HarmThoughts' scale.
- **Domain difference**: High. 10 risk categories, traces from 8 different LRMs (not just R1-distilled), diverse prompt sources (5 datasets). Maximally different provenance.
- **Annotation quality**: Human-AI collaboration with Fleiss κ=0.75 (substantial agreement), 93% annotation accuracy. Gold labels via majority voting.
- **Access**: ✅ HuggingFace [ReasoningShield/ReasoningShield-Dataset](https://huggingface.co/datasets/ReasoningShield/ReasoningShield-Dataset) + GitHub
- **Verdict**: **Best candidate by far.** Pre-existing reasoning traces with sentence-level safety annotations eliminates the generation bottleneck. The safety-level transitions can serve as CP proxies. Scale (9.2K) dwarfs HarmThoughts. Different LRMs provide cross-model generalization. Published with human annotation validation.

### 7. AISafety-Student Reasoning Safety Behaviours (2025)
- **What it is**: 50K+ annotated sentences from reasoning traces, labeled with 20 distinct safety behaviors across 6 categories.
- **Traces**: ✅ Yes. Contains reasoning traces with sentence-level behavior labels.
- **CP annotations**: Partial. Labels include behaviors like "expression of safety concerns" and "speculation on user intent" which could identify transition points in reasoning. Not CP per se, but richer behavioral taxonomy.
- **Scale**: 50K+ sentences (unknown number of full traces).
- **Domain difference**: High. 20 behavior types provide fine-grained view unavailable in HarmThoughts.
- **Access**: ✅ HuggingFace [AISafety-Student/reasoning-safety-behaviours](https://huggingface.co/datasets/AISafety-Student/reasoning-safety-behaviours)
- **Caveats**: LLM-as-a-judge annotations (no human validation reported). Unclear how many distinct traces/prompts are included.
- **Verdict**: Strong secondary candidate. Rich behavioral annotations could enable novel analyses beyond CP-based detection, but LLM-only annotation quality is a concern.

### 8. SafeRBench (2025)
- **What it is**: Benchmark with micro-thought chunking that segments reasoning traces into coherent units with 6 safety intent tags.
- **Traces**: ✅ Yes, with micro-thought segmentation.
- **CP annotations**: 6 safety intent tags per chunk—could identify commitment-like transitions.
- **Scale**: Unknown (paper doesn't specify dataset size clearly).
- **Access**: ❓ No confirmed open release found. Paper on arXiv but no HuggingFace/GitHub dataset link discovered.
- **Verdict**: Conceptually very relevant but availability unclear. Cannot rely on this unless data release is confirmed.

### 9. Nvidia Nemotron Content Safety Reasoning Dataset
- **What it is**: 28K samples with reasoning traces for content safety classification, generated by DeepSeek-R1, Qwen3-32B, gpt-oss-120b.
- **Traces**: ✅ Yes. Full-length and reduced reasoning traces.
- **CP annotations**: No. Labels are at sample level (safe/unsafe classification), not step level.
- **Scale**: 28K + 8.7K = 36.7K samples. Large.
- **Domain difference**: Medium. Standard content safety taxonomy.
- **Access**: ✅ HuggingFace [nvidia/Nemotron-Content-Safety-Reasoning-Dataset](https://huggingface.co/datasets/nvidia/Nemotron-Content-Safety-Reasoning-Dataset)
- **Verdict**: Good scale and has reasoning traces, but designed for guardrail training, not step-level safety monitoring. Would need post-hoc CP annotation. Still viable as a prompt+trace source.

### 10. SafeChain (ACL Findings 2025)
- **What it is**: First CoT-style safety training dataset with fine-grained analysis of reasoning traces and final answers.
- **Traces**: ✅ Yes. CoT traces from 12 reasoning models including DeepSeek-R1 series, QwQ, etc.
- **CP annotations**: Has trace-level analysis distinguishing reasoning trace safety from final answer safety.
- **Scale**: Not precisely stated.
- **Domain difference**: High. Multi-model (12 LRMs), uses StrongReject + WildJailbreak prompts.
- **Access**: Published at ACL 2025. Website: [safe-chain.github.io](https://safe-chain.github.io/)
- **Verdict**: Relevant conceptually. Would need to verify exact data format and availability.

## Recommendation

### Top-1: ReasoningShield Dataset
**Why**: This is the only dataset that simultaneously provides (a) pre-existing reasoning traces from multiple LRMs, (b) sentence-level safety annotations that can serve as CP proxies, (c) sufficient scale (9.2K annotated pairs), (d) human-validated annotation quality (κ=0.75), and (e) confirmed open access on HuggingFace. It eliminates the trace generation bottleneck entirely and provides cross-model generalization evidence. The 10 risk categories and 3 safety levels enable mapping the first safe→borderline/unsafe transition to a CP-like annotation.

**Risk**: The safety-level annotations are not identical to CP annotations—they mark "where risk appears in reasoning" rather than "where the model commits to harmful output." However, for validating the metric-bias pattern (layer selection sensitivity), what matters is having a meaningful step-level binary signal, and safe→unsafe transitions serve this purpose.

### Top-2: AdvBench (with R1-8B trace generation)
**Why**: If ReasoningShield's annotation scheme proves incompatible with our CP framework, AdvBench provides 520 prompts with maximal domain difference from HarmThoughts. Generating traces with R1-8B is straightforward (we already have the pipeline), and the scale is 10× HarmThoughts. The pure adversarial framing ensures we're testing the pattern on a clearly different distribution.

### Honorable mention: SORRY-Bench
**Why**: If taxonomic diversity matters for the argument, SORRY-Bench's 45 balanced categories enable per-category layer selection analysis. Could show the pattern holds across all 45 harm types, not just aggregate.

## Generation Plan (if traces need to be generated)

### Scenario A: ReasoningShield (no generation needed)
- Download dataset from HuggingFace
- Filter for traces from models closest to our setup (R1-distilled variants)
- Map 3-level safety annotations → binary CP labels (first safe→borderline/unsafe transition = CP)
- Estimated time: **~2 hours** (data processing + validation)

### Scenario B: AdvBench with R1-8B generation
- **Prompts**: 520 harmful behaviors
- **Generation**: R1-8B inference, avg ~500 tokens/trace (based on HarmThoughts stats)
- **Total tokens**: ~260K tokens generation
- **GPU time**: RTX 6000 Ada (48GB), R1-8B at ~30 tokens/sec → ~2.4 hours generation
- **CP annotation**: LLM-based (GPT-4o or Claude) + spot-check human validation
  - Annotation prompt: identify the first step where model commits to providing harmful content
  - Estimated: ~3 hours annotation + 1 hour validation
- **Hidden state extraction**: ~1 hour (reuse existing pipeline)
- **Total estimated time**: **~8 hours end-to-end**

### Scenario C: SORRY-Bench with R1-8B generation
- **Prompts**: 450 base (skip linguistic mutations for initial replication)
- **Similar timeline to AdvBench**: ~7 hours end-to-end
