# Paper Framing — Collapse-Aware Mixing

> ⚠️ **SUPERSEDED by artifacts/narrative_draft.md** — 本文件保留为历史记录，不再作为当前 framing 参考。原假设（eff_rank 是 leading indicator）已被 D014 否定，三条路径全封（D018）。当前叙事方向见 narrative_draft.md。
>
> ~~Draft — conditional on MVP GO.~~ MVP (v7) 已完成，结论：C1 核心假设 FALSIFIED（eff_rank 在 collapse 中反升）。

## Title (候选)
1. **Closing the Loop: Spectral Effective Rank as a Leading Indicator for Active Model Collapse Control**
2. **From Monitoring to Control: PI-Regulated Data Mixing via Spectral Collapse Detection**
3. **Collapse-Aware Mixing: Closed-Loop Control of Synthetic Data Ratios Using Spectral Effective Rank**

## Story Arc

1. **Problem**: Model collapse in iterative LLM training with synthetic data is well-documented (Shumailov et al., 2024). As models train on their own outputs across generations, quality degrades — PPL rises, diversity drops, tail distributions vanish.

2. **Gap**: Recent work (SIGMA, 2026) demonstrates spectral analysis of embedding Gram matrices can *detect* collapse, and ERBP (2025) provides theoretical grounding for entropy-based reservoir management. But both are **passive** — they diagnose after the fact, offering no mechanism to *prevent* collapse during training.

3. **Insight**: Spectral effective rank of the embedding Gram matrix is a **leading indicator** of collapse — it drops before PPL rises, providing an actionable early warning signal. This temporal gap creates a window for intervention.

4. **Solution**: We build a PI (proportional-integral) controller that monitors spectral effective rank in real-time and dynamically adjusts the real/synthetic data mixing ratio. When rank drops (early collapse signal), the controller increases real data proportion; when rank stabilizes, it relaxes back. This is the first **closed-loop control** system for model collapse.

5. **Result**: The controller automatically maintains model quality across generations without manual tuning of data ratios, outperforming fixed mixing strategies and uncontrolled baselines.

## Core Claims (精确表述)

- **C1 (Leading Indicator)**: In iterative synthetic training of autoregressive LMs, spectral effective rank of the embedding Gram matrix decreases by ≥3 points (absolute) or ≥0.5% (relative) from G0 final at checkpoint t while held-out PPL has not yet increased by ≥2 points or ≥5% from G0 final — establishing effective rank as a leading indicator of model collapse.
  - *Strength*: Empirical observation on Pythia-1B. Does not claim universality across all architectures/scales.

- **C2 (Controller Mechanism)**: A PI controller using spectral effective rank as input signal can automatically adjust real/synthetic data mixing ratio w_t ∈ [0.1, 0.9], responding to collapse dynamics without manual intervention.
  - *Strength*: Mechanistic claim — the controller works as designed. Ablation over Kp, Ki validates sensitivity.

- **C3 (Collapse Mitigation)**: Closed-loop PI control of data mixing ratio reduces model collapse severity (measured by final PPL, generation-over-generation KL divergence, and vocabulary coverage) compared to fixed-ratio baselines across 3+ generations of iterative training.
  - *Strength*: Comparative claim. We do NOT claim collapse is "solved" — only that it is measurably mitigated.

## Novelty vs SIGMA

| Dimension | SIGMA (2026-01) | Ours |
|-----------|-----------------|------|
| Spectral metric | Gram matrix spectral bounds (upper/lower) | Effective rank (entropy-based, continuous) |
| Role of metric | Post-hoc collapse detection/diagnosis | Real-time leading indicator for control |
| Control mechanism | None — passive monitoring only | PI controller with automatic ratio adjustment |
| Data mixing | Not addressed | Core contribution: dynamic real/synthetic mixing |
| Temporal analysis | Collapse detection at convergence | Leading indicator: rank precedes PPL degradation |
| Actionability | "Collapse is happening" | "Collapse is approaching → adjust now" |

