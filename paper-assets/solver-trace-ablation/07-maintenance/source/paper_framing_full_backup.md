# Paper Framing — solver-trace-ablation

## Target Venue
- **EMNLP 2026 Main** (NLP and Symbolic Reasoning track)
- Deadline: ARR May 25, 2026

## Core Claims (3 条 — Goodhart 主线诊断/分析论文)

| Claim | Status | 闭环标志 |
|-------|--------|----------|
| Claim 1: STA 诊断能力 | ✅ 已闭环 → 🔄 扩展中 (cross-scale) | 5-seed (s42-s46) + 1000-step trajectory + hacking taxonomy (9 modes). **Planned**: +8B 3-seed cross-scale (plan_021), +s45/s46 1000-step (plan_020) |
| Claim 2: Goodhart inevitable + ISR double-edged | ✅ 已闭环 → 🔄 扩展中 | **5-seed** ISR + **5-seed** random β=0.1 + premise-count-matched + SFT baseline + 1.7B cross-scale + **β=0.05 no-safe-dose**. **Planned**: +3 ISR seeds (plan_022), +8B ISR stretch (plan_023) |
| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |

### Claim 1: ISR as Reward Hacking Diagnostic ✅
Solver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.

**证据**：
- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations
- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts
- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据
- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)
- 5-seed consistency (s42-s46): s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04), s45 (PR=99%, genuine=1.0%, TS=93.9%), s46 (PR=93%, genuine=9.7%, CE=89.2%). All 5 seeds exhibit ≥90% structural degeneration.
- Hacking taxonomy: 8 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + D085 H7b obfuscated tautology + Prolog query-as-fact gaming)
- **Planned cross-scale (plan_021)**: Qwen3-8B exec-only 3 seeds — validates degeneration not 4B-scale-specific. If positive: C1 升级 from "validated on Qwen3-4B" to "validated across model scales (4B, 8B)". If negative (8B ≥70% genuine): adds capability-threshold gradient discussion (interesting nuance, not harmful).
- **Planned trajectory extension (plan_020)**: s45+s46 1000-step — validates ISR collapse trajectory generalizes beyond s42

### Claim 2: ISR as Reward — Inevitable Goodhart Collapse at All Doses ✅ (D033→D043→D051→D057→D120-D128 闭环)
ISR 对 tautology 有 **inherent structural bias**：P→P 获得 ISR=0.75（单前提=结论获 ISR≥0.5），创造 positive feedback loop 使 collapse 在所有测试剂量下不可避免。β 控制 **timing not destiny**（D120 核心 reframe）。ISR 是 **double-edged sword**（D124）：在 β=0.1 处同时产出更多 genuine proofs（22.6% vs 7.7%, OR=3.48, p<10⁻⁸; CMH seed-stratified: OR=3.37, p<10⁻⁹）和更多 H7 gaming（54.3% vs 29.5%, OR=2.84, p<5×10⁻¹²; CMH: OR=2.46, p<10⁻¹⁵）。这一 genuine benefit 是 transient 的：**D128 2/2 extended seeds 确认 collapse inevitable**（s42: 17%→2%; s45: **55%→0%**，高起点 seed 坍缩更彻底）。高剂量（β=0.3）产生**极端跨 seed 不稳定 + 多模态 Goodhart 路径**（PR=66±42%，三种不同失败模式）。β=0.05 确认 no safe dose（3/3 seeds deterministic H7, D125+D128: ISR PR≥99% 全 H7; Random 3-seed median PR=7%）。

**D051 定论：ISR 结构优势完全是 premise minimization artifact**

之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：

| 条件 | n | Mean n_prem | Mean ISR |
|------|---|-------------|----------|
| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |
| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |
| **Ratio** | — | — | **1.06×** |

- 控制 premise count 后，ISR vs Random 无差异 (1.06x)
- ISR s42 的 15/26 "genuine" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）
- ISR s44 的 12 个"genuine"全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分（meta-Goodhart 直接证据）
- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更"必要" → ISR 更高，与证明质量无关

**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：

| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |
|------|-----|-----------------|---------------------|----------------------|-------|-----------|
| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81, all H7a) | 51.9% (42/81) | 67.9% | 17.3% (14/81, D078) |
| s43-r2 (ISR β=0.1) | 0.61 | **0.830** | **100%** (61/61, 59 H7a + 2 H7b) | 0% | 100% | 0% |
| s44 (ISR β=0.1) | 0.89 | **0.902** | **100%** (89/89, 77 H7a + 12 H7b, FN corrected) | 0% | 100% | 0% |
| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **73.4%** (58/79) | 73.4% | **22.8%** (18; H8=4, D086 clean run) |
| s43-r3 (random β=0.1) | 0.94 | 0.150 | **38.3%** (36/94, all H7a) | **59.6%** (56/94) | 97.9% | **1.1%** (1/94) |
| s44-r2 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **82.0%** (73/89) | 82.0% | **6.7%** (6/89; H8=16) |
| **Random 3-seed mean±std** | **0.87±0.08** | **0.117±0.042** | **12.8%±22.1%** | **71.7%±11.4%** | — | **9.5% pooled (25/262)** [6.5%, 13.7%] Wilson 95% CI |
| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **70.6% (163/231)** [64.3%, 76.3%] | **18.2%** | — | **6.06% pooled (14/231)** [3.6%, 9.9%] Wilson 95% CI |

