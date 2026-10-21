# paper figure fig6 training curves

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig6_training_curves_20260518T204247_result.json`
- **Structured JSON:** [`d86f298d70457eb1f36e.json`](../../sessions/d8/d86f298d70457eb1f36e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册。

**输出文件:**
- PDF: `figures/paper/fig6_training_curves.pdf` (24 KB)
- PNG: `figures/paper/fig6_training_curves.png` (310 KB)
- 生成脚本: `figures/paper/gen_fig6_training_curves.py`

**数据来源:**
- Cell A seed1 (7o9bjszm), Cell B (6liw7fm1), Cell A seed2 (jhwyg4tc): 完整 step-by-step 数据来自 W&B
- Cell D (6d4oml60): W&B 仅返回 1 个数据点，使用 registry 的 4 个关键点 (step 0/1/5/15) + PCHIP 插值

**Panel (a)** 展示 train success rate: seed1 在 step 3→4 崩溃至 0%, Cell B 在 3-26% 间剧烈振荡, Cell D 从 12.5% 稳步升至 28%。**Panel (b)** 展示 action validity: seed1 从 97% 崩至 ~3% (action_is_effective), 而 Cell B 保持 82-98%, Cell D 保持 95-99%。

---
