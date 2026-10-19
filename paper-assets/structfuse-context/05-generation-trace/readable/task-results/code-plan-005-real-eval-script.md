# code plan 005 real eval script

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_005_real_eval_script_20260514T204618_result.json`
- **Structured JSON:** [`ef74d9ff1b0acaf5713c.json`](../../sessions/ef/ef74d9ff1b0acaf5713c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Checkpoint 发现逻辑已经存在（搜索 `best/`, `best_by_recall_at_1/`, `best_by_val_loss/` 子目录下的 `model.pt`），无需修改。

完成。修改总结：

1. **mock_predictions seed 修复** (line 278-279): `hash(strategy)` 替换为确定性 `STRATEGY_SEED_OFFSET` 字典
2. **`run_pool_size_controlled_analysis()`** (line 484): 在同一 pool_size bin 内比较策略 R@1，计算 within-bin delta 和 count-weighted aggregate delta，排除候选池大小 confound
3. **`run_dataflow_pool_cross_analysis()`** (line 558): (dataflow_bin × pool_size_bin) 交叉分析，n<30 标记 underpowered
4. **输出完整**:
   - JSON: 新增 `by_pool_size_controlled` 和 `by_dataflow_x_pool_size` 两节
   - CSV: 17 行 pool_size_controlled（含 AGGREGATE weighted delta）+ 27 行 cross-analysis（含 underpowered 标记）
   - PDF: 新增 pool-controlled 对比图 + dataflow×pool_size heatmap per strategy
5. **`--checkpoints-dir` 模式**: 已有 `best/`, `best_by_recall_at_1/`, `best_by_val_loss/` checkpoint 发现逻辑，无需改动

---
