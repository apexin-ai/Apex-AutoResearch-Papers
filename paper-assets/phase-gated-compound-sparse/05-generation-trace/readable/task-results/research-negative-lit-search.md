# research negative lit search

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_negative-lit-search_20260513T212407_result.json`
- **Structured JSON:** [`56a2b1f2571ad9d1f07f.json`](../../sessions/56/56a2b1f2571ad9d1f07f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调研完成，已保存到 `memory.md`。核心发现：

**Q1: Compound sparsity 是否总是 super-additive？**
— 是，有直接证据。SparK (AAAI 2026) 报告 ThinK + SnapKV/PyramidKV 组合时性能暴跌 65%；Joint Pruning+Quantization (CVPR 2020) 显示 compound 有效阈值从 80% 降到 60%。无论文报告过 sub-additive（协同）效应。

**Q2: Phase-dependent sparsity？**
— ThinKV (ICLR 2026 Oral) 是最相关的工作：将 CoT 分解为 reasoning/execution/transition 三种 thought type，发现不同 type 需要不同压缩策略。与我们的 phase 划分高度吻合。RaaS (ACL 2025) 发现了 milestone tokens 的"先重要后衰减"模式，可解释 reasoning phase 交互更强。

**Q3: Interaction Index 度量？**
— **无直接先例**。现有工作用 accuracy gap 定性报告交互，未形式化为 index。Compression Scaling Laws 的 "effective parameter count" 是最近的类似度量，但只针对单一压缩维度。这是我们的方法论贡献。

**Q4: KV cache 方法与 head pruning 交互？**
— SparK/ThinK 研究了 channel pruning + token eviction 的交互，但 **head pruning + KV eviction** 的组合在文献中未被系统研究过。这是我们的空白填补点。

**Q5: Reasoning model sparsity 分析？**
— RAC (NeurIPS 2025) 在 DeepSeek-R1-Distill-7B 上证实 reasoning model 对 sparsity 更敏感（标准方法导致 CoT 退化）。RESP 和 SSGR 进一步证实需要 reasoning-aware pruning。

**我们工作的独特定位**：首次量化 head pruning + KV eviction 的 compound interaction，首次提出 Interaction Index，首次发现 compound interaction 的 phase-dependent 行为。与 ThinKV 角度正交（他们优化单一压缩策略，我们量化多维压缩交互）。

Sources:
- [SparK (AAAI 2026)](https://arxiv.org/abs/2508.15212)
- [ThinKV (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01290)
- [RaaS (ACL 2025)](https://arxiv.org/abs/2502.11147)
- [RAC - Reasoning Models Can Be Pruned (NeurIPS 2025)](https://arxiv.org/abs/2509.12464)
- [Compression Scaling Laws](https://arxiv.org/abs/2502.16440)
- [Lethe (AAAI 2026)](https://arxiv.org/abs/2511.06029)
- [MixedDimKV](https://arxiv.org/abs/2603.20616)
- [RESP](https://arxiv.org/abs/2512.02185)
- [SSGR](https://arxiv.org/abs/2511.18864)
- [DeepSeek NSA](https://arxiv.org/abs/2502.11089)
- [LKV](https://arxiv.org/abs/2605.06676)
- [Joint Pruning & Quantization (CVPR 2020)](https://openaccess.thecvf.com/content_CVPR_2020/papers/Yang_Automatic_Neural_Network_Compression_by_Sparsity-Quantization_Joint_Learning_A_Constrained_CVPR_2020_paper.pdf)

---
