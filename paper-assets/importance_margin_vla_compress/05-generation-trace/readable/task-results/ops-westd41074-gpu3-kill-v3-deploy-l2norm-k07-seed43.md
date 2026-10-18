# ops westd41074 gpu3 kill v3 deploy l2norm k07 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-gpu3-kill-v3-deploy-l2norm-k07-seed43_20260521T112822_result.json`
- **Structured JSON:** [`af68a01fc2669683da65.json`](../../sessions/af/af68a01fc2669683da65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**Step 1**: PID 190611 (π0.5 random k=0.7 v3) 已杀掉，registry 更新为 DONE/killed。

**Step 2**: π0.5 L2norm k=0.7 seed43 已部署，PID **209861**。

**Step 3**: Registry 已更新：
- `eval_pi05_l2norm_k07_object_seed43`: RUNNING, parent=eval_pi05_l2norm_k07_object_seed42
- `eval_pi05_random_k07_object_seed42`: 已确认 DONE/success, SR=77.2%

**Step 4 验证**: GPU3 (UUID 5de49e5a) 上两个进程共存：
- PID 59671 — M64v6 训练, 27464 MiB
- PID 209861 — eval_pi05_l2norm_k07_object_seed43, 9700 MiB

日志显示已完成模型加载、pruning，进入 libero_object 评估（10 tasks, 50 episodes each）。

---
