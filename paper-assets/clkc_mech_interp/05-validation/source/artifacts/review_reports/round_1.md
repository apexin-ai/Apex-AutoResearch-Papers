---
round: 1
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-24T15:10:04.783347+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations

**目标 Venue**: EMNLP 2026 via ACL Rolling Review
**审稿模式**: Fresh (Round 1)
**Reviewer 编排**: 2 人（R1: 方法严谨性/实验/统计; R2: 新颖性/完整性/写作）

---

## Summary

本文研究多语言 LLM 中跨语言知识冲突信号的可检测性和因果相关性。通过 Llama-3.1-8B-Instruct、Qwen3-8B 和 Gemma-2-9B-IT 三个模型的残差流 probing，发现冲突信号可跨语言线性检测，ZH→EN 迁移优于 EN→ZH 约 7pp，且该不对称性与 XNLI 非冲突基线匹配（非冲突特异性）。Representation steering 在 Llama L13（41% depth）成功（Fisher p=0.002），但在 L28（probe peak, 88%）及 Qwen/Gemma 中均失败，揭示 Detection ≠ Decision 层分离。

---

## Strengths

- **S1**: 首次多架构/多语言知识冲突信号的系统性 probing 研究，填补了 Zhao et al. (2024) 单语工作到跨语言的空白
- **S2**: Confound exclusion pipeline 设计周全（COMET tercile + token overlap + XNLI baseline + EN-DE 对照），为跨语言 probing 树立方法论范式
- **S3**: XNLI baseline 对比实验设计巧妙——用同一 pipeline 证明不对称性非冲突特异性
- **S4**: 对 negative results 的诚实处理（Qwen/Gemma steering 零翻转），避免 publication bias
- **S5**: 独立复现（N=201, Appendix B）展示 L13 周围因果梯度的空间精度，增强结果可信度
- **S6**: 写作清晰，Discussion 中对结果的解读审慎（"architecture-specific" 限定）

---

## Weaknesses

### Critical（影响接收决定）

- **W-C1** [共识] **Detection ≠ Decision 因果声明泛化性严重不足（N=1 模型）**
  - Steering 仅 Llama L13 成功，Qwen (p=0.785, 0 flips) 和 Gemma (p=0.448, 88.9% probe acc, 0 flips) 全部失败
  - Gemma 高 probe accuracy 下零效应构成对 "probe direction = causal direction" 的强力反证
  - Abstract/Introduction 的 framing 暗示 general principle（"A dissociation emerges between detection and decision" 未加模型限定）
  - 无法区分：Llama 特有特征 vs 线性 steering 局限 vs 统计偶然

- **W-C2** [共识] **Steering 实验多重比较校正不完整**
  - 主实验在 3 层 × 10 α = 30 次检验，Bonferroni 仅层内应用（0.05/10=0.005）
  - 若全 family 校正（0.05/30≈0.00167），L13 正方向 p=0.002 不再显著
  - 独立复现 p<0.001 和负方向 p<0.001 部分缓解，但缺乏明确的 family definition 说明

- **W-C3** [共识] **Qwen3-8B 引用错误**
  - 论文使用 Qwen3-8B（36 layers）但引用 Qwen2.5 Technical Report (arXiv:2412.15115)
  - 正确引用应为 Qwen3 Technical Report (Yang et al., 2025; arXiv:2505.09388)

### Major（影响评分）

- **W-M1** [共识] 单种子实验：所有 probing 结果基于单次 split，未报告多种子 mean±std
- **W-M2** [共识] "非冲突特异"声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验
- **W-M3** [共识] COMET tercile 分析统计功效不足（每 tercile 64-91 样本），Gemma 未报告
- **W-M4** [共识] 标题和 Abstract 使用 "Cross-Lingual" 暗示一般性，实验仅覆盖 EN-ZH
- **W-M5** [共识] Related Work 遗漏关键引用：Meng et al. (2022), Geiger et al. (2024), Turner et al. (2023), Marks et al. (2024)
- **W-M6** [共识] Bib 条目多处使用非标准 "and others" 格式
- **W-M7** [共识] 跨模型比较在不同样本子集上进行，未报告重叠度

### Minor

- **W-m1** [共识] 翻译模型 (Qwen3-8B) 与实验对象重叠，未讨论 confound
- **W-m2** [共识] Table 3 caption "p<0.05" 与正文 Bonferroni 阈值 0.005 不一致
- **W-m3** [R2] Qwen Δ_asym CI 包含零 [-0.6, 13.7]，"consistent across all three architectures" 表述过强
- **W-m4** [R2] Cross-task probe transfer 重要实验结果放在 Discussion 而非 Experiments，结构不佳
- **W-m5** [R2] "A suggestive MLP trend" 段 CI 含零，"suggestive" 表述有 cherry-picking 风险

---

## Reviewer Consensus

以下问题双方一致（标注 [AGREE]）：
1. Detection ≠ Decision 的 N=1 模型局限是论文最核心缺陷
2. Bonferroni 校正 family definition 需明确，虽独立复现部分缓解
3. Qwen3 引用必须更正
4. 单种子实验不足，至少需讨论其影响
5. CI 重叠 ≠ 等价性检验
6. Confound exclusion pipeline 是论文最大方法论贡献
7. 论文对 negative results 的诚实处理值得赞赏

---

## Reviewer Divergence

