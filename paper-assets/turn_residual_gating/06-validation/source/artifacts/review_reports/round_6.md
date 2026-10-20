---
round: 6
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T21:33:05.755755+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 6 审稿报告（合并版）

**Target Venue**: EMNLP 2026 (ARR)  
**Paper**: Turn-Residual Gating  
**Reviewers**: R1（方法/实验严谨性）、R2（新颖性/完整性）  
**轮次**: Round 6（fresh re-review，无前轮记忆）  
**交叉分享**: 完成，R1↔R2 逐条回应  

---

## Summary

论文研究 exposure bias 是否导致 multi-turn transformer 中 auxiliary attention loss（GAR）在 autoregressive generation 下崩塌。通过五路对比设计（Base→LoRA-only→Uniform Gate→ThreadGate→PCGrad）逐步排除替代解释，发现 TF-AR GAR gap 达 8–17×，scheduled sampling 在 Qwen 上压缩至 1.3×、Llama 上压缩至 2.9×。研究问题 genuinely novel，实验设计严谨，附录极为详尽（24 页），但因果归因措辞过强、核心指标（GAR）与下游任务关联薄弱、跨模型验证不完整。

---

## Strengths

1. **研究问题 genuinely novel**：exposure bias 是否影响 auxiliary attention objectives——此前未被系统研究。两位 Reviewer 独立确认 novelty claim 成立。
2. **五路对比设计有方法论贡献**：逐一隔离变量的排除设计优于简单 baseline 对比，对该领域后续工作有参考价值。
3. **统计分析规范**（Qwen 主实验）：bootstrap CI、Wilcoxon signed-rank tests、per-category breakdown、N=50 评估。
4. **附录极为详尽**：24 页涵盖 loss formulation 搜索历史、per-seed 结果、梯度冲突分析、per-turn/per-head 分析。Reproducibility 4/5。
5. **Scheduled sampling 应用有实用价值**：首次将 SS 应用于 auxiliary attention objectives，Qwen 上效果显著（7.8×→1.3×）。
6. **写作质量整体良好**：逻辑清晰，claim-evidence 对应关系明确，格式完全合规。
7. **Negative result 的科学价值**：well-characterized negative result 对该领域有 warning value。

---

## Weaknesses（按严重程度排序）

### Must-Fix（3 个，影响接收决定）

**MF1** [Critical | R1+R2 强共识] **因果排除链不完整 + "causal exclusion" 措辞过强**

两位 Reviewer 从不同角度指向同一根本问题：
- **R1 角度（方法论）**：PCGrad 仅排除梯度*方向*冲突，未排除梯度*幅值*失衡。Appendix J/L 显示 NTP 梯度幅值压倒 GAR 7.5–14.7×，但论文未测试 λ_GAR rescaling（放大 GAR 权重至与 NTP magnitude parity）。这意味着 exposure bias 归因无法与"NTP 幅值淹没 GAR 信号"这一替代假说区分。
- **R2 角度（术语精确性）**："Causal exclusion" 在 philosophy of mind 中有严格含义（interventionist causal inference），论文实际做的是消融排除法（ablation-based elimination），不是严格因果推断。Limitations 自己承认未排除 KV cache drift。SS 在 Llama 上残留 2.9× gap 进一步说明可能有其他因素。
- **R1 交叉回应确认**：即便改措辞，实质问题仍在——λ_GAR rescaling 实验缺失。

**要求**：(1) 措辞从 "causal exclusion chain" 改为 "diagnostic exclusion chain" 或 "systematic ablation-based exclusion"（Abstract 第 3 句、§1 Contribution 2、§5.2 标题）；(2) λ_GAR rescaling 实验或在 Discussion 中显式讨论 magnitude imbalance 作为 confound。

**MF2** [Critical | R1+R2 强共识] **GAR 与下游任务性能关联薄弱**

- r=0.200 仅解释 4% 下游方差（r²=0.04），95% CI ≈ [0.05, 0.35] 极宽
- β-steering instruction retention：McNemar p=0.077 不显著，且高度 category-specific——仅 content constraints 显著改善 (+23.8pp)，format (+6.7pp)、count (0)、position (0) 几乎无变化
- PPL 在所有配置下几乎相同（2.78）
- R1 交叉回应："强烈同意，应升级严重性"——GAR collapse 的实际下游危害未得到充分论证

**要求**：(1) 重新定位 GAR 为 attention mechanism collapse 的诊断指标，明确不声称下游因果；(2) 标题从 "Destroys" 降调为 "Collapses"（描述 attention 行为而非下游灾难）；(3) 正文讨论 GAR 作为 proxy metric 的局限性（per-category 分化 + r²=0.04）。

**MF3** [Critical | R1 主导，R2 认同] **跨模型验证不完整**

