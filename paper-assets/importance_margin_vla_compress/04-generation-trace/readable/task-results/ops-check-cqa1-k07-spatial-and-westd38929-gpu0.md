# ops check cqa1 k07 spatial and westd38929 gpu0

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cqa1-k07-spatial-and-westd38929-gpu0_20260524T124811_result.json`
- **Structured JSON:** [`637a119a39887c2ad945.json`](../../sessions/63/637a119a39887c2ad945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### A. cqa1-33015 — L2norm k=0.7 Spatial ✅ 已完成

**SR = 68.2%** (341/500)，耗时 143.9 min

| Task | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|------|----|----|----|----|----|----|----|----|----|----|
| SR% | 86 | 92 | 88 | 44 | 48 | 56 | 82 | 52 | 86 | 48 |

Registry 已更新：`eval_pi05_l2norm_k07_spatial_seed42_postfix` → DONE/success，metrics 已记录。

**GPU 状态**：GPU 0-2 被占用（GPU 0 跑 l2norm k=0.3 spatial），**GPU 3 空闲可用**。

---

### B. westd-38929 GPU 0 — L2norm k=0.95 Long 🏃 运行中

- **实验**: `eval_pi05_l2norm_k095_long_seed42_postfix`
- **参数**: `--prune_mode l2norm --keep_ratio 0.95 --suite libero_10`
- **PID**: 401837
- **进度**: Task 3 进行中 (ep 20/50)，已完成 T0=92%, T1=100%, T2=98%，约 **30% 完成**
- **日志**: `/root/autodl-tmp/importance_margin_vla_compress/logs/l2norm_k095_long_seed42.log`

此实验之前未注册，已创建 registry 条目并设为 RUNNING。

---
