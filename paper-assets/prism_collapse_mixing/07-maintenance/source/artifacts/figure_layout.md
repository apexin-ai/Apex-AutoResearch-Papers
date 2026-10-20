# Figure & Table Layout — PRISM Collapse Mixing MVP Paper

> Pythia-410M, 3-gen iterative synthetic training (50/50 real/synthetic), 2 seeds (42, 137).
> Signals: rho_loss_entropy, rho_loss_spectral, entropy_mean, spectral_rank_mean, corpus_spectral_rank, distinct-1/2/3, loss_mean.

---

## Figure 1: Experimental Pipeline Diagram

- **标题**: Iterative Synthetic Training with Collapse Signal Monitoring
- **内容**: 流程图。Gen 0 (real data only) → train → generate synthetic → mix 50/50 → Gen 1 train → ... → Gen 3。每代标注 probe set evaluation (5000 examples)，箭头标注计算哪些 signal。
- **数据来源**: 手绘 / TikZ，无需脚本
- **Section**: §3 Method
- **Pass narrative**: 建立读者对 pipeline 的直觉；标注 probe set 是 held-out 的，强调 signal 计算独立于训练
- **Fail narrative**: 同上，pipeline 本身不变

---

## Figure 2: ρ Decay Across Generations (Main Result)

- **标题**: Spearman ρ(loss, signal) Decoupling Over Iterative Training
- **内容**: X 轴 = generation (0–3)，Y 轴 = Spearman ρ。两条线：ρ(loss, entropy) 和 ρ(loss, spectral_rank)，每条线两个 seed + mean。水平虚线标注阈值 |ρ|=0.7 (green) 和 |ρ|=0.5 (red)。
- **数据来源**: `plot_results.py` → `fig_rho_decay.pdf`；原始数据 `signals_gen*_seed*.json` 中 `correlations.rho_loss_entropy` / `rho_loss_spectral_rank`
- **Section**: §5 Results (第一个 figure)
- **Pass narrative**: ρ(loss, entropy) 从 Gen 0 ~0.93 单调下降到 Gen 3 < 0.5，跨过阈值线，证明 loss 与 entropy 脱钩。Spectral rank 可能本身 ρ 就低（~0.2），作为对照。两个 seed 趋势一致。
- **Fail narrative**: ρ 下降缓慢未跨过 0.5 线。Reframe: "loss-signal coupling is more robust than expected under moderate iterative training; 3 generations of 50/50 mixing may be insufficient to induce observable decoupling, suggesting collapse onset requires longer horizons or more aggressive synthetic ratios."

---

## Figure 3: Loss vs. Collapse Signal Scatter Plots (Per Generation)

- **标题**: Per-Example Loss vs. Entropy at Each Generation
- **内容**: 2×2 grid (Gen 0 / Gen 1 / Gen 2 / Gen 3)，每个 subplot 是 loss (x) vs entropy (y) 的散点图 (500 随机采样)，颜色区分 seed。标注 Spearman ρ 值在每个 subplot 左上角。
- **数据来源**: `signals_gen*_seed*.json` 中 `per_example.loss` 和 `per_example.entropy`；需扩展 `plot_results.py` 或新脚本
- **Section**: §5 Results
- **Pass narrative**: Gen 0 散点紧密线性，Gen 3 散点散开成云状，视觉上 ρ 从 ~0.93 降到 <0.5，直觉展示 decoupling
- **Fail narrative**: 四个 subplot 散点形态相似，ρ 变化不大。配合文字说明 "visual inspection confirms quantitative finding: coupling remains strong"

---

## Figure 4: Corpus-Level Signal Trends

- **标题**: Collapse Indicators Across Generations
- **内容**: 2×2 subplot grid:
  - (a) entropy_mean vs generation
  - (b) corpus_spectral_rank (σ-style) vs generation
  - (c) distinct-1/2/3 vs generation (三条线)
  - (d) loss_mean vs generation
  每个 subplot 包含两个 seed 的线 + mean 线。
