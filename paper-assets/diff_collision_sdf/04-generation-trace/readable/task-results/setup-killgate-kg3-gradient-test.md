# setup killgate kg3 gradient test

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_killgate_kg3_gradient_test_20260519T163131_result.json`
- **Structured JSON:** [`330b0ca1f15a7f2df811.json`](../../sessions/33/330b0ca1f15a7f2df811.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**KG-3: PASS**

5 个配置全部通过，核心结论：

- **梯度稳定**：无 NaN/explode/vanish，所有配置下 action 梯度范数在 0.016–0.98 范围内
- **方向正确**：有限差分验证确认沿梯度负方向移动 action 可降低 collision cost
- **逐层传播通畅**：梯度从 SDF decoder layer4 → layer1 → ActionProjection → action tokens 无断层
- **Eikonal |∇SDF| ≈ 0.12–0.15**（随机初始化下偏低，训练后会收敛到 ~1.0，不影响结论）

脚本和报告已写入 `artifacts/`。

---
