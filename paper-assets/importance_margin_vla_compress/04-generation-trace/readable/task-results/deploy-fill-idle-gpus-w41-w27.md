# deploy fill idle gpus w41 w27

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_fill_idle_gpus_w41_w27_20260527T095633_result.json`
- **Structured JSON:** [`b04381a506c77a38fa6c.json`](../../sessions/b0/b04381a506c77a38fa6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个部署均无法执行，跳过。**

| GPU | 实验 | 状态 |
|-----|------|------|
| westd-41074:cuda:3 | eval_openvla_attn_k05_goal_seed42_v4 | **跳过** — models 目录为空，`openvla-7b-finetuned-libero-goal` 不存在 |
| westd-27271:cuda:0 | eval_openvla_l2norm_k095_long_seed42_w27 | **跳过** — `/root/autodl-tmp/models/` 目录不存在，`openvla-7b-finetuned-libero-10` 缺失 |

两台服务器上 eval 脚本都在，但所需的 finetuned 模型权重均未部署。按指示不下载模型（没时间），两个备份实验取消。主实验仍在原服务器运行，需确保 cqa1:cuda:3 (Goal Attn k=0.5 v3) 和 westd-38929:cuda:1 (L2norm k=0.95 Long) 顺利完成。

---