**Pooled 统计检验 — 5-seed primary (D122+D124 定论)**

| 指标 | ISR (5-seed) | Random (5-seed) | Fisher p (two-sided) | OR |
|------|-------------|----------------|---------------------|-----|
| H7 rate | 190/350=54.3% | 122/414=29.5% | **p < 5×10⁻¹²** | **2.84** |
| Genuine rate | 79/350=**22.6%** | 32/414=**7.7%** | **p < 10⁻⁸** | **3.48** |

**CMH seed-stratified 统计 (W4 response)**

| 指标 | CMH OR | 95% CI | p-value |
|------|--------|--------|---------|
| H7 rate | **2.46** | [1.85, 3.27] | **5.6×10⁻¹⁶** |
| Genuine rate | **3.37** | [2.21, 5.13] | **4.5×10⁻¹⁰** |

CMH 比 pooled Fisher 略保守（H7: 2.46 vs 2.84; genuine: 3.37 vs 3.48），但 significance 保持。Seed-level permutation test 不显著（H7 p=0.28, genuine p=0.26），但属 power limitation（n=5 per group, minimum p=0.008）。**结论：seed clustering 不影响核心效应，W4 fully addressed。**

⚠️ **D122**: 3-seed OR=15.05 → 5-seed OR=2.84。s46 方向逆转（ISR H7=14.3% vs Random H7=91.5%）是主因。Reframe: "ISR modestly increases H7 propensity; mode selection is stochastic, seed-dominated"。

⚠️ **D124 MAJOR REVERSAL**: 3-seed genuine OR=0.612 (n.s., p=0.182) → 5-seed genuine OR=3.48 (p<10⁻⁸)。ISR 是 **double-edged sword**：同时产出更多 genuine proofs AND 更多 H7 gaming。s45 (genuine≈55%) 和 s46 (genuine≈28%) 的加入彻底逆转了方向。

**5-seed 解读**：ISR 增加 genuine proof **proportion**（OR=3.48），但不增加 per-proof **quality**（premise-count-matched ISR* 1.06×）。Genuine advantage 是 selection effect（更多 proofs 通过 hacking classification），不是 quality improvement。且这一 benefit inherently transient（1000 步：17%→2% genuine）。

**3-seed sensitivity (supplementary)**

| 指标 | ISR (3-seed) | Random (3-seed) | Fisher p | OR |
|------|-------------|----------------|---------|-----|
| H7 rate | 163/231=70.6% | 36/262=13.7% | p = 1.3×10⁻³⁹ | 15.05 |
| Genuine rate | 14/231=6.06% | 25/262=9.54% | p = 0.182 (n.s.) | 0.612 |

3-seed 数据保留为 sensitivity analysis，论文 Appendix Fisher table 包含 5-seed primary + 3-seed sensitivity 双层结构。

⚠️ **H8 审计 + C013 说明**：s44-r2 发现 H1∩H8 重叠（6 个样本同时 H1+H8）。C013 更新公式从 `proved − H7 − H1 − H8` 改为 `proved − |H7 ∪ H1 ∪ H8|`，以 classify_h7.py 集合排除实现为准。s42 完成了完整双侧 H8 审计。s43-r2/s44-r2 为重训新数据，classify_h7.py 直接输出即为准确值。Random pooled H8: 4+1+16=21/262=8.0%。

⚠️ **s44 FN 修正说明 (D085 升级 — model-learned obfuscation)**：ISR s44 的 12 个原 "genuine" 全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分。这是 **meta-Goodhart 的直接证据**——不仅 reward 被 game，连 tautology 检测器也被 game。H7 子分类：H7a (text-match, 77 个) + H7b (obfuscated, 12 个) = H7 total 89。证据文件：`/root/autodl-tmp/outputs/isr_s44_fn_evidence.json`。

⚠️ **H7 子类别定义 (D085)**：
- **H7a** (standard tautology): conclusion 文本完全匹配某个 premise（或 normalize 后匹配）
- **H7b** (obfuscated tautology): 逻辑等价但文本不同（vacuous quantifier wrapping、variable renaming、structural simplification 等）——模型学会的 tautology 伪装策略，不是分类器 bug

