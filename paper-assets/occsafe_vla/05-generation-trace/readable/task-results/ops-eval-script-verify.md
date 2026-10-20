# ops eval script verify

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-script-verify_20260526T150634_result.json`
- **Structured JSON:** [`fd9d4453b0340a64a7f5.json`](../../sessions/fd/fd9d4453b0340a64a7f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器全部就绪。

## Eval 就绪报告

| 检查项 | westd-34685 | westd-10894 |
|--------|:-----------:|:-----------:|
| eval 脚本存在 | ✓ | ✓ |
| conda env `occsafe` + torch 2.11.0+cu128 | ✓ | ✓ |
| mujoco + libero 可导入 | ✓ | ✓ |
| draccus + robosuite 可导入 | ✓ (robosuite warning 可忽略) | ✓ (同) |
| LIBERO bddl_files (含 libero_spatial) | ✓ | ✓ |
| LIBERO init_files (含 libero_spatial) | ✓ | ✓ |
| LIBERO config.yaml 路径正确 | ✓ | ✓ |

**结论：两台服务器 eval 环境均已就绪，训练完成后可直接运行。**

唯一差异：westd-10894 的 `datasets` 路径指向包内默认位置（`../datasets`），而 westd-34685 的指向 `/root/autodl-tmp/libero_datasets`。这不影响 eval（eval 不读 datasets，只用 bddl_files 和 init_states）。

---
