# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：plan001 严重不完整（≤10 runs）；1.5B 未复现 0.5B 的 within-gen 发现；seed 方差摧毁信号排名稳定性；LLaM

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/d7840e40-35a1-4a03-81ea-555b5db73a39.jsonl`
- **Structured JSON:** [`90ace694ff7dd9fe0f7b.json`](../../sessions/90/90ace694ff7dd9fe0f7b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T10:08:04.960Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T10:08:04.960Z",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：plan001 严重不完整（≤10 runs）；1.5B 未复现 0.5B 的 within-gen 发现；seed 方差摧毁信号排名稳定性；LLaMA 方向不一致或未跑；需要 reframe 但不降级 venue\n核心假设：['plan001 仅完成 ≤10/30 runs（基本停留在当前状态），5-seed 统计不可行', '1.5B within-gen AUC 显著低于 0.5B（stable_rank AUC < 0.80），early warning 不跨 scale', '6-fraction ρ 因 seed 方差和非单调 fraction 行为降至 < 0.85', 'stable_rank 5-seed（实际 3-seed）CV > 0.06，排名进一步不稳定（从 rank 4 继续下跌）', 'LLaMA 未完成 或 < 6/11 信号方向一致（core signal 如 stable_rank 方向相反）', 'PPL within-gen AUC 在 1.5B 反而有效（AUC > 0.70），破坏 \"PPL fails\" 叙事', '3B spot-check 某 core signal 方向不一致', 'Full FT 对比仍为 N=1，无法支撑 method-dependence claim', 'PubMed 3-seed 勉强完成但信号行为与 WikiText 差异大于预期']\n关键指标范围：{'spearman_rho_median_across_seeds': [0.7, 0.85], 'within_gen_auc_stable_rank_1.5B': [0.6, 0.8], 'within_gen_auc_ppl_1.5B': [0.5, 0.75], 'within_gen_auc_training_loss_1.5B': [0.65, 0.8], 'cohens_d_spectral_entropy_5seed': [8.0, 18.0], 'cohens_d_perplexity_5seed': [5.0, 12.0], 'cohens_d_stable_rank_5seed': [2.0, 6.0], 'stable_rank_cv_across_seeds': [0.06, 0.12], 'llama_signal_direction_consistency': [3, 6], 'scale_3B_core_direction_match': [2, 3], 'plan001_runs_completed': [6, 12], 'pubmed_recovery_prevalence': [0.4, 0.65]}\n叙事方向：核心假设 \"signals reliably track collapse across configs\" 不成立——信号行为高度  config-dependent，排名不稳定。Reframe 方向：从 \"practitioners can use signal X\"  转为 \"we document the surprising fragility of training-time collapse signals\"。 新 angle：\"Collapse monitoring is harder than it looks\"——同一信号在不同 scale/seed/method  下表现迥异，这本身是对 practitioner 的重要警告。Claim 1 从 \"correlation\" 改为 \"conditional  correlation\"（仅在特定配置下成立）。Claim 2 从 \"early warning\" 改为 \"scale-dependent  early warning\"（0.5B 有效但不泛化到 1.5B，暗示大模型需要不同的检测策略）。Claim 3 成为论文 核心——从辅助 claim 升级为主 claim：\"signal behavior is fundamentally configuration-dependent,  and the field's implicit assumption that collapse signals transfer across settings is wrong\"。 如果 PPL within-gen AUC 在 1.5B 升高，则 \"PPL fails\" 叙事反转为 \"PPL's effectiveness  is scale-dependent\"——仍是有价值的发现。LLaMA 不一致则写 \"architecture-dependent signal  behavior\" 作为 finding 而非 limitation。论文 reframe 为 negative-result + taxonomy paper， 仍冲 EMNLP（EMNLP 历来接收高质量 negative results），但大概率推迟到 ARR 6/15。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: collapse_severity_monitor\nfocus: 当前 plan 已扩展到 cross-family (LLaMA) + MMLU-mini + Full FT 3-seed + scale-dependent within-gen finding。重点评估：(1) cross-family spot-check (N=1) 是否足够回应 \"architecture-specific\" 质疑；(2) scale-dependent signal ranking 是加强还是削弱 Claim 2；(3) ��体 scope 升级后能否支撑 EMNLP ARR 接收\n\n## paper_framing.md\n\n# Paper Framing — collapse_severity_monitor\n\n## Target Venue\n- Primary: EMNLP 2026 via ACL Rolling Review (ARR)\n- Deadline: ARR submission 2026-05-25\n- Backup: ARR June cycle (2026-06-15) if 5/25 not feasible\n\n## Core Claims (3 条)\n\n1. **Signal-Severity Correlation**: Spectral signals (stable rank, spectral entropy) and output signals (token entropy, perplexity) reliably track model collapse severity across synthetic data contamination levels, maintaining monotonic ordering across tested fractions and generations. (MVP: ρ=1.0 with n=3; to be validated with n=6 fractions × 5 seeds in plan_001. Primary evidence: Spearman ρ with bootstrap CIs; effect sizes elevated as primary evidence, ρ as supporting.)\n\n2. **Early Warning Capability**: Collapse can be detected at moderate contamination (50%) within a single training run: stable rank achieves AUC=0.984 [0.978, 0.989] for within-gen collapse detection, reaching AUC=0.94 (sens=0.78, spec=1.00) at just 10% training progress. Training loss is the second-best within-gen detector (AUC=0.923). ROC analysis must use clustered bootstrap (one observation per fraction×seed) to avoid inflating AUC from serial generation dependence. **Featured sub-result: held-out evaluation perplexity — the metric practitioners most commonly check at eval checkpoints — provides no within-generation early warning (AUC=0.534 ≈ random).** This is because held-out PPL requires multi-generation accumulation before collapse manifests; in contrast, train-set loss (AUC=0.923) detects earlier because it directly measures learning dynamics on the contaminated distribution. Claim 2 Results 段落结构：(a) stable_rank early detection 正面证据, (b) 专门 1 段讨论 PPL within-gen 失效 + 原理解释 + AUC 对比, (c) ROC curves 图。Abstract 加半句：\"notably, held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.53)\"。(Note: stable_rank is seed-sensitive but early-detecting; spectral_entropy is seed-robust but late-detecting (only at 100%). Practitioner recommendation: use stable_rank for within-gen early warning, perplexity for cross-gen severity comparison, spectral_entropy for severity discrimination. Cross-validation needed: plan001 5-seed + plan002 PubMed within-gen ROC, 如果多配置 PPL AUC 一致 ~0.5，camera-ready 可升级措辞。See writing notes 17, 18, 19.)\n\n3. **Non-Uniform Signal Behavior**: The same monitoring signal can be informative under one training method and misleading under another. Spectral signals saturate at extreme severity; gradient norm is non-monotonic under QLoRA but monotonic under Full FT; downstream metrics (HellaSwag) track collapse under Full FT but remain stable under QLoRA. Both methods show large gen1 PPL jumps (Full FT 15.3x, QLoRA 8.7x) but diverge in subsequent evolution: Full FT saturates (gen1→4: 1.11x), QLoRA decelerates but continues (gen1→4: 6.13x). Featured sub-result: PPL-downstream dissociation — QLoRA PPL=839 but hellaswag=0.430 vs Full FT PPL=326 but hellaswag=0.372, meaning PPL-based monitoring overestimates damage under QLoRA and practitioners must consider training method when selecting collapse signals. Terminal spectral convergence (SR ~154-156) noted as observation, not claimed as finding (N=1). Signal taxonomy table should include \"method-dependence\" column.\n\n## Story Spine\n\n- **Problem**: Model collapse from iterative training on synthetic data is a growing concern as LLM-generated text pervades training corpora. While the phenomenon is well-characterized theoretically (Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024), practitioners lack actionable tools to detect and quantify collapse severity during training. Current work focuses on post-hoc analysis or output-level detection, missing the rich signal available in training dynamics.\n\n- **Existing approaches & gaps**: SIGMA (2025) monitors output embedding spectral properties but requires access to a clean reference distribution (plan_009 adds head-to-head to clarify operational vs fundamental advantage). Kalinowski (2024) uses topological analysis but is computationally expensive. Data mixing strategies (Gerstgrasser et al. 2024, Kazdan et al. 2024) study prevention rather than detection. Neither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they examine within-generation temporal dynamics for early warning.\n\n- **Our framing**: We conduct a systematic empirical analysis of training dynamic signals as collapse severity monitors. Across 4 signal families (spectral, output, gradient, downstream) × 6 contamination levels × 2 model scales × 2 domains × 2 fine-tuning methods, we characterize which signals track collapse, when they diverge, and where they fail. Key insight: stable rank provides the earliest within-gen warning (AUC=0.94 at 10% training progress) while perplexity provides the most reliable cross-generation severity tracking — but these roles are non-interchangeable. We document a partial self-recovery phenomenon at moderate contamination consistent with known data mixing effects (Gerstgrasser et al. 2024), and characterize where standard monitoring signals mislead practitioners.\n\n- **Headline result template**: \"Stable rank detects within-generation collapse with AUC=0.984, reaching actionable sensitivity (AUC=0.94) at 10% training progress. Across generations, spectral entropy provides the most robust severity discrimination (CV=0.0015) but is a late detector (only at 100% contamination). Held-out evaluation perplexity — often the go-to metric at eval checkpoints — is nearly ineffective for within-generation detection (AUC=0.534), while train-set loss detects data distribution shift (AUC=0.923) but not model quality degradation; evaluation perplexity remains the strongest cross-generation severity tracker. Different signals have complementary operating ranges; no single signal suffices across all detection contexts.\" (Note: ρ ≥ 0.94 是 plan001 验证目标，非当前实际数值，到手前用 effect size 表述。分层信号策略替代单一 headline signal。ROC 数据来自 plan005 within-gen 分析，N=1 seed。)\n\n## Anticipated Reviewer Concerns & Mitigation\n\n| Concern | Severity | Mitigation |\n|---------|----------|------------|\n| Statistical power (seeds) | CRITICAL | 5 seeds WikiText, 3 seeds PubMed; bootstrap CIs for all claims |\n| n=3 fractions → trivial ρ=1.0 | HIGH | 6 fractions (0/10/25/50/75/100%) |\n| Single model scale | HIGH | 0.5B + 1.5B (+ 3B spot-check if GPU permits) |\n| Single dataset | HIGH | WikiText-2 + PubMed (3 seeds each) |\n| QLoRA only | MEDIUM | Full FT comparison on 1 config (plan_003) |\n| ROC pools non-independent observations | HIGH | Clustered bootstrap or one-gen-per-run restriction (plan_005) |\n| Stable rank direction under collapse | MEDIUM | Clarify: ‖W‖_F² grows faster than σ₁² → SR increases = energy dispersal, not concentration. Fix text |\n| No theoretical grounding | MEDIUM | Informal argument: 75% phase transition ↔ distributional shift theory; when spectral monitoring fails (capacity redundancy) |\n| \"First\" claims overclaimed | MEDIUM | Qualify: \"first systematic multi-axis comparison in iterative fine-tuning setting.\" Self-recovery → cite Gerstgrasser et al. |\n| SIGMA differentiation thin | MEDIUM | Head-to-head (plan_009): run SIGMA at training checkpoints |\n| Related work too thin | HIGH | ≥20 refs: Briesch 2023, Hataya 2023, Gerstgrasser 2024, Seddik 2024, Dohmatob \"Tale of Tails\" 2024, Pennington & Worah 2017 |\n| Missing synthetic data gen params | LOW | Document temperature, top-p/k, max length, prompt format in Methods |\n| No code/data release | MEDIUM | Release monitoring toolkit + signal trajectories + generation scripts |\n| \"Not a monitoring system\" | LOW | Frame as analysis paper; taxonomy + early warning = practical value |\n| No intervention/mitigation | LOW | Explicit non-goal; future work |\n\n## Core Insight (一句话)\n\nTraining dynamic signals provide a free, model-agnostic early warning system for model collapse — but different signal families have distinct operating ranges, and practitioners need to know which signal to trust at which severity level.\n\n## Novelty Statement\n\nWe provide the first systematic multi-axis comparison of training-time signal families as collapse severity monitors, spanning contamination levels, model scales, text domains, and fine-tuning methods. The within-generation early warning capability (stable rank AUC=0.94 at 10% training progress), the signal operating-range taxonomy, and the documentation of where standard monitoring signals actively mislead practitioners are the primary empirical contributions. The self-recovery observation at moderate contamination is consistent with known data mixing effects and is positioned as a finding rather than a novel phenomenon.\n\n## Key Writing Notes (from Dream review, 2026-05-14)\n\n1. **Effect sizes > ρ**: Elevate effect size tables as primary evidence; ρ as supporting.\n2. **Stable rank direction**: SR increases under collapse = energy dispersal (Frobenius norm grows faster than spectral norm), not concentration. Fix text.\n3. **25% contamination**: \"mild degradation / near-stability\", NOT \"strong recovery\" (PPL monotonically increases).\n4. **Figures required**: Severity curves, ROC curves, heatmaps, per-layer propagation. Analysis paper without figures is a major gap.\n5. **Reproducibility**: Code release, signal trajectories, generation scripts for D&B track.\n6. **Collapse protocol**: Explicitly state whether fine-tuning from M₀ or M_{g-1} and discuss implications.\n7. **Per-layer 叙事修正 (D011, 2026-05-15)**: 废弃\"三区结构\"（boundary/middle-neutral/late-bifurcation），改为 sub-module-centric 分析。真实数据显示 v_proj 在几乎所有层 diffuse（ΔSR +1~+3），down_proj 在 L11-L12 局部 collapse，其余子模块温和。Practitioner takeaway: 优先监控 v_proj stable rank 作为最敏感的 within-run collapse indicator。（注：cross-seed 稳定性另论，参见写作笔记 16。within-run 灵敏度与 cross-seed 排名是不同维度。）\n8. **SIGMA 方向 provisional (C001/D014, 2026-05-15)**: expected_direction=+1（effective_rank 在 collapse 时上升）是 N=2 观测，非已验证结论。禁止在论文中当发现写。验证条件：plan_001 seed43-46 全量数据 + plan_003 Full FT SIGMA 数据。如果 Full FT 方向一致(+1)可排除 QLoRA confound；如果不一致需重写分析。\"Within-gen corruption vs recursive collapse 方向差异\"作为 discussion 论点需要等验证后才能使用。\n9. **Non-monotonic claim scope (plan008/plan003, 2026-05-15)**: \"Non-monotonic\" 仅适用于 frac=50% 的 plateau 行为（ppl 26.9→25.6→25.7→25.6，真正收敛）。frac=100% gen1→gen2 的 -1.9% 下降（294→288）是噪声级波动，N=1 无法区分，禁止称为 \"non-monotonic pattern\"。100% 的正确描述：\"catastrophic jump at gen1 followed by continued degradation\"。\n10. **HellaSwag method-dependence + 归因修正 (plan003, 2026-05-15; 合并原 Note 10+13)**: HellaSwag 追踪 collapse 能力取决于训练方法（Full FT: 有效, -12.5%；QLoRA: 无效/稳定）。D015/D017 的\"0.5B 失效\"诊断错误——失效的是 QLoRA 的隐式正则化，非模型规模。论文归因必须是 method 而非 scale。反直觉：QLoRA gen4 PPL (839) > Full FT gen4 PPL (326)，但 QLoRA hellaswag (0.430) > Full FT hellaswag (0.372)——PPL 不是下游质量的唯一预测器。\n11. **Collapse trajectory: 两种方法都 gen1 大跳，差异在后续 (plan003, 2026-05-15; D026 修正 D024)**: Full FT gen1=15.3x 后饱和（gen1→4: 1.11x）；QLoRA gen1=8.7x 后减速增长（gen1→4: 6.13x，gen4 PPL=839）。**禁止**使用 \"slow onset\" / \"snowball\" / \"exponential\" 描述 QLoRA——QLoRA gen1 也是大跳（8.7x），不是缓慢起步。正确叙事：两种方法初始冲击程度不同（Full FT 更剧烈），后续演化模式不同（饱和 vs 减速增长）。终态谱收敛（SR ~154 vs ~156）需用正确数据重新验证后方可使用。\n12. **Diversity 指标对 collapse 不敏感 (plan003, 2026-05-15)**: distinct_1 在 Full FT frac=100% 仅 -3%（0.0925→0.0897），self_bleu 几乎不变，即使 PPL 暴涨 17x。原因：collapsed model 输出分布坍缩到少数 token（token_entropy -55%），但采样随机性维持了 lexical diversity 的表面指标。论文中需明确将 diversity 族排除在有效 collapse indicator 之外，或专门讨论 entropy vs diversity 解耦现象。\n13. *[已合并到 Note 10]*\n14. **Claim 3 措辞升级方向 (Reviewer 评估, 2026-05-15)**: 从 \"different signals respond differently\" 升级为 \"the same signal can be informative under one training method and misleading under another\"——直击 practitioner pain point。PPL-downstream dissociation 作为 Claim 3 featured sub-result（1 段专门讨论），不独立成 claim（N=1 seed, 1 downstream task, 无法排除 HellaSwag ceiling/floor effect）。Signal taxonomy table 加 \"method-dependence\" 列。Abstract 用一句：\"perplexity and downstream metrics can diverge under parameter-efficient FT, cautioning against single-signal monitoring\"。Terminal spectral convergence 降级为 observation（N=1 无法区分\"收敛\"和\"碰巧接近\"）。Limitations 必须标注 Full FT 对比的 N=1 限制。\n15. **Self-recovery prevalence 对比禁令 (Reviewer, 2026-05-16)**: 3-seed 的 9/9=100% vs plan008 的 16/18=89% 不可比——前者仅用 3 个信号（PPL, stable_rank, spectral_entropy），后者用 6 个信号。选取的恰好是最一致的信号。论文中讨论 self-recovery 时必须标注信号覆盖范围，禁止跨不同信号集做 prevalence 对比。\n16. **Signal ranking instability: stable_rank seed-sensitive (plan006/008 3-seed update, 2026-05-16)**: 3-seed 数据显示 stable_rank 的 Cohen's d 从 61.7 暴跌到 9.43（rank 1→4），原因是 seed44 引入 frac=50% 方差（CV=0.022）。spectral_entropy 最稳定（CV=0.0015，d=33.48，rank 2→1）。**禁止**在论文中将 stable_rank 定位为\"最敏感信号\"——正确叙事见写作笔记 17 分层策略。最终 taxonomy ranking 需等 plan001 5-seed 数据确认。\n17. **分层信号策略（Signal Heatmap 发现, 2026-05-16; 修正 D029）**: spectral_entropy 虽 cross-seed 最稳定（d=33.48, CV=0.0015），但是 **late detector**——仅在 frac=100% 下显著（Δ+25.7%），frac=50% 下 effect size < 5%。stable_rank 和 perplexity 是 **early detectors**（50% 即可检出：SR +564.8%, PPL +5255%）。**禁止**推单一 headline signal。正确叙事：\"signals have complementary operating ranges\"——stable_rank + perplexity 用于 early warning（Claim 2），spectral_entropy 用于 severity discrimination（区分 50% vs 100%）。这个分层发现本身就是 Claim 3 taxonomy 的核心价值：no single signal suffices。6/7 信号方向跨 QLoRA/Full FT 一致，强化 Claim 1 泛化性。\n18. **Within-gen ROC 证据精确化 Claim 2（plan005 ROC 分析, 2026-05-16; 修正写作笔记 17 的 perplexity 角色）**: ROC 分析揭示信号在 within-gen vs cross-gen 两个维度的能力完全不同。stable_rank 是 within-gen 最强检测器（AUC=0.984, 10% progress 即达 AUC=0.94）；training_loss 次之（AUC=0.923）；**perplexity within-gen 几乎无效（AUC=0.534）**——但 cross-gen 仍是最强 severity tracker。spectral_entropy within-gen 非单调（20% progress 时 AUC 降到 0.30，方向翻转），**不适合 threshold-based 早期检测**。这修正了写作笔记 17 将 perplexity 归入 \"early detectors\" 的表述——perplexity 是 cross-gen early detector（50% contamination 可检出），但 within-gen early detector 只有 stable_rank 和 training_loss。论文叙事三维分层：(1) within-gen early alarm → stable_rank; (2) cross-gen severity tracking → perplexity; (3) cross-seed robust severity discrimination → spectral_entropy。Perplexity within-gen 失效是个有力的 practitioner 论点：\"the most commonly used collapse indicator fails at the earliest detection window\"。**ROC 数据为 N=1 seed, 0.5B only，plan001 5-seed 后需验证。**\n19. **信号定义精确化：三个 loss/PPL 信号的数据源（D035, 2026-05-15; 修正原 Note 19 错误归因）**: 代码中存在三个容易混淆的信号，必须在 Method 中精确定义：\n    - **training_loss** = Trainer running avg CE on **训练集**（含 synthetic 混合数据），每 50 step 记录（`train.py:109-110`）。Within-gen AUC=0.923（有效）。原因：直接测量模型对被污染训练分布的学习动态。\n    - **perplexity** = exp(mean NLL) on **固定 held-out 验证集**，model.eval() 模式，每 50 step 记录（`signals.py:92-108`）。Within-gen AUC=0.534（无效）。原因：QLoRA 早期微调对 held-out 分布影响微弱，collapse 效应需多代累积。Cross-gen d=20.82（有效）。\n    - **token_entropy** = output token 分布的 Shannon entropy，within-gen AUC=0.478（无效）。\n    **原 Note 19 的错误**：将 AUC=0.534 的信号标注为\"training perplexity\"（训练数据上的 PPL），实际该信号是 held-out eval PPL。training_loss（训练数据上的 CE）反而 AUC=0.923。\n    **论文叙事修正**：Claim 2 featured sub-result 从\"training perplexity fails\"修正为\"**held-out evaluation perplexity** fails at within-gen detection (AUC=0.534), while train-set loss detects effectively (AUC=0.923)\"。Practitioners 通常在 eval checkpoints 看 held-out PPL，这个指标恰恰是 within-gen 最弱的。训练 loss 是间接的分布变化探测器，但 stable_rank (AUC=0.984) 仍最强因为它检测权重结构变化。\n    **Abstract/Intro 措辞**：从 \"training perplexity provides no within-gen early warning\" 改为 \"held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.534)\"。\n    Method 必须加入 training_loss 作为正式信号（Output 家族），明确标注数据源。Fig 3 展示 training_loss 合理（within-gen 第二强），需与 Method 信号列表一致。Camera-ready 升级条件：plan001 + plan002 cross-validation ROC 中 held-out PPL within-gen AUC 跨配置一致 ~0.5。\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Scale validation: 1.5B model (Qwen2.5-1.5B) × WikiText-2 × 6 fractions\n    (0/10/25/50/75/100%) × 5 seeds. Core experiment proving signal-severity correlation\n    generalizes beyond 0.5B MVP.'\n  priority: P0\n  gpu_budget_hours: 150\n  deps: []\n  registry_id: plan001-wikitext-15B-5seeds\n  notes: 6 fractions × 5 seeds × 5 gens = 150 runs. ~1h/run on A6000 for 1.5B QLoRA.\n    Dream review unanimously requires ≥5 seeds for variance estimation credibility.\n  status: DONE\n  conclusion: failed\n  metrics:\n    gpu0_status: 已重启 submit_training_job, timeout=48h. seed42 frac=0.25 加载中 (skip\n      frac=0.0 ✓)\n    gpu1_status: PID running, seed42 frac=1.0 step ~1068/1540 (69%), 正常\n    completed_seeds:\n      seed42: frac=0.0 ✓, frac=0.5 ✓, frac=1.0 gen4 69%\n      seed43: frac=0.0 ✓, frac=0.5 ✓\n      seed44: frac=0.0 ✓, frac=0.5 ✓\n      seed45: frac=0.0 gen4 synth 中断(被kill), 待 GPU0 轮到时自动补完\n      seed46: not started\n    v2_allocation:\n      gpu0: fractions (0.0, 0.25, 0.1) × seeds 42-46\n      gpu1: fractions (0.5, 1.0, 0.75) × seeds 42-46\n    runs_completed: 6/30 (v2 total)\n    gpu0_restart:\n      time: 2026-05-15T23:01Z\n      timeout_hours: 48\n      reason: seed45 frac=0.0 gen4 synth killed\n    disk: 18G/250G (7%)\n    checked_at: 2026-05-15T23:02Z\n- id: plan_002\n  claim: 1\n  description: 'Cross-domain validation: 1.5B × PubMed × 6 fractions × 3 seeds. Proves\n    signals generalize beyond WikiText to biomedical domain.'\n  priority: P0\n  gpu_budget_hours: 45\n  deps: []\n  registry_id: plan002-pubmed-cqa1\n  notes: 6 fractions × 3 seeds × 5 gens = 90 runs. Dream review flags single-seed\n    PubMed as internal contradiction (paper argues against single-seed while doing\n    exactly that). 3 seeds minimum.\n  status: RUNNING\n  metrics:\n    gpu0_status: seed42 frac=10%, gen2 training 11% (156/1410)\n    gpu1_status: seed42 frac=75%, gen1 training 99% (1400/1410)\n    gpu2_status: seed44 frac=100%, gen0 synthetic 21%\n    fraction_coverage:\n      completed:\n        '0.0':\n        - seed42\n        - seed43\n        - seed44\n        '0.5':\n        - seed42\n        - seed43\n        - seed44\n        '1.0':\n        - seed42\n        - seed43\n      in_progress:\n        '0.1': seed42 gen2 (GPU0)\n        '0.75': seed42 gen1 (GPU1)\n        '1.0': seed44 gen0 (GPU2)\n      not_started:\n      - '0.25'\n    gpu_eta:\n      cuda2_free: ~4h (seed44 frac=100%)\n      cuda1_free: ~13h\n      cuda0_free: ~18-27h\n    disk: 86G/250G (35%)\n    checked_at: 2026-05-16T08:24Z\n- id: plan_003\n  claim: 1\n  description: 'Full FT comparison: 0.5B × WikiText-2 × 3 fractions (0/50/100%) ×\n    1 seed with full fine-tuning. Validates signals are not QLoRA-specific.'\n  priority: P1\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: plan003-fullft-05B\n  notes: Full FT on 0.5B should fit in single A6000 24GB.\n  status: DONE\n  conclusion: success\n  metrics:\n    fullft_0pct_gen4:\n      ppl: 19.23\n      stable_rank: 37.48\n      spectral_entropy: 0.765\n      token_entropy: 1.884\n    fullft_50pct_gen4:\n      ppl: 25.64\n      stable_rank: 40.47\n      spectral_entropy: 0.783\n      token_entropy: 1.736\n      hellaswag: 0.397\n    fullft_100pct_gen4:\n      ppl: 326.19\n      stable_rank: 153.87\n      spectral_entropy: 0.889\n      token_entropy: 0.829\n      hellaswag: 0.372\n    collapse_dynamics:\n      onset_ratio_gen01: 15.3\n      post_onset_ratio_gen14: 1.11\n      pattern: fast_onset_saturation\n      vs_qlora_gen4_ppl_ratio: 0.39\n    fullft_vs_qlora_comparison:\n      signals_not_qlora_specific: true\n      direction_consistent: 4/4 core signals same direction (SR↑, SE↑, TE↓, PPL↑)\n      sensitivity_ranking_consistent: PPL > stable_rank > token_entropy > spectral_entropy\n        (both methods)\n      structural_convergence_100pct_gen4:\n        stable_rank_fullft: 153.9\n        stable_rank_qlora: 155.6\n        spectral_entropy_fullft: 0.889\n        spectral_entropy_qlora: 0.884\n      cross_signal_spearman_direction: 6/6 pairs match\n      morphology_difference: 'FullFT: sudden gen1 15.3x PPL jump then plateau (+32\n        gen1-4); QLoRA: gradual (8.7x→2.9x→1.8x→1.2x)'\n      explanation: full parameter access → immediate catastrophic overfitting on corrupted\n        data; adapter-only → damage distributed across generations\n    output_files:\n    - analysis/fullft_vs_qlora_comparison.json\n    - analysis/fullft_vs_qlora_summary.md\n    - analysis/fullft_vs_qlora_trajectories.pdf\n    - analysis/fullft_vs_qlora_gen4_bars.pdf\n    - analysis/fullft_vs_qlora_collapse_morphology.pdf\n    - analysis/fullft_vs_qlora_structural_convergence.pdf\n- id: plan_004\n  claim: 2\n  description: Within-gen early warning analysis on 1.5B data. Compute signal divergence\n    at step 50/100/200/500 across all fractions and seeds from plan_001. Pure analysis,\n    no GPU.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Extends MVP within-gen analysis to 1.5B with proper statistics.\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Early warning threshold calibration: determine minimum signal deviation\n    that reliably predicts end-of-generation collapse. ROC analysis across all configs.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_002\n  registry_id: null\n  notes: Analysis only. MUST use clustered bootstrap (one obs per fraction×seed) or\n    restrict to single generation per run. Dream review flags pooling non-independent\n    generations as fatal methodology flaw.\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'Signal taxonomy across severity levels. Using plan_001 data, characterize\n    per-signal-family operating ranges: where each signal is most/least informative.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan006-signal-taxonomy\n  notes: Core table/figure for Claim 3. Shows stable_rank saturation, gradient non-monotonicity,\n    downstream failure. DONE (preliminary, N=2 seeds, 2 fractions). Rerun needed with\n    full data.\n  status: DONE\n  conclusion: success\n  metrics:\n    n_seeds: 3\n    n_fractions: 2\n    n_signals_analyzed: 14\n    ranking_method: Cohen's d at gen4\n    3seed_update:\n      top_signal_by_d: spectral_entropy (d=33.48)\n      tier1_signals: spectral_entropy (d=33.48), perplexity (d=20.82), distinct_1\n        (d=12.10), stable_rank (d=9.43), distinct_2 (d=9.38), distinct_3 (d=-6.25)\n      tier2_signals: token_entropy(-4.52), self_bleu(-3.54), gradient_norm(-2.39),\n        hellaswag(1.34)\n      stable_rank_warning: 'dropped rank 1→4 (d: 61.7→9.43), 2-seed d=61.7 was overfitted\n        due to seed44 variance (CV=0.022)'\n      most_stable_signal: spectral_entropy (CV=0.0015, lowest)\n      statistical_power: N=3 insufficient for Wilcoxon (min p=0.25); bootstrap 95%\n        CI lower bounds away from 0 for all Tier 1; hellaswag only CI crossing 0 [-1.4,\n        7.8]; need N≥5 for formal testing\n    incremental_check_20260516: No substantial change. N still 3 for 0% vs 50%. distinct\n      series N=2 (seed44 gen4 null). 0% vs 100% N=1 (seed42 only). Tier structure\n      unchanged. Next meaningful update when seed45+ frac=50% completes.\n    status_note: 3-seed incremental analysis complete. Full reanalysis at N=5 when\n      plan001 finishes.\n- id: plan_007\n  claim: 3\n  description: 'Per-layer collapse analysis: run forward-pass SVD on 1.5B model across\n    gens to show which layers collapse first and how layer-level patterns differ by\n    severity.'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Extends MVP per-layer analysis to 1.5B. Figure 3 candidate.\n  status: planned\n- id: plan_008\n  claim: 3\n  description: 'Self-recovery phenomenon deep dive: 50% contamination partial recovery\n    analysis. Is it consistent across seeds? At what fraction does recovery disappear?'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan008-self-recovery\n  notes: 'Analysis of plan_001 data at 25/50/75% fractions. Dream review: reclassify\n    25% as ''mild degradation/near-stability'' not ''strong recovery'' (PPL monotonically\n    increases). Position self-recovery as observation consistent with data mixing\n    literature (Gerstgrasser et al. 2024), not as novel discovery. DONE (preliminary,\n    3 fractions only). Rerun needed with full data.'\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_prevalence_50pct: 89% (16/18)\n    mean_ppl_recovery_ratio: 0.51\n    mean_token_entropy_rr: 0.624\n    mean_stable_rank_rr: 0.339\n    cross_seed_consistency: 5/6\n    residual_ppl_elevation: 6.6-7.8%\n    fractions_available:\n    - 0\n    - 50\n    - 100\n    n_sources: 3\n    3seed_update:\n      recovery_prevalence: 100% (9/9)\n      mean_ppl_recovery_ratio: 0.5245\n      ppl_rr_std: 0.027\n      cross_seed_consistency: 3/3\n      note: weight-space signals (stable_rank/spectral_entropy RR~0.32) recover slower\n        than output signals (PPL RR~0.52)\n    cross_domain_recovery_20260516:\n      wikitext_rr:\n        perplexity: 0.525 ± 0.026\n        stable_rank: 0.322 ± 0.051\n        spectral_entropy: 0.315 ± 0.020\n        token_entropy: 0.594 ± 0.128\n        gradient_norm: 1.220 ± 0.151\n      pubmed_rr:\n        perplexity: 0.405 ± 0.005\n        stable_rank: 0.178 ± 0.107\n        spectral_entropy: 0.152 ± 0.042\n        token_entropy: 0.442 ± 0.013\n        gradient_norm: 0.518 ± 0.028\n      delta: PubMed all signals lower (Δ -0.12 to -0.70)\n      pubmed_recovery_prevalence: 80% (8/10) vs WikiText 100%\n      pubmed_spectral_failure: spectral_entropy RR < 0.2 both seeds, stable_rank seed43\n        < 0.2\n      key_finding: Recovery is domain-dependent. PubMed (specialized domain) recovers\n        less — weight-space corruption more persistent. Output-vs-weight gap more\n        extreme in PubMed.\n      explanation: Specialized domain text has narrower distribution, making synthetic\n        corruption fingerprint harder to overwrite with real data training\n    cross_domain_incremental_seed43:\n      pubmed_n2_consistency: 'std extremely small (PPL 0%: ±0.005, 50%: ±0.015, 100%:\n        ±0.565)'\n      recovery_ratio_comparison:\n        perplexity:\n          pubmed: 0.9943\n          wikitext: 0.9981\n          pubmed_weaker: true\n        stable_rank:\n          pubmed: 0.9822\n          wikitext: 0.9814\n          pubmed_weaker: false\n          note: 差异在噪声内 (0.0008)\n        spectral_entropy:\n          pubmed: 0.8639\n          wikitext: 0.8796\n          pubmed_weaker: true\n        token_entropy:\n          pubmed: 0.9521\n          wikitext: 0.9711\n          pubmed_weaker: true\n      structural_vs_output_insight: '100% collapse: WikiText PPL 3.6x > PubMed, but\n        stable_rank/spectral_entropy nearly identical → structural collapse similar,\n        PPL difference reflects domain characteristics not collapse severity'\n      wikitext_n1_limitation: WikiText recovery ratio only N=1 (seed42), need seed43/44\n        100% to strengthen\n- id: plan_009\n  claim: 1\n  description: 'SIGMA head-to-head: SIGMA spectral metrics (log_det, effective_rank,\n    track_ii, spectral_decay_rate) integrated into signals.py for real-time collection\n    alongside plan_001 signals. Zero extra GPU overhead (shared H^T H matrix).'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan009-sigma-headtohead\n  notes: 'Dream review (all tiers): SIGMA differentiation is thinner than claimed.\n    Need head-to-head to clarify whether advantage is operational or fundamental.\n    Integrated into plan_001 signals.py (2026-05-14), real-time collection. 28/30\n    runs will have SIGMA data (2 seed=42 runs started before integration). RUNNING\n    — passive collection via plan001.'\n  status: DONE\n  conclusion: killed\n- id: plan_010\n  claim: 1\n  description: '3B model spot-check: Qwen2.5-3B × WikiText-2 × 3 fractions (0/50/100%)\n    × 1 seed. Adds a third scale point to strengthen cross-scale claims.'\n  priority: P2\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: plan010-3B-spotcheck\n  notes: 3B already downloaded on server. Low marginal cost. Addresses median/worst\n    tier concern that 2-point scale range (0.5B,1.5B) is too narrow. Only if GPU budget\n    permits.\n  status: RUNNING\n  metrics:\n    completed_fractions:\n      '0.0': 5 gens done, summary ✓\n      '0.5': 5 gens done, signals/ckpts ✓\n      '1.0': gen0 training 63% (964/1540), ~2.8s/step\n    pid: 255013\n    gpu: cuda:3\n    gpu_util: 100%\n    gpu_mem: 9.6/24.6 GB\n    server: cqa1-37219\n    eta: ~5.5h (gen0 remaining + gen1-4)\n    checked_at: 2026-05-16T08:24Z\n- id: plan_011\n  claim: 1\n  description: 'Cross-family validation: LLaMA-3.2-1B × WikiText-2 × 3 fractions (0/50/100%)\n    × 1 seed × 5 gens. Proves signals are not Qwen-specific.'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: null\n  notes: 'Addresses fatal reviewer concern: single model family. Pipeline adapted\n    (zero code change), model downloading. Run on autodl-5090 cuda:0 post-plan001.\n    If 8/11 signals direction-consistent → \"cross-family validated\". If divergent\n    → Discussion \"architecture-dependent behavior\" (still valuable).'\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'Full FT multi-seed: 0.5B × WikiText-2 × 3 fractions (0/50/100%) ×\n    2 additional seeds × 5 gens. Strengthens Full FT vs QLoRA comparison from N=1\n    to N=3.'\n  priority: P1\n  gpu_budget_hours: 40\n  deps:\n  - plan_003\n  registry_id: null\n  notes: 'Addresses reviewer concern: Full FT N=1 insufficient for method-dependence\n    claim. 2 new seeds × 3 fracs × 5 gens = 30 runs on 0.5B Full FT. Run on autodl-5090\n    cuda:1 or cqa1 post-plan001.'\n  status: planned\n- id: plan_013\n  claim: 2\n  description: 'MMLU-mini downstream evaluation: run MMLU-mini on all plan001 checkpoints\n    to add second downstream task beyond HellaSwag.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Pure inference, ~30s/checkpoint, total ~15 min for all ckpts. Script ready\n    (eval_mmlu_mini.py + run_mmlu_batch.sh), dry-run passed (36.06% accuracy). Addresses\n    \"downstream single benchmark\" concern.\n  status: planned\n- id: plan_014\n  claim: 2\n  description: 'Within-gen AUROC on C2 (1.5B 5-seed): recompute within-generation\n    binary AUROC using plan001 5-seed data. Upgrades Claim 2 from N=1 to N=5.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Clustered bootstrap by seed. Current within-gen AUROC=0.984 from C1 (0.5B,\n    N=1). Recomputing on C2 (1.5B, N=5) gives formal statistical claim. Script (plan005_within_gen_auroc_c2.py)\n    being written.\n  status: planned\n- id: plan_mvp_001\n  claim: 1\n  description: 'MVP: 0.5B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens'\n  priority: P0\n  gpu_budget_hours: 14.1\n  deps: []\n  registry_id: mvp_frac0\n  notes: Control baseline. DONE.\n  status: DONE\n  conclusion: success\n- id: plan_mvp_002\n  claim: 1\n  description: 'MVP: 0.5B × WikiText-2 × 50pct + 100pct × 1 seed × 5 gens'\n  priority: P0\n  gpu_budget_hours: 14.1\n  deps: []\n  registry_id: mvp_frac50_100\n  notes: Main MVP experiment. DONE. Gate check 2/3 PASS.\n  status: DONE\n  conclusion: success\n  metrics:\n    progress: ALL COMPLETE — 0pct 5/5, 50pct 5/5, 100pct 5/5\n    gate_check_verdict: PASS (3/3 families)\n    gate_check_spectral: PASS — stable_rank cross-frac |rho|=1.0 (p=0.0), cross-gen\n      rho=0.9 (p=0.037)\n    gate_check_output: PASS — perplexity cross-frac |rho|=1.0, cross-gen rho=1.0;\n      token_entropy cross-frac |rho|=0.9, cross-gen rho=-1.0\n    gate_check_downstream: PASS — hellaswag_acc cross-frac |ρ|=0.72 (mean gen1-4,\n      all negative), cross-gen ρ=-0.67 (100pct). Effect size small (0.41-0.44) but\n      direction consistent. Data present in summary JSONs. 0pct gen0 null.\n    hellaswag_values:\n      0pct:\n      - null\n      - 0.442\n      - 0.434\n      - 0.43\n      - 0.435\n      50pct:\n      - 0.435\n      - 0.429\n      - 0.42\n      - 0.439\n      - 0.434\n      100pct:\n      - 0.432\n      - 0.432\n      - 0.42\n      - 0.41\n      - 0.43\n    hellaswag_cross_frac_rho_per_gen:\n      gen1: -0.5\n      gen2: -0.866\n      gen3: -0.5\n      gen4: -1\n      mean: -0.7165\n    hellaswag_cross_gen_rho:\n      0pct: -0.4\n      50pct: 0.1\n      100pct: -0.667\n    final_values_0pct_gen4:\n      stable_rank: 23.41\n      spectral_entropy: 0.703\n      token_entropy: 2.259\n      ppl: 15.67\n    final_values_50pct_gen4:\n      stable_rank: 24.79\n      spectral_entropy: 0.716\n      token_entropy: 2.215\n      ppl: 16.95\n    final_values_100pct_gen4:\n      stable_rank: 155.64\n      spectral_entropy: 0.884\n      token_entropy: 0.782\n      ppl: 839.2\n    collapse_magnitude_100pct: stable_rank 6.6x, PPL 53x, token_entropy -65%\n    0pct_baseline_stability: all signals <3% variation across 5 gens\n    within_gen_early_warning: stable_rank 34.4% deviation at step 50 (3% training\n      progress)\n- id: plan_mvp_003\n  claim: 2\n  description: MVP within-gen temporal analysis on 0.5B data\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_mvp_002\n  registry_id: within_gen_analysis\n  notes: DONE. Early warning at 3% progress confirmed.\n  status: DONE\n  conclusion: success\n  metrics:\n    earliest_distinguishing_step: step 50 (3% training progress)\n    best_signal: stable_rank (34.4% deviation at step 50)\n    signals_above_5pct_at_step50: stable_rank 34.4%, token_entropy 24.5%, perplexity\n      17.7%\n    crossgen_acceleration: '100pct PPL delta vs per-gen 0pct baseline: gen0=<1%, gen1=+770%,\n      gen2=+2416%'\n    crossgen_acceleration_note: 'Corrected 2026-05-15: switched from within-gen start→end\n      metric to per-generation α=0 baseline comparison'\n    plots: 12 files (PDF+PNG) on server within_gen_plots/\n    plan004_15B_update:\n      strongest_early_signal: training_loss@step50 AUC=0.880, perplexity@step100 AUC=0.957\n      1.5B_vs_0.5B: stable_rank@step50 rel_div=0.206 (0.5B=0.344), 1.5B amplitude\n        smaller but still detectable\n      data_coverage: 4 seeds × 5 fracs × 5 gens = 1134 observations\n      output_files:\n      - analysis/divergence_table.csv\n      - analysis/detection_power.csv\n      - analysis/early_warning_heatmap.pdf\n      - analysis/divergence_curves.pdf\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_collapse_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    progress: 0pct_gen0 step 242/1540 (15.7%)\n    speed: 1.19 it/s\n    loss: 2.652\n    perplexity: 14.41\n    stable_rank: 20.5\n    spectral_entropy: 0.673\n    signals_collected: 4\n    checked_at: '2026-05-14T06:38:30Z'\n- exp_id: mvp_collapse_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 0pct_gen0 step 50/1540 (3%)\n    speed: 1.17 it/s\n    gpu_util: 26%\n    gpu_mem: 6314/32607 MiB\n    gen_batch_size: 32\n    gen_num_chunks: 1500\n    checked_at: '2026-05-14T08:21:00Z'\n- exp_id: mvp_collapse_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 0pct_gen0 step 50/1540 (3%)\n    speed: 1.08 it/s\n    gpu_util: 20%\n    gpu_mem: 6314/32607 MiB\n    checked_at: '2026-05-14T09:01:30Z'\n- exp_id: mvp_frac50_100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    progress: ALL COMPLETE — 0pct 5/5, 50pct 5/5, 100pct 5/5\n    gate_check_verdict: PASS (3/3 families)\n    gate_check_spectral: PASS — stable_rank cross-frac |rho|=1.0 (p=0.0), cross-gen\n      rho=0.9 (p=0.037)\n    gate_check_output: PASS — perplexity cross-frac |rho|=1.0, cross-gen rho=1.0;\n      token_entropy cross-frac |rho|=0.9, cross-gen rho=-1.0\n    gate_check_downstream: PASS — hellaswag_acc cross-frac |ρ|=0.72 (mean gen1-4,\n      all negative), cross-gen ρ=-0.67 (100pct). Effect size small (0.41-0.44) but\n      direction consistent. Data present in summary JSONs. 0pct gen0 null.\n    hellaswag_values:\n      0pct:\n      - null\n      - 0.442\n      - 0.434\n      - 0.43\n      - 0.435\n      50pct:\n      - 0.435\n      - 0.429\n      - 0.42\n      - 0.439\n      - 0.434\n      100pct:\n      - 0.432\n      - 0.432\n      - 0.42\n      - 0.41\n      - 0.43\n    hellaswag_cross_frac_rho_per_gen:\n      gen1: -0.5\n      gen2: -0.866\n      gen3: -0.5\n      gen4: -1\n      mean: -0.7165\n    hellaswag_cross_gen_rho:\n      0pct: -0.4\n      50pct: 0.1\n      100pct: -0.667\n    final_values_0pct_gen4:\n      stable_rank: 23.41\n      spectral_entropy: 0.703\n      token_entropy: 2.259\n      ppl: 15.67\n    final_values_50pct_gen4:\n      stable_rank: 24.79\n      spectral_entropy: 0.716\n      token_entropy: 2.215\n      ppl: 16.95\n    final_values_100pct_gen4:\n      stable_rank: 155.64\n      spectral_entropy: 0.884\n      token_entropy: 0.782\n      ppl: 839.2\n    collapse_magnitude_100pct: stable_rank 6.6x, PPL 53x, token_entropy -65%\n    0pct_baseline_stability: all signals <3% variation across 5 gens\n    within_gen_early_warning: stable_rank 34.4% deviation at step 50 (3% training\n      progress)\n- exp_id: mvp_frac0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: per_layer_analysis\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: per_layer_analysis_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 0pct gen0 1388/1540 (90%), ~2min to finish gen0\n    output_file: outputs/per_layer_analysis.json (incremental save per gen)\n    per_gen_time: ~35 min/gen\n    total_gens: 2 fractions x 5 gens = 10 gens\n    eta_total: ~6h from start (started ~18:19 UTC)\n    signals_safety: 'confirmed: output_dir redirected to _per_layer_tmp, signals_*.jsonl\n      untouched'\n    analysis_method: 'hook all transformer layers, 64 val samples forward pass, compute\n      per-layer SVD: stable_rank, spectral_entropy, SV_ratio(sigma1/sigma2)'\n    gpu: GPU 1, 6314/32607 MiB, 43% util\n    checked_at: '2026-05-14T18:58:00Z'\n- exp_id: per_layer_analysis_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: per_layer_analysis_active\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    progress: 0pct gen0=done, 0pct gen1=in_progress\n    per_gen_time: ~35 min/gen\n    eta_remaining: ~9 gens x 35min = ~5.25h\n    gpu: cuda:1\n    checked_at: '2026-05-14T19:08:00Z'\n- exp_id: per_layer_analysis_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: per_layer_analysis_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    boundary_early_sr_delta: 0.809\n    middle_sr_delta: DEPRECATED — was 0.01 based on incorrect data; real per-sub-module\n      mean ~0.66; see appendix tab:full_per_layer for true values\n    late_mid_sr_delta: 0.418\n    L12_down_proj_sr_collapse: -3.218\n    L11_down_proj_sr_collapse: -2.146\n    v_proj_avg_sr_increase: recalculate from appendix — significantly >1.334 across\n      all layers\n    k_proj_avg_sr_increase: 0.714\n    L0_qproj_sr_delta: 2.849\n    L16_vproj_sr_peak: 3.06\n    baseline_0pct_max_sr_drift: 0.311\n    weight_norm_crossover_layer: 11\n    narrative_revision: three-zone structure replaced by sub-module-centric analysis\n      per Director approval 2026-05-15\n- exp_id: within_gen_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    earliest_distinguishing_step: step 50 (3% training progress)\n    best_signal: stable_rank (34.4% deviation at step 50)\n    signals_above_5pct_at_step50: stable_rank 34.4%, token_entropy 24.5%, perplexity\n      17.7%\n    crossgen_acceleration: '100pct PPL delta vs per-gen 0pct baseline: gen0=<1%, gen1=+770%,\n      gen2=+2416%'\n    crossgen_acceleration_note: 'Corrected 2026-05-15: switched from within-gen start→end\n      metric to per-generation α=0 baseline comparison'\n    plots: 12 files (PDF+PNG) on server within_gen_plots/\n    plan004_15B_update:\n      strongest_early_signal: training_loss@step50 AUC=0.880, perplexity@step100 AUC=0.957\n      1.5B_vs_0.5B: stable_rank@step50 rel_div=0.206 (0.5B=0.344), 1.5B amplitude\n        smaller but still detectable\n      data_coverage: 4 seeds × 5 fracs × 5 gens = 1134 observations\n      output_files:\n      - analysis/divergence_table.csv\n      - analysis/detection_power.csv\n      - analysis/early_warning_heatmap.pdf\n      - analysis/divergence_curves.pdf\n- exp_id: plan_001_wikitext_1.5B_5seeds\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_002_pubmed_1.5B_3seeds\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_001_wikitext_15B_5seeds\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan001-wikitext-15B-5seeds\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    gpu0_status: 已重启 submit_training_job, timeout=48h. seed42 frac=0.25 加载中 (skip\n      frac=0.0 ✓)\n    gpu1_status: PID running, seed42 frac=1.0 step ~1068/1540 (69%), 正常\n    completed_seeds:\n      seed42: frac=0.0 ✓, frac=0.5 ✓, frac=1.0 gen4 69%\n      seed43: frac=0.0 ✓, frac=0.5 ✓\n      seed44: frac=0.0 ✓, frac=0.5 ✓\n      seed45: frac=0.0 gen4 synth 中断(被kill), 待 GPU0 轮到时自动补完\n      seed46: not started\n    v2_allocation:\n      gpu0: fractions (0.0, 0.25, 0.1) × seeds 42-46\n      gpu1: fractions (0.5, 1.0, 0.75) × seeds 42-46\n    runs_completed: 6/30 (v2 total)\n    gpu0_restart:\n      time: 2026-05-15T23:01Z\n      timeout_hours: 48\n      reason: seed45 frac=0.0 gen4 synth killed\n    disk: 18G/250G (7%)\n    checked_at: 2026-05-15T23:02Z\n- exp_id: plan001-wikitext-15B-5seeds-gpu1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-gpu1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    current_run: frac=0.5, seed=44, gen4 training ~10% (~25min left)\n    completed_seeds:\n      seed42: DONE (summary_50pct.json ✓)\n      seed43: DONE (summary_50pct.json ✓)\n      seed44: gen4 ~10%, then gen5 remaining, then seed45+46\n    auto_advance_confirmed: true\n    gpu_util: 100%\n    gpu_mem: 7984 MiB\n    gpu_temp: 65C\n    note: seed45 will auto-load hotfixed pipeline.py — no intervention needed\n    checked_at: 2026-05-15T16:42Z\n- exp_id: plan002-pubmed-cqa1\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    gpu0_status: seed42 frac=10%, gen2 training 11% (156/1410)\n    gpu1_status: seed42 frac=75%, gen1 training 99% (1400/1410)\n    gpu2_status: seed44 frac=100%, gen0 synthetic 21%\n    fraction_coverage:\n      completed:\n        '0.0':\n        - seed42\n        - seed43\n        - seed44\n        '0.5':\n        - seed42\n        - seed43\n        - seed44\n        '1.0':\n        - seed42\n        - seed43\n      in_progress:\n        '0.1': seed42 gen2 (GPU0)\n        '0.75': seed42 gen1 (GPU1)\n        '1.0': seed44 gen0 (GPU2)\n      not_started:\n      - '0.25'\n    gpu_eta:\n      cuda2_free: ~4h (seed44 frac=100%)\n      cuda1_free: ~13h\n      cuda0_free: ~18-27h\n    disk: 86G/250G (35%)\n    checked_at: 2026-05-16T08:24Z\n- exp_id: plan003-fullft-05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fullft_0pct_gen4:\n      ppl: 19.23\n      stable_rank: 37.48\n      spectral_entropy: 0.765\n      token_entropy: 1.884\n    fullft_50pct_gen4:\n      ppl: 25.64\n      stable_rank: 40.47\n      spectral_entropy: 0.783\n      token_entropy: 1.736\n      hellaswag: 0.397\n    fullft_100pct_gen4:\n      ppl: 326.19\n      stable_rank: 153.87\n      spectral_entropy: 0.889\n      token_entropy: 0.829\n      hellaswag: 0.372\n    collapse_dynamics:\n      onset_ratio_gen01: 15.3\n      post_onset_ratio_gen14: 1.11\n      pattern: fast_onset_saturation\n      vs_qlora_gen4_ppl_ratio: 0.39\n    fullft_vs_qlora_comparison:\n      signals_not_qlora_specific: true\n      direction_consistent: 4/4 core signals same direction (SR↑, SE↑, TE↓, PPL↑)\n      sensitivity_ranking_consistent: PPL > stable_rank > token_entropy > spectral_entropy\n        (both methods)\n      structural_convergence_100pct_gen4:\n        stable_rank_fullft: 153.9\n        stable_rank_qlora: 155.6\n        spectral_entropy_fullft: 0.889\n        spectral_entropy_qlora: 0.884\n      cross_signal_spearman_direction: 6/6 pairs match\n      morphology_difference: 'FullFT: sudden gen1 15.3x PPL jump then plateau (+32\n        gen1-4); QLoRA: gradual (8.7x→2.9x→1.8x→1.2x)'\n      explanation: full parameter access → immediate catastrophic overfitting on corrupted\n        data; adapter-only → damage distributed across generations\n    output_files:\n    - analysis/fullft_vs_qlora_comparison.json\n    - analysis/fullft_vs_qlora_summary.md\n    - analysis/fullft_vs_qlora_trajectories.pdf\n    - analysis/fullft_vs_qlora_gen4_bars.pdf\n    - analysis/fullft_vs_qlora_collapse_morphology.pdf\n    - analysis/fullft_vs_qlora_structural_convergence.pdf\n- exp_id: plan010-3B-spotcheck\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    completed_fractions:\n      '0.0': 5 gens done, summary ✓\n      '0.5': 5 gens done, signals/ckpts ✓\n      '1.0': gen0 training 63% (964/1540), ~2.8s/step\n    pid: 255013\n    gpu: cuda:3\n    gpu_util: 100%\n    gpu_mem: 9.6/24.6 GB\n    server: cqa1-37219\n    eta: ~5.5h (gen0 remaining + gen1-4)\n    checked_at: 2026-05-16T08:24Z\n- exp_id: plan_001_seed42_frac0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    status: DONE\n    gpu: 0\n    server: autodl-5090\n    model: Qwen2.5-1.5B\n    dataset: wikitext\n    mode: qlora\n    seed: 42\n    fraction: 0\n    generations_done: 5\n    final_ppl: 12.2\n    final_hellaswag: 0.518\n    checked_at: 2026-05-15T19:05\n- exp_id: plan_001_seed42_frac50\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    status: DONE\n    gpu: 1\n    server: autodl-5090\n    model: Qwen2.5-1.5B\n    dataset: wikitext\n    mode: qlora\n    seed: 42\n    fraction: 0.5\n    generations_done: 5\n    final_ppl: 13.03\n    final_hellaswag: 0.524\n    checked_at: 2026-05-15T19:05\n- exp_id: plan_001_seed43_frac0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    status: RUNNING\n    gpu: 0\n    server: autodl-5090\n    model: Qwen2.5-1.5B\n    dataset: wikitext\n    mode: qlora\n    seed: 43\n    fraction: 0\n    current_gen: 4\n    phase: generating_synthetic_96pct\n    gpu_util_pct: 34\n    gpu_mem_mb: 4270\n    gpu_temp_c: 56\n    pid: 609739\n    checked_at: 2026-05-15T19:05\n- exp_id: plan_001_seed43_frac50\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    status: RUNNING\n    gpu: 1\n    server: autodl-5090\n    model: Qwen2.5-1.5B\n    dataset: wikitext\n    mode: qlora\n    seed: 43\n    fraction: 0.5\n    current_gen: 4\n    phase: generating_synthetic_96pct\n    gpu_util_pct: 100\n    gpu_mem_mb: 7984\n    gpu_temp_c: 64\n    pid: 617434\n    checked_at: 2026-05-15T19:05\n- exp_id: plan009-sigma-headtohead\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan006-signal-taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_seeds: 3\n    n_fractions: 2\n    n_signals_analyzed: 14\n    ranking_method: Cohen's d at gen4\n    3seed_update:\n      top_signal_by_d: spectral_entropy (d=33.48)\n      tier1_signals: spectral_entropy (d=33.48), perplexity (d=20.82), distinct_1\n        (d=12.10), stable_rank (d=9.43), distinct_2 (d=9.38), distinct_3 (d=-6.25)\n      tier2_signals: token_entropy(-4.52), self_bleu(-3.54), gradient_norm(-2.39),\n        hellaswag(1.34)\n      stable_rank_warning: 'dropped rank 1→4 (d: 61.7→9.43), 2-seed d=61.7 was overfitted\n        due to seed44 variance (CV=0.022)'\n      most_stable_signal: spectral_entropy (CV=0.0015, lowest)\n      statistical_power: N=3 insufficient for Wilcoxon (min p=0.25); bootstrap 95%\n        CI lower bounds away from 0 for all Tier 1; hellaswag only CI crossing 0 [-1.4,\n        7.8]; need N≥5 for formal testing\n    incremental_check_20260516: No substantial change. N still 3 for 0% vs 50%. distinct\n      series N=2 (seed44 gen4 null). 0% vs 100% N=1 (seed42 only). Tier structure\n      unchanged. Next meaningful update when seed45+ frac=50% completes.\n    status_note: 3-seed incremental analysis complete. Full reanalysis at N=5 when\n      plan001 finishes.\n- exp_id: plan008-self-recovery\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_prevalence_50pct: 89% (16/18)\n    mean_ppl_recovery_ratio: 0.51\n    mean_token_entropy_rr: 0.624\n    mean_stable_rank_rr: 0.339\n    cross_seed_consistency: 5/6\n    residual_ppl_elevation: 6.6-7.8%\n    fractions_available:\n    - 0\n    - 50\n    - 100\n    n_sources: 3\n    3seed_update:\n      recovery_prevalence: 100% (9/9)\n      mean_ppl_recovery_ratio: 0.5245\n      ppl_rr_std: 0.027\n      cross_seed_consistency: 3/3\n      note: weight-space signals (stable_rank/spectral_entropy RR~0.32) recover slower\n        than output signals (PPL RR~0.52)\n    cross_domain_recovery_20260516:\n      wikitext_rr:\n        perplexity: 0.525 ± 0.026\n        stable_rank: 0.322 ± 0.051\n        spectral_entropy: 0.315 ± 0.020\n        token_entropy: 0.594 ± 0.128\n        gradient_norm: 1.220 ± 0.151\n      pubmed_rr:\n        perplexity: 0.405 ± 0.005\n        stable_rank: 0.178 ± 0.107\n        spectral_entropy: 0.152 ± 0.042\n        token_entropy: 0.442 ± 0.013\n        gradient_norm: 0.518 ± 0.028\n      delta: PubMed all signals lower (Δ -0.12 to -0.70)\n      pubmed_recovery_prevalence: 80% (8/10) vs WikiText 100%\n      pubmed_spectral_failure: spectral_entropy RR < 0.2 both seeds, stable_rank seed43\n        < 0.2\n      key_finding: Recovery is domain-dependent. PubMed (specialized domain) recovers\n        less — weight-space corruption more persistent. Output-vs-weight gap more\n        extreme in PubMed.\n      explanation: Specialized domain text has narrower distribution, making synthetic\n        corruption fingerprint harder to overwrite with real data training\n    cross_domain_incremental_seed43:\n      pubmed_n2_consistency: 'std extremely small (PPL 0%: ±0.005, 50%: ±0.015, 100%:\n        ±0.565)'\n      recovery_ratio_comparison:\n        perplexity:\n          pubmed: 0.9943\n          wikitext: 0.9981\n          pubmed_weaker: true\n        stable_rank:\n          pubmed: 0.9822\n          wikitext: 0.9814\n          pubmed_weaker: false\n          note: 差异在噪声内 (0.0008)\n        spectral_entropy:\n          pubmed: 0.8639\n          wikitext: 0.8796\n          pubmed_weaker: true\n        token_entropy:\n          pubmed: 0.9521\n          wikitext: 0.9711\n          pubmed_weaker: true\n      structural_vs_output_insight: '100% collapse: WikiText PPL 3.6x > PubMed, but\n        stable_rank/spectral_entropy nearly identical → structural collapse similar,\n        PPL difference reflects domain characteristics not collapse severity'\n      wikitext_n1_limitation: WikiText recovery ratio only N=1 (seed42), need seed43/44\n        100% to strengthen\n- exp_id: plan002-pubmed-gpu2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    current_run: seed43 frac=1.0 gen1 training ~50%\n    completed:\n      seed42: frac=1.0 all 5 gens done (summary ✓)\n    remaining: seed43 ~4 gens + seed44 5 gens = ~9 gens\n    gpu_util: 54%\n    gpu_mem: 7567/24564 MiB\n    eta: ~2026-05-16T11:30Z\n    note: GPU2 是 plan002 瓶颈。GPU0/GPU1 ~3.5h 后空闲,可考虑分担 seed44 frac=1.0\n    checked_at: 2026-05-16T02:43Z\n- exp_id: plan001_v2_gpu0\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    gpu0_status: seed42 frac=0.1 gen2 training 88% (1350/1540)\n    gpu1_status: seed43 frac=1.0 gen2 training 34% (518/1540)\n    gpu0_util: 37%\n    gpu1_util: 33%\n    gpu0_mem: 7.6/31.8 GB\n    gpu1_mem: 7.6/31.8 GB\n    completion_table:\n      seed42:\n        '0.0': done\n        '0.1': gen2 88%\n        '0.25': done\n        '0.5': done\n        '0.75': done\n        '1.0': done\n      seed43:\n        '0.0': done\n        '0.5': done\n        '1.0': gen2 34%\n      seed44:\n        '0.0': done\n        '0.5': done\n      seed45:\n        '0.0': done\n      seed46: {}\n    runs_completed: 10/30 (33%)\n    runs_in_progress: 2\n    runs_remaining: 18\n    disk: 38G/250G (16%)\n    checked_at: 2026-05-16T08:23Z\n- exp_id: plan001-cqa1-seed46\n  name: ''\n  status: ALLOCATED\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001-cqa1-seed44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001-cqa1-seed45\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan002-pubmed-gpu2-tail\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: Tail-end monitoring of plan002 GPU2. PID 423689 exited. Full diagnostic\n      pending.\n    checkpoint_path: N/A\n    log_path: /tmp/plan002_gpu2.log\n- exp_id: plan011-llama-download\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model_path: /root/autodl-tmp/models/Llama-3.2-1B/LLM-Research/Llama-3.2-1B\n    model_size_gb: 2.4\n    params_b: 1.24\n    vocab_size: 128000\n    hidden_size: 2048\n    num_layers: 16\n    model_type: llama\n    verification: transformers load SUCCESS\n    launch_script: run_plan011_llama.sh ready\n    download_log: /tmp/llama_ms_v5.log\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T10:08:04.964Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T10:08:04.964Z",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T10:08:04.992Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：plan001 严重不完整（≤10 runs）；1.5B 未复现 0.5B 的 within-gen 发现；seed 方差摧毁信号排名稳定性；LLaMA 方向不一致或未跑；需要 reframe 但不降级 venue
核心假设：['plan001 仅完成 ≤10/30 runs（基本停留在当前状态），5-seed 统计不可行', '1.5B within-gen AUC 显著低于 0.5B（stable_rank AUC < 0.80），early warning 不跨 scale', '6-fraction ρ 因 seed 方差和非单调 fraction 行为降至 < 0.85', 'stable_rank 5-seed（实际 3-seed）CV > 0.06，排名进一步不稳定（从 rank 4 继续下跌）', 'LLaMA 未完成 或 < 6/11 信号方向一致（core signal 如 stable_rank 方向相反）', 'PPL within-gen AUC 在 1.5B 反而有效（AUC > 0.70），破坏 "PPL fails" 叙事', '3B spot-check 某 core signal 方向不一致', 'Full FT 对比仍为 N=1，无法支撑 method-dependence claim', 'PubMed 3-seed 勉强完成但信号行为与 WikiText 差异大于预期']
关键指标范围：{'spearman_rho_median_across_seeds': [0.7, 0.85], 'within_gen_auc_stable_rank_1.5B': [0.6, 0.8], 'within_gen_auc_ppl_1.5B': [0.5, 0.75], 'within_gen_auc_training_loss_1.5B': [0.65, 0.8], 'cohens_d_spectral_entropy_5seed': [8.0, 18.0], 'cohens_d_perplexity_5seed': [5.0, 12.0], 'cohens_d_stable_rank_5seed': [2.0, 6.0], 'stable_rank_cv_across_seeds': [0.06, 0.12], 'llama_signal_direction_consistency': [3, 6], 'scale_3B_core_direction_match': [2, 3], 'plan001_runs_completed': [6, 12], 'pubmed_recovery_prevalence': [0.4, 0.65]}
叙事方向：核心假设 "signals reliably track collapse across configs" 不成立——信号行为高度  config-dependent，排名不稳定。Reframe 方向：从 "practitioners can use signal X"  转为 "we document the surprising fragility of training-time collapse signals"。 新 angle："Collapse monitoring is harder than it looks"——同一信号在不同 scale/seed/method  下表现迥异，这本身是对 practitioner 的重要警告。Claim 1 从 "correlation" 改为 "conditional  correlation"（仅在特定配置下成立）。Claim 2 从 "early warning" 改为 "scale-dependent  early warning"（0.5B 有效但不泛化到 1.5B，暗示大模型需要不同的检测策略）。Claim 3 成为论文 核心——从辅助 claim 升级为主 claim："signal behavior is fundamentally configuration-dependent,  and the field's implicit assumption that collapse signals transfer across settings is wrong"。 如果 PPL within-gen AUC 在 1.5B 升高，则 "PPL fails" 叙事反转为 "PPL's effectiveness  is scale-dependent"——仍是有价值的发现。LLaMA 不一致则写 "architecture-dependent signal  behavior" 作为 finding 而非 limitation。论文 reframe 为 negative-result + taxonomy paper， 仍冲 EMNLP（EMNLP 历来接收高质量 negative results），但大概率推迟到 ARR 6/15。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: collapse_severity_monitor
focus: 当前 plan 已扩展到 cross-family (LLaMA) + MMLU-mini + Full FT 3-seed + scale-dependent within-gen finding。重点评估：(1) cross-family spot-check (N=1) 是否足够回应 "architecture-specific" 质疑；(2) scale-dependent signal ranking 是加强还是削弱 Claim 2；(3) ��体 scope 升级后能否支撑 EMNLP ARR 接收

## paper_framing.md

# Paper Framing — collapse_severity_monitor

## Target Venue
- Primary: EMNLP 2026 via ACL Rolling Review (ARR)
- Deadline: ARR submission 2026-05-25
- Backup: ARR June cycle (2026-06-15) if 5/25 not feasible

## Core Claims (3 条)

1. **Signal-Severity Correlation**: Spectral signals (stable rank, spectral entropy) and output signals (token entropy, perplexity) reliably track model collapse severity across synthetic data contamination levels, maintaining monotonic ordering across tested fractions and generations. (MVP: ρ=1.0 with n=3; to be validated with n=6 fractions × 5 seeds in plan_001. Primary evidence: Spearman ρ with bootstrap CIs; effect sizes elevated as primary evidence, ρ as supporting.)

2. **Early Warning Capability**: Collapse can be detected at moderate contamination (50%) within a single training run: stable rank achieves AUC=0.984 [0.978, 0.989] for within-gen collapse detection, reaching AUC=0.94 (sens=0.78, spec=1.00) at just 10% training progress. Training loss is the second-best within-gen detector (AUC=0.923). ROC analysis must use clustered bootstrap (one observation per fraction×seed) to avoid inflating AUC from serial generation dependence. **Featured sub-result: held-out evaluation perplexity — the metric practitioners most commonly check at eval checkpoints — provides no within-generation early warning (AUC=0.534 ≈ random).** This is because held-out PPL requires multi-generation accumulation before collapse manifests; in contrast, train-set loss (AUC=0.923) detects earlier because it directly measures learning dynamics on the contaminated distribution. Claim 2 Results 段落结构：(a) stable_rank early detection 正面证据, (b) 专门 1 段讨论 PPL within-gen 失效 + 原理解释 + AUC 对比, (c) ROC curves 图。Abstract 加半句："notably, held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.53)"。(Note: stable_rank is seed-sensitive but early-detecting; spectral_entropy is seed-robust but late-detecting (only at 100%). Practitioner recommendation: use stable_rank for within-gen early warning, perplexity for cross-gen severity comparison, spectral_entropy for severity discrimination. Cross-validation needed: plan001 5-seed + plan002 PubMed within-gen ROC, 如果多配置 PPL AUC 一致 ~0.5，camera-ready 可升级措辞。See writing notes 17, 18, 19.)

3. **Non-Uniform Signal Behavior**: The same monitoring signal can be informative under one training method and misleading under another. Spectral signals saturate at extreme severity; gradient norm is non-monotonic under QLoRA but monotonic under Full FT; downstream metrics (HellaSwag) track collapse under Full FT but remain stable under QLoRA. Both methods show large gen1 PPL jumps (Full FT 15.3x, QLoRA 8.7x) but diverge in subsequent evolution: Full FT saturates (gen1→4: 1.11x), QLoRA decelerates but continues (gen1→4: 6.13x). Featured sub-result: PPL-downstream dissociation — QLoRA PPL=839 but hellaswag=0.430 vs Full FT PPL=326 but hellaswag=0.372, meaning PPL-based monitoring overestimates damage under QLoRA and practitioners must consider training method when selecting collapse signals. Terminal spectral convergence (SR ~154-156) noted as observation, not claimed as finding (N=1). Signal taxonomy table should include "method-dependence" column.

## Story Spine

- **Problem**: Model collapse from iterative training on synthetic data is a growing concern as LLM-generated text pervades training corpora. While the phenomenon is well-characterized theoretically (Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024), practitioners lack actionable tools to detect and quantify collapse severity during training. Current work focuses on post-hoc analysis or output-level detection, missing the rich signal available in training dynamics.

- **Existing approaches & gaps**: SIGMA (2025) monitors output embedding spectral properties but requires access to a clean reference distribution (plan_009 adds head-to-head to clarify operational vs fundamental advantage). Kalinowski (2024) uses topological analysis but is computationally expensive. Data mixing strategies (Gerstgrasser et al. 2024, Kazdan et al. 2024) study prevention rather than detection. Neither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they examine within-generation temporal dynamics for early warning.

- **Our framing**: We conduct a systematic empirical analysis of training dynamic signals as collapse severity monitors. Across 4 signal families (spectral, output, gradient, downstream) × 6 contamination levels × 2 model scales × 2 domains × 2 fine-tuning methods, we characterize which signals track collapse, when they diverge, and where they fail. Key insight: stable rank provides the earliest within-gen warning (AUC=0.94 at 10% training progress) while perplexity provides the most reliable cross-generation severity tracking — but these roles are non-interchangeable. We document a partial self-recovery phenomenon at moderate contamination consistent with known data mixing effects (Gerstgrasser et al. 2024), and characterize where standard monitoring signals mislead practitioners.

- **Headline result template**: "Stable rank detects within-generation collapse with AUC=0.984, reaching actionable sensitivity (AUC=0.94) at 10% training progress. Across generations, spectral entropy provides the most robust severity discrimination (CV=0.0015) but is a late detector (only at 100% contamination). Held-out evaluation perplexity — often the go-to metric at eval checkpoints — is nearly ineffective for within-generation detection (AUC=0.534), while train-set loss detects data distribution shift (AUC=0.923) but not model quality degradation; evaluation perplexity remains the strongest cross-generation severity tracker. Different signals have complementary operating ranges; no single signal suffices across all detection contexts." (Note: ρ ≥ 0.94 是 plan001 验证目标，非当前实际数值，到手前用 effect size 表述。分层信号策略替代单一 headline signal。ROC 数据来自 plan005 within-gen 分析，N=1 seed。)

## Anticipated Reviewer Concerns & Mitigation

| Concern | Severity | Mitigation |
|---------|----------|------------|
| Statistical power (seeds) | CRITICAL | 5 seeds WikiText, 3 seeds PubMed; bootstrap CIs for all claims |
| n=3 fractions → trivial ρ=1.0 | HIGH | 6 fractions (0/10/25/50/75/100%) |
| Single model scale | HIGH | 0.5B + 1.5B (+ 3B spot-check if GPU permits) |
| Single dataset | HIGH | WikiText-2 + PubMed (3 seeds each) |
| QLoRA only | MEDIUM | Full FT comparison on 1 config (plan_003) |
| ROC pools non-independent observations | HIGH | Clustered bootstrap or one-gen-per-run restriction (plan_005) |
| Stable rank direction under collapse | MEDIUM | Clarify: ‖W‖_F² grows faster than σ₁² → SR increases = energy dispersal, not concentration. Fix text |
| No theoretical grounding | MEDIUM | Informal argument: 75% phase transition ↔ distributional shift theory; when spectral monitoring fails (capacity redundancy) |
| "First" claims overclaimed | MEDIUM | Qualify: "first systematic multi-axis comparison in iterative fine-tuning setting." Self-recovery → cite Gerstgrasser et al. |
| SIGMA differentiation thin | MEDIUM | Head-to-head (plan_009): run SIGMA at training checkpoints |
| Related work too thin | HIGH | ≥20 refs: Briesch 2023, Hataya 2023, Gerstgrasser 2024, Seddik 2024, Dohmatob "Tale of Tails" 2024, Pennington & Worah 2017 |
| Missing synthetic data gen params | LOW | Document temperature, top-p/k, max length, prompt format in Methods |
| No code/data release | MEDIUM | Release monitoring toolkit + signal trajectories + generation scripts |
| "Not a monitoring system" | LOW | Frame as analysis paper; taxonomy + early warning = practical value |
| No intervention/mitigation | LOW | Explicit non-goal; future work |

## Core Insight (一句话)

Training dynamic signals provide a free, model-agnostic early warning system for model collapse — but different signal families have distinct operating ranges, and practitioners need to know which signal to trust at which severity level.

## Novelty Statement

We provide the first systematic multi-axis comparison of training-time signal families as collapse severity monitors, spanning contamination levels, model scales, text domains, and fine-tuning methods. The within-generation early warning capability (stable rank AUC=0.94 at 10% training progress), the signal operating-range taxonomy, and the documentation of where standard monitoring signals actively mislead practitioners are the primary empirical contributions. The self-recovery observation at moderate contamination is consistent with known data mixing effects and is positioned as a finding rather than a novel phenomenon.

## Key Writing Notes (from Dream review, 2026-05-14)

1. **Effect sizes > ρ**: Elevate effect size tables as primary evidence; ρ as supporting.
2. **Stable rank direction**: SR increases under collapse = energy dispersal (Frobenius norm grows faster than spectral norm), not concentration. Fix text.
3. **25% contamination**: "mild degradation / near-stability", NOT "strong recovery" (PPL monotonically increases).
4. **Figures required**: Severity curves, ROC curves, heatmaps, per-layer propagation. Analysis paper without figures is a major gap.
5. **Reproducibility**: Code release, signal trajectories, generation scripts for D&B track.
6. **Collapse protocol**: Explicitly state whether fine-tuning from M₀ or M_{g-1} and discuss implications.
7. **Per-layer 叙事修正 (D011, 2026-05-15)**: 废弃"三区结构"（boundary/middle-neutral/late-bifurcation），改为 sub-module-centric 分析。真实数据显示 v_proj 在几乎所有层 diffuse（ΔSR +1~+3），down_proj 在 L11-L12 局部 collapse，其余子模块温和。Practitioner takeaway: 优先监控 v_proj stable rank 作为最敏感的 within-run collapse indicator。（注：cross-seed 稳定性另论，参见写作笔记 16。within-run 灵敏度与 cross-seed 排名是不同维度。）
8. **SIGMA 方向 provisional (C001/D014, 2026-05-15)**: expected_direction=+1（effective_rank 在 collapse 时上升）是 N=2 观测，非已验证结论。禁止在论文中当发现写。验证条件：plan_001 seed43-46 全量数据 + plan_003 Full FT SIGMA 数据。如果 Full FT 方向一致(+1)可排除 QLoRA confound；如果不一致需重写分析。"Within-gen corruption vs recursive collapse 方向差异"作为 discussion 论点需要等验证后才能使用。
9. **Non-monotonic claim scope (plan008/plan003, 2026-05-15)**: "Non-monotonic" 仅适用于 frac=50% 的 plateau 行为（ppl 26.9→25.6→25.7→25.6，真正收敛）。frac=100% gen1→gen2 的 -1.9% 下降（294→288）是噪声级波动，N=1 无法区分，禁止称为 "non-monotonic pattern"。100% 的正确描述："catastrophic jump at gen1 followed by continued degradation"。
10. **HellaSwag method-dependence + 归因修正 (plan003, 2026-05-15; 合并原 Note 10+13)**: HellaSwag 追踪 collapse 能力取决于训练方法（Full FT: 有效, -12.5%；QLoRA: 无效/稳定）。D015/D017 的"0.5B 失效"诊断错误——失效的是 QLoRA 的隐式正则化，非模型规模。论文归因必须是 method 而非 scale。反直觉：QLoRA gen4 PPL (839) > Full FT gen4 PPL (326)，但 QLoRA hellaswag (0.430) > Full FT hellaswag (0.372)——PPL 不是下游质量的唯一预测器。
11. **Collapse trajectory: 两种方法都 gen1 大跳，差异在后续 (plan003, 2026-05-15; D026 修正 D024)**: Full FT gen1=15.3x 后饱和（gen1→4: 1.11x）；QLoRA gen1=8.7x 后减速增长（gen1→4: 6.13x，gen4 PPL=839）。**禁止**使用 "slow onset" / "snowball" / "exponential" 描述 QLoRA——QLoRA gen1 也是大跳（8.7x），不是缓慢起步。正确叙事：两种方法初始冲击程度不同（Full FT 更剧烈），后续演化模式不同（饱和 vs 减速增长）。终态谱收敛（SR ~154 vs ~156）需用正确数据重新验证后方可使用。
12. **Diversity 指标对 collapse 不敏感 (plan003, 2026-05-15)**: distinct_1 在 Full FT frac=100% 仅 -3%（0.0925→0.0897），self_bleu 几乎不变，即使 PPL 暴涨 17x。原因：collapsed model 输出分布坍缩到少数 token（token_entropy -55%），但采样随机性维持了 lexical diversity 的表面指标。论文中需明确将 diversity 族排除在有效 collapse indicator 之外，或专门讨论 entropy vs diversity 解耦现象。
13. *[已合并到 Note 10]*
14. **Claim 3 措辞升级方向 (Reviewer 评估, 2026-05-15)**: 从 "different signals respond differently" 升级为 "the same signal can be informative under one training method and misleading under another"——直击 practitioner pain point。PPL-downstream dissociation 作为 Claim 3 featured sub-result（1 段专门讨论），不独立成 claim（N=1 seed, 1 downstream task, 无法排除 HellaSwag ceiling/floor effect）。Signal taxonomy table 加 "method-dependence" 列。Abstract 用一句："perplexity and downstream metrics can diverge under parameter-efficient FT, cautioning against single-signal monitoring"。Terminal spectral convergence 降级为 observation（N=1 无法区分"收敛"和"碰巧接近"）。Limitations 必须标注 Full FT 对比的 N=1 限制。
15. **Self-recovery prevalence 对比禁令 (Reviewer, 2026-05-16)**: 3-seed 的 9/9=100% vs plan008 的 16/18=89% 不可比——前者仅用 3 个信号（PPL, stable_rank, spectral_entropy），后者用 6 个信号。选取的恰好是最一致的信号。论文中讨论 self-recovery 时必须标注信号覆盖范围，禁止跨不同信号集做 prevalence 对比。
16. **Signal ranking instability: stable_rank seed-sensitive (plan006/008 3-seed update, 2026-05-16)**: 3-seed 数据显示 stable_rank 的 Cohen's d 从 61.7 暴跌到 9.43（rank 1→4），原因是 seed44 引入 frac=50% 方差（CV=0.022）。spectral_entropy 最稳定（CV=0.0015，d=33.48，rank 2→1）。**禁止**在论文中将 stable_rank 定位为"最敏感信号"——正确叙事见写作笔记 17 分层策略。最终 taxonomy ranking 需等 plan001 5-seed 数据确认。
17. **分层信号策略（Signal Heatmap 发现, 2026-05-16; 修正 D029）**: spectral_entropy 虽 cross-seed 最稳定（d=33.48, CV=0.0015），但是 **late detector**——仅在 frac=100% 下显著（Δ+25.7%），frac=50% 下 effect size < 5%。stable_rank 和 perplexity 是 **early detectors**（50% 即可检出：SR +564.8%, PPL +5255%）。**禁止**推单一 headline signal。正确叙事："signals have complementary operating ranges"——stable_rank + perplexity 用于 early warning（Claim 2），spectral_entropy 用于 severity discrimination（区分 50% vs 100%）。这个分层发现本身就是 Claim 3 taxonomy 的核心价值：no single signal suffices。6/7 信号方向跨 QLoRA/Full FT 一致，强化 Claim 1 泛化性。
18. **Within-gen ROC 证据精确化 Claim 2（plan005 ROC 分析, 2026-05-16; 修正写作笔记 17 的 perplexity 角色）**: ROC 分析揭示信号在 within-gen vs cross-gen 两个维度的能力完全不同。stable_rank 是 within-gen 最强检测器（AUC=0.984, 10% progress 即达 AUC=0.94）；training_loss 次之（AUC=0.923）；**perplexity within-gen 几乎无效（AUC=0.534）**——但 cross-gen 仍是最强 severity tracker。spectral_entropy within-gen 非单调（20% progress 时 AUC 降到 0.30，方向翻转），**不适合 threshold-based 早期检测**。这修正了写作笔记 17 将 perplexity 归入 "early detectors" 的表述——perplexity 是 cross-gen early detector（50% contamination 可检出），但 within-gen early detector 只有 stable_rank 和 training_loss。论文叙事三维分层：(1) within-gen early alarm → stable_rank; (2) cross-gen severity tracking → perplexity; (3) cross-seed robust severity discrimination → spectral_entropy。Perplexity within-gen 失效是个有力的 practitioner 论点："the most commonly used collapse indicator fails at the earliest detection window"。**ROC 数据为 N=1 seed, 0.5B only，plan001 5-seed 后需验证。**
19. **信号定义精确化：三个 loss/PPL 信号的数据源（D035, 2026-05-15; 修正原 Note 19 错误归因）**: 代码中存在三个容易混淆的信号，必须在 Method 中精确定义：
    - **training_loss** = Trainer running avg CE on **训练集**（含 synthetic 混合数据），每 50 step 记录（`train.py:109-110`）。Within-gen AUC=0.923（有效）。原因：直接测量模型对被污染训练分布的学习动态。
    - **perplexity** = exp(mean NLL) on **固定 held-out 验证集**，model.eval() 模式，每 50 step 记录（`signals.py:92-108`）。Within-gen AUC=0.534（无效）。原因：QLoRA 早期微调对 held-out 分布影响微弱，collapse 效应需多代累积。Cross-gen d=20.82（有效）。
    - **token_entropy** = output token 分布的 Shannon entropy，within-gen AUC=0.478（无效）。
    **原 Note 19 的错误**：将 AUC=0.534 的信号标注为"training perplexity"（训练数据上的 PPL），实际该信号是 held-out eval PPL。training_loss（训练数据上的 CE）反而 AUC=0.923。
    **论文叙事修正**：Claim 2 featured sub-result 从"training perplexity fails"修正为"**held-out evaluation perplexity** fails at within-gen detection (AUC=0.534), while train-set loss detects effectively (AUC=0.923)"。Practitioners 通常在 eval checkpoints 看 held-out PPL，这个指标恰恰是 within-gen 最弱的。训练 loss 是间接的分布变化探测器，但 stable_rank (AUC=0.984) 仍最强因为它检测权重结构变化。
    **Abstract/Intro 措辞**：从 "training perplexity provides no within-gen early warning" 改为 "held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.534)"。
    Method 必须加入 training_loss 作为正式信号（Output 家族），明确标注数据源。Fig 3 展示 training_loss 合理（within-gen 第二强），需与 Method 信号列表一致。Camera-ready 升级条件：plan001 + plan002 cross-validation ROC 中 held-out PPL within-gen AUC 跨配置一致 ~0.5。


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: 'Scale validation: 1.5B model (Qwen2.5-1.5B) × WikiText-2 × 6 fractions
    (0/10/25/50/75/100%) × 5 seeds. Core experiment proving signal-severity correlation
    generalizes beyond 0.5B MVP.'
  priority: P0
  gpu_budget_hours: 150
  deps: []
  registry_id: plan001-wikitext-15B-5seeds
  notes: 6 fractions × 5 seeds × 5 gens = 150 runs. ~1h/run on A6000 for 1.5B QLoRA.
    Dream review unanimously requires ≥5 seeds for variance estimation credibility.
  status: DONE
  conclusion: failed
  metrics:
    gpu0_status: 已重启 submit_training_job, timeout=48h. seed42 frac=0.25 加载中 (skip
      frac=0.0 ✓)
    gpu1_status: PID running, seed42 frac=1.0 step ~1068/1540 (69%), 正常
    completed_seeds:
      seed42: frac=0.0 ✓, frac=0.5 ✓, frac=1.0 gen4 69%
      seed43: frac=0.0 ✓, frac=0.5 ✓
      seed44: frac=0.0 ✓, frac=0.5 ✓
      seed45: frac=0.0 gen4 synth 中断(被kill), 待 GPU0 轮到时自动补完
      seed46: not started
    v2_allocation:
      gpu0: fractions (0.0, 0.25, 0.1) × seeds 42-46
      gpu1: fractions (0.5, 1.0, 0.75) × seeds 42-46
    runs_completed: 6/30 (v2 total)
    gpu0_restart:
      time: 2026-05-15T23:01Z
      timeout_hours: 48
      reason: seed45 frac=0.0 gen4 synth killed
    disk: 18G/250G (7%)
    checked_at: 2026-05-15T23:02Z
- id: plan_002
  claim: 1
  description: 'Cross-domain validation: 1.5B × PubMed × 6 fractions × 3 seeds. Proves
    signals generalize beyond WikiText to biomedical domain.'
  priority: P0
  gpu_budget_hours: 45
  deps: []
  registry_id: plan002-pubmed-cqa1
  notes: 6 fractions × 3 seeds × 5 gens = 90 runs. Dream review flags single-seed
    PubMed as internal contradiction (paper argues against single-seed while doing
    exactly that). 3 seeds minimum.
  status: RUNNING
  metrics:
    gpu0_status: seed42 frac=10%, gen2 training 11% (156/1410)
    gpu1_status: seed42 frac=75%, gen1 training 99% (1400/1410)
    gpu2_status: seed44 frac=100%, gen0 synthetic 21%
    fraction_coverage:
      completed:
        '0.0':
        - seed42
        - seed43
        - seed44
        '0.5':
        - seed42
        - seed43
        - seed44
        '1.0':
        - seed42
        - seed43
      in_progress:
        '0.1': seed42 gen2 (GPU0)
        '0.75': seed42 gen1 (GPU1)
        '1.0': seed44 gen0 (GPU2)
      not_started:
      - '0.25'
    gpu_eta:
      cuda2_free: ~4h (seed44 frac=100%)
      cuda1_free: ~13h
      cuda0_free: ~18-27h
    disk: 86G/250G (35%)
    checked_at: 2026-05-16T08:24Z
- id: plan_003
  claim: 1
  description: 'Full FT comparison: 0.5B × WikiText-2 × 3 fractions (0/50/100%) ×
    1 seed with full fine-tuning. Validates signals are not QLoRA-specific.'
  priority: P1
  gpu_budget_hours: 20
  deps: []
  registry_id: plan003-fullft-05B
  notes: Full FT on 0.5B should fit in single A6000 24GB.
  status: DONE
  conclusion: success
  metrics:
    fullft_0pct_gen4:
      ppl: 19.23
      stable_rank: 37.48
      spectral_entropy: 0.765
      token_entropy: 1.884
    fullft_50pct_gen4:
      ppl: 25.64
      stable_rank: 40.47
      spectral_entropy: 0.783
      token_entropy: 1.736
      hellaswag: 0.397
    fullft_100pct_gen4:
      ppl: 326.19
      stable_rank: 153.87
      spectral_entropy: 0.889
      token_entropy: 0.829
      hellaswag: 0.372
    collapse_dynamics:
      onset_ratio_gen01: 15.3
      post_onset_ratio_gen14: 1.11
      pattern: fast_onset_saturation
      vs_qlora_gen4_ppl_ratio: 0.39
    fullft_vs_qlora_comparison:
      signals_not_qlora_specific: true
      direction_consistent: 4/4 core signals same direction (SR↑, SE↑, TE↓, PPL↑)
      sensitivity_ranking_consistent: PPL > stable_rank > token_entropy > spectral_entropy
        (both methods)
      structural_convergence_100pct_gen4:
        stable_rank_fullft: 153.9
        stable_rank_qlora: 155.6
        spectral_entropy_fullft: 0.889
        spectral_entropy_qlora: 0.884
      cross_signal_spearman_direction: 6/6 pairs match
      morphology_difference: 'FullFT: sudden gen1 15.3x PPL jump then plateau (+32
        gen1-4); QLoRA: gradual (8.7x→2.9x→1.8x→1.2x)'
      explanation: full parameter access → immediate catastrophic overfitting on corrupted
        data; adapter-only → damage distributed across generations
    output_files:
    - analysis/fullft_vs_qlora_comparison.json
    - analysis/fullft_vs_qlora_summary.md
    - analysis/fullft_vs_qlora_trajectories.pdf
    - analysis/fullft_vs_qlora_gen4_bars.pdf
    - analysis/fullft_vs_qlora_collapse_morphology.pdf
    - analysis/fullft_vs_qlora_structural_convergence.pdf
- id: plan_004
  claim: 2
  description: Within-gen early warning analysis on 1.5B data. Compute signal divergence
    at step 50/100/200/500 across all fractions and seeds from plan_001. Pure analysis,
    no GPU.
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: null
  notes: Extends MVP within-gen analysis to 1.5B with proper statistics.
  status: planned
- id: plan_005
  claim: 2
  description: 'Early warning threshold calibration: determine minimum signal deviation
    that reliably predicts end-of-generation collapse. ROC analysis across all configs.'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  - plan_002
  registry_id: null
  notes: Analysis only. MUST use clustered bootstrap (one obs per fraction×seed) or
    restrict to single generation per run. Dream review flags pooling non-independent
    generations as fatal methodology flaw.
  status: planned
- id: plan_006
  claim: 3
  description: 'Signal taxonomy across severity levels. Using plan_001 data, characterize
    per-signal-family operating ranges: where each signal is most/least informative.'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: plan006-signal-taxonomy
  notes: Core table/figure for Claim 3. Shows stable_rank saturation, gradient non-monotonicity,
    downstream failure. DONE (preliminary, N=2 seeds, 2 fractions). Rerun needed with
    full data.
  status: DONE
  conclusion: success
  metrics:
    n_seeds: 3
    n_fractions: 2
    n_signals_analyzed: 14
    ranking_method: Cohen's d at gen4
    3seed_update:
      top_signal_by_d: spectral_entropy (d=33.48)
      tier1_signals: spectral_entropy (d=33.48), perplexity (d=20.82), distinct_1
        (d=12.10), stable_rank (d=9.43), distinct_2 (d=9.38), distinct_3 (d=-6.25)
      tier2_signals: token_entropy(-4.52), self_bleu(-3.54), gradient_norm(-2.39),
        hellaswag(1.34)
      stable_rank_warning: 'dropped rank 1→4 (d: 61.7→9.43), 2-seed d=61.7 was overfitted
        due to seed44 variance (CV=0.022)'
      most_stable_signal: spectral_entropy (CV=0.0015, lowest)
      statistical_power: N=3 insufficient for Wilcoxon (min p=0.25); bootstrap 95%
        CI lower bounds away from 0 for all Tier 1; hellaswag only CI crossing 0 [-1.4,
        7.8]; need N≥5 for formal testing
    incremental_check_20260516: No substantial change. N still 3 for 0% vs 50%. distinct
      series N=2 (seed44 gen4 null). 0% vs 100% N=1 (seed42 only). Tier structure
      unchanged. Next meaningful update when seed45+ frac=50% completes.
    status_note: 3-seed incremental analysis complete. Full reanalysis at N=5 when
      plan001 finishes.
- id: plan_007
  claim: 3
  description: 'Per-layer collapse analysis: run forward-pass SVD on 1.5B model across
    gens to show which layers collapse first and how layer-level patterns differ by
    severity.'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - plan_001
  registry_id: null
  notes: Extends MVP per-layer analysis to 1.5B. Figure 3 candidate.
  status: planned
- id: plan_008
  claim: 3
  description: 'Self-recovery phenomenon deep dive: 50% contamination partial recovery
    analysis. Is it consistent across seeds? At what fraction does recovery disappear?'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: plan008-self-recovery
  notes: 'Analysis of plan_001 data at 25/50/75% fractions. Dream review: reclassify
    25% as ''mild degradation/near-stability'' not ''strong recovery'' (PPL monotonically
    increases). Position self-recovery as observation consistent with data mixing
    literature (Gerstgrasser et al. 2024), not as novel discovery. DONE (preliminary,
    3 fractions only). Rerun needed with full data.'
  status: DONE
  conclusion: success
  metrics:
    recovery_prevalence_50pct: 89% (16/18)
    mean_ppl_recovery_ratio: 0.51
    mean_token_entropy_rr: 0.624
    mean_stable_rank_rr: 0.339
    cross_seed_consistency: 5/6
    residual_ppl_elevation: 6.6-7.8%
    fractions_available:
    - 0
    - 50
    - 100
    n_sources: 3
    3seed_update:
      recovery_prevalence: 100% (9/9)
      mean_ppl_recovery_ratio: 0.5245
      ppl_rr_std: 0.027
      cross_seed_consistency: 3/3
      note: weight-space signals (stable_rank/spectral_entropy RR~0.32) recover slower
        than output signals (PPL RR~0.52)
    cross_domain_recovery_20260516:
      wikitext_rr:
        perplexity: 0.525 ± 0.026
        stable_rank: 0.322 ± 0.051
        spectral_entropy: 0.315 ± 0.020
        token_entropy: 0.594 ± 0.128
        gradient_norm: 1.220 ± 0.151
      pubmed_rr:
        perplexity: 0.405 ± 0.005
        stable_rank: 0.178 ± 0.107
        spectral_entropy: 0.152 ± 0.042
        token_entropy: 0.442 ± 0.013
        gradient_norm: 0.518 ± 0.028
      delta: PubMed all signals lower (Δ -0.12 to -0.70)
      pubmed_recovery_prevalence: 80% (8/10) vs WikiText 100%
      pubmed_spectral_failure: spectral_entropy RR < 0.2 both seeds, stable_rank seed43
        < 0.2
      key_finding: Recovery is domain-dependent. PubMed (specialized domain) recovers
        less — weight-space corruption more persistent. Output-vs-weight gap more
        extreme in PubMed.
      explanation: Specialized domain text has narrower distribution, making synthetic
        corruption fingerprint harder to overwrite with real data training
    cross_domain_incremental_seed43:
      pubmed_n2_consistency: 'std extremely small (PPL 0%: ±0.005, 50%: ±0.015, 100%:
        ±0.565)'
      recovery_ratio_comparison:
        perplexity:
          pubmed: 0.9943
          wikitext: 0.9981
          pubmed_weaker: true
        stable_rank:
          pubmed: 0.9822
          wikitext: 0.9814
          pubmed_weaker: false
          note: 差异在噪声内 (0.0008)
        spectral_entropy:
          pubmed: 0.8639
          wikitext: 0.8796
          pubmed_weaker: true
        token_entropy:
          pubmed: 0.9521
          wikitext: 0.9711
          pubmed_weaker: true
      structural_vs_output_insight: '100% collapse: WikiText PPL 3.6x > PubMed, but
        stable_rank/spectral_entropy nearly identical → structural collapse similar,
        PPL difference reflects domain characteristics not collapse severity'
      wikitext_n1_limitation: WikiText recovery ratio only N=1 (seed42), need seed43/44
        100% to strengthen
- id: plan_009
  claim: 1
  description: 'SIGMA head-to-head: SIGMA spectral metrics (log_det, effective_rank,
    track_ii, spectral_decay_rate) integrated into signals.py for real-time collection
    alongside plan_001 signals. Zero extra GPU overhead (shared H^T H matrix).'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: plan009-sigma-headtohead
  notes: 'Dream review (all tiers): SIGMA differentiation is thinner than claimed.
    Need head-to-head to clarify whether advantage is operational or fundamental.
    Integrated into plan_001 signals.py (2026-05-14), real-time collection. 28/30
    runs will have SIGMA data (2 seed=42 runs started before integration). RUNNING
    — passive collection via plan001.'
  status: DONE
  conclusion: killed
- id: plan_010
  claim: 1
  description: '3B model spot-check: Qwen2.5-3B × WikiText-2 × 3 fractions (0/50/100%)
    × 1 seed. Adds a third scale point to strengthen cross-scale claims.'
  priority: P2
  gpu_budget_hours: 20
  deps: []
  registry_id: plan010-3B-spotcheck
  notes: 3B already downloaded on server. Low marginal cost. Addresses median/worst
    tier concern that 2-point scale range (0.5B,1.5B) is too narrow. Only if GPU budget
    permits.
  status: RUNNING
  metrics:
    completed_fractions:
      '0.0': 5 gens done, summary ✓
      '0.5': 5 gens done, signals/ckpts ✓
      '1.0': gen0 training 63% (964/1540), ~2.8s/step
    pid: 255013
    gpu: cuda:3
    gpu_util: 100%
    gpu_mem: 9.6/24.6 GB
    server: cqa1-37219
    eta: ~5.5h (gen0 remaining + gen1-4)
    checked_at: 2026-05-16T08:24Z
- id: plan_011
  claim: 1
  description: 'Cross-family validation: LLaMA-3.2-1B × WikiText-2 × 3 fractions (0/50/100%)
    × 1 seed × 5 gens. Proves signals are not Qwen-specific.'
  priority: P0
  gpu_budget_hours: 20
  deps: []
  registry_id: null
  notes: 'Addresses fatal reviewer concern: single model family. Pipeline adapted
    (zero code change), model downloading. Run on autodl-5090 cuda:0 post-plan001.
    If 8/11 signals direction-consistent → "cross-family validated". If divergent
    → Discussion "architecture-dependent behavior" (still valuable).'
  status: planned
- id: plan_012
  claim: 3
  description: 'Full FT multi-seed: 0.5B × WikiText-2 × 3 fractions (0/50/100%) ×
    2 additional seeds × 5 gens. Strengthens Full FT vs QLoRA comparison from N=1
    to N=3.'
  priority: P1
  gpu_budget_hours: 40
  deps:
  - plan_003
  registry_id: null
  notes: 'Addresses reviewer concern: Full FT N=1 insufficient for method-dependence
    claim. 2 new seeds × 3 fracs × 5 gens = 30 runs on 0.5B Full FT. Run on autodl-5090
    cuda:1 or cqa1 post-plan001.'
  status: planned
- id: plan_013
  claim: 2
  description: 'MMLU-mini downstream evaluation: run MMLU-mini on all plan001 checkpoints
    to add second downstream task beyond HellaSwag.'
  priority: P0
  gpu_budget_hours: 1
  deps:
  - plan_001
  registry_id: null
  notes: Pure inference, ~30s/checkpoint, total ~15 min for all ckpts. Script ready
    (eval_mmlu_mini.py + run_mmlu_batch.sh), dry-run passed (36.06% accuracy). Addresses
    "downstream single benchmark" concern.
  status: planned
- id: plan_014
  claim: 2
  description: 'Within-gen AUROC on C2 (1.5B 5-seed): recompute within-generation
    binary AUROC using plan001 5-seed data. Upgrades Claim 2 from N=1 to N=5.'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: null
  notes: Clustered bootstrap by seed. Current within-gen AUROC=0.984 from C1 (0.5B,
    N=1). Recomputing on C2 (1.5B, N=5) gives formal statistical claim. Script (plan005_within_gen_auroc_c2.py)
    being written.
  status: planned
- id: plan_mvp_001
  claim: 1
  description: 'MVP: 0.5B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens'
  priority: P0
  gpu_budget_hours: 14.1
  deps: []
  registry_id: mvp_frac0
  notes: Control baseline. DONE.
  status: DONE
  conclusion: success
- id: plan_mvp_002
  claim: 1
  description: 'MVP: 0.5B × WikiText-2 × 50pct + 100pct × 1 seed × 5 gens'
  priority: P0
  gpu_budget_hours: 14.1
  deps: []
  registry_id: mvp_frac50_100
  notes: Main MVP experiment. DONE. Gate check 2/3 PASS.
  status: DONE
  conclusion: success
  metrics:
    progress: ALL COMPLETE — 0pct 5/5, 50pct 5/5, 100pct 5/5
    gate_check_verdict: PASS (3/3 families)
    gate_check_spectral: PASS — stable_rank cross-frac |rho|=1.0 (p=0.0), cross-gen
      rho=0.9 (p=0.037)
    gate_check_output: PASS — perplexity cross-frac |rho|=1.0, cross-gen rho=1.0;
      token_entropy cross-frac |rho|=0.9, cross-gen rho=-1.0
    gate_check_downstream: PASS — hellaswag_acc cross-frac |ρ|=0.72 (mean gen1-4,
      all negative), cross-gen ρ=-0.67 (100pct). Effect size small (0.41-0.44) but
      direction consistent. Data present in summary JSONs. 0pct gen0 null.
    hellaswag_values:
      0pct:
      - null
      - 0.442
      - 0.434
      - 0.43
      - 0.435
      50pct:
      - 0.435
      - 0.429
      - 0.42
      - 0.439
      - 0.434
      100pct:
      - 0.432
      - 0.432
      - 0.42
      - 0.41
      - 0.43
    hellaswag_cross_frac_rho_per_gen:
      gen1: -0.5
      gen2: -0.866
      gen3: -0.5
      gen4: -1
      mean: -0.7165
    hellaswag_cross_gen_rho:
      0pct: -0.4
      50pct: 0.1
      100pct: -0.667
    final_values_0pct_gen4:
      stable_rank: 23.41
      spectral_entropy: 0.703
      token_entropy: 2.259
      ppl: 15.67
    final_values_50pct_gen4:
      stable_rank: 24.79
      spectral_entropy: 0.716
      token_entropy: 2.215
      ppl: 16.95
    final_values_100pct_gen4:
      stable_rank: 155.64
      spectral_entropy: 0.884
      token_entropy: 0.782
      ppl: 839.2
    collapse_magnitude_100pct: stable_rank 6.6x, PPL 53x, token_entropy -65%
    0pct_baseline_stability: all signals <3% variation across 5 gens
    within_gen_early_warning: stable_rank 34.4% deviation at step 50 (3% training
      progress)
- id: plan_mvp_003
  claim: 2
  description: MVP within-gen temporal analysis on 0.5B data
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_mvp_002
  registry_id: within_gen_analysis
  notes: DONE. Early warning at 3% progress confirmed.
  status: DONE
  conclusion: success
  metrics:
    earliest_distinguishing_step: step 50 (3% training progress)
    best_signal: stable_rank (34.4% deviation at step 50)
    signals_above_5pct_at_step50: stable_rank 34.4%, token_entropy 24.5%, perplexity
      17.7%
    crossgen_acceleration: '100pct PPL delta vs per-gen 0pct baseline: gen0=<1%, gen1=+770%,
      gen2=+2416%'
    crossgen_acceleration_note: 'Corrected 2026-05-15: switched from within-gen start→end
      metric to per-generation α=0 baseline comparison'
    plots: 12 files (PDF+PNG) on server within_gen_plots/
    plan004_15B_update:
      strongest_early_signal: training_loss@step50 AUC=0.880, perplexity@step100 AUC=0.957
      1.5B_vs_0.5B: stable_rank@step50 rel_div=0.206 (0.5B=0.344), 1.5B amplitude
        smaller but still detectable
      data_coverage: 4 seeds × 5 fracs × 5 gens = 1134 observations
      output_files:
      - analysis/divergence_table.csv
      - analysis/detection_power.csv
      - analysis/early_warning_heatmap.pdf
      - analysis/divergence_curves.pdf


## registry (completed experiments)

- exp_id: mvp_collapse_001
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    progress: 0pct_gen0 step 242/1540 (15.7%)
    speed: 1.19 it/s
    loss: 2.652
    perplexity: 14.41
    stable_rank: 20.5
    spectral_entropy: 0.673
    signals_collected: 4
    checked_at: '2026-05-14T06:38:30Z'
- exp_id: mvp_collapse_002
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    progress: 0pct_gen0 step 50/1540 (3%)
    speed: 1.17 it/s
    gpu_util: 26%
    gpu_mem: 6314/32607 MiB
    gen_batch_size: 32
    gen_num_chunks: 1500
    checked_at: '2026-05-14T08:21:00Z'
- exp_id: mvp_collapse_003
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    progress: 0pct_gen0 step 50/1540 (3%)
    speed: 1.08 it/s
    gpu_util: 20%
    gpu_mem: 6314/32607 MiB
    checked_at: '2026-05-14T09:01:30Z'
- exp_id: mvp_frac50_100
  name: ''
  status: DONE
  conclusion: success
  metrics:
    progress: ALL COMPLETE — 0pct 5/5, 50pct 5/5, 100pct 5/5
    gate_check_verdict: PASS (3/3 families)
    gate_check_spectral: PASS — stable_rank cross-frac |rho|=1.0 (p=0.0), cross-gen
      rho=0.9 (p=0.037)
    gate_check_output: PASS — perplexity cross-frac |rho|=1.0, cross-gen rho=1.0;
      token_entropy cross-frac |rho|=0.9, cross-gen rho=-1.0
    gate_check_downstream: PASS — hellaswag_acc cross-frac |ρ|=0.72 (mean gen1-4,
      all negative), cross-gen ρ=-0.67 (100pct). Effect size small (0.41-0.44) but
      direction consistent. Data present in summary JSONs. 0pct gen0 null.
    hellaswag_values:
      0pct:
      - null
      - 0.442
      - 0.434
      - 0.43
      - 0.435
      50pct:
      - 0.435
      - 0.429
      - 0.42
      - 0.439
      - 0.434
      100pct:
      - 0.432
      - 0.432
      - 0.42
      - 0.41
      - 0.43
    hellaswag_cross_frac_rho_per_gen:
      gen1: -0.5
      gen2: -0.866
      gen3: -0.5
      gen4: -1
      mean: -0.7165
    hellaswag_cross_gen_rho:
      0pct: -0.4
      50pct: 0.1
      100pct: -0.667
    final_values_0pct_gen4:
      stable_rank: 23.41
      spectral_entropy: 0.703
      token_entropy: 2.259
      ppl: 15.67
    final_values_50pct_gen4:
      stable_rank: 24.79
      spectral_entropy: 0.716
      token_entropy: 2.215
      ppl: 16.95
    final_values_100pct_gen4:
      stable_rank: 155.64
      spectral_entropy: 0.884
      token_entropy: 0.782
      ppl: 839.2
    collapse_magnitude_100pct: stable_rank 6.6x, PPL 53x, token_entropy -65%
    0pct_baseline_stability: all signals <3% variation across 5 gens
    within_gen_early_warning: stable_rank 34.4% deviation at step 50 (3% training
      progress)
- exp_id: mvp_frac0
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: per_layer_analysis
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: per_layer_analysis_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    progress: 0pct gen0 1388/1540 (90%), ~2min to finish gen0
    output_file: outputs/per_layer_analysis.json (incremental save per gen)
    per_gen_time: ~35 min/gen
    total_gens: 2 fractions x 5 gens = 10 gens
    eta_total: ~6h from start (started ~18:19 UTC)
    signals_safety: 'confirmed: output_dir redirected to _per_layer_tmp, signals_*.jsonl
      untouched'
    analysis_method: 'hook all transformer layers, 64 val samples forward pass, compute
      per-layer SVD: stable_rank, spectral_entropy, SV_ratio(sigma1/sigma2)'
    gpu: GPU 1, 6314/32607 MiB, 43% util
    checked_at: '2026-05-14T18:58:00Z'
- exp_id: per_layer_analysis_v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: per_layer_analysis_active
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    progress: 0pct gen0=done, 0pct gen1=in_progress
    per_gen_time: ~35 min/gen
    eta_remaining: ~9 gens x 35min = ~5.25h
    gpu: cuda:1
    checked_at: '2026-05-14T19:08:00Z'
- exp_id: per_layer_analysis_v4
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: per_layer_analysis_v5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    boundary_early_sr_delta: 0.809
    middle_sr_delta: DEPRECATED — was 0.01 based on incorrect data; real per-sub-module
      mean ~0.66; see appendix tab:full_per_layer for true values
    late_mid_sr_delta: 0.418
    L12_down_proj_sr_collapse: -3.218
    L11_down_proj_sr_collapse: -2.146
    v_proj_avg_sr_increase: recalculate from appendix — significantly >1.334 across
      all layers
    k_proj_avg_sr_increase: 0.714
    L0_qproj_sr_delta: 2.849
    L16_vproj_sr_peak: 3.06
    baseline_0pct_max_sr_drift: 0.311
    weight_norm_crossover_layer: 11
    narrative_revision: three-zone structure replaced by sub-module-centric analysis
      per Director approval 2026-05-15
- exp_id: within_gen_analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    earliest_distinguishing_step: step 50 (3% training progress)
    best_signal: stable_rank (34.4% deviation at step 50)
    signals_above_5pct_at_step50: stable_rank 34.4%, token_entropy 24.5%, perplexity
      17.7%
    crossgen_acceleration: '100pct PPL delta vs per-gen 0pct baseline: gen0=<1%, gen1=+770%,
      gen2=+2416%'
    crossgen_acceleration_note: 'Corrected 2026-05-15: switched from within-gen start→end
      metric to per-generation α=0 baseline comparison'
    plots: 12 files (PDF+PNG) on server within_gen_plots/
    plan004_15B_update:
      strongest_early_signal: training_loss@step50 AUC=0.880, perplexity@step100 AUC=0.957
      1.5B_vs_0.5B: stable_rank@step50 rel_div=0.206 (0.5B=0.344), 1.5B amplitude
        smaller but still detectable
      data_coverage: 4 seeds × 5 fracs × 5 gens = 1134 observations
      output_files:
      - analysis/divergence_table.csv
      - analysis/detection_power.csv
      - analysis/early_warning_heatmap.pdf
      - analysis/divergence_curves.pdf
- exp_id: plan_001_wikitext_1.5B_5seeds
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan_002_pubmed_1.5B_3seeds
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan_001_wikitext_15B_5seeds
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: plan001-wikitext-15B-5seeds
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    gpu0_status: 已重启 submit_training_job, timeout=48h. seed42 frac=0.25 加载中 (skip
      frac=0.0 ✓)
    gpu1_status: PID running, seed42 frac=1.0 step ~1068/1540 (69%), 正常
    completed_seeds:
      seed42: frac=0.0 ✓, frac=0.5 ✓, frac=1.0 gen4 69%
      seed43: frac=0.0 ✓, frac=0.5 ✓
      seed44: frac=0.0 ✓, frac=0.5 ✓
      seed45: frac=0.0 gen4 synth 中断(被kill), 待 GPU0 轮到时自动补完
      seed46: not started
    v2_allocation:
      gpu0: fractions (0.0, 0.25, 0.1) × seeds 42-46
      gpu1: fractions (0.5, 1.0, 0.75) × seeds 42-46
    runs_completed: 6/30 (v2 total)
    gpu0_restart:
      time: 2026-05-15T23:01Z
      timeout_hours: 48
      reason: seed45 frac=0.0 gen4 synth killed
    disk: 18G/250G (7%)
    checked_at: 2026-05-15T23:02Z
- exp_id: plan001-wikitext-15B-5seeds-gpu1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan001-gpu1
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    current_run: frac=0.5, seed=44, gen4 training ~10% (~25min left)
    completed_seeds:
      seed42: DONE (summary_50pct.json ✓)
      seed43: DONE (summary_50pct.json ✓)
      seed44: gen4 ~10%, then gen5 remaining, then seed45+46
    auto_advance_confirmed: true
    gpu_util: 100%
    gpu_mem: 7984 MiB
    gpu_temp: 65C
    note: seed45 will auto-load hotfixed pipeline.py — no intervention needed
    checked_at: 2026-05-15T16:42Z
- exp_id: plan002-pubmed-cqa1
  name: ''
  status: RUNNING
  conclusion: ''
  metrics:
    gpu0_status: seed42 frac=10%, gen2 training 11% (156/1410)
    gpu1_status: seed42 frac=75%, gen1 training 99% (1400/1410)
    gpu2_status: seed44 frac=100%, gen0 synthetic 21%
    fraction_coverage:
      completed:
        '0.0':
        - seed42
        - seed43
        - seed44
        '0.5':
        - seed42
        - seed43
        - seed44
        '1.0':
        - seed42
        - seed43
      in_progress:
        '0.1': seed42 gen2 (GPU0)
        '0.75': seed42 gen1 (GPU1)
        '1.0': seed44 gen0 (GPU2)
      not_started:
      - '0.25'
    gpu_eta:
      cuda2_free: ~4h (seed44 frac=100%)
      cuda1_free: ~13h
      cuda0_free: ~18-27h
    disk: 86G/250G (35%)
    checked_at: 2026-05-16T08:24Z
- exp_id: plan003-fullft-05B
  name: ''
  status: DONE
  conclusion: success
  metrics:
    fullft_0pct_gen4:
      ppl: 19.23
      stable_rank: 37.48
      spectral_entropy: 0.765
      token_entropy: 1.884
    fullft_50pct_gen4:
      ppl: 25.64
      stable_rank: 40.47
      spectral_entropy: 0.783
      token_entropy: 1.736
      hellaswag: 0.397
    fullft_100pct_gen4:
      ppl: 326.19
      stable_rank: 153.87
      spectral_entropy: 0.889
      token_entropy: 0.829
      hellaswag: 0.372
    collapse_dynamics:
      onset_ratio_gen01: 15.3
      post_onset_ratio_gen14: 1.11
      pattern: fast_onset_saturation
      vs_qlora_gen4_ppl_ratio: 0.39
    fullft_vs_qlora_comparison:
      signals_not_qlora_specific: true
      direction_consistent: 4/4 core signals same direction (SR↑, SE↑, TE↓, PPL↑)
      sensitivity_ranking_consistent: PPL > stable_rank > token_entropy > spectral_entropy
        (both methods)
      structural_convergence_100pct_gen4:
        stable_rank_fullft: 153.9
        stable_rank_qlora: 155.6
        spectral_entropy_fullft: 0.889
        spectral_entropy_qlora: 0.884
      cross_signal_spearman_direction: 6/6 pairs match
      morphology_difference: 'FullFT: sudden gen1 15.3x PPL jump then plateau (+32
        gen1-4); QLoRA: gradual (8.7x→2.9x→1.8x→1.2x)'
      explanation: full parameter access → immediate catastrophic overfitting on corrupted
        data; adapter-only → damage distributed across generations
    output_files:
    - analysis/fullft_vs_qlora_comparison.json
    - analysis/fullft_vs_qlora_summary.md
    - analysis/fullft_vs_qlora_trajectories.pdf
    - analysis/fullft_vs_qlora_gen4_bars.pdf
    - analysis/fullft_vs_qlora_collapse_morphology.pdf
    - analysis/fullft_vs_qlora_structural_convergence.pdf
- exp_id: plan010-3B-spotcheck
  name: ''
  status: RUNNING
  conclusion: ''
  metrics:
    completed_fractions:
      '0.0': 5 gens done, summary ✓
      '0.5': 5 gens done, signals/ckpts ✓
      '1.0': gen0 training 63% (964/1540), ~2.8s/step
    pid: 255013
    gpu: cuda:3
    gpu_util: 100%
    gpu_mem: 9.6/24.6 GB
    server: cqa1-37219
    eta: ~5.5h (gen0 remaining + gen1-4)
    checked_at: 2026-05-16T08:24Z
- exp_id: plan_001_seed42_frac0
  name: ''
  status: PREPARING
  conclusion: ''
  metrics:
    status: DONE
    gpu: 0
    server: autodl-5090
    model: Qwen2.5-1.5B
    dataset: wikitext
    mode: qlora
    seed: 42
    fraction: 0
    generations_done: 5
    final_ppl: 12.2
    final_hellaswag: 0.518
    checked_at: 2026-05-15T19:05
- exp_id: plan_001_seed42_frac50
  name: ''
  status: PREPARING
  conclusion: ''
  metrics:
    status: DONE
    gpu: 1
    server: autodl-5090
    model: Qwen2.5-1.5B
    dataset: wikitext
    mode: qlora
    seed: 42
    fraction: 0.5
    generations_done: 5
    final_ppl: 13.03
    final_hellaswag: 0.524
    checked_at: 2026-05-15T19:05
- exp_id: plan_001_seed43_frac0
  name: ''
  status: PREPARING
  conclusion: ''
  metrics:
    status: RUNNING
    gpu: 0
    server: autodl-5090
    model: Qwen2.5-1.5B
    dataset: wikitext
    mode: qlora
    seed: 43
    fraction: 0
    current_gen: 4
    phase: generating_synthetic_96pct
    gpu_util_pct: 34
    gpu_mem_mb: 4270
    gpu_temp_c: 56
    pid: 609739
    checked_at: 2026-05-15T19:05
- exp_id: plan_001_seed43_frac50
  name: ''
  status: PREPARING
  conclusion: ''
  metrics:
    status: RUNNING
    gpu: 1
    server: autodl-5090
    model: Qwen2.5-1.5B
    dataset: wikitext
    mode: qlora
    seed: 43
    fraction: 0.5
    current_gen: 4
    phase: generating_synthetic_96pct
    gpu_util_pct: 100
    gpu_mem_mb: 7984
    gpu_temp_c: 64
    pid: 617434
    checked_at: 2026-05-15T19:05
- exp_id: plan009-sigma-headtohead
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan006-signal-taxonomy
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_seeds: 3
    n_fractions: 2
    n_signals_analyzed: 14
    ranking_method: Cohen's d at gen4
    3seed_update:
      top_signal_by_d: spectral_entropy (d=33.48)
      tier1_signals: spectral_entropy (d=33.48), perplexity (d=20.82), distinct_1
        (d=12.10), stable_rank (d=9.43), distinct_2 (d=9.38), distinct_3 (d=-6.25)
      tier2_signals: token_entropy(-4.52), self_bleu(-3.54), gradient_norm(-2.39),
        hellaswag(1.34)
      stable_rank_warning: 'dropped rank 1→4 (d: 61.7→9.43), 2-seed d=61.7 was overfitted
        due to seed44 variance (CV=0.022)'
      most_stable_signal: spectral_entropy (CV=0.0015, lowest)
      statistical_power: N=3 insufficient for Wilcoxon (min p=0.25); bootstrap 95%
        CI lower bounds away from 0 for all Tier 1; hellaswag only CI crossing 0 [-1.4,
        7.8]; need N≥5 for formal testing
    incremental_check_20260516: No substantial change. N still 3 for 0% vs 50%. distinct
      series N=2 (seed44 gen4 null). 0% vs 100% N=1 (seed42 only). Tier structure
      unchanged. Next meaningful update when seed45+ frac=50% completes.
    status_note: 3-seed incremental analysis complete. Full reanalysis at N=5 when
      plan001 finishes.
- exp_id: plan008-self-recovery
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_prevalence_50pct: 89% (16/18)
    mean_ppl_recovery_ratio: 0.51
    mean_token_entropy_rr: 0.624
    mean_stable_rank_rr: 0.339
    cross_seed_consistency: 5/6
    residual_ppl_elevation: 6.6-7.8%
    fractions_available:
    - 0
    - 50
    - 100
    n_sources: 3
    3seed_update:
      recovery_prevalence: 100% (9/9)
      mean_ppl_recovery_ratio: 0.5245
      ppl_rr_std: 0.027
      cross_seed_consistency: 3/3
      note: weight-space signals (stable_rank/spectral_entropy RR~0.32) recover slower
        than output signals (PPL RR~0.52)
    cross_domain_recovery_20260516:
      wikitext_rr:
        perplexity: 0.525 ± 0.026
        stable_rank: 0.322 ± 0.051
        spectral_entropy: 0.315 ± 0.020
        token_entropy: 0.594 ± 0.128
        gradient_norm: 1.220 ± 0.151
      pubmed_rr:
        perplexity: 0.405 ± 0.005
        stable_rank: 0.178 ± 0.107
        spectral_entropy: 0.152 ± 0.042
        token_entropy: 0.442 ± 0.013
        gradient_norm: 0.518 ± 0.028
      delta: PubMed all signals lower (Δ -0.12 to -0.70)
      pubmed_recovery_prevalence: 80% (8/10) vs WikiText 100%
      pubmed_spectral_failure: spectral_entropy RR < 0.2 both seeds, stable_rank seed43
        < 0.2
      key_finding: Recovery is domain-dependent. PubMed (specialized domain) recovers
        less — weight-space corruption more persistent. Output-vs-weight gap more
        extreme in PubMed.
      explanation: Specialized domain text has narrower distribution, making synthetic
        corruption fingerprint harder to overwrite with real data training
    cross_domain_incremental_seed43:
      pubmed_n2_consistency: 'std extremely small (PPL 0%: ±0.005, 50%: ±0.015, 100%:
        ±0.565)'
      recovery_ratio_comparison:
        perplexity:
          pubmed: 0.9943
          wikitext: 0.9981
          pubmed_weaker: true
        stable_rank:
          pubmed: 0.9822
          wikitext: 0.9814
          pubmed_weaker: false
          note: 差异在噪声内 (0.0008)
        spectral_entropy:
          pubmed: 0.8639
          wikitext: 0.8796
          pubmed_weaker: true
        token_entropy:
          pubmed: 0.9521
          wikitext: 0.9711
          pubmed_weaker: true
      structural_vs_output_insight: '100% collapse: WikiText PPL 3.6x > PubMed, but
        stable_rank/spectral_entropy nearly identical → structural collapse similar,
        PPL difference reflects domain characteristics not collapse severity'
      wikitext_n1_limitation: WikiText recovery ratio only N=1 (seed42), need seed43/44
        100% to strengthen
- exp_id: plan002-pubmed-gpu2
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    current_run: seed43 frac=1.0 gen1 training ~50%
    completed:
      seed42: frac=1.0 all 5 gens done (summary ✓)
    remaining: seed43 ~4 gens + seed44 5 gens = ~9 gens
    gpu_util: 54%
    gpu_mem: 7567/24564 MiB
    eta: ~2026-05-16T11:30Z
    note: GPU2 是 plan002 瓶颈。GPU0/GPU1 ~3.5h 后空闲,可考虑分担 seed44 frac=1.0
    checked_at: 2026-05-16T02:43Z
- exp_id: plan001_v2_gpu0
  name: ''
  status: RUNNING
  conclusion: ''
  metrics:
    gpu0_status: seed42 frac=0.1 gen2 training 88% (1350/1540)
    gpu1_status: seed43 frac=1.0 gen2 training 34% (518/1540)
    gpu0_util: 37%
    gpu1_util: 33%
    gpu0_mem: 7.6/31.8 GB
    gpu1_mem: 7.6/31.8 GB
    completion_table:
      seed42:
        '0.0': done
        '0.1': gen2 88%
        '0.25': done
        '0.5': done
        '0.75': done
        '1.0': done
      seed43:
        '0.0': done
        '0.5': done
        '1.0': gen2 34%
      seed44:
        '0.0': done
        '0.5': done
      seed45:
        '0.0': done
      seed46: {}
    runs_completed: 10/30 (33%)
    runs_in_progress: 2
    runs_remaining: 18
    disk: 38G/250G (16%)
    checked_at: 2026-05-16T08:23Z
- exp_id: plan001-cqa1-seed46
  name: ''
  status: ALLOCATED
  conclusion: ''
  metrics: {}
- exp_id: plan001-cqa1-seed44
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001-cqa1-seed45
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan002-pubmed-gpu2-tail
  name: ''
  status: DONE
  conclusion: success
  metrics:
    note: Tail-end monitoring of plan002 GPU2. PID 423689 exited. Full diagnostic
      pending.
    checkpoint_path: N/A
    log_path: /tmp/plan002_gpu2.log
- exp_id: plan011-llama-download
  name: ''
  status: DONE
  conclusion: success
  metrics:
    model_path: /root/autodl-tmp/models/Llama-3.2-1B/LLM-Research/Llama-3.2-1B
    model_size_gb: 2.4
    params_b: 1.24
    vocab_size: 128000
    hidden_size: 2048
    num_layers: 16
    model_type: llama
    verification: transformers load SUCCESS
    launch_script: run_plan011_llama.sh ready
    download_log: /tmp/llama_ms_v5.log

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
  "promptId": "98611a59-a712-4e6f-b839-ddc70dc31359",
  "type": "user",
  "uuid": "3ef441ef-27d3-47f0-b5ff-5975a8bb4976",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T10:08:04.989Z_

```json
{
  "parentUuid": "3ef441ef-27d3-47f0-b5ff-5975a8bb4976",
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
  "uuid": "59189aea-586e-4738-92a6-f42dd6f0f564",
  "timestamp": "2026-05-16T10:08:04.989Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T10:08:04.989Z_

```json
{
  "parentUuid": "59189aea-586e-4738-92a6-f42dd6f0f564",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "102a97e7-3d83-4f44-83d0-906b97074ce1",
  "timestamp": "2026-05-16T10:08:04.989Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：plan001 严重不完整（≤10 runs）；1.5B 未复现 0.5B 的 within-gen 发现；seed 方差摧毁信号排名稳定性；LLaMA 方向不一致或未跑；需要 reframe 但不降级 venue 核心假设：['plan001 仅完成 ≤10/30 runs（基本停留在当前状态），5-se…",
  "leafUuid": "102a97e7-3d83-4f44-83d0-906b97074ce1",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze collapse signal robustness across scales and reframe for EMNLP",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39"
}
```

---

### Assistant

_source line 8 · 2026-05-16T10:08:36.752Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental results for the "worst" tier scenario across all planned experiments in the experiment_plan. I need to go through each experiment and predict what the results would look like under the worst-case assumptions defined in Phase 1.

Let me carefully go through each experiment plan and generate worst-tier predictions with rationales.

Key worst-tier assumptions:
- plan001 ≤10 runs completed (currently 6/30, worst = stays around 6-10)
- 1.5B within-gen AUC for stable_rank < 0.80
- 6-fraction ρ < 0.85 due to seed variance and non-monotonic fraction behavior


- stable_rank shows high cross-seed variability (CV > 0.06), making rankings unreliable
- LLaMA results either fail to show consistent directional signals or contradict core findings like stable_rank
- PPL achieves within-gen AUC above 0.70 at 1.5B, undermining the "PPL fails" hypothesis
- 3B spot-checks reveal inconsistent signal directions across methods
- Full fine-tuning with N=1 can't establish method-dependence claims
- PubMed and WikiText diverge more substantially than anticipated

Now I'm working through each experiment plan to flesh out what these worst-case results would look like in detail.

Plan 001 would only yield 8-10 completed runs out of 30 across the scale validation, leaving most seed-fraction combinations missing and making 5-seed statistics infeasible. The sparse data that does exist points to lower AUC for stable_rank at 1.5B. Plan 002 crosses into PubMed but encounters very different signal behavior compared to WikiText, with low recovery prevalence and inconsistent core signal directions. Plan 003 is already done and shows success, though I'm framing it conservatively given the N=1 limitation. Plan 004 depends on plan 001's data, so limited completions would weaken the early warning analysis and show stable_rank AUC dropping notably at 1.5B. Plan 005 on ROC threshold calibration also hinges on plan 001's results.

Plan 006 has preliminary results from 3 seeds but would remain stuck there if the 5-seed data never materializes, leaving rankings unstable. Plan 007's per-layer analysis on 1.5B gets blocked or severely limited by plan 001's gaps. Plan 008 has preliminary self-recovery results but needs the full dataset to be complete. Plan 009 was already killed. Plan 010 is currently running on the 3B spot-check but might show inconsistent signal directions at that scale. Plan 011 on LLaMA cross-family is still planned and could run but might only achieve consistency across fewer than 6 of the 11 signals.

For the remaining planned experiments, plan 012's full fine-tuning with multiple seeds likely won't run at all due to GPU constraints. Plan 013's MMLU-mini downstream task depends on plan 001 and would suffer from limited checkpoint availability, making results inconclusive. Plan 014's within-generation AUROC on 1.5B with 5 seeds also depends on plan 001 and would probably max out at 3-seed results instead.

I should focus on generating worst-case predictions for all the planned and running experiments, making sure to include the actual results for the ones already done while being systematic about the failure modes for the rest.

Generating worst-tier predictions across metric ranges...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "102a97e7-3d83-4f44-83d0-906b97074ce1",
  "isSidechain": false,
  "requestId": "req_011Cb64dEpKYtGbpzV67q8zV",
  "type": "assistant",
  "uuid": "4e7bd1c1-4810-45be-b65e-be35e9ccb26a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhTqhJoEmQoNa1KpCJzsBd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26992,
      "cache_read_input_tokens": 11841,
      "output_tokens": 20495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 20495,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26992
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

_source line 9 · 2026-05-16T10:14:40.004Z_

```yaml
tier: worst
narrative_guidance: >
  核心叙事 "signals reliably track collapse across configs" 不成立。信号行为高度 config-dependent，
  排名不稳定。Reframe 为 negative-result + taxonomy paper："Collapse monitoring is harder than
  it looks"——同一信号在不同 scale/seed/method 下表现迥异。Claim 3 升级为主 claim（configuration-
  dependence），Claim 1 降为 conditional correlation，Claim 2 降为 scale-dependent early warning。
  仍冲 EMNLP（negative results track），但推迟至 ARR 6/15。

imagined_experiments:
  # ============================================================
  # plan_001: 1.5B × WikiText × 6 fractions × 5 seeds (P0, FAILED)
  # ============================================================
  - name: "1.5B Scale Validation (WikiText, 5-seed)"
    plan_id: plan_001
    description: >
      Qwen2.5-1.5B × WikiText-2 × 6 fractions × 5 seeds × 5 gens。
      核心实验，验证 signal-severity correlation 在更大 scale 的泛化性。
    expected_results:
      runs_completed: 10
      runs_total: 30
      seeds_with_full_6frac: 1  # 只有 seed42 接近完成全部 6 fractions
      seeds_with_partial_data: 3  # seed43/44/45 各有 2-3 fractions
      seeds_with_no_data: 1  # seed46 完全未启动
      fraction_coverage_seed42: [0.0, 0.1, 0.25, 0.5, 0.75, 1.0]  # 唯一完整 seed
      fraction_coverage_seed43: [0.0, 0.5, 1.0]
      fraction_coverage_seed44: [0.0, 0.5]
      fraction_coverage_seed45: [0.0]
      fraction_coverage_seed46: []
      # seed42 6-fraction Spearman (唯一可计算的)
      spearman_rho_seed42_stable_rank: 0.83
      spearman_rho_seed42_spectral_entropy: 0.89
      spearman_rho_seed42_perplexity: 0.94
      spearman_rho_seed42_token_entropy: -0.77
      # 跨 seed median（仅 3 seeds 有 0/50 对，无法做 6-frac ρ）
      spearman_rho_median_across_seeds_2frac: 0.78  # 仅 0% vs 50% 对比
      # 1.5B gen4 terminal values (seed42, frac=100%)
      ppl_1.5B_100pct_gen4: 412.5
      stable_rank_1.5B_100pct_gen4: 98.3
      spectral_entropy_1.5B_100pct_gen4: 0.861
      token_entropy_1.5B_100pct_gen4: 0.91
      # 1.5B gen4 terminal values (seed42, frac=50%)
      ppl_1.5B_50pct_gen4: 14.8
      stable_rank_1.5B_50pct_gen4: 31.2
      spectral_entropy_1.5B_50pct_gen4: 0.728
      # 1.5B gen4 terminal values (seed42, frac=0%)
      ppl_1.5B_0pct_gen4: 11.9
      stable_rank_1.5B_0pct_gen4: 28.7
      spectral_entropy_1.5B_0pct_gen4: 0.711
      # stable_rank CV across seeds (0% vs 50%)
      stable_rank_cv_0pct: 0.031
      stable_rank_cv_50pct: 0.085  # seed44 方差大
      stable_rank_cv_100pct: null  # 仅 seed42 有数据
      # Cohen's d 估计 (3 seeds, 0% vs 50% only)
      cohens_d_stable_rank_3seed: 3.1
      cohens_d_spectral_entropy_3seed: 9.2
      cohens_d_perplexity_3seed: 7.8
      # collapse magnitude at 1.5B vs 0.5B
      collapse_magnitude_1.5B_sr: "3.4x (vs 0.5B 6.6x)"
      collapse_magnitude_1.5B_ppl: "34.7x (vs 0.5B 53x)"
    result_rationale: >
      GPU0 反复 OOM/kill（seed45 gen4 synth 中断后虽重启但 48h timeout 内仅多完成 2-3 runs），
      GPU1 按序推进但 1.5B QLoRA ~1h/run × 5 gens 意味着每个 fraction-seed 组合需 5h，
      30 runs 需 ~150 GPU-hours / 2 GPUs ≈ 75h 净运行时间，加上 OOM 重启、queue 空闲、
      synth generation 瓶颈，实际产出 ~10 runs。seed46 完全来不及。seed42 作为起始 seed
      优先级最高，基本跑完 6 fractions。关键后果：5-seed 统计完全不可行，只能对 3 seeds
      做 2-fraction (0% vs 50%) 的有限比较。stable_rank 在 1.5B 的 collapse magnitude
      显著低于 0.5B（3.4x vs 6.6x），因为 1.5B 的参数冗余吸收了部分 collapse 能量——
      权重矩阵维度更高，Frobenius norm 增长被更大的矩阵稀释。这直接降低了 stable_rank
      作为 collapse indicator 的灵敏度。seed44 在 frac=50% 引入的异常方差（CV=0.085）
      在 1.5B 进一步放大（0.5B 时 CV=0.022），因为 1.5B 的 optimization landscape 更复杂，
      不同 seed 的训练轨迹分歧更大。6-fraction ρ 仅 seed42 可计算，且因 frac=10% 和
      frac=25% 的非单调行为（10% 几乎无变化，25% 轻微恶化但与 10% 无显著差异）拉低至 0.83。
    tables:
      - name: "Tab: 1.5B Completion Matrix"
        columns: [seed, "frac=0.0", "frac=0.1", "frac=0.25", "frac=0.5", "frac=0.75", "frac=1.0"]
        rows:
          - [42, "✓", "✓", "✓", "✓", "✓", "✓"]
          - [43, "✓", "—", "—", "✓", "—", "gen3"]
          - [44, "✓", "—", "—", "✓", "—", "—"]
          - [45, "✓", "—", "—", "—", "—", "—"]
          - [46, "—", "—", "—", "—", "—", "—"]
      - name: "Tab: 1.5B Signal Values at gen4 (seed42)"
        columns: [fraction, ppl, stable_rank, spectral_entropy, token_entropy]
        rows:
          - ["0%", 11.9, 28.7, 0.711, 2.18]
          - ["10%", 12.1, 29.0, 0.713, 2.16]
          - ["25%", 12.8, 29.9, 0.718, 2.12]
          - ["50%", 14.8, 31.2, 0.728, 2.05]
          - ["75%", 38.4, 52.1, 0.793, 1.58]
          - ["100%", 412.5, 98.3, 0.861, 0.91]
      - name: "Tab: stable_rank CV across seeds (1.5B, gen4)"
        columns: [fraction, CV, n_seeds, note]
        rows:
          - ["0%", 0.031, 4, "seed42-45"]
          - ["50%", 0.085, 3, "seed42-44, seed44 outlier"]
          - ["100%", "N/A", 1, "seed42 only"]
    figures_description:
      - "Fig: 1.5B severity curves (seed42 only, 6 fractions) — 可画但 N=1 无 CI"
      - "Fig: 1.5B vs 0.5B collapse magnitude bar chart — 显示 1.5B amplitude 系统性低于 0.5B"
      - "Fig: stable_rank seed variance scatter (frac=50%, 3 seeds) — 显示 seed44 离群"
    analysis: >
      plan001 是 worst tier 的核心灾难点。10/30 完成率意味着论文无法声称 "5-seed validation"，
      只能写 "up to 4 seeds where available, with complete 6-fraction coverage for one seed"。
      这直接摧毁了 Claim 1 的统计基础——Reviewer 会问 "你自己说 single-seed 不够，
      结果自己也是 near-single-seed？" 6-fraction ρ=0.83 (seed42) 因 10%/25% 非单调而低于
      MVP 的 ρ=1.0（当时只有 3 fractions），但仍 > 0.7。Cross-seed median ρ 仅基于
      2-fraction 对比，统计意义有限。1.5B collapse magnitude 系统性低于 0.5B 是最关键的
      negative finding：暗示 scale 增大会 dilute collapse signal，这对 "practitioners can
      use these signals on production-scale models" 的叙事是根本性打击。Reframe 方向：
      "signal sensitivity is scale-dependent, and larger models may require different
      detection thresholds or entirely different signal families。"

  # ============================================================
  # plan_002: PubMed cross-domain 1.5B × 3 seeds (P0, RUNNING)
  # ============================================================
  - name: "PubMed Cross-Domain Validation (1.5B, 3-seed)"
    plan_id: plan_002
    description: >
      Qwen2.5-1.5B × PubMed × 6 fractions × 3 seeds × 5 gens。
      证明信号在生物医学领域的泛化性。
    expected_results:
      runs_completed: 55  # 90 total, 大部分完成但 frac=0.25 缺失
      fraction_coverage:
        "0.0": [seed42, seed43, seed44]
        "0.1": [seed42, seed43]  # seed44 未完成
        "0.25": []  # 完全未启动
        "0.5": [seed42, seed43, seed44]
        "0.75": [seed42, seed43]
        "1.0": [seed42, seed43, seed44]
      # PubMed gen4 values (seed42, frac=100%)
      ppl_pubmed_100pct_gen4: 187.3
      stable_rank_pubmed_100pct_gen4: 89.7
      spectral_entropy_pubmed_100pct_gen4: 0.849
      token_entropy_pubmed_100pct_gen4: 1.02
      # PubMed gen4 values (seed42, frac=50%)
      ppl_pubmed_50pct_gen4: 28.4
      stable_rank_pubmed_50pct_gen4: 33.1
      # Cross-domain signal direction comparison
      direction_consistent_signals: 8  # /11 total signals
      direction_inconsistent_signals: ["gradient_norm", "hellaswag", "self_bleu"]
      # Recovery
      pubmed_recovery_prevalence_3seed: 0.60  # 60%，低于 WikiText 100%
      pubmed_recovery_ratio_ppl: 0.38
      pubmed_recovery_ratio_stable_rank: 0.15  # 比 WikiText 显著更低
      # Spearman (5 available fractions, 3 seeds)
      spearman_rho_pubmed_median: 0.80
      # Key divergence from WikiText
      pubmed_spectral_entropy_delta_50pct: "+3.2%"  # WikiText +2.4%
      pubmed_stable_rank_delta_50pct: "+8.1%"  # WikiText +5.5%
      pubmed_wikitext_ranking_agreement: "4/7 top signals same rank"
    result_rationale: >
      PubMed 的 3-GPU 并行 + 较小数据集（1410 steps vs 1540）使得 3 seeds 大部分完成，
      但 frac=0.25 因排在 queue 末尾且 GPU0 最慢（~27h ETA）而完全缺失。关键发现：
      PubMed 作为 specialized domain，其词汇分布比 WikiText 窄得多，导致 synthetic data
      的 "指纹" 更深——同等 contamination fraction 下 collapse 更严重（PPL 187 vs WikiText
      预期 ~412 看似更低，但 PubMed baseline PPL ~22 vs WikiText ~12，相对倍数 8.5x vs
      34.7x 说明绝对值不可比）。然而 recovery 更差（prevalence 60% vs WikiText 100%），
      因为窄分布意味着 real data 训练难以 "覆盖" synthetic corruption 的全部影响。
      3/11 信号方向不一致：gradient_norm 在 PubMed 单调递增（WikiText 非单调），hellaswag
      在 PubMed 几乎不变（domain mismatch——HellaSwag 是常识推理，PubMed FT 对其影响本就小），
      self_bleu 方向相反（PubMed collapsed text 更重复但 self_bleu 定义导致方向翻转）。
      这 3 个不一致中 gradient_norm 是 core signal，削弱 Claim 1 泛化性。信号排名仅
      4/7 与 WikiText 一致，特别是 stable_rank 在 PubMed 的 Cohen's d 可能高于 WikiText
      （反转 WikiText 的排名），这进一步证明 ranking 是 config-dependent。
    tables:
      - name: "Tab: PubMed Fraction Coverage"
        columns: [fraction, seed42, seed43, seed44, complete]
        rows:
          - ["0%", "✓", "✓", "✓", "3/3"]
          - ["10%", "✓", "✓", "—", "2/3"]
          - ["25%", "—", "—", "—", "0/3"]
          - ["50%", "✓", "✓", "✓", "3/3"]
          - ["75%", "✓", "✓", "—", "2/3"]
          - ["100%", "✓", "✓", "✓", "3/3"]
      - name: "Tab: PubMed vs WikiText Signal Direction (1.5B, gen4 frac=100%)"
        columns: [signal, wikitext_direction, pubmed_direction, consistent]
        rows:
          - [stable_rank, "↑", "↑", "✓"]
          - [spectral_entropy, "↑", "↑", "✓"]
          - [perplexity, "↑", "↑", "✓"]
          - [token_entropy, "↓", "↓", "✓"]
          - [training_loss, "↑", "↑", "✓"]
          - [gradient_norm, "non-monotonic", "↑ monotonic", "✗"]
          - [hellaswag, "↓", "flat (±0.01)", "✗"]
          - [self_bleu, "↑", "↓", "✗"]
      - name: "Tab: PubMed Recovery Ratios (frac=50%, 3 seeds)"
        columns: [signal, mean_RR, std, wikitext_RR, delta]
        rows:
          - [perplexity, 0.38, 0.04, 0.52, -0.14]
          - [stable_rank, 0.15, 0.09, 0.32, -0.17]
          - [spectral_entropy, 0.13, 0.04, 0.32, -0.19]
          - [token_entropy, 0.41, 0.02, 0.59, -0.18]
    figures_description:
      - "Fig: PubMed vs WikiText severity curves overlay — 显示 PubMed 在低 fraction 更敏感但高 fraction 饱和更早"
      - "Fig: Recovery ratio comparison heatmap (domain × signal) — PubMed 全线更低"
    analysis: >
      PubMed 勉强完成但 frac=0.25 缺失意味着 6-fraction ρ 实际只有 5 点（最多），
      且与 WikiText 的信号排名差异大于预期（4/7 vs 期望 6/7），直接支持 worst tier
      "signals behave differently across domains" 叙事。Recovery prevalence 60% 远低于
      WikiText 100%，与已有 cross_domain_recovery 数据一致（0.5B 时 PubMed 80%），
      暗示 scale↑ + specialized domain 双重压力下 recovery 进一步恶化。gradient_norm
      方向不一致特别伤——它是论文 Claim 3 "non-monotonic under QLoRA" 的支撑信号之一，
      PubMed 说它是 monotonic 的，直接削弱该 finding 的泛化性。

  # ============================================================
  # plan_003: Full FT comparison (DONE, success) — 报告实际数据 + worst framing
  # ============================================================
  - name: "Full FT Comparison (0.5B, N=1)"
    plan_id: plan_003
    description: >
      0.5B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × Full FT。已完成。
    expected_results:
      # 实际数据（已完成）
      fullft_100pct_gen4_ppl: 326.19
      fullft_100pct_gen4_sr: 153.87
      fullft_100pct_gen4_se: 0.889
      fullft_100pct_gen4_te: 0.829
      fullft_100pct_gen4_hellaswag: 0.372
      direction_consistent: "4/4 core signals"
      onset_ratio: 15.3
      post_onset_ratio: 1.11
      # worst-tier framing
      n_seeds: 1
      can_support_method_dependence_claim: false
      reviewer_vulnerability: "N=1 无法区分 method effect 和 seed-specific behavior"
    result_rationale: >
      plan_003 已成功完成且数据强——4/4 core signals 方向一致，collapse morphology 差异清晰
      （Full FT fast-onset-saturation vs QLoRA gradual）。但在 worst tier 下，这些发现的
      价值被 N=1 限制严重削弱：Reviewer 会说 "you have one run, this could be an outlier,
      the morphology difference could reverse with a different seed"。PPL-downstream
      dissociation（QLoRA PPL 839 > Full FT 326，但 QLoRA hellaswag 0.430 > Full FT 0.372）
      是有力发现，但同样 N=1 无法排除 HellaSwag ceiling/floor effect。Terminal spectral
      convergence（SR ~154 vs ~156）在 N=1 下完全不可信——"碰巧接近" 与 "真正收敛" 无法区分。
    tables:
      - name: "Tab: Full FT vs QLoRA gen4 Comparison (actual data, N=1)"
        columns: [metric, Full_FT, QLoRA, direction_match]
        rows:
          - [PPL, 326.19, 839.20, "both ↑ ✓"]
          - [stable_rank, 153.87, 155.64, "both ↑ ✓"]
          - [spectral_entropy, 0.889, 0.884, "both ↑ ✓"]
          - [token_entropy, 0.829, 0.782, "both ↓ ✓"]
          - [hellaswag, 0.372, 0.430, "divergent magnitude"]
    figures_description:
      - "Fig: collapse morphology comparison (已有 PDF) — Full FT gen1 大跳 + 饱和 vs QLoRA 逐代增长"
    analysis: >
      数据本身是论文最强的 Claim 3 证据，但 N=1 在 worst tier 下 = 无法在论文中作为
      claim-level evidence，只能作为 "illustrative example" 或 "case study"。plan_012
      （Full FT 3-seed）在 worst tier 下不会运行（GPU 全被 plan_001/002 占满），所以
      Full FT 对比永远停留在 N=1。Claim 3 的 method-dependence 论点只能依赖方向性证据
      + QLoRA 多 seed 数据，不能做 formal statistical comparison。

  # ============================================================
  # plan_004: Within-gen early warning on 1.5B (depends plan_001)
  # ============================================================
  - name: "1.5B Within-Gen Early Warning Analysis"
    plan_id: plan_004
    description: >
      用 plan_001 的 1.5B 数据做 within-generation signal divergence 分析。纯分析。
    expected_results:
      data_available: "seed42 完整 6 fracs + seed43/44 各 2 fracs"
      effective_n_for_auroc: 1  # 仅 seed42 有足够 fraction 覆盖
      within_gen_auc_stable_rank_1.5B: 0.72
      within_gen_auc_training_loss_1.5B: 0.78
      within_gen_auc_ppl_1.5B: 0.68  # 破坏 "PPL fails" 叙事
      within_gen_auc_spectral_entropy_1.5B: 0.55
      within_gen_auc_token_entropy_1.5B: 0.51
      stable_rank_step50_rel_div_1.5B: 0.14  # (0.5B 时 0.344，amplitude 缩减 60%)
      earliest_detection_step_1.5B: "step 100 (6.5% progress)"  # 晚于 0.5B 的 step 50
      ppl_within_gen_auc_reversal: true  # PPL 从 0.534 (0.5B) 升至 0.68 (1.5B)
    result_rationale: >
      1.5B 的参数冗余使 within-gen signal divergence amplitude 系统性降低。stable_rank
      在 step 50 的 relative divergence 从 0.5B 的 34.4% 降至 ~14%——因为 1.5B 的权重矩阵
      更大，相同程度的 corruption 导致的 Frobenius norm 相对变化更小。AUC 从 0.984 降至
      0.72，仍高于随机但不再 "near-perfect"。关键反转：PPL within-gen AUC 从 0.5B 的
      0.534 升至 1.5B 的 0.68。原因：1.5B 模型对 held-out distribution 的记忆容量更大，
      fine-tuning early steps 对 held-out PPL 的影响在 0.5B 被模型容量限制压制（模型太小，
      即使不 collapse 早期 PPL 波动也大），而 1.5B 的 baseline PPL 更稳定（更低 variance），
      使得 contamination-induced PPL 变化相对更可检测。这直接破坏了 "held-out PPL fails
      at within-gen detection" 的叙事——它在 0.5B fails 但在 1.5B doesn't，说明 PPL 的
      within-gen 检测能力是 scale-dependent 的。training_loss AUC 也从 0.923 降至 0.78，
      但仍是第二强信号。spectral_entropy 在 1.5B 更差（0.55），因为 1.5B 的 spectral
      structure 对 early perturbation 更鲁棒。最早检测从 step 50 推迟到 step 100。
    tables:
      - name: "Tab: Within-Gen AUC Comparison (0.5B vs 1.5B)"
        columns: [signal, "AUC_0.5B", "AUC_1.5B", delta, scale_robust]
        rows:
          - [stable_rank, 0.984, 0.72, -0.264, "✗ (large drop)"]
          - [training_loss, 0.923, 0.78, -0.143, "✗"]
          - [perplexity, 0.534, 0.68, +0.146, "✗ (reversed!)"]
          - [spectral_entropy, 0.61, 0.55, -0.06, "~ (both weak)"]
          - [token_entropy, 0.478, 0.51, +0.03, "~ (both ~random)"]
    figures_description:
      - "Fig: Within-gen ROC curves 0.5B vs 1.5B overlay — stable_rank 曲线从左上角后退，PPL 曲线前移"
      - "Fig: Early warning heatmap (step × signal × scale) — 1.5B 热色区向右推移"
    analysis: >
      这是 worst tier 最具破坏力的结果。(1) stable_rank AUC 跌至 0.72 意味着 Claim 2
      "AUC=0.984" 是 scale-specific 的，不能泛化；(2) PPL AUC 反转意味着 "PPL fails"
      叙事在 1.5B 不成立，必须改为 "PPL effectiveness is scale-dependent"；(3) 两个变化
      合在一起暗示没有任何信号在所有 scale 下都 "work"——核心 practitioner 价值 = 0
      除非加 scale-specific 条件。Reframe 方向：Claim 2 从 "early warning" 变为
      "scale-dependent early warning capability"，stable_rank 在 0.5B 有效但大模型需要
      不同策略。PPL reversal 成为 positive finding："we discover that the optimal
      monitoring signal changes with model scale"。

  # ============================================================
  # plan_005: ROC threshold calibration (depends plan_001 + plan_002)
  # ============================================================
  - name: "ROC Threshold Calibration (Cross-Config)"
    plan_id: plan_005
    description: >
      用 plan_001 + plan_002 数据做跨配置 AUROC + clustered bootstrap。
    expected_results:
      feasible: "partial — plan_001 数据不足，只能做 limited analysis"
      effective_configs_for_pooled_roc: 3  # 0.5B-WikiText, partial-1.5B-WikiText, partial-1.5B-PubMed
      clustered_bootstrap_possible: false  # N=1 完整 seed 无法 cluster
      alternative_analysis: "per-config ROC without bootstrap, qualitative comparison"
      pooled_auc_stable_rank: 0.81  # 混合 scale 后 AUC 降低
      pooled_auc_ppl: 0.63  # 混合后 PPL 在中间地带
      optimal_threshold_stable_rank_0.5B: 1.25  # relative deviation
      optimal_threshold_stable_rank_1.5B: 1.08  # 不同 threshold
      threshold_transferable: false
    result_rationale: >
      Clustered bootstrap 需要多个独立 seed 作为 cluster unit，但 plan_001 仅 seed42
      有完整数据，无法做 proper clustering。只能退回到 per-config 单独 ROC + 定性比较。
      跨 scale pooled AUC 下降因为 0.5B 和 1.5B 的 optimal threshold 不同——0.5B 的
      stable_rank signal 振幅更大（relative deviation 34% vs 14%），如果用 0.5B calibrated
      threshold 在 1.5B 上会大量 miss（false negative rate ↑），反之 1.5B threshold 在
      0.5B 上会大量 false alarm。这证明 threshold 不可跨 scale 迁移，practitioner 需要
      per-scale calibration——进一步支持 "harder than it looks" 叙事。
    tables:
      - name: "Tab: Per-Config Within-Gen AUC (N=1 each)"
        columns: [config, auc_sr, auc_ppl, auc_tloss, optimal_sr_threshold]
        rows:
          - ["0.5B-WikiText", 0.984, 0.534, 0.923, 1.25]
          - ["1.5B-WikiText", 0.72, 0.68, 0.78, 1.08]
          - ["1.5B-PubMed", 0.69, 0.71, 0.74, 1.12]
    figures_description:
      - "Fig: ROC curves per-config overlay — 三条曲线明显分开，没有 universal optimal point"
    analysis: >
      plan_005 在 worst tier 下基本沦为定性分析。无法做 clustered bootstrap = 无法给
      AUC 加 CI = Reviewer 会质疑 "these are point estimates from single runs"。但
      定性发现（threshold 不可迁移）本身是强 negative result，直接进入 reframed Claim 2。

  # ============================================================
  # plan_006: Signal Taxonomy (DONE preliminary, N=3)
  # ============================================================
  - name: "Signal Taxonomy Across Severity Levels"
    plan_id: plan_006
    description: >
      用 plan_001 数据做 per-signal operating range 表征。已有 N=3 preliminary。
    expected_results:
      # plan_001 不完整 → 无法升级到 N=5
      final_n_seeds: 3  # 停留在 preliminary 水平
      final_n_fractions: 2  # 仍只有 0% vs 50%（100% 仅 seed42）
      cohens_d_stable_rank_5seed: null  # 无法计算
      cohens_d_stable_rank_3seed: 3.1  # 从 0.5B 的 9.43 进一步降低（1.5B amplitude 更小）
      cohens_d_spectral_entropy_3seed: 9.2
      cohens_d_perplexity_3seed: 7.8
      ranking_1.5B: "SE > PPL > SR (reversed from 0.5B where SE > distinct > PPL > SR)"
      ranking_stable_across_scales: false
      stable_rank_rank_at_1.5B: 3  # 从 0.5B 的 rank 4 没有恢复
      stable_rank_cv_1.5B: 0.085
    result_rationale: >
      plan_001 完成率低 → plan_006 无法从 N=3 升级到 N=5，taxonomy table 永远带着
      "preliminary, N=3, 2 fractions only" 的标签。1.5B 的 ranking 与 0.5B 不同
      （stable_rank 在 1.5B 更弱因为参数冗余稀释效应），直接证明 ranking is scale-dependent。
      spectral_entropy 仍然最稳定（CV 最低）但仍是 late detector，perplexity 在 1.5B
      的 cross-gen d 仍高。关键：原计划用 5-seed Wilcoxon test 给 tier 结构加 p-value，
      N=3 完全不可能（min p=0.25），只能用 bootstrap CI，但 N=3 bootstrap CI 宽到
      几乎无法区分 Tier 1 和 Tier 2。
    tables:
      - name: "Tab: Signal Ranking Comparison (0.5B N=3 vs 1.5B N=3)"
        columns: [rank, "0.5B signal (d)", "1.5B signal (d)", same]
        rows:
          - [1, "spectral_entropy (33.48)", "spectral_entropy (9.2)", "✓"]
          - [2, "perplexity (20.82)", "perplexity (7.8)", "✓"]
          - [3, "distinct_1 (12.10)", "stable_rank (3.1)", "✗"]
          - [4, "stable_rank (9.43)", "token_entropy (2.8)", "✗"]
    figures_description:
      - "Fig: Signal heatmap (severity × signal, 1.5B) — 仅 2 fractions，热图稀疏"
      - "Fig: Ranking stability across scales — 显示 top 2 稳定，bottom half 乱序"
    analysis: >
      taxonomy 的 "top 2 stable across scales"（spectral_entropy, perplexity）是可用的
      positive finding。但 stable_rank 的 ranking 波动（0.5B rank 4, 1.5B rank 3——
      但 d 值从 9.43 降至 3.1，接近 Tier 2 边界）严重削弱了它作为 "recommended signal"
      的地位。论文需要诚实写：spectral_entropy 和 perplexity 的 ranking 跨 scale 稳定，
      但 stable_rank——within-gen 最强信号——在 cross-gen taxonomy 中不稳定。
      这恰好与分层策略一致：不同维度需要不同信号，没有 universal winner。

  # ============================================================
  # plan_007: Per-layer 1.5B analysis (depends plan_001)
  # ============================================================
  - name: "Per-Layer Collapse Propagation (1.5B)"
    plan_id: plan_007
    description: >
      1.5B model forward-pass SVD 分析 per-layer collapse pattern。需 plan_001 checkpoints。
    expected_results:
      feasible: "limited — 仅 seed42 frac=0/100% checkpoints 可用"
      n_layers_analyzed: 28  # Qwen2.5-1.5B has 28 layers
      v_proj_diffusion_pattern: "consistent with 0.5B — v_proj SR↑ across layers"
      down_proj_collapse_layers: [22, 23, 24]  # 不同于 0.5B 的 L11/L12（scale-specific）
      scale_layer_pattern_match: "partial — v_proj 一致，down_proj collapse 位置不同"
      n_seeds_for_validation: 1
    result_rationale: >
      plan_001 仅 seed42 有 frac=0% 和 frac=100% 的完整 checkpoints，所以 per-layer
      分析只能在 N=1 seed 上做。1.5B 有 28 layers（vs 0.5B 的 24 layers），down_proj
      collapse 的位置从 0.5B 的 L11/L12 迁移到更深层（L22-24），这符合"更大模型的
      collapse 从深层开始"的直觉，但 N=1 无法确认是否 consistent。v_proj diffusion
      pattern 与 0.5B 一致（所有层 SR↑）是 positive，但同样 N=1。整个分析只能作为
      "illustrative example" 放在 appendix，不能支撑论文 claim。
    tables:
      - name: "Tab: Per-Layer Pattern Comparison (0.5B vs 1.5B, N=1)"
        columns: [sub_module, "0.5B pattern", "1.5B pattern", consistent]
        rows:
          - [v_proj, "SR↑ all layers", "SR↑ all layers", "✓"]
          - [k_proj, "SR↑ moderate", "SR↑ moderate", "✓"]
          - [q_proj, "SR↑ boundary layers", "SR↑ boundary layers", "✓"]
          - [down_proj, "SR↓ L11-L12", "SR↓ L22-L24", "方向✓ 位置✗"]
          - [up_proj, "minimal change", "minimal change", "✓"]
    figures_description:
      - "Fig: Per-layer SR delta heatmap (1.5B, seed42) — 28 层 × 5 sub-modules"
    analysis: >
      Per-layer 在 worst tier 下基本是 appendix material。N=1 + 仅两个 fractions
      的对比太弱。但 v_proj 的跨 scale 一致性是可以写的："v_proj consistently shows
      the strongest diffusion across both scales"，作为 practitioner recommendation
      的支撑（"monitor v_proj stable rank"）。down_proj 位置差异有趣但不可 claim。

  # ============================================================
  # plan_008: Self-Recovery Deep Dive (DONE preliminary)
  # ============================================================
  - name: "Self-Recovery Phenomenon Analysis"
    plan_id: plan_008
    description: >
      50% contamination 下的 partial recovery 现象分析。已有 preliminary 结果。
    expected_results:
      # 无法升级到 6 fractions（plan_001 不完整）
      fractions_analyzable: [0, 50, 100]  # 仍只有 3 个，缺 10/25/75
      recovery_prevalence_wikitext_3seed: "100% (9/9)"
      recovery_prevalence_pubmed_3seed: "60% (6/10)"  # 降低
      recovery_prevalence_1.5B: null  # plan_001 数据不足无法做 1.5B recovery 分析
      # 关键缺失
      recovery_threshold_fraction: unknown  # 需要 25%/75% 数据确定 recovery 消失的 threshold
      recovery_vs_fraction_monotonic: unknown
      # 跨 domain 差异
      wikitext_vs_pubmed_recovery_gap: "显著 — PubMed recovery 更弱且更不稳定"
    result_rationale: >
      plan_008 依赖 plan_001 的 intermediate fraction (10%/25%/75%) 数据来回答 "recovery
      在哪个 fraction 消失"。plan_001 不完整意味着这个核心问题无解。现有 3-fraction
      数据（0/50/100%）只能说 "50% 有 recovery, 100% 没有"，无法确定 boundary。
      PubMed 的 recovery prevalence 降至 60% 与 worst tier 假设一致（pubmed_recovery_
      prevalence: [0.4, 0.65]），且 spectral signals 的 recovery ratio < 0.2 意味着
      weight-space damage 在 PubMed 几乎不可逆。论文只能写 "recovery is observed at
      50% contamination in WikiText but is weaker and less consistent in PubMed"，
      无法给出 recovery boundary 或 mechanism。
    tables:
      - name: "Tab: Recovery Prevalence Summary"
        columns: [config, prevalence, mean_PPL_RR, n_seeds, note]
        rows:
          - ["0.5B WikiText (QLoRA)", "100% (9/9)", 0.525, 3, "preliminary"]
          - ["0.5B WikiText (Full FT)", "N/A", "N/A", 1, "plan_003 单 seed"]
          - ["1.5B WikiText (QLoRA)", "N/A", "N/A", "—", "plan_001 不足"]
          - ["1.5B PubMed", "60%", 0.38, 3, "partial fractions"]
    figures_description:
      - "Fig: Recovery ratio comparison (WikiText vs PubMed) — 已有的 cross-domain 对比图"
    analysis: >
      Self-recovery 在 worst tier 下只能作为 "observation" 而非 "finding"，因为 (1) 不知道
      boundary fraction，(2) 不知道 1.5B 是否也有 recovery，(3) PubMed 的低 prevalence
      说明 recovery 不是 universal。写作方向："we observe partial recovery at moderate
      contamination, consistent with Gerstgrasser et al. 2024, but note this is
      domain-dependent and may not extend to larger scales or specialized domains"。

  # ============================================================
  # plan_009: SIGMA head-to-head (DONE, killed)
  # ============================================================
  - name: "SIGMA Head-to-Head"
    plan_id: plan_009
    description: >
      SIGMA spectral metrics 实时集成到 plan_001。已 killed。
    expected_results:
      data_collected: "minimal — 仅 seed42 前几个 runs 有 SIGMA signals"
      sigma_log_det_direction: "+1 (增大)"
      sigma_effective_rank_direction: "+1 (增大)"
      head_to_head_feasible: false
      data_usable_for_paper: false
    result_rationale: >
      plan_009 作为 plan_001 的 passive piggyback，随 plan_001 的低完成率一起失效。
      更关键的是 plan_009 被 killed（可能因 signals.py 集成导致 OOM 或计算开销超预期）。
      少量 SIGMA 数据无法做 systematic head-to-head，论文只能在 Related Work 中
      概念性对比 SIGMA（"requires clean reference distribution"），不能写 empirical
      comparison。这意味着 SIGMA differentiation 停留在 "operational advantage" 的
      论述层面，Reviewer concern "SIGMA differentiation thin" 无法用数据回应。
    tables: []
    figures_description: []
    analysis: >
      plan_009 killed = SIGMA 对比成为 paper limitation。论文必须在 Related Work 中
      承认 "we did not conduct a direct empirical comparison with SIGMA; our
      differentiation is based on methodological differences (clean reference
      requirement vs. reference-free monitoring)"。

  # ============================================================
  # plan_010: 3B Spot-Check (RUNNING)
  # ============================================================
  - name: "3B Model Spot-Check"
    plan_id: plan_010
    description: >
      Qwen2.5-3B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens。
    expected_results:
      completed: true  # frac=0.0 和 0.5 已完成，frac=1.0 ~5.5h ETA
      # 3B gen4 terminal values
      ppl_3B_0pct_gen4: 10.8
      ppl_3B_50pct_gen4: 12.3
      ppl_3B_100pct_gen4: 285.6
      stable_rank_3B_0pct_gen4: 32.1
      stable_rank_3B_50pct_gen4: 33.8
      stable_rank_3B_100pct_gen4: 78.4
      spectral_entropy_3B_0pct_gen4: 0.698
      spectral_entropy_3B_50pct_gen4: 0.713
      spectral_entropy_3B_100pct_gen4: 0.842
      token_entropy_3B_0pct_gen4: 2.31
      token_entropy_3B_50pct_gen4: 2.22
      token_entropy_3B_100pct_gen4: 1.15
      # Direction consistency
      core_signal_directions:
        stable_rank: "↑ (但 magnitude 仅 2.4x vs 0.5B 6.6x vs 1.5B 3.4x)"
        spectral_entropy: "↑ ✓"
        perplexity: "↑ ✓"
        token_entropy: "↓ ✓"
        training_loss: "↑ ✓"
        gradient_norm: "↑ (0.5B 时 non-monotonic)"  # 方向不一致
        hellaswag: "flat (Δ < 0.01)"  # 方向不一致（0.5B QLoRA 也 flat，但 Full FT ↓）
      scale_3B_core_direction_match: 3  # SR, SE, PPL 一致; gradient_norm 和 collapse magnitude 不一致
      collapse_magnitude_3B_sr: "2.4x"  # 继续递减趋势: 0.5B=6.6x, 1.5B=3.4x, 3B=2.4x
      collapse_magnitude_3B_ppl: "26.4x"  # 也递减: 0.5B=53x, 1.5B=34.7x, 3B=26.4x
    result_rationale: >
      3B 完成是 worst tier 的少数亮点之一（N=1, 3 fractions 工作量小）。然而结果证实了
      worst tier 的核心恐惧：collapse signal magnitude 随 scale 持续递减。stable_rank
      从 0.5B 的 6.6x → 1.5B 的 3.4x → 3B 的 2.4x，呈 clear diminishing trend。
      这意味着 7B/13B/70B 模型上 stable_rank 可能完全失效。PPL 也在递减但仍 26.4x，
      说明 output signal 比 spectral signal 更 scale-robust。3/5 core signals 方向一致
      （SR↑, SE↑, PPL↑）但 gradient_norm 在 3B 变成 monotonic（与 0.5B QLoRA 的
      non-monotonic 不一致——可能因为 3B 的 gradient space 更大，non-monotonicity 被
      平均掉了）。HellaSwag flat 与 0.5B QLoRA 一致（是 method effect 不是 scale effect）
      但无法区分，因为 3B 也是 QLoRA。关键：core direction match = 3（out of ~5 core
      signals），刚好在 worst tier 范围 [2,3] 的上界。
    tables:
      - name: "Tab: 3B Gen4 Signals (N=1, seed42)"
        columns: [fraction, ppl, stable_rank, spectral_entropy, token_entropy]
        rows:
          - ["0%", 10.8, 32.1, 0.698, 2.31]
          - ["50%", 12.3, 33.8, 0.713, 2.22]
          - ["100%", 285.6, 78.4, 0.842, 1.15]
      - name: "Tab: Collapse Magnitude Across Scales (frac=100% gen4 SR relative to 0%)"
        columns: [scale, sr_ratio, ppl_ratio, trend]
        rows:
          - ["0.5B", "6.6x", "53x", "—"]
          - ["1.5B", "3.4x", "34.7x", "↓"]
          - ["3B", "2.4x", "26.4x", "↓↓"]
    figures_description:
      - "Fig: Collapse magnitude vs scale — log-log plot 显示 near-linear 递减"
      - "Fig: 3B severity curves (3 fractions) — 形状与 0.5B/1.5B 类似但 dynamic range 更小"
    analysis: >
      3B 数据是 "double-edged sword"。方向一致 = signals 仍然 "work" at 3B；但 magnitude
      递减 = signals 越来越弱。这条递减趋势线是 worst tier 最有力的 negative finding：
      extrapolate 到 7B/13B 意味着 stable_rank 可能 < 1.5x（noise level），spectral
      signals 完全失效。论文必须写 "our signals show diminishing sensitivity with scale,
      suggesting that production-scale models (>7B) may require fundamentally different
      monitoring approaches"。这本身是有价值的 finding（EMNLP negative result），但
      摧毁了 "practitioner tool" 叙事。

  # ============================================================
  # plan_011: LLaMA Cross-Family (planned, not started)
  # ============================================================
  - name: "LLaMA Cross-Family Validation"
    plan_id: plan_011
    description: >
      LLaMA-3.2-1B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens。
      验证信号不是 Qwen-specific。
    expected_results:
      completed: "partial — frac=0% 和 frac=50% 完成, frac=100% gen2 中断"
      reason_incomplete: "GPU 资源被 plan_001 v2 占据，LLaMA 排队到 05-17 才开始，time out"
      # LLaMA gen4 values (where available)
      ppl_llama_0pct_gen4: 18.7
      ppl_llama_50pct_gen4: 22.1
      stable_rank_llama_0pct_gen4: 25.4
      stable_rank_llama_50pct_gen4: 24.1  # 注意：方向相反！SR↓ under 50% contamination
      spectral_entropy_llama_0pct_gen4: 0.721
      spectral_entropy_llama_50pct_gen4: 0.738
      token_entropy_llama_0pct_gen4: 2.19
      token_entropy_llama_50pct_gen4: 2.08
      # frac=100% 仅到 gen2
      ppl_llama_100pct_gen2: 89.4
      stable_rank_llama_100pct_gen2: 42.7
      # Direction consistency
      signal_direction_consistency: 5  # out of 11
      core_signal_issues:
        stable_rank: "方向相反 at frac=50%（SR↓ vs Qwen SR↑），frac=100% gen2 方向正确（↑）"
        gradient_norm: "magnitude 极不同（LLaMA 10x larger fluctuation）"
        hellaswag: "LLaMA 下降更明显（-8% at 50%，Qwen 几乎 flat）"
      llama_signal_direction_consistency: 5  # [3,6] 范围内
      stable_rank_direction_reversed_at_50pct: true
    result_rationale: >
      LLaMA 在 worst tier 下要么未完成（GPU 排队），要么完成但方向不一致。这里取
      "部分完成 + 核心信号方向不一致" 的中间情况。stable_rank 在 LLaMA frac=50% 下降
      而非上升，原因：LLaMA 和 Qwen 的 attention 架构不同（LLaMA 用 RoPE + GQA，
      Qwen 用 RoPE + GQA 但 head 数量和 hidden size 比例不同），在 moderate contamination
      下 LLaMA 的权重矩阵 spectral structure 响应方式不同——Frobenius norm 增长慢于
      σ₁²，导致 SR 下降。这在 frac=100% 下被 overwhelming corruption 掩盖（SR 仍上升），
      但 frac=50% 的 moderate regime 暴露了 architecture-dependent behavior。5/11 信号
      方向一致低于 "cross-family validated" 阈值（8/11）。关键：stable_rank 作为
      Claim 2 的 flagship signal 在 LLaMA 50% 方向相反，这是对 paper framing 的
      根本性打击。即使 frac=100% 方向正确，"the most important signal reverses direction
      at moderate contamination in a different architecture" 是 devastating。
    tables:
      - name: "Tab: LLaMA vs Qwen Signal Direction (frac=50% gen4)"
        columns: [signal, "Qwen direction", "LLaMA direction", consistent]
        rows:
          - [stable_rank, "↑ (+5.9%)", "↓ (-5.1%)", "✗ REVERSED"]
          - [spectral_entropy, "↑ (+1.8%)", "↑ (+2.4%)", "✓"]
          - [perplexity, "↑ (+8.2%)", "↑ (+18.2%)", "✓"]
          - [token_entropy, "↓ (-1.9%)", "↓ (-5.0%)", "✓"]
          - [training_loss, "↑", "↑", "✓"]
          - [gradient_norm, "non-monotonic", "↑ large fluct.", "✗"]
          - [hellaswag, "flat", "↓ (-8%)", "✗"]
          - [self_bleu, "↑", "↑", "✓"]
          - [distinct_1, "↓", "↓", "✓"]
          - [distinct_2, "↓", "↑", "✗"]
          - [distinct_3, "↓", "↑", "✗"]
      - name: "Tab: LLaMA Completion Status"
        columns: [fraction, status, gens_completed]
        rows:
          - ["0%", "DONE", "5/5"]
          - ["50%", "DONE", "5/5"]
          - ["100%", "INCOMPLETE", "2/5 (中断 gen2 training)"]
    figures_description:
      - "Fig: LLaMA vs Qwen stable_rank trajectory at frac=50% — 方向相反的对比图"
      - "Fig: Cross-family signal consistency radar chart — 仅 5/11 在中心"
    analysis: >
      LLaMA 结果是 worst tier 的 "smoking gun"。stable_rank 方向反转直接摧毁了
      Claim 2 的 generality——"stable_rank detects collapse early" 仅对 Qwen 成立。
      论文必须 reframe：从 "stable_rank is a universal early warning signal" 到
      "signal behavior is architecture-dependent; stable_rank direction at moderate
      contamination depends on the model's spectral response to distribution shift"。
      这成为 reframed Claim 3 的核心证据："the same signal can be informative under one
      architecture and misleading under another"。frac=100% 未完成是遗憾但不致命——
      已有 gen2 数据显示极端 contamination 下方向一致（都↑），说明 divergence 仅在
      moderate regime。5/11 一致性意味着论文要写 "architecture-dependent signal behavior"
      而非 "limitation"——这是 finding。

  # ============================================================
  # plan_012: Full FT Multi-Seed (planned, not started)
  # ============================================================
  - name: "Full FT Multi-Seed Extension"
    plan_id: plan_012
    description: >
      0.5B × WikiText-2 × 3 fractions × 2 additional seeds × Full FT。
      将 Full FT 对比从 N=1 升级到 N=3。
    expected_results:
      completed: false
      reason: "GPU 全部被 plan_001/002/010 占据，无剩余 capacity"
      runs_completed: 0
      runs_total: 30
    result_rationale: >
      plan_012 优先级 P1，排在 plan_001 (P0), plan_002 (P0), plan_010 (P2, 但已在运行)
      之后。在 worst tier 下 plan_001 还在缓慢推进（占据 autodl-5090 双 GPU），
      plan_002 占据 cqa1 三个 GPU，plan_010 占 cqa1 第四个 GPU。没有空闲 GPU 给
      plan_012。即使 plan_001 部分完成释放 GPU，剩余时间优先给 plan_011 (P0, LLaMA)
      而非 plan_012 (P1)。结果：Full FT 对比永远停留在 N=1。
    tables: []
    figures_description: []
    analysis: >
      plan_012 不跑 = Claim 3 method-dependence 论点永远基于 N=1。论文必须在 Limitations
      中明确写 "Full FT comparison is based on a single seed and should be interpreted
      as illustrative rather than conclusive"。Reviewer 可能要求 revision 时补跑。

  # ============================================================
  # plan_013: MMLU-mini Downstream Evaluation (depends plan_001)
  # ============================================================
  - name: "MMLU-mini Downstream Evaluation"
    plan_id: plan_013
    description: >
      在 plan_001 所有 checkpoint 上跑 MMLU-mini。纯 inference，~15 min。
    expected_results:
      checkpoints_available: 50  # ~10 runs × 5 gens 的 checkpoints
      checkpoints_needed: 150  # 30 runs × 5 gens
      coverage: "33% of intended"
      mmlu_mini_0pct_gen4_mean: 0.361  # 1.5B baseline
      mmlu_mini_50pct_gen4_mean: 0.358  # 几乎不变
      mmlu_mini_100pct_gen4_seed42: 0.312  # 下降但 N=1
      mmlu_vs_hellaswag_correlation: 0.62  # moderate，非 redundant
      mmlu_collapse_sensitivity: "weak — 仅 100% 有明显下降，50% 无信号"
      mmlu_hellaswag_dissociation: false  # 两个 downstream 方向一致（都不敏感）
    result_rationale: >
      MMLU-mini 能跑（纯 inference，15 min），但只有 plan_001 已完成 runs 的 checkpoints
      可用。1.5B 在 MMLU-mini 的 baseline ~36%（接近 random = 25%），所以 collapse
      导致的 accuracy 下降空间有限。frac=50% 几乎无变化（0.361→0.358, -0.8%）说明
      MMLU-mini 和 HellaSwag 一样对 moderate contamination 不敏感。frac=100% 下降到 31.2%
      但接近 random chance，无法区分 "模型 collapsed" 和 "模型本来就不擅长"。作为第二个
      downstream benchmark 它确认了 "downstream metrics are late/weak collapse detectors"
      的叙事，但没有提供 HellaSwag 之外的新信息。两个 downstream task 之间无 dissociation
      = 论文少了一个有趣的 finding。
    tables:
      - name: "Tab: MMLU-mini Accuracy Across Configs (1.5B)"
        columns: [fraction, gen0, gen2, gen4, "Δ from baseline"]
        rows:
          - ["0%", 0.363, 0.361, 0.361, "—"]
          - ["50%", 0.360, 0.359, 0.358, "-0.8%"]
          - ["100%", 0.358, 0.342, 0.312, "-13.6%"]
    figures_description:
      - "Fig: MMLU-mini vs HellaSwag trajectory comparison — 两条线几乎平行下降"
    analysis: >
      MMLU-mini 完成但价值有限。它确认了 "downstream tasks are not early collapse detectors"
      但没有提供 HellaSwag dissociation 等新发现。在 worst tier 叙事中它是 neutral——
      不伤也不帮。可以写一句 "collapse sensitivity is consistent across two downstream
      benchmarks (HellaSwag, MMLU-mini)"，作为 robustness check 而非 finding。

  # ============================================================
  # plan_014: Within-Gen AUROC on 1.5B 5-seed (depends plan_001)
  # ============================================================
  - name: "Within-Gen AUROC Recomputation (1.5B, Multi-Seed)"
    plan_id: plan_014
    description: >
      用 plan_001 5-seed 数据重新计算 within-gen AUROC + clustered bootstrap。
      将 Claim 2 从 N=1 升级到 N=5。
    expected_results:
      feasible: "degraded — 最多 3 seeds 有 within-gen step-level 数据"
      effective_n_seeds: 3  # seed42 完整, seed43/44 仅 frac=0+50
      clustered_bootstrap_n: 3  # 不足以给 narrow CI
      within_gen_auc_stable_rank_1.5B_3seed_mean: 0.71
      within_gen_auc_stable_rank_1.5B_3seed_ci95: [0.58, 0.84]
      within_gen_auc_ppl_1.5B_3seed_mean: 0.66
      within_gen_auc_ppl_1.5B_3seed_ci95: [0.49, 0.83]
      within_gen_auc_training_loss_1.5B_3seed_mean: 0.76
      within_gen_auc_training_loss_1.5B_3seed_ci95: [0.62, 0.90]
      auc_ci_width: "0.26 (too wide for strong claims)"
    result_rationale: >
      plan_001 只有 3 seeds 有足够的 fraction 覆盖做 within-gen analysis，clustered
      bootstrap 以 seed 为 cluster unit 只有 3 clusters = CI 极宽。stable_rank AUC
      mean 0.71 的 95% CI [0.58, 0.84] 包含了 "barely above random" 到 "decent" 的
      全部范围，无法支撑 strong claim。与 0.5B 的 0.984 (N=1, no CI) 相比，1.5B 的
      CI 下界 0.58 暗示 worst case 下 stable_rank 在 1.5B 可能接近无效。training_loss
      是唯一 CI 下界 > 0.6 的信号，成为 1.5B 的 "least bad" within-gen detector。
      PPL 的 CI 包含 0.5（random），无法 claim PPL within-gen 有效或无效——尴尬的
      "inconclusive" 状态。
    tables:
      - name: "Tab: 1.5B Within-Gen AUROC with Bootstrap CI (N=3 seeds)"
        columns: [signal, mean_AUC, ci_lower, ci_upper, "vs 0.5B (N=1)"]
        rows:
          - [stable_rank, 0.71, 0.58, 0.84, "0.984 (↓↓)"]
          - [training_loss, 0.76, 0.62, 0.90, "0.923 (↓)"]
          - [perplexity, 0.66, 0.49, 0.83, "0.534 (↑?)"]
          - [spectral_entropy, 0.54, 0.41, 0.67, "0.61 (~)"]
          - [token_entropy, 0.50, 0.38, 0.62, "0.478 (~)"]
    figures_description:
      - "Fig: 1.5B AUROC forest plot with CI bars — 几乎所有 CI 都跨越 reasonable vs unreasonable"
    analysis: >
      plan_014 在 worst tier 下产出的是 "wide CI, nothing conclusive"。论文无法写
      "1.5B within-gen AUC = X"，只能写 "1.5B within-gen detection is weaker than 0.5B
      with wide confidence intervals (N=3), suggesting scale-dependent detection
      capability"。这是 honest 的但 reviewer 会说 "insufficient evidence"。Claim 2
      降级为 "demonstrated at 0.5B, with suggestive but inconclusive evidence at 1.5B"。

  # ============================================================
  # Completed MVP experiments (brief entries for completeness)
  # ============================================================
  - name: "MVP Baseline (0.5B × 3 fractions × 1 seed)"
    plan_id: plan_mvp_001
    description: "MVP baseline control. DONE."
    expected_results:
      status: "已完成，actual data 不变"
      note: "MVP 数据在 worst tier 下仍有效——它是唯一 clean, complete dataset"
    result_rationale: >
      MVP 数据不受 worst tier 影响，它已经完成且 gate check PASS。但在 worst tier 叙事下，
      MVP 的 N=1, 3-fraction, 0.5B-only 数据成为论文的 primary evidence base（因为后续
      实验都 incomplete），这本身就是 worst tier 的标志——论文主要靠 pilot study 数据。
    tables: []
    figures_description: []
    analysis: "MVP 数据不变，但成为论文最强证据这个事实本身是 worst tier 的定义。"

  - name: "MVP Main Experiment (0.5B × 3 fractions × 1 seed)"
    plan_id: plan_mvp_002
    description: "MVP main experiment. DONE, PASS."
    expected_results:
      status: "已完成，所有 gate check PASS"
      core_metrics:
        stable_rank_auc_within_gen: 0.984
        ppl_auc_within_gen: 0.534
        spearman_rho_3frac: 1.0
    result_rationale: "实际数据，不是预测。0.5B N=1 ρ=1.0 是 trivial（3 points），论文不能用。"
    tables: []
    figures_description: []
    analysis: "已完成。Worst tier 下这些数值不变但 generalizability 被后续实验 undermine。"

  - name: "MVP Within-Gen Analysis"
    plan_id: plan_mvp_003
    description: "0.5B within-gen temporal analysis. DONE."
    expected_results:
      status: "已完成"
      earliest_detection: "step 50 (3% progress)"
      best_signal: "stable_rank (34.4% deviation)"
    result_rationale: "实际数据。在 worst tier 下仅为 0.5B/N=1 的 point estimate，无 CI。"
    tables: []
    figures_description: []
    analysis: "已完成。Worst tier 下 0.5B 的 early warning 数据仍可用但 scale 泛化失败。"

# ============================================================
# Worst-Tier Summary Table
# ============================================================
summary:
  total_experiments: 14
  completed_as_planned: 4  # plan_003, plan_mvp_001, plan_mvp_002, plan_mvp_003
  completed_degraded: 5  # plan_002 (partial fracs), plan_006 (N=3 stuck), plan_008 (3 fracs), plan_010 (full), plan_013
  incomplete_or_blocked: 3  # plan_001 (10/30), plan_011 (partial), plan_014 (degraded CI)
  not_started: 2  # plan_012 (no GPU), plan_007 (blocked)
  killed: 1  # plan_009

  key_metrics_worst:
    plan001_runs_completed: 10
    spearman_rho_median_across_seeds: 0.78
    within_gen_auc_stable_rank_1.5B: 0.72
    within_gen_auc_ppl_1.5B: 0.68
    within_gen_auc_training_loss_1.5B: 0.78
    cohens_d_spectral_entropy_3seed: 9.2
    cohens_d_perplexity_3seed: 7.8
    cohens_d_stable_rank_3seed: 3.1
    stable_rank_cv_across_seeds: 0.085
    llama_signal_direction_consistency: 5  # out of 11
    scale_3B_core_direction_match: 3  # out of 5
    pubmed_recovery_prevalence: 0.60

  paper_reframe:
    title_direction: "Collapse Monitoring Is Harder Than It Looks: Signal Behavior Is Fundamentally Configuration-Dependent"
    claim1_revised: "Conditional correlation — signals track collapse only within specific scale/domain/architecture configurations"
    claim2_revised: "Scale-dependent early warning — 0.5B detection does not transfer to 1.5B; larger models may need different signal families"
    claim3_promoted: "MAIN CLAIM — the same signal can be informative under one config and misleading under another; the field's implicit assumption of signal transferability is wrong"
    venue: "EMNLP via ARR 6/15 (推迟 3 weeks)"
    venue_rationale: "Negative result + taxonomy 仍适合 EMNLP，但需要 extra time 完善 reframed narrative 和补充可能的 partial plan_001 数据"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e7bd1c1-4810-45be-b65e-be35e9ccb26a",
  "isSidechain": false,
  "requestId": "req_011Cb64dEpKYtGbpzV67q8zV",
  "type": "assistant",
  "uuid": "1d1ab3f4-2e79-4241-aea9-873feb9c5098",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhTqhJoEmQoNa1KpCJzsBd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26992,
      "cache_read_input_tokens": 11841,
      "output_tokens": 20495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 20495,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26992
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：plan001 严重不完整（≤10 runs）；1.5B 未复现 0.5B 的 within-gen 发现；seed 方差摧毁信号排名稳定性；LLaMA 方向不一致或未跑；需要 reframe 但不降级 venue 核心假设：['plan001 仅完成 ≤10/30 runs（基本停留在当前状态），5-se…",
  "leafUuid": "1d1ab3f4-2e79-4241-aea9-873feb9c5098",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze collapse signal robustness across scales and reframe for EMNLP",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：plan001 严重不完整（≤10 runs）；1.5B 未复现 0.5B 的 within-gen 发现；seed 方差摧毁信号排名稳定性；LLaMA 方向不一致或未跑；需要 reframe 但不降级 venue 核心假设：['plan001 仅完成 ≤10/30 runs（基本停留在当前状态），5-se…",
  "leafUuid": "1d1ab3f4-2e79-4241-aea9-873feb9c5098",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze collapse signal robustness across scales and reframe for EMNLP",
  "sessionId": "d7840e40-35a1-4a03-81ea-555b5db73a39"
}
```

---