- Llama 仅 3/5 条件（缺 PCGrad + Uniform Gate），N=20，单种子
- Llama 用 median 报告，Qwen 用 mean——统计标准不可比
- SS Llama 残留 2.9× gap 是 Qwen 1.3× 的 2.2 倍，可能暗示架构差异（GQA/RoPE）带来的其他因素
- Llama median 报告可能放大 baseline gap（27×），使 compression ratio 视觉效果更大

**要求**：(1) Llama 补全 5/5 条件 + mean/median 双报；(2) Abstract 改为具体数字而非 "substantially"；(3) §5.5 标题考虑降级为 "Cross-Model Replication"。

### Should-Fix（7 个，影响评分但不一票否决）

**SF1** [Warning | R2 Must-Fix → R1 rebut → Director 裁定 Should-Fix] **单一数据集限制 generalizability**
- 所有实验仅在 UltraChat 8K 上。R2 认为应 Must-Fix，R1 反驳：诊断性论文的机制发现依赖 training dynamics 而非数据分布，UltraChat 18 种对话类型已提供 domain diversity。Director 裁定：诊断性研究可接受单数据集，但 Limitations 需明确讨论，future work 需承诺跨数据集验证。

**SF2** [Warning | R1+R2 共识] **β-steering 部分循环论证**
- boost attention → attention metric (GAR) recovers 是 by construction 的同义反复。下游效果（p=0.077）未达显著。§5.4 应拆为两段：GAR 恢复标注 "by construction" + 下游效果单独报告。

**SF3** [Warning | R2 提出，R1 交叉同意] **SS Llama 残留 2.9× gap，Abstract "substantially" 模糊**
- Abstract 应报告具体数字："compressing the gap from 7.8× to 1.3× on Qwen and from 27× to 2.9× (median) on Llama"。2.9× 残留需更深入讨论根因（架构差异 vs SS 通用性限制）。

**SF4** [Warning | R2 提出，R1 交叉同意] **仅 LoRA fine-tuning，未验证 full fine-tuning**
- LoRA 限制模型重组 attention patterns 的 capacity，可能 confound 排除链中的 capacity 排除步骤（Base→LoRA-only 测试的是 "LoRA 形式的有限参数" 而非 "更多参数"）。Limitations 需讨论。

**SF5** [Warning | R2 提出，R1 交叉同意] **Dou et al. attention forcing 讨论不够深入**
- 应补充：(1) Dou et al. 是否在 AR 下观察到类似 collapse；(2) 本文发现能否 retrospectively 解释 attention forcing 的效果/局限；(3) 方法论互补性。

**SF6** [Warning | R1 提出] **Loss formulation 搜索（v1-v9）过拟合风险**
- 9 次迭代在同一数据集（UltraChat）上选择 loss formulation，final choice 可能对该数据集过拟合。

**SF7** [Warning | R1 提出] **SS 替代解释未排除**
- SS 改变了训练动态（curriculum effect），不仅仅是修复 exposure bias。需讨论 SS 效果的可能替代机制。

### Minor（5 个，不影响接收）

- **m1**: Figure 1 信息密度过高，print size 下文字可能难读（R1+R2 共识）
- **m2**: §3.4 五路对比可加 flow diagram 提高可读性（R2 提出，R1 同意）
- **m3**: Appendix C instruction retention 18-category McNemar's test 缺 FDR/Bonferroni 校正（R1+R2 共识）
- **m4**: 最后一页（p.34）>75% 空白，可压缩（视觉审查）
- **m5**: 前两页纯文本无 display item，第一个视觉锚点在 p.3（视觉审查）

---

## Questions

1. 如果将 λ_GAR 放大至 NTP/GAR magnitude parity（约 7.5–14.7×），TF-AR gap 是否缩小？这是区分 exposure bias 归因与 magnitude imbalance 假说的关键实验。
2. SS+LoRA-only（无 ThreadGate）是否达到与 SS+ThreadGate 相似的 GAR recovery？如果是，ThreadGate 的独立贡献为零，论文 story 需要调整。
3. Llama 上 SS 残留 2.9× gap 的根因是什么？是 GQA/RoPE 架构差异，还是 SS 的 mixing ratio 需要 architecture-specific tuning？
4. GAR-D（Dongre et al. 原版）在所有条件下接近零，为什么选择 GAR-ours 而非讨论 GAR-D 失败的原因？

---

## Missing References

- **Dou et al. (2024) attention forcing**：论文已引用但讨论不够深入，需补充 AR 退化是否被观察到的讨论（R1+R2 共识）
- **Zhang et al. 2024 "Tell Your Model Where to Attend"**：缺失，应在 Discussion 概念对比中覆盖
- 其他引用：R2 novelty 验证确认无严重遗漏。Dongre et al. (2026)、Qiu et al. (2025)、Li et al. (2024) 均正确引用。

