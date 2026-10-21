# PPL 与 Downstream Task 性能断裂：文献调研报告

## 1. 核心结论

**这个现象在文献中是已知的，但尚未被系统性研究。** 多篇论文从不同角度观察到了 PPL-downstream disconnect，但大多作为实验附带发现报告，而非作为核心研究问题。我们的工作在以下方面构成**文献空白**：

- 在 **contextual sparsity predictor + KL distillation** 设置下首次系统报告
- 50% activation sparsity 下 **PPL 仅 1.96x 但 GSM8K 崩溃 98%** 的极端 disconnect 程度
- **repetition degeneration** 作为稀疏化模型的生成退化模式

---

## 2. 直接相关论文

### 2.1 PPL 作为评估指标的不充分性

| 论文 | 年份/会议 | 关键发现 |
|------|-----------|----------|
| Khanal & Capone, "Evaluating the Impact of Compression Techniques on Task-Specific Performance of LLMs" | 2024, arXiv:2409.11233 | **SparseGPT 和 Wanda 在 50% sparsity 下保持 PPL，但下游任务显著退化。** 提出 Jensen-Shannon Divergence 作为更全面的度量。明确指出 "perplexity as the sole evaluation metric is inadequate"。 |
| Xu et al., "Beyond Perplexity: Multi-dimensional Safety Evaluation of LLM Compression" | 2024, EMNLP Findings | PPL 在 45-60% sparsity 前几乎无变化，但完全无法捕捉能力退化。"normalized perplexity score shows poor alignment with human-aligned evaluation, incorrectly assigning high scores to methods exhibiting severe performance collapse." |
| Kodathala & Vunnam, "LLMs can Compress LLMs: Adaptive Pruning by Agents" | 2026, arXiv:2601.09694 | **N:M structured pruning 在 25-30% sparsity 下 factual QA (FreebaseQA) 准确率下降 >97%，但 PPL 几乎无变化。** 这是最极端的 PPL-downstream disconnect 案例。|

**可引用段落：**
> "While SparseGPT and Wanda preserve perplexity even at 50% sparsity, they suffer significant degradation on downstream tasks, highlighting the inadequacy of perplexity as the sole evaluation metric." — Khanal & Capone (2024)

> "Structured N:M pruning methods experience near-total collapse in factual question-answering, losing over 97% of accuracy, while maintaining reasonable perplexity scores." — Kodathala & Vunnam (2026)

### 2.2 稀疏化模型的生成退化 (Degeneration Traps)

| 论文 | 年份 | 关键发现 |
|------|------|----------|
| Siam et al., "Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery" | 2026, arXiv:2604.27115 | 定义了两类退化陷阱：**Type 1 trap**（推理成功但 EOS 预测失败，无限循环）和 **Type 2 trap**（推理过程本身断裂，早期坍缩为重复/无意义 token）。我们观察到的 GSM8K 退化属于 **Type 2 trap**。 |

**可引用段落：**
> "Type 2 traps occur when the model fails to perform meaningful reasoning, collapsing early or mid-generation into incoherent and nonsensical text such as repeated symbols, tokens, or sequences." — Siam et al. (2026)

> "Removing a small subset of highly task-specific neurons (~10%) causes complete performance collapse... robustness threshold around 15-20% pruning." — Siam et al. (2026)

**与我们的联系：** 我们的 sparse model 在 GSM8K 生成中 1-3 句后进入重复循环，完全符合 Type 2 trap 的描述。但 Siam et al. 研究的是 weight pruning，我们是 activation sparsity，机制不同但表现一致。

### 2.3 校准数据分布不匹配

| 论文 | 年份/会议 | 关键发现 |
|------|-----------|----------|
| Bandari et al., "Is C4 Dataset Optimal for Pruning?" | 2024, EMNLP | C4 不是最优校准数据；在 aggressive pruning 下不同校准数据导致下游性能差异显著。算术数据集作为校准数据表现更好。 |
| "Beware of Calibration Data for Pruning Large Language Models" | 2024, arXiv:2410.17711 | 校准数据选择对 post-training pruning 下游任务性能影响极大，尤其在高 sparsity 下。 |

**与我们的联系：** 我们用 C4 数据训练 predictor，但评估在 WikiText-2 (PPL) 和下游 benchmark 上。PPL 评估本身也是 WikiText 这类通用语言建模数据——对 "easy token" 友好。下游任务要求精确知识检索和推理链——对 "hard token" 敏感。

---

## 3. 理论解释框架

综合文献，PPL-downstream disconnect 有三层解释：

### 3.1 PPL 是平均指标，下游任务要求精确 token selection

PPL = exp(avg cross-entropy)，对所有 token 位置等权平均。自然语言中 ~80% 的 token 是高频、可预测的（function words、常见 n-gram），只有 ~20% 是 "hard token"（知识检索、数值推理、逻辑连接词）。

**稀疏化优先丢失 hard token 的精度，但 PPL 被 easy token 主导。** Khanal & Capone (2024) 的 JS Divergence 发现印证了这一点——PPL 变化小但 output distribution 已经显著偏移。

### 3.2 Repetition degeneration 不被 PPL 惩罚

我们的核心观察：sparse model 生成重复 token，但每个重复 token 的条件概率仍然较高（模型"自信地"重复）。在 teacher-forcing 评估（即 PPL 计算）中，模型看到的是 ground truth context，不会进入重复循环；PPL 衡量的是 one-step prediction quality，不是 autoregressive generation quality。

