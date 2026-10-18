# audit cqa1 gpu status 20260526b

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1-gpu-status-20260526b_20260526T182543_result.json`
- **Structured JSON:** [`aabf9993903859a360a4.json`](../../sessions/aa/aabf9993903859a360a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

```
GPU 0: [空闲] PID 199389 已死亡（/proc 不存在）
       实验=eval_pi05_l2norm_k075_long_seed42_v3
       状态：日志停在 Task 5 开始 (09:08 May 26)，无 RESULT 行，无 exit file
       → 已崩溃或被杀

GPU 1: [空闲] eval_pi05_attention_k07_long_seed42 启动失败
       EXIT_CODE=127: "python: command not found"
       原因：job 脚本用了 bare `python` 而非 `/root/miniconda3/bin/python`
       → 需要修复后重新提交

GPU 2: [运行中] PID=582964, 显存 10225/24564 MiB, GPU利用率 31%
       实验=attention k=0.5 libero_10 seed42（第二次运行）
       第一次运行已完成：SR=49.8% (22:37 May 26)
       当前进程 01:36 May 27 启动，在同一 tmux session 中
       → 注意：这是重复运行，第一次结果已保存

GPU 3: [运行中] PID=546287, 显存 10409/24564 MiB, GPU利用率 59%
       实验=eval_pi05_attn_k095_long_seed42（attention k=0.95 libero_10 seed42）
       进度：Task 5 进行中，当前累计 SR≈90.4% (226/250)
       ⚠️ 注意：这不是 l2norm_k05_spatial_seed42_postfix，而是 attention k=0.95
```

**关键发现**：
1. **GPU 1 失败**：`python` 命令找不到，需用 `/root/miniconda3/bin/python` 重新提交
2. **GPU 0 已死**：l2norm k=0.75 v3 在 Task 5 处中断，无最终结果
3. **GPU 2 重复跑**：attn k=0.5 第一次已完成 (SR=49.8%)，当前是第二次运行
4. **GPU 3 实际实验与预期不符**：跑的是 attn k=0.95 而非 l2norm k=0.5 spatial

---
