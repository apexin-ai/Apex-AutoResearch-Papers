# Framing-Evidence Alignment Check (2026-05-15)

## 1. 各 Claim 证据覆盖率

### Claim 1: Canary→Diversity Granger-Causal Precedence — **中**

| 证据维度 | 状态 | 详情 |
|----------|------|------|
| α=1.0, 4 seeds | **完成** | 24/24 FDR-sig, cross-corr lag=-1 (std=0.0), permutation Granger 差分后 4/4 SIG |
| α=0.50 | **完成** | 0/4 FDR-sig（严格方法全归零），仅 naive_xcorr 8/8 |
| α=0.25 | **完成** | 类似 α=0.50，严格方法不过 FDR |
| α=0.75 | **在跑** | gen 2/10, ETA ~3.5h。**Pivotal**: 决定 scope 是 "α≥0.75" 还是 "α=1.0 only" |
| plan_006 (T=21) | **在跑** | gen 14/20, ETA ~3h。TY power 改善 + ECE co-primary 判定 |
| 多架构验证 | **未做** | plan_010 (Pythia-1.4B / GPT-2) 仅 PREPARING |

**评估**: α=1.0 证据坚实，但 scope 极窄。当前措辞 "at high contamination levels" 是审慎的，但若 α=0.75 也归零，"high" 实际上只意味着 "full replacement"——实用价值论述将非常困难。paper_framing.md 约束 #21 的措辞已正确预判了这一风险。

**当前最大缺口**: α=0.75 结果（数小时内出）。

---

### Claim 2: Regime-Dependent Predictability — **中偏弱**

| 证据维度 | 状态 | 详情 |
|----------|------|------|
| Drift dose-response (5 α) | **完成** | d1: -13.8%@α=0 → -40.3%@α=0.25 → -37.3%@α=0.50 → ~-93%@α=1.0 |
| 非单调性 (α=0.25 > α=0.50) | **单 seed** | 仅 seed=42，差值 3pp (40.3% vs 37.3%)，无置信区间 |
| Detectability boundary | **完成** | α=1.0 24/24 vs α=0.50 0/4 FDR-sig，清晰二元分界 |
| Perplexity 伪回归确认 | **完成** | D017: 差分后 0/8 SIG (F≈0, p=0.99) |
| ECE regime switch | **单 seed** | α=0.25 gen1 下降 -14%（反向）；α=1.0 gen1 +2926% |
| Multi-seed (α=0.25/0.50) | **QUEUED** | 4 runs 排队中，未开始 |

**评估**: Detectability boundary 和 perplexity 伪回归是稳固的子发现。但非单调 dose-response（Claim 2 最吸引眼球的部分）仅有 3pp 差值、单 seed，统计上不可区分于噪声。paper_framing.md 约束 #23 已正确要求标注 "observed at seed=42; multi-seed confirmation required"，但主文若要将此作为 regime map 的 "核心特征"（约束 #22），multi-seed 是刚需。

**当前最大缺口**: multi-seed 尚未开跑。这是 Weak Accept → Accept 的首要条件（约束 #23 原话）。

---

### Claim 3: Method × Regime Interaction — **强**

| 证据维度 | 状态 | 详情 |
|----------|------|------|
| Method ablation (5 methods) | **完成** | naive 16/16 → TY 4/16; spurious_rate 75%/62.5% |
| 2×2 差分对比表 | **完成** | diversity 通道不变 (12/12→12/12)，perplexity 通道归零 (6-8/8→0/8) |
| d_max sensitivity | **完成** | 0%↔94% spurious rate 震荡 |
| TY power analysis | **完成** | T=10 power 0.05-0.20 (plan_009, N=1000 Monte Carlo) |
| Method×regime 极端例证 | **完成** | α=0.50: naive_xcorr 100% sig vs strict 0% sig |
| BH FDR 校正 | **完成** | 全 battery 已加 FDR，无结论翻转 |

**评估**: 多层证据结构完整（Layer 1-3），无需额外实验即可成立。最强且最 novel 的 claim。paper_framing.md 约束 #25 正确识别了证据强度排序 (Claim 3 > 2 > 1)。

**无重大缺口。**

---

## 2. 当前最大风险点（按严重性排序）

1. **Multi-seed 全部 QUEUED（未跑）** — 非单调 dose-response 和 ECE regime switch 均为 point estimate。若 multi-seed 推翻非单调性，Claim 2 的 regime map 叙事需要大幅修改。这是唯一可能迫使论文结构性改写的风险。

2. **α=0.75 结果（数小时内）** — 若也 null，Claim 1 scope 收缩至 "α=1.0 only"。论文标题/摘要中 "canary prediction" 的实用价值论述将依赖 pure boundary mapping 定位，reviewer 可能质疑 "so what"。

3. **单模型 + 单数据集** — Pythia-410M × WikiText-103。plan_010（Pythia-1.4B/GPT-2）和 domain-transfer（C4）均未启动。Reviewer concern 表中已列出但无应对实验。这是 venue-specific 风险——AAAI 对 empirical breadth 容忍度稍高，但仍需至少 scale spot-check。

