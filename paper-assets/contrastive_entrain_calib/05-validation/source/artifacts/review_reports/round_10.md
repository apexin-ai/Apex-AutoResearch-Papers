---
round: 10
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-25T23:53:47.588106+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 10 审稿报告

**Venue**: EMNLP 2026 (ARR)  
**Reviewers**: R1, R2  
**轮次**: Round 10 (交叉回应后收敛)  
**收敛状态**: 8/10 AGREE, 2 partial REBUT; Overall 评分一致

---

## Summary

论文提出 "probe reward trap"——在 GRPO 中使用基于线性 probe（d_syc）的 reward signal 训练 sycophancy calibration 时，模型经历 behavioral death（ToF→0），而 ACT（token-level SFT + contrastive loss）成功避免此陷阱。核心 contributions 包括三点：C1 = GRPO 失败、C2 = 1,300-step behavioral death 先于 entropy collapse 的时序观察、C3 = supervision granularity 是 ACT 成功的候选解释。

论文在单一模型（Qwen3-8B）、单一方向质量（离线 AUROC 0.83 / 训练时有效 AUROC ~0.60）、单一 RL 配置（GRPO, group_size=2, 256-token completion）下运行实验。两位 Reviewer 一致认为：实验配置的非标准性（尤其 group_size=2 和 256-token truncation）构成强替代解释，而论文的因果声明和泛化 framing 超出了证据所能支撑的范围。

---

## Strengths

1. **实践警示价值 (S1)**：行为死亡先于熵崩溃 1,300 步的时序观察对从业者有价值——标准监控手段（entropy/KL）无法及时预警，这一盲区在 representation-based RL 中未被充分文档化。

2. **实验框架清晰 (S2)**：Figure 2 有效传达了 Direction Extraction → Reward Design Space → Supervision Paradigm 的三层实验设计逻辑。评分空间（F1-F3 × R1-R3）的系统覆盖在方法论层面有教育意义。

3. **ACT 方法本身 (S3)**：Token-level contrastive alignment training 在 47/47 checkpoints 保持正向 sycophancy score，跨 seed 稳定。作为负面结果的对照，ACT 的成功为后续工作提供了有价值的方向。

4. **可复现性 (S4)**：Appendix A Table 5 超参数完整，匿名 GitHub 承诺代码/数据发布。

5. **d_syc 跨模型验证 (S5)**：Table 1 在 Qwen3-8B 和 Llama-3-8B 上验证了 d_syc 的判别力（AUROC 0.83/0.78），证明方向本身跨架构可迁移。

---

## Weaknesses

### Critical

**W1. Novelty 定位不充分——Goodhart regressional variant 的已知实例化 [R1 AGREE, R2 首提]**

"Probe reward trap" 本质上是 Goodhart's Law（Manheim & Garrabrant, 2019）regressional variant 在 activation-space reward 场景下的具体实例。论文已引用 Manheim & Garrabrant（Section 2, p3），但未与 Goodhart 四分类进行实质性对话，也未明确论证增量贡献。两位 Reviewer 共识：论文应重新定位为 "首次在 representation-based RL 中文档化 Goodhart failure 的时序动态"，而非声称发现了新现象。

**W2. 核心实验仅在单一模型上进行 [R1 AGREE, R2 首提]**

Qwen3-8B 是唯一进行了完整 GRPO/ACT 训练的模型。Llama-3-8B 仅验证 d_syc 判别力（Table 1），未运行任何训练实验。"1,300-step lag" 在不同架构/规模上是否复现完全未知。标题 "Sycophancy Calibration" 暗示的泛化性缺乏实验支撑。

**W3. ACT vs GRPO 对比存在 5+ 维度混淆变量 [双方共识]**

ACT 与 GRPO 之间至少同时变化：(a) 监督粒度（token vs. completion）, (b) 学习范式（SFT + L2 loss vs. policy gradient）, (c) 序列长度（ACT max_seq_len=1,024 vs. GRPO max_completion_length=256, 4× 差异）, (d) label 信息量（ACT 使用 labeled valid/invalid pairs 显式包含 warrant 信息 vs GRPO 仅有标量 reward）, (e) 训练数据对齐方式。C3 的 "supervision granularity" 归因无法从这些混淆中隔离。

