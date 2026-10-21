# deploy westd41074 gpu0 attn k085 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu0_attn_k085_long_20260526T013300_result.json`
- **Structured JSON:** [`0eaabe52971eba5cc207.json`](../../sessions/0e/0eaabe52971eba5cc207.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总：

**GPU0 部署结果**
- **PID**: 300693
- **GPU0 显存**: 16188 MiB（已加载模型）
- **tmux session**: `eval_attn_k085_long_v3`
- **日志**: `/root/autodl-tmp/logs/eval_openvla_attn_k085_long_seed42_v3.log`
- **进度**: 已开始 Task 1/10 (`put both the alphabet soup and the tomato sauce in the basket`)，Attn Pruning 256→217 vision tokens (k=0.85)

**nvidia-smi 全貌**
| GPU | Util | Memory |
|-----|------|--------|
| 0 | 0% | 16188 MiB ← **本实验** |
| 1 | 20% | 15980 MiB |
| 2 | 0% | 15980 MiB |
| 3 | 0% | 15980 MiB |

**注意**: Registry 中该 exp_id 已有 DONE 状态（之前跑过 overall_sr=45.8%），无法转回 RUNNING。spec 已更新为本次部署信息。如需独立追踪本次运行，建议创建 v4 exp_id。

---
