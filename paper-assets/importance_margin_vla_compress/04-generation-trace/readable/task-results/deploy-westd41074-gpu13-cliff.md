# deploy westd41074 gpu13 cliff

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu13_cliff_20260526T075148_result.json`
- **Structured JSON:** [`133153b0ee632f0ccde3.json`](../../sessions/13/133153b0ee632f0ccde3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇报：

## 部署结果

| 实验 | GPU | tmux 会话 | Token Pruning | 状态 |
|------|-----|-----------|---------------|------|
| `eval_openvla_l2norm_k085_object_seed42` | cuda:1 (15980 MiB) | `eval_k085_obj` | 256→217 tokens (k=0.85) | RUNNING，Task 1/10 已开始 |
| `eval_openvla_l2norm_k095_object_seed42` | cuda:3 (15980 MiB) | `eval_k095_obj` | 256→243 tokens (k=0.95) | RUNNING，Task 1/10 已开始 |

- 服务器: westd-41074
- 10 tasks × 50 episodes = 500 episodes/实验
- 预估完成时间: ~4-5 小时（约 11:50-12:50 UTC）
- 日志路径: `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_l2norm_k0{85,95}_object_seed42.log`

---
