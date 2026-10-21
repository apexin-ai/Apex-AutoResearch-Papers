# Mechanistic Evidence Narrative Audit

Generated: 2026-05-29
Scope: CIVO paper mechanistic evidence strength — reward prediction gap environmental differences + error bars/variability reporting

---

## Part 1: Reward Prediction Gap Environmental Differences

### 1.1 Walker–Cheetah Reward Gap Paradox Lacks Direct Mechanistic Explanation

**现状**: 论文在三处描述了这一矛盾：
- Main text F2 (experiments_results.tex:107): "reward fidelity degradation is one transmission pathway but not necessary"
- Discussion (analysis.tex:6): 并列陈述 Walker 1.63× gap 与 Cheetah 1.00× gap
- Appendix §C.1 (appendix.tex:571): "In Cheetah, where the reward gap is absent (1.00×), CIVO must be transmitted through an alternative pathway, possibly dynamics-model prior drift in the latent state space"

论文承认了矛盾但对 Cheetah 的替代路径仅给出推测性语言（"possibly"），未提供直接证据。

**建议改进**: 将 Cheetah "dynamics prior drift" 假说从推测升级为有数据支撑的论述。现有数据可支撑以下论证链：

1. **Embedding geometry 一致性**: Cheetah trained cosine = -0.84 to -0.90（Table cosine_sim），与 Walker 可比，证明 Cheetah 的 RSSM 同样对 dt=1/dt=2 产生了最大分离
2. **Observation fidelity 反转**: Cheetah obs_MSE gap = 0.93×（dt=2 预测反而更好），而 Walker = 1.35×。这暗示 Cheetah RSSM 在 observation 空间"过拟合"了 dt=2 的动力学，可能以牺牲 latent-space calibration 为代价
3. **Embedding norm dynamics 差异**: Walker e(dt) norms grow 1.4-2.2× over training; Cheetah norms remain constant (≤1.04×) despite continued cosine relaxation（appendix.tex:910）。方向变化而非幅度变化暗示不同的 co-adaptation 机制
4. **Random-policy decomposition缺失**: 36%/64% dynamics-bias/actor-exploitation 分解仅在 Walker 上执行。若在 Cheetah 上复现，可直接验证 Cheetah 是否有更高的 dynamics bias 占比来补偿 reward gap 的缺失

建议在 Discussion 段添加 2-3 句，将上述 1-3 点整合为"converging circumstantial evidence"，并在 Limitations 段明确标注"Cheetah random-policy decomposition not performed"作为 future work。

**所需数据来源**: 
- 已有：cosine similarity (Table cosine_sim), obs fidelity (Table rssm_fidelity), norm dynamics (appendix §C.3)
- 缺失但可计算：Cheetah random-policy decomposition（需 N=100 rollouts on Cheetah 008d checkpoint）

**优先级**: P1 — Reviewer 几乎必然会追问"为什么 Cheetah 没有 reward gap 但 CIVO 更严重"。当前 "possibly" 不够。

---

### 1.2 Reward Fidelity Gap 数值在不同 Protocol 间差异大，论文未充分讨论

**现状**: Walker reward prediction gap 在不同测量条件下差异显著：
- v3 standardized (Table rssm_fidelity, 论文主引用): **1.63×**
- v2 analysis (analysis_rssm_fidelity_v2.json): **1.50×**
- Posterior-conditioned extended (Table rssm_fidelity_ext): **3.11×**
- Prior analysis on different checkpoints (rssm_fidelity_analysis.md): baseline 1.30× → 1.56×

论文在 appendix (line 640) 有一句 disclaimer："Reward prediction gap magnitude varies across checkpoints and measurement protocols: this posterior-conditioned analysis yields 3.11×, while v3 standardized analysis yields 1.63×"。但 main text 只引用 1.63× 和 1.00×。

**建议改进**: 
1. 在 main text F2 的 "Mechanism evidence" 段，将 "1.63×" 改为 "1.50–1.63× (protocol-dependent; Appendix C.1)" 来表示这不是一个精确数值
2. 在 Table rssm_fidelity 的 caption 中加一句：measurement protocol affects magnitude (1.50–3.11×) but qualitative pattern (trained > baseline > no-emb) is consistent
3. 对 Cheetah 1.00× 也应注明这是单次测量，无 multi-seed 验证

