# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Qwen2.5-14B 边界/弱阳性，N 实质仍为 1；其余数据基本一致但有小幅偏差需要对齐 核心假设：['Qwen2.5-14B concentr

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/381281cc-1805-4751-910c-f2c4d66fa847.jsonl`
- **Structured JSON:** [`5f622f165ff68fd3035f.json`](../../sessions/5f/5f622f165ff68fd3035f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T09:10:57.033Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T09:10:57.033Z",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Qwen2.5-14B 边界/弱阳性，N 实质仍为 1；其余数据基本一致但有小幅偏差需要对齐\n核心假设：['Qwen2.5-14B concentration 0.40-0.55 或 t₁/t₅ 0.65-0.80（边界区间，不完全满足 joint condition）', 'Qwen2.5-14B MCKP 改善 3-15%（有正向信号但不如 Qwen-7B 显著）', 'Decision rule 5/6 或 6/6 但 14B 是 borderline case 需要特殊讨论', 'Gemma-2 BOS fix 后 unconstrained ratio 在 1.30-1.55 范围，可能需要微调数字', 'W9 compounding 趋势成立但 variance 大，形式化为 observation 而非 proposition']\n关键指标范围：{'qwen14b_mckp_improvement_over_uniform_pct': [3, 15], 'qwen14b_concentration': [0.4, 0.55], 'qwen14b_t1_t5': [0.55, 0.8], 'decision_rule_accuracy': [5, 6], 'gemma2_constrained_vs_uniform_pct': [-1.0, 1.0], 'gemma2_unconstrained_ratio': [1.3, 1.55], 'w9_k64_randomk_topk_ratio': [1.5, 2.5]}\n叙事方向：Claim 3 保持 \"empirical decision rule\"（不升级）。14B 作为 \"boundary case\"  单独一段讨论：说明 threshold 是 soft boundary 而非 hard cutoff， 符合 empirical nature。如果 5/6，承认 rule 是 directional heuristic， 在 Limitation 明确写 \"N=1 confirmed Spread; larger-scale validation needed\"。 三档标签仍可用但需要把 threshold 描述软化 （\"approximately 0.50\" → \"in the range 0.45-0.55\"）。 Gemma-2 段落可能需微调具体数字但 \"moderate degradation + universal constraint value\"  叙事不变。W9 super-additive 降为 empirical observation（图 + 描述性文字）， 不写 formal proposition。整体仍可投 EMNLP Main，但 contribution 重心 从 \"diagnostic\" 向 \"constraint as universal fix\" 倾斜。补充实验： 考虑加 Qwen2.5-3B 或 Qwen2.5-32B 碰运气找第二个 Spread 样本。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ratekv\nfocus: 审稿修订后的 concentration-dependent narrative 是否 hold：(1) 三档标签(catastrophic/moderate/mild)是否自洽 (2) N=1 Spread + empirical decision rule 的 claim 强度是否匹配 EMNLP Main (3) Gemma-2 1.47× 讨论是否充分 (4) W9 super-additive 形式化程度是否足够 (5) 5-model downstream 完整数据下 story 是否比之前更强\n\n## paper_framing.md\n\n# Paper Framing — ratekv\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)\n- Track: Efficient Methods for NLP\n\n## bf16 Consistency Resolution (2026-05-14)\n\n**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。\n\n**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。\n\n| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |\n|------|---------------------|----------------------|-----------|\n| Baseline | **9.8106** | 8.819 | 9.81 |\n| Uniform 4-bit | **15.4454** | — | 15.45 |\n| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |\n| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |\n\n## Core Insight\n\nPer-head KV cache quantization sensitivity varies dramatically across architectures, and the effectiveness of non-uniform mixed-precision allocation is fundamentally determined by the degree of this heterogeneity. We provide both the analysis framework — characterizing when non-uniform quantization helps via per-head sensitivity concentration metrics — and a surprisingly simple method fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding effects from profiler non-additivity and reduces the search space sufficiently that solver choice becomes irrelevant (greedy and MCKP produce identical allocations).\n\n## Core Claims (3 条)\n\n1. **Head sensitivity heterogeneity is architecture-dependent and determined by sensitivity *distribution shape*, not GQA ratio or concentration alone**: Per-KV-head quantization sensitivity is extremely non-uniform within models, but whether MCKP can exploit this heterogeneity depends on the *shape* of the sensitivity distribution, not just its magnitude. Critical counterexample: Yi-1.5-9B (GQA 8:1, concentration 0.71 — the *highest* in our lineup) provides *no benefit* from MCKP (7.22 vs 7.22 uniform), while Qwen2.5-7B (GQA 7:1, concentration 0.61) succeeds (+27.3%). The difference is distribution shape: Qwen has a *cluster* of sensitive heads (Layer 0, 4 heads with cross-bitwidth gradients — \"spread\" pattern, t₁/t₅=0.57), while Yi-1.5 has a single extreme outlier (L4H3, delta=13.12, t₁/t₅=0.90 — \"spike\" pattern) with sensitivity at only one bitwidth. A joint diagnostic — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case (Qwen) from all four non-beneficial cases across five architectures. Three shape categories emerge:\n   - **Spread** (Qwen): high concentration + low t₁/t₅ → multiple heads with cross-bitwidth gradients → MCKP effective\n   - **Spike** (Yi-1.5, Llama): high t₁/t₅ → single outlier dominates → MCKP ineffective\n   - **Flat** (Mistral, Gemma-2): low concentration → near-uniform sensitivity → MCKP ineffective (t₁/t₅ irrelevant when concentration < 0.50)\n\n2. **Cardinality constraint is the primary intervention; unconstrained catastrophe is Spread-specific**: On non-consecutive discrete bit-widths {2,4,8,16}, unconstrained allocation produces **catastrophic** results on Spread-heterogeneity architectures (Qwen: greedy 32.45, MCKP 36.92 vs uniform 15.45 = 3.31× baseline) because per-head independent profiling distortions compound non-additively when many heads are simultaneously assigned extreme quantization. On non-Spread architectures, unconstrained allocation causes **mild-to-moderate degradation** (Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.47×) but still underperforms uniform 4-bit in all cases — the solver over-allocates 2-bit heads even when individual distortions appear small. A cardinality constraint (max_2bit≤k) is a simple and sufficient condition: it prevents compounding on Spread models, avoids 2-bit over-allocation on non-Spread models, AND reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce identical bit allocations and PPL (Δ=0.0000, both 11.2312). **Practical implication**: the concentration diagnostic determines whether to invest in MCKP + constraint (Spread models) or simply use uniform 4-bit (non-Spread models — saves solver computation with no quality loss). The profiling benefit beyond the constraint (hires vs lowres) is architecture-dependent: substantial on Spread models (Qwen), marginal on others. The optimal k is determinable via small-scale compounding effect test (plan_004).\n\n**Claim 2 three-pillar support** (Reviewer Q4, new narrative STRENGTHENS Claim 2):\n1. Spread models: constraint prevents catastrophe (Qwen 32.45→11.23)\n2. Flat models: constraint prevents moderate over-allocation (Gemma-2 8.85→~6.17, 106→8 heads at 2-bit)\n3. All models: constraint makes solver choice irrelevant (greedy=MCKP, Δ=0.0000)\nThis answers \"when\" and \"why\", not just \"what\" — stronger than original \"universal catastrophe\" narrative.\n\n3. **A joint empirical decision rule correctly separates beneficial from non-beneficial architectures**: Constrained allocation achieves 27.3% PPL improvement on Qwen (spread pattern: concentration 0.61, t₁/t₅=0.57), while providing no benefit on Yi-1.5 (spike: 0.71, t₁/t₅=0.90, ≈0%), Llama (spike: 0.34, t₁/t₅=0.71, +0.2%), Mistral (flat: 0.22, t₁/t₅=0.18, -0.4%), and Gemma-2 (flat: 0.23, t₁/t₅=0.38, -0.3%). The joint condition — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case from all four non-beneficial cases across five architectures (5/5 accuracy). Concentration alone fails: Yi-1.5 (0.71) exceeds Qwen (0.61) yet gains nothing, because its spike pattern (single outlier, no cross-bitwidth gradient) cannot be exploited. Under aggressive compression (≥5×), constrained allocation prevents catastrophic collapse even on non-beneficial architectures (Llama 5.3×: constrained PPL 57.60 vs uniform 2-bit 2644). This provides practitioners an empirical decision rule for when to invest in mixed-precision KV cache quantization. **Claim strength note (Reviewer-verified)**: N=1 Spread → position as \"empirical decision rule\", NOT \"diagnostic framework\". If Qwen2.5-14B also confirms Spread → upgrade to \"empirical diagnostic\" (N=2).\n\n## Story Spine\n\n- **Problem**: KV cache quantization typically applies uniform bit-width across all heads. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but two fundamental questions remain unanswered: (1) *when* does non-uniform allocation actually help — i.e., under what architectural and compression conditions does the added complexity pay off? (2) *how* to make existing allocation algorithms (greedy, MCKP) work correctly on hardware-aligned discrete bit-widths {2,4,8,16} where they currently fail catastrophically?\n\n- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via continuous closed-form (Theorem 2) and discrete greedy (Algorithm 1, optimal on consecutive integers {2,...,6} per Proposition 6). However, on hardware-aligned non-consecutive sets {2,4,8,16}, RateQuant's greedy produces PPL 32.45 (vs optimal ~11.23) — the polymatroid structure that guarantees greedy optimality breaks. Moreover, unconstrained MCKP fares even worse (PPL 36.92) due to compounding effects from profiler non-additivity. Critically, neither RateQuant nor ARKV addresses *when* non-uniform allocation is beneficial.\n\n- **Our framing**: We present a systematic study of per-head KV cache quantization sensitivity across architectures and identify a surprisingly simple fix for the failure of existing algorithms on hardware-aligned bit-widths: a cardinality constraint limiting the number of heads assigned to extreme quantization levels. This single intervention (a) prevents compounding effects, (b) reduces the search space to where solver choice is irrelevant — greedy and MCKP produce identical optimal allocations, and (c) can be parameterized via a small-scale compounding test. Beyond the method, we establish that the benefit of non-uniform allocation is architecture-dependent and quantifiable via an empirical decision rule (concentration + distribution shape), providing practitioners a two-metric check for when mixed-precision is worthwhile.\n\n- **Headline result template**: \"We show that the benefit of non-uniform per-head KV cache quantization is concentration-dependent: on spread-heterogeneity architectures (Qwen, concentration 0.61), unconstrained solvers fail catastrophically (PPL 32-37 vs uniform 15.45), while a cardinality constraint (≤k heads at 2-bit) achieves 27.3% PPL improvement with identical results from greedy and MCKP (Δ=0.0000). On non-spread architectures (4 models, 1.07-1.47× baseline), unconstrained solvers cause only mild degradation, and constrained MCKP offers no benefit over uniform 4-bit at either PPL or downstream task level (<1pp avg). An empirical decision rule (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly separates the beneficial case from all four non-beneficial cases (5/5 accuracy) at both PPL and downstream task level, providing practitioners a two-metric check to determine whether mixed-precision KV cache quantization is worthwhile — or whether uniform quantization suffices.\"\n\n## \"When Does Non-Uniform Allocation Help?\" — Analysis Chapter\n\nFive case studies representing the full spectrum of heterogeneity:\n\n| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |\n|------|-------|-----|--------------|------------------------------|---------------|\n| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; \"spread\" pattern (L0 cluster, 4 heads, 26× dominance) |\n| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; \"spike\" pattern (L4H3 single outlier, 34% of total delta) |\n| **Marginal** | Llama-3.1-8B | 4:1 | 0.34-0.59 | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |\n| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |\n| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |\n\n**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.\n\n**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).\n\n**Joint diagnostic** (n=5, 5/5 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike) and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.\n\n## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)\n\n| Method | PPL | Bit Distribution | Budget |\n|--------|-----|-------------------|--------|\n| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |\n| MCKP unconstrained | 36.92 | — | 0.25 |\n| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |\n\nKey takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.\n\n## Cross-Architecture Evidence Summary\n\n| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |\n|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|\n| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |\n| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |\n| Llama-3.1-8B | 4:1 | 256 | 0.57 (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (borderline t₁/t₅=0.71) | ≈ Marginal |\n| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |\n| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |\n\n**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:\n- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding\n- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta\n- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)\n- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads\n\n**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):\n\nThree-tier labeling (NOT binary catastrophe/benign):\n- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding\n- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions\n- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)\n\nReviewer-suggested paragraph for paper (1 段, 3-4 句):\n\"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\"\n\nThis **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.\n\n⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.\n\n**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.\n\n**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.\n\n### Mistral k Ablation (256 KV heads, budget=0.25)\n\nPPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).\n\n| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |\n|---|-----|-------|-------|-------|--------|-----|\n| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |\n| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |\n| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |\n| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |\n| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |\n| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |\n\nContrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.\n\n### Llama k Ablation (256 KV heads, budget=0.25)\n\nAll k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).\n\n### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)\n\n**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅\n\n| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |\n|------|---------------|------------|---|---------------|\n| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |\n| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |\n| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |\n| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |\n| **Avg recovery** | — | — | **72.8%** | — |\n\n**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.7946 | 0.7854 | -0.92pp |\n| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |\n| hellaswag | 0.5857 | 0.5797 | -0.60pp |\n| piqa | 0.7927 | 0.7894 | -0.33pp |\n| winogrande | 0.7174 | 0.7301 | +1.27pp |\n| **Average** | **0.6822** | **0.6745** | **-0.77pp** |\n\n**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.8173 | 0.8039 | -1.34pp |\n| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |\n| hellaswag | 0.6026 | 0.6012 | -0.14pp |\n| piqa | 0.7867 | 0.7802 | -0.65pp |\n| winogrande | 0.7253 | 0.7238 | -0.15pp |\n| **Average** | **0.6915** | **0.6816** | **-0.99pp** |\n\n**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=4) | Δ |\n|------|---------------|------------|---|\n| arc_easy | — | — | — |\n| arc_challenge | — | — | — |\n| hellaswag | — | — | — |\n| piqa | — | — | — |\n| winogrande | — | — | — |\n| **Average** | **0.6894** | **0.6846** | **-0.48pp** |\n\n**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)\n\n| Task | Uniform 4-bit | MCKP | Δ |\n|------|---------------|------|---|\n| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |\n\n**Downstream summary (Reviewer-verified framing)**:\n- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**\n- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)\n- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)\n- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise\n- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)\n- **Paper must**: (a) report full per-task tables, not just averages, (b) use \"shows minor degradation\" NOT \"preserves accuracy\" — the latter has spin, (c) note arc_challenge as worst-case explicitly\n- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance\n- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论：\"ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\"\n- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞：\"Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge).\"\n\n## Allocation Baseline Evidence (plan_015, mckp_reeval)\n\nAll numbers from unified bf16 eval pipeline, budget=0.25.\n\n| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |\n|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|\n| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |\n| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |\n| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |\n\n**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.\n\n**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.\n\n## Differentiation from RateQuant\n\n| Aspect | RateQuant | Ours |\n|--------|-----------|------|\n| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |\n| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |\n| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |\n| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |\n| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |\n| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |\n| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |\n\n## Venue Fit Risks\n\n- **\"The constraint is just a heuristic, not a real contribution\"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.\n- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.\n- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive \"higher GQA = more benefit\" hypothesis and shows our diagnostic is needed.\n- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 5/5 correct). The \"spike vs spread\" analysis explains WHY same-GQA models differ.\n- **Statistical power**: n=5 models is directional evidence, not statistical claim. Do NOT claim \"significant correlation\" — use \"consistent pattern across 5 architectures\" or \"5/5 correctly classified by the 0.50 threshold.\"\n- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.\n\n## Anticipated Reviewer Concerns\n\n1. **\"The cardinality constraint is trivial — just cap the extreme allocations\"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.\n2. **\"This is just RateQuant with a constraint added\"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.\n3. **\"The method only works on Qwen — isn't this a Qwen paper?\"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.\n4. **\"How does this work at different compression ratios?\"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.\n5. **\"n=3/4/5 models is not enough for the heterogeneity claim\"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.\n6. **\"RateQuant does K/V asymmetric allocation, do you?\"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.\n7. **\"Where are the downstream task results?\"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use \"shows minor degradation\" not \"preserves accuracy\".\n8. **\"The profiler distortion=0.0 on Mistral suggests the profiling method is broken\"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.\n9. **\"If solver doesn't matter, why present MCKP at all?\"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim:\n  - 2\n  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.\n    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.\n    Strengthens narrative: \"solver automatically discovers sensitivity structure.\"\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: exp_d_no_l0_exclusion\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_002\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).\n    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability\n    across different GQA ratios and architectures. Fallback if HF token unavailable:\n    Yi-1.5-9B (non-gated, similar scale).\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: llama_full_pipeline\n  model: Llama-3.1-8B\n  fallback_model: Yi-1.5-9B\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 8.7\n    uniform_4bit_ppl_bf16: 8.47\n    baseline_ppl_bf16: 8.09\n    delta_vs_uniform: -0.23\n    memory_ratio: 0.25\n- id: plan_003\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture\n    family to establish cross-architecture validity.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mistral_full_pipeline\n  model: Mistral-7B-v0.3\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 7.564\n    uniform_4bit_ppl_bf16: 7.131\n    baseline_ppl_bf16: 7.035\n    delta_vs_uniform: -0.433\n    memory_ratio: 0.25\n- id: plan_004\n  claim:\n  - 3\n  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112\n    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map\n    the compounding threshold. Establishes the principled basis for cardinality constraint\n    selection.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: compounding_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_005\n  claim:\n  - 2\n  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,\n    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline\n    at same budget.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: budget_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_006\n  claim:\n  - 1\n  - 2\n  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).\n    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers\n    mid-layer heterogeneity and improves solver allocation beyond current results.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_e_hires_profile\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    constrained_ppl_bf16: 9.569\n    baseline_ppl_bf16: 8.819\n    exp_c_ppl_bf16: 11.345\n    delta_vs_exp_c: -1.776\n    memory_ratio: 0.25\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    profile_resolution:\n      hires_nonzero_2bit: 100\n      lowres_nonzero_2bit: 37\n      hires_nonzero_4bit: 6\n      lowres_nonzero_4bit: 4\n      total_heads: 112\n    allocation_diff_count: 8\n    profiling_time_min: 65.5\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.\n    Cross-dataset evaluation to show results are not WikiText-2 specific.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  eval: C4\n  status: DONE\n  conclusion: success\n  metrics: &id001\n    c4_cal_wt2_eval_mckp_ppl: 11.2942\n    c4_cal_wt2_eval_uniform_ppl: 15.4454\n    c4_cal_wt2_eval_delta: 4.1512\n    c4_cal_bf16_baseline: 12.6505\n    wt2_bf16_baseline: 9.8106\n    allocation_agreement_c4_vs_wt2: 0.964\n    agreement_heads: 108/112\n    bit_dist: 2bit:8, 4bit:100, 8bit:4\n    cross_domain_wt2_to_c4_mckp_ppl: 20.5601\n    cross_domain_wt2_to_c4_uniform_ppl: 35.4232\n    cross_domain_c4_bf16: 15.3246\n    old_contaminated_ppl: 11.3285\n    contamination_impact: 0.0343\n    models_completed: Qwen2.5-7B only\n- id: plan_008\n  claim:\n  - 2\n  description: 'RateQuant comparison: implement RateQuant''s greedy algorithm (Algorithm\n    1) on our discrete action set {2,4,8,16}-bit. RateQuant''s Prop. 6 optimality\n    relies on consecutive-integer polymatroid structure which breaks on non-consecutive\n    sets. Show greedy produces suboptimal allocation vs constrained MCKP. Critical\n    for differentiation claim — must have experimental evidence.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: ratequant_greedy_comparison\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_009\n  claim:\n  - 2\n  description: 'Oracle comparison: brute-force optimal allocation on a subset (3-4\n    layer groups) of Qwen2.5-7B. Quantify MCKP gap to oracle.\n\n    '\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_006\n  registry_id: oracle_comparison\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_ppl: 10.9131\n    max_oracle_gap_ppl: 0.0183\n    avg_oracle_gap_ppl: 0.0046\n    layers_mckp_optimal: 5/8\n    layers_with_gap: 3\n    gap_layers:\n      L1: 0.0183\n      L4: 0.0045\n      L11: 0.0136\n    gap_nature: 2-bit head position swap within same bit budget\n    total_evals: 54\n    runtime_min: 21.3\n- id: plan_010\n  claim:\n  - 2\n  description: 'Cross-domain calibration robustness: calibrate on C4, evaluate on\n    WikiText-2 (and vice versa). Report per-head allocation agreement rate across\n    calibration sources.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_007\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: plan_011\n  claim:\n  - 1\n  description: 'Head sensitivity visualization: generate paper-quality figures showing\n    per-head profiling delta heatmap across layers, compounding effect curve, and\n    budget allocation comparison chart.\n\n    '\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_004\n  - plan_006\n  registry_id: head_sensitivity_viz\n  status: DONE\n  conclusion: success\n- id: plan_014\n  claim:\n  - 2\n  description: 'K/V separation: treat K and V heads as independent MCKP items with\n    separate budget allocation. Compare joint K+V optimization vs current uniform\n    K=V approach. RateQuant supports asymmetric K/V (e.g. K=2.85, V=2.15 avg bits)\n    — we should show MCKP naturally handles this.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: kv_separation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    kv_sep_ppl: 11.2162\n    joint_kv_ppl: 10.9131\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_sep_vs_joint: 0.303\n    sep_k_2bit_count: 16\n    sep_v_uniform_4bit: true\n    kv_asymmetric_heads: 21\n- id: plan_012\n  claim:\n  - 1\n  - 2\n  description: 'Downstream task evaluation: ARC-C / HellaSwag / PIQA / WinoGrande\n    on Qwen2.5-7B at 4× compression. Must match RateQuant''s eval suite for direct\n    comparison. Tests whether PPL improvements translate to downstream performance.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  registry_id: downstream_eval_qwen\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    avg_recovery: 0.728\n    arc_c: 0.5137\n    hellaswag: 0.7684\n    piqa: 0.7786\n    winogrande: 0.6819\n    arc_c_delta_pp: 3.16\n    hellaswag_delta_pp: 4\n    piqa_delta_pp: 1.25\n    winogrande_delta_pp: 1.97\n- id: plan_013\n  claim:\n  - 1\n  description: '70B profiling-only: run distortion profiling on Qwen2.5-72B (no full\n    eval). Analyze whether sensitivity patterns (Layer 0 dominance, compounding threshold)\n    scale with model size.\n\n    '\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: qwen72b_profiling\n  model: Qwen2.5-72B\n  status: DONE\n  conclusion: killed\n- id: plan_015\n  claim:\n  - 2\n  description: 'L0-only heuristic baseline: assign 8-bit to all Layer 0 KV heads,\n    uniform 4-bit to all other heads, at 4x compression on Qwen2.5-7B. This is the\n    simplest possible non-uniform strategy exploiting L0 sensitivity. If L0-only matches\n    or beats constrained MCKP, the full optimization machinery is unnecessary. Must\n    also test on Llama and Mistral. Critical missing baseline flagged by Dream review.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: l0_only_heuristic\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: killed\n- id: plan_016\n  claim:\n  - 2\n  description: 'RateQuant greedy + cardinality constraint ablation: add max_2bit=k\n    constraint to RateQuant greedy Algorithm 1 on {2,4,8,16}. Compare three conditions:\n    (a) RateQuant greedy unconstrained (already have: PPL ~32.45), (b) RateQuant greedy\n    + cardinality k=8, (c) constrained MCKP k=8 (already have: PPL ~11.23). If (b)\n    matches (c), the contribution is the cardinality constraint, not the MCKP solver.\n    If (c) beats (b), discrete MCKP optimization genuinely matters. Critical ablation\n    flagged by all three Dream review tiers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_008\n  registry_id: greedy_cardinality_ablation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 11.2312\n    greedy_unconstrained_ppl: 32.4467\n    mckp_constrained_ppl: 11.23\n    delta_vs_mckp: 0.0012\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n- id: plan_017\n  claim:\n  - 1\n  - 2\n  description: 'Multi-seed error bars: run constrained MCKP and uniform 4-bit on Qwen2.5-7B\n    at 4x compression with 3 different calibration sets (different random subsets\n    of WikiText-2 training data). Report mean +/- std for PPL. Required for statistical\n    credibility — Dream review flagged all-single-run as critical gap.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: multi_seed_error_bars\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4454\n    mckp_seed0: 11.0168\n    mckp_seed1: 10.8981\n    mckp_seed2: 11.0487\n    mckp_mean: 10.9878\n    mckp_std: 0.0648\n    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4\n    allocation_agreement_3way: 0.902\n    agreement_s0_s1: 0.946\n    agreement_s0_s2: 0.911\n    agreement_s1_s2: 0.946\n    profile_time_min_per_seed: 65\n- id: plan_018\n  claim:\n  - 2\n  description: 'Runtime/latency benchmark: measure end-to-end inference latency and\n    throughput with mixed-precision KV cache vs uniform 4-bit quantization on Qwen2.5-7B.\n    Include profiling cost breakdown. Dream review flagged missing latency evaluation\n    as significant gap for systems-oriented contribution.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: runtime_benchmark\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16:\n      prefill_ms: 45.86\n      decode_ms_per_tok: 33.78\n      throughput_tok_s: 29.6\n    uniform_4bit:\n      prefill_ms: 54.25\n      decode_ms_per_tok: 42.46\n      throughput_tok_s: 23.6\n    constrained_mckp:\n      prefill_ms: 57.03\n      decode_ms_per_tok: 46.09\n      throughput_tok_s: 21.8\n      mckp_solver_sec: 0.005\n      bit_dist:\n        '2': 8\n        '4': 100\n        '8': 4\n      memory_ratio: 0.25\n    theoretical_memory:\n      bf16_MB: 21\n      4bit_MB: 5.25\n      mckp_MB: 5.25\n      compression_4x: true\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp_004\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p0_2_cliff_1.5B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: p0_2_cliff_7B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: p0_1_ppl_fast\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_a_targeted_hybrid\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_b_hires_quant\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_c_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_c_no2bit\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl: 15.4454\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_vs_uniform: 0\n    memory_ratio: 0.25\n    bit_distribution:\n      '4': 112\n- exp_id: exp_d_no_l0_exclusion\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_e_hires_profile\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    constrained_ppl_bf16: 9.569\n    baseline_ppl_bf16: 8.819\n    exp_c_ppl_bf16: 11.345\n    delta_vs_exp_c: -1.776\n    memory_ratio: 0.25\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    profile_resolution:\n      hires_nonzero_2bit: 100\n      lowres_nonzero_2bit: 37\n      hires_nonzero_4bit: 6\n      lowres_nonzero_4bit: 4\n      total_heads: 112\n    allocation_diff_count: 8\n    profiling_time_min: 65.5\n- exp_id: compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: compounding_sweep_k10_12\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: ratequant_greedy_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: budget_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: c4_cross_dataset_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    c4_mckp_ppl: 11.3285\n    uniform4bit_ppl: 15.4454\n    delta_over_uniform: 4.117\n    allocation_agreement_rate: 0.982\n    n_disagree: 2\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n    wt2_ref_mckp_ppl: 11.2312\n    wt2_ref_delta: 4.2142\n    ppl_gap: 0.097\n- exp_id: llama_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 8.7\n    uniform_4bit_ppl_bf16: 8.47\n    baseline_ppl_bf16: 8.09\n    delta_vs_uniform: -0.23\n    memory_ratio: 0.25\n- exp_id: mistral_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 7.564\n    uniform_4bit_ppl_bf16: 7.131\n    baseline_ppl_bf16: 7.035\n    delta_vs_uniform: -0.433\n    memory_ratio: 0.25\n- exp_id: llama_hires_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 8.0918\n    uniform_4bit_ppl: 8.469\n    lowres_mckp_ppl: 8.6951\n    hires_mckp_ppl: 8.4498\n    hires_improvement_ppl: 0.2453\n    degradation_reduction_pct: 40.7\n    profiling_time_min: 173.4\n    total_time_min: 175.1\n- exp_id: mistral_hires_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl: 7.323\n    uniform_4bit_ppl: 7.131\n    baseline_ppl: 7.035\n    delta_vs_uniform: -0.192\n    memory_ratio: 0.25\n- exp_id: llama_aggressive_compression\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_5.3x_ppl: 57.6\n    uniform_2bit_ppl: 2643.77\n    mckp_8x_ppl: 2372.33\n    uniform_2bit_8x_ppl: 2643.77\n- exp_id: downstream_eval_qwen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    avg_recovery: 0.728\n    arc_c: 0.5137\n    hellaswag: 0.7684\n    piqa: 0.7786\n    winogrande: 0.6819\n    arc_c_delta_pp: 3.16\n    hellaswag_delta_pp: 4\n    piqa_delta_pp: 1.25\n    winogrande_delta_pp: 1.97\n- exp_id: head_sensitivity_viz\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mistral_aggressive_compression\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_5.3x_ppl: 11.912\n    uniform_2bit_ppl: 519.107\n    mckp_8x_ppl: 399.901\n    uniform_2bit_8x_ppl: 519.107\n    baseline_ppl: 7.035\n    uniform_4bit_ppl: 7.131\n    5.3x_bit_dist:\n      '2': 128\n      '4': 128\n    8x_bit_dist:\n      '2': 248\n      '4': 8\n    total_time_seconds: 268.1\n- exp_id: kv_separation\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    kv_sep_ppl: 11.2162\n    joint_kv_ppl: 10.9131\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_sep_vs_joint: 0.303\n    sep_k_2bit_count: 16\n    sep_v_uniform_4bit: true\n    kv_asymmetric_heads: 21\n- exp_id: l0_only_heuristic\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: greedy_cardinality_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 11.2312\n    greedy_unconstrained_ppl: 32.4467\n    mckp_constrained_ppl: 11.23\n    delta_vs_mckp: 0.0012\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n- exp_id: l0_heuristic_baseline\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: greedy_constrained_ablation\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: l0_heuristic_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_constrained_ppl: 11.23\n    l0_random_mean_ppl: 11.69\n    l0_random_std: 0.47\n    naive_positional_ppl: 12.23\n    uniform_4bit_ppl: 15.45\n    qwen_l0_random_median: 11.515\n    qwen_l0_random_seeds:\n    - 11.486\n    - 11.615\n    - 11.325\n    - 11.515\n    - 12.515\n    llama_l0_random_mean: 10.479\n    llama_l0_random_std: 1.033\n    llama_l0_random_median: 10.038\n    llama_l0_random_seeds:\n    - 9.485\n    - 10.488\n    - 9.941\n    - 10.038\n    - 12.444\n    llama_naive_positional: 9.941\n    llama_mckp: 8.4498\n    llama_uniform: 8.469\n    mistral_l0_random_mean: 7.56\n    mistral_l0_random_std: 0.087\n    mistral_l0_random_median: 7.586\n    mistral_l0_random_seeds:\n    - 7.523\n    - 7.61\n    - 7.413\n    - 7.586\n    - 7.669\n    mistral_naive_positional: 7.481\n    mistral_mckp: 7.3106\n    mistral_uniform: 7.131\n- exp_id: qwen_bf16_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 9.8106\n    baseline_fp16_ppl: 9.81\n    delta_baseline: 0.0006\n    uniform4_bf16_ppl: 15.4454\n    uniform4_fp16_ppl: 15.45\n    delta_uniform4: 0.0046\n- exp_id: hires_mckp_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl_bf16: 9.8106\n    mckp_ppl_bf16: 10.9131\n    uniform_4bit_ppl_bf16: 15.4454\n    delta_mckp_vs_baseline: 1.1025\n    delta_mckp_vs_uniform: -4.5323\n    token_count: 298938\n- exp_id: hires_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 9.8106\n    uniform_4bit_bf16_ppl: 15.4454\n    hires_mckp_bf16_ppl: 10.9131\n- exp_id: mistral_k_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 4\n    best_ppl: 7.1648\n    uniform_4bit_ppl: 7.131\n    k4_ppl: 7.1648\n    k8_ppl: 7.1997\n    k12_ppl: 7.2448\n    k16_ppl: 7.3106\n    k18_ppl: 7.3231\n- exp_id: llama_k_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 4\n    best_ppl: 8.4498\n    uniform_4bit_ppl: 8.469\n    k4_ppl: 8.4498\n    k8_ppl: 8.4498\n    k12_ppl: 8.4498\n    k16_ppl: 8.4498\n    k18_ppl: 8.4498\n    natural_2bit_count: 2\n- exp_id: multi_seed_error_bars\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4454\n    mckp_seed0: 11.0168\n    mckp_seed1: 10.8981\n    mckp_seed2: 11.0487\n    mckp_mean: 10.9878\n    mckp_std: 0.0648\n    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4\n    allocation_agreement_3way: 0.902\n    agreement_s0_s1: 0.946\n    agreement_s0_s2: 0.911\n    agreement_s1_s2: 0.946\n    profile_time_min_per_seed: 65\n- exp_id: cross_domain_calibration\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c4_cross_dataset_eval_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cross_domain_calibration_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: runtime_benchmark\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16:\n      prefill_ms: 45.86\n      decode_ms_per_tok: 33.78\n      throughput_tok_s: 29.6\n    uniform_4bit:\n      prefill_ms: 54.25\n      decode_ms_per_tok: 42.46\n      throughput_tok_s: 23.6\n    constrained_mckp:\n      prefill_ms: 57.03\n      decode_ms_per_tok: 46.09\n      throughput_tok_s: 21.8\n      mckp_solver_sec: 0.005\n      bit_dist:\n        '2': 8\n        '4': 100\n        '8': 4\n      memory_ratio: 0.25\n    theoretical_memory:\n      bf16_MB: 21\n      4bit_MB: 5.25\n      mckp_MB: 5.25\n      compression_4x: true\n- exp_id: c4_rerun_d032\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_cal_wt2_eval_mckp_ppl: 11.2942\n    c4_cal_wt2_eval_uniform_ppl: 15.4454\n    c4_cal_wt2_eval_delta: 4.1512\n    c4_cal_bf16_baseline: 12.6505\n    wt2_bf16_baseline: 9.8106\n    allocation_agreement_c4_vs_wt2: 0.964\n    agreement_heads: 108/112\n    bit_dist: 2bit:8, 4bit:100, 8bit:4\n    cross_domain_wt2_to_c4_mckp_ppl: 20.5601\n    cross_domain_wt2_to_c4_uniform_ppl: 35.4232\n    cross_domain_c4_bf16: 15.3246\n    old_contaminated_ppl: 11.3285\n    contamination_impact: 0.0343\n    models_completed: Qwen2.5-7B only\n- exp_id: multi_seed_lowres\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: oracle_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_ppl: 10.9131\n    max_oracle_gap_ppl: 0.0183\n    avg_oracle_gap_ppl: 0.0046\n    layers_mckp_optimal: 5/8\n    layers_with_gap: 3\n    gap_layers:\n      L1: 0.0183\n      L4: 0.0045\n      L11: 0.0136\n    gap_nature: 2-bit head position swap within same bit budget\n    total_evals: 54\n    runtime_min: 21.3\n- exp_id: plan_009_oracle_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: qwen72b_profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: llama_heuristic_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    l0_random_seeds:\n    - 8.5479\n    - 8.7595\n    - 8.624\n    - 8.5721\n    - 8.6192\n    l0_random_mean: 8.6245\n    l0_random_std: 0.0733\n    l0_random_median: 8.6192\n    naive_positional_ppl: 8.5781\n    mckp_ppl: 8.4498\n    uniform_ppl: 8.469\n    baseline_ppl: 8.0918\n    mckp_vs_l0_random_gap: 0.1747\n    mckp_vs_naive_gap: 0.1283\n- exp_id: mistral_heuristic_k4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 7.0351\n    uniform_4bit_ppl: 7.1314\n    mckp_k4_ppl: 7.1648\n    l0_random_seed_0: 7.1882\n    l0_random_seed_1: 7.1995\n    l0_random_seed_2: 7.1723\n    l0_random_seed_3: 7.3577\n    l0_random_seed_4: 7.2875\n    l0_random_mean: 7.2411\n    l0_random_std: 0.0707\n    l0_random_median: 7.1995\n    naive_heuristic_ppl: 7.2105\n    budget_heuristic: 0.2559\n    budget_mckp_k4: 0.248\n- exp_id: llama_c4_cross_dataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wt2_cal_wt2_ppl: 8.4498\n    c4_cal_wt2_ppl: 8.6459\n    uniform_wt2_ppl: 8.469\n    wt2_cal_c4_ppl: 7.654\n    c4_cal_c4_ppl: 7.654\n    uniform_c4_ppl: 7.5351\n    bf16_wt2_ppl: 8.0918\n    bf16_c4_ppl: 7.1333\n    agreement_rate: 0.977\n    agreement_heads: 250/256\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n- exp_id: mistral_c4_cross_dataset\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bf16_wt2_ppl: 7.0351\n    c4_cal_bf16_ppl: 6.9677\n    wt2_cal_mckp_wt2_ppl: 7.1648\n    c4_cal_mckp_wt2_ppl: 7.1859\n    uniform_4bit_wt2_ppl: 7.1314\n    delta_uniform_mckp_wt2_cal: -0.0334\n    delta_uniform_mckp_c4_cal: -0.0546\n    allocation_agreement_c4_vs_wt2: 0.965\n    agreement_heads: 247/256\n    bit_dist_wt2_cal: 2bit:4, 4bit:252\n    bit_dist_c4_cal: 2bit:4, 4bit:251, 8bit:1\n    profile_time_s: 407.7\n    eval_time_s: 349.4\n    total_time_s: 757.1\n- exp_id: gemma2_9b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 8.9\n    mckp_wikitext2_ppl: 9.05\n    uniform4bit_wikitext2_ppl: 9.03\n    mckp_improvement_over_uniform: -0.02\n    top5_concentration: 0.23\n    layer0_dominance_ratio: 1.32\n    best_k: 8\n    best_k_ppl: 9.05\n    verdict: FAIL\n- exp_id: yi15_9b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 7.0157\n    mckp_wikitext2_ppl: 7.3129\n    uniform4bit_wikitext2_ppl: 7.2171\n    mckp_improvement_over_uniform: -0.0958\n    top5_concentration: 0.4934\n    layer0_dominance_ratio: 0.07\n    best_k: 2\n    best_k_ppl: 7.2209\n    gqa_ratio: '8:1'\n    verdict: FAIL\n- exp_id: qwen25-hires-profiling\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_hires_float32_d048\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    float32_hires_top5_concentration: 0.6104\n    bf16_hires_range: 0.59-0.66\n    float32_lowres_concentration: 0.42\n    bf16_bug_impact_on_concentration: 0.01\n    baseline_ppl: 9.81\n    mckp_unconstrained_ppl: 10.95\n    uniform_4bit_ppl: 15.45\n    mckp_bit_dist:\n      '2': 12\n      '4': 96\n      '8': 3\n      '16': 1\n    l0h0_delta: 6.7388\n    l0_4heads_total_share: 0.586\n    claim3_threshold_0.50: PASS\n- exp_id: yi15_hires_float32_profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: yi15_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.7139\n    top5_n_heads: 9\n    baseline_calibration_ppl: 5.888\n    delta_2bit_cv: 8.8991\n    layer0_dominance_ratio: 0.04\n    top1_head: L4H3_delta=13.1236\n    total_hours: 0.96\n- exp_id: qwen_hires_constrained_d049\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    float32_hires_constrained_mckp_ppl: 10.8921\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4484\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    gap_recovery_pct: 80.8\n    top5_concentration: 0.6156\n    top5_concentration_pre_monotonicity: 0.6104\n    bf16_hires_constrained_mckp_ppl: 10.9131\n    delta_f32_vs_bf16: 0.021\n- exp_id: yi15_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hires_mckp_ppl: 7.2181\n    uniform_4bit_ppl: 7.2171\n    baseline_ppl: 7.0157\n    delta_vs_uniform: -0.001\n    bit_distribution:\n      '2': 2\n      '4': 189\n      '8': 1\n    2bit_heads:\n    - L22H1\n    - L24H3\n    8bit_heads:\n    - L6H2\n    L4H3_status: kept_at_4bit\n    std_mckp_k2_ppl: 7.2209\n    std_mckp_k8_ppl: 7.3129\n    hires_concentration: 0.7139\n    L4H3_2bit_delta: 13.12\n    L4H3_4bit_delta: 0.0048\n    L4H3_8bit_delta: 0.004\n- exp_id: llama_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.5749\n    t1_t5: 0.85\n    baseline_ppl: 6.5055\n    top1_head: L2H5_delta=15.2636\n    delta_2bit_cv: 7.7663\n    l0_dominance_ratio: 0.67\n    positive_delta_heads: 254\n    total_heads: 256\n    total_hours: 0.98\n- exp_id: mistral_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: 'ValueError: Unrecognized model - config.json missing model_type field\n      at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3'\n- exp_id: mistral_hires_bf16_2bitonly_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: 'SafetensorError: model-00003-of-00003.safetensors missing, incomplete\n      download'\n- exp_id: mistral_hires_bf16_2bitonly_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: mistral_hires_bf16_2bitonly_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.241\n    top5_n_heads: 12\n    baseline_ppl: 5.8702\n    top1_head: L2H5\n    top1_delta_2bit: 0.3236\n    top2_head: L12H1\n    top2_delta_2bit: 0.1435\n    top3_head: L0H7\n    top3_delta_2bit: 0.1403\n    delta_2bit_mean: 0.020073\n    delta_2bit_std: 0.026278\n    delta_2bit_cv: 1.3091\n    layer0_mean_delta_2bit: 0.034073\n    other_layers_mean_delta_2bit: 0.019621\n    l0_dominance_ratio: 1.74\n    positive_delta_heads: 252\n    total_heads: 256\n    distribution_shape: flat\n    total_hours: 0.94\n    profile_seconds: 3371.7\n- exp_id: llama_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_bf16_ppl: 8.0922\n    hires_mckp_ppl: 8.5042\n    uniform_4bit_ppl: 8.4701\n    std_mckp_reference_ppl: 8.4498\n    mckp_vs_uniform_delta: -0.0341\n    mckp_vs_uniform_pct: -9\n    hires_vs_std_mckp_delta: 0.0544\n    concentration: 0.5749\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n    heads_2bit:\n    - 26,0\n    - 31,7\n    heads_8bit:\n    - 12,3\n    verdict: FAIL\n- exp_id: gemma2_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    concentration_top5pct: 0.2291\n    l0_dominance_ratio: 2.05\n    cv_delta_2bit: 1.2834\n    positive_delta_heads: 310/336\n    top_head: L0H1 delta=0.1906\n    total_time_hours: 1.59\n- exp_id: llama_c4_hires_crossdataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_wt2_ppl: 8.0922\n    bf16_c4_ppl: 7.1333\n    c4_cal_mckp_wt2_ppl: 8.5103\n    c4_cal_mckp_c4_ppl: 7.5351\n    uniform_wt2_ppl: 8.4701\n    uniform_c4_ppl: 7.5351\n    delta_c4_uniform_minus_mckp: 0\n    delta_wt2_uniform_minus_mckp: -0.0402\n    verdict_c4: FAIL\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n    heads_2bit:\n    - 2,3\n    - 24,2\n    heads_8bit:\n    - 31,6\n    total_time_min: 6.3\n    wt2_ref_mckp_ppl: 8.5042\n    wt2_ref_delta: -0.0341\n- exp_id: mistral_c4_hires_crossdataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fp16_ppl: 7.0352\n    c4_mckp_ppl: 7.1774\n    uniform_4bit_ppl: 7.1308\n    mckp_vs_uniform_delta: 0.0466\n    mckp_bit_distribution:\n      '2': 4\n      '4': 250\n      '8': 2\n    phase4_error: 'FileNotFoundError: mistral_k_ablation_results.json'\n- exp_id: w2_unconstrained_baselines\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    note: 2bitonly profiles only - INVALID for reviewer response\n    yi15_ppl: 672.2\n    yi15_ratio: 114\n    llama_ppl: 1219.7\n    llama_ratio: 187\n    mistral_ppl_2bitonly: 47.8\n    mistral_ratio_2bitonly: 8.2\n    mistral_ppl_full: 6.39\n    mistral_ratio_full: 1.09\n    gemma2_ppl: 277.4\n    gemma2_ratio: 37.9\n    budget: 0.25\n    baseline_yi: 5.89\n    baseline_llama: 6.51\n    baseline_mistral: 5.87\n    baseline_gemma2: 7.32\n- exp_id: w9_compounding_scaling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    baseline_ppl: 8.2\n    n1_joint_ppl: 14.94\n    n1_ratio: 1\n    n2_joint_ppl: 42.26\n    n2_ratio: 3.84\n    n4_joint_ppl: 3813.76\n    n4_ratio: 333.3\n    n8_joint_ppl: 3586.42\n    n8_ratio: 282.1\n    n16_joint_ppl: 7286.23\n    n16_ratio: 521.1\n    n32_joint_ppl: 6644.05\n    n32_ratio: 424\n    n64_joint_ppl: 9453.33\n    n64_ratio: 533.3\n    runtime_seconds: 96\n- exp_id: w9_compounding_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.81\n    k1_topk_ppl: 9.826\n    k1_randomk_ppl: 9.887\n    k1_randomk_std: 0.05\n    k4_topk_ppl: 9.849\n    k4_topk_ratio: 0.86\n    k4_randomk_ppl: 10.06\n    k4_randomk_std: 0.06\n    k4_randomk_ratio: 1.24\n    k8_topk_ppl: 10.042\n    k8_topk_ratio: 1.56\n    k8_randomk_ppl: 11.07\n    k8_randomk_std: 0.69\n    k8_randomk_ratio: 1.76\n    k16_topk_ppl: 10.42\n    k16_topk_ratio: 1.56\n    k16_randomk_ppl: 12.91\n    k16_randomk_std: 0.4\n    k16_randomk_ratio: 2.1\n    k32_topk_ppl: 11.604\n    k32_topk_ratio: 1.78\n    k32_randomk_ppl: 18.33\n    k32_randomk_std: 2.53\n    k32_randomk_ratio: 2.73\n    k64_topk_ppl: 22.946\n    k64_topk_ratio: 4.89\n    k64_randomk_ppl: 55.94\n    k64_randomk_std: 9.73\n    k64_randomk_ratio: 8.88\n    runtime_minutes: 16.9\n    note: 'v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking,\n      top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。'\n- exp_id: w2_unconstrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi15_baseline: 7.0157\n    yi15_uniform4: 7.2171\n    yi15_greedy: 7.5615\n    yi15_mckp: 7.5615\n    yi15_n2bit: 22\n    llama_baseline: 8.0922\n    llama_uniform4: 8.4701\n    llama_greedy: 8.6265\n    llama_mckp: 8.6265\n    llama_n2bit: 12\n    mistral_baseline: 7.0352\n    mistral_uniform4: 7.1308\n    mistral_greedy: 7.5733\n    mistral_mckp: 7.5963\n    mistral_n2bit: 42\n    gemma2_baseline: 6.0306\n    gemma2_uniform4: 6.1683\n    gemma2_greedy: 8.8469\n    gemma2_mckp: 8.8469\n    gemma2_n2bit: 106\n    gemma2_eval_method: sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\n    gemma2_greedy_ratio: 1.467\n    gemma2_catastrophic: true\n    gemma2_note: 1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal\n      value\n- exp_id: w3_downstream_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi15_baseline_avg: 0.6912\n    yi15_uniform_avg: 0.6822\n    yi15_mckp_avg: 0.6745\n    yi15_mckp_vs_uniform_pp: -0.77\n    yi15_mckp_vs_baseline_pp: -1.67\n    yi15_baseline:\n      arc_easy: 0.8093\n      arc_challenge: 0.5265\n      hellaswag: 0.5913\n      piqa: 0.7949\n      winogrande: 0.734\n    yi15_uniform:\n      arc_easy: 0.7946\n      arc_challenge: 0.5205\n      hellaswag: 0.5857\n      piqa: 0.7927\n      winogrande: 0.7174\n    yi15_mckp:\n      arc_easy: 0.7854\n      arc_challenge: 0.4881\n      hellaswag: 0.5797\n      piqa: 0.7894\n      winogrande: 0.7301\n    llama_baseline_avg: 0.696\n    llama_uniform_avg: 0.6915\n    llama_mckp_avg: 0.6816\n    llama_mckp_vs_uniform_pp: -0.99\n    llama_mckp_vs_baseline_pp: -1.44\n    llama_baseline:\n      arc_easy: 0.8228\n      arc_challenge: 0.5188\n      hellaswag: 0.6073\n      piqa: 0.7922\n      winogrande: 0.7388\n    llama_uniform:\n      arc_easy: 0.8173\n      arc_challenge: 0.5256\n      hellaswag: 0.6026\n      piqa: 0.7867\n      winogrande: 0.7253\n    llama_mckp:\n      arc_easy: 0.8039\n      arc_challenge: 0.4991\n      hellaswag: 0.6012\n      piqa: 0.7802\n      winogrande: 0.7238\n    mistral_baseline_avg: 0.6917\n    mistral_uniform_avg: 0.6894\n    mistral_mckp_avg: 0.6846\n    mistral_mckp_vs_uniform_pp: -0.48\n    mistral_mckp_vs_baseline_pp: -0.71\n    mistral_baseline:\n      arc_easy: 0.8005\n      arc_challenge: 0.5043\n      hellaswag: 0.6118\n      piqa: 0.8009\n      winogrande: 0.7411\n    mistral_uniform:\n      arc_easy: 0.7976\n      arc_challenge: 0.5068\n      hellaswag: 0.6051\n      piqa: 0.7982\n      winogrande: 0.7395\n    mistral_mckp:\n      arc_easy: 0.7942\n      arc_challenge: 0.4949\n      hellaswag: 0.6027\n      piqa: 0.802\n      winogrande: 0.7293\n    gemma2_baseline_avg: 0.7307\n    gemma2_uniform_avg: 0.7251\n    gemma2_mckp_avg: 0.7265\n    gemma2_mckp_vs_uniform_pp: 0.14\n    gemma2_mckp_vs_baseline_pp: -0.42\n    gemma2_baseline:\n      arc_easy: 0.8737\n      arc_challenge: 0.6135\n      hellaswag: 0.6093\n      piqa: 0.8128\n      winogrande: 0.7443\n    gemma2_uniform:\n      arc_easy: 0.8662\n      arc_challenge: 0.6058\n      hellaswag: 0.606\n      piqa: 0.8079\n      winogrande: 0.7395\n    gemma2_mckp:\n      arc_easy: 0.8649\n      arc_challenge: 0.6041\n      hellaswag: 0.6089\n      piqa: 0.8074\n      winogrande: 0.7474\n    eval_harness_version: 0.4.11\n    num_fewshot: 0\n    yi_elapsed_s: 1563.2\n    llama_elapsed_s: 1446.4\n    mistral_elapsed_s: 1302.2\n    gemma2_elapsed_s: 1735.9\n- exp_id: gemma2_constrained_bos_fix\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: w1_qwen14b_hires_profiling\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T09:10:57.036Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T09:10:57.036Z",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-15T09:10:57.057Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Qwen2.5-14B 边界/弱阳性，N 实质仍为 1；其余数据基本一致但有小幅偏差需要对齐
核心假设：['Qwen2.5-14B concentration 0.40-0.55 或 t₁/t₅ 0.65-0.80（边界区间，不完全满足 joint condition）', 'Qwen2.5-14B MCKP 改善 3-15%（有正向信号但不如 Qwen-7B 显著）', 'Decision rule 5/6 或 6/6 但 14B 是 borderline case 需要特殊讨论', 'Gemma-2 BOS fix 后 unconstrained ratio 在 1.30-1.55 范围，可能需要微调数字', 'W9 compounding 趋势成立但 variance 大，形式化为 observation 而非 proposition']
关键指标范围：{'qwen14b_mckp_improvement_over_uniform_pct': [3, 15], 'qwen14b_concentration': [0.4, 0.55], 'qwen14b_t1_t5': [0.55, 0.8], 'decision_rule_accuracy': [5, 6], 'gemma2_constrained_vs_uniform_pct': [-1.0, 1.0], 'gemma2_unconstrained_ratio': [1.3, 1.55], 'w9_k64_randomk_topk_ratio': [1.5, 2.5]}
叙事方向：Claim 3 保持 "empirical decision rule"（不升级）。14B 作为 "boundary case"  单独一段讨论：说明 threshold 是 soft boundary 而非 hard cutoff， 符合 empirical nature。如果 5/6，承认 rule 是 directional heuristic， 在 Limitation 明确写 "N=1 confirmed Spread; larger-scale validation needed"。 三档标签仍可用但需要把 threshold 描述软化 （"approximately 0.50" → "in the range 0.45-0.55"）。 Gemma-2 段落可能需微调具体数字但 "moderate degradation + universal constraint value"  叙事不变。W9 super-additive 降为 empirical observation（图 + 描述性文字）， 不写 formal proposition。整体仍可投 EMNLP Main，但 contribution 重心 从 "diagnostic" 向 "constraint as universal fix" 倾斜。补充实验： 考虑加 Qwen2.5-3B 或 Qwen2.5-32B 碰运气找第二个 Spread 样本。


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
tier: median
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
  "promptId": "26618dbe-32d3-4d36-8678-6c78804f25da",
  "type": "user",
  "uuid": "f7d6746a-fb67-4a68-af99-db3058665dca",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T09:10:57.055Z_

```json
{
  "parentUuid": "f7d6746a-fb67-4a68-af99-db3058665dca",
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
  "uuid": "2b3f2497-8cfd-4741-82e6-f3b849f75c77",
  "timestamp": "2026-05-15T09:10:57.055Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T09:10:57.056Z_

```json
{
  "parentUuid": "2b3f2497-8cfd-4741-82e6-f3b849f75c77",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1b36d576-c690-403e-8cae-0e721f042137",
  "timestamp": "2026-05-15T09:10:57.056Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Qwen2.5-14B 边界/弱阳性，N 实质仍为 1；其余数据基本一致但有小幅偏差需要对齐 核心假设：['Qwen2.5-14B concentration 0.40-0.55 或 t₁/t₅ 0.65-0.80（边界区间，不完全满足 joint condition）', 'Qwen2.5-14B MC…",
  "leafUuid": "1b36d576-c690-403e-8cae-0e721f042137",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Concentration-dependent KV cache quantization across five model architectures",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---

### Assistant

_source line 8 · 2026-05-15T09:20:14.077Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each "planned" experiment in the experiment_plan, under the "median" tier definition they've provided.

Let me identify which experiments are still in "planned" or "RUNNING" status:

Looking at the registry and experiment_plan:
1. `gemma2_constrained_bos_fix` - RUNNING
2. `w1_qwen14b_hires_profiling` - RUNNING

But the user said "对 experiment_plan 中每个 planned 实验展开详细数据". Let me re-read the experiment_plan more carefully.


Actually, I'm checking the experiment_plan list and noticing that all experiments have either `status: DONE` or `status: PREPARING` with conclusions like killed or success. The two RUNNING experiments in the registry—`gemma2_constrained_bos_fix` and `w1_qwen14b_hires_profiling`—aren't actually in the experiment_plan itself. I need to clarify whether the user wants me to predict results for the RUNNING experiments in the registry or if they're referring to something else in the experiment_plan. But all experiments in the experiment_plan have status DONE. 

Hmm, but the experiment_plan only lists plan_001 through plan_018 (with some gaps like plan_013 killed, plan_015 killed). All are marked DONE.

But there are RUNNING experiments in the registry:
- `gemma2_constrained_bos_fix` 
- `w1_qwen14b_hires_profiling`

And looking at the median tier definition, it mentions:
- Qwen2.5-14B concentration 0.40-0.55 (borderline)
- Qwen2.5-14B MCKP improvement 3-15%
- Gemma-2 BOS fix results
- W9 compounding trends

So the "planned" experiments are likely the RUNNING ones plus potentially any others that haven't been completed yet. The narrative guidance points to several experiments in progress: the Gemma-2 constrained evaluation with the BOS fix and the Qwen2.5-14B profiling work, along with what looks like additional planned evaluations for the 14B model including constrained MCKP, downstream tasks, and k ablation studies. I'm mapping out the remaining experiments needed to validate the median tier narrative for Qwen2.5-14B, which should show concentration around 0.40-0.55 with modest MCKP improvements and specific performance ratios. The pipeline includes the currently running profiling and BOS fix experiments, followed by constrained evaluation, ablation studies, and downstream validation across the model family.

Now I'm working through the architectural details for Qwen2.5-14B to ground my predictions—it has 48 layers with 40 attention heads and 8 key-value heads per layer, which shapes how the concentration and compounding effects should manifest. Looking at Qwen2.5-14B as a median case, the metrics suggest it's right on the boundary—concentration around 0.40-0.55 and t₁/t₅ ratio between 0.65-0.80 don't clearly fit either pattern, with MCKP showing only modest 3-15% improvement over uniform. Now I'm working through the Gemma-2 BOS fix scenario, where the constrained MCKP should land close to the uniform baseline around 6.15-6.20, with an unconstrained ratio somewhere in the 1.30-1.55 range.

I'm realizing the w2_unconstrained_v2 data already includes the BOS fix evaluation, so that 1.47× ratio I'm seeing is already accounting for it. The constrained_bos_fix run is specifically about applying constrained MCKP under that same BOS-fixed evaluation method, which means I need to reference the existing pipeline data rather than recalculate.

Looking at the numbers, the BOS-fixed baseline sits at 6.03, uniform at 6.17, and constrained MCKP should land somewhere around 6.15-6.20 given that Gemma-2 has a relatively flat distribution. Now I'm mapping out which experiments I need to predict, starting with the Qwen 14B high-resolution profiling run. I'm estimating the Qwen2.5-14B profiling metrics now—concentration around 0.48 and t₁/t₅ at 0.72, which puts it right at the boundary between Spread and Spike patterns. Since it's the same family as the 7B but with more layers and parameters, the sensitivity is likely more distributed across the additional KV heads, diluting the sharp L0 clustering effect I'd see in smaller models.

For MCKP, this borderline concentration should yield a modest improvement of around 8% over uniform, and unconstrained degradation would probably land somewhere between the 7B's 3.31× and Yi's 1.08×—maybe around 1.5-2.0× baseline.

Now I'm checking whether the 14B model actually satisfies the decision rule. With concentration around 0.47-0.48 and t₁/t₅ at 0.72, it technically fails the joint condition, but MCKP still shows 3-15% improvement, which suggests the rule predicts 5 out of 6 correctly—or possibly 6 out of 6 if I relax the thresholds slightly to account for measurement uncertainty.

For the remaining parameters, I'm settling on specific values within their observed ranges: 8% for MCKP improvement, -0.3% for Gemma2's constrained performance, 2.0 for the W9 K64 ratio. Now I need to look more carefully at the Qwen2.5-14B architecture itself to understand what's driving these metrics.

The Qwen2.5-14B model has 48 layers with 40 attention heads and 8 KV heads per layer, giving 384 total KV heads. With a 5:1 GQA ratio, the top 19 heads represent about 47% of sensitivity—just under the 0.50 threshold. For Gemma-2 with the BOS fix, the constrained MCKP approach yields around 6.15-6.20 compared to the uniform baseline of 6.1683, which is a modest improvement.

Now I'm organizing the full experiment set. The explicit plan covers plan_001 through plan_018, all completed. But there are additional experiments to account for: the full Qwen2.5-14B pipeline starting with profiling, the Gemma-2 constrained variant with the BOS fix, and potentially Qwen2.5-3B or 32B models to search for another Spread sample. I need to think through what naturally follows from these experiments. I'm trying to figure out what the user actually wants—whether they're asking about experiments marked as "planned" in a document I haven't seen, or just the ones that are currently running and needed to complete the paper. Given the context, I think they mean all the experiments whose results we don't have yet, so I'll list out the ones that are actively running or would be natural next steps for the median tier narrative.

Now I'm going to write out detailed predictions for each of these experiments.

For Qwen2.5-14B, I need to establish reasonable baseline perplexity values—the 14B model should perform better than the 7B variant, so I'm estimating around 7.5 on WikiText-2. From there, I can project how uniform 4-bit quantization would degrade performance relative to that baseline, accounting for how the degradation ratio might differ between model sizes.

Now I'm working through the MCKP improvement calculations. If uniform 4-bit quantization lands around 10.9 PPL, then applying the 8% improvement from MCKP brings it down to roughly 10.03. For the k-ablation study, I'm thinking about what the optimal number of heads would look like—if this is a borderline model, the curve should show a shallow U-shape with the sweet spot somewhere in the 12-16 range out of 384 total heads.

For the unconstrained case, I need to recalibrate my thinking. With a concentration of 0.47, the degradation ratio should fall somewhere between the extremes I've seen—Qwen 7B showed a 3.76× degradation while Yi was only 1.08×, so for a borderline 14B model I'm estimating around 1.4× as a middle ground. That would put unconstrained PPL at roughly 12.0, or about 1.10× worse than the uniform baseline.

Now looking at downstream effects: if the MCKP improvement is only 8% at the perplexity level, the downstream task improvements would be more modest than what Qwen 7B achieved. I'm thinking maybe +0.5 to +1.5 percentage points average across tasks rather than the +2.6pp we saw there.

Before I write out the YAML, I should double-check the Qwen2.5-14B baseline perplexity—published benchmarks on WikiText-2 typically show it around 6.5-7.5, so I'll use 7.2 as my reference point. I'm also reconsidering what the user meant by "experiment_plan 中每个 planned 实验"—they might be asking specifically about experiments from the plan that haven't been executed yet, though looking at the list, it seems like most have been covered.

Actually, I think they're asking for predictions across a broader scope: the currently running experiments, any additional ones needed to complete the 14B narrative, the Gemma-2 BOS fix verification, and potential W9 follow-ups. Let me structure my response to cover all of those comprehensively.

I should also nail down the Qwen2.5-14B architecture details—48 layers, hidden size 5120, 40 attention heads with 8 KV heads, which gives a 5:1 GQA ratio, though I want to verify those specs are correct. I'm not entirely confident in those exact numbers, so let me work with what seems most reliable—like the Qwen2.5-14B having 48 layers with 8 KV heads per layer totaling 384 KV heads. Now I'll structure the output systematically using the YAML template with tier, narrative guidance, and imagined experiments that include descriptions, expected results, and analysis.

Drafting the response now...

actually, I need to reconsider the Qwen2.5-14B baseline metrics more carefully. The WikiText-2 perplexity should be around 6.5-7.5, so I'll use 7.2 as my baseline. For uniform 4-bit quantization, the Qwen2.5-7B shows a 1.575× degradation ratio, but larger models tend to be more robust to quantization, so I'm estimating a lower ratio of around 1.50× for the 14B variant, which would put uniform 4-bit at roughly 10.8—though that feels high, so I should adjust downward. Let me examine the actual data patterns from the 7B model to calibrate this more accurately.

Looking at the degradation ratios across different models, Qwen2.5-7B stands out with a 1.575× penalty for uniform 4-bit, while Yi-1.5-9B, Llama-3.1-8B, Mistral-7B, and Gemma-2-9B all show much smaller degradation ratios between 1.01× and 1.05×. The key insight is that Qwen2.5-7B's severe uniform 4-bit degradation stems from its high sensitivity heterogeneity—the spread pattern means that forcing all heads to 4-bit is particularly damaging for the sensitive L0 heads. For the 14B model operating under median tier heterogeneity, the uniform degradation should be considerably less severe than the 7B variant.

Now I'm working through the expected degradation ratio for the 14B model. With a concentration of 0.47 compared to 0.61 for the 7B, the L0 effect gets diluted, so I'd estimate the uniform 4-bit degradation ratio around 1.20-1.35×. Starting from a baseline of 7.2, that would put uniform 4-bit performance at roughly 9.0. Then applying MCKP with an 8% improvement, I need to clarify how that improvement percentage is actually defined in the existing data—whether it's calculated as (uniform - mckp) / uniform or some other formulation.

Looking at the actual improvement rates from the data, Qwen 7B shows 27.3% while Llama shows only 0.2%, so 8% sits in a reasonable middle ground for the 14B model. That gives me mckp = 9.0 × 0.92 = 8.28, which represents a 0.72 PPL point improvement—meaningful but not dramatic, fitting the "borderline positive" characterization.

For the unconstrained case, I'm realizing the degradation is much more variable depending on how many attention heads get assigned to 2-bit quantization. With concentration values ranging from 0.23 to 0.71 across different models, the impact varies wildly—from mild degradation around 1.12× baseline for some models to catastrophic failures for others like Qwen-7B with its high concentration of 0.61.

For the 14B model with concentration 0.47, I'm estimating the solver would allocate somewhere between 15-21% of heads to 2-bit, resulting in degradation around 1.25-1.50×. The tricky part is that unconstrained behavior really depends on how well the profiler can distinguish between heads when concentration is borderline—the solver might still over-allocate to 2-bit even when it shouldn't.

I'm going to settle on reasonable estimates and move forward with finalizing the Qwen2.5-14B predictions, which has 48 layers, 384 total KV heads with GQA 5:1, a baseline PPL around 7.15, and that concentration value of 0.47.

Now I'm working through the specific metrics for this model: the distribution shows a borderline spread/spike pattern with some sensitive heads in L0 but a weaker cluster than the 7B, plus maybe 1-2 mid-layer outliers. The constrained MCKP approach gives about 8.65 PPL (8% improvement over uniform 4-bit), while unconstrained MCKP degrades to 12.5 (1.75× baseline). The optimal k sits around 12-16 with a shallow U-shaped curve. The concentration threshold predicts this should be non-beneficial, but the model actually shows modest benefit—a borderline case that breaks the rule.

I'm reconsidering the decision rule accuracy here. If the rule misses this case, that's a miss under the median tier, so I'd score it 5 out of 6. But if I soften the threshold to treat 0.47 as sitting in a boundary zone around 0.50 rather than a clear miss, I can frame this as a borderline case that aligns with the narrative guidance. For the Qwen family specifically at 14B scale, the 7B has a tight L0 cluster of 4 highly sensitive heads, while at 14B with 384 total heads, the top 5% expands to 19 heads instead of 5-6, so the distribution spreads out more.

Now I'm organizing the experiments I want to run: the Qwen 14B profiling, constrained MCKP, k-ablation, unconstrained, and downstream tasks, plus the Gemma2 constrained fix, and potentially some W9 follow-ups or a cross-model validation. Let me finalize the output structure.

Looking more carefully at the median tier assumptions: Qwen 14B likely sits in a borderline concentration range around 0.40-0.55 with moderate t₁/t₅ ratios, showing modest MCKP improvements compared to the 7B variant. The decision rule might apply but needs careful handling for this edge case, Gemma2's BOS fix should bring the unconstrained ratio into a specific range that might need tuning, and the W9 compounding pattern holds up despite higher variance.

Now I'm mapping out the key metric ranges that would anchor these experiments—MCKP improvements, concentration levels, decision rule accuracy, and the various ratio comparisons across models. The W9 compounding experiment is already complete with results, so I can work from those actual findings rather than predictions.

Looking at the k64 random versus topk ratio from that data, it comes in at 2.44, which sits at the higher end of the expected 1.5-2.5 range. The large standard deviation suggests natural variance in the W9 trend, so a new experiment might not be necessary—instead, I should formalize the W9 findings as an empirical observation with supporting data and description rather than proposing it as a formal theoretical claim.

Stepping back at the actual experiments in the pipeline, I should stick with what's already running and their direct follow-ups rather than adding complexity. The core sequence is the two active experiments plus their natural continuations: the Qwen profiling work flowing into constrained MCKP evaluation, then k ablation, unconstrained solving, and downstream tasks, alongside the Gemma BOS fix experiment and the final revalidation across six models.

Now looking at the performance ratio between random-k and top-k approaches—the existing data shows random-k at 55.94 perplexity versus top-k at 22.946, giving a ratio of 2.44, which sits at the upper end of what I'd expect in a median scenario. The w9 experiment is already complete, so I'm examining whether this ratio would stabilize differently with additional seeds or methodological refinements.

Rather than proposing a new experiment, I'll treat this as an analytical observation about the variance in the existing results. Now I'm finalizing the YAML with concrete numbers for Qwen2.5-14B—48 layers with 384 total KV heads under 5:1 GQA, baseline WikiText-2 perplexity of 7.15, concentration at 0.47, and a t₁/t₅ ratio of 0.72. For the perplexity predictions, I need to clarify what "improvement" represents—the gap between uniform and MCKP approaches shows roughly 29% improvement on the 7B model.

For the 14B median tier estimate with 8% improvement, I'm working backward from the uniform 4-bit degradation. Since the top 19 heads represent 47% of total sensitivity but the model has 384 heads overall, forcing all heads to 4-bit still damages those critical ones significantly. The uniform 4-bit penalty should be less severe than the 7B's 1.575× multiplier—I'm estimating around 1.35× for the 14B, which would put uniform quantization at roughly 9.65 perplexity.

With the 8% improvement from MCKP, that brings the mixed-precision result down to 8.88. The constrained approach with an optimal k around 12 heads (3% of total) performs much better than unconstrained, where the solver over-allocates to 60-80 heads at 2-bit and degrades to 11.44 perplexity. For downstream tasks, I'm seeing modest gains across the board—around 0.5 to 1.5 percentage points depending on the benchmark, with HellaSwag showing the strongest improvement at 1.5pp.

I should double-check the baseline perplexity for Qwen2.5-14B on WikiText-2 to make sure my calculations are grounded in the right reference point.

For the 14B model in FP16, I'm estimating around 7.25 based on the 7B baseline of 9.81 and typical scaling patterns. Now looking at how uniform 4-bit quantization affects different models—Qwen-7B shows an extreme 1.575× ratio due to its spread pattern hammering the L0 cluster, while other models like Yi-9B and Mistral-7B are much more resilient at 1.029× and 1.013×. For the 14B with its borderline concentration around 0.47, I'd expect the ratio to fall somewhere between Qwen-7B's extreme and the more stable models.

Given the lower concentration means fewer heads are critically sensitive to quantization, I'm settling on a 1.20× degradation ratio for uniform 4-bit. That puts the uniform 4-bit perplexity at 8.70, and with MCKP delivering an 8% improvement, the final MCKP perplexity comes to 8.00.

For the unconstrained case with moderate concentration, the solver would likely allocate 50-70 heads to 2-bit, pushing perplexity up to around 10.88. Looking at the k ablation, I see a shallow U-shape with k=12 as the sweet spot at 8.00, while k=0 (uniform 4-bit) hits 8.70 and other values cluster around 8.05-8.15.

For downstream task performance, I'm scaling from the Qwen-7B results—an 8% PPL improvement would translate to roughly +0.76pp average downstream, with a plausible range of +0.3 to +1.5pp depending on the task. Now I'm ready to compile the YAML output, though I need to check the Gemma-2 constrained baseline values from the previous run.

Looking at the old pipeline without the BOS fix, I see MCKP was slightly worse than uniform (9.05 vs 9.03). With the BOS fix applied, the constrained MCKP should land around 6.19, which is nearly identical to the uniform baseline of 6.17—the relationship between them should remain consistent since the concentration is too flat for MCKP to provide meaningful gains.

For the unconstrained ratio, I already have greedy at 8.85 and baseline at 6.03 from the previous experiment, giving a ratio of 1.467 that falls within the expected 1.30-1.55 range, so that doesn't need adjustment.

Now I'm trying to clarify what the gemma2_constrained_bos_fix experiment is actually supposed to do—whether it's just rerunning the constrained MCKP with the BOS fix or if it's also verifying the unconstrained numbers.

Looking at the experiment plan more carefully, I see there are 18 planned experiments listed, plus some optional supplementary ones mentioned in the guidance—like potentially testing Qwen2.5-3B or 32B to find another spread sample.

For the median tier, I don't necessarily need to run those optional experiments if the 14B model is borderline; the paper can work with just one confirmed spread model. So my final experiment count includes the core Qwen 14B experiments (profiling, constrained MCKP, k ablation, unconstrained, and downstream), the Gemma2 constrained run with the BOS fix, the decision rule validation across six models, and optionally the smaller Qwen variants if needed.

Now I'm double-checking the GQA ratios across the Qwen2.5 family to make sure I have the architecture details right—the 7B uses 7:1, the 14B uses 5:1, and the 32B uses 8:1.

For the 14B model with 384 total KV heads, the top 5% comes to about 19 heads, which I'll use as my threshold. Before I finalize the YAML configuration, I want to reconsider how the sensitivity distribution should look for the 14B under the median tier, particularly how those initial high-sensitivity heads cluster together.

The 7B model shows a clear L0 cluster of 4 heads that dominate the sensitivity profile with cross-bitwidth gradients, but the 14B's larger architecture with 8 KV heads per layer means that sensitivity might spread differently—either across more L0 heads or concentrated in fewer. Since L0 represents only about 2% of the total heads in 14B versus 3.6% in 7B, that cluster's relative contribution gets diluted, though it should still be present. I'm estimating the L0 dominance ratio at around 35-45% of the top-5% sensitivity, with possibly 1-2 additional mid-layer sensitive heads mixed in.

Looking at the concentration metrics, 19 heads account for 47% of total sensitivity, and the t₁/t₅ ratio of 0.72 suggests one particularly dominant head among the top-5%—higher than 7B's 0.57 but not as extreme as Yi's 0.90. This puts the 14B model in a borderline zone between the Spread pattern and a more mixed distribution, though that t₁/t₅ value is starting to lean toward a spike-like pattern.

The decision rule would predict "non-beneficial" since concentration falls below 0.50 and t₁/t₅ exceeds 0.70, yet the model actually shows 8% improvement. This is a genuine edge case where the modest gains suggest the rule captures the general trend but misses some nuance at the boundaries.

Now I'm shifting to actually writing out the YAML configuration and being more precise about the 14B downstream task predictions. For the larger model, I'd expect higher baseline performance across the board—ARC-C around 0.58, HellaSwag near 0.81, PIQA approaching 0.81.

With uniform 4-bit quantization, there's a consistent degradation, but MCKP recovers roughly 1 percentage point on average. The recovery rate here is lower than what I saw with 7B—probably around 45-55% versus the 7B's 72.8%—which makes sense given the relationship between perplexity improvement and downstream task recovery. B had 27.3% PPL improvement and 72.8% recovery. If 14B has 8% PPL improvement, recovery would be... well, it's not linear but let me estimate.

Actually, recovery rate = (uniform - mckp) / (uniform - baseline). For PPL:
- 14B: (8.70 - 8.00) / (8.70 - 7.25) = 0.70 / 1.45 = 48.3%

For downstream, the recovery would be similar order: ~40-55%.

Let me finalize downstream numbers:
- Baseline avg: 0.730
- Uniform avg: 0.715
- MCKP avg: 0.722
- Δ MCKP vs uniform: +0.7pp
- Recovery: 46.7%

Now I need to work through what the k-ablation would look like for 14B. With 384 KV heads and concentration around 0.47, the top 5% would be roughly 19 heads, so optimal k should fall somewhere in the 10-16 range. Looking at the compounding sweep across different k values, I can see the PPL trajectory from uniform at 8.70 down to near-optimal around k=12-16 at 8.00, then degrading again as k increases further. Looking at the rest of the k-ablation results, the performance degrades noticeably at k=32 and beyond, confirming that k=12 is indeed optimal with an 8% improvement over uniform quantization. Now I need to verify the bit distribution works out—with k=12 heads at 2-bit and the remaining heads distributed across higher bit-widths to stay within the 0.25 budget constraint, the average should land around 4 bits per head.

Examining the profiling data from the high-resolution sensitivity analysis, the top heads show much more moderate deltas compared to the 7B model—L0H0 has a 2-bit delta of 3.2, which is less than half of what we saw before. The sensitivity is more distributed across the first layer and a few mid-layer outliers, suggesting the 14B model's attention patterns are less concentrated in critical heads.

Now I'm checking the decision rule against all six models to see if the concentration and top-1-to-top-5 ratio pattern holds up. The first few models confirm the pattern—high concentration with low ratio spread predicts beneficial quantization, while high concentration paired with a high ratio spread predicts minimal gains—but I need to verify this holds across the remaining models. The rule achieves 5 out of 6 accuracy, correctly identifying the non-beneficial cases while the 14B model falls into that boundary zone where the thresholds become ambiguous. With the softened threshold approach, I can frame this as the rule successfully classifying all non-borderline cases, with the 14B model explicitly landing in the zone where directional guidance applies rather than binary classification. Now I'm ready to write out the YAML structure, and I should also check the Gemma-2 BOS fix by comparing the old pipeline data against the corrected version. Looking at the expected results for the constrained MCKP approach, I'm seeing a PPL around 6.17 that's essentially within noise of uniform quantization, with the best k value at 8 and a relatively flat k-PPL curve. Now I'm checking the bit distribution across quantization levels—2-bit, 4-bit, and 8-bit allocations—and calculating whether we're staying within the target average of 4 bits per parameter, though it looks like the current allocation might be overshooting that budget.

Let me recalculate the bit allocation more carefully. With 336 heads and a 4-bit average budget, I need exactly 1344 total bits. If I shift 8 heads down to 2-bit, that saves 16 bits, which I can use to accommodate 4 heads at 8-bit instead. This gives me a valid distribution of 8 heads at 2-bit, 324 at 4-bit, and 4 at 8-bit that sums to exactly the budget. Now I'm wondering whether the concentration patterns might affect this allocation further.

Since the concentration is only 0.23, the solver doesn't have much signal to distinguish between heads, so the 8 heads selected for 2-bit quantization are somewhat arbitrary—they're all similarly insensitive. This explains why the MCKP and uniform approaches yield nearly identical results for Gemma-2. Now I'm ready to write out the YAML configuration. Let me structure it clearly and comprehensively for the user, and I should also reconsider the constrained ratio for Gemma-2 with the BOS fix applied. The old pipeline without the fix showed MCKP at 9.05 versus uniform at 9.03, a difference of about -0.22%. With the BOS fix in place, the relative performance should remain similar, so both approaches should converge around 6.17.

I'm refining the numbers to be more precise: using the baseline of 6.0306 from the unconstrained version, the uniform 4-bit result of 6.1683, and estimating the constrained MCKP at around 6.19. For the median tier improvement range, I'll set the Gemma-2 constrained versus uniform percentage at -0.3% to reflect a slight degradation consistent with measurement noise.

I'm also considering whether the profiling step was affected by the BOS fix—but since profiling happens on calibration data rather than the test set, and the BOS fix only impacts evaluation, the profiles should remain unchanged. The experiment is purely about evaluating the constrained allocation under the corrected evaluation procedure. Now I'm ready to write out the YAML with this rationale included. I'm keeping the empirical decision rule intact and treating the 14B model as a boundary case—acknowledging that the threshold is a soft range rather than a hard cutoff, which aligns with the empirical nature of the findings. I'll note in the limitations that we have only one confirmed case and need larger-scale validation. For the W9 super-additivity, I'm treating it as an empirical observation supported by figures and description rather than a formal proposition, and I'm shifting the contribution focus from diagnostic insights toward the constraint as a universal fix. Now I'm planning high-resolution profiling experiments on Qwen2.5-14B to measure per-head 2-bit distortion across its 384 KV heads with GQA compression. concentration and t₁/t₅. Looking at the Qwen2.5-14B results, the architectural patterns from the 7B model seem to persist, but the larger model has 384 KV heads instead of 112, spreading the top-5% attention across 19 heads rather than 5-6. While L0 still dominates with 8 of those heads, the remaining 11 are distributed through middle layers, which explains why concentration dropped to 0.47. Interestingly, L0's strongest head (L0H0) shows increased relative importance with a t₁/t₅ ratio of 0.72 compared to 0.57 in the 7B model.

The Delta CV metric of ~3.85 sits between the flat models like Mistral and Gemma-2 but below the 7B baseline, suggesting a "diluted spread" pattern where the L0 cluster still exists but gets weakened relative to the overall head distribution. Looking at the top sensitive heads, L0H0 leads at 3.21, followed by L0H3 and L0H5, with middle-layer heads like L8H2 and L12H6 interspersed in the rankings.

The heatmap shows L0 has 4-5 distinct bright spots rather than being fully illuminated like the 7B model, while the cumulative sensitivity curve falls between the steeper 7B and the flatter baseline models—indicating the 14B maintains some L0 clustering but with less concentration than smaller variants.

The key insight is that the 14B model sits right at the boundary: its concentration of 0.47 just barely misses the 0.50 threshold, and the t₁/t₅ ratio of 0.72 just clears the 0.70 threshold, so it fails the joint condition despite being close on both metrics. This makes it a borderline case—neither a clean Spread pattern nor a clear Spike/Flat pattern.

Now I'm setting up a constrained MCKP evaluation for the Qwen2.5-14B model... The 14B model's lower concentration (0.47) compared to smaller models means its sensitive heads suffer less collateral damage under uniform quantization, but MCKP can still find meaningful optimization by promoting the top 12 heads to 8-bit and compensating with 2-bit elsewhere—recovering 8% PPL improvement versus 27% for the 7B model, since there's less heterogeneity to exploit overall.

Now I'm examining the ablation results across different k values to see where the optimal allocation point lies. The k-PPL curve shows a shallow U-shape with the minimum at k=12, and from k=12 to k=20 it's essentially flat with minimal variation, indicating a smoother sensitivity distribution compared to the 7B model. The solver equivalence holds here too—greedy and MCKP produce identical results at k=12—confirming that the constraint is the primary driver of improvement. While the 8% gain is less dramatic than the 7B's 27%, it's statistically meaningful and well above the noise floor seen in other models.

Now I'm setting up the unconstrained solver evaluation for Qwen2.5-14B to measure how much performance degrades when we remove the cardinality constraint, with expected PPL values around 11.30-11.60 and roughly 15-16% of heads quantized to 2-bit.

The concentration parameter of 0.47 positions this model's degradation between Qwen-7B's severe collapse and the milder impact seen in Yi/Llama/Mistral, so the solver over-allocates 2-bit heads because the profiler assigns similar low delta values across most intermediate layers—resulting in about 58-62 heads being quantized, which is fewer than Gemma-2's 31.5% but more than Yi's 11.5% since the 14B model has more moderate-but-nonzero differences that keep some heads at 4-bit—and this compounding effect from the 2-bit heads produces roughly a 1.56× degradation ratio.

This puts the 14B model in the moderate degradation category alongside Gemma-2, demonstrating that the constraint approach still provides value when dealing with medium-level heterogeneity. Now I'm looking at the performance comparison table across different allocation strategies.

The unconstrained greedy approach achieves 1.56× degradation, which fills a crucial gap in the paper's three-tier classification—we now have two data points for the moderate category instead of just Gemma-2's 1.47×, making the catastrophic-moderate-mild spectrum more robust. When constraints are applied with k=12, the perplexity improves dramatically from 11.30 down to 8.00, a 29% improvement that reinforces how effective constraints are as a universal solution.

Now I'm looking at the downstream evaluation results for Qwen2.5-14B at 4× compression across standard benchmarks, comparing baseline performance against uniform and MCKP quantization approaches with their respective accuracy metrics and recovery percentages. The 8% PPL improvement translates to about +0.7pp downstream performance, which aligns well with Qwen-7B's scaling ratio—the 14B model shows roughly one-third the gains of the 7B across all tasks, with reasoning-heavy benchmarks like ARC-C and HellaSwag benefiting most while simpler commonsense tasks like PIQA show minimal improvement. The recovery rate of 46.7% is notably lower than the 7B's 72.8%, suggesting the relationship between concentration and optimization potential continues to hold at this scale. Looking at the downstream task results for Qwen2.5-14B, the modest improvements across all four benchmarks (+0.4 to +1.0pp) align with the borderline positive perplexity signal, though the +0.7pp average lacks multi-seed confidence intervals and could have ±0.5pp noise, so I should hedge the significance claim in the paper. The ARC-C improvement of +1.0pp is notably smaller than the 7B's +3.16pp, reinforcing that reasoning tasks are more sensitive to KV cache quality.

Now I'm re-evaluating Gemma-2-9B's constrained MCKP with the corrected BOS-prepend sliding window approach, which should replace the earlier buggy baseline of 8.9 with the proper 6.03 perplexity, and I'm expecting the constrained allocation to yield around 6.19 PPL with a best-k of 8 and a specific bit distribution favoring 4-bit quantization.

Looking at the ablation results across different k values and the unconstrained greedy baseline, I'm noticing that Gemma-2's flat head sensitivity distribution (concentration 0.23, coefficient of variation 1.28) makes it nearly impossible for the profiler to meaningfully differentiate between heads, so the 8 selected 2-bit heads are essentially arbitrary—the sensitivity deltas are too small to produce meaningful optimization gains, which explains why the constrained MCKP result of 6.19 PPL is barely different from the uniform 4-bit baseline of 6.17.

The k-PPL curve shows a monotonic increase pattern similar to Mistral, where each additional 2-bit head contributes roughly equal degradation, and the unconstrained ratio of 1.47× aligns with what I confirmed in the previous experiment after the BOS fix, so the main contribution here is establishing a BOS-corrected constrained baseline to replace the outdated numbers in the paper.

Generating markdown table... Looking at the k-ablation results, the PPL increases monotonically but very gradually as k grows from 0 to 24, with no U-shaped curve appearing. The BOS fix substantially changed the absolute baseline numbers but didn't alter the core findings—MCKP still doesn't help Gemma-2, and the difference between constrained and uniform approaches remains within noise margins. I need to update all the Gemma-2 figures in the paper to reflect the corrected baseline, though the main narrative stays intact: flat distributions show that constraints have universal value in preventing over-allocation, but MCKP optimization itself doesn't provide additional benefits.

Now I'm planning to validate the decision rule across six models by adding Qwen2.5-14B as a test case, checking whether the joint diagnostic of concentration ≳0.50 and t₁/t₅ ≲0.70 holds up. The rule should correctly classify five out of six models, with Qwen2.5-14B appearing as a borderline case near the decision boundaries.

Looking at the results, Qwen2.5-14B falls just outside both thresholds with a concentration of 0.47 and t₁/t₅ of 0.72, causing the rule to predict "non-beneficial" when it actually shows an 8% improvement—a false negative. This reveals the thresholds are soft boundaries rather than hard cutoffs, and the rule is being overly conservative in this edge case.

Generating markdown table... I'm looking at how to frame the decision rule's accuracy more carefully—rather than claiming 5/6 correctness, I should acknowledge that it successfully classifies all the non-borderline cases while noting that Qwen2.5-14B legitimately falls into the boundary zone I've identified. I'm also softening the threshold language from a hard cutoff to a range, and I need to add a limitations section that clarifies this is a directional heuristic validated on a small set of architectures.

For the W9 compounding observation, I'm treating this as an empirical finding rather than a formal claim, and I'm examining the variance in the random-k versus top-k ratio to understand the stability of this effect. Generating markdown table... The ratio actually decreases from k=32 to k=64 (2.73 down to 2.44), which suggests non-monotonic behavior in the extreme regime—possibly due to evaluation saturation. This reinforces treating this as an observation rather than a formal claim, so I'll present it descriptively in the Analysis section alongside the figure without assigning it a proposition number or formal statement. If reviewers push for formal analysis, I can point to future work and note that a single model isn't sufficient for formalization.

Now I'm integrating the Qwen2.5-14B results as a boundary case study in the Analysis section, updating the cross-architecture table with its metrics, refining the decision rule accuracy claim to account for the boundary case, adding a limitation note about the N=1 confirmation, and softening the threshold range from strictly ≳0.50 to 0.45-0.55.

The key insight is that concentration operates as a continuous variable—the performance benefit scales smoothly across models from Mistral's 0.22 (−0.4%) through to the 7B's 0.61 (+27%)—and the 14B result alongside Gemma-2 demonstrates that constraints still provide value even at moderate concentration levels, though the universality of this pattern matters more than pinpointing exact diagnostic boundaries.

For the paper, I'm reframing the contributions: the cardinality constraint as the primary finding that benefits all three model tiers, concentration-based diagnostics as secondary validation, and the 14B boundary case as a tertiary analysis that enriches the narrative without weakening the core claim.

The updated visualization will show six models plotted by concentration versus MCKP improvement, with 14B explicitly marked as a boundary case and a regression line fitted through the concentration-benefit relationship.

Across all three claims, the 14B model actually strengthens the paper—it demonstrates that heterogeneity is architecture-dependent, that constraints help even moderate cases, and that the decision rule holds empirically with 5/5 non-borderline accuracy. The honest discussion of boundary behavior is more defensible than dismissing outliers, and EMNLP reviewers will likely focus on formalizing that boundary treatment rather than attacking the sample size.

Now I'm double-checking the compression ratios from the data—I had k=64 at 2.44 but k=32 showing 2.73, so let me verify those numbers against the actual results. Looking at the k=32 and k=16 ratios, I can see the pattern holds—the randomk to topk ratio increases monotonically as k decreases, reaching 2.44 at k=64, which fits perfectly within the expected [1.5, 2.5] range for this metric. I'm trying to figure out what these ratio values represent. Let me test if they're the marginal PPL increase per head compared to k=1 baseline, but my calculations don't match—I'm getting 0.61 instead of 0.86. Maybe the ratio is actually (PPL at k minus baseline) divided by (k times the PPL increase at k=1), which would show how much the effect compounds, but that's still giving me 0.61 for k=4 topk, not 0.86.

These recorded ratios might be using a formula I'm not reconstructing correctly, but it doesn't matter much for what I need to output—I'll just work with the raw PPL values and the randomk versus topk comparison directly.

Now I'm putting together the final YAML output. I'm also weighing whether to include an optional experiment with Qwen2.5-3B or Qwen2.5-32B to hunt for a second Spread sample, since the 14B model sits right on the borderline without providing one. The 3B would be extremely small with heavy grouped-query attention, so it's uncertain whether it would actually exhibit Spread behavior. I need to clarify what the user actually asked for—they want predictions only for the explicitly planned experiments, not speculative ones like the Qwen models. So I'll note those as optional considerations but keep the main focus on the firm plans. For the 14B model, I should include the greedy versus MCKP equivalence prediction since that pattern has held consistently across all tested models. I'm also working through the bit distribution math for the k=12 case on 14B to understand the compensation needed.

Now I'm calculating how to optimally allocate the extra bits from the 2-bit heads. With 12 heads at 2-bit saving 24 bits total, I need to figure out whether upgrading to 8-bit or 16-bit heads gives the best sensitivity gains, but the math is getting complex—MCKP would handle this optimization better than manual calculation. Let me verify this is correct by checking with 8 at 8-bit, which gives 1544—too high. So 6 at 8-bit is the right answer, confirming the distribution of 12 heads at 2-bit, 366 at 4-bit, and 6 at 8-bit totals exactly 1536 bits with a memory ratio of 0.25.

Now I'm exploring whether including some 16-bit heads could work instead, setting up equations to see if that produces a valid allocation. I'll stick with the 6 at 8-bit allocation for simplicity. Let me verify the budget math for the 14B model with k=12: the allocation {2:12, 4:366, 8:6} totals 384 heads, and checking the bit budget: 12×2 + 366×4 + 6×8 = 1536, which equals 384×4, so that checks out. Now I need to finalize the output and make sure everything is internally consistent.

Looking at the 14B results, the MCKP approach with k=12 achieves 8.00 compared to 8.70 for uniform 4-bit quantization, recovering about 48% of the gap to baseline. The unconstrained versions show higher performance at 11.30 for greedy and 11.60 for MCKP. On the downstream task, MCKP averages 0.722 compared to 0.715 for uniform, gaining about 0.7 percentage points.

Now I'm ready to write out the YAML configuration. But I should account for the profiling time estimate for the 14B model—with 384 attention heads versus 112 for the 7B, plus the larger model size making forward passes slower, the hires profiling would take roughly 7-8 hours per seed, which is significantly longer than the 65 minutes needed for 7B. iling is 64 sequences × 2048 tokens × 384 heads = very expensive. Let me say ~4-5 hours if GPU is efficient.

Actually, the profiling time depends on:
- Per-head evaluation: for each head, quantize it and measure PPL
- 384 heads × (64 seq × 2048 tok) = very long
- Qwen-7B hires: 65 min for 112 heads → ~0.58 min/head
- Qwen-14B: 384 heads × 0.58 × 2 (larger model) ≈ 446 min

So ~7.5 hours. That's a lot. Let me include this as a planning consideration.

Actually, looking at yi15_hires_bf16_2bitonly: total_hours=0.96 for 192 heads. That's much faster than Qwen-7B's 65 min for 112 heads. The 2-bit-only profiling is faster because it skips the full bitwidth sweep and just measures the delta at 2-bit precision. Comparing across models, the 14B full hires profiling would scale up from the 7B baseline by both the head count ratio and model size factor—roughly 3.4× the 7B time times 1.7× for the larger model, putting it around 6 hours.

Now I'm checking the concentration metrics from the existing models to validate my estimates before finalizing the YAML configuration. Looking at the t₁/t₅ ratio, a value of 0.72 means the top head dominates the sensitivity distribution—it accounts for 72% of what the top 5 heads contribute combined, leaving the remaining four heads to share only 28%. That's a pretty concentrated pattern. In contrast, the 7B model's ratio of 0.57 shows a more balanced spread where the strongest head is less dominant. For the 14B, this concentration-versus-spread distinction pushes it into that borderline "diluted spread" territory, which aligns with the median tier classification.

Now I'm working through the YAML structure and need to think through the Gemma-2 BOS fix experiment more carefully. The unconstrained numbers are already in the current dataset, but the constrained allocation with BOS fix is what's missing. Looking at the old buggy data, the constrained MCKP achieved 9.05 PPL with k=8, compared to uniform at 9.03. Once the BOS fix is applied, the baseline drops significantly to 6.03 and uniform to 6.17, so the constrained MCKP should scale proportionally and likely show a meaningful improvement in that regime.

I'm also considering whether the BOS fix would change the optimal k value for Gemma-2, though the profiling methodology should remain consistent.  Since the heads show relatively flat sensitivity under the fix, most k values would yield similar performance, so I'll stick with k=8 as the baseline. Now I need to write out the YAML configuration with these parameters finalized.

For the w9 entry, I'm reconsidering whether to frame this as a new experiment or an analysis task—the data collection is already complete, so this is really about formalizing the approach rather than running something new. I'll include it but clarify that it's analysis-focused rather than requiring fresh experiments.

Looking at what actually needs to be planned: the running experiments (w1 profiling and the BOS fix), the natural follow-ups like the constrained MCKP variant and k ablation, then the unconstrained and downstream tasks. I should also note the analysis pieces—how the 14B results fit into the broader decision framework and ultimately into the paper narrative.

Consolidating where it makes sense, I'm settling on eight experiments that cover the progression from profiling through downstream evaluation, plus the validation and synthesis work. Each one has a clear purpose without redundancy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b36d576-c690-403e-8cae-0e721f042137",
  "isSidechain": false,
  "requestId": "req_011Cb46TdkQWoVGZgyuvvKvM",
  "type": "assistant",
  "uuid": "342285fe-ed2e-4454-b42a-83cefbe4a0f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkynimEt68SScn25Jnptbu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 31515,
      "cache_read_input_tokens": 11841,
      "output_tokens": 29961,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 29961,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 31515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31515
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

_source line 9 · 2026-05-15T09:20:14.081Z_

Let me review the experiment plan and running experiments to build the complete prediction set.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "342285fe-ed2e-4454-b42a-83cefbe4a0f9",
  "isSidechain": false,
  "requestId": "req_011Cb46TdkQWoVGZgyuvvKvM",
  "type": "assistant",
  "uuid": "a54b8f71-4f49-44d8-8359-8c0f841e1787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkynimEt68SScn25Jnptbu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 31515,
      "cache_read_input_tokens": 11841,
      "output_tokens": 29961,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 29961,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 31515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31515
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

_source line 10 · 2026-05-15T09:20:14.082Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011nfzHoHRZUzDahhrgwYffN`</summary>

```json
{
  "pattern": "**/*experiment*plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a54b8f71-4f49-44d8-8359-8c0f841e1787",
  "isSidechain": false,
  "requestId": "req_011Cb46TdkQWoVGZgyuvvKvM",
  "type": "assistant",
  "uuid": "45cf5f2c-cbce-4517-9958-7325d59be8a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkynimEt68SScn25Jnptbu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 31515,
      "cache_read_input_tokens": 11841,
      "output_tokens": 29961,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 29961,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 31515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31515
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

_source line 11 · 2026-05-15T09:20:14.112Z_

<details><summary>↩ Tool result · `toolu_011nfzHoHRZUzDahhrgwYffN`</summary>

```text
projects/demo_calibrated_sim/experiment_plan.lock
projects/demo_calibrated_sim/experiment_plan.yaml
projects/ratekv/experiment_plan.lock
projects/ratekv/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45cf5f2c-cbce-4517-9958-7325d59be8a9",
  "isSidechain": false,
  "promptId": "26618dbe-32d3-4d36-8678-6c78804f25da",
  "type": "user",
  "uuid": "50ab9fd7-4190-4b5b-9cd5-a3675cebc80f",
  "toolUseResult": {
    "filenames": [
      "projects/demo_calibrated_sim/experiment_plan.lock",
      "projects/demo_calibrated_sim/experiment_plan.yaml",
      "projects/ratekv/experiment_plan.lock",
      "projects/ratekv/experiment_plan.yaml"
    ],
    "durationMs": 21,
    "numFiles": 4,
    "truncated": false
  },
  "sourceToolAssistantUUID": "45cf5f2c-cbce-4517-9958-7325d59be8a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Qwen2.5-14B 边界/弱阳性，N 实质仍为 1；其余数据基本一致但有小幅偏差需要对齐 核心假设：['Qwen2.5-14B concentration 0.40-0.55 或 t₁/t₅ 0.65-0.80（边界区间，不完全满足 joint condition）', 'Qwen2.5-14B MC…",
  "leafUuid": "50ab9fd7-4190-4b5b-9cd5-a3675cebc80f",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Concentration-dependent KV cache quantization across five model architectures",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---

### Tool call

_source line 14 · 2026-05-15T09:20:17.978Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NZVKMeWXxjR1v9MC9iJRNa`</summary>

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
  "parentUuid": "50ab9fd7-4190-4b5b-9cd5-a3675cebc80f",
  "isSidechain": false,
  "requestId": "req_011Cb47AhLqsEFE3r2E7LGnS",
  "type": "assistant",
  "uuid": "e478cd9c-58d1-4e17-9c79-525bc1904ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JawUEcWysmur3stdCEGyxt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29967,
      "cache_read_input_tokens": 43356,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 43356,
          "cache_creation_input_tokens": 29967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29967
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

_source line 15 · 2026-05-15T09:20:17.998Z_

<details><summary>↩ Tool result · `toolu_01NZVKMeWXxjR1v9MC9iJRNa`</summary>

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
  "parentUuid": "e478cd9c-58d1-4e17-9c79-525bc1904ede",
  "isSidechain": false,
  "promptId": "26618dbe-32d3-4d36-8678-6c78804f25da",
  "type": "user",
  "uuid": "4c874101-845c-4d8b-8cf7-a879425dd98e",
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
  "sourceToolAssistantUUID": "e478cd9c-58d1-4e17-9c79-525bc1904ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16 · 2026-05-15T09:20:18.077Z_

````json
{
  "parentUuid": "4c874101-845c-4d8b-8cf7-a879425dd98e",
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
  "uuid": "78b45237-bd41-4052-9827-75e532c0c6cd",
  "timestamp": "2026-05-15T09:20:18.077Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Qwen2.5-14B 边界/弱阳性，N 实质仍为 1；其余数据基本一致但有小幅偏差需要对齐 核心假设：['Qwen2.5-14B concentration 0.40-0.55 或 t₁/t₅ 0.65-0.80（边界区间，不完全满足 joint condition）', 'Qwen2.5-14B MC…",
  "leafUuid": "78b45237-bd41-4052-9827-75e532c0c6cd",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Concentration-dependent KV cache quantization across five model architectures",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---

### Tool call

_source line 19 · 2026-05-15T09:20:22.498Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jm8D3YXP6uepVKFpkXpgvK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/experiment_plan.lock"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78b45237-bd41-4052-9827-75e532c0c6cd",
  "isSidechain": false,
  "requestId": "req_011Cb47AzH547ZM5rA6h1e2Y",
  "type": "assistant",
  "uuid": "1ba942d5-cd69-4939-b365-e2836a333c61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjDWRG9JSwjHThijLtYwYh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8419,
      "cache_read_input_tokens": 73323,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 73323,
          "cache_creation_input_tokens": 8419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8419
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

_source line 20 · 2026-05-15T09:20:22.504Z_

<details><summary>↩ Tool result · `toolu_01Jm8D3YXP6uepVKFpkXpgvK`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ba942d5-cd69-4939-b365-e2836a333c61",
  "isSidechain": false,
  "promptId": "26618dbe-32d3-4d36-8678-6c78804f25da",
  "type": "user",
  "uuid": "3bcc38dd-2897-45b9-845b-3d5384806301",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/experiment_plan.lock",
      "content": "",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "1ba942d5-cd69-4939-b365-e2836a333c61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T09:20:30.124Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BfvkKgMcFkN9L3C7yuNKN7`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find RUNNING experiments and 14B config",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/, I need to find:\n\n1. Any files referencing \"gemma2_constrained_bos_fix\" or \"w1_qwen14b\" — these are RUNNING experiments, I want to see their configs/scripts\n2. Any file describing Qwen2.5-14B model architecture (number of layers, KV heads, GQA ratio)\n3. The registry file that contains experiment statuses (look for files with \"registry\" in name or YAML files that contain exp_id entries)\n4. Any planning docs or phase documents that describe what experiments are \"planned\" vs \"done\"\n\nSearch broadly - check artifacts/, scripts/, configs/, and any YAML/JSON/MD files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bcc38dd-2897-45b9-845b-3d5384806301",
  "isSidechain": false,
  "requestId": "req_011Cb47BKH51sz5zzZbQUAtM",
  "type": "assistant",
  "uuid": "262c64b7-1556-45f4-8e85-846fc6221fe6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHqK3jqTYbGn8c2mT9yMHi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 125,
      "cache_read_input_tokens": 81742,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 125,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 81742,
          "cache_creation_input_tokens": 125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 125
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

_source line 22 · 2026-05-15T09:21:14.362Z_

<details><summary>↩ Tool result · `toolu_01BfvkKgMcFkN9L3C7yuNKN7`</summary>

```text
Perfect! I have gathered all the necessary information. Let me compile my findings.

## Summary of Findings

Based on my comprehensive search of the ratekv project, here are the answers to your four questions:

### 1. RUNNING EXPERIMENTS: gemma2_constrained_bos_fix & w1_qwen14b_hires_profiling

**Checkpoint/Status Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/checkpoints/gemma2_constrained_bos_fix_RUNNING_20260515T082240.json`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/checkpoints/w1_qwen14b_hires_profiling_RUNNING_20260515T082242.json`

**Experiment Details from checkpoint files:**

**gemma2_constrained_bos_fix:**
- Status: RUNNING (started 2026-05-15 08:22:09Z)
- GPU: cuda:0 on westd-37397
- Hypothesis: Re-evaluate Table 2 Gemma-2 constrained MCKP numbers with BOS fix (sliding window + BOS prepend). Original eval may have been affected by cold-start bug.
- Command: `CUDA_VISIBLE_DEVICES=0 python -u gemma2_constrained_bos_fix.py`
- Model: Gemma-2-9B
- Data: WikiText-2 test set + merged profiles, 336 heads
- Log path: `/root/ratekv/logs/gemma2_constrained_bos_fix.log`

**w1_qwen14b_hires_profiling:**
- Status: RUNNING (started 2026-05-15 08:22:15Z)
- GPU: cuda:1 on westd-37397
- Hypothesis: W1 new model: Qwen2.5-14B hires bf16 2-bit-only profiling. **48L x 8KV (GQA 5:1), 384 heads.** Same Qwen family as 7B (Spread, concentration=0.61) — tests whether diagnostic generalizes within model family at larger scale.
- Command: `CUDA_VISIBLE_DEVICES=1 python -u run_qwen14b_hires_profiling.py`
- Model: Qwen2.5-14B
- Data: calibration_hires.json (64 seq x 2048 tok), 384 heads (48L x 8KV)
- Log path: `/root/ratekv/logs/qwen14b_hires_profiling.log`
- Baseline PPL: 5.8432

**Location of actual scripts:** The checkpoint files don't specify full paths, but the scripts are likely in the project root. The experiment runner uses `run_qwen14b_hires_profiling.py` and `gemma2_constrained_bos_fix.py`.

---

### 2. QWEN2.5-14B MODEL ARCHITECTURE

From the checkpoint file `w1_qwen14b_hires_profiling_RUNNING_20260515T082242.json`, the key architecture details are:

- **Number of Layers:** 48 (denoted as 48L)
- **KV Heads:** 8 per layer (total 384 heads across all layers = 48 × 8)
- **GQA Ratio:** 5:1 (Group Query Attention)
- **Query Heads:** 40 (5 × 8 = 40 query heads per layer)

Additional context from paper_framing.md shows Qwen2.5-7B has:
- 28 layers × 112 KV heads = 3,136 total KV heads
- GQA ratio: 7:1
- Concentration: 0.61 ("Spread" pattern)

The 14B model (48L × 8KV) follows the same Qwen family architecture but is significantly larger.

---

### 3. REGISTRY FILE WITH EXPERIMENT STATUSES

**Primary Registry File:**
`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml` (49,827 tokens)

This file contains full experiment tracking with fields:
- `exp_id`: experiment identifier
- `status`: DONE, RUNNING, PENDING, ALLOCATED, QUEUED
- `hypothesis`: what each experiment tests
- `spec`: command, GPU, server, log path, model name, data details
- `conclusion`: outcome and notes

**Secondary Registry:**
`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/dream_registry.yaml`

This tracks "dream" sessions (multi-agent paper writing/review runs):
- Two dreams: `dream_20260514T002109` (status: done) and `dream_20260515T085855` (status: imagining)

---

### 4. PLANNING & PHASE DOCUMENTS

**Primary Planning Document:**
`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/ROADMAP.md`

Key information:
- **Current Phase:** 审稿响应 (Reviewer Response) — 补实验收尾 + 写作集成
- **Submission Target:** EMNLP 2026 Main (ARR May 25, 2026)
- **Reviewer Scores:** R1 2.5/5, R2 2/5 → Weak Reject (2.25/5)

**W-Series Progress (Experiments Status):**
- ✅ **W2**: 5/5 unconstrained baselines (gradient: 3.31× → 1.47× → 1.07-1.08×) — DONE
- ✅ **W3**: 5/5 downstream eval — DONE
- ✅ **W9**: compounding v2 (1.56-4.89× super-additivity) — DONE
- 🔄 **W1**: Qwen2.5-14B profiling **RUNNING** (cuda:1, ~3h)
- ⏳ **W4**: Qwen outlier analysis → Paper Agent writing

**Other Planning Docs:**
- `decisions.yaml` (54 entries) - Decision log with D001-D051+ tracking eviction pivot, metric changes, BOS bug fixes, GQA proxy insights
- `paper_framing.md` (150+ lines) - Core narrative, claims, evidence summary
- `IDEA_BRIEF.md` - Original project proposal with background

**Timeline:** 10 days to submission with buffer of 5 days
- Days 0-1: W1 profiling + OPT profiling + Gemma-2 constrained
- Days 1-3: Paper Agent writing integration + W1 result incorporation
- Days 3-4: Reference audit + final review
- Days 4-5: Submit paper to review (continue mode)

---

### Quick Reference Paths:

| Item | Path |
|------|------|
| Running experiments (checkpoint status) | `/ratekv/checkpoints/` |
| Main registry | `/ratekv/registry.yaml` |
| Dream registry | `/ratekv/dream_registry.yaml` |
| Roadmap & planning | `/ratekv/ROADMAP.md` |
| Decision log | `/ratekv/decisions.yaml` |
| Core narrative | `/ratekv/paper_framing.md` |
| Experiment scripts | `/ratekv/run_*.py` (likely location) |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "262c64b7-1556-45f4-8e85-846fc6221fe6",
  "isSidechain": false,
  "promptId": "26618dbe-32d3-4d36-8678-6c78804f25da",
  "type": "user",
  "uuid": "5e0e7164-8c2f-49b2-943d-726b5548ffb7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/, I need to find:\n\n1. Any files referencing \"gemma2_constrained_bos_fix\" or \"w1_qwen14b\" — these are RUNNING experiments, I want to see their configs/scripts\n2. Any file describing Qwen2.5-14B model architecture (number of layers, KV heads, GQA ratio)\n3. The registry file that contains experiment statuses (look for files with \"registry\" in name or YAML files that contain exp_id entries)\n4. Any planning docs or phase documents that describe what experiments are \"planned\" vs \"done\"\n\nSearch broadly - check artifacts/, scripts/, configs/, and any YAML/JSON/MD files.",
    "agentId": "a64df78e50178953a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have gathered all the necessary information. Let me compile my findings.\n\n## Summary of Findings\n\nBased on my comprehensive search of the ratekv project, here are the answers to your four questions:\n\n### 1. RUNNING EXPERIMENTS: gemma2_constrained_bos_fix & w1_qwen14b_hires_profiling\n\n**Checkpoint/Status Files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/checkpoints/gemma2_constrained_bos_fix_RUNNING_20260515T082240.json`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/checkpoints/w1_qwen14b_hires_profiling_RUNNING_20260515T082242.json`\n\n**Experiment Details from checkpoint files:**\n\n**gemma2_constrained_bos_fix:**\n- Status: RUNNING (started 2026-05-15 08:22:09Z)\n- GPU: cuda:0 on westd-37397\n- Hypothesis: Re-evaluate Table 2 Gemma-2 constrained MCKP numbers with BOS fix (sliding window + BOS prepend). Original eval may have been affected by cold-start bug.\n- Command: `CUDA_VISIBLE_DEVICES=0 python -u gemma2_constrained_bos_fix.py`\n- Model: Gemma-2-9B\n- Data: WikiText-2 test set + merged profiles, 336 heads\n- Log path: `/root/ratekv/logs/gemma2_constrained_bos_fix.log`\n\n**w1_qwen14b_hires_profiling:**\n- Status: RUNNING (started 2026-05-15 08:22:15Z)\n- GPU: cuda:1 on westd-37397\n- Hypothesis: W1 new model: Qwen2.5-14B hires bf16 2-bit-only profiling. **48L x 8KV (GQA 5:1), 384 heads.** Same Qwen family as 7B (Spread, concentration=0.61) — tests whether diagnostic generalizes within model family at larger scale.\n- Command: `CUDA_VISIBLE_DEVICES=1 python -u run_qwen14b_hires_profiling.py`\n- Model: Qwen2.5-14B\n- Data: calibration_hires.json (64 seq x 2048 tok), 384 heads (48L x 8KV)\n- Log path: `/root/ratekv/logs/qwen14b_hires_profiling.log`\n- Baseline PPL: 5.8432\n\n**Location of actual scripts:** The checkpoint files don't specify full paths, but the scripts are likely in the project root. The experiment runner uses `run_qwen14b_hires_profiling.py` and `gemma2_constrained_bos_fix.py`.\n\n---\n\n### 2. QWEN2.5-14B MODEL ARCHITECTURE\n\nFrom the checkpoint file `w1_qwen14b_hires_profiling_RUNNING_20260515T082242.json`, the key architecture details are:\n\n- **Number of Layers:** 48 (denoted as 48L)\n- **KV Heads:** 8 per layer (total 384 heads across all layers = 48 × 8)\n- **GQA Ratio:** 5:1 (Group Query Attention)\n- **Query Heads:** 40 (5 × 8 = 40 query heads per layer)\n\nAdditional context from paper_framing.md shows Qwen2.5-7B has:\n- 28 layers × 112 KV heads = 3,136 total KV heads\n- GQA ratio: 7:1\n- Concentration: 0.61 (\"Spread\" pattern)\n\nThe 14B model (48L × 8KV) follows the same Qwen family architecture but is significantly larger.\n\n---\n\n### 3. REGISTRY FILE WITH EXPERIMENT STATUSES\n\n**Primary Registry File:**\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml` (49,827 tokens)\n\nThis file contains full experiment tracking with fields:\n- `exp_id`: experiment identifier\n- `status`: DONE, RUNNING, PENDING, ALLOCATED, QUEUED\n- `hypothesis`: what each experiment tests\n- `spec`: command, GPU, server, log path, model name, data details\n- `conclusion`: outcome and notes\n\n**Secondary Registry:**\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/dream_registry.yaml`\n\nThis tracks \"dream\" sessions (multi-agent paper writing/review runs):\n- Two dreams: `dream_20260514T002109` (status: done) and `dream_20260515T085855` (status: imagining)\n\n---\n\n### 4. PLANNING & PHASE DOCUMENTS\n\n**Primary Planning Document:**\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/ROADMAP.md`\n\nKey information:\n- **Current Phase:** 审稿响应 (Reviewer Response) — 补实验收尾 + 写作集成\n- **Submission Target:** EMNLP 2026 Main (ARR May 25, 2026)\n- **Reviewer Scores:** R1 2.5/5, R2 2/5 → Weak Reject (2.25/5)\n\n**W-Series Progress (Experiments Status):**\n- ✅ **W2**: 5/5 unconstrained baselines (gradient: 3.31× → 1.47× → 1.07-1.08×) — DONE\n- ✅ **W3**: 5/5 downstream eval — DONE\n- ✅ **W9**: compounding v2 (1.56-4.89× super-additivity) — DONE\n- 🔄 **W1**: Qwen2.5-14B profiling **RUNNING** (cuda:1, ~3h)\n- ⏳ **W4**: Qwen outlier analysis → Paper Agent writing\n\n**Other Planning Docs:**\n- `decisions.yaml` (54 entries) - Decision log with D001-D051+ tracking eviction pivot, metric changes, BOS bug fixes, GQA proxy insights\n- `paper_framing.md` (150+ lines) - Core narrative, claims, evidence summary\n- `IDEA_BRIEF.md` - Original project proposal with background\n\n**Timeline:** 10 days to submission with buffer of 5 days\n- Days 0-1: W1 profiling + OPT profiling + Gemma-2 constrained\n- Days 1-3: Paper Agent writing integration + W1 result incorporation\n- Days 3-4: Reference audit + final review\n- Days 4-5: Submit paper to review (continue mode)\n\n---\n\n### Quick Reference Paths:\n\n| Item | Path |\n|------|------|\n| Running experiments (checkpoint status) | `/ratekv/checkpoints/` |\n| Main registry | `/ratekv/registry.yaml` |\n| Dream registry | `/ratekv/dream_registry.yaml` |\n| Roadmap & planning | `/ratekv/ROADMAP.md` |\n| Decision log | `/ratekv/decisions.yaml` |\n| Core narrative | `/ratekv/paper_framing.md` |\n| Experiment scripts | `/ratekv/run_*.py` (likely location) |"
      }
    ],
    "totalDurationMs": 44234,
    "totalTokens": 56133,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5464,
      "cache_read_input_tokens": 48806,
      "output_tokens": 1857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5464
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1857,
          "cache_read_input_tokens": 48806,
          "cache_creation_input_tokens": 5464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5464,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 9,
      "searchCount": 8,
      "bashCount": 6,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "262c64b7-1556-45f4-8e85-846fc6221fe6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T09:23:07.189Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key information:

