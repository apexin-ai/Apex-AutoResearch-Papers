# harvest bjb1 32546 vla only results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546-vla-only-results_20260524T205956_result.json`
- **Structured JSON:** [`987e5b5802cb01f5cf7f.json`](../../sessions/98/987e5b5802cb01f5cf7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### bjb1-32546 — VLA-only 实验（全部仍在运行）

启动时间 ~04:18，已运行 ~46 分钟，每个 benchmark 10 个 task：

| 实验 | 完成 task | 当前进度 | 已完成 task 的 SR |
|------|----------|---------|-----------------|
| obj-s42 | 3/10 | task 4 starting | 81.7% (49/60) |
| obj-s43 | 3/10 | task 4 starting | 71.7% (43/60) |
| obj-s44 | 3/10 | task 4 starting | 71.7% (43/60) |
| goal-s42 | 3/10 | task 4, 15/20 rollouts | 91.7% (55/60) |
| long-s43 | 1/10 | task 2, 5/20 rollouts | 20.0% (4/20) |

已完成的 task 明细：
- **obj-s42**: alphabet_soup 85%, cream_cheese 75%, salad_dressing 85%
- **obj-s43**: alphabet_soup 70%, cream_cheese 70%, salad_dressing 75%
- **obj-s44**: alphabet_soup 70%, cream_cheese 70%, salad_dressing 75%
- **goal-s42**: middle_drawer 85%, bowl_on_stove 100%, wine_bottle 90%
- **long-s43**: alphabet_soup_tomato 20%

**预计剩余时间**：~15 min/task → obj/goal 约 1.5-2h，long 更久（长 horizon task 慢）

**GPU 1：完全空闲**（0%, 2 MiB）

---

### bjb2-40593 — K=5 spatial s42（即将完成）

9/10 tasks 已完成，第 10 个 task 在跑（15/20 rollouts）。约 10-15 min 完成。

| Task | SR |
|------|-----|
| bowl_between_plate_and_ramekin | 95.0% (19/20) |
| bowl_next_to_ramekin | 90.0% (18/20) |
| bowl_from_table_center | 100.0% (20/20) |
| bowl_on_cookie_box | 100.0% (20/20) |
| bowl_in_top_drawer | 65.0% (13/20) |
| bowl_on_ramekin | 0.0% (0/20) |
| bowl_next_to_cookie_box | 95.0% (19/20) |
| bowl_on_stove | 80.0% (16/20) |
| bowl_next_to_plate | 85.0% (17/20) |
| bowl_on_wooden_cabinet | *running* |

9-task 平均 SR = **78.9%** (142/180)

---

**结论**：全部实验仍在运行，无可收割结果。bjb2 K=5 spatial 最快完成（~15min），bjb1 的 5 个 VLA-only 还需 1.5-2+ 小时。

---