4. **Scheffer et al. 未进 literature_map.yaml** — paper_framing.md 约束 #13 标注为 "必引"，Story Spine 中已提及，但 literature_map.yaml 中缺失。需补录。

---

## 3. 在跑/待跑实验对各 Claim 的贡献

| 实验 | 状态 | Claim 1 | Claim 2 | Claim 3 | 说明 |
|------|------|---------|---------|---------|------|
| **α=0.75** | RUNNING (2/10) | **核心** | 高 | 中 | Claim 1 scope 扩展的唯一机会；Claim 2 regime boundary 精度提升 |
| **plan_006** (20gen) | RUNNING (14/20) | 高 | 中 | 中 | T=21 提升 TY power（Claim 1 补充）；ECE co-primary 判定；长序列 diversity lead 稳定性 |
| **multi-seed** (4 runs) | QUEUED | 低 | **核心** | 低 | 非单调性置信区间 = Claim 2 的生死线；ECE regime switch 可重复性 |

优先级建议：multi-seed（a025_s43 优先）应在 α=0.75 完成后立即上 GPU。

---

## 4. Framing 措辞与证据强度匹配检查

### 措辞已恰当的部分
- Claim 1 主句限定 "at high contamination levels" — 与当前仅 α=1.0 稳固的证据匹配 ✓
- Perplexity 通道用 "spurious association confirmed by first-differencing" — 措辞精确 ✓
- "Regime map" 而非 "phase diagram" — 4-5 个 α 值不足以用物理学术语 ✓
- CRS 降级为 illustration — 与 Dream 三档共识一致 ✓
- TY 降级为辅助指标 — 有 plan_009 power analysis 支撑 ✓
- f² 效应量禁用 Cohen 基准 — 正确处理小 df_resid 问题 ✓

### 需要微调的措辞

1. **Headline result template 中 "1-2 generations ahead"** — 当前仅 α=1.0 有此 lead，α=0.25/0.50 无显著 lead。建议加限定："at full synthetic replacement (α=1.0), token entropy exhibits ... 1-2 generations ahead"。

2. **Story Spine 中 "predictability regime map delineates which collapse dimensions are forecastable"** — 当前 regime map 只有 2 个非平凡点确认有/无 Granger sig（α=1.0 有, α=0.50 无），α=0.75 pending。若 α=0.75 null，map 退化为单点。建议加 "preliminary" 或明确说 "identifies a detectability boundary between α=0.50 and α=1.0"，而非暗示连续 mapping。

3. **非单调 dose-response 在 Evidence strategy 中列为 "Primary = raw drift magnitude dose-response"** — 这是正确策略（方法无关），但主文中非单调性结论需显著标注单 seed 限制。当前约束 #23 已要求标注，但 Headline result template 中未提及非单调性，建议保持如此——在 multi-seed 确认前不放入 headline。

4. **ECE "conditional secondary canary" 措辞** — paper_framing.md 说 "secondary only in TY consistency; equivalent across all other methods"。但约束 #20 揭示 ECE 在低 α 有反向信号。建议措辞更新为 "conditional secondary: equivalent to token_entropy at α≥0.50 across non-TY methods, but unreliable at α=0.25 due to first-generation sign reversal"。

### 文献 contextualization 缺口

| 文献 | Claim | 状态 |
|------|-------|------|
| Scheffer et al. 2009/2012 | Story Spine | paper_framing.md 已标注必引，**但 literature_map.yaml 中缺失** — 需补录 |
| He et al. 2025 (golden ratio) | Claim 2 非单调性 | literature_map.yaml 已锚定 ✓ |
| Xu & Cheng 2025 (mixing ratios) | Claim 2 regime boundary | literature_map.yaml 已锚定 ✓ |
| Truong & Truong 2025 | Claim 2 (canary 失效边界) | literature_map.yaml 已收录 ✓ |
| Chen et al. 2025 (scales) | Claim 1 (ECE 先驱) | literature_map.yaml 已收录，4 点差异化已写入 Story Spine ✓ |

---

## 5. Reviewer 攻击面预判

按杀伤力排序：

1. **"Only works at α=1.0, who trains on 100% synthetic data?"** — 若 α=0.75 null，这是致命攻击。应对：boundary mapping 贡献定位 + 引用 Dohmatob 2025 "即使极小比例也触发 collapse" 论证研究必要性。但 reviewer 可能不买账。

2. **"Single model, single dataset"** — 无应对实验。plan_010 和 domain-transfer 均未启动。至少需要 Pythia-1.4B spot-check 一个核心条件。

3. **"Non-monotonic dose-response is noise"** — 3pp 差值单 seed，reviewer 一句 "within noise margin" 即可驳回。multi-seed 是唯一解。

4. **"Granger ≠ causality, why not do intervention?"** — paper_framing.md 已准备 Discussion 声明 + future work。CRS illustration 部分缓解但不消除。风险可控。

5. **"T=10 too short for any time-series inference"** — plan_006 (T=21) 在跑，plan_009 已提供 power analysis。若 plan_006 完成且结论一致，此攻击面大幅缩小。
