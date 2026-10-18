# deploy w27 seed45 highvar

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_w27_seed45_highvar_20260528T000547_result.json`
- **Structured JSON:** [`f1f50cd277aa5e492e7c.json`](../../sessions/f1/f1f50cd277aa5e492e7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已正常启动，正在加载 π0.5 模型。

**部署完成汇总：**

| 实验 | GPU | PID | tmux session | 状态 |
|------|-----|-----|-------------|------|
| L2norm k=0.75 seed45 | w27:cuda0 | 346959 | `l2norm_k075_s45` | RUNNING ✓ |
| Random k=0.85 seed45 | w27:cuda1 | 347032 | `random_k085_s45` | RUNNING ✓ |

注意：`submit_training_job` 工具当前不可用，已用 tmux session + 显式 `CUDA_VISIBLE_DEVICES` 替代，避免了 nohup 的环境变量丢失问题（C005 的根因）。

---
