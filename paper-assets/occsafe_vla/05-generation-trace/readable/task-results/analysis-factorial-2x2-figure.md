# analysis factorial 2x2 figure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_factorial_2x2_figure_20260525T084747_result.json`
- **Structured JSON:** [`8d966d8500de364eb34b.json`](../../sessions/8d/8d966d8500de364eb34b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 注册工具不可用，跳过。

### 结果

**文件路径：**
- `/root/occsafe_vla/artifacts/factorial_2x2_bar.pdf` (22K)
- `/root/occsafe_vla/artifacts/factorial_2x2_bar.png` (95K)
- `/root/autodl-tmp/analysis/factorial_2x2_bar.pdf`
- `/root/autodl-tmp/analysis/factorial_2x2_bar.png`

**视觉确认：**
- 4 根柱子分别对应 BN+Flow (深蓝, 0.797)、BN−Flow (浅蓝, 0.746)、LN+Flow (深红, 0.743)、LN−Flow (浅红, 0.765)
- 误差棒 (SE) 正确显示，BN+Flow 的 SE 最大（seed 方差较大）
- Vanilla baseline 灰色虚线在 0.780 处
- 蓝色双向箭头标注 BN 的 +5.1pp gradient flow 增益
- 红色双向箭头标注 LN 的 −2.2pp gradient flow 损害
- 右下角标注 Interaction: p=0.025, η²=0.484
- 交互效应的交叉模式清晰可见：BN 受益于 gradient flow，LN 反而受损

---