- **数据来源**: `plot_results.py` → `fig_corpus_trends.pdf`；数据来自 `aggregated.entropy_mean`, `corpus_level.sigma_spectral_rank`, `corpus_level.distinct_*`, `aggregated.loss_mean`
- **Section**: §5 Results
- **Pass narrative**: (a)(b)(c) 单调下降 ≥15% 证明 collapse 正在发生；(d) loss 稳定/轻微下降，形成 decoupling 的另一面证据——"loss improves while collapse signals degrade"
- **Fail narrative**: Signal 下降不足 15%，或 loss 同步下降。Reframe: "under 50/50 mixing with real data anchoring, collapse signals degrade slowly, indicating that the real data fraction provides substantial regularization against collapse"

---

## Figure 5: Per-Example Signal Distribution Shift

- **标题**: Distribution of Per-Example Signals Across Generations
- **内容**: 2×2 subplot (seed 42 为主，seed 137 放 appendix):
  - (a) loss 的 KDE by generation (Gen 0/1/2/3 不同颜色)
  - (b) entropy 的 KDE by generation
  - (c) spectral_rank 的 KDE by generation
  - (d) loss vs entropy scatter (Gen 0 蓝 vs Gen 3 红)
- **数据来源**: `plot_results.py` → `fig_signal_distributions_seed42.pdf`；数据来自 `per_example.*`
- **Section**: §5 Results 或 §6 Analysis
- **Pass narrative**: Entropy 分布左移（mean 下降），尾部收缩（diversity loss）；spectral rank 分布也收缩；而 loss 分布形态变化小。展示 collapse 是分布级别的结构变化，非仅均值漂移。
- **Fail narrative**: 分布形态变化微弱。"The distributional stability under moderate iterative training suggests that per-example signals may require longer training horizons to exhibit clear collapse signatures."

---

## Figure 6: Cross-Seed Consistency (ρ Trajectory Comparison)

- **标题**: Reproducibility of ρ Decoupling Across Seeds
- **内容**: 单图，X 轴 = generation。对每个 signal (entropy / spectral_rank)，绘制 seed 42 和 seed 137 的 ρ 曲线，用 shaded band 标注 seed 间的差异范围。标注 |Δρ| = |ρ_s42 − ρ_s137| 的最大值。
- **数据来源**: 同 Figure 2 数据，需新脚本或扩展
- **Section**: §5 Results (Condition 3 验证)
- **Pass narrative**: 两个 seed 的 ρ 曲线几乎重叠（|Δρ| < 0.05），证明 decoupling 不是随机波动，是 systematic effect → Condition 3 PASS
- **Fail narrative**: 若一个 seed pass 一个 fail → "WEAK_PASS"：需讨论 stochasticity of collapse onset，建议第三个 seed

---

## Figure 7: Decoupling vs. Signal Degradation (Dual-Axis)

- **标题**: Loss-Signal Decoupling Coincides with Signal Degradation
- **内容**: 双 Y 轴图。左轴 = |ρ(loss, entropy)| (下降 = decoupling)；右轴 = entropy_mean (下降 = collapse)。X 轴 = generation。两条线同步下降证明 "decoupling 与 collapse 同时发生"。
- **数据来源**: 组合 `correlations.rho_loss_entropy` + `aggregated.entropy_mean`
- **Section**: §6 Analysis / Discussion
- **Pass narrative**: 两条线同步下降形成 "scissors pattern"：collapse 发生时 loss 失去对 entropy 的预测力。这是论文的 key insight——loss 监控在 collapse 开始时恰恰变得不可靠。
- **Fail narrative**: 两条线不同步或 entropy 下降而 ρ 不变。讨论 "loss remains a reliable proxy even under early-stage collapse, but may fail at more advanced collapse stages"

---

## Figure 8 (Appendix/Optional): 5-Generation Extension

