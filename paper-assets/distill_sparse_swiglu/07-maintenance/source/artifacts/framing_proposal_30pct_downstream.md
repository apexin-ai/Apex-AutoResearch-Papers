# Framing 调整提案：30% Downstream Negative 结果

> 生成时间: 2026-05-16 | 触发: lm_eval_kl_30pct_s42 negative result + D030

---

## 1. 原 Claim

**Claim 3 (paper_framing.md)**:
> "KL advantage grows with sparsity level (testable prediction): BCE's per-neuron factorized gradient misses joint neuron interactions scaling as O(s²D²). We predict KL-vs-BCE delta follows approximately quadratic curve in sparsity level s."

隐含假设：低 sparsity（如 30%）是安全的操作点，论文 Story Spine 中 "30% 为推荐配置" 的叙事建立在 "PPL 好 → downstream 也好" 的未验证前提之上。

---

## 2. 实验结果（客观数字）

### 2.1 KL 30% Downstream (exp: lm_eval_kl_30pct_s42)

| Task | Dense | KL 30% | Drop | 备注 |
|------|-------|--------|------|------|
| arc_challenge (acc_norm) | 0.5819 | 0.3737 | **-35.8%** | 与 50% 的 -35.2% 几乎相同 |
| winogrande (acc) | 0.7814 | 0.6756 | **-13.5%** | 最轻微的退化 |
| mmlu (acc) | 0.6532 | 0.2874 | **-56.0%** | ≈4-choice 随机水平 (0.25) |
| gsm8k (flexible) | 0.5004 | 0.0781 | **-84.4%** | 近乎完全丧失 |

### 2.2 KL 30% PPL (exp: kl_sparsity30_s42_v3)

| Metric | Value |
|--------|-------|
| true_dense_ppl | 6.12 |
| predictor_hard_mask_ppl | 7.30 (+19.3%) |
| teal_sparse_ppl | 8.98 (+46.7%) |
| model_level_sparsity | 0.300 |
| per-layer sparsity | 早期 0.13-0.23, 中间 0.30-0.34, **后层 0.50-0.70** |

### 2.3 跨条件对比

| Metric | KL 30% | KL 50% | TEAL 50% | Dense |
|--------|--------|--------|----------|-------|
| **PPL (TEAL)** | 8.98 | 12.00±0.07 | 23.31 | 6.12 |
| arc_challenge | 0.3737 | 0.3771 | 0.2910 | 0.5819 |
| winogrande | 0.6756 | 0.6156 | 0.5556 | 0.7814 |
| mmlu | 0.2874 | 0.2591 | 0.2856 | 0.6532 |
| gsm8k | 0.0781 | 0.0121 | 0.0190 | 0.5004 |

数据来源: lm_eval_kl_30pct_s42, lm_eval_kl_s42, lm_eval_teal_50pct, lm_eval_dense, kl_sparsity30_s42_v3

---

## 3. 重新审视

### 3.1 被挑战的 Hypothesis

**H_safe_30**: "30% sparsity 是安全操作点，PPL 退化可控 → downstream 退化也可控。"

这一假设被彻底否定。MMLU 在 30% 就崩到接近随机 (0.2874 vs random 0.25)，GSM8K 丧失 84%。PPL 仅 +47% 不足以预测 downstream 灾难。

**H_ppl_proxy**: "PPL 是 sparse model 质量的可靠代理指标。"

30% 数据点将此否定从 "50% 的特例" 升级为 "系统性规律"：
- 30% PPL: 8.98 (+47%)，但 MMLU ≈ random
- 50% PPL: 12.00 (+96%)，但 MMLU ≈ random
- PPL 几乎翻倍，MMLU 退化程度几乎相同 → PPL 变化量与 downstream 退化量不相关

### 3.2 被忽略的变量：Per-Layer Sparsity 不均匀

**这是根因。** 全局 top-k 将 sparsity 集中在后层：

- 30% global → Layer 26-31 实际 sparsity 41-70%（Layer 31 高达 70.3%）
- 后层直连 LM head，负责精确知识检索和推理链延续
- PPL 是平均指标（前层正常即可拉低），downstream 依赖后层逐 token 精确输出

**这与 50% 的 PPL-downstream disconnect 是完全相同的机制**，只是程度不同：
- 50% global → 后层 sparsity 可能超过 80%（待 P0 任务确认）
- 30% global → 后层 sparsity 50-70%，仍在 "崩溃区"