1. **Qwen2.5-14B**: 48 layers, 8 KV heads/layer, 384 total, GQA 5:1, **baseline PPL = 5.8432** (from checkpoint)
2. **gemma2_constrained_bos_fix**: RUNNING, 336 heads
3. **w1_qwen14b_hires_profiling**: RUNNING, baseline PPL = 5.8432

Important: the baseline PPL for 14B is **5.8432**, not 7.25 as I estimated. This is significantly lower, which makes sense for a larger model.
 
Now I'm recalculating the 14B projections with this corrected baseline. For the median tier with uniform 4-bit quantization, I need to estimate the degradation ratio—looking at the existing data points like Qwen-7B showing a 1.575× increase and Yi-9B showing only 1.029×, the 14B model likely falls somewhere in between, probably around 1.15-1.25×, which would put uniform quantization around 7.01 PPL.

Actually, reconsidering the Spread pattern concentration at 0.47 for the 14B, I think 1.30× is more realistic, giving me 7.59 PPL for uniform quantization. Then applying the 8% improvement from MCKP brings it down to 6.98 PPL, which represents a 61% recovery of the gap between baseline and uniform quantization.

But the recovery seems low at 34.9% when I divide by 1.75. Let me reconsider what baseline I'm actually using here. The checkpoint baseline_ppl of 5.8432 appears to be the calibration set perplexity, not the test set baseline. For Qwen-7B, the calibration baseline was around 8.82 while the test set baseline was 9.81, so these differ significantly. I should verify whether the other models like Yi-1.5 and Mistral are also showing calibration baselines rather than test set baselines in their checkpoints.

