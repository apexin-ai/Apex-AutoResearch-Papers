# ops check pca verification

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_pca_verification_20260520T092424_result.json`
- **Structured JSON:** [`f7e364d06c22dd34e2da.json`](../../sessions/f7/f7e364d06c22dd34e2da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成（May 20 12:52，耗时 560s）。关键结果：

## PCA Artifact Verification — R1-8B, PCA-100d vs No-PCA

**状态**: ✅ 已完成，209 traces，25 layers × 4 windows × 5 metrics，bootstrap 1000x

### 核心发现：PCA-100d 在 HarmThoughts R1-8B 上**确实产生 artifact**

| 指标 | PCA-100d 最佳 | No-PCA 最佳 | 结论 |
|------|-------------|------------|------|
| **bal_acc** | 0.825 (L13,W5) | 0.801 (L12,W5) | PCA 略高 +2.4pp，但可能是过拟合噪声维度 |
| **precision** | 0.633 (L20,W5) | 0.732 (L12,W5) | **No-PCA 大幅领先 +10pp** |
| **FPR** | 0.145 (L23,W3) | 0.072 (L8,W15) | **No-PCA FPR 低一倍** |
| **crossing_rate** | 0.558 (L0,W5) | 0.512 (L0,W15) | PCA 略高，但最佳层塌缩到 L0 |
| **composite** | 0.430 (L10,W15) | 0.803 (L12,W5) | **No-PCA 碾压，差距近 2x** |

### 关键 artifact 模式

1. **L0 artifact 确认**: PCA-100d 的 crossing_rate 和 composite 最佳层塌缩到 L0/L1，说明 PCA 降维后 L0 的噪声被放大为虚假信号
2. **Precision-FPR 退化**: PCA 将 precision 拉低 ~10pp、FPR 翻倍，说明降维丢弃了区分 safe/unsafe 的关键维度
3. **最佳层不一致**: PCA 下各指标最佳层散布在 L0-L20，而 No-PCA 稳定在 L9-L16 中层区间——PCA 引入了虚假的层间变异
4. **Bal_acc 假性提升**: PCA 的 bal_acc 略高但 composite 远低，说明 bal_acc 的提升来自降维后的过拟合而非真实信号

**结论**: PCA-100d 在 HarmThoughts R1-8B 上复现了 L0 artifact，与之前在其他模型上的发现一致。No-PCA 是更可靠的 baseline。

---