### 3.3 已做实验的有效性

| 实验 | 新 framing 下是否有效 | 说明 |
|------|----------------------|------|
| KL vs BCE PPL (Claim 1) | ✅ 完全有效 | PPL 层面 KL 优势不受影响 |
| SPON orthogonality (Claim 2) | ✅ 完全有效 | logit 空间分解不依赖 downstream |
| STE vs Gumbel ablation | ✅ 完全有效 | 训练稳定性结论独立于 downstream |
| Mistral cross-arch PPL | ✅ 有效（PPL 层面）| downstream 待补 |
| 50% downstream collapse (D028) | ✅ 升值 | 从 "负面结果" 变为 "系统性发现的一个数据点" |
| 30% downstream collapse (D030) | ✅ 核心新证据 | 证明 PPL-downstream disconnect 是普遍现象 |
| GSM8K 生成质量对比 | ✅ 升值 | 提供 disconnect 的机制解释 |
| 文献调研 (PPL-downstream) | ✅ 关键支撑 | 定位我们的贡献在文献空白中 |

---

## 4. 新 Narrative 骨架（3 种备选）

### Narrative A: "PPL-Downstream Disconnect 是论文核心贡献之一"

**核心论点**: 在 contextual sparsity prediction 框架下，PPL 不是可靠的质量指标。我们系统性地展示这一 disconnect，分析根因（per-layer sparsity imbalance），并提出诊断协议。

**Story Spine 调整**:
- Problem: 不变
- Existing approaches & gaps: 增加 "所有现有工作仅用 PPL 评估 sparse model 质量"
- Our contribution: (1) KL >> BCE/compensation [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) PPL-downstream disconnect 的系统性证据 + 根因分析 + 文献定位** [替换原 Claim 3]
- Headline: "KL distillation produces the best PPL-quality sparse predictor, but PPL alone is insufficient — we demonstrate a systematic PPL-downstream disconnect caused by per-layer sparsity imbalance under global top-k allocation."

**优点**: 诚实、有文献支撑（Khanal & Capone 2024, Xu et al. 2024 EMNLP, Kodathala & Vunnam 2026, Siam et al. 2026）、填补文献空白（无论文在 contextual sparsity + KL distillation 下系统研究此现象）、所有已做实验全部可用。

**风险**: Reviewer 可能认为 "发现问题但没解决" 不够 contribution；需要 uniform allocation 实验作为 "指向解决方案" 的 bridge。

**强度匹配**: 30% 和 50% 两个数据点 + TEAL 50% 对照 + 文献支撑 = 中等强度。可支撑 "systematic evidence" 但不足以支撑 "definitive characterization"。

### Narrative B: "Per-Layer Allocation 修复 Downstream Collapse"（需新实验）

**核心论点**: Global top-k allocation 是 downstream collapse 的根因。Per-layer uniform allocation（每层独立 top-k）能在保持 sparsity 目标的同时恢复 downstream quality。KL + uniform allocation 是正确的推理管线。

**Story Spine 调整**:
- Problem: 增加 "global top-k allocation 导致 per-layer sparsity 不均匀，摧毁后层精确输出"
- Our contribution: (1) KL >> all [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) Uniform allocation 修复 downstream collapse，KL + uniform 是推荐管线** [替换原 Claim 3]
- Headline: "KL distillation + per-layer uniform allocation achieves [X] downstream quality at 30% sparsity, within [Y]% of dense, while global top-k allocation causes catastrophic downstream collapse despite acceptable PPL."

**优点**: 提供解决方案（不只是诊断问题）、30% uniform 如果 downstream 恢复则有强 positive result、自然承接 PPL-disconnect 发现。

**风险**: **完全依赖未完成的实验（ROADMAP P0 任务）。** 如果 uniform allocation 不能修复 downstream（即问题不仅仅是 per-layer imbalance，而是 sparsity 本身摧毁了某些能力），则此 narrative 崩塌。

**实验依赖**: uniform_30pct + uniform_50pct downstream eval（ROADMAP 已列 P0）

### Narrative C: "Task-Sensitive Sparsity Spectrum"

**核心论点**: 不同 downstream task 对 sparsity 的敏感度存在质的差异。我们构建 task × sparsity 退化矩阵，揭示三层敏感度谱系。

