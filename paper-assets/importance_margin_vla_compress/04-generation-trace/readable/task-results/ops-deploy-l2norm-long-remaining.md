# ops deploy l2norm long remaining

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-l2norm-long-remaining_20260524T132528_result.json`
- **Structured JSON:** [`88059716d039f55c0e31.json`](../../sessions/88/88059716d039f55c0e31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，两个实验均已启动并注册为 RUNNING：

| 实验 | 服务器 | GPU | exp_id | 状态 |
|------|--------|-----|--------|------|
| L2norm k=0.3 Long | westd-41074 | GPU 2 | `eval_pi05_l2norm_k03_long_seed42_postfix` | RUNNING |
| L2norm k=0.5 Spatial | cqa1-33015 | GPU 3 | `eval_pi05_l2norm_k05_spatial_seed42_postfix` | RUNNING |

**调整说明：**
- cqa1 GPU 1 在用 (10 GB, 39% util)，改用 GPU 3
- L2norm k=0.7 Spatial 已有 DONE/success 结果 (SR=67%)，替换为 L2norm k=0.5 Spatial（填补 Spatial 曲线 k=0.3~0.7 空白）
- cqa1 命令未加 `TRANSFORMERS_OFFLINE`/`HF_HUB_OFFLINE`，与该服务器历史实验一致

---
