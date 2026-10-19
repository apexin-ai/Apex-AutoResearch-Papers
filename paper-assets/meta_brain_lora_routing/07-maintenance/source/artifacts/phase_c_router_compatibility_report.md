# Phase C: PAR Router 兼容性验证报告

**日期**: 2026-05-16  
**结论**: **NEED_RETRAIN** — Router 不兼容 pi0_libero，需要重新收集激活并重训。

---

## 1. PaliGemma 权重变化分析

pi0_libero fine-tuning **未冻结 PaliGemma**，所有权重均已修改：

| 指标 | 值 |
|------|-----|
| 总参数组数 | 777 |
| 已变化 | 777 (100%) |
| 未变化 | 0 (0%) |
| 所有 key 平均差异 | 0.3462 |

### Vision Tower 各层平均差异

| Layer | Mean Diff | 备注 |
|-------|-----------|------|
| 0 | 0.5006 | |
| 1-5 | 0.287~0.339 | |
| **6** | **0.2856** | **Router 所用层** |
| 7-15 | 0.269~0.293 | |
| 16-26 | 0.340~0.986 | 越深变化越大 |

### Layer 6 各参数详细差异

| 参数 | Mean Abs Diff | Max Diff |
|------|--------------|----------|
| mlp.fc1.bias | 1.6753 | 4.1250 |
| layer_norm2.weight | 0.8224 | 2.5469 |
| layer_norm1.weight | 0.7463 | 2.1875 |
| self_attn.k_proj.bias | 0.5219 | 2.1875 |
| self_attn.q_proj.bias | 0.2599 | 8.5000 |
| mlp.fc2.bias | 0.1222 | 2.4688 |
| layer_norm2.bias | 0.1083 | 3.0938 |
| self_attn.out_proj.bias | 0.1077 | 1.8594 |
| layer_norm1.bias | 0.0672 | 4.4375 |
| self_attn.v_proj.bias | 0.0309 | 0.2969 |
| mlp.fc1.weight | 0.0195 | 0.4551 |
| self_attn.q_proj.weight | 0.0184 | 0.2734 |
| self_attn.k_proj.weight | 0.0182 | 0.2695 |
| mlp.fc2.weight | 0.0173 | 0.7344 |
| self_attn.v_proj.weight | 0.0175 | 0.2910 |
| self_attn.out_proj.weight | 0.0164 | 0.7578 |

## 2. 对 Router 的影响

**Router 架构**: 2-layer MLP (2048 → 256 → 3), 使用 paligemma_layer_6 的 first token。

**原始激活统计** (pi0_base 上收集):
- mean ≈ -0.05, std ≈ 5.4, range [-232, 43]

**影响判断**:
- LayerNorm 权重/bias 变化 > 0.7（相当于重新缩放激活分布）
- MLP bias 变化高达 1.67（直接偏移激活均值）
- 这些变化会导致 layer 6 输出的激活分布发生根本性改变
- Router 在新分布上的分类边界将失效

**预期 F1 下降**: 无法精确估计（未加载 pi0_libero 推理），但基于 LayerNorm 和 bias 的大幅变化，预计 F1 将**严重下降**（估计 < 0.5），Router 基本失效。

## 3. 重训工作量评估

| 项目 | 估计 |
|------|------|
| 前置依赖 | Phase B 完成 pi0_libero 加载修复 |
| 激活收集 | 每种扰动类型 ~100 episodes × 6 类型 = ~600 samples |
| 收集耗时 | 1-2 小时（依赖推理速度） |
| Router 训练 | < 10 分钟（2-layer MLP, 5-fold CV） |
| GPU 需求 | 1× GPU（激活收集时加载 pi0_libero） |
| 总耗时 | ~2-3 小时（排除 Phase B 依赖等待） |

## 4. 建议下一步

1. **等待 Phase B** 完成 pi0_libero 模型加载兼容性修复
2. **复用现有管线**: `phase1/train_par_router.py` 和激活收集流程可直接复用，只需将模型换为 pi0_libero
3. **考虑冻结策略**: 如果后续还有 fine-tuning 迭代，建议在 pi0 fine-tuning 时**冻结 vision tower**（至少前 10 层），避免每次重训 Router
4. **备选方案**: 如果 Phase B 耗时较长，可先用 weight diff 做线性校正（affine transform on activations），作为临时 workaround 快速验证流程
