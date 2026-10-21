# deploy openvla attn westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_openvla_attn_westd38929_20260524T184237_result.json`
- **Structured JSON:** [`5597079fb2568cdf7471.json`](../../sessions/55/5597079fb2568cdf7471.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**不需要部署——两个实验已经在跑了。** 已补注册到 registry。

## 汇报

| 实验 | GPU | PID | 运行时间 | 命令 | 当前进度 |
|------|-----|-----|---------|------|---------|
| `eval_openvla_attn_k09_object_seed42_v3` | GPU0 | 692475 | ~18h | `--mode attention_prune --k_ratio 0.9 --suite libero_object` | Task 1/10, Ep 30/50 (日志缓冲，实际进度更远) |
| `eval_openvla_attn_k085_object_seed42` | GPU1 | 693434 | ~17h | `--mode attention_prune --k_ratio 0.85 --suite libero_object` | Task 1/10, Ep 30/50 (日志缓冲，实际进度更远) |

**关键细节：**
- 脚本：`eval_openvla_l2norm_libero.py`，已支持 `attention_prune` mode
- 模型：`/root/autodl-tmp/openvla-libero-object`
- 输出将写入 `eval_results/openvla_attn_prune_k0{9,85}_object_seed42.json`
- 日志文件各仅 25 行（Python stdout 缓冲），但 GPU 内存占用 ~16GB 且 utilization 正常，进程在正常运行
- 按 ~2 eps/min × 500 episodes ≈ 4h 估算，可能已接近或完成。结果文件尚未生成，说明至少还在跑
- GPU2/GPU3 的 π0.5 实验未动

---