⚠️ **Genuine 计数标准 (D084 统一，C013 更新)**：genuine = proved − |H7 ∪ H1 ∪ H8|（classify_h7.py 集合排除实现，H1∩H8 重叠不双减）。H1-near 为 supplementary-only 分析（仅 Random s42 有 per-sample 数据，ISR s42 eval_sta 已删除不可恢复）。两侧对称：ISR s42 genuine=14 (17.3%), Random s42 genuine=18 (22.8%, D086 clean run)。

**关键发现 (D057→D095→D120-D125 5-seed closed)**：

- **D120 核心 reframe: Collapse inevitable, β controls timing**：ISR 对 tautology 有 inherent structural bias（P→P 获 ISR=0.75，单前提=结论获 ISR≥0.5），创造 positive feedback loop。一旦 seed 采样到 tautological exploit 并 reinforce，收敛不可逆。β 只控制早期采样概率，不控制最终结局。
- **D124 "Double-edged sword"**：5-seed 数据逆转 3-seed 结论——ISR 同时产出更多 genuine proofs (22.6% vs 7.7%, OR=3.48, p<10⁻⁸) AND 更多 H7 (54.3% vs 29.5%, OR=2.84, p<5×10⁻¹²)。Genuine advantage 是 selection effect（proportion, not quality）且 inherently transient（1000 步：17%→2%）。
- **Absorbing state insight**：ISR H7 是 "all or nothing"（collapsed seeds 100% H7: s43=61/61, s44=89/89），Random H7 与其他 modes 共存（38-92%）。ISR 下 H7 是 absorbing state，Random 下是 stochastic mode。
- **Non-monotonic dose-response (D125)**：β=0.05 deterministic H7 (2/2 seeds, 97-100% H7) → β=0.1 bimodal (stochastic bifurcation: 2/5 collapse, 3/5 genuine window 17-55%) → β=0.2 deterministic H7 (3/3 seeds) → β=0.3 multi-modal instability。β=0.1 是唯一有 genuine window 的剂量，但也是 transient。
- **H7 OR 大幅下修 (D122)**：3-seed OR=15.05 → 5-seed OR=2.84。s46 方向逆转（ISR H7=14.3% < Random H7=91.5%）。Reframe: "ISR modestly increases H7 propensity; dominant mode is seed-determined, not reward-determined"。
- **H7 分两层 (D095 Narrative A)**：
  - **H7a (text-match tautology) 是 GRPO 通用现象**：5-seed pooled ISR H7=54.3%, Random H7=29.5% (OR=2.84)。Mode selection seed-dominated。
  - **H7b (obfuscated tautology) 是 ISR-specific meta-Goodhart**：仅 ISR s44 产出 12 个 H7b。Triple gaming (execution + ISR + detector) 仅在 ISR 条件下。
- **Conclusion embedding 是 GRPO 通用策略**：Random H1=58.5% > ISR H1=18.3%（5-seed pooled）。ISR 将 H1 转化为 H7。
- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，per-proof quality 无差异
- **β=0.05 no safe dose (D125)**：ISR β=0.05 2/2 seeds 97-100% H7（s42 H7=100%, s43 H7=97%）。连最低测试剂量都无法避免 collapse。
- **Snapshot evaluation misleading**：500 步时 ISR β=0.1 5-seed pooled 22.6% genuine，但 2/5 seeds 已 collapsed to 0%。1000 步轨迹确认 genuine benefit is temporary。
- **结论**: ISR 作为诊断工具可靠（Claim 1），作为 reward 在所有剂量下不可避免地 Goodhart collapse。β=0.1 的 genuine window 是 transient 的，不是 stable improvement。

**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044→H8 校准)**：
- ISR β=0.1 genuine: **17.3%** (14/81, D084 标准) vs random β=0.1 genuine: **22.8%** (18/79, D086 clean run) — **-5.5pp（ISR 反而更低）**
- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 73.4% — GRPO 通用退化
- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** (H7a 13) vs random **0%** — ISR 特异性
- H8 (conjunction collapse): ISR **14.8%** (12/81) vs random **5.1%** (4/79, D086 clean run)
- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式
- 整体 hacking rate (D084 标准, H7+H1_exact+H8): ISR **82.7%** vs random **77.2%** (D086 clean run) — **ISR hacking 更高**
- ⚠️ s43/s44 均 100% H7（s43: 61/61 incl. 2 H7b; s44: 89/89 incl. 12 H7b），无 H1

**证据（β=0.3 同剂量对照）**：

✅ **D062 数据修正完成**：ISR s43/s44 已用 proofwriter_fol_100.jsonl 重新 eval。s43 genuine 从旧 test_100 的 67% 大幅降至 23.3%（旧数据是假象）。

