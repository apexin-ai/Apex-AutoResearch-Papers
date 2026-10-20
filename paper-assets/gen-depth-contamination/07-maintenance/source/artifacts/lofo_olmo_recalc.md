# LOFO Table Recalculation: OLMo C4 AUC Update

## Data Change

| Metric | Old | New |
|--------|-----|-----|
| OLMo-1B AUC_1v2 | 0.6146 | 0.508 |
| OLMo-1B AUC_2v3 | 0.5497 | 0.4973 |
| OLMo-1B K* | 2 | 1 |

## Agreement Impact

| Metric | Old | New |
|--------|-----|-----|
| Agreement | 8/9 (89%) | 2/9 (22%) |
| θ̂ range | [0.5725, 0.6004] | [0.5297, 0.5914] |
| θ̂ mean | 0.5894 | 0.5534 |

## Full Recalculation (New Data)

### Fold 1: Hold out Pythia
- Training min(AUC_1v2) = 0.5080 (OLMo-1B)
- Training max(AUC_2v3) = 0.5893 (Qwen-1.5B-RW)
- θ̂ = (0.5080 + 0.5893) / 2 = **0.5487**
- Pythia-1.4B: AUC_1v2=0.6539 > θ̂, AUC_2v3=0.5515 > θ̂ → K*_θ̂=3, K*_0.60=2, **MISMATCH**

### Fold 2: Hold out OLMo
- Training min(AUC_1v2) = 0.5935 (Mistral-7B)
- Training max(AUC_2v3) = 0.5893 (Qwen-1.5B-RW)
- θ̂ = (0.5935 + 0.5893) / 2 = **0.5914**
- OLMo-1B: AUC_1v2=0.508 ≤ θ̂ → K*_θ̂=1, K*_0.60=1, **MATCH**

### Fold 3: Hold out Qwen (5 models)
- Training min(AUC_1v2) = 0.5080 (OLMo-1B)
- Training max(AUC_2v3) = 0.5515 (Pythia-1.4B)
- θ̂ = (0.5080 + 0.5515) / 2 = **0.5297**
- Qwen-1.5B-RW: 0.6957 > θ̂, 0.5893 > θ̂ → K*_θ̂=3, K*_0.60=2, **MISMATCH**
- Qwen-7B: 0.6178 > θ̂, 0.5460 > θ̂ → K*_θ̂=3, K*_0.60=2, **MISMATCH**
- Qwen-1.5B-base: 0.6262 > θ̂, 0.5496 > θ̂ → K*_θ̂=3, K*_0.60=2, **MISMATCH**
- Qwen-1.5B-cont: 0.6114 > θ̂, 0.5609 > θ̂ → K*_θ̂=3, K*_0.60=2, **MISMATCH**
- Qwen-14B: 0.6210 > θ̂, 0.5494 > θ̂ → K*_θ̂=3, K*_0.60=2, **MISMATCH**

### Fold 4: Hold out LLaMA
- Training min(AUC_1v2) = 0.5080 (OLMo-1B)
- Training max(AUC_2v3) = 0.5893 (Qwen-1.5B-RW)
- θ̂ = (0.5080 + 0.5893) / 2 = **0.5487**
- LLaMA-3.1-8B: 0.6123 > θ̂, 0.5274 ≤ θ̂ → K*_θ̂=2, K*_0.60=2, **MATCH**

### Fold 5: Hold out Mistral
- Training min(AUC_1v2) = 0.5080 (OLMo-1B)
- Training max(AUC_2v3) = 0.5893 (Qwen-1.5B-RW)
- θ̂ = (0.5080 + 0.5893) / 2 = **0.5487**
- Mistral-7B: 0.5935 > θ̂, 0.5402 ≤ θ̂ → K*_θ̂=2, K*_0.60=1, **MISMATCH**

## Result Table (would-be .tex)

| Held-out | Model | AUC_1v2 | AUC_2v3 | θ̂ | K*_θ̂ | K*_0.60 | Match |
|----------|-------|---------|---------|------|-------|---------|-------|
| Pythia | Pythia-1.4B | 0.6539 | 0.5515 | 0.5487 | 3 | 2 | x |
| OLMo | OLMo-1B | 0.5080 | 0.4973 | 0.5914 | 1 | 1 | v |
| Qwen | Qwen-1.5B-RW | 0.6957 | 0.5893 | 0.5297 | 3 | 2 | x |
| | Qwen-7B | 0.6178 | 0.5460 | 0.5297 | 3 | 2 | x |
| | Qwen-1.5B-base | 0.6262 | 0.5496 | 0.5297 | 3 | 2 | x |
| | Qwen-1.5B-cont | 0.6114 | 0.5609 | 0.5297 | 3 | 2 | x |
| | Qwen-14B | 0.6210 | 0.5494 | 0.5297 | 3 | 2 | x |
| LLaMA | LLaMA-3.1-8B | 0.6123 | 0.5274 | 0.5487 | 2 | 2 | v |
| Mistral | Mistral-7B | 0.5935 | 0.5402 | 0.5487 | 2 | 1 | x |

## Root Cause Analysis

OLMo-1B 的 AUC_1v2=0.508 接近随机水平（0.5），是所有 C4 模型中的极端异常值。当 OLMo 在训练集中时（4/5 个 fold），它成为 min(AUC_1v2) 并将 θ̂ 从 ~0.59 拉低到 ~0.53-0.55。这导致：

1. **θ̂ 被系统性低估**：大多数 AUC_2v3 值都高于被压低的 θ̂，导致算法预测 K*_θ̂ ≥ 3，而 K*_0.60 只给 K*=2
2. **Mistral fold 翻转**：Mistral 从 match 变为 mismatch（θ̂=0.5487 < 0.5935，所以 K*_θ̂=2，但 K*_0.60=1）
3. **唯一不受影响的 fold**：hold-out OLMo（训练集不含 OLMo 时 θ̂=0.5914 不变）和 hold-out LLaMA（虽然 θ̂ 降低，但 LLaMA 的 AUC_2v3=0.5274 < θ̂=0.5487 所以仍然 K*=2）

本质问题：LOFO 的 θ̂ 用 min(AUC_1v2) 作为下界，一个 K*=1 的异常模型（AUC 接近 0.5）会主导整个估计。

## Director 决策选项

1. **排除 K*=1 模型出 LOFO 训练集**：K*=1 意味着 gen-1 都无法区分，这类模型本身不携带关于 θ 的有效信息。排除后 C4 LOFO 回到 OLMo-free 状态，θ̂ 稳定在 0.57-0.60。但这改变了算法定义，需要在论文中说明。

2. **用 median 代替 min**：θ̂ = (median(AUC_1v2) + max(AUC_2v3)) / 2，对异常值更鲁棒。但同样改变算法定义。

3. **保持原算法，如实报告 22% agreement**：说明 OLMo 作为 K*=1 模型的特殊性，论证 LOFO 在排除极端 K*=1 模型后仍然有效。

4. **仅更新 OLMo 行的 AUC 和 K*，不重算 θ̂**：保持 θ̂ 不变（因为 θ̂ 的目的是验证 θ=0.60 的合理性，而非精确估计），只更新 OLMo 的 K* 从 2 到 1。但这在数学上不一致。

5. **将 LOFO 中的 min 改为 percentile（如 10th percentile）**：在只有 4-8 个训练样本时，percentile 和 min 几乎等价，效果有限。