**W4. 训练时有效 AUROC 仅 0.60——论文 "high discriminability fails" 的 framing 不成立 [双方共识]**

离线 AUROC 0.83 是 full-length response 上的 5-fold CV 结果。训练时由于 256-token truncation，有效 AUROC 降至 ~0.60。论文核心叙事 "high discriminability ≠ reward utility" 建立在 0.83 上，但训练中实际使用的信号质量远低于此。论文未测试消除 truncation 后（512+ token completion）是否仍然失败。

**W5. GRPO group_size=2 严重偏离标准实践 [持续 critical, Round 3 首提]**

标准 GRPO 使用 group_size 8-64。gs=2 仅提供极弱的 baseline signal，可能本身就足以解释训练失败。gs=8 ablation 仅 3 checkpoints 后 early termination（0.084→0.085→0.054, declining），termination 标准不明确，引入选择偏差。

**W6. Contrastive pairs 无人工验证 [持续 critical, Round 6 首提]**

全部 181 对由 GPT-4.1 生成，无 IAA，cross-model generalization（GPT→Qwen/Llama）不能排除 probe 捕捉的是生成风格而非语义。

### Warning

**W7. Abstract/Intro framing 过度泛化 [双方 AGREE]**

"Every formulation that converts it into a GRPO reward collapses" 和 "Every GRPO reward formulation we tested fails" 在字面上准确，但在读者感知层面暗示了比证据更广泛的否定结论。应限定为 "under our specific configuration (Qwen3-8B, group_size=2, 256-token completion)"。

**W8. d_syc 编码内容论证存在循环推理 [双方 AGREE]**

推理链：GRPO 失败 → d_syc 编码错误信息 → GRPO 必然失败。缺少独立验证（如 activation steering intervention 实验）打破循环。

**W9. 1,300-step lag 的超参数敏感度未讨论 [双方 AGREE]**

1,300 是单 seed、单配置下的单个数字。未分析对 LR、KL 系数、group_size、LoRA rank 的敏感度。应至少报告 3 seed 下 lag 的范围。

**W10. C1/C2/C3 贡献缺乏独立性 [R1 部分 AGREE]**

C3 本质是 C1 的候选解释，不算独立贡献。建议重组为一个核心发现 + 两个子发现，而非三个并列 contributions。

**W11. ACT 成功可能因为 label quality 而非 supervision granularity [双方 AGREE]**

ACT 使用 labeled valid/invalid pairs 显式包含 "是否应该改变" 的信息。这可能是 ACT 成功的根本原因，进一步削弱 C3 的归因。

**W12. Conclusion 因果归因逻辑错误 [持续, Round 9 首提]**

将 d_syc 语义局限归因为所有 GRPO 失败原因，但 R3-only GRPO 不使用 d_syc，需要独立解释。

**W13. 4/31 vs 4/28 数字不一致 [持续, Round 4 首提]**

Introduction 用 4/31，Table 4 用 4/28，混合 gs=2 和 gs=8 数据，仍未统一。

---

## Questions

1. 消除 256-token truncation（使用 512+ token completion）后，d_syc-based GRPO 是否仍然失败？训练时 AUROC 能否接近 0.83？
2. 1,300-step lag 在 3 个不同 seed 下的范围是多少？
3. 将 token-level reward shaping 引入 GRPO（隔离 supervision granularity 因素）结果如何？
4. 如果在 d_syc 方向做 activation steering（正方向移动），是否同时增加 warranted revision 和 sycophantic capitulation 的概率？（独立验证 d_syc 无法区分两者）
5. ACT 成功是否主要因为其标注中包含 warrant 信息（labeled valid/invalid），而非 supervision granularity？
6. 将 ACT 的 max_seq_len 限制到 256 后表现如何？（隔离序列长度因素）

---

## Missing References

**双方共识应引用：**
1. Pimentel et al. (2020) "Information-Theoretic Probing with MDL" — probe 表达能力与 selectivity
2. Rafailov et al. (2024) DPO — reward modeling alternative
3. Voita & Titov (2020) — probing methodology
4. Hewitt & Liang (2019) — probe selectivity
5. Belinkov (2022) — probing survey