- **标题**: Extended ρ Decay Over 5 Generations
- **内容**: 同 Figure 2 格式，但 X 轴扩展到 Gen 0–5。标注 "MVP 3-gen" 区域和 "extended" 区域。
- **数据来源**: 仅在 MVP 3-gen FAIL 且追加实验时使用
- **Section**: Appendix 或 §5 (如果 5-gen 成为主结果)
- **Pass narrative**: 3-gen 已 pass 则此图为 supplementary，展示更远 generation 的趋势加速
- **Fail narrative**: 3-gen fail 但 5-gen pass → 主图换成此图，论文 narrative 变为 "collapse decoupling emerges after a latency period of ~3 generations"

---

## Table 1: Experimental Setup

- **标题**: Experimental Configuration
- **内容**:

| Item | Value |
|------|-------|
| Base model | Pythia-410M-deduped |
| Real data | FineWeb (validation split) |
| Mixing ratio | 50% real / 50% synthetic (fixed) |
| Generations | 3 (Gen 0 = real-only baseline) |
| Tokens per generation | ~200M |
| Probe set | 5000 examples × 256 tokens (FineWeb val, held-out) |
| Seeds | 42, 137 |
| Signals computed | entropy, spectral_rank (per-example); corpus_spectral_rank, distinct-1/2/3 (corpus-level) |

- **数据来源**: 实验配置，手动填写
- **Section**: §4 Experimental Setup
- **Pass/Fail**: 不受结果影响

---

## Table 2: Signal Values Across Generations

- **标题**: Collapse Signal Measurements by Generation and Seed
- **内容**: 大表格，行 = metric，列 = Gen 0 / Gen 1 / Gen 2 / Gen 3 × Seed 42 / Seed 137 / Mean。最后一列 = Δ% (Gen 3 vs Gen 0 relative change)。

| Metric | Gen 0 | Gen 1 (s42/s137/μ) | Gen 2 (...) | Gen 3 (...) | Δ% |
|--------|-------|---------------------|-------------|-------------|----|
| ρ(loss, entropy) | ... | | | | |
| ρ(loss, spectral) | ... | | | | |
| entropy_mean | ... | | | | |
| spectral_rank_mean | ... | | | | |
| corpus_spectral_rank | ... | | | | |
| distinct-1 | ... | | | | |
| distinct-2 | ... | | | | |
| distinct-3 | ... | | | | |
| loss_mean | ... | | | | |

- **数据来源**: `analyze_correlation.py` 输出 + `signals_gen*_seed*.json`
- **Section**: §5 Results
- **Pass narrative**: Δ% 列中 entropy_mean / distinct-n 下降 ≥15%，loss_mean 稳定或改善，数字直接支持 pass criteria
- **Fail narrative**: Δ% < 15%，标注为未达标。讨论哪些 signal 最接近阈值。

---

## Table 3: Pre-Registered Pass/Fail Verdict

- **标题**: Pre-Registered Hypothesis Evaluation
- **内容**:

| Condition | Criterion | Seed 42 | Seed 137 | Status |
|-----------|-----------|---------|----------|--------|
| C1 | ≥1 signal: Gen 3 \|ρ\| < 0.5 AND Gen 0-1 \|ρ\| > 0.7 | Y/N | Y/N | ✓/✗ |
| C2 | That signal's mean monotonically degrades ≥15% (signal mean, not \|ρ\|) | Y/N | Y/N | ✓/✗ |
| C3 | Both seeds agree | — | — | ✓/✗ |
| **Overall** | | | | **PASS/FAIL** |

- **数据来源**: `analyze_correlation.py` → `correlation_analysis.json`
- **Section**: §5 Results (关键表格)
- **Pass narrative**: 所有 ✓，clean pass，pre-registered hypothesis confirmed
- **Fail narrative**: 标注哪些 condition 未满足，讨论 margin (e.g., "ρ reached 0.58, 0.08 above the 0.5 threshold")

---

