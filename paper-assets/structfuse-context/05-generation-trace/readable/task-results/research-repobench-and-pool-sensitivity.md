# research repobench and pool sensitivity

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_repobench_and_pool_sensitivity_20260516T050845_result.json`
- **Structured JSON:** [`9b9c24b8ca176123ffd6.json`](../../sessions/9b/9b9c24b8ca176123ffd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

## RepoBench-R
- **数据位置**: HF `tianyang/repobench-r`，本地无
- **Java subset**: **Yes** — `java_cff.gz` (270 MB) + `java_cfr.gz` (190 MB)
- **Python subset**: `python_cff.gz` (140 MB) + `python_cfr.gz` (97 MB)
- **总大小**: ~697 MB compressed
- **下载时间估计**: AutoDL proxy 下约 10-30 min（取决于 network_turbo 速度）
- **eval 脚本**: 无现成 repobench eval 脚本（服务器上未找到）
- **注意**: `datasets` 库不再支持 loading script（repobench-r.py），需用 `hf_hub_download` 直接下 gz 文件手动解析

## Pool Size Sensitivity
- 评估池机制：`evaluate_with_pool()` 从全局 **2980 个 query** 中跨 repo 随机采样 pool_size-1 个负样本 + 1 个正样本
- **pool=500 完全可行**（2980 >> 500，无需修改代码）
- **evaluate_pool50.py 扩展难度**: 零改动，直接 `--pool-size 100/200/500` 即可
- 训练数据 repo 文件分布（10K 样本采样）: P25=3, P50=11, P75=24 — 但这是每条记录的候选数，不影响评估池

## Pool=50 Eval 进度
- **PID 138134**: 已结束
- **已完成**: 12/12 checkpoints ✓
- **结果文件**: `/root/autodl-tmp/structfuse/results/pool50_eval_qwen_all.json`
- **最佳 checkpoint**:

| Checkpoint | R@1 | R@5 |
|---|---|---|
| embedding_distance_s43/best_by_recall_at_1 | **0.3897±0.0048** | **0.9259±0.0009** |
| random_s43/best_by_recall_at_1 | 0.3829±0.0062 | 0.9121±0.0019 |
| embedding_distance_s44/best_by_val_loss | 0.3694±0.0057 | 0.9031±0.0015 |
| dataflow_aware_s43/best_by_recall_at_1 | 0.3660±0.0054 | 0.8931±0.0027 |

---