**Key differentiator**: SIGMA answers "is collapse occurring?"; we answer "collapse is approaching — here's the automatic corrective action." The relationship is analogous to a **thermometer** (SIGMA) vs. a **thermostat** (ours).

## Novelty vs EntroPIC

EntroPIC（Yang et al., 2025）与本工作均采用 PI 控制范式稳定训练过程，且均证明了纯比例控制（P-only）不足以应对累积误差，积分项（I-term）不可或缺。然而，两者在三个核心维度上存在本质差异：

| Dimension | EntroPIC (Yang et al., 2025) | Ours |
|-----------|------------------------------|------|
| Controlled variable | RL loss coefficients (参数更新空间) | Data mixing ratio w_t (数据空间) |
| Control signal | Policy entropy (输出分布多样性) | Spectral effective rank (内部表征维度利用率) |
| Application | RLHF/GRPO entropy collapse (探索-利用平衡) | Iterative synthetic pretraining collapse (分布退化防护) |
| Intervention surface | Gradient signal weighting | Training data distribution reconstruction |

**控制变量不同。** EntroPIC 调节 RL 训练中正/负样本的 loss 系数，作用于参数更新空间；我们调节 iterative pretraining 中 synthetic-to-real 的数据混合比例，作用于数据空间。前者是梯度信号的加权，后者是训练数据分布的重构。

**控制信号不同。** EntroPIC 以 policy 输出分布的 entropy 为反馈信号；我们以权重矩阵的 spectral effective rank 为反馈信号，度量模型内部表征的维度利用率。Effective rank 是一个更早期的 collapse 前兆指标——entropy 下降时 collapse 可能已经开始，而 spectral rank 的收缩往往先于可观测的性能退化。

**应用场景不同。** EntroPIC 解决 RLHF/GRPO 阶段的 entropy collapse（模型过早收敛到确定性策略）；我们解决 iterative synthetic pretraining 中的 model collapse（多轮自训练导致分布退化）。

**共同点与方法论传承。** 两者共享 PI 控制的方法论内核。EntroPIC 验证了 PI 控制在 ML 训练稳定性问题上的有效性，为本工作提供旁证支持。但 control surface 的根本差异（参数空间 loss weighting vs 数据空间 mixing ratio，policy entropy vs spectral effective rank）确保了充分的新颖性。

## Reviewer Concerns (预期)

### RC1: Scale — "Only Pythia-1B, does this generalize?"
- **预备回应**: Pythia family shares architecture with GPT-NeoX/LLaMA. Effective rank is architecture-agnostic (computed on embedding space, not architecture-specific components). We acknowledge scale as a limitation and frame Pythia-1B as proof-of-concept for the control paradigm. Stretch goal: Pythia-2.8B validation if GPU budget allows.

