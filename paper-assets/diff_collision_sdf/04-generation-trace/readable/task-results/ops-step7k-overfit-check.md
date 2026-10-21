# ops step7k overfit check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_step7k_overfit_check_20260523T095945_result.json`
- **Structured JSON:** [`18d0ab84a892da7a70cd.json`](../../sessions/18/18d0ab84a892da7a70cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕，报告已写入 `artifacts/step7k_overfit_check.md`。核心发现：

**训练状态**：6/6 全部正常运行，GPU 满载 ~27GB。s0 已到 step ~11230 (37%)，s1/s2 在 step ~8700 (29%)。

**Overfit 警告**：
- s0 的 action_loss 均值已降至 **0.0176-0.0179**，低于 0.02 警戒线
- s1/s2 在 0.020 边界，预计 step ~11000 也会进入 < 0.02 区域

**Lambda 区分度**：**完全没有**。l005 vs l01 的 action_loss 差异 < 2%，全部在噪声范围内。lambda=0.05 和 0.1 对 action 学习无影响。

**grad_norm**：稳定在 0.09-0.10，无突变，但高于预期的 0.04-0.05。

**异常**：s2_l01 的 SDF loss (~0.067) 是其他 run (~0.034) 的 2 倍。

---