**所需数据来源**: 已有所有数据，仅需 prose 调整

**优先级**: P2 — 不影响核心结论（定性 pattern 一致），但精确引用单一数值而不讨论 protocol sensitivity 可能被视为 selective reporting

---

### 1.3 RSSM Fidelity 分析缺少 Cheetah Multi-Seed 数据

**现状**: Table rssm_fidelity 中 Walker 有 3 行（baseline, trained, no-emb），Cheetah 只有 1 行（trained），且每行均为单 seed、单 checkpoint。无 error bars。

**建议改进**: 
1. 在 Table rssm_fidelity 的 caption 或 footnote 中明确标注每行的 seed/checkpoint 来源和 n=1 的限制
2. 考虑在 Limitations 段加一句："RSSM fidelity measurements are single-seed single-checkpoint; cross-seed fidelity variability is not characterized"

**所需数据来源**: 若要修复则需在 Cheetah 的多个 seed checkpoint 上运行 fidelity analysis（需服务器计算）

**优先级**: P2 — 单 seed 的 fidelity 数据是 reviewer 可能攻击的点，但论文已将 fidelity gap 定位为"one pathway but not necessary"，降低了单点数据的关键性

---

### 1.4 "多路径"假说可用 Dynamics Bias 数据更直接支撑

**现状**: 论文在 appendix (line 573) 提供了 Walker random-policy decomposition：36% dynamics bias + 64% actor exploitation。这个分解非常有力地说明了 CIVO 的两个必要阶段。但论文没有将此数据与 Cheetah 的情况联系起来进行对比论证。

**建议改进**: 在 appendix §C.1 的 "alternative pathway" 讨论后，添加一个推理段落：
> "Walker 的 random-policy decomposition显示 dynamics bias 贡献 36%。在 Cheetah 中，reward fidelity gap 的缺失（1.00×）意味着 reward-channel 对 dynamics bias 的贡献接近零，因此如果 Cheetah 的 CIVO 严重度更高，则其 dynamics bias 必须几乎完全通过 latent-state prior drift（而非 reward prediction）传导。Cheetah observation fidelity gap 为 0.93×（dt=2 预测更好）进一步支持此解释：RSSM 在 observation 空间的 dt=2 校准良好，但 prior（无 observation 条件）仍可能在 latent space 中产生 reward-favorable 轨迹。"

**所需数据来源**: 已有所有数据，仅需 prose 改进

**优先级**: P1 — 这段推理能将"推测"升级为"有数据约束的推断"，大幅加强叙事

---

## Part 2: Error Bars 和 Variability 报告审计

### 2.1 Table 1 (tab:main_results) Error Bar 审计

**现状**:

| 行 | Eval@final | NVE | 状态 |
|---|---|---|---|
| 001 Baseline (n=4) | $787.7 ± 230.8$ ✅ | 1.00× (无 std) ⚠️ | NVE 是归一化基准，std 不适用 |
| 008d (n=5) | $190.6 ± 90.2$ ✅ | $3.32 ± 1.61×$ ✅ | 完整 |
| 008f (n=4) | $302.4 ± 134.8$ ✅ | $1.09 ± 0.42×$ ✅ | 完整 |
| 008a (n=4) | $820.9 ± 68.8$ ✅ | $0.46 ± 0.19×$ ✅ | 完整 |
| 015b (n=1) | 204.2 | 1.45× | 单 seed，无 std ⚠️ |
| 022b (n=1) | 300.7 | 0.63× | 单 seed，无 std ⚠️ |
| 078 Cheetah (n=4) | $123.2 ± 132.9$ ✅ | med. 2.3× ✅ | median+range 适合极端 outlier |
| 019b-050 (n=1 each) | 单值 | 单值 | 单 seed ⚠️ |
| 046 (n=1) | 150.5 | 1.35× | 单 seed ⚠️ |

**建议改进**: 
1. 单 seed 行已有 n 标注（隐含在 Config 列或缺失）。建议在 caption 中统一声明："Single-seed entries report point estimates; multi-seed entries report mean±std (sample standard deviation)"
2. 015b/022b 是重要的 frozen control，建议补充说明"frozen-embedding multi-seed results in Table three_way_emb (0/6, 0/10)"以缓解单 seed 担忧