**文献支持：** Xu et al. (2024) 明确指出 "a compressed model may achieve a perplexity score nearly identical to the original's while generating text that is factually different."

### 3.3 知识存储的脆弱性 > 语言建模的鲁棒性

Kodathala & Vunnam (2026) 的发现最为极端：25-30% sparsity 下 factual QA 崩溃 97%，但 PPL 不变。这表明：
- **语言建模能力**（语法、流畅性、局部连贯性）分布在大量参数中，对稀疏化鲁棒
- **知识存储**（factual recall）集中在少量参数路径中，极度脆弱
- **推理能力**（multi-step reasoning）依赖完整的 attention-MLP 交互链，是最脆弱的

---

## 4. 30% vs 50% 的转折点

### 4.1 文献中的 sparsity threshold

| 来源 | Threshold | 描述 |
|------|-----------|------|
| TEAL (Liu et al., 2024) | 25% safe, 40% minimal, 50%+ degradation | Llama-3-8B 在 25% 近零退化，40% 轻微，50% 开始显著退化 |
| Siam et al. (2026) | 15-20% | Task-specific neuron pruning 的 robustness threshold |
| "Sparsity wall" 文献 | 50-60% | 多篇论文报告的 unstructured pruning "性能悬崖" |
| Kodathala & Vunnam (2026) | 25-30% (structured) | N:M structured sparsity 对 factual knowledge 的 catastrophic threshold |
| SparseGPT (Frantar & Alistarh, 2023) | 50% (unstructured) | 可达 50% unstructured sparsity with ~1pt PPL loss |

### 4.2 对我们的启示

我们的 30% sparsity 实验是关键的对比点。如果 30% sparsity 下下游任务保持良好而 50% 崩溃，这符合文献中报告的 phase transition 现象。论文可以 claim：

> "Contextual activation sparsity exhibits a phase transition between 30-50% sparsity: language modeling perplexity degrades gracefully (1.3x → 1.96x), but downstream task performance undergoes catastrophic collapse, consistent with the 'sparsity wall' observed in weight pruning literature."

---

## 5. 与 Contextual Sparsity 方法的对比

| 方法 | MLP Sparsity | PPL | 下游任务 | 是否报告 disconnect |
|------|-------------|-----|----------|-------------------|
| **DejaVu** (Liu et al., 2023, ICML) | 85-95% | 保持 | 7 个 few-shot 任务保持 | 否——但用 OPT-175B，大模型更鲁棒 |
| **TEAL** (Liu et al., 2024, ICLR 2025) | 25-50% | 轻微退化 | 50% 下开始显著退化 | 部分——报告了数值但未深入讨论 |
| **ShadowLLM** (2024, EMNLP) | - | - | 比 DejaVu 提升 15% | 否——focused on predictor architecture |
| **Ours** | 50% | 12.00 (1.96x) | ARC -35%, MMLU -60%, GSM8K -98% | **是——本文核心发现** |

**文献空白：** DejaVu 在超大模型 (OPT-175B) 上实验，大模型对 sparsity 更鲁棒。TEAL 在 Llama-3-8B 上的 50% 结果有下游退化但未深入分析。**没有论文系统研究过 contextual sparsity predictor + distillation 训练下的 PPL-downstream disconnect。**

---

## 6. 可引用文献清单

### 核心引用（Discussion section 必用）
1. **Khanal & Capone (2024)** — PPL 不足以评估压缩模型，arXiv:2409.11233
2. **Xu et al. (2024)** — "Beyond Perplexity"，EMNLP Findings，arXiv:2407.04965
3. **Siam et al. (2026)** — Degeneration traps (Type 1/2)，arXiv:2604.27115
4. **Kodathala & Vunnam (2026)** — Catastrophic factual knowledge degradation at low sparsity，arXiv:2601.09694

### 方法对比引用
5. **TEAL** (Liu et al., 2024) — Training-free activation sparsity baseline，arXiv:2408.14690
6. **DejaVu** (Liu et al., 2023) — Contextual sparsity predictor，ICML 2023
7. **ShadowLLM** (2024) — Predictor-based contextual sparsity，EMNLP 2024
8. **SparseGPT** (Frantar & Alistarh, 2023) — One-shot pruning，ICML 2023

### 校准数据引用
9. **Bandari et al. (2024)** — "Is C4 Dataset Optimal for Pruning?"，EMNLP 2024，arXiv:2410.07461
10. **"Beware of Calibration Data"** (2024) — arXiv:2410.17711

---

## 7. 论文 Discussion Section 写作建议

建议论文中用以下结构讨论：

1. **Observation**: 50% sparsity 下 PPL 仅 12.00 但 GSM8K 0.01，构成极端 PPL-downstream disconnect
2. **Prior evidence**: 引 Khanal & Capone (2024) 和 Xu et al. (2024) 确认这是已知但未充分研究的现象
3. **Mechanism**: PPL 是平均指标，被 easy token 主导；稀疏化优先损伤 hard token 的精度；autoregressive generation 中的错误会 compound（引 Siam et al. 的 Type 2 trap）
4. **Knowledge fragility**: 引 Kodathala & Vunnam (2026) 关于 factual knowledge 的 catastrophic degradation
5. **Implication**: PPL 单独不足以评估稀疏化模型的实用性，需要下游 benchmark；30% sparsity 可能是实用安全边界
