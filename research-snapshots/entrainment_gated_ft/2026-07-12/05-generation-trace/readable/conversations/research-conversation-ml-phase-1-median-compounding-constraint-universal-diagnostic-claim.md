# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Compounding 发现和 constraint 有效性被认可，但 'universal' 语言和 diagnostic 的 claim 强度受

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/141b11e8-8b0e-437b-b7b1-f0f21e658ad9.jsonl`
- **Structured JSON:** [`347432a7e378daf0c26c.json`](../../sessions/34/347432a7e378daf0c26c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T02:22:49.025Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T02:22:49.025Z",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Compounding 发现和 constraint 有效性被认可，但 'universal' 语言和 diagnostic 的 claim 强度受到质疑；需要降低 claim 语气并补充实验\n核心假设：['A1: compounding 被认可为有价值的实证发现，但 reviewer 指出 RateQuant Appendix M 已 acknowledge 该现象（novelty 打折）', \"A2: 8 个架构不足以支撑 'universal'——reviewer 要求去掉该词或补充至 12+ 模型\", \"A3: constraint 被部分 reviewer 视为 'obvious in hindsight' / 'just a hyperparameter'，需要更强的 principled justification\", \"A4: 1/8 benefit 被 1-2 个 reviewer 视为方法有效性不足的证据（'method only works on Qwen'）\", 'A5: diagnostic n=9 被拒绝作为独立 claim——只能作为 observation 或 hypothesis', 'A6: 缺少 eviction baseline 和 multi-seed downstream CI 被标为 significant gap']\n关键指标范围：{'avg_review_score_arr': [2.8, 3.5], 'claims_surviving_intact': [1, 2], 'p_accept_emnlp_main': [0.15, 0.35], 'major_reviewer_objections': [2, 3], 'narrative_rewrite_pct': [25, 45], 'unconstrained_degradation_universality': [6, 8], 'solver_equivalence_delta': [0.0, 0.001], 'diagnostic_accuracy': [7, 9], 'downstream_consistency_with_ppl': [4, 5]}\n叙事方向：需要调整 claim 强度。(1) \"universal failure mode\" → \"consistent failure pattern across 8 diverse architectures\"， 去掉 universal 一词，改为 \"widespread\" 或 \"systematic\"。(2) constraint contribution 从 \"核心方法贡献\"  重新定位为 \"principled analysis insight that yields a practical fix\"——强调分析贡献而非方法贡献。 (3) diagnostic 从独立 claim 降级为 Section 5 的 empirical observation + \"testable hypothesis for future work\"。 补充实验：(a) 2-3 个额外架构的 profiling（不需要 full pipeline），(b) downstream multi-seed CI 至少在 Qwen 上， (c) 在 related work 中更显式地讨论 RateQuant Appendix M 的 compounding acknowledgment 并 clarify 区别。 论文 reframe 为 \"empirical analysis paper with practical implications\" 而非 \"method paper\"。 EMNLP Efficient Methods track 仍然适合，但需要在 intro 中前置 analysis contribution。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ratekv\nfocus: Evaluate the compounding-forward framing: core contribution is 2-bit compounding as universal failure mode + constraint as universal fix + \"non-uniform rarely helps\" as key negative result. N=1 Spread is a feature (7/8 don't need non-uniform) not a bug. Compare with concentration-dependent framing where N=1 was a weakness.\n\n## paper_framing.md\n\n# Paper Framing — ratekv\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)\n- Track: Efficient Methods for NLP\n\n## bf16 Consistency Resolution (2026-05-14)\n\n**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。\n\n**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。\n\n| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |\n|------|---------------------|----------------------|-----------|\n| Baseline | **9.8106** | 8.819 | 9.81 |\n| Uniform 4-bit | **15.4454** | — | 15.45 |\n| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |\n| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |\n\n## Core Insight\n\nPer-head KV cache quantization on hardware-aligned bit-widths {2,4,8,16} has an unreported universal failure mode: 2-bit quantization distortions compound non-additively through the residual stream, causing ALL tested unconstrained solvers (greedy, MCKP) to systematically over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 architectures (1.07×–3.31× baseline). A cardinality constraint (≤k heads at 2-bit) universally prevents this over-allocation, and furthermore reduces the feasible set to where solver choice becomes irrelevant (greedy = MCKP, Δ=0.0000). Under moderate compression (4×), only 1/8 architectures benefits from non-uniform allocation over uniform 4-bit — providing the first empirical evidence that the implicit assumption \"non-uniform is always better than uniform\" is wrong in KV cache quantization. The core contribution is the compounding effect discovery + universal constraint fix, not the allocation algorithm.\n\n## Core Claims (3 条)\n\n1. **2-bit compounding is a universal failure mode for unconstrained per-head allocation**: On hardware-aligned non-consecutive bit-widths {2,4,8,16}, per-head independent profiling distortions compound non-additively when multiple heads are simultaneously assigned 2-bit quantization. This causes ALL tested unconstrained solvers to over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 diverse architectures (Qwen 3.31×, Gemma-2 1.47×, Yi 1.08×, Llama 1.07×, Mistral 1.08×, Pythia, Qwen-14B, Phi-3-medium). Quantitative evidence of non-additivity: per-head profiling predicts joint PPL ≈11 but actual joint 2-bit PPL is 32–37 (3× prediction error). This is the first systematic characterization of compounding effects in per-head KV cache quantization. Long-context amplifies the failure: at 8K tokens, uniform 4-bit degrades 11.15× baseline while constrained MCKP degrades only 1.23× — a 9× gap in degradation rate.\n\n2. **A cardinality constraint is the universal fix — and makes solver choice irrelevant**: A simple cardinality constraint (max_2bit ≤ k) is sufficient to prevent compounding across ALL tested architectures. Three universally beneficial properties: (a) prevents catastrophic over-allocation on sensitive architectures (Qwen: 32.45 → 10.91), (b) prevents moderate over-allocation on flat architectures (Gemma-2: 8.85 → 6.17, reducing 2-bit heads from 106 to 8), (c) reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce IDENTICAL bit allocations and PPL (Δ=0.0000). The constraint is parameterizable via small-scale compounding test (k≤8 universally safe: <2.5% degradation across all architectures). Practical implication: practitioners need only add one integer parameter to existing pipelines.\n\n3. **Non-uniform allocation benefit is rare — most models should use uniform 4-bit**: Under moderate compression (4×), only 1/8 tested architectures (Qwen2.5-7B, \"spread\" sensitivity pattern) benefits from non-uniform allocation (+27.3% PPL, +1.9pp downstream avg). The remaining 7/8 show no benefit or minor degradation (<1pp avg downstream). A 2-metric empirical diagnostic (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly classifies all 9 tested models (9/9 accuracy), providing practitioners a simple check: if the diagnostic says \"no\" — skip profiling and use uniform 4-bit with zero quality loss. This is the first systematic study of *when* non-uniform KV cache quantization is beneficial, correcting the implicit assumption that it always helps.\n\n## Story Spine\n\n- **Problem**: Per-head mixed-precision KV cache quantization promises better quality-compression tradeoffs than uniform bit-width. But on hardware-aligned non-consecutive bit-widths {2,4,8,16}, we discover that existing allocation algorithms (greedy, MCKP) systematically FAIL — producing worse results than naive uniform 4-bit across ALL tested architectures. The failure mode is unreported: 2-bit quantization distortions compound non-additively, and solvers consistently over-allocate 2-bit heads. Meanwhile, the field implicitly assumes non-uniform allocation always helps, but no systematic study has tested this across architectures.\n\n- **Existing approaches & gaps**: RateQuant provides R-D optimal per-head allocation via continuous closed-form and discrete greedy (optimal on consecutive integers {2,...,6}). KIVI and ARKV apply uniform or heuristic mixed-precision. However, on hardware-aligned {2,4,8,16}: (a) RateQuant's greedy produces PPL 32.45 vs optimal ~10.91 — polymatroid optimality breaks, (b) unconstrained MCKP fares even worse (PPL 36.92) due to compounding, (c) NO prior work addresses *when* non-uniform allocation is actually beneficial vs when uniform suffices.\n\n- **Our framing**: We present three contributions: (1) the first characterization of 2-bit compounding effects in per-head KV cache quantization — showing that profiling non-additivity causes ALL unconstrained solvers to fail on {2,4,8,16} across 8/8 architectures; (2) a simple universal fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding, makes solver choice irrelevant (greedy=MCKP, Δ=0.0000), and is safely parameterizable (k≤8 universally safe); (3) the first systematic study of *when* non-uniform allocation helps — answer: rarely (1/8 architectures at moderate compression), with a 2-metric diagnostic (9/9 correct) that tells practitioners whether to invest in profiling or just use uniform 4-bit.\n\n- **Headline result template**: \"We show that per-head KV cache quantization on hardware-aligned bit-widths has a universal failure mode: 2-bit distortions compound non-additively, causing ALL unconstrained solvers to underperform uniform 4-bit across 8 architectures. A cardinality constraint (≤k heads at 2-bit) universally fixes this, making solver choice irrelevant (greedy=MCKP, Δ=0.0000). Surprisingly, under moderate compression, only 1/8 architectures benefits from non-uniform allocation at all — most models should simply use uniform 4-bit. A 2-metric diagnostic (9/9 accuracy) provides practitioners a simple check to determine when profiling is worthwhile. At long context (8K tokens), the constraint reduces degradation from 11.15× to 1.23× baseline, demonstrating critical deployment value.\"\n\n## \"When Does Non-Uniform Allocation Help?\" — Analysis Chapter\n\nFive case studies representing the full spectrum of heterogeneity:\n\n| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |\n|------|-------|-----|--------------|------------------------------|---------------|\n| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; \"spread\" pattern (L0 cluster, 4 heads, 26× dominance) |\n| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; \"spike\" pattern (L4H3 single outlier, 64% of total delta) |\n| **Marginal** | Llama-3.1-8B | 4:1 | 0.57 (hires) | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |\n| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |\n| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |\n\n**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.\n\n**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).\n\n**Joint diagnostic** (n=8, 8/8 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike), CodeLlama (0.80, t₁/t₅=0.81 — spike), and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.\n\n## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)\n\n| Method | PPL | Bit Distribution | Budget |\n|--------|-----|-------------------|--------|\n| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |\n| MCKP unconstrained | 36.92 | — | 0.25 |\n| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |\n\nKey takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.\n\n## Cross-Architecture Evidence Summary\n\n| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |\n|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|\n| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |\n| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |\n| Llama-3.1-8B | 4:1 | 256 | **0.57** (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (t₁/t₅≈0.85, single dominant L2H5) | ≈ Marginal |\n| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |\n| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |\n\n**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:\n- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding\n- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta\n- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)\n- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads\n\n**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):\n\nThree-tier labeling (NOT binary catastrophe/benign):\n- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding\n- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions\n- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)\n\nReviewer-suggested paragraph for paper (1 段, 3-4 句):\n\"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\"\n\nThis **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.\n\n⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.\n\n**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.\n\n**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.\n\n### Mistral k Ablation (256 KV heads, budget=0.25)\n\nPPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).\n\n| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |\n|---|-----|-------|-------|-------|--------|-----|\n| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |\n| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |\n| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |\n| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |\n| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |\n| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |\n\nContrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.\n\n### Llama k Ablation (256 KV heads, budget=0.25)\n\nAll k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).\n\n### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)\n\n**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅\n\n| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |\n|------|---------------|------------|---|---------------|\n| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |\n| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |\n| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |\n| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |\n| **Avg recovery** | — | — | **72.8%** | — |\n\n**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.7946 | 0.7854 | -0.92pp |\n| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |\n| hellaswag | 0.5857 | 0.5797 | -0.60pp |\n| piqa | 0.7927 | 0.7894 | -0.33pp |\n| winogrande | 0.7174 | 0.7301 | +1.27pp |\n| **Average** | **0.6822** | **0.6745** | **-0.77pp** |\n\n**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.8173 | 0.8039 | -1.34pp |\n| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |\n| hellaswag | 0.6026 | 0.6012 | -0.14pp |\n| piqa | 0.7867 | 0.7802 | -0.65pp |\n| winogrande | 0.7253 | 0.7238 | -0.15pp |\n| **Average** | **0.6915** | **0.6816** | **-0.99pp** |\n\n**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=4) | Δ |\n|------|---------------|------------|---|\n| arc_easy | — | — | — |\n| arc_challenge | — | — | — |\n| hellaswag | — | — | — |\n| piqa | — | — | — |\n| winogrande | — | — | — |\n| **Average** | **0.6894** | **0.6846** | **-0.48pp** |\n\n**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)\n\n| Task | Uniform 4-bit | MCKP | Δ |\n|------|---------------|------|---|\n| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |\n\n**Downstream summary (Reviewer-verified framing)**:\n- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**\n- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)\n- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)\n- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise\n- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)\n- **Paper must**: (a) report full per-task tables, not just averages, (b) use \"shows minor degradation\" NOT \"preserves accuracy\" — the latter has spin, (c) note arc_challenge as worst-case explicitly\n- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance\n- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论：\"ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\"\n- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞：\"Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge).\"\n\n## Allocation Baseline Evidence (plan_015, mckp_reeval)\n\nAll numbers from unified bf16 eval pipeline, budget=0.25.\n\n| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |\n|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|\n| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |\n| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |\n| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |\n\n**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.\n\n**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.\n\n## Differentiation from RateQuant\n\n| Aspect | RateQuant | Ours |\n|--------|-----------|------|\n| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |\n| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |\n| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |\n| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |\n| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |\n| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |\n| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |\n\n## Venue Fit Risks\n\n- **\"The constraint is just a heuristic, not a real contribution\"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.\n- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.\n- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive \"higher GQA = more benefit\" hypothesis and shows our diagnostic is needed.\n- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 8/8 correct). The \"spike vs spread\" analysis explains WHY same-GQA models differ.\n- **Statistical power**: n=8 models is directional evidence, not statistical claim. Do NOT claim \"significant correlation\" — use \"consistent pattern across 8 architectures\" or \"8/8 correctly classified by the 0.50 threshold.\"\n- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.\n\n## Anticipated Reviewer Concerns\n\n1. **\"The cardinality constraint is trivial — just cap the extreme allocations\"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.\n2. **\"This is just RateQuant with a constraint added\"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.\n3. **\"The method only works on Qwen — isn't this a Qwen paper?\"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.\n4. **\"How does this work at different compression ratios?\"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.\n5. **\"n=3/4/5 models is not enough for the heterogeneity claim\"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.\n6. **\"RateQuant does K/V asymmetric allocation, do you?\"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.\n7. **\"Where are the downstream task results?\"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use \"shows minor degradation\" not \"preserves accuracy\".\n8. **\"The profiler distortion=0.0 on Mistral suggests the profiling method is broken\"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.\n9. **\"If solver doesn't matter, why present MCKP at all?\"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim:\n  - 2\n  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.\n    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.\n    Strengthens narrative: \"solver automatically discovers sensitivity structure.\"\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: exp_d_no_l0_exclusion\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_002\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).\n    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability\n    across different GQA ratios and architectures. Fallback if HF token unavailable:\n    Yi-1.5-9B (non-gated, similar scale).\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: llama_full_pipeline\n  model: Llama-3.1-8B\n  fallback_model: Yi-1.5-9B\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 8.7\n    uniform_4bit_ppl_bf16: 8.47\n    baseline_ppl_bf16: 8.09\n    delta_vs_uniform: -0.23\n    memory_ratio: 0.25\n- id: plan_003\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture\n    family to establish cross-architecture validity.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mistral_full_pipeline\n  model: Mistral-7B-v0.3\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 7.564\n    uniform_4bit_ppl_bf16: 7.131\n    baseline_ppl_bf16: 7.035\n    delta_vs_uniform: -0.433\n    memory_ratio: 0.25\n- id: plan_004\n  claim:\n  - 3\n  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112\n    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map\n    the compounding threshold. Establishes the principled basis for cardinality constraint\n    selection.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: compounding_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_005\n  claim:\n  - 2\n  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,\n    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline\n    at same budget.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: budget_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_006\n  claim:\n  - 1\n  - 2\n  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).\n    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers\n    mid-layer heterogeneity and improves solver allocation beyond current results.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_e_hires_profile\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    constrained_ppl_bf16: 9.569\n    baseline_ppl_bf16: 8.819\n    exp_c_ppl_bf16: 11.345\n    delta_vs_exp_c: -1.776\n    memory_ratio: 0.25\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    profile_resolution:\n      hires_nonzero_2bit: 100\n      lowres_nonzero_2bit: 37\n      hires_nonzero_4bit: 6\n      lowres_nonzero_4bit: 4\n      total_heads: 112\n    allocation_diff_count: 8\n    profiling_time_min: 65.5\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.\n    Cross-dataset evaluation to show results are not WikiText-2 specific.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  eval: C4\n  status: DONE\n  conclusion: success\n  metrics: &id001\n    c4_cal_wt2_eval_mckp_ppl: 11.2942\n    c4_cal_wt2_eval_uniform_ppl: 15.4454\n    c4_cal_wt2_eval_delta: 4.1512\n    c4_cal_bf16_baseline: 12.6505\n    wt2_bf16_baseline: 9.8106\n    allocation_agreement_c4_vs_wt2: 0.964\n    agreement_heads: 108/112\n    bit_dist: 2bit:8, 4bit:100, 8bit:4\n    cross_domain_wt2_to_c4_mckp_ppl: 20.5601\n    cross_domain_wt2_to_c4_uniform_ppl: 35.4232\n    cross_domain_c4_bf16: 15.3246\n    old_contaminated_ppl: 11.3285\n    contamination_impact: 0.0343\n    models_completed: Qwen2.5-7B only\n- id: plan_008\n  claim:\n  - 2\n  description: 'RateQuant comparison: implement RateQuant''s greedy algorithm (Algorithm\n    1) on our discrete action set {2,4,8,16}-bit. RateQuant''s Prop. 6 optimality\n    relies on consecutive-integer polymatroid structure which breaks on non-consecutive\n    sets. Show greedy produces suboptimal allocation vs constrained MCKP. Critical\n    for differentiation claim — must have experimental evidence.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: ratequant_greedy_comparison\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_009\n  claim:\n  - 2\n  description: 'Oracle comparison: brute-force optimal allocation on a subset (3-4\n    layer groups) of Qwen2.5-7B. Quantify MCKP gap to oracle.\n\n    '\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_006\n  registry_id: oracle_comparison\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_ppl: 10.9131\n    max_oracle_gap_ppl: 0.0183\n    avg_oracle_gap_ppl: 0.0046\n    layers_mckp_optimal: 5/8\n    layers_with_gap: 3\n    gap_layers:\n      L1: 0.0183\n      L4: 0.0045\n      L11: 0.0136\n    gap_nature: 2-bit head position swap within same bit budget\n    total_evals: 54\n    runtime_min: 21.3\n- id: plan_010\n  claim:\n  - 2\n  description: 'Cross-domain calibration robustness: calibrate on C4, evaluate on\n    WikiText-2 (and vice versa). Report per-head allocation agreement rate across\n    calibration sources.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_007\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: plan_011\n  claim:\n  - 1\n  description: 'Head sensitivity visualization: generate paper-quality figures showing\n    per-head profiling delta heatmap across layers, compounding effect curve, and\n    budget allocation comparison chart.\n\n    '\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_004\n  - plan_006\n  registry_id: head_sensitivity_viz\n  status: DONE\n  conclusion: success\n- id: plan_014\n  claim:\n  - 2\n  description: 'K/V separation: treat K and V heads as independent MCKP items with\n    separate budget allocation. Compare joint K+V optimization vs current uniform\n    K=V approach. RateQuant supports asymmetric K/V (e.g. K=2.85, V=2.15 avg bits)\n    — we should show MCKP naturally handles this.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: kv_separation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    kv_sep_ppl: 11.2162\n    joint_kv_ppl: 10.9131\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_sep_vs_joint: 0.303\n    sep_k_2bit_count: 16\n    sep_v_uniform_4bit: true\n    kv_asymmetric_heads: 21\n- id: plan_012\n  claim:\n  - 1\n  - 2\n  description: 'Downstream task evaluation: ARC-C / HellaSwag / PIQA / WinoGrande\n    on Qwen2.5-7B at 4× compression. Must match RateQuant''s eval suite for direct\n    comparison. Tests whether PPL improvements translate to downstream performance.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  registry_id: downstream_eval_qwen\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    avg_recovery: 0.728\n    arc_c: 0.5137\n    hellaswag: 0.7684\n    piqa: 0.7786\n    winogrande: 0.6819\n    arc_c_delta_pp: 3.16\n    hellaswag_delta_pp: 4\n    piqa_delta_pp: 1.25\n    winogrande_delta_pp: 1.97\n- id: plan_013\n  claim:\n  - 1\n  description: '70B profiling-only: run distortion profiling on Qwen2.5-72B (no full\n    eval). Analyze whether sensitivity patterns (Layer 0 dominance, compounding threshold)\n    scale with model size.\n\n    '\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: qwen72b_profiling\n  model: Qwen2.5-72B\n  status: DONE\n  conclusion: killed\n- id: plan_015\n  claim:\n  - 2\n  description: 'L0-only heuristic baseline: assign 8-bit to all Layer 0 KV heads,\n    uniform 4-bit to all other heads, at 4x compression on Qwen2.5-7B. This is the\n    simplest possible non-uniform strategy exploiting L0 sensitivity. If L0-only matches\n    or beats constrained MCKP, the full optimization machinery is unnecessary. Must\n    also test on Llama and Mistral. Critical missing baseline flagged by Dream review.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: l0_only_heuristic\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: killed\n- id: plan_016\n  claim:\n  - 2\n  description: 'RateQuant greedy + cardinality constraint ablation: add max_2bit=k\n    constraint to RateQuant greedy Algorithm 1 on {2,4,8,16}. Compare three conditions:\n    (a) RateQuant greedy unconstrained (already have: PPL ~32.45), (b) RateQuant greedy\n    + cardinality k=8, (c) constrained MCKP k=8 (already have: PPL ~11.23). If (b)\n    matches (c), the contribution is the cardinality constraint, not the MCKP solver.\n    If (c) beats (b), discrete MCKP optimization genuinely matters. Critical ablation\n    flagged by all three Dream review tiers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_008\n  registry_id: greedy_cardinality_ablation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 11.2312\n    greedy_unconstrained_ppl: 32.4467\n    mckp_constrained_ppl: 11.23\n    delta_vs_mckp: 0.0012\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n- id: plan_017\n  claim:\n  - 1\n  - 2\n  description: 'Multi-seed error bars: run constrained MCKP and uniform 4-bit on Qwen2.5-7B\n    at 4x compression with 3 different calibration sets (different random subsets\n    of WikiText-2 training data). Report mean +/- std for PPL. Required for statistical\n    credibility — Dream review flagged all-single-run as critical gap.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: multi_seed_error_bars\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4454\n    mckp_seed0: 11.0168\n    mckp_seed1: 10.8981\n    mckp_seed2: 11.0487\n    mckp_mean: 10.9878\n    mckp_std: 0.0648\n    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4\n    allocation_agreement_3way: 0.902\n    agreement_s0_s1: 0.946\n    agreement_s0_s2: 0.911\n    agreement_s1_s2: 0.946\n    profile_time_min_per_seed: 65\n- id: plan_018\n  claim:\n  - 2\n  description: 'Runtime/latency benchmark: measure end-to-end inference latency and\n    throughput with mixed-precision KV cache vs uniform 4-bit quantization on Qwen2.5-7B.\n    Include profiling cost breakdown. Dream review flagged missing latency evaluation\n    as significant gap for systems-oriented contribution.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: runtime_benchmark\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16:\n      prefill_ms: 45.86\n      decode_ms_per_tok: 33.78\n      throughput_tok_s: 29.6\n    uniform_4bit:\n      prefill_ms: 54.25\n      decode_ms_per_tok: 42.46\n      throughput_tok_s: 23.6\n    constrained_mckp:\n      prefill_ms: 57.03\n      decode_ms_per_tok: 46.09\n      throughput_tok_s: 21.8\n      mckp_solver_sec: 0.005\n      bit_dist:\n        '2': 8\n        '4': 100\n        '8': 4\n      memory_ratio: 0.25\n    theoretical_memory:\n      bf16_MB: 21\n      4bit_MB: 5.25\n      mckp_MB: 5.25\n      compression_4x: true\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp_004\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p0_2_cliff_1.5B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: p0_2_cliff_7B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: p0_1_ppl_fast\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_a_targeted_hybrid\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_b_hires_quant\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_c_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_c_no2bit\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl: 15.4454\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_vs_uniform: 0\n    memory_ratio: 0.25\n    bit_distribution:\n      '4': 112\n- exp_id: exp_d_no_l0_exclusion\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_e_hires_profile\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    constrained_ppl_bf16: 9.569\n    baseline_ppl_bf16: 8.819\n    exp_c_ppl_bf16: 11.345\n    delta_vs_exp_c: -1.776\n    memory_ratio: 0.25\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    profile_resolution:\n      hires_nonzero_2bit: 100\n      lowres_nonzero_2bit: 37\n      hires_nonzero_4bit: 6\n      lowres_nonzero_4bit: 4\n      total_heads: 112\n    allocation_diff_count: 8\n    profiling_time_min: 65.5\n- exp_id: compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: compounding_sweep_k10_12\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: ratequant_greedy_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: budget_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: c4_cross_dataset_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    c4_mckp_ppl: 11.3285\n    uniform4bit_ppl: 15.4454\n    delta_over_uniform: 4.117\n    allocation_agreement_rate: 0.982\n    n_disagree: 2\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n    wt2_ref_mckp_ppl: 11.2312\n    wt2_ref_delta: 4.2142\n    ppl_gap: 0.097\n- exp_id: llama_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 8.7\n    uniform_4bit_ppl_bf16: 8.47\n    baseline_ppl_bf16: 8.09\n    delta_vs_uniform: -0.23\n    memory_ratio: 0.25\n- exp_id: mistral_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 7.564\n    uniform_4bit_ppl_bf16: 7.131\n    baseline_ppl_bf16: 7.035\n    delta_vs_uniform: -0.433\n    memory_ratio: 0.25\n- exp_id: llama_hires_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 8.0918\n    uniform_4bit_ppl: 8.469\n    lowres_mckp_ppl: 8.6951\n    hires_mckp_ppl: 8.4498\n    hires_improvement_ppl: 0.2453\n    degradation_reduction_pct: 40.7\n    profiling_time_min: 173.4\n    total_time_min: 175.1\n- exp_id: mistral_hires_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl: 7.323\n    uniform_4bit_ppl: 7.131\n    baseline_ppl: 7.035\n    delta_vs_uniform: -0.192\n    memory_ratio: 0.25\n- exp_id: llama_aggressive_compression\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_5.3x_ppl: 57.6\n    uniform_2bit_ppl: 2643.77\n    mckp_8x_ppl: 2372.33\n    uniform_2bit_8x_ppl: 2643.77\n- exp_id: downstream_eval_qwen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    avg_recovery: 0.728\n    arc_c: 0.5137\n    hellaswag: 0.7684\n    piqa: 0.7786\n    winogrande: 0.6819\n    arc_c_delta_pp: 3.16\n    hellaswag_delta_pp: 4\n    piqa_delta_pp: 1.25\n    winogrande_delta_pp: 1.97\n- exp_id: head_sensitivity_viz\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mistral_aggressive_compression\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_5.3x_ppl: 11.912\n    uniform_2bit_ppl: 519.107\n    mckp_8x_ppl: 399.901\n    uniform_2bit_8x_ppl: 519.107\n    baseline_ppl: 7.035\n    uniform_4bit_ppl: 7.131\n    5.3x_bit_dist:\n      '2': 128\n      '4': 128\n    8x_bit_dist:\n      '2': 248\n      '4': 8\n    total_time_seconds: 268.1\n- exp_id: kv_separation\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    kv_sep_ppl: 11.2162\n    joint_kv_ppl: 10.9131\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_sep_vs_joint: 0.303\n    sep_k_2bit_count: 16\n    sep_v_uniform_4bit: true\n    kv_asymmetric_heads: 21\n- exp_id: l0_only_heuristic\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: greedy_cardinality_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 11.2312\n    greedy_unconstrained_ppl: 32.4467\n    mckp_constrained_ppl: 11.23\n    delta_vs_mckp: 0.0012\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n- exp_id: l0_heuristic_baseline\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: greedy_constrained_ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: l0_heuristic_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_constrained_ppl: 11.23\n    l0_random_mean_ppl: 11.69\n    l0_random_std: 0.47\n    naive_positional_ppl: 12.23\n    uniform_4bit_ppl: 15.45\n    qwen_l0_random_median: 11.515\n    qwen_l0_random_seeds:\n    - 11.486\n    - 11.615\n    - 11.325\n    - 11.515\n    - 12.515\n    llama_l0_random_mean: 10.479\n    llama_l0_random_std: 1.033\n    llama_l0_random_median: 10.038\n    llama_l0_random_seeds:\n    - 9.485\n    - 10.488\n    - 9.941\n    - 10.038\n    - 12.444\n    llama_naive_positional: 9.941\n    llama_mckp: 8.4498\n    llama_uniform: 8.469\n    mistral_l0_random_mean: 7.56\n    mistral_l0_random_std: 0.087\n    mistral_l0_random_median: 7.586\n    mistral_l0_random_seeds:\n    - 7.523\n    - 7.61\n    - 7.413\n    - 7.586\n    - 7.669\n    mistral_naive_positional: 7.481\n    mistral_mckp: 7.3106\n    mistral_uniform: 7.131\n- exp_id: qwen_bf16_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 9.8106\n    baseline_fp16_ppl: 9.81\n    delta_baseline: 0.0006\n    uniform4_bf16_ppl: 15.4454\n    uniform4_fp16_ppl: 15.45\n    delta_uniform4: 0.0046\n- exp_id: hires_mckp_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl_bf16: 9.8106\n    mckp_ppl_bf16: 10.9131\n    uniform_4bit_ppl_bf16: 15.4454\n    delta_mckp_vs_baseline: 1.1025\n    delta_mckp_vs_uniform: -4.5323\n    token_count: 298938\n- exp_id: hires_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 9.8106\n    uniform_4bit_bf16_ppl: 15.4454\n    hires_mckp_bf16_ppl: 10.9131\n- exp_id: mistral_k_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 4\n    best_ppl: 7.1648\n    uniform_4bit_ppl: 7.131\n    k4_ppl: 7.1648\n    k8_ppl: 7.1997\n    k12_ppl: 7.2448\n    k16_ppl: 7.3106\n    k18_ppl: 7.3231\n- exp_id: llama_k_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 4\n    best_ppl: 8.4498\n    uniform_4bit_ppl: 8.469\n    k4_ppl: 8.4498\n    k8_ppl: 8.4498\n    k12_ppl: 8.4498\n    k16_ppl: 8.4498\n    k18_ppl: 8.4498\n    natural_2bit_count: 2\n- exp_id: multi_seed_error_bars\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4454\n    mckp_seed0: 11.0168\n    mckp_seed1: 10.8981\n    mckp_seed2: 11.0487\n    mckp_mean: 10.9878\n    mckp_std: 0.0648\n    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4\n    allocation_agreement_3way: 0.902\n    agreement_s0_s1: 0.946\n    agreement_s0_s2: 0.911\n    agreement_s1_s2: 0.946\n    profile_time_min_per_seed: 65\n- exp_id: cross_domain_calibration\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c4_cross_dataset_eval_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cross_domain_calibration_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: runtime_benchmark\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16:\n      prefill_ms: 45.86\n      decode_ms_per_tok: 33.78\n      throughput_tok_s: 29.6\n    uniform_4bit:\n      prefill_ms: 54.25\n      decode_ms_per_tok: 42.46\n      throughput_tok_s: 23.6\n    constrained_mckp:\n      prefill_ms: 57.03\n      decode_ms_per_tok: 46.09\n      throughput_tok_s: 21.8\n      mckp_solver_sec: 0.005\n      bit_dist:\n        '2': 8\n        '4': 100\n        '8': 4\n      memory_ratio: 0.25\n    theoretical_memory:\n      bf16_MB: 21\n      4bit_MB: 5.25\n      mckp_MB: 5.25\n      compression_4x: true\n- exp_id: c4_rerun_d032\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_cal_wt2_eval_mckp_ppl: 11.2942\n    c4_cal_wt2_eval_uniform_ppl: 15.4454\n    c4_cal_wt2_eval_delta: 4.1512\n    c4_cal_bf16_baseline: 12.6505\n    wt2_bf16_baseline: 9.8106\n    allocation_agreement_c4_vs_wt2: 0.964\n    agreement_heads: 108/112\n    bit_dist: 2bit:8, 4bit:100, 8bit:4\n    cross_domain_wt2_to_c4_mckp_ppl: 20.5601\n    cross_domain_wt2_to_c4_uniform_ppl: 35.4232\n    cross_domain_c4_bf16: 15.3246\n    old_contaminated_ppl: 11.3285\n    contamination_impact: 0.0343\n    models_completed: Qwen2.5-7B only\n- exp_id: multi_seed_lowres\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: oracle_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_ppl: 10.9131\n    max_oracle_gap_ppl: 0.0183\n    avg_oracle_gap_ppl: 0.0046\n    layers_mckp_optimal: 5/8\n    layers_with_gap: 3\n    gap_layers:\n      L1: 0.0183\n      L4: 0.0045\n      L11: 0.0136\n    gap_nature: 2-bit head position swap within same bit budget\n    total_evals: 54\n    runtime_min: 21.3\n- exp_id: plan_009_oracle_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: qwen72b_profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: llama_heuristic_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    l0_random_seeds:\n    - 8.5479\n    - 8.7595\n    - 8.624\n    - 8.5721\n    - 8.6192\n    l0_random_mean: 8.6245\n    l0_random_std: 0.0733\n    l0_random_median: 8.6192\n    naive_positional_ppl: 8.5781\n    mckp_ppl: 8.4498\n    uniform_ppl: 8.469\n    baseline_ppl: 8.0918\n    mckp_vs_l0_random_gap: 0.1747\n    mckp_vs_naive_gap: 0.1283\n- exp_id: mistral_heuristic_k4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 7.0351\n    uniform_4bit_ppl: 7.1314\n    mckp_k4_ppl: 7.1648\n    l0_random_seed_0: 7.1882\n    l0_random_seed_1: 7.1995\n    l0_random_seed_2: 7.1723\n    l0_random_seed_3: 7.3577\n    l0_random_seed_4: 7.2875\n    l0_random_mean: 7.2411\n    l0_random_std: 0.0707\n    l0_random_median: 7.1995\n    naive_heuristic_ppl: 7.2105\n    budget_heuristic: 0.2559\n    budget_mckp_k4: 0.248\n- exp_id: llama_c4_cross_dataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wt2_cal_wt2_ppl: 8.4498\n    c4_cal_wt2_ppl: 8.6459\n    uniform_wt2_ppl: 8.469\n    wt2_cal_c4_ppl: 7.654\n    c4_cal_c4_ppl: 7.654\n    uniform_c4_ppl: 7.5351\n    bf16_wt2_ppl: 8.0918\n    bf16_c4_ppl: 7.1333\n    agreement_rate: 0.977\n    agreement_heads: 250/256\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n- exp_id: mistral_c4_cross_dataset\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bf16_wt2_ppl: 7.0351\n    c4_cal_bf16_ppl: 6.9677\n    wt2_cal_mckp_wt2_ppl: 7.1648\n    c4_cal_mckp_wt2_ppl: 7.1859\n    uniform_4bit_wt2_ppl: 7.1314\n    delta_uniform_mckp_wt2_cal: -0.0334\n    delta_uniform_mckp_c4_cal: -0.0546\n    allocation_agreement_c4_vs_wt2: 0.965\n    agreement_heads: 247/256\n    bit_dist_wt2_cal: 2bit:4, 4bit:252\n    bit_dist_c4_cal: 2bit:4, 4bit:251, 8bit:1\n    profile_time_s: 407.7\n    eval_time_s: 349.4\n    total_time_s: 757.1\n- exp_id: gemma2_9b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 8.9\n    mckp_wikitext2_ppl: 9.05\n    uniform4bit_wikitext2_ppl: 9.03\n    mckp_improvement_over_uniform: -0.02\n    top5_concentration: 0.23\n    layer0_dominance_ratio: 1.32\n    best_k: 8\n    best_k_ppl: 9.05\n    verdict: FAIL\n- exp_id: yi15_9b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 7.0157\n    mckp_wikitext2_ppl: 7.3129\n    uniform4bit_wikitext2_ppl: 7.2171\n    mckp_improvement_over_uniform: -0.0958\n    top5_concentration: 0.4934\n    layer0_dominance_ratio: 0.07\n    best_k: 2\n    best_k_ppl: 7.2209\n    gqa_ratio: '8:1'\n    verdict: FAIL\n- exp_id: qwen25-hires-profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_hires_float32_d048\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    float32_hires_top5_concentration: 0.6104\n    bf16_hires_range: 0.59-0.66\n    float32_lowres_concentration: 0.42\n    bf16_bug_impact_on_concentration: 0.01\n    baseline_ppl: 9.81\n    mckp_unconstrained_ppl: 10.95\n    uniform_4bit_ppl: 15.45\n    mckp_bit_dist:\n      '2': 12\n      '4': 96\n      '8': 3\n      '16': 1\n    l0h0_delta: 6.7388\n    l0_4heads_total_share: 0.586\n    claim3_threshold_0.50: PASS\n- exp_id: yi15_hires_float32_profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: yi15_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.7139\n    top5_n_heads: 9\n    baseline_calibration_ppl: 5.888\n    delta_2bit_cv: 8.8991\n    layer0_dominance_ratio: 0.04\n    top1_head: L4H3_delta=13.1236\n    total_hours: 0.96\n- exp_id: qwen_hires_constrained_d049\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    float32_hires_constrained_mckp_ppl: 10.8921\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4484\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    gap_recovery_pct: 80.8\n    top5_concentration: 0.6156\n    top5_concentration_pre_monotonicity: 0.6104\n    bf16_hires_constrained_mckp_ppl: 10.9131\n    delta_f32_vs_bf16: 0.021\n- exp_id: yi15_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hires_mckp_ppl: 7.2181\n    uniform_4bit_ppl: 7.2171\n    baseline_ppl: 7.0157\n    delta_vs_uniform: -0.001\n    bit_distribution:\n      '2': 2\n      '4': 189\n      '8': 1\n    2bit_heads:\n    - L22H1\n    - L24H3\n    8bit_heads:\n    - L6H2\n    L4H3_status: kept_at_4bit\n    std_mckp_k2_ppl: 7.2209\n    std_mckp_k8_ppl: 7.3129\n    hires_concentration: 0.7139\n    L4H3_2bit_delta: 13.12\n    L4H3_4bit_delta: 0.0048\n    L4H3_8bit_delta: 0.004\n- exp_id: llama_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.5749\n    t1_t5: 0.85\n    baseline_ppl: 6.5055\n    top1_head: L2H5_delta=15.2636\n    delta_2bit_cv: 7.7663\n    l0_dominance_ratio: 0.67\n    positive_delta_heads: 254\n    total_heads: 256\n    total_hours: 0.98\n- exp_id: mistral_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: 'ValueError: Unrecognized model - config.json missing model_type field\n      at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3'\n- exp_id: mistral_hires_bf16_2bitonly_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: 'SafetensorError: model-00003-of-00003.safetensors missing, incomplete\n      download'\n- exp_id: mistral_hires_bf16_2bitonly_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mistral_hires_bf16_2bitonly_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.241\n    top5_n_heads: 12\n    baseline_ppl: 5.8702\n    top1_head: L2H5\n    top1_delta_2bit: 0.3236\n    top2_head: L12H1\n    top2_delta_2bit: 0.1435\n    top3_head: L0H7\n    top3_delta_2bit: 0.1403\n    delta_2bit_mean: 0.020073\n    delta_2bit_std: 0.026278\n    delta_2bit_cv: 1.3091\n    layer0_mean_delta_2bit: 0.034073\n    other_layers_mean_delta_2bit: 0.019621\n    l0_dominance_ratio: 1.74\n    positive_delta_heads: 252\n    total_heads: 256\n    distribution_shape: flat\n    total_hours: 0.94\n    profile_seconds: 3371.7\n- exp_id: llama_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_bf16_ppl: 8.0922\n    hires_mckp_ppl: 8.5042\n    uniform_4bit_ppl: 8.4701\n    std_mckp_reference_ppl: 8.4498\n    mckp_vs_uniform_delta: -0.0341\n    mckp_vs_uniform_pct: -9\n    hires_vs_std_mckp_delta: 0.0544\n    concentration: 0.5749\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n    heads_2bit:\n    - 26,0\n    - 31,7\n    heads_8bit:\n    - 12,3\n    verdict: FAIL\n- exp_id: gemma2_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    concentration_top5pct: 0.2291\n    l0_dominance_ratio: 2.05\n    cv_delta_2bit: 1.2834\n    positive_delta_heads: 310/336\n    top_head: L0H1 delta=0.1906\n    total_time_hours: 1.59\n- exp_id: llama_c4_hires_crossdataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_wt2_ppl: 8.0922\n    bf16_c4_ppl: 7.1333\n    c4_cal_mckp_wt2_ppl: 8.5103\n    c4_cal_mckp_c4_ppl: 7.5351\n    uniform_wt2_ppl: 8.4701\n    uniform_c4_ppl: 7.5351\n    delta_c4_uniform_minus_mckp: 0\n    delta_wt2_uniform_minus_mckp: -0.0402\n    verdict_c4: FAIL\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n    heads_2bit:\n    - 2,3\n    - 24,2\n    heads_8bit:\n    - 31,6\n    total_time_min: 6.3\n    wt2_ref_mckp_ppl: 8.5042\n    wt2_ref_delta: -0.0341\n- exp_id: mistral_c4_hires_crossdataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fp16_ppl: 7.0352\n    c4_mckp_ppl: 7.1774\n    uniform_4bit_ppl: 7.1308\n    mckp_vs_uniform_delta: 0.0466\n    mckp_bit_distribution:\n      '2': 4\n      '4': 250\n      '8': 2\n    phase4_error: 'FileNotFoundError: mistral_k_ablation_results.json'\n- exp_id: w2_unconstrained_baselines\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    note: 2bitonly profiles only - INVALID for reviewer response\n    yi15_ppl: 672.2\n    yi15_ratio: 114\n    llama_ppl: 1219.7\n    llama_ratio: 187\n    mistral_ppl_2bitonly: 47.8\n    mistral_ratio_2bitonly: 8.2\n    mistral_ppl_full: 6.39\n    mistral_ratio_full: 1.09\n    gemma2_ppl: 277.4\n    gemma2_ratio: 37.9\n    budget: 0.25\n    baseline_yi: 5.89\n    baseline_llama: 6.51\n    baseline_mistral: 5.87\n    baseline_gemma2: 7.32\n- exp_id: w9_compounding_scaling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    baseline_ppl: 8.2\n    n1_joint_ppl: 14.94\n    n1_ratio: 1\n    n2_joint_ppl: 42.26\n    n2_ratio: 3.84\n    n4_joint_ppl: 3813.76\n    n4_ratio: 333.3\n    n8_joint_ppl: 3586.42\n    n8_ratio: 282.1\n    n16_joint_ppl: 7286.23\n    n16_ratio: 521.1\n    n32_joint_ppl: 6644.05\n    n32_ratio: 424\n    n64_joint_ppl: 9453.33\n    n64_ratio: 533.3\n    runtime_seconds: 96\n- exp_id: w9_compounding_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.81\n    k1_topk_ppl: 9.826\n    k1_randomk_ppl: 9.887\n    k1_randomk_std: 0.05\n    k4_topk_ppl: 9.849\n    k4_topk_ratio: 0.86\n    k4_randomk_ppl: 10.06\n    k4_randomk_std: 0.06\n    k4_randomk_ratio: 1.24\n    k8_topk_ppl: 10.042\n    k8_topk_ratio: 1.56\n    k8_randomk_ppl: 11.07\n    k8_randomk_std: 0.69\n    k8_randomk_ratio: 1.76\n    k16_topk_ppl: 10.42\n    k16_topk_ratio: 1.56\n    k16_randomk_ppl: 12.91\n    k16_randomk_std: 0.4\n    k16_randomk_ratio: 2.1\n    k32_topk_ppl: 11.604\n    k32_topk_ratio: 1.78\n    k32_randomk_ppl: 18.33\n    k32_randomk_std: 2.53\n    k32_randomk_ratio: 2.73\n    k64_topk_ppl: 22.946\n    k64_topk_ratio: 4.89\n    k64_randomk_ppl: 55.94\n    k64_randomk_std: 9.73\n    k64_randomk_ratio: 8.88\n    runtime_minutes: 16.9\n    note: 'v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking,\n      top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。'\n- exp_id: w2_unconstrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi15_baseline: 7.0157\n    yi15_uniform4: 7.2171\n    yi15_greedy: 7.5615\n    yi15_mckp: 7.5615\n    yi15_n2bit: 22\n    llama_baseline: 8.0922\n    llama_uniform4: 8.4701\n    llama_greedy: 8.6265\n    llama_mckp: 8.6265\n    llama_n2bit: 12\n    mistral_baseline: 7.0352\n    mistral_uniform4: 7.1308\n    mistral_greedy: 7.5733\n    mistral_mckp: 7.5963\n    mistral_n2bit: 42\n    gemma2_baseline: 6.0306\n    gemma2_uniform4: 6.1683\n    gemma2_greedy: 8.8469\n    gemma2_mckp: 8.8469\n    gemma2_n2bit: 106\n    gemma2_eval_method: sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\n    gemma2_greedy_ratio: 1.467\n    gemma2_catastrophic: true\n    gemma2_note: 1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal\n      value\n- exp_id: w3_downstream_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi15_baseline_avg: 0.6912\n    yi15_uniform_avg: 0.6822\n    yi15_mckp_avg: 0.6745\n    yi15_mckp_vs_uniform_pp: -0.77\n    yi15_mckp_vs_baseline_pp: -1.67\n    yi15_baseline:\n      arc_easy: 0.8093\n      arc_challenge: 0.5265\n      hellaswag: 0.5913\n      piqa: 0.7949\n      winogrande: 0.734\n    yi15_uniform:\n      arc_easy: 0.7946\n      arc_challenge: 0.5205\n      hellaswag: 0.5857\n      piqa: 0.7927\n      winogrande: 0.7174\n    yi15_mckp:\n      arc_easy: 0.7854\n      arc_challenge: 0.4881\n      hellaswag: 0.5797\n      piqa: 0.7894\n      winogrande: 0.7301\n    llama_baseline_avg: 0.696\n    llama_uniform_avg: 0.6915\n    llama_mckp_avg: 0.6816\n    llama_mckp_vs_uniform_pp: -0.99\n    llama_mckp_vs_baseline_pp: -1.44\n    llama_baseline:\n      arc_easy: 0.8228\n      arc_challenge: 0.5188\n      hellaswag: 0.6073\n      piqa: 0.7922\n      winogrande: 0.7388\n    llama_uniform:\n      arc_easy: 0.8173\n      arc_challenge: 0.5256\n      hellaswag: 0.6026\n      piqa: 0.7867\n      winogrande: 0.7253\n    llama_mckp:\n      arc_easy: 0.8039\n      arc_challenge: 0.4991\n      hellaswag: 0.6012\n      piqa: 0.7802\n      winogrande: 0.7238\n    mistral_baseline_avg: 0.6917\n    mistral_uniform_avg: 0.6894\n    mistral_mckp_avg: 0.6846\n    mistral_mckp_vs_uniform_pp: -0.48\n    mistral_mckp_vs_baseline_pp: -0.71\n    mistral_baseline:\n      arc_easy: 0.8005\n      arc_challenge: 0.5043\n      hellaswag: 0.6118\n      piqa: 0.8009\n      winogrande: 0.7411\n    mistral_uniform:\n      arc_easy: 0.7976\n      arc_challenge: 0.5068\n      hellaswag: 0.6051\n      piqa: 0.7982\n      winogrande: 0.7395\n    mistral_mckp:\n      arc_easy: 0.7942\n      arc_challenge: 0.4949\n      hellaswag: 0.6027\n      piqa: 0.802\n      winogrande: 0.7293\n    gemma2_baseline_avg: 0.7307\n    gemma2_uniform_avg: 0.7251\n    gemma2_mckp_avg: 0.7265\n    gemma2_mckp_vs_uniform_pp: 0.14\n    gemma2_mckp_vs_baseline_pp: -0.42\n    gemma2_baseline:\n      arc_easy: 0.8737\n      arc_challenge: 0.6135\n      hellaswag: 0.6093\n      piqa: 0.8128\n      winogrande: 0.7443\n    gemma2_uniform:\n      arc_easy: 0.8662\n      arc_challenge: 0.6058\n      hellaswag: 0.606\n      piqa: 0.8079\n      winogrande: 0.7395\n    gemma2_mckp:\n      arc_easy: 0.8649\n      arc_challenge: 0.6041\n      hellaswag: 0.6089\n      piqa: 0.8074\n      winogrande: 0.7474\n    eval_harness_version: 0.4.11\n    num_fewshot: 0\n    yi_elapsed_s: 1563.2\n    llama_elapsed_s: 1446.4\n    mistral_elapsed_s: 1302.2\n    gemma2_elapsed_s: 1735.9\n- exp_id: gemma2_constrained_bos_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 6.0306\n    uniform_4bit_ppl: 6.1683\n    constrained_mckp_ppl: 6.1951\n    mckp_vs_uniform_delta: 0.0267\n    mckp_delta_ppl: 0.1645\n    uniform_delta_ppl: 0.1377\n    bit_distribution:\n      '2': 8\n      '4': 324\n      '8': 4\n    n_2bit: 8\n    max_2bit: 8\n    memory_ratio: 0.25\n    eval_method: sliding_window_bos_fix\n    elapsed_seconds: 490.3\n- exp_id: w1_qwen14b_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 5.8432\n    concentration: 0.3312\n    t1_t5: 0.68\n    shape: Flat\n    l0_dominance: 15.5\n    cv: 3.7418\n    positive_heads: 370\n    total_heads: 384\n    top10_heads:\n    - head: L0H5\n      delta: 1.84494\n    - head: L0H4\n      delta: 0.236669\n    - head: L0H2\n      delta: 0.136971\n    - head: L28H4\n      delta: 0.099279\n    - head: L28H5\n      delta: 0.07576\n    - head: L27H4\n      delta: 0.071269\n    - head: L0H0\n      delta: 0.070018\n    - head: L28H6\n      delta: 0.063737\n    - head: L26H0\n      delta: 0.061462\n    - head: L31H3\n      delta: 0.061062\n    elapsed_min: 161.3\n    note: 't1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio'\n- exp_id: w1_pythia14b_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 13.6347\n    concentration: 0.2439\n    t1_t5: 0.28\n    shape: Flat\n    l0_dominance: 0.51\n    cv: 1.2172\n    positive_heads: 362\n    total_heads: 384\n    top5_heads:\n    - head: L1H11\n      delta: 1.016355\n    - head: L12H14\n      delta: 0.784513\n    - head: L8H4\n      delta: 0.759118\n    - head: L11H2\n      delta: 0.632357\n    - head: L13H2\n      delta: 0.522849\n    elapsed_min: 25.7\n    note: 't1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio'\n- exp_id: kivi_baseline_qwen_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_2bit_r128: 12.83\n    qwen_4bit_r128: 9.9\n    qwen_2bit_r0: 13.34\n    qwen_4bit_r0: 9.91\n    llama_2bit_r128: 9.84\n    llama_4bit_r128: 8.14\n    llama_2bit_r0: 10.08\n    llama_4bit_r0: 8.14\n    group_size: 32\n    eval_data: WikiText-2 test\n    note: r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\n- exp_id: qwen14b_constrained_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16: 6.8654\n    ppl_uniform_4bit: 7.202\n    ppl_constrained_mckp: 7.2206\n    ppl_unconstrained_mckp: 7.6923\n    delta_constrained_vs_uniform: -0.0185\n    delta_constrained_vs_uniform_pct: -5.51\n    delta_unconstrained_vs_uniform: -0.4902\n    bit_distribution_constrained:\n      '2': 8\n      '4': 374\n      '8': 1\n      '16': 1\n    bit_distribution_unconstrained:\n      '2': 77\n      '4': 271\n      '8': 35\n      '16': 1\n    concentration: 0.33\n    top1_pct: 0.2262\n    top5_pct: 0.3304\n    t1_t5: 0.68\n    shape: Flat\n- exp_id: pythia14b_constrained_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16: 16.4893\n    ppl_uniform_4bit: 24.2894\n    ppl_constrained_mckp: 24.4521\n    ppl_unconstrained_mckp: 31.5415\n    concentration: t1=0.0289, t5=0.2439\n    t1_t5: 0.0289/0.2439\n    shape: Flat\n    constrained_vs_uniform_gap: 0.1627\n- exp_id: qwen7b_8k_context_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16_8k: 6.97\n    ppl_constrained_mckp_8k: 8.59\n    ppl_uniform_4bit_8k: 77.75\n    ppl_bf16_2k: 9.81\n    ppl_constrained_mckp_2k: 10.89\n    ppl_uniform_4bit_2k: 15.45\n    mckp_improvement_over_uniform_8k: 97.7%\n    mckp_improvement_over_uniform_2k: 80.8%\n    shape: Spread\n    concentration: 0.5992\n    context_length: 8192\n    note: 'Concentration-dependent benefit amplifies at longer context: uniform 4-bit\n      catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust\n      (+23%)'\n- exp_id: qwen7b_8k_spotcheck\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: yi15_8k_spotcheck\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: llama_8k_spotcheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16_8k: 5.5958\n    ppl_constrained_mckp_8k: 6.0537\n    ppl_uniform_4bit_8k: 6.0364\n    mckp_improvement_over_uniform_8k: -0.0174\n    mckp_improvement_pct_8k: -3.94\n    ppl_bf16_2k: 8.0922\n    ppl_constrained_mckp_2k: 8.5042\n    ppl_uniform_4bit_2k: 8.4701\n    shape: Spike\n    concentration: 0.5749\n    t1_over_t5: 0.71\n    context_length: 8192\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n- exp_id: kivi_baseline_qwen7b_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_kivi_4bit_g32_r128: 9.8976\n    tokens: 298938\n    chunks: 583\n    stride: 512\n    model: Qwen2.5-7B\n    comparison_mckp_ppl: 10.91\n    comparison_uniform_ppl: 15.45\n    comparison_bf16_ppl: 9.81\n- exp_id: mistral_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kivi_mckp_combined_qwen7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: qwen14b_greedy_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 7.2206\n    mckp_constrained_ppl: 7.2206\n    delta_vs_mckp: 0\n    bit_distribution:\n      '2': 8\n      '4': 374\n      '8': 1\n      '16': 1\n    memory_ratio: 0.25\n    solver_time_sec: 0.08\n    total_time_min: 1.8\n- exp_id: mistral_uniform_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mistral_hires_constrained_mckp_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 7.0352\n    mckp_wikitext2_ppl: 7.1341\n    uniform4bit_wikitext2_ppl: 7.1308\n    mckp_improvement_over_uniform: -0.0033\n    mckp_improvement_pct: -3.48\n    verdict: FAIL\n    bit_distribution:\n      '2': 2\n      '4': 254\n    fix_note: 'uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130'\n- exp_id: phi3_medium_hires_profiling_check\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: codellama_7b_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: llama_compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 0\n    best_ppl: 8.0922\n    k0_ppl: 8.0922\n    k2_ppl: 8.1243\n    k4_ppl: 8.1803\n    k8_ppl: 8.2259\n    k16_ppl: 8.4378\n    k32_ppl: 9.0506\n    k64_ppl: 11.991\n    k128_ppl: 40.2067\n    k256_ppl: 1519.1888\n    budget: 0.25\n- exp_id: mistral_compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k0_ppl: 7.1308\n    k2_ppl: 7.1471\n    k4_ppl: 7.164\n    k8_ppl: 7.2001\n    k16_ppl: 7.31\n    k32_ppl: 7.4877\n    k64_ppl: 7.5932\n    k128_ppl: 7.5932\n    k256_ppl: 7.5932\n    best_k: 0\n    best_ppl: 7.1308\n    note: PPL monotonically increases with k; all-4bit optimal at budget=0.25; solver\n      saturates at k>=64 (41 actual 2-bit heads)\n- exp_id: phi3_medium_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: llama_downstream_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge:\n      fp16: 0.5188\n      uniform_4bit: 0.5256\n      mckp_k2: 0.5179\n    hellaswag:\n      fp16: 0.6073\n      uniform_4bit: 0.6024\n      mckp_k2: 0.6021\n    piqa:\n      fp16: 0.7922\n      uniform_4bit: 0.7873\n      mckp_k2: 0.7867\n    winogrande:\n      fp16: 0.7388\n      uniform_4bit: 0.7261\n      mckp_k2: 0.7309\n    avg_delta_vs_uniform: -0.1\n    bit_distribution:\n      4bit: 253\n      8bit: 1\n      2bit: 2\n    budget: 0.25\n    total_distortion: 0.7015\n    elapsed_sec: 3387\n- exp_id: yi_mistral_downstream_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi_k2:\n      arc_challenge:\n        baseline: 0.5265\n        uniform: 0.5205\n        mckp_k2: 0.4991\n      hellaswag:\n        baseline: 0.5912\n        uniform: 0.5855\n        mckp_k2: 0.5818\n      piqa:\n        baseline: 0.7949\n        uniform: 0.7916\n        mckp_k2: 0.7916\n      winogrande:\n        baseline: 0.7332\n        uniform: 0.7206\n        mckp_k2: 0.7238\n      avg_delta_vs_uniform: -0.0055\n      bit_distribution:\n        4bit: 189\n        8bit: 1\n        2bit: 2\n    mistral_k2:\n      arc_challenge:\n        baseline: 0.5043\n        uniform: 0.5068\n        mckp_k2: 0.5068\n      hellaswag:\n        baseline: 0.6118\n        uniform: 0.6051\n        mckp_k2: 0.605\n      piqa:\n        baseline: 0.8009\n        uniform: 0.7987\n        mckp_k2: 0.7982\n      winogrande:\n        baseline: 0.7411\n        uniform: 0.7395\n        mckp_k2: 0.7388\n      avg_delta_vs_uniform: -0.0003\n      bit_distribution:\n        4bit: 254\n        2bit: 2\n    elapsed_sec: 2672\n- exp_id: mistral_compounding_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k0_ppl: 7.0352\n    k2_ppl: 7.0366\n    k4_ppl: 7.0453\n    k8_ppl: 7.0636\n    k16_ppl: 7.1139\n    k32_ppl: 7.2378\n    k64_ppl: 7.7747\n    k128_ppl: 10.473\n    k256_ppl: 45.2766\n    budget: 0.25\n    n_heads: 256\n- exp_id: qwen_compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_compounding_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_k0: 9.8106\n    ppl_k8: 10.0474\n    ppl_k64: 23.2176\n    ppl_k256: 98.7523\n    max_compounding_ratio: 10.07\n    n_heads_total: 112\n    n_2bit_ceiling: 96\n    budget: 0.25\n- exp_id: codellama_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 7.6978\n    top5_concentration: 0.7975\n    t1_t5: 0.8131\n    distribution_shape: Spike\n    cv: 18.3153\n    l0_dominance_ratio: 0.8\n    top5_sensitive_heads:\n    - layer: 1\n      head: 1\n      delta_2bit: 22.998339\n    - layer: 1\n      head: 18\n      delta_2bit: 2.042989\n    - layer: 1\n      head: 11\n      delta_2bit: 1.460641\n    - layer: 0\n      head: 15\n      delta_2bit: 0.942934\n    - layer: 30\n      head: 31\n      delta_2bit: 0.839968\n    total_kv_heads: 1024\n    gqa_ratio: 1\n    profile_time_hours: 3.7\n- exp_id: gemma2_downstream_k2_4task\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gemma2_downstream_k8_4task\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: qwen_3seed_downstream_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge:\n      bf16: 0.4582\n      uniform: 0.459\n      mckp_mean: 0.459\n      mckp_std: 0.0035\n      delta: 0\n    hellaswag:\n      bf16: 0.5887\n      uniform: 0.5335\n      mckp_mean: 0.5748\n      mckp_std: 0.0022\n      delta: 0.0413\n    winogrande:\n      bf16: 0.7119\n      uniform: 0.6622\n      mckp_mean: 0.678\n      mckp_std: 0.0115\n      delta: 0.0158\n    piqa:\n      bf16: 0.7818\n      uniform: 0.7552\n      mckp_mean: 0.7748\n      mckp_std: 0.0023\n      delta: 0.0196\n    avg_delta: 0.0192\n    elapsed_sec: 2714\n- exp_id: gemma2_downstream_k8_4task_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge:\n      baseline: 0.6135\n      uniform: 0.6058\n      mckp_k8: 0.6049\n      delta: -0.0009\n    hellaswag:\n      baseline: 0.6093\n      uniform: 0.6092\n      mckp_k8: 0.6089\n      delta: -0.0003\n    winogrande:\n      baseline: 0.7443\n      uniform: 0.738\n      mckp_k8: 0.7443\n      delta: 0.0063\n    piqa:\n      baseline: 0.8128\n      uniform: 0.8036\n      mckp_k8: 0.8079\n      delta: 0.0043\n    avg_delta: 0.0024\n    bit_distribution:\n      4bit: 324\n      2bit: 8\n      8bit: 4\n    elapsed_sec: 2321\n- exp_id: llama_3seed_downstream_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_delta: -0.8\n    hellaswag_delta: 0\n    piqa_delta: -0.1\n    winogrande_delta: 0.5\n    avg_delta: -0.1\n    std_all_tasks: 0\n    note: Single profile → deterministic allocation → all 3 seeds identical\n- exp_id: falcon7b_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: deepseekvl_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: internlm2_7b_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: phi3_medium_hires_profiling_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.1742\n    top5_n_heads: 20\n    baseline_calibration_ppl: 4.783\n    delta_2bit_cv: 0.8905\n    layer0_dominance_ratio: 0.04\n    shape: Spread\n    t1_t5_ratio: 0.24\n    top1_head: L9H6\n    top1_delta_2bit: 0.1806\n    total_heads: 400\n    profiling_hours: 2.48\n    note: Low concentration but t1/t5=0.24 indicates sensitivity spread across multiple\n      heads — confirmed Spread pattern. Mid-layer concentration (L8-L11).\n- exp_id: falcon7b_hires_profiling_v2\n  name: ''\n  status: PENDING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T02:22:49.028Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T02:22:49.028Z",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-16T02:22:49.050Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Compounding 发现和 constraint 有效性被认可，但 'universal' 语言和 diagnostic 的 claim 强度受到质疑；需要降低 claim 语气并补充实验
核心假设：['A1: compounding 被认可为有价值的实证发现，但 reviewer 指出 RateQuant Appendix M 已 acknowledge 该现象（novelty 打折）', "A2: 8 个架构不足以支撑 'universal'——reviewer 要求去掉该词或补充至 12+ 模型", "A3: constraint 被部分 reviewer 视为 'obvious in hindsight' / 'just a hyperparameter'，需要更强的 principled justification", "A4: 1/8 benefit 被 1-2 个 reviewer 视为方法有效性不足的证据（'method only works on Qwen'）", 'A5: diagnostic n=9 被拒绝作为独立 claim——只能作为 observation 或 hypothesis', 'A6: 缺少 eviction baseline 和 multi-seed downstream CI 被标为 significant gap']
关键指标范围：{'avg_review_score_arr': [2.8, 3.5], 'claims_surviving_intact': [1, 2], 'p_accept_emnlp_main': [0.15, 0.35], 'major_reviewer_objections': [2, 3], 'narrative_rewrite_pct': [25, 45], 'unconstrained_degradation_universality': [6, 8], 'solver_equivalence_delta': [0.0, 0.001], 'diagnostic_accuracy': [7, 9], 'downstream_consistency_with_ppl': [4, 5]}
叙事方向：需要调整 claim 强度。(1) "universal failure mode" → "consistent failure pattern across 8 diverse architectures"， 去掉 universal 一词，改为 "widespread" 或 "systematic"。(2) constraint contribution 从 "核心方法贡献"  重新定位为 "principled analysis insight that yields a practical fix"——强调分析贡献而非方法贡献。 (3) diagnostic 从独立 claim 降级为 Section 5 的 empirical observation + "testable hypothesis for future work"。 补充实验：(a) 2-3 个额外架构的 profiling（不需要 full pipeline），(b) downstream multi-seed CI 至少在 Qwen 上， (c) 在 related work 中更显式地讨论 RateQuant Appendix M 的 compounding acknowledgment 并 clarify 区别。 论文 reframe 为 "empirical analysis paper with practical implications" 而非 "method paper"。 EMNLP Efficient Methods track 仍然适合，但需要在 intro 中前置 analysis contribution。


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
  "promptId": "c576fd4f-16bc-47dd-ab5f-a8755eac9d29",
  "type": "user",
  "uuid": "577fd2f0-a74a-449b-bb15-8b50270319a3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T02:22:49.048Z_

```json
{
  "parentUuid": "577fd2f0-a74a-449b-bb15-8b50270319a3",
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
  "uuid": "b172f368-e167-4c90-8db2-903a09fb5736",
  "timestamp": "2026-05-16T02:22:49.048Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T02:22:49.048Z_

```json
{
  "parentUuid": "b172f368-e167-4c90-8db2-903a09fb5736",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "92f6a028-35f2-4e3d-ae06-b18741d04161",
  "timestamp": "2026-05-16T02:22:49.048Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Compounding 发现和 constraint 有效性被认可，但 'universal' 语言和 diagnostic 的 claim 强度受到质疑；需要降低 claim 语气并补充实验 核心假设：['A1: compounding 被认可为有价值的实证发现，但 reviewer 指出 RateQu…",
  "leafUuid": "92f6a028-35f2-4e3d-ae06-b18741d04161",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze KV cache compounding effects and diagnostic thresholds",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9"
}
```

---

### Assistant

_source line 8 · 2026-05-16T02:23:17.422Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each experiment in the `experiment_plan` under the **median** tier scenario. I need to go through every planned experiment and produce expected results with rationales explaining why this median tier would produce those specific outcomes.

Let me carefully go through each experiment plan and generate predictions consistent with the median tier definition:

**Median tier meaning:**
- Compounding discovery and constraint effectiveness are acknowledged, but "universal" language and diagnostic claim strength are questioned
- Need to lower claim tone and supplement with experiments
- Core assumptions A1-A6 define the reviewer pushback

**Key metric ranges for median:**


Now I'm looking at the expected metric ranges that define the median tier outcome—review scores hovering around 3.0-3.5, only 1-2 claims surviving peer review intact, acceptance probability at EMNLP main around 15-35%, with 2-3 major objections from reviewers. The narrative will need substantial revision (25-45% rewrite), unconstrained degradation will show moderate universality concerns (6-8 points), solver equivalence will be nearly identical (0.0-0.001 delta), diagnostic accuracy will be solid (7-9), and downstream consistency with perplexity will be weak (4-5).

For each experiment in the plan, I need to generate predicted results that align with this median-tier reception—essentially simulating what the reviewer feedback and outcome metrics would look like given the actual experimental results we already have. Continuing through the experiment list, I see the remaining plans covering hires profiling, C4 evaluation, RateQuant and oracle comparisons, cross-domain calibration, visualization work, downstream evaluation on Qwen, 72B profiling that was killed, K/V separation exploration, and L0-only heuristics.

Now I'm thinking through how to frame these results for reviewers—what findings they'd readily accept versus what might raise questions—and I need to construct predictions for the median tier with concrete numbers and explanations for why those specific values would emerge at that performance level.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92f6a028-35f2-4e3d-ae06-b18741d04161",
  "isSidechain": false,
  "requestId": "req_011Cb5T9SCKnTitkeHyKZB22",
  "type": "assistant",
  "uuid": "43f3a564-df89-4990-bafa-543b5c42a093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcNaM3b6SS3ACVsACWNNEE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 36354,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1151,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 36354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36354
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

_source line 9 · 2026-05-16T02:23:17.423Z_

I'll review the experiment plan and registry data to produce detailed median-tier predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43f3a564-df89-4990-bafa-543b5c42a093",
  "isSidechain": false,
  "requestId": "req_011Cb5T9SCKnTitkeHyKZB22",
  "type": "assistant",
  "uuid": "ddeb9084-3a5c-4249-8e87-af798e775515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcNaM3b6SS3ACVsACWNNEE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 36354,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1151,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 36354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36354
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

_source line 10 · 2026-05-16T02:23:17.486Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01V2FdqyRuTGTQtfDJzCTVd7`</summary>

```json
{
  "pattern": "**/*experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddeb9084-3a5c-4249-8e87-af798e775515",
  "isSidechain": false,
  "requestId": "req_011Cb5T9SCKnTitkeHyKZB22",
  "type": "assistant",
  "uuid": "c9b24979-7804-4e2e-a9ee-80d52395da53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcNaM3b6SS3ACVsACWNNEE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 36354,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1151,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 36354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36354
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

_source line 11 · 2026-05-16T02:23:17.545Z_

<details><summary>↩ Tool result · `toolu_01V2FdqyRuTGTQtfDJzCTVd7`</summary>

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
  "parentUuid": "c9b24979-7804-4e2e-a9ee-80d52395da53",
  "isSidechain": false,
  "promptId": "c576fd4f-16bc-47dd-ab5f-a8755eac9d29",
  "type": "user",
  "uuid": "bfe5cfd4-5df5-4e72-a318-92c8dec3f9b4",
  "toolUseResult": {
    "filenames": [
      "projects/demo_calibrated_sim/experiment_plan.lock",
      "projects/demo_calibrated_sim/experiment_plan.yaml",
      "projects/ratekv/experiment_plan.lock",
      "projects/ratekv/experiment_plan.yaml"
    ],
    "durationMs": 44,
    "numFiles": 4,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c9b24979-7804-4e2e-a9ee-80d52395da53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T02:23:21.357Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GiVSysBHfw1nY6inST7tmU`</summary>

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
  "parentUuid": "bfe5cfd4-5df5-4e72-a318-92c8dec3f9b4",
  "isSidechain": false,
  "requestId": "req_011Cb5TBXtgVkYppXCgC1Xvr",
  "type": "assistant",
  "uuid": "67d776a9-d484-4bec-bbe7-715ebaf4eede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZaG38nREgmmSwyBCmb1g8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1213,
      "cache_read_input_tokens": 48195,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 48195,
          "cache_creation_input_tokens": 1213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1213
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

_source line 13 · 2026-05-16T02:23:21.367Z_

<details><summary>↩ Tool result · `toolu_01GiVSysBHfw1nY6inST7tmU`</summary>

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
  "parentUuid": "67d776a9-d484-4bec-bbe7-715ebaf4eede",
  "isSidechain": false,
  "promptId": "c576fd4f-16bc-47dd-ab5f-a8755eac9d29",
  "type": "user",
  "uuid": "bb8c1327-a3a2-4767-86f9-1f4733b8ecd0",
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
  "sourceToolAssistantUUID": "67d776a9-d484-4bec-bbe7-715ebaf4eede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14 · 2026-05-16T02:23:21.392Z_

````json
{
  "parentUuid": "bb8c1327-a3a2-4767-86f9-1f4733b8ecd0",
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
  "uuid": "20109776-0399-429a-82d6-d67ee66dad3c",
  "timestamp": "2026-05-16T02:23:21.392Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Compounding 发现和 constraint 有效性被认可，但 'universal' 语言和 diagnostic 的 claim 强度受到质疑；需要降低 claim 语气并补充实验 核心假设：['A1: compounding 被认可为有价值的实证发现，但 reviewer 指出 RateQu…",
  "leafUuid": "20109776-0399-429a-82d6-d67ee66dad3c",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze KV cache compounding effects and diagnostic thresholds",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9"
}
```

---

### Tool call

_source line 17 · 2026-05-16T02:23:24.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K1arWnmxULNcuMYhQrheXG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/experiment_plan.yaml",
  "offset": 0,
  "limit": 271
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20109776-0399-429a-82d6-d67ee66dad3c",
  "isSidechain": false,
  "requestId": "req_011Cb5TBpJf2GncTZSC7Nokn",
  "type": "assistant",
  "uuid": "12a0dc3c-1d33-4d83-9857-32c0ae6387d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t7oYLxmkg7Cqr2wXiryqj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8419,
      "cache_read_input_tokens": 49408,
      "output_tokens": 117,
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
          "output_tokens": 117,
          "cache_read_input_tokens": 49408,
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

_source line 18 · 2026-05-16T02:23:24.582Z_

<details><summary>↩ Tool result · `toolu_01K1arWnmxULNcuMYhQrheXG`</summary>

```text
0	experiments:
1	- id: plan_001
2	  claim:
3	  - 2
4	  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.
5	    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.
6	    Strengthens narrative: "solver automatically discovers sensitivity structure."
7	
8	    '
9	  priority: P0
10	  gpu_budget_hours: 1
11	  deps: []
12	  registry_id: exp_d_no_l0_exclusion
13	  model: Qwen2.5-7B
14	  eval: WikiText-2
15	- id: plan_002
16	  claim:
17	  - 1
18	  - 2
19	  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).
20	    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability
21	    across different GQA ratios and architectures. Fallback if HF token unavailable:
22	    Yi-1.5-9B (non-gated, similar scale).
23	
24	    '
25	  priority: P0
26	  gpu_budget_hours: 4
27	  deps: []
28	  registry_id: llama_full_pipeline
29	  model: Llama-3.1-8B
30	  fallback_model: Yi-1.5-9B
31	  eval: WikiText-2
32	- id: plan_003
33	  claim:
34	  - 1
35	  - 2
36	  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture
37	    family to establish cross-architecture validity.
38	
39	    '
40	  priority: P0
41	  gpu_budget_hours: 4
42	  deps: []
43	  registry_id: mistral_full_pipeline
44	  model: Mistral-7B-v0.3
45	  eval: WikiText-2
46	- id: plan_004
47	  claim:
48	  - 3
49	  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112
50	    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map
51	    the compounding threshold. Establishes the principled basis for cardinality constraint
52	    selection.
53	
54	    '
55	  priority: P0
56	  gpu_budget_hours: 3
57	  deps: []
58	  registry_id: compounding_sweep
59	  model: Qwen2.5-7B
60	  eval: WikiText-2
61	- id: plan_005
62	  claim:
63	  - 2
64	  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,
65	    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline
66	    at same budget.
67	
68	    '
69	  priority: P0
70	  gpu_budget_hours: 3
71	  deps: []
72	  registry_id: budget_sweep
73	  model: Qwen2.5-7B
74	  eval: WikiText-2
75	- id: plan_006
76	  claim:
77	  - 1
78	  - 2
79	  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).
80	    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers
81	    mid-layer heterogeneity and improves solver allocation beyond current results.
82	
83	    '
84	  priority: P0
85	  gpu_budget_hours: 3
86	  deps: []
87	  registry_id: exp_e_hires_profile
88	  model: Qwen2.5-7B
89	  eval: WikiText-2
90	- id: plan_007
91	  claim:
92	  - 1
93	  - 2
94	  - 3
95	  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.
96	    Cross-dataset evaluation to show results are not WikiText-2 specific.
97	
98	    '
99	  priority: P0
100	  gpu_budget_hours: 2
101	  deps: []
102	  registry_id: c4_rerun_d032
103	  model: Qwen2.5-7B
104	  eval: C4
105	- id: plan_008
106	  claim:
107	  - 2
108	  description: 'RateQuant comparison: implement RateQuant''s greedy algorithm (Algorithm
109	    1) on our discrete action set {2,4,8,16}-bit. RateQuant''s Prop. 6 optimality
110	    relies on consecutive-integer polymatroid structure which breaks on non-consecutive
111	    sets. Show greedy produces suboptimal allocation vs constrained MCKP. Critical
112	    for differentiation claim — must have experimental evidence.
113	
114	    '
115	  priority: P0
116	  gpu_budget_hours: 4
117	  deps: []
118	  registry_id: ratequant_greedy_comparison
119	  model: Qwen2.5-7B
120	  eval: WikiText-2
121	- id: plan_009
122	  claim:
123	  - 2
124	  description: 'Oracle comparison: brute-force optimal allocation on a subset (3-4
125	    layer groups) of Qwen2.5-7B. Quantify MCKP gap to oracle.
126	
127	    '
128	  priority: P1
129	  gpu_budget_hours: 6
130	  deps:
131	  - plan_006
132	  registry_id: oracle_comparison
133	  model: Qwen2.5-7B
134	- id: plan_010
135	  claim:
136	  - 2
137	  description: 'Cross-domain calibration robustness: calibrate on C4, evaluate on
138	    WikiText-2 (and vice versa). Report per-head allocation agreement rate across
139	    calibration sources.
140	
141	    '
142	  priority: P1
143	  gpu_budget_hours: 2
144	  deps:
145	  - plan_007
146	  registry_id: c4_rerun_d032
147	  model: Qwen2.5-7B
148	- id: plan_011
149	  claim:
150	  - 1
151	  description: 'Head sensitivity visualization: generate paper-quality figures showing
152	    per-head profiling delta heatmap across layers, compounding effect curve, and
153	    budget allocation comparison chart.
154	
155	    '
156	  priority: P1
157	  gpu_budget_hours: 1
158	  deps:
159	  - plan_004
160	  - plan_006
161	  registry_id: head_sensitivity_viz
162	- id: plan_014
163	  claim:
164	  - 2
165	  description: 'K/V separation: treat K and V heads as independent MCKP items with
166	    separate budget allocation. Compare joint K+V optimization vs current uniform
167	    K=V approach. RateQuant supports asymmetric K/V (e.g. K=2.85, V=2.15 avg bits)
168	    — we should show MCKP naturally handles this.
169	
170	    '
171	  priority: P1
172	  gpu_budget_hours: 3
173	  deps: []
174	  registry_id: kv_separation
175	  model: Qwen2.5-7B
176	  eval: WikiText-2
177	- id: plan_012
178	  claim:
179	  - 1
180	  - 2
181	  description: 'Downstream task evaluation: ARC-C / HellaSwag / PIQA / WinoGrande
182	    on Qwen2.5-7B at 4× compression. Must match RateQuant''s eval suite for direct
183	    comparison. Tests whether PPL improvements translate to downstream performance.
184	
185	    '
186	  priority: P1
187	  gpu_budget_hours: 8
188	  deps:
189	  - plan_005
190	  registry_id: downstream_eval_qwen
191	  model: Qwen2.5-7B
192	- id: plan_013
193	  claim:
194	  - 1
195	  description: '70B profiling-only: run distortion profiling on Qwen2.5-72B (no full
196	    eval). Analyze whether sensitivity patterns (Layer 0 dominance, compounding threshold)
197	    scale with model size.
198	
199	    '
200	  priority: P1
201	  gpu_budget_hours: 4
202	  deps: []
203	  registry_id: qwen72b_profiling
204	  model: Qwen2.5-72B
205	- id: plan_015
206	  claim:
207	  - 2
208	  description: 'L0-only heuristic baseline: assign 8-bit to all Layer 0 KV heads,
209	    uniform 4-bit to all other heads, at 4x compression on Qwen2.5-7B. This is the
210	    simplest possible non-uniform strategy exploiting L0 sensitivity. If L0-only matches
211	    or beats constrained MCKP, the full optimization machinery is unnecessary. Must
212	    also test on Llama and Mistral. Critical missing baseline flagged by Dream review.
213	
214	    '
215	  priority: P0
216	  gpu_budget_hours: 1
217	  deps: []
218	  registry_id: l0_only_heuristic
219	  model: Qwen2.5-7B
220	  eval: WikiText-2
221	- id: plan_016
222	  claim:
223	  - 2
224	  description: 'RateQuant greedy + cardinality constraint ablation: add max_2bit=k
225	    constraint to RateQuant greedy Algorithm 1 on {2,4,8,16}. Compare three conditions:
226	    (a) RateQuant greedy unconstrained (already have: PPL ~32.45), (b) RateQuant greedy
227	    + cardinality k=8, (c) constrained MCKP k=8 (already have: PPL ~11.23). If (b)
228	    matches (c), the contribution is the cardinality constraint, not the MCKP solver.
229	    If (c) beats (b), discrete MCKP optimization genuinely matters. Critical ablation
230	    flagged by all three Dream review tiers.
231	
232	    '
233	  priority: P0
234	  gpu_budget_hours: 2
235	  deps:
236	  - plan_008
237	  registry_id: greedy_cardinality_ablation
238	  model: Qwen2.5-7B
239	  eval: WikiText-2
240	- id: plan_017
241	  claim:
242	  - 1
243	  - 2
244	  description: 'Multi-seed error bars: run constrained MCKP and uniform 4-bit on Qwen2.5-7B
245	    at 4x compression with 3 different calibration sets (different random subsets
246	    of WikiText-2 training data). Report mean +/- std for PPL. Required for statistical
247	    credibility — Dream review flagged all-single-run as critical gap.
248	
249	    '
250	  priority: P1
251	  gpu_budget_hours: 3
252	  deps: []
253	  registry_id: multi_seed_error_bars
254	  model: Qwen2.5-7B
255	  eval: WikiText-2
256	- id: plan_018
257	  claim:
258	  - 2
259	  description: 'Runtime/latency benchmark: measure end-to-end inference latency and
260	    throughput with mixed-precision KV cache vs uniform 4-bit quantization on Qwen2.5-7B.
261	    Include profiling cost breakdown. Dream review flagged missing latency evaluation
262	    as significant gap for systems-oriented contribution.
263	
264	    '
265	  priority: P1
266	  gpu_budget_hours: 2
267	  deps: []
268	  registry_id: runtime_benchmark
269	  model: Qwen2.5-7B
270	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12a0dc3c-1d33-4d83-9857-32c0ae6387d3",
  "isSidechain": false,
  "promptId": "c576fd4f-16bc-47dd-ab5f-a8755eac9d29",
  "type": "user",
  "uuid": "88cda05a-6fa2-44ab-afff-de0b2672720c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/experiment_plan.yaml",
      "content": "experiments:\n- id: plan_001\n  claim:\n  - 2\n  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.\n    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.\n    Strengthens narrative: \"solver automatically discovers sensitivity structure.\"\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: exp_d_no_l0_exclusion\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_002\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).\n    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability\n    across different GQA ratios and architectures. Fallback if HF token unavailable:\n    Yi-1.5-9B (non-gated, similar scale).\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: llama_full_pipeline\n  model: Llama-3.1-8B\n  fallback_model: Yi-1.5-9B\n  eval: WikiText-2\n- id: plan_003\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture\n    family to establish cross-architecture validity.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mistral_full_pipeline\n  model: Mistral-7B-v0.3\n  eval: WikiText-2\n- id: plan_004\n  claim:\n  - 3\n  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112\n    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map\n    the compounding threshold. Establishes the principled basis for cardinality constraint\n    selection.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: compounding_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_005\n  claim:\n  - 2\n  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,\n    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline\n    at same budget.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: budget_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_006\n  claim:\n  - 1\n  - 2\n  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).\n    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers\n    mid-layer heterogeneity and improves solver allocation beyond current results.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_e_hires_profile\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.\n    Cross-dataset evaluation to show results are not WikiText-2 specific.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  eval: C4\n- id: plan_008\n  claim:\n  - 2\n  description: 'RateQuant comparison: implement RateQuant''s greedy algorithm (Algorithm\n    1) on our discrete action set {2,4,8,16}-bit. RateQuant''s Prop. 6 optimality\n    relies on consecutive-integer polymatroid structure which breaks on non-consecutive\n    sets. Show greedy produces suboptimal allocation vs constrained MCKP. Critical\n    for differentiation claim — must have experimental evidence.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: ratequant_greedy_comparison\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_009\n  claim:\n  - 2\n  description: 'Oracle comparison: brute-force optimal allocation on a subset (3-4\n    layer groups) of Qwen2.5-7B. Quantify MCKP gap to oracle.\n\n    '\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_006\n  registry_id: oracle_comparison\n  model: Qwen2.5-7B\n- id: plan_010\n  claim:\n  - 2\n  description: 'Cross-domain calibration robustness: calibrate on C4, evaluate on\n    WikiText-2 (and vice versa). Report per-head allocation agreement rate across\n    calibration sources.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_007\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n- id: plan_011\n  claim:\n  - 1\n  description: 'Head sensitivity visualization: generate paper-quality figures showing\n    per-head profiling delta heatmap across layers, compounding effect curve, and\n    budget allocation comparison chart.\n\n    '\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_004\n  - plan_006\n  registry_id: head_sensitivity_viz\n- id: plan_014\n  claim:\n  - 2\n  description: 'K/V separation: treat K and V heads as independent MCKP items with\n    separate budget allocation. Compare joint K+V optimization vs current uniform\n    K=V approach. RateQuant supports asymmetric K/V (e.g. K=2.85, V=2.15 avg bits)\n    — we should show MCKP naturally handles this.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: kv_separation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_012\n  claim:\n  - 1\n  - 2\n  description: 'Downstream task evaluation: ARC-C / HellaSwag / PIQA / WinoGrande\n    on Qwen2.5-7B at 4× compression. Must match RateQuant''s eval suite for direct\n    comparison. Tests whether PPL improvements translate to downstream performance.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  registry_id: downstream_eval_qwen\n  model: Qwen2.5-7B\n- id: plan_013\n  claim:\n  - 1\n  description: '70B profiling-only: run distortion profiling on Qwen2.5-72B (no full\n    eval). Analyze whether sensitivity patterns (Layer 0 dominance, compounding threshold)\n    scale with model size.\n\n    '\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: qwen72b_profiling\n  model: Qwen2.5-72B\n- id: plan_015\n  claim:\n  - 2\n  description: 'L0-only heuristic baseline: assign 8-bit to all Layer 0 KV heads,\n    uniform 4-bit to all other heads, at 4x compression on Qwen2.5-7B. This is the\n    simplest possible non-uniform strategy exploiting L0 sensitivity. If L0-only matches\n    or beats constrained MCKP, the full optimization machinery is unnecessary. Must\n    also test on Llama and Mistral. Critical missing baseline flagged by Dream review.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: l0_only_heuristic\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_016\n  claim:\n  - 2\n  description: 'RateQuant greedy + cardinality constraint ablation: add max_2bit=k\n    constraint to RateQuant greedy Algorithm 1 on {2,4,8,16}. Compare three conditions:\n    (a) RateQuant greedy unconstrained (already have: PPL ~32.45), (b) RateQuant greedy\n    + cardinality k=8, (c) constrained MCKP k=8 (already have: PPL ~11.23). If (b)\n    matches (c), the contribution is the cardinality constraint, not the MCKP solver.\n    If (c) beats (b), discrete MCKP optimization genuinely matters. Critical ablation\n    flagged by all three Dream review tiers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_008\n  registry_id: greedy_cardinality_ablation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_017\n  claim:\n  - 1\n  - 2\n  description: 'Multi-seed error bars: run constrained MCKP and uniform 4-bit on Qwen2.5-7B\n    at 4x compression with 3 different calibration sets (different random subsets\n    of WikiText-2 training data). Report mean +/- std for PPL. Required for statistical\n    credibility — Dream review flagged all-single-run as critical gap.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: multi_seed_error_bars\n  model: Qwen2.5-7B\n  eval: WikiText-2\n- id: plan_018\n  claim:\n  - 2\n  description: 'Runtime/latency benchmark: measure end-to-end inference latency and\n    throughput with mixed-precision KV cache vs uniform 4-bit quantization on Qwen2.5-7B.\n    Include profiling cost breakdown. Dream review flagged missing latency evaluation\n    as significant gap for systems-oriented contribution.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: runtime_benchmark\n  model: Qwen2.5-7B\n",
      "numLines": 271,
      "startLine": 0,
      "totalLines": 271
    }
  },
  "sourceToolAssistantUUID": "12a0dc3c-1d33-4d83-9857-32c0ae6387d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T02:23:32.710Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me construct the comprehensive YAML with median-tier predictions for each experiment. I need to use the actual experimental results from the registry and frame them through the lens of median-tier reviewer reception.

For the median tier:
- Compounding is acknowledged but novelty is discounted (RateQuant Appendix M)
- "Universal" language rejected → need 12+ models or drop the word
- Constraint seen as "obvious in hindsight" / "just a hyperparameter"
- 1/8 benefit seen as weakness ("only works on Qwen")
- Diagnostic n=9 rejected as independent claim


- Missing eviction baseline and multi-seed downstream CI will be flagged as methodological gaps

Now I'm working through each experiment with actual numbers and the median-tier critique in mind.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88cda05a-6fa2-44ab-afff-de0b2672720c",
  "isSidechain": false,
  "requestId": "req_011Cb5TC4VC54YYKJFwvBtNs",
  "type": "assistant",
  "uuid": "4d5d46df-46df-448c-9592-7668e30359e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SrCBBEQynMEp6pYnGRY9tr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 57827,
      "output_tokens": 14662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14662,
          "cache_read_input_tokens": 57827,
          "cache_creation_input_tokens": 3501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3501
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

_source line 20 · 2026-05-16T02:28:17.968Z_

```yaml
tier: median
narrative_guidance: >
  Compounding 发现被承认为有价值的实证贡献，但 RateQuant Appendix M 已 acknowledge 该现象导致 novelty 打折。
  Reviewer 要求去掉 'universal' 改为 'consistent pattern across 8 architectures'，constraint 被部分 reviewer 
  视为 'obvious hyperparameter tuning' 而非 principled contribution，需要更强的理论 justification。
  1/8 downstream benefit 被至少 1 位 reviewer 视为 'this only works on Qwen'。Diagnostic n=9 只能作为 
  observation，不能作为独立 claim。论文需要 reframe 为 empirical analysis paper，前置 analysis contribution。
  预估 narrative rewrite 30-40%，主要集中在 intro、claim 措辞、和 related work 对 RateQuant 的讨论。

imagined_experiments:
  - name: "L0 Exclusion Removal Ablation"
    plan_id: "plan_001"
    description: >
      移除 L0 排除约束，仅保留 max_2bit=8，验证 solver 纯粹从 profiling data 自动发现 L0 敏感结构。
    expected_results:
      solver_auto_assigns_8bit_to_L0: true
      ppl_without_l0_exclusion: 10.91
      ppl_with_l0_exclusion: 10.91
      delta: 0.0
      l0_heads_assigned_8bit: 4
      bit_distribution: "{2:8, 4:100, 8:4}"
    result_rationale: >
      Median 档下该结果被 reviewer 认可为 neat ablation——solver 自动发现 L0 是最敏感的层，
      不需要手动排除。但 reviewer 会指出这只在 Qwen 上验证（L0 dominance ratio=26×），
      对于 L0 dominance 低的架构（Yi 0.07，Mistral 1.74）solver 是否同样能自动发现正确结构
      缺少验证。一位 reviewer 可能注释 "this is expected — L0 has the largest profiling delta 
      by far, so any reasonable solver would protect it." 不会成为主要 objection，但也不会
      被视为独立贡献。
    tables:
      - caption: "Table: L0 Exclusion Ablation (Qwen2.5-7B, budget=0.25)"
        rows:
          - condition: "MCKP + L0 exclusion + max_2bit=8"
            ppl: 10.91
            l0_bit: "8-bit (hard-coded)"
            note: "原始设置"
          - condition: "MCKP + max_2bit=8 only"
            ppl: 10.91
            l0_bit: "8-bit (solver-discovered)"
            note: "solver 自动分配"
    figures_description:
      - "Bit allocation heatmap 对比：有/无 L0 exclusion，两者完全一致"
    analysis: >
      Reviewer 评价：supportive but minor。在 median 档中被视为 completeness ablation 
      而非核心证据。reviewer 可能建议移到 appendix。不影响主要 claim 但增加 paper 完整性。

  - name: "Llama-3.1-8B Full Pipeline Replication"
    plan_id: "plan_002"
    description: >
      在 Llama-3.1-8B（GQA 4:1）上复制完整 pipeline——profiling、constrained MCKP、PPL 评估。
      测试跨架构泛化性。
    expected_results:
      baseline_ppl_bf16: 8.09
      uniform_4bit_ppl: 8.47
      mckp_constrained_ppl: 8.45
      delta_vs_uniform_pct: 0.2
      delta_vs_uniform_ppl: 0.02
      memory_ratio: 0.25
      bit_distribution: "{2:2, 4:253, 8:1}"
      natural_2bit_count: 2
      constraint_binds: false
      unconstrained_degradation_ratio: 1.07
      top5_concentration: 0.57
      distribution_shape: "Spike"
    result_rationale: >
      Median 档下，Llama 的 marginal 结果（+0.2% vs uniform）成为 reviewer 攻击点之一。
      reviewer 会写 "the method provides essentially no benefit on Llama — the +0.2% 
      improvement is within noise." Llama 的 spike distribution（L2H5 单个 outlier 主导，
      t₁/t₅≈0.85）导致 solver 只选择 2 个 head 做 2-bit，constraint 从不触发（natural k=2 < max_2bit=8），
      MCKP 优化空间极小。这解释了为什么 PPL 差异几乎为零。但从 compounding 角度，
      unconstrained 仍然 1.07× baseline，说明即使 mild 情况下 solver 仍会略微 over-allocate。
      Reviewer 会要求诚实报告 "no benefit" 而非 spin 为 positive。在 median 档中，
      这个 negative result 本身不被反对——reviewer 反对的是用 8 个架构中只有 1 个 positive 
      来声称 method 有效。
    tables:
      - caption: "Table: Llama-3.1-8B Pipeline Results (budget=0.25)"
        rows:
          - method: "BF16 baseline"
            ppl: 8.09
            bits: "16"
            note: ""
          - method: "Uniform 4-bit"
            ppl: 8.47
            bits: "4.0"
            note: ""
          - method: "Unconstrained MCKP"
            ppl: 8.63
            bits: "mixed"
            note: "1.07× baseline"
          - method: "Constrained MCKP (k=8)"
            ppl: 8.45
            bits: "{2:2, 4:253, 8:1}"
            note: "+0.2% vs uniform"
    figures_description:
      - "Per-head sensitivity heatmap：极少数 head 有显著 delta，大部分 flat"
    analysis: >
      Median reviewer 会同时肯定和批评：肯定 honest reporting of negative result，
      批评 "if 7/8 architectures show no benefit, this is not a method paper — it's an 
      analysis paper that happens to find one architecture where optimization helps." 
      这强化了 reframe 为 empirical analysis 的需要。

  - name: "Mistral-7B-v0.3 Full Pipeline Replication"
    plan_id: "plan_003"
    description: >
      在 Mistral-7B-v0.3 上复制完整 pipeline。不同架构家族，建立跨架构有效性。
    expected_results:
      baseline_ppl_bf16: 7.035
      uniform_4bit_ppl: 7.131
      mckp_constrained_ppl: 7.165
      delta_vs_uniform_pct: -0.5
      delta_vs_uniform_ppl: -0.034
      memory_ratio: 0.25
      bit_distribution: "{2:4, 4:252}"
      unconstrained_degradation_ratio: 1.08
      top5_concentration: 0.22
      distribution_shape: "Flat"
      k_ablation_monotonic: true
      best_k_still_worse_than_uniform: true
    result_rationale: >
      Mistral 是最强 negative case：MCKP 在所有 k 值下都 worse than uniform。
      PPL 随 k 单调递增（k=4: 7.165, k=8: 7.200, k=18: 7.323），profiler 报告近零 
      sensitivity 差异（concentration=0.22, CV=1.31）。这表明 Mistral 的 KV head 
      sensitivity 高度均匀——没有 head 从 2-bit downgrade 中获益。Median reviewer 
      会将此视为 "method failure on flat architectures" 和 "proof that uniform 4-bit 
      is optimal when profiler gives zero signal." 对 compounding claim 仍有帮助：
      unconstrained 1.08× 表明即使 flat distribution，solver 仍 over-allocate 
      2-bit heads（42/256=16.4%）。但 reviewer 会质疑 "1.08× is hardly catastrophic 
      — this is within the range where a practitioner wouldn't even notice."
    tables:
      - caption: "Table: Mistral-7B-v0.3 k-Ablation (budget=0.25)"
        rows:
          - k: 4
            ppl: 7.165
            n_2bit: 4
            note: "best constrained, still > uniform"
          - k: 8
            ppl: 7.200
            n_2bit: 8
            note: ""
          - k: 16
            ppl: 7.311
            n_2bit: 16
            note: ""
          - k: "uniform"
            ppl: 7.131
            n_2bit: 0
            note: "optimal for Mistral"
    figures_description:
      - "k-PPL 单调递增曲线，与 Qwen 的 U-shaped 对比"
    analysis: >
      在 median 档中，Mistral negative result 既是弱点也是优势。弱点：method 不 work。
      优势：honest negative result 增加 credibility，且支持 diagnostic 的必要性——
      如果没有 diagnostic，practitioners 会浪费 profiling 时间在 Mistral 这样的模型上。
      Reviewer 2 (偏方法) 会将此作为 "method only works on Qwen" 的证据。
      Reviewer 3 (偏分析) 会认可这增加了 paper 的科学价值。

  - name: "Compounding Effect Characterization Sweep"
    plan_id: "plan_004"
    description: >
      在 Qwen2.5-7B 上扫 max_2bit 从 0 到 112，绘制 PPL vs max_2bit 曲线，
      确定 compounding 阈值。建立 cardinality constraint 的 principled 基础。
    expected_results:
      k0_ppl: 9.81
      k8_ppl: 10.05
      k16_ppl: 10.42
      k32_ppl: 11.60
      k64_ppl: 23.22
      k112_ppl: 98.75
      compounding_threshold_k: 16
      max_compounding_ratio: 10.07
      curve_shape: "superlinear after k≈16, exponential after k≈48"
      safe_k_range: "k≤8 universally <2.5% degradation"
    result_rationale: >
      Compounding sweep 是 median 档中最被认可的实验——提供了 compounding 效应的
      定量证据。PPL 在 k≤8 时近线性增长（9.81→10.05, +2.4%），k=16-32 开始加速
      （10.42→11.60），k≥48 后指数爆炸（23.22→98.75）。这条曲线是 "principled 
      basis for constraint selection" 的核心证据。但 median reviewer 会有两个质疑：
      (1) "这条曲线只在 Qwen 上做了——其他架构的阈值可能完全不同"（A2），
      (2) "RateQuant Appendix M 已经 acknowledge compounding，这个 sweep 只是
      quantified 了已知现象"（A1）。需要补充 Llama 和 Mistral 的 compounding sweep 
      来部分 address (1)——实际已有数据（llama_compounding_sweep, mistral_compounding_sweep_v2）
      可以回应。Reviewer 对 k≤8 safety 的 claim 会接受，但会要求去掉 "universally safe" 
      改为 "safe across all tested architectures."
    tables:
      - caption: "Table: Compounding Sweep (Qwen2.5-7B, budget=0.25)"
        rows:
          - k: 0
            ppl: 9.81
            ratio_to_baseline: "1.00×"
          - k: 8
            ppl: 10.05
            ratio_to_baseline: "1.02×"
          - k: 16
            ppl: 10.42
            ratio_to_baseline: "1.06×"
          - k: 32
            ppl: 11.60
            ratio_to_baseline: "1.18×"
          - k: 64
            ppl: 23.22
            ratio_to_baseline: "2.37×"
          - k: 112
            ppl: 98.75
            ratio_to_baseline: "10.07×"
    figures_description:
      - "PPL vs max_2bit 曲线（log-scale y-axis），标注 safe zone（k≤8）和 catastrophic zone（k≥48）"
      - "三架构对比 compounding sweep（Qwen U-shaped, Llama flat, Mistral monotonic）"
    analysis: >
      Median reviewer 的核心反馈：compounding effect 是 real and well-characterized，
      但 novelty 因 RateQuant Appendix M 打折。建议在 related work 中显式讨论 
      "RateQuant acknowledges compounding in Appendix M but does not characterize the 
      threshold or provide a fix — our sweep provides the first quantitative mapping." 
      三架构对比增加说服力：Qwen 的 U-shape（optimal k=8）、Llama 的 flat profile
      （natural k=2, constraint irrelevant）、Mistral 的 monotonic increase（every 
      2-bit head hurts）展示了 architecture-dependent compounding behavior。

  - name: "Budget Sweep (2×/4×/8× Compression)"
    plan_id: "plan_005"
    description: >
      在 Qwen2.5-7B 上测试 2×/4×/8× 压缩比下的 constrained MCKP vs uniform baseline。
    expected_results:
      budget_0.5_mckp_ppl: 9.85
      budget_0.5_uniform_ppl: 9.86
      budget_0.5_delta_pct: 0.1
      budget_0.25_mckp_ppl: 10.91
      budget_0.25_uniform_ppl: 15.45
      budget_0.25_delta_pct: 29.4
      budget_0.125_mckp_ppl: 57.60
      budget_0.125_uniform_2bit_ppl: 2643.77
      budget_0.125_delta_ratio: "45.9×"
      compression_amplifies_benefit: true
    result_rationale: >
      Budget sweep 展示了核心趋势：压缩越激进，constrained MCKP vs uniform 的差距越大。
      在 2× 压缩下差异几乎为零（都接近 baseline），4× 时 MCKP 优势 29.4%，8× 时
      MCKP 57.60 vs uniform 2643.77（45×差距）。Median reviewer 会认可 aggressive 
      compression 的 practical value（"at 8× compression, the constraint is the difference 
      between usable and unusable"），但会指出：(a) 2× 结果说明 moderate compression 下
      benefit 主要来自 Qwen 的 spread pattern 而非 method 本身，(b) 8× 的 PPL=57.60 
      虽远好于 2643.77，但 absolute 值仍然很高——"is a 57.60 PPL model actually usable?" 
      需要补充 aggressive compression 下的 downstream task 评估。(c) 只在 Qwen 上做了
      full sweep，Llama 的 aggressive compression 数据（57.60 vs 2643.77）虽有但
      仅一个点，不是 sweep。
    tables:
      - caption: "Table: Budget Sweep (Qwen2.5-7B)"
        rows:
          - compression: "2× (budget=0.5)"
            mckp_ppl: 9.85
            uniform_ppl: 9.86
            delta: "~0%"
          - compression: "4× (budget=0.25)"
            mckp_ppl: 10.91
            uniform_ppl: 15.45
            delta: "29.4%"
          - compression: "8× (budget=0.125)"
            mckp_ppl: 57.60
            uniform_ppl: 2643.77
            delta: "45.9×"
    figures_description:
      - "Compression ratio vs PPL 对比图：MCKP 和 uniform 两条线在高压缩比处剧烈分离"
    analysis: >
      Median 档中被部分接受。Reviewer 认可 practical implication（高压缩比下 constraint 
      essential），但质疑 moderate compression（主要应用场景）下只有 Qwen 获益的泛化性。
      建议补充 Llama/Mistral 的 budget sweep 至少在 8× 压缩点。

  - name: "High-Resolution Profiling"
    plan_id: "plan_006"
    description: >
      64 seq × 2048 tokens 的高分辨率 profiling（vs 16×512），验证更好的 profiling 
      是否改善 solver allocation。
    expected_results:
      hires_constrained_ppl_bf16: 10.91
      lowres_constrained_ppl_bf16: 11.23
      baseline_ppl_bf16: 9.81
      improvement_vs_lowres: 0.32
      improvement_pct: 2.8
      hires_nonzero_2bit_heads: 100
      lowres_nonzero_2bit_heads: 37
      allocation_diff_count: 8
      profiling_time_min: 65.5
      bit_distribution: "{2:8, 4:100, 8:4}"
    result_rationale: >
      高分辨率 profiling 将 PPL 从 11.23 降到 10.91（-2.8%），说明 profiling resolution 
      matters。核心改进来自更准确的 sensitivity ranking：hires 发现 100/112 heads 有
      非零 2-bit delta（vs lowres 37/112），导致 8 个 head 的 allocation 改变。
      Median reviewer 反应分化：(a) 方法 reviewer 认为这说明 "profiling quality drives 
      results more than solver choice — the real engineering is in the profiler, not MCKP"，
      进一步削弱 solver 作为贡献的地位；(b) 系统 reviewer 注意到 65.5 min profiling time 
      并质疑 "practitioners won't spend an hour profiling a 7B model to save 0.32 PPL"。
      需要在 paper 中 trade-off profiling cost vs quality，并论证 lowres 已足够好
      （11.23 vs uniform 15.45, 仍有 27.3% improvement）。
    tables:
      - caption: "Table: Profiling Resolution Impact (Qwen2.5-7B, k=8)"
        rows:
          - resolution: "Low-res (16×512)"
            ppl: 11.23
            nonzero_heads: 37
            time_min: "~10"
          - resolution: "High-res (64×2048)"
            ppl: 10.91
            nonzero_heads: 100
            time_min: 65.5
          - resolution: "Uniform 4-bit"
            ppl: 15.45
            nonzero_heads: "N/A"
            time_min: 0
    figures_description:
      - "Per-head delta comparison：lowres vs hires scatter plot，标注 allocation 改变的 8 个 head"
    analysis: >
      Median 档中作为 engineering insight 被接受。Reviewer 不会 object 但建议
      放 appendix 而非 main body。对 claim 的影响中性——既不强化也不削弱核心论点。

  - name: "C4 Cross-Dataset Evaluation"
    plan_id: "plan_007"
    description: >
      在 C4 上评估 Qwen2.5-7B（calibrate on WikiText-2, eval on C4; calibrate on C4, eval on WikiText-2），
      验证结果不是 WikiText-2 specific。
    expected_results:
      c4_cal_wt2_eval_mckp_ppl: 11.29
      c4_cal_wt2_eval_uniform_ppl: 15.45
      c4_cal_wt2_eval_delta: 4.15
      allocation_agreement_c4_vs_wt2: 0.964
      agreement_heads: "108/112"
      cross_domain_wt2_to_c4_mckp_ppl: 20.56
      cross_domain_wt2_to_c4_uniform_ppl: 35.42
      contamination_impact: 0.034
    result_rationale: >
      96.4% allocation agreement 跨 calibration source 是 positive signal：profiling 
      的 head sensitivity ranking 对 calibration data 不敏感。Median reviewer 会认可 
      cross-dataset robustness 但指出：(a) 只在 Qwen 上验证（"is this agreement rate 
      architecture-dependent?"），(b) 4/112 disagreement heads 的 identity 和影响未讨论，
      (c) cross-domain PPL（WiKi→C4: 20.56 vs uniform 35.42）虽然 MCKP 仍胜出，
      但绝对 PPL 远高于 same-domain（11.29），说明 calibration domain mismatch 仍有成本。
      Reviewer 会建议 "report agreement rate on at least one more architecture" 作为
      minor revision。已有 llama_c4_cross_dataset（97.7% agreement）和 
      mistral_c4_cross_dataset（96.5%）数据可以回应。
    tables:
      - caption: "Table: Cross-Dataset Calibration Agreement"
        rows:
          - model: "Qwen2.5-7B"
            agreement: "108/112 (96.4%)"
            same_domain_ppl: 11.29
            cross_domain_ppl: 20.56
          - model: "Llama-3.1-8B"
            agreement: "250/256 (97.7%)"
            same_domain_ppl: 8.45
            cross_domain_ppl: 8.65
          - model: "Mistral-7B-v0.3"
            agreement: "247/256 (96.5%)"
            same_domain_ppl: 7.16
            cross_domain_ppl: 7.19
    figures_description: []
    analysis: >
      三架构的 >96% agreement 是 strong evidence for calibration robustness。
      Median reviewer 视为 useful supplementary experiment，不会 object。
      建议放 Section 4 或 appendix。

  - name: "RateQuant Greedy Comparison"
    plan_id: "plan_008"
    description: >
      实现 RateQuant 的 greedy Algorithm 1 在 {2,4,8,16} 上，展示 greedy 在
      non-consecutive 集合上 suboptimal。
    expected_results:
      ratequant_greedy_unconstrained_ppl: 32.45
      mckp_unconstrained_ppl: 36.92
      uniform_4bit_ppl: 15.45
      greedy_bit_distribution: "{2:68, 4:30, 8:4, 16:10}"
      both_worse_than_uniform: true
      greedy_better_than_mckp_unconstrained: true
    result_rationale: >
      关键发现：两个 solver 在 unconstrained 设置下都 worse than uniform，但 greedy 
      (32.45) 反而比 MCKP (36.92) 好！这颠覆了 "MCKP is better optimizer" 的叙事。
      Median reviewer 会抓住这个点："if greedy outperforms MCKP unconstrained, 
      why do you need MCKP at all?" 回应：unconstrained 时两者都失败（compounding），
      差异无意义；constrained 时两者完全一致（Δ=0.0000）——plan_016 的 solver equivalence 
      证据。但这确实削弱了 MCKP 作为 solver contribution 的叙事，支持 reframe：
      "constraint is the contribution, not the solver." 一位 reviewer 会标注 
      "the unconstrained MCKP being worse than greedy suggests the ILP formulation 
      interacts poorly with compounding — discuss this." 需要在 paper 中解释为什么
      MCKP 更容易 over-allocate 2-bit（因为它更 aggressively optimizes per-head 
      cost-benefit，导致更多 2-bit assignments）。
    tables:
      - caption: "Table: Unconstrained Solver Comparison (Qwen2.5-7B)"
        rows:
          - solver: "RateQuant Greedy (unconstrained)"
            ppl: 32.45
            n_2bit: 68
            status: "FAIL"
          - solver: "MCKP (unconstrained)"
            ppl: 36.92
            n_2bit: "≥68"
            status: "FAIL"
          - solver: "Uniform 4-bit"
            ppl: 15.45
            n_2bit: 0
            status: "baseline"
    figures_description:
      - "Bar chart: 三种 method PPL 对比，unconstrained 均远超 uniform"
    analysis: >
      Median 档中该实验的价值被 reinterpret：不再是 "MCKP beats greedy" 
      而是 "both fail without constraint, both succeed with constraint." 
      这是 solver equivalence 叙事的第一半证据。Reviewer 认可这个 framing shift。

  - name: "Oracle Comparison (Subset Brute-Force)"
    plan_id: "plan_009"
    description: >
      在 Qwen2.5-7B 的 3-4 个 layer group 上做 brute-force optimal allocation，
      量化 MCKP gap to oracle。
    expected_results:
      mckp_ppl: 10.91
      max_oracle_gap_ppl: 0.018
      avg_oracle_gap_ppl: 0.005
      layers_mckp_optimal: "5/8"
      layers_with_gap: 3
      gap_nature: "2-bit head position swap within same bit budget"
      total_evals: 54
    result_rationale: >
      MCKP 与 oracle 的 gap 极小（max 0.018 PPL, avg 0.005 PPL），5/8 layer groups 
      完全 optimal，3 个 gap 来自同 budget 下 2-bit head 位置互换。Median reviewer 
      会认可 "MCKP is near-optimal within the constrained feasible set" 但立刻指出：
      "combined with plan_016 showing greedy=MCKP, this means the constraint defines 
      the quality — any solver that respects the constraint is near-optimal. The MCKP 
      formulation adds no value." 这进一步支持 constraint-as-contribution framing，
      但同时使 MCKP 作为 method 贡献更不站得住。reviewer 建议 "present MCKP as the 
      analysis framework, not the algorithmic contribution." 在 median 档中这个实验
      反而帮助了 reframe——它是 "solver doesn't matter" 叙事的 complementary evidence。
    tables:
      - caption: "Table: MCKP vs Oracle Gap (Qwen2.5-7B, per layer group)"
        rows:
          - layer_group: "L0-L3"
            mckp_optimal: true
            gap_ppl: 0.0
          - layer_group: "L4-L7"
            mckp_optimal: false
            gap_ppl: 0.0045
          - layer_group: "L8-L11"
            mckp_optimal: false
            gap_ppl: 0.0136
          - layer_group: "L12-L15"
            mckp_optimal: true
            gap_ppl: 0.0
    figures_description: []
    analysis: >
      Near-zero oracle gap 与 solver equivalence 共同构成 "constraint is what matters" 
      的完整论证。Median reviewer 视为 thorough analysis, 建议作为 Section 4 的
      supporting evidence。

  - name: "Cross-Domain Calibration Robustness"
    plan_id: "plan_010"
    description: >
      C4 calibration → WikiText-2 eval 和反方向，报告 per-head allocation agreement rate。
    expected_results:
      allocation_agreement_c4_vs_wt2: 0.964
      agreement_heads: "108/112"
      c4_cal_wt2_eval_mckp_ppl: 11.29
      cross_domain_gap_vs_same_domain: 0.06
    result_rationale: >
      与 plan_007 共享数据。96.4% agreement 说明 profiling-based sensitivity ranking 
      对 calibration source 高度鲁棒。Median reviewer 反应温和 positive——这是
      expected behavior（"if head sensitivity is an architectural property, it shouldn't 
      depend on calibration data"），所以不会 strongly impress but also won't object。
      主要 reviewer concern 是 Qwen-only，但已有三架构数据（Qwen 96.4%, Llama 97.7%, 
      Mistral 96.5%）可补充。
    tables: []
    figures_description: []
    analysis: >
      Minor positive signal。在 median 档中作为 robustness check 被接受，
      不影响 overall score。

  - name: "Head Sensitivity Visualization"
    plan_id: "plan_011"
    description: >
      生成 per-head profiling delta heatmap、compounding curve、budget allocation 对比图。
    expected_results:
      figures_generated: 3
      heatmap_shows_l0_dominance: true
      compounding_curve_elbow: "k≈16"
      allocation_comparison_shows_constraint_effect: true
    result_rationale: >
      可视化是 presentation quality 问题而非科学证据。Median reviewer 会在
      minor comments 中评价："Figure X clearly shows the L0 dominance pattern" 
      或 "the compounding curve would benefit from error bars." 不影响 score 但
      好的可视化可以帮助 reviewer 快速理解 compounding 现象。关键是 heatmap 要
      展示 Qwen（spread, L0 cluster 明显）vs Yi（spike, 单个 L4H3 突出）vs 
      Gemma-2（flat, 无显著差异）的对比——如果只展示 Qwen，reviewer 会说 
      "cherry-picked visualization."
    tables: []
    figures_description:
      - "Per-head 2-bit delta heatmap（layers × heads），色彩标注 Qwen L0 cluster"
      - "Compounding sweep 曲线（PPL vs k），标注 safe/moderate/catastrophic zones"
      - "Budget allocation 对比（stacked bar: 2/4/8/16 bit distribution across methods）"
    analysis: >
      Presentation-level contribution。Median reviewer 可能 suggest 改进但不会
      因为 visualization 加分或扣分。

  - name: "K/V Separation"
    plan_id: "plan_014"
    description: >
      K 和 V heads 作为独立 MCKP items，独立 budget allocation。与 joint K=V 方法对比。
    expected_results:
      kv_sep_ppl: 11.22
      joint_kv_ppl: 10.91
      uniform_4bit_ppl: 15.45
      delta_sep_vs_joint: 0.31
      sep_k_2bit_count: 16
      sep_v_uniform_4bit: true
      kv_asymmetric_heads: 21
    result_rationale: >
      K/V separation 反而 worse（11.22 vs 10.91, +0.31 PPL）。separation 给 K heads 
      分配了 16 个 2-bit（超过 max_2bit=8 的 joint 约束），导致 K cache compounding。
      V heads 在 separation 下全部 4-bit（optimal for V），但 K cache 的退化超过了
      V 的收益。Median reviewer 会认为这是 negative result 但有 insight value：
      "K cache is more sensitive to 2-bit compounding than V — this explains why 
      joint K=V treatment with a single cardinality constraint works better." 
      一位 reviewer 可能 suggest "apply per-cache-type cardinality constraint" 
      as future work。不会成为 major objection。
    tables:
      - caption: "Table: K/V Separation vs Joint (Qwen2.5-7B, k=8)"
        rows:
          - method: "Joint K=V (k=8)"
            ppl: 10.91
            k_2bit: 8
            v_2bit: 0
          - method: "K/V Separation"
            ppl: 11.22
            k_2bit: 16
            v_2bit: 0
          - method: "Uniform 4-bit"
            ppl: 15.45
            k_2bit: 0
            v_2bit: 0
    figures_description: []
    analysis: >
      Negative result 但 informative。在 median 档中被视为 thorough ablation，
      可放 appendix。不影响核心 claim。

  - name: "Downstream Task Evaluation (Qwen2.5-7B)"
    plan_id: "plan_012"
    description: >
      ARC-C / HellaSwag / PIQA / WinoGrande 在 Qwen2.5-7B 4× 压缩下评估。
      验证 PPL improvement 转化为 downstream performance。
    expected_results:
      arc_c_uniform: 0.4812
      arc_c_mckp: 0.5137
      arc_c_delta_pp: 3.16
      hellaswag_uniform: 0.7284
      hellaswag_mckp: 0.7684
      hellaswag_delta_pp: 4.00
      piqa_uniform: 0.7661
      piqa_mckp: 0.7786
      piqa_delta_pp: 1.25
      winogrande_uniform: 0.6622
      winogrande_mckp: 0.6819
      winogrande_delta_pp: 1.97
      avg_recovery: 0.728
      bf16_avg: 0.688
    result_rationale: >
      Qwen downstream gains 一致 positive（+1.25 to +4.00pp），与 PPL improvement 
      方向一致。但 median reviewer 的核心 objection 是 A4："this only works on Qwen."
      跨架构 downstream 数据显示 Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, 
      Gemma-2 +0.14pp（noise）。reviewer 会写："4/5 architectures show negative or 
      negligible downstream effect. The method degrades downstream performance on most 
      models." 另一个 median-specific concern 是 lack of multi-seed CI：3.16pp arc_c 
      delta 没有 confidence interval，"could be within single-run variance"（A6）。
      已有 qwen_3seed_downstream_ci（arc_c std=0.0035, hellaswag std=0.0022）
      可部分回应。arc_challenge 跨模型系统性退化（Yi -3.24pp, Llama -2.65pp, 
      Mistral -1.19pp）会被特别标注——reviewer 要求主动讨论这个 pattern。
    tables:
      - caption: "Table: Downstream Evaluation — Full Cross-Architecture"
        rows:
          - model: "Qwen (Spread)"
            avg_delta_pp: "+2.60"
            arc_c_delta: "+3.16"
            verdict: "Benefit"
          - model: "Yi-1.5 (Spike)"
            avg_delta_pp: "-0.77"
            arc_c_delta: "-3.24"
            verdict: "Degradation"
          - model: "Llama (Spike)"
            avg_delta_pp: "-0.99"
            arc_c_delta: "-2.65"
            verdict: "Degradation"
          - model: "Mistral (Flat)"
            avg_delta_pp: "-0.48"
            arc_c_delta: "-1.19"
            verdict: "Degradation"
          - model: "Gemma-2 (Flat)"
            avg_delta_pp: "+0.14"
            arc_c_delta: "-0.17"
            verdict: "Noise"
    figures_description:
      - "Per-task per-model heatmap（MCKP delta vs uniform），突出 arc_challenge 系统性退化"
    analysis: >
      Median 档中这是 double-edged evidence。Qwen 的 downstream gains 被认可但
      限定为 "architecture-specific"。跨架构 degradation 要求论文措辞从
      "non-uniform improves downstream" 改为 "non-uniform allocation improves downstream 
      performance specifically on architectures with spread sensitivity patterns (1/5 
      tested); on other architectures, uniform 4-bit should be preferred." 
      arc_challenge 系统性退化需要主动讨论段落。

  - name: "70B Profiling-Only"
    plan_id: "plan_013"
    description: >
      在 Qwen2.5-72B 上做 distortion profiling（不做 full eval），分析 sensitivity 
      patterns 是否随模型大小 scale。
    expected_results:
      status: killed
      sensitivity_pattern_observed: null
      l0_dominance_scales: null
    result_rationale: >
      实验被 killed（可能 OOM 或 timeout）。Median reviewer 会注意到 "only 7B-14B 
      scale models tested" 并标注为 limitation："no evidence that findings generalize 
      to production-scale models (70B+)." 但在 median 档中这是 minor gap 而非 major 
      objection——大多数 KV cache quantization papers 也只测 7B-14B。缺少 70B 数据
      会降低 "practical implications" 的说服力但不会导致 reject。建议在 limitations 
      中明确承认 "our experiments are limited to 7B-14B scale; scaling behavior of 
      compounding effects to 70B+ models remains an open question."
    tables: []
    figures_description: []
    analysis: >
      Missing data。Median reviewer 标注为 limitation，不作为 reject reason。

  - name: "L0-Only Heuristic Baseline"
    plan_id: "plan_015"
    description: >
      最简单的 non-uniform 策略：L0 heads 8-bit，其余 uniform 4-bit。如果
      L0-only 匹配 MCKP，full optimization 不必要。
    expected_results:
      qwen_mckp_ppl: 10.91
      qwen_l0_random_mean: 11.69
      qwen_l0_random_std: 0.47
      qwen_l0_random_median: 11.52
      qwen_naive_positional_ppl: 12.23
      llama_mckp_ppl: 8.45
      llama_l0_random_mean: 10.48
      llama_naive_positional: 9.94
      mistral_mckp_ppl: 7.16
      mistral_l0_random_mean: 7.56
      mistral_naive_positional: 7.48
      mckp_consistently_beats_l0_random: true
    result_rationale: >
      L0-only heuristic 的 PPL（Qwen median 11.52, mean 11.69）consistently worse 
      than MCKP（10.91），差距 -5.2%。这说明 profiling-based allocation 在 constraint 
      内仍有 optimization value——不仅仅是 "protect L0 and done." Median reviewer 
      反应正面但有 nuance：(a) "MCKP beats L0-random by 5.2% — meaningful but not 
      dramatic. The naive positional heuristic (12.23) is much worse, so profiling does 
      matter." (b) "seed variance in L0-random is large (std=0.47, range 11.33-12.52), 
      suggesting the specific choice of which non-L0 heads get 2-bit matters significantly." 
      (c) Llama 和 Mistral 上 MCKP vs L0-random gap 更大（Llama: 8.45 vs 10.04 median, 
      -15.8%），说明 even on non-benefit architectures, random constraint-respecting 
      allocation is much worse than MCKP — the solver finds better allocations even when 
      the absolute PPL difference vs uniform is small. 这个 experiment 的原始设计被 kill
      但后来用 corrected version (l0_heuristic_corrected) 完成。
    tables:
      - caption: "Table: MCKP vs Heuristic Baselines (budget=0.25)"
        rows:
          - model: "Qwen"
            mckp: 10.91
            l0_random_median: 11.52
            naive_positional: 12.23
            uniform: 15.45
          - model: "Llama"
            mckp: 8.45
            l0_random_median: 10.04
            naive_positional: 9.94
            uniform: 8.47
          - model: "Mistral"
            mckp: 7.16
            l0_random_median: 7.59
            naive_positional: 7.48
            uniform: 7.13
    figures_description:
      - "Bar chart per architecture: MCKP < L0-random < naive positional（Qwen pattern）"
    analysis: >
      Median reviewer 认为这是 critical missing baseline 被补充后的 adequate response。
      MCKP vs L0-random gap（5-16%）证明 solver 在 constraint-respecting 方案中仍有
      optimization 价值。但 Mistral 的 MCKP(7.16) > uniform(7.13) 再次说明 flat 
      architecture 上任何 non-uniform 都是 net negative。

  - name: "Greedy + Cardinality Constraint Ablation (Solver Equivalence)"
    plan_id: "plan_016"
    description: >
      RateQuant greedy + max_2bit=k 约束。对比 (a) greedy unconstrained, 
      (b) greedy constrained k=8, (c) MCKP constrained k=8。
    expected_results:
      greedy_unconstrained_ppl: 32.45
      greedy_constrained_ppl: 11.23
      mckp_constrained_ppl: 11.23
      delta_greedy_vs_mckp_constrained: 0.0012
      bit_distribution_identical: true
      distribution: "{2:8, 4:100, 8:4}"
    result_rationale: >
      这是 paper 最 powerful 的单个实验：constrained greedy = constrained MCKP 
      (Δ=0.0012 PPL, identical bit distribution)。证明 constraint 是唯一 intervention 
      that matters——两个算法复杂度完全不同的 solver 在 constraint 下产生相同解。
      Median reviewer 对此实验的反应最 positive："this is the strongest evidence in the 
      paper — it shows the cardinality constraint is the real contribution, not the 
      optimization algorithm." 但也引发 A3 concern："if a simple cardinality constraint 
      is all you need, this is essentially one hyperparameter — is that a sufficient 
      contribution for a main conference paper?" Reviewer 会要求 (a) 更强的 principled 
      justification for why cardinality constraint works（不只是 empirical observation），
      (b) 讨论 constraint 与 RateQuant 的 distortion model 的关系。Qwen14b 上也验证了
      solver equivalence（greedy=MCKP, Δ=0.0），增加了 generality。
    tables:
      - caption: "Table: Solver Equivalence Under Constraint (Qwen2.5-7B, k=8)"
        rows:
          - solver: "Greedy unconstrained"
            ppl: 32.45
            bit_dist: "{2:68, 4:30, 8:4, 16:10}"
            status: "FAIL"
          - solver: "Greedy + max_2bit=8"
            ppl: 11.23
            bit_dist: "{2:8, 4:100, 8:4}"
            status: "PASS"
          - solver: "MCKP + max_2bit=8"
            ppl: 11.23
            bit_dist: "{2:8, 4:100, 8:4}"
            status: "PASS"
          - solver: "Uniform 4-bit"
            ppl: 15.45
            bit_dist: "all 4-bit"
            status: "baseline"
    figures_description:
      - "Side-by-side bit allocation heatmaps: greedy constrained vs MCKP constrained（完全一致）"
    analysis: >
      Median 档中被认可为 paper 的 highlight。两位 reviewer 会引用此结果支持
      "the constraint is the contribution" narrative。但第三位 reviewer 用此结果
      反驳 "then what exactly is the technical contribution — discovering that you need 
      a max_2bit cap? That's a hyperparameter, not a method."

  - name: "Multi-Seed Error Bars"
    plan_id: "plan_017"
    description: >
      Qwen2.5-7B 上 3 个不同 calibration seed 的 constrained MCKP，报告 mean±std。
    expected_results:
      mckp_seed0: 11.02
      mckp_seed1: 10.90
      mckp_seed2: 11.05
      mckp_mean: 10.99
      mckp_std: 0.065
      bit_dist_all_seeds: "{2:8, 4:100, 8:4}"
      allocation_agreement_3way: 0.902
      uniform_4bit_ppl: 15.45
      improvement_significant: true
      ci_95_upper: 11.12
      ci_95_lower: 10.86
    result_rationale: >
      std=0.065 意味着 95% CI 约 [10.86, 11.12]，远低于 uniform 15.45——improvement 
      统计上 robust。Bit distribution 在所有 seed 下一致（{2:8, 4:100, 8:4}），
      allocation agreement 90.2% 跨 seed。Median reviewer 会认可 PPL stability 但有
      两个 residual concerns：(a) "3 seeds is the minimum — 5 seeds with proper CI would 
      be more convincing"（minor revision level），(b) "allocation agreement 90.2% means 
      10% of heads flip between seeds — which heads and how does it affect downstream?" 
      更严重的是 A6：**缺少 multi-seed downstream CI**。PPL multi-seed 已有，但 
      downstream 的 arc_c +3.16pp 没有 error bar。qwen_3seed_downstream_ci 提供了
      部分数据（arc_c std=0.0035），但只在 Qwen 上。Reviewer 会标注 "multi-seed 
      downstream CI missing for non-Qwen architectures" 作为 significant gap。
    tables:
      - caption: "Table: Multi-Seed PPL Stability (Qwen2.5-7B, k=8)"
        rows:
          - seed: 0
            ppl: 11.02
            bit_dist: "{2:8, 4:100, 8:4}"
          - seed: 1
            ppl: 10.90
            bit_dist: "{2:8, 4:100, 8:4}"
          - seed: 2
            ppl: 11.05
            bit_dist: "{2:8, 4:100, 8:4}"
          - seed: "mean±std"
            ppl: "10.99±0.065"
            bit_dist: "consistent"
    figures_description:
      - "Error bar plot: MCKP mean±std vs uniform（non-overlapping）"
    analysis: >
      Median reviewer 接受 PPL 层面的 statistical credibility 但要求 downstream CI。
      这是 median 档的 typical gap——不至于 reject 但会是 "requested revision" 的一部分。

  - name: "Runtime/Latency Benchmark"
    plan_id: "plan_018"
    description: >
      End-to-end inference latency 和 throughput，mixed-precision KV cache vs uniform 4-bit。
    expected_results:
      bf16_prefill_ms: 45.86
      bf16_decode_ms: 33.78
      bf16_throughput: 29.6
      uniform4_prefill_ms: 54.25
      uniform4_decode_ms: 42.46
      uniform4_throughput: 23.6
      mckp_prefill_ms: 57.03
      mckp_decode_ms: 46.09
      mckp_throughput: 21.8
      mckp_solver_time_sec: 0.005
      memory_compression_4x: true
      mckp_overhead_vs_uniform_pct: 8.5
      mckp_overhead_vs_bf16_pct: 36.4
    result_rationale: >
      令人意外的 negative finding：mixed-precision MCKP 比 uniform 4-bit 更慢
      （throughput 21.8 vs 23.6 tok/s, -7.6%），甚至比 bf16 baseline 更慢
      （21.8 vs 29.6 tok/s, -26.4%）。原因是 mixed-precision 需要 per-head 不同
      的 dequantization kernel，当前实现缺少 fused kernel optimization。
      Median reviewer 反应强烈 negative："the method provides 29% PPL improvement 
      on Qwen but costs 8% throughput — practitioners would need to decide if PPL 
      improvement justifies speed regression. On 7/8 architectures where there's no 
      PPL benefit, the speed cost is pure overhead." 这成为 major objection 之一（A6 
      范畴）。MCKP solver 本身只需 0.005s（negligible），所以 overhead 完全来自
      inference-time mixed-precision dequantization。需要在 paper 中承认 "current 
      implementation uses naive per-head dequantization; a fused kernel could eliminate 
      the overhead" 并标注为 engineering limitation, not fundamental。但 reviewer 会
      counter："without the optimized kernel, the practical benefit claim is weakened."
    tables:
      - caption: "Table: Runtime Benchmark (Qwen2.5-7B, seq_len=2048)"
        rows:
          - method: "BF16 (no quantization)"
            prefill_ms: 45.86
            decode_ms: 33.78
            throughput: 29.6
            memory_MB: 21
          - method: "Uniform 4-bit"
            prefill_ms: 54.25
            decode_ms: 42.46
            throughput: 23.6
            memory_MB: 5.25
          - method: "Constrained MCKP"
            prefill_ms: 57.03
            decode_ms: 46.09
            throughput: 21.8
            memory_MB: 5.25
    figures_description:
      - "Throughput vs memory tradeoff scatter plot：三种 method 的 Pareto 位置"
    analysis: >
      Median 档中这是 second major objection source。Runtime overhead 与 
      "practical implications" claim 冲突。Paper 需要 reframe："memory-bound 
      scenarios (long context, large batch) where 4× memory reduction enables 
      deployment that bf16 cannot." 8K context 实验（qwen7b_8k_context_eval: 
      uniform 77.75 vs MCKP 8.59）是 strongest counterargument——at long context, 
      memory savings dominate and quality gap amplifies dramatically。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d5d46df-46df-448c-9592-7668e30359e8",
  "isSidechain": false,
  "requestId": "req_011Cb5TC4VC54YYKJFwvBtNs",
  "type": "assistant",
  "uuid": "8f9fc777-fb26-40e1-8223-882f861be281",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SrCBBEQynMEp6pYnGRY9tr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 57827,
      "output_tokens": 14662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14662,
          "cache_read_input_tokens": 57827,
          "cache_creation_input_tokens": 3501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3501
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Compounding 发现和 constraint 有效性被认可，但 'universal' 语言和 diagnostic 的 claim 强度受到质疑；需要降低 claim 语气并补充实验 核心假设：['A1: compounding 被认可为有价值的实证发现，但 reviewer 指出 RateQu…",
  "leafUuid": "8f9fc777-fb26-40e1-8223-882f861be281",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze KV cache compounding effects and diagnostic thresholds",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Compounding 发现和 constraint 有效性被认可，但 'universal' 语言和 diagnostic 的 claim 强度受到质疑；需要降低 claim 语气并补充实验 核心假设：['A1: compounding 被认可为有价值的实证发现，但 reviewer 指出 RateQu…",
  "leafUuid": "8f9fc777-fb26-40e1-8223-882f861be281",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze KV cache compounding effects and diagnostic thresholds",
  "sessionId": "141b11e8-8b0e-437b-b7b1-f0f21e658ad9"
}
```

---
