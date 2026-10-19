# eval analyze 24k v2 results

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_analyze_24k_v2_results_20260527T065513_result.json`
- **Structured JSON:** [`0b10d654a622110c573f.json`](../../sessions/0b/0b10d654a622110c573f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**eval_stepwise_s0_l1_24k_v2 结果（含 --pi05 ✓）：**

| Task | TSR | CAR |
|------|-----|-----|
| orange_juice | 30% | 54% |
| chocolate_pudding | 78% | 72% |
| milk | 30% | 64% |
| bbq_sauce | 64% | 20% |
| **Overall** | **50.5%** | **52.5%** |

- frozen=0%（全 4 task 均为 0），dfCAR=52.5%（= raw CAR）
- 确认原 24K frozen=29.5% 纯属缺 --pi05 的 artifact

**完整 seed0 learning curve 现在是：** 16K=55.5 → 20K=55 → 22K=60.5 → **24K=52.5** → 26K=53.5

CAR 在 52.5-60.5% 区间波动，围绕 LoRA baseline (54.5%) 持平。Scenario B (redundant) 进一步确认，无任何 collapse 迹象。

Registry 已更新：status=DONE, conclusion=negative, metrics 已记录。Memory.md 24K 数据点已补入，GPU cuda:0 标为空闲。

---
