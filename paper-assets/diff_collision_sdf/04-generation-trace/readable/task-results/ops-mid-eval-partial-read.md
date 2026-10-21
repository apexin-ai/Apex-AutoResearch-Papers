# ops mid eval partial read

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mid_eval_partial_read_20260523T112534_result.json`
- **Structured JSON:** [`62db1399ce73eb82035f.json`](../../sessions/62/62db1399ce73eb82035f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在 Task 0，各完成 18/50 episodes（18/200 总进度）。解析结果如下：

## Mid-Eval Partial Results (Step 10K)

### 数据量
- s0_l005: 18/200 episodes 完成（Task 0: 18/50）
- s0_l01: 18/200 episodes 完成（Task 0: 18/50）
- 速度：~2.1 min/episode，预计剩余 ~6.4h

### s0_l005 (λ=0.005) — PARTIAL 18/200 (Task 0 only)
- **TSR: 11.1%** (2/18 success)
- **CAR: 72.2%** (13/18 collision-free)
- **frozen_rate: 0%** (最低 ee_disp=0.6001，无 frozen)
- Collisions: 5 episodes (yellow_book×2, moka_pot×2, wine_bottle×1)

### s0_l01 (λ=0.01) — PARTIAL 18/200 (Task 0 only)
- **TSR: 22.2%** (4/18 success)
- **CAR: 55.6%** (10/18 collision-free)
- **frozen_rate: 0%** (最低 ee_disp=0.9154，无 frozen)
- Collisions: 8 episodes (moka_pot×2, yellow_book×2, wine_bottle×2, red_coffee_mug×2)

### D012 Gate 初步判断（PARTIAL — 仅 Task 0, 样本量极小）

| 指标 | s0_l005 | s0_l01 | baseline |
|------|---------|--------|----------|
| TSR | 11.1% | 22.2% | — |
| CAR | 72.2% | 55.6% | 26.8% |
| frozen | 0% | 0% | — |

- **CAR vs baseline 26.8%**: 两个 λ 都显著高于 baseline（72.2% / 55.6% vs 26.8%），**强 positive 信号**
- **TSR**: l01(22.2%) > l005(11.1%)，λ 更大 TSR 更高但碰撞也更多——符合安全-性能 tradeoff 预期
- **frozen_rate**: 0%，模型没有出现冻结行为
- **信号方向: positive**——CAR 大幅提升，且未牺牲为 frozen

**注意**: 仅 Task 0 的 18 个 episode，4 个 task 中只跑了 1 个，置信度很低。l005 的 CAR 优势特别明显（72% vs 56%），且 TSR 的差距可能随更多 task 收窄。建议等至少完成 Task 0 全部 50 episodes 后再做判断。

---
