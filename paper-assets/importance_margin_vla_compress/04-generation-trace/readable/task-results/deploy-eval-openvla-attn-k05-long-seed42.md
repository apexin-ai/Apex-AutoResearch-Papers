# deploy eval openvla attn k05 long seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_openvla_attn_k05_long_seed42_20260526T154428_result.json`
- **Structured JSON:** [`3ace07d9558d8c101ece.json`](../../sessions/3a/3ace07d9558d8c101ece.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 正在运行活跃实验，Task 3/10 Ep 20/50，预计还需 ~3 小时完成。

**状态汇报：**

```
DEPLOYED: no
MODEL_MISSING: false
MODEL_PATH: /root/autodl-tmp/openvla-7b-finetuned-libero-10
```

**阻塞原因：** cuda:1 被 `eval_openvla_random_k05_goal_seed42` 占用（PID 357375, 15946 MiB），当前进度 Task 3/10，~2 eps/min，预计还需约 3 小时。

cuda:0 同样被占用（PID 307307, 15946 MiB）。

**选项：**
1. Kill PID 357375 释放 cuda:1 立即部署（goal random k=0.5 数据会丢失）
2. 等 goal 实验跑完后再部署
3. 换其他服务器

需要你决定。

---
