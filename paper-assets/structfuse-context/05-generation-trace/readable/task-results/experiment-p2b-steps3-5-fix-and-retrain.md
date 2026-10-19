# experiment p2b steps3 5 fix and retrain

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_p2b_steps3-5_fix_and_retrain_20260512T194430_result.json`
- **Structured JSON:** [`6cbed56c08e2b88ab124.json`](../../sessions/6c/6cbed56c08e2b88ab124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果清晰了。报告如下：

---

## Step 3 结果：数据验证失败 — 停止

**`train_dataflow.jsonl` 和 `train_embedding.jsonl` 的 md5 完全相同。**

### 根因分析

代码层面的修复（`non_pos` 只排除 `connected_files` 而非 `connected_all`）已正确应用，但**不产生任何效果**，原因是底层数据本身的限制：

| repo | pos | dataflow图中文件数 | 非gold的dataflow文件数 |
|------|-----|--------------------|----------------------|
| flask | 14 | 7 | **0** |
| requests | 8 | 6 | **0** |
| pytest | 40 | 14 | **0** |
| pylint | 35 | 6 | **0** |
| xarray | **0** (无训练数据) | 90 | 89 |
| astropy | 19 | 0 | **0** |
| sphinx | 130 | 61 | **0** |
| matplotlib | 163 | 120 | **0** |

对于所有**产出训练数据的 repo**，`bounded_dataflow.csv` 中的 dataflow 连接**完全是 gold `connected_files` 的子集**。没有任何额外的 dataflow 连接可供 `build_candidate_pools` 区分两种策略。

### 因果链

1. `connected_all = connected_files ∪ df_connections[buggy_file]`
2. 但 `df_connections[buggy_file] ⊆ connected_files`（所有 productive repos）
3. 所以 `connected_all == connected_files`
4. `build_candidate_pools` 的 `disconnected` 过滤器 `[f for f in non_pos if f not in connected_set]` 不会移除任何文件
5. `embedding` 和 `dataflow` 池完全相同（都是 BM25 top-50 from identical set）

### 修复方向

仅修改 `build_p2b_data.py` 的过滤逻辑**无法解决**此问题。需要以下之一：

**方案 A**：扩展 dataflow 连接定义——用 2-hop 传递闭包或 repo 级全图连通分量，让 dataflow 连接超出 gold 范围

**方案 B**：改变 dataflow 策略的含义——不再"排除 dataflow 连接的文件"，而是按 dataflow 距离重新加权 BM25 排序（距离远的文件优先作为 negative）

**方案 C**：重新运行 CodeQL dataflow 分析，放宽 bound 限制以发现更多跨文件连接

---

**按指令要求，已停止后续步骤（训练和评估）。** 请指示如何处理。

---