**Task 敏感度分层（基于现有数据）**:

| 敏感度 | Task | 30% drop | 50% drop | 特征 |
|--------|------|----------|----------|------|
| Robust | WinoGrande | -13.5% | -21.2% | 渐进退化，30% 保留 87% |
| Cliff | ARC-c | -35.8% | -35.2% | 在 ≤30% 已到 cliff，30→50% 无进一步退化 |
| Ultra-fragile | MMLU | -56.0% | -60.3% | 30% 即 ≈ random，知识检索彻底丧失 |
| Ultra-fragile | GSM8K | -84.4% | -97.6% | 30% 残留微弱，50% 完全丧失 |

**Story Spine 调整**:
- Our contribution: (1) KL >> all [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) Task-sensitive sparsity spectrum: 对 sparsity 的退化不是均匀的，而是 task-dependent 的阶梯式崩溃** [替换原 Claim 3]

**优点**: 每个数字都是 informative 的（包括负面结果）；ARC-c 在 30→50% 无进一步退化是独特发现；GSM8K 的 gradual degradation (0.0781 → 0.0121) 说明存在连续退化（非二元 cliff）。

**风险**: 数据点有限（仅 30% 和 50% 两个 level，4 个 task）。需要更多 sparsity level（如 10%, 20%, 40%）才能画出完整 spectrum。

**推荐**: **Narrative A 为主线，Narrative C 为子节**。Narrative B 作为 "future direction" 或在 uniform 实验完成后升级为主线。

---

## 5. 对论文各章节的影响

### Abstract
- **删除**: "30% 为推荐配置" 相关措辞
- **新增**: "我们发现 PPL 与 downstream quality 存在系统性 disconnect：30% sparsity 下 PPL 仅 +47% 但 MMLU 崩至随机水平"
- **保留**: KL >> BCE/compensation headline 不变

### Introduction
- Story Spine 的 "headline result template" 需重写
- 增加第三段：PPL-downstream disconnect 的 motivation
- 引用 Khanal & Capone (2024), Xu et al. (2024)

### Related Work
- 新增小节："PPL as Evaluation Metric for Sparse Models"
- 引用 4 篇文献调研结果（见 memory.md "PPL-downstream disconnect 文献支撑"）

### Method
- 无重大影响。KL loss、predictor architecture、Gumbel relaxation 不变
- 可增加 per-layer sparsity 分析工具的描述

### Experiments — PPL Results (原有)
- **完全保留**。KL vs BCE、KL vs TEAL、SPON orthogonality、STE ablation 全部有效
- 增加 caveat: "PPL results are necessary but not sufficient for quality assessment"

### Experiments — Downstream Results (新增/重写)
- **核心新增章节**: Task × Sparsity 退化矩阵
- 30% 和 50% 两个 level × 4 tasks × 2 methods (KL, TEAL)
- Figure: 退化热力图（task 行, sparsity 列, color = drop%）
- WinoGrande gradual degradation vs MMLU/GSM8K cliff 对比

### Experiments — PPL-Downstream Disconnect Analysis (新增)
- Per-layer sparsity 分布可视化（30% vs 50%）
- 后层 over-pruning → downstream collapse 的因果链
- GSM8K 生成质量对比（dense vs sparse, 来自 gsm8k_gen_compare）
- 文献对比：我们的发现与 Khanal (2024) / Siam (2026) 的一致性

### Discussion
- PPL 作为 sparse model 评估指标的局限性
- Per-layer allocation 作为潜在修复方向
- Task sensitivity 分层的实践意义

### Conclusion
- 三句话公式：(1) KL >> all on PPL axis; (2) PPL ≠ downstream under global top-k; (3) per-layer sparsity imbalance 是根因，指向 uniform allocation 方向

---

## 6. 建议下一步实验

### 实验 1: [P0] 50% Per-Layer Sparsity 分布提取
- **目的**: 确认 50% global top-k 是否存在同样的后层集中模式
- **方法**: 从 mvp_kl_norm_v2_s42 predictor 提取 per-layer sparsity 分布
- **预期**: 后层 sparsity >> 50%（与 30% 的 0.50-0.70 模式一致但更极端）
- **填补矩阵**: 确认 30% 和 50% 共享同一根因
- **耗时**: < 1 GPU·h

