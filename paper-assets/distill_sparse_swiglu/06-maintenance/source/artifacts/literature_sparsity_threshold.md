# Literature Survey: Sparsity Threshold / Phase Transition in Activation Sparsity

## 1. Phase Transition in LLM Compression (直接相关)

**Ma et al., "Phase transitions in large language model compression", npj AI (Nature), 2026**
- 系统分析 30+ 压缩方法的 Phase Transition Point (PTP)
- 核心发现：structured pruning 在 30-45% sparsity 处崩溃，unstructured pruning 在 55-65% 处崩溃
- 性能呈现 "gradual degradation → exponential collapse" 模式
- **直接支持我们的观察**：50% activation sparsity 恰好落在 structured/unstructured 的 PTP 区间

## 2. Sparsing Law (ICML 2025)

**Song et al., "Sparsing Law: Towards LLMs with Greater Activation Sparsity", ICML 2025**
- 提出 PPL-p% sparsity metric，建立 activation sparsity 的 scaling law
- 发现：ReLU 和 SiLU 的 sparsity 随训练量呈 power-law 演化（方向相反）
- activation ratio 与 width-depth ratio 线性相关，存在 bottleneck point
- **启示**：sparsity 有内在极限，不是无限可压缩的

## 3. CATS (COLM 2024)

**Lee et al., "CATS: Contextually-Aware Thresholding for Sparsity in LLMs", COLM 2024**
- 50% MLP activation sparsity 时 downstream 保持 ~99% 原始性能
- 但这是针对 post-training thresholding，非 distillation-based prediction
- **关键区别**：CATS 用精确阈值保留最重要的 activations，而 predictor-based 方法有预测误差累积

## 4. DejaVu (ICML 2023)

**Liu et al., "Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time", ICML 2023**
- OPT-175B 在 75% sparsity 前无 accuracy drop
- Predictor accuracy：浅层 >99%，深层 ~93%
- **但**：仅评估 PPL 和简单 zero-shot，未系统测试 MMLU/GSM8K 等推理任务

## 5. PPL-Downstream Disconnect

**多篇论文报告此现象（2024-2025）**：
- Týr-the-Pruner (2025): 不同 pruning mask 可达相似 PPL 但 downstream 差异显著
- GISP (2025): layer-wise reconstruction 保 PPL 但不优化 downstream accuracy
- **核心机制**：PPL 衡量 average next-token prediction，不反映 multi-step reasoning 能力

## 6. SwiGLU 特殊性

**ProSparse (COLING 2025) + TurboSparse (2024)**：
- SwiGLU 在 80% sparsity 时 PPL 急剧恶化
- dReLU 可在 90% sparsity 保持性能
- **解释**：SwiGLU 的 gate 机制使 activation 分布更 dense，强制稀疏化损失更大

## 总结与 Framing 建议

### 是否有人提出过类似 threshold 概念？
**是。** Ma et al. (2026) 的 PTP 概念完全对应我们的观察。但他们聚焦 weight pruning/quantization，**activation sparsity 的 PTP 尚未被系统研究**。

### 我们的发现够不够作为 contribution？
**够，但需要精确定位**：
1. 我们的贡献不是 "threshold 存在"（已被 Ma et al. 证明），而是 **activation sparsity prediction 中的 threshold 行为**——predictor error 在高 sparsity 下非线性放大
2. PPL-downstream disconnect 在 contextual sparsity 中的具体表现（30% 可修复 vs 50% 不可逆）是新发现
3. 建议 framing："Phase transition in contextual sparsity prediction reveals a critical regime (~40-50%) where allocation strategies lose efficacy, distinct from the gradual PPL degradation"

### 理论解释方向
- 信息瓶颈：50% sparsity 时 MLP 的有效 rank 低于下游任务所需的最小表征维度
- Predictor 误差累积：单层 93% accuracy × 32 layers = 全局大量错误选择
- 与 Ma et al. 的 "三类冗余耗尽" 理论一致：超过 PTP 后压缩破坏非冗余信息
