# paper figure generation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure-generation_20260516T195628_result.json`
- **Structured JSON:** [`7907993870e3cecc1594.json`](../../sessions/79/7907993870e3cecc1594.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个文件全部生成成功：

| 文件 | 路径 | 大小 |
|------|------|------|
| NVE 轨迹 (PDF) | `/root/autodl-tmp/event-gated-adaptive-horizon/figures/fig_nve_trajectories.pdf` | 22K |
| NVE 轨迹 (PNG) | `/root/autodl-tmp/event-gated-adaptive-horizon/figures/fig_nve_trajectories.png` | 277K |
| 梯度分解 (PDF) | `/root/autodl-tmp/event-gated-adaptive-horizon/figures/fig_gradient_decomposition.pdf` | 42K |
| 梯度分解 (PNG) | `/root/autodl-tmp/event-gated-adaptive-horizon/figures/fig_gradient_decomposition.png` | 202K |

**图 1 (NVE Trajectories)**: 5 条实验曲线（008d/008f/018v2/009b/010b），NVE=1.5 诊断阈值线，35K 诊断窗口标注，008d 55K collapse 和 010b 65K spike 箭头标注。

**图 2 (Gradient Decomposition)**: 左 panel 008d 无 SGS（obs 从 26%→93% 爆炸），右 panel 018v2 Full SGS 反事实（obs 温和增长 12%→24%，KL 保持主导），底部注释实际训练中 100% KL。

生成脚本保留在 `figures/gen_figures.py`，可随时调参重跑。

---