---

## External Review

**状态**: 未请求

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成  
**结果**: 0 critical, 1 warning, 8 info

- **[WARNING]** p12: 附录末页仅 ~12 行（约 1/6 页面），超过 3/4 页面空白。建议调整布局合并到 p11。
- **[INFO]** p2: Figure 1(a) axis label/legend 字号偏小（接近 70% 下限）
- **[INFO]** p4: Figure 2 面板内嵌文字字号较小，关键数字可考虑加大或移入 caption
- **[INFO]** p4: Figure 2(b) F1/F2/F3 标记间距紧凑
- **[INFO]** p5: Figure 3 线型在 150dpi 下差异不够明显，建议加 marker
- **[INFO]** p7: Table 4 列间距偏窄（8 列单栏）
- **[INFO]** p8: Figure 4 legend 字号偏小
- **[INFO]** p5-8: 所有 Table booktabs 风格 ✓，Table 4 最优值加粗 ✓
- **[INFO]** p9: Limitations 简短合规 ✓，References 格式统一 ✓

---

## Overall Assessment

**Score: 3.0 — Findings**

**评分理由**：

论文报告了一个有实践参考价值的负面结果（probe-based reward 在 GRPO 中导致 behavioral death），并提供了有意义的时序分析（C2）。但存在以下根本性问题使其无法达到主会议接收水平：

1. **实验配置非标准**：group_size=2 + 256-token truncation 构成强替代解释，无法确定失败源于方法固有缺陷还是配置缺陷。
2. **因果声明缺乏独立验证**：ACT vs GRPO 对比存在 5+ 混淆维度，无消融隔离各因素。
3. **单模型限制**：所有训练仅在 Qwen3-8B 上进行，泛化性无从判断。
4. **Novelty 定位问题**：核心命题与 Goodhart's Law 高度同构，增量贡献论证不足。

作为 Findings 接收的理由：时序分析（behavioral death 先于 entropy collapse）对从业者有警示价值，ACT 方法本身提供了有价值的正面对照，实验框架的系统性覆盖对后续工作有参考意义。

**两位 Reviewer 分歧记录**：
| 问题 | R1 | R2 |
|------|----|----|
| GRPO 失败首要解释 | 实验配置缺陷（gs=2 + truncation） | 方向质量不足 + Goodhart 已知现象 |
| Figure 2 | 优势（有效传达框架） | 劣势（信息过密） |
| Excitement | 3/5 | 2.5/5 |
| AUROC 0.83 解读 | 离线尚可，问题在训练时 0.60 | 0.83 本身不够高 |

---

## Detailed Comments

### 对作者的建议（按优先级排序）

1. **[必须] 消除 truncation 混淆**：运行 512+ token completion 的 GRPO，报告训练时有效 AUROC 及结果。如仍失败，"高判别力方向在 GRPO 中失败" 的结论才能成立。

2. **[必须] 重新定位 novelty**：承认 Goodhart regressional variant，将贡献定位为 "首次在 activation-space reward RL 中文档化其时序结构（behavioral death 先于 entropy collapse）及其对标准监控的盲区"。

3. **[必须] 降级或消融 C3**：当前 C3 归因无法从 5+ 混淆中隔离。最低限度消融：(a) token-level reward shaping in GRPO 或 (b) ACT max_seq_len=256。否则将 C3 从 "contribution" 降为 "hypothesis"。

4. **[强烈建议] 统一 framing**：全文限定为 "under our configuration"，避免 "every formulation fails" 的感知泛化。Abstract/Conclusion 中明确 group_size=2, 256-token, Qwen3-8B-only。

5. **[强烈建议] 分路归因**：Conclusion 中为 d_syc-based GRPO（truncation → 低有效 AUROC）和 R3-only GRPO（per-completion granularity? NLI truncation?）分别提供失败解释。

6. **[建议] 补充缺失引用**：Pimentel et al. (2020), Hewitt & Liang (2019), Belinkov (2022), Voita & Titov (2020), Rafailov et al. (2024)。

7. **[建议] 统一 4/31 vs 4/28 数字**，正式定义 "behavioral death"，贡献重组为 1 core + 2 sub-findings。