---

## External Review

**状态**：pending（已发送请求，尚未返回）。Stanford Agentic Reviewer 审稿结果未在本轮报告截止前到达。

---

## Visual Layout Check（非评分项）

**状态**: done (0 critical, 2 warning, 19 info)

**Warnings**:
1. 前两页纯文本（Abstract + Introduction + Related Work），无 display item，第一个视觉锚点（Figure 1）在 p.3。审稿人翻过两整页纯文字才看到第一张图，第一印象略弱。
2. 最后一页（p.34）仅顶部 ~20% 有内容，>75% 空白。

**Positive findings**:
- 主文本 8 页含 6 Figure + 1 Table = 7 个 display items，密度 0.88/页，合理
- 配色柔和（蓝/橙/绿/灰），饱和度适中，不同 figure 语义连贯
- Figure/Table 均出现在首次引用附近，无 float 推后
- Caption 自包含，公式渲染正确，无 margin overflow
- 格式完全合规：8 页正文、~191 词 Abstract、Limitations 在正文内、匿名化正确

---

## Overall Assessment

**Overall Score: 3.5 / 5（Borderline Conference）**

| 维度 | R1 | R2 | 合并 |
|------|----|----|------|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 3.5 | 3.0 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.5 | **3.5** |

**评分理由**：

论文提出了一个 genuinely novel 的研究问题（exposure bias 对 auxiliary attention objectives 的影响），且实验设计（五路排除）在方法论上有贡献。附录 24 页展现了扎实的实验工作量，统计分析（Qwen 主实验）规范。

但三个 Must-Fix 问题阻止了更高评分：
1. **因果归因不完备**（复发 6 轮）——"causal exclusion" 措辞过强，λ_GAR rescaling 实验缺失使归因链有实质缺口
2. **核心指标与下游脱节**（复发 6 轮）——r²=0.04 + p=0.077 + per-category 高度分化，GAR collapse 的实际危害未论证
3. **跨模型验证断裂**——Llama 仅 3/5 条件、median/mean 不可比、SS 残留 2.9× gap

**Rebuttal 期望**：如果作者能 (1) 提供 λ_GAR rescaling 实验结果或等效的 magnitude control；(2) 将 GAR 重新定位为诊断指标并降调下游因果声称；(3) 补全 Llama 5/5 条件 + mean/median 双报，评分可考虑提升至 4.0（Conference）。

---

## Detailed Comments

### 交叉分享共识点

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| "Causal exclusion" 措辞 | Must-Fix (方法论) | Must-Fix (术语) | **强共识 Must-Fix** |
| GAR 下游有效性 | Must-Fix (r=0.200) | Should-Fix→升级 | **强共识 Must-Fix** |
| 跨模型验证 | Must-Fix (3/5条件) | Should-Fix (SS gap) | **合并 Must-Fix** |
| SS Llama 2.9× gap | Should-Fix | Should-Fix | **共识 Should-Fix** |
| β-steering 循环论证 | Should-Fix | 未独立提出 | Should-Fix |
| LoRA-only 限制 | 交叉同意 | Should-Fix | Should-Fix |

### 交叉分享分歧点

| 问题 | R1 | R2 | Director 裁定 |
|------|----|----|---------------|
| 单数据集 | Should-Fix（诊断性论文可接受） | Must-Fix（限制 generalizability） | **Should-Fix**——机制性发现依赖 training dynamics 而非数据，但需在 Limitations 明确讨论 |
| 附录篇幅 | 优势（严谨性体现） | Minor（偏大） | **优势**——EMNLP 无附录页数限制 |
| Abstract footnote | 合规（ACL 模板允许） | Minor（不常见） | **无需修改**——合规且有先例 |
| 数字重复 "8-17×" | 正常科学写作 | Minor（重复感） | **无需修改**——关键 effect size 重复符合惯例 |

### Novelty 验证

R2 独立确认以下 novelty claims 成立：
1. "首次实证 exposure bias 崩塌 auxiliary attention objectives"——文献搜索未发现先前工作
2. "Scheduled sampling 首次应用于 auxiliary attention objectives in multi-turn"——Mihaylova & Martins (2019) 仅用于 single-turn NMT primary loss
3. 未发现严重的 related work 遗漏

### Issue Tracker 统计（Round 6）

| 状态 | 数量 |
|------|------|
| open | 12 |
| in_progress | 22 |
| resolved | 9 |
| **total** | **43** |

其中 critical severity in_progress/open: 5 个（R2-N1, R2-N3, R2-C3, R2-W3/R4-N1, R1-W5）