Looking at the calibration-to-test ratios across models, they're consistently lower on calibration sets. For Qwen-7B specifically, the ratio between test and calibration is about 1.11, so I can estimate the Qwen-14B test baseline should be around 7.0-7.5 based on similar model patterns. Looking at the test set perplexity for Qwen2.5-14B, I'd estimate around 6.78 based on the model's known performance—roughly 1.5-2.0 points lower than the 7B variant's 9.81 perplexity on WikiText-2.

But wait, that 9.81 for the 7B seems high depending on the evaluation settings. Let me use the calibration baselines as a reference point: the 14B calibration is about 33% lower than the 7B calibration, which would suggest the 14B test perplexity should be around 6.5-7.0 given our specific evaluation pipeline. I'm settling on 7.05 as the test baseline for Qwen2.5-14B and working through the quantization impact — uniform 4-bit degradation brings it to 8.81, then MCKP with 8% recovery gets it down to 8.11, which represents about 40% recovery of the degradation. Let me reconsider whether the uniform degradation for 14B should follow the same pattern as the 7B model. Now I'm calculating the MCKP improvement percentage differently—looking at the actual PPL values rather than trying to derive uniform first. For a 14B model with moderate degradation, I'll use a uniform value of 9.15 (about 1.30× the baseline of 7.05) and apply the 8% improvement target to get the MCKP result.

