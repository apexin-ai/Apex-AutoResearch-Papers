# deploy s47 batch w41 w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_s47_batch_w41_w38_20260529T021726_result.json`
- **Structured JSON:** [`bc507a874351a7967e2e.json`](../../sessions/bc/bc507a874351a7967e2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动：

| 实验 | 服务器 | GPU | 状态 |
|------|--------|-----|------|
| `eval_pi05_attention_k050_long_seed47_w41` | westd-41074 | cuda:0 | 正在加载模型 |
| `eval_pi05_attention_k085_long_seed47_w38` | westd-38929 | cuda:0 | 模型已加载，8749 MiB 显存占用 |

westd-41074 加载稍慢但日志正常（Config 和 Loading 信息已输出）。westd-38929 已完成模型加载并启用 gradient checkpointing。

剩余 6 个 s47 bonus 实验（优先级 3-8）需等这两个完成后或找到其他空闲 GPU 再部署。

---
