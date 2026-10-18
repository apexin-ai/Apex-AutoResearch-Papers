# deploy westd38929 gpu3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_gpu3_20260527T115826_result.json`
- **Structured JSON:** [`04b172429bbe82a09f84.json`](../../sessions/04/04b172429bbe82a09f84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已启动，正在加载 π0.5 模型。π0.5 模型加载需要几分钟，之后 GPU 显存会上升。

**部署完成：**

| 项目 | 值 |
|------|-----|
| exp_id | `eval_pi05_l2norm_k05_long_seed42_strict` |
| 服务器 | westd-38929, GPU3 (cuda:3) |
| tmux session | `pi05_l2norm_k05_strict` |
| 日志 | `/root/autodl-tmp/importance_margin_vla_compress/logs/pi05_l2norm_k05_long_strict.log` |
| 预计耗时 | ~3h（π0.5 实验） |
| Registry 状态 | RUNNING |

westd-38929 现在 4 GPU 全部在用：GPU0=OV_random_k095_long, GPU1=OV_l2norm_k095_long, GPU2=OV_l2norm_k075_long_v2, GPU3=PI05_l2norm_k05_strict。

---
