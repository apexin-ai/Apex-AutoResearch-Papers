# ops mid eval d012 step10k

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mid_eval_d012_step10k_20260523T102039_result.json`
- **Structured JSON:** [`08a4511a7206cb4e2040.json`](../../sessions/08/08a4511a7206cb4e2040.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

serve_policy 已 kill，显存恢复到仅训练占用 27GB/GPU。

## D012 Mid-Eval Results (Step 10K)

### s0_l005 (λ=0.005, step 10000)
- **TSR: 47%**
- **CAR: 58%**
- **frozen_rate: 0%**
- **D012 Gate: FAIL** (TSR 47% < 50% 阈值)

### s0_l01 (λ=0.01, step 10000)
- **TSR: 49%**
- **CAR: 56.5%**
- **frozen_rate: 0%**
- **D012 Gate: FAIL** (TSR 49% < 50% 阈值)

### Per-Task Breakdown

| Task | s0_l005 TSR | s0_l005 CAR | s0_l01 TSR | s0_l01 CAR |
|------|-------------|-------------|------------|------------|
| 0: orange juice → basket | 18% | 62% | 26% | 56% |
| 1: chocolate pudding → basket | 70% | 72% | 72% | 70% |
| 2: salad dressing → basket | 40% | 72% | 46% | 72% |
| 3: bbq sauce → basket | 60% | 26% | 52% | 28% |

### Lambda 对比
- **TSR**: λ=0.01 (49%) 略优于 λ=0.005 (47%)，差距很小
- **CAR**: λ=0.005 (58%) 略优于 λ=0.01 (56.5%)，差距也很小
- **Task 0**: λ=0.01 明显更好 (TSR 26% vs 18%)
- **Task 3**: λ=0.005 明显更好 (TSR 60% vs 52%)，但 CAR 都很差 (26-28%)
- **Task 1/2**: 两者 CAR 一致 (70-72%)，TSR 接近

### 初步结论
- 两个 lambda 的整体表现非常接近，无显著差异
- **CAR 通过了 33% 阈值**（58%/56.5%），说明 SDF 对 collision avoidance 有明显效果
- **TSR 差 1-3% 未过 50% 阈值**，主要被 Task 0 拖累（TSR 仅 18-26%）
- **Task 3 的 CAR 异常低 (26-28%)**，与其他 task 的 70%+ 形成鲜明对比
- frozen_rate 为 0%，模型没有出现冻住现象
- Step 10K 是中间 checkpoint，训练到 30K 步后 TSR 有望继续提升

---
