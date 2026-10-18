# deploy westd 41074 gpu01 tmux fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-41074-gpu01-tmux-fix_20260525T201623_result.json`
- **Structured JSON:** [`4d8153a2c6816dc442a0.json`](../../sessions/4d/4d8153a2c6816dc442a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

| 实验 | GPU | tmux session | Registry 状态 |
|------|-----|-------------|--------------|
| `eval_openvla_random_k05_object_seed42_v2` | cuda:0 (15980 MiB, 83%) | 运行中 | RUNNING |
| `eval_openvla_l2norm_k05_object_seed42_v2` | cuda:1 (15980 MiB, 69%) | 运行中 | RUNNING |

两个实验已通过 tmux 部署到 westd-41074 的 GPU 0/1，日志写入 `~/runs/importance_margin_vla_compress/`，registry 状态已更新为 RUNNING。

---
