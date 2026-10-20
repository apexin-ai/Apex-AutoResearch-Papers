# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：三条 claim 全部成立，reviewer 认可 compounding 发现的新颖性和 constraint 的实用价值，1/8 benefit 被

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/ef6aff79-615e-462c-9b0b-b3504a778d9b.jsonl`
- **Structured JSON:** [`e6fb93423b656d0188c8.json`](../../sessions/e6/e6fb93423b656d0188c8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T02:16:38.243Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T02:16:38.243Z",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：三条 claim 全部成立，reviewer 认可 compounding 发现的新颖性和 constraint 的实用价值，1/8 benefit 被视为诚实的 negative result 而非弱点\n核心假设：['A1: 2-bit compounding 在 KV cache 文献中确实未被系统刻画（novelty 成立）', 'A2: 8/8 架构全部复现 unconstrained degradation（universality 被接受）', 'A3: cardinality constraint 被视为 principled intervention（非 trivial heuristic），因为 solver equivalence (Δ=0.0000) 证明了 constraint 才是核心', 'A4: 1/8 benefit + 7/8 negative 被视为对 field 隐含假设的重要修正', 'A5: diagnostic (9/9 accuracy) 作为 testable hypothesis 被接受，不需要统计显著性', 'A6: RateQuant 区分清晰——polymatroid 在 {2,4,8,16} 上 breaks 这一点被认可']\n关键指标范围：{'avg_review_score_arr': [3.5, 4.0], 'claims_surviving_intact': [3, 3], 'p_accept_emnlp_main': [0.4, 0.6], 'major_reviewer_objections': [0, 1], 'narrative_rewrite_pct': [0, 10], 'unconstrained_degradation_universality': [8, 8], 'solver_equivalence_delta': [0.0, 0.001], 'diagnostic_accuracy': [8, 9], 'downstream_consistency_with_ppl': [5, 5]}\n叙事方向：原始 framing 完全成立。Title: \"2-Bit Compounding: A Universal Failure Mode in Per-Head KV Cache Quantization\"。 三条 claim 原样保留：(1) compounding 是 universal failure mode，(2) cardinality constraint 是 universal fix 且 solver-agnostic，(3) non-uniform rarely helps + diagnostic。 Reviewer 可能要求增加 1-2 个模型或 error bar 作为 minor revision，但核心叙事不需调整。 长上下文结果 (11.15× vs 1.23×) 作为 deployment motivation 的 headline 数字。 Qwen 是 showcase，7/8 negative 是 contribution 的一部分。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ratekv\nfocus: Evaluate the compounding-forward framing: core contribution is 2-bit compounding as universal failure mode + constraint as universal fix + \"non-uniform rarely helps\" as key negative result. N=1 Spread is a feature (7/8 don't need non-uniform) not a bug. Compare with concentration-dependent framing where N=1 was a weakness.\n\n## paper_framing.md\n\n# Paper Framing — ratekv\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)\n- Track: Efficient Methods for NLP\n\n## bf16 Consistency Resolution (2026-05-14)\n\n**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。\n\n**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。\n\n| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |\n|------|---------------------|----------------------|-----------|\n| Baseline | **9.8106** | 8.819 | 9.81 |\n| Uniform 4-bit | **15.4454** | — | 15.45 |\n| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |\n| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |\n\n## Core Insight\n\nPer-head KV cache quantization on hardware-aligned bit-widths {2,4,8,16} has an unreported universal failure mode: 2-bit quantization distortions compound non-additively through the residual stream, causing ALL tested unconstrained solvers (greedy, MCKP) to systematically over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 architectures (1.07×–3.31× baseline). A cardinality constraint (≤k heads at 2-bit) universally prevents this over-allocation, and furthermore reduces the feasible set to where solver choice becomes irrelevant (greedy = MCKP, Δ=0.0000). Under moderate compression (4×), only 1/8 architectures benefits from non-uniform allocation over uniform 4-bit — providing the first empirical evidence that the implicit assumption \"non-uniform is always better than uniform\" is wrong in KV cache quantization. The core contribution is the compounding effect discovery + universal constraint fix, not the allocation algorithm.\n\n## Core Claims (3 条)\n\n1. **2-bit compounding is a universal failure mode for unconstrained per-head allocation**: On hardware-aligned non-consecutive bit-widths {2,4,8,16}, per-head independent profiling distortions compound non-additively when multiple heads are simultaneously assigned 2-bit quantization. This causes ALL tested unconstrained solvers to over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 diverse architectures (Qwen 3.31×, Gemma-2 1.47×, Yi 1.08×, Llama 1.07×, Mistral 1.08×, Pythia, Qwen-14B, Phi-3-medium). Quantitative evidence of non-additivity: per-head profiling predicts joint PPL ≈11 but actual joint 2-bit PPL is 32–37 (3× prediction error). This is the first systematic characterization of compounding effects in per-head KV cache quantization. Long-context amplifies the failure: at 8K tokens, uniform 4-bit degrades 11.15× baseline while constrained MCKP degrades only 1.23× — a 9× gap in degradation rate.\n\n2. **A cardinality constraint is the universal fix — and makes solver choice irrelevant**: A simple cardinality constraint (max_2bit ≤ k) is sufficient to prevent compounding across ALL tested architectures. Three universally beneficial properties: (a) prevents catastrophic over-allocation on sensitive architectures (Qwen: 32.45 → 10.91), (b) prevents moderate over-allocation on flat architectures (Gemma-2: 8.85 → 6.17, reducing 2-bit heads from 106 to 8), (c) reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce IDENTICAL bit allocations and PPL (Δ=0.0000). The constraint is parameterizable via small-scale compounding test (k≤8 universally safe: <2.5% degradation across all architectures). Practical implication: practitioners need only add one integer parameter to existing pipelines.\n\n3. **Non-uniform allocation benefit is rare — most models should use uniform 4-bit**: Under moderate compression (4×), only 1/8 tested architectures (Qwen2.5-7B, \"spread\" sensitivity pattern) benefits from non-uniform allocation (+27.3% PPL, +1.9pp downstream avg). The remaining 7/8 show no benefit or minor degradation (<1pp avg downstream). A 2-metric empirical diagnostic (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly classifies all 9 tested models (9/9 accuracy), providing practitioners a simple check: if the diagnostic says \"no\" — skip profiling and use uniform 4-bit with zero quality loss. This is the first systematic study of *when* non-uniform KV cache quantization is beneficial, correcting the implicit assumption that it always helps.\n\n## Story Spine\n\n- **Problem**: Per-head mixed-precision KV cache quantization promises better quality-compression tradeoffs than uniform bit-width. But on hardware-aligned non-consecutive bit-widths {2,4,8,16}, we discover that existing allocation algorithms (greedy, MCKP) systematically FAIL — producing worse results than naive uniform 4-bit across ALL tested architectures. The failure mode is unreported: 2-bit quantization distortions compound non-additively, and solvers consistently over-allocate 2-bit heads. Meanwhile, the field implicitly assumes non-uniform allocation always helps, but no systematic study has tested this across architectures.\n\n- **Existing approaches & gaps**: RateQuant provides R-D optimal per-head allocation via continuous closed-form and discrete greedy (optimal on consecutive integers {2,...,6}). KIVI and ARKV apply uniform or heuristic mixed-precision. However, on hardware-aligned {2,4,8,16}: (a) RateQuant's greedy produces PPL 32.45 vs optimal ~10.91 — polymatroid optimality breaks, (b) unconstrained MCKP fares even worse (PPL 36.92) due to compounding, (c) NO prior work addresses *when* non-uniform allocation is actually beneficial vs when uniform suffices.\n\n- **Our framing**: We present three contributions: (1) the first characterization of 2-bit compounding effects in per-head KV cache quantization — showing that profiling non-additivity causes ALL unconstrained solvers to fail on {2,4,8,16} across 8/8 architectures; (2) a simple universal fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding, makes solver choice irrelevant (greedy=MCKP, Δ=0.0000), and is safely parameterizable (k≤8 universally safe); (3) the first systematic study of *when* non-uniform allocation helps — answer: rarely (1/8 architectures at moderate compression), with a 2-metric diagnostic (9/9 correct) that tells practitioners whether to invest in profiling or just use uniform 4-bit.\n\n- **Headline result template**: \"We show that per-head KV cache quantization on hardware-aligned bit-widths has a universal failure mode: 2-bit distortions compound non-additively, causing ALL unconstrained solvers to underperform uniform 4-bit across 8 architectures. A cardinality constraint (≤k heads at 2-bit) universally fixes this, making solver choice irrelevant (greedy=MCKP, Δ=0.0000). Surprisingly, under moderate compression, only 1/8 architectures benefits from non-uniform allocation at all — most models should simply use uniform 4-bit. A 2-metric diagnostic (9/9 accuracy) provides practitioners a simple check to determine when profiling is worthwhile. At long context (8K tokens), the constraint reduces degradation from 11.15× to 1.23× baseline, demonstrating critical deployment value.\"\n\n## \"When Does Non-Uniform Allocation Help?\" — Analysis Chapter\n\nFive case studies representing the full spectrum of heterogeneity:\n\n| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |\n|------|-------|-----|--------------|------------------------------|---------------|\n| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; \"spread\" pattern (L0 cluster, 4 heads, 26× dominance) |\n| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; \"spike\" pattern (L4H3 single outlier, 64% of total delta) |\n| **Marginal** | Llama-3.1-8B | 4:1 | 0.57 (hires) | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |\n| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |\n| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |\n\n**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.\n\n**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).\n\n**Joint diagnostic** (n=8, 8/8 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike), CodeLlama (0.80, t₁/t₅=0.81 — spike), and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.\n\n## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)\n\n| Method | PPL | Bit Distribution | Budget |\n|--------|-----|-------------------|--------|\n| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |\n| MCKP unconstrained | 36.92 | — | 0.25 |\n| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |\n\nKey takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.\n\n## Cross-Architecture Evidence Summary\n\n| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |\n|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|\n| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |\n| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |\n| Llama-3.1-8B | 4:1 | 256 | **0.57** (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (t₁/t₅≈0.85, single dominant L2H5) | ≈ Marginal |\n| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |\n| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |\n\n**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:\n- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding\n- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta\n- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)\n- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads\n\n**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):\n\nThree-tier labeling (NOT binary catastrophe/benign):\n- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding\n- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions\n- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)\n\nReviewer-suggested paragraph for paper (1 段, 3-4 句):\n\"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\"\n\nThis **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.\n\n⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.\n\n**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.\n\n**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.\n\n### Mistral k Ablation (256 KV heads, budget=0.25)\n\nPPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).\n\n| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |\n|---|-----|-------|-------|-------|--------|-----|\n| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |\n| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |\n| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |\n| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |\n| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |\n| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |\n\nContrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.\n\n### Llama k Ablation (256 KV heads, budget=0.25)\n\nAll k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).\n\n### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)\n\n**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅\n\n| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |\n|------|---------------|------------|---|---------------|\n| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |\n| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |\n| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |\n| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |\n| **Avg recovery** | — | — | **72.8%** | — |\n\n**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.7946 | 0.7854 | -0.92pp |\n| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |\n| hellaswag | 0.5857 | 0.5797 | -0.60pp |\n| piqa | 0.7927 | 0.7894 | -0.33pp |\n| winogrande | 0.7174 | 0.7301 | +1.27pp |\n| **Average** | **0.6822** | **0.6745** | **-0.77pp** |\n\n**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.8173 | 0.8039 | -1.34pp |\n| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |\n| hellaswag | 0.6026 | 0.6012 | -0.14pp |\n| piqa | 0.7867 | 0.7802 | -0.65pp |\n| winogrande | 0.7253 | 0.7238 | -0.15pp |\n| **Average** | **0.6915** | **0.6816** | **-0.99pp** |\n\n**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=4) | Δ |\n|------|---------------|------------|---|\n| arc_easy | — | — | — |\n| arc_challenge | — | — | — |\n| hellaswag | — | — | — |\n| piqa | — | — | — |\n| winogrande | — | — | — |\n| **Average** | **0.6894** | **0.6846** | **-0.48pp** |\n\n**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)\n\n| Task | Uniform 4-bit | MCKP | Δ |\n|------|---------------|------|---|\n| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |\n\n**Downstream summary (Reviewer-verified framing)**:\n- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**\n- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)\n- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)\n- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise\n- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)\n- **Paper must**: (a) report full per-task tables, not just averages, (b) use \"shows minor degradation\" NOT \"preserves accuracy\" — the latter has spin, (c) note arc_challenge as worst-case explicitly\n- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance\n- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论：\"ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\"\n- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞：\"Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge).\"\n\n## Allocation Baseline Evidence (plan_015, mckp_reeval)\n\nAll numbers from unified bf16 eval pipeline, budget=0.25.\n\n| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |\n|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|\n| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |\n| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |\n| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |\n\n**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.\n\n**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.\n\n## Differentiation from RateQuant\n\n| Aspect | RateQuant | Ours |\n|--------|-----------|------|\n| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |\n| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |\n| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |\n| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |\n| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |\n| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |\n| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |\n\n## Venue Fit Risks\n\n- **\"The constraint is just a heuristic, not a real contribution\"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.\n- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.\n- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive \"higher GQA = more benefit\" hypothesis and shows our diagnostic is needed.\n- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 8/8 correct). The \"spike vs spread\" analysis explains WHY same-GQA models differ.\n- **Statistical power**: n=8 models is directional evidence, not statistical claim. Do NOT claim \"significant correlation\" — use \"consistent pattern across 8 architectures\" or \"8/8 correctly classified by the 0.50 threshold.\"\n- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.\n\n## Anticipated Reviewer Concerns\n\n1. **\"The cardinality constraint is trivial — just cap the extreme allocations\"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.\n2. **\"This is just RateQuant with a constraint added\"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.\n3. **\"The method only works on Qwen — isn't this a Qwen paper?\"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.\n4. **\"How does this work at different compression ratios?\"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.\n5. **\"n=3/4/5 models is not enough for the heterogeneity claim\"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.\n6. **\"RateQuant does K/V asymmetric allocation, do you?\"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.\n7. **\"Where are the downstream task results?\"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use \"shows minor degradation\" not \"preserves accuracy\".\n8. **\"The profiler distortion=0.0 on Mistral suggests the profiling method is broken\"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.\n9. **\"If solver doesn't matter, why present MCKP at all?\"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim:\n  - 2\n  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.\n    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.\n    Strengthens narrative: \"solver automatically discovers sensitivity structure.\"\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: exp_d_no_l0_exclusion\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_002\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).\n    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability\n    across different GQA ratios and architectures. Fallback if HF token unavailable:\n    Yi-1.5-9B (non-gated, similar scale).\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: llama_full_pipeline\n  model: Llama-3.1-8B\n  fallback_model: Yi-1.5-9B\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 8.7\n    uniform_4bit_ppl_bf16: 8.47\n    baseline_ppl_bf16: 8.09\n    delta_vs_uniform: -0.23\n    memory_ratio: 0.25\n- id: plan_003\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture\n    family to establish cross-architecture validity.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mistral_full_pipeline\n  model: Mistral-7B-v0.3\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 7.564\n    uniform_4bit_ppl_bf16: 7.131\n    baseline_ppl_bf16: 7.035\n    delta_vs_uniform: -0.433\n    memory_ratio: 0.25\n- id: plan_004\n  claim:\n  - 3\n  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112\n    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map\n    the compounding threshold. Establishes the principled basis for cardinality constraint\n    selection.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: compounding_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_005\n  claim:\n  - 2\n  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,\n    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline\n    at same budget.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: budget_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_006\n  claim:\n  - 1\n  - 2\n  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).\n    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers\n    mid-layer heterogeneity and improves solver allocation beyond current results.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_e_hires_profile\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    constrained_ppl_bf16: 9.569\n    baseline_ppl_bf16: 8.819\n    exp_c_ppl_bf16: 11.345\n    delta_vs_exp_c: -1.776\n    memory_ratio: 0.25\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    profile_resolution:\n      hires_nonzero_2bit: 100\n      lowres_nonzero_2bit: 37\n      hires_nonzero_4bit: 6\n      lowres_nonzero_4bit: 4\n      total_heads: 112\n    allocation_diff_count: 8\n    profiling_time_min: 65.5\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.\n    Cross-dataset evaluation to show results are not WikiText-2 specific.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  eval: C4\n  status: DONE\n  conclusion: success\n  metrics: &id001\n    c4_cal_wt2_eval_mckp_ppl: 11.2942\n    c4_cal_wt2_eval_uniform_ppl: 15.4454\n    c4_cal_wt2_eval_delta: 4.1512\n    c4_cal_bf16_baseline: 12.6505\n    wt2_bf16_baseline: 9.8106\n    allocation_agreement_c4_vs_wt2: 0.964\n    agreement_heads: 108/112\n    bit_dist: 2bit:8, 4bit:100, 8bit:4\n    cross_domain_wt2_to_c4_mckp_ppl: 20.5601\n    cross_domain_wt2_to_c4_uniform_ppl: 35.4232\n    cross_domain_c4_bf16: 15.3246\n    old_contaminated_ppl: 11.3285\n    contamination_impact: 0.0343\n    models_completed: Qwen2.5-7B only\n- id: plan_008\n  claim:\n  - 2\n  description: 'RateQuant comparison: implement RateQuant''s greedy algorithm (Algorithm\n    1) on our discrete action set {2,4,8,16}-bit. RateQuant''s Prop. 6 optimality\n    relies on consecutive-integer polymatroid structure which breaks on non-consecutive\n    sets. Show greedy produces suboptimal allocation vs constrained MCKP. Critical\n    for differentiation claim — must have experimental evidence.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: ratequant_greedy_comparison\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_009\n  claim:\n  - 2\n  description: 'Oracle comparison: brute-force optimal allocation on a subset (3-4\n    layer groups) of Qwen2.5-7B. Quantify MCKP gap to oracle.\n\n    '\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_006\n  registry_id: oracle_comparison\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_ppl: 10.9131\n    max_oracle_gap_ppl: 0.0183\n    avg_oracle_gap_ppl: 0.0046\n    layers_mckp_optimal: 5/8\n    layers_with_gap: 3\n    gap_layers:\n      L1: 0.0183\n      L4: 0.0045\n      L11: 0.0136\n    gap_nature: 2-bit head position swap within same bit budget\n    total_evals: 54\n    runtime_min: 21.3\n- id: plan_010\n  claim:\n  - 2\n  description: 'Cross-domain calibration robustness: calibrate on C4, evaluate on\n    WikiText-2 (and vice versa). Report per-head allocation agreement rate across\n    calibration sources.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_007\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: plan_011\n  claim:\n  - 1\n  description: 'Head sensitivity visualization: generate paper-quality figures showing\n    per-head profiling delta heatmap across layers, compounding effect curve, and\n    budget allocation comparison chart.\n\n    '\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_004\n  - plan_006\n  registry_id: head_sensitivity_viz\n  status: DONE\n  conclusion: success\n- id: plan_014\n  claim:\n  - 2\n  description: 'K/V separation: treat K and V heads as independent MCKP items with\n    separate budget allocation. Compare joint K+V optimization vs current uniform\n    K=V approach. RateQuant supports asymmetric K/V (e.g. K=2.85, V=2.15 avg bits)\n    — we should show MCKP naturally handles this.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: kv_separation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    kv_sep_ppl: 11.2162\n    joint_kv_ppl: 10.9131\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_sep_vs_joint: 0.303\n    sep_k_2bit_count: 16\n    sep_v_uniform_4bit: true\n    kv_asymmetric_heads: 21\n- id: plan_012\n  claim:\n  - 1\n  - 2\n  description: 'Downstream task evaluation: ARC-C / HellaSwag / PIQA / WinoGrande\n    on Qwen2.5-7B at 4× compression. Must match RateQuant''s eval suite for direct\n    comparison. Tests whether PPL improvements translate to downstream performance.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  registry_id: downstream_eval_qwen\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    avg_recovery: 0.728\n    arc_c: 0.5137\n    hellaswag: 0.7684\n    piqa: 0.7786\n    winogrande: 0.6819\n    arc_c_delta_pp: 3.16\n    hellaswag_delta_pp: 4\n    piqa_delta_pp: 1.25\n    winogrande_delta_pp: 1.97\n- id: plan_013\n  claim:\n  - 1\n  description: '70B profiling-only: run distortion profiling on Qwen2.5-72B (no full\n    eval). Analyze whether sensitivity patterns (Layer 0 dominance, compounding threshold)\n    scale with model size.\n\n    '\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: qwen72b_profiling\n  model: Qwen2.5-72B\n  status: DONE\n  conclusion: killed\n- id: plan_015\n  claim:\n  - 2\n  description: 'L0-only heuristic baseline: assign 8-bit to all Layer 0 KV heads,\n    uniform 4-bit to all other heads, at 4x compression on Qwen2.5-7B. This is the\n    simplest possible non-uniform strategy exploiting L0 sensitivity. If L0-only matches\n    or beats constrained MCKP, the full optimization machinery is unnecessary. Must\n    also test on Llama and Mistral. Critical missing baseline flagged by Dream review.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: l0_only_heuristic\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: killed\n- id: plan_016\n  claim:\n  - 2\n  description: 'RateQuant greedy + cardinality constraint ablation: add max_2bit=k\n    constraint to RateQuant greedy Algorithm 1 on {2,4,8,16}. Compare three conditions:\n    (a) RateQuant greedy unconstrained (already have: PPL ~32.45), (b) RateQuant greedy\n    + cardinality k=8, (c) constrained MCKP k=8 (already have: PPL ~11.23). If (b)\n    matches (c), the contribution is the cardinality constraint, not the MCKP solver.\n    If (c) beats (b), discrete MCKP optimization genuinely matters. Critical ablation\n    flagged by all three Dream review tiers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_008\n  registry_id: greedy_cardinality_ablation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 11.2312\n    greedy_unconstrained_ppl: 32.4467\n    mckp_constrained_ppl: 11.23\n    delta_vs_mckp: 0.0012\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n- id: plan_017\n  claim:\n  - 1\n  - 2\n  description: 'Multi-seed error bars: run constrained MCKP and uniform 4-bit on Qwen2.5-7B\n    at 4x compression with 3 different calibration sets (different random subsets\n    of WikiText-2 training data). Report mean +/- std for PPL. Required for statistical\n    credibility — Dream review flagged all-single-run as critical gap.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: multi_seed_error_bars\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4454\n    mckp_seed0: 11.0168\n    mckp_seed1: 10.8981\n    mckp_seed2: 11.0487\n    mckp_mean: 10.9878\n    mckp_std: 0.0648\n    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4\n    allocation_agreement_3way: 0.902\n    agreement_s0_s1: 0.946\n    agreement_s0_s2: 0.911\n    agreement_s1_s2: 0.946\n    profile_time_min_per_seed: 65\n- id: plan_018\n  claim:\n  - 2\n  description: 'Runtime/latency benchmark: measure end-to-end inference latency and\n    throughput with mixed-precision KV cache vs uniform 4-bit quantization on Qwen2.5-7B.\n    Include profiling cost breakdown. Dream review flagged missing latency evaluation\n    as significant gap for systems-oriented contribution.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: runtime_benchmark\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16:\n      prefill_ms: 45.86\n      decode_ms_per_tok: 33.78\n      throughput_tok_s: 29.6\n    uniform_4bit:\n      prefill_ms: 54.25\n      decode_ms_per_tok: 42.46\n      throughput_tok_s: 23.6\n    constrained_mckp:\n      prefill_ms: 57.03\n      decode_ms_per_tok: 46.09\n      throughput_tok_s: 21.8\n      mckp_solver_sec: 0.005\n      bit_dist:\n        '2': 8\n        '4': 100\n        '8': 4\n      memory_ratio: 0.25\n    theoretical_memory:\n      bf16_MB: 21\n      4bit_MB: 5.25\n      mckp_MB: 5.25\n      compression_4x: true\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp_004\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p0_2_cliff_1.5B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: p0_2_cliff_7B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: p0_1_ppl_fast\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_a_targeted_hybrid\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_b_hires_quant\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_c_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_c_no2bit\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl: 15.4454\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_vs_uniform: 0\n    memory_ratio: 0.25\n    bit_distribution:\n      '4': 112\n- exp_id: exp_d_no_l0_exclusion\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_e_hires_profile\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    constrained_ppl_bf16: 9.569\n    baseline_ppl_bf16: 8.819\n    exp_c_ppl_bf16: 11.345\n    delta_vs_exp_c: -1.776\n    memory_ratio: 0.25\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    profile_resolution:\n      hires_nonzero_2bit: 100\n      lowres_nonzero_2bit: 37\n      hires_nonzero_4bit: 6\n      lowres_nonzero_4bit: 4\n      total_heads: 112\n    allocation_diff_count: 8\n    profiling_time_min: 65.5\n- exp_id: compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: compounding_sweep_k10_12\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: ratequant_greedy_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: budget_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: c4_cross_dataset_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    c4_mckp_ppl: 11.3285\n    uniform4bit_ppl: 15.4454\n    delta_over_uniform: 4.117\n    allocation_agreement_rate: 0.982\n    n_disagree: 2\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n    wt2_ref_mckp_ppl: 11.2312\n    wt2_ref_delta: 4.2142\n    ppl_gap: 0.097\n- exp_id: llama_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 8.7\n    uniform_4bit_ppl_bf16: 8.47\n    baseline_ppl_bf16: 8.09\n    delta_vs_uniform: -0.23\n    memory_ratio: 0.25\n- exp_id: mistral_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 7.564\n    uniform_4bit_ppl_bf16: 7.131\n    baseline_ppl_bf16: 7.035\n    delta_vs_uniform: -0.433\n    memory_ratio: 0.25\n- exp_id: llama_hires_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 8.0918\n    uniform_4bit_ppl: 8.469\n    lowres_mckp_ppl: 8.6951\n    hires_mckp_ppl: 8.4498\n    hires_improvement_ppl: 0.2453\n    degradation_reduction_pct: 40.7\n    profiling_time_min: 173.4\n    total_time_min: 175.1\n- exp_id: mistral_hires_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl: 7.323\n    uniform_4bit_ppl: 7.131\n    baseline_ppl: 7.035\n    delta_vs_uniform: -0.192\n    memory_ratio: 0.25\n- exp_id: llama_aggressive_compression\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_5.3x_ppl: 57.6\n    uniform_2bit_ppl: 2643.77\n    mckp_8x_ppl: 2372.33\n    uniform_2bit_8x_ppl: 2643.77\n- exp_id: downstream_eval_qwen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    avg_recovery: 0.728\n    arc_c: 0.5137\n    hellaswag: 0.7684\n    piqa: 0.7786\n    winogrande: 0.6819\n    arc_c_delta_pp: 3.16\n    hellaswag_delta_pp: 4\n    piqa_delta_pp: 1.25\n    winogrande_delta_pp: 1.97\n- exp_id: head_sensitivity_viz\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mistral_aggressive_compression\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_5.3x_ppl: 11.912\n    uniform_2bit_ppl: 519.107\n    mckp_8x_ppl: 399.901\n    uniform_2bit_8x_ppl: 519.107\n    baseline_ppl: 7.035\n    uniform_4bit_ppl: 7.131\n    5.3x_bit_dist:\n      '2': 128\n      '4': 128\n    8x_bit_dist:\n      '2': 248\n      '4': 8\n    total_time_seconds: 268.1\n- exp_id: kv_separation\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    kv_sep_ppl: 11.2162\n    joint_kv_ppl: 10.9131\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_sep_vs_joint: 0.303\n    sep_k_2bit_count: 16\n    sep_v_uniform_4bit: true\n    kv_asymmetric_heads: 21\n- exp_id: l0_only_heuristic\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: greedy_cardinality_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 11.2312\n    greedy_unconstrained_ppl: 32.4467\n    mckp_constrained_ppl: 11.23\n    delta_vs_mckp: 0.0012\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n- exp_id: l0_heuristic_baseline\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: greedy_constrained_ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: l0_heuristic_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_constrained_ppl: 11.23\n    l0_random_mean_ppl: 11.69\n    l0_random_std: 0.47\n    naive_positional_ppl: 12.23\n    uniform_4bit_ppl: 15.45\n    qwen_l0_random_median: 11.515\n    qwen_l0_random_seeds:\n    - 11.486\n    - 11.615\n    - 11.325\n    - 11.515\n    - 12.515\n    llama_l0_random_mean: 10.479\n    llama_l0_random_std: 1.033\n    llama_l0_random_median: 10.038\n    llama_l0_random_seeds:\n    - 9.485\n    - 10.488\n    - 9.941\n    - 10.038\n    - 12.444\n    llama_naive_positional: 9.941\n    llama_mckp: 8.4498\n    llama_uniform: 8.469\n    mistral_l0_random_mean: 7.56\n    mistral_l0_random_std: 0.087\n    mistral_l0_random_median: 7.586\n    mistral_l0_random_seeds:\n    - 7.523\n    - 7.61\n    - 7.413\n    - 7.586\n    - 7.669\n    mistral_naive_positional: 7.481\n    mistral_mckp: 7.3106\n    mistral_uniform: 7.131\n- exp_id: qwen_bf16_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 9.8106\n    baseline_fp16_ppl: 9.81\n    delta_baseline: 0.0006\n    uniform4_bf16_ppl: 15.4454\n    uniform4_fp16_ppl: 15.45\n    delta_uniform4: 0.0046\n- exp_id: hires_mckp_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl_bf16: 9.8106\n    mckp_ppl_bf16: 10.9131\n    uniform_4bit_ppl_bf16: 15.4454\n    delta_mckp_vs_baseline: 1.1025\n    delta_mckp_vs_uniform: -4.5323\n    token_count: 298938\n- exp_id: hires_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 9.8106\n    uniform_4bit_bf16_ppl: 15.4454\n    hires_mckp_bf16_ppl: 10.9131\n- exp_id: mistral_k_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 4\n    best_ppl: 7.1648\n    uniform_4bit_ppl: 7.131\n    k4_ppl: 7.1648\n    k8_ppl: 7.1997\n    k12_ppl: 7.2448\n    k16_ppl: 7.3106\n    k18_ppl: 7.3231\n- exp_id: llama_k_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 4\n    best_ppl: 8.4498\n    uniform_4bit_ppl: 8.469\n    k4_ppl: 8.4498\n    k8_ppl: 8.4498\n    k12_ppl: 8.4498\n    k16_ppl: 8.4498\n    k18_ppl: 8.4498\n    natural_2bit_count: 2\n- exp_id: multi_seed_error_bars\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4454\n    mckp_seed0: 11.0168\n    mckp_seed1: 10.8981\n    mckp_seed2: 11.0487\n    mckp_mean: 10.9878\n    mckp_std: 0.0648\n    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4\n    allocation_agreement_3way: 0.902\n    agreement_s0_s1: 0.946\n    agreement_s0_s2: 0.911\n    agreement_s1_s2: 0.946\n    profile_time_min_per_seed: 65\n- exp_id: cross_domain_calibration\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c4_cross_dataset_eval_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cross_domain_calibration_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: runtime_benchmark\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16:\n      prefill_ms: 45.86\n      decode_ms_per_tok: 33.78\n      throughput_tok_s: 29.6\n    uniform_4bit:\n      prefill_ms: 54.25\n      decode_ms_per_tok: 42.46\n      throughput_tok_s: 23.6\n    constrained_mckp:\n      prefill_ms: 57.03\n      decode_ms_per_tok: 46.09\n      throughput_tok_s: 21.8\n      mckp_solver_sec: 0.005\n      bit_dist:\n        '2': 8\n        '4': 100\n        '8': 4\n      memory_ratio: 0.25\n    theoretical_memory:\n      bf16_MB: 21\n      4bit_MB: 5.25\n      mckp_MB: 5.25\n      compression_4x: true\n- exp_id: c4_rerun_d032\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_cal_wt2_eval_mckp_ppl: 11.2942\n    c4_cal_wt2_eval_uniform_ppl: 15.4454\n    c4_cal_wt2_eval_delta: 4.1512\n    c4_cal_bf16_baseline: 12.6505\n    wt2_bf16_baseline: 9.8106\n    allocation_agreement_c4_vs_wt2: 0.964\n    agreement_heads: 108/112\n    bit_dist: 2bit:8, 4bit:100, 8bit:4\n    cross_domain_wt2_to_c4_mckp_ppl: 20.5601\n    cross_domain_wt2_to_c4_uniform_ppl: 35.4232\n    cross_domain_c4_bf16: 15.3246\n    old_contaminated_ppl: 11.3285\n    contamination_impact: 0.0343\n    models_completed: Qwen2.5-7B only\n- exp_id: multi_seed_lowres\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: oracle_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_ppl: 10.9131\n    max_oracle_gap_ppl: 0.0183\n    avg_oracle_gap_ppl: 0.0046\n    layers_mckp_optimal: 5/8\n    layers_with_gap: 3\n    gap_layers:\n      L1: 0.0183\n      L4: 0.0045\n      L11: 0.0136\n    gap_nature: 2-bit head position swap within same bit budget\n    total_evals: 54\n    runtime_min: 21.3\n- exp_id: plan_009_oracle_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: qwen72b_profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: llama_heuristic_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    l0_random_seeds:\n    - 8.5479\n    - 8.7595\n    - 8.624\n    - 8.5721\n    - 8.6192\n    l0_random_mean: 8.6245\n    l0_random_std: 0.0733\n    l0_random_median: 8.6192\n    naive_positional_ppl: 8.5781\n    mckp_ppl: 8.4498\n    uniform_ppl: 8.469\n    baseline_ppl: 8.0918\n    mckp_vs_l0_random_gap: 0.1747\n    mckp_vs_naive_gap: 0.1283\n- exp_id: mistral_heuristic_k4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 7.0351\n    uniform_4bit_ppl: 7.1314\n    mckp_k4_ppl: 7.1648\n    l0_random_seed_0: 7.1882\n    l0_random_seed_1: 7.1995\n    l0_random_seed_2: 7.1723\n    l0_random_seed_3: 7.3577\n    l0_random_seed_4: 7.2875\n    l0_random_mean: 7.2411\n    l0_random_std: 0.0707\n    l0_random_median: 7.1995\n    naive_heuristic_ppl: 7.2105\n    budget_heuristic: 0.2559\n    budget_mckp_k4: 0.248\n- exp_id: llama_c4_cross_dataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wt2_cal_wt2_ppl: 8.4498\n    c4_cal_wt2_ppl: 8.6459\n    uniform_wt2_ppl: 8.469\n    wt2_cal_c4_ppl: 7.654\n    c4_cal_c4_ppl: 7.654\n    uniform_c4_ppl: 7.5351\n    bf16_wt2_ppl: 8.0918\n    bf16_c4_ppl: 7.1333\n    agreement_rate: 0.977\n    agreement_heads: 250/256\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n- exp_id: mistral_c4_cross_dataset\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bf16_wt2_ppl: 7.0351\n    c4_cal_bf16_ppl: 6.9677\n    wt2_cal_mckp_wt2_ppl: 7.1648\n    c4_cal_mckp_wt2_ppl: 7.1859\n    uniform_4bit_wt2_ppl: 7.1314\n    delta_uniform_mckp_wt2_cal: -0.0334\n    delta_uniform_mckp_c4_cal: -0.0546\n    allocation_agreement_c4_vs_wt2: 0.965\n    agreement_heads: 247/256\n    bit_dist_wt2_cal: 2bit:4, 4bit:252\n    bit_dist_c4_cal: 2bit:4, 4bit:251, 8bit:1\n    profile_time_s: 407.7\n    eval_time_s: 349.4\n    total_time_s: 757.1\n- exp_id: gemma2_9b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 8.9\n    mckp_wikitext2_ppl: 9.05\n    uniform4bit_wikitext2_ppl: 9.03\n    mckp_improvement_over_uniform: -0.02\n    top5_concentration: 0.23\n    layer0_dominance_ratio: 1.32\n    best_k: 8\n    best_k_ppl: 9.05\n    verdict: FAIL\n- exp_id: yi15_9b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 7.0157\n    mckp_wikitext2_ppl: 7.3129\n    uniform4bit_wikitext2_ppl: 7.2171\n    mckp_improvement_over_uniform: -0.0958\n    top5_concentration: 0.4934\n    layer0_dominance_ratio: 0.07\n    best_k: 2\n    best_k_ppl: 7.2209\n    gqa_ratio: '8:1'\n    verdict: FAIL\n- exp_id: qwen25-hires-profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_hires_float32_d048\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    float32_hires_top5_concentration: 0.6104\n    bf16_hires_range: 0.59-0.66\n    float32_lowres_concentration: 0.42\n    bf16_bug_impact_on_concentration: 0.01\n    baseline_ppl: 9.81\n    mckp_unconstrained_ppl: 10.95\n    uniform_4bit_ppl: 15.45\n    mckp_bit_dist:\n      '2': 12\n      '4': 96\n      '8': 3\n      '16': 1\n    l0h0_delta: 6.7388\n    l0_4heads_total_share: 0.586\n    claim3_threshold_0.50: PASS\n- exp_id: yi15_hires_float32_profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: yi15_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.7139\n    top5_n_heads: 9\n    baseline_calibration_ppl: 5.888\n    delta_2bit_cv: 8.8991\n    layer0_dominance_ratio: 0.04\n    top1_head: L4H3_delta=13.1236\n    total_hours: 0.96\n- exp_id: qwen_hires_constrained_d049\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    float32_hires_constrained_mckp_ppl: 10.8921\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4484\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    gap_recovery_pct: 80.8\n    top5_concentration: 0.6156\n    top5_concentration_pre_monotonicity: 0.6104\n    bf16_hires_constrained_mckp_ppl: 10.9131\n    delta_f32_vs_bf16: 0.021\n- exp_id: yi15_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hires_mckp_ppl: 7.2181\n    uniform_4bit_ppl: 7.2171\n    baseline_ppl: 7.0157\n    delta_vs_uniform: -0.001\n    bit_distribution:\n      '2': 2\n      '4': 189\n      '8': 1\n    2bit_heads:\n    - L22H1\n    - L24H3\n    8bit_heads:\n    - L6H2\n    L4H3_status: kept_at_4bit\n    std_mckp_k2_ppl: 7.2209\n    std_mckp_k8_ppl: 7.3129\n    hires_concentration: 0.7139\n    L4H3_2bit_delta: 13.12\n    L4H3_4bit_delta: 0.0048\n    L4H3_8bit_delta: 0.004\n- exp_id: llama_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.5749\n    t1_t5: 0.85\n    baseline_ppl: 6.5055\n    top1_head: L2H5_delta=15.2636\n    delta_2bit_cv: 7.7663\n    l0_dominance_ratio: 0.67\n    positive_delta_heads: 254\n    total_heads: 256\n    total_hours: 0.98\n- exp_id: mistral_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: 'ValueError: Unrecognized model - config.json missing model_type field\n      at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3'\n- exp_id: mistral_hires_bf16_2bitonly_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: 'SafetensorError: model-00003-of-00003.safetensors missing, incomplete\n      download'\n- exp_id: mistral_hires_bf16_2bitonly_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mistral_hires_bf16_2bitonly_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.241\n    top5_n_heads: 12\n    baseline_ppl: 5.8702\n    top1_head: L2H5\n    top1_delta_2bit: 0.3236\n    top2_head: L12H1\n    top2_delta_2bit: 0.1435\n    top3_head: L0H7\n    top3_delta_2bit: 0.1403\n    delta_2bit_mean: 0.020073\n    delta_2bit_std: 0.026278\n    delta_2bit_cv: 1.3091\n    layer0_mean_delta_2bit: 0.034073\n    other_layers_mean_delta_2bit: 0.019621\n    l0_dominance_ratio: 1.74\n    positive_delta_heads: 252\n    total_heads: 256\n    distribution_shape: flat\n    total_hours: 0.94\n    profile_seconds: 3371.7\n- exp_id: llama_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_bf16_ppl: 8.0922\n    hires_mckp_ppl: 8.5042\n    uniform_4bit_ppl: 8.4701\n    std_mckp_reference_ppl: 8.4498\n    mckp_vs_uniform_delta: -0.0341\n    mckp_vs_uniform_pct: -9\n    hires_vs_std_mckp_delta: 0.0544\n    concentration: 0.5749\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n    heads_2bit:\n    - 26,0\n    - 31,7\n    heads_8bit:\n    - 12,3\n    verdict: FAIL\n- exp_id: gemma2_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    concentration_top5pct: 0.2291\n    l0_dominance_ratio: 2.05\n    cv_delta_2bit: 1.2834\n    positive_delta_heads: 310/336\n    top_head: L0H1 delta=0.1906\n    total_time_hours: 1.59\n- exp_id: llama_c4_hires_crossdataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_wt2_ppl: 8.0922\n    bf16_c4_ppl: 7.1333\n    c4_cal_mckp_wt2_ppl: 8.5103\n    c4_cal_mckp_c4_ppl: 7.5351\n    uniform_wt2_ppl: 8.4701\n    uniform_c4_ppl: 7.5351\n    delta_c4_uniform_minus_mckp: 0\n    delta_wt2_uniform_minus_mckp: -0.0402\n    verdict_c4: FAIL\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n    heads_2bit:\n    - 2,3\n    - 24,2\n    heads_8bit:\n    - 31,6\n    total_time_min: 6.3\n    wt2_ref_mckp_ppl: 8.5042\n    wt2_ref_delta: -0.0341\n- exp_id: mistral_c4_hires_crossdataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fp16_ppl: 7.0352\n    c4_mckp_ppl: 7.1774\n    uniform_4bit_ppl: 7.1308\n    mckp_vs_uniform_delta: 0.0466\n    mckp_bit_distribution:\n      '2': 4\n      '4': 250\n      '8': 2\n    phase4_error: 'FileNotFoundError: mistral_k_ablation_results.json'\n- exp_id: w2_unconstrained_baselines\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    note: 2bitonly profiles only - INVALID for reviewer response\n    yi15_ppl: 672.2\n    yi15_ratio: 114\n    llama_ppl: 1219.7\n    llama_ratio: 187\n    mistral_ppl_2bitonly: 47.8\n    mistral_ratio_2bitonly: 8.2\n    mistral_ppl_full: 6.39\n    mistral_ratio_full: 1.09\n    gemma2_ppl: 277.4\n    gemma2_ratio: 37.9\n    budget: 0.25\n    baseline_yi: 5.89\n    baseline_llama: 6.51\n    baseline_mistral: 5.87\n    baseline_gemma2: 7.32\n- exp_id: w9_compounding_scaling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    baseline_ppl: 8.2\n    n1_joint_ppl: 14.94\n    n1_ratio: 1\n    n2_joint_ppl: 42.26\n    n2_ratio: 3.84\n    n4_joint_ppl: 3813.76\n    n4_ratio: 333.3\n    n8_joint_ppl: 3586.42\n    n8_ratio: 282.1\n    n16_joint_ppl: 7286.23\n    n16_ratio: 521.1\n    n32_joint_ppl: 6644.05\n    n32_ratio: 424\n    n64_joint_ppl: 9453.33\n    n64_ratio: 533.3\n    runtime_seconds: 96\n- exp_id: w9_compounding_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.81\n    k1_topk_ppl: 9.826\n    k1_randomk_ppl: 9.887\n    k1_randomk_std: 0.05\n    k4_topk_ppl: 9.849\n    k4_topk_ratio: 0.86\n    k4_randomk_ppl: 10.06\n    k4_randomk_std: 0.06\n    k4_randomk_ratio: 1.24\n    k8_topk_ppl: 10.042\n    k8_topk_ratio: 1.56\n    k8_randomk_ppl: 11.07\n    k8_randomk_std: 0.69\n    k8_randomk_ratio: 1.76\n    k16_topk_ppl: 10.42\n    k16_topk_ratio: 1.56\n    k16_randomk_ppl: 12.91\n    k16_randomk_std: 0.4\n    k16_randomk_ratio: 2.1\n    k32_topk_ppl: 11.604\n    k32_topk_ratio: 1.78\n    k32_randomk_ppl: 18.33\n    k32_randomk_std: 2.53\n    k32_randomk_ratio: 2.73\n    k64_topk_ppl: 22.946\n    k64_topk_ratio: 4.89\n    k64_randomk_ppl: 55.94\n    k64_randomk_std: 9.73\n    k64_randomk_ratio: 8.88\n    runtime_minutes: 16.9\n    note: 'v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking,\n      top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。'\n- exp_id: w2_unconstrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi15_baseline: 7.0157\n    yi15_uniform4: 7.2171\n    yi15_greedy: 7.5615\n    yi15_mckp: 7.5615\n    yi15_n2bit: 22\n    llama_baseline: 8.0922\n    llama_uniform4: 8.4701\n    llama_greedy: 8.6265\n    llama_mckp: 8.6265\n    llama_n2bit: 12\n    mistral_baseline: 7.0352\n    mistral_uniform4: 7.1308\n    mistral_greedy: 7.5733\n    mistral_mckp: 7.5963\n    mistral_n2bit: 42\n    gemma2_baseline: 6.0306\n    gemma2_uniform4: 6.1683\n    gemma2_greedy: 8.8469\n    gemma2_mckp: 8.8469\n    gemma2_n2bit: 106\n    gemma2_eval_method: sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\n    gemma2_greedy_ratio: 1.467\n    gemma2_catastrophic: true\n    gemma2_note: 1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal\n      value\n- exp_id: w3_downstream_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi15_baseline_avg: 0.6912\n    yi15_uniform_avg: 0.6822\n    yi15_mckp_avg: 0.6745\n    yi15_mckp_vs_uniform_pp: -0.77\n    yi15_mckp_vs_baseline_pp: -1.67\n    yi15_baseline:\n      arc_easy: 0.8093\n      arc_challenge: 0.5265\n      hellaswag: 0.5913\n      piqa: 0.7949\n      winogrande: 0.734\n    yi15_uniform:\n      arc_easy: 0.7946\n      arc_challenge: 0.5205\n      hellaswag: 0.5857\n      piqa: 0.7927\n      winogrande: 0.7174\n    yi15_mckp:\n      arc_easy: 0.7854\n      arc_challenge: 0.4881\n      hellaswag: 0.5797\n      piqa: 0.7894\n      winogrande: 0.7301\n    llama_baseline_avg: 0.696\n    llama_uniform_avg: 0.6915\n    llama_mckp_avg: 0.6816\n    llama_mckp_vs_uniform_pp: -0.99\n    llama_mckp_vs_baseline_pp: -1.44\n    llama_baseline:\n      arc_easy: 0.8228\n      arc_challenge: 0.5188\n      hellaswag: 0.6073\n      piqa: 0.7922\n      winogrande: 0.7388\n    llama_uniform:\n      arc_easy: 0.8173\n      arc_challenge: 0.5256\n      hellaswag: 0.6026\n      piqa: 0.7867\n      winogrande: 0.7253\n    llama_mckp:\n      arc_easy: 0.8039\n      arc_challenge: 0.4991\n      hellaswag: 0.6012\n      piqa: 0.7802\n      winogrande: 0.7238\n    mistral_baseline_avg: 0.6917\n    mistral_uniform_avg: 0.6894\n    mistral_mckp_avg: 0.6846\n    mistral_mckp_vs_uniform_pp: -0.48\n    mistral_mckp_vs_baseline_pp: -0.71\n    mistral_baseline:\n      arc_easy: 0.8005\n      arc_challenge: 0.5043\n      hellaswag: 0.6118\n      piqa: 0.8009\n      winogrande: 0.7411\n    mistral_uniform:\n      arc_easy: 0.7976\n      arc_challenge: 0.5068\n      hellaswag: 0.6051\n      piqa: 0.7982\n      winogrande: 0.7395\n    mistral_mckp:\n      arc_easy: 0.7942\n      arc_challenge: 0.4949\n      hellaswag: 0.6027\n      piqa: 0.802\n      winogrande: 0.7293\n    gemma2_baseline_avg: 0.7307\n    gemma2_uniform_avg: 0.7251\n    gemma2_mckp_avg: 0.7265\n    gemma2_mckp_vs_uniform_pp: 0.14\n    gemma2_mckp_vs_baseline_pp: -0.42\n    gemma2_baseline:\n      arc_easy: 0.8737\n      arc_challenge: 0.6135\n      hellaswag: 0.6093\n      piqa: 0.8128\n      winogrande: 0.7443\n    gemma2_uniform:\n      arc_easy: 0.8662\n      arc_challenge: 0.6058\n      hellaswag: 0.606\n      piqa: 0.8079\n      winogrande: 0.7395\n    gemma2_mckp:\n      arc_easy: 0.8649\n      arc_challenge: 0.6041\n      hellaswag: 0.6089\n      piqa: 0.8074\n      winogrande: 0.7474\n    eval_harness_version: 0.4.11\n    num_fewshot: 0\n    yi_elapsed_s: 1563.2\n    llama_elapsed_s: 1446.4\n    mistral_elapsed_s: 1302.2\n    gemma2_elapsed_s: 1735.9\n- exp_id: gemma2_constrained_bos_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 6.0306\n    uniform_4bit_ppl: 6.1683\n    constrained_mckp_ppl: 6.1951\n    mckp_vs_uniform_delta: 0.0267\n    mckp_delta_ppl: 0.1645\n    uniform_delta_ppl: 0.1377\n    bit_distribution:\n      '2': 8\n      '4': 324\n      '8': 4\n    n_2bit: 8\n    max_2bit: 8\n    memory_ratio: 0.25\n    eval_method: sliding_window_bos_fix\n    elapsed_seconds: 490.3\n- exp_id: w1_qwen14b_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 5.8432\n    concentration: 0.3312\n    t1_t5: 0.68\n    shape: Flat\n    l0_dominance: 15.5\n    cv: 3.7418\n    positive_heads: 370\n    total_heads: 384\n    top10_heads:\n    - head: L0H5\n      delta: 1.84494\n    - head: L0H4\n      delta: 0.236669\n    - head: L0H2\n      delta: 0.136971\n    - head: L28H4\n      delta: 0.099279\n    - head: L28H5\n      delta: 0.07576\n    - head: L27H4\n      delta: 0.071269\n    - head: L0H0\n      delta: 0.070018\n    - head: L28H6\n      delta: 0.063737\n    - head: L26H0\n      delta: 0.061462\n    - head: L31H3\n      delta: 0.061062\n    elapsed_min: 161.3\n    note: 't1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio'\n- exp_id: w1_pythia14b_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 13.6347\n    concentration: 0.2439\n    t1_t5: 0.28\n    shape: Flat\n    l0_dominance: 0.51\n    cv: 1.2172\n    positive_heads: 362\n    total_heads: 384\n    top5_heads:\n    - head: L1H11\n      delta: 1.016355\n    - head: L12H14\n      delta: 0.784513\n    - head: L8H4\n      delta: 0.759118\n    - head: L11H2\n      delta: 0.632357\n    - head: L13H2\n      delta: 0.522849\n    elapsed_min: 25.7\n    note: 't1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio'\n- exp_id: kivi_baseline_qwen_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_2bit_r128: 12.83\n    qwen_4bit_r128: 9.9\n    qwen_2bit_r0: 13.34\n    qwen_4bit_r0: 9.91\n    llama_2bit_r128: 9.84\n    llama_4bit_r128: 8.14\n    llama_2bit_r0: 10.08\n    llama_4bit_r0: 8.14\n    group_size: 32\n    eval_data: WikiText-2 test\n    note: r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\n- exp_id: qwen14b_constrained_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16: 6.8654\n    ppl_uniform_4bit: 7.202\n    ppl_constrained_mckp: 7.2206\n    ppl_unconstrained_mckp: 7.6923\n    delta_constrained_vs_uniform: -0.0185\n    delta_constrained_vs_uniform_pct: -5.51\n    delta_unconstrained_vs_uniform: -0.4902\n    bit_distribution_constrained:\n      '2': 8\n      '4': 374\n      '8': 1\n      '16': 1\n    bit_distribution_unconstrained:\n      '2': 77\n      '4': 271\n      '8': 35\n      '16': 1\n    concentration: 0.33\n    top1_pct: 0.2262\n    top5_pct: 0.3304\n    t1_t5: 0.68\n    shape: Flat\n- exp_id: pythia14b_constrained_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16: 16.4893\n    ppl_uniform_4bit: 24.2894\n    ppl_constrained_mckp: 24.4521\n    ppl_unconstrained_mckp: 31.5415\n    concentration: t1=0.0289, t5=0.2439\n    t1_t5: 0.0289/0.2439\n    shape: Flat\n    constrained_vs_uniform_gap: 0.1627\n- exp_id: qwen7b_8k_context_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16_8k: 6.97\n    ppl_constrained_mckp_8k: 8.59\n    ppl_uniform_4bit_8k: 77.75\n    ppl_bf16_2k: 9.81\n    ppl_constrained_mckp_2k: 10.89\n    ppl_uniform_4bit_2k: 15.45\n    mckp_improvement_over_uniform_8k: 97.7%\n    mckp_improvement_over_uniform_2k: 80.8%\n    shape: Spread\n    concentration: 0.5992\n    context_length: 8192\n    note: 'Concentration-dependent benefit amplifies at longer context: uniform 4-bit\n      catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust\n      (+23%)'\n- exp_id: qwen7b_8k_spotcheck\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: yi15_8k_spotcheck\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: llama_8k_spotcheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16_8k: 5.5958\n    ppl_constrained_mckp_8k: 6.0537\n    ppl_uniform_4bit_8k: 6.0364\n    mckp_improvement_over_uniform_8k: -0.0174\n    mckp_improvement_pct_8k: -3.94\n    ppl_bf16_2k: 8.0922\n    ppl_constrained_mckp_2k: 8.5042\n    ppl_uniform_4bit_2k: 8.4701\n    shape: Spike\n    concentration: 0.5749\n    t1_over_t5: 0.71\n    context_length: 8192\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n- exp_id: kivi_baseline_qwen7b_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_kivi_4bit_g32_r128: 9.8976\n    tokens: 298938\n    chunks: 583\n    stride: 512\n    model: Qwen2.5-7B\n    comparison_mckp_ppl: 10.91\n    comparison_uniform_ppl: 15.45\n    comparison_bf16_ppl: 9.81\n- exp_id: mistral_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kivi_mckp_combined_qwen7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: qwen14b_greedy_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 7.2206\n    mckp_constrained_ppl: 7.2206\n    delta_vs_mckp: 0\n    bit_distribution:\n      '2': 8\n      '4': 374\n      '8': 1\n      '16': 1\n    memory_ratio: 0.25\n    solver_time_sec: 0.08\n    total_time_min: 1.8\n- exp_id: mistral_uniform_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mistral_hires_constrained_mckp_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 7.0352\n    mckp_wikitext2_ppl: 7.1341\n    uniform4bit_wikitext2_ppl: 7.1308\n    mckp_improvement_over_uniform: -0.0033\n    mckp_improvement_pct: -3.48\n    verdict: FAIL\n    bit_distribution:\n      '2': 2\n      '4': 254\n    fix_note: 'uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130'\n- exp_id: phi3_medium_hires_profiling_check\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: codellama_7b_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: llama_compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 0\n    best_ppl: 8.0922\n    k0_ppl: 8.0922\n    k2_ppl: 8.1243\n    k4_ppl: 8.1803\n    k8_ppl: 8.2259\n    k16_ppl: 8.4378\n    k32_ppl: 9.0506\n    k64_ppl: 11.991\n    k128_ppl: 40.2067\n    k256_ppl: 1519.1888\n    budget: 0.25\n- exp_id: mistral_compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k0_ppl: 7.1308\n    k2_ppl: 7.1471\n    k4_ppl: 7.164\n    k8_ppl: 7.2001\n    k16_ppl: 7.31\n    k32_ppl: 7.4877\n    k64_ppl: 7.5932\n    k128_ppl: 7.5932\n    k256_ppl: 7.5932\n    best_k: 0\n    best_ppl: 7.1308\n    note: PPL monotonically increases with k; all-4bit optimal at budget=0.25; solver\n      saturates at k>=64 (41 actual 2-bit heads)\n- exp_id: phi3_medium_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: llama_downstream_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge:\n      fp16: 0.5188\n      uniform_4bit: 0.5256\n      mckp_k2: 0.5179\n    hellaswag:\n      fp16: 0.6073\n      uniform_4bit: 0.6024\n      mckp_k2: 0.6021\n    piqa:\n      fp16: 0.7922\n      uniform_4bit: 0.7873\n      mckp_k2: 0.7867\n    winogrande:\n      fp16: 0.7388\n      uniform_4bit: 0.7261\n      mckp_k2: 0.7309\n    avg_delta_vs_uniform: -0.1\n    bit_distribution:\n      4bit: 253\n      8bit: 1\n      2bit: 2\n    budget: 0.25\n    total_distortion: 0.7015\n    elapsed_sec: 3387\n- exp_id: yi_mistral_downstream_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi_k2:\n      arc_challenge:\n        baseline: 0.5265\n        uniform: 0.5205\n        mckp_k2: 0.4991\n      hellaswag:\n        baseline: 0.5912\n        uniform: 0.5855\n        mckp_k2: 0.5818\n      piqa:\n        baseline: 0.7949\n        uniform: 0.7916\n        mckp_k2: 0.7916\n      winogrande:\n        baseline: 0.7332\n        uniform: 0.7206\n        mckp_k2: 0.7238\n      avg_delta_vs_uniform: -0.0055\n      bit_distribution:\n        4bit: 189\n        8bit: 1\n        2bit: 2\n    mistral_k2:\n      arc_challenge:\n        baseline: 0.5043\n        uniform: 0.5068\n        mckp_k2: 0.5068\n      hellaswag:\n        baseline: 0.6118\n        uniform: 0.6051\n        mckp_k2: 0.605\n      piqa:\n        baseline: 0.8009\n        uniform: 0.7987\n        mckp_k2: 0.7982\n      winogrande:\n        baseline: 0.7411\n        uniform: 0.7395\n        mckp_k2: 0.7388\n      avg_delta_vs_uniform: -0.0003\n      bit_distribution:\n        4bit: 254\n        2bit: 2\n    elapsed_sec: 2672\n- exp_id: mistral_compounding_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k0_ppl: 7.0352\n    k2_ppl: 7.0366\n    k4_ppl: 7.0453\n    k8_ppl: 7.0636\n    k16_ppl: 7.1139\n    k32_ppl: 7.2378\n    k64_ppl: 7.7747\n    k128_ppl: 10.473\n    k256_ppl: 45.2766\n    budget: 0.25\n    n_heads: 256\n- exp_id: qwen_compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_compounding_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_k0: 9.8106\n    ppl_k8: 10.0474\n    ppl_k64: 23.2176\n    ppl_k256: 98.7523\n    max_compounding_ratio: 10.07\n    n_heads_total: 112\n    n_2bit_ceiling: 96\n    budget: 0.25\n- exp_id: codellama_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 7.6978\n    top5_concentration: 0.7975\n    t1_t5: 0.8131\n    distribution_shape: Spike\n    cv: 18.3153\n    l0_dominance_ratio: 0.8\n    top5_sensitive_heads:\n    - layer: 1\n      head: 1\n      delta_2bit: 22.998339\n    - layer: 1\n      head: 18\n      delta_2bit: 2.042989\n    - layer: 1\n      head: 11\n      delta_2bit: 1.460641\n    - layer: 0\n      head: 15\n      delta_2bit: 0.942934\n    - layer: 30\n      head: 31\n      delta_2bit: 0.839968\n    total_kv_heads: 1024\n    gqa_ratio: 1\n    profile_time_hours: 3.7\n- exp_id: gemma2_downstream_k2_4task\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gemma2_downstream_k8_4task\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: qwen_3seed_downstream_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge:\n      bf16: 0.4582\n      uniform: 0.459\n      mckp_mean: 0.459\n      mckp_std: 0.0035\n      delta: 0\n    hellaswag:\n      bf16: 0.5887\n      uniform: 0.5335\n      mckp_mean: 0.5748\n      mckp_std: 0.0022\n      delta: 0.0413\n    winogrande:\n      bf16: 0.7119\n      uniform: 0.6622\n      mckp_mean: 0.678\n      mckp_std: 0.0115\n      delta: 0.0158\n    piqa:\n      bf16: 0.7818\n      uniform: 0.7552\n      mckp_mean: 0.7748\n      mckp_std: 0.0023\n      delta: 0.0196\n    avg_delta: 0.0192\n    elapsed_sec: 2714\n- exp_id: gemma2_downstream_k8_4task_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge:\n      baseline: 0.6135\n      uniform: 0.6058\n      mckp_k8: 0.6049\n      delta: -0.0009\n    hellaswag:\n      baseline: 0.6093\n      uniform: 0.6092\n      mckp_k8: 0.6089\n      delta: -0.0003\n    winogrande:\n      baseline: 0.7443\n      uniform: 0.738\n      mckp_k8: 0.7443\n      delta: 0.0063\n    piqa:\n      baseline: 0.8128\n      uniform: 0.8036\n      mckp_k8: 0.8079\n      delta: 0.0043\n    avg_delta: 0.0024\n    bit_distribution:\n      4bit: 324\n      2bit: 8\n      8bit: 4\n    elapsed_sec: 2321\n- exp_id: llama_3seed_downstream_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_delta: -0.8\n    hellaswag_delta: 0\n    piqa_delta: -0.1\n    winogrande_delta: 0.5\n    avg_delta: -0.1\n    std_all_tasks: 0\n    note: Single profile → deterministic allocation → all 3 seeds identical\n- exp_id: falcon7b_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: deepseekvl_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: internlm2_7b_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: phi3_medium_hires_profiling_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.1742\n    top5_n_heads: 20\n    baseline_calibration_ppl: 4.783\n    delta_2bit_cv: 0.8905\n    layer0_dominance_ratio: 0.04\n    shape: Spread\n    t1_t5_ratio: 0.24\n    top1_head: L9H6\n    top1_delta_2bit: 0.1806\n    total_heads: 400\n    profiling_hours: 2.48\n    note: Low concentration but t1/t5=0.24 indicates sensitivity spread across multiple\n      heads — confirmed Spread pattern. Mid-layer concentration (L8-L11).\n- exp_id: falcon7b_hires_profiling_v2\n  name: ''\n  status: PENDING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T02:16:38.247Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T02:16:38.247Z",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T02:16:38.270Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：三条 claim 全部成立，reviewer 认可 compounding 发现的新颖性和 constraint 的实用价值，1/8 benefit 被视为诚实的 negative result 而非弱点
核心假设：['A1: 2-bit compounding 在 KV cache 文献中确实未被系统刻画（novelty 成立）', 'A2: 8/8 架构全部复现 unconstrained degradation（universality 被接受）', 'A3: cardinality constraint 被视为 principled intervention（非 trivial heuristic），因为 solver equivalence (Δ=0.0000) 证明了 constraint 才是核心', 'A4: 1/8 benefit + 7/8 negative 被视为对 field 隐含假设的重要修正', 'A5: diagnostic (9/9 accuracy) 作为 testable hypothesis 被接受，不需要统计显著性', 'A6: RateQuant 区分清晰——polymatroid 在 {2,4,8,16} 上 breaks 这一点被认可']
关键指标范围：{'avg_review_score_arr': [3.5, 4.0], 'claims_surviving_intact': [3, 3], 'p_accept_emnlp_main': [0.4, 0.6], 'major_reviewer_objections': [0, 1], 'narrative_rewrite_pct': [0, 10], 'unconstrained_degradation_universality': [8, 8], 'solver_equivalence_delta': [0.0, 0.001], 'diagnostic_accuracy': [8, 9], 'downstream_consistency_with_ppl': [5, 5]}
叙事方向：原始 framing 完全成立。Title: "2-Bit Compounding: A Universal Failure Mode in Per-Head KV Cache Quantization"。 三条 claim 原样保留：(1) compounding 是 universal failure mode，(2) cardinality constraint 是 universal fix 且 solver-agnostic，(3) non-uniform rarely helps + diagnostic。 Reviewer 可能要求增加 1-2 个模型或 error bar 作为 minor revision，但核心叙事不需调整。 长上下文结果 (11.15× vs 1.23×) 作为 deployment motivation 的 headline 数字。 Qwen 是 showcase，7/8 negative 是 contribution 的一部分。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: ratekv
focus: Evaluate the compounding-forward framing: core contribution is 2-bit compounding as universal failure mode + constraint as universal fix + "non-uniform rarely helps" as key negative result. N=1 Spread is a feature (7/8 don't need non-uniform) not a bug. Compare with concentration-dependent framing where N=1 was a weakness.

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

Per-head KV cache quantization on hardware-aligned bit-widths {2,4,8,16} has an unreported universal failure mode: 2-bit quantization distortions compound non-additively through the residual stream, causing ALL tested unconstrained solvers (greedy, MCKP) to systematically over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 architectures (1.07×–3.31× baseline). A cardinality constraint (≤k heads at 2-bit) universally prevents this over-allocation, and furthermore reduces the feasible set to where solver choice becomes irrelevant (greedy = MCKP, Δ=0.0000). Under moderate compression (4×), only 1/8 architectures benefits from non-uniform allocation over uniform 4-bit — providing the first empirical evidence that the implicit assumption "non-uniform is always better than uniform" is wrong in KV cache quantization. The core contribution is the compounding effect discovery + universal constraint fix, not the allocation algorithm.

## Core Claims (3 条)

1. **2-bit compounding is a universal failure mode for unconstrained per-head allocation**: On hardware-aligned non-consecutive bit-widths {2,4,8,16}, per-head independent profiling distortions compound non-additively when multiple heads are simultaneously assigned 2-bit quantization. This causes ALL tested unconstrained solvers to over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 diverse architectures (Qwen 3.31×, Gemma-2 1.47×, Yi 1.08×, Llama 1.07×, Mistral 1.08×, Pythia, Qwen-14B, Phi-3-medium). Quantitative evidence of non-additivity: per-head profiling predicts joint PPL ≈11 but actual joint 2-bit PPL is 32–37 (3× prediction error). This is the first systematic characterization of compounding effects in per-head KV cache quantization. Long-context amplifies the failure: at 8K tokens, uniform 4-bit degrades 11.15× baseline while constrained MCKP degrades only 1.23× — a 9× gap in degradation rate.

2. **A cardinality constraint is the universal fix — and makes solver choice irrelevant**: A simple cardinality constraint (max_2bit ≤ k) is sufficient to prevent compounding across ALL tested architectures. Three universally beneficial properties: (a) prevents catastrophic over-allocation on sensitive architectures (Qwen: 32.45 → 10.91), (b) prevents moderate over-allocation on flat architectures (Gemma-2: 8.85 → 6.17, reducing 2-bit heads from 106 to 8), (c) reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce IDENTICAL bit allocations and PPL (Δ=0.0000). The constraint is parameterizable via small-scale compounding test (k≤8 universally safe: <2.5% degradation across all architectures). Practical implication: practitioners need only add one integer parameter to existing pipelines.

3. **Non-uniform allocation benefit is rare — most models should use uniform 4-bit**: Under moderate compression (4×), only 1/8 tested architectures (Qwen2.5-7B, "spread" sensitivity pattern) benefits from non-uniform allocation (+27.3% PPL, +1.9pp downstream avg). The remaining 7/8 show no benefit or minor degradation (<1pp avg downstream). A 2-metric empirical diagnostic (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly classifies all 9 tested models (9/9 accuracy), providing practitioners a simple check: if the diagnostic says "no" — skip profiling and use uniform 4-bit with zero quality loss. This is the first systematic study of *when* non-uniform KV cache quantization is beneficial, correcting the implicit assumption that it always helps.

## Story Spine

- **Problem**: Per-head mixed-precision KV cache quantization promises better quality-compression tradeoffs than uniform bit-width. But on hardware-aligned non-consecutive bit-widths {2,4,8,16}, we discover that existing allocation algorithms (greedy, MCKP) systematically FAIL — producing worse results than naive uniform 4-bit across ALL tested architectures. The failure mode is unreported: 2-bit quantization distortions compound non-additively, and solvers consistently over-allocate 2-bit heads. Meanwhile, the field implicitly assumes non-uniform allocation always helps, but no systematic study has tested this across architectures.

- **Existing approaches & gaps**: RateQuant provides R-D optimal per-head allocation via continuous closed-form and discrete greedy (optimal on consecutive integers {2,...,6}). KIVI and ARKV apply uniform or heuristic mixed-precision. However, on hardware-aligned {2,4,8,16}: (a) RateQuant's greedy produces PPL 32.45 vs optimal ~10.91 — polymatroid optimality breaks, (b) unconstrained MCKP fares even worse (PPL 36.92) due to compounding, (c) NO prior work addresses *when* non-uniform allocation is actually beneficial vs when uniform suffices.

- **Our framing**: We present three contributions: (1) the first characterization of 2-bit compounding effects in per-head KV cache quantization — showing that profiling non-additivity causes ALL unconstrained solvers to fail on {2,4,8,16} across 8/8 architectures; (2) a simple universal fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding, makes solver choice irrelevant (greedy=MCKP, Δ=0.0000), and is safely parameterizable (k≤8 universally safe); (3) the first systematic study of *when* non-uniform allocation helps — answer: rarely (1/8 architectures at moderate compression), with a 2-metric diagnostic (9/9 correct) that tells practitioners whether to invest in profiling or just use uniform 4-bit.

- **Headline result template**: "We show that per-head KV cache quantization on hardware-aligned bit-widths has a universal failure mode: 2-bit distortions compound non-additively, causing ALL unconstrained solvers to underperform uniform 4-bit across 8 architectures. A cardinality constraint (≤k heads at 2-bit) universally fixes this, making solver choice irrelevant (greedy=MCKP, Δ=0.0000). Surprisingly, under moderate compression, only 1/8 architectures benefits from non-uniform allocation at all — most models should simply use uniform 4-bit. A 2-metric diagnostic (9/9 accuracy) provides practitioners a simple check to determine when profiling is worthwhile. At long context (8K tokens), the constraint reduces degradation from 11.15× to 1.23× baseline, demonstrating critical deployment value."

## "When Does Non-Uniform Allocation Help?" — Analysis Chapter

Five case studies representing the full spectrum of heterogeneity:

| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |
|------|-------|-----|--------------|------------------------------|---------------|
| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; "spread" pattern (L0 cluster, 4 heads, 26× dominance) |
| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; "spike" pattern (L4H3 single outlier, 64% of total delta) |
| **Marginal** | Llama-3.1-8B | 4:1 | 0.57 (hires) | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |
| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |
| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |

**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.

**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).

**Joint diagnostic** (n=8, 8/8 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike), CodeLlama (0.80, t₁/t₅=0.81 — spike), and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.

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
| Llama-3.1-8B | 4:1 | 256 | **0.57** (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (t₁/t₅≈0.85, single dominant L2H5) | ≈ Marginal |
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
- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 8/8 correct). The "spike vs spread" analysis explains WHY same-GQA models differ.
- **Statistical power**: n=8 models is directional evidence, not statistical claim. Do NOT claim "significant correlation" — use "consistent pattern across 8 architectures" or "8/8 correctly classified by the 0.50 threshold."
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
  status: DONE
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
  status: DONE
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
  status: DONE
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
  status: DONE
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
  status: DONE
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
  status: DONE
  conclusion: success
  metrics:
    baseline_ppl: 6.0306
    uniform_4bit_ppl: 6.1683
    constrained_mckp_ppl: 6.1951
    mckp_vs_uniform_delta: 0.0267
    mckp_delta_ppl: 0.1645
    uniform_delta_ppl: 0.1377
    bit_distribution:
      '2': 8
      '4': 324
      '8': 4
    n_2bit: 8
    max_2bit: 8
    memory_ratio: 0.25
    eval_method: sliding_window_bos_fix
    elapsed_seconds: 490.3
- exp_id: w1_qwen14b_hires_profiling
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_ppl: 5.8432
    concentration: 0.3312
    t1_t5: 0.68
    shape: Flat
    l0_dominance: 15.5
    cv: 3.7418
    positive_heads: 370
    total_heads: 384
    top10_heads:
    - head: L0H5
      delta: 1.84494
    - head: L0H4
      delta: 0.236669
    - head: L0H2
      delta: 0.136971
    - head: L28H4
      delta: 0.099279
    - head: L28H5
      delta: 0.07576
    - head: L27H4
      delta: 0.071269
    - head: L0H0
      delta: 0.070018
    - head: L28H6
      delta: 0.063737
    - head: L26H0
      delta: 0.061462
    - head: L31H3
      delta: 0.061062
    elapsed_min: 161.3
    note: 't1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio'
- exp_id: w1_pythia14b_hires_profiling
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_ppl: 13.6347
    concentration: 0.2439
    t1_t5: 0.28
    shape: Flat
    l0_dominance: 0.51
    cv: 1.2172
    positive_heads: 362
    total_heads: 384
    top5_heads:
    - head: L1H11
      delta: 1.016355
    - head: L12H14
      delta: 0.784513
    - head: L8H4
      delta: 0.759118
    - head: L11H2
      delta: 0.632357
    - head: L13H2
      delta: 0.522849
    elapsed_min: 25.7
    note: 't1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio'
- exp_id: kivi_baseline_qwen_llama
  name: ''
  status: DONE
  conclusion: success
  metrics:
    qwen_2bit_r128: 12.83
    qwen_4bit_r128: 9.9
    qwen_2bit_r0: 13.34
    qwen_4bit_r0: 9.91
    llama_2bit_r128: 9.84
    llama_4bit_r128: 8.14
    llama_2bit_r0: 10.08
    llama_4bit_r0: 8.14
    group_size: 32
    eval_data: WikiText-2 test
    note: r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)
- exp_id: qwen14b_constrained_pipeline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_bf16: 6.8654
    ppl_uniform_4bit: 7.202
    ppl_constrained_mckp: 7.2206
    ppl_unconstrained_mckp: 7.6923
    delta_constrained_vs_uniform: -0.0185
    delta_constrained_vs_uniform_pct: -5.51
    delta_unconstrained_vs_uniform: -0.4902
    bit_distribution_constrained:
      '2': 8
      '4': 374
      '8': 1
      '16': 1
    bit_distribution_unconstrained:
      '2': 77
      '4': 271
      '8': 35
      '16': 1
    concentration: 0.33
    top1_pct: 0.2262
    top5_pct: 0.3304
    t1_t5: 0.68
    shape: Flat
- exp_id: pythia14b_constrained_pipeline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_bf16: 16.4893
    ppl_uniform_4bit: 24.2894
    ppl_constrained_mckp: 24.4521
    ppl_unconstrained_mckp: 31.5415
    concentration: t1=0.0289, t5=0.2439
    t1_t5: 0.0289/0.2439
    shape: Flat
    constrained_vs_uniform_gap: 0.1627
- exp_id: qwen7b_8k_context_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_bf16_8k: 6.97
    ppl_constrained_mckp_8k: 8.59
    ppl_uniform_4bit_8k: 77.75
    ppl_bf16_2k: 9.81
    ppl_constrained_mckp_2k: 10.89
    ppl_uniform_4bit_2k: 15.45
    mckp_improvement_over_uniform_8k: 97.7%
    mckp_improvement_over_uniform_2k: 80.8%
    shape: Spread
    concentration: 0.5992
    context_length: 8192
    note: 'Concentration-dependent benefit amplifies at longer context: uniform 4-bit
      catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust
      (+23%)'
- exp_id: qwen7b_8k_spotcheck
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: yi15_8k_spotcheck
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: llama_8k_spotcheck
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_bf16_8k: 5.5958
    ppl_constrained_mckp_8k: 6.0537
    ppl_uniform_4bit_8k: 6.0364
    mckp_improvement_over_uniform_8k: -0.0174
    mckp_improvement_pct_8k: -3.94
    ppl_bf16_2k: 8.0922
    ppl_constrained_mckp_2k: 8.5042
    ppl_uniform_4bit_2k: 8.4701
    shape: Spike
    concentration: 0.5749
    t1_over_t5: 0.71
    context_length: 8192
    bit_distribution:
      '2': 2
      '4': 253
      '8': 1
- exp_id: kivi_baseline_qwen7b_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_kivi_4bit_g32_r128: 9.8976
    tokens: 298938
    chunks: 583
    stride: 512
    model: Qwen2.5-7B
    comparison_mckp_ppl: 10.91
    comparison_uniform_ppl: 15.45
    comparison_bf16_ppl: 9.81
- exp_id: mistral_hires_constrained_mckp
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: kivi_mckp_combined_qwen7b
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: qwen14b_greedy_constrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    greedy_constrained_ppl: 7.2206
    mckp_constrained_ppl: 7.2206
    delta_vs_mckp: 0
    bit_distribution:
      '2': 8
      '4': 374
      '8': 1
      '16': 1
    memory_ratio: 0.25
    solver_time_sec: 0.08
    total_time_min: 1.8
- exp_id: mistral_uniform_reeval
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mistral_hires_constrained_mckp_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    baseline_wikitext2_ppl: 7.0352
    mckp_wikitext2_ppl: 7.1341
    uniform4bit_wikitext2_ppl: 7.1308
    mckp_improvement_over_uniform: -0.0033
    mckp_improvement_pct: -3.48
    verdict: FAIL
    bit_distribution:
      '2': 2
      '4': 254
    fix_note: 'uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130'
- exp_id: phi3_medium_hires_profiling_check
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: codellama_7b_hires_profiling
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: llama_compounding_sweep
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_k: 0
    best_ppl: 8.0922
    k0_ppl: 8.0922
    k2_ppl: 8.1243
    k4_ppl: 8.1803
    k8_ppl: 8.2259
    k16_ppl: 8.4378
    k32_ppl: 9.0506
    k64_ppl: 11.991
    k128_ppl: 40.2067
    k256_ppl: 1519.1888
    budget: 0.25
- exp_id: mistral_compounding_sweep
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k0_ppl: 7.1308
    k2_ppl: 7.1471
    k4_ppl: 7.164
    k8_ppl: 7.2001
    k16_ppl: 7.31
    k32_ppl: 7.4877
    k64_ppl: 7.5932
    k128_ppl: 7.5932
    k256_ppl: 7.5932
    best_k: 0
    best_ppl: 7.1308
    note: PPL monotonically increases with k; all-4bit optimal at budget=0.25; solver
      saturates at k>=64 (41 actual 2-bit heads)
- exp_id: phi3_medium_hires_profiling
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: llama_downstream_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    arc_challenge:
      fp16: 0.5188
      uniform_4bit: 0.5256
      mckp_k2: 0.5179
    hellaswag:
      fp16: 0.6073
      uniform_4bit: 0.6024
      mckp_k2: 0.6021
    piqa:
      fp16: 0.7922
      uniform_4bit: 0.7873
      mckp_k2: 0.7867
    winogrande:
      fp16: 0.7388
      uniform_4bit: 0.7261
      mckp_k2: 0.7309
    avg_delta_vs_uniform: -0.1
    bit_distribution:
      4bit: 253
      8bit: 1
      2bit: 2
    budget: 0.25
    total_distortion: 0.7015
    elapsed_sec: 3387
- exp_id: yi_mistral_downstream_k2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    yi_k2:
      arc_challenge:
        baseline: 0.5265
        uniform: 0.5205
        mckp_k2: 0.4991
      hellaswag:
        baseline: 0.5912
        uniform: 0.5855
        mckp_k2: 0.5818
      piqa:
        baseline: 0.7949
        uniform: 0.7916
        mckp_k2: 0.7916
      winogrande:
        baseline: 0.7332
        uniform: 0.7206
        mckp_k2: 0.7238
      avg_delta_vs_uniform: -0.0055
      bit_distribution:
        4bit: 189
        8bit: 1
        2bit: 2
    mistral_k2:
      arc_challenge:
        baseline: 0.5043
        uniform: 0.5068
        mckp_k2: 0.5068
      hellaswag:
        baseline: 0.6118
        uniform: 0.6051
        mckp_k2: 0.605
      piqa:
        baseline: 0.8009
        uniform: 0.7987
        mckp_k2: 0.7982
      winogrande:
        baseline: 0.7411
        uniform: 0.7395
        mckp_k2: 0.7388
      avg_delta_vs_uniform: -0.0003
      bit_distribution:
        4bit: 254
        2bit: 2
    elapsed_sec: 2672
- exp_id: mistral_compounding_sweep_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k0_ppl: 7.0352
    k2_ppl: 7.0366
    k4_ppl: 7.0453
    k8_ppl: 7.0636
    k16_ppl: 7.1139
    k32_ppl: 7.2378
    k64_ppl: 7.7747
    k128_ppl: 10.473
    k256_ppl: 45.2766
    budget: 0.25
    n_heads: 256
- exp_id: qwen_compounding_sweep
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen_compounding_sweep_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_k0: 9.8106
    ppl_k8: 10.0474
    ppl_k64: 23.2176
    ppl_k256: 98.7523
    max_compounding_ratio: 10.07
    n_heads_total: 112
    n_2bit_ceiling: 96
    budget: 0.25
- exp_id: codellama_hires_profiling
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_ppl: 7.6978
    top5_concentration: 0.7975
    t1_t5: 0.8131
    distribution_shape: Spike
    cv: 18.3153
    l0_dominance_ratio: 0.8
    top5_sensitive_heads:
    - layer: 1
      head: 1
      delta_2bit: 22.998339
    - layer: 1
      head: 18
      delta_2bit: 2.042989
    - layer: 1
      head: 11
      delta_2bit: 1.460641
    - layer: 0
      head: 15
      delta_2bit: 0.942934
    - layer: 30
      head: 31
      delta_2bit: 0.839968
    total_kv_heads: 1024
    gqa_ratio: 1
    profile_time_hours: 3.7
- exp_id: gemma2_downstream_k2_4task
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: gemma2_downstream_k8_4task
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: qwen_3seed_downstream_ci
  name: ''
  status: DONE
  conclusion: success
  metrics:
    arc_challenge:
      bf16: 0.4582
      uniform: 0.459
      mckp_mean: 0.459
      mckp_std: 0.0035
      delta: 0
    hellaswag:
      bf16: 0.5887
      uniform: 0.5335
      mckp_mean: 0.5748
      mckp_std: 0.0022
      delta: 0.0413
    winogrande:
      bf16: 0.7119
      uniform: 0.6622
      mckp_mean: 0.678
      mckp_std: 0.0115
      delta: 0.0158
    piqa:
      bf16: 0.7818
      uniform: 0.7552
      mckp_mean: 0.7748
      mckp_std: 0.0023
      delta: 0.0196
    avg_delta: 0.0192
    elapsed_sec: 2714
- exp_id: gemma2_downstream_k8_4task_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    arc_challenge:
      baseline: 0.6135
      uniform: 0.6058
      mckp_k8: 0.6049
      delta: -0.0009
    hellaswag:
      baseline: 0.6093
      uniform: 0.6092
      mckp_k8: 0.6089
      delta: -0.0003
    winogrande:
      baseline: 0.7443
      uniform: 0.738
      mckp_k8: 0.7443
      delta: 0.0063
    piqa:
      baseline: 0.8128
      uniform: 0.8036
      mckp_k8: 0.8079
      delta: 0.0043
    avg_delta: 0.0024
    bit_distribution:
      4bit: 324
      2bit: 8
      8bit: 4
    elapsed_sec: 2321
- exp_id: llama_3seed_downstream_ci
  name: ''
  status: DONE
  conclusion: success
  metrics:
    arc_challenge_delta: -0.8
    hellaswag_delta: 0
    piqa_delta: -0.1
    winogrande_delta: 0.5
    avg_delta: -0.1
    std_all_tasks: 0
    note: Single profile → deterministic allocation → all 3 seeds identical
- exp_id: falcon7b_hires_profiling
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: deepseekvl_hires_profiling
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: internlm2_7b_hires_profiling
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: phi3_medium_hires_profiling_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    top5_concentration: 0.1742
    top5_n_heads: 20
    baseline_calibration_ppl: 4.783
    delta_2bit_cv: 0.8905
    layer0_dominance_ratio: 0.04
    shape: Spread
    t1_t5_ratio: 0.24
    top1_head: L9H6
    top1_delta_2bit: 0.1806
    total_heads: 400
    profiling_hours: 2.48
    note: Low concentration but t1/t5=0.24 indicates sensitivity spread across multiple
      heads — confirmed Spread pattern. Mid-layer concentration (L8-L11).
- exp_id: falcon7b_hires_profiling_v2
  name: ''
  status: PENDING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: best
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
  "promptId": "4ac18e22-b68c-4a04-9b13-5cf3c8fb8c23",
  "type": "user",
  "uuid": "25e60572-2476-4499-b526-14c3761a18f3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T02:16:38.268Z_

```json
{
  "parentUuid": "25e60572-2476-4499-b526-14c3761a18f3",
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
  "uuid": "6e6aa511-5249-4835-a7ef-66973870364a",
  "timestamp": "2026-05-16T02:16:38.268Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T02:16:38.268Z_

```json
{
  "parentUuid": "6e6aa511-5249-4835-a7ef-66973870364a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "56f8e6ee-787f-4331-8b5c-211633ba8db4",
  "timestamp": "2026-05-16T02:16:38.268Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 claim 全部成立，reviewer 认可 compounding 发现的新颖性和 constraint 的实用价值，1/8 benefit 被视为诚实的 negative result 而非弱点 核心假设：['A1: 2-bit compounding 在 KV cache 文献中确实未被系统刻画（…",
  "leafUuid": "56f8e6ee-787f-4331-8b5c-211633ba8db4",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "2-bit compounding in KV cache quantization—universal failure and constraint fix",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b"
}
```

---

### Assistant

_source line 8 · 2026-05-16T02:16:58.111Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each experiment in the experiment_plan, under the "best" tier scenario. I need to go through every planned experiment and produce expected results with rationales explaining why those results would occur in this best-case scenario.

Let me carefully go through the experiment plan and the registry to understand what experiments exist and what their actual results were. The user wants me to produce imagined/predicted results for each experiment under the "best" tier assumptions.

Let me read through the experiment plan carefully and produce the YAML output. I need to map each plan_id to its actual results (since most are DONE) and frame them within the "best" tier narrative.
 
I'm re-reading the request to clarify what's being asked. The user wants me to generate the predicted results for each experiment as they would appear under the best-case tier scenario—essentially creating an imagined version of what these experiments would show if everything went optimally. This is part of a simulation exercise for evaluating the paper review outcome.

Now I'll work through each experiment plan systematically, using the actual completed results as the foundation while framing them through the lens of the best tier narrative, and providing clear rationales for why these results support that interpretation.

Generating the comprehensive YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56f8e6ee-787f-4331-8b5c-211633ba8db4",
  "isSidechain": false,
  "requestId": "req_011Cb5Sg6tiGKGPAYkbrLTYE",
  "type": "assistant",
  "uuid": "37260920-a223-4dd1-9907-b082f112ebe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCDCDnhurEdmYnnrFwBT15",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 36251,
      "cache_read_input_tokens": 11841,
      "output_tokens": 20077,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 20077,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 36251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36251
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

_source line 9 · 2026-05-16T02:22:46.714Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。三条 claim 原样保留。Reviewer 认可 2-bit compounding 作为 universal failure mode 的新颖性，
  cardinality constraint 作为 principled intervention（非 trivial heuristic），1/8 benefit 作为对 field 隐含假设的重要修正。
  avg_review_score 3.5-4.0，p_accept 0.4-0.6，major objections 0-1，narrative rewrite 0-10%。

imagined_experiments:
  - name: "L0 exclusion removal"
    plan_id: "plan_001"
    description: >
      移除 solver 中的 L0 硬排除约束，仅保留 max_2bit=8。验证 solver 纯粹从 profiling data 自动发现 L0 sensitivity，
      将 L0 heads 分配到 8-bit。
    expected_results:
      solver_auto_assigns_l0_8bit: true
      ppl_with_l0_exclusion: 10.91
      ppl_without_l0_exclusion: 10.91
      delta: 0.0
      l0_heads_assigned_8bit: 4
      bit_distribution: {2: 8, 4: 100, 8: 4}
    result_rationale: >
      best 档下，profiling data 的信号足够强：L0 的 4 个 head 的 2-bit delta (合计占总 delta 58.6%) 远高于其他 head。
      MCKP solver 在 max_2bit=8 约束下，自然将这 4 个 high-delta head 升到 8-bit，无需硬编码 L0 排除规则。
      这强化了 "constraint 是 principled，不是 ad-hoc" 的叙事——solver 自动发现了结构，constraint 只防止过度分配。
      Reviewer 在 best 档下接受这一点作为 constraint principled-ness 的证据。
    tables:
      - name: "L0 Exclusion Ablation"
        rows:
          - {condition: "With L0 exclusion", ppl: 10.91, l0_bits: "8-bit (forced)", other_2bit: 8}
          - {condition: "Without L0 exclusion", ppl: 10.91, l0_bits: "8-bit (auto)", other_2bit: 8}
    figures_description:
      - "Bit allocation heatmap showing solver auto-discovers L0 sensitivity pattern identical to forced exclusion"
    analysis: >
      PPL delta=0.0 证明 L0 排除是冗余的——profiling quality 足以让 solver 自主发现。
      这消除了 "你的方法依赖 L0 domain knowledge" 的攻击面。

  - name: "Llama-3.1-8B full pipeline"
    plan_id: "plan_002"
    description: >
      在 Llama-3.1-8B (GQA 4:1, 256 KV heads) 上复现完整 pipeline。
      测试 cross-architecture generalizability。
    expected_results:
      baseline_ppl_bf16: 8.09
      uniform_4bit_ppl: 8.47
      mckp_constrained_ppl: 8.45
      mckp_unconstrained_ppl: 8.63
      delta_constrained_vs_uniform: +0.2%
      unconstrained_degradation_ratio: 1.07
      natural_2bit_count: 2
      concentration: 0.57
      distribution_shape: "Spike"
    result_rationale: >
      Llama 是 spike 型架构（L2H5 single dominant head, t₁/t₅≈0.85）。GQA=4:1 + 256 heads 意味着
      sensitivity 分散在大量 heads 上，单个 outlier 无法被 MCKP 充分利用。unconstrained solver 仅选 12 heads
      到 2-bit (4.7%)，compounding 效应轻微但仍存在 (1.07×)。constrained MCKP 与 uniform 几乎持平 (+0.2%)。
      best 档下 reviewer 接受这是对 Claim 3 的正面证据：spike 型 + 低 concentration 架构不需要 non-uniform，
      diagnostic 正确预测了这一结果。7/8 negative 是 contribution 的一部分。
    tables:
      - name: "Llama-3.1-8B Pipeline Results"
        rows:
          - {method: "BF16 baseline", ppl: 8.09}
          - {method: "Uniform 4-bit", ppl: 8.47}
          - {method: "MCKP constrained (k=2)", ppl: 8.45}
          - {method: "MCKP unconstrained", ppl: 8.63}
    figures_description:
      - "Per-head sensitivity heatmap: single dominant L2H5 outlier, rest flat"
    analysis: >
      Llama 代表 "spike + low benefit" 的典型案例。constrained MCKP 自然选 k=2（constraint never binds），
      与 uniform 差异在噪声范围内。unconstrained 仍比 uniform 差 (1.07×)，确认 compounding 是 universal。

  - name: "Mistral-7B-v0.3 full pipeline"
    plan_id: "plan_003"
    description: >
      在 Mistral-7B-v0.3 上复现完整 pipeline。不同架构族验证 cross-architecture validity。
    expected_results:
      baseline_ppl_bf16: 7.04
      uniform_4bit_ppl: 7.13
      mckp_constrained_ppl: 7.16
      mckp_unconstrained_ppl: 7.57
      delta_constrained_vs_uniform: -0.4%
      unconstrained_degradation_ratio: 1.08
      concentration: 0.22
      distribution_shape: "Flat"
      k_ablation_monotonic: true
    result_rationale: >
      Mistral 是 flat 型架构（concentration=0.22, CV=1.31）。profiler 报告近零信号差异——heads 间 sensitivity
      几乎无差别。unconstrained solver 将 42/256=16.4% heads 分到 2-bit，因为无法区分好坏，
      累积 compounding 产生 1.08× 退化。k ablation 单调递增（每增加一个 2-bit head 都是损失），
      证实 profiler zero-signal = uniform 最优。best 档下 reviewer 认可这是 Claim 3 的关键证据：
      flat 型架构 profiling 是浪费，直接 uniform 即可。
    tables:
      - name: "Mistral-7B-v0.3 Pipeline Results"
        rows:
          - {method: "BF16 baseline", ppl: 7.04}
          - {method: "Uniform 4-bit", ppl: 7.13}
          - {method: "MCKP constrained (k=4)", ppl: 7.16}
          - {method: "MCKP unconstrained", ppl: 7.57}
      - name: "Mistral k Ablation"
        rows:
          - {k: 4, ppl: 7.165}
          - {k: 8, ppl: 7.200}
          - {k: 12, ppl: 7.245}
          - {k: 16, ppl: 7.311}
          - {k: 18, ppl: 7.323}
    figures_description:
      - "Monotonically increasing k-PPL curve: zero-signal profiler means every 2-bit allocation hurts"
    analysis: >
      Mistral 的 monotonic k-PPL 曲线与 Qwen 的 U-shaped 形成对比——论文中并列展示，直观说明
      spread vs flat 的根本区别。Constrained 比 uniform 略差 0.4%，确认 non-uniform 无价值。

  - name: "Compounding effect characterization sweep"
    plan_id: "plan_004"
    description: >
      在 Qwen2.5-7B 上 sweep max_2bit 从 0 到 112。绘制 PPL vs max_2bit 曲线，
      定位 compounding threshold。
    expected_results:
      ppl_k0: 9.81
      ppl_k8: 10.05
      ppl_k16: 10.42
      ppl_k32: 11.60
      ppl_k64: 22.95
      ppl_k112: ~98.8
      safe_threshold_k: 8
      degradation_at_k8_pct: 2.4%
      compounding_onset: "k≈16-32"
      curve_shape: "U-shaped with sharp elbow at k≈32"
    result_rationale: >
      Qwen 是 spread 型 (L0 cluster of 4 heads)。k≤8 时，solver 仅将低-sensitivity heads 分到 2-bit，
      compounding 可控 (<2.5%)。k=8 是 sweet spot：允许 8 个 2-bit heads 释放 budget 给 L0 4 heads 升 8-bit，
      PPL 显著优于 uniform。k>16 后 compounding 呈超线性增长——2-bit distortion 通过 residual stream
      非加性累积，profiling 预测 joint PPL≈11 但实际 32-37 (3× error)。best 档下 reviewer 接受这是
      compounding 效应的 first quantitative characterization，U-shaped 曲线是 headline figure。
    tables:
      - name: "Qwen Compounding Sweep"
        rows:
          - {k: 0, ppl: 9.81, ratio_to_baseline: 1.00}
          - {k: 8, ppl: 10.05, ratio_to_baseline: 1.02}
          - {k: 16, ppl: 10.42, ratio_to_baseline: 1.06}
          - {k: 32, ppl: 11.60, ratio_to_baseline: 1.18}
          - {k: 64, ppl: 22.95, ratio_to_baseline: 2.34}
          - {k: 112, ppl: 98.75, ratio_to_baseline: 10.07}
    figures_description:
      - "PPL vs max_2bit sweep: U-shaped curve with safe zone (k≤8), transition zone (16-32), catastrophic zone (>48)"
      - "Superposition: Qwen U-shaped vs Mistral monotonic vs Llama flat — three regimes in one figure"
    analysis: >
      compounding sweep 是 Claim 1 的核心定量证据。k=8 threshold 在所有架构上 universally safe (<2.5% degradation)，
      为 Claim 2 的 constraint parameterization 提供实证基础。

  - name: "Budget sweep (2×, 4×, 8×)"
    plan_id: "plan_005"
    description: >
      在 Qwen2.5-7B 上测试 constrained MCKP 在 compression ratio 2×, 4×, 8×
      (budget=0.5, 0.25, 0.125)。
    expected_results:
      budget_0.5:
        mckp_ppl: ~9.85
        uniform_ppl: ~10.2
        delta_pct: +3.4%
      budget_0.25:
        mckp_ppl: 10.91
        uniform_ppl: 15.45
        delta_pct: +29.4%
      budget_0.125:
        mckp_ppl: ~57.6
        uniform_2bit_ppl: ~2644
        delta_pct: ">97%"
    result_rationale: >
      Compression 越激进，non-uniform allocation 的价值越大。2× 时 budget 充裕，大部分 heads 留在 4-bit，
      差异小。4× 是 paper 主战场，MCKP +29.4% 是 headline。8× 时 uniform 只能全 2-bit (PPL 2644 catastrophic)，
      而 MCKP 通过 cardinality constraint 保护关键 heads 在 4-bit，PPL 57.6——仍然高但 45× better。
      best 档下 reviewer 接受 "compression amplifies benefit" 作为 deployment motivation。
    tables:
      - name: "Budget Sweep Results"
        rows:
          - {budget: 0.50, compression: "2×", mckp_ppl: 9.85, uniform_ppl: 10.2, improvement: "+3.4%"}
          - {budget: 0.25, compression: "4×", mckp_ppl: 10.91, uniform_ppl: 15.45, improvement: "+29.4%"}
          - {budget: 0.125, compression: "8×", mckp_ppl: 57.6, uniform_ppl: 2644, improvement: ">97%"}
    figures_description:
      - "Log-scale PPL vs compression ratio: MCKP and uniform diverge exponentially at aggressive compression"
    analysis: >
      Budget sweep 回答 reviewer Q4 ("How does this work at different compression ratios?")。
      关键 insight: moderate compression 是 practical sweet spot，aggressive compression 展示 constraint 的 catastrophic prevention 价值。

  - name: "High-resolution profiling"
    plan_id: "plan_006"
    description: >
      64 seq × 2048 tokens hires profiling (vs 16×512 lowres)。验证 profiling quality
      影响 allocation quality。
    expected_results:
      hires_mckp_ppl: 10.91
      lowres_mckp_ppl: 11.23
      improvement_ppl: 0.32
      improvement_pct: 2.9%
      hires_nonzero_2bit_heads: 100
      lowres_nonzero_2bit_heads: 37
      profiling_time_min: 65.5
      allocation_diff_count: 8
      bit_distribution: {2: 8, 4: 100, 8: 4}
    result_rationale: >
      hires profiling 将 non-zero 2-bit delta 的 head 数从 37 增到 100/112，给 solver 更多信号区分 heads。
      PPL 从 11.23 降到 10.91 (gap recovery 从 ~75% 升到 ~81%)。8 个 head 的分配发生变化。
      best 档下，reviewer 认可 profiling resolution 是一个 practical hyperparameter，65 min 的开销对
      offline profiling 可接受。这强化了 "profiling data quality matters" 的叙事，但 constraint 仍然是
      primary intervention——hires 只是 marginal improvement on top of constraint。
    tables:
      - name: "Profiling Resolution Comparison"
        rows:
          - {resolution: "16×512 (lowres)", mckp_ppl: 11.23, nonzero_heads: 37, time_min: ~10}
          - {resolution: "64×2048 (hires)", mckp_ppl: 10.91, nonzero_heads: 100, time_min: 65.5}
    figures_description:
      - "Per-head delta heatmap: lowres vs hires, showing hires reveals mid-layer sensitivity structure"
    analysis: >
      hires profiling 是论文 §5.4 的 ablation。关键区别：lowres 下 solver 只能区分 37 heads，
      hires 下能区分 100 heads。但两者 bit distribution 完全相同 (2:8, 4:100, 8:4)——constraint 的稳定性
      进一步证明它是 robust intervention。

  - name: "C4 cross-dataset evaluation"
    plan_id: "plan_007"
    description: >
      在 C4 上 calibrate 和 evaluate，验证结果不依赖 WikiText-2。包含 cross-domain transfer。
    expected_results:
      c4_cal_wt2_eval_mckp_ppl: 11.29
      c4_cal_wt2_eval_uniform_ppl: 15.45
      allocation_agreement_c4_vs_wt2: 0.964
      agreement_heads: "108/112"
      cross_domain_wt2_to_c4_mckp_ppl: 20.56
      cross_domain_wt2_to_c4_uniform_ppl: 35.42
      contamination_impact: 0.034
    result_rationale: >
      96.4% allocation agreement (108/112 heads) 证明 profiling-based allocation 对 calibration data 的 choice 鲁棒。
      4 个不一致 heads 的 delta 差异小，对最终 PPL 影响仅 0.034。cross-domain transfer (wt2→c4) 同样
      MCKP >> uniform (20.56 vs 35.42)。best 档下 reviewer 接受 "calibration-robust" 的 claim，
      不要求额外 calibration domain 实验。WikiText-2 contamination 不是 concern。
    tables:
      - name: "Cross-Dataset Calibration"
        rows:
          - {calibration: "WikiText-2", eval: "WikiText-2", mckp_ppl: 10.91, uniform_ppl: 15.45}
          - {calibration: "C4", eval: "WikiText-2", mckp_ppl: 11.29, uniform_ppl: 15.45}
          - {calibration: "WikiText-2", eval: "C4", mckp_ppl: 20.56, uniform_ppl: 35.42}
    figures_description: []
    analysis: >
      C4 实验回答 "WikiText-2 specific?" 质疑。96.4% agreement 是 strong evidence。
      cross-domain transfer 性能比同 domain 差但 MCKP 优势保持。

  - name: "RateQuant greedy comparison"
    plan_id: "plan_008"
    description: >
      实现 RateQuant Algorithm 1 greedy 在 {2,4,8,16} 上。证明 polymatroid optimality
      在非连续 bit-width 上 breaks。
    expected_results:
      greedy_unconstrained_ppl: 32.45
      mckp_unconstrained_ppl: 36.92
      uniform_4bit_ppl: 15.45
      greedy_2bit_count: 68
      greedy_bit_dist: {2: 68, 4: 30, 8: 4, 16: 10}
    result_rationale: >
      RateQuant 的 greedy 依赖 polymatroid structure (Prop. 6)，要求 bit-width 是连续整数 {2,...,6}。
      在 {2,4,8,16} 上，marginal gain per bit 的 submodularity breaks：2→4 的 gain-per-bit 与 4→8 的
      gain-per-bit 不再单调，greedy 过度分配 2-bit (68/112 = 60.7%)。PPL 32.45 (3.31× baseline)。
      甚至 MCKP unconstrained 更差 (36.92)——因为 independent profiling 低估了 joint 2-bit distortion。
      best 档下 reviewer 接受这是 RateQuant 在 hardware-aligned bit-widths 上的 genuine gap，
      我们的 constraint 修复了这个 gap。
    tables:
      - name: "RateQuant vs MCKP on {2,4,8,16}"
        rows:
          - {method: "RateQuant greedy (unconstrained)", ppl: 32.45, "2bit_heads": 68}
          - {method: "MCKP (unconstrained)", ppl: 36.92, "2bit_heads": "~70"}
          - {method: "Uniform 4-bit", ppl: 15.45, "2bit_heads": 0}
    figures_description:
      - "Bit allocation comparison: greedy vs MCKP vs constrained, showing over-allocation of 2-bit"
    analysis: >
      核心 differentiation evidence。两个 SOTA solver 都 fail——问题不在 solver algorithm，在 compounding。
      这消除了 "换个更好的 solver 就行" 的反驳。

  - name: "Oracle comparison"
    plan_id: "plan_009"
    description: >
      Brute-force optimal allocation on subset of layers。量化 MCKP 与 oracle 的 gap。
    expected_results:
      mckp_ppl: 10.91
      max_oracle_gap_ppl: 0.018
      avg_oracle_gap_ppl: 0.005
      layers_mckp_optimal: "5/8"
      layers_with_gap: 3
      gap_nature: "2-bit head position swap within same bit budget"
      total_evals: 54
    result_rationale: >
      constrained MCKP 在 5/8 layers 上 exactly optimal。3 个 layer 上存在 0.005-0.018 PPL 的微小 gap，
      来源是 2-bit head 的位置交换（同一 bit budget 内选择不同的 head 放 2-bit）。gap < 0.02 PPL 证明
      constrained MCKP 是 near-optimal solver，独立 profiling 的 non-additivity 在 k≤8 时可控。
      best 档下 reviewer 不会追问 oracle gap——0.018 PPL 在 baseline 9.81 上是 0.18%，可忽略。
    tables:
      - name: "Oracle Gap by Layer Group"
        rows:
          - {layer_group: "L0-L3", oracle_gap: 0.0}
          - {layer_group: "L1", oracle_gap: 0.018}
          - {layer_group: "L4", oracle_gap: 0.005}
          - {layer_group: "L11", oracle_gap: 0.014}
    figures_description: []
    analysis: >
      Oracle comparison 回答 "MCKP 是否足够好"。avg gap 0.005 证明 constrained MCKP + independent profiling
      在 k≤8 下是 practically optimal。gap 的 nature (position swap) 说明 non-additivity 在小 k 下
      影响 limited to head ordering，不影响 bit budget 分配。

  - name: "Cross-domain calibration robustness"
    plan_id: "plan_010"
    description: >
      calibrate on C4, evaluate on WikiText-2 (and vice versa)。报告 per-head allocation agreement。
    expected_results:
      allocation_agreement_c4_vs_wt2: 0.964
      agreement_heads: "108/112"
      c4_cal_wt2_eval_mckp_ppl: 11.29
      wt2_cal_c4_eval_mckp_ppl: 20.56
      contamination_impact: 0.034
    result_rationale: >
      同 plan_007。per-head sensitivity 的 ranking 主要由 architecture 决定（哪些 head 做 attention
      over long-range patterns），calibration data 的 domain 只影响 delta 的 magnitude 而非 ordering。
      96.4% agreement 是 strong cross-domain robustness。best 档下 reviewer 满意。
    tables: []
    figures_description: []
    analysis: "与 plan_007 合并报告。96.4% agreement 是 appendix 的支撑数据。"

  - name: "Head sensitivity visualization"
    plan_id: "plan_011"
    description: >
      生成 paper-quality figures: per-head delta heatmap, compounding curve, allocation comparison。
    expected_results:
      figures_generated: 3
      heatmap_shows_l0_cluster: true
      compounding_curve_shows_u_shape: true
      allocation_chart_shows_over_allocation: true
    result_rationale: >
      可视化是 paper 的 communication backbone。best 档下 reviewer 通过图理解三个核心 claim：
      (1) heatmap 立即可见 L0 cluster 的 spread pattern vs 其他架构的 flat/spike，
      (2) compounding curve 的 U-shape 直观展示 k=8 sweet spot，
      (3) allocation comparison 清晰对比 unconstrained (60% 2-bit) vs constrained (7% 2-bit) vs uniform (0% 2-bit)。
      好的 figure 降低 reviewer cognitive load，增加 acceptance probability。
    tables: []
    figures_description:
      - "Fig 1: Per-head 2-bit delta heatmap (layer × head) for Qwen — L0 cluster clearly visible"
      - "Fig 2: PPL vs max_2bit sweep — Qwen U-shape, Llama flat, Mistral monotonic in one panel"
      - "Fig 3: Stacked bar chart of bit allocation across methods (unconstrained / constrained / uniform)"
    analysis: "Figures 是论文最重要的 communication tool。Fig 2 (compounding curve) 是 contribution 的 single best visualization。"

  - name: "Downstream task evaluation (Qwen)"
    plan_id: "plan_012"
    description: >
      ARC-C / HellaSwag / PIQA / WinoGrande on Qwen2.5-7B at 4× compression。
      验证 PPL improvement 转化为 downstream gain。
    expected_results:
      arc_c: {uniform: 0.481, mckp: 0.514, delta_pp: 3.16}
      hellaswag: {uniform: 0.728, mckp: 0.768, delta_pp: 4.00}
      piqa: {uniform: 0.766, mckp: 0.779, delta_pp: 1.25}
      winogrande: {uniform: 0.662, mckp: 0.682, delta_pp: 1.97}
      avg_recovery_pct: 72.8
      bf16_baseline_avg: ~0.699
    result_rationale: >
      Qwen 是 spread 型，PPL 提升 27.3% (15.45→10.91)。downstream 任务与 PPL 的相关性在 moderate compression
      下通常成立。+1.25 到 +4.00pp 的 per-task gain 与 PPL gap 的 magnitude 一致——HellaSwag 和 ARC-C
      对 KV cache quality 最敏感（需要 multi-hop reasoning），PIQA 最不敏感（常识判断，单步）。
      72.8% avg recovery 意味着 constrained MCKP 恢复了从 baseline 到 uniform 4-bit 退化的 72.8%。
      best 档下 reviewer 接受 downstream consistency 作为 PPL claim 的 validation。
    tables:
      - name: "Qwen2.5-7B Downstream (0-shot)"
        rows:
          - {task: "ARC-C", bf16: 0.529, uniform_4bit: 0.481, mckp: 0.514, delta_pp: "+3.16"}
          - {task: "HellaSwag", bf16: 0.783, uniform_4bit: 0.728, mckp: 0.768, delta_pp: "+4.00"}
          - {task: "PIQA", bf16: 0.793, uniform_4bit: 0.766, mckp: 0.779, delta_pp: "+1.25"}
          - {task: "WinoGrande", bf16: 0.690, uniform_4bit: 0.662, mckp: 0.682, delta_pp: "+1.97"}
    figures_description:
      - "Bar chart: BF16 / Uniform / MCKP per task, with recovery % annotation"
    analysis: >
      Downstream eval 是 reviewer 必问项 (Q7)。Qwen 的 consistent gains across 4 tasks 验证 PPL→downstream 转化。
      HellaSwag +4.00pp 是 headline downstream 数字。

  - name: "Qwen2.5-72B profiling (scale test)"
    plan_id: "plan_013"
    description: >
      在 72B 上运行 profiling-only。分析 sensitivity patterns 是否随 model size scale。
    expected_results:
      status: "killed (GPU memory)"
      partial_result: "L0 sensitivity pattern visible in partial profiling"
      paper_treatment: "mentioned as future work"
    result_rationale: >
      72B profiling 在现有 GPU 资源下被 killed (OOM)。best 档下 reviewer 接受这是 resource limitation，
      不是 methodological flaw。7B/9B/14B 的 cross-scale evidence (Qwen-7B, Qwen-14B) 已经
      demonstrate sensitivity pattern scales。72B 是 "nice to have"，论文中列为 future work。
      reviewer 可能作为 minor revision 要求之一，但不影响 acceptance。
    tables: []
    figures_description: []
    analysis: "72B 是 0-1 个 major objection 的 potential source。best 档下以 future work 处理。"

  - name: "K/V separation"
    plan_id: "plan_014"
    description: >
      K 和 V heads 作为独立 MCKP items。测试 K/V asymmetric budget 是否优于 joint K=V。
    expected_results:
      kv_sep_ppl: 11.22
      joint_kv_ppl: 10.91
      uniform_4bit_ppl: 15.45
      delta_sep_vs_joint: +0.30
      sep_k_2bit_count: 16
      sep_v_uniform_4bit: true
      kv_asymmetric_heads: 21
    result_rationale: >
      K/V separation 在 Qwen 上略差 (+0.30 PPL)。原因：K heads 的 sensitivity 分布与 V heads 不同——
      V heads 更 uniform (solver 将 V 全部留 4-bit)，K heads 有更多 heterogeneity (16 个 2-bit vs joint 的 8 个)。
      分离后 K side 过度分配 2-bit (少了 V heads 的 budget 共享 buffering)。best 档下 reviewer 认可
      negative result：K/V joint optimization 更好，framework 自然 handles K/V without asymmetric treatment。
      这回答了 reviewer Q6 ("RateQuant does K/V asymmetric allocation, do you?")。
    tables:
      - name: "K/V Separation Ablation"
        rows:
          - {method: "Joint K+V MCKP", ppl: 10.91, "k_2bit": 8, "v_2bit": 0}
          - {method: "Separate K/V MCKP", ppl: 11.22, "k_2bit": 16, "v_2bit": 0}
          - {method: "Uniform 4-bit", ppl: 15.45, "k_2bit": 0, "v_2bit": 0}
    figures_description: []
    analysis: >
      Negative result 但有 insight value：V heads 对 quantization 更 robust，K heads 更 sensitive。
      Joint optimization 通过 budget sharing 自动 discovers 这一点。

  - name: "L0-only heuristic baseline"
    plan_id: "plan_015"
    description: >
      最简单的 non-uniform 策略：L0 全部 8-bit，其余 4-bit。以及 L0-constrained random 和 naive positional。
      测试 MCKP 是否优于 trivial heuristics。
    expected_results:
      mckp_constrained_ppl: 10.91
      l0_random_mean: 11.69
      l0_random_std: 0.42
      l0_random_median: 11.52
      naive_positional_ppl: 12.23
      uniform_4bit_ppl: 15.45
      mckp_vs_l0_random_median_gap: -5.2%
      qwen_mckp_beats_all_heuristics: true
      llama_mckp_ppl: 8.45
      llama_l0_random_median: 10.04
      llama_mckp_vs_l0_gap: -15.8%
      mistral_mckp_ppl: 7.16
      mistral_l0_random_median: 7.59
      mistral_mckp_vs_l0_gap: -5.7%
    result_rationale: >
      L0-random (随机选 k 个非 L0 heads 放 2-bit) 在 Qwen 上 median 11.52 vs MCKP 10.91。
      MCKP 的 profiling-based 选择 consistently beats random by 5-16%。naive positional (按 layer 顺序)
      更差 (12.23)。关键 insight：L0 sensitivity 是 necessary but not sufficient——MCKP 还需要正确选择
      which non-L0 heads 放 2-bit。Llama 上 gap 更大 (15.8%) 因为只有 2 个 optimal 2-bit heads，
      random selection 容易选到 sensitive heads。best 档下 reviewer 接受 MCKP 优于 all tested heuristics，
      profiling 有 genuine value (在 benefit 存在的架构上)。
    tables:
      - name: "Allocation Baseline Comparison (3 models)"
        rows:
          - {model: "Qwen", mckp: 10.91, l0_random_median: 11.52, naive: 12.23, uniform: 15.45}
          - {model: "Llama", mckp: 8.45, l0_random_median: 10.04, naive: 9.94, uniform: 8.47}
          - {model: "Mistral", mckp: 7.16, l0_random_median: 7.59, naive: 7.48, uniform: 7.13}
    figures_description:
      - "Grouped bar chart: MCKP / L0-random / Naive / Uniform across 3 models"
    analysis: >
      MCKP consistently outperforms all heuristics on all 3 models。但 Llama 和 Mistral 上 MCKP 仍不如 uniform，
      reinforcing Claim 3：profiling 只在 spread 型上有 net value。

  - name: "Greedy + cardinality constraint ablation (solver equivalence)"
    plan_id: "plan_016"
    description: >
      RateQuant greedy + max_2bit=8 vs MCKP + max_2bit=8。验证 constraint 是 primary intervention，
      solver choice 无关。
    expected_results:
      greedy_constrained_ppl: 11.2312
      mckp_constrained_ppl: 11.2312
      delta: 0.0000
      greedy_unconstrained_ppl: 32.45
      mckp_unconstrained_ppl: 36.92
      bit_distribution_both: {2: 8, 4: 100, 8: 4}
      allocation_identical: true
    result_rationale: >
      这是论文最重要的 ablation。Δ=0.0000 意味着 constrained greedy 和 constrained MCKP 产生
      IDENTICAL bit allocation。原因：cardinality constraint (k=8) 将 feasible set 缩小到
      C(100,8)×C(8,4) 个可行解，在这个 reduced space 里 greedy 的 marginal gain ordering
      与 MCKP 的 global optimal 收敛。unconstrained 下两者都 fail（但 mode 不同：greedy 32.45 vs MCKP 36.92），
      constrained 下都 succeed 且完全一致。best 档下 reviewer 认可这是 "constraint is THE contribution"
      的最 powerful evidence——practitioners 不需要实现 MCKP，只需给现有 greedy 加一个参数。
      A3 假设 (solver equivalence proves constraint is core) 完全成立。
    tables:
      - name: "Solver Equivalence (Qwen, k=8)"
        rows:
          - {solver: "Greedy unconstrained", ppl: 32.45, "2bit_heads": 68}
          - {solver: "MCKP unconstrained", ppl: 36.92, "2bit_heads": "~70"}
          - {solver: "Greedy + max_2bit=8", ppl: 11.2312, "2bit_heads": 8}
          - {solver: "MCKP + max_2bit=8", ppl: 11.2312, "2bit_heads": 8}
          - {solver: "Uniform 4-bit", ppl: 15.45, "2bit_heads": 0}
    figures_description:
      - "2×2 matrix: {unconstrained, constrained} × {greedy, MCKP} — the key figure showing constraint is what matters"
    analysis: >
      Solver equivalence table 是 Claim 2 的 crown jewel。建议作为 Table 1 or prominently in §4。
      Reviewer 在 best 档下将 Δ=0.0000 视为 compelling evidence that "the cardinality constraint,
      not the solver, is the core contribution." 同时在 Qwen-14B 上 greedy=MCKP (Δ=0.0000) 复现。

  - name: "Multi-seed error bars"
    plan_id: "plan_017"
    description: >
      3 个不同 calibration seeds 的 constrained MCKP 和 uniform 4-bit on Qwen2.5-7B。
      报告 mean±std。
    expected_results:
      mckp_mean: 10.99
      mckp_std: 0.065
      mckp_seeds: [11.02, 10.90, 11.05]
      uniform_4bit_ppl: 15.45
      bit_dist_all_seeds: "2:8, 4:100, 8:4"
      allocation_agreement_3way: 0.902
      pairwise_agreement_range: [0.911, 0.946]
    result_rationale: >
      std=0.065 在 mean=10.99 上是 0.59% CV——非常稳定。所有 3 seeds 产生 identical macro allocation
      (2:8, 4:100, 8:4)，90.2% heads 在 3 seeds 间完全一致。不一致的 ~10% heads 是 sensitivity 接近的
      mid-range heads (borderline 2-bit vs 4-bit)，对 PPL 影响 <0.1。uniform 是 deterministic (15.45)，
      MCKP mean 10.99 与 hires single-run 10.91 差 0.08——来自 calibration data sampling variance。
      best 档下 reviewer 接受 error bar 证明 robustness，不要求更多 seeds。
      "MCKP 10.99±0.065 vs Uniform 15.45" 的 confidence interval 完全不重叠。
    tables:
      - name: "Multi-Seed Results (Qwen, 4×)"
        rows:
          - {seed: 0, mckp_ppl: 11.02, bit_dist: "2:8 4:100 8:4"}
          - {seed: 1, mckp_ppl: 10.90, bit_dist: "2:8 4:100 8:4"}
          - {seed: 2, mckp_ppl: 11.05, bit_dist: "2:8 4:100 8:4"}
          - {summary: "Mean±Std", mckp_ppl: "10.99±0.065", bit_dist: "identical"}
          - {reference: "Uniform 4-bit", ppl: 15.45, bit_dist: "all 4-bit"}
    figures_description:
      - "Error bar plot: MCKP (3 seeds) vs Uniform, with CI bands"
    analysis: >
      Error bars 是 reviewer 必问项。std=0.065 证明 single-run results 是 representative。
      macro allocation 在 seeds 间 stable。remaining variance 来自 borderline heads 的 ordering。

  - name: "Runtime/latency benchmark"
    plan_id: "plan_018"
    description: >
      端到端 inference latency 和 throughput：mixed-precision KV cache vs uniform 4-bit vs BF16。
    expected_results:
      bf16_decode_ms: 33.78
      uniform_4bit_decode_ms: 42.46
      mckp_decode_ms: 46.09
      mckp_solver_sec: 0.005
      bf16_throughput: 29.6
      uniform_4bit_throughput: 23.6
      mckp_throughput: 21.8
      theoretical_memory_4x_compression: true
      mckp_overhead_vs_uniform_pct: 8.5%
    result_rationale: >
      mixed-precision KV cache 比 uniform 4-bit 慢 8.5% (46.09 vs 42.46 ms/tok)。原因：
      per-head 不同 bit-width 需要 dynamic dequantization dispatch，而 uniform 可以 batch all heads
      同一 kernel。MCKP solver 本身只需 0.005 sec (negligible)。memory 完全相同 (5.25 MB, 4× compression)。
      best 档下 reviewer 接受 8.5% latency overhead 作为 reasonable trade-off——PPL 从 15.45 降到 10.91
      (29% improvement) 的代价是 8.5% latency。论文应该诚实报告 latency overhead 而非隐藏。
      reviewer 可能作为 minor revision 要求 longer-sequence latency 数据（长序列下 KV cache decode
      是 bottleneck，overhead 比例可能变化）。
    tables:
      - name: "Runtime Benchmark (Qwen, seq_len=2048)"
        rows:
          - {method: "BF16", prefill_ms: 45.86, decode_ms: 33.78, throughput: 29.6, memory_MB: 21}
          - {method: "Uniform 4-bit", prefill_ms: 54.25, decode_ms: 42.46, throughput: 23.6, memory_MB: 5.25}
          - {method: "Constrained MCKP", prefill_ms: 57.03, decode_ms: 46.09, throughput: 21.8, memory_MB: 5.25}
    figures_description:
      - "Latency breakdown bar chart with memory footprint overlay"
    analysis: >
      Runtime benchmark 回答 systems reviewer concern。8.5% overhead 是 honest cost。
      但 long-context scenario (8K tokens) 是 deployment motivation：uniform 4-bit at 8K degrades 11.15×
      while MCKP stays at 1.23× — the quality gap more than justifies the latency cost.
      MCKP solver overhead (5ms) 是 one-time cost, amortized over entire inference session.

  # === Additional cross-architecture experiments (beyond original plan) ===

  - name: "Gemma-2-9B full pipeline"
    plan_id: "gemma2_9b_full_pipeline"
    description: >
      Gemma-2-9B (GQA 2:1, 336 KV heads) 完整 pipeline。最低 GQA ratio 的 anchor point。
    expected_results:
      baseline_ppl: 6.03
      uniform_4bit_ppl: 6.17
      constrained_mckp_ppl: 6.20
      unconstrained_degradation_ratio: 1.47
      concentration: 0.23
      distribution_shape: "Flat"
      n_2bit_unconstrained: 106
    result_rationale: >
      Gemma-2 是 flat 型 (concentration=0.23, CV=1.28)。solver 无法区分 heads，unconstrained 将
      106/336=31.5% heads 分到 2-bit。每个 head 的 per-head delta 很小但累积效应产生 1.47× degradation——
      这是 "moderate" tier，不是 catastrophic 也不是 mild。best 档下 reviewer 要求 paper 讨论
      three-tier labeling (catastrophic 3.31× / moderate 1.47× / mild 1.07-1.08×)，这 strengthens
      "constraint 对所有架构都有价值" 的 claim。constrained MCKP 将 2-bit 从 106 减到 8，PPL 6.20 vs uniform 6.17——
      delta 在噪声范围，确认 flat 型不需要 non-uniform。
    tables:
      - name: "Gemma-2-9B Results"
        rows:
          - {method: "BF16 baseline", ppl: 6.03}
          - {method: "Uniform 4-bit", ppl: 6.17}
          - {method: "MCKP constrained (k=8)", ppl: 6.20}
          - {method: "MCKP unconstrained", ppl: 8.85, note: "1.47× baseline"}
    figures_description: []
    analysis: >
      Gemma-2 的 1.47× moderate degradation 是论文需要主动讨论的 point。
      它证明 constraint 即使在 flat 型上也有 value (106→8 2-bit heads)，strengthens universality claim。

  - name: "Yi-1.5-9B full pipeline"
    plan_id: "yi15_9b_full_pipeline"
    description: >
      Yi-1.5-9B (GQA 8:1, 192 KV heads) 完整 pipeline。最高 GQA ratio 的 counterexample。
    expected_results:
      baseline_ppl: 7.02
      uniform_4bit_ppl: 7.22
      hires_mckp_ppl: 7.22
      unconstrained_degradation_ratio: 1.08
      concentration: 0.71
      distribution_shape: "Spike"
      t1_t5: 0.90
      l4h3_dominance: "single outlier, 64% of total delta"
    result_rationale: >
      Yi-1.5 是 spike 型 (L4H3 single extreme outlier, concentration 0.71 但 t₁/t₅=0.90)。
      GQA 8:1 是所有测试模型中最高，但 benefit = 0%。原因：single outlier 不 create optimization opportunity——
      solver 给 L4H3 升 8-bit 后，剩余 heads 全部 near-identical sensitivity，无法区分。
      这 disproves "higher GQA = more benefit" naive hypothesis。best 档下 reviewer 认可 Yi-1.5
      是 diagnostic 的 critical validation：concentration 0.71 > 0.50 threshold，但 t₁/t₅=0.90 > 0.70——
      joint diagnostic 正确预测 "no benefit"。单用 concentration 会误判。
    tables:
      - name: "Yi-1.5-9B Results"
        rows:
          - {method: "BF16 baseline", ppl: 7.02}
          - {method: "Uniform 4-bit", ppl: 7.22}
          - {method: "MCKP constrained (k=2)", ppl: 7.22}
          - {method: "Diagnostic prediction", result: "No benefit (conc=0.71 BUT t₁/t₅=0.90 > 0.70)"}
    figures_description:
      - "Scatter: Yi-1.5 vs Qwen in (concentration, t₁/t₅) space — both high concentration but different t₁/t₅"
    analysis: >
      Yi-1.5 是 Claim 3 的 strongest supporting evidence。GQA 最高但 benefit 最低——
      joint diagnostic 的 necessity 因此建立。

  - name: "Cross-architecture compounding sweeps"
    plan_id: "llama_compounding_sweep + mistral_compounding_sweep_v2 + qwen_compounding_sweep_v2"
    description: >
      Llama, Mistral, Qwen 各自的 compounding sweep (PPL vs k)。三个 regime 对比。
    expected_results:
      qwen_curve: "U-shaped, optimal k=8, catastrophic k>32"
      llama_curve: "Monotonic but gentle, k=0 optimal at 4×, catastrophic k>128"
      mistral_curve: "Monotonic, k=0 optimal, catastrophic k>128"
      qwen_k8_degradation_pct: 2.4
      llama_k8_degradation_pct: 1.7
      mistral_k8_degradation_pct: 0.4
      universally_safe_k: 8
    result_rationale: >
      三种 curve 形状反映三种 sensitivity distribution：
      - Qwen (spread): k=8 释放 budget 给 L0 cluster → PPL 下降；k>8 compounding → PPL 上升 = U-shape
      - Llama (spike): 每增加一个 2-bit head 都轻微增加 PPL，但 sensitivity 分散所以增速慢
      - Mistral (flat): 与 Llama 类似但更 flat，所有 head 贡献相似 compounding
      关键：k≤8 在所有三种 regime 下 degradation < 2.5%，证明 k=8 是 universally safe threshold。
      best 档下 reviewer 接受 3-architecture sweep 作为 constraint parameterization 的实证基础。
    tables:
      - name: "Compounding Sweep Summary (k=8)"
        rows:
          - {model: "Qwen", k8_ppl: 10.05, baseline: 9.81, degradation_pct: 2.4, curve: "U-shaped"}
          - {model: "Llama", k8_ppl: 8.23, baseline: 8.09, degradation_pct: 1.7, curve: "Monotonic gentle"}
          - {model: "Mistral", k8_ppl: 7.06, baseline: 7.04, degradation_pct: 0.4, curve: "Monotonic flat"}
    figures_description:
      - "Three-panel compounding curve: Qwen / Llama / Mistral, with k=8 safe zone shaded"
    analysis: >
      Cross-architecture compounding sweep 是 universality claim 的 quantitative backbone。
      三种 curve 形状 + 一个 universally safe k = principled parameterization。

  - name: "8K long-context evaluation"
    plan_id: "qwen7b_8k_context_eval"
    description: >
      Qwen2.5-7B 在 8K token context 下的 PPL 评估。Long-context amplification effect。
    expected_results:
      ppl_bf16_8k: 6.97
      ppl_mckp_8k: 8.59
      ppl_uniform_4bit_8k: 77.75
      mckp_degradation_ratio_8k: 1.23
      uniform_degradation_ratio_8k: 11.15
      degradation_gap: "9×"
      ppl_bf16_2k: 9.81
      ppl_mckp_2k: 10.91
      ppl_uniform_4bit_2k: 15.45
    result_rationale: >
      Long context 放大 2-bit compounding：uniform 4-bit 在 8K 下 PPL 77.75 (11.15× baseline)。
      原因：每个 decode step 的 attention 覆盖更多 KV cache entries，2-bit quantization error
      在 longer attention span 上累积更多。constrained MCKP 通过保护 sensitive heads 在 higher bit-width，
      仅 1.23× degradation。9× gap in degradation rate 是 deployment motivation 的 headline 数字。
      best 档下 reviewer 认可 long-context 结果作为 practical impact evidence——real deployment 通常
      operates at 4K-32K context，uniform 4-bit 在此范围内 unacceptable。
    tables:
      - name: "Long Context PPL (Qwen, 4×)"
        rows:
          - {context: "2K", bf16: 9.81, mckp: 10.91, uniform: 15.45, mckp_ratio: "1.11×", uniform_ratio: "1.57×"}
          - {context: "8K", bf16: 6.97, mckp: 8.59, uniform: 77.75, mckp_ratio: "1.23×", uniform_ratio: "11.15×"}
    figures_description:
      - "PPL vs context length: MCKP stays flat while uniform 4-bit explodes — the deployment motivation figure"
    analysis: >
      Long-context result 是 paper 的 deployment hook。"11.15× vs 1.23×" 在 abstract 中出现。
      Reviewer 在 best 档下将此视为 constraint 的 practical value 的 strongest evidence。

  - name: "Qwen-14B constrained pipeline + solver equivalence"
    plan_id: "qwen14b_constrained_pipeline + qwen14b_greedy_constrained"
    description: >
      Qwen2.5-14B (384 KV heads) 验证 scale generalization 和 solver equivalence。
    expected_results:
      baseline_ppl: 6.87
      uniform_4bit_ppl: 7.20
      constrained_mckp_ppl: 7.22
      unconstrained_mckp_ppl: 7.69
      greedy_constrained_ppl: 7.22
      delta_greedy_vs_mckp: 0.0000
      concentration: 0.33
      shape: "Flat"
      unconstrained_over_uniform: true
    result_rationale: >
      Qwen-14B (384 heads, flat 型 concentration=0.33) 展示两点：
      (1) unconstrained still fails (7.69 > 7.20 uniform)，即使在 14B scale
      (2) solver equivalence 完美复现 (greedy constrained = MCKP constrained, Δ=0.0000)
      14B 是 flat 型所以 non-uniform benefit ≈ 0%，与 Claim 3 一致。
      best 档下 reviewer 认可 14B 作为 scale validation + solver equivalence 的 second data point。
    tables:
      - name: "Qwen-14B Results"
        rows:
          - {method: "BF16", ppl: 6.87}
          - {method: "Uniform 4-bit", ppl: 7.20}
          - {method: "MCKP constrained", ppl: 7.22}
          - {method: "Greedy constrained", ppl: 7.22, note: "Δ=0.0000 vs MCKP"}
          - {method: "MCKP unconstrained", ppl: 7.69}
    figures_description: []
    analysis: >
      Solver equivalence 在 14B 上完美复现，strengthens "constraint makes solver irrelevant" universality。

  - name: "Pythia-1.4B constrained pipeline"
    plan_id: "pythia14b_constrained_pipeline"
    description: >
      Pythia-1.4B (MHA, 384 KV heads) 在非 GQA 架构上验证。
    expected_results:
      baseline_ppl: 16.49
      uniform_4bit_ppl: 24.29
      constrained_mckp_ppl: 24.45
      unconstrained_mckp_ppl: 31.54
      delta_constrained_vs_uniform: -0.16
      concentration: 0.24
      shape: "Flat"
    result_rationale: >
      Pythia 是 MHA (non-GQA) 架构，384 KV heads，flat 型 (concentration=0.24)。
      unconstrained 显著 fail (31.54 vs 24.29 uniform, 1.30×)。constrained 与 uniform 几乎持平。
      best 档下 reviewer 认可：(1) compounding 不仅影响 GQA 架构，MHA 同样受害，strengthens universality；
      (2) flat 型 non-uniform 无价值，consistent with diagnostic prediction。
    tables:
      - name: "Pythia-1.4B Results"
        rows:
          - {method: "BF16", ppl: 16.49}
          - {method: "Uniform 4-bit", ppl: 24.29}
          - {method: "MCKP constrained", ppl: 24.45}
          - {method: "MCKP unconstrained", ppl: 31.54}
    figures_description: []
    analysis: >
      Pythia 扩展 architecture coverage 到 MHA (GQA ratio 1:1)。8/8 unconstrained degradation confirmed。

  - name: "Phi-3-medium hires profiling"
    plan_id: "phi3_medium_hires_profiling_v2"
    description: >
      Phi-3-medium (400 KV heads) profiling。第 8 个架构，完成 8/8 universality。
    expected_results:
      concentration: 0.17
      t1_t5: 0.24
      shape: "Spread (low concentration)"
      cv: 0.89
      top1_head: "L9H6"
      total_heads: 400
    result_rationale: >
      Phi-3-medium concentration=0.17 (lowest in our test set)，但 t₁/t₅=0.24 suggests sensitivity
      spread across multiple mid-layer heads (L8-L11 cluster)。低 concentration + low t₁/t₅ 是
      "diffuse spread" pattern——sensitivity exists but not concentrated enough for MCKP to exploit at 4×。
      best 档下这补全了第 8 个架构的 profiling data，支持 8/8 unconstrained degradation universality claim。
      full constrained pipeline 未完成（资源限制），但 profiling pattern is sufficient for diagnostic validation。
    tables:
      - name: "Phi-3-medium Profiling Summary"
        rows:
          - {metric: "Top-5% concentration", value: 0.17}
          - {metric: "t₁/t₅", value: 0.24}
          - {metric: "Distribution shape", value: "Diffuse spread"}
          - {metric: "Diagnostic prediction", value: "No benefit at 4× (conc < 0.50)"}
    figures_description: []
    analysis: >
      Phi-3-medium 是 diagnostic 的 edge case：concentration 低但 t₁/t₅ 也低。
      Joint diagnostic 预测 no benefit (concentration < 0.50)。9/9 accuracy 如果 full pipeline 确认。

  - name: "CodeLlama-7B profiling"
    plan_id: "codellama_hires_profiling"
    description: >
      CodeLlama-7B (MHA, 1024 KV heads) profiling。Spike pattern validation。
    expected_results:
      concentration: 0.80
      t1_t5: 0.81
      shape: "Spike"
      top1_head: "L1H1 (delta=23.0)"
      total_heads: 1024
      diagnostic_prediction: "No benefit (t₁/t₅=0.81 > 0.70)"
    result_rationale: >
      CodeLlama 是 extreme spike：L1H1 delta=23.0，next head 仅 2.04。concentration 0.80 (highest tested)
      但 t₁/t₅=0.81——single dominant outlier。与 Yi-1.5 (0.71/0.90) 类似的 spike pattern。
      Joint diagnostic 正确预测 no benefit (t₁/t₅ > 0.70)。best 档下 reviewer 认可 CodeLlama 作为
      concentration alone 不够的 second example (alongside Yi-1.5)，justifying joint diagnostic。
    tables:
      - name: "CodeLlama-7B Profiling"
        rows:
          - {metric: "Concentration", value: 0.80}
          - {metric: "t₁/t₅", value: 0.81}
          - {metric: "Shape", value: "Spike (L1H1 dominant)"}
          - {metric: "Diagnostic", value: "No benefit (conc>0.50 BUT t₁/t₅>0.70)"}
    figures_description: []
    analysis: >
      CodeLlama 与 Yi-1.5 形成 spike-pattern pair。两者都有 high concentration 但 high t₁/t₅——
      single outlier cannot be exploited by MCKP。9/9 diagnostic accuracy (9th model)。

  - name: "KIVI baseline comparison"
    plan_id: "kivi_baseline_qwen_llama + kivi_baseline_qwen7b_v2"
    description: >
      KIVI (per-channel group quantization) 作为 orthogonal baseline。验证 per-head 方法的 positioning。
    expected_results:
      qwen_kivi_4bit_g32_r128: 9.90
      qwen_kivi_4bit_g32_r0: 9.91
      qwen_mckp_constrained: 10.91
      qwen_uniform_4bit: 15.45
      llama_kivi_4bit_r128: 8.14
      llama_uniform_4bit: 8.47
    result_rationale: >
      KIVI 4-bit (g32, r128) 在 Qwen 上 PPL 9.90——比我们的 constrained MCKP 10.91 更好。
      但两者是 orthogonal 且 complementary：KIVI 优化 per-channel group quantization granularity，
      我们优化 per-head bit-width allocation。best 档下 reviewer 理解 positioning：
      (1) 我们的 contribution 是 compounding failure mode 的 discovery + constraint fix，不是 beat KIVI
      (2) KIVI + 我们的 constraint 可以 combine (per-head allocation + per-channel group quantization)
      (3) KIVI 的 group quantization 减轻了 per-value quantization error，所以在 uniform bit-width 下更好
      Paper 应清晰 position as complementary，不 compete on PPL numbers。
    tables:
      - name: "KIVI Comparison (Qwen, 4×)"
        rows:
          - {method: "KIVI 4-bit (g32, r128)", ppl: 9.90, approach: "per-channel"}
          - {method: "Constrained MCKP", ppl: 10.91, approach: "per-head"}
          - {method: "Uniform 4-bit (ours)", ppl: 15.45, approach: "per-head"}
          - {method: "BF16 baseline", ppl: 9.81, approach: "—"}
    figures_description: []
    analysis: >
      KIVI 是 orthogonal method。论文 position：KIVI 优化 within-bit quantization quality，
      我们优化 cross-bit allocation + discover failure mode。两者 combine for further improvement。

  - name: "Cross-architecture downstream eval (Yi, Llama, Mistral, Gemma-2)"
    plan_id: "w3_downstream_eval + gemma2_downstream_k8_4task_v2"
    description: >
      5 个模型的完整 downstream eval (5 tasks, 0-shot)。验证 PPL→downstream consistency。
    expected_results:
      qwen_avg_delta_vs_uniform: "+1.92pp"
      yi_avg_delta_vs_uniform: "-0.77pp"
      llama_avg_delta_vs_uniform: "-0.99pp"
      mistral_avg_delta_vs_uniform: "-0.48pp"
      gemma2_avg_delta_vs_uniform: "+0.14pp (noise)"
      downstream_consistency_with_ppl: "5/5"
      arc_challenge_systematic_degradation: true
    result_rationale: >
      Downstream results 完美 mirror PPL patterns：Qwen (spread) 是唯一 consistent gainer (+1.25 to +4.00pp)。
      4 个 non-spread 模型显示 minor systematic degradation (Yi -0.77, Llama -0.99, Mistral -0.48) 或
      noise (Gemma-2 +0.14)。arc_challenge 是 worst-case task (Yi -3.24pp, Llama -2.65pp)——
      multi-step reasoning 对 KV cache error 最敏感。best 档下 reviewer 要求 paper 诚实报告
      per-task tables 并讨论 arc_challenge 系统性信号，但接受 diagnostic 正确预测 downstream outcomes (5/5)
      作为 Claim 3 的 strong validation。
    tables:
      - name: "Downstream Summary (5 models, 0-shot avg)"
        rows:
          - {model: "Qwen (Spread)", delta_pp: "+1.92", prediction: "Benefit", correct: "✓"}
          - {model: "Yi-1.5 (Spike)", delta_pp: "-0.77", prediction: "No benefit", correct: "✓"}
          - {model: "Llama (Spike)", delta_pp: "-0.99", prediction: "No benefit", correct: "✓"}
          - {model: "Mistral (Flat)", delta_pp: "-0.48", prediction: "No benefit", correct: "✓"}
          - {model: "Gemma-2 (Flat)", delta_pp: "+0.14", prediction: "No benefit", correct: "✓"}
    figures_description:
      - "Per-task heatmap: 5 models × 5 tasks, color-coded by delta vs uniform"
    analysis: >
      5/5 downstream consistency 是 diagnostic 的 ultimate validation。论文必须：
      (a) 报告完整 per-task tables，(b) 用 "shows minor degradation" 不用 "preserves accuracy"，
      (c) 主动讨论 arc_challenge 作为 worst-case。

  - name: "Qwen 3-seed downstream CI"
    plan_id: "qwen_3seed_downstream_ci"
    description: >
      3 个 calibration seeds 的 downstream eval，提供 confidence intervals。
    expected_results:
      hellaswag_delta: "+4.13pp"
      hellaswag_std: 0.0022
      winogrande_delta: "+1.58pp"
      winogrande_std: 0.0115
      piqa_delta: "+1.96pp"
      piqa_std: 0.0023
      arc_challenge_delta: "0.00pp"
      arc_challenge_std: 0.0035
      avg_delta: "+1.92pp"
    result_rationale: >
      3-seed downstream CI 显示 low variance (std 0.002-0.012)。HellaSwag 和 PIQA 的 gain 是 robust
      (CI 不含 0)。arc_challenge delta=0 with std=0.0035 说明 arc_challenge 上 MCKP 和 uniform 差异
      在统计噪声内——但 mean 仍正（与单 seed 的 +3.16pp 不矛盾，因为 3-seed 用了不同 calibration data）。
      WinoGrande std=0.0115 较高，反映 task 的 inherent variance。best 档下 reviewer 接受
      3-seed CI 证明 downstream gains 是 robust，不要求更多 seeds。
    tables:
      - name: "3-Seed Downstream CI (Qwen)"
        rows:
          - {task: "HellaSwag", delta: "+4.13pp", std: 0.0022, robust: "✓"}
          - {task: "PIQA", delta: "+1.96pp", std: 0.0023, robust: "✓"}
          - {task: "WinoGrande", delta: "+1.58pp", std: 0.0115, robust: "✓"}
          - {task: "ARC-C", delta: "0.00pp", std: 0.0035, robust: "borderline"}
    figures_description: []
    analysis: >
      3-seed CI 是 statistical credibility 的必要 evidence。HellaSwag/PIQA robust，
      ARC-C borderline（可能需要 more seeds 作为 minor revision）。

  - name: "W9 compounding scaling (top-k vs random-k)"
    plan_id: "w9_compounding_v2"
    description: >
      Compounding scaling test: top-k (most sensitive) vs random-k heads at 2-bit。
      证明 compounding 是 universal，不依赖 which heads selected。
    expected_results:
      k8_topk_ppl: 10.04
      k8_randomk_mean: 11.07
      k8_randomk_std: 0.69
      k16_topk_ppl: 10.42
      k16_randomk_mean: 12.91
      k32_topk_ppl: 11.60
      k32_randomk_mean: 18.33
      k64_topk_ppl: 22.95
      k64_randomk_mean: 55.94
      compounding_ratio_k64_topk: 4.89
      compounding_ratio_k64_randomk: 8.88
    result_rationale: >
      top-k 选最 sensitive heads 放 2-bit——每个 head 的 per-head impact 最大但 compounding 仍然发生。
      random-k compounding 更严重因为随机可能选到 correlated heads（同一 layer 的多个 head 同时 2-bit
      导致该 layer 的 representation 整体崩溃）。两者都展示超线性增长：k=8→k=64 的 PPL 增长远超 8× ratio。
      best 档下这是 Claim 1 (non-additivity) 的 controlled experiment evidence：
      如果 distortion 是 additive，random-k 应该 ≈ sum of individual deltas，但实际 8.88× > linear prediction。
    tables:
      - name: "Top-k vs Random-k Compounding"
        rows:
          - {k: 8, topk: 10.04, randomk_mean: "11.07±0.69", ratio_topk: "1.56×", ratio_randomk: "1.76×"}
          - {k: 16, topk: 10.42, randomk_mean: "12.91±0.40", ratio_topk: "1.56×", ratio_randomk: "2.10×"}
          - {k: 32, topk: 11.60, randomk_mean: "18.33±2.53", ratio_topk: "1.78×", ratio_randomk: "2.73×"}
          - {k: 64, topk: 22.95, randomk_mean: "55.94±9.73", ratio_topk: "4.89×", ratio_randomk: "8.88×"}
    figures_description:
      - "Log-scale PPL vs k: top-k vs random-k with variance bands — superlinear growth = non-additivity evidence"
    analysis: >
      Top-k vs random-k 是 non-additivity 的 cleanest experimental evidence。
      Random-k 的 higher variance 和 worse mean 说明 head selection matters —— 但即使 top-k (best case)
      也展示 compounding。这支持 "constraint is needed regardless of solver quality"。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37260920-a223-4dd1-9907-b082f112ebe0",
  "isSidechain": false,
  "requestId": "req_011Cb5Sg6tiGKGPAYkbrLTYE",
  "type": "assistant",
  "uuid": "6401cdd1-65a9-492c-b6e3-64543f1c4c33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCDCDnhurEdmYnnrFwBT15",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 36251,
      "cache_read_input_tokens": 11841,
      "output_tokens": 20077,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 20077,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 36251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36251
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 claim 全部成立，reviewer 认可 compounding 发现的新颖性和 constraint 的实用价值，1/8 benefit 被视为诚实的 negative result 而非弱点 核心假设：['A1: 2-bit compounding 在 KV cache 文献中确实未被系统刻画（…",
  "leafUuid": "6401cdd1-65a9-492c-b6e3-64543f1c4c33",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "2-bit compounding in KV cache quantization—universal failure and constraint fix",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 claim 全部成立，reviewer 认可 compounding 发现的新颖性和 constraint 的实用价值，1/8 benefit 被视为诚实的 negative result 而非弱点 核心假设：['A1: 2-bit compounding 在 KV cache 文献中确实未被系统刻画（…",
  "leafUuid": "6401cdd1-65a9-492c-b6e3-64543f1c4c33",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "2-bit compounding in KV cache quantization—universal failure and constraint fix",
  "sessionId": "ef6aff79-615e-462c-9b0b-b3504a778d9b"
}
```

---
