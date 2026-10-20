# Related Work 完整性审查

**审查日期**: 2026-05-24
**论文**: Structured Self-Consistency for Information Extraction

## 当前覆盖情况

- **已引用论文数量**: 约 40 篇（bib 文件中），Related Work 正文直接引用约 20 篇
- **覆盖的主题领域**:
  1. Test-time compute scaling / Best-of-N（Wang 2023, Snell 2025, Brown 2024）
  2. Reward-free selectors / BoN scaling laws（Taubenfeld 2025, Kang 2025, Gao 2023）
  3. Trained verifiers（Cobbe 2021, Lightman 2024）
  4. Consistency for structured IE（Yao 2026, Xie 2023, Yun 2025）
  5. Generative IE / constrained decoding（Zhou 2024 UniversalNER, Sainz 2024 GoLLIE, Willard 2023, Dong 2024 XGrammar）
  6. MBR decoding（Eikema 2022, Eikema 2025）
  7. Uncertainty / confidence estimation（Kuhn 2023, Geng 2024, Xia 2025 survey）
  8. Selective prediction（Geifman 2017）

## 建议补充的引用（按优先级排序）

### P0（强烈建议）

- **"Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction"** (arXiv 2601.16999, Jan 2026) — 理由：直接针对 NER 的不确定性量化，使用 conformal prediction 提供有限样本覆盖保证，与本文的 QE 信号和 selective prediction 高度互补。本文声称 QE 信号可支持 abstention，该工作提供了更强的统计保证框架作为对比。

- **"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models"** (Chakraborty et al., ICLR 2025, arXiv 2412.15287) — 理由：提出针对 BoN 推理策略的训练方法，让模型在训练时就感知 BoN 选择过程。与本文的 "fine-tuned model + stochastic sampling + selection" 范式直接相关——本文在推理端做 selection，该工作在训练端优化 BoN，是互补方向。

- **"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information"** (arXiv 2510.01499, EMNLP 2025) — 理由：超越简单多数投票的 LLM 输出聚合方法，利用高阶信息（模型间相关性、预期准确率）。本文的 entity-level voting 是一种聚合策略，该工作提供了更系统的聚合理论框架。

- **"Assessment of Generative Named Entity Recognition in the Era of Large Language Models"** (arXiv 2601.17898, Jan 2026) — 理由：对生成式 NER 在 LLM 时代的系统评估，覆盖 8 个 LLM 和 4 个标准 NER 数据集，展示 parameter-efficient finetuning + structured format 的竞争力。与本文使用 fine-tuned LLM 做生成式 NER 的实验设置直接对应。

### P1（建议）

- **"Theoretical Guarantees for Minimum Bayes Risk Decoding"** (arXiv 2502.12685, Jun 2025) — 理由：为 MBR 解码提供理论分析，解释其有效性。本文已引用 Eikema 2022/2025 的 MBR 工作，该理论分析可以加强 MBR 相关讨论的理论基础。

- **"Diversified Sampling Improves Scaling LLM Inference"** (arXiv 2502.11027, 2025) — 理由：证明多样化采样改善推理扩展效果。与本文发现的 diversity collapse / LP compression 问题直接相关——如果采样多样性不足，扩展收益受限。

- **"s1: Simple Test-Time Scaling"** (Muennighoff et al., EMNLP 2025) — 理由：已在 bib 中但未在 Related Work 正文中引用。作为简单有效的 test-time scaling 方法，值得在第一段提及。

- **"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs"** (arXiv 2603.03305, Mar 2026) — 理由：constrained decoding 的最新进展，与本文使用 XGrammar 做 constrained decoding 相关，但优先级较低因为本文的重点不在 decoding 方法本身。

- **"Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains"** (arXiv 2603.00924, Mar 2026) — 理由：将 conformal prediction 应用于 LLM-based entity extraction 的具体案例，与本文的 QE + abstention 方向相关。

### P2（可选）

- **"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models"** (arXiv 2505.23038, 2025) — 理由：多个小参数 LLM 的 NER 集成方法，与本文的单模型多采样方法形成对比，但方法论差异较大。

- **"Uncertainty-Aware Decoding with Minimum Bayes Risk"** (arXiv 2503.05318, Mar 2025) — 理由：将 MBR 扩展为不确定性感知解码，与本文的 uncertainty estimation + MBR 结合有概念联系。

- **"Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling"** (arXiv 2510.03199, 2025) — 理由：提出 BoM 策略（先多数投票过滤再 reward 选择），对本文的 selection 策略设计有参考价值，但针对的是 reasoning/code 而非 structured prediction。

- **"Iterative Deepening Sampling as Efficient Test-Time Scaling"** (arXiv 2502.05449, Jun 2025) — 理由：提出 ID-sampling 提升 BoN 效率，与本文的采样效率问题相关但场景不同。

- **Trust but Verify! A Survey on Verification Design for Test-time Scaling** (arXiv 2508.16665, Sep 2025) — 理由：test-time scaling 中 verifier 设计的综述，本文的 QE 信号可视为一种 verification 机制，但该综述主要面向 reasoning 任务。

## 当前 Related Work 的优势和不足

### 优势
- **结构清晰**：三段式组织（test-time compute → structured IE consistency → uncertainty/MBR），逻辑递进
- **定位精准**：每段末尾都明确指出本文与已有工作的区别（"structured prediction requires different aggregation"、"without prompt engineering"、"degeneracy as the primary bottleneck"）
- **核心文献覆盖良好**：self-consistency 原始论文、Snell 2025 test-time scaling、Yao 2026 consistency-accuracy、Xie 2023 entity voting、Eikema MBR 系列均已引用
- **篇幅控制得当**：约半页，符合 EMNLP long paper Related Work 的典型长度

### 不足
- **缺少 2025-2026 生成式 NER 评估文献**：本文在 fine-tuned LLM 上做生成式 NER，但未引用最新的生成式 NER 系统性评估（如 arXiv 2601.17898），使得实验设置的定位不够完整
- **MBR 理论基础薄弱**：引用了 Eikema 2022/2025 但缺少 MBR 的理论保证文献，而本文的 selection 策略本质上是 MBR 的实例化
- **缺少训练端优化的对比视角**：本文在推理端做 selection，但未提及 inference-aware fine-tuning（ICLR 2025）这一互补方向，读者可能质疑为何不在训练时直接优化 BoN
- **聚合方法讨论不够系统**：entity-level voting 是核心贡献之一，但未引用 2025 年关于超越多数投票的聚合理论工作
- **NER 不确定性量化的最新进展未覆盖**：conformal prediction for NER（2026）与本文的 QE + selective prediction 高度相关但未引用
- **bib 中已有但正文未引用的遗漏**：`muennighoff2025s1`（s1: Simple Test-Time Scaling）在 bib 中存在但 Related Work 未提及
