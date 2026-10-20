# 最坏情况预演：4 个 Open Issue 的审稿人追击风险

> 起草者：Reviewer Agent | 日期：2026-05-29
> 目的：为每个 open issue 预判实验最坏结果下审稿人的攻击路径、我们的应对底线、以及是否需要兜底实验

---

## 风险排序总览

| 排名 | Issue | 最坏情况概率 | 追击力度 | 论文存亡影响 |
|------|-------|-------------|---------|-------------|
| **1** | RD2-N1 (n≥5 种子扩充) | 低 (~10%) | 致命级 | 核心 claim 崩塌 |
| **2** | RD2-N2 (v2 Random OCC) | 中低 (~20%) | 高 | 一个 contribution 需重写 |
| **3** | RD3-W3 (λ sweep) | 中 (~30%) | 中 | guidelines 需限定 |
| **4** | RD2-W4 (BN eval mode) | 中高 (~40%) | 低 | 仅影响 discussion 假说 |

---

## Issue 1: RD2-N1 — 种子扩充后效应量缩水

### 最坏情况定义

n≥5 后 Detach+LN vs Vanilla 的 Hedges' g 降至 <0.5，bootstrap 95% CI 含零。同时 gradient flow 主效应 η² 降至 <0.06。

### 概率评估：**低 (~10%)**

当前证据为什么抵抗这个最坏情况：
- 已有 4th seed (Detach+LN = 0.784)，纳入后 g 从 1.89 变为 ~2.31（因 SD 下降），效应反而增强
- 4 个 factorial cell 的方向一致性跨 14 个独立 seed 全部成立（ON < OFF 在 BN 和 LN 行都成立）
- 要让 g 从 ~1.89 降到 <0.5，需要新增 seed 中出现 Detach+LN CAR ≈ 0.72 或 Vanilla CAR ≈ 0.80 的极端值，概率基于当前分布极低

**但真正的脆弱点不是 Cell 4 vs Vanilla，而是 gradient flow 主效应**。当前 η²=0.180 处于 large 边界，如果新 seed 缩小 Cell 1 和 Cell 3 的差距（BN 行 ON-OFF gap 从 4.2pp 缩到 ~1pp），gradient flow 效应可能消失。Cell 1 (Full OCC BN) 当前 std=0.064（3× 其他），高方差意味着新 seed 可能大幅偏移均值。

### 审稿人最可能的追击措辞

> "After expanding to n=5, the gradient flow main effect remains non-significant (p=[值]>0.05) with a reduced effect size (η²=[值]). The authors' central claim of 'two additive main effects' is now effectively a single-effect story—only normalization type matters. The paper's contribution is correspondingly reduced: it demonstrates that LayerNorm is preferable to BatchNorm in auxiliary heads, which, while useful, is a narrower finding than the originally claimed factorial decomposition. The gradient flow recommendation ('detach gradients') lacks sufficient statistical support."

### 我们的底线应对

**底线立场：保住 Detach+LN 最优 + normalization 显著 + 交互项零。**

即使 gradient flow 效应缩水，论文的核心价值仍成立：

1. **Detach+LN vs Vanilla 的 pairwise 效应几乎不可能翻转**：4th seed 已确认方向，g=2.31 (n=4)。除非第 5 个 seed 出现 CAR<0.70 的灾难性异常值，pairwise 比较仍然显著。这是 planned comparison，不受 ANOVA 主效应影响。

2. **"One strong effect + one directional effect" 仍是有价值的 factorial finding**：
   - 交互项 η²≈0.005 是论文最稳固的统计结果——证明两个因素独立
   - Normalization 显著 (p=0.041) 是独立成立的发现
   - Gradient flow 即使 underpowered，方向一致仍有信息量

3. **退守表述**：

> "The factorial design reveals one significant main effect (normalization: LN > BN, p_perm=[值], η²=[值]) and one directionally consistent but sub-threshold effect (gradient flow: OFF > ON, η²=[值]). The two factors combine additively (interaction η²<0.01). The practical recommendation—Detach+LN—derives from the converging direction of both factors and is supported by the planned pairwise comparison (g=[值], p=[值], CI excludes zero)."

