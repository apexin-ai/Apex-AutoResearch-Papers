# code oracle refine flag

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_oracle_refine_flag_20260522T144301_result.json`
- **Structured JSON:** [`a9c0b95dc54353024556.json`](../../sessions/a9/a9c0b95dc54353024556.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，6 处 `force_refine` 引用位置正确：

| 行号 | 修改 |
|------|------|
| 293 | 函数签名添加 `force_refine=False` |
| 327 | 条件改为 `if (force_refine or sdf_scalar < refine_margin)` |
| 339 | force_refine 时打印 debug 日志 |
| 383 | argparse 添加 `--force_refine` |
| 764 | 调用处传入 `force_refine=args.force_refine` |
| 1034 | 输出 JSON config 记录 `force_refine` |

关于 `--refine_margin 10.0` 方案：由于条件是 `sdf_scalar < refine_margin`，设 margin=10 确实等价于 force_refine（SDF 值通常远小于 10），两种方式都可以用于 oracle 实验。

---
