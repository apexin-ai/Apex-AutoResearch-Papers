# figure fig6 training curves

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig6-training-curves_20260517T205023_result.json`
- **Structured JSON:** [`ee17a4b03d0555495193.json`](../../sessions/ee/ee17a4b03d0555495193.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件无法下载到本地预览，但根据文件大小（PDF: 18KB, PNG: 129KB）和无报错的生成过程，图表已正确产出。

---

**产出文件:**
- `/root/cost-verify-agent-rl/artifacts/figures/fig6_training_curves.pdf`
- `/root/cost-verify-agent-rl/artifacts/figures/fig6_training_curves.png`

**使用的数据数值表:**

| Step | exp029 (Episode-level) Success % | exp029 Action Valid % | hsweep_h2_seed1 (Step-indep.) Success % | hsweep_h2_seed1 Action Valid % |
|------|------|------|------|------|
| 0 | 12.5 | 78.3 | 0.0 | 88.1 |
| 5 | 25.0 | 70.4 | 3.125 | 20.5 |
| 10 | 25.0 | 60.2 | 0.0 | 0.5 |
| 15 | 28.125 | 54.5 | 0.0 | 0.06 |

**注意:** 实际数据与 Director 描述不同。hsweep_h2_seed1 的 action_valid 不是"从 ~80% 升至 99.9%"，而是从 88.1% 崩溃到 0.06%。这是更极端的退化模式：step-independent 训练导致模型连有效动作都无法生成（完全策略崩溃），而 episode-level 训练保持稳定学习。

**图表布局:** 2×1 subplot，共享 X 轴。上图为 Val Success Rate，下图为 Action Validity。蓝色圆点实线 = episode-level，红色三角实线 = step-independent。Serif 字体，无标题，300 dpi。

---
