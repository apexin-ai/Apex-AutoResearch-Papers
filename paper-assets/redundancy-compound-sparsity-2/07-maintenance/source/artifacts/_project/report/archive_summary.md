# Archive Summary — O(1) Recurrence-Aware KV Eviction (EMA Centroid)

> 项目 archive 日期: 2026-05-12 | 决策: D009→D010 | 模型: DeepSeek-R1-Distill-Qwen-14B | 服务器: westd-16980

## 1. 项目假设与证伪过程

本项目提出用 EMA (Exponential Moving Average) centroid similarity 作为 O(1) per-token KV cache eviction signal，替代 R-KV 的 O(B²) pairwise scoring。核心假设是：EMA 平滑的 centroid 能有效近似 exact mean，以低计算开销识别冗余 token。项目经历两次 pivot：首先 cross-axis 假说（KV similarity → MLP sparsity）在 MVP 中证伪（|r|=0.12）；随后 pivot 到 O(1) EMA eviction，但在 sanity gate（EMA vs random PPL gap ≥5%）上连续失败。gamma sweep 8 个 decay rate 全面测试后，最优 gamma=0.99 仅 beat random 1.38%，远低于 5% 门槛。文献调研揭示根因：EMA smoothing 导致 centroid 收敛到全局均值丧失区分度（DefensiveKV 已给出理论解释），而 KeyDiff 用 exact per-step mean 可达 <0.2pp 损失。EMA 是有偏估计器的本质缺陷无法通过调参修复。

## 2. 关键数据表

### 2.1 Gamma Sweep 全谱（WikiText-2, 32K tokens, 50% budget）

| gamma | PPL | vs Random | vs Full |
|-------|-----|-----------|---------|
| **full** (无驱逐) | **7.1822** | — | baseline |
| **recency** | **7.1758** | — | -0.09% |
| **random** | **7.6353** | baseline | +6.31% |
| ema_0.99 | 7.5302 | **+1.38%** | +4.85% |
| ema_0.95 | 7.6367 | -0.02% | +6.33% |
| ema_0.9 | 7.7788 | -1.88% | +8.31% |
| ema_0.8 | 7.9878 | -4.62% | +11.22% |
| ema_0.7 | 8.1367 | -6.57% | +13.29% |
| ema_0.5 | 8.1352 | -6.55% | +13.27% |
| ema_0.3 | 8.2099 | -7.53% | +14.31% |
| ema_0.1 | 8.1707 | -7.01% | +13.76% |

Gate: beat random ≥5%? **NO** (best: +1.38%)

**关键发现**: gamma=0.99（EMA 衰减极慢 ≈ exact running mean）是唯一 beat random 的值，趋势跨零点在 γ∈(0.95, 0.99)。这与 KeyDiff (exact per-step mean) 的成功完全一致——centroid 思路本身可行，EMA approximation 是失败根因。gamma 越接近 1.0（即 EMA 越接近 exact mean），eviction 质量越高，直接验证了"近似质量是瓶颈"这一结论。

### 2.2 D003 Sanity Check（初始验证）

| 策略 | WikiText PPL | Reasoning PPL |
|------|-------------|---------------|
| full | 7.1822 | 1.2120 |
| recency | 7.1758 | 1.2170 |
| random | 7.6432 | 1.2271 |
| ema_0.9 | 7.7788 | 1.2522 |
| ema_0.7 | 8.1367 | 1.2706 |
| ema_0.5 | 8.1352 | 1.2780 |

### 2.3 Inverted EMA（方向性验证）

| 策略 | WikiText PPL | vs Random |
|------|-------------|-----------|
| inverted_ema_0.9 | 8.7898 | **-15.1%** |
| ema_0.9 | 7.7788 | -1.88% |
| random | 7.6432 | baseline |

反转 EMA 方向（驱逐高分 token）大幅恶化，验证了 EMA scoring 的方向正确性，但正向 EMA 仍不足以 beat random。

### 2.4 辅助分析

| 分析 | 结论 |
|------|------|
| attn_vs_ema 相关性 | Pearson 0.126 / Spearman -0.163，EMA 与 attention 互补但不可区分于噪声 |
| decay_curve | CV decay 0.72-0.96，centroid cos stability >0.998，支持 EMA≈noisy recency |
| heatmap (WikiText) | 中层(16-35) EMA 信号最强但最不稳定；gamma 越大层间方差越小（过度平滑）|
| heatmap (Reasoning) | 与 WikiText pattern 高度一致，差异集中在浅层(0-13) |

