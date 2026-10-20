# viz tau sensitivity curve

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_tau_sensitivity_curve_20260515T200839_result.json`
- **Structured JSON:** [`678a85e1cc5c07067ea0.json`](../../sessions/67/678a85e1cc5c07067ea0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完成。

**产出文件：**

| 文件 | 路径 | 大小 |
|------|------|------|
| PDF | `/root/provenance_weight_training/output/figures/tau_sensitivity.pdf` | 29 KB |
| PNG | `/root/provenance_weight_training/output/figures/tau_sensitivity.png` | 203 KB |

图表内容：
- 左轴（蓝色实线圆点）：Held-out PPL vs τ，τ=0.8 处 PPL 最低 (17.6527)，星号标注
- 右轴（红色虚线方块）：Mean b* vs τ，τ=0.8 处同样星号标注
- 灰色水平虚线：Uniform baseline PPL=17.6939
- 浅蓝色阴影：Safe range [0.5, 0.8]
- 绘图脚本：`/root/provenance_weight_training/output/figures/plot_tau_sensitivity_v2.py`

---