这个表述：
- 不 overclaim gradient flow 显著
- 保留 factorial 方法论贡献（交互项零的发现）
- 保留 practical guideline（基于 pairwise 而非 ANOVA 主效应）

### 是否需要兜底实验

**不需要额外实验，但需要预写两版数字段。** n≥5 的结果只有量的变化，不会改变需要做的实验类型。如果 gradient flow 效应确实缩水，问题出在统计力，而不是实验设计——继续加 seed 到 n=8 可以解决，但 GPU 预算可能不允许。

**预防措施**：如果 n=5 后 gradient flow η²<0.10，建议 Director 立即评估是否将 Cell 1 和 Cell 3 各加到 n=8（每 cell +3 runs × 13h = ~78 GPU·h）。这是唯一可能需要的"兜底实验"。

---

## Issue 2: RD2-N2 — v2 Random OCC 显著异于 Full OCC

### 最坏情况定义

v2 Random OCC 与 Full OCC BN (v2) 的差异 |Δ| > 5pp 且 Hedges' g > 0.8，方向为 Random OCC 显著高于 Full OCC。

### 概率评估：**中低 (~20%)**

v1 下 Random OCC (0.789) 与 Full OCC (0.797) 仅差 0.8pp。v2 中 Full OCC BN 降到 0.725，但这是 BN+GF 组合的效应，Random OCC 同样使用 BN+GF，应受到相同的 BN running stats 影响。理论上两者应同步下降。

**但**：Full OCC BN v2 的 std=0.064 异常高，3 个 seed 中最差的 (0.654) 极度偏离。如果 Random OCC v2 的 seed 碰巧没有这种极端异常值，均值可能高出 Full OCC 5-8pp。这不是 content effect，而是 BN+GF 的 stochastic instability 在不同 label 分布下的表现差异。

### 审稿人最可能的追击措辞

> "Random OCC (v2) achieves CAR [值], substantially higher than Full OCC BN (0.725, Δ=[值]pp, g=[值]). This directly contradicts the paper's central claim that 'spatial content does not detectably affect outcomes.' The v1 content irrelevance result does not generalize to v2, consistent with the paper's own codebase sensitivity finding. The claim should be retracted."

### 我们的底线应对

**底线立场：从 "content irrelevance" 退守到 "content effect confounded with BN instability"。**

关键防御逻辑：Cell 1 (Full OCC BN) 的 std=0.064 是所有 cell 中最高的。n=3 下 Random OCC 与 Full OCC 的差异可能完全落在 Cell 1 的 confidence interval 内。

**三层退守：**

**Level 1（差异在 CI 内）**——不需退守：
> "The difference between Random OCC and Full OCC under v2 ([值]pp) falls within the cross-seed confidence interval of the Full OCC BN cell (SD=0.064). Content irrelevance is maintained: both conditions produce comparable outcomes under the volatile BN + gradient flow combination."

**Level 2（差异显著但可解释）**——退守到 "instability-mediated"：
> "Under v2, Random OCC achieves a higher mean CAR than Full OCC BN ([值] vs 0.725), but this difference is likely mediated by the BN + gradient flow instability documented in §4.1 (Full OCC BN SD=0.064, 2× all other cells) rather than by label content per se. The structured occupancy labels may interact with BN running statistics differently from random binary labels, creating condition-specific stochastic sensitivity. Both conditions remain below Detach+LN, and the practical guideline (detach gradients, use LN) is unaffected."

**Level 3（差异显著且无法解释）**——退守到 partial claim：
> "Content irrelevance holds under v1 but not under v2. Under v2, structured occupancy labels are associated with [higher/lower] safety than random labels ([值] vs [值], g=[值]). This finding is confounded with the BN + gradient flow instability specific to v2, and we cannot determine whether the content effect is genuine or an artifact of the volatile optimization landscape. We downgrade content irrelevance to a preliminary observation limited to the v1 codebase."

此时论文需要修改：
- Contribution #1 删除 content irrelevance 子句
- Discussion "Content irrelevance" 段重写为 "Content sensitivity under BN + gradient flow"
- Limitations 增加 content effect 的 codebase-dependent 性质

### 是否需要兜底实验

