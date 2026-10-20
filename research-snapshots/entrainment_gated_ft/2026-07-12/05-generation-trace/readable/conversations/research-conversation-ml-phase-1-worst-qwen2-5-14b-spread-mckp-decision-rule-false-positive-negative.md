# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Qwen2.5-14B 不是 Spread 或 MCKP 无效，decision rule 出现 false positive/negative，核心

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/ed67fc76-685e-40e0-9769-deccf8f764ed.jsonl`
- **Structured JSON:** [`9eef623e8cb7baf0f3d8.json`](../../sessions/9e/9eef623e8cb7baf0f3d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T09:26:52.969Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T09:26:52.969Z",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Qwen2.5-14B 不是 Spread 或 MCKP 无效，decision rule 出现 false positive/negative，核心 diagnostic 叙事不成立\n核心假设：['Qwen2.5-14B concentration ≥0.50 但 MCKP 无改善（类似 Yi-1.5，diagnostic false positive）', '或 Qwen2.5-14B concentration <0.40（Flat pattern），Qwen 系列只有 7B 是 Spread', 'Decision rule accuracy 降至 4/6 或 5/6 但有 high-confidence failure', 'Gemma-2 BOS fix 显著改变 unconstrained ratio（<1.25 或 >1.60），三档标签需重新校准', 'W9 compounding 数据 non-monotonic 或 variance 掩盖趋势']\n关键指标范围：{'qwen14b_mckp_improvement_over_uniform_pct': [-3, 3], 'qwen14b_concentration': [0.3, 0.75], 'qwen14b_t1_t5': [0.4, 0.95], 'decision_rule_accuracy': [4, 5], 'gemma2_constrained_vs_uniform_pct': [-2.0, 2.0], 'gemma2_unconstrained_ratio': [1.15, 1.65], 'w9_k64_randomk_topk_ratio': [1.0, 2.0]}\n叙事方向：放弃 \"diagnostic/decision rule\" 作为核心 contribution，reframe 为三条新主线： (1) **Cardinality constraint as universal safeguard** — 不依赖 diagnostic， 所有 5-6 个模型上 constraint 都 ≤ uniform 或防止 catastrophe， 这是一个 architecture-agnostic 的 practical fix； (2) **Systematic negative result** — \"we tested 5+ architectures and found  non-uniform KV cache quantization is beneficial in only 1/5-6 cases\"， 这本身是有价值的 finding（saves practitioners time），framing 类似 \"Challenging common assumptions about mixed-precision KV cache\"； (3) **Compounding effect characterization** — 即使 diagnostic 不成立， discrete non-consecutive bit-width 上 solver 失败的机制分析 （W9 data + Qwen catastrophe）仍是 novel contribution。 三档标签改为纯描述性（按倍数分 tier，不绑定 distribution shape 解释）。 论文标题从 \"When Does X Help\" 转向 \"The Cardinality Constraint You Need  for Hardware-Aligned KV Cache Quantization\"。仍投 EMNLP Main Efficient Methods， 但卖点从 analysis 转向 practical method + surprising negative results。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ratekv\nfocus: 审稿修订后的 concentration-dependent narrative 是否 hold：(1) 三档标签(catastrophic/moderate/mild)是否自洽 (2) N=1 Spread + empirical decision rule 的 claim 强度是否匹配 EMNLP Main (3) Gemma-2 1.47× 讨论是否充分 (4) W9 super-additive 形式化程度是否足够 (5) 5-model downstream 完整数据下 story 是否比之前更强\n\n## paper_framing.md\n\n# Paper Framing — ratekv\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)\n- Track: Efficient Methods for NLP\n\n## bf16 Consistency Resolution (2026-05-14)\n\n**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。\n\n**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。\n\n| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |\n|------|---------------------|----------------------|-----------|\n| Baseline | **9.8106** | 8.819 | 9.81 |\n| Uniform 4-bit | **15.4454** | — | 15.45 |\n| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |\n| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |\n\n## Core Insight\n\nPer-head KV cache quantization sensitivity varies dramatically across architectures, and the effectiveness of non-uniform mixed-precision allocation is fundamentally determined by the degree of this heterogeneity. We provide both the analysis framework — characterizing when non-uniform quantization helps via per-head sensitivity concentration metrics — and a surprisingly simple method fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding effects from profiler non-additivity and reduces the search space sufficiently that solver choice becomes irrelevant (greedy and MCKP produce identical allocations).\n\n## Core Claims (3 条)\n\n1. **Head sensitivity heterogeneity is architecture-dependent and determined by sensitivity *distribution shape*, not GQA ratio or concentration alone**: Per-KV-head quantization sensitivity is extremely non-uniform within models, but whether MCKP can exploit this heterogeneity depends on the *shape* of the sensitivity distribution, not just its magnitude. Critical counterexample: Yi-1.5-9B (GQA 8:1, concentration 0.71 — the *highest* in our lineup) provides *no benefit* from MCKP (7.22 vs 7.22 uniform), while Qwen2.5-7B (GQA 7:1, concentration 0.61) succeeds (+27.3%). The difference is distribution shape: Qwen has a *cluster* of sensitive heads (Layer 0, 4 heads with cross-bitwidth gradients — \"spread\" pattern, t₁/t₅=0.57), while Yi-1.5 has a single extreme outlier (L4H3, delta=13.12, t₁/t₅=0.90 — \"spike\" pattern) with sensitivity at only one bitwidth. A joint diagnostic — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case (Qwen) from all four non-beneficial cases across five architectures. Three shape categories emerge:\n   - **Spread** (Qwen): high concentration + low t₁/t₅ → multiple heads with cross-bitwidth gradients → MCKP effective\n   - **Spike** (Yi-1.5, Llama): high t₁/t₅ → single outlier dominates → MCKP ineffective\n   - **Flat** (Mistral, Gemma-2): low concentration → near-uniform sensitivity → MCKP ineffective (t₁/t₅ irrelevant when concentration < 0.50)\n\n2. **Cardinality constraint is the primary intervention; unconstrained catastrophe is Spread-specific**: On non-consecutive discrete bit-widths {2,4,8,16}, unconstrained allocation produces **catastrophic** results on Spread-heterogeneity architectures (Qwen: greedy 32.45, MCKP 36.92 vs uniform 15.45 = 3.31× baseline) because per-head independent profiling distortions compound non-additively when many heads are simultaneously assigned extreme quantization. On non-Spread architectures, unconstrained allocation causes **mild-to-moderate degradation** (Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.47×) but still underperforms uniform 4-bit in all cases — the solver over-allocates 2-bit heads even when individual distortions appear small. A cardinality constraint (max_2bit≤k) is a simple and sufficient condition: it prevents compounding on Spread models, avoids 2-bit over-allocation on non-Spread models, AND reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce identical bit allocations and PPL (Δ=0.0000, both 11.2312). **Practical implication**: the concentration diagnostic determines whether to invest in MCKP + constraint (Spread models) or simply use uniform 4-bit (non-Spread models — saves solver computation with no quality loss). The profiling benefit beyond the constraint (hires vs lowres) is architecture-dependent: substantial on Spread models (Qwen), marginal on others. The optimal k is determinable via small-scale compounding effect test (plan_004).\n\n**Claim 2 three-pillar support** (Reviewer Q4, new narrative STRENGTHENS Claim 2):\n1. Spread models: constraint prevents catastrophe (Qwen 32.45→11.23)\n2. Flat models: constraint prevents moderate over-allocation (Gemma-2 8.85→~6.17, 106→8 heads at 2-bit)\n3. All models: constraint makes solver choice irrelevant (greedy=MCKP, Δ=0.0000)\nThis answers \"when\" and \"why\", not just \"what\" — stronger than original \"universal catastrophe\" narrative.\n\n3. **A joint empirical decision rule correctly separates beneficial from non-beneficial architectures**: Constrained allocation achieves 27.3% PPL improvement on Qwen (spread pattern: concentration 0.61, t₁/t₅=0.57), while providing no benefit on Yi-1.5 (spike: 0.71, t₁/t₅=0.90, ≈0%), Llama (spike: 0.34, t₁/t₅=0.71, +0.2%), Mistral (flat: 0.22, t₁/t₅=0.18, -0.4%), and Gemma-2 (flat: 0.23, t₁/t₅=0.38, -0.3%). The joint condition — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case from all four non-beneficial cases across five architectures (5/5 accuracy). Concentration alone fails: Yi-1.5 (0.71) exceeds Qwen (0.61) yet gains nothing, because its spike pattern (single outlier, no cross-bitwidth gradient) cannot be exploited. Under aggressive compression (≥5×), constrained allocation prevents catastrophic collapse even on non-beneficial architectures (Llama 5.3×: constrained PPL 57.60 vs uniform 2-bit 2644). This provides practitioners an empirical decision rule for when to invest in mixed-precision KV cache quantization. **Claim strength note (Reviewer-verified)**: N=1 Spread → position as \"empirical decision rule\", NOT \"diagnostic framework\". If Qwen2.5-14B also confirms Spread → upgrade to \"empirical diagnostic\" (N=2).\n\n## Story Spine\n\n- **Problem**: KV cache quantization typically applies uniform bit-width across all heads. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but two fundamental questions remain unanswered: (1) *when* does non-uniform allocation actually help — i.e., under what architectural and compression conditions does the added complexity pay off? (2) *how* to make existing allocation algorithms (greedy, MCKP) work correctly on hardware-aligned discrete bit-widths {2,4,8,16} where they currently fail catastrophically?\n\n- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via continuous closed-form (Theorem 2) and discrete greedy (Algorithm 1, optimal on consecutive integers {2,...,6} per Proposition 6). However, on hardware-aligned non-consecutive sets {2,4,8,16}, RateQuant's greedy produces PPL 32.45 (vs optimal ~11.23) — the polymatroid structure that guarantees greedy optimality breaks. Moreover, unconstrained MCKP fares even worse (PPL 36.92) due to compounding effects from profiler non-additivity. Critically, neither RateQuant nor ARKV addresses *when* non-uniform allocation is beneficial.\n\n- **Our framing**: We present a systematic study of per-head KV cache quantization sensitivity across architectures and identify a surprisingly simple fix for the failure of existing algorithms on hardware-aligned bit-widths: a cardinality constraint limiting the number of heads assigned to extreme quantization levels. This single intervention (a) prevents compounding effects, (b) reduces the search space to where solver choice is irrelevant — greedy and MCKP produce identical optimal allocations, and (c) can be parameterized via a small-scale compounding test. Beyond the method, we establish that the benefit of non-uniform allocation is architecture-dependent and quantifiable via an empirical decision rule (concentration + distribution shape), providing practitioners a two-metric check for when mixed-precision is worthwhile.\n\n- **Headline result template**: \"We show that the benefit of non-uniform per-head KV cache quantization is concentration-dependent: on spread-heterogeneity architectures (Qwen, concentration 0.61), unconstrained solvers fail catastrophically (PPL 32-37 vs uniform 15.45), while a cardinality constraint (≤k heads at 2-bit) achieves 27.3% PPL improvement with identical results from greedy and MCKP (Δ=0.0000). On non-spread architectures (4 models, 1.07-1.47× baseline), unconstrained solvers cause only mild degradation, and constrained MCKP offers no benefit over uniform 4-bit at either PPL or downstream task level (<1pp avg). An empirical decision rule (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly separates the beneficial case from all four non-beneficial cases (5/5 accuracy) at both PPL and downstream task level, providing practitioners a two-metric check to determine whether mixed-precision KV cache quantization is worthwhile — or whether uniform quantization suffices.\"\n\n## \"When Does Non-Uniform Allocation Help?\" — Analysis Chapter\n\nFive case studies representing the full spectrum of heterogeneity:\n\n| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |\n|------|-------|-----|--------------|------------------------------|---------------|\n| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; \"spread\" pattern (L0 cluster, 4 heads, 26× dominance) |\n| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; \"spike\" pattern (L4H3 single outlier, 34% of total delta) |\n| **Marginal** | Llama-3.1-8B | 4:1 | 0.34-0.59 | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |\n| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |\n| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |\n\n**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.\n\n**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).\n\n**Joint diagnostic** (n=5, 5/5 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike) and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.\n\n## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)\n\n| Method | PPL | Bit Distribution | Budget |\n|--------|-----|-------------------|--------|\n| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |\n| MCKP unconstrained | 36.92 | — | 0.25 |\n| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |\n\nKey takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.\n\n## Cross-Architecture Evidence Summary\n\n| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |\n|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|\n| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |\n| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |\n| Llama-3.1-8B | 4:1 | 256 | 0.57 (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (borderline t₁/t₅=0.71) | ≈ Marginal |\n| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |\n| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |\n\n**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:\n- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding\n- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta\n- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)\n- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads\n\n**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):\n\nThree-tier labeling (NOT binary catastrophe/benign):\n- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding\n- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions\n- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)\n\nReviewer-suggested paragraph for paper (1 段, 3-4 句):\n\"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\"\n\nThis **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.\n\n⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.\n\n**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.\n\n**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.\n\n### Mistral k Ablation (256 KV heads, budget=0.25)\n\nPPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).\n\n| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |\n|---|-----|-------|-------|-------|--------|-----|\n| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |\n| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |\n| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |\n| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |\n| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |\n| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |\n\nContrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.\n\n### Llama k Ablation (256 KV heads, budget=0.25)\n\nAll k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).\n\n### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)\n\n**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅\n\n| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |\n|------|---------------|------------|---|---------------|\n| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |\n| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |\n| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |\n| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |\n| **Avg recovery** | — | — | **72.8%** | — |\n\n**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.7946 | 0.7854 | -0.92pp |\n| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |\n| hellaswag | 0.5857 | 0.5797 | -0.60pp |\n| piqa | 0.7927 | 0.7894 | -0.33pp |\n| winogrande | 0.7174 | 0.7301 | +1.27pp |\n| **Average** | **0.6822** | **0.6745** | **-0.77pp** |\n\n**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.8173 | 0.8039 | -1.34pp |\n| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |\n| hellaswag | 0.6026 | 0.6012 | -0.14pp |\n| piqa | 0.7867 | 0.7802 | -0.65pp |\n| winogrande | 0.7253 | 0.7238 | -0.15pp |\n| **Average** | **0.6915** | **0.6816** | **-0.99pp** |\n\n**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=4) | Δ |\n|------|---------------|------------|---|\n| arc_easy | — | — | — |\n| arc_challenge | — | — | — |\n| hellaswag | — | — | — |\n| piqa | — | — | — |\n| winogrande | — | — | — |\n| **Average** | **0.6894** | **0.6846** | **-0.48pp** |\n\n**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)\n\n| Task | Uniform 4-bit | MCKP | Δ |\n|------|---------------|------|---|\n| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |\n\n**Downstream summary (Reviewer-verified framing)**:\n- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**\n- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)\n- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)\n- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise\n- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)\n- **Paper must**: (a) report full per-task tables, not just averages, (b) use \"shows minor degradation\" NOT \"preserves accuracy\" — the latter has spin, (c) note arc_challenge as worst-case explicitly\n- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance\n- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论：\"ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\"\n- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞：\"Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge).\"\n\n## Allocation Baseline Evidence (plan_015, mckp_reeval)\n\nAll numbers from unified bf16 eval pipeline, budget=0.25.\n\n| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |\n|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|\n| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |\n| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |\n| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |\n\n**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.\n\n**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.\n\n## Differentiation from RateQuant\n\n| Aspect | RateQuant | Ours |\n|--------|-----------|------|\n| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |\n| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |\n| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |\n| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |\n| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |\n| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |\n| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |\n\n## Venue Fit Risks\n\n- **\"The constraint is just a heuristic, not a real contribution\"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.\n- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.\n- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive \"higher GQA = more benefit\" hypothesis and shows our diagnostic is needed.\n- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 5/5 correct). The \"spike vs spread\" analysis explains WHY same-GQA models differ.\n- **Statistical power**: n=5 models is directional evidence, not statistical claim. Do NOT claim \"significant correlation\" — use \"consistent pattern across 5 architectures\" or \"5/5 correctly classified by the 0.50 threshold.\"\n- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.\n\n## Anticipated Reviewer Concerns\n\n1. **\"The cardinality constraint is trivial — just cap the extreme allocations\"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.\n2. **\"This is just RateQuant with a constraint added\"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.\n3. **\"The method only works on Qwen — isn't this a Qwen paper?\"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.\n4. **\"How does this work at different compression ratios?\"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.\n5. **\"n=3/4/5 models is not enough for the heterogeneity claim\"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.\n6. **\"RateQuant does K/V asymmetric allocation, do you?\"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.\n7. **\"Where are the downstream task results?\"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use \"shows minor degradation\" not \"preserves accuracy\".\n8. **\"The profiler distortion=0.0 on Mistral suggests the profiling method is broken\"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.\n9. **\"If solver doesn't matter, why present MCKP at all?\"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim:\n  - 2\n  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.\n    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.\n    Strengthens narrative: \"solver automatically discovers sensitivity structure.\"\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: exp_d_no_l0_exclusion\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_002\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).\n    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability\n    across different GQA ratios and architectures. Fallback if HF token unavailable:\n    Yi-1.5-9B (non-gated, similar scale).\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: llama_full_pipeline\n  model: Llama-3.1-8B\n  fallback_model: Yi-1.5-9B\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 8.7\n    uniform_4bit_ppl_bf16: 8.47\n    baseline_ppl_bf16: 8.09\n    delta_vs_uniform: -0.23\n    memory_ratio: 0.25\n- id: plan_003\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture\n    family to establish cross-architecture validity.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mistral_full_pipeline\n  model: Mistral-7B-v0.3\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 7.564\n    uniform_4bit_ppl_bf16: 7.131\n    baseline_ppl_bf16: 7.035\n    delta_vs_uniform: -0.433\n    memory_ratio: 0.25\n- id: plan_004\n  claim:\n  - 3\n  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112\n    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map\n    the compounding threshold. Establishes the principled basis for cardinality constraint\n    selection.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: compounding_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_005\n  claim:\n  - 2\n  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,\n    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline\n    at same budget.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: budget_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_006\n  claim:\n  - 1\n  - 2\n  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).\n    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers\n    mid-layer heterogeneity and improves solver allocation beyond current results.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_e_hires_profile\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    constrained_ppl_bf16: 9.569\n    baseline_ppl_bf16: 8.819\n    exp_c_ppl_bf16: 11.345\n    delta_vs_exp_c: -1.776\n    memory_ratio: 0.25\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    profile_resolution:\n      hires_nonzero_2bit: 100\n      lowres_nonzero_2bit: 37\n      hires_nonzero_4bit: 6\n      lowres_nonzero_4bit: 4\n      total_heads: 112\n    allocation_diff_count: 8\n    profiling_time_min: 65.5\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.\n    Cross-dataset evaluation to show results are not WikiText-2 specific.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  eval: C4\n  status: DONE\n  conclusion: success\n  metrics: &id001\n    c4_cal_wt2_eval_mckp_ppl: 11.2942\n    c4_cal_wt2_eval_uniform_ppl: 15.4454\n    c4_cal_wt2_eval_delta: 4.1512\n    c4_cal_bf16_baseline: 12.6505\n    wt2_bf16_baseline: 9.8106\n    allocation_agreement_c4_vs_wt2: 0.964\n    agreement_heads: 108/112\n    bit_dist: 2bit:8, 4bit:100, 8bit:4\n    cross_domain_wt2_to_c4_mckp_ppl: 20.5601\n    cross_domain_wt2_to_c4_uniform_ppl: 35.4232\n    cross_domain_c4_bf16: 15.3246\n    old_contaminated_ppl: 11.3285\n    contamination_impact: 0.0343\n    models_completed: Qwen2.5-7B only\n- id: plan_008\n  claim:\n  - 2\n  description: 'RateQuant comparison: implement RateQuant''s greedy algorithm (Algorithm\n    1) on our discrete action set {2,4,8,16}-bit. RateQuant''s Prop. 6 optimality\n    relies on consecutive-integer polymatroid structure which breaks on non-consecutive\n    sets. Show greedy produces suboptimal allocation vs constrained MCKP. Critical\n    for differentiation claim — must have experimental evidence.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: ratequant_greedy_comparison\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_009\n  claim:\n  - 2\n  description: 'Oracle comparison: brute-force optimal allocation on a subset (3-4\n    layer groups) of Qwen2.5-7B. Quantify MCKP gap to oracle.\n\n    '\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_006\n  registry_id: oracle_comparison\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_ppl: 10.9131\n    max_oracle_gap_ppl: 0.0183\n    avg_oracle_gap_ppl: 0.0046\n    layers_mckp_optimal: 5/8\n    layers_with_gap: 3\n    gap_layers:\n      L1: 0.0183\n      L4: 0.0045\n      L11: 0.0136\n    gap_nature: 2-bit head position swap within same bit budget\n    total_evals: 54\n    runtime_min: 21.3\n- id: plan_010\n  claim:\n  - 2\n  description: 'Cross-domain calibration robustness: calibrate on C4, evaluate on\n    WikiText-2 (and vice versa). Report per-head allocation agreement rate across\n    calibration sources.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_007\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: plan_011\n  claim:\n  - 1\n  description: 'Head sensitivity visualization: generate paper-quality figures showing\n    per-head profiling delta heatmap across layers, compounding effect curve, and\n    budget allocation comparison chart.\n\n    '\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_004\n  - plan_006\n  registry_id: head_sensitivity_viz\n  status: DONE\n  conclusion: success\n- id: plan_014\n  claim:\n  - 2\n  description: 'K/V separation: treat K and V heads as independent MCKP items with\n    separate budget allocation. Compare joint K+V optimization vs current uniform\n    K=V approach. RateQuant supports asymmetric K/V (e.g. K=2.85, V=2.15 avg bits)\n    — we should show MCKP naturally handles this.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: kv_separation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    kv_sep_ppl: 11.2162\n    joint_kv_ppl: 10.9131\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_sep_vs_joint: 0.303\n    sep_k_2bit_count: 16\n    sep_v_uniform_4bit: true\n    kv_asymmetric_heads: 21\n- id: plan_012\n  claim:\n  - 1\n  - 2\n  description: 'Downstream task evaluation: ARC-C / HellaSwag / PIQA / WinoGrande\n    on Qwen2.5-7B at 4× compression. Must match RateQuant''s eval suite for direct\n    comparison. Tests whether PPL improvements translate to downstream performance.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  registry_id: downstream_eval_qwen\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    avg_recovery: 0.728\n    arc_c: 0.5137\n    hellaswag: 0.7684\n    piqa: 0.7786\n    winogrande: 0.6819\n    arc_c_delta_pp: 3.16\n    hellaswag_delta_pp: 4\n    piqa_delta_pp: 1.25\n    winogrande_delta_pp: 1.97\n- id: plan_013\n  claim:\n  - 1\n  description: '70B profiling-only: run distortion profiling on Qwen2.5-72B (no full\n    eval). Analyze whether sensitivity patterns (Layer 0 dominance, compounding threshold)\n    scale with model size.\n\n    '\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: qwen72b_profiling\n  model: Qwen2.5-72B\n  status: DONE\n  conclusion: killed\n- id: plan_015\n  claim:\n  - 2\n  description: 'L0-only heuristic baseline: assign 8-bit to all Layer 0 KV heads,\n    uniform 4-bit to all other heads, at 4x compression on Qwen2.5-7B. This is the\n    simplest possible non-uniform strategy exploiting L0 sensitivity. If L0-only matches\n    or beats constrained MCKP, the full optimization machinery is unnecessary. Must\n    also test on Llama and Mistral. Critical missing baseline flagged by Dream review.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: l0_only_heuristic\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: killed\n- id: plan_016\n  claim:\n  - 2\n  description: 'RateQuant greedy + cardinality constraint ablation: add max_2bit=k\n    constraint to RateQuant greedy Algorithm 1 on {2,4,8,16}. Compare three conditions:\n    (a) RateQuant greedy unconstrained (already have: PPL ~32.45), (b) RateQuant greedy\n    + cardinality k=8, (c) constrained MCKP k=8 (already have: PPL ~11.23). If (b)\n    matches (c), the contribution is the cardinality constraint, not the MCKP solver.\n    If (c) beats (b), discrete MCKP optimization genuinely matters. Critical ablation\n    flagged by all three Dream review tiers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_008\n  registry_id: greedy_cardinality_ablation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 11.2312\n    greedy_unconstrained_ppl: 32.4467\n    mckp_constrained_ppl: 11.23\n    delta_vs_mckp: 0.0012\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n- id: plan_017\n  claim:\n  - 1\n  - 2\n  description: 'Multi-seed error bars: run constrained MCKP and uniform 4-bit on Qwen2.5-7B\n    at 4x compression with 3 different calibration sets (different random subsets\n    of WikiText-2 training data). Report mean +/- std for PPL. Required for statistical\n    credibility — Dream review flagged all-single-run as critical gap.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: multi_seed_error_bars\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4454\n    mckp_seed0: 11.0168\n    mckp_seed1: 10.8981\n    mckp_seed2: 11.0487\n    mckp_mean: 10.9878\n    mckp_std: 0.0648\n    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4\n    allocation_agreement_3way: 0.902\n    agreement_s0_s1: 0.946\n    agreement_s0_s2: 0.911\n    agreement_s1_s2: 0.946\n    profile_time_min_per_seed: 65\n- id: plan_018\n  claim:\n  - 2\n  description: 'Runtime/latency benchmark: measure end-to-end inference latency and\n    throughput with mixed-precision KV cache vs uniform 4-bit quantization on Qwen2.5-7B.\n    Include profiling cost breakdown. Dream review flagged missing latency evaluation\n    as significant gap for systems-oriented contribution.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: runtime_benchmark\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16:\n      prefill_ms: 45.86\n      decode_ms_per_tok: 33.78\n      throughput_tok_s: 29.6\n    uniform_4bit:\n      prefill_ms: 54.25\n      decode_ms_per_tok: 42.46\n      throughput_tok_s: 23.6\n    constrained_mckp:\n      prefill_ms: 57.03\n      decode_ms_per_tok: 46.09\n      throughput_tok_s: 21.8\n      mckp_solver_sec: 0.005\n      bit_dist:\n        '2': 8\n        '4': 100\n        '8': 4\n      memory_ratio: 0.25\n    theoretical_memory:\n      bf16_MB: 21\n      4bit_MB: 5.25\n      mckp_MB: 5.25\n      compression_4x: true\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp_004\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p0_2_cliff_1.5B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: p0_2_cliff_7B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: p0_1_ppl_fast\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_a_targeted_hybrid\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_b_hires_quant\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_c_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_c_no2bit\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl: 15.4454\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_vs_uniform: 0\n    memory_ratio: 0.25\n    bit_distribution:\n      '4': 112\n- exp_id: exp_d_no_l0_exclusion\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_e_hires_profile\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    constrained_ppl_bf16: 9.569\n    baseline_ppl_bf16: 8.819\n    exp_c_ppl_bf16: 11.345\n    delta_vs_exp_c: -1.776\n    memory_ratio: 0.25\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    profile_resolution:\n      hires_nonzero_2bit: 100\n      lowres_nonzero_2bit: 37\n      hires_nonzero_4bit: 6\n      lowres_nonzero_4bit: 4\n      total_heads: 112\n    allocation_diff_count: 8\n    profiling_time_min: 65.5\n- exp_id: compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: compounding_sweep_k10_12\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: ratequant_greedy_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: budget_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: c4_cross_dataset_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    c4_mckp_ppl: 11.3285\n    uniform4bit_ppl: 15.4454\n    delta_over_uniform: 4.117\n    allocation_agreement_rate: 0.982\n    n_disagree: 2\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n    wt2_ref_mckp_ppl: 11.2312\n    wt2_ref_delta: 4.2142\n    ppl_gap: 0.097\n- exp_id: llama_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 8.7\n    uniform_4bit_ppl_bf16: 8.47\n    baseline_ppl_bf16: 8.09\n    delta_vs_uniform: -0.23\n    memory_ratio: 0.25\n- exp_id: mistral_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 7.564\n    uniform_4bit_ppl_bf16: 7.131\n    baseline_ppl_bf16: 7.035\n    delta_vs_uniform: -0.433\n    memory_ratio: 0.25\n- exp_id: llama_hires_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 8.0918\n    uniform_4bit_ppl: 8.469\n    lowres_mckp_ppl: 8.6951\n    hires_mckp_ppl: 8.4498\n    hires_improvement_ppl: 0.2453\n    degradation_reduction_pct: 40.7\n    profiling_time_min: 173.4\n    total_time_min: 175.1\n- exp_id: mistral_hires_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl: 7.323\n    uniform_4bit_ppl: 7.131\n    baseline_ppl: 7.035\n    delta_vs_uniform: -0.192\n    memory_ratio: 0.25\n- exp_id: llama_aggressive_compression\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_5.3x_ppl: 57.6\n    uniform_2bit_ppl: 2643.77\n    mckp_8x_ppl: 2372.33\n    uniform_2bit_8x_ppl: 2643.77\n- exp_id: downstream_eval_qwen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    avg_recovery: 0.728\n    arc_c: 0.5137\n    hellaswag: 0.7684\n    piqa: 0.7786\n    winogrande: 0.6819\n    arc_c_delta_pp: 3.16\n    hellaswag_delta_pp: 4\n    piqa_delta_pp: 1.25\n    winogrande_delta_pp: 1.97\n- exp_id: head_sensitivity_viz\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mistral_aggressive_compression\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_5.3x_ppl: 11.912\n    uniform_2bit_ppl: 519.107\n    mckp_8x_ppl: 399.901\n    uniform_2bit_8x_ppl: 519.107\n    baseline_ppl: 7.035\n    uniform_4bit_ppl: 7.131\n    5.3x_bit_dist:\n      '2': 128\n      '4': 128\n    8x_bit_dist:\n      '2': 248\n      '4': 8\n    total_time_seconds: 268.1\n- exp_id: kv_separation\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    kv_sep_ppl: 11.2162\n    joint_kv_ppl: 10.9131\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_sep_vs_joint: 0.303\n    sep_k_2bit_count: 16\n    sep_v_uniform_4bit: true\n    kv_asymmetric_heads: 21\n- exp_id: l0_only_heuristic\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: greedy_cardinality_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 11.2312\n    greedy_unconstrained_ppl: 32.4467\n    mckp_constrained_ppl: 11.23\n    delta_vs_mckp: 0.0012\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n- exp_id: l0_heuristic_baseline\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: greedy_constrained_ablation\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: l0_heuristic_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_constrained_ppl: 11.23\n    l0_random_mean_ppl: 11.69\n    l0_random_std: 0.47\n    naive_positional_ppl: 12.23\n    uniform_4bit_ppl: 15.45\n    qwen_l0_random_median: 11.515\n    qwen_l0_random_seeds:\n    - 11.486\n    - 11.615\n    - 11.325\n    - 11.515\n    - 12.515\n    llama_l0_random_mean: 10.479\n    llama_l0_random_std: 1.033\n    llama_l0_random_median: 10.038\n    llama_l0_random_seeds:\n    - 9.485\n    - 10.488\n    - 9.941\n    - 10.038\n    - 12.444\n    llama_naive_positional: 9.941\n    llama_mckp: 8.4498\n    llama_uniform: 8.469\n    mistral_l0_random_mean: 7.56\n    mistral_l0_random_std: 0.087\n    mistral_l0_random_median: 7.586\n    mistral_l0_random_seeds:\n    - 7.523\n    - 7.61\n    - 7.413\n    - 7.586\n    - 7.669\n    mistral_naive_positional: 7.481\n    mistral_mckp: 7.3106\n    mistral_uniform: 7.131\n- exp_id: qwen_bf16_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 9.8106\n    baseline_fp16_ppl: 9.81\n    delta_baseline: 0.0006\n    uniform4_bf16_ppl: 15.4454\n    uniform4_fp16_ppl: 15.45\n    delta_uniform4: 0.0046\n- exp_id: hires_mckp_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl_bf16: 9.8106\n    mckp_ppl_bf16: 10.9131\n    uniform_4bit_ppl_bf16: 15.4454\n    delta_mckp_vs_baseline: 1.1025\n    delta_mckp_vs_uniform: -4.5323\n    token_count: 298938\n- exp_id: hires_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 9.8106\n    uniform_4bit_bf16_ppl: 15.4454\n    hires_mckp_bf16_ppl: 10.9131\n- exp_id: mistral_k_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 4\n    best_ppl: 7.1648\n    uniform_4bit_ppl: 7.131\n    k4_ppl: 7.1648\n    k8_ppl: 7.1997\n    k12_ppl: 7.2448\n    k16_ppl: 7.3106\n    k18_ppl: 7.3231\n- exp_id: llama_k_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 4\n    best_ppl: 8.4498\n    uniform_4bit_ppl: 8.469\n    k4_ppl: 8.4498\n    k8_ppl: 8.4498\n    k12_ppl: 8.4498\n    k16_ppl: 8.4498\n    k18_ppl: 8.4498\n    natural_2bit_count: 2\n- exp_id: multi_seed_error_bars\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4454\n    mckp_seed0: 11.0168\n    mckp_seed1: 10.8981\n    mckp_seed2: 11.0487\n    mckp_mean: 10.9878\n    mckp_std: 0.0648\n    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4\n    allocation_agreement_3way: 0.902\n    agreement_s0_s1: 0.946\n    agreement_s0_s2: 0.911\n    agreement_s1_s2: 0.946\n    profile_time_min_per_seed: 65\n- exp_id: cross_domain_calibration\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c4_cross_dataset_eval_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cross_domain_calibration_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: runtime_benchmark\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16:\n      prefill_ms: 45.86\n      decode_ms_per_tok: 33.78\n      throughput_tok_s: 29.6\n    uniform_4bit:\n      prefill_ms: 54.25\n      decode_ms_per_tok: 42.46\n      throughput_tok_s: 23.6\n    constrained_mckp:\n      prefill_ms: 57.03\n      decode_ms_per_tok: 46.09\n      throughput_tok_s: 21.8\n      mckp_solver_sec: 0.005\n      bit_dist:\n        '2': 8\n        '4': 100\n        '8': 4\n      memory_ratio: 0.25\n    theoretical_memory:\n      bf16_MB: 21\n      4bit_MB: 5.25\n      mckp_MB: 5.25\n      compression_4x: true\n- exp_id: c4_rerun_d032\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_cal_wt2_eval_mckp_ppl: 11.2942\n    c4_cal_wt2_eval_uniform_ppl: 15.4454\n    c4_cal_wt2_eval_delta: 4.1512\n    c4_cal_bf16_baseline: 12.6505\n    wt2_bf16_baseline: 9.8106\n    allocation_agreement_c4_vs_wt2: 0.964\n    agreement_heads: 108/112\n    bit_dist: 2bit:8, 4bit:100, 8bit:4\n    cross_domain_wt2_to_c4_mckp_ppl: 20.5601\n    cross_domain_wt2_to_c4_uniform_ppl: 35.4232\n    cross_domain_c4_bf16: 15.3246\n    old_contaminated_ppl: 11.3285\n    contamination_impact: 0.0343\n    models_completed: Qwen2.5-7B only\n- exp_id: multi_seed_lowres\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: oracle_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_ppl: 10.9131\n    max_oracle_gap_ppl: 0.0183\n    avg_oracle_gap_ppl: 0.0046\n    layers_mckp_optimal: 5/8\n    layers_with_gap: 3\n    gap_layers:\n      L1: 0.0183\n      L4: 0.0045\n      L11: 0.0136\n    gap_nature: 2-bit head position swap within same bit budget\n    total_evals: 54\n    runtime_min: 21.3\n- exp_id: plan_009_oracle_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: qwen72b_profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: llama_heuristic_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    l0_random_seeds:\n    - 8.5479\n    - 8.7595\n    - 8.624\n    - 8.5721\n    - 8.6192\n    l0_random_mean: 8.6245\n    l0_random_std: 0.0733\n    l0_random_median: 8.6192\n    naive_positional_ppl: 8.5781\n    mckp_ppl: 8.4498\n    uniform_ppl: 8.469\n    baseline_ppl: 8.0918\n    mckp_vs_l0_random_gap: 0.1747\n    mckp_vs_naive_gap: 0.1283\n- exp_id: mistral_heuristic_k4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 7.0351\n    uniform_4bit_ppl: 7.1314\n    mckp_k4_ppl: 7.1648\n    l0_random_seed_0: 7.1882\n    l0_random_seed_1: 7.1995\n    l0_random_seed_2: 7.1723\n    l0_random_seed_3: 7.3577\n    l0_random_seed_4: 7.2875\n    l0_random_mean: 7.2411\n    l0_random_std: 0.0707\n    l0_random_median: 7.1995\n    naive_heuristic_ppl: 7.2105\n    budget_heuristic: 0.2559\n    budget_mckp_k4: 0.248\n- exp_id: llama_c4_cross_dataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wt2_cal_wt2_ppl: 8.4498\n    c4_cal_wt2_ppl: 8.6459\n    uniform_wt2_ppl: 8.469\n    wt2_cal_c4_ppl: 7.654\n    c4_cal_c4_ppl: 7.654\n    uniform_c4_ppl: 7.5351\n    bf16_wt2_ppl: 8.0918\n    bf16_c4_ppl: 7.1333\n    agreement_rate: 0.977\n    agreement_heads: 250/256\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n- exp_id: mistral_c4_cross_dataset\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bf16_wt2_ppl: 7.0351\n    c4_cal_bf16_ppl: 6.9677\n    wt2_cal_mckp_wt2_ppl: 7.1648\n    c4_cal_mckp_wt2_ppl: 7.1859\n    uniform_4bit_wt2_ppl: 7.1314\n    delta_uniform_mckp_wt2_cal: -0.0334\n    delta_uniform_mckp_c4_cal: -0.0546\n    allocation_agreement_c4_vs_wt2: 0.965\n    agreement_heads: 247/256\n    bit_dist_wt2_cal: 2bit:4, 4bit:252\n    bit_dist_c4_cal: 2bit:4, 4bit:251, 8bit:1\n    profile_time_s: 407.7\n    eval_time_s: 349.4\n    total_time_s: 757.1\n- exp_id: gemma2_9b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 8.9\n    mckp_wikitext2_ppl: 9.05\n    uniform4bit_wikitext2_ppl: 9.03\n    mckp_improvement_over_uniform: -0.02\n    top5_concentration: 0.23\n    layer0_dominance_ratio: 1.32\n    best_k: 8\n    best_k_ppl: 9.05\n    verdict: FAIL\n- exp_id: yi15_9b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 7.0157\n    mckp_wikitext2_ppl: 7.3129\n    uniform4bit_wikitext2_ppl: 7.2171\n    mckp_improvement_over_uniform: -0.0958\n    top5_concentration: 0.4934\n    layer0_dominance_ratio: 0.07\n    best_k: 2\n    best_k_ppl: 7.2209\n    gqa_ratio: '8:1'\n    verdict: FAIL\n- exp_id: qwen25-hires-profiling\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_hires_float32_d048\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    float32_hires_top5_concentration: 0.6104\n    bf16_hires_range: 0.59-0.66\n    float32_lowres_concentration: 0.42\n    bf16_bug_impact_on_concentration: 0.01\n    baseline_ppl: 9.81\n    mckp_unconstrained_ppl: 10.95\n    uniform_4bit_ppl: 15.45\n    mckp_bit_dist:\n      '2': 12\n      '4': 96\n      '8': 3\n      '16': 1\n    l0h0_delta: 6.7388\n    l0_4heads_total_share: 0.586\n    claim3_threshold_0.50: PASS\n- exp_id: yi15_hires_float32_profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: yi15_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.7139\n    top5_n_heads: 9\n    baseline_calibration_ppl: 5.888\n    delta_2bit_cv: 8.8991\n    layer0_dominance_ratio: 0.04\n    top1_head: L4H3_delta=13.1236\n    total_hours: 0.96\n- exp_id: qwen_hires_constrained_d049\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    float32_hires_constrained_mckp_ppl: 10.8921\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4484\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    gap_recovery_pct: 80.8\n    top5_concentration: 0.6156\n    top5_concentration_pre_monotonicity: 0.6104\n    bf16_hires_constrained_mckp_ppl: 10.9131\n    delta_f32_vs_bf16: 0.021\n- exp_id: yi15_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hires_mckp_ppl: 7.2181\n    uniform_4bit_ppl: 7.2171\n    baseline_ppl: 7.0157\n    delta_vs_uniform: -0.001\n    bit_distribution:\n      '2': 2\n      '4': 189\n      '8': 1\n    2bit_heads:\n    - L22H1\n    - L24H3\n    8bit_heads:\n    - L6H2\n    L4H3_status: kept_at_4bit\n    std_mckp_k2_ppl: 7.2209\n    std_mckp_k8_ppl: 7.3129\n    hires_concentration: 0.7139\n    L4H3_2bit_delta: 13.12\n    L4H3_4bit_delta: 0.0048\n    L4H3_8bit_delta: 0.004\n- exp_id: llama_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.5749\n    t1_t5: 0.85\n    baseline_ppl: 6.5055\n    top1_head: L2H5_delta=15.2636\n    delta_2bit_cv: 7.7663\n    l0_dominance_ratio: 0.67\n    positive_delta_heads: 254\n    total_heads: 256\n    total_hours: 0.98\n- exp_id: mistral_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: 'ValueError: Unrecognized model - config.json missing model_type field\n      at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3'\n- exp_id: mistral_hires_bf16_2bitonly_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: 'SafetensorError: model-00003-of-00003.safetensors missing, incomplete\n      download'\n- exp_id: mistral_hires_bf16_2bitonly_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: mistral_hires_bf16_2bitonly_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.241\n    top5_n_heads: 12\n    baseline_ppl: 5.8702\n    top1_head: L2H5\n    top1_delta_2bit: 0.3236\n    top2_head: L12H1\n    top2_delta_2bit: 0.1435\n    top3_head: L0H7\n    top3_delta_2bit: 0.1403\n    delta_2bit_mean: 0.020073\n    delta_2bit_std: 0.026278\n    delta_2bit_cv: 1.3091\n    layer0_mean_delta_2bit: 0.034073\n    other_layers_mean_delta_2bit: 0.019621\n    l0_dominance_ratio: 1.74\n    positive_delta_heads: 252\n    total_heads: 256\n    distribution_shape: flat\n    total_hours: 0.94\n    profile_seconds: 3371.7\n- exp_id: llama_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_bf16_ppl: 8.0922\n    hires_mckp_ppl: 8.5042\n    uniform_4bit_ppl: 8.4701\n    std_mckp_reference_ppl: 8.4498\n    mckp_vs_uniform_delta: -0.0341\n    mckp_vs_uniform_pct: -9\n    hires_vs_std_mckp_delta: 0.0544\n    concentration: 0.5749\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n    heads_2bit:\n    - 26,0\n    - 31,7\n    heads_8bit:\n    - 12,3\n    verdict: FAIL\n- exp_id: gemma2_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    concentration_top5pct: 0.2291\n    l0_dominance_ratio: 2.05\n    cv_delta_2bit: 1.2834\n    positive_delta_heads: 310/336\n    top_head: L0H1 delta=0.1906\n    total_time_hours: 1.59\n- exp_id: llama_c4_hires_crossdataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_wt2_ppl: 8.0922\n    bf16_c4_ppl: 7.1333\n    c4_cal_mckp_wt2_ppl: 8.5103\n    c4_cal_mckp_c4_ppl: 7.5351\n    uniform_wt2_ppl: 8.4701\n    uniform_c4_ppl: 7.5351\n    delta_c4_uniform_minus_mckp: 0\n    delta_wt2_uniform_minus_mckp: -0.0402\n    verdict_c4: FAIL\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n    heads_2bit:\n    - 2,3\n    - 24,2\n    heads_8bit:\n    - 31,6\n    total_time_min: 6.3\n    wt2_ref_mckp_ppl: 8.5042\n    wt2_ref_delta: -0.0341\n- exp_id: mistral_c4_hires_crossdataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fp16_ppl: 7.0352\n    c4_mckp_ppl: 7.1774\n    uniform_4bit_ppl: 7.1308\n    mckp_vs_uniform_delta: 0.0466\n    mckp_bit_distribution:\n      '2': 4\n      '4': 250\n      '8': 2\n    phase4_error: 'FileNotFoundError: mistral_k_ablation_results.json'\n- exp_id: w2_unconstrained_baselines\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    note: 2bitonly profiles only - INVALID for reviewer response\n    yi15_ppl: 672.2\n    yi15_ratio: 114\n    llama_ppl: 1219.7\n    llama_ratio: 187\n    mistral_ppl_2bitonly: 47.8\n    mistral_ratio_2bitonly: 8.2\n    mistral_ppl_full: 6.39\n    mistral_ratio_full: 1.09\n    gemma2_ppl: 277.4\n    gemma2_ratio: 37.9\n    budget: 0.25\n    baseline_yi: 5.89\n    baseline_llama: 6.51\n    baseline_mistral: 5.87\n    baseline_gemma2: 7.32\n- exp_id: w9_compounding_scaling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    baseline_ppl: 8.2\n    n1_joint_ppl: 14.94\n    n1_ratio: 1\n    n2_joint_ppl: 42.26\n    n2_ratio: 3.84\n    n4_joint_ppl: 3813.76\n    n4_ratio: 333.3\n    n8_joint_ppl: 3586.42\n    n8_ratio: 282.1\n    n16_joint_ppl: 7286.23\n    n16_ratio: 521.1\n    n32_joint_ppl: 6644.05\n    n32_ratio: 424\n    n64_joint_ppl: 9453.33\n    n64_ratio: 533.3\n    runtime_seconds: 96\n- exp_id: w9_compounding_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.81\n    k1_topk_ppl: 9.826\n    k1_randomk_ppl: 9.887\n    k1_randomk_std: 0.05\n    k4_topk_ppl: 9.849\n    k4_topk_ratio: 0.86\n    k4_randomk_ppl: 10.06\n    k4_randomk_std: 0.06\n    k4_randomk_ratio: 1.24\n    k8_topk_ppl: 10.042\n    k8_topk_ratio: 1.56\n    k8_randomk_ppl: 11.07\n    k8_randomk_std: 0.69\n    k8_randomk_ratio: 1.76\n    k16_topk_ppl: 10.42\n    k16_topk_ratio: 1.56\n    k16_randomk_ppl: 12.91\n    k16_randomk_std: 0.4\n    k16_randomk_ratio: 2.1\n    k32_topk_ppl: 11.604\n    k32_topk_ratio: 1.78\n    k32_randomk_ppl: 18.33\n    k32_randomk_std: 2.53\n    k32_randomk_ratio: 2.73\n    k64_topk_ppl: 22.946\n    k64_topk_ratio: 4.89\n    k64_randomk_ppl: 55.94\n    k64_randomk_std: 9.73\n    k64_randomk_ratio: 8.88\n    runtime_minutes: 16.9\n    note: 'v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking,\n      top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。'\n- exp_id: w2_unconstrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi15_baseline: 7.0157\n    yi15_uniform4: 7.2171\n    yi15_greedy: 7.5615\n    yi15_mckp: 7.5615\n    yi15_n2bit: 22\n    llama_baseline: 8.0922\n    llama_uniform4: 8.4701\n    llama_greedy: 8.6265\n    llama_mckp: 8.6265\n    llama_n2bit: 12\n    mistral_baseline: 7.0352\n    mistral_uniform4: 7.1308\n    mistral_greedy: 7.5733\n    mistral_mckp: 7.5963\n    mistral_n2bit: 42\n    gemma2_baseline: 6.0306\n    gemma2_uniform4: 6.1683\n    gemma2_greedy: 8.8469\n    gemma2_mckp: 8.8469\n    gemma2_n2bit: 106\n    gemma2_eval_method: sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\n    gemma2_greedy_ratio: 1.467\n    gemma2_catastrophic: true\n    gemma2_note: 1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal\n      value\n- exp_id: w3_downstream_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi15_baseline_avg: 0.6912\n    yi15_uniform_avg: 0.6822\n    yi15_mckp_avg: 0.6745\n    yi15_mckp_vs_uniform_pp: -0.77\n    yi15_mckp_vs_baseline_pp: -1.67\n    yi15_baseline:\n      arc_easy: 0.8093\n      arc_challenge: 0.5265\n      hellaswag: 0.5913\n      piqa: 0.7949\n      winogrande: 0.734\n    yi15_uniform:\n      arc_easy: 0.7946\n      arc_challenge: 0.5205\n      hellaswag: 0.5857\n      piqa: 0.7927\n      winogrande: 0.7174\n    yi15_mckp:\n      arc_easy: 0.7854\n      arc_challenge: 0.4881\n      hellaswag: 0.5797\n      piqa: 0.7894\n      winogrande: 0.7301\n    llama_baseline_avg: 0.696\n    llama_uniform_avg: 0.6915\n    llama_mckp_avg: 0.6816\n    llama_mckp_vs_uniform_pp: -0.99\n    llama_mckp_vs_baseline_pp: -1.44\n    llama_baseline:\n      arc_easy: 0.8228\n      arc_challenge: 0.5188\n      hellaswag: 0.6073\n      piqa: 0.7922\n      winogrande: 0.7388\n    llama_uniform:\n      arc_easy: 0.8173\n      arc_challenge: 0.5256\n      hellaswag: 0.6026\n      piqa: 0.7867\n      winogrande: 0.7253\n    llama_mckp:\n      arc_easy: 0.8039\n      arc_challenge: 0.4991\n      hellaswag: 0.6012\n      piqa: 0.7802\n      winogrande: 0.7238\n    mistral_baseline_avg: 0.6917\n    mistral_uniform_avg: 0.6894\n    mistral_mckp_avg: 0.6846\n    mistral_mckp_vs_uniform_pp: -0.48\n    mistral_mckp_vs_baseline_pp: -0.71\n    mistral_baseline:\n      arc_easy: 0.8005\n      arc_challenge: 0.5043\n      hellaswag: 0.6118\n      piqa: 0.8009\n      winogrande: 0.7411\n    mistral_uniform:\n      arc_easy: 0.7976\n      arc_challenge: 0.5068\n      hellaswag: 0.6051\n      piqa: 0.7982\n      winogrande: 0.7395\n    mistral_mckp:\n      arc_easy: 0.7942\n      arc_challenge: 0.4949\n      hellaswag: 0.6027\n      piqa: 0.802\n      winogrande: 0.7293\n    gemma2_baseline_avg: 0.7307\n    gemma2_uniform_avg: 0.7251\n    gemma2_mckp_avg: 0.7265\n    gemma2_mckp_vs_uniform_pp: 0.14\n    gemma2_mckp_vs_baseline_pp: -0.42\n    gemma2_baseline:\n      arc_easy: 0.8737\n      arc_challenge: 0.6135\n      hellaswag: 0.6093\n      piqa: 0.8128\n      winogrande: 0.7443\n    gemma2_uniform:\n      arc_easy: 0.8662\n      arc_challenge: 0.6058\n      hellaswag: 0.606\n      piqa: 0.8079\n      winogrande: 0.7395\n    gemma2_mckp:\n      arc_easy: 0.8649\n      arc_challenge: 0.6041\n      hellaswag: 0.6089\n      piqa: 0.8074\n      winogrande: 0.7474\n    eval_harness_version: 0.4.11\n    num_fewshot: 0\n    yi_elapsed_s: 1563.2\n    llama_elapsed_s: 1446.4\n    mistral_elapsed_s: 1302.2\n    gemma2_elapsed_s: 1735.9\n- exp_id: gemma2_constrained_bos_fix\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: w1_qwen14b_hires_profiling\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T09:26:52.973Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T09:26:52.973Z",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-15T09:26:53.008Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Qwen2.5-14B 不是 Spread 或 MCKP 无效，decision rule 出现 false positive/negative，核心 diagnostic 叙事不成立
核心假设：['Qwen2.5-14B concentration ≥0.50 但 MCKP 无改善（类似 Yi-1.5，diagnostic false positive）', '或 Qwen2.5-14B concentration <0.40（Flat pattern），Qwen 系列只有 7B 是 Spread', 'Decision rule accuracy 降至 4/6 或 5/6 但有 high-confidence failure', 'Gemma-2 BOS fix 显著改变 unconstrained ratio（<1.25 或 >1.60），三档标签需重新校准', 'W9 compounding 数据 non-monotonic 或 variance 掩盖趋势']
关键指标范围：{'qwen14b_mckp_improvement_over_uniform_pct': [-3, 3], 'qwen14b_concentration': [0.3, 0.75], 'qwen14b_t1_t5': [0.4, 0.95], 'decision_rule_accuracy': [4, 5], 'gemma2_constrained_vs_uniform_pct': [-2.0, 2.0], 'gemma2_unconstrained_ratio': [1.15, 1.65], 'w9_k64_randomk_topk_ratio': [1.0, 2.0]}
叙事方向：放弃 "diagnostic/decision rule" 作为核心 contribution，reframe 为三条新主线： (1) **Cardinality constraint as universal safeguard** — 不依赖 diagnostic， 所有 5-6 个模型上 constraint 都 ≤ uniform 或防止 catastrophe， 这是一个 architecture-agnostic 的 practical fix； (2) **Systematic negative result** — "we tested 5+ architectures and found  non-uniform KV cache quantization is beneficial in only 1/5-6 cases"， 这本身是有价值的 finding（saves practitioners time），framing 类似 "Challenging common assumptions about mixed-precision KV cache"； (3) **Compounding effect characterization** — 即使 diagnostic 不成立， discrete non-consecutive bit-width 上 solver 失败的机制分析 （W9 data + Qwen catastrophe）仍是 novel contribution。 三档标签改为纯描述性（按倍数分 tier，不绑定 distribution shape 解释）。 论文标题从 "When Does X Help" 转向 "The Cardinality Constraint You Need  for Hardware-Aligned KV Cache Quantization"。仍投 EMNLP Main Efficient Methods， 但卖点从 analysis 转向 practical method + surprising negative results。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: ratekv
focus: 审稿修订后的 concentration-dependent narrative 是否 hold：(1) 三档标签(catastrophic/moderate/mild)是否自洽 (2) N=1 Spread + empirical decision rule 的 claim 强度是否匹配 EMNLP Main (3) Gemma-2 1.47× 讨论是否充分 (4) W9 super-additive 形式化程度是否足够 (5) 5-model downstream 完整数据下 story 是否比之前更强

## paper_framing.md

# Paper Framing — ratekv

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)
- Track: Efficient Methods for NLP

## bf16 Consistency Resolution (2026-05-14)

**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。

**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。

| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |
|------|---------------------|----------------------|-----------|
| Baseline | **9.8106** | 8.819 | 9.81 |
| Uniform 4-bit | **15.4454** | — | 15.45 |
| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |
| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |

## Core Insight

Per-head KV cache quantization sensitivity varies dramatically across architectures, and the effectiveness of non-uniform mixed-precision allocation is fundamentally determined by the degree of this heterogeneity. We provide both the analysis framework — characterizing when non-uniform quantization helps via per-head sensitivity concentration metrics — and a surprisingly simple method fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding effects from profiler non-additivity and reduces the search space sufficiently that solver choice becomes irrelevant (greedy and MCKP produce identical allocations).

## Core Claims (3 条)

1. **Head sensitivity heterogeneity is architecture-dependent and determined by sensitivity *distribution shape*, not GQA ratio or concentration alone**: Per-KV-head quantization sensitivity is extremely non-uniform within models, but whether MCKP can exploit this heterogeneity depends on the *shape* of the sensitivity distribution, not just its magnitude. Critical counterexample: Yi-1.5-9B (GQA 8:1, concentration 0.71 — the *highest* in our lineup) provides *no benefit* from MCKP (7.22 vs 7.22 uniform), while Qwen2.5-7B (GQA 7:1, concentration 0.61) succeeds (+27.3%). The difference is distribution shape: Qwen has a *cluster* of sensitive heads (Layer 0, 4 heads with cross-bitwidth gradients — "spread" pattern, t₁/t₅=0.57), while Yi-1.5 has a single extreme outlier (L4H3, delta=13.12, t₁/t₅=0.90 — "spike" pattern) with sensitivity at only one bitwidth. A joint diagnostic — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case (Qwen) from all four non-beneficial cases across five architectures. Three shape categories emerge:
   - **Spread** (Qwen): high concentration + low t₁/t₅ → multiple heads with cross-bitwidth gradients → MCKP effective
   - **Spike** (Yi-1.5, Llama): high t₁/t₅ → single outlier dominates → MCKP ineffective
   - **Flat** (Mistral, Gemma-2): low concentration → near-uniform sensitivity → MCKP ineffective (t₁/t₅ irrelevant when concentration < 0.50)

2. **Cardinality constraint is the primary intervention; unconstrained catastrophe is Spread-specific**: On non-consecutive discrete bit-widths {2,4,8,16}, unconstrained allocation produces **catastrophic** results on Spread-heterogeneity architectures (Qwen: greedy 32.45, MCKP 36.92 vs uniform 15.45 = 3.31× baseline) because per-head independent profiling distortions compound non-additively when many heads are simultaneously assigned extreme quantization. On non-Spread architectures, unconstrained allocation causes **mild-to-moderate degradation** (Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.47×) but still underperforms uniform 4-bit in all cases — the solver over-allocates 2-bit heads even when individual distortions appear small. A cardinality constraint (max_2bit≤k) is a simple and sufficient condition: it prevents compounding on Spread models, avoids 2-bit over-allocation on non-Spread models, AND reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce identical bit allocations and PPL (Δ=0.0000, both 11.2312). **Practical implication**: the concentration diagnostic determines whether to invest in MCKP + constraint (Spread models) or simply use uniform 4-bit (non-Spread models — saves solver computation with no quality loss). The profiling benefit beyond the constraint (hires vs lowres) is architecture-dependent: substantial on Spread models (Qwen), marginal on others. The optimal k is determinable via small-scale compounding effect test (plan_004).

**Claim 2 three-pillar support** (Reviewer Q4, new narrative STRENGTHENS Claim 2):
1. Spread models: constraint prevents catastrophe (Qwen 32.45→11.23)
2. Flat models: constraint prevents moderate over-allocation (Gemma-2 8.85→~6.17, 106→8 heads at 2-bit)
3. All models: constraint makes solver choice irrelevant (greedy=MCKP, Δ=0.0000)
This answers "when" and "why", not just "what" — stronger than original "universal catastrophe" narrative.

3. **A joint empirical decision rule correctly separates beneficial from non-beneficial architectures**: Constrained allocation achieves 27.3% PPL improvement on Qwen (spread pattern: concentration 0.61, t₁/t₅=0.57), while providing no benefit on Yi-1.5 (spike: 0.71, t₁/t₅=0.90, ≈0%), Llama (spike: 0.34, t₁/t₅=0.71, +0.2%), Mistral (flat: 0.22, t₁/t₅=0.18, -0.4%), and Gemma-2 (flat: 0.23, t₁/t₅=0.38, -0.3%). The joint condition — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case from all four non-beneficial cases across five architectures (5/5 accuracy). Concentration alone fails: Yi-1.5 (0.71) exceeds Qwen (0.61) yet gains nothing, because its spike pattern (single outlier, no cross-bitwidth gradient) cannot be exploited. Under aggressive compression (≥5×), constrained allocation prevents catastrophic collapse even on non-beneficial architectures (Llama 5.3×: constrained PPL 57.60 vs uniform 2-bit 2644). This provides practitioners an empirical decision rule for when to invest in mixed-precision KV cache quantization. **Claim strength note (Reviewer-verified)**: N=1 Spread → position as "empirical decision rule", NOT "diagnostic framework". If Qwen2.5-14B also confirms Spread → upgrade to "empirical diagnostic" (N=2).

## Story Spine

- **Problem**: KV cache quantization typically applies uniform bit-width across all heads. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but two fundamental questions remain unanswered: (1) *when* does non-uniform allocation actually help — i.e., under what architectural and compression conditions does the added complexity pay off? (2) *how* to make existing allocation algorithms (greedy, MCKP) work correctly on hardware-aligned discrete bit-widths {2,4,8,16} where they currently fail catastrophically?

- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via continuous closed-form (Theorem 2) and discrete greedy (Algorithm 1, optimal on consecutive integers {2,...,6} per Proposition 6). However, on hardware-aligned non-consecutive sets {2,4,8,16}, RateQuant's greedy produces PPL 32.45 (vs optimal ~11.23) — the polymatroid structure that guarantees greedy optimality breaks. Moreover, unconstrained MCKP fares even worse (PPL 36.92) due to compounding effects from profiler non-additivity. Critically, neither RateQuant nor ARKV addresses *when* non-uniform allocation is beneficial.

- **Our framing**: We present a systematic study of per-head KV cache quantization sensitivity across architectures and identify a surprisingly simple fix for the failure of existing algorithms on hardware-aligned bit-widths: a cardinality constraint limiting the number of heads assigned to extreme quantization levels. This single intervention (a) prevents compounding effects, (b) reduces the search space to where solver choice is irrelevant — greedy and MCKP produce identical optimal allocations, and (c) can be parameterized via a small-scale compounding test. Beyond the method, we establish that the benefit of non-uniform allocation is architecture-dependent and quantifiable via an empirical decision rule (concentration + distribution shape), providing practitioners a two-metric check for when mixed-precision is worthwhile.

- **Headline result template**: "We show that the benefit of non-uniform per-head KV cache quantization is concentration-dependent: on spread-heterogeneity architectures (Qwen, concentration 0.61), unconstrained solvers fail catastrophically (PPL 32-37 vs uniform 15.45), while a cardinality constraint (≤k heads at 2-bit) achieves 27.3% PPL improvement with identical results from greedy and MCKP (Δ=0.0000). On non-spread architectures (4 models, 1.07-1.47× baseline), unconstrained solvers cause only mild degradation, and constrained MCKP offers no benefit over uniform 4-bit at either PPL or downstream task level (<1pp avg). An empirical decision rule (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly separates the beneficial case from all four non-beneficial cases (5/5 accuracy) at both PPL and downstream task level, providing practitioners a two-metric check to determine whether mixed-precision KV cache quantization is worthwhile — or whether uniform quantization suffices."

## "When Does Non-Uniform Allocation Help?" — Analysis Chapter

Five case studies representing the full spectrum of heterogeneity:

| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |
|------|-------|-----|--------------|------------------------------|---------------|
| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; "spread" pattern (L0 cluster, 4 heads, 26× dominance) |
| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; "spike" pattern (L4H3 single outlier, 34% of total delta) |
| **Marginal** | Llama-3.1-8B | 4:1 | 0.34-0.59 | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |
| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |
| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |

**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.

**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).

**Joint diagnostic** (n=5, 5/5 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike) and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.

## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)

| Method | PPL | Bit Distribution | Budget |
|--------|-----|-------------------|--------|
| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |
| MCKP unconstrained | 36.92 | — | 0.25 |
| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |

Key takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.

## Cross-Architecture Evidence Summary

| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |
|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|
| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |
| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |
| Llama-3.1-8B | 4:1 | 256 | 0.57 (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (borderline t₁/t₅=0.71) | ≈ Marginal |
| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |
| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |

**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:
- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding
- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta
- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)
- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads

**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):

Three-tier labeling (NOT binary catastrophe/benign):
- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding
- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions
- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)

Reviewer-suggested paragraph for paper (1 段, 3-4 句):
"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape."

This **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.

⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.

**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.

**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.

### Mistral k Ablation (256 KV heads, budget=0.25)

PPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).

| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |
|---|-----|-------|-------|-------|--------|-----|
| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |
| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |
| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |
| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |
| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |
| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |

Contrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.

### Llama k Ablation (256 KV heads, budget=0.25)

All k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).

### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)

**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅

| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |
|------|---------------|------------|---|---------------|
| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |
| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |
| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |
| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |
| **Avg recovery** | — | — | **72.8%** | — |

**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)

| Task | Uniform 4-bit | MCKP (k=8) | Δ |
|------|---------------|------------|---|
| arc_easy | 0.7946 | 0.7854 | -0.92pp |
| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |
| hellaswag | 0.5857 | 0.5797 | -0.60pp |
| piqa | 0.7927 | 0.7894 | -0.33pp |
| winogrande | 0.7174 | 0.7301 | +1.27pp |
| **Average** | **0.6822** | **0.6745** | **-0.77pp** |

**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)

| Task | Uniform 4-bit | MCKP (k=8) | Δ |
|------|---------------|------------|---|
| arc_easy | 0.8173 | 0.8039 | -1.34pp |
| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |
| hellaswag | 0.6026 | 0.6012 | -0.14pp |
| piqa | 0.7867 | 0.7802 | -0.65pp |
| winogrande | 0.7253 | 0.7238 | -0.15pp |
| **Average** | **0.6915** | **0.6816** | **-0.99pp** |

**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)

| Task | Uniform 4-bit | MCKP (k=4) | Δ |
|------|---------------|------------|---|
| arc_easy | — | — | — |
| arc_challenge | — | — | — |
| hellaswag | — | — | — |
| piqa | — | — | — |
| winogrande | — | — | — |
| **Average** | **0.6894** | **0.6846** | **-0.48pp** |

**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)

| Task | Uniform 4-bit | MCKP | Δ |
|------|---------------|------|---|
| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |

**Downstream summary (Reviewer-verified framing)**:
- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**
- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)
- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)
- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise
- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)
- **Paper must**: (a) report full per-task tables, not just averages, (b) use "shows minor degradation" NOT "preserves accuracy" — the latter has spin, (c) note arc_challenge as worst-case explicitly
- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance
- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论："ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate."
- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞："Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge)."

## Allocation Baseline Evidence (plan_015, mckp_reeval)

All numbers from unified bf16 eval pipeline, budget=0.25.

| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |
|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|
| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |
| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |
| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |

**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.

**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.

## Differentiation from RateQuant

| Aspect | RateQuant | Ours |
|--------|-----------|------|
| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |
| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |
| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |
| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |
| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |
| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |
| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |

## Venue Fit Risks

- **"The constraint is just a heuristic, not a real contribution"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.
- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.
- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive "higher GQA = more benefit" hypothesis and shows our diagnostic is needed.
- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 5/5 correct). The "spike vs spread" analysis explains WHY same-GQA models differ.
- **Statistical power**: n=5 models is directional evidence, not statistical claim. Do NOT claim "significant correlation" — use "consistent pattern across 5 architectures" or "5/5 correctly classified by the 0.50 threshold."
- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.

## Anticipated Reviewer Concerns

1. **"The cardinality constraint is trivial — just cap the extreme allocations"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.
2. **"This is just RateQuant with a constraint added"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.
3. **"The method only works on Qwen — isn't this a Qwen paper?"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.
4. **"How does this work at different compression ratios?"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.
5. **"n=3/4/5 models is not enough for the heterogeneity claim"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.
6. **"RateQuant does K/V asymmetric allocation, do you?"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.
7. **"Where are the downstream task results?"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use "shows minor degradation" not "preserves accuracy".
8. **"The profiler distortion=0.0 on Mistral suggests the profiling method is broken"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.
9. **"If solver doesn't matter, why present MCKP at all?"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.


## experiment_plan (with registry status)

- id: plan_001
  claim:
  - 2
  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.
    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.
    Strengthens narrative: "solver automatically discovers sensitivity structure."

    '
  priority: P0
  gpu_budget_hours: 1
  deps: []
  registry_id: exp_d_no_l0_exclusion
  model: Qwen2.5-7B
  eval: WikiText-2
  status: DONE
  conclusion: success
- id: plan_002
  claim:
  - 1
  - 2
  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).
    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability
    across different GQA ratios and architectures. Fallback if HF token unavailable:
    Yi-1.5-9B (non-gated, similar scale).

    '
  priority: P0
  gpu_budget_hours: 4
  deps: []
  registry_id: llama_full_pipeline
  model: Llama-3.1-8B
  fallback_model: Yi-1.5-9B
  eval: WikiText-2
  status: DONE
  conclusion: negative
  metrics:
    mckp_ppl_bf16: 8.7
    uniform_4bit_ppl_bf16: 8.47
    baseline_ppl_bf16: 8.09
    delta_vs_uniform: -0.23
    memory_ratio: 0.25
- id: plan_003
  claim:
  - 1
  - 2
  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture
    family to establish cross-architecture validity.

    '
  priority: P0
  gpu_budget_hours: 4
  deps: []
  registry_id: mistral_full_pipeline
  model: Mistral-7B-v0.3
  eval: WikiText-2
  status: DONE
  conclusion: negative
  metrics:
    mckp_ppl_bf16: 7.564
    uniform_4bit_ppl_bf16: 7.131
    baseline_ppl_bf16: 7.035
    delta_vs_uniform: -0.433
    memory_ratio: 0.25
- id: plan_004
  claim:
  - 3
  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112
    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map
    the compounding threshold. Establishes the principled basis for cardinality constraint
    selection.

    '
  priority: P0
  gpu_budget_hours: 3
  deps: []
  registry_id: compounding_sweep
  model: Qwen2.5-7B
  eval: WikiText-2
  status: DONE
  conclusion: success
- id: plan_005
  claim:
  - 2
  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,
    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline
    at same budget.

    '
  priority: P0
  gpu_budget_hours: 3
  deps: []
  registry_id: budget_sweep
  model: Qwen2.5-7B
  eval: WikiText-2
  status: DONE
  conclusion: success
- id: plan_006
  claim:
  - 1
  - 2
  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).
    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers
    mid-layer heterogeneity and improves solver allocation beyond current results.

    '
  priority: P0
  gpu_budget_hours: 3
  deps: []
  registry_id: exp_e_hires_profile
  model: Qwen2.5-7B
  eval: WikiText-2
  status: DONE
  conclusion: success
  metrics:
    constrained_ppl_bf16: 9.569
    baseline_ppl_bf16: 8.819
    exp_c_ppl_bf16: 11.345
    delta_vs_exp_c: -1.776
    memory_ratio: 0.25
    bit_distribution:
      '2': 8
      '4': 100
      '8': 4
    profile_resolution:
      hires_nonzero_2bit: 100
      lowres_nonzero_2bit: 37
      hires_nonzero_4bit: 6
      lowres_nonzero_4bit: 4
      total_heads: 112
    allocation_diff_count: 8
    profiling_time_min: 65.5
- id: plan_007
  claim:
  - 1
  - 2
  - 3
  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.
    Cross-dataset evaluation to show results are not WikiText-2 specific.

    '
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: c4_rerun_d032
  model: Qwen2.5-7B
  eval: C4
  status: DONE
  conclusion: success
  metrics: &id001
    c4_cal_wt2_eval_mckp_ppl: 11.2942
    c4_cal_wt2_eval_uniform_ppl: 15.4454
    c4_cal_wt2_eval_delta: 4.1512
    c4_cal_bf16_baseline: 12.6505
    wt2_bf16_baseline: 9.8106
    allocation_agreement_c4_vs_wt2: 0.964
    agreement_heads: 108/112
    bit_dist: 2bit:8, 4bit:100, 8bit:4
    cross_domain_wt2_to_c4_mckp_ppl: 20.5601
    cross_domain_wt2_to_c4_uniform_ppl: 35.4232
    cross_domain_c4_bf16: 15.3246
    old_contaminated_ppl: 11.3285
    contamination_impact: 0.0343
    models_completed: Qwen2.5-7B only
- id: plan_008
  claim:
  - 2
  description: 'RateQuant comparison: implement RateQuant''s greedy algorithm (Algorithm
    1) on our discrete action set {2,4,8,16}-bit. RateQuant''s Prop. 6 optimality
    relies on consecutive-integer polymatroid structure which breaks on non-consecutive
    sets. Show greedy produces suboptimal allocation vs constrained MCKP. Critical
    for differentiation claim — must have experimental evidence.

    '
  priority: P0
  gpu_budget_hours: 4
  deps: []
  registry_id: ratequant_greedy_comparison
  model: Qwen2.5-7B
  eval: WikiText-2
  status: DONE
  conclusion: success
- id: plan_009
  claim:
  - 2
  description: 'Oracle comparison: brute-force optimal allocation on a subset (3-4
    layer groups) of Qwen2.5-7B. Quantify MCKP gap to oracle.

    '
  priority: P1
  gpu_budget_hours: 6
  deps:
  - plan_006
  registry_id: oracle_comparison
  model: Qwen2.5-7B
  status: DONE
  conclusion: success
  metrics:
    mckp_ppl: 10.9131
    max_oracle_gap_ppl: 0.0183
    avg_oracle_gap_ppl: 0.0046
    layers_mckp_optimal: 5/8
    layers_with_gap: 3
    gap_layers:
      L1: 0.0183
      L4: 0.0045
      L11: 0.0136
    gap_nature: 2-bit head position swap within same bit budget
    total_evals: 54
    runtime_min: 21.3
- id: plan_010
  claim:
  - 2
  description: 'Cross-domain calibration robustness: calibrate on C4, evaluate on
    WikiText-2 (and vice versa). Report per-head allocation agreement rate across
    calibration sources.

    '
  priority: P1
  gpu_budget_hours: 2
  deps:
  - plan_007
  registry_id: c4_rerun_d032
  model: Qwen2.5-7B
  status: DONE
  conclusion: success
  metrics: *id001
- id: plan_011
  claim:
  - 1
  description: 'Head sensitivity visualization: generate paper-quality figures showing
    per-head profiling delta heatmap across layers, compounding effect curve, and
    budget allocation comparison chart.

    '
  priority: P1
  gpu_budget_hours: 1
  deps:
  - plan_004
  - plan_006
  registry_id: head_sensitivity_viz
  status: DONE
  conclusion: success
- id: plan_014
  claim:
  - 2
  description: 'K/V separation: treat K and V heads as independent MCKP items with
    separate budget allocation. Compare joint K+V optimization vs current uniform
    K=V approach. RateQuant supports asymmetric K/V (e.g. K=2.85, V=2.15 avg bits)
    — we should show MCKP naturally handles this.

    '
  priority: P1
  gpu_budget_hours: 3
  deps: []
  registry_id: kv_separation
  model: Qwen2.5-7B
  eval: WikiText-2
  status: DONE
  conclusion: negative
  metrics:
    kv_sep_ppl: 11.2162
    joint_kv_ppl: 10.9131
    uniform_4bit_ppl: 15.4454
    baseline_ppl: 9.8106
    delta_sep_vs_joint: 0.303
    sep_k_2bit_count: 16
    sep_v_uniform_4bit: true
    kv_asymmetric_heads: 21
- id: plan_012
  claim:
  - 1
  - 2
  description: 'Downstream task evaluation: ARC-C / HellaSwag / PIQA / WinoGrande
    on Qwen2.5-7B at 4× compression. Must match RateQuant''s eval suite for direct
    comparison. Tests whether PPL improvements translate to downstream performance.

    '
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan_005
  registry_id: downstream_eval_qwen
  model: Qwen2.5-7B
  status: DONE
  conclusion: success
  metrics:
    avg_recovery: 0.728
    arc_c: 0.5137
    hellaswag: 0.7684
    piqa: 0.7786
    winogrande: 0.6819
    arc_c_delta_pp: 3.16
    hellaswag_delta_pp: 4
    piqa_delta_pp: 1.25
    winogrande_delta_pp: 1.97
- id: plan_013
  claim:
  - 1
  description: '70B profiling-only: run distortion profiling on Qwen2.5-72B (no full
    eval). Analyze whether sensitivity patterns (Layer 0 dominance, compounding threshold)
    scale with model size.

    '
  priority: P1
  gpu_budget_hours: 4
  deps: []
  registry_id: qwen72b_profiling
  model: Qwen2.5-72B
  status: DONE
  conclusion: killed
- id: plan_015
  claim:
  - 2
  description: 'L0-only heuristic baseline: assign 8-bit to all Layer 0 KV heads,
    uniform 4-bit to all other heads, at 4x compression on Qwen2.5-7B. This is the
    simplest possible non-uniform strategy exploiting L0 sensitivity. If L0-only matches
    or beats constrained MCKP, the full optimization machinery is unnecessary. Must
    also test on Llama and Mistral. Critical missing baseline flagged by Dream review.

    '
  priority: P0
  gpu_budget_hours: 1
  deps: []
  registry_id: l0_only_heuristic
  model: Qwen2.5-7B
  eval: WikiText-2
  status: DONE
  conclusion: killed
- id: plan_016
  claim:
  - 2
  description: 'RateQuant greedy + cardinality constraint ablation: add max_2bit=k
    constraint to RateQuant greedy Algorithm 1 on {2,4,8,16}. Compare three conditions:
    (a) RateQuant greedy unconstrained (already have: PPL ~32.45), (b) RateQuant greedy
    + cardinality k=8, (c) constrained MCKP k=8 (already have: PPL ~11.23). If (b)
    matches (c), the contribution is the cardinality constraint, not the MCKP solver.
    If (c) beats (b), discrete MCKP optimization genuinely matters. Critical ablation
    flagged by all three Dream review tiers.

    '
  priority: P0
  gpu_budget_hours: 2
  deps:
  - plan_008
  registry_id: greedy_cardinality_ablation
  model: Qwen2.5-7B
  eval: WikiText-2
  status: DONE
  conclusion: success
  metrics:
    greedy_constrained_ppl: 11.2312
    greedy_unconstrained_ppl: 32.4467
    mckp_constrained_ppl: 11.23
    delta_vs_mckp: 0.0012
    bit_distribution:
      '2': 8
      '4': 100
      '8': 4
    memory_ratio: 0.25
- id: plan_017
  claim:
  - 1
  - 2
  description: 'Multi-seed error bars: run constrained MCKP and uniform 4-bit on Qwen2.5-7B
    at 4x compression with 3 different calibration sets (different random subsets
    of WikiText-2 training data). Report mean +/- std for PPL. Required for statistical
    credibility — Dream review flagged all-single-run as critical gap.

    '
  priority: P1
  gpu_budget_hours: 3
  deps: []
  registry_id: multi_seed_error_bars
  model: Qwen2.5-7B
  eval: WikiText-2
  status: DONE
  conclusion: success
  metrics:
    baseline_ppl: 9.8106
    uniform_4bit_ppl: 15.4454
    mckp_seed0: 11.0168
    mckp_seed1: 10.8981
    mckp_seed2: 11.0487
    mckp_mean: 10.9878
    mckp_std: 0.0648
    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4
    allocation_agreement_3way: 0.902
    agreement_s0_s1: 0.946
    agreement_s0_s2: 0.911
    agreement_s1_s2: 0.946
    profile_time_min_per_seed: 65
- id: plan_018
  claim:
  - 2
  description: 'Runtime/latency benchmark: measure end-to-end inference latency and
    throughput with mixed-precision KV cache vs uniform 4-bit quantization on Qwen2.5-7B.
    Include profiling cost breakdown. Dream review flagged missing latency evaluation
    as significant gap for systems-oriented contribution.

    '
  priority: P1
  gpu_budget_hours: 2
  deps: []
  registry_id: runtime_benchmark
  model: Qwen2.5-7B
  status: DONE
  conclusion: success
  metrics:
    baseline_bf16:
      prefill_ms: 45.86
      decode_ms_per_tok: 33.78
      throughput_tok_s: 29.6
    uniform_4bit:
      prefill_ms: 54.25
      decode_ms_per_tok: 42.46
      throughput_tok_s: 23.6
    constrained_mckp:
      prefill_ms: 57.03
      decode_ms_per_tok: 46.09
      throughput_tok_s: 21.8
      mckp_solver_sec: 0.005
      bit_dist:
        '2': 8
        '4': 100
        '8': 4
      memory_ratio: 0.25
    theoretical_memory:
      bf16_MB: 21
      4bit_MB: 5.25
      mckp_MB: 5.25
      compression_4x: true


## registry (completed experiments)

- exp_id: mvp_001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sanity_001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_002
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sanity_002
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_003
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sanity_003
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sanity_004
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mvp_004
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: p0_2_cliff_1.5B
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: p0_2_cliff_7B
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: p0_1_ppl_fast
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: exp_a_targeted_hybrid
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: exp_b_hires_quant
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: exp_c_constrained_mckp
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_c_no2bit
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    mckp_ppl: 15.4454
    uniform_4bit_ppl: 15.4454
    baseline_ppl: 9.8106
    delta_vs_uniform: 0
    memory_ratio: 0.25
    bit_distribution:
      '4': 112
- exp_id: exp_d_no_l0_exclusion
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_e_hires_profile
  name: ''
  status: DONE
  conclusion: success
  metrics:
    constrained_ppl_bf16: 9.569
    baseline_ppl_bf16: 8.819
    exp_c_ppl_bf16: 11.345
    delta_vs_exp_c: -1.776
    memory_ratio: 0.25
    bit_distribution:
      '2': 8
      '4': 100
      '8': 4
    profile_resolution:
      hires_nonzero_2bit: 100
      lowres_nonzero_2bit: 37
      hires_nonzero_4bit: 6
      lowres_nonzero_4bit: 4
      total_heads: 112
    allocation_diff_count: 8
    profiling_time_min: 65.5
- exp_id: compounding_sweep
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: compounding_sweep_k10_12
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: ratequant_greedy_comparison
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: budget_sweep
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: c4_cross_dataset_eval
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    c4_mckp_ppl: 11.3285
    uniform4bit_ppl: 15.4454
    delta_over_uniform: 4.117
    allocation_agreement_rate: 0.982
    n_disagree: 2
    bit_distribution:
      '2': 8
      '4': 100
      '8': 4
    memory_ratio: 0.25
    wt2_ref_mckp_ppl: 11.2312
    wt2_ref_delta: 4.2142
    ppl_gap: 0.097
- exp_id: llama_full_pipeline
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    mckp_ppl_bf16: 8.7
    uniform_4bit_ppl_bf16: 8.47
    baseline_ppl_bf16: 8.09
    delta_vs_uniform: -0.23
    memory_ratio: 0.25
- exp_id: mistral_full_pipeline
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    mckp_ppl_bf16: 7.564
    uniform_4bit_ppl_bf16: 7.131
    baseline_ppl_bf16: 7.035
    delta_vs_uniform: -0.433
    memory_ratio: 0.25
- exp_id: llama_hires_pipeline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_ppl: 8.0918
    uniform_4bit_ppl: 8.469
    lowres_mckp_ppl: 8.6951
    hires_mckp_ppl: 8.4498
    hires_improvement_ppl: 0.2453
    degradation_reduction_pct: 40.7
    profiling_time_min: 173.4
    total_time_min: 175.1
- exp_id: mistral_hires_pipeline
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    mckp_ppl: 7.323
    uniform_4bit_ppl: 7.131
    baseline_ppl: 7.035
    delta_vs_uniform: -0.192
    memory_ratio: 0.25
- exp_id: llama_aggressive_compression
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mckp_5.3x_ppl: 57.6
    uniform_2bit_ppl: 2643.77
    mckp_8x_ppl: 2372.33
    uniform_2bit_8x_ppl: 2643.77
- exp_id: downstream_eval_qwen
  name: ''
  status: DONE
  conclusion: success
  metrics:
    avg_recovery: 0.728
    arc_c: 0.5137
    hellaswag: 0.7684
    piqa: 0.7786
    winogrande: 0.6819
    arc_c_delta_pp: 3.16
    hellaswag_delta_pp: 4
    piqa_delta_pp: 1.25
    winogrande_delta_pp: 1.97
- exp_id: head_sensitivity_viz
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mistral_aggressive_compression
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mckp_5.3x_ppl: 11.912
    uniform_2bit_ppl: 519.107
    mckp_8x_ppl: 399.901
    uniform_2bit_8x_ppl: 519.107
    baseline_ppl: 7.035
    uniform_4bit_ppl: 7.131
    5.3x_bit_dist:
      '2': 128
      '4': 128
    8x_bit_dist:
      '2': 248
      '4': 8
    total_time_seconds: 268.1
- exp_id: kv_separation
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    kv_sep_ppl: 11.2162
    joint_kv_ppl: 10.9131
    uniform_4bit_ppl: 15.4454
    baseline_ppl: 9.8106
    delta_sep_vs_joint: 0.303
    sep_k_2bit_count: 16
    sep_v_uniform_4bit: true
    kv_asymmetric_heads: 21
- exp_id: l0_only_heuristic
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: greedy_cardinality_ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    greedy_constrained_ppl: 11.2312
    greedy_unconstrained_ppl: 32.4467
    mckp_constrained_ppl: 11.23
    delta_vs_mckp: 0.0012
    bit_distribution:
      '2': 8
      '4': 100
      '8': 4
    memory_ratio: 0.25
- exp_id: l0_heuristic_baseline
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: greedy_constrained_ablation
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: l0_heuristic_corrected
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mckp_constrained_ppl: 11.23
    l0_random_mean_ppl: 11.69
    l0_random_std: 0.47
    naive_positional_ppl: 12.23
    uniform_4bit_ppl: 15.45
    qwen_l0_random_median: 11.515
    qwen_l0_random_seeds:
    - 11.486
    - 11.615
    - 11.325
    - 11.515
    - 12.515
    llama_l0_random_mean: 10.479
    llama_l0_random_std: 1.033
    llama_l0_random_median: 10.038
    llama_l0_random_seeds:
    - 9.485
    - 10.488
    - 9.941
    - 10.038
    - 12.444
    llama_naive_positional: 9.941
    llama_mckp: 8.4498
    llama_uniform: 8.469
    mistral_l0_random_mean: 7.56
    mistral_l0_random_std: 0.087
    mistral_l0_random_median: 7.586
    mistral_l0_random_seeds:
    - 7.523
    - 7.61
    - 7.413
    - 7.586
    - 7.669
    mistral_naive_positional: 7.481
    mistral_mckp: 7.3106
    mistral_uniform: 7.131
- exp_id: qwen_bf16_reeval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_bf16_ppl: 9.8106
    baseline_fp16_ppl: 9.81
    delta_baseline: 0.0006
    uniform4_bf16_ppl: 15.4454
    uniform4_fp16_ppl: 15.45
    delta_uniform4: 0.0046
- exp_id: hires_mckp_reeval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_ppl_bf16: 9.8106
    mckp_ppl_bf16: 10.9131
    uniform_4bit_ppl_bf16: 15.4454
    delta_mckp_vs_baseline: 1.1025
    delta_mckp_vs_uniform: -4.5323
    token_count: 298938
- exp_id: hires_reeval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_bf16_ppl: 9.8106
    uniform_4bit_bf16_ppl: 15.4454
    hires_mckp_bf16_ppl: 10.9131
- exp_id: mistral_k_ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_k: 4
    best_ppl: 7.1648
    uniform_4bit_ppl: 7.131
    k4_ppl: 7.1648
    k8_ppl: 7.1997
    k12_ppl: 7.2448
    k16_ppl: 7.3106
    k18_ppl: 7.3231
- exp_id: llama_k_ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_k: 4
    best_ppl: 8.4498
    uniform_4bit_ppl: 8.469
    k4_ppl: 8.4498
    k8_ppl: 8.4498
    k12_ppl: 8.4498
    k16_ppl: 8.4498
    k18_ppl: 8.4498
    natural_2bit_count: 2
- exp_id: multi_seed_error_bars
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_ppl: 9.8106
    uniform_4bit_ppl: 15.4454
    mckp_seed0: 11.0168
    mckp_seed1: 10.8981
    mckp_seed2: 11.0487
    mckp_mean: 10.9878
    mckp_std: 0.0648
    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4
    allocation_agreement_3way: 0.902
    agreement_s0_s1: 0.946
    agreement_s0_s2: 0.911
    agreement_s1_s2: 0.946
    profile_time_min_per_seed: 65
- exp_id: cross_domain_calibration
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: c4_cross_dataset_eval_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cross_domain_calibration_v2
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: runtime_benchmark
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_bf16:
      prefill_ms: 45.86
      decode_ms_per_tok: 33.78
      throughput_tok_s: 29.6
    uniform_4bit:
      prefill_ms: 54.25
      decode_ms_per_tok: 42.46
      throughput_tok_s: 23.6
    constrained_mckp:
      prefill_ms: 57.03
      decode_ms_per_tok: 46.09
      throughput_tok_s: 21.8
      mckp_solver_sec: 0.005
      bit_dist:
        '2': 8
        '4': 100
        '8': 4
      memory_ratio: 0.25
    theoretical_memory:
      bf16_MB: 21
      4bit_MB: 5.25
      mckp_MB: 5.25
      compression_4x: true
- exp_id: c4_rerun_d032
  name: ''
  status: DONE
  conclusion: success
  metrics:
    c4_cal_wt2_eval_mckp_ppl: 11.2942
    c4_cal_wt2_eval_uniform_ppl: 15.4454
    c4_cal_wt2_eval_delta: 4.1512
    c4_cal_bf16_baseline: 12.6505
    wt2_bf16_baseline: 9.8106
    allocation_agreement_c4_vs_wt2: 0.964
    agreement_heads: 108/112
    bit_dist: 2bit:8, 4bit:100, 8bit:4
    cross_domain_wt2_to_c4_mckp_ppl: 20.5601
    cross_domain_wt2_to_c4_uniform_ppl: 35.4232
    cross_domain_c4_bf16: 15.3246
    old_contaminated_ppl: 11.3285
    contamination_impact: 0.0343
    models_completed: Qwen2.5-7B only
- exp_id: multi_seed_lowres
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: oracle_comparison
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mckp_ppl: 10.9131
    max_oracle_gap_ppl: 0.0183
    avg_oracle_gap_ppl: 0.0046
    layers_mckp_optimal: 5/8
    layers_with_gap: 3
    gap_layers:
      L1: 0.0183
      L4: 0.0045
      L11: 0.0136
    gap_nature: 2-bit head position swap within same bit budget
    total_evals: 54
    runtime_min: 21.3
- exp_id: plan_009_oracle_comparison
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: qwen72b_profiling
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: llama_heuristic_k2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    l0_random_seeds:
    - 8.5479
    - 8.7595
    - 8.624
    - 8.5721
    - 8.6192
    l0_random_mean: 8.6245
    l0_random_std: 0.0733
    l0_random_median: 8.6192
    naive_positional_ppl: 8.5781
    mckp_ppl: 8.4498
    uniform_ppl: 8.469
    baseline_ppl: 8.0918
    mckp_vs_l0_random_gap: 0.1747
    mckp_vs_naive_gap: 0.1283
- exp_id: mistral_heuristic_k4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_bf16_ppl: 7.0351
    uniform_4bit_ppl: 7.1314
    mckp_k4_ppl: 7.1648
    l0_random_seed_0: 7.1882
    l0_random_seed_1: 7.1995
    l0_random_seed_2: 7.1723
    l0_random_seed_3: 7.3577
    l0_random_seed_4: 7.2875
    l0_random_mean: 7.2411
    l0_random_std: 0.0707
    l0_random_median: 7.1995
    naive_heuristic_ppl: 7.2105
    budget_heuristic: 0.2559
    budget_mckp_k4: 0.248
- exp_id: llama_c4_cross_dataset
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    wt2_cal_wt2_ppl: 8.4498
    c4_cal_wt2_ppl: 8.6459
    uniform_wt2_ppl: 8.469
    wt2_cal_c4_ppl: 7.654
    c4_cal_c4_ppl: 7.654
    uniform_c4_ppl: 7.5351
    bf16_wt2_ppl: 8.0918
    bf16_c4_ppl: 7.1333
    agreement_rate: 0.977
    agreement_heads: 250/256
    bit_distribution:
      '2': 2
      '4': 253
      '8': 1
- exp_id: mistral_c4_cross_dataset
  name: ''
  status: DONE
  conclusion: success
  metrics:
    bf16_wt2_ppl: 7.0351
    c4_cal_bf16_ppl: 6.9677
    wt2_cal_mckp_wt2_ppl: 7.1648
    c4_cal_mckp_wt2_ppl: 7.1859
    uniform_4bit_wt2_ppl: 7.1314
    delta_uniform_mckp_wt2_cal: -0.0334
    delta_uniform_mckp_c4_cal: -0.0546
    allocation_agreement_c4_vs_wt2: 0.965
    agreement_heads: 247/256
    bit_dist_wt2_cal: 2bit:4, 4bit:252
    bit_dist_c4_cal: 2bit:4, 4bit:251, 8bit:1
    profile_time_s: 407.7
    eval_time_s: 349.4
    total_time_s: 757.1
- exp_id: gemma2_9b_full_pipeline
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    baseline_wikitext2_ppl: 8.9
    mckp_wikitext2_ppl: 9.05
    uniform4bit_wikitext2_ppl: 9.03
    mckp_improvement_over_uniform: -0.02
    top5_concentration: 0.23
    layer0_dominance_ratio: 1.32
    best_k: 8
    best_k_ppl: 9.05
    verdict: FAIL
- exp_id: yi15_9b_full_pipeline
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    baseline_wikitext2_ppl: 7.0157
    mckp_wikitext2_ppl: 7.3129
    uniform4bit_wikitext2_ppl: 7.2171
    mckp_improvement_over_uniform: -0.0958
    top5_concentration: 0.4934
    layer0_dominance_ratio: 0.07
    best_k: 2
    best_k_ppl: 7.2209
    gqa_ratio: '8:1'
    verdict: FAIL
- exp_id: qwen25-hires-profiling
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: qwen_hires_float32_d048
  name: ''
  status: DONE
  conclusion: success
  metrics:
    float32_hires_top5_concentration: 0.6104
    bf16_hires_range: 0.59-0.66
    float32_lowres_concentration: 0.42
    bf16_bug_impact_on_concentration: 0.01
    baseline_ppl: 9.81
    mckp_unconstrained_ppl: 10.95
    uniform_4bit_ppl: 15.45
    mckp_bit_dist:
      '2': 12
      '4': 96
      '8': 3
      '16': 1
    l0h0_delta: 6.7388
    l0_4heads_total_share: 0.586
    claim3_threshold_0.50: PASS
- exp_id: yi15_hires_float32_profiling
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: yi15_hires_bf16_2bitonly
  name: ''
  status: DONE
  conclusion: success
  metrics:
    top5_concentration: 0.7139
    top5_n_heads: 9
    baseline_calibration_ppl: 5.888
    delta_2bit_cv: 8.8991
    layer0_dominance_ratio: 0.04
    top1_head: L4H3_delta=13.1236
    total_hours: 0.96
- exp_id: qwen_hires_constrained_d049
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    float32_hires_constrained_mckp_ppl: 10.8921
    baseline_ppl: 9.8106
    uniform_4bit_ppl: 15.4484
    bit_distribution:
      '2': 8
      '4': 100
      '8': 4
    gap_recovery_pct: 80.8
    top5_concentration: 0.6156
    top5_concentration_pre_monotonicity: 0.6104
    bf16_hires_constrained_mckp_ppl: 10.9131
    delta_f32_vs_bf16: 0.021
- exp_id: yi15_hires_constrained_mckp
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    hires_mckp_ppl: 7.2181
    uniform_4bit_ppl: 7.2171
    baseline_ppl: 7.0157
    delta_vs_uniform: -0.001
    bit_distribution:
      '2': 2
      '4': 189
      '8': 1
    2bit_heads:
    - L22H1
    - L24H3
    8bit_heads:
    - L6H2
    L4H3_status: kept_at_4bit
    std_mckp_k2_ppl: 7.2209
    std_mckp_k8_ppl: 7.3129
    hires_concentration: 0.7139
    L4H3_2bit_delta: 13.12
    L4H3_4bit_delta: 0.0048
    L4H3_8bit_delta: 0.004
- exp_id: llama_hires_bf16_2bitonly
  name: ''
  status: DONE
  conclusion: success
  metrics:
    top5_concentration: 0.5749
    t1_t5: 0.85
    baseline_ppl: 6.5055
    top1_head: L2H5_delta=15.2636
    delta_2bit_cv: 7.7663
    l0_dominance_ratio: 0.67
    positive_delta_heads: 254
    total_heads: 256
    total_hours: 0.98
- exp_id: mistral_hires_bf16_2bitonly
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    error: 'ValueError: Unrecognized model - config.json missing model_type field
      at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3'
- exp_id: mistral_hires_bf16_2bitonly_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    error: 'SafetensorError: model-00003-of-00003.safetensors missing, incomplete
      download'
- exp_id: mistral_hires_bf16_2bitonly_v3
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: mistral_hires_bf16_2bitonly_v4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    top5_concentration: 0.241
    top5_n_heads: 12
    baseline_ppl: 5.8702
    top1_head: L2H5
    top1_delta_2bit: 0.3236
    top2_head: L12H1
    top2_delta_2bit: 0.1435
    top3_head: L0H7
    top3_delta_2bit: 0.1403
    delta_2bit_mean: 0.020073
    delta_2bit_std: 0.026278
    delta_2bit_cv: 1.3091
    layer0_mean_delta_2bit: 0.034073
    other_layers_mean_delta_2bit: 0.019621
    l0_dominance_ratio: 1.74
    positive_delta_heads: 252
    total_heads: 256
    distribution_shape: flat
    total_hours: 0.94
    profile_seconds: 3371.7
- exp_id: llama_hires_constrained_mckp
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    baseline_bf16_ppl: 8.0922
    hires_mckp_ppl: 8.5042
    uniform_4bit_ppl: 8.4701
    std_mckp_reference_ppl: 8.4498
    mckp_vs_uniform_delta: -0.0341
    mckp_vs_uniform_pct: -9
    hires_vs_std_mckp_delta: 0.0544
    concentration: 0.5749
    bit_distribution:
      '2': 2
      '4': 253
      '8': 1
    heads_2bit:
    - 26,0
    - 31,7
    heads_8bit:
    - 12,3
    verdict: FAIL
- exp_id: gemma2_hires_bf16_2bitonly
  name: ''
  status: DONE
  conclusion: success
  metrics:
    concentration_top5pct: 0.2291
    l0_dominance_ratio: 2.05
    cv_delta_2bit: 1.2834
    positive_delta_heads: 310/336
    top_head: L0H1 delta=0.1906
    total_time_hours: 1.59
- exp_id: llama_c4_hires_crossdataset
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    bf16_wt2_ppl: 8.0922
    bf16_c4_ppl: 7.1333
    c4_cal_mckp_wt2_ppl: 8.5103
    c4_cal_mckp_c4_ppl: 7.5351
    uniform_wt2_ppl: 8.4701
    uniform_c4_ppl: 7.5351
    delta_c4_uniform_minus_mckp: 0
    delta_wt2_uniform_minus_mckp: -0.0402
    verdict_c4: FAIL
    bit_distribution:
      '2': 2
      '4': 253
      '8': 1
    heads_2bit:
    - 2,3
    - 24,2
    heads_8bit:
    - 31,6
    total_time_min: 6.3
    wt2_ref_mckp_ppl: 8.5042
    wt2_ref_delta: -0.0341
- exp_id: mistral_c4_hires_crossdataset
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    fp16_ppl: 7.0352
    c4_mckp_ppl: 7.1774
    uniform_4bit_ppl: 7.1308
    mckp_vs_uniform_delta: 0.0466
    mckp_bit_distribution:
      '2': 4
      '4': 250
      '8': 2
    phase4_error: 'FileNotFoundError: mistral_k_ablation_results.json'
- exp_id: w2_unconstrained_baselines
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    note: 2bitonly profiles only - INVALID for reviewer response
    yi15_ppl: 672.2
    yi15_ratio: 114
    llama_ppl: 1219.7
    llama_ratio: 187
    mistral_ppl_2bitonly: 47.8
    mistral_ratio_2bitonly: 8.2
    mistral_ppl_full: 6.39
    mistral_ratio_full: 1.09
    gemma2_ppl: 277.4
    gemma2_ratio: 37.9
    budget: 0.25
    baseline_yi: 5.89
    baseline_llama: 6.51
    baseline_mistral: 5.87
    baseline_gemma2: 7.32
- exp_id: w9_compounding_scaling
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    baseline_ppl: 8.2
    n1_joint_ppl: 14.94
    n1_ratio: 1
    n2_joint_ppl: 42.26
    n2_ratio: 3.84
    n4_joint_ppl: 3813.76
    n4_ratio: 333.3
    n8_joint_ppl: 3586.42
    n8_ratio: 282.1
    n16_joint_ppl: 7286.23
    n16_ratio: 521.1
    n32_joint_ppl: 6644.05
    n32_ratio: 424
    n64_joint_ppl: 9453.33
    n64_ratio: 533.3
    runtime_seconds: 96
- exp_id: w9_compounding_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_ppl: 9.81
    k1_topk_ppl: 9.826
    k1_randomk_ppl: 9.887
    k1_randomk_std: 0.05
    k4_topk_ppl: 9.849
    k4_topk_ratio: 0.86
    k4_randomk_ppl: 10.06
    k4_randomk_std: 0.06
    k4_randomk_ratio: 1.24
    k8_topk_ppl: 10.042
    k8_topk_ratio: 1.56
    k8_randomk_ppl: 11.07
    k8_randomk_std: 0.69
    k8_randomk_ratio: 1.76
    k16_topk_ppl: 10.42
    k16_topk_ratio: 1.56
    k16_randomk_ppl: 12.91
    k16_randomk_std: 0.4
    k16_randomk_ratio: 2.1
    k32_topk_ppl: 11.604
    k32_topk_ratio: 1.78
    k32_randomk_ppl: 18.33
    k32_randomk_std: 2.53
    k32_randomk_ratio: 2.73
    k64_topk_ppl: 22.946
    k64_topk_ratio: 4.89
    k64_randomk_ppl: 55.94
    k64_randomk_std: 9.73
    k64_randomk_ratio: 8.88
    runtime_minutes: 16.9
    note: 'v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking,
      top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。'
- exp_id: w2_unconstrained_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    yi15_baseline: 7.0157
    yi15_uniform4: 7.2171
    yi15_greedy: 7.5615
    yi15_mckp: 7.5615
    yi15_n2bit: 22
    llama_baseline: 8.0922
    llama_uniform4: 8.4701
    llama_greedy: 8.6265
    llama_mckp: 8.6265
    llama_n2bit: 12
    mistral_baseline: 7.0352
    mistral_uniform4: 7.1308
    mistral_greedy: 7.5733
    mistral_mckp: 7.5963
    mistral_n2bit: 42
    gemma2_baseline: 6.0306
    gemma2_uniform4: 6.1683
    gemma2_greedy: 8.8469
    gemma2_mckp: 8.8469
    gemma2_n2bit: 106
    gemma2_eval_method: sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)
    gemma2_greedy_ratio: 1.467
    gemma2_catastrophic: true
    gemma2_note: 1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal
      value
- exp_id: w3_downstream_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    yi15_baseline_avg: 0.6912
    yi15_uniform_avg: 0.6822
    yi15_mckp_avg: 0.6745
    yi15_mckp_vs_uniform_pp: -0.77
    yi15_mckp_vs_baseline_pp: -1.67
    yi15_baseline:
      arc_easy: 0.8093
      arc_challenge: 0.5265
      hellaswag: 0.5913
      piqa: 0.7949
      winogrande: 0.734
    yi15_uniform:
      arc_easy: 0.7946
      arc_challenge: 0.5205
      hellaswag: 0.5857
      piqa: 0.7927
      winogrande: 0.7174
    yi15_mckp:
      arc_easy: 0.7854
      arc_challenge: 0.4881
      hellaswag: 0.5797
      piqa: 0.7894
      winogrande: 0.7301
    llama_baseline_avg: 0.696
    llama_uniform_avg: 0.6915
    llama_mckp_avg: 0.6816
    llama_mckp_vs_uniform_pp: -0.99
    llama_mckp_vs_baseline_pp: -1.44
    llama_baseline:
      arc_easy: 0.8228
      arc_challenge: 0.5188
      hellaswag: 0.6073
      piqa: 0.7922
      winogrande: 0.7388
    llama_uniform:
      arc_easy: 0.8173
      arc_challenge: 0.5256
      hellaswag: 0.6026
      piqa: 0.7867
      winogrande: 0.7253
    llama_mckp:
      arc_easy: 0.8039
      arc_challenge: 0.4991
      hellaswag: 0.6012
      piqa: 0.7802
      winogrande: 0.7238
    mistral_baseline_avg: 0.6917
    mistral_uniform_avg: 0.6894
    mistral_mckp_avg: 0.6846
    mistral_mckp_vs_uniform_pp: -0.48
    mistral_mckp_vs_baseline_pp: -0.71
    mistral_baseline:
      arc_easy: 0.8005
      arc_challenge: 0.5043
      hellaswag: 0.6118
      piqa: 0.8009
      winogrande: 0.7411
    mistral_uniform:
      arc_easy: 0.7976
      arc_challenge: 0.5068
      hellaswag: 0.6051
      piqa: 0.7982
      winogrande: 0.7395
    mistral_mckp:
      arc_easy: 0.7942
      arc_challenge: 0.4949
      hellaswag: 0.6027
      piqa: 0.802
      winogrande: 0.7293
    gemma2_baseline_avg: 0.7307
    gemma2_uniform_avg: 0.7251
    gemma2_mckp_avg: 0.7265
    gemma2_mckp_vs_uniform_pp: 0.14
    gemma2_mckp_vs_baseline_pp: -0.42
    gemma2_baseline:
      arc_easy: 0.8737
      arc_challenge: 0.6135
      hellaswag: 0.6093
      piqa: 0.8128
      winogrande: 0.7443
    gemma2_uniform:
      arc_easy: 0.8662
      arc_challenge: 0.6058
      hellaswag: 0.606
      piqa: 0.8079
      winogrande: 0.7395
    gemma2_mckp:
      arc_easy: 0.8649
      arc_challenge: 0.6041
      hellaswag: 0.6089
      piqa: 0.8074
      winogrande: 0.7474
    eval_harness_version: 0.4.11
    num_fewshot: 0
    yi_elapsed_s: 1563.2
    llama_elapsed_s: 1446.4
    mistral_elapsed_s: 1302.2
    gemma2_elapsed_s: 1735.9
- exp_id: gemma2_constrained_bos_fix
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: w1_qwen14b_hires_profiling
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: worst
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f114f0f3-7484-4f66-92b9-ae6b798ef7f0",
  "type": "user",
  "uuid": "23f25523-5a10-4ecc-bf62-406abdf6076b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T09:26:53.005Z_

```json
{
  "parentUuid": "23f25523-5a10-4ecc-bf62-406abdf6076b",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "732dc7f0-f4e7-412c-a86d-8aee094bf452",
  "timestamp": "2026-05-15T09:26:53.005Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T09:26:53.005Z_

```json
{
  "parentUuid": "732dc7f0-f4e7-412c-a86d-8aee094bf452",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0b89fa8a-c045-4ffd-8e10-fd69febc76c5",
  "timestamp": "2026-05-15T09:26:53.005Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Qwen2.5-14B 不是 Spread 或 MCKP 无效，decision rule 出现 false positive/negative，核心 diagnostic 叙事不成立 核心假设：['Qwen2.5-14B concentration ≥0.50 但 MCKP 无改善（类似 Yi-1.5，d…",
  "leafUuid": "0b89fa8a-c045-4ffd-8e10-fd69febc76c5",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing when per-head KV cache quantization helps across architectures",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Assistant

_source line 8 · 2026-05-15T09:26:57.696Z_

I'll review the experiment plan to identify all experiments that need worst-tier predictions, then generate detailed imagined data.

Let me first check which experiments are still RUNNING or PLANNED (not yet completed).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b89fa8a-c045-4ffd-8e10-fd69febc76c5",
  "isSidechain": false,
  "requestId": "req_011Cb47g6xxj3Vj8M95AWYU6",
  "type": "assistant",
  "uuid": "5fbfa782-3df6-4703-a34b-ceef55cec006",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136cHgV2F4RagtTKUb3Limt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 31522,
      "cache_read_input_tokens": 11841,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 237,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 31522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31522
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T09:27:01.718Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0152HMvuLzKN97Lz1PnMFETG`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan and running experiments",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_2, find all files related to experiment planning. I need to understand:\n1. Which experiments have status RUNNING or PLANNED (not DONE)\n2. The full experiment_plan entries for those experiments\n3. Any files named experiment_plan*.yaml or similar\n\nSearch broadly: experiment_plan, plan.yaml, registry, running experiments. Check artifacts/ directory too."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fbfa782-3df6-4703-a34b-ceef55cec006",
  "isSidechain": false,
  "requestId": "req_011Cb47g6xxj3Vj8M95AWYU6",
  "type": "assistant",
  "uuid": "5b5a6448-8e6e-4085-857d-6097e432c8e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136cHgV2F4RagtTKUb3Limt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 31522,
      "cache_read_input_tokens": 11841,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 237,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 31522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31522
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T09:27:39.800Z_

<details><summary>↩ Tool result · `toolu_0152HMvuLzKN97Lz1PnMFETG`</summary>

````text
Perfect! Now I have all the information needed. Let me compile the comprehensive report.

## Summary: Experiment Planning and Status

I've found and analyzed all experiment-related files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_2`. Here's what you need to know:

### **Key Files Located**

1. **Experiment Plans (YAML):**
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/experiment_plan.yaml` - 9 experiments (plan_001-plan_005b, plan_006, plan_aux_001-003)
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/experiment_plan.yaml` - 18 planned experiments (plan_001-018)

2. **Active Registries (YAML):**
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/registry.yaml` - 27 experiments tracked
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml` - 60+ experiments tracked
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/global/registry.yaml` - Global tracking (global and project-spanning experiments)

---

## **RUNNING/PLANNED Experiments (Non-DONE)**

### **1. demo_calibrated_sim Project**
**Status: ANALYZING (1 experiment)**
- **Experiment ID:** `bcp7b-multirun-001`
- **Plan Reference:** `plan_005b`
- **Status:** ANALYZING
- **Created:** 2026-05-13T15:45:33.648Z
- **Updated:** 2026-05-13T15:46:13.388Z
- **GPU:** cuda:2, PID 174169
- **Hypothesis:** 7B BCP multi-run replication to verify FM1 (completion collapse) and FM2 (cross-dim interference) reproducibility across 3 additional runs. Brings C1 evidence strength to match C2/C3 levels.
- **Model:** Qwen2.5-7B-Instruct
- **Data:** tau-bench dev split (20 tasks × 6 variants × 3 runs = 360 total episodes)
- **Log Path:** ~/runs/demo_calibrated_sim/bcp7b-multirun-001.log

**Full experiment_plan.yaml entry for plan_005b:**
```yaml
- id: plan_005b
  name: 7B BCP Multi-Run Replication
  claim: C1
  description: Replicate mvp-004 (7B base BCP) 3 additional runs. Current C1 evidence 
    (FM1/FM2) based on single run n=19-20. This brings C1 to 4 runs total, matching 
    C2/C3 evidence strength.
  priority: P1
  depends_on:
    - plan_001
  registry_id: bcp7b-multirun-001
  notes: High-value low-cost. Directly addresses Reviewer concern about FM1/FM2 variance artifact risk.
```

---

### **2. ratekv Project**
**Status: RUNNING (2 experiments)**

#### **Experiment 1: gemma2_constrained_bos_fix**
- **Status:** RUNNING
- **Created:** 2026-05-15T08:22:09.894Z
- **Updated:** 2026-05-15T08:22:40.295Z
- **GPU:** cuda:0, PID 315364
- **Server:** westd-37397
- **Hypothesis:** Re-evaluate Table 2 Gemma-2 constrained MCKP numbers with BOS fix (sliding window + BOS prepend). Original eval may have been affected by cold-start bug.
- **Model:** Gemma-2-9B (336 KV heads)
- **Data:** WikiText-2 test set + merged profiles
- **Log Path:** /root/ratekv/logs/gemma2_constrained_bos_fix.log

#### **Experiment 2: w1_qwen14b_hires_profiling**
- **Status:** RUNNING
- **Created:** 2026-05-15T08:22:15.199Z
- **Updated:** 2026-05-15T08:22:42.256Z
- **GPU:** cuda:1, PID 315787
- **Server:** westd-37397
- **Hypothesis:** W1 new model: Qwen2.5-14B hires bf16 2-bit-only profiling (48 layers × 8 KV heads = 384 heads). Tests whether diagnostic generalizes within Qwen model family at larger scale.
- **Model:** Qwen2.5-14B
- **Data:** calibration_hires.json (64 seq × 2048 tokens)
- **Log Path:** /root/ratekv/logs/qwen14b_hires_profiling.log

---

### **3. Global Registry**
**Status: RUNNING (1 experiment)**
- **Experiment ID:** `yi15_hires_bf16_2bitonly`
- **Status:** RUNNING
- **Created:** 2026-05-14T19:50:16.917Z
- **Updated:** 2026-05-14T19:50:42.363Z
- **GPU:** cuda:1
- **Server:** westd-37397
- **Hypothesis:** Yi-1.5 hires bf16 2-bit only: 高分辨率数据下 concentration 是否从 0.49 变化，确认 spike pattern 是否稳定
- **Model:** Yi-1.5-9B
- **Data:** WikiText-2 train (64 seq × 2048 tok hires profiling)
- **Architecture:** 48 layers, 4 KV heads per layer, GQA ratio 8:1

---

## **PLANNED Experiments (In experiment_plan.yaml but not yet started)**

### **ratekv/experiment_plan.yaml - Active Plans**
All 18 plans listed with priorities P0 (highest) and P1:

**P0 Priority (Critical):**
- plan_001: Remove L0 exclusion constraint (1h GPU) - registry: exp_d_no_l0_exclusion
- plan_002: Llama-3.1-8B full pipeline (4h GPU) - registry: llama_full_pipeline
- plan_003: Mistral-7B-v0.3 full pipeline (4h GPU) - registry: mistral_full_pipeline
- plan_004: Compounding effect sweep (3h GPU) - registry: compounding_sweep
- plan_005: Budget sweep 2x/4x/8x (3h GPU) - registry: budget_sweep
- plan_006: Hires profiling (3h GPU) - registry: exp_e_hires_profile
- plan_007: C4 cross-dataset eval (2h GPU) - registry: c4_rerun_d032
- plan_008: RateQuant greedy comparison (4h GPU) - registry: ratequant_greedy_comparison
- plan_015: L0-only heuristic baseline (1h GPU) - registry: l0_only_heuristic
- plan_016: RateQuant greedy + cardinality ablation (2h GPU) - registry: greedy_cardinality_ablation

**P1 Priority (Important):**
- plan_009: Oracle comparison (6h GPU)
- plan_010: Cross-domain calibration robustness (2h GPU)
- plan_011: Head sensitivity visualization (1h GPU)
- plan_012: Downstream task evaluation (8h GPU)
- plan_013: 70B profiling-only (4h GPU)
- plan_014: K/V separation analysis (3h GPU)
- plan_017: Multi-seed error bars (3h GPU)
- plan_018: Runtime/latency benchmark (2h GPU)

---

## **Summary Statistics**

| Project | RUNNING | ANALYZING | PLANNED | DONE |
|---------|---------|-----------|---------|------|
| demo_calibrated_sim | 0 | 1 | 8 | 19 |
| ratekv | 2 | 0 | 18 | 40+ |
| global | 1 | 0 | - | 1 |
| **TOTAL** | **3** | **1** | **26+** | **60+** |

The three RUNNING experiments are all started within the last 24 hours (May 14-15, 2026) and are actively profiling/evaluating quantization strategies on different model architectures.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "5b5a6448-8e6e-4085-857d-6097e432c8e7",
  "isSidechain": false,
  "promptId": "f114f0f3-7484-4f66-92b9-ae6b798ef7f0",
  "type": "user",
  "uuid": "9ae699ce-4690-48b3-8b75-528aa77708e4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_2, find all files related to experiment planning. I need to understand:\n1. Which experiments have status RUNNING or PLANNED (not DONE)\n2. The full experiment_plan entries for those experiments\n3. Any files named experiment_plan*.yaml or similar\n\nSearch broadly: experiment_plan, plan.yaml, registry, running experiments. Check artifacts/ directory too.",
    "agentId": "a3a2a4ce779436576",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information needed. Let me compile the comprehensive report.\n\n## Summary: Experiment Planning and Status\n\nI've found and analyzed all experiment-related files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_2`. Here's what you need to know:\n\n### **Key Files Located**\n\n1. **Experiment Plans (YAML):**\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/experiment_plan.yaml` - 9 experiments (plan_001-plan_005b, plan_006, plan_aux_001-003)\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/experiment_plan.yaml` - 18 planned experiments (plan_001-018)\n\n2. **Active Registries (YAML):**\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/registry.yaml` - 27 experiments tracked\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml` - 60+ experiments tracked\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/global/registry.yaml` - Global tracking (global and project-spanning experiments)\n\n---\n\n## **RUNNING/PLANNED Experiments (Non-DONE)**\n\n### **1. demo_calibrated_sim Project**\n**Status: ANALYZING (1 experiment)**\n- **Experiment ID:** `bcp7b-multirun-001`\n- **Plan Reference:** `plan_005b`\n- **Status:** ANALYZING\n- **Created:** 2026-05-13T15:45:33.648Z\n- **Updated:** 2026-05-13T15:46:13.388Z\n- **GPU:** cuda:2, PID 174169\n- **Hypothesis:** 7B BCP multi-run replication to verify FM1 (completion collapse) and FM2 (cross-dim interference) reproducibility across 3 additional runs. Brings C1 evidence strength to match C2/C3 levels.\n- **Model:** Qwen2.5-7B-Instruct\n- **Data:** tau-bench dev split (20 tasks × 6 variants × 3 runs = 360 total episodes)\n- **Log Path:** ~/runs/demo_calibrated_sim/bcp7b-multirun-001.log\n\n**Full experiment_plan.yaml entry for plan_005b:**\n```yaml\n- id: plan_005b\n  name: 7B BCP Multi-Run Replication\n  claim: C1\n  description: Replicate mvp-004 (7B base BCP) 3 additional runs. Current C1 evidence \n    (FM1/FM2) based on single run n=19-20. This brings C1 to 4 runs total, matching \n    C2/C3 evidence strength.\n  priority: P1\n  depends_on:\n    - plan_001\n  registry_id: bcp7b-multirun-001\n  notes: High-value low-cost. Directly addresses Reviewer concern about FM1/FM2 variance artifact risk.\n```\n\n---\n\n### **2. ratekv Project**\n**Status: RUNNING (2 experiments)**\n\n#### **Experiment 1: gemma2_constrained_bos_fix**\n- **Status:** RUNNING\n- **Created:** 2026-05-15T08:22:09.894Z\n- **Updated:** 2026-05-15T08:22:40.295Z\n- **GPU:** cuda:0, PID 315364\n- **Server:** westd-37397\n- **Hypothesis:** Re-evaluate Table 2 Gemma-2 constrained MCKP numbers with BOS fix (sliding window + BOS prepend). Original eval may have been affected by cold-start bug.\n- **Model:** Gemma-2-9B (336 KV heads)\n- **Data:** WikiText-2 test set + merged profiles\n- **Log Path:** /root/ratekv/logs/gemma2_constrained_bos_fix.log\n\n#### **Experiment 2: w1_qwen14b_hires_profiling**\n- **Status:** RUNNING\n- **Created:** 2026-05-15T08:22:15.199Z\n- **Updated:** 2026-05-15T08:22:42.256Z\n- **GPU:** cuda:1, PID 315787\n- **Server:** westd-37397\n- **Hypothesis:** W1 new model: Qwen2.5-14B hires bf16 2-bit-only profiling (48 layers × 8 KV heads = 384 heads). Tests whether diagnostic generalizes within Qwen model family at larger scale.\n- **Model:** Qwen2.5-14B\n- **Data:** calibration_hires.json (64 seq × 2048 tokens)\n- **Log Path:** /root/ratekv/logs/qwen14b_hires_profiling.log\n\n---\n\n### **3. Global Registry**\n**Status: RUNNING (1 experiment)**\n- **Experiment ID:** `yi15_hires_bf16_2bitonly`\n- **Status:** RUNNING\n- **Created:** 2026-05-14T19:50:16.917Z\n- **Updated:** 2026-05-14T19:50:42.363Z\n- **GPU:** cuda:1\n- **Server:** westd-37397\n- **Hypothesis:** Yi-1.5 hires bf16 2-bit only: 高分辨率数据下 concentration 是否从 0.49 变化，确认 spike pattern 是否稳定\n- **Model:** Yi-1.5-9B\n- **Data:** WikiText-2 train (64 seq × 2048 tok hires profiling)\n- **Architecture:** 48 layers, 4 KV heads per layer, GQA ratio 8:1\n\n---\n\n## **PLANNED Experiments (In experiment_plan.yaml but not yet started)**\n\n### **ratekv/experiment_plan.yaml - Active Plans**\nAll 18 plans listed with priorities P0 (highest) and P1:\n\n**P0 Priority (Critical):**\n- plan_001: Remove L0 exclusion constraint (1h GPU) - registry: exp_d_no_l0_exclusion\n- plan_002: Llama-3.1-8B full pipeline (4h GPU) - registry: llama_full_pipeline\n- plan_003: Mistral-7B-v0.3 full pipeline (4h GPU) - registry: mistral_full_pipeline\n- plan_004: Compounding effect sweep (3h GPU) - registry: compounding_sweep\n- plan_005: Budget sweep 2x/4x/8x (3h GPU) - registry: budget_sweep\n- plan_006: Hires profiling (3h GPU) - registry: exp_e_hires_profile\n- plan_007: C4 cross-dataset eval (2h GPU) - registry: c4_rerun_d032\n- plan_008: RateQuant greedy comparison (4h GPU) - registry: ratequant_greedy_comparison\n- plan_015: L0-only heuristic baseline (1h GPU) - registry: l0_only_heuristic\n- plan_016: RateQuant greedy + cardinality ablation (2h GPU) - registry: greedy_cardinality_ablation\n\n**P1 Priority (Important):**\n- plan_009: Oracle comparison (6h GPU)\n- plan_010: Cross-domain calibration robustness (2h GPU)\n- plan_011: Head sensitivity visualization (1h GPU)\n- plan_012: Downstream task evaluation (8h GPU)\n- plan_013: 70B profiling-only (4h GPU)\n- plan_014: K/V separation analysis (3h GPU)\n- plan_017: Multi-seed error bars (3h GPU)\n- plan_018: Runtime/latency benchmark (2h GPU)\n\n---\n\n## **Summary Statistics**\n\n| Project | RUNNING | ANALYZING | PLANNED | DONE |\n|---------|---------|-----------|---------|------|\n| demo_calibrated_sim | 0 | 1 | 8 | 19 |\n| ratekv | 2 | 0 | 18 | 40+ |\n| global | 1 | 0 | - | 1 |\n| **TOTAL** | **3** | **1** | **26+** | **60+** |\n\nThe three RUNNING experiments are all started within the last 24 hours (May 14-15, 2026) and are actively profiling/evaluating quantization strategies on different model architectures."
      }
    ],
    "totalDurationMs": 38076,
    "totalTokens": 72301,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 217,
      "cache_read_input_tokens": 69930,
      "output_tokens": 2149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 217
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2149,
          "cache_read_input_tokens": 69930,
          "cache_creation_input_tokens": 217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 217,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 1,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "5b5a6448-8e6e-4085-857d-6097e432c8e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Assistant

_source line 11 · 2026-05-15T09:29:12.506Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. The two RUNNING experiments in ratekv are:
1. `gemma2_constrained_bos_fix` - Re-evaluate Gemma-2 constrained MCKP with BOS fix
2. `w1_qwen14b_hires_profiling` - Qwen2.5-14B hires profiling

For the worst tier, I need to generate predictions for ALL planned experiments in the experiment_plan. But actually, looking more carefully at the user's request, they want me to generate worst-tier predictions for each **planned** experiment in the experiment_plan. Most experiments are already DONE, but I should generate worst-tier imagined results for all of them based on the worst-tier definition.
 
Re-reading the request more carefully, the user is asking for detailed data for all experiments in the experiment_plan, not just the ones currently marked as planned. Even though many are already completed, I should generate worst-tier predictions across the entire set. definition, I need to generate worst-tier simulation results for all 18 experiments in the plan. For the ones already marked as DONE with actual results, I'll imagine what those results would look like under worst-case conditions, and for the RUNNING experiments, I'll project worst-case outcomes. This is essentially a calibration exercise to help the team prepare a worst-case narrative for the paper.

Now I'm ready to generate the YAML output with detailed worst-tier data for each experiment. I'm noticing there are additional experiments beyond the main plan_001 through plan_018 sequence—ones with "w" prefixes like the two currently running experiments (gemma2_constrained_bos_fix and w1_qwen14b_hires_profiling) plus others like w2_unconstrained_v2, w3_downstream_eval, and w9_compounding_v2. I need to clarify how these fit into the overall structure and what they're specifically testing. to be additional work items not in the original experiment_plan.

The RUNNING experiments are:
1. gemma2_constrained_bos_fix
2. w1_qwen14b_hires_profiling

For worst tier, the key predictions are:
1. w1_qwen14b_hires_profiling → Qwen2.5-14B profiling shows either concentration ≥0.50 but spike pattern (like Yi), or concentration <0.40 (flat) → diagnostic false positive or Qwen family is inconsistent
2. gemma2_constrained_bos_fix → BOS fix significantly changes numbers, requiring recalibration of three-tier labels

Let me also think about what experiments WOULD be needed after these RUNNING ones complete:
- After profiling Qwen14B, there would be constrained MCKP eval
- After Gemma-2 BOS fix, the constrained results may change, which means I need to re-evaluate how the three-tier classification holds up with the corrected baseline.

Now I'm reconsidering what the user actually wants - they're asking for detailed data on each planned experiment in experiment_plan (plan_001 through plan_018) plus the currently running ones, since those are the experiments that haven't finished yet and need predictions. I'm mapping out what the worst-tier results would look like across all the key experiments — where plan_001's L0 exclusion fix still helps but more weakly, the negative results stay negative, the compounding and budget sweeps show murkier trends, and the cross-dataset and greedy comparisons don't support the claims as strongly.

Looking at the remaining experiments, the oracle gap widens, cross-domain calibration agreement drops, downstream gains don't match the perplexity improvements, the 70B pattern breaks, K/V separation shows no benefit, and the greedy variants end up matching MCKP anyway — plus high variance across seeds and runtime overhead would further undermine the conclusions.

For the running experiments, the BOS fix appears to shift the ratio significantly for the constrained Gemma2 case, and the Qwen14B high-resolution profiling is still in progress.

Now I need to determine whether to include just the 18 planned experiments or also account for the two active runs, then write out the comprehensive YAML covering the worst-tier scenario where Qwen14B's concentration sits near the threshold but its spike pattern creates a false positive for the Spread diagnostic.

For the worst-tier results, I'm thinking through how each experiment would play out consistently. The Gemma2 BOS fix shifts the unconstrained ratio significantly, W9 shows non-monotonic behavior at certain k values, and the decision rule accuracy drops from perfect to mixed performance. I'll frame Qwen14B as the key challenge—it looks like Spread based on concentration but actually exhibits spike behavior, which directly undermines the diagnostic's reliability.

Now I'm reconsidering the approach: some experiments are already complete with real results, so for the worst tier I should either keep those results if they're consistent with the new data, or acknowledge that the worst tier is primarily defined by what the new experiments reveal rather than retroactively changing what's already been done. The narrative shifts because the framework that worked for Qwen 7B doesn't generalize to these new cases.

Actually, the clearest path is to treat this as a pre-registration exercise and generate worst-tier predicted results for all 18 planned experiments plus the two critical running ones, as if I'm forecasting what would happen under that scenario. Now I need to nail down the specific metric ranges for the worst tier based on the definition: Qwen 14B improvement stays between -3 and 3 percent, concentration falls in the 0.3 to 0.75 range, the T1/T5 ratio lands between 0.4 and 0.95, and decision rule accuracy stays at 4 or 5.

For the Qwen 14B experiment specifically, I'm working through a tricky diagnostic: if I set concentration around 0.52 (just above the 0.50 threshold) and T1/T5 at 0.88, the joint diagnostic would actually predict non-beneficial results due to the spike pattern, which creates a false positive scenario I need to navigate carefully. real false positive, we'd need concentration ≥0.50 AND t₁/t₅ ≤0.70 but MCKP fails - OR concentration ≥0.50 AND t₁/t₅ ~0.65 (borderline) but MCKP improvement ~0% → the thresholds are wrong.

Let me reconsider this. The worst tier describes cases where concentration ≥0.50 but MCKP shows no improvement (like Yi-1.5, a diagnostic false positive), or concentration <0.40 (Flat pattern, where only Qwen 7B is Spread).

Option A has concentration=0.52 and t₁/t₅=0.62, meeting both Spread criteria, yet MCKP improvement is only ~1% - this is a false positive where the diagnostic predicts benefit but doesn't deliver. Option B has concentration=0.35 with a Flat pattern, correctly identified as non-Spread. Option A is more damaging because it reveals the diagnostic can't distinguish beneficial from non-beneficial cases even when both metrics align, whereas Option B shows the diagnostic working correctly by rejecting a non-Spread case. one false positive).

Actually, let me check: with 6 models (5 original + Qwen14B), if Qwen14B is a false positive, the decision rule accuracy would be 5/6 (missed Qwen14B). That's within the worst-tier range of [4, 5]... wait, 5/6 is 5 out of 6, which is 5 correct. The range says [4, 5], so 5/6 accuracy is at the boundary.

For it to be 4/6 or below, we'd need another failure. Perhaps Gemma-2 BOS fix changes its categorization somehow.

Let me go with this worst-tier scenario:
- Qwen14B: concentration=0.52, t₁/t₅=0.62, MCKP improvement +1.2% (noise-level) → false positive
- Gemma-2 BOS fix: unconstrained ratio shifts to either 1.58× or 1.22×
- Decision rule: 5/6 correct (Qwen14B is false positive)
- W9 compounding: k=64 randomk/topk ratio = 1.45 (lower than current 1.82)

Now checking the W9 data against the worst-tier bounds—the actual k64 ratio is 2.44, which exceeds the [1.0, 2.0] range, so the worst-tier scenario would require the randomk/topk distinction to narrow significantly.

I need to generate worst-tier predictions for all 18 experiment plan entries plus the 2 running experiments, then write out the full YAML with counterfactuals for completed experiments.

Generating the comprehensive YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ae699ce-4690-48b3-8b75-528aa77708e4",
  "isSidechain": false,
  "requestId": "req_011Cb47jYoJhyguBR7entxFu",
  "type": "assistant",
  "uuid": "8664aedf-0bac-4f88-8372-4de3a2134e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPHZG17U7zwYLLw6YVhR6e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 43363,
      "output_tokens": 4754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4754,
          "cache_read_input_tokens": 43363,
          "cache_creation_input_tokens": 2394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2394
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-15T09:29:12.982Z_

Let me check the current state of running experiments and any additional worklist files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8664aedf-0bac-4f88-8372-4de3a2134e54",
  "isSidechain": false,
  "requestId": "req_011Cb47jYoJhyguBR7entxFu",
  "type": "assistant",
  "uuid": "d0a1dc15-4a4e-478f-af55-9236987eecb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPHZG17U7zwYLLw6YVhR6e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 43363,
      "output_tokens": 4754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4754,
          "cache_read_input_tokens": 43363,
          "cache_creation_input_tokens": 2394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2394
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T09:29:13.446Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019iSDhw8zA1LA8vh8g2TJ6j`</summary>

```json
{
  "pattern": "projects/ratekv/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0a1dc15-4a4e-478f-af55-9236987eecb2",
  "isSidechain": false,
  "requestId": "req_011Cb47jYoJhyguBR7entxFu",
  "type": "assistant",
  "uuid": "3831a484-7348-46eb-b988-f189b75f6ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPHZG17U7zwYLLw6YVhR6e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 43363,
      "output_tokens": 4754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4754,
          "cache_read_input_tokens": 43363,
          "cache_creation_input_tokens": 2394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2394
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T09:29:13.847Z_

<details><summary>↩ Tool result · `toolu_014zwjswHt2X7y7AG5x4KjcK`</summary>

```text
projects/ratekv/task_context/history/reviewer/loop_1.md
projects/ratekv/task_context/history/director/loop_1.md
projects/ratekv/task_context/history/agent/loop_1.md
projects/ratekv/docs/IDEA_BRIEF.md
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/paper_framing.md
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/paper_framing.md
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/paper_framing.md
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/review_report.md
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/review_report.md
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/review_report.md
projects/ratekv/task_context/history/reviewer/loop_2.md
projects/ratekv/task_context/history/director/loop_2.md
projects/ratekv/artifacts/plan_011/chart/fig1_head_delta_heatmap.md
projects/ratekv/artifacts/plan_011/chart/fig2_compounding_curve.md
projects/ratekv/artifacts/plan_011/chart/fig3_allocation_comparison.md
projects/ratekv/task_context/history/agent/loop_2.md
projects/ratekv/task_context/history/agent/loop_2_1778758749.md
projects/ratekv/task_context/history/reviewer/loop_3.md
projects/ratekv/task_context/history/director/loop_3.md
projects/ratekv/task_context/history/agent/loop_3.md
projects/ratekv/task_context/history/agent/loop_3_1778760425.md
projects/ratekv/task_context/history/agent/loop_3_1778770984.md
projects/ratekv/artifacts/_project/report/reference_audit_report.md
projects/ratekv/artifacts/reference_audit_report.md
projects/ratekv/task_context/history/reviewer/loop_4.md
projects/ratekv/task_context/director.md
projects/ratekv/task_context/history/agent/loop_4.md
projects/ratekv/task_context/history/agent/loop_4_1778773416.md
projects/ratekv/task_context/history/agent/loop_4_1778783373.md
projects/ratekv/task_context/history/agent/loop_5.md
projects/ratekv/task_context/history/reviewer/loop_5.md
projects/ratekv/task_context/history/reviewer/loop_5_1778798501.md
projects/ratekv/task_context/history/agent/loop_5_1778784705.md
projects/ratekv/artifacts/_project/report/paper_patch_audit.md
projects/ratekv/artifacts/paper_patch_audit.md
projects/ratekv/task_context/history/agent/loop_4_1778785575.md
projects/ratekv/artifacts/spike_vs_spread_literature.md
projects/ratekv/task_context/history/agent/loop_5_1778795035.md
projects/ratekv/artifacts/p0_patch_drafts.md
projects/ratekv/task_context/history/agent/loop_6.md
projects/ratekv/task_context/history/agent/loop_6_1778796766.md
projects/ratekv/task_context/history/agent/loop_6_1778798593.md
projects/ratekv/task_context/history/reviewer/loop_6.md
projects/ratekv/task_context/history/agent/loop_6_1778806193.md
projects/ratekv/task_context/history/agent/loop_7.md
projects/ratekv/task_context/history/agent/loop_5_1778806694.md
projects/ratekv/task_context/history/agent/loop_7_1778806778.md
projects/ratekv/task_context/history/agent/loop_7_1778807603.md
projects/ratekv/task_context/history/agent/loop_7_1778808893.md
projects/ratekv/task_context/history/agent/loop_7_1778809880.md
projects/ratekv/task_context/history/agent/loop_7_1778819733.md
projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8/CLAUDE.md
projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8/AGENTS.md
projects/ratekv/.claude/sessions/review_reviewer_2_ee7a8b68/CLAUDE.md
projects/ratekv/.claude/sessions/review_reviewer_2_ee7a8b68/AGENTS.md
projects/ratekv/.claude/sessions/review_director_a1fe96c5/CLAUDE.md
projects/ratekv/.claude/sessions/review_director_a1fe96c5/AGENTS.md
projects/ratekv/artifacts/review_reports/round_2.md
projects/ratekv/task_context/history/agent/loop_7_1778819736.md
projects/ratekv/.claude/sessions/agent_78ef6a44/CLAUDE.md
projects/ratekv/.claude/sessions/agent_78ef6a44/AGENTS.md
projects/ratekv/task_context/history/agent/loop_7_1778819777.md
projects/ratekv/.claude/sessions/agent_1e49e5db/CLAUDE.md
projects/ratekv/.claude/sessions/agent_1e49e5db/AGENTS.md
projects/ratekv/task_context/history/agent/loop_8.md
projects/ratekv/.claude/sessions/agent_3e0e8f72/CLAUDE.md
projects/ratekv/.claude/sessions/agent_3e0e8f72/AGENTS.md
projects/ratekv/task_context/history/agent/loop_8_1778819795.md
projects/ratekv/.claude/sessions/agent_19826e6d/CLAUDE.md
projects/ratekv/.claude/sessions/agent_19826e6d/AGENTS.md
projects/ratekv/task_context/history/agent/loop_8_1778819810.md
projects/ratekv/.claude/sessions/agent_830db028/CLAUDE.md
projects/ratekv/.claude/sessions/agent_830db028/AGENTS.md
projects/ratekv/task_context/history/agent/loop_8_1778819905.md
projects/ratekv/.claude/sessions/agent_5ba08d96/CLAUDE.md
projects/ratekv/.claude/sessions/agent_5ba08d96/AGENTS.md
projects/ratekv/task_context/history/agent/loop_8_1778821223.md
projects/ratekv/.claude/sessions/agent_4bce0d32/CLAUDE.md
projects/ratekv/.claude/sessions/agent_4bce0d32/AGENTS.md
projects/ratekv/task_context/reviewer.md
projects/ratekv/task_context/agent.md
projects/ratekv/.claude/sessions/agent_95a2eba1/CLAUDE.md
projects/ratekv/.claude/sessions/agent_95a2eba1/AGENTS.md
projects/ratekv/.claude/sessions/briefer_7c08a6fe/CLAUDE.md
projects/ratekv/.claude/sessions/briefer_7c08a6fe/AGENTS.md
projects/ratekv/memory.md
projects/ratekv/report.md
projects/ratekv/paper_framing.md
projects/ratekv/ROADMAP.md
projects/ratekv/.claude/sessions/agent_01ae092a/CLAUDE.md
projects/ratekv/.claude/sessions/agent_01ae092a/AGENTS.md
projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c/CLAUDE.md
projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c/AGENTS.md
projects/ratekv/.claude/sessions/director_72e42815/CLAUDE.md
projects/ratekv/.claude/sessions/director_72e42815/AGENTS.md
projects/ratekv/.claude/CLAUDE.md
projects/ratekv/AGENTS.md
projects/ratekv/.claude/sessions/reviewer_fe2ad71b/CLAUDE.md
projects/ratekv/.claude/sessions/reviewer_fe2ad71b/AGENTS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "201a9dcd-8e52-497e-b251-cee33a4de318",
  "isSidechain": false,
  "promptId": "f114f0f3-7484-4f66-92b9-ae6b798ef7f0",
  "type": "user",
  "uuid": "b5a656fe-7f1b-4d57-9b9a-ac5eec4ed16d",
  "toolUseResult": {
    "filenames": [
      "projects/ratekv/task_context/history/reviewer/loop_1.md",
      "projects/ratekv/task_context/history/director/loop_1.md",
      "projects/ratekv/task_context/history/agent/loop_1.md",
      "projects/ratekv/docs/IDEA_BRIEF.md",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/paper_framing.md",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/paper_framing.md",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/paper_framing.md",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/review_report.md",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/review_report.md",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/review_report.md",
      "projects/ratekv/task_context/history/reviewer/loop_2.md",
      "projects/ratekv/task_context/history/director/loop_2.md",
      "projects/ratekv/artifacts/plan_011/chart/fig1_head_delta_heatmap.md",
      "projects/ratekv/artifacts/plan_011/chart/fig2_compounding_curve.md",
      "projects/ratekv/artifacts/plan_011/chart/fig3_allocation_comparison.md",
      "projects/ratekv/task_context/history/agent/loop_2.md",
      "projects/ratekv/task_context/history/agent/loop_2_1778758749.md",
      "projects/ratekv/task_context/history/reviewer/loop_3.md",
      "projects/ratekv/task_context/history/director/loop_3.md",
      "projects/ratekv/task_context/history/agent/loop_3.md",
      "projects/ratekv/task_context/history/agent/loop_3_1778760425.md",
      "projects/ratekv/task_context/history/agent/loop_3_1778770984.md",
      "projects/ratekv/artifacts/_project/report/reference_audit_report.md",
      "projects/ratekv/artifacts/reference_audit_report.md",
      "projects/ratekv/task_context/history/reviewer/loop_4.md",
      "projects/ratekv/task_context/director.md",
      "projects/ratekv/task_context/history/agent/loop_4.md",
      "projects/ratekv/task_context/history/agent/loop_4_1778773416.md",
      "projects/ratekv/task_context/history/agent/loop_4_1778783373.md",
      "projects/ratekv/task_context/history/agent/loop_5.md",
      "projects/ratekv/task_context/history/reviewer/loop_5.md",
      "projects/ratekv/task_context/history/reviewer/loop_5_1778798501.md",
      "projects/ratekv/task_context/history/agent/loop_5_1778784705.md",
      "projects/ratekv/artifacts/_project/report/paper_patch_audit.md",
      "projects/ratekv/artifacts/paper_patch_audit.md",
      "projects/ratekv/task_context/history/agent/loop_4_1778785575.md",
      "projects/ratekv/artifacts/spike_vs_spread_literature.md",
      "projects/ratekv/task_context/history/agent/loop_5_1778795035.md",
      "projects/ratekv/artifacts/p0_patch_drafts.md",
      "projects/ratekv/task_context/history/agent/loop_6.md",
      "projects/ratekv/task_context/history/agent/loop_6_1778796766.md",
      "projects/ratekv/task_context/history/agent/loop_6_1778798593.md",
      "projects/ratekv/task_context/history/reviewer/loop_6.md",
      "projects/ratekv/task_context/history/agent/loop_6_1778806193.md",
      "projects/ratekv/task_context/history/agent/loop_7.md",
      "projects/ratekv/task_context/history/agent/loop_5_1778806694.md",
      "projects/ratekv/task_context/history/agent/loop_7_1778806778.md",
      "projects/ratekv/task_context/history/agent/loop_7_1778807603.md",
      "projects/ratekv/task_context/history/agent/loop_7_1778808893.md",
      "projects/ratekv/task_context/history/agent/loop_7_1778809880.md",
      "projects/ratekv/task_context/history/agent/loop_7_1778819733.md",
      "projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8/CLAUDE.md",
      "projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8/AGENTS.md",
      "projects/ratekv/.claude/sessions/review_reviewer_2_ee7a8b68/CLAUDE.md",
      "projects/ratekv/.claude/sessions/review_reviewer_2_ee7a8b68/AGENTS.md",
      "projects/ratekv/.claude/sessions/review_director_a1fe96c5/CLAUDE.md",
      "projects/ratekv/.claude/sessions/review_director_a1fe96c5/AGENTS.md",
      "projects/ratekv/artifacts/review_reports/round_2.md",
      "projects/ratekv/task_context/history/agent/loop_7_1778819736.md",
      "projects/ratekv/.claude/sessions/agent_78ef6a44/CLAUDE.md",
      "projects/ratekv/.claude/sessions/agent_78ef6a44/AGENTS.md",
      "projects/ratekv/task_context/history/agent/loop_7_1778819777.md",
      "projects/ratekv/.claude/sessions/agent_1e49e5db/CLAUDE.md",
      "projects/ratekv/.claude/sessions/agent_1e49e5db/AGENTS.md",
      "projects/ratekv/task_context/history/agent/loop_8.md",
      "projects/ratekv/.claude/sessions/agent_3e0e8f72/CLAUDE.md",
      "projects/ratekv/.claude/sessions/agent_3e0e8f72/AGENTS.md",
      "projects/ratekv/task_context/history/agent/loop_8_1778819795.md",
      "projects/ratekv/.claude/sessions/agent_19826e6d/CLAUDE.md",
      "projects/ratekv/.claude/sessions/agent_19826e6d/AGENTS.md",
      "projects/ratekv/task_context/history/agent/loop_8_1778819810.md",
      "projects/ratekv/.claude/sessions/agent_830db028/CLAUDE.md",
      "projects/ratekv/.claude/sessions/agent_830db028/AGENTS.md",
      "projects/ratekv/task_context/history/agent/loop_8_1778819905.md",
      "projects/ratekv/.claude/sessions/agent_5ba08d96/CLAUDE.md",
      "projects/ratekv/.claude/sessions/agent_5ba08d96/AGENTS.md",
      "projects/ratekv/task_context/history/agent/loop_8_1778821223.md",
      "projects/ratekv/.claude/sessions/agent_4bce0d32/CLAUDE.md",
      "projects/ratekv/.claude/sessions/agent_4bce0d32/AGENTS.md",
      "projects/ratekv/task_context/reviewer.md",
      "projects/ratekv/task_context/agent.md",
      "projects/ratekv/.claude/sessions/agent_95a2eba1/CLAUDE.md",
      "projects/ratekv/.claude/sessions/agent_95a2eba1/AGENTS.md",
      "projects/ratekv/.claude/sessions/briefer_7c08a6fe/CLAUDE.md",
      "projects/ratekv/.claude/sessions/briefer_7c08a6fe/AGENTS.md",
      "projects/ratekv/memory.md",
      "projects/ratekv/report.md",
      "projects/ratekv/paper_framing.md",
      "projects/ratekv/ROADMAP.md",
      "projects/ratekv/.claude/sessions/agent_01ae092a/CLAUDE.md",
      "projects/ratekv/.claude/sessions/agent_01ae092a/AGENTS.md",
      "projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c/CLAUDE.md",
      "projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c/AGENTS.md",
      "projects/ratekv/.claude/sessions/director_72e42815/CLAUDE.md",
      "projects/ratekv/.claude/sessions/director_72e42815/AGENTS.md",
      "projects/ratekv/.claude/CLAUDE.md",
      "projects/ratekv/AGENTS.md",
      "projects/ratekv/.claude/sessions/reviewer_fe2ad71b/CLAUDE.md",
      "projects/ratekv/.claude/sessions/reviewer_fe2ad71b/AGENTS.md"
    ],
    "durationMs": 24,
    "numFiles": 99,
    "truncated": false
  },
  "sourceToolAssistantUUID": "201a9dcd-8e52-497e-b251-cee33a4de318",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T09:29:13.471Z_

<details><summary>↩ Tool result · `toolu_019iSDhw8zA1LA8vh8g2TJ6j`</summary>

```text
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/imagined_experiments.yaml
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/imagined_experiments.yaml
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/imagined_experiments.yaml
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/review_context.yaml
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/review_context.yaml
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/review_context.yaml
projects/ratekv/artifacts/dream_reports/dream_20260514T002109/meta.yaml
projects/ratekv/artifacts/figures/manifest.yaml
projects/ratekv/writing_plan.yaml
projects/ratekv/experiment_plan.yaml
projects/ratekv/literature_map.yaml
projects/ratekv/artifacts/manifest.yaml
projects/ratekv/artifacts/review_issues.yaml
projects/ratekv/decisions.yaml
projects/ratekv/registry.yaml
projects/ratekv/paper_provenance.yaml
projects/ratekv/dream_registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3831a484-7348-46eb-b988-f189b75f6ca8",
  "isSidechain": false,
  "promptId": "f114f0f3-7484-4f66-92b9-ae6b798ef7f0",
  "type": "user",
  "uuid": "5b280365-e500-4bc1-95c0-83e0ca2b0c0e",
  "toolUseResult": {
    "filenames": [
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/imagined_experiments.yaml",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/imagined_experiments.yaml",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/imagined_experiments.yaml",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/review_context.yaml",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/review_context.yaml",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/review_context.yaml",
      "projects/ratekv/artifacts/dream_reports/dream_20260514T002109/meta.yaml",
      "projects/ratekv/artifacts/figures/manifest.yaml",
      "projects/ratekv/writing_plan.yaml",
      "projects/ratekv/experiment_plan.yaml",
      "projects/ratekv/literature_map.yaml",
      "projects/ratekv/artifacts/manifest.yaml",
      "projects/ratekv/artifacts/review_issues.yaml",
      "projects/ratekv/decisions.yaml",
      "projects/ratekv/registry.yaml",
      "projects/ratekv/paper_provenance.yaml",
      "projects/ratekv/dream_registry.yaml"
    ],
    "durationMs": 18,
    "numFiles": 17,
    "truncated": false
  },
  "sourceToolAssistantUUID": "3831a484-7348-46eb-b988-f189b75f6ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T09:29:13.815Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014zwjswHt2X7y7AG5x4KjcK`</summary>

```json
{
  "pattern": "projects/ratekv/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b280365-e500-4bc1-95c0-83e0ca2b0c0e",
  "isSidechain": false,
  "requestId": "req_011Cb47jYoJhyguBR7entxFu",
  "type": "assistant",
  "uuid": "201a9dcd-8e52-497e-b251-cee33a4de318",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPHZG17U7zwYLLw6YVhR6e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 43363,
      "output_tokens": 4754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4754,
          "cache_read_input_tokens": 43363,
          "cache_creation_input_tokens": 2394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2394
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Qwen2.5-14B 不是 Spread 或 MCKP 无效，decision rule 出现 false positive/negative，核心 diagnostic 叙事不成立 核心假设：['Qwen2.5-14B concentration ≥0.50 但 MCKP 无改善（类似 Yi-1.5，d…",
  "leafUuid": "b5a656fe-7f1b-4d57-9b9a-ac5eec4ed16d",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing when per-head KV cache quantization helps across architectures",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Assistant

_source line 19 · 2026-05-15T09:29:16.995Z_

<details><summary>Logged reasoning block</summary>

```text
Let me check the existing worst-tier dream report and the experiment plan to understand what's already been done and what format to follow.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5a656fe-7f1b-4d57-9b9a-ac5eec4ed16d",
  "isSidechain": false,
  "requestId": "req_011Cb47rVAE783d2GRkTw85h",
  "type": "assistant",
  "uuid": "1c143dd0-ebd2-4ee9-8b24-1feed9348137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfSVXM5Q3dT1Gqs8NnfSYG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7348,
      "cache_read_input_tokens": 45757,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7348,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 45757,
          "cache_creation_input_tokens": 7348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7348
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T09:29:17.981Z_

<details open><summary>🔧 Tool call — Read · `toolu_019hNBeQXn7VgUQ3pgNqXdCm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c143dd0-ebd2-4ee9-8b24-1feed9348137",
  "isSidechain": false,
  "requestId": "req_011Cb47rVAE783d2GRkTw85h",
  "type": "assistant",
  "uuid": "8195b566-a605-49b3-9017-db57c67e1abb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfSVXM5Q3dT1Gqs8NnfSYG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7348,
      "cache_read_input_tokens": 45757,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7348,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 45757,
          "cache_creation_input_tokens": 7348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7348
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T09:29:17.986Z_

<details><summary>↩ Tool result · `toolu_019hNBeQXn7VgUQ3pgNqXdCm`</summary>

```text
1	tier: worst
2	narrative_guidance: '原始 framing 的三条 claims 都无法原样保留。从 "general method paper" 转为 "empirical
3	  analysis paper with method contribution"。新核心叙事：Per-head KV cache sensitivity is
4	  architecture-dependent — 我们提供首个跨模型族系统刻画，揭示 compounding effects 与 GQA ratio 相关，并表明
5	  constrained discrete optimization 是必要的但最优 constraints 是 model-specific 的。Qwen 结果作为
6	  strong positive case study 而非 general claim；跨模型差异本身作为 empirical finding； 强调 MCKP
7	  framework 的 flexibility 而非 specific constraint 的 universality。 仍冲 EMNLP Main，positioning
8	  从 "efficient method" 转向 "empirical analysis + practical framework"。
9	
10	  '
11	imagined_experiments:
12	- name: L0 Auto-Discovery (No L0 Exclusion)
13	  plan_id: plan_001
14	  description: '去掉 L0 exclusion 硬约束，仅保留 max_2bit=8，观察 solver 是否仍从 profiling 数据自动将
15	    Layer 0 heads 分配到 8-bit。
16	
17	    '
18	  expected_results:
19	    qwen_no_l0excl_ppl_wikitext: 17.2
20	    qwen_baseline_constrained_ppl: 11.23
21	    ppl_degradation_vs_constrained_pct: 53.2
22	    l0_heads_assigned_8bit: 0
23	    l0_heads_assigned_4bit: 5
24	    l0_heads_assigned_2bit: 2
25	    solver_auto_discovers_l0: false
26	  result_rationale: 'Profiler 在 per-head independent 测量下，L0 heads 的 delta 虽然绝对值最高，
27	    但在 MCKP budget 竞争中，solver 倾向于将 8-bit 预算分配给中层若干 high-delta heads（它们的 delta-per-bit-cost
28	    ratio 更优）。L0 的关键性来自 其与后续层的 compounding interaction，而非 independent delta 本身。 去掉显式
29	    L0 exclusion 后，solver 将 L0 部分 heads 降至 4-bit 甚至 2-bit， 触发严重的 compounding 劣化。PPL
30	    从 11.23 恶化到 ~17.2（+53%）， 远超 10% 阈值。这证明 profiler 信号不足以自动发现 L0 的特殊地位， L0 exclusion
31	    本质上是 domain knowledge injection 而非 data-driven discovery。
32	
33	    '
34	  tables:
35	  - name: L0 Exclusion Ablation
36	    columns:
37	    - config
38	    - l0_bitwidth
39	    - ppl_wikitext
40	    - delta_vs_constrained
41	    rows:
42	    - - constrained_with_l0excl
43	      - 8-bit (forced)
44	      - 11.23
45	      - baseline
46	    - - no_l0excl_max2bit8
47	      - mixed 4/2-bit (solver)
48	      - 17.2
49	      - +53.2%
50	    - - uniform_4bit
51	      - 4-bit
52	      - 15.45
53	      - +37.6%
54	  figures_description:
55	  - 'Bar chart: PPL comparison across three configs. no_l0excl 比 uniform 4-bit 还差，说明
56	    solver 在无 L0 保护时做出了比均匀分配更糟的选择。'
57	  analysis: 'Solver 不仅未发现 L0，反而因 budget 优化将 L0 降级，结果比 uniform 更差。 这说明 "automatic discovery"
58	    claim 不成立——L0 protection 是 necessary prior knowledge。在 reframed narrative 中，这反而强化了
59	    "constraints as regularization" 的论点：正确的 constraint 需要 model-specific knowledge，
60	    而非纯数据驱动。
61	
62	    '
63	- name: Llama-3.1-8B Full Pipeline Replication
64	  plan_id: plan_002
65	  description: '在 Llama-3.1-8B (GQA 4:1) 上复现完整 pipeline：profile → constrained MCKP
66	    → eval。
67	
68	    '
69	  expected_results:
70	    llama_uniform4bit_ppl_wikitext: 8.95
71	    llama_constrained_mckp_ppl_wikitext: 8.31
72	    llama_ppl_improvement_pct: 7.2
73	    llama_unconstrained_mckp_ppl: 9.83
74	    llama_l0_delta_rank: not dominant (rank 12-18 among 32 layers)
75	    llama_num_heads_determining_70pct_degradation: ~15% of heads (vs Qwen 3.6%)
76	    llama_compounding_severity: mild
77	    llama_optimal_max2bit: 24
78	  result_rationale: 'Llama 的 GQA ratio 4:1（每层 8 KV heads，共 256 heads）使得 sensitivity
79	    分布比 Qwen (GQA 7:1, 每层 4 KV heads, 共 112 heads) 更均匀。更多的 KV heads 意味着每个 head 承载更少的信息量，individual
80	    head 的 failure 影响更小。 L0 不再是 dominant sensitivity source——sensitivity 分散在多个层的多个
81	    heads 上。 Constrained MCKP 仍优于 uniform（7.2%），但远低于 Qwen 的 27%， 因为 head heterogeneity
82	    本身更低。Unconstrained MCKP 的 PPL（9.83）虽差于 constrained 但并未 catastrophic failure（对比
83	    Qwen 的 36.92）， 因为 compounding effect 在 GQA 4:1 下更温和——更多 heads 分担了 extreme quantization
84	    的 joint distortion。这削弱了 "compounding is universal and catastrophic" 的论点。
85	
86	    '
87	  tables:
88	  - name: Llama-3.1-8B Allocation Results
89	    columns:
90	    - method
91	    - ppl_wikitext
92	    - compression
93	    - improvement_vs_uniform
94	    rows:
95	    - - uniform_4bit
96	      - 8.95
97	      - 4×
98	      - baseline
99	    - - constrained_mckp
100	      - 8.31
101	      - 4×
102	      - 7.2%
103	    - - unconstrained_mckp
104	      - 9.83
105	      - 4×
106	      - -9.8% (worse than uniform)
107	  figures_description:
108	  - 'Per-head delta heatmap (32 layers × 8 heads): 相比 Qwen 的 L0 spike pattern，Llama
109	    呈现更均匀的分布，peak sensitivity 分散在 L0-L3 和 L28-L31。'
110	  - 'Sensitivity CDF: Llama 需要 ~15% 的 heads 才覆盖 70% degradation，Qwen 仅需 3.6%。'
111	  analysis: '7.2% 改进虽然 positive 但 marginal——reviewer 会质疑是否 justifies method complexity。Unconstrained
112	    未 catastrophic failure 意味着 Llama 上 cardinality constraint 的 motivation 更弱。核心发现：GQA
113	    ratio 越低， sensitivity 越分散，constrained MCKP 的边际收益越小。 这支持 "sensitivity structure
114	    is architecture-dependent" 的 reframed narrative。
115	
116	    '
117	- name: Mistral-7B-v0.3 Full Pipeline Replication
118	  plan_id: plan_003
119	  description: '在 Mistral-7B-v0.3 上复现完整 pipeline，建立跨架构有效性。
120	
121	    '
122	  expected_results:
123	    mistral_uniform4bit_ppl_wikitext: 8.42
124	    mistral_constrained_mckp_ppl_wikitext: 7.93
125	    mistral_ppl_improvement_pct: 5.8
126	    mistral_unconstrained_mckp_ppl: 8.71
127	    mistral_l0_delta_rank: rank 5-8 among 32 layers
128	    mistral_sliding_window_complication: true
129	    mistral_optimal_max2bit: 20
130	  result_rationale: 'Mistral 同样是 GQA 4:1（与 Llama 相同），但 sliding window attention 改变了
131	    KV cache 的 usage pattern——早期 token 的 KV 被 evict，使得 对 precision 的依赖模式不同。Sensitivity
132	    分布更接近 Llama（分散型）， 但 sliding window 还引入了 position-dependent sensitivity 的额外复杂度，
133	    我们的 position-agnostic profiler 无法捕获。改进幅度 5.8% 进一步确认 低 GQA ratio 下 method 边际收益有限。Unconstrained
134	    MCKP PPL 8.71 仅比 uniform 差 3.4%——完全没有 catastrophic failure， 进一步削弱 compounding
135	    的 universal catastrophic 叙事。
136	
137	    '
138	  tables:
139	  - name: Mistral-7B Results
140	    columns:
141	    - method
142	    - ppl_wikitext
143	    - compression
144	    - improvement_vs_uniform
145	    rows:
146	    - - uniform_4bit
147	      - 8.42
148	      - 4×
149	      - baseline
150	    - - constrained_mckp
151	      - 7.93
152	      - 4×
153	      - 5.8%
154	    - - unconstrained_mckp
155	      - 8.71
156	      - 4×
157	      - -3.4%
158	  figures_description:
159	  - 'Per-head delta heatmap: 类似 Llama 的分散模式，但 sliding window 导致后半层 sensitivity 整体偏高。'
160	  analysis: 'Mistral 的 5.8% 改进是三个模型中最低的。Sliding window attention 使得 我们的 static profiling
161	    假设部分失效。与 Llama 结果联合看， GQA 4:1 模型上 constrained MCKP 的 value proposition 弱于 GQA
162	    7:1。 但这正是 reframed narrative 的核心 finding：GQA ratio 决定了 head sensitivity 的集中度，进而决定了
163	    per-head allocation 的收益空间。
164	
165	    '
166	- name: Compounding Effect Sweep (Qwen)
167	  plan_id: plan_004
168	  description: '在 Qwen2.5-7B 上 sweep max_2bit from 0 to 112，绘制 PPL vs max_2bit curve，
169	    刻画 compounding threshold。
170	
171	    '
172	  expected_results:
173	    qwen_compounding_curve:
174	      max2bit_0: 11.89
175	      max2bit_4: 11.45
176	      max2bit_8: 11.23
177	      max2bit_16: 11.31
178	      max2bit_24: 12.05
179	      max2bit_48: 15.78
180	      max2bit_75: 24.31
181	      max2bit_112: 36.92
182	    elbow_k_qwen: 8
183	    curve_shape: hockey stick with clear elbow at k=8
184	  result_rationale: 'Qwen 的 GQA 7:1 产生少量（112 个）但每个 information-dense 的 KV heads。 当少量
185	    heads 被极端量化时，joint distortion 仍可控（k≤8 时 PPL 平稳）， 但超过阈值后 compounding 急剧恶化——因为 dense
186	    heads 之间的 interaction 在 extreme quantization 下是超线性的。k=8 处有清晰 elbow。 这个 curve 在
187	    Qwen 上非常漂亮，是 paper 的核心 figure 之一。
188	
189	    '
190	  tables:
191	  - name: Compounding Sweep (Qwen2.5-7B)
192	    columns:
193	    - max_2bit_k
194	    - ppl_wikitext
195	    - num_heads_at_2bit_actual
196	    - delta_vs_k8
197	    rows:
198	    - - 0
199	      - 11.89
200	      - 0
201	      - +5.9%
202	    - - 4
203	      - 11.45
204	      - 4
205	      - +2.0%
206	    - - 8
207	      - 11.23
208	      - 8
209	      - baseline
210	    - - 16
211	      - 11.31
212	      - 16
213	      - +0.7%
214	    - - 24
215	      - 12.05
216	      - 24
217	      - +7.3%
218	    - - 48
219	      - 15.78
220	      - 44
221	      - +40.5%
222	    - - 75
223	      - 24.31
224	      - 68
225	      - +116.6%
226	    - - 112
227	      - 36.92
228	      - 95
229	      - +228.8%
230	  figures_description:
231	  - 'PPL vs max_2bit curve (hockey stick): x 轴 max_2bit k, y 轴 WikiText-2 PPL. 清晰
232	    elbow at k=8. Annotate optimal zone k∈[4,16].'
233	  analysis: 'Qwen 上 compounding curve 有教科书般清晰的 elbow，但问题在于 这种 pattern 是否跨模型复现——在 worst
234	    档下，Llama 和 Mistral 上该 curve 预计平坦或无 elbow（见 plan_002/003 的 unconstrained 结果）。 Reframed
235	    narrative 将此作为 "GQA-ratio-dependent compounding" 的 case study 而非 universal phenomenon。
236	
237	    '
238	- name: Budget Sweep (Qwen)
239	  plan_id: plan_005
240	  description: '在 Qwen2.5-7B 上测试 constrained MCKP 在 2×, 4×, 8× 压缩率下的表现， 与同 budget
241	    的 uniform baseline 对比。
242	
243	    '
244	  expected_results:
245	    qwen_2x_uniform_ppl: 7.82
246	    qwen_2x_constrained_ppl: 7.45
247	    qwen_2x_improvement_pct: 4.7
248	    qwen_4x_uniform_ppl: 15.45
249	    qwen_4x_constrained_ppl: 11.23
250	    qwen_4x_improvement_pct: 27.3
251	    qwen_8x_uniform_ppl: 89.4
252	    qwen_8x_constrained_ppl: 42.6
253	    qwen_8x_improvement_pct: 52.3
254	  result_rationale: '2× 压缩下 budget 充裕（平均 8-bit），大部分 heads 已在安全区间， per-head optimization
255	    的空间有限（4.7%）。4× 是 sweet spot（27.3%）， 与已有 MVP 结果一致。8× 极端压缩下，constrained MCKP 改进幅度最大
256	    （52.3%）但绝对 PPL 仍然很高（42.6），因为 budget 不足以保护 所有 critical heads——即使最优分配也无法避免严重质量损失。
257	    这些数字都是 Qwen-specific 的，鉴于 Llama/Mistral 在 4× 时 仅有 5-7% 改进，它们在 2× 和 8× 下的改进预计更小。
258	
259	    '
260	  tables:
261	  - name: Budget Sweep (Qwen2.5-7B)
262	    columns:
263	    - compression
264	    - uniform_ppl
265	    - constrained_ppl
266	    - improvement_pct
267	    rows:
268	    - - 2×
269	      - 7.82
270	      - 7.45
271	      - 4.7%
272	    - - 4×
273	      - 15.45
274	      - 11.23
275	      - 27.3%
276	    - - 8×
277	      - 89.4
278	      - 42.6
279	      - 52.3%
280	  figures_description:
281	  - 'Bar chart: uniform vs constrained PPL at each compression ratio. 4× 是 narrative
282	    sweet spot。'
283	  - 'Line plot: improvement % vs compression ratio. 随压缩率增加收益增大，但绝对 PPL 也恶化。'
284	  analysis: 'Budget sweep 在 Qwen 上 works well，但 reviewer 会要求看 Llama/Mistral 的 budget
285	    sweep——在 worst 档下这些预计仅有 2-5% 改进空间，弱化 method 的 general value proposition。 Reframe:
286	    强调 per-head allocation 在高压缩率下更 critical， 且 benefit 与 architecture 的 sensitivity
287	    concentration 正相关。
288	
289	    '
290	- name: High-Resolution Profiling (Qwen)
291	  plan_id: plan_006
292	  description: '用 64 seq × 2048 tokens（vs 当前 16×512）做高分辨率 profiling， 重跑 MCKP，测试是否发现
293	    mid-layer heterogeneity 并改善分配。
294	
295	    '
296	  expected_results:
297	    hires_nonzero_head_pct: 31
298	    lores_nonzero_head_pct: 16
299	    hires_constrained_ppl: 11.09
300	    lores_constrained_ppl: 11.23
301	    hires_improvement_over_lores_pct: 1.2
302	    hires_new_midlayer_discoveries: 3
303	    hires_profiling_time_hours: 2.8
304	  result_rationale: '高分辨率 profiling 将 nonzero-delta heads 从 16% 提升到 31%， 确实发现了几个 mid-layer
305	    heads 有 measurable sensitivity。 但这些 newly-discovered heads 的 delta 仅占 total distortion
306	    的 ~3%， 对 MCKP allocation 几乎无影响——solver 仍然做出几乎相同的分配决策。 PPL 仅从 11.23 降至 11.09（1.2%
307	    改善），不足以 justify 4× 的 profiling compute overhead。根本原因：在 2-bit 分辨率下， 大部分 mid-layer
308	    heads 确实 insensitive（这是真信号而非 measurement noise），profiler resolution 不是 bottleneck，
309	    head sensitivity 的 long-tail distribution 本身是 fundamental。
310	
311	    '
312	  tables:
313	  - name: Profiling Resolution Comparison
314	    columns:
315	    - resolution
316	    - nonzero_head_pct
317	    - constrained_ppl
318	    - profiling_hours
319	    rows:
320	    - - 16×512 (lores)
321	      - 16%
322	      - 11.23
323	      - 0.7
324	    - - 64×2048 (hires)
325	      - 31%
326	      - 11.09
327	      - 2.8
328	  figures_description:
329	  - 'Delta heatmap comparison: lores vs hires. Hires 在 mid-layers 多出几个非零点，但量级很小。'
330	  - 'Scatter plot: lores delta vs hires delta per head. 高相关 (r>0.95)，说明 lores 已足够。'
331	  analysis: 'Hires profiling 是 negative result：profiler resolution 并非 fundamental
332	    limitation，sensitivity 的 sparse 分布本身是 architecture 的 intrinsic property。这其实是 informative
333	    negative—— 说明 16×512 已经是 cost-effective 的 profiling budget。 但无法 claim "better
334	    profiling → better allocation"。
335	
336	    '
337	- name: C4 Cross-Dataset Evaluation (Qwen)
338	  plan_id: plan_007
339	  description: '在 C4 上评估 Qwen2.5-7B 的 constrained MCKP 和 uniform 4-bit， 测试结果是否 WikiText-2
340	    specific。
341	
342	    '
343	  expected_results:
344	    c4_uniform4bit_ppl: 18.73
345	    c4_constrained_mckp_ppl: 16.92
346	    c4_improvement_pct: 9.7
347	    c4_rank_correlation_with_wikitext: 0.58
348	    c4_allocation_agreement_pct: 72
349	  result_rationale: 'C4 是更多样化的 web corpus，分布与 WikiText-2 有显著差异。 Per-head sensitivity
350	    在 C4 上的排序与 WikiText-2 仅有中等相关 (rank corr 0.58)，因为不同 domain 的 text 激活不同 heads。 改进幅度从
351	    27% 降至 9.7%——仍 positive 但显著缩水。 Allocation agreement 72% 意味着 ~28% 的 heads 在两个 dataset
352	    上被分配了不同的 bit-width，暗示 optimal allocation 是 distribution-dependent 的。这弱化了 "one-shot
353	    profiling" 的实用性叙事。
354	
355	    '
356	  tables:
357	  - name: C4 Evaluation (Qwen2.5-7B)
358	    columns:
359	    - dataset
360	    - uniform_ppl
361	    - constrained_ppl
362	    - improvement_pct
363	    rows:
364	    - - WikiText-2
365	      - 15.45
366	      - 11.23
367	      - 27.3%
368	    - - C4
369	      - 18.73
370	      - 16.92
371	      - 9.7%
372	  - name: Cross-Dataset Allocation Agreement
373	    columns:
374	    - metric
375	    - value
376	    rows:
377	    - - rank_correlation
378	      - 0.58
379	    - - allocation_agreement
380	      - 72%
381	    - - l0_protection_consistent
382	      - 'yes'
383	  figures_description:
384	  - 'Scatter: per-head delta (WikiText-2) vs per-head delta (C4). 中等相关，visible outliers
385	    in mid-layers.'
386	  analysis: 'C4 上 9.7% 改进刚好低于 10% 的 "显著" 阈值（在 worst 定义中）。 Rank correlation 0.58 处于
387	    worst 范围内 [0.45, 0.7]。 这意味着 profiling 的 calibration data 选择 matters—— reviewer
388	    会问 "which calibration set should a practitioner use?" Reframe: 承认 allocation 是
389	    partially distribution-dependent， 但 L0 protection 是 robust across datasets。
390	
391	    '
392	- name: RateQuant Comparison (Reverse Waterfilling)
393	  plan_id: plan_008
394	  description: '实现 RateQuant 的 reverse waterfilling 在离散 action set 上的版本， 与 constrained
395	    MCKP 对比。
396	
397	    '
398	  expected_results:
399	    llama_waterfilling_ppl: 8.52
400	    llama_constrained_ppl: 8.31
401	    llama_waterfilling_vs_mckp_gap: 2.5
402	    qwen_waterfilling_ppl: 12.87
403	    qwen_constrained_ppl: 11.23
404	    qwen_waterfilling_vs_mckp_gap: 14.6
405	  result_rationale: 'Reverse waterfilling 本质上是 continuous relaxation + rounding， 在
406	    Llama 这种 sensitivity 分散的模型上，rounding error 较小 （因为 head 之间 delta 差异小，rounding 方向影响有限），
407	    所以 waterfilling 与 MCKP 差距仅 2.5%。在 Qwen 上差距更大 （14.6%），因为 L0 的 extreme sensitivity
408	    导致 rounding 在 critical head 上犯错——但这个差距比 constrained vs unconstrained 的差距（11.23
409	    vs 36.92）小得多，reviewer 可能认为 waterfilling + L0 heuristic 就足够了，不需要完整 MCKP machinery。
410	
411	    '
412	  tables:
413	  - name: Waterfilling vs MCKP
414	    columns:
415	    - model
416	    - waterfilling_ppl
417	    - constrained_mckp_ppl
418	    - gap_pct
419	    rows:
420	    - - Qwen2.5-7B
421	      - 12.87
422	      - 11.23
423	      - 14.6%
424	    - - Llama-3.1-8B
425	      - 8.52
426	      - 8.31
427	      - 2.5%
428	  figures_description:
429	  - 'Bar chart: waterfilling vs MCKP across models. Qwen 差距明显，Llama 差距 marginal。'
430	  analysis: '在 Llama 上 waterfilling 与 MCKP 几乎等效（2.5% gap）， 削弱了 "discrete MCKP is fundamentally
431	    necessary" 的 claim。 Reviewer 会问：如果只在 GQA 7:1 模型上 MCKP 明显优于 waterfilling， 那这是 method
432	    contribution 还是 Qwen-specific trick？ Reframe: 强调 MCKP framework 的 flexibility（能自然嵌入
433	    cardinality constraint，waterfilling 不行）。
434	
435	    '
436	- name: Oracle Comparison (Brute-Force Subset)
437	  plan_id: plan_009
438	  description: '在 Qwen 的 3-4 layer groups 上做 brute-force 穷举最优分配， 量化 MCKP 与 oracle
439	    的差距。
440	
441	    '
442	  expected_results:
443	    oracle_subset_ppl: 10.41
444	    mckp_subset_ppl: 10.78
445	    mckp_to_oracle_gap_pct: 3.6
446	    oracle_allocation_agrees_with_mckp_pct: 81
447	  result_rationale: '在小规模子集上，brute-force oracle 能利用 joint evaluation 捕捉 compounding
448	    interaction，找到 MCKP additive assumption 遗漏的 inter-head synergies。3.6% 的 gap 说明
449	    MCKP 虽然 near-optimal 但并非 optimal——additive distortion model 即使加了 cardinality constraint
450	    也有 residual error。 在 worst 档下，这个 gap 比预期大（理想情况应 <2%）， 暗示 compounding 的 non-additivity
451	    比 cardinality constraint 能 capture 的更复杂（涉及 specific head combinations， 不仅仅是 count）。
452	
453	    '
454	  tables:
455	  - name: Oracle vs MCKP (Subset, Qwen2.5-7B)
456	    columns:
457	    - method
458	    - subset_ppl
459	    - gap_to_oracle
460	    rows:
461	    - - brute_force_oracle
462	      - 10.41
463	      - 0%
464	    - - constrained_mckp
465	      - 10.78
466	      - 3.6%
467	    - - unconstrained_mckp
468	      - 14.93
469	      - 43.4%
470	  figures_description:
471	  - 'Allocation diff heatmap: oracle vs MCKP on subset layers. ~19% heads 被不同分配。'
472	  analysis: '3.6% gap 虽然不大但 non-trivial。在 reframed narrative 中， 这是 honest limitation：cardinality
473	    constraint 是 first-order approximation，full interaction structure 需要更复杂的 constraint
474	    设计或 iterative profiling。
475	
476	    '
477	- name: Cross-Domain Calibration Robustness
478	  plan_id: plan_010
479	  description: '用 C4 calibrate、WikiText-2 evaluate（及反向），报告 per-head allocation 跨 calibration
480	    source 的一致率。
481	
482	    '
483	  expected_results:
484	    calib_c4_eval_wiki_ppl: 12.14
485	    calib_wiki_eval_wiki_ppl: 11.23
486	    calib_c4_eval_c4_ppl: 16.92
487	    calib_wiki_eval_c4_ppl: 17.85
488	    cross_calib_allocation_agreement_pct: 68
489	    l0_robust_across_calib: true
490	  result_rationale: 'Calibration data 影响 per-head delta 估计。C4 calibration 在 WikiText-2
491	    上评估时 PPL 12.14（vs 同 domain 的 11.23）， degradation 8.1%。反向（wiki calib → C4 eval）degradation
492	    5.5%。 Allocation agreement 68% 低于理想（>85%），说明约 1/3 的 heads 的最优 bit-width 是 distribution-dependent。
493	    L0 protection 跨 calibration 一致（因为 L0 在任何 distribution 上 都是 dominant），但 mid-layer
494	    分配不稳定。
495	
496	    '
497	  tables:
498	  - name: Cross-Calibration Results (Qwen2.5-7B)
499	    columns:
500	    - calibration
501	    - eval_dataset
502	    - ppl
503	    - vs_matched_calib
504	    rows:
505	    - - WikiText-2
506	      - WikiText-2
507	      - 11.23
508	      - baseline
509	    - - C4
510	      - WikiText-2
511	      - 12.14
512	      - +8.1%
513	    - - C4
514	      - C4
515	      - 16.92
516	      - baseline
517	    - - WikiText-2
518	      - C4
519	      - 17.85
520	      - +5.5%
521	  figures_description:
522	  - 'Heatmap diff: C4-calibrated vs Wiki-calibrated allocation. 差异集中在 mid-layers。'
523	  analysis: 'Cross-calibration degradation 是 real concern。Practitioner 需要 选择与 deployment
524	    distribution 匹配的 calibration data。 在 reframed narrative 中，这是 practical limitation
525	    的 honest characterization，也是 future work direction。
526	
527	    '
528	- name: Head Sensitivity Visualization
529	  plan_id: plan_011
530	  description: '生成 paper-quality figures：per-head delta heatmap、compounding curve、
531	    budget allocation comparison。
532	
533	    '
534	  expected_results:
535	    figures_generated: 4
536	    key_visual_finding: cross-model heatmap comparison dramatically shows architecture-dependent
537	      sensitivity
538	  result_rationale: 'Visualization 本身不产生新数据，但在 worst 档下，cross-model heatmap 成为 paper
539	    最重要的 figure——直观展示 Qwen (concentrated, L0-dominant) vs Llama/Mistral (dispersed,
540	    no single dominant layer) 的对比。Compounding curve 只在 Qwen 上有 dramatic elbow， Llama/Mistral
541	    的 curve 相对平坦。这些 visual 恰好 serve reframed narrative。
542	
543	    '
544	  tables: []
545	  figures_description:
546	  - 'Figure 1: 三模型 per-head delta heatmap 横向对比 (3 panels). Qwen 的 L0 spike 非常醒目，Llama/Mistral
547	    分散。'
548	  - 'Figure 2: Compounding effect curves (3 lines on same plot). Qwen hockey stick,
549	    Llama/Mistral 近似线性。'
550	  - 'Figure 3: Budget allocation Sankey diagram — bits flow from budget to layers
551	    to heads。'
552	  - 'Figure 4: GQA ratio vs sensitivity concentration scatter (3 data points + trend).'
553	  analysis: 'Visualization 在 worst 档下反而更有 impact，因为跨模型差异 本身就是 visually striking finding。
554	
555	    '
556	- name: Downstream Task Evaluation (MMLU/LongBench)
557	  plan_id: plan_012
558	  description: '在 Qwen2.5-7B 4× 压缩下跑 MMLU 和 LongBench，测试 PPL 改进 是否 translate to downstream
559	    performance。
560	
561	    '
562	  expected_results:
563	    qwen_fp16_mmlu: 68.2
564	    qwen_uniform4bit_mmlu: 64.1
565	    qwen_constrained_mmlu: 65.8
566	    qwen_mmlu_recovery_pct: 41.5
567	    qwen_fp16_longbench_avg: 45.3
568	    qwen_uniform4bit_longbench_avg: 38.7
569	    qwen_constrained_longbench_avg: 41.2
570	    qwen_longbench_recovery_pct: 37.9
571	  result_rationale: 'PPL 改进（27%）不会线性 translate 到 downstream tasks。 MMLU 是 knowledge-intensive
572	    的 multiple-choice task， quantization 主要影响 calibration（logit precision）而非 knowledge
573	    recall，所以 recovery 有限（41.5%）。 LongBench 涉及 long context，KV cache quantization
574	    对 long-range attention 的影响更大，但 constrained MCKP 的 per-head allocation 在 long context
575	    下的 optimality 可能不同于 short context（profiling 用 2048 tokens）， 导致 recovery 更低（37.9%）。整体
576	    downstream improvement 存在但 modest，不足以成为独立 claim。
577	
578	    '
579	  tables:
580	  - name: Downstream Performance (Qwen2.5-7B, 4×)
581	    columns:
582	    - task
583	    - fp16
584	    - uniform_4bit
585	    - constrained_mckp
586	    - recovery_pct
587	    rows:
588	    - - MMLU
589	      - 68.2
590	      - 64.1
591	      - 65.8
592	      - 41.5%
593	    - - LongBench_avg
594	      - 45.3
595	      - 38.7
596	      - 41.2
597	      - 37.9%
598	  figures_description:
599	  - 'Grouped bar chart: FP16 / uniform / constrained on MMLU and LongBench.'
600	  analysis: 'Downstream results 是 positive but modest。在 worst 档下 不足以作为 strong selling
601	    point。建议在 paper 中放为 supplementary experiment，主叙事仍以 PPL 为核心 metric， downstream
602	    作为 sanity check。
603	
604	    '
605	- name: 70B Profiling-Only (Qwen2.5-72B)
606	  plan_id: plan_013
607	  description: '在 Qwen2.5-72B 上只跑 distortion profiling（不做完整 eval）， 分析 sensitivity
608	    patterns 是否随 model size 缩放。
609	
610	    '
611	  expected_results:
612	    qwen72b_l0_dominance: true
613	    qwen72b_l0_delta_ratio_vs_avg: ~60× (vs 7B 的 100×)
614	    qwen72b_nonzero_head_pct: 22
615	    qwen72b_sensitivity_concentration: 5.1% heads cover 70% degradation
616	    qwen72b_gqa_ratio: 7:1 (same as 7B)
617	  result_rationale: '72B 与 7B 共享 GQA 7:1 架构，所以 L0 dominance 保持（支持 GQA-ratio-dependent
618	    hypothesis）。但 72B 有 80 layers vs 7B 的 28， 更多层分摊了 sensitivity，L0 的 relative dominance
619	    降低 （60× vs 100×）。Nonzero head pct 22% 略高于 7B 的 16%， 因为更深的 model 有更多层的 heads 对
620	    quantization 有 non-trivial sensitivity。但 concentration 仍然高（5.1%）， 确认 GQA 7:1 架构的
621	    sensitivity 集中特性。
622	
623	    '
624	  tables:
625	  - name: Scale Comparison (Qwen Family)
626	    columns:
627	    - model
628	    - layers
629	    - kv_heads
630	    - l0_delta_ratio
631	    - nonzero_pct
632	    - top_heads_for_70pct
633	    rows:
634	    - - Qwen2.5-7B
635	      - 28
636	      - 112
637	      - 100×
638	      - 16%
639	      - 3.6%
640	    - - Qwen2.5-72B
641	      - 80
642	      - 320
643	      - 60×
644	      - 22%
645	      - 5.1%
646	  figures_description:
647	  - 'Per-head delta heatmap: 72B (80×4). 与 7B 相同的 L0 spike pattern，但 relative magnitude
648	    较小。'
649	  analysis: 72B profiling 支持 GQA-ratio-dependent sensitivity hypothesis—— 同 GQA ratio
650	    的不同 model sizes 有相似但不完全相同的 pattern。 在 worst 档下，这是 supporting evidence for reframed
651	    narrative， 但不足以 claim "method scales to 70B" 因为我们没有做完整 eval。 作为 paper 的 supplementary
652	    evidence 足够。
653	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8195b566-a605-49b3-9017-db57c67e1abb",
  "isSidechain": false,
  "promptId": "f114f0f3-7484-4f66-92b9-ae6b798ef7f0",
  "type": "user",
  "uuid": "542a7635-6403-4a44-991d-99bf7b26415c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/imagined_experiments.yaml",
      "content": "tier: worst\nnarrative_guidance: '原始 framing 的三条 claims 都无法原样保留。从 \"general method paper\" 转为 \"empirical\n  analysis paper with method contribution\"。新核心叙事：Per-head KV cache sensitivity is\n  architecture-dependent — 我们提供首个跨模型族系统刻画，揭示 compounding effects 与 GQA ratio 相关，并表明\n  constrained discrete optimization 是必要的但最优 constraints 是 model-specific 的。Qwen 结果作为\n  strong positive case study 而非 general claim；跨模型差异本身作为 empirical finding； 强调 MCKP\n  framework 的 flexibility 而非 specific constraint 的 universality。 仍冲 EMNLP Main，positioning\n  从 \"efficient method\" 转向 \"empirical analysis + practical framework\"。\n\n  '\nimagined_experiments:\n- name: L0 Auto-Discovery (No L0 Exclusion)\n  plan_id: plan_001\n  description: '去掉 L0 exclusion 硬约束，仅保留 max_2bit=8，观察 solver 是否仍从 profiling 数据自动将\n    Layer 0 heads 分配到 8-bit。\n\n    '\n  expected_results:\n    qwen_no_l0excl_ppl_wikitext: 17.2\n    qwen_baseline_constrained_ppl: 11.23\n    ppl_degradation_vs_constrained_pct: 53.2\n    l0_heads_assigned_8bit: 0\n    l0_heads_assigned_4bit: 5\n    l0_heads_assigned_2bit: 2\n    solver_auto_discovers_l0: false\n  result_rationale: 'Profiler 在 per-head independent 测量下，L0 heads 的 delta 虽然绝对值最高，\n    但在 MCKP budget 竞争中，solver 倾向于将 8-bit 预算分配给中层若干 high-delta heads（它们的 delta-per-bit-cost\n    ratio 更优）。L0 的关键性来自 其与后续层的 compounding interaction，而非 independent delta 本身。 去掉显式\n    L0 exclusion 后，solver 将 L0 部分 heads 降至 4-bit 甚至 2-bit， 触发严重的 compounding 劣化。PPL\n    从 11.23 恶化到 ~17.2（+53%）， 远超 10% 阈值。这证明 profiler 信号不足以自动发现 L0 的特殊地位， L0 exclusion\n    本质上是 domain knowledge injection 而非 data-driven discovery。\n\n    '\n  tables:\n  - name: L0 Exclusion Ablation\n    columns:\n    - config\n    - l0_bitwidth\n    - ppl_wikitext\n    - delta_vs_constrained\n    rows:\n    - - constrained_with_l0excl\n      - 8-bit (forced)\n      - 11.23\n      - baseline\n    - - no_l0excl_max2bit8\n      - mixed 4/2-bit (solver)\n      - 17.2\n      - +53.2%\n    - - uniform_4bit\n      - 4-bit\n      - 15.45\n      - +37.6%\n  figures_description:\n  - 'Bar chart: PPL comparison across three configs. no_l0excl 比 uniform 4-bit 还差，说明\n    solver 在无 L0 保护时做出了比均匀分配更糟的选择。'\n  analysis: 'Solver 不仅未发现 L0，反而因 budget 优化将 L0 降级，结果比 uniform 更差。 这说明 \"automatic discovery\"\n    claim 不成立——L0 protection 是 necessary prior knowledge。在 reframed narrative 中，这反而强化了\n    \"constraints as regularization\" 的论点：正确的 constraint 需要 model-specific knowledge，\n    而非纯数据驱动。\n\n    '\n- name: Llama-3.1-8B Full Pipeline Replication\n  plan_id: plan_002\n  description: '在 Llama-3.1-8B (GQA 4:1) 上复现完整 pipeline：profile → constrained MCKP\n    → eval。\n\n    '\n  expected_results:\n    llama_uniform4bit_ppl_wikitext: 8.95\n    llama_constrained_mckp_ppl_wikitext: 8.31\n    llama_ppl_improvement_pct: 7.2\n    llama_unconstrained_mckp_ppl: 9.83\n    llama_l0_delta_rank: not dominant (rank 12-18 among 32 layers)\n    llama_num_heads_determining_70pct_degradation: ~15% of heads (vs Qwen 3.6%)\n    llama_compounding_severity: mild\n    llama_optimal_max2bit: 24\n  result_rationale: 'Llama 的 GQA ratio 4:1（每层 8 KV heads，共 256 heads）使得 sensitivity\n    分布比 Qwen (GQA 7:1, 每层 4 KV heads, 共 112 heads) 更均匀。更多的 KV heads 意味着每个 head 承载更少的信息量，individual\n    head 的 failure 影响更小。 L0 不再是 dominant sensitivity source——sensitivity 分散在多个层的多个\n    heads 上。 Constrained MCKP 仍优于 uniform（7.2%），但远低于 Qwen 的 27%， 因为 head heterogeneity\n    本身更低。Unconstrained MCKP 的 PPL（9.83）虽差于 constrained 但并未 catastrophic failure（对比\n    Qwen 的 36.92）， 因为 compounding effect 在 GQA 4:1 下更温和——更多 heads 分担了 extreme quantization\n    的 joint distortion。这削弱了 \"compounding is universal and catastrophic\" 的论点。\n\n    '\n  tables:\n  - name: Llama-3.1-8B Allocation Results\n    columns:\n    - method\n    - ppl_wikitext\n    - compression\n    - improvement_vs_uniform\n    rows:\n    - - uniform_4bit\n      - 8.95\n      - 4×\n      - baseline\n    - - constrained_mckp\n      - 8.31\n      - 4×\n      - 7.2%\n    - - unconstrained_mckp\n      - 9.83\n      - 4×\n      - -9.8% (worse than uniform)\n  figures_description:\n  - 'Per-head delta heatmap (32 layers × 8 heads): 相比 Qwen 的 L0 spike pattern，Llama\n    呈现更均匀的分布，peak sensitivity 分散在 L0-L3 和 L28-L31。'\n  - 'Sensitivity CDF: Llama 需要 ~15% 的 heads 才覆盖 70% degradation，Qwen 仅需 3.6%。'\n  analysis: '7.2% 改进虽然 positive 但 marginal——reviewer 会质疑是否 justifies method complexity。Unconstrained\n    未 catastrophic failure 意味着 Llama 上 cardinality constraint 的 motivation 更弱。核心发现：GQA\n    ratio 越低， sensitivity 越分散，constrained MCKP 的边际收益越小。 这支持 \"sensitivity structure\n    is architecture-dependent\" 的 reframed narrative。\n\n    '\n- name: Mistral-7B-v0.3 Full Pipeline Replication\n  plan_id: plan_003\n  description: '在 Mistral-7B-v0.3 上复现完整 pipeline，建立跨架构有效性。\n\n    '\n  expected_results:\n    mistral_uniform4bit_ppl_wikitext: 8.42\n    mistral_constrained_mckp_ppl_wikitext: 7.93\n    mistral_ppl_improvement_pct: 5.8\n    mistral_unconstrained_mckp_ppl: 8.71\n    mistral_l0_delta_rank: rank 5-8 among 32 layers\n    mistral_sliding_window_complication: true\n    mistral_optimal_max2bit: 20\n  result_rationale: 'Mistral 同样是 GQA 4:1（与 Llama 相同），但 sliding window attention 改变了\n    KV cache 的 usage pattern——早期 token 的 KV 被 evict，使得 对 precision 的依赖模式不同。Sensitivity\n    分布更接近 Llama（分散型）， 但 sliding window 还引入了 position-dependent sensitivity 的额外复杂度，\n    我们的 position-agnostic profiler 无法捕获。改进幅度 5.8% 进一步确认 低 GQA ratio 下 method 边际收益有限。Unconstrained\n    MCKP PPL 8.71 仅比 uniform 差 3.4%——完全没有 catastrophic failure， 进一步削弱 compounding\n    的 universal catastrophic 叙事。\n\n    '\n  tables:\n  - name: Mistral-7B Results\n    columns:\n    - method\n    - ppl_wikitext\n    - compression\n    - improvement_vs_uniform\n    rows:\n    - - uniform_4bit\n      - 8.42\n      - 4×\n      - baseline\n    - - constrained_mckp\n      - 7.93\n      - 4×\n      - 5.8%\n    - - unconstrained_mckp\n      - 8.71\n      - 4×\n      - -3.4%\n  figures_description:\n  - 'Per-head delta heatmap: 类似 Llama 的分散模式，但 sliding window 导致后半层 sensitivity 整体偏高。'\n  analysis: 'Mistral 的 5.8% 改进是三个模型中最低的。Sliding window attention 使得 我们的 static profiling\n    假设部分失效。与 Llama 结果联合看， GQA 4:1 模型上 constrained MCKP 的 value proposition 弱于 GQA\n    7:1。 但这正是 reframed narrative 的核心 finding：GQA ratio 决定了 head sensitivity 的集中度，进而决定了\n    per-head allocation 的收益空间。\n\n    '\n- name: Compounding Effect Sweep (Qwen)\n  plan_id: plan_004\n  description: '在 Qwen2.5-7B 上 sweep max_2bit from 0 to 112，绘制 PPL vs max_2bit curve，\n    刻画 compounding threshold。\n\n    '\n  expected_results:\n    qwen_compounding_curve:\n      max2bit_0: 11.89\n      max2bit_4: 11.45\n      max2bit_8: 11.23\n      max2bit_16: 11.31\n      max2bit_24: 12.05\n      max2bit_48: 15.78\n      max2bit_75: 24.31\n      max2bit_112: 36.92\n    elbow_k_qwen: 8\n    curve_shape: hockey stick with clear elbow at k=8\n  result_rationale: 'Qwen 的 GQA 7:1 产生少量（112 个）但每个 information-dense 的 KV heads。 当少量\n    heads 被极端量化时，joint distortion 仍可控（k≤8 时 PPL 平稳）， 但超过阈值后 compounding 急剧恶化——因为 dense\n    heads 之间的 interaction 在 extreme quantization 下是超线性的。k=8 处有清晰 elbow。 这个 curve 在\n    Qwen 上非常漂亮，是 paper 的核心 figure 之一。\n\n    '\n  tables:\n  - name: Compounding Sweep (Qwen2.5-7B)\n    columns:\n    - max_2bit_k\n    - ppl_wikitext\n    - num_heads_at_2bit_actual\n    - delta_vs_k8\n    rows:\n    - - 0\n      - 11.89\n      - 0\n      - +5.9%\n    - - 4\n      - 11.45\n      - 4\n      - +2.0%\n    - - 8\n      - 11.23\n      - 8\n      - baseline\n    - - 16\n      - 11.31\n      - 16\n      - +0.7%\n    - - 24\n      - 12.05\n      - 24\n      - +7.3%\n    - - 48\n      - 15.78\n      - 44\n      - +40.5%\n    - - 75\n      - 24.31\n      - 68\n      - +116.6%\n    - - 112\n      - 36.92\n      - 95\n      - +228.8%\n  figures_description:\n  - 'PPL vs max_2bit curve (hockey stick): x 轴 max_2bit k, y 轴 WikiText-2 PPL. 清晰\n    elbow at k=8. Annotate optimal zone k∈[4,16].'\n  analysis: 'Qwen 上 compounding curve 有教科书般清晰的 elbow，但问题在于 这种 pattern 是否跨模型复现——在 worst\n    档下，Llama 和 Mistral 上该 curve 预计平坦或无 elbow（见 plan_002/003 的 unconstrained 结果）。 Reframed\n    narrative 将此作为 \"GQA-ratio-dependent compounding\" 的 case study 而非 universal phenomenon。\n\n    '\n- name: Budget Sweep (Qwen)\n  plan_id: plan_005\n  description: '在 Qwen2.5-7B 上测试 constrained MCKP 在 2×, 4×, 8× 压缩率下的表现， 与同 budget\n    的 uniform baseline 对比。\n\n    '\n  expected_results:\n    qwen_2x_uniform_ppl: 7.82\n    qwen_2x_constrained_ppl: 7.45\n    qwen_2x_improvement_pct: 4.7\n    qwen_4x_uniform_ppl: 15.45\n    qwen_4x_constrained_ppl: 11.23\n    qwen_4x_improvement_pct: 27.3\n    qwen_8x_uniform_ppl: 89.4\n    qwen_8x_constrained_ppl: 42.6\n    qwen_8x_improvement_pct: 52.3\n  result_rationale: '2× 压缩下 budget 充裕（平均 8-bit），大部分 heads 已在安全区间， per-head optimization\n    的空间有限（4.7%）。4× 是 sweet spot（27.3%）， 与已有 MVP 结果一致。8× 极端压缩下，constrained MCKP 改进幅度最大\n    （52.3%）但绝对 PPL 仍然很高（42.6），因为 budget 不足以保护 所有 critical heads——即使最优分配也无法避免严重质量损失。\n    这些数字都是 Qwen-specific 的，鉴于 Llama/Mistral 在 4× 时 仅有 5-7% 改进，它们在 2× 和 8× 下的改进预计更小。\n\n    '\n  tables:\n  - name: Budget Sweep (Qwen2.5-7B)\n    columns:\n    - compression\n    - uniform_ppl\n    - constrained_ppl\n    - improvement_pct\n    rows:\n    - - 2×\n      - 7.82\n      - 7.45\n      - 4.7%\n    - - 4×\n      - 15.45\n      - 11.23\n      - 27.3%\n    - - 8×\n      - 89.4\n      - 42.6\n      - 52.3%\n  figures_description:\n  - 'Bar chart: uniform vs constrained PPL at each compression ratio. 4× 是 narrative\n    sweet spot。'\n  - 'Line plot: improvement % vs compression ratio. 随压缩率增加收益增大，但绝对 PPL 也恶化。'\n  analysis: 'Budget sweep 在 Qwen 上 works well，但 reviewer 会要求看 Llama/Mistral 的 budget\n    sweep——在 worst 档下这些预计仅有 2-5% 改进空间，弱化 method 的 general value proposition。 Reframe:\n    强调 per-head allocation 在高压缩率下更 critical， 且 benefit 与 architecture 的 sensitivity\n    concentration 正相关。\n\n    '\n- name: High-Resolution Profiling (Qwen)\n  plan_id: plan_006\n  description: '用 64 seq × 2048 tokens（vs 当前 16×512）做高分辨率 profiling， 重跑 MCKP，测试是否发现\n    mid-layer heterogeneity 并改善分配。\n\n    '\n  expected_results:\n    hires_nonzero_head_pct: 31\n    lores_nonzero_head_pct: 16\n    hires_constrained_ppl: 11.09\n    lores_constrained_ppl: 11.23\n    hires_improvement_over_lores_pct: 1.2\n    hires_new_midlayer_discoveries: 3\n    hires_profiling_time_hours: 2.8\n  result_rationale: '高分辨率 profiling 将 nonzero-delta heads 从 16% 提升到 31%， 确实发现了几个 mid-layer\n    heads 有 measurable sensitivity。 但这些 newly-discovered heads 的 delta 仅占 total distortion\n    的 ~3%， 对 MCKP allocation 几乎无影响——solver 仍然做出几乎相同的分配决策。 PPL 仅从 11.23 降至 11.09（1.2%\n    改善），不足以 justify 4× 的 profiling compute overhead。根本原因：在 2-bit 分辨率下， 大部分 mid-layer\n    heads 确实 insensitive（这是真信号而非 measurement noise），profiler resolution 不是 bottleneck，\n    head sensitivity 的 long-tail distribution 本身是 fundamental。\n\n    '\n  tables:\n  - name: Profiling Resolution Comparison\n    columns:\n    - resolution\n    - nonzero_head_pct\n    - constrained_ppl\n    - profiling_hours\n    rows:\n    - - 16×512 (lores)\n      - 16%\n      - 11.23\n      - 0.7\n    - - 64×2048 (hires)\n      - 31%\n      - 11.09\n      - 2.8\n  figures_description:\n  - 'Delta heatmap comparison: lores vs hires. Hires 在 mid-layers 多出几个非零点，但量级很小。'\n  - 'Scatter plot: lores delta vs hires delta per head. 高相关 (r>0.95)，说明 lores 已足够。'\n  analysis: 'Hires profiling 是 negative result：profiler resolution 并非 fundamental\n    limitation，sensitivity 的 sparse 分布本身是 architecture 的 intrinsic property。这其实是 informative\n    negative—— 说明 16×512 已经是 cost-effective 的 profiling budget。 但无法 claim \"better\n    profiling → better allocation\"。\n\n    '\n- name: C4 Cross-Dataset Evaluation (Qwen)\n  plan_id: plan_007\n  description: '在 C4 上评估 Qwen2.5-7B 的 constrained MCKP 和 uniform 4-bit， 测试结果是否 WikiText-2\n    specific。\n\n    '\n  expected_results:\n    c4_uniform4bit_ppl: 18.73\n    c4_constrained_mckp_ppl: 16.92\n    c4_improvement_pct: 9.7\n    c4_rank_correlation_with_wikitext: 0.58\n    c4_allocation_agreement_pct: 72\n  result_rationale: 'C4 是更多样化的 web corpus，分布与 WikiText-2 有显著差异。 Per-head sensitivity\n    在 C4 上的排序与 WikiText-2 仅有中等相关 (rank corr 0.58)，因为不同 domain 的 text 激活不同 heads。 改进幅度从\n    27% 降至 9.7%——仍 positive 但显著缩水。 Allocation agreement 72% 意味着 ~28% 的 heads 在两个 dataset\n    上被分配了不同的 bit-width，暗示 optimal allocation 是 distribution-dependent 的。这弱化了 \"one-shot\n    profiling\" 的实用性叙事。\n\n    '\n  tables:\n  - name: C4 Evaluation (Qwen2.5-7B)\n    columns:\n    - dataset\n    - uniform_ppl\n    - constrained_ppl\n    - improvement_pct\n    rows:\n    - - WikiText-2\n      - 15.45\n      - 11.23\n      - 27.3%\n    - - C4\n      - 18.73\n      - 16.92\n      - 9.7%\n  - name: Cross-Dataset Allocation Agreement\n    columns:\n    - metric\n    - value\n    rows:\n    - - rank_correlation\n      - 0.58\n    - - allocation_agreement\n      - 72%\n    - - l0_protection_consistent\n      - 'yes'\n  figures_description:\n  - 'Scatter: per-head delta (WikiText-2) vs per-head delta (C4). 中等相关，visible outliers\n    in mid-layers.'\n  analysis: 'C4 上 9.7% 改进刚好低于 10% 的 \"显著\" 阈值（在 worst 定义中）。 Rank correlation 0.58 处于\n    worst 范围内 [0.45, 0.7]。 这意味着 profiling 的 calibration data 选择 matters—— reviewer\n    会问 \"which calibration set should a practitioner use?\" Reframe: 承认 allocation 是\n    partially distribution-dependent， 但 L0 protection 是 robust across datasets。\n\n    '\n- name: RateQuant Comparison (Reverse Waterfilling)\n  plan_id: plan_008\n  description: '实现 RateQuant 的 reverse waterfilling 在离散 action set 上的版本， 与 constrained\n    MCKP 对比。\n\n    '\n  expected_results:\n    llama_waterfilling_ppl: 8.52\n    llama_constrained_ppl: 8.31\n    llama_waterfilling_vs_mckp_gap: 2.5\n    qwen_waterfilling_ppl: 12.87\n    qwen_constrained_ppl: 11.23\n    qwen_waterfilling_vs_mckp_gap: 14.6\n  result_rationale: 'Reverse waterfilling 本质上是 continuous relaxation + rounding， 在\n    Llama 这种 sensitivity 分散的模型上，rounding error 较小 （因为 head 之间 delta 差异小，rounding 方向影响有限），\n    所以 waterfilling 与 MCKP 差距仅 2.5%。在 Qwen 上差距更大 （14.6%），因为 L0 的 extreme sensitivity\n    导致 rounding 在 critical head 上犯错——但这个差距比 constrained vs unconstrained 的差距（11.23\n    vs 36.92）小得多，reviewer 可能认为 waterfilling + L0 heuristic 就足够了，不需要完整 MCKP machinery。\n\n    '\n  tables:\n  - name: Waterfilling vs MCKP\n    columns:\n    - model\n    - waterfilling_ppl\n    - constrained_mckp_ppl\n    - gap_pct\n    rows:\n    - - Qwen2.5-7B\n      - 12.87\n      - 11.23\n      - 14.6%\n    - - Llama-3.1-8B\n      - 8.52\n      - 8.31\n      - 2.5%\n  figures_description:\n  - 'Bar chart: waterfilling vs MCKP across models. Qwen 差距明显，Llama 差距 marginal。'\n  analysis: '在 Llama 上 waterfilling 与 MCKP 几乎等效（2.5% gap）， 削弱了 \"discrete MCKP is fundamentally\n    necessary\" 的 claim。 Reviewer 会问：如果只在 GQA 7:1 模型上 MCKP 明显优于 waterfilling， 那这是 method\n    contribution 还是 Qwen-specific trick？ Reframe: 强调 MCKP framework 的 flexibility（能自然嵌入\n    cardinality constraint，waterfilling 不行）。\n\n    '\n- name: Oracle Comparison (Brute-Force Subset)\n  plan_id: plan_009\n  description: '在 Qwen 的 3-4 layer groups 上做 brute-force 穷举最优分配， 量化 MCKP 与 oracle\n    的差距。\n\n    '\n  expected_results:\n    oracle_subset_ppl: 10.41\n    mckp_subset_ppl: 10.78\n    mckp_to_oracle_gap_pct: 3.6\n    oracle_allocation_agrees_with_mckp_pct: 81\n  result_rationale: '在小规模子集上，brute-force oracle 能利用 joint evaluation 捕捉 compounding\n    interaction，找到 MCKP additive assumption 遗漏的 inter-head synergies。3.6% 的 gap 说明\n    MCKP 虽然 near-optimal 但并非 optimal——additive distortion model 即使加了 cardinality constraint\n    也有 residual error。 在 worst 档下，这个 gap 比预期大（理想情况应 <2%）， 暗示 compounding 的 non-additivity\n    比 cardinality constraint 能 capture 的更复杂（涉及 specific head combinations， 不仅仅是 count）。\n\n    '\n  tables:\n  - name: Oracle vs MCKP (Subset, Qwen2.5-7B)\n    columns:\n    - method\n    - subset_ppl\n    - gap_to_oracle\n    rows:\n    - - brute_force_oracle\n      - 10.41\n      - 0%\n    - - constrained_mckp\n      - 10.78\n      - 3.6%\n    - - unconstrained_mckp\n      - 14.93\n      - 43.4%\n  figures_description:\n  - 'Allocation diff heatmap: oracle vs MCKP on subset layers. ~19% heads 被不同分配。'\n  analysis: '3.6% gap 虽然不大但 non-trivial。在 reframed narrative 中， 这是 honest limitation：cardinality\n    constraint 是 first-order approximation，full interaction structure 需要更复杂的 constraint\n    设计或 iterative profiling。\n\n    '\n- name: Cross-Domain Calibration Robustness\n  plan_id: plan_010\n  description: '用 C4 calibrate、WikiText-2 evaluate（及反向），报告 per-head allocation 跨 calibration\n    source 的一致率。\n\n    '\n  expected_results:\n    calib_c4_eval_wiki_ppl: 12.14\n    calib_wiki_eval_wiki_ppl: 11.23\n    calib_c4_eval_c4_ppl: 16.92\n    calib_wiki_eval_c4_ppl: 17.85\n    cross_calib_allocation_agreement_pct: 68\n    l0_robust_across_calib: true\n  result_rationale: 'Calibration data 影响 per-head delta 估计。C4 calibration 在 WikiText-2\n    上评估时 PPL 12.14（vs 同 domain 的 11.23）， degradation 8.1%。反向（wiki calib → C4 eval）degradation\n    5.5%。 Allocation agreement 68% 低于理想（>85%），说明约 1/3 的 heads 的最优 bit-width 是 distribution-dependent。\n    L0 protection 跨 calibration 一致（因为 L0 在任何 distribution 上 都是 dominant），但 mid-layer\n    分配不稳定。\n\n    '\n  tables:\n  - name: Cross-Calibration Results (Qwen2.5-7B)\n    columns:\n    - calibration\n    - eval_dataset\n    - ppl\n    - vs_matched_calib\n    rows:\n    - - WikiText-2\n      - WikiText-2\n      - 11.23\n      - baseline\n    - - C4\n      - WikiText-2\n      - 12.14\n      - +8.1%\n    - - C4\n      - C4\n      - 16.92\n      - baseline\n    - - WikiText-2\n      - C4\n      - 17.85\n      - +5.5%\n  figures_description:\n  - 'Heatmap diff: C4-calibrated vs Wiki-calibrated allocation. 差异集中在 mid-layers。'\n  analysis: 'Cross-calibration degradation 是 real concern。Practitioner 需要 选择与 deployment\n    distribution 匹配的 calibration data。 在 reframed narrative 中，这是 practical limitation\n    的 honest characterization，也是 future work direction。\n\n    '\n- name: Head Sensitivity Visualization\n  plan_id: plan_011\n  description: '生成 paper-quality figures：per-head delta heatmap、compounding curve、\n    budget allocation comparison。\n\n    '\n  expected_results:\n    figures_generated: 4\n    key_visual_finding: cross-model heatmap comparison dramatically shows architecture-dependent\n      sensitivity\n  result_rationale: 'Visualization 本身不产生新数据，但在 worst 档下，cross-model heatmap 成为 paper\n    最重要的 figure——直观展示 Qwen (concentrated, L0-dominant) vs Llama/Mistral (dispersed,\n    no single dominant layer) 的对比。Compounding curve 只在 Qwen 上有 dramatic elbow， Llama/Mistral\n    的 curve 相对平坦。这些 visual 恰好 serve reframed narrative。\n\n    '\n  tables: []\n  figures_description:\n  - 'Figure 1: 三模型 per-head delta heatmap 横向对比 (3 panels). Qwen 的 L0 spike 非常醒目，Llama/Mistral\n    分散。'\n  - 'Figure 2: Compounding effect curves (3 lines on same plot). Qwen hockey stick,\n    Llama/Mistral 近似线性。'\n  - 'Figure 3: Budget allocation Sankey diagram — bits flow from budget to layers\n    to heads。'\n  - 'Figure 4: GQA ratio vs sensitivity concentration scatter (3 data points + trend).'\n  analysis: 'Visualization 在 worst 档下反而更有 impact，因为跨模型差异 本身就是 visually striking finding。\n\n    '\n- name: Downstream Task Evaluation (MMLU/LongBench)\n  plan_id: plan_012\n  description: '在 Qwen2.5-7B 4× 压缩下跑 MMLU 和 LongBench，测试 PPL 改进 是否 translate to downstream\n    performance。\n\n    '\n  expected_results:\n    qwen_fp16_mmlu: 68.2\n    qwen_uniform4bit_mmlu: 64.1\n    qwen_constrained_mmlu: 65.8\n    qwen_mmlu_recovery_pct: 41.5\n    qwen_fp16_longbench_avg: 45.3\n    qwen_uniform4bit_longbench_avg: 38.7\n    qwen_constrained_longbench_avg: 41.2\n    qwen_longbench_recovery_pct: 37.9\n  result_rationale: 'PPL 改进（27%）不会线性 translate 到 downstream tasks。 MMLU 是 knowledge-intensive\n    的 multiple-choice task， quantization 主要影响 calibration（logit precision）而非 knowledge\n    recall，所以 recovery 有限（41.5%）。 LongBench 涉及 long context，KV cache quantization\n    对 long-range attention 的影响更大，但 constrained MCKP 的 per-head allocation 在 long context\n    下的 optimality 可能不同于 short context（profiling 用 2048 tokens）， 导致 recovery 更低（37.9%）。整体\n    downstream improvement 存在但 modest，不足以成为独立 claim。\n\n    '\n  tables:\n  - name: Downstream Performance (Qwen2.5-7B, 4×)\n    columns:\n    - task\n    - fp16\n    - uniform_4bit\n    - constrained_mckp\n    - recovery_pct\n    rows:\n    - - MMLU\n      - 68.2\n      - 64.1\n      - 65.8\n      - 41.5%\n    - - LongBench_avg\n      - 45.3\n      - 38.7\n      - 41.2\n      - 37.9%\n  figures_description:\n  - 'Grouped bar chart: FP16 / uniform / constrained on MMLU and LongBench.'\n  analysis: 'Downstream results 是 positive but modest。在 worst 档下 不足以作为 strong selling\n    point。建议在 paper 中放为 supplementary experiment，主叙事仍以 PPL 为核心 metric， downstream\n    作为 sanity check。\n\n    '\n- name: 70B Profiling-Only (Qwen2.5-72B)\n  plan_id: plan_013\n  description: '在 Qwen2.5-72B 上只跑 distortion profiling（不做完整 eval）， 分析 sensitivity\n    patterns 是否随 model size 缩放。\n\n    '\n  expected_results:\n    qwen72b_l0_dominance: true\n    qwen72b_l0_delta_ratio_vs_avg: ~60× (vs 7B 的 100×)\n    qwen72b_nonzero_head_pct: 22\n    qwen72b_sensitivity_concentration: 5.1% heads cover 70% degradation\n    qwen72b_gqa_ratio: 7:1 (same as 7B)\n  result_rationale: '72B 与 7B 共享 GQA 7:1 架构，所以 L0 dominance 保持（支持 GQA-ratio-dependent\n    hypothesis）。但 72B 有 80 layers vs 7B 的 28， 更多层分摊了 sensitivity，L0 的 relative dominance\n    降低 （60× vs 100×）。Nonzero head pct 22% 略高于 7B 的 16%， 因为更深的 model 有更多层的 heads 对\n    quantization 有 non-trivial sensitivity。但 concentration 仍然高（5.1%）， 确认 GQA 7:1 架构的\n    sensitivity 集中特性。\n\n    '\n  tables:\n  - name: Scale Comparison (Qwen Family)\n    columns:\n    - model\n    - layers\n    - kv_heads\n    - l0_delta_ratio\n    - nonzero_pct\n    - top_heads_for_70pct\n    rows:\n    - - Qwen2.5-7B\n      - 28\n      - 112\n      - 100×\n      - 16%\n      - 3.6%\n    - - Qwen2.5-72B\n      - 80\n      - 320\n      - 60×\n      - 22%\n      - 5.1%\n  figures_description:\n  - 'Per-head delta heatmap: 72B (80×4). 与 7B 相同的 L0 spike pattern，但 relative magnitude\n    较小。'\n  analysis: 72B profiling 支持 GQA-ratio-dependent sensitivity hypothesis—— 同 GQA ratio\n    的不同 model sizes 有相似但不完全相同的 pattern。 在 worst 档下，这是 supporting evidence for reframed\n    narrative， 但不足以 claim \"method scales to 70B\" 因为我们没有做完整 eval。 作为 paper 的 supplementary\n    evidence 足够。\n",
      "numLines": 653,
      "startLine": 1,
      "totalLines": 653
    }
  },
  "sourceToolAssistantUUID": "8195b566-a605-49b3-9017-db57c67e1abb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T09:29:18.052Z_

<details><summary>↩ Tool result · `toolu_01RMs5kUhX97KaLDpcqAd4CE`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim:
4	  - 2
5	  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.
6	    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.
7	    Strengthens narrative: "solver automatically discovers sensitivity structure."
8	
9	    '
10	  priority: P0
11	  gpu_budget_hours: 1
12	  deps: []
13	  registry_id: exp_d_no_l0_exclusion
14	  model: Qwen2.5-7B
15	  eval: WikiText-2
16	- id: plan_002
17	  claim:
18	  - 1
19	  - 2
20	  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).
21	    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability
22	    across different GQA ratios and architectures. Fallback if HF token unavailable:
23	    Yi-1.5-9B (non-gated, similar scale).
24	
25	    '
26	  priority: P0
27	  gpu_budget_hours: 4
28	  deps: []
29	  registry_id: llama_full_pipeline
30	  model: Llama-3.1-8B
31	  fallback_model: Yi-1.5-9B
32	  eval: WikiText-2
33	- id: plan_003
34	  claim:
35	  - 1
36	  - 2
37	  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture
38	    family to establish cross-architecture validity.
39	
40	    '
41	  priority: P0
42	  gpu_budget_hours: 4
43	  deps: []
44	  registry_id: mistral_full_pipeline
45	  model: Mistral-7B-v0.3
46	  eval: WikiText-2
47	- id: plan_004
48	  claim:
49	  - 3
50	  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112
51	    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map
52	    the compounding threshold. Establishes the principled basis for cardinality constraint
53	    selection.
54	
55	    '
56	  priority: P0
57	  gpu_budget_hours: 3
58	  deps: []
59	  registry_id: compounding_sweep
60	  model: Qwen2.5-7B
61	  eval: WikiText-2
62	- id: plan_005
63	  claim:
64	  - 2
65	  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,
66	    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline
67	    at same budget.
68	
69	    '
70	  priority: P0
71	  gpu_budget_hours: 3
72	  deps: []
73	  registry_id: budget_sweep
74	  model: Qwen2.5-7B
75	  eval: WikiText-2
76	- id: plan_006
77	  claim:
78	  - 1
79	  - 2
80	  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).
81	    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers
82	    mid-layer heterogeneity and improves solver allocation beyond current results.
83	
84	    '
85	  priority: P0
86	  gpu_budget_hours: 3
87	  deps: []
88	  registry_id: exp_e_hires_profile
89	  model: Qwen2.5-7B
90	  eval: WikiText-2
91	- id: plan_007
92	  claim:
93	  - 1
94	  - 2
95	  - 3
96	  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.
97	    Cross-dataset evaluation to show results are not WikiText-2 specific.
98	
99	    '
100	  priority: P0
101	  gpu_budget_hours: 2
102	  deps: []
103	  registry_id: c4_rerun_d032
104	  model: Qwen2.5-7B
105	  eval: C4
106	- id: plan_008
107	  claim:
108	  - 2
109	  description: 'RateQuant comparison: implement RateQuant''s greedy algorithm (Algorithm
110	    1) on our discrete action set {2,4,8,16}-bit. RateQuant''s Prop. 6 optimality
111	    relies on consecutive-integer polymatroid structure which breaks on non-consecutive
112	    sets. Show greedy produces suboptimal allocation vs constrained MCKP. Critical
113	    for differentiation claim — must have experimental evidence.
114	
115	    '
116	  priority: P0
117	  gpu_budget_hours: 4
118	  deps: []
119	  registry_id: ratequant_greedy_comparison
120	  model: Qwen2.5-7B
121	  eval: WikiText-2
122	- id: plan_009
123	  claim:
124	  - 2
125	  description: 'Oracle comparison: brute-force optimal allocation on a subset (3-4
126	    layer groups) of Qwen2.5-7B. Quantify MCKP gap to oracle.
127	
128	    '
129	  priority: P1
130	  gpu_budget_hours: 6
131	  deps:
132	  - plan_006
133	  registry_id: oracle_comparison
134	  model: Qwen2.5-7B
135	- id: plan_010
136	  claim:
137	  - 2
138	  description: 'Cross-domain calibration robustness: calibrate on C4, evaluate on
139	    WikiText-2 (and vice versa). Report per-head allocation agreement rate across
140	    calibration sources.
141	
142	    '
143	  priority: P1
144	  gpu_budget_hours: 2
145	  deps:
146	  - plan_007
147	  registry_id: c4_rerun_d032
148	  model: Qwen2.5-7B
149	- id: plan_011
150	  claim:
151	  - 1
152	  description: 'Head sensitivity visualization: generate paper-quality figures showing
153	    per-head profiling delta heatmap across layers, compounding effect curve, and
154	    budget allocation comparison chart.
155	
156	    '
157	  priority: P1
158	  gpu_budget_hours: 1
159	  deps:
160	  - plan_004
161	  - plan_006
162	  registry_id: head_sensitivity_viz
163	- id: plan_014
164	  claim:
165	  - 2
166	  description: 'K/V separation: treat K and V heads as independent MCKP items with
167	    separate budget allocation. Compare joint K+V optimization vs current uniform
168	    K=V approach. RateQuant supports asymmetric K/V (e.g. K=2.85, V=2.15 avg bits)
169	    — we should show MCKP naturally handles this.
170	
171	    '
172	  priority: P1
173	  gpu_budget_hours: 3
174	  deps: []
175	  registry_id: kv_separation
176	  model: Qwen2.5-7B
177	  eval: WikiText-2
178	- id: plan_012
179	  claim:
180	  - 1
181	  - 2
182	  description: 'Downstream task evaluation: ARC-C / HellaSwag / PIQA / WinoGrande
183	    on Qwen2.5-7B at 4× compression. Must match RateQuant''s eval suite for direct
184	    comparison. Tests whether PPL improvements translate to downstream performance.
185	
186	    '
187	  priority: P1
188	  gpu_budget_hours: 8
189	  deps:
190	  - plan_005
191	  registry_id: downstream_eval_qwen
192	  model: Qwen2.5-7B
193	- id: plan_013
194	  claim:
195	  - 1
196	  description: '70B profiling-only: run distortion profiling on Qwen2.5-72B (no full
197	    eval). Analyze whether sensitivity patterns (Layer 0 dominance, compounding threshold)
198	    scale with model size.
199	
200	    '
201	  priority: P1
202	  gpu_budget_hours: 4
203	  deps: []
204	  registry_id: qwen72b_profiling
205	  model: Qwen2.5-72B
206	- id: plan_015
207	  claim:
208	  - 2
209	  description: 'L0-only heuristic baseline: assign 8-bit to all Layer 0 KV heads,
210	    uniform 4-bit to all other heads, at 4x compression on Qwen2.5-7B. This is the
211	    simplest possible non-uniform strategy exploiting L0 sensitivity. If L0-only matches
212	    or beats constrained MCKP, the full optimization machinery is unnecessary. Must
213	    also test on Llama and Mistral. Critical missing baseline flagged by Dream review.
214	
215	    '
216	  priority: P0
217	  gpu_budget_hours: 1
218	  deps: []
219	  registry_id: l0_only_heuristic
220	  model: Qwen2.5-7B
221	  eval: WikiText-2
222	- id: plan_016
223	  claim:
224	  - 2
225	  description: 'RateQuant greedy + cardinality constraint ablation: add max_2bit=k
226	    constraint to RateQuant greedy Algorithm 1 on {2,4,8,16}. Compare three conditions:
227	    (a) RateQuant greedy unconstrained (already have: PPL ~32.45), (b) RateQuant greedy
228	    + cardinality k=8, (c) constrained MCKP k=8 (already have: PPL ~11.23). If (b)
229	    matches (c), the contribution is the cardinality constraint, not the MCKP solver.
230	    If (c) beats (b), discrete MCKP optimization genuinely matters. Critical ablation
231	    flagged by all three Dream review tiers.
232	
233	    '
234	  priority: P0
235	  gpu_budget_hours: 2
236	  deps:
237	  - plan_008
238	  registry_id: greedy_cardinality_ablation
239	  model: Qwen2.5-7B
240	  eval: WikiText-2
241	- id: plan_017
242	  claim:
243	  - 1
244	  - 2
245	  description: 'Multi-seed error bars: run constrained MCKP and uniform 4-bit on Qwen2.5-7B
246	    at 4x compression with 3 different calibration sets (different random subsets
247	    of WikiText-2 training data). Report mean +/- std for PPL. Required for statistical
248	    credibility — Dream review flagged all-single-run as critical gap.
249	
250	    '
251	  priority: P1
252	  gpu_budget_hours: 3
253	  deps: []
254	  registry_id: multi_seed_error_bars
255	  model: Qwen2.5-7B
256	  eval: WikiText-2
257	- id: plan_018
258	  claim:
259	  - 2
260	  description: 'Runtime/latency benchmark: measure end-to-end inference latency and
261	    throughput with mixed-precision KV cache vs uniform 4-bit quantization on Qwen2.5-7B.
262	    Include profiling cost breakdown. Dream review flagged missing latency evaluation
263	    as significant gap for systems-oriented contribution.
264	
265	    '
266	  priority: P1
267	  gpu_budget_hours: 2
268	  deps: []
269	  registry_id: runtime_benchmark
270	  model: Qwen2.5-7B
271	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5df4fbe8-8f49-4bf9-9206-1a034003ba4e",
  "isSidechain": false,
  "promptId": "f114f0f3-7484-4f66-92b9-ae6b798ef7f0",
  "type": "user",
  "uuid": "87e8c9cc-a7b8-4fa6-bfde-11fcc424236f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/experiment_plan.yaml",
      "content": "experiments:\n- id: plan_001\n  claim:\n  - 2\n  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.\n    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.\n    Strengthens narrative: \"solver automatically discovers sensitivity structure.\"\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: exp_d_no_l0_exclusion\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_002\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).\n    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability\n    across different GQA ratios and architectures. Fallback if HF token unavailable:\n    Yi-1.5-9B (non-gated, similar scale).\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: llama_full_pipeline\n  model: Llama-3.1-8B\n  fallback_model: Yi-1.5-9B\n  eval: WikiText-2\n- id: plan_003\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture\n    family to establish cross-architecture validity.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mistral_full_pipeline\n  model: Mistral-7B-v0.3\n  eval: WikiText-2\n- id: plan_004\n  claim:\n  - 3\n  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112\n    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map\n    the compounding threshold. Establishes the principled basis for cardinality constraint\n    selection.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: compounding_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_005\n  claim:\n  - 2\n  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,\n    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline\n    at same budget.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: budget_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_006\n  claim:\n  - 1\n  - 2\n  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).\n    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers\n    mid-layer heterogeneity and improves solver allocation beyond current results.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_e_hires_profile\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.\n    Cross-dataset evaluation to show results are not WikiText-2 specific.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  eval: C4\n- id: plan_008\n  claim:\n  - 2\n  description: 'RateQuant comparison: implement RateQuant''s greedy algorithm (Algorithm\n    1) on our discrete action set {2,4,8,16}-bit. RateQuant''s Prop. 6 optimality\n    relies on consecutive-integer polymatroid structure which breaks on non-consecutive\n    sets. Show greedy produces suboptimal allocation vs constrained MCKP. Critical\n    for differentiation claim — must have experimental evidence.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: ratequant_greedy_comparison\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_009\n  claim:\n  - 2\n  description: 'Oracle comparison: brute-force optimal allocation on a subset (3-4\n    layer groups) of Qwen2.5-7B. Quantify MCKP gap to oracle.\n\n    '\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_006\n  registry_id: oracle_comparison\n  model: Qwen2.5-7B\n- id: plan_010\n  claim:\n  - 2\n  description: 'Cross-domain calibration robustness: calibrate on C4, evaluate on\n    WikiText-2 (and vice versa). Report per-head allocation agreement rate across\n    calibration sources.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_007\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n- id: plan_011\n  claim:\n  - 1\n  description: 'Head sensitivity visualization: generate paper-quality figures showing\n    per-head profiling delta heatmap across layers, compounding effect curve, and\n    budget allocation comparison chart.\n\n    '\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_004\n  - plan_006\n  registry_id: head_sensitivity_viz\n- id: plan_014\n  claim:\n  - 2\n  description: 'K/V separation: treat K and V heads as independent MCKP items with\n    separate budget allocation. Compare joint K+V optimization vs current uniform\n    K=V approach. RateQuant supports asymmetric K/V (e.g. K=2.85, V=2.15 avg bits)\n    — we should show MCKP naturally handles this.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: kv_separation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_012\n  claim:\n  - 1\n  - 2\n  description: 'Downstream task evaluation: ARC-C / HellaSwag / PIQA / WinoGrande\n    on Qwen2.5-7B at 4× compression. Must match RateQuant''s eval suite for direct\n    comparison. Tests whether PPL improvements translate to downstream performance.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  registry_id: downstream_eval_qwen\n  model: Qwen2.5-7B\n- id: plan_013\n  claim:\n  - 1\n  description: '70B profiling-only: run distortion profiling on Qwen2.5-72B (no full\n    eval). Analyze whether sensitivity patterns (Layer 0 dominance, compounding threshold)\n    scale with model size.\n\n    '\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: qwen72b_profiling\n  model: Qwen2.5-72B\n- id: plan_015\n  claim:\n  - 2\n  description: 'L0-only heuristic baseline: assign 8-bit to all Layer 0 KV heads,\n    uniform 4-bit to all other heads, at 4x compression on Qwen2.5-7B. This is the\n    simplest possible non-uniform strategy exploiting L0 sensitivity. If L0-only matches\n    or beats constrained MCKP, the full optimization machinery is unnecessary. Must\n    also test on Llama and Mistral. Critical missing baseline flagged by Dream review.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: l0_only_heuristic\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_016\n  claim:\n  - 2\n  description: 'RateQuant greedy + cardinality constraint ablation: add max_2bit=k\n    constraint to RateQuant greedy Algorithm 1 on {2,4,8,16}. Compare three conditions:\n    (a) RateQuant greedy unconstrained (already have: PPL ~32.45), (b) RateQuant greedy\n    + cardinality k=8, (c) constrained MCKP k=8 (already have: PPL ~11.23). If (b)\n    matches (c), the contribution is the cardinality constraint, not the MCKP solver.\n    If (c) beats (b), discrete MCKP optimization genuinely matters. Critical ablation\n    flagged by all three Dream review tiers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_008\n  registry_id: greedy_cardinality_ablation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_017\n  claim:\n  - 1\n  - 2\n  description: 'Multi-seed error bars: run constrained MCKP and uniform 4-bit on Qwen2.5-7B\n    at 4x compression with 3 different calibration sets (different random subsets\n    of WikiText-2 training data). Report mean +/- std for PPL. Required for statistical\n    credibility — Dream review flagged all-single-run as critical gap.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: multi_seed_error_bars\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_018\n  claim:\n  - 2\n  description: 'Runtime/latency benchmark: measure end-to-end inference latency and\n    throughput with mixed-precision KV cache vs uniform 4-bit quantization on Qwen2.5-7B.\n    Include profiling cost breakdown. Dream review flagged missing latency evaluation\n    as significant gap for systems-oriented contribution.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: runtime_benchmark\n  model: Qwen2.5-7B\n",
      "numLines": 271,
      "startLine": 1,
      "totalLines": 271
    }
  },
  "sourceToolAssistantUUID": "5df4fbe8-8f49-4bf9-9206-1a034003ba4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T09:29:18.045Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RMs5kUhX97KaLDpcqAd4CE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "542a7635-6403-4a44-991d-99bf7b26415c",
  "isSidechain": false,
  "requestId": "req_011Cb47rVAE783d2GRkTw85h",
  "type": "assistant",
  "uuid": "5df4fbe8-8f49-4bf9-9206-1a034003ba4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfSVXM5Q3dT1Gqs8NnfSYG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7348,
      "cache_read_input_tokens": 45757,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7348,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 45757,
          "cache_creation_input_tokens": 7348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7348
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 24 · 2026-05-15T09:29:18.139Z_

````json
{
  "parentUuid": "87e8c9cc-a7b8-4fa6-bfde-11fcc424236f",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**ratekv**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"ratekv\")` 或 `load_project_config(\"ratekv\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/ratekv/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "91513a94-7639-466a-8fd6-4f53ac8e80fe",
  "timestamp": "2026-05-15T09:29:18.139Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Qwen2.5-14B 不是 Spread 或 MCKP 无效，decision rule 出现 false positive/negative，核心 diagnostic 叙事不成立 核心假设：['Qwen2.5-14B concentration ≥0.50 但 MCKP 无改善（类似 Yi-1.5，d…",
  "leafUuid": "91513a94-7639-466a-8fd6-4f53ac8e80fe",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing when per-head KV cache quantization helps across architectures",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Assistant

_source line 27 · 2026-05-15T09:34:48.454Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me also check the existing worst-tier dream report to understand how it was structured, and see the remaining experiments (particularly the currently running ones and the w-series experiments that aren't in the original experiment_plan).

The existing worst-tier dream report only covers plan_001 through plan_013. I need to now generate a new, updated worst-tier prediction that covers ALL experiments in the experiment_plan (plan_001 through plan_018) plus the currently RUNNING experiments (gemma2_constrained_bos_fix, w1_qwen14b_hires_profiling).
 
Now I'm reviewing the worst-tier criteria from Phase 1: Qwen2.5-14B showing high concentration without MCKP improvement or low concentration with flat patterns, decision rule accuracy dropping to 4-5 out of 6 with high-confidence failures, the Gemma-2 BOS fix causing significant shifts in the unconstrained ratio, and W9 exhibiting non-monotonic or high-variance behavior in the compounding data.

Looking at the specific metric ranges that define this tier, I'm seeing tight bounds across the board—MCKP improvement barely moving between -3 and 3 percent, concentration hovering between 0.3 and 0.75, and the decision rule accuracy constrained to just 4 or 5 correct predictions. The narrative is shifting away from positioning this as a diagnostic or decision-rule problem and instead reframing it around cardinality constraints as a primary contribution.

Now I need to map out the experimental coverage—the original 18 plans plus the two currently running experiments, then account for the implied follow-ups around Qwen14B constrained MCKP, downstream tasks, and the compounding effects with w9. I need to include the running experiments since they're essential to the worst-tier scenario. For the Qwen14B case specifically, I'm modeling a false positive where the concentration metric (0.53) and t₁/t₅ ratio (0.63) both suggest a "Spread" pattern, but the actual MCKP improvement is negligible at +1.8%—just noise within the expected range. This happens because the 14B model's larger layer count dilutes L0's relative contribution, spreading sensitivity across early layers rather than concentrating it in a single layer.

The t₁/t₅ stays low because no individual head dominates the pattern, and MCKP fails to detect real improvement since the sensitivity differences are too small in absolute magnitude to break through the profiler noise at this scale. For Gemma-2, the BOS fix complicates things by reducing the unconstrained ratio from 1.47× down to 1.22×, which pushes the three-tier label barely above "mild" and forces a recalibration—the original degradation was partly inflated by how the BOS cold-start bug disproportionately affected 2-bit heads. This leaves me with a decision rule that achieves 5/6 accuracy with the Qwen14B false positive, which is acceptable but noticeably weaker than before.

Now I'm looking at the W9 compounding issue where the k64 randomk/topk ratio sits at 1.52 within the expected range, but the variance at k=32 and k=64 is so high that the trend becomes statistically indistinguishable from noise at intermediate k values. I need to write out the full YAML structure now, covering all 18 experiment plan entries with their names, plan IDs, descriptions, expected results, rationales, tables, figures, and analysis sections.

I'm realizing this is a substantial output, so I need to be systematic: I'll include all experiment plans from plan_001 through plan_018 (noting that plan_011 is visualization-focused and plan_014 handles K/V separation), plus the two currently running experiments for Gemma-2 with the BOS fix and W1 Qwen14B with higher profiling, along with the implied worst-tier follow-ups for Qwen14B. That brings me to roughly 20-22 total entries.

For the experiments already completed, I need to generate what the worst-tier data would look like. For some like plan_001, the worst tier doesn't significantly change the Qwen 7B results—instead, the worst tier is defined by the new experiments with Qwen14B and the Gemma-2 BOS fix. So I'll generate worst-tier predictions for plan_001 through plan_013 based on what the previous dream report already established.

But now the user is asking me to extend this to all experiments including plan_014 through plan_018 and the running experiments, with an updated worst-tier definition that incorporates the Qwen14B and Gemma-2 BOS fix scenarios. The existing worst report has 13 entries, so I need to add coverage for the remaining plans and the active experiments. Since the user asked for detailed data on every planned experiment in the experiment_plan, I should regenerate all 18 plus the running experiments using this updated worst-tier definition.

Let me start writing the complete output now. The decision rule breaks down at 5/6 cases—Qwen14B's false positive means I can't claim this is a reliable empirical diagnostic. Looking at how this affects each experiment: plan_001 still works on Qwen 7B but loses generalizability since the pattern doesn't scale to 14B within the same family. Plans 002 and 003 are already negative with no change in worst-tier. Plan_004 shows compounding works on 7B but becomes Qwen-specific in worst-tier, complicated further by variance issues in the W9 data. Plan_005 needs evaluation.

Plan_006 through plan_010 all show the same pattern—they work on Qwen 7B but the improvements are model-specific, with cross-dataset transfer weakening and agreement rates dropping in worst-tier conditions. Plan_012 demonstrates downstream improvement only on Qwen. Plan_013 is pending.

Looking at the remaining plans, K/V separation fails entirely, while the L0 heuristic converges toward MCKP in worst-tier scenarios, which actually strengthens the narrative that the constraint itself is the key contribution. Multi-seed experiments show higher variance undermines statistical significance in worst tier, and mixed-precision has runtime overhead compared to uniform quantization. The BOS fix and false positive diagnostic are notable data points that shift the numbers meaningfully.

I have enough to structure the YAML now, though I need to finalize the worst-tier analysis first. Looking at the experiment breakdown across models, most of the plan is actually Qwen 7B-focused with just a few experiments on other models like Llama and Mistral, plus some multi-model comparisons and ablations. For the worst-tier framing, the Qwen 7B results stay largely the same, but I'm reinterpreting them through the lens of limited generalization and the cardinality constraint being the only robust contribution. worst tier means degraded cross-dataset transfer for plan_007 and higher variance across seeds for plan_010. Now I'm writing out the YAML predictions.

Actually, I'm realizing the previous worst-tier predictions were genuinely counterfactual—they imagined different outcomes entirely, not just slightly worse numbers. For instance, plan_001 went from discovering L0 to failing completely, and plan_002 flipped from negative to positive results. These aren't minor variations but fundamentally different scenarios, which makes sense since worst tier represents a universe where things go wrong.

But the worst-tier definition itself has shifted since those initial predictions. It's no longer about Qwen 7B experiments failing—those actually succeeded in reality. Instead, the current worst tier focuses on what would break the framework: Qwen 14B producing false positives or flat results, the BOS fix changing Gemma-2's behavior, the decision rule degrading to 4-5 out of 6, and W9 becoming non-monotonic. So for the updated worst tier, Qwen 7B should still succeed as it did, but the new data points are what would invalidate the story.

I need to generate worst-tier predictions for plans 001 through 018 using this updated definition. Qwen 7B experiments should have results similar to actual (since in the updated worst tier, Qwen 7B IS the one model that works). The worst tier is about the overall story being weakened by new data, not about Qwen 7B experiments failing.

But for experiments involving other models (plan_002 Llama, plan_003 Mistral, plan_013 72B), the worst tier should have them fail to show benefit (which they actually did in reality).

So the updated worst-tier imagined experiments should:
1. For Qwen 7B experiments: results similar to actuals (success on this one model)
2. For other model experiments: results showing no benefit (similar to actuals or worse)
3. For NEW experiments (Qwen14B, Gemma-2 BOS): worst-case results as defined
4. For W9 compounding: non-monotonic or high-variance data

Now I'm setting up the YAML with specific scenarios. For Qwen14B, I want to create a false positive where the diagnostic predicts Spread based on concentration and spread metrics, but the actual improvement is negligible. I'll use concentration of 0.53 with a t₁/t₅ ratio of 0.63 to trigger the diagnostic, while keeping MCKP improvement at +1.8% to stay within the noise range. For Gemma-2 BOS, I'm simplifying the unconstrained ratio from 1.47× down to 1.

22× and showing the three-tier label collapsing to mild. For W9, I'm introducing non-monotonic behavior at intermediate k values with high variance masking any clear trend. Let me finalize these numbers and write out the complete YAML structure.

I'm reviewing the worst-tier metric ranges one more time to ensure consistency, then selecting specific values within those bounds that reinforce the narrative—like a modest 1.8% improvement for Qwen14B that reads as noise, a concentration score of 0.53 that crosses the diagnostic threshold, and a T1/T5 ratio of 0.63 that falls below the 0.70 cutoff.

Now I'm filling in the remaining metrics: decision rule accuracy at 5 out of 6 (with Qwen14B as the false positive), Gemma-2's constrained-versus-uniform showing a slight -0.8% deficit, the unconstrained ratio at 1.22 (well below the 1.47× baseline), and W9's topk ratio at 1.52 (weaker than the actual ~2.44). These numbers work together—Qwen14B looks like it should benefit from MCKP but doesn't, Gemma-2's moderate tier collapses once the BOS fix is applied, and W9's compounding effect gets dampened by variance, leaving the decision rule at 5 out of 6 correct.

For Qwen14B itself, I'm looking at the architecture: 48 layers with 8 KV heads totaling 384 heads and a 7:1 GQA ratio matching Qwen7B. The baseline perplexity sits around 7.2 (better than the 7B variant), uniform 4-bit quantization pushes it to ~9.5, and MCKP constrained brings it down to ~9.33 for a modest 1.8% gain, while unconstrained MCKP lands somewhere around 12.1 or higher—still not compelling enough to flip the classification.

Now I'm reconsidering why MCKP underperforms here despite the concentration metric suggesting moderate heterogeneity. The issue might be that with 384 heads, the absolute performance gap between uniform and baseline is relatively small (32% degradation from 7.2 to 9.5), and even though the heterogeneity pattern looks structurally similar to cases where MCKP works, it's not substantial enough in absolute terms to exploit. Plus, spreading the same information across more heads means each individual head carries less weight, so per-head optimization hits diminishing returns.

Let me verify the actual Qwen 14B architecture details to make sure I'm reasoning about the right configuration. fewer attention heads per KV head, which means less information density. Combined with the more distributed sensitivity from having more total KV heads, Qwen14B likely exhibits less heterogeneity than Qwen 7B. The concentration value of 0.53 falls in the moderate range, and with more heads in play, a slightly lower concentration makes sense to maintain comparable effects.

Let me verify the exact architecture details from the profiling data to confirm the KV head count.

So with 384 total KV heads and a 5:1 GQA ratio, the worst-tier scenario becomes quite plausible: the top 5% represents only 19 heads rather than 6, meaning each individual head contributes less to the overall computation. This makes it harder for MCKP to exploit meaningful differences between heads, resulting in a spread-like concentration pattern but with marginal actual improvement gains.

Let me verify the improvement metric calculation—MCKP constrained achieves 9.62 PPL versus uniform's 9.8, which translates to roughly 1.8% improvement, while the unconstrained version degrades to 11.2 PPL (1.56× the baseline).

Now thinking through Qwen 14B's characteristics: with double the KV heads per layer compared to the 7B variant, the sensitivity distribution would be more spread out, though the t₁/t₅ ratio of 0.63 suggests a relatively shallow gradient where heads aren't dramatically heterogeneous—this gives MCKP a modest opportunity to optimize.

But I need to clarify what t₁/t₅ actually measures. Looking back at the definitions, a lower ratio like Qwen's 0.57 indicates a "spread" pattern where sensitivity is distributed across multiple heads, while a higher ratio like Yi's 0.90 represents a "spike" pattern concentrated in a single outlier head. So t₁/t₅ is the ratio of the 1st-ranked head's delta to the 5th-ranked head's delta. A higher ratio means the top head dominates more (spike). A lower ratio means the top heads are more evenly distributed (spread).

Wait, that doesn't make sense. If t₁ is the top head and t₅ is the 5th head, then t₁/t₅ = delta_1 / delta_5. For spike (Yi), t₁/t₅ = 0.90... that means the top head is only 90% of the 5th head? That can't be right.

Let me reconsider what t₁/t₅ actually represents. Looking at the diagnostic pattern where low t₁/t₅ indicates Spread, I think this might be the proportion of the top-5 heads' combined delta that comes from just the top head. So for Yi with 0.90, the single top head accounts for 90% of the top-5 heads' total delta, while for Qwen with 0.57, it's only 57% — meaning the remaining heads share more of the contribution.

For Qwen14B's worst tier, the metrics show concentration at 0.53 and t₁/t₅ at 0.63, which triggers the Spread classification and predicts MCKP would be beneficial. But the actual improvement is only 1.8%, which is a false positive. The real issue is that even though the attention pattern looks spread-like, the absolute delta values are too small for MCKP to exploit effectively across 384 heads at budget 0.25.

Now I need to write out the YAML configuration and figure out what specific numbers to use for Qwen14B.

For the unconstrained behavior, if the model has Spread-like metrics, I'd expect worse performance without constraints—maybe 60-80 heads getting assigned to 2-bit with moderate compounding effects, putting the unconstrained ratio around 1.65×. But this creates a tension: Spread-like metrics should predict both catastrophic unconstrained behavior and MCKP benefits, yet here the MCKP benefit is minimal. The false positive suggests the Spread-like metrics don't actually translate to real gains in this case.

Reconsidering Qwen 14B more carefully: the concentration of 0.53 shows a Spread-like shape, but the absolute deltas are small, so the profiler signal is weak. Unconstrained, the solver probably assigns around 50 heads to 2-bit for a ratio near 1.8×—moderate, between Gemma-2 and Qwen 7B. With constrained allocation at k=8, MCKP finds a slightly better arrangement than uniform, but the improvement is just noise at 1.8%. This makes more sense: concentration captures the distribution shape but not the magnitude, so Qwen 14B has Spread-like structure with smaller absolute values, leading to moderate unconstrained degradation but minimal constrained benefit.

For Gemma-2 with the BOS fix, the unconstrained ratio drops from 1.47× down to 1.22×, a meaningful improvement. The constrained case gets slightly worse after the fix, moving from -0.3% to -0.8% relative to uniform.

Looking at the actual BOS-fixed data from the results, I'm seeing the baseline at 6.03, uniform at 6.17, and greedy/MCKP both at 8.85, which gives that 1.47× ratio. Wait—this means the BOS fix was already applied to the unconstrained results I was analyzing, so the ratio didn't actually improve as much as I thought.

Now the constrained MCKP with BOS fix is running, which will re-evaluate the constrained approach using the corrected evaluation method. The old constrained numbers showed PPL 9.05 versus uniform 9.03, but with BOS-fixed evaluation, the baselines shift to 6.03 and 6.17, so the constrained MCKP should land somewhere in that 6.17–6.25 range for the worst tier, representing about a 1.3% delta instead of the 0.3% the old eval showed. The constrained MCKP results with BOS fix show it performing worse than uniform quantization on Gemma-2, which contradicts the expected benefit of the constraint. The unconstrained ratio stays at 1.47× since those were already BOS-fixed in the earlier experiment, but the constrained case isn't delivering the improvement I'd hoped for. Or the worst-tier concern points to a deeper issue—maybe the BOS fix in the earlier unconstrained evaluation was incomplete, and the true ratio is actually 1.22× rather than 1.47×. That would mean Gemma-2 collapses from "moderate" into the "mild" category like the others, flattening the three-tier structure into just two tiers and fundamentally reshaping the narrative around constraint effectiveness.

Now I'm setting up the YAML with concrete metrics for Qwen14B, estimating the baseline perplexity around 7.15 and working through the degradation scenarios for uniform quantization and the constrained versus unconstrained MCKP variants.

I'm recalculating the improvement metric to ensure it's statistically meaningful—the current difference between uniform and constrained MCKP is about 2.6 standard deviations, which is actually significant, so I need to dial back the improvement slightly to keep it more realistic. I'm settling on a 0.5% improvement as the clearest case—it's noise-level performance gain that would represent a true false positive, where the diagnostic flags heterogeneity but the actual benefit doesn't justify the added complexity of MCKP.

Now I'm checking the decision rule across all six models: Qwen 7B correctly shows spread with meaningful benefit, Yi-1.5 and Llama both show spike patterns with no benefit as expected, and I'm verifying the remaining models follow this pattern.

Looking at the unconstrained ratios after the BOS fix, most models show mild degradation around 1.07-1.08×, but Qwen 7B jumps to 3.31× which is catastrophic, and Gemma-2 improved from 1.47× down to 1.22×. I'm noticing Gemma-2's significant improvement and wondering how that affects the overall picture.

Actually, this reveals something interesting—Qwen 14B sits at 1.57× which makes it the moderate-tier model now, yet it barely benefits from MCKP at only 0.5% improvement. This breaks the expected pattern where models with worse unconstrained performance should see bigger gains from the fix. The relationship between distribution shape and actual improvement isn't as clean as I thought, which makes this worst-tier scenario particularly valuable to examine.

For the W9 compounding analysis, I'm looking at how the k64 random-to-topk ratio behaves in the worst tier. The actual data shows 2.44, but constrained to the worst-tier range of [1.0, 2.0], it would drop to around 1.52—likely because the compounding curve becomes non-monotonic at large k values or variance gets too high to trust the ratio. Tracing through the k-values from k1 through k32, I can see the ratio gradually climbing from 1.0 up to 1.48 as k increases.

At k64, something interesting happens: the ratio actually dips back down to 1.52 despite both topk and randomk perplexities being extremely high. This suggests that at very large k, both allocation strategies degrade so severely that the gap between smart and random selection narrows—everything becomes bad enough that the relative advantage of topk allocation essentially vanishes.

Now I'm ready to compile the YAML with all the experimental plans I've been analyzing. I need to clarify the scope here—the user asked for worst-tier scenarios for each planned experiment, and while the experiment_plan.yaml contains 18 experiments, the currently running experiments are essential to include since they're part of the active evaluation pipeline. I should generate worst-tier interpretations for all 22 entries, updating the existing ones with the new definition and creating fresh ones for the running experiments and follow-ups. I need to reconsider the scope here—the user specifically asked for experiments within the experiment_plan, but the worst-tier definition references models and fixes that aren't in that plan. I'll include all 18 planned experiments plus the running ones and referenced experiments, making sure to label them clearly so it's obvious what belongs where.

Now I'm reconsidering plan_001 under the new worst-tier definition. Previously I thought it would fail because the solver wouldn't discover L0, but with Qwen 7B actually working in the updated framework, plan_001 should succeed instead. The key shift is that the worst-tier now demonstrates the framework's failure to generalize to new models, not Qwen 7B's failure. Let me draft the YAML entries with specific numbers for each experiment.

For plan_001, the solver discovers L0 on Qwen 7B with PPL of 11.23, matching the constrained result, though this success is specific to Qwen 7B and raises questions about broader generalizability. Plan_002 shows the same negative result as the actual run with minimal improvement across MCKP and uniform approaches. Plan_003 also mirrors the actual negative result with slight performance degradation.

Looking at plan_013, the 70B profiling shows L0 dominance persists in the worst tier but appears weaker than the 7B variant, likely due to the increased layer count affecting concentration patterns—again, this seems to be a Qwen-family characteristic rather than universal. Plan_014 confirms that separating K/V doesn't help, with joint attention outperforming the separated approach. For plan_015, the L0 heuristic performs remarkably close to MCKP on Qwen 7B with a median of 11.52, though results diverge on Llama and Mistral.

On other models, the L0 heuristic actually outperforms MCKP, which undermines the value of the MCKP machinery itself. Plan_016 shows that adding constraints makes the greedy approach equivalent to MCKP with constraints, which actually strengthens the narrative that the constraint itself is the real contribution. For plan_017, multi-seed variance increases substantially in the worst tier—MCKP's standard deviation rises to around 0.12 compared to 0.065 in the actual case, and allocation agreement drops to 0.82 from 0.90, meaning the improvement remains significant but with wider confidence intervals. Plan_018 indicates mixed-precision overhead is present but comparable to the actual results.

Mixed-precision is about 8% slower than uniform precision due to kernel dispatch overhead, which is a legitimate concern for systems-focused reviewers. Now I'm ready to write up the complete YAML with precise numbers and clear rationale for each plan. I should also update the narrative guidance to reflect the revised worst-tier definition. I'll include the Qwen14B profiling experiments and Gemma-2 BOS fix as separate critical entries, then organize everything systematically from plan_001 through plan_018, followed by the running experiments.

Writing YAML structure...

Entry 4 shows a U-shaped curve with an elbow around k=8 on Qwen 7B, but again this pattern doesn't generalize across models. Entry 5 confirms the budget sweep works on Qwen 7B but remains model-specific. Entry 6 finds that higher resolution profiling significantly improves head allocation—hires detects 100 nonzero 2-bit heads versus only 37 in lowres—though this advantage is also Qwen-dependent. Entry 7 demonstrates strong cross-dataset consistency with 96.4% allocation agreement, which is encouraging, but still tied to Qwen. Entry 8 is comparing RateQuant strategies where greedy unconstrained performs poorly at 32.45.

The constraint mechanism is what actually drives the improvement—greedy with constraint becomes equivalent to MCKP with constraint. Entry 9 shows MCKP achieves near-optimal performance with less than 0.02 PPL gap, optimizing 5 out of 8 layers, though again this is Qwen-specific. Entry 10 reconfirms the high cross-dataset agreement. Entry 11 shifts focus to generating visualizations that highlight cross-model diversity. Entry 12 reveals the critical limitation: Qwen 7B shows downstream gains of 1.25 to 4 percentage points, but the other four models actually degrade, and Qwen 14B shows no downstream improvement even in the best tier. Entry 13 attempted 70B profiling but ran into GPU constraints, leaving the scaling pattern unclear. Entry 14 tests K/V separation and finds joint quantization outperforms splitting them. Entry 15 shows that a simple L0 heuristic can recover 80-85% of the MCKP benefit.

The L0 heuristic actually matches or exceeds MCKP on Llama and Mistral, which undermines the value of the more complex MCKP machinery. Entry 16 confirms that adding constraints to greedy selection produces identical results to constrained MCKP, reinforcing that the constraint itself is the real contribution. Entry 17 reveals higher variance in the worst tier with MCKP standard deviation at 0.12—double the actual—though allocation agreement stays around 82%. Entry 18 shows mixed-precision quantization runs about 8% slower than uniform approaches, with profiling taking 65 minutes, making the cost-benefit questionable when only one model out of six actually benefits.

Now looking at Qwen 14B's profiling data with a concentration of 0.53 and head timing ratio of 0.63 across 384 heads and 48 layers with 5:1 grouped query attention. Entry 20 shows MCKP delivers only a 0.5% improvement while the unconstrained ratio jumps to 1.57×, suggesting the diagnostic flagged a false positive. Entry 21 is more revealing—fixing the BOS token in Gemma 2 exposes the true constrained versus uniform gap at -0.8%, with the unconstrained ratio dropping to 1.22×, which collapses the three-tier framework. Entry 22 examines the k64 random-to-topk ratio at 1.52, but the relationship becomes non-monotonic beyond k=32, with variance obscuring the underlying trend.

Actually, I realize the user specifically asked about planned experiments in the experiment_plan, and I already have the w9 data. Rather than treating w9 as a separate entry, I should weave it into the analysis of plan_004 and use it to guide the narrative. So I'll consolidate to 18 plan entries plus these 3 critical ones—w1_qwen14b_hires_profiling, qwen14b_constrained_mckp, and gemma2_constrained_bos_fix—for 21 total, which feels right. Since the user is asking me to regenerate the worst-tier predictions with the updated definition, I need to produce a fresh complete set rather than patch the existing report. My final approach: write all 21 entries in YAML covering the full experiment_plan plus the 3 running experiments.

For the numbers themselves, I'll use values close to actual results for Qwen 7B since it's the only model that performs in the worst tier, actual negative results for other models, and generated worst-tier predictions for the new experiments. The user emphasized that every prediction must include a result_rationale explaining why that result occurs at this tier level, so I need to make sure each entry has a clear, thorough explanation. Let me start writing the YAML with precise numbers and detailed rationales.

Now I'm working through the specific experimental results: the solver discovers L0 with a PPL of 11.23 matching the constrained baseline, MCKP versus uniform sampling showing minimal improvement around 0.2%, the monotonic k scenario producing a slight negative result, and the U-shaped pattern appearing only on Qwen while other models show different behaviors. For the scaling experiments, I'm seeing substantial gains with 2× yielding 4.5%, 4× reaching 27.3%, and 8× hitting 52% improvement, all specific to Qwen's characteristics. The high-resolution profiling shows a 1.8 PPL improvement over low-resolution at 10.91 versus 11.23, taking about 65 minutes. I'm still working through the C4 calibration experiment.

Continuing with the calibration results: C4 calibration achieves 96.4% agreement with WT2 evaluation at 11.29 PPL, while unconstrained approaches like greedy and MCKP fail catastrophically at 32.45 and 36.92 respectively. The oracle gap is remarkably tight at 0.018 PPL maximum and 0.005 average, indicating near-optimal performance. Cross-domain calibration between C4 and WT2 validates the approach with that 96.4% agreement rate. I've generated the figures and found Qwen recovers an average of 72.8% across tasks with gains ranging from 1.25 to 4.00 percentage points. One experiment was incomplete and killed. Separating key-value caches from joint attention shows a negative delta of 0.30 PPL, and I'm examining the L0-random baseline median.

Looking at the L0-random results across models: Qwen sits at 11.52, Llama at 10.04, and Mistral at 7.59, with MCKP showing improvements of 5.2%, 15.8%, and 5.7% respectively. Greedy with constraints matches MCKP with constraints exactly at delta 0.0000. The MCKP results show a mean of 10.99 with tight standard deviation of 0.065 and 90.2% agreement across runs. Mixed-precision inference is 7.6% slower than uniform precision at 21.8 versus 23.6 tokens per second. I'm wondering whether these actual results should be adjusted for the worst-tier scenario, but the Qwen 7B experiments are succeeding with results that align with the actual data.

The real issue is that the story doesn't generalize—Qwen 14B is a false positive, the Gemma-2 BOS fix breaks the three-tier structure, and the W9 compounding effect is model-specific. So for Qwen 7B, I should keep the numbers close to actual since the failure isn't in the experiments themselves but in how the framework generalizes across models. For generalizability tests like the multi-seed variance experiment, I might increase the standard deviation to 0.10 instead of 0.065 to reflect worse-case instability. The 70B experiment in the worst tier would be marked inconclusive since it was terminated. The simplest approach is to keep Qwen 7B results near actual while adjusting only the experiments that specifically test generalization. I need to clarify what the user is actually asking for. They want detailed data for each experiment under the worst-tier assumption—for completed experiments, I'll use the actual results and frame them within the worst-tier narrative, while for new experiments like Qwen 14B and Gemma-2 BOS, I'll generate predicted worst-tier outcomes. Each entry needs a rationale explaining how these results reflect worst-tier dynamics, particularly for Qwen 7B where the worst-tier interpretation doesn't drastically change the underlying data since that model is the one that actually works.

I'm going to structure this systematically: generate worst-tier predictions across all experiments, keep Qwen 7B numbers close to actual since it performs in the worst tier, show other models with minimal benefit, and provide clear rationales for each. I'll prioritize high detail for the core worst-tier experiments like the Qwen 14B profiling and constrained MCKP work, medium detail for the remaining planned experiments, and make sure each prediction is grounded in the worst-tier definition.

Now I'm organizing the full set of 21 entries and matching the existing dream report table format to write this out. I'm starting to write out the detailed entries for each plan, making sure to include concrete numbers and the reasoning behind each approach. Since this is going to be comprehensive, I'll work through them systematically to give the user the full picture they're asking for.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91513a94-7639-466a-8fd6-4f53ac8e80fe",
  "isSidechain": false,
  "requestId": "req_011Cb47roHtkbdZQ5tNhtsWW",
  "type": "assistant",
  "uuid": "99981ff5-377a-40a2-ba80-79553ff4f526",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3xq2DB2TaQwhi7PfiuuXV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20002,
      "cache_read_input_tokens": 73107,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 73107,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T09:40:34.484Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me also check the previous worst-tier dream report to see the remaining experiments (plan_014 through plan_018) and understand the format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99981ff5-377a-40a2-ba80-79553ff4f526",
  "isSidechain": false,
  "requestId": "req_011Cb47roHtkbdZQ5tNhtsWW",
  "type": "assistant",
  "uuid": "4f719e9c-fae3-4ab4-8963-b5e683df9fa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmeEpdhEpji9LcLjJfzg7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20002,
      "cache_read_input_tokens": 73107,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 73107,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T09:40:36.709Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WWeug8yAsenJpNWmrGH2zC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/imagined_experiments.yaml",
  "offset": 553
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f719e9c-fae3-4ab4-8963-b5e683df9fa1",
  "isSidechain": false,
  "requestId": "req_011Cb47roHtkbdZQ5tNhtsWW",
  "type": "assistant",
  "uuid": "5cf4e273-d07c-4688-b2bc-82b7654d6b4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmeEpdhEpji9LcLjJfzg7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20002,
      "cache_read_input_tokens": 73107,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 73107,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T09:40:36.987Z_

<details><summary>↩ Tool result · `toolu_01Cv56s5ocvjWsRR1k82JmDQ`</summary>

```text
1	# ratekv — Research Dashboard
2	
3	> 最后更新: 2026-05-15 08:27 UTC | 更新原因: GPU满载(Gemma-2 BOS + Qwen2.5-14B profiling) + Reviewer framing双重确认 + Paper Agent已启动
4	
5	## 核心方向
6	Per-KV-head 非均匀 bit-width 分配的 **concentration-dependent benefit**：cardinality constraint 是核心方法贡献，distribution shape（spread/spike/flat）决定 non-uniform 是否有效。详见 `paper_framing.md`。
7	
8	## 当前阶段: 审稿响应 — 补实验收尾 + 写作集成
9	
10	**投稿目标**: EMNLP 2026 Main (ARR May 25, 2026, 距今 10 天)
11	**审稿分数**: R1 2.5/5, R2 2/5 → Weak Reject (2.25/5)
12	**策略**: 补实验 ✅ 基本完成 → 写作集成 (Paper Agent 已启动) → W1 新模型 → 二审
13	
14	## 审稿 W-series 进度
15	
16	### CRITICAL — 实验全部完成，写作集成中
17	- [x] **W2**: 5/5 unconstrained baselines (gradient: 3.31× → 1.47× → 1.07-1.08×)
18	- [x] **W3**: 5/5 downstream eval (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp)
19	- [x] **W9**: compounding v2 (1.56-4.89× super-additivity)
20	- [ ] **W1**: Qwen2.5-14B profiling RUNNING (cuda:1, ~3h) + OPT-6.7B 待下载
21	- [ ] **W4**: Qwen outlier 分析 → Paper Agent 写作处理
22	
23	### WARNING — 4/7 resolved, 3 待 Paper Agent
24	- [x] W6 ✅ W7 ✅ W8 ✅ W11 ✅
25	- [ ] W5 (novelty), W9 (形式化), W10 (hires统一) → Paper Agent
26	
27	## Narrative (D053, Reviewer 双重确认)
28	- Claim 3: "empirical decision rule"（非 framework，N=1 Spread）
29	- 三档标签: catastrophic (3.31×) / moderate (1.47×) / mild (1.07-1.08×)
30	- arc_challenge 系统性信号: 主动讨论多步推理敏感
31	- Gemma-2 1.47×: 必须单独段讨论（2-bit 过度分配机制，加强 constraint 论证）
32	- Claim 2 三支柱: 防 catastrophe + 防 over-allocation + solver irrelevance
33	
34	## 5-Model Evidence (W2+W3 全完成)
35	
36	| Model | Conc. | Unconstrained | Constrained | Downstream | Shape |
37	|-------|-------|---------------|-------------|------------|-------|
38	| Qwen | 0.61 | 3.31× ☠️ | +27.3% | +2.6pp ✅ | Spread |
39	| Yi-1.5 | 0.71 | 1.08× | ≈0% | -0.77pp ✅ | Spike |
40	| Llama | 0.57 | 1.07× | +0.2% | -0.99pp ✅ | Spike |
41	| Mistral | 0.24 | 1.08× | -0.4% | -0.48pp ✅ | Flat |
42	| Gemma-2 | 0.23 | 1.47× | -0.3% | +0.14pp ✅ | Flat |
43	
44	## GPU 调度 (两卡满载)
45	westd-37397: 2× RTX PRO 6000 96GB
46	- cuda:0 → **Gemma-2 constrained BOS fix** (100% util, 29GB, ~15min剩余)
47	  完成后 → OPT-6.7B 下载 → OPT hires profiling
48	- cuda:1 → **Qwen2.5-14B W1 hires profiling** (100% util, 33GB, ~3h, 384 heads)
49	  baseline PPL=5.8432
50	
51	## 近期任务
52	- [ ] Gemma-2 constrained完成 → registry + 数据合并 + cuda:0→OPT 下载
53	- [ ] Qwen2.5-14B profiling完成 → concentration分析 → 如Spread则完整pipeline
54	- [ ] Paper Agent LaTeX集成 (W2 Table 2 + W3 Table 5 + W9 + narrative reframe)
55	- [ ] W3 Mistral+Gemma-2 注册 registry
56	- [ ] Reference audit
57	- [ ] 二审提交
58	
59	## Timeline (10天, Reviewer评估充裕)
60	- Day 0-1: W1 Qwen2.5-14B + OPT profiling + Gemma-2 constrained
61	- Day 1-3: Paper Agent 写作集成 + W1 结果补入
62	- Day 3-4: Reference audit + 最终审查
63	- Day 4-5: submit_paper_to_review (continue mode)
64	- Buffer: 5天
65	
66	## GPU 预算
67	本地: 2× RTX PRO 6000
68	剩余: Qwen2.5-14B full pipeline (~6-8h) + OPT profiling (~2h) + Gemma-2 constrained (~0.25h)
69	
70	## 关键决策日志
71	
72	| ID | 日期 | 摘要 | 关联实验 |
73	|----|------|------|----------|
74	| D053 | 2026-05-15 | 叙事转向：从"universal catastrophe"到"concentration-depen | w2_unconstrained_v2, w3_downstream_eval, w9_compounding_v2 |
75	| D052 | 2026-05-15 | 审稿响应：修正 W1 新模型选择为 Qwen2.5-14B + Phi-3-medium + Fal | w2_unconstrained_baselines, w9_compounding_scaling |
76	| D051 | 2026-05-14 | P0 patches: Qwen concentration 全文统一用 0.61（float32  | qwen_hires_float32_d048, exp_e_hires_profile |
77	| D050 | 2026-05-14 | Claim 3 诊断从单一 concentration 阈值升级为 concentration +  | yi15_hires_bf16_2bitonly, yi15_hires_constrained_mckp, qwen_hires_float32_d048 |
78	| D049 | 2026-05-14 | GQA ratio 不足以预测 KV heterogeneity，L0 dominance 是更可靠 | yi15_9b_full_pipeline, qwen25_7b_full_pipeline |
79	| D048 | 2026-05-14 | Qwen hires profiler bf16 bug 发现，concentration 可能被虚 | gemma2_9b_full_pipeline, yi15_9b_full_pipeline |
80	| D047 | 2026-05-14 | Yi-1.5 (GQA 8:1) FAIL 反证 GQA-ratio proxy；Claim 1 修 | yi15_9b_full_pipeline, gemma2_9b_full_pipeline |
81	| D046 | 2026-05-14 | bfloat16 精度 bug 全局修复(.float()) + Gemma-2/Yi-1.5 双  | gemma2_9b_full_pipeline, yi15_9b_full_pipeline |
82	| D045 | 2026-05-14 | Gemma-2 profiler bug confirmed (CRITICAL): 5/336 h | gemma2_9b_full_pipeline, yi15_9b_full_pipeline |
83	| D044 | 2026-05-14 | Gemma-2 BOS token bug identified and fixed — PPL 7 | gemma2_9b_full_pipeline, yi15_9b_full_pipeline |
84	
85	
86	
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8586a87b-563e-4bbb-96b3-de17466e43c0",
  "isSidechain": false,
  "promptId": "f114f0f3-7484-4f66-92b9-ae6b798ef7f0",
  "type": "user",
  "uuid": "93dde2da-fa61-4a37-a4b5-3065555166cc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/ROADMAP.md",
      "content": "# ratekv — Research Dashboard\n\n> 最后更新: 2026-05-15 08:27 UTC | 更新原因: GPU满载(Gemma-2 BOS + Qwen2.5-14B profiling) + Reviewer framing双重确认 + Paper Agent已启动\n\n## 核心方向\nPer-KV-head 非均匀 bit-width 分配的 **concentration-dependent benefit**：cardinality constraint 是核心方法贡献，distribution shape（spread/spike/flat）决定 non-uniform 是否有效。详见 `paper_framing.md`。\n\n## 当前阶段: 审稿响应 — 补实验收尾 + 写作集成\n\n**投稿目标**: EMNLP 2026 Main (ARR May 25, 2026, 距今 10 天)\n**审稿分数**: R1 2.5/5, R2 2/5 → Weak Reject (2.25/5)\n**策略**: 补实验 ✅ 基本完成 → 写作集成 (Paper Agent 已启动) → W1 新模型 → 二审\n\n## 审稿 W-series 进度\n\n### CRITICAL — 实验全部完成，写作集成中\n- [x] **W2**: 5/5 unconstrained baselines (gradient: 3.31× → 1.47× → 1.07-1.08×)\n- [x] **W3**: 5/5 downstream eval (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp)\n- [x] **W9**: compounding v2 (1.56-4.89× super-additivity)\n- [ ] **W1**: Qwen2.5-14B profiling RUNNING (cuda:1, ~3h) + OPT-6.7B 待下载\n- [ ] **W4**: Qwen outlier 分析 → Paper Agent 写作处理\n\n### WARNING — 4/7 resolved, 3 待 Paper Agent\n- [x] W6 ✅ W7 ✅ W8 ✅ W11 ✅\n- [ ] W5 (novelty), W9 (形式化), W10 (hires统一) → Paper Agent\n\n## Narrative (D053, Reviewer 双重确认)\n- Claim 3: \"empirical decision rule\"（非 framework，N=1 Spread）\n- 三档标签: catastrophic (3.31×) / moderate (1.47×) / mild (1.07-1.08×)\n- arc_challenge 系统性信号: 主动讨论多步推理敏感\n- Gemma-2 1.47×: 必须单独段讨论（2-bit 过度分配机制，加强 constraint 论证）\n- Claim 2 三支柱: 防 catastrophe + 防 over-allocation + solver irrelevance\n\n## 5-Model Evidence (W2+W3 全完成)\n\n| Model | Conc. | Unconstrained | Constrained | Downstream | Shape |\n|-------|-------|---------------|-------------|------------|-------|\n| Qwen | 0.61 | 3.31× ☠️ | +27.3% | +2.6pp ✅ | Spread |\n| Yi-1.5 | 0.71 | 1.08× | ≈0% | -0.77pp ✅ | Spike |\n| Llama | 0.57 | 1.07× | +0.2% | -0.99pp ✅ | Spike |\n| Mistral | 0.24 | 1.08× | -0.4% | -0.48pp ✅ | Flat |\n| Gemma-2 | 0.23 | 1.47× | -0.3% | +0.14pp ✅ | Flat |\n\n## GPU 调度 (两卡满载)\nwestd-37397: 2× RTX PRO 6000 96GB\n- cuda:0 → **Gemma-2 constrained BOS fix** (100% util, 29GB, ~15min剩余)\n  完成后 → OPT-6.7B 下载 → OPT hires profiling\n- cuda:1 → **Qwen2.5-14B W1 hires profiling** (100% util, 33GB, ~3h, 384 heads)\n  baseline PPL=5.8432\n\n## 近期任务\n- [ ] Gemma-2 constrained完成 → registry + 数据合并 + cuda:0→OPT 下载\n- [ ] Qwen2.5-14B profiling完成 → concentration分析 → 如Spread则完整pipeline\n- [ ] Paper Agent LaTeX集成 (W2 Table 2 + W3 Table 5 + W9 + narrative reframe)\n- [ ] W3 Mistral+Gemma-2 注册 registry\n- [ ] Reference audit\n- [ ] 二审提交\n\n## Timeline (10天, Reviewer评估充裕)\n- Day 0-1: W1 Qwen2.5-14B + OPT profiling + Gemma-2 constrained\n- Day 1-3: Paper Agent 写作集成 + W1 结果补入\n- Day 3-4: Reference audit + 最终审查\n- Day 4-5: submit_paper_to_review (continue mode)\n- Buffer: 5天\n\n## GPU 预算\n本地: 2× RTX PRO 6000\n剩余: Qwen2.5-14B full pipeline (~6-8h) + OPT profiling (~2h) + Gemma-2 constrained (~0.25h)\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D053 | 2026-05-15 | 叙事转向：从\"universal catastrophe\"到\"concentration-depen | w2_unconstrained_v2, w3_downstream_eval, w9_compounding_v2 |\n| D052 | 2026-05-15 | 审稿响应：修正 W1 新模型选择为 Qwen2.5-14B + Phi-3-medium + Fal | w2_unconstrained_baselines, w9_compounding_scaling |\n| D051 | 2026-05-14 | P0 patches: Qwen concentration 全文统一用 0.61（float32  | qwen_hires_float32_d048, exp_e_hires_profile |\n| D050 | 2026-05-14 | Claim 3 诊断从单一 concentration 阈值升级为 concentration +  | yi15_hires_bf16_2bitonly, yi15_hires_constrained_mckp, qwen_hires_float32_d048 |\n| D049 | 2026-05-14 | GQA ratio 不足以预测 KV heterogeneity，L0 dominance 是更可靠 | yi15_9b_full_pipeline, qwen25_7b_full_pipeline |\n| D048 | 2026-05-14 | Qwen hires profiler bf16 bug 发现，concentration 可能被虚 | gemma2_9b_full_pipeline, yi15_9b_full_pipeline |\n| D047 | 2026-05-14 | Yi-1.5 (GQA 8:1) FAIL 反证 GQA-ratio proxy；Claim 1 修 | yi15_9b_full_pipeline, gemma2_9b_full_pipeline |\n| D046 | 2026-05-14 | bfloat16 精度 bug 全局修复(.float()) + Gemma-2/Yi-1.5 双  | gemma2_9b_full_pipeline, yi15_9b_full_pipeline |\n| D045 | 2026-05-14 | Gemma-2 profiler bug confirmed (CRITICAL): 5/336 h | gemma2_9b_full_pipeline, yi15_9b_full_pipeline |\n| D044 | 2026-05-14 | Gemma-2 BOS token bug identified and fixed — PPL 7 | gemma2_9b_full_pipeline, yi15_9b_full_pipeline |\n\n\n\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  },
  "sourceToolAssistantUUID": "8586a87b-563e-4bbb-96b3-de17466e43c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T09:40:36.735Z_

<details><summary>↩ Tool result · `toolu_01WWeug8yAsenJpNWmrGH2zC`</summary>

```text
553	  analysis: 'Visualization 在 worst 档下反而更有 impact，因为跨模型差异 本身就是 visually striking finding。
554	
555	    '
556	- name: Downstream Task Evaluation (MMLU/LongBench)
557	  plan_id: plan_012
558	  description: '在 Qwen2.5-7B 4× 压缩下跑 MMLU 和 LongBench，测试 PPL 改进 是否 translate to downstream
559	    performance。
560	
561	    '
562	  expected_results:
563	    qwen_fp16_mmlu: 68.2
564	    qwen_uniform4bit_mmlu: 64.1
565	    qwen_constrained_mmlu: 65.8
566	    qwen_mmlu_recovery_pct: 41.5
567	    qwen_fp16_longbench_avg: 45.3
568	    qwen_uniform4bit_longbench_avg: 38.7
569	    qwen_constrained_longbench_avg: 41.2
570	    qwen_longbench_recovery_pct: 37.9
571	  result_rationale: 'PPL 改进（27%）不会线性 translate 到 downstream tasks。 MMLU 是 knowledge-intensive
572	    的 multiple-choice task， quantization 主要影响 calibration（logit precision）而非 knowledge
573	    recall，所以 recovery 有限（41.5%）。 LongBench 涉及 long context，KV cache quantization
574	    对 long-range attention 的影响更大，但 constrained MCKP 的 per-head allocation 在 long context
575	    下的 optimality 可能不同于 short context（profiling 用 2048 tokens）， 导致 recovery 更低（37.9%）。整体
576	    downstream improvement 存在但 modest，不足以成为独立 claim。
577	
578	    '
579	  tables:
580	  - name: Downstream Performance (Qwen2.5-7B, 4×)
581	    columns:
582	    - task
583	    - fp16
584	    - uniform_4bit
585	    - constrained_mckp
586	    - recovery_pct
587	    rows:
588	    - - MMLU
589	      - 68.2
590	      - 64.1
591	      - 65.8
592	      - 41.5%
593	    - - LongBench_avg
594	      - 45.3
595	      - 38.7
596	      - 41.2
597	      - 37.9%
598	  figures_description:
599	  - 'Grouped bar chart: FP16 / uniform / constrained on MMLU and LongBench.'
600	  analysis: 'Downstream results 是 positive but modest。在 worst 档下 不足以作为 strong selling
601	    point。建议在 paper 中放为 supplementary experiment，主叙事仍以 PPL 为核心 metric， downstream
602	    作为 sanity check。
603	
604	    '
605	- name: 70B Profiling-Only (Qwen2.5-72B)
606	  plan_id: plan_013
607	  description: '在 Qwen2.5-72B 上只跑 distortion profiling（不做完整 eval）， 分析 sensitivity
608	    patterns 是否随 model size 缩放。
609	
610	    '
611	  expected_results:
612	    qwen72b_l0_dominance: true
613	    qwen72b_l0_delta_ratio_vs_avg: ~60× (vs 7B 的 100×)
614	    qwen72b_nonzero_head_pct: 22
615	    qwen72b_sensitivity_concentration: 5.1% heads cover 70% degradation
616	    qwen72b_gqa_ratio: 7:1 (same as 7B)
617	  result_rationale: '72B 与 7B 共享 GQA 7:1 架构，所以 L0 dominance 保持（支持 GQA-ratio-dependent
618	    hypothesis）。但 72B 有 80 layers vs 7B 的 28， 更多层分摊了 sensitivity，L0 的 relative dominance
619	    降低 （60× vs 100×）。Nonzero head pct 22% 略高于 7B 的 16%， 因为更深的 model 有更多层的 heads 对
620	    quantization 有 non-trivial sensitivity。但 concentration 仍然高（5.1%）， 确认 GQA 7:1 架构的
621	    sensitivity 集中特性。
622	
623	    '
624	  tables:
625	  - name: Scale Comparison (Qwen Family)
626	    columns:
627	    - model
628	    - layers
629	    - kv_heads
630	    - l0_delta_ratio
631	    - nonzero_pct
632	    - top_heads_for_70pct
633	    rows:
634	    - - Qwen2.5-7B
635	      - 28
636	      - 112
637	      - 100×
638	      - 16%
639	      - 3.6%
640	    - - Qwen2.5-72B
641	      - 80
642	      - 320
643	      - 60×
644	      - 22%
645	      - 5.1%
646	  figures_description:
647	  - 'Per-head delta heatmap: 72B (80×4). 与 7B 相同的 L0 spike pattern，但 relative magnitude
648	    较小。'
649	  analysis: 72B profiling 支持 GQA-ratio-dependent sensitivity hypothesis—— 同 GQA ratio
650	    的不同 model sizes 有相似但不完全相同的 pattern。 在 worst 档下，这是 supporting evidence for reframed
651	    narrative， 但不足以 claim "method scales to 70B" 因为我们没有做完整 eval。 作为 paper 的 supplementary
652	    evidence 足够。
653	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cf4e273-d07c-4688-b2bc-82b7654d6b4b",
  "isSidechain": false,
  "promptId": "f114f0f3-7484-4f66-92b9-ae6b798ef7f0",
  "type": "user",
  "uuid": "c71de7d3-acac-4a80-8851-767ccf3e1824",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/imagined_experiments.yaml",
      "content": "  analysis: 'Visualization 在 worst 档下反而更有 impact，因为跨模型差异 本身就是 visually striking finding。\n\n    '\n- name: Downstream Task Evaluation (MMLU/LongBench)\n  plan_id: plan_012\n  description: '在 Qwen2.5-7B 4× 压缩下跑 MMLU 和 LongBench，测试 PPL 改进 是否 translate to downstream\n    performance。\n\n    '\n  expected_results:\n    qwen_fp16_mmlu: 68.2\n    qwen_uniform4bit_mmlu: 64.1\n    qwen_constrained_mmlu: 65.8\n    qwen_mmlu_recovery_pct: 41.5\n    qwen_fp16_longbench_avg: 45.3\n    qwen_uniform4bit_longbench_avg: 38.7\n    qwen_constrained_longbench_avg: 41.2\n    qwen_longbench_recovery_pct: 37.9\n  result_rationale: 'PPL 改进（27%）不会线性 translate 到 downstream tasks。 MMLU 是 knowledge-intensive\n    的 multiple-choice task， quantization 主要影响 calibration（logit precision）而非 knowledge\n    recall，所以 recovery 有限（41.5%）。 LongBench 涉及 long context，KV cache quantization\n    对 long-range attention 的影响更大，但 constrained MCKP 的 per-head allocation 在 long context\n    下的 optimality 可能不同于 short context（profiling 用 2048 tokens）， 导致 recovery 更低（37.9%）。整体\n    downstream improvement 存在但 modest，不足以成为独立 claim。\n\n    '\n  tables:\n  - name: Downstream Performance (Qwen2.5-7B, 4×)\n    columns:\n    - task\n    - fp16\n    - uniform_4bit\n    - constrained_mckp\n    - recovery_pct\n    rows:\n    - - MMLU\n      - 68.2\n      - 64.1\n      - 65.8\n      - 41.5%\n    - - LongBench_avg\n      - 45.3\n      - 38.7\n      - 41.2\n      - 37.9%\n  figures_description:\n  - 'Grouped bar chart: FP16 / uniform / constrained on MMLU and LongBench.'\n  analysis: 'Downstream results 是 positive but modest。在 worst 档下 不足以作为 strong selling\n    point。建议在 paper 中放为 supplementary experiment，主叙事仍以 PPL 为核心 metric， downstream\n    作为 sanity check。\n\n    '\n- name: 70B Profiling-Only (Qwen2.5-72B)\n  plan_id: plan_013\n  description: '在 Qwen2.5-72B 上只跑 distortion profiling（不做完整 eval）， 分析 sensitivity\n    patterns 是否随 model size 缩放。\n\n    '\n  expected_results:\n    qwen72b_l0_dominance: true\n    qwen72b_l0_delta_ratio_vs_avg: ~60× (vs 7B 的 100×)\n    qwen72b_nonzero_head_pct: 22\n    qwen72b_sensitivity_concentration: 5.1% heads cover 70% degradation\n    qwen72b_gqa_ratio: 7:1 (same as 7B)\n  result_rationale: '72B 与 7B 共享 GQA 7:1 架构，所以 L0 dominance 保持（支持 GQA-ratio-dependent\n    hypothesis）。但 72B 有 80 layers vs 7B 的 28， 更多层分摊了 sensitivity，L0 的 relative dominance\n    降低 （60× vs 100×）。Nonzero head pct 22% 略高于 7B 的 16%， 因为更深的 model 有更多层的 heads 对\n    quantization 有 non-trivial sensitivity。但 concentration 仍然高（5.1%）， 确认 GQA 7:1 架构的\n    sensitivity 集中特性。\n\n    '\n  tables:\n  - name: Scale Comparison (Qwen Family)\n    columns:\n    - model\n    - layers\n    - kv_heads\n    - l0_delta_ratio\n    - nonzero_pct\n    - top_heads_for_70pct\n    rows:\n    - - Qwen2.5-7B\n      - 28\n      - 112\n      - 100×\n      - 16%\n      - 3.6%\n    - - Qwen2.5-72B\n      - 80\n      - 320\n      - 60×\n      - 22%\n      - 5.1%\n  figures_description:\n  - 'Per-head delta heatmap: 72B (80×4). 与 7B 相同的 L0 spike pattern，但 relative magnitude\n    较小。'\n  analysis: 72B profiling 支持 GQA-ratio-dependent sensitivity hypothesis—— 同 GQA ratio\n    的不同 model sizes 有相似但不完全相同的 pattern。 在 worst 档下，这是 supporting evidence for reframed\n    narrative， 但不足以 claim \"method scales to 70B\" 因为我们没有做完整 eval。 作为 paper 的 supplementary\n    evidence 足够。\n",
      "numLines": 101,
      "startLine": 553,
      "totalLines": 653
    }
  },
  "sourceToolAssistantUUID": "5cf4e273-d07c-4688-b2bc-82b7654d6b4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T09:40:36.981Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cv56s5ocvjWsRR1k82JmDQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c71de7d3-acac-4a80-8851-767ccf3e1824",
  "isSidechain": false,
  "requestId": "req_011Cb47roHtkbdZQ5tNhtsWW",
  "type": "assistant",
  "uuid": "8586a87b-563e-4bbb-96b3-de17466e43c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmeEpdhEpji9LcLjJfzg7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20002,
      "cache_read_input_tokens": 73107,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 73107,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Qwen2.5-14B 不是 Spread 或 MCKP 无效，decision rule 出现 false positive/negative，核心 diagnostic 叙事不成立 核心假设：['Qwen2.5-14B concentration ≥0.50 但 MCKP 无改善（类似 Yi-1.5，d…",
  "leafUuid": "93dde2da-fa61-4a37-a4b5-3065555166cc",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing when per-head KV cache quantization helps across architectures",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Assistant

_source line 35 · 2026-05-15T09:41:46.878Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me also check what the existing worst-tier dream report covers. It covers plan_001 through plan_013 but NOT plan_014 through plan_018. And it doesn't cover the new running experiments (gemma2_constrained_bos_fix and w1_qwen14b_hires_profiling).

The user wants me to generate worst-tier predictions for ALL experiments in the experiment_plan. I need to update the previous dream report with:
1. Updated predictions for plan_001-013 (reflecting the new worst-tier definition which is different from the old one)


2. New predictions for plan_014-018
3. Predictions for the running experiments (gemma2_constrained_bos_fix, w1_qwen14b_hires_profiling, and implied follow-ups)

I'm noticing the previous worst-tier dream report is from 2026-05-14 and uses an older definition. The new worst-tier definition has evolved to include Qwen14B false positive/negative rates, Gemma-2 BOS fix impact, W9 compounding non-monotonic behavior, decision rule accuracy dropping to 4/6 or 5/6, and narrative reframing scenarios. I need to regenerate the entire report with these updated criteria.

Now I'm working through the worst-tier scenario carefully. For Qwen2.5-14B, I'm considering a concentration around 0.55 with t₁/t₅ ratio of 0.63, which would trigger the Spread diagnostic but show minimal MCKP improvement—essentially a false positive. Alternatively, concentration could drop to 0.35 for a Flat profile, creating inconsistency across the Qwen family. I'll proceed with the first scenario and generate the complete YAML covering all 18 experiments plus the running ones and W-series.

The Gemma-2 BOS fix weakens the three-tier narrative by collapsing the unconstrained ratio from 1.47× down to 1.22×, while W9's randomk/topk ratio at k=64 drops to around 1.5, breaking the monotonic pattern and muddying the compounding story. With the Qwen14B false positive, the decision rule accuracy drops from 5/5 to 5/6 correct predictions.

For plan_001, the L0 exclusion removal result remains positive since the solver still auto-discovers L0, but the significance gets diminished because the framework's explanatory power is weakened by the other failures.

Actually, I'm realizing the worst-tier scenario isn't about the original 18 experiments changing—those already ran successfully. It's about how the new experiments (Qwen14B, Gemma-2 BOS fix, W9 compounding) invalidate the broader narrative that was built from those completed experiments. So I should be imagining worst-case outcomes for the running and planned experiments specifically, not retroactively changing what's already been observed. I see how the running experiments connect directly to the worst-tier metrics—gemma2_constrained_bos_fix impacts the unconstrained ratio, while the Qwen profiling work affects concentration and decision accuracy. So I should build out a comprehensive YAML that includes all 18 planned experiments with worst-case interpretations of their results, plus these running experiments and their follow-ups as additional entries. For the completed experiments, I'll generate what the worst-tier version of those results would look like—shifting outcomes from success to mixed, reducing narrative significance, that kind of degradation. I'm realizing the user wants me to generate worst-tier predicted data for all experiments as a pre-registration exercise, treating this as a calibrated simulation regardless of which experiments are already done. For each experiment, I need to construct what the worst-tier outcome would look like — where the core diagnostic narrative breaks down and false positives/negatives emerge — then populate the full YAML with these predictions. I need to focus on generating the YAML output systematically now. For the Qwen7B experiments, the worst-tier results will have similar numerical values since the model's behavior doesn't change, but the interpretation shifts—what looked like robust findings becomes more fragile. For the cross-model experiments, I'll show weaker generalization patterns, and the new experiments with Qwen14B and Gemma2 will reveal diagnostic failures that undermine the main narrative. Now I'm looking at the specific metric ranges for the worst-tier experiments and picking values that demonstrate the most problematic failure mode: a false positive where the diagnostic criteria both trigger but the actual improvement is negligible. For Qwen14B, I'll use concentration at 0.55 and t₁/t₅ at 0.63 to hit both thresholds, paired with an MCKP improvement of just +1.2% to show the model behaves like noise despite the warning signs.

The Gemma-2 BOS fix and W9 compounding cases both undermine the tiered classification scheme—the constrained improvement drops to +0.8%, the unconstrained ratio falls from 1.47× to 1.22×, and the k64 ratio shows non-monotonic behavior that masks the underlying trend. This leaves me with 5 out of 6 decision rules correct, with Qwen14B as the sole miss.

Now I'm writing out the YAML configuration with all the model classifications and their rationales, making sure to include plan_012 under the worst tier since downstream benefits only materialize for Qwen7B.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93dde2da-fa61-4a37-a4b5-3065555166cc",
  "isSidechain": false,
  "requestId": "req_011Cb48irCQeFpBUqJvYzLJy",
  "type": "assistant",
  "uuid": "ea84c017-2a73-4fd6-a9bc-fb3bf17d484f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LKiRzMBxwVPFFD1yygGXP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4392,
      "cache_read_input_tokens": 73107,
      "output_tokens": 20102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20102,
          "cache_read_input_tokens": 73107,
          "cache_creation_input_tokens": 4392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4392
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-15T09:46:54.382Z_

Now I have the full context — the old dream report format, the experiment plan, current framing, and running experiments. Let me generate the updated worst-tier predictions aligned with the current framing (concentration-dependent narrative, three-tier labels, joint diagnostic, W-series experiments).

```yaml
tier: worst
narrative_guidance: >
  放弃 "diagnostic/decision rule" 作为核心 contribution，reframe 为三条新主线：
  (1) Cardinality constraint as universal safeguard — 不依赖 diagnostic，所有 5-6 个模型上 constraint 都 ≤ uniform 或防止 catastrophe，architecture-agnostic practical fix；
  (2) Systematic negative result — "we tested 5+ architectures and found non-uniform KV cache quantization is beneficial in only 1/5-6 cases"，saves practitioners time，framing 类似 "Challenging common assumptions about mixed-precision KV cache"；
  (3) Compounding effect characterization — 即使 diagnostic 不成立，discrete non-consecutive bit-width 上 solver 失败的机制分析（W9 data + Qwen catastrophe）仍是 novel contribution。
  三档标签改为纯描述性（按倍数分 tier，不绑定 distribution shape 解释）。
  论文标题从 "When Does X Help" 转向 "The Cardinality Constraint You Need for Hardware-Aligned KV Cache Quantization"。
  仍投 EMNLP Main Efficient Methods，卖点从 analysis 转向 practical method + surprising negative results。
imagined_experiments:
  # ============================================================
  # W1 关键新实验：Qwen2.5-14B (RUNNING, 决定 worst 是否成立)
  # ============================================================
  - name: "Qwen2.5-14B Hires Profiling"
    plan_id: "w1_qwen14b_hires_profiling"
    description: >
      Qwen2.5-14B hires bf16 2-bit-only profiling（48 layers × 8 KV heads = 384 heads）。
      测试 diagnostic 是否在 Qwen 模型族内泛化。
    expected_results:
      qwen14b_baseline_ppl: 5.84
      qwen14b_top5_concentration: 0.55
      qwen14b_t1_t5: 0.63
      qwen14b_l0_dominance_ratio: 8.2
      qwen14b_top1_head: "L0H2"
      qwen14b_top1_delta_2bit: 3.81
      qwen14b_l0_4heads_total_share: 0.41
      qwen14b_delta_2bit_cv: 5.12
      qwen14b_positive_delta_heads: 370
      qwen14b_total_heads: 384
      qwen14b_distribution_shape: "borderline_spread"
      diagnostic_prediction: "Spread (conc≥0.50 AND t₁/t₅≤0.70)"
      diagnostic_correct: false
    result_rationale: >
      Qwen2.5-14B 有 48 layers × 8 KV heads = 384 heads（vs 7B 的 28×4=112）。
      GQA 仍是 7:1，保留 L0 某些 heads 的较高 sensitivity（concentration=0.55，刚过 0.50 阈值）。
      但 14B 的 L0 cluster 比 7B 弱得多：7B 的 L0 4 heads 占 total delta 的 58.6%，
      而 14B 的 L0 heads 仅占 41%——48 层分摊了 sensitivity。t₁/t₅=0.63（<0.70），
      表面看满足 Spread 两个条件。但实际上 14B 的 "spread" 是 illusory：
      L0 heads 的 cross-bitwidth gradient 比 7B 弱（top1 delta=3.81 vs 7B 的 6.74），
      且 sensitivity 在 L0-L3 多层间分散而非集中在 L0 单层。
      这是一种 "diluted spread"——diagnostic 判定为 Spread 但 MCKP 无法有效利用。
    tables:
      - name: "Qwen Family Profiling Comparison"
        columns: [model, layers, kv_heads, concentration, t1_t5, l0_share, top1_delta, shape]
        rows:
          - [Qwen2.5-7B, 28, 112, 0.61, 0.57, "58.6%", 6.74, Spread]
          - [Qwen2.5-14B, 48, 384, 0.55, 0.63, "41.0%", 3.81, "Diluted Spread"]
    figures_description:
      - "Per-head delta heatmap (48×8): L0 有高 delta 但 magnitude 弱于 7B；L1-L3 也有 moderate delta heads，形成 multi-layer spread 而非 single-layer cluster"
    analysis: >
      Diagnostic 两个指标都刚过阈值（concentration 0.55 > 0.50, t₁/t₅ 0.63 < 0.70），
      但边际通过。14B 的关键问题：更多层分摊了 sensitivity，使得 L0 的 dominance 不足以
      让 MCKP 产生有意义的 allocation 差异。这暴露了 joint diagnostic 的 boundary fragility——
      阈值在 border 附近不 robust。

  - name: "Qwen2.5-14B Constrained MCKP"
    plan_id: "w1_qwen14b_constrained_mckp"
    description: >
      基于 14B hires profiling 跑 constrained MCKP（k=8），评估 PPL。
      如果 improvement ≈0%，则 diagnostic 出现 false positive。
    expected_results:
      qwen14b_baseline_ppl: 5.84
      qwen14b_uniform_4bit_ppl: 7.02
      qwen14b_mckp_constrained_k8_ppl: 6.94
      qwen14b_mckp_improvement_over_uniform_pct: 1.2
      qwen14b_mckp_unconstrained_ppl: 8.41
      qwen14b_unconstrained_ratio: 1.44
      qwen14b_bit_distribution: {2: 8, 4: 372, 8: 4}
      qwen14b_greedy_constrained_ppl: 6.94
      qwen14b_solver_equivalence_delta: 0.0000
      decision_rule_accuracy_6models: 5
      decision_rule_total_models: 6
      false_positive_model: "Qwen2.5-14B"
    result_rationale: >
      MCKP constrained PPL=6.94 vs uniform=7.02，improvement 仅 +1.2%（0.08 PPL gap）。
      对比 Qwen7B 的 +27.3%（4.53 PPL gap），14B 的 improvement 在噪声范围内。
      原因：14B 有 384 heads，每个 head 承载的 information 更少（head_dim 同为 128，但 48 层分摊），
      2-bit 降级的 per-head cost 更小。MCKP 将 L0 的 4 heads 分配到 8-bit，但这仅节省了
      total budget 的很小部分——384 heads 中 4 个 8-bit heads 的 budget 释放被稀释到其余 380 heads，
      每个 head 只多获得 ~0.01 bit，不足以改变 bit-width assignment。
      Unconstrained ratio=1.44×（类似 Gemma-2 的 1.47×），solver 将 ~80 heads 分配到 2-bit，
      产生 moderate 而非 catastrophic degradation。
      Decision rule accuracy 从 5/5 降至 5/6：14B 是 false positive（diagnostic 预测 benefit，实际无）。
    tables:
      - name: "Qwen2.5-14B Allocation Results"
        columns: [method, ppl, compression, vs_uniform]
        rows:
          - [baseline bf16, 5.84, "1×", "—"]
          - [uniform 4-bit, 7.02, "4×", baseline]
          - [constrained MCKP k=8, 6.94, "4×", "+1.2%"]
          - [unconstrained MCKP, 8.41, "4×", "-19.8%"]
          - [constrained greedy k=8, 6.94, "4×", "+1.2%"]
      - name: "Decision Rule Accuracy (6 Models)"
        columns: [model, concentration, t1_t5, diagnostic_prediction, actual_benefit, correct]
        rows:
          - [Qwen2.5-7B, 0.61, 0.57, Spread, "+27.3%", "✅"]
          - [Qwen2.5-14B, 0.55, 0.63, Spread, "+1.2%", "❌ FP"]
          - [Yi-1.5-9B, 0.71, 0.90, Spike, "≈0%", "✅"]
          - [Llama-3.1-8B, 0.57, 0.71, Spike, "+0.2%", "✅"]
          - [Mistral-7B, 0.24, 0.18, Flat, "-0.4%", "✅"]
          - [Gemma-2-9B, 0.23, 0.38, Flat, "-0.3%", "✅"]
    figures_description:
      - "Qwen14B vs 7B per-head delta heatmap 对比：14B 的 L0 spike 存在但更弱，sensitivity 分散到 L1-L3"
      - "Decision rule scatter (concentration × t₁/t₅)：14B 落在 Spread 象限但无 benefit，标注为 false positive"
    analysis: >
      Qwen14B 是 diagnostic 的致命反例：同一模型族（Qwen），同一 GQA ratio（7:1），
      concentration 和 t₁/t₅ 都满足 Spread 条件，但 MCKP 改进仅 1.2%。
      根本原因是 more layers dilute sensitivity，使得 per-head allocation 无法 exploit 
      sufficient heterogeneity。这说明 diagnostic 缺少第三个维度：total_kv_heads 或 layer_count。
      但增加维度后 N=6 的样本量完全不足以 fit 三维 boundary。
      Decision rule 降至 5/6 且 failure 发生在 high-confidence prediction（both metrics pass），
      这不是 borderline miss 而是 systematic failure — 严重削弱 diagnostic claim。

  # ============================================================
  # Gemma-2 BOS Fix (RUNNING, 影响三档标签)
  # ============================================================
  - name: "Gemma-2 Constrained MCKP with BOS Fix"
    plan_id: "gemma2_constrained_bos_fix"
    description: >
      用 sliding_window + BOS prepend 修正 eval，重测 Gemma-2 constrained MCKP 和 unconstrained baselines。
      BOS bug 可能导致之前的 1.47× unconstrained ratio 和 -0.3% constrained delta 不准确。
    expected_results:
      gemma2_bos_fix_baseline_ppl: 6.03
      gemma2_bos_fix_uniform_4bit_ppl: 6.17
      gemma2_bos_fix_constrained_mckp_ppl: 6.22
      gemma2_bos_fix_constrained_vs_uniform_pct: -0.8
      gemma2_bos_fix_unconstrained_greedy_ppl: 7.38
      gemma2_bos_fix_unconstrained_ratio: 1.22
      gemma2_bos_fix_n2bit_unconstrained: 106
      gemma2_bos_fix_constrained_bit_dist: {2: 8, 4: 324, 8: 4}
      gemma2_old_unconstrained_ratio: 1.47
      gemma2_ratio_shift: -0.25
    result_rationale: >
      BOS fix 降低了 baseline PPL（711.6→6.03 已确认），也降低了 quantized PPL。
      关键：BOS bug 对 unconstrained allocation 的影响是 non-uniform 的——
      106 个 2-bit heads 的 joint distortion 在有 BOS token 时部分被 BOS 的 attention mass 吸收
      （BOS 通常获得高 attention weight，为后续 token 提供 anchor），
      没有 BOS 时这些 heads 的 distortion 被放大。
      修正后 unconstrained ratio 从 1.47× 降至 1.22×，落入 mild 范围（1.07-1.22×），
      与 Yi/Llama/Mistral 的 1.07-1.08× 更接近。
      三档标签崩塌：原本 Gemma-2 是 "moderate" 独占，现在没有 moderate 了——
      只有 catastrophic（Qwen7B 3.31×）和 mild（其余 4 个模型 1.07-1.22×）。
      Constrained vs uniform 变为 -0.8%（从 -0.3%），方向不变但幅度增大。
    tables:
      - name: "Gemma-2 BOS Fix Impact"
        columns: [metric, before_bos_fix, after_bos_fix, delta]
        rows:
          - [baseline PPL, "711.6 (buggy) / 6.03 (corrected)", 6.03, "—"]
          - [uniform 4-bit PPL, 6.17, 6.17, "0.00"]
          - [unconstrained ratio, "1.47×", "1.22×", "-0.25×"]
          - [constrained vs uniform, "-0.3%", "-0.8%", "-0.5pp"]
          - [2-bit heads (unconstrained), 106, 106, "0"]
      - name: "Revised Three-Tier Labels (COLLAPSED)"
        columns: [tier, ratio_range, models, count]
        rows:
          - [Catastrophic, "≥2.0×", "Qwen2.5-7B (3.31×)", 1]
          - ["Moderate (EMPTY)", "1.25-2.0×", "—", 0]
          - [Mild, "1.0-1.25×", "Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.22×", 4]
    figures_description:
      - "Bar chart: unconstrained ratio across 5 models, before/after BOS fix. Gemma-2 从 moderate 滑入 mild"
    analysis: >
      三档标签失去 moderate 层：Catastrophic (1 model) + Mild (4 models)，
      变成 binary 而非 gradient。原本 "concentration-dependent gradient" 叙事中
      Gemma-2 是关键中间证据（flat-high-2bit mechanism），现在该机制的 magnitude 
      被 BOS bug 虚增。修正后 1.22× 的 over-allocation 仍比 Yi/Llama/Mistral 高，
      但 gap 缩小到 0.14-0.15×，可能在 noise 范围内。
      论文需要重新校准：要么放弃三档（改用连续变量 regression），
      要么承认 moderate tier 的 evidence 不 robust。

  # ============================================================
  # 原 experiment_plan 18 个实验
  # ============================================================
  - name: "L0 Auto-Discovery (No L0 Exclusion)"
    plan_id: "plan_001"
    description: >
      去掉 L0 exclusion 硬约束，仅保留 max_2bit=8，观察 solver 是否仍将 L0 heads 分配到 8-bit。
    expected_results:
      qwen7b_no_l0excl_ppl: 11.23
      qwen7b_l0_heads_assigned_8bit: 4
      qwen7b_solver_auto_discovers_l0: true
      qwen14b_no_l0excl_ppl: 6.97
      qwen14b_l0_heads_assigned_8bit: 2
      qwen14b_solver_partial_discovery: true
    result_rationale: >
      Qwen7B：solver 从 profiling data 自动将 L0 全部 4 heads 分配到 8-bit（delta 极高，cost-benefit ratio 最优），PPL=11.23 不变。这在 7B 上 works 因为 L0 dominance ratio=26×。
      Qwen14B：solver 仅将 L0 的 2/8 heads 分配到 8-bit（L0 dominance ratio 仅 8.2×，不够突出），
      其余 2 个 8-bit 名额给了 L2-L3 的 moderate-delta heads。PPL=6.97（vs constrained 6.94），
      差异很小但说明 14B 的 L0 不再是 unambiguous dominant——auto-discovery 部分失败。
    tables:
      - name: "L0 Auto-Discovery Across Qwen Family"
        columns: [model, l0_dominance, l0_8bit_heads, total_8bit_budget, ppl, auto_discovery]
        rows:
          - [Qwen2.5-7B, "26×", "4/4", 4, 11.23, "Full ✅"]
          - [Qwen2.5-14B, "8.2×", "2/8", 4, 6.97, "Partial ⚠️"]
    figures_description:
      - "Bit allocation comparison: 7B vs 14B 的 L0 heads 分配差异"
    analysis: >
      Auto-discovery 在 7B 上完美，在 14B 上部分失败。
      Reframed narrative 中这不是 critical：constraint 的价值不依赖 auto-discovery，
      constraint 的 contribution 是 preventing compounding 而非 discovering structure。

  - name: "Llama-3.1-8B Full Pipeline"
    plan_id: "plan_002"
    description: >
      Llama-3.1-8B (GQA 4:1) 全 pipeline：profile → constrained MCKP → eval。
    expected_results:
      llama_baseline_ppl: 8.09
      llama_uniform_4bit_ppl: 8.47
      llama_mckp_constrained_ppl: 8.45
      llama_improvement_pct: 0.2
      llama_unconstrained_ratio: 1.07
      llama_concentration: 0.57
      llama_t1_t5: 0.71
      llama_shape: "Spike (borderline)"
      llama_natural_k: 2
    result_rationale: >
      Llama 的 concentration=0.57 接近 0.50 阈值但 t₁/t₅=0.71 刚好超过 0.70，
      被分类为 Spike。实际上 MCKP 仅选择 2 个 heads 做 2-bit（natural k=2），
      constraint 从不 bind。+0.2% improvement 在 noise 范围内。
      在 worst tier 下，Llama 的 borderline t₁/t₅=0.71 使得 diagnostic boundary 
      的 robustness 受质疑——0.70 是 arbitrary cutoff。
    tables:
      - name: "Llama-3.1-8B Results"
        columns: [method, ppl, compression, vs_uniform]
        rows:
          - [baseline bf16, 8.09, "1×", "—"]
          - [uniform 4-bit, 8.47, "4×", baseline]
          - [constrained MCKP k=8, 8.45, "4×", "+0.2%"]
          - [unconstrained, 8.63, "4×", "-1.9%"]
    figures_description:
      - "Per-head delta heatmap (32×8): L2H5 single outlier (15.26), t₁/t₅=0.85 spike pattern"
    analysis: >
      Negative result 在 worst tier 下保持。但 t₁/t₅=0.71 的 borderline 值 
      使 diagnostic 对 Llama 的分类依赖 ±0.01 的阈值精度——如果阈值设为 0.75，
      Llama 会被误分为 Spread，增加 false positive 风险。

  - name: "Mistral-7B-v0.3 Full Pipeline"
    plan_id: "plan_003"
    description: >
      Mistral-7B-v0.3 全 pipeline，Flat distribution 代表。
    expected_results:
      mistral_baseline_ppl: 7.04
      mistral_uniform_4bit_ppl: 7.13
      mistral_mckp_constrained_ppl: 7.16
      mistral_improvement_pct: -0.4
      mistral_unconstrained_ratio: 1.08
      mistral_concentration: 0.24
      mistral_t1_t5: 0.18
      mistral_shape: "Flat"
      mistral_k_monotonic: true
    result_rationale: >
      Mistral concentration=0.24（远低于 0.50），profiler 信号几乎为零。
      Constrained MCKP 比 uniform 差 0.4%——solver 分配的 2-bit heads 
      实际上比 uniform 的 all-4bit 更差。k ablation 单调递增证明 
      每多一个 2-bit head 都 hurts。在 worst tier 下这是 clean negative，
      直接支持 "uniform suffices on flat models" 的叙事。
    tables:
      - name: "Mistral-7B Results"
        columns: [method, ppl, compression, vs_uniform]
        rows:
          - [baseline bf16, 7.04, "1×", "—"]
          - [uniform 4-bit, 7.13, "4×", baseline]
          - [constrained MCKP k=4, 7.16, "4×", "-0.4%"]
          - [unconstrained, 7.57, "4×", "-6.2%"]
    figures_description:
      - "k-PPL curve: 单调递增，无 elbow，与 Qwen 的 U-shape 形成对比"
    analysis: >
      Mistral 是最 clean 的 negative case——profiler signal ≈0，
      任何 non-uniform allocation 都 ≤ uniform。在 reframed narrative 中
      是 "systematic negative result" 的核心证据之一。

  - name: "Compounding Effect Sweep (Qwen7B)"
    plan_id: "plan_004"
    description: >
      Qwen2.5-7B 上 sweep max_2bit 从 0 到 112，绘制 PPL vs k curve。
    expected_results:
      qwen_k0_ppl: 15.45
      qwen_k4_ppl: 11.93
      qwen_k8_ppl: 11.23
      qwen_k10_ppl: 11.18
      qwen_k12_ppl: 11.21
      qwen_k16_ppl: 11.52
      qwen_k24_ppl: 13.07
      qwen_k48_ppl: 19.84
      qwen_k75_ppl: 28.36
      qwen_k112_ppl: 36.92
      elbow_k: 8
      curve_shape: "U-shape with clear minimum at k≈8-10"
    result_rationale: >
      Qwen7B 的 compounding curve 有清晰 U-shape：k 太小（budget 浪费在不需要的 higher-bit heads），
      k 太大（compounding 恶化）。Optimal k=8-10 对应 L0 cluster 的 head 数量。
      这是 Qwen7B 的固有特性，worst tier 不改变此结果。
      但 worst tier 的问题是：此 curve 是否跨模型可复现？
      Llama/Mistral 的 k-PPL curve 平坦或单调，没有 U-shape——
      compounding 的 "dramatic elbow" 是 Spread-specific，不 universal。
    tables:
      - name: "Compounding Sweep (Qwen2.5-7B, budget=0.25)"
        columns: [max_2bit_k, ppl, delta_vs_k8]
        rows:
          - [0, 15.45, "+37.6%"]
          - [4, 11.93, "+6.2%"]
          - [8, 11.23, "baseline (optimal)"]
          - [12, 11.21, "-0.2%"]
          - [16, 11.52, "+2.6%"]
          - [24, 13.07, "+16.4%"]
          - [48, 19.84, "+76.7%"]
          - [112, 36.92, "+228.8%"]
    figures_description:
      - "U-shape PPL vs k curve. Annotate optimal zone k∈[8,12]"
      - "Cross-model overlay: Qwen U-shape vs Llama flat vs Mistral monotonic"
    analysis: >
      Compounding curve 是 paper 的 core figure 之一，在 Qwen 上有力。
      但在 worst tier 下，其意义从 "universal phenomenon" 缩小为
      "Spread-model-specific phenomenon"。Reframe: 
      compounding 的 magnitude 和 shape 是 architecture-dependent，
      但 constraint 在所有模型上都是 safe（≤ uniform）。

  - name: "Budget Sweep (Qwen7B, 2×/4×/8×)"
    plan_id: "plan_005"
    description: >
      Qwen2.5-7B 在三种压缩率下 constrained MCKP vs uniform。
    expected_results:
      qwen_2x_uniform_ppl: 10.07
      qwen_2x_mckp_ppl: 9.89
      qwen_2x_improvement_pct: 1.8
      qwen_4x_uniform_ppl: 15.45
      qwen_4x_mckp_ppl: 11.23
      qwen_4x_improvement_pct: 27.3
      qwen_8x_uniform_ppl: 2644.0
      qwen_8x_mckp_ppl: 42.6
      qwen_8x_improvement_pct: 98.4
    result_rationale: >
      2× 压缩：budget 充裕（avg 8-bit），大部分 heads 在安全区，仅 1.8% 改进。
      4× 是 sweet spot（27.3%），与已有结果一致。
      8× 极端压缩下 uniform = all 2-bit（PPL 2644），constrained MCKP 保护 critical heads
      大幅降低 PPL（42.6），但绝对质量仍很差。
      Worst tier 不改变 Qwen7B 数字，但 cross-model budget sweep
      （如果做的话）会显示 Llama/Mistral 在 2× 和 4× 都无 improvement。
    tables:
      - name: "Budget Sweep (Qwen2.5-7B)"
        columns: [compression, uniform_ppl, mckp_ppl, improvement]
        rows:
          - ["2× (0.50)", 10.07, 9.89, "+1.8%"]
          - ["4× (0.25)", 15.45, 11.23, "+27.3%"]
          - ["8× (0.125)", 2644.0, 42.6, "+98.4%"]
    figures_description:
      - "Compression ratio vs improvement curve: 收益随压缩率增大，但只在 Qwen 上"
    analysis: >
      Budget sweep 在 Qwen 上 compelling。Reframe under worst tier:
      aggressive compression（5.3×+）即使在 non-Spread 模型上也有 cardinality constraint 
      的价值（Llama 5.3×: 57.60 vs 2644）——constraint 在极端场景下 universally 有用。

  - name: "High-Resolution Profiling (Qwen7B)"
    plan_id: "plan_006"
    description: >
      64 seq × 2048 tokens hires profiling，重跑 MCKP。
    expected_results:
      hires_constrained_ppl: 10.91
      lowres_constrained_ppl: 11.23
      hires_improvement_over_lowres_pct: 2.8
      hires_nonzero_2bit: 100
      lowres_nonzero_2bit: 37
      hires_profiling_time_min: 65.5
      allocation_diff_count: 8
    result_rationale: >
      Hires profiling 发现更多 non-zero 2-bit delta heads（100 vs 37），
      改善 MCKP allocation（PPL 10.91 vs 11.23，+2.8%）。
      8 个 heads 的 allocation 改变（从 4-bit 到 2-bit 或反向），
      说明 lowres 有 ~7% 的 misallocation。
      在 worst tier 下，hires 对 Qwen7B 有 modest benefit，
      但对 non-Spread 模型（Llama hires: 8.45 vs 8.50）几乎无差。
      且 hires profiling 耗时 65 min（vs lowres ~10 min），
      cost/benefit ratio 在非 Spread 模型上 unjustified。
    tables:
      - name: "Profiling Resolution Comparison"
        columns: [resolution, nonzero_heads, constrained_ppl, time_min]
        rows:
          - ["16×512 (lowres)", 37, 11.23, "~10"]
          - ["64×2048 (hires)", 100, 10.91, 65.5]
    figures_description:
      - "Delta scatter: lowres vs hires per head. r>0.95 但 tail 有 divergence"
    analysis: >
      Hires 提供 modest improvement，但 profiling cost 6× 增加。
      在 reframed narrative 中，hires vs lowres 是 secondary concern——
      constraint 的 contribution 不依赖 profiling resolution。

  - name: "C4 Cross-Dataset Evaluation (Qwen7B)"
    plan_id: "plan_007"
    description: >
      C4 calibration + WikiText-2 evaluation，测试跨 dataset robustness。
    expected_results:
      c4_cal_wt2_eval_mckp_ppl: 11.29
      c4_cal_wt2_eval_uniform_ppl: 15.45
      c4_cal_wt2_eval_improvement_pct: 26.9
      allocation_agreement_c4_vs_wt2: 0.964
      agreement_heads: "108/112"
      cross_domain_wt2_to_c4_mckp_ppl: 20.56
      cross_domain_wt2_to_c4_uniform_ppl: 35.42
    result_rationale: >
      Allocation agreement 96.4% 说明 calibration source 对 Qwen7B 影响很小
      （112 heads 中仅 4 个 disagree）。这是 因为 L0 的 extreme dominance 
      在任何 distribution 上都一致——agreement 本质上是 "L0 is always dominant"。
      Cross-domain PPL（20.56）比 same-domain（11.29）高很多，
      但 vs uniform 仍有大幅改善（20.56 vs 35.42）。
      Worst tier 的问题：14B 上 agreement 可能更低（L0 dominance 弱，
      mid-layer allocation 更 distribution-dependent）。
    tables:
      - name: "C4 Cross-Dataset (Qwen2.5-7B)"
        columns: [calibration, eval, mckp_ppl, uniform_ppl, improvement]
        rows:
          - [WikiText-2, WikiText-2, 11.29, 15.45, "26.9%"]
          - [C4, WikiText-2, 11.29, 15.45, "26.9%"]
          - [WikiText-2, C4, 20.56, 35.42, "42.0%"]
    figures_description:
      - "Allocation agreement heatmap: 96.4% agree, 4 disagree heads in mid-layers"
    analysis: >
      Cross-dataset robustness 在 Qwen7B 上 strong（L0 dominance 使得 allocation 稳定）。
      但这不 extend 到 non-Spread 模型或 14B（where L0 is less dominant）。

  - name: "RateQuant Greedy Comparison"
    plan_id: "plan_008"
    description: >
      RateQuant greedy (Algorithm 1) on {2,4,8,16} vs constrained MCKP。
    expected_results:
      greedy_unconstrained_ppl: 32.45
      mckp_unconstrained_ppl: 36.92
      greedy_constrained_k8_ppl: 11.23
      mckp_constrained_k8_ppl: 11.23
      greedy_constrained_delta_vs_mckp: 0.0012
      bit_distribution: {2: 8, 4: 100, 8: 4}
    result_rationale: >
      Unconstrained greedy (32.45) 和 MCKP (36.92) 都 catastrophically fail。
      Constrained 后两者 converge（Δ=0.0012 ≈ 0）。
      这是 "constraint is the contribution, not the solver" 的 strongest evidence。
      Worst tier 不改变此结论——solver equivalence under constraint 
      是 Qwen7B 的数学属性（constrained feasible set small enough），
      无论 diagnostic 是否成立。
    tables:
      - name: "Solver Comparison (Qwen2.5-7B, budget=0.25)"
        columns: [method, unconstrained_ppl, constrained_k8_ppl]
        rows:
          - [RateQuant Greedy, 32.45, 11.23]
          - [MCKP, 36.92, 11.23]
          - [Uniform 4-bit, "—", 15.45]
    figures_description:
      - "Bar chart: unconstrained vs constrained for both solvers. Constraint eliminates gap"
    analysis: >
      Solver equivalence under constraint 是 robust result，在 worst tier 下
      成为 paper 的 core contribution 之一（不依赖 diagnostic）。

  - name: "Oracle Comparison (Brute-Force Subset)"
    plan_id: "plan_009"
    description: >
      Qwen7B 3-4 layer groups 上 brute-force optimal vs MCKP。
    expected_results:
      mckp_ppl: 10.91
      max_oracle_gap_ppl: 0.0183
      avg_oracle_gap_ppl: 0.0046
      layers_mckp_optimal: "5/8"
      gap_nature: "2-bit head position swap within same bit budget"
    result_rationale: >
      MCKP gap to oracle 极小（max 0.0183 PPL），5/8 layers 完全 optimal。
      Gap 来源：3 个 layer 上 MCKP 选了 slightly suboptimal 的 2-bit head 位置，
      但 bit budget 完全相同——差异仅在 which head gets 2-bit，非结构性错误。
      即使在 worst tier 下，MCKP near-optimality 成立——这不依赖 diagnostic。
    tables:
      - name: "Oracle vs MCKP (Qwen2.5-7B Subset)"
        columns: [layer_group, mckp_ppl, oracle_ppl, gap]
        rows:
          - [L0-L3, 10.91, 10.91, 0.0000]
          - [L1, "—", "—", 0.0183]
          - [L4, "—", "—", 0.0045]
          - [L11, "—", "—", 0.0136]
    figures_description:
      - "MCKP vs Oracle allocation diff: 3/8 layers 有微小 head swap"
    analysis: >
      Near-optimality 是 standalone result，加强 constraint contribution。

  - name: "Cross-Domain Calibration Robustness"
    plan_id: "plan_010"
    description: >
      C4 calibrate / WikiText-2 evaluate 及反向，报告 allocation agreement。
    expected_results:
      qwen_agreement: 0.964
      llama_agreement: 0.977
      mistral_agreement: 0.965
      qwen14b_predicted_agreement: 0.88
    result_rationale: >
      三个 7-9B 模型都有 >96% agreement，说明 calibration robust。
      但 worst tier 预测 Qwen14B 的 agreement 可能降至 ~88%，
      因为 14B 的 sensitivity 更分散、mid-layer heads 的 ranking 
      更 distribution-dependent。这削弱 "one-shot calibration" 的 practicality claim。
    tables:
      - name: "Cross-Calibration Agreement"
        columns: [model, agreement, heads_agree, total]
        rows:
          - [Qwen2.5-7B, "96.4%", 108, 112]
          - [Llama-3.1-8B, "97.7%", 250, 256]
          - [Mistral-7B, "96.5%", 247, 256]
          - ["Qwen2.5-14B (predicted)", "~88%", "~338", 384]
    figures_description:
      - "Agreement rate vs total_kv_heads scatter: 趋势线显示更多 heads → lower agreement"
    analysis: >
      Cross-calibration robustness 在小模型上 strong，
      但可能不 scale to larger models（more heads → more ambiguity）。

  - name: "Head Sensitivity Visualization"
    plan_id: "plan_011"
    description: >
      Paper-quality figures: per-head delta heatmap, compounding curve, allocation comparison。
    expected_results:
      figures_generated: 5
      key_visual: "5-model heatmap comparison shows architecture diversity"
      worst_tier_impact: "14B heatmap looks like diluted version of 7B, weakens family consistency"
    result_rationale: >
      Visualization 不产生新数据但在 worst tier 下需要更新：
      (1) 加入 14B heatmap 显示 diluted spread pattern（与 7B 对比削弱 Qwen family story）
      (2) 三档 gradient bar chart 中 moderate 消失（Gemma-2 BOS fix）
      (3) Decision rule scatter 中 14B 落在 Spread 象限但标记为 false positive
    tables: []
    figures_description:
      - "Fig 1: 6-model per-head delta heatmap (6 panels). 14B 是 weaker version of 7B"
      - "Fig 2: Compounding curves (Qwen 7B/14B + 3 others). 14B curve 比 7B 平缓"
      - "Fig 3: Decision rule scatter with 14B false positive annotated"
      - "Fig 4: Unconstrained ratio bar chart — only 2 tiers after BOS fix"
    analysis: >
      Visualization 诚实展示 diagnostic 的 limitation 反而增加 credibility。
      14B false positive 在 scatter plot 上是 visible anomaly，需要 explicit 讨论。

  - name: "Downstream Task Evaluation (Qwen7B)"
    plan_id: "plan_012"
    description: >
      ARC-C / HellaSwag / PIQA / WinoGrande on Qwen7B + 4 non-Spread models at 4×。
    expected_results:
      qwen_avg_recovery: 0.728
      qwen_arc_c_delta_pp: 3.16
      qwen_hellaswag_delta_pp: 4.00
      yi_mckp_vs_uniform_pp: -0.77
      llama_mckp_vs_uniform_pp: -0.99
      mistral_mckp_vs_uniform_pp: -0.48
      gemma2_mckp_vs_uniform_pp: 0.14
      qwen14b_predicted_mckp_vs_uniform_pp: -0.2
    result_rationale: >
      5-model downstream data 完整，结果与 PPL 一致。
      Worst tier 预测 Qwen14B downstream：MCKP vs uniform ≈ -0.2pp（与 PPL 的 +1.2% 不一致方向？
      不，PPL improvement +1.2% 意味着 MCKP 稍好，downstream 可能 +0.1-0.3pp 或 noise）。
      但 14B 的 downstream 数据不足以区分 signal vs noise（无 multi-seed CI）。
      论文需报告 14B 但不能 claim benefit。
    tables:
      - name: "Downstream Summary (6 Models)"
        columns: [model, shape, mckp_vs_uniform_pp, diagnostic_correct]
        rows:
          - [Qwen2.5-7B, Spread, "+2.60pp", "✅"]
          - ["Qwen2.5-14B", "Diluted Spread", "-0.2pp (noise)", "❌ FP"]
          - [Yi-1.5-9B, Spike, "-0.77pp", "✅"]
          - [Llama-3.1-8B, Spike, "-0.99pp", "✅"]
          - [Mistral-7B, Flat, "-0.48pp", "✅"]
          - [Gemma-2-9B, Flat, "+0.14pp (noise)", "✅"]
    figures_description:
      - "Grouped bar chart: 6-model downstream delta. Only Qwen7B clearly positive"
    analysis: >
      Downstream data 在 worst tier 下 reinforces "1/6 models benefit"——
      更适合 framing 为 systematic negative result + one strong positive case study。

  - name: "70B Profiling-Only (Qwen2.5-72B)"
    plan_id: "plan_013"
    description: >
      Qwen2.5-72B distortion profiling（不做 eval），分析 sensitivity 是否随 model size 缩放。
    expected_results:
      qwen72b_concentration: 0.48
      qwen72b_t1_t5: 0.69
      qwen72b_l0_dominance_ratio: 5.1
      qwen72b_total_heads: 640
      qwen72b_diagnostic_prediction: "borderline (conc<0.50)"
    result_rationale: >
      72B 有 80 layers × 8 KV heads = 640 heads。更多层进一步稀释 concentration。
      Concentration=0.48（刚低于 0.50 阈值），t₁/t₅=0.69（刚低于 0.70）。
      Diagnostic 预测 borderline/Flat——如果确实如此，
      则 Qwen 模型族呈现 "7B=Spread, 14B=Diluted Spread, 72B=Flat" 的递减梯度，
      说明 model size increase 系统性地 dilute sensitivity concentration。
      这直接挑战 "Qwen family is Spread" 的 assumption。
    tables:
      - name: "Qwen Family Scaling"
        columns: [model, params, layers, kv_heads, concentration, t1_t5, predicted_shape]
        rows:
          - [Qwen2.5-7B, 7B, 28, 112, 0.61, 0.57, Spread]
          - [Qwen2.5-14B, 14B, 48, 384, 0.55, 0.63, "Diluted Spread"]
          - [Qwen2.5-72B, 72B, 80, 640, 0.48, 0.69, "Borderline/Flat"]
    figures_description:
      - "Concentration vs model size: monotonic decrease within Qwen family"
    analysis: >
      如果 72B profiling 证实 concentration < 0.50，则 Spread pattern 
      不是 Qwen architecture 的固有属性而是 small-model artifact。
      这对 diagnostic 的 practical value 是致命打击——
      practitioner 最关心的 large models 恰恰最不可能是 Spread。

  - name: "K/V Separation"
    plan_id: "plan_014"
    description: >
      将 K 和 V heads 作为独立 MCKP items，允许 asymmetric K/V budget。
    expected_results:
      kv_sep_ppl: 11.22
      joint_kv_ppl: 10.91
      uniform_4bit_ppl: 15.45
      delta_sep_vs_joint: 0.31
      sep_k_2bit_count: 16
      sep_v_uniform_4bit: true
    result_rationale: >
      K/V separation 让 solver 独立优化 K 和 V 的 budget。
      结果：V heads 全部 4-bit（sensitivity 低），K heads 有 16 个 2-bit（budget 被 V 让渡）。
      但 PPL 11.22 略差于 joint optimization 的 10.91（Δ=0.31），
      因为 K-only 2-bit 的 compounding 比 joint 分配更 aggressive。
      在 worst tier 下，这是 negative result——joint optimization 优于 separation，
      说明 K/V interaction matters，简单的 asymmetric budget 不够。
    tables:
      - name: "K/V Separation (Qwen2.5-7B)"
        columns: [method, ppl, k_2bit, v_2bit, vs_joint]
        rows:
          - [Joint K+V, 10.91, 4, 4, baseline]
          - [K/V separated, 11.22, 16, 0, "+2.8%"]
          - [Uniform 4-bit, 15.45, 0, 0, "+41.6%"]
    figures_description:
      - "K vs V bit allocation heatmap: separated strategy over-allocates K 2-bit"
    analysis: >
      Negative result：K/V separation 不如 joint optimization。
      论文用 1 paragraph 报告，作为 RateQuant comparison 的补充。

  - name: "L0-Only Heuristic Baseline"
    plan_id: "plan_015"
    description: >
      最简单的 non-uniform 策略：L0 全部 8-bit，其余 uniform 4-bit。
      如果匹配 MCKP，则 full optimization 不必要。
    expected_results:
      qwen_l0_random_mean: 11.69
      qwen_l0_random_median: 11.52
      qwen_l0_random_std: 0.47
      qwen_naive_positional_ppl: 12.23
      qwen_mckp_ppl: 10.91
      llama_l0_random_mean: 10.48
      llama_mckp_ppl: 8.45
      mistral_l0_random_mean: 7.56
      mistral_mckp_ppl: 7.16
    result_rationale: >
      L0-random heuristic（随机选 k 个 non-L0 heads 做 2-bit）在 Qwen 上
      median=11.52 vs MCKP=10.91（gap 5.6%）。MCKP 的优势来自 
      precisely 选择 which non-L0 heads 做 2-bit（vs random）。
      在 Llama/Mistral 上 L0-random 显著差于 MCKP（且 MCKP ≈ uniform），
      说明 heuristic 不是 universal substitute。
      Worst tier 的 concern：14B 上 L0-random 可能 ≈ MCKP（因为 14B 的 MCKP 本身 ≈ uniform），
      进一步削弱 MCKP 的 value proposition。
    tables:
      - name: "L0 Heuristic vs MCKP"
        columns: [model, l0_random_median, mckp, uniform, mckp_vs_heuristic_gap]
        rows:
          - [Qwen2.5-7B, 11.52, 10.91, 15.45, "5.6%"]
          - [Llama-3.1-8B, 10.04, 8.45, 8.47, "18.8%"]
          - [Mistral-7B, 7.59, 7.16, 7.13, "6.0%"]
    figures_description:
      - "MCKP vs heuristic vs uniform across 3 models: MCKP consistently better than heuristic"
    analysis: >
      MCKP outperforms heuristic on all models，但 gap varies。
      在 non-Spread models，MCKP 和 heuristic 都 ≤ uniform——
      the right choice is "don't bother" rather than "optimize better"。

  - name: "RateQuant Greedy + Cardinality Constraint"
    plan_id: "plan_016"
    description: >
      验证 constraint 是否是 key contribution（vs solver choice）。
      Greedy + k=8 vs MCKP + k=8 vs both unconstrained。
    expected_results:
      greedy_unconstrained_ppl: 32.45
      mckp_unconstrained_ppl: 36.92
      greedy_constrained_k8_ppl: 11.23
      mckp_constrained_k8_ppl: 11.23
      delta_greedy_vs_mckp_constrained: 0.0012
      solver_equivalence: true
    result_rationale: >
      Core finding：constraint 使 greedy = MCKP（Δ=0.0012 ≈ 0）。
      Constrained feasible set 小到 greedy 的 local search 等于 global optimum。
      这是 paper 最 robust 的 result——不依赖 diagnostic，不依赖 model choice，
      纯数学属性。在 worst tier 下这是 anchor result。
    tables:
      - name: "Solver Equivalence Under Constraint"
        columns: [method, unconstrained, constrained_k8, delta]
        rows:
          - [RateQuant Greedy, 32.45, 11.23, "—"]
          - [MCKP, 36.92, 11.23, "Δ=0.0012"]
    figures_description:
      - "2×2 grid: solver × constraint, showing constraint eliminates solver gap"
    analysis: >
      在 reframed worst-tier narrative 中，solver equivalence under constraint 
      成为 Claim 1 的 core evidence。不需要 diagnostic 来 motivate。

  - name: "Multi-Seed Error Bars (Qwen7B)"
    plan_id: "plan_017"
    description: >
      3 个 calibration seed 的 constrained MCKP，报告 mean±std。
    expected_results:
      mckp_seed0: 11.02
      mckp_seed1: 10.90
      mckp_seed2: 11.05
      mckp_mean: 10.99
      mckp_std: 0.065
      uniform_ppl: 15.45
      allocation_agreement_3way: 0.902
      bit_dist_all_seeds: "2:8, 4:100, 8:4"
    result_rationale: >
      三个 seed 的 MCKP PPL std=0.065（mean=10.99），95% CI = [10.86, 11.12]。
      与 uniform 的 gap（15.45 - 10.99 = 4.46）远大于 CI width（0.26），
      Qwen7B 上的 improvement 是 statistically robust。
      Bit distribution 三个 seed 完全一致（8:100:4），allocation agreement 90.2%
      （head-level 有 10% variation 但 bit-level distribution 不变）。
      Worst tier 的 concern：14B 上 std 可能更大（sensitivity 更分散 → calibration noise 更大），
      且 improvement 本身在 noise 范围内。
    tables:
      - name: "Multi-Seed Results (Qwen2.5-7B)"
        columns: [seed, mckp_ppl, bit_dist, agreement_with_seed0]
        rows:
          - [seed_0, 11.02, "8:100:4", "—"]
          - [seed_1, 10.90, "8:100:4", "94.6%"]
          - [seed_2, 11.05, "8:100:4", "91.1%"]
          - [mean±std, "10.99±0.065", "—", "—"]
    figures_description:
      - "Error bar plot: 3 seeds with 95% CI, clearly separated from uniform baseline"
    analysis: >
      Qwen7B 的 statistical robustness 是 solid。但 N=3 seeds 仍然 limited。
      论文应报告 "our main result is robust to calibration variation" 但 
      not claim "statistical significance" formally。

  - name: "Runtime/Latency Benchmark (Qwen7B)"
    plan_id: "plan_018"
    description: >
      端到端 inference latency 和 throughput。
    expected_results:
      bf16_prefill_ms: 45.86
      bf16_decode_ms: 33.78
      uniform4_prefill_ms: 54.25
      uniform4_decode_ms: 42.46
      mckp_prefill_ms: 57.03
      mckp_decode_ms: 46.09
      mckp_throughput_tok_s: 21.8
      uniform4_throughput_tok_s: 23.6
      mckp_solver_sec: 0.005
      mckp_overhead_vs_uniform_pct: 8.5
    result_rationale: >
      Mixed-precision MCKP 比 uniform 4-bit 慢 ~8.5%（decode 46.09 vs 42.46 ms/tok），
      因为 mixed bit-width 需要 per-head dequantize dispatch（vs uniform 的 vectorized batch dequant）。
      内存相同（5.25 MB），solver 本身 negligible（5ms）。
      Worst tier 的 concern：8.5% latency overhead 换 PPL improvement 仅在 Qwen7B 上 worth it——
      在 non-Spread 模型上 overhead 仍存在但 PPL 无 improvement，
      纯亏损。Reviewer 会问 "when is the latency cost justified?"
    tables:
      - name: "Runtime Benchmark (Qwen2.5-7B)"
        columns: [config, prefill_ms, decode_ms, throughput, memory_MB]
        rows:
          - [bf16, 45.86, 33.78, "29.6 tok/s", 21.0]
          - [uniform 4-bit, 54.25, 42.46, "23.6 tok/s", 5.25]
          - [MCKP constrained, 57.03, 46.09, "21.8 tok/s", 5.25]
    figures_description:
      - "Latency breakdown bar chart: prefill + decode. MCKP overhead visible but small"
    analysis: >
      8.5% latency overhead 是 acceptable trade-off 但仅在 Spread models 上。
      Reframe: "if diagnostic uncertain, use uniform 4-bit to avoid latency cost" 
      — 这与 worst-tier narrative 的 "conservative recommendation" 一致。

  # ============================================================
  # W9 Compounding Scaling（影响 compounding 叙事）
  # ============================================================
  - name: "W9 Compounding Scaling (Worst Tier)"
    plan_id: "w9_compounding_v2"
    description: >
      Qwen7B 上 top-k vs random-k 2-bit assignment sweep，刻画 super-additivity。
    expected_results:
      k1_topk_ppl: 9.83
      k1_randomk_ppl: 9.89
      k4_topk_ppl: 9.85
      k4_randomk_ppl: 10.06
      k8_topk_ppl: 10.04
      k8_randomk_ppl: 11.07
      k16_topk_ppl: 10.42
      k16_randomk_ppl: 12.91
      k32_topk_ppl: 11.60
      k32_randomk_ppl: 18.33
      k64_topk_ppl: 22.95
      k64_randomk_ppl: 55.94
      k64_randomk_topk_ratio: 1.45
      k32_randomk_topk_ratio: 1.58
      k16_randomk_topk_ratio: 1.24
      non_monotonic_flag: true
      variance_at_k16_masks_trend: true
    result_rationale: >
      Worst-tier 下 k=64 的 randomk/topk ratio 降至 1.45（vs 实际 2.44 的 actual data 中位估计）。
      k=8-16 区间出现 non-monotonic：k=8 ratio=1.76 但 k=16 ratio 回落到 1.24，
      然后 k=32 又升到 1.58。这种 non-monotonicity 可能来自：
      (1) random-k 的 seed variance（std=0.4-2.5 across seeds），
      (2) top-k 在某些 k 值恰好避开 interaction cluster 而 random 没有。
      Non-monotonic behavior 使得 "super-additivity monotonically increases with k" 
      的 clean story 不成立。论文需要 acknowledge variance 并报告 CI。
      ratio 的 overall trend 仍是 increasing（1.24→1.45→1.58→1.45），
      但 non-monotonicity at intermediate k 削弱 formalization strength。
    tables:
      - name: "W9 Compounding (Worst-Tier Interpretation)"
        columns: [k, topk_ppl, randomk_ppl, randomk_std, ratio, monotonic]
        rows:
          - [1, 9.83, 9.89, 0.05, 1.00, "—"]
          - [4, 9.85, 10.06, 0.06, 1.24, "↑"]
          - [8, 10.04, 11.07, 0.69, 1.76, "↑"]
          - [16, 10.42, 12.91, 0.40, 1.24, "↓ ⚠️"]
          - [32, 11.60, 18.33, 2.53, 1.58, "↑"]
          - [64, 22.95, 55.94, 9.73, 1.45, "↓ ⚠️"]
    figures_description:
      - "Ratio vs k line plot with error bars: non-monotonic, variance band wide at k=32,64"
    analysis: >
      在 worst tier 下，W9 data 的 non-monotonicity 和 high variance 
      使得 formal super-additivity claim 不成立。
      Reframe: 报告为 "empirical observation of compounding trend with substantial variance"，
      不 formalize 为 theorem 或 proposition。
      Compounding 的 qualitative story 仍 hold（ratio >1 at all k>1），
      但 quantitative precision 不足以支撑 formal contribution。

  # ============================================================
  # Qwen14B Downstream (implied follow-up)
  # ============================================================
  - name: "Qwen2.5-14B Downstream Eval (Predicted)"
    plan_id: "w1_qwen14b_downstream"
    description: >
      如果 14B profiling + MCKP 完成，需跑 downstream eval 验证 PPL 与 downstream 一致性。
    expected_results:
      qwen14b_baseline_avg: 0.72
      qwen14b_uniform_avg: 0.71
      qwen14b_mckp_avg: 0.71
      qwen14b_mckp_vs_uniform_pp: 0.1
      qwen14b_arc_challenge_delta_pp: -0.5
      qwen14b_hellaswag_delta_pp: 0.3
    result_rationale: >
      PPL improvement +1.2% → downstream ≈ 0pp（noise）。
      arc_challenge 可能略负（-0.5pp），与跨模型的 arc_challenge 系统性敏感一致。
      hellaswag 略正（+0.3pp）但在 seed noise 范围内。
      整体结论：14B downstream 与 PPL 一致——MCKP 无 meaningful benefit。
    tables:
      - name: "Qwen14B Downstream (Predicted)"
        columns: [task, uniform, mckp, delta_pp]
        rows:
          - [arc_challenge, 0.58, 0.575, "-0.5"]
          - [hellaswag, 0.72, 0.723, "+0.3"]
          - [piqa, 0.81, 0.811, "+0.1"]
          - [winogrande, 0.73, 0.728, "-0.2"]
          - [average, 0.71, 0.71, "+0.1"]
    figures_description:
      - "Per-task delta bar chart: all within ±0.5pp noise band"
    analysis: >
      Downstream 确认 14B false positive——不仅 PPL 无 improvement，
      downstream 也在 noise。论文需要 transparent reporting。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea84c017-2a73-4fd6-a9bc-fb3bf17d484f",
  "isSidechain": false,
  "requestId": "req_011Cb48irCQeFpBUqJvYzLJy",
  "type": "assistant",
  "uuid": "b4fb4e78-87d0-4bd0-965a-a2a08dc51086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LKiRzMBxwVPFFD1yygGXP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4392,
      "cache_read_input_tokens": 73107,
      "output_tokens": 20102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20102,
          "cache_read_input_tokens": 73107,
          "cache_creation_input_tokens": 4392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4392
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Qwen2.5-14B 不是 Spread 或 MCKP 无效，decision rule 出现 false positive/negative，核心 diagnostic 叙事不成立 核心假设：['Qwen2.5-14B concentration ≥0.50 但 MCKP 无改善（类似 Yi-1.5，d…",
  "leafUuid": "b4fb4e78-87d0-4bd0-965a-a2a08dc51086",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing when per-head KV cache quantization helps across architectures",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Qwen2.5-14B 不是 Spread 或 MCKP 无效，decision rule 出现 false positive/negative，核心 diagnostic 叙事不成立 核心假设：['Qwen2.5-14B concentration ≥0.50 但 MCKP 无改善（类似 Yi-1.5，d…",
  "leafUuid": "b4fb4e78-87d0-4bd0-965a-a2a08dc51086",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing when per-head KV cache quantization helps across architectures",
  "sessionId": "ed67fc76-685e-40e0-9769-deccf8f764ed"
}
```

---
