# infra urgent p2b restart

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent_p2b_restart_20260512T155409_result.json`
- **Structured JSON:** [`fbcd61b521f9f901569f.json`](../../sessions/fb/fbcd61b521f9f901569f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练正在正常运行，不需要重启。**

### 状态汇总

| 项目 | 状态 |
|------|------|
| GPU cuda:4 | PID 238645 占用 8084 MiB，**非空闲** |
| tmux session | `mvp_p2b_contrastive_training` 存在且活跃 |
| 策略名 | 已修正（日志中使用 `embedding_distance`，非旧名 `embedding`） |
| 旧策略名目录 | 不存在，无需清理 |

### 训练进度 (9 runs)

| Run | 状态 |
|-----|------|
| p2b_random_s42 | ✅ 完成 |
| p2b_random_s123 | ✅ 完成 |
| p2b_random_s456 | ✅ 完成 |
| p2b_embedding_distance_s42 | ✅ 完成 (recall@1=0.874) |
| **p2b_embedding_distance_s123** | **🔄 正在训练** (PID 238645, 134% CPU) |
| p2b_embedding_distance_s456 | ⏳ 等待 |
| p2b_dataflow_aware_s42 | ⏳ 等待 |
| p2b_dataflow_aware_s123 | ⏳ 等待 |
| p2b_dataflow_aware_s456 | ⏳ 等待 |

4/9 完成，第 5 个正在跑。之前的"GPU 空闲"判断有误，实际 cuda:4 在训练中。跳过 Step 3-5，无需操作。

---