**所需数据来源**: 现有数据即可

**优先级**: P3 — Table 1 的多 seed 行已有 ±std，单 seed 行标注清楚，整体合规

---

### 2.2 CIVO Onset Rate 缺少 Binomial Confidence Interval

**现状**: 论文报告的关键 CIVO rate：
- Walker 008d: 3/5 (60%) — 无 CI
- Cheetah 008d: 3/4 (75%) — 无 CI
- Combined 6-DoF: 5/7 (71%) — 无 CI（后扩展为 6/9 in cross_seed_summary）
- Frozen control: 0/16 — 无 CI
- Fisher exact test p < 0.001 ✅ (appendix line 543)

Clopper-Pearson exact 95% CI（计算值）：
- 3/5: [14.7%, 94.7%]
- 3/4: [19.4%, 99.4%]
- 5/7: [29.0%, 96.3%]
- 6/9: [29.9%, 92.5%]
- 0/16: [0%, 20.6%]

**建议改进**: 
1. 在 main text 首次报告 onset rate 时（experiments_results.tex F2 段）添加 Clopper-Pearson CI："CIVO onset occurs in 3 of 5 Walker Walk seeds [95% CI: 15–95%] and 3 of 4 Cheetah seeds [95% CI: 19–99%]"
2. 或至少在 cross-environment table (appendix Table cross_env_civo) 中添加 CI 列
3. 在 Discussion 或 Limitations 段承认 CI 宽度："The wide confidence intervals reflect the inherent variability of CIVO onset; the key discrimination is between trained (6/9) vs. control (0/16) groups, where Fisher exact test confirms significance ($p < 0.001$)"

这是一个平衡：添加 CI 显示 rigor，但也暴露 15-95% 这种极宽区间。建议策略是**主动报告并立即将叙事转向 trained-vs-control 的分组对比（有足够 power）**，而非依赖单组内的 onset rate 精度。

**所需数据来源**: 已有所有 per-seed 数据，CI 纯计算

**优先级**: P1 — Reviewer 最可能攻击的 variability 问题。3/5 和 3/4 在无 CI 的情况下看起来像是 robust finding，但 CI 显示真实范围极宽。主动报告 + 正确 framing 比被 reviewer 指出后 defensive 回应好得多。

---

### 2.3 NVE Peak 跨 Seed Variability 报告不一致

**现状**: 
- Walker 008d: Table 1 报 $3.32 ± 1.61×$ (mean±std, n=5) ✅
- Cheetah 008d: Table 1 报 med. 2.3× with footnote g noting range [0.31, 127.6] ✅
- Cross-env table (appendix): 只报 NVE Peak (max across seeds)，不报 mean/median ⚠️

Per-seed NVE peaks（from cross_seed_summary）：
- Walker 008d: 4.13, 1.62, 1.53, 4.62, 4.72 → mean 3.32±1.61, median 4.13
- Cheetah 008d: 2.3, 0.31, 127.6, 2.3 → mean 33.1±63.0, median 2.3

**建议改进**: 
1. Cross-env table 已报 max NVE Peak，可在 footnote 中补充 Walker mean±std 和 Cheetah median[range]
2. 在正文中讨论 Cheetah s2 (127.6×) 的极端值时，对比其他 onset seeds (2.3×, 2.3×) 来说明 within-environment variability 也很大

**所需数据来源**: 已有

**优先级**: P2 — Table 1 的处理已经合理（Cheetah 用 median+range 是正确的 robust statistics 选择），cross-env table 可补充

---

### 2.4 Table 2 (tab:three_way_emb) 缺少 Error Bars

**现状**: Table 2 报告 gradient condition ablation，NVE peak 和 Eval 均为 range（如 1.53–4.72×）而非 mean±std。样本量从 1/1 到 3/5 不等。

**建议改进**: 
1. 对 n≥3 的行（Trained: n=5, Frozen: n=6），补充 mean±std
2. 对 n=1 的行（Reward detach, Full SGS），保持现状但确保 n 清晰标注

**所需数据来源**: 已有 per-seed 数据

**优先级**: P3 — 这些是 causal ablation 结果，定性 pattern（trained >> frozen/removed）比精确数值更重要