| 议题 | R1 立场 | R2 立场 | 影响 |
|------|---------|---------|------|
| 新颖性评估 | C1+C3 组合有独立方法论贡献，sufficient for borderline conference (3.5) | 整体增量（Zhao 2024 延伸 + N=1 case study + toolkit），仅 Findings (3.0) | 评分差 0.5 |
| Pires 2019 / Chi 2020 | 非必要引用，论文已引更直接后续工作 | 作为跨语言 probing 奠基工作应引用 | Minor |
| Abstract 200 words | 完全合规（≤200 是硬限制） | 建议精简至 190 以下留安全余量 | Negligible |

---

## Questions（需作者澄清）

1. Bonferroni 为什么按层而非按整个 steering 实验校正？是否有先验假设？
2. 独立复现（N=201）是否在观察到 L13 主实验结果之后进行？若是 post-hoc 应明确声明
3. Gemma L21 cross-task transfer dip (0.730) 与 alternating attention 架构的关系？
4. L13 和 L28 的 w_probe cosine similarity 是多少？
5. Qwen Δ_asym CI 包含零，如何支撑 "consistent across all three architectures"？
6. 翻译模型与实验对象重叠对 Qwen 结果的潜在影响？

---

## Missing References

**双方共识必须补充：**
- Meng et al. (2022) "Locating and Editing Factual Associations in GPT" — activation patching 奠基
- Geiger et al. (2024) "Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations" — DAS 替代因果方法
- Turner, Thacker, and Fry (2023) "Activation Addition" — steering 核心方法论
- Marks & Tegmark (2024) "The Geometry of Truth" — 线性 probe 因果效应正面案例
- Qwen Team (2025) Qwen3 Technical Report (arXiv:2505.09388) — 正确模型引用

**R2 建议（R1 部分反对）：**
- Pires et al. (2019) "How Multilingual is Multilingual BERT?" — 跨语言 probing 奠基
- Chi et al. (2020) "Finding Universal Grammatical Relations in Multilingual BERT" — 跨语言共享子空间

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未启用外部审稿配置）

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 3 warning, 10 info）。主要发现：

**Warnings:**
1. 前 3 页纯文本无 display item，审稿人到第 4 页才看到第一个视觉锚点（Figure 1）。建议第 1-2 页添加 pipeline overview 图
2. 第 7-8 页（Discussion+Conclusion+Limitations）连续纯文本无 display item 穿插
3. Figure 1 为单栏内含 3 列子图，轴标签字号小于正文 70%，打印可读性差。建议改为 figure*（双栏全宽）

**Info:**
- 主文 8 页仅 5 个 display items（0.625/页），对实证论文偏少
- Figure 1 caption 未说明 y 轴基线水平（chance=50%）
- Figure 2 仅 6 个数据点，信息密度较低
- 无 margin 溢出、LaTeX 渲染错误或排版缺陷

---

## Overall Assessment

**评分: 3.0 (Findings)**

**置信度: 4/5**

**理由:**

本文方法论设计扎实，confound exclusion pipeline 有示范价值，统计实践整体规范，对 negative results 的诚实处理值得赞赏。然而：

1. 最具新颖性的贡献（Detection ≠ Decision 层分离）仅在 Llama 一个模型上有因果证据，泛化性不足以支撑一般性结论
2. 其余贡献（跨语言可检测性、不对称性刻画）相对于已有工作属增量扩展，不对称性本身可从 English-centric bias 文献预测
3. 多重比较校正方案需更严格说明
4. 单种子实验、CI 重叠代替等价检验等方法论问题削弱结论强度

论文适合 **Findings track**：方法论贡献有参考价值，实证结果可靠，但核心新颖性和结论的泛化性不足以进入主会议。若能补充非 Llama 模型的因果干预成功案例（如通过 activation patching 或 DAS），或显著加强统计分析（多种子、正式等价检验），可重新评估 Conference 级别。

---

## Detailed Comments

### Section 1 (Introduction)
- "A dissociation emerges between detection and decision" — 应加 "in Llama" 限定
- "the first evidence that knowledge conflict signals are linearly detectable across languages" — 改为 "the first cross-lingual evidence"，Zhao et al. (2024) 已有单语证据

### Section 2 (Related Work)
- 第三段 (Representation steering) 缺失 Turner et al. (2023) Activation Addition 和 Marks et al. (2024) Geometry of Truth
- 提到 activation patching 作为 future work 但未引用 Meng et al. (2022) 原始论文

### Section 3 (Method)
- §3.6: "Bonferroni correction applied per model as an independent family" — 需解释为何不按 [层×α] 全 family 校正
- §3.6: Bonferroni threshold = 0.005（k=10）需与 Table 3 caption "p<0.05" 统一

### Section 4 (Experiments)
- §4.3: Qwen CI [-0.6, 13.7] 包含零，"consistent across all three architectures" 应改为 "consistent in direction"
- §4.5: COMET tercile Fisher test 应报告效应量和功效分析
- §4.6: Table 3 中 Qwen/Gemma 行缺具体 flip rates，信息密度不对称

### Section 5 (Discussion)
- Cross-task probe transfer 实验是重要结果，放在 Discussion 结构不佳，应在 Experiments 中报告
- "A suggestive MLP trend" 段建议移至 Appendix

### References
- yang2024qwen25 → 替换为 Qwen3 Technical Report (2505.09388)
- 多个条目 "and others" 格式需补全
- 补充 Meng 2022, Geiger 2024, Turner 2023, Marks 2024