# D009 后论文强度评估 + exp-002 成本效益分析

> 评估日期: 2026-05-19 | 基于: 13 experiments (10 DONE, 1 RUNNING, 2 KILLED), 9 decisions

---

## Part 1: Dream-Style 模拟审稿

### 审稿人视角 (EMNLP ARR)

**Paper type**: Empirical analysis — quantifying per-example divergence under aggregate convergence in hybrid recurrent architectures

**Summary**: The paper uses Wang et al.'s model zoo (72 models, 3 architectures × 5 attention ratios × 2 scales) to show that adding attention to linear recurrent models causes cross-architecture convergence specifically on LAMBADA (ρ=-1.0, BCa CI [-1.0, -0.7]), while per-example effects are nearly non-overlapping (Jaccard < 0.10) and decouple from aggregate dynamics.

---

### Claim-by-Claim 证据评估

#### Claim 1: Task-Specific Convergence — 证据强度 2.5/5

**支撑证据**:
- LAMBADA ρ=-1.0, exact permutation p=0.017 (two-tailed)
- BCa percentile CI [-1.0, -0.7], 100% valid resamples ρ<0
- 效应量大：cross-arch std 从 0.024 → 0.005 (79% 下降)
- 10-benchmark survey: 仅 LAMBADA 显著，task-specificity 本身成为发现

**弱点**:
- **6-Bonferroni adj-p=0.100，10-Bonferroni adj-p=0.167** — 均不 survive。审稿人会首先看这个数字。
- **n=5 data points** 做 Spearman 相关，统计功效极低。ρ=-1.0 在 n=5 时 p 的下界就是 1/60=0.0167，无法更显著。
- BCa CI 的 valid-only 策略（丢弃 11.25% degenerate resamples）会被质疑为 cherry-picking。虽然有理论依据（boundary degeneracy），但审稿人可以合理指出 full CI [-1.0, 0.0] 触及零。
- 10 benchmark 只 1 个显著 ≈ 名义 α=0.05 下的期望假阳性率。Task-specificity reframing 虽巧妙，但审稿人可反驳："LAMBADA 纯上下文预测的特殊性是 post-hoc rationalization"。
- GDN-excluded sensitivity: LAMBADA ρ 降至 -0.7 (p=0.233)。虽然 ARC-Easy 改善至 -0.9 (p=0.083)，但这加强了对核心结果 GDN-dependence 的担忧。

**审稿人可能反应**: "BCa CI 是有意义的，但 Bonferroni 不通过 + n=5 的固有局限 + GDN-excluded 结果弱化 = 难以单独支撑一个 claim。Task-specificity reframing 是可以接受的 narrative，但需要更强的理论驱动（为什么 LAMBADA 而非其他 context-retrieval 任务如 StoryCloze？）"

#### Claim 2: Scale-Dependent Convergence — 证据强度 2.0/5

**支撑证据**:
- 1.3B vs 340M 的 binary contrast（1.3B 完全收敛，340M 部分/非单调）
- 与容量假说一致

**弱点**:
- **仅 2 个 scale points**，无法建立趋势，也无法排除 confound（不同 scale 的训练 dynamics 差异）
- 没有 7B 数据（Wang et al. 也不提供）
- "Scale is a necessary condition" 的表述缺乏足够证据 — 2 点二元对比支撑不了 necessity claim
- 340M rebound mechanism (exp-007) 尚未执行

**审稿人可能反应**: "Two scale points provide an observation, not a finding. Frame as preliminary evidence, not a standalone claim."

#### Claim 3: Per-Example Divergence + Decoupling — 证据强度 3.5/5

**支撑证据**:
- Jaccard < 0.10 across all pairwise comparisons — 量化上有说服力
- **Decoupling finding (exp-010)**: aggregate σ 单调下降 vs Jaccard 4% 时即饱和 — 这是本文最原创的发现
- Surface features 不解释 within-arch helped/hurt (exp-003, negative)
- Perplexity 不解释 within-arch (exp-003-p2, negative)
- Cross-arch KW 显著 (p=0.0005 for hurt samples) — 效应是 structured，非随机噪声
- Net asymmetry 递增 (0.013 → 0.040) — attention 越多，架构特异性效应越分化

