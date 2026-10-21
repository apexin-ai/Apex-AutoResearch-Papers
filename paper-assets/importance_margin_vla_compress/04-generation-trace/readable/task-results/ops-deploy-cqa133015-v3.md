# ops deploy cqa133015 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-cqa133015-v3_20260524T095540_result.json`
- **Structured JSON:** [`7f88fe230c484d0ce942.json`](../../sessions/7f/7f88fe230c484d0ce942.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### cqa1-33015 GPU 部署状态

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 0 | Random k=0.5 Goal (PID 86738) | 86738 | 在跑（~1.5hr 剩余） |
| 1 | **L2norm k=0.95 Goal** | 148749 | 刚启动，模型加载中 |
| 2 | **L2norm k=0.9 Spatial** | 149194 | 刚启动，模型加载中 |
| 3 | **L2norm k=0.7 Spatial** | 149752 | 刚启动，模型加载中 |

### 已完成记录
- **L2norm k=0.5 Spatial**: overall_sr = **57.4%**, 已注册 DONE (registry: `eval_pi05_l2norm_k05_spatial_seed42_postfix`)

4 张卡满载。3 个新实验预计各需 ~2.5hr 完成。

---