### RC2: Controller choice — "Why PI, not PID / RL / adaptive?"
- **预备回应**: PI is deliberately simple — the contribution is the *closed-loop framework*, not the specific controller. PI has 2 hyperparameters (vs. RL's many), is interpretable, and has known stability properties. We ablate over Kp/Ki and show robustness. PID's derivative term adds noise sensitivity without clear benefit at our signal frequency. More sophisticated controllers are future work.

### RC3: Metric choice — "Why effective rank vs. other spectral metrics?"
- **预备回应**: Effective rank (exponential of spectral entropy) captures the full eigenvalue distribution in a single scalar, is differentiable, and has information-theoretic grounding. We compare against condition number and trace norm in ablation and show effective rank has the earliest and most consistent leading indicator property.

### RC4: Data scale — "wikitext-103 is tiny, web-scale data may behave differently"
- **预备回应**: MVP uses wikitext-103 (20M tokens/gen) for rapid iteration to validate the control paradigm. The collapse phenomenon is data-scale-invariant in prior work (Shumailov et al.); our contribution is the control mechanism, not the collapse itself. Scale-up experiments (larger datasets, more tokens/gen) are planned as resources allow, but the core signal (spectral rank as leading indicator) should be observable at any scale where collapse occurs.

### RC5: Practical applicability — "Real training pipelines don't retrain from scratch each generation"
- **预备回应**: Our framework applies to any iterative training setting where synthetic data accumulates: knowledge distillation rounds, self-play, RLHF iterations. The PI controller is agnostic to whether training is from scratch or continued. We frame as a general principle applicable to the growing trend of synthetic data in training pipelines.

## Pivot B Framing (conditional on verification — 2026-05-13)

> ⚠️ **Conditional on analyze_generated_eff_rank.py results.** If generated eff_rank does NOT drop, fall back to Plan A (n-gram PI controller).

### Title (Pivot B 候选)
1. **Self-Referential Spectral Analysis for Closed-Loop Model Collapse Control**
2. **Where You Look Matters: Spectral Monitoring on Self-Generated Text for Active Collapse Prevention** ← Reviewer 推荐：简洁、传达核心 insight
3. ~~Collapse-Aware Mixing: Why Holdout Metrics Miss Model Collapse and How Self-Referential Spectral Rank Catches It~~ （过长，19 词，EMNLP 通常限 ~15 词）

### Story Arc (Pivot B)

1. **Problem**: Same — model collapse in iterative synthetic training.

2. **Gap (升级版)**: SIGMA (2026) uses spectral analysis of embeddings on **holdout/reference data** to detect collapse. We show this fundamentally fails — holdout-side metrics (including eff_rank AND PPL) remain stable while generation quality collapses catastrophically (n-gram entropy -86%, vocab coverage -71%). The collapse signature is invisible from the outside.

3. **Insight (新)**: Collapse manifests in the **generation space**, not the holdout space. Computing spectral effective rank on the model's **own generated text** (self-referential spectral analysis) reveals the dimensional collapse that holdout metrics miss. The model's internal representations stay diverse when processing external input, but collapse when self-referencing.

4. **Solution**: Same PI controller, but driven by self-referential spectral effective rank instead of holdout-based rank. Real-time monitoring of generation-space rank as the control signal for dynamic data mixing.

5. **Result**: Same — controller maintains quality across generations.

### Narrative Strategy (Reviewer-informed — D013)

"Holdout 失灵" 在论文中承担双重角色：
1. **Motivation (Section 1-2)**: "The standard practice of monitoring holdout metrics misses early-stage collapse — holdout eff_rank actually *increases* while generation diversity collapses."
2. **Methodological finding (Section 4 分析)**: "We identify a fundamental asymmetry: encoding capability (holdout) decouples from generation diversity during early collapse." → 解释为什么需要 self-referential surface。

**⚠️ Pivot B 存活条件 (D013)**：generated eff_rank 必须证明比 n-gram entropy **额外有价值**。n-gram entropy 在 G1 step 152 已检测到 collapse（6.93→3.92 一步崩塌），如果 generated eff_rank 也在同一时点才检测到且无额外优势，审稿人会质疑 "为什么要做昂贵的 SVD"。至少需要以下之一：
- (a) generated eff_rank 比 n-gram 更早检测（理想）
- (b) generated eff_rank 提供更平滑的连续信号，适合 PI 控制器渐进反馈（n-gram 是阶跃函数，控制器来不及反应）
- (c) generated eff_rank 在 n-gram 未剧变时已渐进下降——即使同 checkpoint 检测，梯度信息更丰富

**验证方法**：analyze_generated_eff_rank.py 运行后，逐 checkpoint 对比 generated eff_rank 与 n-gram entropy 变化梯度。

### Pivot B GO/NO-GO 判定标准 (D014)

**数据来源**：analyze_generated_eff_rank.py 在 G0/G1/G2 final_model 上的输出。

**GO (Pivot B 成立)**：满足以下全部条件：
1. Generated eff_rank 在 G0→G1→G2 呈**下降**趋势（绝对值下降 ≥5% from G0 final）
2. Generated eff_rank 下降方向与 holdout eff_rank **相反**（holdout 上升 +0.96%，generated 下降）
3. compare_eff_rank_vs_ngram.py verdict ≠ PIVOT_B_FAILS
4. 至少满足存活条件 (a)(b)(c) 之一

**MARGINAL (需要额外数据)**：
- Generated eff_rank 下降但 <5%，或 verdict = PIVOT_B_MARGINAL
- 行动：补充中间 checkpoint 分析（从 3 个 final_model 扩展到全部 18 个 checkpoint），验证渐进性

**KILL (Pivot B 不成立)**：
- Generated eff_rank 不下降、上升、或与 holdout 同向
- verdict = PIVOT_B_LOSES 或 PIVOT_B_FAILS
- 行动：启动 Plan C 或 negative result paper（见 Reviewer 预案评估）

### Core Claims (Pivot B)

- **C1-B (Self-Referential Spectral Collapse Detection)**: Self-referential spectral effective rank (computed on model-generated text) detects model collapse that holdout-side metrics (PPL, standard eff_rank) miss entirely within the first 1–3 generations of iterative synthetic training. This establishes the generation space as the correct measurement surface for early collapse monitoring.
  - *Strength*: Empirical. Does not assume holdout metrics "eventually" detect collapse — frames holdout as blind to early-stage collapse. Narrower than "all generation-side > all holdout-side"（后者文献已有支撑）。Claim 特指 spectral analysis on self-generated text — 文献中不存在。
  - *Must show*: generated eff_rank 比 n-gram entropy 提供额外价值（更早/更平滑/更适合 PI 控制）。具体数字留到 Experiments section，claim 中不硬编码。

- **C2-B (Controller Mechanism)**: Same as C2 — PI controller works with self-referential eff_rank as input.

- **C3-B (Collapse Mitigation)**: Same as C3.

### Novelty vs SIGMA (Pivot B — 升级)

| Dimension | SIGMA (2026-01) | Ours |
|-----------|-----------------|------|
| Measurement surface | Holdout/reference data | **Self-generated text** |
| Spectral metric | Gram matrix spectral bounds | Effective rank on generation space |
| Effectiveness | Detects collapse at convergence | **We prove holdout metrics miss early collapse** |
| Role of metric | Post-hoc diagnosis | **Real-time leading indicator + control signal** |
| Control mechanism | None | PI controller with automatic ratio adjustment |
| Key contribution | "Collapse has spectral signatures" | **"Spectral signatures exist in generation space, not holdout space"** |

**Key differentiator (升级)**: SIGMA's spectral approach effectively diagnoses severe collapse at convergence; we show that early-stage collapse — before holdout metrics move — requires monitoring on a different surface (self-generated text). Our work extends the spectral paradigm from diagnosis to prevention. 内部 shorthand: "thermometer on the wrong surface vs thermostat on the right surface"（不用于正式论文措辞）。

### Anticipated RC6 (Pivot B): "Why spectral rank over n-gram entropy?"

- **预备回应**: Spectral effective rank 直接度量表征空间的维度利用率退化——这是 collapse 的**因**（表征坍缩），而 n-gram entropy 是 collapse 的**果**（输出多样性下降）。信息论层面，eff_rank = exp(H(normalized singular values))，捕获了完整的表征几何结构，而 n-gram entropy 仅统计 surface-level token 频率。作为 PI 控制信号，eff_rank 的优势在于：(1) 信息论根基——对 collapse 机制有因果解释力而非纯相关；(2) [具体数据待 analyze_generated_eff_rank.py 验证] 可能提供更平滑的渐进下降信号（vs n-gram 在粗 checkpoint 分辨率下的剧烈变化），但此点需高频 checkpoint 数据支撑，不作为主要论据。如果实验显示 eff_rank 无额外优势，需要重新评估 Pivot B 可行性。
- **注意**: "n-gram 是阶跃函数" 的论断可能是 checkpoint 分辨率 artifact（v7 间隔 5M tokens），更高频 checkpoint 下 n-gram 可能也是渐进的。不以此作为主要差异化论据。

### Anticipated RC7 (Pivot B): "What's the computational overhead of self-referential monitoring?"

- **预备回应**: Self-referential eff_rank 需要 (1) 生成 N 段文本 (2) forward pass 取 hidden states (3) SVD。比 holdout PPL 贵（holdout 只需 forward pass，不需 generation）。但 (a) monitoring 频率可调（如每 K training steps 采样一次），成本与 K 成反比；(b) 提前检测 collapse 后调整 data mixing 避免的无效训练时间 >> monitoring 成本；(c) 生成阶段可以 batch 处理。[具体 GPU 时间量化待实验补充]

### Anticipated RC8 (Pivot B): "How stable is generated eff_rank across sampling runs?"

- **预备回应**: Holdout eff_rank 是确定性的（相同数据→相同结果），generated eff_rank 取决于 sampling（temperature, top_p, seed）。需证明方差可控。[实验计划：同一 checkpoint 多次采样（5-10 次）计算 generated eff_rank，报告 mean ± std，论证信噪比足够做 PI 控制信号]

## Evidence Map

| Claim | Required Evidence | Experiment | Status |
|-------|-------------------|------------|--------|
| C1 | Temporal gap: rank drops ≥3pts/0.5% before PPL rises ≥2pts/5% | mvp_pilot_v7 | running (v7) |
| C1 | Statistical significance of temporal gap (bootstrap CI) | leading_indicator_analysis | planned |
| C1 | Effective rank vs alternative spectral metrics | spectral_metric_comparison | planned (P0) |
| C2 | Kp/Ki grid sensitivity on Pythia-1B | pi_sweep_p0 | planned (P0) |
| C2 | PI floor test: w_min=0.1 alone vs PI dynamics | baseline_w01 | planned (P0) |
| C2 | PI vs best fixed ratio, 3-seed significance | seed_validation | planned (P0) |
| C2 | Controller responds correctly to rank changes | controller_ablation | planned |
| C2 | Controller robust to hyperparameter variation | controller_sensitivity | planned |
| C3 | Collapse lower bound: pure synthetic (w=0) | baseline_w0 | planned (P0) |
| C3 | No-collapse upper bound: pure real (w=1) | baseline_w1 | planned (P0) |
| C3 | PI vs best fixed ratio, 3-seed significance | seed_validation | planned (P0) |
| C3 | PI control outperforms fixed ratios in final PPL | controller_vs_baselines | planned |
| C3 | PI control maintains higher vocab coverage, lower KL | controller_vs_baselines | planned |
| C3 | Multi-generation stability under control (5 gen) | full_collapse_run | planned |
| RC1 | Scale validation (stretch) | cross_model_validation | stretch |
| RC3 | Metric comparison justification | spectral_metric_comparison | planned (P0) |
| **Pivot B** | | | |
| C1-B | Generated eff_rank drops while holdout eff_rank doesn't | analyze_generated_eff_rank | pending (v7 G2 eval) |
| C1-B | Generated eff_rank provides value beyond n-gram entropy | compare_eff_rank_vs_ngram | pending (after above) |
| C1-B | Per-layer eff_rank reveals collapse locus | analyze_layer_eff_rank | pending (after above) |
| RC6 | Generated eff_rank smoother/earlier than n-gram | compare_eff_rank_vs_ngram | pending |
| RC7 | Monitoring overhead quantification | pivot_b_overhead_timing | planned |
| RC8 | Generated eff_rank stability across sampling runs | pivot_b_sampling_stability | planned |