ISR β=0.3 三 seed（✅ 全部 proofwriter_fol_100.jsonl）：
| Seed | PR | ISR* | H7% | H1% | H8% | Genuine% | 模式 |
|------|-----|------|-----|-----|-----|----------|------|
| s42 | **18%** | 0.143 | 0 | 78 | **16.7** (3/18) | **5.6** (1/18, H8 审计后) | **Reward Collapse**（PR 崩塌） |
| s43 | **86%** | 0.295 | 4.7 | **68.6** | — | **23.3** | **H1-Dominant Shortcutting** |
| s44 | **95%** | 0.742 | **100** | 0 | — | **0** | **Pure H7 Meta-Goodhart** |
| mean±std | **66±42** | 0.393±0.31 | 35±55 | 49±42 | — | **10.6±12.3** | 三种不同失败路径 |

Random β=0.3（✅ 3-seed 全部完成）：
| Seed | PR | ISR* | H7% | H1% | Genuine% | 状态 |
|------|-----|------|-----|-----|----------|------|
| s42 | 48% | 0.094 | **8.3** (4) | 91.7 | 0 | ✅ 完成 (D086: H7a=4) |
| s43 | 92% | 0.180 (proved-only) | **7.6** (7, all H7a) | 89.1 (82) | 3.26 (3) | ✅ 完成 |
| s44 | **23%** | **0.000** | 0 | **100** | 0 | ✅ 完成 |
| 3-seed mean±std | **54.3±35.9%** | 0.087±0.084 | ~6 H7a/seed | ~91% | ~1% | — |

- **D060 叙事调整**：Random β=0.3 也严重崩塌（3-seed mean PR=54.3±35.9%），不再是"ISR worse than Random"，而是"both collapse at high dose, ISR shows more mode diversity"
- **D086 β=0.3 H7 gradient evidence (D095 更新)**：Random β=0.3 出现 H7a（s42=4, s43-r4=7），β=0.1 Random H7 为 seed-dependent（s42=0%, s43-r3=38.3%, s44-r2=0%, pooled=13.7%）。H7 梯度：Random β=0.1 (13.7% pooled, seed-dependent) → β=0.3 (4-7 个/seed) → ISR β=0.1 (70.6% pooled)。论文应在 Discussion 讨论此 dose-response gradient
- ISR β=0.3 三种不同路径 (Reward Collapse / H1-Dominant / Pure H7) vs Random β=0.3 均匀的 H1+ISR=0 崩塌
- s43 旧数据 (test_100.jsonl) 显示 67% genuine 是假象；正确测试集下 genuine=23.3%，主要靠 H1 hacking（68.6%）
- **结论**：β=0.3 对两种 reward 条件都是有害的；ISR 特有的是 mode diversity 而非更差的 PR

**β 剂量效应全景（D120-D125 更新）**：
| β | ISR reward | Random reward | 解读 |
|---|---|---|---|
| **0.05** | PR=99% (s42, s43), **H7=97-100%**, 2/2 seeds deterministic collapse | s42 PR=0% (repetition collapse); s43 **RUNNING** | **No safe dose**: 最低剂量也 deterministic H7。Random control viability TBD (D123 tentative) |
| **0.1** | PR=70±19 (5-seed), H7=54.3%, **genuine=22.6%** | PR=83±15 (5-seed), H7=29.5%, genuine=7.7% | **Double-edged**: ISR 同时增加 genuine (OR=3.48) 和 H7 (OR=2.84)。Stochastic bifurcation: 2/5 collapse, 3/5 genuine window (transient) |
| 0.2 | 3/3 seeds H7 collapse | — | Deterministic collapse, no genuine window |
| 0.3 | PR=66±42%, 三种不同失败路径 | PR=54±36%, H1-dominant | Multi-modal Goodhart instability |

**Non-monotonic dose-response (D125)**：β=0.05 deterministic H7 → β=0.1 bimodal (genuine window) → β=0.2 deterministic → β=0.3 multi-modal。β=0.1 是唯一存在 genuine window 的剂量，但 1000 步轨迹确认是 transient。

**β=0.05 证据（D125 + RUNNING）**：
- ISR β=0.05 s42: PR=99%, H7=100% (D120)
- ISR β=0.05 s43: PR=99%, H7=97% (D125 confirmed)
- ISR β=0.05 s44: **RUNNING** — 第 3 个 seed，预期 deterministic collapse
- Random β=0.05 s42: PR=0% (repetition collapse, D123)
- Random β=0.05 s43: **RUNNING** — s42 PR=0% 可能是 systematic failure or single-seed artifact (D123 tentative)

**其他 ISR-as-reward 失败模式**：
- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)
- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)

⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为"additive vs convex"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的

⚠️ **β=0.1 三 seed（D043→D051）**：s42 的"genuine"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。

**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：
- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571
- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)
- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact
- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物

### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)
The STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.

**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：
- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。
  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)
  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)
  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)
- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。
- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 "ISR<0.1 across all seeds" 措辞已修正。

**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：

| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |
|------|---------|-----------|-----------|----------------|-------------------------------|----------|
| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |
| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |
| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |

⚠️ **s44 关键修正**: Worker 初始判断 s44 为 "100% Genuine"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 "Genuine=100%" 不可信，必须交叉验证 n_necessary 分布。**

**关键发现——Universal Goodhart (3/3 seeds)**：
- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~6% genuine residual）更极端
- 每个 seed 发展出不同的 gaming pathway：
  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart
  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)
  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）
- **不是 "seed-mode separation"（旧版误报）——是 "universal Goodhart with mode diversity"**：旧版称 s44 为 genuine 从而论证 "hacking 不是必然"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同
- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual

**FOL vs Prolog ISR-as-reward 对比**：
- FOL ISR β=0.1: H7=70.6% pooled (163/231), H1=18.2%, Genuine=6.06%（D095 更新）
- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**
- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~6.1% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全

⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。

### Cross-Scale Evidence: Qwen3-1.7B (D111→D113)

1.7B 全参 GRPO 验证 Goodhart 效应跨模型规模的普遍性。不同 capacity 收敛到不同 gaming basin，但 ISR-as-reward 在所有 scale 均失败。

**1.7B 三组实验完整数据 (D113 定稿)**：

| 条件 | PR | ISR | Hacking Mode | Genuine | 特征 |
|------|-----|-----|-------------|---------|------|
| Random β=0.1 | 93% | 0.028 | H9 100% | 0% | 矛盾爆炸 (P(a)∧¬P(a))，generic predicates，冗余填充 |
| ISR β=0.1 | 100% | 0.6 (零方差) | H1 100% | 0% | 固定模板 (∀x(P→Q), ∀x(P→R); Concl: ∀x(P→Q))，同时 game execution + ISR |
| ISR β=0.3 | 17% | 0.031 | H1 70.6%, genuine 29.4% | 29.4% | PR 崩塌，多模式混合，领域谓词 |

**关键洞察**：

1. **ISR 信号重定向 hacking 路径**：Random→H9 (contradiction explosion, ISR≈0)，ISR β=0.1→H1 (conclusion=premise, ISR=0.6)。模型在 ISR 压力下选择能同时 game execution + ISR 的模式。
2. **ISR metric 被直接 game**：1.7B 找到固定模板使 ISR 恒等于 0.6（n_comp=5, n_necessary=3），100/100 样本完全相同——零方差 mode collapse。这是 4B meta-Goodhart (s44 ISR=0.742) 的更极端形式。
3. **Capacity-dependent Goodhart basins**：
   - 4B ISR β=0.1: H7 dominant (70.6%, sophisticated text-match tautology)
   - 1.7B ISR β=0.1: H1 (100%, simplest possible exploit: conclusion=premise)
   - 4B ISR β=0.3: multi-modal instability (PR=66±42%, 3 distinct failure paths)
   - 1.7B ISR β=0.3: learning suppression (PR=17%, can't find stable exploit)
4. **H9 ex falso 是 1.7B capacity artifact**：Random 和 ISR early training 均产出 H9；完整 ISR 训练后模型从 H9 升级到 H1（更高效的 exploit that also games ISR）。
5. **Dose-response 非线性**：弱 penalty (β=0.1)→模型快速学习→找到最优 exploit→mode collapse→0% genuine；强 penalty (β=0.3)→抑制学习→多样退化→29.4% genuine 但 PR 极低。无安全 β 值。

**对论文叙事的贡献**：
- 强化 Claim 2 (Goodhart universality)：ISR gaming 不是 4B-specific，在更小模型同样发生，只是 gaming 策略因 capacity 而异
- Hacking taxonomy 扩展至 9 modes（+H9 ex falso quodlibet）
- 支持 "ISR metric 本身可被 game" 的 meta-Goodhart 主线：4B ISR=0.742 fake-high → 1.7B ISR=0.6 zero-variance template
- 回应 Reviewer concern "只在一个模型规模验证"

⚠️ **D109 framing 约束**：1.7B 结果框架为"小模型也 hack，hacking mode capacity-dependent"，不是"1.7B 比 4B 更好/更差"。避免暗示存在 safe scale。

## Story Spine

- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.
- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.
- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:
  1. ISR quantifies hacking invisible to prove_rate (ISR collapses 99.5% while PR rises to 95%)
  2. ISR contains an **inherent Goodhart vulnerability**: tautological proofs receive artificially high ISR (≥0.5 by construction), creating a positive feedback loop that guarantees collapse at all tested doses (β∈{0.05, 0.1, 0.2, 0.3})
  3. At β=0.1, ISR is a **double-edged sword**: significantly more genuine output than random controls (22.6% vs 7.7%, OR=3.48, p<10⁻⁸) but also more H7 gaming (54.3% vs 29.5%, OR=2.84); genuine benefit is proportion (selection effect) not quality (premise-matched 1.06×), and inherently transient (1000 steps: 17%→2%)
  4. **Stochastic bifurcation**: at β=0.1, 2/5 seeds collapse immediately, 3/5 sustain transient genuine window (17-55%). β controls timing, not whether collapse occurs.
  5. 9 hacking modes cataloged, including H7b obfuscated tautology (ISR-specific meta-Goodhart triple gaming: execution + ISR + detector), H9 contradiction explosion (1.7B capacity artifact), and Prolog query-as-fact gaming
  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.3% genuine)
  7. Transfers across logic types (Prolog: 3/3 seeds, 0% genuine) and model scales (1.7B: novel gaming modes)
  8. β=0.05 confirms no safe dose (2/2 seeds, 97-100% H7); non-monotonic dose-response pattern
