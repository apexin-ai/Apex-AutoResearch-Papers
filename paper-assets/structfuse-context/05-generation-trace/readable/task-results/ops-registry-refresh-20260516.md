# ops registry refresh 20260516

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_refresh_20260516_20260516T025403_result.json`
- **Structured JSON:** [`36e7da1e79ddd02ed9e3.json`](../../sessions/36/36e7da1e79ddd02ed9e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。状态摘要：

## 训练链状态 (2026-05-16 10:55 CST)

### Qwen chain (cuda:0) — PID 337267 alive
| Subrun | Final R@1 | Final val_loss | Status |
|---|---|---|---|
| random_s42 | 0.5503 | 0.5456 | done |
| random_s43 | 0.5501 | 0.5434 | done |
| random_s44 | 0.5542 | 0.4943 | done |
| embedding_distance_s43 | **0.5655** | 0.4876 | done |
| embedding_distance_s44 | 0.5470 | 0.5123 | done |
| dataflow_aware_s43 | 0.5564 | 0.5137 | done |
| dataflow_aware_s44 | — | — | **starting** (step 0, loading model) |
| subruns 7-9/9 | — | — | queued |

Best R@1: **embed_s43 = 0.5655**。GPU 0 当前空闲（刚启动 dataflow_s44，正在加载模型）。ETA 当前 subrun ~17:00 CST。

### StarCoder chain (cuda:1) — PID 519791 alive, 100% util
| Subrun | Final R@1 | Final val_loss | Status |
|---|---|---|---|
| random_s42 | 0.4604 | 0.6134 | done |
| random_s43 | 0.4859 | 0.5503 | done |
| random_s44 | 0.4897 | 0.6263 | done |
| embedding_distance_s42 | 0.4376 | 0.6926 | done (early stop 1500) |
| embedding_distance_s43 | — | — | **running** (step 150/1405, epoch 1) |
| embed_s44 → dataflow ×3 | — | — | queued (4 remaining) |

**embed_s42 R@1=0.4376 低于全部 3 个 random baselines** (0.46/0.49/0.49)。ETA 当前 subrun ~18:00 CST。

### SWE-bench — PID 61328 dead
输出目录存在（bm25_100/300/test、random_s42_100 等子目录），但无完整 .jsonl 结果。与 registry 一致（已标 failed）。

---
