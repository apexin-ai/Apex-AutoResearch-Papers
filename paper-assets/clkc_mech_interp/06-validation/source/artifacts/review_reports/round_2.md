---
round: 2
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T16:49:37.022165+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 2

**论文**: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*
**Venue**: EMNLP 2026 Long Paper (ARR May cycle)
**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性/写作质量)
**流程**: Round 1 初审 + 交叉分享，一轮收敛

---

## Summary

论文研究跨语言知识冲突在 LLM 内部表征中的 mechanistic 特征，在 Llama-3.1-8B、Qwen3-8B、Gemma-3-4B-IT 三个模型上通过 residual stream probing 检测冲突信号，发现：(1) 三个模型均能线性检测冲突（peak accuracy 80-89%），且存在 EN→ZH 方向不对称性；(2) 该不对称性与非冲突 XNLI 任务的迁移不对称性在量级和方向上一致（CI 重叠）；(3) 仅 Llama L13 的 steering 实验产生显著因果效应，Qwen/Gemma 均为零效应。

两位 Reviewer 在三个核心 Must-Fix 上完全一致，Should-Fix 层面有局部分歧（新颖性判断、遗漏引用验证）。

---

## Strengths

1. **XNLI baseline 比较的方法论设计**：用非冲突跨语言任务作为控制条件检验不对称性的特异性，是论文最独特的方法论贡献。（R1, R2 一致）
2. **诚实报告负面结果**：Qwen/Gemma steering 全面失败被完整报告，Gemma 高 probe accuracy + 零 steering 效应被正确解读为 informative negative。（R1, R2 一致）
3. **Confound exclusion pipeline 系统化**：翻译质量分层 + token overlap 分析 + 非冲突 baseline 三重检查。（R1, R2 一致）
4. **三模型比较**：一致的 detectability 和分化的 steerability 提供有价值的对比信息。（R1, R2 一致）
5. **统计规范**：Bootstrap CI、Bonferroni 校正、效应量报告。（R1）

---

## Weaknesses

### Must-Fix（影响接收决定，双方完全共识）

**MF-1** [critical] **标题 "Cross-Lingual" 过度泛化**
实验仅覆盖 EN-ZH 一个语言对，但标题使用无限定的 "Cross-Lingual"。论文自身 Limitations 承认 "only one language pair"，且引用 Kargaran et al. (2024) 指出 conflict resolution preferences vary by language pair。标题是论文最重要的 claim 载体，单一语言对使用无限定泛化术语构成 overclaiming。
- **R1**: AGREE | **R2**: 提出 → **共识**
- 建议：标题加 "English-Chinese" 限定，或增加 1-2 个类型学不同的语言对。

**MF-2** [critical] **"Inherit" 因果措辞仅有相关性证据**
标题核心动词 "Inherit" 意味因果关系（冲突不对称性*因继承*通用跨语言结构而产生），但证据仅为 CI 重叠和方向一致的相关性。CI 重叠仅说明无法拒绝两者不同，不等于共享机制。论文未提供任何因果实验（如 ablation 破坏 cross-lingual alignment 后观察冲突不对称性变化）。R1 补充指出 TOST 等价检验未报告功效，进一步削弱等价声称。
- **R1**: 强烈 AGREE（与 TOST 问题联动） | **R2**: 提出 → **共识**
- 建议：替换为 "Mirror"/"Parallel"；补充 power analysis 或 Bayesian equivalence testing。

**MF-3** [critical] **Detection-decision dissociation 仅 Llama 成立，不支持通用结论**
Steering 仅在 Llama L13 产生显著因果效应（Fisher p = 0.002），Qwen（best p = 0.785）和 Gemma（best p = 0.418）在所有层均为零 directional flips。Abstract 使用 "demonstrate" 暗示通用性，且列为三大 contribution 之一。Gemma 88.9% probe accuracy 下的零效应尤其构成反证——排除 probe 质量作为 confound 后，steering 失败更可能反映方法局限性或架构依赖性。
- **R1**: 提出 | **R2**: 提出 → **共识**（交叉中双方 AGREE）
- 建议：Abstract/Intro 加 "in Llama" 限定；Contributions 列表中降级为 observation；增加 mechanistic 讨论。

### Should-Fix（影响评分，存在部分分歧）