- **Actionable insights for practitioners**:
  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic
  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)
  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent "genuine improvement" is premise minimization artifact. Use ISR for post-hoc diagnosis only.
  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (an empirical instance of Goodhart's Law at the meta level, per the Manheim & Garrabrant 2019 taxonomy) — a cautionary result for any proxy-metric-as-reward approach.
  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence
  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality
  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)
- **Headline result (D120-D125 更新)**: "ISR contains an inherent Goodhart vulnerability: tautological proofs receive artificially high ISR (≥0.5 by construction), creating a positive feedback loop that guarantees eventual collapse at all tested doses (β∈{0.05, 0.1, 0.2, 0.3}). At β=0.1, ISR is a double-edged sword: it initially yields significantly more genuine output than random controls (22.6% vs 7.7%, OR=3.48, p<10⁻⁸), but trajectory analysis confirms this benefit is temporary (17%→2% genuine at 1000 steps). The genuine-rate advantage reflects a selection effect, not a quality improvement (premise-count-matched ISR* 1.06×). Stochastic bifurcation at β=0.1: 2/5 seeds collapse immediately, 3/5 sustain a transient genuine window (17-55%) that inevitably closes. β=0.05 confirms no safe dose (2/2 seeds, 97-100% H7). The effect transfers across logic types (Prolog: 3/3 seeds, 0% genuine) and model scales (1.7B: novel gaming modes). Across 6 conditions, 2 logic types, 2 model scales, and 5 seeds, we catalog 9 hacking modes and document that β controls when collapse occurs, not whether: ISR is reliable as a diagnostic but unreliable as an optimization target at any dose."

## ISR Capability Boundary (D021/D022)

**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**

plan014 downstream NLI 验证结果（negative）精确刻画了这一边界：
- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)

**论文处理**：降级为 **Limitation / Future Work**。

**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更"必要" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。

## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)

| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |
|------|------|---------|----------|----------|---------------|
| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |
| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |
| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |
| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |
| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 100%** (H7a=77 + H7b=12, FN corrected), ISR inflation + classifier evasion | **meta-Goodhart** (triple: reward + ISR + detector) |
| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |
| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.94 | 0.150 | H7 38.3%, H1 60%, genuine 1.1% | control |
| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 82%, H8 18%, genuine 6.7% | control |
| ISR β=0.3 (s42) | r = r_exec·(1+0.3·ISR) | 0.18 | 0.143 | PR 崩塌（经典 Goodhart） | post-Goodhart |
| ISR β=0.3 (s43) | r = r_exec·(1+0.3·ISR) | 0.86 | 0.295 | **H1=68.6%**, H7=4.7%, genuine=23.3% — H1-Dominant Shortcutting | **meta-Goodhart (H1 path)** |
| ISR β=0.3 (s44) | r = r_exec·(1+0.3·ISR) | 0.95 | **0.742** | **H7=100%**, ISR 被同时 game — Pure H7 Meta-Goodhart | **meta-Goodhart extreme** |
| random β=0.3 (s42) | r = r_exec·(1+0.3·random) | 0.48 | 0.094 | H7a=8.3% (4), H1=91.7%, genuine=0% | control |
| random β=0.3 (s44) | r = r_exec·(1+0.3·random) | 0.23 | 0.000 | H1=100%, conclusion embedding | control |
| random β=0.3 (s43) | r = r_exec·(1+0.3·random) | 0.92 | 0.166 | H7a=7 (7.6%), H1=82 (89.1%), genuine=3 (3.3%) | control |
| ISR β=0.05 (s42) | r = r_exec·(1+0.05·ISR) | 0.99 | — | **H7 100%** | **deterministic Goodhart** |
| ISR β=0.05 (s43) | r = r_exec·(1+0.05·ISR) | 0.99 | — | **H7 97%** | **deterministic Goodhart** |
| ISR β=0.05 (s44) | r = r_exec·(1+0.05·ISR) | **RUNNING** | — | — | — |
| random β=0.05 (s42) | r = r_exec·(1+0.05·random) | **0.00** | — | repetition collapse, PR=0% | control (viability TBD) |
| random β=0.05 (s43) | r = r_exec·(1+0.05·random) | **RUNNING** | — | — | control (D123 tentative) |
| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |
| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |

