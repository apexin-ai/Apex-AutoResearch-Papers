# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d.jsonl`
- **Structured JSON:** [`c957f826adfe98c1ef89.json`](../../sessions/c9/c957f826adfe98c1ef89.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T02:14:58.094Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T02:14:58.094Z",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: ratekv\nfocus: Evaluate the compounding-forward framing: core contribution is 2-bit compounding as universal failure mode + constraint as universal fix + \"non-uniform rarely helps\" as key negative result. N=1 Spread is a feature (7/8 don't need non-uniform) not a bug. Compare with concentration-dependent framing where N=1 was a weakness.\n\n## paper_framing.md\n\n# Paper Framing — ratekv\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)\n- Track: Efficient Methods for NLP\n\n## bf16 Consistency Resolution (2026-05-14)\n\n**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。\n\n**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。\n\n| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |\n|------|---------------------|----------------------|-----------|\n| Baseline | **9.8106** | 8.819 | 9.81 |\n| Uniform 4-bit | **15.4454** | — | 15.45 |\n| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |\n| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |\n\n## Core Insight\n\nPer-head KV cache quantization on hardware-aligned bit-widths {2,4,8,16} has an unreported universal failure mode: 2-bit quantization distortions compound non-additively through the residual stream, causing ALL tested unconstrained solvers (greedy, MCKP) to systematically over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 architectures (1.07×–3.31× baseline). A cardinality constraint (≤k heads at 2-bit) universally prevents this over-allocation, and furthermore reduces the feasible set to where solver choice becomes irrelevant (greedy = MCKP, Δ=0.0000). Under moderate compression (4×), only 1/8 architectures benefits from non-uniform allocation over uniform 4-bit — providing the first empirical evidence that the implicit assumption \"non-uniform is always better than uniform\" is wrong in KV cache quantization. The core contribution is the compounding effect discovery + universal constraint fix, not the allocation algorithm.\n\n## Core Claims (3 条)\n\n1. **2-bit compounding is a universal failure mode for unconstrained per-head allocation**: On hardware-aligned non-consecutive bit-widths {2,4,8,16}, per-head independent profiling distortions compound non-additively when multiple heads are simultaneously assigned 2-bit quantization. This causes ALL tested unconstrained solvers to over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 diverse architectures (Qwen 3.31×, Gemma-2 1.47×, Yi 1.08×, Llama 1.07×, Mistral 1.08×, Pythia, Qwen-14B, Phi-3-medium). Quantitative evidence of non-additivity: per-head profiling predicts joint PPL ≈11 but actual joint 2-bit PPL is 32–37 (3× prediction error). This is the first systematic characterization of compounding effects in per-head KV cache quantization. Long-context amplifies the failure: at 8K tokens, uniform 4-bit degrades 11.15× baseline while constrained MCKP degrades only 1.23× — a 9× gap in degradation rate.\n\n2. **A cardinality constraint is the universal fix — and makes solver choice irrelevant**: A simple cardinality constraint (max_2bit ≤ k) is sufficient to prevent compounding across ALL tested architectures. Three universally beneficial properties: (a) prevents catastrophic over-allocation on sensitive architectures (Qwen: 32.45 → 10.91), (b) prevents moderate over-allocation on flat architectures (Gemma-2: 8.85 → 6.17, reducing 2-bit heads from 106 to 8), (c) reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce IDENTICAL bit allocations and PPL (Δ=0.0000). The constraint is parameterizable via small-scale compounding test (k≤8 universally safe: <2.5% degradation across all architectures). Practical implication: practitioners need only add one integer parameter to existing pipelines.\n\n3. **Non-uniform allocation benefit is rare — most models should use uniform 4-bit**: Under moderate compression (4×), only 1/8 tested architectures (Qwen2.5-7B, \"spread\" sensitivity pattern) benefits from non-uniform allocation (+27.3% PPL, +1.9pp downstream avg). The remaining 7/8 show no benefit or minor degradation (<1pp avg downstream). A 2-metric empirical diagnostic (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly classifies all 9 tested models (9/9 accuracy), providing practitioners a simple check: if the diagnostic says \"no\" — skip profiling and use uniform 4-bit with zero quality loss. This is the first systematic study of *when* non-uniform KV cache quantization is beneficial, correcting the implicit assumption that it always helps.\n\n## Story Spine\n\n- **Problem**: Per-head mixed-precision KV cache quantization promises better quality-compression tradeoffs than uniform bit-width. But on hardware-aligned non-consecutive bit-widths {2,4,8,16}, we discover that existing allocation algorithms (greedy, MCKP) systematically FAIL — producing worse results than naive uniform 4-bit across ALL tested architectures. The failure mode is unreported: 2-bit quantization distortions compound non-additively, and solvers consistently over-allocate 2-bit heads. Meanwhile, the field implicitly assumes non-uniform allocation always helps, but no systematic study has tested this across architectures.\n\n- **Existing approaches & gaps**: RateQuant provides R-D optimal per-head allocation via continuous closed-form and discrete greedy (optimal on consecutive integers {2,...,6}). KIVI and ARKV apply uniform or heuristic mixed-precision. However, on hardware-aligned {2,4,8,16}: (a) RateQuant's greedy produces PPL 32.45 vs optimal ~10.91 — polymatroid optimality breaks, (b) unconstrained MCKP fares even worse (PPL 36.92) due to compounding, (c) NO prior work addresses *when* non-uniform allocation is actually beneficial vs when uniform suffices.\n\n- **Our framing**: We present three contributions: (1) the first characterization of 2-bit compounding effects in per-head KV cache quantization — showing that profiling non-additivity causes ALL unconstrained solvers to fail on {2,4,8,16} across 8/8 architectures; (2) a simple universal fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding, makes solver choice irrelevant (greedy=MCKP, Δ=0.0000), and is safely parameterizable (k≤8 universally safe); (3) the first systematic study of *when* non-uniform allocation helps — answer: rarely (1/8 architectures at moderate compression), with a 2-metric diagnostic (9/9 correct) that tells practitioners whether to invest in profiling or just use uniform 4-bit.\n\n- **Headline result template**: \"We show that per-head KV cache quantization on hardware-aligned bit-widths has a universal failure mode: 2-bit distortions compound non-additively, causing ALL unconstrained solvers to underperform uniform 4-bit across 8 architectures. A cardinality constraint (≤k heads at 2-bit) universally fixes this, making solver choice irrelevant (greedy=MCKP, Δ=0.0000). Surprisingly, under moderate compression, only 1/8 architectures benefits from non-uniform allocation at all — most models should simply use uniform 4-bit. A 2-metric diagnostic (9/9 accuracy) provides practitioners a simple check to determine when profiling is worthwhile. At long context (8K tokens), the constraint reduces degradation from 11.15× to 1.23× baseline, demonstrating critical deployment value.\"\n\n## \"When Does Non-Uniform Allocation Help?\" — Analysis Chapter\n\nFive case studies representing the full spectrum of heterogeneity:\n\n| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |\n|------|-------|-----|--------------|------------------------------|---------------|\n| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; \"spread\" pattern (L0 cluster, 4 heads, 26× dominance) |\n| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; \"spike\" pattern (L4H3 single outlier, 64% of total delta) |\n| **Marginal** | Llama-3.1-8B | 4:1 | 0.57 (hires) | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |\n| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |\n| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |\n\n**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.\n\n**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).\n\n**Joint diagnostic** (n=8, 8/8 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike), CodeLlama (0.80, t₁/t₅=0.81 — spike), and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.\n\n## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)\n\n| Method | PPL | Bit Distribution | Budget |\n|--------|-----|-------------------|--------|\n| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |\n| MCKP unconstrained | 36.92 | — | 0.25 |\n| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |\n\nKey takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.\n\n## Cross-Architecture Evidence Summary\n\n| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |\n|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|\n| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |\n| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |\n| Llama-3.1-8B | 4:1 | 256 | **0.57** (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (t₁/t₅≈0.85, single dominant L2H5) | ≈ Marginal |\n| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |\n| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |\n\n**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:\n- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding\n- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta\n- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)\n- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads\n\n**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):\n\nThree-tier labeling (NOT binary catastrophe/benign):\n- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding\n- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions\n- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)\n\nReviewer-suggested paragraph for paper (1 段, 3-4 句):\n\"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\"\n\nThis **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.\n\n⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.\n\n**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.\n\n**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.\n\n### Mistral k Ablation (256 KV heads, budget=0.25)\n\nPPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).\n\n| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |\n|---|-----|-------|-------|-------|--------|-----|\n| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |\n| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |\n| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |\n| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |\n| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |\n| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |\n\nContrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.\n\n### Llama k Ablation (256 KV heads, budget=0.25)\n\nAll k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).\n\n### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)\n\n**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅\n\n| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |\n|------|---------------|------------|---|---------------|\n| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |\n| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |\n| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |\n| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |\n| **Avg recovery** | — | — | **72.8%** | — |\n\n**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.7946 | 0.7854 | -0.92pp |\n| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |\n| hellaswag | 0.5857 | 0.5797 | -0.60pp |\n| piqa | 0.7927 | 0.7894 | -0.33pp |\n| winogrande | 0.7174 | 0.7301 | +1.27pp |\n| **Average** | **0.6822** | **0.6745** | **-0.77pp** |\n\n**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.8173 | 0.8039 | -1.34pp |\n| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |\n| hellaswag | 0.6026 | 0.6012 | -0.14pp |\n| piqa | 0.7867 | 0.7802 | -0.65pp |\n| winogrande | 0.7253 | 0.7238 | -0.15pp |\n| **Average** | **0.6915** | **0.6816** | **-0.99pp** |\n\n**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=4) | Δ |\n|------|---------------|------------|---|\n| arc_easy | — | — | — |\n| arc_challenge | — | — | — |\n| hellaswag | — | — | — |\n| piqa | — | — | — |\n| winogrande | — | — | — |\n| **Average** | **0.6894** | **0.6846** | **-0.48pp** |\n\n**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)\n\n| Task | Uniform 4-bit | MCKP | Δ |\n|------|---------------|------|---|\n| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |\n\n**Downstream summary (Reviewer-verified framing)**:\n- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**\n- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)\n- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)\n- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise\n- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)\n- **Paper must**: (a) report full per-task tables, not just averages, (b) use \"shows minor degradation\" NOT \"preserves accuracy\" — the latter has spin, (c) note arc_challenge as worst-case explicitly\n- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance\n- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论：\"ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\"\n- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞：\"Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge).\"\n\n## Allocation Baseline Evidence (plan_015, mckp_reeval)\n\nAll numbers from unified bf16 eval pipeline, budget=0.25.\n\n| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |\n|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|\n| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |\n| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |\n| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |\n\n**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.\n\n**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.\n\n## Differentiation from RateQuant\n\n| Aspect | RateQuant | Ours |\n|--------|-----------|------|\n| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |\n| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |\n| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |\n| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |\n| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |\n| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |\n| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |\n\n## Venue Fit Risks\n\n- **\"The constraint is just a heuristic, not a real contribution\"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.\n- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.\n- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive \"higher GQA = more benefit\" hypothesis and shows our diagnostic is needed.\n- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 8/8 correct). The \"spike vs spread\" analysis explains WHY same-GQA models differ.\n- **Statistical power**: n=8 models is directional evidence, not statistical claim. Do NOT claim \"significant correlation\" — use \"consistent pattern across 8 architectures\" or \"8/8 correctly classified by the 0.50 threshold.\"\n- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.\n\n## Anticipated Reviewer Concerns\n\n1. **\"The cardinality constraint is trivial — just cap the extreme allocations\"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.\n2. **\"This is just RateQuant with a constraint added\"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.\n3. **\"The method only works on Qwen — isn't this a Qwen paper?\"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.\n4. **\"How does this work at different compression ratios?\"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.\n5. **\"n=3/4/5 models is not enough for the heterogeneity claim\"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.\n6. **\"RateQuant does K/V asymmetric allocation, do you?\"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.\n7. **\"Where are the downstream task results?\"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use \"shows minor degradation\" not \"preserves accuracy\".\n8. **\"The profiler distortion=0.0 on Mistral suggests the profiling method is broken\"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.\n9. **\"If solver doesn't matter, why present MCKP at all?\"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim:\n  - 2\n  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.\n    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.\n    Strengthens narrative: \"solver automatically discovers sensitivity structure.\"\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: exp_d_no_l0_exclusion\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_002\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).\n    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability\n    across different GQA ratios and architectures. Fallback if HF token unavailable:\n    Yi-1.5-9B (non-gated, similar scale).\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: llama_full_pipeline\n  model: Llama-3.1-8B\n  fallback_model: Yi-1.5-9B\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 8.7\n    uniform_4bit_ppl_bf16: 8.47\n    baseline_ppl_bf16: 8.09\n    delta_vs_uniform: -0.23\n    memory_ratio: 0.25\n- id: plan_003\n  claim:\n  - 1\n  - 2\n  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture\n    family to establish cross-architecture validity.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mistral_full_pipeline\n  model: Mistral-7B-v0.3\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 7.564\n    uniform_4bit_ppl_bf16: 7.131\n    baseline_ppl_bf16: 7.035\n    delta_vs_uniform: -0.433\n    memory_ratio: 0.25\n- id: plan_004\n  claim:\n  - 3\n  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112\n    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map\n    the compounding threshold. Establishes the principled basis for cardinality constraint\n    selection.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: compounding_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_005\n  claim:\n  - 2\n  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,\n    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline\n    at same budget.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: budget_sweep\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_006\n  claim:\n  - 1\n  - 2\n  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).\n    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers\n    mid-layer heterogeneity and improves solver allocation beyond current results.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_e_hires_profile\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    constrained_ppl_bf16: 9.569\n    baseline_ppl_bf16: 8.819\n    exp_c_ppl_bf16: 11.345\n    delta_vs_exp_c: -1.776\n    memory_ratio: 0.25\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    profile_resolution:\n      hires_nonzero_2bit: 100\n      lowres_nonzero_2bit: 37\n      hires_nonzero_4bit: 6\n      lowres_nonzero_4bit: 4\n      total_heads: 112\n    allocation_diff_count: 8\n    profiling_time_min: 65.5\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.\n    Cross-dataset evaluation to show results are not WikiText-2 specific.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  eval: C4\n  status: DONE\n  conclusion: success\n  metrics: &id001\n    c4_cal_wt2_eval_mckp_ppl: 11.2942\n    c4_cal_wt2_eval_uniform_ppl: 15.4454\n    c4_cal_wt2_eval_delta: 4.1512\n    c4_cal_bf16_baseline: 12.6505\n    wt2_bf16_baseline: 9.8106\n    allocation_agreement_c4_vs_wt2: 0.964\n    agreement_heads: 108/112\n    bit_dist: 2bit:8, 4bit:100, 8bit:4\n    cross_domain_wt2_to_c4_mckp_ppl: 20.5601\n    cross_domain_wt2_to_c4_uniform_ppl: 35.4232\n    cross_domain_c4_bf16: 15.3246\n    old_contaminated_ppl: 11.3285\n    contamination_impact: 0.0343\n    models_completed: Qwen2.5-7B only\n- id: plan_008\n  claim:\n  - 2\n  description: 'RateQuant comparison: implement RateQuant''s greedy algorithm (Algorithm\n    1) on our discrete action set {2,4,8,16}-bit. RateQuant''s Prop. 6 optimality\n    relies on consecutive-integer polymatroid structure which breaks on non-consecutive\n    sets. Show greedy produces suboptimal allocation vs constrained MCKP. Critical\n    for differentiation claim — must have experimental evidence.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: ratequant_greedy_comparison\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n- id: plan_009\n  claim:\n  - 2\n  description: 'Oracle comparison: brute-force optimal allocation on a subset (3-4\n    layer groups) of Qwen2.5-7B. Quantify MCKP gap to oracle.\n\n    '\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_006\n  registry_id: oracle_comparison\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_ppl: 10.9131\n    max_oracle_gap_ppl: 0.0183\n    avg_oracle_gap_ppl: 0.0046\n    layers_mckp_optimal: 5/8\n    layers_with_gap: 3\n    gap_layers:\n      L1: 0.0183\n      L4: 0.0045\n      L11: 0.0136\n    gap_nature: 2-bit head position swap within same bit budget\n    total_evals: 54\n    runtime_min: 21.3\n- id: plan_010\n  claim:\n  - 2\n  description: 'Cross-domain calibration robustness: calibrate on C4, evaluate on\n    WikiText-2 (and vice versa). Report per-head allocation agreement rate across\n    calibration sources.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_007\n  registry_id: c4_rerun_d032\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: plan_011\n  claim:\n  - 1\n  description: 'Head sensitivity visualization: generate paper-quality figures showing\n    per-head profiling delta heatmap across layers, compounding effect curve, and\n    budget allocation comparison chart.\n\n    '\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_004\n  - plan_006\n  registry_id: head_sensitivity_viz\n  status: DONE\n  conclusion: success\n- id: plan_014\n  claim:\n  - 2\n  description: 'K/V separation: treat K and V heads as independent MCKP items with\n    separate budget allocation. Compare joint K+V optimization vs current uniform\n    K=V approach. RateQuant supports asymmetric K/V (e.g. K=2.85, V=2.15 avg bits)\n    — we should show MCKP naturally handles this.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: kv_separation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: negative\n  metrics:\n    kv_sep_ppl: 11.2162\n    joint_kv_ppl: 10.9131\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_sep_vs_joint: 0.303\n    sep_k_2bit_count: 16\n    sep_v_uniform_4bit: true\n    kv_asymmetric_heads: 21\n- id: plan_012\n  claim:\n  - 1\n  - 2\n  description: 'Downstream task evaluation: ARC-C / HellaSwag / PIQA / WinoGrande\n    on Qwen2.5-7B at 4× compression. Must match RateQuant''s eval suite for direct\n    comparison. Tests whether PPL improvements translate to downstream performance.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  registry_id: downstream_eval_qwen\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    avg_recovery: 0.728\n    arc_c: 0.5137\n    hellaswag: 0.7684\n    piqa: 0.7786\n    winogrande: 0.6819\n    arc_c_delta_pp: 3.16\n    hellaswag_delta_pp: 4\n    piqa_delta_pp: 1.25\n    winogrande_delta_pp: 1.97\n- id: plan_013\n  claim:\n  - 1\n  description: '70B profiling-only: run distortion profiling on Qwen2.5-72B (no full\n    eval). Analyze whether sensitivity patterns (Layer 0 dominance, compounding threshold)\n    scale with model size.\n\n    '\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: qwen72b_profiling\n  model: Qwen2.5-72B\n  status: DONE\n  conclusion: killed\n- id: plan_015\n  claim:\n  - 2\n  description: 'L0-only heuristic baseline: assign 8-bit to all Layer 0 KV heads,\n    uniform 4-bit to all other heads, at 4x compression on Qwen2.5-7B. This is the\n    simplest possible non-uniform strategy exploiting L0 sensitivity. If L0-only matches\n    or beats constrained MCKP, the full optimization machinery is unnecessary. Must\n    also test on Llama and Mistral. Critical missing baseline flagged by Dream review.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: l0_only_heuristic\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: killed\n- id: plan_016\n  claim:\n  - 2\n  description: 'RateQuant greedy + cardinality constraint ablation: add max_2bit=k\n    constraint to RateQuant greedy Algorithm 1 on {2,4,8,16}. Compare three conditions:\n    (a) RateQuant greedy unconstrained (already have: PPL ~32.45), (b) RateQuant greedy\n    + cardinality k=8, (c) constrained MCKP k=8 (already have: PPL ~11.23). If (b)\n    matches (c), the contribution is the cardinality constraint, not the MCKP solver.\n    If (c) beats (b), discrete MCKP optimization genuinely matters. Critical ablation\n    flagged by all three Dream review tiers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_008\n  registry_id: greedy_cardinality_ablation\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 11.2312\n    greedy_unconstrained_ppl: 32.4467\n    mckp_constrained_ppl: 11.23\n    delta_vs_mckp: 0.0012\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n- id: plan_017\n  claim:\n  - 1\n  - 2\n  description: 'Multi-seed error bars: run constrained MCKP and uniform 4-bit on Qwen2.5-7B\n    at 4x compression with 3 different calibration sets (different random subsets\n    of WikiText-2 training data). Report mean +/- std for PPL. Required for statistical\n    credibility — Dream review flagged all-single-run as critical gap.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: multi_seed_error_bars\n  model: Qwen2.5-7B\n  eval: WikiText-2\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4454\n    mckp_seed0: 11.0168\n    mckp_seed1: 10.8981\n    mckp_seed2: 11.0487\n    mckp_mean: 10.9878\n    mckp_std: 0.0648\n    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4\n    allocation_agreement_3way: 0.902\n    agreement_s0_s1: 0.946\n    agreement_s0_s2: 0.911\n    agreement_s1_s2: 0.946\n    profile_time_min_per_seed: 65\n- id: plan_018\n  claim:\n  - 2\n  description: 'Runtime/latency benchmark: measure end-to-end inference latency and\n    throughput with mixed-precision KV cache vs uniform 4-bit quantization on Qwen2.5-7B.\n    Include profiling cost breakdown. Dream review flagged missing latency evaluation\n    as significant gap for systems-oriented contribution.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: runtime_benchmark\n  model: Qwen2.5-7B\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16:\n      prefill_ms: 45.86\n      decode_ms_per_tok: 33.78\n      throughput_tok_s: 29.6\n    uniform_4bit:\n      prefill_ms: 54.25\n      decode_ms_per_tok: 42.46\n      throughput_tok_s: 23.6\n    constrained_mckp:\n      prefill_ms: 57.03\n      decode_ms_per_tok: 46.09\n      throughput_tok_s: 21.8\n      mckp_solver_sec: 0.005\n      bit_dist:\n        '2': 8\n        '4': 100\n        '8': 4\n      memory_ratio: 0.25\n    theoretical_memory:\n      bf16_MB: 21\n      4bit_MB: 5.25\n      mckp_MB: 5.25\n      compression_4x: true\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sanity_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp_004\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p0_2_cliff_1.5B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: p0_2_cliff_7B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: p0_1_ppl_fast\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_a_targeted_hybrid\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_b_hires_quant\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_c_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_c_no2bit\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl: 15.4454\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_vs_uniform: 0\n    memory_ratio: 0.25\n    bit_distribution:\n      '4': 112\n- exp_id: exp_d_no_l0_exclusion\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_e_hires_profile\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    constrained_ppl_bf16: 9.569\n    baseline_ppl_bf16: 8.819\n    exp_c_ppl_bf16: 11.345\n    delta_vs_exp_c: -1.776\n    memory_ratio: 0.25\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    profile_resolution:\n      hires_nonzero_2bit: 100\n      lowres_nonzero_2bit: 37\n      hires_nonzero_4bit: 6\n      lowres_nonzero_4bit: 4\n      total_heads: 112\n    allocation_diff_count: 8\n    profiling_time_min: 65.5\n- exp_id: compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: compounding_sweep_k10_12\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: ratequant_greedy_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: budget_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: c4_cross_dataset_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    c4_mckp_ppl: 11.3285\n    uniform4bit_ppl: 15.4454\n    delta_over_uniform: 4.117\n    allocation_agreement_rate: 0.982\n    n_disagree: 2\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n    wt2_ref_mckp_ppl: 11.2312\n    wt2_ref_delta: 4.2142\n    ppl_gap: 0.097\n- exp_id: llama_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 8.7\n    uniform_4bit_ppl_bf16: 8.47\n    baseline_ppl_bf16: 8.09\n    delta_vs_uniform: -0.23\n    memory_ratio: 0.25\n- exp_id: mistral_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl_bf16: 7.564\n    uniform_4bit_ppl_bf16: 7.131\n    baseline_ppl_bf16: 7.035\n    delta_vs_uniform: -0.433\n    memory_ratio: 0.25\n- exp_id: llama_hires_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 8.0918\n    uniform_4bit_ppl: 8.469\n    lowres_mckp_ppl: 8.6951\n    hires_mckp_ppl: 8.4498\n    hires_improvement_ppl: 0.2453\n    degradation_reduction_pct: 40.7\n    profiling_time_min: 173.4\n    total_time_min: 175.1\n- exp_id: mistral_hires_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mckp_ppl: 7.323\n    uniform_4bit_ppl: 7.131\n    baseline_ppl: 7.035\n    delta_vs_uniform: -0.192\n    memory_ratio: 0.25\n- exp_id: llama_aggressive_compression\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_5.3x_ppl: 57.6\n    uniform_2bit_ppl: 2643.77\n    mckp_8x_ppl: 2372.33\n    uniform_2bit_8x_ppl: 2643.77\n- exp_id: downstream_eval_qwen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    avg_recovery: 0.728\n    arc_c: 0.5137\n    hellaswag: 0.7684\n    piqa: 0.7786\n    winogrande: 0.6819\n    arc_c_delta_pp: 3.16\n    hellaswag_delta_pp: 4\n    piqa_delta_pp: 1.25\n    winogrande_delta_pp: 1.97\n- exp_id: head_sensitivity_viz\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mistral_aggressive_compression\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_5.3x_ppl: 11.912\n    uniform_2bit_ppl: 519.107\n    mckp_8x_ppl: 399.901\n    uniform_2bit_8x_ppl: 519.107\n    baseline_ppl: 7.035\n    uniform_4bit_ppl: 7.131\n    5.3x_bit_dist:\n      '2': 128\n      '4': 128\n    8x_bit_dist:\n      '2': 248\n      '4': 8\n    total_time_seconds: 268.1\n- exp_id: kv_separation\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    kv_sep_ppl: 11.2162\n    joint_kv_ppl: 10.9131\n    uniform_4bit_ppl: 15.4454\n    baseline_ppl: 9.8106\n    delta_sep_vs_joint: 0.303\n    sep_k_2bit_count: 16\n    sep_v_uniform_4bit: true\n    kv_asymmetric_heads: 21\n- exp_id: l0_only_heuristic\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: greedy_cardinality_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 11.2312\n    greedy_unconstrained_ppl: 32.4467\n    mckp_constrained_ppl: 11.23\n    delta_vs_mckp: 0.0012\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    memory_ratio: 0.25\n- exp_id: l0_heuristic_baseline\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: greedy_constrained_ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: l0_heuristic_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_constrained_ppl: 11.23\n    l0_random_mean_ppl: 11.69\n    l0_random_std: 0.47\n    naive_positional_ppl: 12.23\n    uniform_4bit_ppl: 15.45\n    qwen_l0_random_median: 11.515\n    qwen_l0_random_seeds:\n    - 11.486\n    - 11.615\n    - 11.325\n    - 11.515\n    - 12.515\n    llama_l0_random_mean: 10.479\n    llama_l0_random_std: 1.033\n    llama_l0_random_median: 10.038\n    llama_l0_random_seeds:\n    - 9.485\n    - 10.488\n    - 9.941\n    - 10.038\n    - 12.444\n    llama_naive_positional: 9.941\n    llama_mckp: 8.4498\n    llama_uniform: 8.469\n    mistral_l0_random_mean: 7.56\n    mistral_l0_random_std: 0.087\n    mistral_l0_random_median: 7.586\n    mistral_l0_random_seeds:\n    - 7.523\n    - 7.61\n    - 7.413\n    - 7.586\n    - 7.669\n    mistral_naive_positional: 7.481\n    mistral_mckp: 7.3106\n    mistral_uniform: 7.131\n- exp_id: qwen_bf16_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 9.8106\n    baseline_fp16_ppl: 9.81\n    delta_baseline: 0.0006\n    uniform4_bf16_ppl: 15.4454\n    uniform4_fp16_ppl: 15.45\n    delta_uniform4: 0.0046\n- exp_id: hires_mckp_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl_bf16: 9.8106\n    mckp_ppl_bf16: 10.9131\n    uniform_4bit_ppl_bf16: 15.4454\n    delta_mckp_vs_baseline: 1.1025\n    delta_mckp_vs_uniform: -4.5323\n    token_count: 298938\n- exp_id: hires_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 9.8106\n    uniform_4bit_bf16_ppl: 15.4454\n    hires_mckp_bf16_ppl: 10.9131\n- exp_id: mistral_k_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 4\n    best_ppl: 7.1648\n    uniform_4bit_ppl: 7.131\n    k4_ppl: 7.1648\n    k8_ppl: 7.1997\n    k12_ppl: 7.2448\n    k16_ppl: 7.3106\n    k18_ppl: 7.3231\n- exp_id: llama_k_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 4\n    best_ppl: 8.4498\n    uniform_4bit_ppl: 8.469\n    k4_ppl: 8.4498\n    k8_ppl: 8.4498\n    k12_ppl: 8.4498\n    k16_ppl: 8.4498\n    k18_ppl: 8.4498\n    natural_2bit_count: 2\n- exp_id: multi_seed_error_bars\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4454\n    mckp_seed0: 11.0168\n    mckp_seed1: 10.8981\n    mckp_seed2: 11.0487\n    mckp_mean: 10.9878\n    mckp_std: 0.0648\n    bit_dist_all_seeds: 2bit:8, 4bit:100, 8bit:4\n    allocation_agreement_3way: 0.902\n    agreement_s0_s1: 0.946\n    agreement_s0_s2: 0.911\n    agreement_s1_s2: 0.946\n    profile_time_min_per_seed: 65\n- exp_id: cross_domain_calibration\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c4_cross_dataset_eval_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cross_domain_calibration_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: runtime_benchmark\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16:\n      prefill_ms: 45.86\n      decode_ms_per_tok: 33.78\n      throughput_tok_s: 29.6\n    uniform_4bit:\n      prefill_ms: 54.25\n      decode_ms_per_tok: 42.46\n      throughput_tok_s: 23.6\n    constrained_mckp:\n      prefill_ms: 57.03\n      decode_ms_per_tok: 46.09\n      throughput_tok_s: 21.8\n      mckp_solver_sec: 0.005\n      bit_dist:\n        '2': 8\n        '4': 100\n        '8': 4\n      memory_ratio: 0.25\n    theoretical_memory:\n      bf16_MB: 21\n      4bit_MB: 5.25\n      mckp_MB: 5.25\n      compression_4x: true\n- exp_id: c4_rerun_d032\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_cal_wt2_eval_mckp_ppl: 11.2942\n    c4_cal_wt2_eval_uniform_ppl: 15.4454\n    c4_cal_wt2_eval_delta: 4.1512\n    c4_cal_bf16_baseline: 12.6505\n    wt2_bf16_baseline: 9.8106\n    allocation_agreement_c4_vs_wt2: 0.964\n    agreement_heads: 108/112\n    bit_dist: 2bit:8, 4bit:100, 8bit:4\n    cross_domain_wt2_to_c4_mckp_ppl: 20.5601\n    cross_domain_wt2_to_c4_uniform_ppl: 35.4232\n    cross_domain_c4_bf16: 15.3246\n    old_contaminated_ppl: 11.3285\n    contamination_impact: 0.0343\n    models_completed: Qwen2.5-7B only\n- exp_id: multi_seed_lowres\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: oracle_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mckp_ppl: 10.9131\n    max_oracle_gap_ppl: 0.0183\n    avg_oracle_gap_ppl: 0.0046\n    layers_mckp_optimal: 5/8\n    layers_with_gap: 3\n    gap_layers:\n      L1: 0.0183\n      L4: 0.0045\n      L11: 0.0136\n    gap_nature: 2-bit head position swap within same bit budget\n    total_evals: 54\n    runtime_min: 21.3\n- exp_id: plan_009_oracle_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: qwen72b_profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: llama_heuristic_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    l0_random_seeds:\n    - 8.5479\n    - 8.7595\n    - 8.624\n    - 8.5721\n    - 8.6192\n    l0_random_mean: 8.6245\n    l0_random_std: 0.0733\n    l0_random_median: 8.6192\n    naive_positional_ppl: 8.5781\n    mckp_ppl: 8.4498\n    uniform_ppl: 8.469\n    baseline_ppl: 8.0918\n    mckp_vs_l0_random_gap: 0.1747\n    mckp_vs_naive_gap: 0.1283\n- exp_id: mistral_heuristic_k4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_bf16_ppl: 7.0351\n    uniform_4bit_ppl: 7.1314\n    mckp_k4_ppl: 7.1648\n    l0_random_seed_0: 7.1882\n    l0_random_seed_1: 7.1995\n    l0_random_seed_2: 7.1723\n    l0_random_seed_3: 7.3577\n    l0_random_seed_4: 7.2875\n    l0_random_mean: 7.2411\n    l0_random_std: 0.0707\n    l0_random_median: 7.1995\n    naive_heuristic_ppl: 7.2105\n    budget_heuristic: 0.2559\n    budget_mckp_k4: 0.248\n- exp_id: llama_c4_cross_dataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wt2_cal_wt2_ppl: 8.4498\n    c4_cal_wt2_ppl: 8.6459\n    uniform_wt2_ppl: 8.469\n    wt2_cal_c4_ppl: 7.654\n    c4_cal_c4_ppl: 7.654\n    uniform_c4_ppl: 7.5351\n    bf16_wt2_ppl: 8.0918\n    bf16_c4_ppl: 7.1333\n    agreement_rate: 0.977\n    agreement_heads: 250/256\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n- exp_id: mistral_c4_cross_dataset\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bf16_wt2_ppl: 7.0351\n    c4_cal_bf16_ppl: 6.9677\n    wt2_cal_mckp_wt2_ppl: 7.1648\n    c4_cal_mckp_wt2_ppl: 7.1859\n    uniform_4bit_wt2_ppl: 7.1314\n    delta_uniform_mckp_wt2_cal: -0.0334\n    delta_uniform_mckp_c4_cal: -0.0546\n    allocation_agreement_c4_vs_wt2: 0.965\n    agreement_heads: 247/256\n    bit_dist_wt2_cal: 2bit:4, 4bit:252\n    bit_dist_c4_cal: 2bit:4, 4bit:251, 8bit:1\n    profile_time_s: 407.7\n    eval_time_s: 349.4\n    total_time_s: 757.1\n- exp_id: gemma2_9b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 8.9\n    mckp_wikitext2_ppl: 9.05\n    uniform4bit_wikitext2_ppl: 9.03\n    mckp_improvement_over_uniform: -0.02\n    top5_concentration: 0.23\n    layer0_dominance_ratio: 1.32\n    best_k: 8\n    best_k_ppl: 9.05\n    verdict: FAIL\n- exp_id: yi15_9b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 7.0157\n    mckp_wikitext2_ppl: 7.3129\n    uniform4bit_wikitext2_ppl: 7.2171\n    mckp_improvement_over_uniform: -0.0958\n    top5_concentration: 0.4934\n    layer0_dominance_ratio: 0.07\n    best_k: 2\n    best_k_ppl: 7.2209\n    gqa_ratio: '8:1'\n    verdict: FAIL\n- exp_id: qwen25-hires-profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_hires_float32_d048\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    float32_hires_top5_concentration: 0.6104\n    bf16_hires_range: 0.59-0.66\n    float32_lowres_concentration: 0.42\n    bf16_bug_impact_on_concentration: 0.01\n    baseline_ppl: 9.81\n    mckp_unconstrained_ppl: 10.95\n    uniform_4bit_ppl: 15.45\n    mckp_bit_dist:\n      '2': 12\n      '4': 96\n      '8': 3\n      '16': 1\n    l0h0_delta: 6.7388\n    l0_4heads_total_share: 0.586\n    claim3_threshold_0.50: PASS\n- exp_id: yi15_hires_float32_profiling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: yi15_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.7139\n    top5_n_heads: 9\n    baseline_calibration_ppl: 5.888\n    delta_2bit_cv: 8.8991\n    layer0_dominance_ratio: 0.04\n    top1_head: L4H3_delta=13.1236\n    total_hours: 0.96\n- exp_id: qwen_hires_constrained_d049\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    float32_hires_constrained_mckp_ppl: 10.8921\n    baseline_ppl: 9.8106\n    uniform_4bit_ppl: 15.4484\n    bit_distribution:\n      '2': 8\n      '4': 100\n      '8': 4\n    gap_recovery_pct: 80.8\n    top5_concentration: 0.6156\n    top5_concentration_pre_monotonicity: 0.6104\n    bf16_hires_constrained_mckp_ppl: 10.9131\n    delta_f32_vs_bf16: 0.021\n- exp_id: yi15_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hires_mckp_ppl: 7.2181\n    uniform_4bit_ppl: 7.2171\n    baseline_ppl: 7.0157\n    delta_vs_uniform: -0.001\n    bit_distribution:\n      '2': 2\n      '4': 189\n      '8': 1\n    2bit_heads:\n    - L22H1\n    - L24H3\n    8bit_heads:\n    - L6H2\n    L4H3_status: kept_at_4bit\n    std_mckp_k2_ppl: 7.2209\n    std_mckp_k8_ppl: 7.3129\n    hires_concentration: 0.7139\n    L4H3_2bit_delta: 13.12\n    L4H3_4bit_delta: 0.0048\n    L4H3_8bit_delta: 0.004\n- exp_id: llama_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.5749\n    t1_t5: 0.85\n    baseline_ppl: 6.5055\n    top1_head: L2H5_delta=15.2636\n    delta_2bit_cv: 7.7663\n    l0_dominance_ratio: 0.67\n    positive_delta_heads: 254\n    total_heads: 256\n    total_hours: 0.98\n- exp_id: mistral_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: 'ValueError: Unrecognized model - config.json missing model_type field\n      at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3'\n- exp_id: mistral_hires_bf16_2bitonly_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: 'SafetensorError: model-00003-of-00003.safetensors missing, incomplete\n      download'\n- exp_id: mistral_hires_bf16_2bitonly_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mistral_hires_bf16_2bitonly_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.241\n    top5_n_heads: 12\n    baseline_ppl: 5.8702\n    top1_head: L2H5\n    top1_delta_2bit: 0.3236\n    top2_head: L12H1\n    top2_delta_2bit: 0.1435\n    top3_head: L0H7\n    top3_delta_2bit: 0.1403\n    delta_2bit_mean: 0.020073\n    delta_2bit_std: 0.026278\n    delta_2bit_cv: 1.3091\n    layer0_mean_delta_2bit: 0.034073\n    other_layers_mean_delta_2bit: 0.019621\n    l0_dominance_ratio: 1.74\n    positive_delta_heads: 252\n    total_heads: 256\n    distribution_shape: flat\n    total_hours: 0.94\n    profile_seconds: 3371.7\n- exp_id: llama_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_bf16_ppl: 8.0922\n    hires_mckp_ppl: 8.5042\n    uniform_4bit_ppl: 8.4701\n    std_mckp_reference_ppl: 8.4498\n    mckp_vs_uniform_delta: -0.0341\n    mckp_vs_uniform_pct: -9\n    hires_vs_std_mckp_delta: 0.0544\n    concentration: 0.5749\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n    heads_2bit:\n    - 26,0\n    - 31,7\n    heads_8bit:\n    - 12,3\n    verdict: FAIL\n- exp_id: gemma2_hires_bf16_2bitonly\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    concentration_top5pct: 0.2291\n    l0_dominance_ratio: 2.05\n    cv_delta_2bit: 1.2834\n    positive_delta_heads: 310/336\n    top_head: L0H1 delta=0.1906\n    total_time_hours: 1.59\n- exp_id: llama_c4_hires_crossdataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_wt2_ppl: 8.0922\n    bf16_c4_ppl: 7.1333\n    c4_cal_mckp_wt2_ppl: 8.5103\n    c4_cal_mckp_c4_ppl: 7.5351\n    uniform_wt2_ppl: 8.4701\n    uniform_c4_ppl: 7.5351\n    delta_c4_uniform_minus_mckp: 0\n    delta_wt2_uniform_minus_mckp: -0.0402\n    verdict_c4: FAIL\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n    heads_2bit:\n    - 2,3\n    - 24,2\n    heads_8bit:\n    - 31,6\n    total_time_min: 6.3\n    wt2_ref_mckp_ppl: 8.5042\n    wt2_ref_delta: -0.0341\n- exp_id: mistral_c4_hires_crossdataset\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fp16_ppl: 7.0352\n    c4_mckp_ppl: 7.1774\n    uniform_4bit_ppl: 7.1308\n    mckp_vs_uniform_delta: 0.0466\n    mckp_bit_distribution:\n      '2': 4\n      '4': 250\n      '8': 2\n    phase4_error: 'FileNotFoundError: mistral_k_ablation_results.json'\n- exp_id: w2_unconstrained_baselines\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    note: 2bitonly profiles only - INVALID for reviewer response\n    yi15_ppl: 672.2\n    yi15_ratio: 114\n    llama_ppl: 1219.7\n    llama_ratio: 187\n    mistral_ppl_2bitonly: 47.8\n    mistral_ratio_2bitonly: 8.2\n    mistral_ppl_full: 6.39\n    mistral_ratio_full: 1.09\n    gemma2_ppl: 277.4\n    gemma2_ratio: 37.9\n    budget: 0.25\n    baseline_yi: 5.89\n    baseline_llama: 6.51\n    baseline_mistral: 5.87\n    baseline_gemma2: 7.32\n- exp_id: w9_compounding_scaling\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    baseline_ppl: 8.2\n    n1_joint_ppl: 14.94\n    n1_ratio: 1\n    n2_joint_ppl: 42.26\n    n2_ratio: 3.84\n    n4_joint_ppl: 3813.76\n    n4_ratio: 333.3\n    n8_joint_ppl: 3586.42\n    n8_ratio: 282.1\n    n16_joint_ppl: 7286.23\n    n16_ratio: 521.1\n    n32_joint_ppl: 6644.05\n    n32_ratio: 424\n    n64_joint_ppl: 9453.33\n    n64_ratio: 533.3\n    runtime_seconds: 96\n- exp_id: w9_compounding_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 9.81\n    k1_topk_ppl: 9.826\n    k1_randomk_ppl: 9.887\n    k1_randomk_std: 0.05\n    k4_topk_ppl: 9.849\n    k4_topk_ratio: 0.86\n    k4_randomk_ppl: 10.06\n    k4_randomk_std: 0.06\n    k4_randomk_ratio: 1.24\n    k8_topk_ppl: 10.042\n    k8_topk_ratio: 1.56\n    k8_randomk_ppl: 11.07\n    k8_randomk_std: 0.69\n    k8_randomk_ratio: 1.76\n    k16_topk_ppl: 10.42\n    k16_topk_ratio: 1.56\n    k16_randomk_ppl: 12.91\n    k16_randomk_std: 0.4\n    k16_randomk_ratio: 2.1\n    k32_topk_ppl: 11.604\n    k32_topk_ratio: 1.78\n    k32_randomk_ppl: 18.33\n    k32_randomk_std: 2.53\n    k32_randomk_ratio: 2.73\n    k64_topk_ppl: 22.946\n    k64_topk_ratio: 4.89\n    k64_randomk_ppl: 55.94\n    k64_randomk_std: 9.73\n    k64_randomk_ratio: 8.88\n    runtime_minutes: 16.9\n    note: 'v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking,\n      top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。'\n- exp_id: w2_unconstrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi15_baseline: 7.0157\n    yi15_uniform4: 7.2171\n    yi15_greedy: 7.5615\n    yi15_mckp: 7.5615\n    yi15_n2bit: 22\n    llama_baseline: 8.0922\n    llama_uniform4: 8.4701\n    llama_greedy: 8.6265\n    llama_mckp: 8.6265\n    llama_n2bit: 12\n    mistral_baseline: 7.0352\n    mistral_uniform4: 7.1308\n    mistral_greedy: 7.5733\n    mistral_mckp: 7.5963\n    mistral_n2bit: 42\n    gemma2_baseline: 6.0306\n    gemma2_uniform4: 6.1683\n    gemma2_greedy: 8.8469\n    gemma2_mckp: 8.8469\n    gemma2_n2bit: 106\n    gemma2_eval_method: sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\n    gemma2_greedy_ratio: 1.467\n    gemma2_catastrophic: true\n    gemma2_note: 1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal\n      value\n- exp_id: w3_downstream_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi15_baseline_avg: 0.6912\n    yi15_uniform_avg: 0.6822\n    yi15_mckp_avg: 0.6745\n    yi15_mckp_vs_uniform_pp: -0.77\n    yi15_mckp_vs_baseline_pp: -1.67\n    yi15_baseline:\n      arc_easy: 0.8093\n      arc_challenge: 0.5265\n      hellaswag: 0.5913\n      piqa: 0.7949\n      winogrande: 0.734\n    yi15_uniform:\n      arc_easy: 0.7946\n      arc_challenge: 0.5205\n      hellaswag: 0.5857\n      piqa: 0.7927\n      winogrande: 0.7174\n    yi15_mckp:\n      arc_easy: 0.7854\n      arc_challenge: 0.4881\n      hellaswag: 0.5797\n      piqa: 0.7894\n      winogrande: 0.7301\n    llama_baseline_avg: 0.696\n    llama_uniform_avg: 0.6915\n    llama_mckp_avg: 0.6816\n    llama_mckp_vs_uniform_pp: -0.99\n    llama_mckp_vs_baseline_pp: -1.44\n    llama_baseline:\n      arc_easy: 0.8228\n      arc_challenge: 0.5188\n      hellaswag: 0.6073\n      piqa: 0.7922\n      winogrande: 0.7388\n    llama_uniform:\n      arc_easy: 0.8173\n      arc_challenge: 0.5256\n      hellaswag: 0.6026\n      piqa: 0.7867\n      winogrande: 0.7253\n    llama_mckp:\n      arc_easy: 0.8039\n      arc_challenge: 0.4991\n      hellaswag: 0.6012\n      piqa: 0.7802\n      winogrande: 0.7238\n    mistral_baseline_avg: 0.6917\n    mistral_uniform_avg: 0.6894\n    mistral_mckp_avg: 0.6846\n    mistral_mckp_vs_uniform_pp: -0.48\n    mistral_mckp_vs_baseline_pp: -0.71\n    mistral_baseline:\n      arc_easy: 0.8005\n      arc_challenge: 0.5043\n      hellaswag: 0.6118\n      piqa: 0.8009\n      winogrande: 0.7411\n    mistral_uniform:\n      arc_easy: 0.7976\n      arc_challenge: 0.5068\n      hellaswag: 0.6051\n      piqa: 0.7982\n      winogrande: 0.7395\n    mistral_mckp:\n      arc_easy: 0.7942\n      arc_challenge: 0.4949\n      hellaswag: 0.6027\n      piqa: 0.802\n      winogrande: 0.7293\n    gemma2_baseline_avg: 0.7307\n    gemma2_uniform_avg: 0.7251\n    gemma2_mckp_avg: 0.7265\n    gemma2_mckp_vs_uniform_pp: 0.14\n    gemma2_mckp_vs_baseline_pp: -0.42\n    gemma2_baseline:\n      arc_easy: 0.8737\n      arc_challenge: 0.6135\n      hellaswag: 0.6093\n      piqa: 0.8128\n      winogrande: 0.7443\n    gemma2_uniform:\n      arc_easy: 0.8662\n      arc_challenge: 0.6058\n      hellaswag: 0.606\n      piqa: 0.8079\n      winogrande: 0.7395\n    gemma2_mckp:\n      arc_easy: 0.8649\n      arc_challenge: 0.6041\n      hellaswag: 0.6089\n      piqa: 0.8074\n      winogrande: 0.7474\n    eval_harness_version: 0.4.11\n    num_fewshot: 0\n    yi_elapsed_s: 1563.2\n    llama_elapsed_s: 1446.4\n    mistral_elapsed_s: 1302.2\n    gemma2_elapsed_s: 1735.9\n- exp_id: gemma2_constrained_bos_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 6.0306\n    uniform_4bit_ppl: 6.1683\n    constrained_mckp_ppl: 6.1951\n    mckp_vs_uniform_delta: 0.0267\n    mckp_delta_ppl: 0.1645\n    uniform_delta_ppl: 0.1377\n    bit_distribution:\n      '2': 8\n      '4': 324\n      '8': 4\n    n_2bit: 8\n    max_2bit: 8\n    memory_ratio: 0.25\n    eval_method: sliding_window_bos_fix\n    elapsed_seconds: 490.3\n- exp_id: w1_qwen14b_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 5.8432\n    concentration: 0.3312\n    t1_t5: 0.68\n    shape: Flat\n    l0_dominance: 15.5\n    cv: 3.7418\n    positive_heads: 370\n    total_heads: 384\n    top10_heads:\n    - head: L0H5\n      delta: 1.84494\n    - head: L0H4\n      delta: 0.236669\n    - head: L0H2\n      delta: 0.136971\n    - head: L28H4\n      delta: 0.099279\n    - head: L28H5\n      delta: 0.07576\n    - head: L27H4\n      delta: 0.071269\n    - head: L0H0\n      delta: 0.070018\n    - head: L28H6\n      delta: 0.063737\n    - head: L26H0\n      delta: 0.061462\n    - head: L31H3\n      delta: 0.061062\n    elapsed_min: 161.3\n    note: 't1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio'\n- exp_id: w1_pythia14b_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 13.6347\n    concentration: 0.2439\n    t1_t5: 0.28\n    shape: Flat\n    l0_dominance: 0.51\n    cv: 1.2172\n    positive_heads: 362\n    total_heads: 384\n    top5_heads:\n    - head: L1H11\n      delta: 1.016355\n    - head: L12H14\n      delta: 0.784513\n    - head: L8H4\n      delta: 0.759118\n    - head: L11H2\n      delta: 0.632357\n    - head: L13H2\n      delta: 0.522849\n    elapsed_min: 25.7\n    note: 't1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio'\n- exp_id: kivi_baseline_qwen_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_2bit_r128: 12.83\n    qwen_4bit_r128: 9.9\n    qwen_2bit_r0: 13.34\n    qwen_4bit_r0: 9.91\n    llama_2bit_r128: 9.84\n    llama_4bit_r128: 8.14\n    llama_2bit_r0: 10.08\n    llama_4bit_r0: 8.14\n    group_size: 32\n    eval_data: WikiText-2 test\n    note: r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\n- exp_id: qwen14b_constrained_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16: 6.8654\n    ppl_uniform_4bit: 7.202\n    ppl_constrained_mckp: 7.2206\n    ppl_unconstrained_mckp: 7.6923\n    delta_constrained_vs_uniform: -0.0185\n    delta_constrained_vs_uniform_pct: -5.51\n    delta_unconstrained_vs_uniform: -0.4902\n    bit_distribution_constrained:\n      '2': 8\n      '4': 374\n      '8': 1\n      '16': 1\n    bit_distribution_unconstrained:\n      '2': 77\n      '4': 271\n      '8': 35\n      '16': 1\n    concentration: 0.33\n    top1_pct: 0.2262\n    top5_pct: 0.3304\n    t1_t5: 0.68\n    shape: Flat\n- exp_id: pythia14b_constrained_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16: 16.4893\n    ppl_uniform_4bit: 24.2894\n    ppl_constrained_mckp: 24.4521\n    ppl_unconstrained_mckp: 31.5415\n    concentration: t1=0.0289, t5=0.2439\n    t1_t5: 0.0289/0.2439\n    shape: Flat\n    constrained_vs_uniform_gap: 0.1627\n- exp_id: qwen7b_8k_context_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16_8k: 6.97\n    ppl_constrained_mckp_8k: 8.59\n    ppl_uniform_4bit_8k: 77.75\n    ppl_bf16_2k: 9.81\n    ppl_constrained_mckp_2k: 10.89\n    ppl_uniform_4bit_2k: 15.45\n    mckp_improvement_over_uniform_8k: 97.7%\n    mckp_improvement_over_uniform_2k: 80.8%\n    shape: Spread\n    concentration: 0.5992\n    context_length: 8192\n    note: 'Concentration-dependent benefit amplifies at longer context: uniform 4-bit\n      catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust\n      (+23%)'\n- exp_id: qwen7b_8k_spotcheck\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: yi15_8k_spotcheck\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: llama_8k_spotcheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_bf16_8k: 5.5958\n    ppl_constrained_mckp_8k: 6.0537\n    ppl_uniform_4bit_8k: 6.0364\n    mckp_improvement_over_uniform_8k: -0.0174\n    mckp_improvement_pct_8k: -3.94\n    ppl_bf16_2k: 8.0922\n    ppl_constrained_mckp_2k: 8.5042\n    ppl_uniform_4bit_2k: 8.4701\n    shape: Spike\n    concentration: 0.5749\n    t1_over_t5: 0.71\n    context_length: 8192\n    bit_distribution:\n      '2': 2\n      '4': 253\n      '8': 1\n- exp_id: kivi_baseline_qwen7b_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_kivi_4bit_g32_r128: 9.8976\n    tokens: 298938\n    chunks: 583\n    stride: 512\n    model: Qwen2.5-7B\n    comparison_mckp_ppl: 10.91\n    comparison_uniform_ppl: 15.45\n    comparison_bf16_ppl: 9.81\n- exp_id: mistral_hires_constrained_mckp\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kivi_mckp_combined_qwen7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: qwen14b_greedy_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_constrained_ppl: 7.2206\n    mckp_constrained_ppl: 7.2206\n    delta_vs_mckp: 0\n    bit_distribution:\n      '2': 8\n      '4': 374\n      '8': 1\n      '16': 1\n    memory_ratio: 0.25\n    solver_time_sec: 0.08\n    total_time_min: 1.8\n- exp_id: mistral_uniform_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mistral_hires_constrained_mckp_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_wikitext2_ppl: 7.0352\n    mckp_wikitext2_ppl: 7.1341\n    uniform4bit_wikitext2_ppl: 7.1308\n    mckp_improvement_over_uniform: -0.0033\n    mckp_improvement_pct: -3.48\n    verdict: FAIL\n    bit_distribution:\n      '2': 2\n      '4': 254\n    fix_note: 'uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130'\n- exp_id: phi3_medium_hires_profiling_check\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: codellama_7b_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: llama_compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_k: 0\n    best_ppl: 8.0922\n    k0_ppl: 8.0922\n    k2_ppl: 8.1243\n    k4_ppl: 8.1803\n    k8_ppl: 8.2259\n    k16_ppl: 8.4378\n    k32_ppl: 9.0506\n    k64_ppl: 11.991\n    k128_ppl: 40.2067\n    k256_ppl: 1519.1888\n    budget: 0.25\n- exp_id: mistral_compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k0_ppl: 7.1308\n    k2_ppl: 7.1471\n    k4_ppl: 7.164\n    k8_ppl: 7.2001\n    k16_ppl: 7.31\n    k32_ppl: 7.4877\n    k64_ppl: 7.5932\n    k128_ppl: 7.5932\n    k256_ppl: 7.5932\n    best_k: 0\n    best_ppl: 7.1308\n    note: PPL monotonically increases with k; all-4bit optimal at budget=0.25; solver\n      saturates at k>=64 (41 actual 2-bit heads)\n- exp_id: phi3_medium_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: llama_downstream_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge:\n      fp16: 0.5188\n      uniform_4bit: 0.5256\n      mckp_k2: 0.5179\n    hellaswag:\n      fp16: 0.6073\n      uniform_4bit: 0.6024\n      mckp_k2: 0.6021\n    piqa:\n      fp16: 0.7922\n      uniform_4bit: 0.7873\n      mckp_k2: 0.7867\n    winogrande:\n      fp16: 0.7388\n      uniform_4bit: 0.7261\n      mckp_k2: 0.7309\n    avg_delta_vs_uniform: -0.1\n    bit_distribution:\n      4bit: 253\n      8bit: 1\n      2bit: 2\n    budget: 0.25\n    total_distortion: 0.7015\n    elapsed_sec: 3387\n- exp_id: yi_mistral_downstream_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    yi_k2:\n      arc_challenge:\n        baseline: 0.5265\n        uniform: 0.5205\n        mckp_k2: 0.4991\n      hellaswag:\n        baseline: 0.5912\n        uniform: 0.5855\n        mckp_k2: 0.5818\n      piqa:\n        baseline: 0.7949\n        uniform: 0.7916\n        mckp_k2: 0.7916\n      winogrande:\n        baseline: 0.7332\n        uniform: 0.7206\n        mckp_k2: 0.7238\n      avg_delta_vs_uniform: -0.0055\n      bit_distribution:\n        4bit: 189\n        8bit: 1\n        2bit: 2\n    mistral_k2:\n      arc_challenge:\n        baseline: 0.5043\n        uniform: 0.5068\n        mckp_k2: 0.5068\n      hellaswag:\n        baseline: 0.6118\n        uniform: 0.6051\n        mckp_k2: 0.605\n      piqa:\n        baseline: 0.8009\n        uniform: 0.7987\n        mckp_k2: 0.7982\n      winogrande:\n        baseline: 0.7411\n        uniform: 0.7395\n        mckp_k2: 0.7388\n      avg_delta_vs_uniform: -0.0003\n      bit_distribution:\n        4bit: 254\n        2bit: 2\n    elapsed_sec: 2672\n- exp_id: mistral_compounding_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k0_ppl: 7.0352\n    k2_ppl: 7.0366\n    k4_ppl: 7.0453\n    k8_ppl: 7.0636\n    k16_ppl: 7.1139\n    k32_ppl: 7.2378\n    k64_ppl: 7.7747\n    k128_ppl: 10.473\n    k256_ppl: 45.2766\n    budget: 0.25\n    n_heads: 256\n- exp_id: qwen_compounding_sweep\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_compounding_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_k0: 9.8106\n    ppl_k8: 10.0474\n    ppl_k64: 23.2176\n    ppl_k256: 98.7523\n    max_compounding_ratio: 10.07\n    n_heads_total: 112\n    n_2bit_ceiling: 96\n    budget: 0.25\n- exp_id: codellama_hires_profiling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_ppl: 7.6978\n    top5_concentration: 0.7975\n    t1_t5: 0.8131\n    distribution_shape: Spike\n    cv: 18.3153\n    l0_dominance_ratio: 0.8\n    top5_sensitive_heads:\n    - layer: 1\n      head: 1\n      delta_2bit: 22.998339\n    - layer: 1\n      head: 18\n      delta_2bit: 2.042989\n    - layer: 1\n      head: 11\n      delta_2bit: 1.460641\n    - layer: 0\n      head: 15\n      delta_2bit: 0.942934\n    - layer: 30\n      head: 31\n      delta_2bit: 0.839968\n    total_kv_heads: 1024\n    gqa_ratio: 1\n    profile_time_hours: 3.7\n- exp_id: gemma2_downstream_k2_4task\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gemma2_downstream_k8_4task\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: qwen_3seed_downstream_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge:\n      bf16: 0.4582\n      uniform: 0.459\n      mckp_mean: 0.459\n      mckp_std: 0.0035\n      delta: 0\n    hellaswag:\n      bf16: 0.5887\n      uniform: 0.5335\n      mckp_mean: 0.5748\n      mckp_std: 0.0022\n      delta: 0.0413\n    winogrande:\n      bf16: 0.7119\n      uniform: 0.6622\n      mckp_mean: 0.678\n      mckp_std: 0.0115\n      delta: 0.0158\n    piqa:\n      bf16: 0.7818\n      uniform: 0.7552\n      mckp_mean: 0.7748\n      mckp_std: 0.0023\n      delta: 0.0196\n    avg_delta: 0.0192\n    elapsed_sec: 2714\n- exp_id: gemma2_downstream_k8_4task_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge:\n      baseline: 0.6135\n      uniform: 0.6058\n      mckp_k8: 0.6049\n      delta: -0.0009\n    hellaswag:\n      baseline: 0.6093\n      uniform: 0.6092\n      mckp_k8: 0.6089\n      delta: -0.0003\n    winogrande:\n      baseline: 0.7443\n      uniform: 0.738\n      mckp_k8: 0.7443\n      delta: 0.0063\n    piqa:\n      baseline: 0.8128\n      uniform: 0.8036\n      mckp_k8: 0.8079\n      delta: 0.0043\n    avg_delta: 0.0024\n    bit_distribution:\n      4bit: 324\n      2bit: 8\n      8bit: 4\n    elapsed_sec: 2321\n- exp_id: llama_3seed_downstream_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_delta: -0.8\n    hellaswag_delta: 0\n    piqa_delta: -0.1\n    winogrande_delta: 0.5\n    avg_delta: -0.1\n    std_all_tasks: 0\n    note: Single profile → deterministic allocation → all 3 seeds identical\n- exp_id: falcon7b_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: deepseekvl_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: internlm2_7b_hires_profiling\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: phi3_medium_hires_profiling_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    top5_concentration: 0.1742\n    top5_n_heads: 20\n    baseline_calibration_ppl: 4.783\n    delta_2bit_cv: 0.8905\n    layer0_dominance_ratio: 0.04\n    shape: Spread\n    t1_t5_ratio: 0.24\n    top1_head: L9H6\n    top1_delta_2bit: 0.1806\n    total_heads: 400\n    profiling_hours: 2.48\n    note: Low concentration but t1/t5=0.24 indicates sensitivity spread across multiple\n      heads — confirmed Spread pattern. Mid-layer concentration (L8-L11).\n- exp_id: falcon7b_hires_profiling_v2\n  name: ''\n  status: PENDING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T02:14:58.097Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T02:14:58.097Z",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-16T02:14:58.120Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d55dd7b4-384e-4f71-a220-bc7a7ef917ff",
  "type": "user",
  "uuid": "7f8c55b1-2082-4699-9dba-34d8059c6428",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T02:14:58.116Z_

```json
{
  "parentUuid": "7f8c55b1-2082-4699-9dba-34d8059c6428",
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
  "uuid": "f44351d2-aa4b-44b1-b870-176a8c17f7b1",
  "timestamp": "2026-05-16T02:14:58.116Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T02:14:58.116Z_

```json
{
  "parentUuid": "f44351d2-aa4b-44b1-b870-176a8c17f7b1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0566dcc3-4a0a-4e3b-856c-11ab618ebaeb",
  "timestamp": "2026-05-16T02:14:58.116Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "0566dcc3-4a0a-4e3b-856c-11ab618ebaeb",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier Dream scenario for RateKV",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d"
}
```

---

### Assistant

_source line 8 · 2026-05-16T02:15:45.047Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research data carefully to define three tiers for a Dream simulation.

The paper is about per-head KV cache quantization on hardware-aligned bit-widths {2,4,8,16}. The core contributions are:
1. 2-bit compounding as universal failure mode
2. Cardinality constraint as universal fix
3. "Non-uniform rarely helps" as key negative result

Let me think about what best/median/worst means for this specific paper given the data and framing.

Key claims:
1. 2-bit compounding is universal failure mode (8/8 architectures)


2. Cardinality constraint fixes this universally and makes the choice of solver irrelevant since greedy matching performs identically to the more complex MCKP approach
3. Non-uniform quantization provides minimal benefit, helping in only 1 out of 8 architectures at moderate compression levels

The evidence spans eight different model architectures with unconstrained degradation ranging from 1.07× to 3.31× the baseline, and the solver equivalence shows zero difference between approaches, while diagnostic accuracy holds across all tested models.

Now I'm thinking through how this would actually land with reviewers—what scenarios could play out. The best case is all three claims hold up and they see the work as novel and useful. More realistically, some claims might need softening and we'd get pushback requiring adjustments. Worst case, the core framing gets attacked and needs rethinking entirely. I'm considering what assumptions would hold up under scrutiny: whether the universality claim survives across all 8 models, whether the solver equivalence result strikes reviewers as genuinely surprising and valuable, and whether the honest negative result about non-uniform benefits reads as a strength rather than a limitation. I need to define what I'm actually measuring here — this is a simulation of how the research might be received, so the metrics should reflect review outcomes. I'm thinking about claims that survive scrutiny, review scores on a competitive scale, acceptance likelihood, and how much pushback each tier would face. For the best-case scenario, all three core claims hold up: the 2-bit compounding as a universal failure mode, the constraint as a universal fix, and that non-uniform quantization rarely helps — and the paper gets accepted.

In the median case, the universality claim gets questioned because n=8 isn't enough evidence, and the constraint is seen as useful but not particularly novel. I'd need to shift the narrative toward the empirical analysis itself rather than claiming a methodological breakthrough. For the worst case, reviewers reject the whole "universal failure mode" framing as either architecture-specific or already established, and the constraint looks trivial — so I'd reposition it as a comprehensive empirical study of the design space with the contribution being the systematic analysis and diagnostics.

Now I'm setting up the actual metrics to track: average review scores on the ARR scale, how many of the three claims survive intact, acceptance probability, the number of fundamental objections that need addressing, how likely a rebuttal is to resolve those objections, and what narrative adjustments each scenario requires.

I'm laying out the ranges for best, median, and worst cases across these dimensions. The best case keeps most claims intact with minimal narrative changes needed. The median case loses one or two claims and requires moderate reframing. The worst case loses all claims and needs substantial repositioning. But looking at this again, the paper does have solid empirical coverage across those eight architectures — the real vulnerability is the incrementality concern and whether the constraint itself gets dismissed as trivial.

Now I'm identifying the core assumptions that would need to hold for each tier. The best outcome requires all eight assumptions to survive scrutiny — that the 2-bit compounding is genuinely novel, the effect generalizes across architectures, the constraint is both sufficient and non-trivial, and the diagnostic approach adds real value. The median case only needs the foundational assumptions about novelty and universality plus the solver equivalence result. I'm mapping which assumptions are load-bearing for each acceptance scenario.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0566dcc3-4a0a-4e3b-856c-11ab618ebaeb",
  "isSidechain": false,
  "requestId": "req_011Cb5SYioyUsNoHoxVAkbUu",
  "type": "assistant",
  "uuid": "303e5234-4db5-4477-b2ad-9581d269e09a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QM6PdQQEDJZXrHM5GrZSTZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35793,
      "cache_read_input_tokens": 11841,
      "output_tokens": 4344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4344,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35793
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

_source line 9 · 2026-05-16T02:16:35.343Z_

```yaml
tiers:
  best:
    meaning: "三条 claim 全部成立，reviewer 认可 compounding 发现的新颖性和 constraint 的实用价值，1/8 benefit 被视为诚实的 negative result 而非弱点"
    key_assumptions:
      - "A1: 2-bit compounding 在 KV cache 文献中确实未被系统刻画（novelty 成立）"
      - "A2: 8/8 架构全部复现 unconstrained degradation（universality 被接受）"
      - "A3: cardinality constraint 被视为 principled intervention（非 trivial heuristic），因为 solver equivalence (Δ=0.0000) 证明了 constraint 才是核心"
      - "A4: 1/8 benefit + 7/8 negative 被视为对 field 隐含假设的重要修正"
      - "A5: diagnostic (9/9 accuracy) 作为 testable hypothesis 被接受，不需要统计显著性"
      - "A6: RateQuant 区分清晰——polymatroid 在 {2,4,8,16} 上 breaks 这一点被认可"
    number_ranges:
      avg_review_score_arr: [3.5, 4.0]
      claims_surviving_intact: [3, 3]
      p_accept_emnlp_main: [0.40, 0.60]
      major_reviewer_objections: [0, 1]
      narrative_rewrite_pct: [0, 10]
      unconstrained_degradation_universality: [8, 8]  # 8/8 architectures
      solver_equivalence_delta: [0.0, 0.001]
      diagnostic_accuracy: [8, 9]  # out of 9
      downstream_consistency_with_ppl: [5, 5]  # out of 5 models
    narrative_direction: >
      原始 framing 完全成立。Title: "2-Bit Compounding: A Universal Failure Mode in Per-Head KV Cache Quantization"。
      三条 claim 原样保留：(1) compounding 是 universal failure mode，(2) cardinality constraint 是 universal fix 且 solver-agnostic，(3) non-uniform rarely helps + diagnostic。
      Reviewer 可能要求增加 1-2 个模型或 error bar 作为 minor revision，但核心叙事不需调整。
      长上下文结果 (11.15× vs 1.23×) 作为 deployment motivation 的 headline 数字。
      Qwen 是 showcase，7/8 negative 是 contribution 的一部分。

  median:
    meaning: "Compounding 发现和 constraint 有效性被认可，但 'universal' 语言和 diagnostic 的 claim 强度受到质疑；需要降低 claim 语气并补充实验"
    key_assumptions:
      - "A1: compounding 被认可为有价值的实证发现，但 reviewer 指出 RateQuant Appendix M 已 acknowledge 该现象（novelty 打折）"
      - "A2: 8 个架构不足以支撑 'universal'——reviewer 要求去掉该词或补充至 12+ 模型"
      - "A3: constraint 被部分 reviewer 视为 'obvious in hindsight' / 'just a hyperparameter'，需要更强的 principled justification"
      - "A4: 1/8 benefit 被 1-2 个 reviewer 视为方法有效性不足的证据（'method only works on Qwen'）"
      - "A5: diagnostic n=9 被拒绝作为独立 claim——只能作为 observation 或 hypothesis"
      - "A6: 缺少 eviction baseline 和 multi-seed downstream CI 被标为 significant gap"
    number_ranges:
      avg_review_score_arr: [2.8, 3.5]
      claims_surviving_intact: [1, 2]  # claim 1 (compounding) likely survives; claim 2 (constraint) needs softening; claim 3 (diagnostic) demoted
      p_accept_emnlp_main: [0.15, 0.35]
      major_reviewer_objections: [2, 3]
      narrative_rewrite_pct: [25, 45]
      unconstrained_degradation_universality: [6, 8]  # reviewer may dispute mild cases (1.07×) as "not really failure"
      solver_equivalence_delta: [0.0, 0.001]  # data unchanged, but reviewer may say "so what"
      diagnostic_accuracy: [7, 9]  # if forced to add models, some may break diagnostic
      downstream_consistency_with_ppl: [4, 5]
    narrative_direction: >
      需要调整 claim 强度。(1) "universal failure mode" → "consistent failure pattern across 8 diverse architectures"，
      去掉 universal 一词，改为 "widespread" 或 "systematic"。(2) constraint contribution 从 "核心方法贡献" 
      重新定位为 "principled analysis insight that yields a practical fix"——强调分析贡献而非方法贡献。
      (3) diagnostic 从独立 claim 降级为 Section 5 的 empirical observation + "testable hypothesis for future work"。
      补充实验：(a) 2-3 个额外架构的 profiling（不需要 full pipeline），(b) downstream multi-seed CI 至少在 Qwen 上，
      (c) 在 related work 中更显式地讨论 RateQuant Appendix M 的 compounding acknowledgment 并 clarify 区别。
      论文 reframe 为 "empirical analysis paper with practical implications" 而非 "method paper"。
      EMNLP Efficient Methods track 仍然适合，但需要在 intro 中前置 analysis contribution。

  worst:
    meaning: "核心 'universal failure mode' narrative 被拒——reviewer 认为 compounding 是已知现象、constraint 是 trivial engineering、1/8 benefit 证明方法无价值"
    key_assumptions:
      - "A1: reviewer 引用 RateQuant Appendix M + 其他量化文献，论证 compounding 不是新发现（novelty claim 被否）"
      - "A2: 'universal' 在 n=8 上不成立，且 mild cases (1.07×) 被 reviewer 认为是噪声而非 failure"
      - "A3: cardinality constraint 被定性为 'grid search over one hyperparameter'——不构成贡献"
      - "A4: 7/8 negative result 被解读为 'non-uniform KV cache quantization is a solved non-problem at 4× compression'"
      - "A5: solver equivalence 被视为 'constraint 过强导致问题退化'——不是 insight 而是 artifact"
      - "A6: 缺乏理论分析解释 WHY compounding happens——纯经验性 paper 在 EMNLP 被 undervalued"
    number_ranges:
      avg_review_score_arr: [2.0, 2.8]
      claims_surviving_intact: [0, 1]
      p_accept_emnlp_main: [0.02, 0.12]
      major_reviewer_objections: [3, 5]
      narrative_rewrite_pct: [60, 80]
      unconstrained_degradation_universality: [5, 7]  # reviewer discounts mild (1.07-1.08×) as within noise
      solver_equivalence_delta: [0.0, 0.001]  # data same but framed negatively
      diagnostic_accuracy: [6, 8]  # additional models or stricter evaluation breaks some
      downstream_consistency_with_ppl: [3, 5]
    narrative_direction: >
      核心 framing 需要彻底重构，但仍冲 EMNLP 不降级。新 angle: 从 "failure mode discovery + fix" 
      转向 "When Does Per-Head KV Cache Quantization Help? A Systematic Empirical Study"。
      核心贡献变为：(1) 首个跨架构系统研究 per-head KV cache 量化的适用条件——在 8+ 架构上的 comprehensive 
      benchmark 本身就是贡献（EMNLP resource/benchmark 传统），(2) sensitivity distribution taxonomy 
      (spike/spread/flat) 作为理解不同架构量化行为的 framework，(3) 实用 diagnostic 帮助从业者决定是否值得 
      profiling。Compounding 和 constraint 从 main claims 降级为 Section 4 的 "analysis of allocation 
      failures"——支撑证据而非核心贡献。论文 title 改为 "Per-Head KV Cache Quantization: When It Helps, 
      When It Hurts, and How to Tell"。这个 framing 下 7/8 negative 变成资产（comprehensive coverage），
      1/8 positive 变成 interesting case study，n=8 变成 reasonable benchmark scope。
      需要补充的实验：(a) 至少 3 个额外架构的 profiling 数据充实 benchmark，(b) 更多压缩比的 systematic sweep，
      (c) 与 KIVI/GEAR 等更多 baseline 的对比。牺牲 narrative sharpness 换取 robustness。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "303e5234-4db5-4477-b2ad-9581d269e09a",
  "isSidechain": false,
  "requestId": "req_011Cb5SYioyUsNoHoxVAkbUu",
  "type": "assistant",
  "uuid": "37d471e8-31cf-4e8d-9ecb-2ee435eafb25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QM6PdQQEDJZXrHM5GrZSTZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35793,
      "cache_read_input_tokens": 11841,
      "output_tokens": 4344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4344,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35793
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "37d471e8-31cf-4e8d-9ecb-2ee435eafb25",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier Dream scenario for RateKV",
  "sessionId": "29ec6bd2-67b5-47ca-a2ed-69cf14f2fb4d"
}
```

---
