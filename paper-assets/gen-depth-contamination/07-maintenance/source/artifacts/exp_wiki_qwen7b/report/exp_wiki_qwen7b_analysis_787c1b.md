# exp_wiki_qwen7b Analysis

## 结论
K* = 2 (success)

Qwen2.5-7B 在 Wikipedia 上 K*=2，与 Qwen2.5-1.5B 一致，验证了 Qwen 家族在 Wikipedia 上的 K*=2 pattern 跨规模成立。

## 关键指标
| Depth comparison | AUC (mean) | AUC (std) | JSD | 判定 |
|-----------------|-----------|-----------|-----|------|
| 0 vs 1 | 0.9673 | 0.0024 | 0.083514 | 显著 > chance |
| 1 vs 2 | 0.6108 | 0.0092 | 0.010991 | > 0.60 threshold |
| 2 vs 3 | 0.5562 | 0.0137 | 0.005550 | ≈ chance |
| 3 vs 4 | 0.5297 | 0.0099 | 0.004611 | ≈ chance |
| 4 vs 5 | 0.5290 | 0.0105 | 0.003894 | ≈ chance |

Ordinal classification: MAE=1.2501, Accuracy=0.3532

## 与假设对比

| 模型 | 语料 | K* | 备注 |
|------|------|----|------|
| Qwen2.5-1.5B | Wikipedia | 2 | 已知 |
| **Qwen2.5-7B** | **Wikipedia** | **2** | **本实验** |
| Pythia-1.4B | Wikipedia | 1 | 已知 |
| OLMo-1B | Wikipedia | 1 | 已知 |
| LLaMA-3.1-8B | Wikipedia | 1 | 已知 |
| Mistral-7B | Wikipedia | 1 | 已知 |

假设验证：Qwen 家族在 Wikipedia 上 K*=2 是 scale-consistent 的（1.5B → 7B 均为 K*=2），而其他所有模型家族在 Wikipedia 上均为 K*=1。

## 解读

1. **Qwen 家族独特性确认**：在 Wikipedia 语料上，仅 Qwen 家族维持 K*=2，其他模型（含同为 7B 级的 LLaMA-8B、Mistral-7B）均为 K*=1。这不是规模效应，而是模型家族/预训练策略的特征。

2. **AUC 衰减模式**：depth 0→1 极强 (0.97)，depth 1→2 刚过阈值 (0.61)，depth 2→3 急剧跌落至 chance (0.56)。JSD 同步从 0.011 骤降至 0.006，表明 depth 2 是 contamination 信号的边界。

3. **跨语料对比**：Qwen-7B 在 C4 上 K*=2，在 arXiv 上 K*=3，在 Wikipedia 上 K*=2。Wikipedia 的 K*=2 低于 arXiv 的 K*=3，符合 Wikipedia 作为通用文本其 continuation 信号更快饱和的预期。

4. **Top features**：freq_entropy 和 surp_d1_skew 是最重要的判别特征，与其他实验一致。
