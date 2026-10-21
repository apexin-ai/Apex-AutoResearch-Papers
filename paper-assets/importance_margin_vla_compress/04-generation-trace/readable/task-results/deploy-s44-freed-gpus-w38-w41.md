# deploy s44 freed gpus w38 w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_s44_freed_gpus_w38_w41_20260528T004002_result.json`
- **Structured JSON:** [`dbdb0a06a4e6c2a4ef78.json`](../../sessions/db/dbdb0a06a4e6c2a4ef78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

w38:cuda:1 仍在加载 pi0.5 模型（磁盘读取阶段，尚未上显存），正常行为——pi0.5 模型加载需 2-5 分钟。

## 部署结果

| 实验 | 服务器:GPU | PID | 状态 |
|------|-----------|-----|------|
| `eval_pi05_attn_k085_long_seed44_strict_w38_v2` | westd-38929:cuda:1 | 885137 | RUNNING（模型加载中） |
| `eval_pi05_attn_k05_long_seed44_strict_w41` | westd-41074:cuda:3 | 448227 | RUNNING（已开始评估） |

**注意**：w38 的实验用了 `_v2` 后缀，因为原 exp_id `eval_pi05_attn_k085_long_seed44_strict_w38` 的 tmux 会话仍在 cuda:0 上运行（PID 672324，同参数实验）。如果 cuda:0 的旧实验是冗余的，可以 kill 掉释放资源。

---
