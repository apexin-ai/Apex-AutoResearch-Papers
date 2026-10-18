# deploy eval openvla random k085 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_openvla_random_k085_object_seed42_20260526T132041_result.json`
- **Structured JSON:** [`f2b3889cab39504c583f.json`](../../sessions/f2/f2b3889cab39504c583f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:3 被占用，无法部署。**

当前 cuda:3 上正在运行的进程：

| 字段 | 值 |
|---|---|
| PID | 642262 |
| 已运行 | ~8 分钟 |
| 显存占用 | 15470 MiB |
| 命令 | `eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_object --seed 42` |

这是 L2norm k=0.75 Object seed42 的评测任务。实际上 4 张卡全部被占用（每张 ~16GB）。

其他已确认信息：
- 模型路径：`/root/autodl-tmp/openvla-libero-object`（短名称，已验证存在）
- 评测脚本：已验证存在

需要等当前任务完成后再部署，或者指定其他服务器/GPU。

---
