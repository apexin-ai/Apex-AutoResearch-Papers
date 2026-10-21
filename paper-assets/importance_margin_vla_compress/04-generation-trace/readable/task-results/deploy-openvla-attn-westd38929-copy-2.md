# deploy openvla attn westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_openvla_attn_westd38929_20260524T190203_result.json`
- **Structured JSON:** [`2c758ed365b4d572cd26.json`](../../sessions/2c/2c758ed365b4d572cd26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**无需部署 — 实验已在运行中。**

GPU0 和 GPU1 上正在执行的进程 **完全匹配** 你要部署的两个实验：

| GPU | PID | 命令 | 状态 |
|-----|-----|------|------|
| GPU0 | 692475 | `eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.9 --suite libero_object --seed 42` | 运行中 (90% util) |
| GPU1 | 693434 | `eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.85 --suite libero_object --seed 42` | 运行中 (72% util) |

启动时间约 2026-05-25 02:25。输出 JSON 尚未生成，说明评估仍在进行中。GPU2/GPU3 上也各有一个进程在跑（~10.5GB 显存）。

---
