# ops plan003 to eval scalar unc

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan003-to-eval-scalar-unc_20260513T235456_result.json`
- **Structured JSON:** [`638466a4ca245965e19b.json`](../../sessions/63/638466a4ca245965e19b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

evaluate.py 已修复完成（4处改动），等待训练完成后立即启动 eval。

**已完成的准备工作：**
- 修复 `unc_dim = 3 * H_EFF` → `unc_dim = 3`（匹配训练时的 scalar_unc 配置）
- 添加 `_to_scalar_uf()` 函数（40D CGS → 3D 压缩）
- `select_action_crm` 增加 `mode` 参数，`crm_scalar` 模式自动压缩
- 调用处传递 `args.mode`

90秒后回来检查训练是否完成。

---
