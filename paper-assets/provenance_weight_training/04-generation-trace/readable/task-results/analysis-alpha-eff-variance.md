# analysis alpha eff variance

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_eff_variance_20260522T174506_result.json`
- **Structured JSON:** [`038a910758f3385a6419.json`](../../sessions/03/038a910758f3385a6419.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**α_eff 方差分解（R²≈0.47, 53% 未解释方差）**

| 来源 | 占比 | 证据 |
|------|------|------|
| 检测器噪声 | **70.2%** | TF-IDF 准确率 85.8%, FP=19.4%, 8.8%样本在边界区(acc≈55%) |
| adaptive b 变换 | **29.8%** | b* 把 α_eff 压缩向 τ=0.7, 降低与真实组成的相关性 |

**关键发现：**
- B=4→B=16 使 α_eff 方差下降 10.25×，但 R² 不变（0.47→0.44），说明**瓶颈在检测器质量而非 batch 大小**
- mean_q 方差比 = 4.04，完美符合二项分布 1/B 缩放理论
- 70% 的 gap 是任何基于检测器的方法都会有的固有限制，30% 是 adaptive 算法的刻意设计（保证 α_eff≥τ）

报告已保存到 artifacts 并注册。

---