**如果 Level 2 或 Level 3 触发：考虑 v2 Random OCC + LN 实验。**

如果 Random OCC 与 Full OCC 的差异只在 BN 行存在，在 LN 行消失，则说明差异确实是 BN instability 产物而非 content effect。这需要额外 1 个条件 × 3+ seeds ≈ 39 GPU·h。

**但这是 nice-to-have 而非必须**——Level 2 的退守表述已经足够应对 workshop 审稿。

---

## Issue 3: RD3-W3 — λ=0.1 导致严重恶化

### 最坏情况定义

λ₀=0.1 条件下 CAR 大幅恶化（比 default λ₀=0.01 低 >10pp），而 λ₀=0.001 接近 Vanilla，呈现强 dose-response。

### 概率评估：**中 (~30%)**

λ₀=0.1 使有效 auxiliary loss weight 增加 10×。在 Full OCC BN (GF ON) 条件下，这会大幅放大 auxiliary gradient 对 LoRA 的影响。考虑到 default λ₀=0.01 已产生负面效应，10× 放大后效应加剧是合理的。

### 审稿人最可能的追击措辞

> "The gradient flow safety deficit varies by [值]pp across a single order of magnitude in λ₀ (Table [ref]). The paper's practical guideline to 'detach auxiliary gradients' implicitly assumes the finding generalizes across loss weight settings, but the dose-response pattern suggests the deficit at λ₀=0.01 may simply be a specific operating point on a continuous curve. At λ₀=0.001, the deficit [vanishes/is negligible], which would mean practitioners using smaller auxiliary weights need not detach. The guideline is over-broad."

### 我们的底线应对

**底线立场：dose-response 强化而非削弱论文——它提供了额外的 mechanistic evidence。**

关键反转：λ 敏感性实际上**支持**论文的 story——如果 auxiliary gradient magnitude 越大，safety 越差，这恰恰说明 gradient flow 是问题的核心机制。

**回应框架**：

> "The dose-response relationship between λ₀ and CAR (Table [ref]) provides additional evidence that auxiliary gradient magnitude mediates the safety deficit. At λ₀=0.001, the deficit is negligible, consistent with the mechanism: when auxiliary gradients are <0.2% of action gradient magnitude, they have minimal impact on the LoRA optimization trajectory. At λ₀=0.1, the deficit is amplified, confirming the causal direction.
>
> This refines, rather than undermines, the practical guideline: (1) **Detaching gradients remains the safest choice** regardless of λ₀ (it eliminates the mechanism entirely, at zero cost). (2) If gradient flow is desired, λ₀ should be kept small (≤0.001) to minimize interference, though even this does not provide the LN-mediated safety advantage of the Detach+LN configuration. (3) The exponential decay schedule λ(t) = λ₀·exp(−t/50000) provides partial mitigation by reducing effective λ over training."

**论文修改**：
- Appendix 新增 λ sensitivity table + dose-response 解释
- Discussion practical guideline 增加 λ 条件："For practitioners who retain gradient flow, use LN and keep λ₀ ≤ 0.01"
- 不需要改 Contribution

### 是否需要兜底实验

**不需要。** dose-response 结果无论方向如何都可以整合到论文中。如果三个 λ 值产生相同 CAR（insensitive），说明 robustness；如果产生 monotonic dose-response，说明机制可解释；唯一真正难处理的是非单调结果（λ=0.001 最差或 λ=0.1 最好），但这在物理上没有合理解释，概率极低 (<5%)。

---

## Issue 4: RD2-W4 — BN Eval Mode 无效果

### 最坏情况定义

训练时将 occ_head 设为 eval mode（冻结 BN running stats），但 CAR 与标准训练无显著差异（|Δ|<2pp, g<0.3）。

### 概率评估：**中高 (~40%)**

BN running stats corruption 只是多个可能机制之一。BN 的 forward pass 还涉及 per-batch mean/var 计算（train mode 下使用 batch stats 而非 running stats 做 normalization），这对梯度信号有独立影响。即使 running stats 冻结，batch-level normalization 仍可能改变梯度质量。

### 审稿人最可能的追击措辞

