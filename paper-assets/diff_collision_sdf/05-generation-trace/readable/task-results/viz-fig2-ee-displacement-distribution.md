# viz fig2 ee displacement distribution

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig2_ee_displacement_distribution_20260526T132558_result.json`
- **Structured JSON:** [`87baff156c65a6544824.json`](../../sessions/87/87baff156c65a6544824.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Fig 2 完成。

**输出文件**：
- PDF: `artifacts/figures/fig2_ee_displacement_distribution.pdf`
- PNG: `artifacts/figures/fig2_ee_displacement_distribution.png`
- 绘图脚本: `artifacts/figures/plot_fig2.py`

**数据摘要**（200 episodes/model）：
| 模型 | μ (m) | 范围 (m) |
|------|-------|----------|
| Pi0.5 Baseline | 0.367 | 0.27–0.46 |
| LoRA-only s1 | 0.388 | 0.29–0.82 |
| SDF λ=0.005 s0 | 0.386 | 0.30–0.64 |
| SDF λ=0.01 s0 | 0.395 | 0.31–0.87 |

所有 800 个 episode 的 max EE displacement 均在 0.27–0.87m，远高于 frozen threshold τ\_d=0.1mm（~3000× gap），确认无 action collapse。

---