**SF-1** [warning] **单种子实验设计**
所有 probing 实验使用单一随机种子，不满足 Sellam et al. 2022 多种子标准。Bootstrap CI 仅量化采样不确定性，不覆盖训练随机性。
- **R1**: Must-Fix 级别 | **R2**: 未单独列为 must-fix（Reproducibility 4/5）
- 建议：至少 3-5 个种子，报告均值±标准差。

**SF-2** [warning] **TOST 等价检验无 power analysis**
Section 4.4 用 TOST 检验等价性但未报告统计功效。样本量有限时 TOST 不显著可能仅因功效不足。
- **R1**: Must-Fix 级别 | **R2**: 同意一般性关切
- 建议：补充 power analysis 或改用 Bayesian equivalence testing (BF < 1/3)。

**SF-3** [warning] **Confound exclusion pipeline 局限性**
(a) COMET tercile 分层每组仅 64-91 样本，功效不足以检测 2-3pp 效应；Gemma 数据未报告。(b) Llama token overlap 有 weak negative correlation (r = −0.15, p = 0.012)，仅靠 "weak" 定性判断不足以排除。(c) 翻译模型 Qwen3-SB 与实验对象 Qwen3-8B 同系列，可能引入 tokenization 偏好 confound。
- **事实性澄清**：R1 交叉回应中指出 R2 将 Llama Δ=+1.7pp 误归为 Qwen，p 值也不对应论文数字。Table 2 实际为 Qwen Δ=−5.6pp, p=0.695；Llama Δ=+1.7pp, p=0.761。

**SF-4** [warning] **Qwen/Gemma steering 失败缺乏 mechanistic 分析**
Gemma 88.9% probe accuracy 但 steering 零效应。论文仅结论 "architecture-dependent"，未讨论可能原因：非线性因果结构、residual stream 结构差异、attention pattern、layer normalization 实现差异等。
- **R1**: AGREE | **R2**: 提出 → **共识**

**SF-5** [warning] **跨模型样本自选择偏差**
各模型用自身知识过滤样本（Llama 1368, Qwen 966, Gemma 1590），导致跨模型比较基于不同样本集。建议报告三模型样本集重叠度并在 Limitations 讨论。
- **R1**: 提出 | **R2**: AGREE

**SF-6** [warning/disputed] **新颖性相对 Zhao et al. 2024 的定位**
- **R2**: 认为增量贡献——Zhao 已建立 probing 框架，本文主要是跨语言扩展 + 大部分失败的 steering
- **R1**: REBUT——confound exclusion pipeline、XNLI baseline 设计、多模型比较有独立方法论价值
- **分歧未解决**，两种判断均有道理。建议作者在 Introduction 中更明确 articulate 独特贡献。

**SF-7** [warning] **遗漏相关工作**
R2 指出遗漏 3 篇直接相关工作：Pokharel et al. 2026 "Cross-Lingual Activation Steering" (arXiv:2601.16390)、"Steering into New Embedding Spaces" (arXiv:2502.15639)、"Steering Knowledge Selection Behaviours" (arXiv:2410.15999)。R1 部分反驳，认为需先验证真实性和具体相关点。

### Minor（不影响接收）

1. Abstract "confronts" 用词不常见，建议改为 "examines"
2. Figure 1 部分模型颜色在小尺寸下辨识度偏低，建议增加 marker shape 差异
3. Table 1 注释（Δ_asym 定义）放在脚注中易被忽略，建议在正文 Section 4.3 显著提及
4. Section 3.2 数据过滤可能引入选择偏差（只保留模型自信的知识），应在 Limitations 提及
5. Appendix B/C 中部分关键数据考虑提升到正文
6. 检查 arXiv preprint 引用是否已被会议接收并更新格式

---

## Questions for Authors

1. CI 重叠能否排除冲突不对称性和 XNLI 不对称性由不同机制碰巧量级相近的可能？是否考虑过 partial correlation 或 mediation analysis？（R2）
2. Qwen/Gemma steering 失败是否可能是 probe direction injection 方法本身在这些架构上的适用性问题？是否尝试过 Activation Addition、DAS 等替代方法？（R2）
3. 模型间样本差异（1368/966/1590）对跨模型比较公平性的影响？（R2）
4. 翻译模型 Qwen3-SB 与实验模型同系列的 tokenization 偏好风险？（R1, R2）
5. 多种子实验下 peak layer 位置和不对称性量级是否稳定？（R1）
6. Abstract 中 "shared multilingual representations" 和 "detectability does not imply causal relevance" 的逻辑衔接如何加强？（R1）

---

## Missing References

