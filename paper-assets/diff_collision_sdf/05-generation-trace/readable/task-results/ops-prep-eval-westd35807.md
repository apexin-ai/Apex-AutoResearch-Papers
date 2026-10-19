# ops prep eval westd35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_eval_westd35807_20260523T004307_result.json`
- **Structured JSON:** [`71cc7efaa38a0456e6d4.json`](../../sessions/71/71cc7efaa38a0456e6d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/eval_readiness_westd35807.md`。

**检查结果汇总**：

| 检查项 | 状态 |
|--------|------|
| 项目代码 | ✅ `/root/colliforce-vla` |
| eval 脚本 | ⚠️ 存在但缺少增强 metric |
| 测试数据 (safelibero_object) | ✅ |
| Pi0.5 base checkpoint | ✅ 6.7GB |
| 训练 checkpoint | ⏳ 4个目录已建，文件尚未生成 |
| GPU | ✅ 4x RTX PRO 6000 全部训练中 |
| 依赖 (openpi_client, libero) | ✅ 在 libero conda env 中 |

**P0 阻塞项**：`eval_pi05_safelibero.py` 缺少 `robot_total_displacement`、`min_ee_obstacle_distance`、`is_frozen/frozen_rate`、pass/fail gate (CAR≥33% + TSR≥50%)。需下一个 worker 修复后才能执行有效的 D012 eval。

---