## 3. 可转移的发现

1. **EMA Asymmetry**: EMA 的驱逐方向是正确的（inverted_ema +15% 恶化），但 EMA 近似 exact mean 的误差消除了其优势。这区分了"信号方向错"vs"信号精度不够"两类失败。

2. **Per-layer EMA Structure**: 中间层(16-35) EMA centroid similarity 最强但也最不稳定（std 最大），浅层(0-5)最弱。这一 pattern 在 WikiText 和 reasoning traces 上一致，暗示 per-layer adaptive gamma 可能有价值（但本项目未验证）。

3. **Recency 几乎完美**: recency eviction PPL (7.1758) 略优于 full cache (7.1822)，暗示驱逐旧 token 有微弱正则化效果。任何 eviction 方法的真正竞争对手是 recency 而非 random——random 只是最低门槛。

4. **gamma→1 收敛**: gamma 越大 EMA 越接近 recency（gamma=0.99 时 EMA PPL 7.53 接近 recency 7.18），验证了 EMA 的上界即 recency。EMA 在 gamma<0.95 时大幅劣于 random，说明低 gamma 的过度平滑是灾难性的。

## 4. 文献定位

| 方法 | 关系 | 关键差异 |
|------|------|---------|
| **KeyDiff** (NeurIPS'25) | 最近亲——同用 centroid | KeyDiff 用 exact per-step mean (O(B))，我们用 EMA (O(1))。exact mean 有效而 EMA 无效，证明近似质量是关键瓶颈 |
| **DefensiveKV** (ICLR'26) | 理论解释 | Mean aggregation stability assumption 脆弱，importance 突变时灾难性失败。EMA 是 smoothed mean，更脆弱 |
| **NACL** (ACL'24) | 门槛设定 | Random eviction 通过多样性采样提供隐式 robustness，确定性 scoring 必须足够精确才能 beat random |
| **StreamingLLM/Lost-in-Middle** | Recency 解释 | LLM attention 天然 U-shaped (primacy + recency)，recency 与 inductive bias 天然对齐 |

## 5. 对后续研究的建议

1. **Exact centroid vs EMA**: KeyDiff 的 exact per-step mean 在 8K budget 下仅 0.17pp 损失。如果复杂度可接受（O(B) per token），exact centroid 是可行方向。挑战在于 O(B) 是否比 attention-based O(B) 方法（H2O, TOVA）有优势——需要在 throughput 而非 PPL 上证明价值。

2. **Per-layer adaptive strategy**: heatmap 显示不同层 EMA 信号强度差异大。PyramidKV 的层级 budget 分配思路 + 层级 adaptive scoring 可能有价值。

3. **Benchmark 选择**: WikiText-2 32K prefill 上 recency 几乎完美（与 full 差 0.09%），不是 eviction 方法的好 benchmark。建议用 LongBench multi-doc QA 或 Needle-in-a-Haystack，这些任务对中间位置信息有硬依赖。

4. **Query-aware 方向**: HashEvict 和 FASA 的 pre-attention query-aware scoring 在理论上更有前景（直接预测当前步 attention），但复杂度也更高（O(B·d') 或 O(B·F)）。

## 6. 实验清单

| exp_id | conclusion | 关键指标 |
|--------|-----------|---------|
| carc_mvp_seed42 | negative | |r|=0.12, cross-axis 证伪 |
| carc_mvp_seed1337 | negative | |r|=0.11, 确认 cross-axis 证伪 |
| sanity_kv_eviction | negative | EMA vs random gap 0.9% |
| d003_wikitext_32k | negative | EMA vs random gap -1.77% |
| d003_reasoning_traces | negative | EMA vs random gap -2.05% |
| analysis_decay_curve | negative | CV decay 支持 EMA≈noisy recency |
| analysis_attn_vs_ema | negative | |r|<0.3, 互补不可区分于噪声 |
| analysis_gamma_sweep | negative | best gamma=0.99 仅 +1.38% vs random |
| analysis_heatmap | **success** | 中层信号最强，层间结构清晰 |
| inverted_ema_wikitext | negative | inverted PPL +15% vs random |
| inverted_ema_reasoning | negative (killed) | wikitext 已结论性 |
| inverted_ema_reasoning_v2 | killed | D007 skip |

**总计: 1 success / 10 negative / 1 killed / 0 failed**