For the k ablation, I'm comparing the optimal head selection across model sizes—14B needs only about 3.1% of its heads at 2-bit precision compared to 7B's 7.1%, which makes sense since the larger model's sensitivity is more distributed across its architecture.

Now I'm working through the unconstrained baseline, estimating around 1.55× degradation for 14B, which gives a perplexity of 10.93. With these numbers locked in—baseline 7.05, uniform 4-bit at 9.15, MCKP at 8.42, and unconstrained at 10.93—I'm getting an 8% improvement with 34.8% recovery, but I should verify whether 9.15 is actually realistic for uniform 4-bit quantization by checking what other models show.

Looking at the cross-model data, Qwen-7B is a major outlier at 1.575× degradation, while most other models cluster tightly between 1.01-1.05×. Since my 14B model has borderline Spread characteristics (concentration 0.47 versus 7B's 0.61), the degradation ratio should fall somewhere between these extremes—probably around 1.10-1.20×, which would put uniform 4-bit at roughly 8.11 perplexity.

Now I'm working through what MCKP at 8% would achieve on that baseline. The absolute improvement is smaller than the 7B case—only 0.65 PPL points versus 4.5 for 7B—but the recovery rate of 61.3% is actually higher. This suggests the 14B model's borderline Spread status means quantization hits it less severely overall, so there's less room for MCKP to recover.

The key difference is that while Qwen-7B has a few extremely sensitive heads in L0 that dominate the degradation when forced to 4-bit, the 14B model likely has sensitivity spread across more heads with lower individual impact, making the uniform quantization hit less catastrophically.

I'm estimating the uniform 4-bit degradation for 14B at around 1.20× the baseline, which gives me 8.46 perplexity, and with MCKP recovery I'd get roughly 48% of the gap back.

Actually, let me reconsider this using the Qwen calibration data—the 14B model shows a 34% lower calibration perplexity compared to 7B, so if that ratio holds on the test set, my baseline should be closer to 6.50 rather than 7.05. That shifts everything down: uniform 4-bit would be 7.80, and MCKP at 8% improvement would bring it back down slightly.

Now I'm settling on these final numbers: baseline 6.50, uniform 7.80, MCKP 7.18 with 47.7% recovery. For the unconstrained case at 1.55× ratio I get 10.08, and looking at the k ablation across different head counts, the sweet spot appears to be k=12 where performance peaks before degrading slightly at k=16. The shallow U-shape confirms k=12 is optimal, with the bit distribution breaking down to 2-bit, 4-bit, and 8-bit tokens that average exactly 4.0 bits per token. Looking at the downstream evaluation metrics for the 14B model, the BF16 baselines are notably higher across all tasks, and I'm seeing how uniform quantization degrades performance—particularly on ARC-C where it drops from 0.565 to 0.548.

The MCKP approach recovers most of that loss, gaining back about 0.7 percentage points on average and achieving roughly 58% recovery of the gap between uniform and full precision. These results look solid, so I'm moving forward with writing out the YAML configuration. I need to be careful with the Gemma-2 BOS fix though—the baseline sits at 6.0306 while uniform quantization pushes it to 6.1, so I'll need to account for that shift. I'm verifying the baseline matches across sources — the BOS fix brought it down from 8.9 to 6.03, which is a substantial shift. For the constrained MCKP setup with this fix, I'm looking at whether k=8 (optimal from the old pipeline) still holds, though the profiling data shouldn't change even though evaluation metrics have shifted.

Since the profiles come from calibration data rather than the test set, the same allocation {2:8, 4:324, 8:4} would apply, giving a budget of 4.0 bits and a PPL around 6.19. Across the k ablation, all values cluster near the uniform result since head sensitivities are fairly consistent.

Now I'm finalizing the YAML with these numbers. I should also clarify what the user meant by "每个 planned 实验" — they're likely referring to experiments in the median tier narrative that are either completed or currently running, not just those listed in experiment_plan.yaml.

So I need to include the two RUNNING experiments from the registry, the natural follow-ups like the 14B constrained MCKP and k ablation studies, plus the analysis tasks. I'll skip OPT since it's not part of the median tier definition, and now I'm ready to structure the final YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e0e7164-8c2f-49b2-943d-726b5548ffb7",
  "isSidechain": false,
  "requestId": "req_011Cb47F8wLNbYZ94Hq3vpL2",
  "type": "assistant",
  "uuid": "a997f859-399e-4490-a48c-48c38f23040a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHDB5og3b3YKae7ubyveSZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2147,
      "cache_read_input_tokens": 81867,
      "output_tokens": 17853,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17853,
          "cache_read_input_tokens": 81867,
          "cache_creation_input_tokens": 2147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2147
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

_source line 24 · 2026-05-15T09:26:50.588Z_

Good — I have the key info. Qwen2.5-14B: 48L × 8KV = 384 heads, GQA 5:1, calibration baseline PPL = 5.8432. Now I'll build the complete prediction set.

```yaml
tier: median
narrative_guidance: >
  Claim 3 保持 "empirical decision rule"（不升级）。14B 作为 boundary case 
  单独一段讨论：threshold 是 soft boundary 而非 hard cutoff。
  Decision rule 5/6（14B 是 type-II error），承认 rule 是 directional heuristic，
  Limitation 明确写 "N=1 confirmed Spread; boundary behavior is continuous, not binary."
  三档标签仍可用但 threshold 软化（"approximately 0.50" → "in the range 0.45-0.55"）。
  Gemma-2 段落微调 BOS-fixed 数字但叙事不变。
  W9 super-additive 降为 empirical observation（图+描述性文字），不写 formal proposition。
  Contribution 重心从 "diagnostic" 向 "constraint as universal fix" 倾斜。
  仍可投 EMNLP Main。

imagined_experiments:

  # ────────────────────────────────────────
  # Experiment 1: Qwen2.5-14B hires profiling (RUNNING)
  # ────────────────────────────────────────
  - name: "Qwen2.5-14B hires 2-bit-only profiling"
    plan_id: "w1_qwen14b_hires_profiling"
    description: >
      High-resolution profiling (64 seq × 2048 tok) on Qwen2.5-14B (48L × 8KV = 384 heads, GQA 5:1).
      Measure per-head 2-bit distortion delta, compute concentration and t₁/t₅.
      Tests whether Qwen-7B's Spread pattern generalizes within family at larger scale.
    expected_results:
      calibration_baseline_ppl: 5.8432
      test_baseline_bf16_ppl: 6.50
      total_kv_heads: 384
      top5pct_n_heads: 19
      top5_concentration: 0.47
      t1_t5: 0.72
      delta_2bit_cv: 3.85
      l0_dominance_ratio: 0.38
      top1_head: "L0H0"
      top1_delta_2bit: 3.21
      top2_head: "L0H3"
      top2_delta_2bit: 2.78
      top3_head: "L0H5"
      top3_delta_2bit: 2.14
      top4_head: "L8H2"
      top4_delta_2bit: 1.82
      top5_head: "L0H1"
      top5_delta_2bit: 1.53
      l0_heads_in_top19: 5
      positive_delta_heads: 378
      distribution_shape: "diluted_spread"
      profiling_time_hours: 3.5
    result_rationale: >
      Qwen2.5-14B 同属 Qwen2.5 家族，L0 敏感 cluster 的 architectural pattern 大概率保留。
      但 14B 有 384 个 KV head（vs 7B 的 112），top-5% 从 ~6 heads 扩至 19 heads。
      L0 的 8 个 head 中 ~5 个出现在 top-19，但 L0 只占 top-19 的 26%（5/19），
      其余 14 头散布在中层（L5-L15），导致 concentration 从 7B 的 0.61 下降至 0.47——
      恰好落在 0.50 threshold 以下。
      同时，L0 内部虽有多头敏感，但最强头（L0H0, delta=3.21）相对 top-5 heads 的占比上升
      （t₁/t₅=0.72 vs 7B 的 0.57），因为中层 heads 稀释了 top-5 中非 L0 头的贡献。
      整体呈现 "diluted spread"：L0 cluster 存在但在全局分布中被稀释。
      CV=3.85 高于 flat 模型（Mistral 1.31, Gemma-2 1.28）但低于 7B 的数值，
      进一步佐证 heterogeneity 介于 Spread 和 Flat 之间。
    tables:
      - title: "Qwen2.5-14B top-10 sensitive heads (hires 2-bit delta)"
        columns: ["head", "delta_2bit"]
        rows:
          - ["L0H0",  3.21]
          - ["L0H3",  2.78]
          - ["L0H5",  2.14]
          - ["L8H2",  1.82]
          - ["L0H1",  1.53]
          - ["L12H6", 1.31]
          - ["L0H7",  1.18]
          - ["L5H4",  0.98]
          - ["L15H1", 0.87]
          - ["L0H2",  0.82]
    figures_description:
      - >
        Per-head 2-bit delta heatmap (48×8): L0 行有 4-5 个明显亮点但非全亮，
        L5-L15 中层有零星亮点。与 7B（L0 全亮、其余全暗）形成鲜明对比：
        14B 是 "渐变" 而非 "断崖"。
      - >
        Cumulative sensitivity curve: 斜率比 7B 平缓但比 Yi/Mistral/Gemma-2 陡，
        inflection point 在 top-5%（19 heads）处 — 14B 精确落在 7B 和 Flat 模型中间。
    analysis: >
      关键发现：concentration 0.47 和 t₁/t₅ 0.72 都恰好 miss joint condition
      （conc < 0.50 AND t₁/t₅ > 0.70）。这不是 Spread 也不是 Flat——
      是 "diluted spread"，joint condition 边界上的 continuous behavior。
      14B 的 GQA 5:1（vs 7B 的 7:1）可能是稀释的结构性因素之一：
      每层 8 个 KV heads 比 4 个更均匀，L0 cluster 效应被分散。

  # ────────────────────────────────────────
  # Experiment 2: Qwen2.5-14B constrained MCKP + k ablation
  # ────────────────────────────────────────
  - name: "Qwen2.5-14B constrained MCKP eval + k ablation"
    plan_id: "w1_qwen14b_constrained_mckp"
    description: >
      Constrained MCKP on Qwen2.5-14B at budget=0.25 (4× compression)。
      Sweep k ∈ {0,4,8,12,16,20,24,32,48} 寻找 optimal max_2bit。
      Verify greedy = MCKP at optimal k (solver equivalence).
    expected_results:
      baseline_bf16_ppl: 6.50
      uniform_4bit_ppl: 7.80
      uniform_baseline_ratio: 1.200
      constrained_mckp_ppl: 7.18
      mckp_improvement_over_uniform_pct: 7.9
      greedy_constrained_ppl: 7.18
      greedy_mckp_delta: 0.0000
      optimal_k: 12
      gap_recovery_pct: 47.7
      bit_distribution:
        "2": 12
        "4": 366
        "8": 6
      memory_ratio: 0.25
      k_ablation:
        k0:  7.80
        k4:  7.52
        k8:  7.28
        k12: 7.18
        k16: 7.21
        k20: 7.28
        k24: 7.38
        k32: 7.65
        k48: 8.42
    result_rationale: >
      Uniform 4-bit degradation ratio 1.20×——低于 7B 的 1.575× 但显著高于 Flat 模型的 1.01-1.05×。
      原因：14B 的 L0 cluster 虽然被稀释（concentration 0.47 vs 0.61），
      但仍包含 ~5 个高敏感头，被迫 4-bit 时产生可观的 degradation。
      MCKP 将 top-12 敏感头从 4-bit 降至 2-bit 并将 6 个最敏感头升至 8-bit，
      利用这部分 heterogeneity 获得 7.9% 改善——有意义但远低于 7B 的 27.3%。
      k-PPL curve 呈浅 U 型：minimum 在 k=12（≈top-5% 的 63%），
      compounding onset 在 k>32 后缓慢上升。U 型深度 (7.80-7.18=0.62) 远小于 7B 的 (15.45-10.91=4.54)，
      反映可利用的 sensitivity budget 更少。
      Solver equivalence 仍然成立（greedy = MCKP，Δ=0.0000），
      constraint 是 primary intervention 的 claim 在 14B 上同样成立。
      Recovery 47.7% 低于 7B 的 80.8%，与 concentration 的衰减定量一致。
    tables:
      - title: "Qwen2.5-14B k ablation (384 KV heads, budget=0.25)"
        columns: ["k (max_2bit)", "PPL", "note"]
        rows:
          - [0,  7.80, "= uniform 4-bit"]
          - [4,  7.52, ""]
          - [8,  7.28, ""]
          - [12, 7.18, "optimal ✓"]
          - [16, 7.21, ""]
          - [20, 7.28, ""]
          - [24, 7.38, ""]
          - [32, 7.65, "compounding visible"]
          - [48, 8.42, "compounding dominant"]
      - title: "Qwen2.5-14B allocation comparison"
        columns: ["method", "PPL", "vs uniform"]
        rows:
          - ["Baseline bf16",          6.50,  "—"]
          - ["Uniform 4-bit",          7.80,  "—"]
          - ["MCKP constrained k=12",  7.18,  "+7.9%"]
          - ["Greedy constrained k=12", 7.18, "Δ=0.0000 vs MCKP"]
    figures_description:
      - >
        k-PPL curve: 浅 U 型，minimum k=12，深度 0.62 PPL。
        与 7B 的深 U 型（深度 4.54 PPL）叠图对比，
        清晰展示 concentration 与 U 型深度的正相关。
    analysis: >
      7.9% 改善远超 noise range（Gemma-2 -0.35%, Mistral -0.48%），
      是 genuine positive signal。但也远低于 7B 的 27.3%——
      这正是 median tier 的核心预期：borderline positive，不足以升级 N=1 Spread claim。
      k=12 到 k=20 接近 plateau（PPL Δ < 0.10），说明 sensitivity 分布比 7B 更平滑。
      论文中 14B 应呈现为 "the benefit of non-uniform allocation degrades gracefully
      as concentration decreases, confirming the diagnostic as a continuous predictor
      rather than a binary classifier."

  # ────────────────────────────────────────
  # Experiment 3: Qwen2.5-14B unconstrained solver eval
  # ────────────────────────────────────────
  - name: "Qwen2.5-14B unconstrained solver eval"
    plan_id: "w1_qwen14b_unconstrained"
    description: >
      Run unconstrained greedy and MCKP on Qwen2.5-14B.
      Measure compounding degradation, 2-bit head count, and ratio vs baseline.
    expected_results:
      baseline_bf16_ppl: 6.50
      uniform_4bit_ppl: 7.80
      greedy_unconstrained_ppl: 10.15
      mckp_unconstrained_ppl: 10.35
      greedy_ratio_vs_baseline: 1.562
      mckp_ratio_vs_baseline: 1.592
      n_2bit_greedy: 58
      n_2bit_mckp: 62
      pct_2bit_greedy: 15.1
      pct_2bit_mckp: 16.1
      greedy_bit_distribution:
        "2": 58
        "4": 318
        "8": 6
        "16": 2
      constrained_improvement_vs_unconstrained_pct: 29.3
    result_rationale: >
      Concentration 0.47 使 unconstrained 表现落在 Qwen-7B 的 catastrophic（3.31×）
      和 Spike/Flat 的 mild（1.07-1.08×）之间。
      Solver 仍然 over-allocate 2-bit：profiler 对大部分中间层 heads 给出相似的低 delta，
      solver 将 ~58 头（15.1%）降为 2-bit——比 Gemma-2 的 31.5% 少
      （14B 有更多 "中等但非零" 差异供 solver 利用），但比 Yi 的 11.5% 多。
      58 个 2-bit heads 的 compounding effect 产生 ~1.56× degradation——moderate 级别，
      与 Gemma-2（1.47×）处于同一档。
      Constraint 将 PPL 从 10.15 降至 7.18（改善 29.3%），
      证明 constraint 在 moderate degradation 区间也有显著价值——
      不只是 catastrophic 场景（7B）的 "急救"，也是 moderate 场景的 "优化"。
    tables:
      - title: "Qwen2.5-14B unconstrained vs constrained comparison"
        columns: ["method", "PPL", "×baseline", "2-bit heads (%)"]
        rows:
          - ["Baseline bf16",          6.50,   "1.00×", "—"]
          - ["Uniform 4-bit",          7.80,   "1.20×", "0 (0%)"]
          - ["Greedy unconstrained",   10.15,  "1.56×", "58 (15.1%)"]
          - ["MCKP unconstrained",     10.35,  "1.59×", "62 (16.1%)"]
          - ["Greedy constrained k=12", 7.18,  "1.10×", "12 (3.1%)"]
          - ["MCKP constrained k=12",  7.18,   "1.10×", "12 (3.1%)"]
    figures_description: []
    analysis: >
      14B 的 1.56× 填补三档分类的关键空白：
      现有 "moderate" 只有 Gemma-2（1.47×），14B 提供第二个数据点（1.56×），
      使 catastrophic（3.31×）- moderate（1.47-1.56×）- mild（1.07-1.08×）更 robust。
      论文叙事：14B 和 Gemma-2 的 moderate degradation 虽然成因不同
      （14B = diluted spread compounding, Gemma-2 = flat over-allocation），
      但 constraint 在两者上都有效——strengthens "universal fix" 的 claim。
      注意 greedy ≠ MCKP（10.15 vs 10.35），unconstrained 时 solver choice matters；
      但 constrained 后 greedy = MCKP（Δ=0.0000）。这与 7B 的模式完全一致。

  # ────────────────────────────────────────
  # Experiment 4: Qwen2.5-14B downstream eval
  # ────────────────────────────────────────
  - name: "Qwen2.5-14B downstream task eval"
    plan_id: "w1_qwen14b_downstream"
    description: >
      Downstream evaluation (ARC-C, HellaSwag, PIQA, WinoGrande) on Qwen2.5-14B,
      0-shot, at 4× compression. Validates whether 7.9% PPL improvement translates to downstream.
    expected_results:
      baseline_avg: 0.721
      uniform_avg: 0.709
      mckp_avg: 0.716
      mckp_vs_uniform_avg_pp: 0.7
      recovery_pct: 58.3
      per_task:
        arc_challenge:
          baseline: 0.565
          uniform: 0.548
          mckp: 0.557
          delta_pp: 0.9
        hellaswag:
          baseline: 0.800
          uniform: 0.785
          mckp: 0.793
          delta_pp: 0.8
        piqa:
          baseline: 0.805
          uniform: 0.798
          mckp: 0.802
          delta_pp: 0.4
        winogrande:
          baseline: 0.715
          uniform: 0.705
          mckp: 0.712
          delta_pp: 0.7
    result_rationale: >
      PPL 7.9% 改善在 downstream 上转化为平均 +0.7pp。
      Qwen-7B 的 scaling 参考：27.3% PPL → +2.6pp downstream（ratio ~0.095pp/1% PPL）。
      14B 的 7.9% PPL → 预期 ~0.75pp，实际约 +0.7pp，高度一致。
      所有 4 个 task 都是正 delta（+0.4 到 +0.9pp），这与 7B 的全正模式一致，
      但幅度约为 7B 的 1/3——与 concentration 衰减的预期匹配。
      ARC-C 和 HellaSwag 受益最大（reasoning-heavy tasks 对 KV cache 质量更敏感），
      PIQA 最小（较简单的 commonsense，对 subtle cache 差异不敏感）。
      关键问题：+0.7pp 均值没有 multi-seed CI，单 run noise ~±0.5pp，
      所以 "positive signal" 有 significance 风险。
      论文措辞应 hedge："shows modest but consistent positive delta across all four tasks."
    tables:
      - title: "Qwen2.5-14B downstream task results (0-shot, 4× compression)"
        columns: ["Task", "BF16 Baseline", "Uniform 4-bit", "MCKP k=12", "Δ (pp)"]
        rows:
          - ["ARC-Challenge", 0.565, 0.548, 0.557, "+0.9"]
          - ["HellaSwag",     0.800, 0.785, 0.793, "+0.8"]
          - ["PIQA",          0.805, 0.798, 0.802, "+0.4"]
          - ["WinoGrande",    0.715, 0.705, 0.712, "+0.7"]
          - ["Average",       0.721, 0.709, 0.716, "+0.7"]
    figures_description: []
    analysis: >
      14B downstream 支持 "diagnostic correctly predicts downstream" 的 claim：
      borderline PPL → borderline downstream。关键对比：
      - 7B (Spread, conc=0.61): avg +2.6pp, all positive, 72.8% recovery
      - 14B (diluted spread, 0.47): avg +0.7pp, all positive, 58.3% recovery  
      - Yi/Llama/Mistral (Spike/Flat): avg -0.48 to -0.99pp, mixed signs
      14B 的 "all positive but modest" 精确落在 Spread 和 non-Spread 之间，
      与 concentration gradient 叙事完全吻合。
      但必须在论文中标注："without multi-seed confidence intervals, 
      the per-task deltas (+0.4 to +0.9pp) are within typical single-run noise."

  # ────────────────────────────────────────
  # Experiment 5: Gemma-2 constrained MCKP with BOS fix (RUNNING)
  # ────────────────────────────────────────
  - name: "Gemma-2-9B constrained MCKP with BOS fix"
    plan_id: "gemma2_constrained_bos_fix"
    description: >
      Re-evaluate constrained MCKP on Gemma-2-9B using corrected BOS-prepend 
      sliding-window evaluation (stride=512, max_length=2048)。
      Replaces old numbers (baseline=8.9, mckp=9.05) that were affected by BOS bug.
    expected_results:
      baseline_bf16_ppl: 6.0306
      uniform_4bit_ppl: 6.1683
      constrained_mckp_ppl: 6.19
      mckp_vs_uniform_pct: -0.35
      best_k: 8
      bit_distribution:
        "2": 8
        "4": 324
        "8": 4
      memory_ratio: 0.25
      unconstrained_greedy_ppl: 8.85
      unconstrained_ratio: 1.467
      k_ablation:
        k0:  6.17
        k4:  6.17
        k8:  6.19
        k12: 6.22
        k16: 6.25
        k24: 6.31
    result_rationale: >
      Gemma-2 的 flat 分布（concentration 0.23, CV 1.28）意味着 profiler 
      几乎无法区分 heads。MCKP 选出的 8 个 2-bit 头实质上是 "noise-driven"——
      sensitivity delta 差异太小，任何选择都无法带来有意义的优化。
      PPL 6.19 vs uniform 6.17（-0.35%）完全在 noise 范围内。
      k-PPL 近似单调递增（像 Mistral），因为每增加一个 2-bit head 都是 "equal damage"。
      BOS fix 大幅改变 absolute PPL（8.9→6.03）但不改变 relative conclusions。
      unconstrained ratio 1.47× 已在 w2_unconstrained_v2 中确认（BOS-fixed 数据），
      不需要修改。
      此实验主要价值：提供 BOS-fixed constrained baseline 替换论文旧数字。
      三档分类中的 "moderate" 标签不变，因为 1.47× 是 unconstrained 的数字（已有）。
    tables:
      - title: "Gemma-2-9B BOS-fixed results summary"
        columns: ["method", "PPL", "note"]
        rows:
          - ["Baseline bf16",              6.03,  "BOS-fixed ✓"]
          - ["Uniform 4-bit",              6.17,  "BOS-fixed ✓"]
          - ["MCKP constrained k=8",       6.19,  "-0.35% vs uniform"]
          - ["Greedy unconstrained",       8.85,  "1.47× baseline (from w2_v2)"]
          - ["Old baseline (BOS bug)",     8.90,  "deprecated"]
          - ["Old MCKP (BOS bug)",         9.05,  "deprecated"]
      - title: "Gemma-2-9B k ablation (BOS-fixed, 336 heads)"
        columns: ["k", "PPL", "note"]
        rows:
          - [0,  6.17, "= uniform"]
          - [4,  6.17, "≈ uniform"]
          - [8,  6.19, "best k (marginal)"]
          - [12, 6.22, ""]
          - [16, 6.25, ""]
          - [24, 6.31, "monotonic increase"]
    figures_description:
      - >
        k-PPL curve: 近单调递增，从 6.17（k=0）到 6.31（k=24），
        斜率极平。与 Qwen-7B 的深 U 型形成极端对比。
        论文中可与 Mistral（也是单调）并排展示。
    analysis: >
      BOS fix 后 Gemma-2 constrained 结果确认论文两个关键叙事：
      (1) Flat distribution → MCKP 无益（-0.35% ≈ noise）
      (2) Constraint 仍有 universal value：unconstrained 1.47× → constrained ≈ uniform，
          prevents 106→8 heads at 2-bit 的 over-allocation。
      论文需更新的数字：Table 2 的 Gemma-2 行从 (8.9/9.03/9.05) 改为 (6.03/6.17/6.19)。
      Cross-architecture table 的 constrained vs uniform 从 "-0.3%" 改为 "-0.35%"（几乎不变）。
      下游指标不需要重测（W3 的下游 eval 用的是独立 pipeline，不受 BOS 影响）。

  # ────────────────────────────────────────
  # Experiment 6: Decision rule revalidation (6 models)
  # ────────────────────────────────────────
  - name: "Decision rule revalidation with 6 models"
    plan_id: "decision_rule_6model"
    description: >
      Revalidate joint diagnostic (concentration ≳0.50 AND t₁/t₅ ≲0.70)
      with Qwen2.5-14B as sixth model. Assess accuracy and boundary behavior.
    expected_results:
      rule_accuracy_hard: "5/6"
      rule_accuracy_non_borderline: "5/5"
      n_borderline_cases: 1
      borderline_model: "Qwen2.5-14B"
      borderline_conc: 0.47
      borderline_t1t5: 0.72
      borderline_actual_improvement_pct: 7.9
      rule_prediction_for_14b: "non-beneficial"
      error_type: "type-II (false negative)"
      softened_threshold_conc: "0.45-0.55"
      softened_threshold_t1t5: "0.65-0.75"
    result_rationale: >
      14B 的 concentration 0.47（<0.50）和 t₁/t₅ 0.72（>0.70）使其在 hard threshold 下
      被分类为 non-beneficial，但实际 7.9% 改善是 genuine positive。
      Type-II error（false negative）——rule 过于保守。
      但 14B 恰好落在两个 threshold 的边界（0.47 vs 0.50, 0.72 vs 0.70，各差 0.03 和 0.02），
      说明 threshold 是 soft boundary 而非 hard cutoff。
      这实际上 STRENGTHENS 而非 weakens 论文叙事：
      (a) 5/5 non-borderline accuracy 完美——rule 对 "clear cases" 100% 正确
      (b) Boundary case 的 7.9% 改善介于 Spread（27%）和 non-Spread（≤0.2%）之间——
          continuous behavior 符合 physical intuition
      (c) 承认 soft boundary 比 claim hard cutoff 更 scientifically honest → reviewer credibility
      Decision rule 的 practical value 不减：practitioners 用 rule 筛选 "是否值得投入 MCKP"，
      boundary case 的 7.9% 改善虽然 positive 但可能不 justify profiling cost（7B 级别才值得）。
    tables:
      - title: "Joint diagnostic evaluation across 6 architectures"
        columns: ["Model", "GQA", "Conc.", "t₁/t₅", "Shape", "MCKP Δ", "Rule prediction", "Correct?"]
        rows:
          - ["Qwen2.5-7B",   "7:1", 0.61, 0.57, "Spread",          "+27.3%",  "beneficial",     "✅"]
          - ["Yi-1.5-9B",    "8:1", 0.71, 0.90, "Spike",           "≈0%",     "non-beneficial",  "✅"]
          - ["Llama-3.1-8B", "4:1", 0.57, 0.71, "Spike (border)",  "+0.2%",   "non-beneficial",  "✅"]
          - ["Mistral-7B",   "4:1", 0.22, 0.18, "Flat",            "-0.4%",   "non-beneficial",  "✅"]
          - ["Gemma-2-9B",   "2:1", 0.23, 0.38, "Flat",            "-0.35%",  "non-beneficial",  "✅"]
          - ["Qwen2.5-14B",  "5:1", 0.47, 0.72, "Diluted Spread",  "+7.9%",   "non-beneficial",  "❌ (boundary)"]
    figures_description:
      - >
        2D scatter: X=concentration, Y=t₁/t₅. 6 models color-coded by actual benefit magnitude。
        Threshold quadrant 线 at conc=0.50 和 t₁/t₅=0.70。
        14B 标注 boundary zone (shaded rectangle 0.45-0.55 × 0.65-0.75)。
        Qwen-7B (green) 在右下象限（高 conc + 低 t₁/t₅ = Spread），其余 5 个在其他象限。
        14B (yellow) 恰在交界处。
    analysis: >
      论文措辞建议（median tier）：
      - 不说 "5/6 accuracy"——框架为：
        "The rule correctly classifies all five non-borderline architectures.
        Qwen2.5-14B falls in the boundary zone (concentration=0.47, t₁/t₅=0.72)
        with a modest 7.9% benefit, illustrating that the diagnostic thresholds
        represent soft boundaries rather than hard cutoffs."
      - Threshold 从 "≳0.50" 软化为 "in the range 0.45-0.55"
      - Claim 3 不升级——仍是 "empirical decision rule"
      - Limitation: "validated on 6 architectures with N=1 confirmed Spread (Qwen2.5-7B);
        the boundary case (14B) provides directional evidence that benefit degrades
        continuously with concentration."
      Concentration-benefit gradient 的 6 个数据点：
      0.22 → -0.4%, 0.23 → -0.35%, 0.47 → +7.9%, 0.57 → +0.2%, 0.61 → +27.3%, 0.71 → ≈0%。
      非单调（Yi-1.5 的 0.71 / 0% 打破单调）正是 t₁/t₅ 作为 second dimension 的 justification。

  # ────────────────────────────────────────
  # Experiment 7: W9 compounding super-additivity observation
  # ────────────────────────────────────────
  - name: "W9 compounding super-additivity formalization"
    plan_id: "w9_compounding_observation"
    description: >
      不需要新实验——基于 w9_compounding_v2 已有数据，
      将 super-additive compounding trend 形式化为 empirical observation（非 proposition）。
      评估 variance 和 formalization 适当程度。
    expected_results:
      # 以下全为已有数据，此处重新组织用于论文呈现
      k64_topk_ppl: 22.946
      k64_randomk_ppl: 55.94
      k64_randomk_std: 9.73
      k64_randomk_topk_ratio: 2.44
      k32_randomk_topk_ratio: 1.58
      k16_randomk_topk_ratio: 1.24
      k8_randomk_topk_ratio: 1.10
      ratio_trend: "monotonically increasing from 1.01 (k=1) to 2.44 (k=64)"
      variance_assessment: "high — k64 randomk std=9.73 (17.4% CV)"
      formalization_level: "observation (figure + descriptive text)"
    result_rationale: >
      W9 数据展示明确的 super-additive trend：随 k 增大，
      random-k 的 PPL 增长快于 top-k，randomk/topk ratio 单调递增
      （1.01 → 1.10 → 1.24 → 1.58 → 2.44）。
      但以下因素阻止 formal proposition：
      (a) 仅在 Qwen-7B 一个模型上测试——n=1 不足以 generalize
      (b) k=64 的 randomk std=9.73（PPL range ~46-66），variance 极大
      (c) ratio 的增长 pattern（k=32: 1.58 → k=64: 2.44 跳跃大）
          可能部分来自 evaluation saturation（极高 PPL 区间 noise 大）
      Median tier 的 ratio range [1.5, 2.5] 包含实际的 2.44——
      但 2.44 接近上界且 high variance，说明 point estimate 不可靠。
      论文处理：Analysis 章节放 Figure + 2-3 句描述，
      不给 Proposition 编号，不写 formal bound。
      如 reviewer 追问，指向 "future work: cross-architecture compounding characterization."
    tables:
      - title: "Compounding super-additivity: random-k vs top-k (Qwen2.5-7B)"
        columns: ["k", "top-k PPL", "random-k PPL (mean±std)", "ratio (random/top)"]
        rows:
          - [1,  9.826,  "9.887±0.05",  1.01]
          - [4,  9.849,  "10.06±0.06",  1.02]
          - [8,  10.042, "11.07±0.69",  1.10]
          - [16, 10.42,  "12.91±0.40",  1.24]
          - [32, 11.604, "18.33±2.53",  1.58]
          - [64, 22.946, "55.94±9.73",  2.44]
    figures_description:
      - >
        双线图 + error bars：X 轴 k（log scale），Y 轴 PPL。
        top-k 线（实线，narrow error bars）和 random-k 线（虚线，宽 error bars）。
        Gap 随 k 单调增大，error bars 在 k≥32 后急剧扩大。
        标注 ratio at each k。右侧 inset 小图：ratio vs k（同样单调递增）。
    analysis: >
      论文措辞建议：
      "We observe that assigning randomly-selected heads to 2-bit produces
      disproportionately worse perplexity than assigning the highest-sensitivity
      heads, and this gap widens monotonically with the number of 2-bit heads
      (Figure X). At k=64, random selection yields 2.44× the degradation of
      sensitivity-ranked selection. This super-additive behavior motivates
      the cardinality constraint: by limiting the number of extreme-quantization
      assignments, the constraint prevents compounding from low-sensitivity heads
      that individually appear harmless but collectively degrade quality."
      不写 "Observation 1:" 或 "Finding:" 的 formal header——
      integrate into Analysis 段落的 descriptive text 中。

  # ────────────────────────────────────────
  # Experiment 8: Paper-level synthesis (14B integration)
  # ────────────────────────────────────────
  - name: "Qwen2.5-14B paper narrative integration"
    plan_id: "w1_qwen14b_paper_integration"
    description: >
      将 14B 全部结果整合进论文叙事。
      14B 作为 "boundary case study" 在 Analysis section 单独一段。
      更新 cross-architecture table 和 decision rule discussion。
    expected_results:
      cross_architecture_table_new_row:
        model: "Qwen2.5-14B"
        gqa: "5:1"
        kv_heads: 384
        concentration: 0.47
        unconstrained_ratio: "1.56×"
        constrained_vs_uniform: "+7.9% (7.18 vs 7.80)"
        shape: "Diluted Spread"
        verdict: "⚠️ Boundary positive"
      three_tier_classification:
        catastrophic: ["Qwen2.5-7B (3.31×)"]
        moderate: ["Gemma-2-9B (1.47×)", "Qwen2.5-14B (1.56×)"]
        mild: ["Yi-1.5-9B (1.08×)", "Llama-3.1-8B (1.07×)", "Mistral-7B (1.08×)"]
      claim_updates:
        claim1: "STRENGTHENED — third distribution shape (diluted spread) adds taxonomic depth"
        claim2: "STRENGTHENED — constraint effective on moderate cases, not just catastrophic"
        claim3: "MAINTAINED — empirical decision rule, 5/5 non-borderline correct, boundary discussed"
      contribution_reweight:
        primary: "Cardinality constraint as universal fix (all 6 models benefit from constraint)"
        secondary: "Concentration-based diagnostic (5/5 non-borderline, boundary continuous)"
        tertiary: "Boundary behavior analysis (14B as case study for soft thresholds)"
      limitation_additions:
        - "N=1 confirmed Spread; boundary behavior continuous, not binary"
        - "14B downstream improvement (+0.7pp avg) lacks multi-seed CI"
        - "GQA 5:1 (14B) is untested in prior work — dilution mechanism is hypothesis"
    result_rationale: >
      14B 在 median tier 下不能升级 claim（N 仍为 1）但增加了三个维度的 depth：
      (1) Concentration-benefit gradient：6 个数据点比 5 个更密，
          尤其 0.47 填补了 0.23 (Flat) 和 0.61 (Spread) 之间的空白。
          Gradient 叙事："benefit varies continuously with concentration"
          现在有 6 个 data points 而非 5 个。
      (2) 三档分类 "moderate" 从 n=1（Gemma-2 only）变为 n=2（+14B），
          且两者成因不同——增加了分类的 robustness 和解释力。
      (3) Decision rule 的 "soft boundary" 讨论是 14B 独特贡献，
          5 个模型看不出来——必须有一个 boundary case 才能展示 continuity。
      整体 EMNLP Main 可投性评估（median tier）：
      - 最可能的 reviewer 攻击点从 "N=1 Spread" 转向 "boundary needs formal treatment"
      - 后者更容易 defend：can point to continuous gradient + acknowledged as future work
      - Contribution 重心调整到 constraint universality 后，
        即使 diagnostic 被 reviewer 质疑为 "n=6 too small"，
        constraint 贡献独立于样本量。
    tables:
      - title: "Updated cross-architecture evidence summary (6 models)"
        columns: ["Model", "GQA", "KV Heads", "Conc.", "Uncons. ×base", "Constrained Δ", "Shape", "Verdict"]
        rows:
          - ["Qwen2.5-7B",   "7:1", 112, 0.61, "3.31×", "+27.3%",  "Spread",          "✅ Strong positive"]
          - ["Qwen2.5-14B",  "5:1", 384, 0.47, "1.56×", "+7.9%",   "Diluted Spread",  "⚠️ Boundary positive"]
          - ["Yi-1.5-9B",    "8:1", 192, 0.71, "1.08×", "≈0%",     "Spike",           "❌ GQA counterexample"]
          - ["Llama-3.1-8B", "4:1", 256, 0.57, "1.07×", "+0.2%",   "Spike (border)",  "≈ Marginal"]
          - ["Mistral-7B",   "4:1", 256, 0.22, "1.08×", "-0.4%",   "Flat",            "❌ Negative"]
          - ["Gemma-2-9B",   "2:1", 336, 0.23, "1.47×", "-0.35%",  "Flat",            "❌ Strongest negative"]
    figures_description:
      - >
        Concentration vs MCKP improvement scatter (6 models)。
        X 轴 concentration, Y 轴 improvement %。
        14B（黄色三角）标注 boundary zone。
        Qwen-7B（绿色圆）在右上，Flat 模型（红色方）在左下。
        14B 精确落在中间位置。
        可选：拟合 trend line（排除 Yi-1.5 outlier），展示 positive correlation。
    analysis: >
      Median tier 总评：
      论文 contribution 三层递进成立：
      L1 — Constraint works everywhere（6/6 models）: undeniable, pure engineering value。
      L2 — Diagnostic separates clear cases（5/5 non-borderline）: useful practical rule。
      L3 — Boundary behavior is continuous（14B case study）: adds analytical depth。
      如果 reviewer 接受 L1 和 L2，论文就能过。L3 是 bonus depth。
      与 optimistic tier 的关键差距：无法升级到 "diagnostic framework"（N=1 Spread 不变）。
      与 pessimistic tier 的关键差距：14B 的 positive signal 虽 modest 但 consistent across tasks，
      不至于 invalidate diagnostic——最坏情况是 soft boundary，不是 wrong boundary。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a997f859-399e-4490-a48c-48c38f23040a",
  "isSidechain": false,
  "requestId": "req_011Cb47F8wLNbYZ94Hq3vpL2",
  "type": "assistant",
  "uuid": "3d01daf6-161a-4943-bcee-b8d385274bda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHDB5og3b3YKae7ubyveSZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2147,
      "cache_read_input_tokens": 81867,
      "output_tokens": 17853,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17853,
          "cache_read_input_tokens": 81867,
          "cache_creation_input_tokens": 2147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2147
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Qwen2.5-14B 边界/弱阳性，N 实质仍为 1；其余数据基本一致但有小幅偏差需要对齐 核心假设：['Qwen2.5-14B concentration 0.40-0.55 或 t₁/t₅ 0.65-0.80（边界区间，不完全满足 joint condition）', 'Qwen2.5-14B MC…",
  "leafUuid": "3d01daf6-161a-4943-bcee-b8d385274bda",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Concentration-dependent KV cache quantization across five model architectures",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Qwen2.5-14B 边界/弱阳性，N 实质仍为 1；其余数据基本一致但有小幅偏差需要对齐 核心假设：['Qwen2.5-14B concentration 0.40-0.55 或 t₁/t₅ 0.65-0.80（边界区间，不完全满足 joint condition）', 'Qwen2.5-14B MC…",
  "leafUuid": "3d01daf6-161a-4943-bcee-b8d385274bda",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Concentration-dependent KV cache quantization across five model architectures",
  "sessionId": "381281cc-1805-4751-910c-f2c4d66fa847"
}
```

---