> "The BN eval-mode ablation shows no significant effect (CAR [值] ≈ [值], g=[值]). The running-statistics hypothesis (Discussion §5) is falsified. The paper offers no alternative mechanism. The 'mechanism remains open' conclusion, combined with the non-significant gradient flow main effect and the falsified BN hypothesis, means the paper provides no mechanistic understanding beyond the bare factorial observation."

### 我们的底线应对

**底线立场：这是影响最小的最坏情况。论文的价值从来不依赖机制解释。**

论文的 4 个 contribution 中，只有 Discussion 中的假说段与 BN 机制相关，且该段已经标注为 "hypothesize but do not directly test"。即使假说被否定：

1. ✅ Contribution #1 (Detach+LN 最优 + factorial 结果) 不受影响
2. ✅ Contribution #2 (factorial 方法论) 不受影响
3. ✅ Contribution #3 (practical guidelines) 不受影响——guidelines 基于行为数据而非机制
4. ✅ Contribution #4 (codebase sensitivity) 不受影响

**回应框架**：

> "We agree that the eval-mode ablation falsifies the running-statistics drift hypothesis as the sole mechanism. We have updated the Discussion to reflect this:
>
> 'Freezing BN running statistics does not eliminate the gradient flow deficit (Table [ref]), indicating that the mechanism operates through the forward-pass batch normalization computation itself rather than through inference-time statistics drift. When auxiliary inputs shift the per-batch mean and variance during training, the normalized representations differ between BN and LN even for identical inputs, potentially altering the LoRA optimization trajectory. Direct verification of this refined hypothesis (e.g., comparing per-batch vs. running statistics divergence across training) is left to future work.'
>
> We emphasize that the paper's contributions—the factorial finding, the LN advantage, and the practical guidelines—are established by behavioral data (Tables 1–2) and do not require a confirmed mechanism."

**论文修改**：
- Discussion 假说段从 "running-statistics drift" 改为 "forward-pass batch-level normalization"
- 新增一句 eval-mode 结果作为 negative evidence
- "Mechanism remains open" 保持不变，但假说更精确
- Limitations 中已有 "mechanistically plausible but not directly verified"，不需改

### 是否需要兜底实验

**不需要。** 这是 4 个 issue 中唯一一个即使最坏情况发生也不需要任何额外实验的。机制解释是锦上添花，不是论文的承重结构。

---

## 交叉风险分析：多个最坏情况同时发生

| 组合 | 联合概率 | 影响 |
|------|---------|------|
| RD2-N1 + RD2-N2 同时最坏 | ~2% | **致命**：效应缩水 + content claim 翻转 = 论文需根本重构 |
| RD2-N1 + RD3-W3 同时最坏 | ~3% | **严重**：效应弱 + λ 依赖 = "finding is fragile" |
| RD2-N2 + RD2-W4 同时最坏 | ~8% | **可控**：content 重写 + 机制重写，但核心 claim 不变 |
| RD3-W3 + RD2-W4 同时最坏 | ~12% | **轻微**：均可在 appendix/discussion 层面消化 |

**唯一需要预案的致命组合**：RD2-N1 + RD2-N2 同时最坏。此时论文的退守路线是：

> "一项 negative finding + methodology contribution 论文"：We tested 12 configurations of auxiliary spatial heads and found no configuration that robustly improves VLA collision avoidance. The factorial methodology reveals that normalization type is the only detectable factor, with LayerNorm providing a modest advantage. The study highlights the fragility of auxiliary head training dynamics and the dominance of implementation details (codebase sensitivity) over design choices.

这仍是一篇可发表的 workshop paper（负面结果 + 方法论），但贡献降级。

---

## 行动建议

1. **RD2-N1 优先级最高**——它影响所有其他 issue 的解读（数字是论文的基础）
2. **RD2-N2 第二优先**——content claim 是审稿人攻击面最大的点
3. **RD3-W3 和 RD2-W4 可并行，优先级相当**——结果无论如何都可整合
4. **预写两版 Results 数字段**（效应保持 vs 效应缩水），等数据填入即可提交
5. **如果 RD2-N1 后 gradient flow η²<0.10，立即评估是否追加 seed 到 n=8**
