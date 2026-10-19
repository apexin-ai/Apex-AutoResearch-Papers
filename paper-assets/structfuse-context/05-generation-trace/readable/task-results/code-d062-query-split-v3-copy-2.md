# code d062 query split v3

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d062_query_split_v3_20260516T064508_result.json`
- **Structured JSON:** [`fdd7e399df8dac485ddc.json`](../../sessions/fd/fdd7e399df8dac485ddc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D062 Query Split 实现完成。

## 汇总

### 修改的文件
- **evaluate_pool50.py** — 新增 `--selection-set` 和 `--test-set` 两个互斥参数，在加载 val data 后按 JSON 文件中的 indices 过滤 query 列表

### 新建的文件
| 文件 | 说明 |
|------|------|
| `generate_query_split.py` | 按 repo 分层抽样，生成 selection/test split |
| `run_d062_eval.py` | 三阶段批量评估脚本（selection eval → best 选择 → test eval） |
| `selection_queries.json` | 504 queries（用于 checkpoint 选择） |
| `test_queries.json` | 2476 queries（用于最终报告） |

### Split 统计
- **Total**: 2980 queries, 21 repos
- **Selection set**: 504 queries (各 repo 占比 15.0%-17.3%，分布一致)
- **Test set**: 2476 queries
- seed=42，两组无交集

### 验证结果
- `--selection-set` 参数正常工作：2980 total → 504 filtered
- 单 checkpoint (random_s42 best_by_recall_at_1) 测试通过：R@1=0.2669, R@5=0.7867
- 结果 JSON 正确输出

### Checkpoint 可用性
- random: s42, s43, s44 ✓
- dataflow_aware: s43, s44 ✓（无 s42）
- embedding_distance: s43, s44 ✓（无 s42）
- 共 7 个 checkpoint，`run_d062_eval.py` 已配置自动发现

---
