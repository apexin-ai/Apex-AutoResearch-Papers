# M1 Phase Segmentation 诊断分析

## 1. Phase Segmentation 质量统计

### KDE 失败率
- **41/50 (82%) 样本触发 halved-bandwidth fallback**
- 0/50 触发 equal-partition fallback（halved bandwidth 最终都找到了 2 个 minima）
- 仅 9/50 (18%) 样本在默认 bandwidth（Scott's rule）下找到 2 个 local minima

### Phase 数量分布

| 组别 | 样本数 | 平均 phase 数 | 范围 |
|------|--------|---------------|------|
| 默认 bandwidth 成功 | 9 | 16.8 | 6–35 |
| Halved bandwidth fallback | 41 | 3.95 | 2–11 |

两组形成明显双峰：
- **成功组**产生大量 phase 交替（6–35），说明 sparsity 序列有足够变异被 KDE 捕捉
- **失败组**多数仅切分 2–4 个 phase，KDE 被迫在噪声中找分割点

### Token 分布（极度失衡）

| Phase | Token 数 | 占比 | Segment 数 |
|-------|----------|------|-----------|
| execution | 1,022 | **1.2%** | 25 |
| reasoning | 7,007 | **8.1%** | 96 |
| transition | 78,178 | **90.7%** | 192 |

**Total: 86,207 tokens across 313 segments, 50 problems**

## 2. 根因分析：为什么 90% 是 transition

### 分类机制
`_assign_phases` 使用 KDE 密度曲线的 2 个 local minima 作为 threshold：
```
sparsity ≤ threshold[0]  →  execution
threshold[0] < sparsity ≤ threshold[1]  →  reasoning
sparsity > threshold[1]  →  transition
```

### 问题链条

1. **Sparsity 分布不是 tri-modal**：82% 样本的 Scott bandwidth KDE 找不到 2 个 minima，说明分布本质上是 unimodal 或 weakly bimodal（主模态集中在高 sparsity 区域）

2. **Halved bandwidth 引入伪结构**：强制将 bandwidth 从 Scott 降到 0.05，相当于 overfit KDE 到噪声，找到的 "minima" 是密度估计的波动而非真实模态分界

3. **Threshold 偏低**：在 unimodal 高 sparsity 分布上强行切两刀，两个 threshold 都落在主模态的左尾，导致绝大多数 token（主模态体）超过 threshold[1] → 全部归类为 transition

4. **Perplexity 侧证**：dense PPL 在三个 phase 间差异极小（execution=2.25, reasoning=1.18, transition=1.10），说明这些 "phase" 在语言模型行为上没有实质区分度

## 3. Sparsity 分布形态判断

**强证据指向 unimodal（或 quasi-unimodal）分布：**

- 82% KDE 失败率 = 分布中不存在 2 个清晰的 density valley
- 90.7% token 归为同一类 = 绝大多数 sparsity 值集中在一个窄区间
- 无 fallback 成功的 9 个样本多为长序列（phase 数 6–35），更可能是序列长度带来的自然变异而非 tri-modal 结构

**结论：DeepSeek-R1-Distill-Qwen-7B 在 MATH 生成中的 attention sparsity 本质上不是 tri-modal。ThinKV 的 3-phase taxonomy（execution/reasoning/transition）不适用于此模型-任务组合。**

## 4. 建议

### P1 判定：需要 pivot

当前 phase detection 方法（KDE tri-modal assumption）已被证伪。调整 bandwidth 无法修复——问题不在 bandwidth 参数，而在 tri-modal 假设本身。

### 可能的替代方向

1. **数据驱动 phase 检测**：不预设模态数，用 Gaussian Mixture Model（GMM）+ BIC/AIC 自动选择最优组件数。如果 BIC 选出 k=1，则确认 unimodal
2. **基于 token 语义的 segmentation**：用 `<think>`/`</think>` 标签或其他文本特征做 phase 划分，而非依赖 attention sparsity
3. **per-layer sparsity profile**：当前是跨 head 平均的标量 sparsity。不同层可能有不同模式——聚合掩盖了可能存在的 layer-wise multi-modality
4. **放弃 phase-gated 框架**：如果 sparsity 确实 unimodal，则 "不同 phase 需要不同压缩策略" 的前提不成立。可转向 token-level adaptive sparsity（连续值），而非离散 phase 分类

### 下一步验证
- 跑一个诊断实验：对 5–10 个样本 dump 原始 sparsity 数组，做直方图 + GMM fit，正式确认分布形态
- 对比 per-layer sparsity 分布（而非 layer-averaged），看是否有层级出现 multi-modality