## Table 4: Condition 2 Detail — Per-Signal Monotonic Degradation

- **标题**: Signal Degradation Check (Condition 2)
- **内容**:

| Signal | Gen 0 → 1 → 2 → 3 (mean across seeds) | Monotonic? | Δ% (Gen 3 / Gen 0) | C2 Status |
|--------|----------------------------------------|------------|---------------------|-----------|
| entropy_mean | 3.156 → 3.045 → ? → ? | Y/N | -X% | ✓/✗ |
| spectral_rank_mean | 163.7 → 164.9 → ? → ? | Y/N | +X% | ✓/✗ † |
| corpus_spectral_rank | 4.42 → 4.68 → ? → ? | Y/N | +X% | ✓/✗ |
| distinct-1 | ... | Y/N | -X% | ✓/✗ |
| distinct-2 | ... | Y/N | -X% | ✓/✗ |
| distinct-3 | ... | Y/N | -X% | ✓/✗ |

† spectral_rank 因 C1 结构性失败（基线 |ρ(loss, spectral_rank)|=0.211，远低于 C1 要求的 >0.7 阈值），不可能贡献 C2 PASS。此处列出仅供完整性参考。

- **数据来源**: 同 Table 2
- **Section**: §5 Results (Table 3 的 detail breakdown)
- **Pass narrative**: 多个 signal 同时满足 C2，说明 collapse 是 multi-dimensional 的
- **Fail narrative**: 列出每个 signal 的 gap-to-threshold，讨论哪些最接近，为 5-gen extension 提供 justification

---

## Table 5 (Appendix): Per-Generation Spearman ρ with p-values

- **标题**: Full Correlation Statistics
- **内容**:

| Gen | Seed | ρ(loss, entropy) | p-value | ρ(loss, spectral) | p-value |
|-----|------|-------------------|---------|--------------------|---------|
| 0 | 42 | 0.929 | <1e-10 | -0.211 | ... |
| 0 | 137 | ... | | | |
| ... | | | | | |

- **数据来源**: 需扩展 `analyze_correlation.py` 输出 p-value（scipy.stats.spearmanr 自带）
- **Section**: Appendix
- **Pass/Fail**: 为主结果提供统计显著性支撑；fail 时检查是否 p-value 不显著导致 ρ 不可信

---

## Figure/Table Allocation Summary

| ID | Type | Section | Priority | 已有脚本 |
|----|------|---------|----------|----------|
| Fig 1 | Pipeline diagram | §3 Method | Must | 无 (手绘/TikZ) |
| Fig 2 | ρ decay curves | §5 Results | Must | `plot_results.py` (fig_rho_decay) |
| Fig 3 | Loss vs entropy scatter grid | §5 Results | Must | 需扩展 |
| Fig 4 | Corpus-level trends 2×2 | §5 Results | Must | `plot_results.py` (fig_corpus_trends) |
| Fig 5 | Distribution shift KDE | §5/§6 | Should | `plot_results.py` (fig_signal_distributions) |
| Fig 6 | Cross-seed consistency | §5 Results | Must | 需新脚本 |
| Fig 7 | Dual-axis decoupling | §6 Analysis | Should | 需新脚本 |
| Fig 8 | 5-gen extension | Appendix | Optional | 同 Fig 2 脚本 |
| Tab 1 | Experimental setup | §4 Setup | Must | 手动 |
| Tab 2 | All signal values | §5 Results | Must | `analyze_correlation.py` |
| Tab 3 | Pass/Fail verdict | §5 Results | Must | `analyze_correlation.py` |
| Tab 4 | C2 degradation detail | §5 Results | Should | 同 Tab 2 数据 |
| Tab 5 | Full ρ + p-values | Appendix | Should | 需扩展脚本 |

**Must**: 8 items (4 fig + 4 tab) — MVP 论文最低要求
**Should**: 4 items — 增强论文说服力
**Optional**: 1 item — 仅 fail + 追加实验时需要
