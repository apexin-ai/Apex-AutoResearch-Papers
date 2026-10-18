# analysis smolvla entropy perlayer fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_smolvla_entropy_perlayer_fix_20260518T071428_result.json`
- **Structured JSON:** [`d891fa6e78a366348976.json`](../../sessions/d8/d891fa6e78a366348976.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果：

## 采样验证
- 10 个 LIBERO-Object task 全部覆盖，每个 task 26 帧，共 260 帧
- task 20-29 逐一确认（orange juice, ketchup, cream cheese, bbq sauce, alphabet soup, milk, salad dressing, butter, tomato sauce, chocolate pudding）

## 结果对比

| 指标 | 旧（bug, task 0-8） | 新（LIBERO-Object, task 20-29） |
|---|---|---|
| **Overall entropy ratio** | 0.944 | **0.9521** |

差异仅 +0.008，**结论不变**：SmolVLA 的 vision attention entropy 在 LIBERO-Object 上仍然很高（~0.95），注意力分布接近均匀。

## Per-layer breakdown（新结果）

| Layer | Entropy | Vis Frac |
|-------|---------|----------|
| L0  | 0.9826 | 0.5951 |
| L1  | 0.9561 | 0.6693 |
| L2  | 0.9597 | 0.5137 |
| L3  | 0.9434 | 0.6170 |
| L4  | 0.9408 | 0.4429 |
| L5  | 0.9406 | 0.5684 |
| L6  | 0.9474 | 0.4555 |
| L7  | 0.9628 | 0.5861 |
| L8  | 0.9614 | 0.4748 |
| L9  | 0.9572 | 0.5875 |
| L10 | 0.9455 | 0.4638 |
| L11 | 0.9510 | 0.6060 |
| L12 | 0.9485 | 0.4877 |
| L13 | 0.9311 | 0.5935 |
| L14 | 0.9482 | 0.5264 |
| L15 | 0.9566 | 0.6703 |

所有 layer entropy 都在 0.93-0.98 范围，L13 最低（0.9311）。论文中的 claim 无需更新。结果已保存至 `eval_results/smolvla_attention_entropy_perlayer_fixed.json`。

---