**弱点**:
- Per-example divergence 是 well-documented phenomenon (D'Amour et al. 2022, ensemble diversity literature)。Contribution 是 quantification，非 discovery — 这在 *ACL venue 的 novelty bar 偏低。
- 仅在 LAMBADA 上有 per-example 数据。如果其他 benchmark 也做 per-example 分析但 Jaccard 同样低，task-specificity 叙事会受冲击（underspecification 是 universal 的，与 task type 无关）。
- exp-004 (attention weight patterns) 还在跑，暂无 mechanistic description

**审稿人可能反应**: "Decoupling finding is genuinely interesting and well-executed. The quantification is clean. However, connecting this to D'Amour et al. 2022 weakens novelty — you're confirming underspecification exists in one more domain. The decoupling timescale analysis partially saves it."

---

### Dream Weakness 评估

| Weakness | 状态 | 缓解程度 | 剩余风险 |
|----------|------|----------|----------|
| **W1: Single-benchmark** | D009 策略 | 中等 | BCa CI defensible 但 Bonferroni failure 仍是最大攻击面。Task-specificity rationalization 可被质疑为 post-hoc |
| **W2: Missing related work** | 待写 | 未缓解 | 20+ references 需要。ensemble diversity + underspecification positioning 是 acceptance 的必要条件 |
| **W3: Mechanistic overclaiming** | 已 reframe | 大部分缓解 | "Characterization" 替代 "mechanism" 是正确的。exp-004 结果需谨慎使用（descriptive only） |
| **W4: Incremental over Wang** | exp-009 文档化 | 部分缓解 | 4-dimensional differentiation 是合理的，但审稿人对 "analytical depth on existing models" 的接受度因人而异 |

---

### Overall Assessment 预测

**最可能评分: 2.5 — Borderline Findings**

理由:
- **上行路径到 3.0 (Findings)**: 如果 Related Work 做得出色（20+ refs, 精准 positioning as "quantification in emerging architecture class"），writing 质量高，统计报告透明且自信（不过度 apologize），decoupling finding 作为核心 contribution 被突出 → 3.0 可达。
- **下行风险到 2.0 (Resubmit)**: 如果审稿人对 BCa valid-only 策略不买账（view as cherry-picking），或将 task-specificity reframing 判定为 spin，或认为整体 novelty 不足 → 2.0。
- 3 个 reviewer 中预期 1 个给 3.0-3.5（appreciate empirical rigor + decoupling），1 个给 2.5（borderline novelty），1 个给 2.0-2.5（single benchmark + incremental）。

**到 Findings 3.0 的关键差距**:
1. ★★★ Related Work quality — 这是最大 leverage point，0 GPU cost
2. ★★☆ Task-specificity 的理论解释需要更深（为什么 LAMBADA 而非 xstorycloze/COPA？context-prediction 的形式化定义是什么？）
3. ★★☆ Decoupling finding 需要作为 title/abstract 级 contribution，不能埋在 Section 4
4. ★☆☆ exp-004 attention patterns — 如果能 show architecture-specific attention distributions correlate with helped/hurt，adds descriptive depth

**评分分布预测 (3 reviewers)**:

| Scenario | R1 | R2 | R3 | Average | 概率 |
|----------|----|----|-----|---------|------|
| 乐观（writing 出色 + related work 强） | 3.5 | 3.0 | 2.5 | 3.0 | 25% |
| 基线（正常执行） | 3.0 | 2.5 | 2.5 | 2.7 | 45% |
| 悲观（审稿人不买 BCa + task-specificity） | 2.5 | 2.0 | 2.0 | 2.2 | 30% |

---

## Part 2: exp-002 成本效益分析

### exp-002 规格
- **内容**: HellaSwag/ARC-C/ARC-Easy 上 per-example logprob 分析 (extract + Jaccard + helped/hurt characterization)
- **GPU 时间**: 20h (RTX PRO 6000)
- **距 DDL**: ~27 天 (June 15)

### D009 后 exp-002 目标重估

| 原始目标 | D009 后状态 | 分析 |
|----------|------------|------|
| 验证多 benchmark per-example 收敛 | ❌ 目标已失效 | Claim 1 已从 "多 benchmark 收敛" 转向 "LAMBADA-specific"。exp-002 不再服务原始目的 |
| 为 Claim 1 提供多 benchmark Jaccard 证据 | ⚠️ 部分相关 | 如果 non-LAMBADA benchmarks 也有低 Jaccard → underspecification is universal → 实际上**削弱** task-specificity 叙事 |
| 补充材料 | ✅ 仍有价值 | 多 benchmark per-example 数据可放 appendix，展示 thoroughness |

### 三种结果场景

**场景 A: Non-LAMBADA benchmarks 也有低 Jaccard (~0.10)**
- 含义: underspecification 是 universal 的，与 task type 无关
- 影响: **负面** — 削弱 "task-specific convergence" 叙事。如果 per-example divergence 到处存在，LAMBADA 的特殊性仅在 aggregate 层面，削弱 Claim 1 的解释力
- 审稿人可能说: "Per-example divergence is task-independent; your aggregate convergence finding on LAMBADA alone is even thinner"

**场景 B: Non-LAMBADA benchmarks Jaccard 明显更高 (~0.3-0.5)**
- 含义: LAMBADA 的低 Jaccard 与其 aggregate convergence 有关联 → convergent tasks have more diverse per-example dynamics
- 影响: **正面** — 直接支持 decoupling 叙事，且提供 cross-task contrast
- 但这个结果需要理论解释，且可能只提供 suggestive evidence (n=4 tasks, no formal test)

**场景 C: 结果 noisy，无清晰 pattern**
- 含义: per-example dynamics 在 non-retrieval tasks 上不稳定
- 影响: **中性** — 放进 supplementary，不改变主 story

### 成本-收益矩阵

| 维度 | 评估 |
|------|------|
| **GPU 成本** | 20h / 单卡 = ~1 天 wall time。exp-004 完成后才能开始。实际可用窗口 ~25 天 |
| **信息价值** | 场景 A (40% 概率): 负面信息，强迫修改叙事。场景 B (25%): 有价值但非 decisive。场景 C (35%): 浪费 |
| **对评分的影响** | 乐观估计: +0.1-0.2 (supplementary completeness)。exp-002 不解决任何 Major weakness |
| **机会成本** | 20h GPU 可跑 exp-007 (2h, 340M rebound) + 留 18h buffer 给 exp-004 follow-ups 或论文 figure 生成 |
| **风险** | 场景 A 会制造新的 narrative problem，需要额外时间修补 |

### 结论: exp-002 **不推荐执行**

理由:
1. **Expected value 为负**: 场景 A（最可能）实际上损害论文叙事
2. **不解决核心弱点**: W1/W2/W3/W4 没有一个因 exp-002 改善
3. **LAMBADA 单 benchmark 的 per-example 数据已经足够**: Claim 3 的 evidence chain（Jaccard < 0.10 + decoupling + surface/perplexity negative + cross-arch KW）已完整
4. **GPU 时间更好的用途**: exp-007 (2h) 为 Claim 2 提供 340M rebound 分析；剩余时间留给 exp-004 follow-up

### 不做 exp-002，论文是否仍够 Findings 3.0？

**是的**，条件是:
- Related Work 做到位 (20+ refs, 精准 positioning)
- Decoupling finding 提升为 title-level contribution
- 统计报告透明 (BCa + Bonferroni caveat + GDN sensitivity)
- exp-004 提供 descriptive attention pattern data
- Writing quality 高于平均

exp-002 的缺失不会被审稿人注意到——审稿人不会主动想 "为什么没在其他 benchmark 做 per-example 分析"，除非作者自己提起。

---

## Part 3: 下一步优先级排序

### Tier 1 — 必须完成 (决定 accept/reject)

| 优先级 | 任务 | 预估投入 | 理由 |
|--------|------|----------|------|
| P0 | **Related Work 撰写** | 2-3 天 writing | W2 是唯一 blocking weakness。20+ references covering: ensemble diversity, underspecification, dataset cartography, hybrid architecture survey, attention interpretability |
| P0 | **exp-004 完成 + 分析** | ~数小时 (已在跑) | Claim 3 的 descriptive depth。如有 architecture-specific attention patterns → 有价值的 figure |
| P0 | **Paper draft** | ~7-10 天 | DDL June 15，最迟 June 5 开写。Decoupling 作为核心 contribution |

### Tier 2 — 强烈推荐 (提升 0.2-0.5 分)

| 优先级 | 任务 | 预估投入 | 理由 |
|--------|------|----------|------|
| P1 | **LAMBADA task-specificity 理论解释** | 1 天 analysis | 为什么 LAMBADA 而非 StoryCloze？需要 formal characterization of "pure context prediction" vs "commonsense completion" |
| P1 | **exp-007: 340M rebound** | 2h GPU + 0.5 天 analysis | Claim 2 补充。340M 非单调 rebound 的 mechanism — 如果能解释 why，增加论文深度 |
| P1 | **Figure/table 质量** | 2-3 天 | Decoupling 的 dual-axis figure (aggregate σ vs Jaccard across attention ratios) 是 key visual |

### Tier 3 — 可选 (marginal improvement)

| 优先级 | 任务 | 预估投入 | 理由 |
|--------|------|----------|------|
| P2 | exp-002 (multi-benchmark per-example) | 20h GPU + 1 天 | 上述分析: expected value 为负，不推荐 |
| P2 | Dream 重新模拟 (post-D009) | 0.5 天 | 验证新 framing 评分是否改善，但不改变实际行动 |

### 时间线建议 (27 天到 DDL)

```
Week 1 (May 19-25): exp-004 完成 → 分析; 开始 Related Work; exp-007 (2h)
Week 2 (May 26-Jun 1): Paper draft (Intro + Method + Results); figures
Week 3 (Jun 2-8):  Paper draft (Related Work + Discussion + Limitations); internal review
Week 4 (Jun 9-15): Polish + LaTeX + submission
```

---

## 总结

- **当前论文强度**: 2.5 (Borderline Findings)，通过 writing + related work 可达 3.0
- **exp-002 建议**: 不做。Expected value 为负，不解决核心 weakness，GPU 更好用于 exp-007
- **最大 leverage point**: Related Work quality + Decoupling 作为核心 contribution + 统计透明度
- **风险底线**: 即使 Findings 3.0 不到，honest empirical work + 透明统计报告在 ARR 系统中有 2nd cycle 的基础
