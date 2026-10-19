# fix qwen cuda0 check resume

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_qwen_cuda0_check_resume_20260514T175730_result.json`
- **Structured JSON:** [`23908a2fd20b728774dc.json`](../../sessions/23/23908a2fd20b728774dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### cuda:0 — Qwen
- **random_s43**: ✅ 已完成，early stopped at step 1500/2810
  - best val_loss = 0.4476 (step 500), best R@1 = 0.5554 (step 1500)
  - Checkpoints: `best_by_val_loss`, `best_by_recall_at_1`, `final`
- **random_s44**: 🟢 已自动启动 [2/9]，01:58:37 CST 开始，模型加载完毕，正在跑 epoch 1（1408 batches/epoch）
- GPU 利用率 100%，显存 50481/97887 MiB

### cuda:1 — StarCoder
- **random_s43**: 🟢 resume 已启动，01:40:30 CST 开始，当前 step 50（刚起步）
- 1405 batches/epoch
- GPU 利用率 100%，显存 92034/97887 MiB

### tmux sessions
| Session | 状态 |
|---------|------|
| m2_qwen_s43 | 运行 run_m2_full_qwen.sh，当前 [2/9] random_s44 |
| m2_starcoder_s43 | 运行 StarCoder random_s43 |
| qwen_s42_watcher | 监控中 |
| starcoder_s42_watcher | 监控中，检测到 m2_full_starcoder 已完成，m2_starcoder_s43 运行中 |
| m1_reextract_v2 | 数据提取进程 |

### 结论
**两张 GPU 均满载运行，无需干预。** Qwen 脚本会自动按队列跑完 9 个 runs（random/embedding_distance/dataflow_aware × seeds）。StarCoder resume 也已正常启动。

---
