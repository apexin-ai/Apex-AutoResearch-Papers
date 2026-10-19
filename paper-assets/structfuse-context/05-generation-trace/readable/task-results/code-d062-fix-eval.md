# code d062 fix eval

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d062_fix_eval_20260516T070422_result.json`
- **Structured JSON:** [`f9a86bfe616006f4babf.json`](../../sessions/f9/f9a86bfe616006f4babf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估正在正常运行：

- **PID**: 155968
- **Phase 2** 开始，正在评估第 1/14 个 checkpoint（random_s42_best_by_val_loss）
- Selection set 正确加载 504 samples
- 模型加载成功

**产出总结**：

1. **创建的脚本**：
   - `/root/structfuse/scripts/generate_query_split.py` — 按 repo 分层 split，line index 方式避免 query_id 重复导致的泄漏
   - `/root/structfuse/scripts/evaluate_pool50.py` — 基于 eval_p2b_pooled.py，支持 `--selection-set` / `--test-set` 行索引过滤
   - `/root/structfuse/scripts/run_d062_eval.py` — 编排脚本，`find_checkpoints()` 同时扫描 `best_by_val_loss` + `best_by_recall_at_1` 两种目录，含 BM25 备用路径

2. **Split**: 2980 → 504 selection + 2476 test（无重叠）

3. **Checkpoint 发现**: 14 个（3 strategies × {s42,s43,s44} 中存在的 seed × 2 ckpt_types）。无 BM25 checkpoint 存在。

4. **正在运行**: PID 155968，日志 `/root/autodl-tmp/structfuse/logs/d062_eval.log`

---
