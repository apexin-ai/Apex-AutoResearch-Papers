# deploy westd38929 gpu1 next

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929-gpu1-next_20260524T034549_result.json`
- **Structured JSON:** [`1f79e7489db3a743e6b5.json`](../../sessions/1f/1f79e7489db3a743e6b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已部署完成。

**实验**: `eval_xvla_l2norm_k07_spatial_seed42_v2`
- **配置**: X-VLA L2norm k=0.7, libero_spatial, seed42, GPU 1
- **服务器**: westd-38929
- **背景**: v1 已有 SR=72% 但结果文件丢失，重跑生成 Table 2 数据。Spatial L2norm 现有 k=0.3/0.5/0.85，补齐 k=0.7 缺口
- **预计耗时**: ~80-90 分钟

当前 westd-38929 GPU 占用：
| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | eval_xvla_random_k085_long_seed42 | RUNNING |
| 1 | eval_xvla_l2norm_k07_spatial_seed42_v2 | RUNNING (刚提交) |
| 2 | eval_xvla_l2norm_k03_goal_seed42_v3 | RUNNING |
| 3 | eval_xvla_l2norm_k07_goal_seed42_v2 | RUNNING |

---
