# paper figure fig6 regenerate real data

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig6-regenerate-real-data_20260518T210803_result.json`
- **Structured JSON:** [`ff7c3923498e32d56fef.json`](../../sessions/ff/ff7c3923498e32d56fef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成，输出到 `figures/paper/fig6_training_curves.pdf` 和 `.png`。

**数据来源与字段：**
- **Cell A** (run 7o9bjszm, hsweep-h2-seed1): `train/AlfworldSG/success` + `train/AlfworldSG/action_is_effective`, 14 步 (steps 1-14)
- **Cell B** (run 6liw7fm1, factorial-h2-episode-adv): 同上字段, 14 步 (steps 1-14)
- **Cell C** (run 7a59sudo, exp029 episode-level): 同上字段, 15 步 (steps 1-15)；val 用 `val-env/AlfworldSG/success`, 4 个点 (steps 0, 5, 10, 15)

**故事线清晰可见：**
- Cell A (橙红): train success 从 ~19% 迅速 collapse 到 0%，action validity 同步崩溃
- Cell B (黄色): train success 在 0-20% 间震荡，action validity 维持 ~80-98%
- Cell C (蓝色): train success 持续上升至 ~44%，action validity 稳定在 93-99%，val 从 12.5% 稳步上升到 28.1%

---