| 引用 | 来源 | 共识状态 |
|------|------|----------|
| Pokharel et al. 2026 "Cross-Lingual Activation Steering" (arXiv:2601.16390) | R2 | R1 待验证 |
| "Steering into New Embedding Spaces" (arXiv:2502.15639) | R2 | R1 待验证 |
| "Steering Knowledge Selection Behaviours" (arXiv:2410.15999) | R2 | R1 待验证 |

Round 1 曾指出遗漏的 Meng 2022、Geiger 2024、Turner 2023、Marks 2024 在本轮未被再次提出，可能已补充。

---

## External Review

**状态**：未请求。

---

## Visual Layout Check（非评分项）

**状态**：✅ 已完成（0 critical, 2 warning, 8 info）

| 严重性 | 位置 | 发现 |
|--------|------|------|
| ⚠️ warning | Pages 1-4 | 连续 4 页纯文本无 display item，第一个 figure 到 page 5 才出现。建议将 Figure 1 或 pipeline 概览图前置到 page 2-3 |
| ⚠️ warning | Page 5 | Figure 1 + Table 1 + Figure 2 三个 display item 挤在同一页，与前 4 页空旷形成不均匀节奏。建议分散到相邻页 |
| ℹ️ info | Page 5 | Figure 1 部分模型颜色小尺寸下辨识度偏低 |
| ℹ️ info | Page 5 | Figure 2 bar 标签字号偏小（建议 ≥8pt） |
| ℹ️ info | Pages 5-7 | Tables 1-3 booktabs 风格规范专业 |
| ℹ️ info | General | 无 margin 溢出、无公式渲染错误、页眉页脚符合 ACL 匿名投稿模板 |

---

## Overall Assessment

| Reviewer | 分数 | 定位 |
|----------|------|------|
| R1 | 3.5 | Borderline Conference |
| R2 | 3.0 | Findings |
| **圆桌共识** | **3.0** | **Findings** |

### 评分理由

三个核心 Must-Fix 问题均为 claim-evidence 系统性不匹配，两位 Reviewer 完全一致：
1. 标题 "Cross-Lingual" 泛化 vs. 单一语言对证据
2. "Inherit" 因果措辞 vs. 相关性证据
3. "Demonstrate" 通用结论 vs. 单模型 steering 成功

这些不是表述瑕疵——它们直接影响论文的 contribution 定位和可信度。论文的方法论设计（XNLI baseline、confound exclusion pipeline、三模型比较）有独立价值，但当前 framing 将方法论优势包装为超出证据的结论。

**0.5 分分歧来源**：R1 认为方法论扩展有独立价值，修复 framing + multi-seed 后可达 Conference；R2 认为即使修复，核心贡献仍为增量性（XNLI baseline 是 negative finding，steering 大部分失败）。

### 修改路径

收窄标题和 abstract claims → 补充多种子实验 → 增加 TOST power analysis → 将 detection-decision dissociation 限定为 Llama-specific observation → 修改后适合 Findings 接收。如增加语言对或因果实验则有望冲击 Conference。

---

## Detailed Comments

### Framing 重构

- 标题：加 "English-Chinese" 限定或改为 "in English-Chinese Knowledge Conflicts"
- "Inherit" → "Mirror" 或 "Parallel"
- Abstract "demonstrate" → "suggest" 或 "observe in Llama"
- Contribution 3 从 "Detection-decision layer dissociation" 降级为 "Llama-specific observation suggesting detection-decision dissociation"

### 统计补充

- 多种子（≥3）probing 实验，报告 mean±std
- TOST power analysis 或 Bayesian equivalence testing (BF < 1/3)
- COMET tercile 效应量和功效分析
- Gemma confound 分析数据补充

### 讨论扩展

- Qwen/Gemma steering 失败的 mechanistic 假设（非线性因果结构、attention 架构差异等）
- 翻译模型重叠 confound 讨论
- 跨模型样本集重叠度统计
- 新颖性相对 Zhao et al. 2024 的明确定位

### 与 Round 1 的比较

Round 1 的 3 个 critical issue（Bonferroni 跨层校正、Detection≠Decision N=1、Qwen3 引用错误）中，后两者在本轮持续存在或演化（N=1 问题升级为更广泛的 framing 问题），Bonferroni 和引用错误未被本轮提出（可能已修复，需确认）。本轮新增 "Cross-Lingual" 标题泛化和 "Inherit" 因果措辞两个 critical 问题，聚焦于论文叙事层面的 claim-evidence 匹配。