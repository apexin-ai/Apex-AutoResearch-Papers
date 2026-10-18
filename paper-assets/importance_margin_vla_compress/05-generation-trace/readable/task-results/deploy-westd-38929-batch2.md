# deploy westd 38929 batch2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-38929-batch2_20260523T152138_result.json`
- **Structured JSON:** [`4800e2e29be92ef67f43.json`](../../sessions/48/4800e2e29be92ef67f43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-38929 方案 B 部署完成。汇总：

| GPU | exp_id | 模型 | 方法 | Suite | tmux session |
|-----|--------|------|------|-------|-------------|
| 0 | `eval_pi05_random_k0925_goal_seed42_w38` | π0.5 | Random k=0.925 | libero_goal | 同名 |
| 1 | `eval_pi05_l2norm_k0925_goal_seed42_w38` | π0.5 | L2norm k=0.925 | libero_goal | 同名 |
| 2 | `eval_e5_xvla_attn_last_goal_k03` | X-VLA | attention_last k=0.3 | libero_goal | 同名 |
| 3 | `eval_e5_xvla_attn_mean_goal_k03` | X-VLA | attention_mean k=0.3 | libero_goal | 同名 |

- OpenVLA Goal/Long 模型不存在，走了方案 B
- 4 个 tmux session 均已启动，registry 状态已更新为 RUNNING
- X-VLA attn_last 已开始 Task 0 评估，π0.5 正在加载模型
- 日志路径：`/root/autodl-tmp/logs/&lt;exp_id>.log`

---
