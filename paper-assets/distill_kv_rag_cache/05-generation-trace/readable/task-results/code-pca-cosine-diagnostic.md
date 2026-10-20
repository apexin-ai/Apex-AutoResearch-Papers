# code pca cosine diagnostic

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pca-cosine-diagnostic_20260514T081236_result.json`
- **Structured JSON:** [`2105cff0ab954b4c3560.json`](../../sessions/21/2105cff0ab954b4c3560.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总结果：

## Summary Table

| Ratio | PCA mode | Keys cosine (mean) | Values cosine (mean) | Key MSE | Value MSE |
|-------|----------|-------------------|---------------------|---------|-----------|
| 4x | per-sample | 0.9990 | 0.9888 | 0.009061 | 0.001673 |
| 4x | offline | 0.9987 | 0.9864 | 0.011468 | 0.002064 |
| 8x | per-sample | 0.9658 | 0.7909 | 0.331852 | 0.077809 |
| 8x | offline | 0.9578 | 0.7733 | 0.417829 | 0.077988 |
| 16x | per-sample | 0.8712 | 0.6494 | 1.724829 | 0.449035 |
| 16x | offline | 0.8435 | 0.6655 | 2.336273 | 0.699000 |

## 分析

### 1. Cosine > 0.99 但 F1 有 gap → RoPE 放大量化噪声

4x 压缩下 keys cosine 0.999、values cosine 0.989，几乎完美重建。如果此压缩率下 EM 恢复但 F1 仍有 gap，说明：
- **微小的重建误差经 RoPE 旋转后被放大**——query-key dot product 对高频旋转维度的误差极其敏感
- Values 的 cosine 稍低（0.989 vs 0.999），但 value 误差直接影响输出分布的 soft token，这正是 F1（部分匹配）比 EM（精确匹配）更敏感的原因

### 2. Per-layer 分析：哪些层压缩质量最差？

**Layer 0 的 values 一致最差**——所有压缩率和模式下：
- 4x: values cosine ~0.93（其他层 >0.98）
- 8x: values cosine ~0.65（其他层 >0.77）
- 16x: values cosine ~0.53（其他层 >0.62）

**Layer 24（倒数第 8 层）次差**，尤其 values：
- 8x: values 0.776 vs 其他中间层 0.80-0.82
- 16x: values 0.624 vs 其他中间层 0.65-0.68

Keys 跨层分布相对均匀，Layer 0 始终最好（cosine ~0.994-0.977），说明 **values 的压缩难度在不同层间差异远大于 keys**。

### 3. Per-sample vs Offline PCA 的差距

| Ratio | Keys cosine gap | Values cosine gap | Key MSE ratio |
|-------|----------------|-------------------|---------------|
| 4x | 0.0003 | 0.0024 | 1.27x |
| 8x | 0.0080 | 0.0176 | 1.26x |
| 16x | 0.0277 | -0.0161* | 1.35x |

Offline PCA 的 keys 一致劣于 per-sample（基底不完全匹配当前输入的主成分方向），差距随压缩率增大而扩大。

*16x offline values cosine 反而略高于 per-sample（0.6655 vs 0.6494），但 MSE 明显更大（0.699 vs 0.449）——这说明在极高压缩率下，offline 基底保留了更多中等重要的方向，cosine 略好但绝对误差更大。总体而言 **offline 和 per-sample 差距在合理范围内（4x 几乎无差，8x 约 1-2% cosine 损失）**。

---
