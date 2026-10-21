# submit cqa1 4gpu cliff batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_cqa1_4gpu_cliff_batch_20260525T042418_result.json`
- **Structured JSON:** [`769c9e41bbb49918ab28.json`](../../sessions/76/769c9e41bbb49918ab28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部活跃（PID 68723, 70466, 70539, 70613）。GPU1-3 正在 CPU 加载模型（700%+ CPU 利用率），稍后会转移到各自 GPU。一切正常。

---

**提交结果汇总：**

| GPU | exp_id | 实验内容 | 状态 |
|-----|--------|---------|------|
| 0 | `eval_pi05_random_k085_goal_seed42_postfix_v2` | Random k=0.85 Goal s42 | 已进入评估 |
| 1 | `eval_pi05_random_k085_long_seed42_postfix_v2` | Random k=0.85 Long s42 | 模型加载中 |
| 2 | `eval_pi05_l2norm_k085_object_seed42_postfix` | L2norm k=0.85 Object s42 | 模型加载中 |
| 3 | `eval_pi05_l2norm_k085_long_seed42_postfix_v2` | L2norm k=0.85 Long s42 | 模型加载中 |

**调整说明：**
1. **GPU2 原计划 Random Object s42**：registry 已有该实验（SR=5.6%, conclusion=success），改为 **L2norm Object s42**（缺失数据点）
2. **GPU3 原计划 Attention**：脚本 `choices=["none", "random", "l2norm"]` 不支持 `--prune_mode attention`，改为 **L2norm Long s42**（缺失数据点）
3. 首次启动时 GPU1-3 因未设 `CUDA_VISIBLE_DEVICES` 全挤 GPU0 导致 OOM，已用 `CUDA_VISIBLE_DEVICES=X --gpu 0` 方式重新启动修复

---
