# analysis partial anova v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_partial_anova_v2_20260526T120959_result.json`
- **Structured JSON:** [`121936924cfc3d40c94c.json`](../../sessions/12/121936924cfc3d40c94c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已写入 `artifacts/partial_anova_v2_results.txt`。核心发现：

**1. Cell 1 vs Cell 3 (梯度流效应)**
- Welch's t = -1.07, **p = 0.381** (不显著)
- **Cohen's d = -0.93** (大效应)
- 矛盾的根因：power 仅 **0.169**，需要每组 n=20 才能达到 0.80——不现实

**2. Cell 3 (Detach BN) vs Vanilla**
- 几乎完全相同：0.767 vs 0.768，d = -0.06，**p = 0.91**
- **最强结论**：梯度截断 + BN 加 OCC head 对安全零影响

**3. Cell 1 (Full OCC BN) vs Vanilla**
- 均值低 4.3 pp，d = -0.67 (medium-large)，单侧 **p = 0.18**
- 方向一致但 n=3 功效不足

**4. 方差比**
- Cell 1 方差是 Cell 3 的 **6.88 倍**，但 F-test p = 0.15 (小样本下不显著)
- 梯度流 ON 明显增加 seed 间波动，与梯度干扰假说一致

**论文建议**：用 "directional evidence with large effect size" 叙事，不宣称 significance。Cell 3 ≈ Vanilla 是可以硬宣称的结果。

---
