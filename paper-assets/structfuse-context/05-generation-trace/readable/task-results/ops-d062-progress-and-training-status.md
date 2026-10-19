# ops d062 progress and training status

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d062_progress_and_training_status_20260516T093030_result.json`
- **Structured JSON:** [`09c06243a4f7406719d7.json`](../../sessions/09/09c06243a4f7406719d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕，汇总如下：

---

## 状态报告

### 1. D062 Eval (PID 158647, cuda:1)
**运行中**，已跑 1h38m。进度：**2/14 完成，正在跑 [3/14]**

Phase 2 selection set evaluation（504 samples per checkpoint，14 个 checkpoint 待评估）

已完成的结果文件（`/root/autodl-tmp/structfuse/d062_results/`）：

| 文件 | R@1 | R@5 | R@10 |
|------|-----|-----|------|
| `selection_random_s42_best_by_val_loss.json` | 0.230 | 0.625 | 0.802 |
| `selection_random_s42_best_by_recall_at_1.json` | 0.230 | 0.625 | 0.802 |

两个 checkpoint 结果完全相同（R@1=23.0%）。

**注意**：`[1/14] random_s42_best_by_val_loss` 在 300/504 处报 ERROR（eval failed），但仍产出了 JSON（内容和 best_by_recall_at_1 一致——可能是 retry 或 fallback 逻辑写入的）。当前正在评估 `[3/14] random_s43_best_by_val_loss`（running R@1 ~0.34，明显更好）。

预计完成：按每个 checkpoint ~7min 计，剩余 12 个约 84min，**约 1.5 小时后完成**。

### 2. GPU 状态
| GPU | 型号 | 显存使用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell | 66.8 / 97.9 GB | 100% |
| 1 | RTX PRO 6000 Blackwell | 69.9 / 97.9 GB | 100% |

两卡满载。

### 3. Qwen 主链 (PID 337267, cuda:0)
**运行中**，已跑 **1天22小时**。

wrapper 脚本 `run_m2_full_qwen.sh` 下有两部分：
- random_s42 早前单独完成（主 log 记录）
- s43plus_all 子脚本正在跑剩余 9 个 run

**s43plus_all 进度（6/9 已启动，5/9 已完成训练）**：

| Run | 状态 | 开始时间 |
|-----|------|---------|
| random_s43 | ✅ 完成 | May 14 19:24 |
| random_s44 | ✅ 完成 | May 15 01:58 |
| embedding_distance_s43 | ✅ 完成 | May 15 08:32 |
| embedding_distance_s44 | ✅ 完成 | May 15 14:50 |
| dataflow_aware_s43 | ✅ 完成 | May 15 23:53 |
| **dataflow_aware_s44** | **🔄 训练中** (step 900/~1405, epoch 1) | May 16 10:54 |
| s43plus_all | 待启动 | - |
| (还有2个) | 待启动 | - |

当前 `dataflow_aware_s44` loss=0.08，step 900。按进度估算，当前 run 还需 ~4-5 小时，整个 Qwen 链还需 **~1-2 天**。

### 4. StarCoder 链 (PID 519791, cuda:1)
**运行中**，已跑 **1天15小时**。Resume 脚本跑 8 个 run。

**进度（4/8 已启动，3/8 已完成）**：

| Run | 状态 |
|-----|------|
| random_s43 | ✅ 完成 (May 15) |
| random_s44 | ✅ 完成 (May 16) |
| embedding_distance_s42 | ✅ 完成 (May 16 10:06) |
| **embedding_distance_s43** | **🔄 训练中** (step 950/~1405, epoch 1) | 
| embedding_distance_s44 ~ s43plus_all 等 | 待启动 |

当前 `embedding_distance_s43` loss=0.22，step 950。StarCoder 链还需 **~2-3 天**。

### 5. tmux
`tmux list-sessions` 被 read_only 拦截，无法查看。

---

**总结**：D062 eval 预计 ~1.5h 完成（2/14 done）。Qwen 链 6/9+1 done，StarCoder 链 3/8 done，两卡满载正常运转。D062 eval 的 `[1/14]` 有一个 ERROR 需关注——虽然产出了 JSON 但可能是脏数据。

---