---

### 2.5 Table 3 (tab:intervention_hierarchy) 的 Prevention Rate 缺少 CI

**现状**: Prevention rate 列报告 bare fractions（0/10, 1/6, 3/6, 3/4, 7/7, 6/6）。Fisher exact tests 在 appendix line 543 有报告。但 Table 3 本身无 CI。

**建议改进**: 在 Table 3 的 Rate 列旁添加 95% CI（Clopper-Pearson），或至少在 caption 注明 "Fisher exact p-values in Appendix C.1"。

关键值：
- TCN σ=0.2: 3/6 (50%) [95% CI: 12–88%]
- Wide dual: 3/4 (75%) [95% CI: 19–99%]
- Frozen: 7/7 (100%) [95% CI: 59–100%]
- Removed: 6/6 (100%) [95% CI: 54–100%]

注意 frozen 7/7 的下界是 59%，removed 6/6 的下界是 54%，而 TCN 3/6 的区间与 untreated 0/10 的区间 [0–31%] 有重叠。这其实强化了论文的核心论点：只有 embedding removal/freezing 有 statistically significant prevention。

**所需数据来源**: 已有，纯计算

**优先级**: P2 — 会显著提升 statistical rigor 的外观，且 CI 实际上支持论文结论

---

### 2.6 Reward Prediction Gap 数值缺少 Uncertainty Quantification

**现状**: Table rssm_fidelity 中所有 fidelity gap 值（1.63×, 1.00×, 1.56×, 1.01× 等）均为 point estimates，无 std/CI。每个数据点基于 600 samples (15 episodes × 40 test points)，样本量足够计算 bootstrap CI。

**建议改进**: 
1. 在 Table rssm_fidelity 中为 Gap 列添加 95% bootstrap CI（数据已有，需从 raw JSON 重新计算 per-episode gap 的 variability）
2. 最低限度：在 caption 中注明 "n=600 posterior-conditioned samples per cell; bootstrap CI deferred to supplementary"

**所需数据来源**: 需从服务器的 raw JSON（logdir/analysis_rssm_walker_fidelity.json）计算 per-episode 统计量

**优先级**: P2 — 1.63× vs 1.00× 的对比是核心 mechanistic claim，point estimate 无 uncertainty 可被质疑

---

## 改进优先级汇总

| 优先级 | 发现 | 所需工作 | 类型 |
|--------|------|----------|------|
| **P1** | §1.1 Walker-Cheetah reward gap 缺直接解释 | Prose：整合现有 cosine/obs/norm 数据为 converging evidence | 叙事改进 |
| **P1** | §1.4 多路径假说可用 dynamics bias 数据加强 | Prose：在 appendix 添加推理段落 | 叙事改进 |
| **P1** | §2.2 CIVO onset rate 缺 binomial CI | 计算 CI + 添加到正文/表格 | 统计改进 |
| **P2** | §1.2 Fidelity gap protocol sensitivity 未充分讨论 | Prose：main text 用 range 替代 point estimate | 叙事改进 |
| **P2** | §1.3 Cheetah fidelity 缺 multi-seed | 标注限制 或 补跑实验 | 数据/标注 |
| **P2** | §2.3 NVE peak 跨 seed 报告不一致 | Cross-env table 补 mean/median | 表格改进 |
| **P2** | §2.5 Intervention prevention rate 缺 CI | 计算 CI + 添加到 Table 3 | 统计改进 |
| **P2** | §2.6 Reward fidelity gap 缺 uncertainty | Bootstrap CI 或标注 sample size | 统计改进 |
| **P3** | §2.1 Table 1 单 seed 行标注 | Caption 统一声明 | 标注 |
| **P3** | §2.4 Table 2 缺 mean±std | 补充多 seed 行的 mean±std | 表格改进 |

---

## 注意：数据锁定约束

以上所有建议均为 **prose polish / formatting / statistical annotation** 层面的改进，不涉及修改任何实验数值或表格数据。C001 数据锁定约束下，建议的操作为：
1. 在现有数值旁补充 CI（从已有 per-seed 数据计算，不改变原始数值）
2. 调整叙事措辞（如 "1.63×" → "1.50–1.63× (protocol-dependent)"）
3. 添加 Limitations 段落中的方法论声明
