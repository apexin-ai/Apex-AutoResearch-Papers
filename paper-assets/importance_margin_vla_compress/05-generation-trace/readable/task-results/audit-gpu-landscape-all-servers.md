# audit gpu landscape all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu-landscape-all-servers_20260524T023040_result.json`
- **Structured JSON:** [`9856e3d6b24301b06a22.json`](../../sessions/98/9856e3d6b24301b06a22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册为 artifact。

总结：14 块 GPU 中 11 块在跑实验，**3 块空闲**（westd-38929 GPU2/3 各 98GB，cqa1-33015 GPU3 24GB）。orphan `eval_pi05_l2norm_k07_goal_seed43_v2` 已注册为 RUNNING；`eval_openvla_l2norm_k05_goal_seed42_v2` registry 标记 DONE 但进程仍活跃（PID 486402），状态机不允许回退，建议等其自然完成后由 cron 更新。3 个已完成实验待收割结果。

---