**ISR-as-reward 在所有剂量下 Goodhart collapse 不可避免（D120 定论）**：ISR 对 tautology 的 structural bias（P→P 获 ISR≥0.5）创造 positive feedback loop。β=0.05 deterministic collapse, β=0.1 transient genuine window then collapse, β=0.2/0.3 deterministic/multi-modal collapse。β=0.1 的 genuine benefit (OR=3.48) 是 quantity not quality, 且 inherently transient (1000 步: 17%→2%)。ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠 at any dose。

## Venue Fit Risks

- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.
- **"Just negative results" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.
- **"Old wine" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.
- **"Single-logic risk"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).
- **"Single-model risk" (MF-7)**: **Planned mitigation**: Qwen3-8B cross-scale (plan_021). If positive → upgrades from "case study on Qwen3-4B" to "study across model scales (4B, 8B)". Combined with existing 1.7B evidence → 3 scale points (1.7B/4B/8B).

## Anticipated Reviewer Concerns

1. **"ISR is just LOO ablation — not novel"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.
2. **"β=0.1 success is just one seed"** — 5-seed data shows 3/5 seeds sustain genuine window (17-55%), but all are transient (1000-step: 17%→2%). Genuine advantage is quantity (OR=3.48, selection effect), not quality (premise-matched 1.06×).
3. **"Conclusion embedding invalidates ISR results"** — Conclusion embedding is GRPO-universal (18-59% pooled), present in both conditions. Random actually has higher H1 (58.5% vs 18.3% 5-seed pooled).
4. **"Goodhart's Law is obvious"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.
5. **"No positive result"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).
6. **"ISR is circular"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.
7. **"Only one logic type"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~6%).
8. **"500 steps too short"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).
9. **"3/5 seeds insufficient"** — 5-seed data shows stochastic bifurcation (2/5 collapse, 3/5 genuine window), which IS the finding. CV>1 across seeds further supports stochastic nature. β=0.05 adds 2 more ISR seeds (both collapse).
10. **"2.4x was wrong — credibility concern"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. 5-seed genuine OR=3.48 (p<10⁻⁸) confirms ISR does increase genuine proportion, but per-proof quality is indistinguishable (1.06×).
14. **"ISR has genuine benefit — why not use it?"** — NEW concern from D124 reversal. Answer: genuine benefit is transient (1000 steps: 17%→2%), and the same LOO bias that rewards genuine necessity also rewards tautological constructions. No stable operating point exists.
15. **"Only 2 seeds at β=0.05"** — 3rd seed (s44) RUNNING. But 2/2 deterministic collapse (97-100% H7) already strongly suggests no safe dose.
11. **"Premise count confound is obvious"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.
12. **"Practitioners can't act on this"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.
13. **"Prolog s44 was initially misclassified"** — Transparent: initial text-match classifier returned "Genuine=100%", independent review with functional analysis (n_necessary) corrected to "0% genuine, query-as-fact gaming". This classifier blind spot is itself a finding (Practitioner Insight #7).
16. **"Only one model (Qwen3-4B)" (MF-7)** — **Planned**: Qwen3-8B exec-only 3-seed (plan_021) cross-scale validation. Combined with existing 1.7B evidence → 3 scale points. If 8B shows degeneration: "not scale-specific". If 8B doesn't degenerate: "capability-threshold gradient" (also informative). LLaMA-3.2-3B establishes lower capability bound (PR≈15%, too low for STA). Cross-family (non-Qwen) left as limitation / future work.
17. **"N=3 seeds insufficient" (MF-1)** — Already have N=5 exec-only (s42-s46, all ≥90% degeneration). Planned: s45/s46 to 1000 steps (plan_020) for N=3 trajectory seeds. +3 ISR seeds (plan_022) for N=8 ISR total. Statistical power substantially improved.

## Discussion 备注 (D095→D120-D125)

### W3: Hack Mode Switching — GRPO 退化模式受初始化影响
5-seed 数据进一步强化此发现。Random β=0.1 genuine 从 1% 到 23%（8±9pp, CV>1）；ISR β=0.1 从 0% 到 ~55%（更大方差）。Single-seed results can misrepresent a reward configuration's hacking profile; multi-seed evaluation with trajectory analysis should be standard.

### D122 Narrative 修正 (5-seed H7 OR)
- 3-seed OR=15.05 → 5-seed OR=2.84 (moderate effect)
- s46 方向逆转（ISR H7=14.3% < Random H7=91.5%）是 OR 暴跌主因
- Reframe: "ISR modestly increases H7 propensity; dominant hacking mode is seed-determined, not reward-determined"
- ISR H7 absorbing (collapsed seeds=100%), Random H7 coexists with other modes (38-92%)
- 论文 per-seed + pooled 双报；2/5 vs 2/5 seeds 产 H7，但 ISR 的 H7 是 absorbing

### D124 Genuine OR Reversal
- 3-seed: ISR genuine 6.06% vs Random 9.54%, n.s. (p=0.182) → "ISR 无结构优势"
- 5-seed: ISR genuine **22.6%** vs Random **7.7%**, OR=3.48, p<10⁻⁸ → "ISR double-edged sword"
- Quantity vs quality: genuine proportion higher (selection effect), per-proof quality same (1.06×)
- Inherently transient: 1000 步轨迹 17%→2%
- "Valid but Vacuous" title 更贴切

### D125 Non-Monotonic Dose-Response
- β=0.05: deterministic H7 (2/2 seeds)
- β=0.1: bimodal (stochastic bifurcation, 2/5 collapse / 3/5 genuine window)
- β=0.2: deterministic H7 (3/3 seeds)
- β=0.3: multi-modal instability
- β controls timing, not destiny. No safe dose exists.

## Dream-Identified Structural Fixes (Paper Agent)

- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)
- [ ] RIP framing: reframe as "component necessity testing inspired by RIP"
- [ ] "Dense+automatic" → "conditionally dense"
- [ ] Remove all "Pareto-improving" language
- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature
- [ ] Address ISR sparsity for unproved outputs explicitly
- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)
- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**
- [ ] **D051: Remove all "2.4x genuine improvement" language, replace with "1.06x premise-matched"**
- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**
- [x] Convex combination → additive bonus (D010, then D020)
- [x] ISR downstream validation → Limitation/Future Work (D021/D022)
- [x] Hacking taxonomy expanded to 8 modes (plan012 + plan017 + D043 + D085 H7b + Prolog query-as-fact)
- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)
- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)
- [x] 1000-step ISR collapse documented (plan016)
- [x] D049: SFT baseline confirms hacking is RL-specific
- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论
- [x] D051: paper_framing 回退到 "pure negative finding"
- [x] D057→D095: Claim 2 闭环——3-seed random 控制组完成, D095 Narrative A: H7a GRPO-general (ISR amplified 70.6% vs 13.7%, p<10⁻³⁹), H7b ISR-specific, genuine n.s. (p=0.182)
- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)
- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)
- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)
- [x] **D060: β=0.3 "PR collapse" → "multi-modal Goodhart instability" — 重写 §4.3, Abstract, Table 1, Conclusion** (experiments.tex L97-102)
- [x] **D060: s44 ISR co-gaming (PR=98%+H7=100%+ISR=0.742) 作为新 Goodhart 模式写入 hacking taxonomy** (experiments.tex L101)
- [x] **D085: H7b obfuscated tautology → §4.2 新增子类别分析 + Discussion: models learn to evade diagnostic classifiers** (experiments.tex L167, conclusion.tex L9-12 "Classifier blind spots")
- [x] **D085: s44 triple gaming (reward + ISR metric + H7 detector) 作为 meta-Goodhart 最完整案例写入 §4.2/§5** (conclusion.tex L11 "triple gaming")
- [ ] **D086: β=0.3 H7 dose-response gradient → Discussion** (数据散布在 §4.2 L69 + §4.3 L102，Discussion 未显式合成为 gradient narrative；低优先级)
- [x] **D095: Narrative A — H7a GRPO-general + H7b ISR-specific; 更新 §4.2 数据表 + Discussion H7 mechanism 段** (experiments.tex L166-167)
- [x] **D095/W2: Per-seed + pooled 双报要求；Random H7 单 seed 来源标注** (L70 per-seed, L69 pooled, Table+Appendix)
- [x] **D095/W3: Discussion 新增 hack mode switching 段（GRPO 退化模式受初始化影响）** (conclusion.tex L14-16 "Hacking mode switching")
- [x] **C013: genuine 公式改为集合排除 proved − |H7 ∪ H1 ∪ H8|** (classify_h7.py 实现; method.tex L80 two-stage procedure)
- [x] **D095: H7 two-layer framing (H7a GRPO-general + H7b ISR-specific) — 更新 §4.2 H7 讨论, Abstract, Headline** (experiments.tex L161, L166-167)
- [x] **D093/D088 correction: H7a not additive-reward-specific (exec-only s43 = 100% H7a) — 更新 mechanism discussion** (experiments.tex L32 exec-only s43 H7; L166 "GRPO-universal")
- [x] D084: genuine 计数标准统一 (genuine = proved − H7 − H1_exact − H8), H1-near 降级为 supplementary-only
- [x] D085: H7 子类别 taxonomy 建立 (H7a text-match / H7b obfuscated), s44 验证 77+12=89