### 实验 2: [P0] Uniform Per-Layer Allocation 30% + 50%
- **目的**: 验证 per-layer sparsity 均匀分配是否修复 downstream collapse
- **方法**: 每层独立 top-k（不需重新训练 predictor，仅修改推理时的 mask 生成策略）
- **评估**: PPL + arc_challenge + winogrande + mmlu + gsm8k
- **关键对比**:
  - uniform_30% vs global_30% downstream
  - uniform_50% vs global_50% downstream
- **预期 A（乐观）**: 30% uniform 恢复 MMLU > 0.50, GSM8K > 0.30 → 激活 Narrative B
- **预期 B（悲观）**: uniform 仍然崩 → PPL-disconnect 不仅仅是 allocation 问题，sparsity 本身摧毁某些能力
- **耗时**: ~2 GPU·h (4 conditions × 0.5h each)
- **决策点**: 若预期 A 成立 → 论文 Claim 3 切换到 Narrative B；若预期 B → 锁定 Narrative A+C

### 实验 3: TEAL 30% Downstream (已在 ROADMAP)
- **目的**: 与 KL 30% 对比，验证 30% collapse 是否为所有 sparsity 方法的固有限制
- **方法**: lm_eval_teal.py --sparsity_target 0.3
- **预期**: TEAL 30% 也崩（与 TEAL 50% 同模式），但可能比 KL 30% 更差（与 50% 的 TEAL < KL 一致）
- **填补矩阵**: 完成 method × sparsity × task 三维矩阵的最后一个 condition
- **耗时**: ~1 GPU·h
- **状态**: registry 中 lm_eval_teal_30pct 已 PREPARING

### 实验 4: [P1] 10% / 20% Sparsity Downstream
- **目的**: 找到 downstream 退化的 onset point（目前只知道 30% 已崩，但不知道 threshold 在哪）
- **方法**: 需先训练 10% 和 20% predictor，再跑 downstream
- **价值**: 如果 20% 尚可但 30% 崩 → 确认 threshold 在 20-30% 区间；如果 10% 就崩 → 问题更严重
- **耗时**: ~4 GPU·h (2 training + 2 eval)
- **优先级**: P1 — 对 Narrative C 重要但对 DDL (05-25) 非必需

### 实验 5: [P1] Per-Layer Sparsity Cap Ablation
- **目的**: 测试约束后层 sparsity 上限（如 max 40%/layer）是否比 uniform 更好
- **方法**: 修改 TEAL global top-k，增加 per-layer cap 约束
- **评估**: PPL + 4 task downstream
- **价值**: 如果 capped > uniform on PPL but capped ≈ uniform on downstream → 可得到 PPL-downstream Pareto 最优点
- **耗时**: ~2 GPU·h
- **优先级**: P1 — 仅在 uniform 实验（实验 2）出正面结果后执行

---

## 7. 决策树摘要

```
uniform_30% downstream 结果
├── MMLU > 0.50, GSM8K > 0.30 (downstream 恢复)
│   → Narrative B 为主线: "KL + uniform allocation = 推荐管线"
│   → Claim 3 重写为 allocation strategy comparison
│   → 30% uniform 成为论文 headline positive result
│
├── MMLU 0.35-0.50, GSM8K 0.10-0.30 (部分恢复)
│   → Narrative A+B 混合: disconnect 是真实的，uniform 缓解但不消除
│   → 论文贡献 = 诊断 + 部分修复
│
└── MMLU < 0.35, GSM8K < 0.10 (无恢复)
    → Narrative A+C 为主线: PPL-disconnect 是根本性限制
    → per-layer imbalance 是 necessary 但 not sufficient 的根因
    → 论文贡献 = 系统性 disconnect 证据 + task sensitivity spectrum
```

---

## 写作红线

1. **禁止 cherry-picking**: 不能只报 WinoGrande（退化最轻）而隐藏 MMLU/GSM8K
2. **所有定量 claim 附 exp_id**: 每个数字必须追溯到 registry
3. **强度匹配**: "systematic evidence" 而非 "definitive proof"（仅 2 个 sparsity level）
4. **禁止 "30% is the recommended operating point"**: 数据明确否定
5. **PPL 结果保留但降级**: PPL 表格前后必须加 caveat，不能单独作为 quality claim 的依据
