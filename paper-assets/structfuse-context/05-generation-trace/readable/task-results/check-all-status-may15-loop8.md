# check all status may15 loop8

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-status-may15-loop8_20260515T010827_result.json`
- **Structured JSON:** [`2e146ec3911f6f6cd999.json`](../../sessions/2e/2e146ec3911f6f6cd999.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态汇总

| 进程 | 状态 | 当前任务 | 进度 | 变化 |
|------|------|---------|------|------|
| **M2 Qwen** (cuda:0, PID 337267) | ✅ 运行中 (13h44m) | `embedding_distance_s43` | step 150/1405 (epoch 1) | ⚠️ **random_s44 已完成**，进入新 subrun |
| **M2 StarCoder** (cuda:1, PID 519791) | ✅ 运行中 (7h05m) | `random_s43` | step 1300/1405 (epoch 1/2) | 1050→1300 (+250) |
| **m1_reextract_v2** (CPU) | ✅ 运行中 | CodeQL 提取 | **44173 行** | 22842→44173 (+93%，已超目标 28276) |
| **BM25 Qwen watcher** | ✅ 待命 | 监控 PID 337267 | — | 未触发 |
| **BM25 StarCoder watcher** | ✅ 待命 | 监控 PID 519791 | — | 未触发 |

### GPU & 磁盘

| 资源 | 状态 |
|------|------|
| GPU 0 | 100% util, 49.5/97.9 GiB (50.6%) |
| GPU 1 | 100% util, 54.3/97.9 GiB (55.5%) |
| 磁盘 /root/autodl-tmp | 173G/250G (70%) |

### 关键变化

1. **Qwen random_s44 已完成** — early stopping 在 step 1500 触发：
   - Best val_loss=**0.4252** (step 500)
   - Best R@1=**0.6009**, R@5=0.9583, R@10=1.0
   - 链已自动推进到 `embedding_distance_s43`，刚开始 ~36 分钟

2. **StarCoder random_s43** 接近 epoch 1 结束 (1300/1405)：
   - Best val_loss=0.5279 (step 500), Best R@1=0.4780 (step 1000)
   - 预计 ~1h 内完成 epoch 1

3. **m1_reextract** 仍在运行且产出远超预期 (44173 vs 目标 28276)，tmux 显示 09:09 仍在处理 CodeQL call graph

---
