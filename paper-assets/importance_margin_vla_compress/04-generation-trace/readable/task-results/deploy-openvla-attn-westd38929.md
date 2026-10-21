# deploy openvla attn westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_openvla_attn_westd38929_20260524T182259_result.json`
- **Structured JSON:** [`a02c2bd2092cd17da072.json`](../../sessions/a0/a02c2bd2092cd17da072.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**状态汇总：**

| GPU | 实验 | PID | k_ratio | Tokens | 状态 |
|-----|------|-----|---------|--------|------|
| 0 | OpenVLA Attn k=0.9 Object seed42 | 692469 | 0.9 | 256→230 | 运行中 (58% util) |
| 1 | OpenVLA Attn k=0.85 Object seed42 | 693429 | 0.85 | 256→217 | 运行中 (84% util) |

**输出文件：**
- `eval_results/openvla_attn_prune_k09_object_seed42.json`
- `eval_results/openvla_attn_prune_k085_object_seed42.json`

已注册每小时 :23 分 cron 监控（job b0ef1bf1）。每个实验约 500 episodes（10 tasks × 50），预计 3-5 小时完成。

---
